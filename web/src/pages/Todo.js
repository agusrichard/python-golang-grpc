import { useState } from 'react'

import TodosList from '../components/TodosList'
import CreateTodo from '../components/CreateTodo'

const TodoComponent = ({ userId }) => {
  const [isEdit, setIsEdit] = useState(false)
  const [todoId, setTodoId] = useState('')


  return (
    <>
      <h1>Todo App</h1>
      <CreateTodo
        userId={userId}
        isEdit={isEdit}
        todoId={setTodoId}
        setTodoId={setTodoId}
        setIsEdit={setIsEdit}
      />
      <TodosList
        userId={userId}
        isEdit={isEdit}
        todoId={todoId}
        setIsEdit={setIsEdit}
        setTodoId={setTodoId}
      />
    </>
  )
}

export default TodoComponent