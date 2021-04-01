package main

import (
	"fmt"
	"log"
	"net"

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

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", 9000))
	if err != nil {
		log.Printf("failed to listen: %v\n", err)
	}
	fmt.Println("Listen to port 9000")

	if err := grpcServer.Serve(lis); err != nil {
		log.Printf("failed to serve: %s\n", err)
	}
}
