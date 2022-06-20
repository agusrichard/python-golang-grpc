# gRPC Web

Compile:

```shell
protoc -I=src/proto auth.proto \
    --js_out=import_style=commonjs:./src/api \
    --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./src/api
```

```shell
protoc -I=src/proto todo.proto \
    --js_out=import_style=commonjs:./src/api \
    --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./src/api
```
