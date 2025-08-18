import React from 'react';
import styles from "./Input.module.css";
import { useState } from 'react';

function Input(){
    const [inputMode, setInputMode] = useState("");
    return(
        <div className={styles.container}>
            <h1>Enter a melody...</h1>
            <select id="mode" name="mode" onClick={(e) => setInputMode(e.target.value)}>
                <option value="" disabled selected>Select Input Method</option>
                <option value="MIDI">Upload Midi File</option>
                <option value="Notes">Type Notes</option>
                <option value="Audio">Record Audio</option>
            </select>
            {inputMode === "MIDI" &&
                <input type="file" accept=".mid, .midi" className={styles.fileInput}/>
            }
            {inputMode === "Notes" &&
                <p>Feature coming soon</p>
            }
            {inputMode === "Audio" &&
                <p>Feature coming soon</p>
            }
        </div>
    );
}

export default Input;