import flask


from webapp.routes import configure_routes


test_blueprint = flask.Blueprint(
    name='test',
    import_name=__name__,
    template_folder='templates',
    static_folder='static',
)
configure_routes(test_blueprint)
