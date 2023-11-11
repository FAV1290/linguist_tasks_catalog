import flask


from webapp.views import (
    user_profile, user_sign_in, process_login, process_logout,
    add_task, process_task_add, delete_task, process_task_delete, edit_task, process_task_edit,
)


def configure_routes(blueprint: flask.Blueprint) -> None:
    add_rule = blueprint.add_url_rule
    add_rule('/', view_func=user_profile, methods=['GET'])
    add_rule('/sign_in', view_func=user_sign_in, methods=['GET'])
    add_rule('/process_login', view_func=process_login, methods=['POST'])
    add_rule('/process_logout', view_func=process_logout, methods=['GET'])
    add_rule('/tasks/add', view_func=add_task, methods=['GET'])
    add_rule('/tasks/process_add', view_func=process_task_add, methods=['POST'])
    add_rule('/tasks/<task_id>/delete', view_func=delete_task, methods=['GET'])
    add_rule('/tasks/<task_id>/process_delete', view_func=process_task_delete, methods=['GET'])
    add_rule('/tasks/<task_id>/edit', view_func=edit_task, methods=['GET'])
    add_rule('/tasks/<task_id>/process_edit', view_func=process_task_edit, methods=['POST'])
