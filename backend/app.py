from library import create_app
from library.task.controller import create, read, update, delete,login,logout,register,todo
from flask import Flask,render_template,send_file,url_for


app = create_app()    

app.register_blueprint(create)
app.register_blueprint(read)
app.register_blueprint(update)
app.register_blueprint(delete)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(todo)

if __name__ == "__main__":
    app.run(debug=True)

