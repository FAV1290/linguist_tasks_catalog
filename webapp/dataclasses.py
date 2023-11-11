import uuid
import decimal
import datetime
import dataclasses


from webapp.enums import TaskStatus


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
            f'{float(self.price_rur):_}₽'.replace('_', ' ').replace('.', ','),
            self.linguist,
        )
        return str_tuple
