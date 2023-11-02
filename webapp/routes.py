import flask


from webapp.views import user_profile, user_sign_in, process_login, process_logout


def configure_routes(blueprint: flask.Blueprint) -> None:
    blueprint.add_url_rule('/', view_func=user_profile, methods=['GET', 'POST'])
    blueprint.add_url_rule('/sign_in', view_func=user_sign_in, methods=['GET'])
    blueprint.add_url_rule('/process_login', view_func=process_login, methods=['POST'])
    blueprint.add_url_rule('/process_logout', view_func=process_logout, methods=['GET'])
