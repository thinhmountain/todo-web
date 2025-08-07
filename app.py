from library import create_app
from library.task.controller import create, read, update, delete
from flask_cors import CORS

if __name__ == "__main__":
    app = create_app()
    CORS(app)  # Thêm dòng này để bật CORS
    app.register_blueprint(create)
    app.register_blueprint(read)
    app.register_blueprint(update)
    app.register_blueprint(delete)

    app.run(debug=True)

