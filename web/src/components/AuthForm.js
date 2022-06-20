import { TextField } from "@mui/material"

const AuthForm = ({ setUsername, setPassword }) => {
  return (
    <div>
      <div className="input-container">
        <TextField id="username" label="Username" variant="outlined" onChange={e => setUsername(e.target.value)} />
      </div>
      <div className="input-container">
        <TextField id="password" label="Password" variant="outlined" type="password" onChange={e => setPassword(e.target.value)} />
      </div>
    </div>
  )
}

export default AuthForm