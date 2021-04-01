package main

import (
	"fmt"
	"log"
	"net"
	"todo/config"
	"todo/repository"
	"todo/todo"
	"todo/usecase"

	"google.golang.org/grpc"
)

func main() {
	db := config.ConnectDB()
	TodoRepository := repository.InitTodoRepository(db)
	todoUsecase := usecase.InitUserUsecase(TodoRepository)

	s := todo.InitServer(todoUsecase)

	grpcServer := grpc.NewServer()

	todo.RegisterTodoServiceServer(grpcServer, &s)

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", 3000))
	if err != nil {
		log.Println("failed to listen: ", err)
	}
	fmt.Println("Listen to port 3000")

	if err := grpcServer.Serve(lis); err != nil {
		log.Println("failed to serve: ", err)
	}
}
