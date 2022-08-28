import React, { useState, useEffect} from "react";
import { Link } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from "axios";

function Login() {
   const[username, setUsername] = useState()
   const[password, setPassword] = useState()

   async function login(){
      try {
        const user = await axios.post('http://127.0.0.1:8000/users_management_app/login/', {'username':username, 'password': password})
        localStorage.setItem('token', JSON.stringify(user.data.token))
        localStorage.setItem('username', JSON.stringify(user.data.user.username))

        let temp = user.data.user.groups
        let group_names = temp.map((e)=> e.name )
        localStorage.setItem('groups', JSON.stringify(group_names))

      }catch (error) {
        console.log(error)
      }

   }


  return (
  <>
  <Container style={{ width: "40vw",}}>
   <h1 className="mb-5"  style = {{ textAlign: "center",}} >Login To Archive</h1>
   <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail" className="form">
        <Form.Control className="mb-3" type="username" placeholder="username" onChange={(e)=>{ setUsername(e.target.value)} }/>
        <Form.Control className="mb-3" type="password"  placeholder="password" onChange={(e)=>{ setPassword(e.target.value)} }/>
          <Link as={Link} to={{pathname: `/login`}}>
             <div className="d-grid gap-2">
               <Button variant="dark" onClick={login}>
                 login
               </Button>
             </div>
          </Link>
      </Form.Group>
   </Form>
   </Container>
  </>
    );
}

export default Login;