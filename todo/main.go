package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"strconv"
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

	serverPort, _ := strconv.Atoi(os.Getenv("TODO_SERVICE_PORT"))
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", serverPort))
	if err != nil {
		log.Println("failed to listen: ", err)
	}
	fmt.Println(fmt.Sprintf("Listen to port %v", serverPort))

	if err := grpcServer.Serve(lis); err != nil {
		log.Println("failed to serve: ", err)
	}
}
