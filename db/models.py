import uuid
import typing
import decimal
import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash


from db import Base


class User(Base, UserMixin):
    __tablename__ = 'users'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    email: Mapped[str] = mapped_column(
        sqlalchemy.String(64),
        index=True,
        unique=True,
        nullable=False,
    )
    password: Mapped[str] = mapped_column(sqlalchemy.TEXT, nullable=False)

    @classmethod
    def find_user_by_email(cls, email: str | None) -> typing.Self | None:
        if not email:
            return None
        target_user = cls.query.filter(cls.email == email).first()
        return target_user

    def check_password(self, password: str | None) -> bool:
        if not password:
            return False
        return check_password_hash(self.password, password)


class UserProfile(Base):
    __tablename__ = 'profiles'
    user_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    user_name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)


class Client(Base):
    __tablename__ = 'clients'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    payment_delay_months: Mapped[int] = mapped_column(sqlalchemy.SmallInteger)

    @classmethod
    def fetch_user_clients(cls, profile_id: uuid.UUID) -> list[typing.Self]:
        clients_list = cls.query.filter(cls.owner_id == profile_id).order_by(cls.name).all()
        return clients_list


class Linguist(Base):
    __tablename__ = 'linguists'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)

    @classmethod
    def fetch_user_linguists(cls, profile_id: uuid.UUID) -> list[typing.Self]:
        linguists = cls.query.filter(cls.owner_id == profile_id).order_by(cls.name).all()
        return linguists


class TaskType(Base):
    __tablename__ = 'task_types'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)
    pricing_type: Mapped[str] = mapped_column(sqlalchemy.String(64), nullable=False)
    runtime_rate_usd: Mapped[decimal.Decimal] = mapped_column(sqlalchemy.DECIMAL())
    events_rate_usd: Mapped[decimal.Decimal] = mapped_column(sqlalchemy.DECIMAL())
    custom_rate_usd: Mapped[decimal.Decimal] = mapped_column(sqlalchemy.DECIMAL())

    @classmethod
    def fetch_user_tasktypes(cls, profile_id: uuid.UUID) -> list[typing.Self]:
        tasktypes = cls.query.filter(cls.owner_id == profile_id).order_by(cls.name).all()
        return tasktypes


class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, primary_key=True)
    owner_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    name: Mapped[str] = mapped_column(sqlalchemy.String(128), nullable=False)
    status: Mapped[str] = mapped_column(sqlalchemy.String(64), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime, nullable=False)
    deadline_at: Mapped[datetime.datetime] = mapped_column(sqlalchemy.DateTime)
    runtime: Mapped[decimal.Decimal] = mapped_column(sqlalchemy.DECIMAL())
    events: Mapped[int] = mapped_column(sqlalchemy.Integer)
    client_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID)
    type_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID, nullable=False)
    linguist_id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID)

    @classmethod
    def fetch_user_tasks(cls, profile_id: uuid.UUID) -> list[typing.Self]:
        tasks_list = cls.query.filter(cls.owner_id == profile_id).order_by(cls.created_at).all()
        return tasks_list


if __name__ == '__main__':
    Base.metadata.create_all(bind=Base.engine)
