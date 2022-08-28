import React from "react";
import { Link } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';

import Navbar from 'react-bootstrap/Navbar';
import { useState } from 'react';
import Offcanvas from 'react-bootstrap/Offcanvas';

let username = JSON.parse(localStorage.getItem('username'));
function Header({ name, ...props }) {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  return (
     <>
     <div style={{ backgroundColor: "#000000", padding: "0.5rem", marginBottom: "2rem"}}>
        <button variant="dark" onClick={handleShow} className='sidebar-btn'>☰</button>
      </div>
      <Offcanvas show={show} onHide={handleClose} {...props} style={{ backgroundColor: "#000000", color: "#fff"}}>
        <Offcanvas.Header>
          <Offcanvas.Title>Archive</Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
              <Nav.Link as={Link} to="/login" style={{ color: "#fff",}}>Login</Nav.Link>
              <Nav.Link as={Link} to="/logout" style={{ color: "#fff",}}>Logout</Nav.Link>
        </Offcanvas.Body>
      </Offcanvas>
    </>

  );
}

export default Header;