package config

import (
	"fmt"
	"os"
	"strconv"

	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

var DB *sqlx.DB

// ConnectDB to get all needed db connections for application
func ConnectDB() *sqlx.DB {
	DB = getDBConnection()

	return DB
}

func getDBConnection() *sqlx.DB {
	var dbConnectionStr string
	port, _ := strconv.Atoi(os.Getenv("POSTGRES_PORT"))

	dbConnectionStr = fmt.Sprintf(
		"host=%s port=%d dbname=%s user=%s password=%s sslmode=disable",
		os.Getenv("POSTGRES_HOST"),
		port,
		os.Getenv("POSTGRES_DB"),
		os.Getenv("POSTGRES_USER"),
		os.Getenv("POSTGRES_PASSWORD"),
	)

	db, err := sqlx.Open("postgres", dbConnectionStr)
	if err != nil {
		panic(err)
	}

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	//TODO: experiment with correct values
	db.SetMaxIdleConns(1)
	db.SetMaxOpenConns(5)

	fmt.Println("Connected to DB")
	return db
}
