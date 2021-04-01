import grpc
from auth import auth_pb2 as pb2
from auth import auth_pb2_grpc as pb2_grpc


class AuthClient:
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 9000

        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = pb2_grpc.AuthServiceStub(self.channel)

    def register(self, username, password):
        register_request = pb2.RegisterRequest(username=username,
                                               password=password)
        return self.stub.Register(register_request)

    def login(self, username, password):
        login_request = pb2.LoginRequest(username=username, password=password)
        return self.stub.Login(login_request)

    def validate_token(self, token):
        validate_token_request = pb2.ValidateTokenRequest(token=token)
        return self.stub.ValidateToken(validate_token_request)