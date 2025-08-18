import React from "react";
import styles from "./Nav.module.css";
import { Link } from "react-router-dom";

function Nav(){
    return (
        <nav>
            <ul>
                <li className={styles.logo}><a>
                    <span className={styles.purple}>musi</span>    
                    <span className={styles.black}>search</span>
                </a></li>
                <li><Link to="/about" title="About">About</Link></li>
                <li><Link to="/" title="Home">Home</Link></li>
            </ul>
        </nav>
    )
}

export default Nav;