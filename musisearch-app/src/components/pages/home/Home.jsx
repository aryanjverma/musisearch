import React from "react";
import styles from "./Home.module.css"; 
import Nav from "../../layouts/Nav/Nav.jsx";
import Intro from "./Intro/Intro.jsx";
import Input from "./Input/Input.jsx";
function Home() {
    return (
        <>
            <Nav />
            <Intro />
            <Input />
        </>
    )
}

export default Home;