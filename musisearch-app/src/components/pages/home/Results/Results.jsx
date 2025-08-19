import React from 'react';
import styles from './Results.module.css';
import { FileContext } from '../FileContext';
import { useState } from 'react';
import axios from 'axios'
import Card from './Card/Card.jsx';

function Results(){
    const [results, setResults] = useState([]);
    return(
        <div className={styles.container}>
            <h1>Results...</h1>
            {FileContext === null ? (<p>Submit a melody above.</p>) :
            (<ul>
                {results.length > 0 ? results.map((result,index)=>(<Card key={index} result={result} />)) :
                (<p>No results found.</p>)}
            </ul>)
            }
        </div>
    );
}

export default Results;