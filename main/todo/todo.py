import json
from flask import (
    Blueprint,
    g,
    jsonify,
    request,
    render_template,
    session,
    redirect,
    url_for,
)

from todo.client import TodoClient
from middleware.middleware import token_required

todo_blueprint = Blueprint("todo_blueprint", __name__)


@todo_blueprint.route("/create", methods=["GET", "POST"])
@token_required
def create_todo():
    if request.method == "POST":
        try:
            title = request.form["title"]
            description = request.form["description"]
            user_data = session["user_data"]
            if title == "" or description == "":
                raise ValueError("Please fill the title and description")
            client = TodoClient()
            client.create_todo(
                title=request.form["title"],
                description=description,
                user_id=user_data.get("ID"),
            )
            return redirect(url_for("todo_blueprint.get_todos"))
        except Exception as error:
            return render_template("todo/create.html", error=str(error))
    return render_template("todo/create.html")


@todo_blueprint.route("/get", methods=["GET"])
@token_required
def get_todos():
    try:
        user_data = session["user_data"]
        client = TodoClient()
        result = client.get_todos(user_id=user_data.get("ID"))
        data = json.loads(result.data)
        return render_template("todo/list.html", todos=data)
    except Exception as error:
        return render_template("todo/list.html", error=str(error))


@todo_blueprint.route("/get/<int:todo_id>", methods=["GET"])
@token_required
def get_todo(todo_id):
    try:
        user_data = session["user_data"]
        client = TodoClient()
        result = client.get_todo(item_id=todo_id, user_id=user_data.get("ID"))
        data = json.loads(result.data)
        return render_template("todo/item.html", todo=data)
    except Exception as error:
        return render_template("todo/item.html", error=str(error))


@todo_blueprint.route("/update/<int:todo_id>", methods=["POST"])
@token_required
def update_todo(todo_id):
    try:
        user_data = session["user_data"]
        client = TodoClient()
        client.update_todo(todo_id, request.form["title"], request.form["description"])
        result_get = client.get_todo(todo_id, user_data.get("ID"))
        json.loads(result_get.data)
        return redirect(url_for("todo_blueprint.get_todos"))
    except Exception as error:
        return render_template("todo/item.html", error=str(error))


@todo_blueprint.route("/delete/<int:todo_id>", methods=["GET"])
@token_required
def delete_todo(todo_id):
    try:
        client = TodoClient()
        client.delete_todo(todo_id)
        return redirect(url_for("todo_blueprint.get_todos"))
    except Exception as error:
        return render_template("todo/item.html", error=str(error))
