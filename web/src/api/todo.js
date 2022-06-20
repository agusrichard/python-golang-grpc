import { TodoServiceClient } from './todo_grpc_web_pb'
import { CreateTodoRequest, GetTodoRequest, GetTodosRequest, UpdateTodoRequest, DeleteTodoRequest } from './todo_pb'

const client = new TodoServiceClient('http://localhost:2000')

const getTodos = (userId, handleGetTodos) => {
  const request = new GetTodosRequest()
  request.setUserid(userId)
  client.getTodos(request, null, (err, response) => {
    if (err) {
      console.log(err)
    } else {
      console.log(response)
      const result = response.getData()
      handleGetTodos(JSON.parse(result))
    }
  })
}

const getTodo = (userId, todoId) => {
  const request = new GetTodoRequest()
  request.setUserid(userId)
  request.setItemid(todoId)
  client.getTodo(request, null, (err, response) => {
    if (err) {
      console.log(err)
    } else {
      console.log(response)
    }
  })
}

const createTodo = (userId, title, description) => {
  const request = new CreateTodoRequest()
  request.setUserid(userId)
  request.setTitle(title)
  request.setDescription(description)
  client.createTodo(request, null, (err, response) => {
    if (err) {
      console.log("create todo err", err)
    } else {
      console.log("create todo response", response)
    }
  })
}

const updateTodo = (todoId, title, description) => {
  const request = new UpdateTodoRequest()
  request.setId(todoId)
  request.setTitle(title)
  request.setDescription(description)
  client.updateTodo(request, null, (err, response) => {
    if (err) {
      console.log(err)
    } else {
      console.log(response)
    }
  })
}

const deleteTodo = (todoId) => {
  const request = new DeleteTodoRequest()
  request.setId(todoId)
  client.deleteTodo(request, null, (err, response) => {
    if (err) {
      console.log(err)
    } else {
      console.log(response)
    }
  })
}


export {
  getTodos,
  getTodo,
  createTodo,
  updateTodo,
  deleteTodo,
}