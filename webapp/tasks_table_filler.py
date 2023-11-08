import uuid
import decimal


from db import Base
from webapp.enums import TaskStatus, TaskPricingType
from db.models import Task, Client, Linguist, TaskType
from webapp.usd_rur_rates_parser import calculate_usd_to_rur_rate


def find_client_in_list_by_id(clients: list[Client], id: uuid.UUID) -> Client | None:
    target_client = [client for client in clients if client.id == id]
    return target_client[0] if target_client else None


def find_linguist_in_list_by_id(linguists: list[Linguist], id: uuid.UUID) -> Linguist | None:
    target_linguist = [linguist for linguist in linguists if linguist.id == id]
    return target_linguist[0] if target_linguist else None


def find_tasktype_in_list_by_id(tasktypes: list[TaskType], id: uuid.UUID) -> TaskType | None:
    target_tasktype = [tasktype for tasktype in tasktypes if tasktype.id == id]
    return target_tasktype[0] if target_tasktype else None


def find_object_in_list_by_id(
    objects_list: list[Client | Linguist | TaskType],
    id: uuid.UUID,
) -> Base | None:
    target_object = [object for object in objects_list if object.id == id]
    return target_object[0] if target_object else None


def calculate_task_price(task: Task, tasktype: TaskType) -> decimal.Decimal:
    pricing_type = TaskPricingType(tasktype.pricing_type)
    if pricing_type.value == 'C':
        return tasktype.custom_rate_usd
    elif pricing_type.value == 'E':
        return tasktype.events_rate_usd * task.events
    elif pricing_type.value == 'R':
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
) -> dict[str, str]:
    client = find_client_in_list_by_id(clients, task.client_id)
    linguist = find_linguist_in_list_by_id(linguists, task.linguist_id)
    tasktype = find_tasktype_in_list_by_id(tasktypes, task.type_id)
    if tasktype:
        price = calculate_task_price(task, tasktype)
    else:
        price = decimal.Decimal(0.0)
    usd_to_rur_rate = calculate_usd_to_rur_rate()
    task_row = {
        'Title': task.name,
        'Status': TaskStatus(task.status).value.capitalize(),
        'Deadline': task.deadline_at.strftime('%d.%m.%y %H:%M'),
        'Runtime': str(task.runtime),
        'Events': str(task.events),
        'E/R': str(decimal.Decimal(task.events / task.runtime).quantize(decimal.Decimal("1.00"))),
        'Client': client.name if client else '-',
        'Task type': tasktype.name if tasktype else '-',
        'Price (USD)': f'${price.quantize(decimal.Decimal("1.00"))}',
        'Price (RUR)': f'{(price * usd_to_rur_rate).quantize(decimal.Decimal("1.00"))}₽',
        'Linguist': linguist.name if linguist else '-',
        }
    return task_row


def aggregate_profile_table_data(
    profile_id: uuid.UUID,
) -> list[dict[str, str]]:
    profile_tasks = Task.fetch_user_tasks(profile_id)
    profile_clients = Client.fetch_user_clients(profile_id)
    profile_linguists = Linguist.fetch_user_linguists(profile_id)
    profile_tasktypes = TaskType.fetch_user_tasktypes(profile_id)
    tasks_table_contents = []
    for task in profile_tasks:
        task_row = create_tasks_table_row(
            task, profile_clients, profile_linguists, profile_tasktypes)
        tasks_table_contents.append(task_row)
    return tasks_table_contents
