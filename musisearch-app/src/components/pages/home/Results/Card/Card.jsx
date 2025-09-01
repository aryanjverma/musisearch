import React from 'react';
import styles from './Card.module.css';
import MidiPlayer from '../../../../layouts/MidiPlayer/MidiPlayer.jsx'

import { useState } from 'react';

function Card({id, result}){
    let color = "";
    const [selectedId, setSelectedId] = useState(null);
    const [isRight, setIsRight] = useState(null);

    console.log(result.accuracy);
    if(result.accuracy >= 85){
        color = styles.darkGreen;
    } else if(result.accuracy >=75){
        color = styles.lightGreen;
    } else if(result.accuracy >=50){
        color = styles.yellow;
    } else if(result.accuracy >=33){
        color = styles.orange;
    } else{
        color = styles.red;
    }
    return (
        <div className={styles.container} key={id} id={id}>
            <p className={color}>{result.accuracy}%</p>
            <h1>{result.title}</h1>
            <h2>{result.creator}</h2>
            <div className={styles.feedback} id="feedback">
                <label>{result.accuracy}% match found at {result.timestamp} seconds. Was this accurate?</label>
                {isRight === null ? (
                    <>
                        <button onClick={()=>{setIsRight(true)}}>Yes</button>
                        <button onClick={()=>{setIsRight(true)}}>No</button>
                    </>
                )  :
                (
                    <button>Resubmit</button>
                )
                }
            </div>
            <MidiPlayer midiUrl={result.midiUrl} startTime={result.timestamp}></MidiPlayer> 
        </div>
    );
}

export default Card;