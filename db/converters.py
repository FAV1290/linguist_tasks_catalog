import uuid
import datetime


from db.models import Task


def create_task_object(
    profile_id: uuid.UUID,
    form_response: dict[str, str],
) -> Task:
    new_task = Task(
        id=uuid.uuid4(),
        owner_id=profile_id,
        name=form_response['name'],
        status=form_response['status'],
        created_at=datetime.datetime.now(),
        deadline_at=form_response['deadline_at'],
        runtime=form_response['runtime'],
        events=form_response['events'],
        client_id=form_response['client_id'],
        type_id=form_response['type_id'],
        linguist_id=form_response['linguist_id'],
    )
    return new_task
