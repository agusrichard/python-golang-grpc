import { AuthServiceClient } from './auth_grpc_web_pb'
import { RegisterRequest, LoginRequest } from './auth_pb'

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

const login = (username, password) => {
    const request = new LoginRequest()
    request.setUsername(username)
    request.setPassword(password)
    client.login(request, null, (err, response) => {
        if (err) {
            console.log(err)
        } else {
            console.log(response)
        }
    })
}

const validateToken = (token) => {

}

export default {
    login,
    register,
    validateToken
}