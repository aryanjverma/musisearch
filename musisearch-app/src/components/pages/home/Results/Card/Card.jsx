import React from 'react';
import styles from './Card.module.css';

function Card({keyz, result}){
    return (
        <div className={styles.container} key={keyz}>
            <h1>{result.title}</h1>
        </div>
    );
}

export default Card;