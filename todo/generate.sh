protoc --go_out=./todo --go_opt=paths=source_relative \
    --go-grpc_out=./todo --go-grpc_opt=paths=source_relative \
    ./todo.proto