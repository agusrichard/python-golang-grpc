import { useState } from 'react'

import './App.css'
import authClient from './api/auth'

function App() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = () => {
    authClient.register(username, password)
  }

  return (
    <div className="App">
      <h1>Hello World</h1>
      <div>
        <input type="text" placeholder="username" onChange={e => setUsername(e.target.value)} />
        <input type="password" placeholder="password" onChange={e => setPassword(e.target.value)} />
        <button onClick={handleSubmit}>Register</button>
      </div>
    </div>
  )
}

export default App
