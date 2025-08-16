import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/home/Home.jsx';
import About from './components/pages/about/About.jsx';
import "./App.css";

function App() {
        return (
          <Router>
            <Routes>
              <Route path="/"element={<Home/>}/>
              <Route path="/about" element={<About/>}/>
            </Routes>
          </Router>
        );
}

export default App;
