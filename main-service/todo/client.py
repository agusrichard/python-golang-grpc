import grpc
from . import todo_pb2 as pb2, todo_pb2_grpc as pb2_grpc


class TodoClient:
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 3000

        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def create_todo(self, title, description, user_id):
        request = pb2.CreateTodoRequest(title=title,
                                        description=description,
                                        userID=user_id)
        return self.stub.CreateTodo(request)

    def get_todos(self, user_id):
        request = pb2.GetTodosRequest(userID=user_id)
        return self.stub.GetTodos(request)

    def update_todo(self, id, title, description):
        request = pb2.UpdateTodoRequest(id=id,
                                        title=title,
                                        description=description)
        return self.stub.UpdateTodo(request)

    def delete_todo(self, id):
        request = pb2.DeleteTodoRequest(id=id)
        return self.stub.DeleteTodo(request)
