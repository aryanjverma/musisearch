import React from "react";
import styles from "./Nav.module.css";

function Nav(){
    return (
        <nav>
            <ul>
                <li className={styles.logo}><a>musisearch</a></li>
                <li><a href="">About</a></li>
                <li><a href="">Home</a></li>
            </ul>
        </nav>
    )
}

export default Nav;