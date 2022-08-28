import './App.css';
import { BrowserRouter as Router, Routes, Route, useParams, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios";

/* component imports */
import Header from "./component/Header";
import Login from "./component/Login"

function App() {
  document.title = `Archive`
  return (
    <>
        <Router>
          <Header />
            <Routes>
              <Route path="/login"  element={<Login/>}></Route>
            </Routes>
       </Router>

    </>
  );
}

export default App;
