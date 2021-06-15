This project is a simple ToDo Website that helps users to not forget their tasks on a specific day.     

You can add a task, edit and delete it. The project also keeps track of the time that the user has added the task. 

Before being able to do the basic CRUD operations with the tasks, you have to log in. 
When the user has already written his/her tasks, he can log out and the tasks are saved. 

Technologies used on this project are:
    
    Python 
    HTML
    CSS
    Flask
    SQLAlchemy


The project is run byn by: 

    - Opening app.py file and running it.
      
    -Accessing it in the browser through the localhost server

On the app.py file you can also see the models used in the project like *USER* and *TODO*.

The database operations are done through the SQLALchemy also in the *app.py* file. 

Some examples of SQLAlchemy usage in the project:
   
    tasks = Todo.query.order_by(Todo.date_created).all()
    task_to_delete = Todo.query.get_or_404(id) 
    task = Todo.query.get_or_404(id)

DEPENDECIES used on this project are written in the *requirements.txt* file.
In the templates folder you can find the HTML of the project while in the static directory is written the CSS.

Some basic UNIT TESTING is also done on the *unittest* directory.

This project also has some endpoints to access data.

*Remember that you cannot access the endpoints before logging in!*

    '/' - to access the homepage of the project
    '/login' - to login as a user
    '/logout' - to logout
    '/delete/<int:id>' - to delete a specific user
    '/update/<int:id>'

*The UI/UX of the *logout* and *login* can still be developed better.
*Register page might be needed.
