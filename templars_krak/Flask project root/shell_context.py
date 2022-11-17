

from app.config import Config
from app import app, db
from app.users.models import User
from app.models import Post


"""This shell context will be 'magically' found by flask when calling
the cli:
$ flask shell
 """

@app.shell_context_processor
def make_shell_context():
    context = {
        "db": db,
        "User": User,
        "Post": Post,
    }
    return context