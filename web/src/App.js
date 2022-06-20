import './App.css'
import { useState } from 'react'

import TodoComponent from './pages/Todo'
import AuthComponent from './pages/Auth'
import { Button } from '@mui/material'

function App() {
  const [userId, setUserId] = useState('')
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  const handleLogin = (id) => {
    setIsLoggedIn(true)
    setUserId(id)
  }

  const handleLogout = () => {
    setIsLoggedIn(false)
    setUserId('')
  }

  console.log('userId', userId)

  return (
    <div className="App">
      <div className="container">
        {
          isLoggedIn ? <TodoComponent userId={userId} /> : <AuthComponent handleLogin={handleLogin} />
        }
        {isLoggedIn && <div className='button-logout'>
          <Button variant='contained' onClick={handleLogout}>Logout</Button>
        </div>}
      </div>
    </div>
  )
}

export default App
