import { useState, useEffect } from 'react'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import Typography from '@mui/material/Typography'
import CardActions from '@mui/material/CardActions'
import Button from '@mui/material/Button'

import { getTodos } from '../api/todo'

const TodosList = ({ userId, todoId, setIsEdit, setTodoId }) => {
  const [todos, setTodos] = useState([])

  console.log('todos', todos)

  useEffect(() => {
    getTodos(userId, data => setTodos(data))
  }, [userId, todoId])

  return (
    <div className="todos-list">
      <h2>Todos List</h2>
      <div>
        {
          todos.length === 0 ?
            <div>No Todos</div>
            :
            <div>
              {todos.map(todo => (
                <Card key={todo.id} variant="outlined">
                  <CardContent>
                    <Typography variant="h5" component="div">{todo.title}</Typography>
                    <Typography variant="body2" component="div">{todo.description}</Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small" color="success" variant="contained" OnClick={() => {
                      setIsEdit(true)
                      setTodoId(todo.id)
                    }}>Edit</Button>
                    <Button size="small" color="error" variant="contained">Delete</Button>
                  </CardActions>
                </Card>
              ))}
            </div>
        }
      </div>
    </div>
  )
}

export default TodosList