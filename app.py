from flask import Flask
from config import app, db
from main.atividade_controller import atividade_bp

db.init_app(app)
app.register_blueprint(atividade_bp)


if __name__ == '__main__':
    with app.app_context():
        if app.config['DEBUG']:
            db.create_all()


    app.run(
        host=app.config['HOST'],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
