import React from "react";
import styles from "./Intro.module.css";

function Intro(){
    return (
        <div className={styles.container}>
            <h1>
                <span>musi</span>
                <span className={styles.black}>search</span>
            </h1>
            <h2>Search for songs by melody.</h2>
        </div>
    )
}

export default Intro;