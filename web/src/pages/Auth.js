import { useState } from 'react'
import { Button } from '@mui/material'

import AuthForm from '../components/AuthForm'
import { register, login } from '../api/auth'

const AuthComponent = ({ handleLogin }) => {
  const [isRegister, setIsRegister] = useState(true)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const changeAuth = () => {
    setIsRegister(!isRegister)
  }

  const handleSubmit = () => {
    setUsername('')
    setPassword('')
    if (isRegister) {
      register(username, password)
      setIsRegister(prev => !prev)
    } else {
      login(username, password, handleLogin)
    }
  }

  return (
    <div>
      <h1>{isRegister ? 'Register' : 'Login'}</h1>
      <AuthForm
        setUsername={setUsername}
        setPassword={setPassword}
      />
      <Button variant='contained' onClick={handleSubmit}>{isRegister ? 'Register' : 'Login'}</Button>
      <div className='bottom-auth-form'>
        <Button variant='contained' color='info' onClick={changeAuth}>{!isRegister ? 'Register' : 'Login'}</Button>
      </div>
    </div >
  )
}

export default AuthComponent