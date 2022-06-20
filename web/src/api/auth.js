import { AuthServiceClient } from './auth_grpc_web_pb'
import { RegisterRequest, LoginRequest, ValidateTokenRequest } from './auth_pb'

const client = new AuthServiceClient('http://localhost:1000')

const register = (username, password) => {
  const request = new RegisterRequest()
  request.setUsername(username)
  request.setPassword(password)
  client.register(request, null, (err, response) => {
    if (err) {
      console.log(err)
    } else {
      console.log(response)
    }
  })
}

const login = (username, password, handleLogin) => {
  let token = ''

  const loginRequest = new LoginRequest()
  loginRequest.setUsername(username)
  loginRequest.setPassword(password)
  client.login(loginRequest, null, async (err, loginResponse) => {
    if (err) {
      console.log(err)
    } else {
      console.log(loginResponse)
      token = loginResponse.getToken()
      const validateTokenRequest = new ValidateTokenRequest()
      validateTokenRequest.setToken(token)
      client.validateToken(validateTokenRequest, null, (err, validateTokenResponse) => {
        if (err) {
          console.log(err)
        } else {
          console.log(validateTokenResponse)
          const message = validateTokenResponse.getMessage()
          const result = JSON.parse(message)
          handleLogin(result['ID'])
        }
      })
    }
  })
}

export {
  login,
  register,
}