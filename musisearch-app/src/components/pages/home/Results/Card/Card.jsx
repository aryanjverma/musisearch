import React from 'react';
import styles from './Card.module.css';
import MidiPlayer from '../../../../layouts/MidiPlayer/MidiPlayer.jsx'

function Card({cardKey, result}){
    let color = "";
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
        <div className={styles.container} key={cardKey}>
            <p className={color}>{result.accuracy}%</p>
            <h1>{result.title}</h1>
            <h2>{result.creator}</h2>
            <h3>{result.accuracy}% match found at {result.timestamp} seconds. Was this accurate?</h3>
            <MidiPlayer midiUrl={result.midiUrl} startTime={result.timestamp}></MidiPlayer> 
        </div>
    );
}

export default Card;