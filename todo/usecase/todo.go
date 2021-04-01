package usecase

import (
	"encoding/json"
	"log"
	"todo/models"
	"todo/repository"
)

type todoUsecase struct {
	todoRepository repository.TodoRepository
}

type TodoUsecase interface {
	CreateTodo(todo models.Todo) (bool, error)
	GetTodos(userID int64) (string, error)
	GetTodo(userID, itemID int64) (string, error)
	UpdateTodo(todo models.Todo) (bool, error)
	DeleteTodo(id int64) (bool, error)
}

func InitUserUsecase(todoRepository repository.TodoRepository) TodoUsecase {
	return &todoUsecase{
		todoRepository,
	}
}

func (todoUsecase *todoUsecase) CreateTodo(todo models.Todo) (bool, error) {
	_, err := todoUsecase.todoRepository.CreateTodo(todo)
	if err != nil {
		log.Println("Error create todo", err)
		return false, err
	}

	return true, nil
}

func (todoUsecase *todoUsecase) GetTodos(userID int64) (string, error) {
	todos, err := todoUsecase.todoRepository.GetTodos(userID)
	if err != nil {
		log.Println("Error get todos", err)
		return "", err
	}

	result, err := json.Marshal(todos)

	return string(result), nil
}

func (todoUsecase *todoUsecase) GetTodo(itemID, userID int64) (string, error) {
	todo, err := todoUsecase.todoRepository.GetTodo(itemID, userID)
	if err != nil {
		log.Println("Error get todos", err)
		return "", err
	}

	result, err := json.Marshal(todo)

	return string(result), nil
}

func (todoUsecase *todoUsecase) UpdateTodo(todo models.Todo) (bool, error) {
	_, err := todoUsecase.todoRepository.UpdateTodo(todo)
	if err != nil {
		log.Println("Error update todo", err)
		return false, err
	}

	return true, nil
}

func (todoUsecase *todoUsecase) DeleteTodo(id int64) (bool, error) {
	_, err := todoUsecase.todoRepository.DeleteTodo(id)
	if err != nil {
		log.Println("Error delete todo", err)
		return false, err
	}

	return true, nil
}
