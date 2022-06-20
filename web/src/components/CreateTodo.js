import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'
import { useState } from 'react'

import { createTodo, updateTodo } from '../api/todo'

const CreateTodo = ({ userId, isEdit, setIsEdit, todoId, setTodoId }) => {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = () => {
    setIsEdit(false)
    setTitle('')
    setDescription('')
    if (isEdit) {
      updateTodo(todoId, title, description)
    } else {
      setTodoId('created')
      createTodo(userId, title, description)
    }
  }

  return (
    <div className="create-todo">
      <form>
        <div className="input-container">
          <TextField id="title" label="Title" variant="outlined" onChange={e => setTitle(e.target.value)} />
        </div>
        <div className="input-container">
          <TextField
            id="description"
            label="Description"
            placeholder="Description"
            multiline
            onChange={e => setDescription(e.target.value)}
          />
        </div>
        <Button variant="contained" onClick={handleSubmit}>{isEdit ? 'Edit' : 'Add'}</Button>
      </form>
    </div>
  )
}

export default CreateTodo