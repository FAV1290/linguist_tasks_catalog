from webapp import build_app


if __name__ == '__main__':
    app = build_app()
    app.run(debug=True)
