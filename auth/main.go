package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"strconv"

	"auth/auth"
	"auth/config"
	"auth/repository"
	"auth/usecase"

	"google.golang.org/grpc"
)

func main() {
	db := config.ConnectDB()
	userRepository := repository.InitUserRepository(db)
	userUsecase := usecase.InitUserUsecase(userRepository)

	s := auth.InitServer(userUsecase)

	grpcServer := grpc.NewServer()

	auth.RegisterAuthServiceServer(grpcServer, &s)
	serverPort, _ := strconv.Atoi(os.Getenv("AUTH_SERVICE_PORT"))

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", serverPort))
	if err != nil {
		log.Printf("failed to listen: %v\n", err)
	}
	fmt.Println(fmt.Sprintf("Listen to port %v", serverPort))

	if err := grpcServer.Serve(lis); err != nil {
		log.Printf("failed to serve: %s\n", err)
	}
}
