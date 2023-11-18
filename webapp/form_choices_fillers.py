import uuid
import typing


from webapp.enums import TaskStatus


def create_status_choices() -> list[tuple[str, str]]:
    choices = []
    for status in TaskStatus:
        value = status.value
        label = status.value.capitalize()
        choices.append((value, label))
    return choices


def create_name_to_id_choices(
    fetcher_function: typing.Callable,
    profile_id: uuid.UUID,
) -> list[tuple[uuid.UUID, str]]:
    choices = []
    objects = fetcher_function(profile_id)
    for object in objects:
        value = object.id
        label = object.name
        choices.append((value, label))
    return choices
