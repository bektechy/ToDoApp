from flask import Flask, render_template, url_for, request, redirect, Response
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Flask login
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Flask login config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)

        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

    def __str__(self):
        return f'{self.name}'

    def get_id(self):
        return self.id


# create some users with ids 1 to 20
users = [User(id) for id in range(1, 21)]


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_secret":
            id = username.split("user")[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p style="text-align: center">Username: </p>
            <p style="text-align: center"><input type=text name=username placeholder=Enter username>
            <p style="text-align: center">Password: </p>
            <p style="text-align: center"><input type=password name=password placeholder=Enter Password>
            <p style="text-align: center"><input type=submit value=Login>
        </form>
        ''')


@login_manager.user_loader
def user_loader(user_id):
    return User(user_id)


# logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('logout.html')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<h1>Login failed</h1>')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    # everytime we make a new element returns Task and ID of the task
    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/', methods=['POST', 'GET'])
@login_required
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue !!"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There is an issue with the task"


@app.route('/update/<int:id>', methods=['POST', 'GET'])
@login_required
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            "An error while updating"
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run()
