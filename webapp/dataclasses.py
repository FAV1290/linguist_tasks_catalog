import uuid
import decimal
import datetime
import dataclasses


from webapp.enums import TaskStatus, TaskPricingType


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class TasksTableRow:
    id: uuid.UUID
    title: str
    status: TaskStatus
    deadline_at: datetime.datetime
    runtime: decimal.Decimal
    events: int
    events_to_runtime: decimal.Decimal
    client: str
    tasktype: str
    price_usd: decimal.Decimal
    price_rur: decimal.Decimal
    linguist: str

    @staticmethod
    def column_names() -> list[str]:
        columns = [
            'Title', 'Status', 'Deadline',
            'Runtime', 'Events', 'E/R',
            'Client', 'Task Type',
            'Price (USD)', 'Price (RUR)', 'Linguist',
        ]
        return columns

    @property
    def convert_to_str_tuple(self) -> tuple[str, ...]:
        str_tuple = (
            self.title,
            self.status.value.capitalize(),
            self.deadline_at.strftime('%d.%m.%y %H:%M'),
            str(self.runtime),
            str(self.events),
            str(self.events_to_runtime),
            self.client,
            self.tasktype,
            f'${float(self.price_usd):_}'.replace('_', ' '),
            f'{float(self.price_rur):_} ₽'.replace('_', ' ').replace('.', ','),
            self.linguist,
        )
        return str_tuple


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class ClientsTableRow:
    id: uuid.UUID
    name: str
    payment_delay_months: int

    @staticmethod
    def column_names() -> list[str]:
        columns = ['Client', 'Payment delay']
        return columns

    @property
    def convert_to_str_tuple(self) -> tuple[str, ...]:
        str_tuple = (self.name, f'{self.payment_delay_months} month(s)')
        return str_tuple


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class LinguistsTableRow:
    id: uuid.UUID
    name: str
    email: str = '-'

    @staticmethod
    def column_names() -> list[str]:
        columns = ['Linguist', 'E-mail']
        return columns

    @property
    def convert_to_str_tuple(self) -> tuple[str, ...]:
        str_tuple = (self.name, self.email)
        return str_tuple
    

@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class TaskTypesTableRow:
    id: uuid.UUID
    name: str
    pricing_type: TaskPricingType
    runtime_rate_usd: decimal.Decimal
    events_rate_usd: decimal.Decimal
    custom_rate_usd: decimal.Decimal

    @staticmethod
    def column_names() -> list[str]:
        columns = ['Task Type', 'Pricing model', 'Runtime rate', 'Events rate', 'Custom rate']
        return columns

    @property
    def convert_to_str_tuple(self) -> tuple[str, ...]:
        str_tuple = (
            self.name,
            self.pricing_type.show_label,
            f'${float(self.runtime_rate_usd):_}'.replace('_', ' '),
            f'${float(self.events_rate_usd):_}'.replace('_', ' '),
            f'${float(self.custom_rate_usd):_}'.replace('_', ' '),
        )
        return str_tuple
    