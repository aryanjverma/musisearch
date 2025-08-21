import React from 'react';
import styles from './Results.module.css';
import { useContext } from 'react';
import { FileContext } from '../FileContext.jsx';
import { useState } from 'react';
import axios from 'axios'
import Card from './Card/Card.jsx';

function Results(){
    const file = useContext(FileContext);
    console.log(file);
    const [results, setResults] = useState([]);
    return(
        <div className={styles.container}>
            <h1>Results...</h1>
            {file === null ? (<p>Submit a melody above.</p>) :
            (results.length > 0 ? results.map((result,index)=>(<Card key={index} result={result} />)) :
                (<p>No results found.</p>))
            }
        </div>
    );
}

export default Results;