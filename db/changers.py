import uuid
import typing


from db import Base
from db.models import Client, Linguist, TaskType, Task


def add_object(object: Client | Linguist | TaskType | Task) -> None:
    Base.db_session.add(object)
    Base.db_session.commit()


def delete_object(object: Client | Linguist | TaskType | Task) -> None:
    Base.db_session.delete(object)
    Base.db_session.commit()


def update_task(profile_id: uuid.UUID, task_id: uuid.UUID, form_response: typing.Mapping) -> None:
    is_owner_valid, target_task = Task.validate_owner(task_id, profile_id)
    if is_owner_valid and target_task:
        target_task.name = form_response['name']
        target_task.status = form_response['status']
        target_task.deadline_at = form_response['deadline_at']
        target_task.runtime = form_response['runtime']
        target_task.events = form_response['events']
        target_task.client_id = form_response['client_id']
        target_task.type_id = form_response['type_id']
        target_task.linguist_id = form_response['linguist_id']
    Base.db_session.commit()
