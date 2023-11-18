import uuid
import typing
from decimal import Decimal


from webapp.dataclasses import TasksTableRow
from webapp.enums import TaskStatus, TaskPricingType
from db.models import Task, Client, Linguist, TaskType
from webapp.usd_rur_rates_parser import calculate_usd_to_rur_rate


def find_object_in_list_by_id(
    objects_list: typing.Sequence[Client | Linguist | TaskType],
    id: uuid.UUID,
) -> Client | Linguist | TaskType | None:
    target_object = [object for object in objects_list if object.id == id]
    return target_object[0] if target_object else None


def calculate_task_price_usd(task: Task, tasktype: TaskType) -> Decimal:
    pricing_type = TaskPricingType(tasktype.pricing_type)
    if pricing_type == TaskPricingType.custom_only:
        return tasktype.custom_rate_usd
    elif pricing_type == TaskPricingType.events_only:
        return tasktype.events_rate_usd * task.events
    elif pricing_type == TaskPricingType.runtime_only:
        return tasktype.runtime_rate_usd * task.runtime
    else:
        events_price = tasktype.events_rate_usd * task.events
        runtime_price = tasktype.runtime_rate_usd * task.runtime
        return events_price + runtime_price


def create_tasks_table_row(
    task: Task,
    clients: list[Client],
    linguists: list[Linguist],
    tasktypes: list[TaskType],
    usd_to_rur_rate: Decimal,
) -> TasksTableRow:
    client = find_object_in_list_by_id(clients, task.client_id)
    linguist = find_object_in_list_by_id(linguists, task.linguist_id)
    tasktype = find_object_in_list_by_id(tasktypes, task.type_id)
    if tasktype and isinstance(tasktype, TaskType):
        price = calculate_task_price_usd(task, tasktype)
    else:
        price = Decimal(0.0)
    task_row = TasksTableRow(
        id=task.id,
        title=task.name,
        status=TaskStatus(task.status),
        deadline_at=task.deadline_at,
        runtime=task.runtime,
        events=task.events,
        events_to_runtime=Decimal(task.events / task.runtime).quantize(Decimal('1.00')),
        client=client.name if client else '-',
        tasktype=tasktype.name if tasktype else '-',
        price_usd=price.quantize(Decimal('1.00')),
        price_rur=(price * usd_to_rur_rate).quantize(Decimal('1.00')),
        linguist=linguist.name if linguist else '-'
    )
    return task_row


def aggregate_profile_table_data(
    profile_id: uuid.UUID,
) -> list[TasksTableRow]:
    profile_tasks = Task.fetch_user_tasks(profile_id)
    profile_clients = Client.fetch_user_clients(profile_id)
    profile_linguists = Linguist.fetch_user_linguists(profile_id)
    profile_tasktypes = TaskType.fetch_user_tasktypes(profile_id)
    usd_to_rur_rate = calculate_usd_to_rur_rate()
    tasks_table = []
    for task in profile_tasks:
        task_row = create_tasks_table_row(
            task, profile_clients, profile_linguists, profile_tasktypes, usd_to_rur_rate)
        tasks_table.append(task_row)
    return tasks_table
