import React from 'react';
import styles from "./Input.module.css";
import { useState } from 'react';
import { FileContext, FileDispatchContext } from "../FileContext.jsx";

function Input(){
    const [inputMode, setInputMode] = useState("MIDI");
    return(
        <div className={styles.container}>
            <h1>Enter a melody...</h1>
            <select id="mode" name="mode" onClick={(e) => setInputMode(e.target.value)}>
                <option value="MIDI">Upload Midi File</option>
                <option value="Notes">Type Notes</option>
                <option value="Audio">Record Audio</option>
            </select>
            {inputMode === "MIDI" &&
                <form onSubmit={(e) => {
                    e.preventDefault()
                    const fileInput = document.getElementById("midi");
                    const file = fileInput.files[0];
                    if (file) {
                        const reader = new FileReader();
                        reader.onload = (event) => {
                            const midiData = event.target.result;
                            // Dispatch the file to the context
                            dispatchFile({ type: 'SET', payload: midiData });
                        };
                        reader.readAsArrayBuffer(file);
                    }
                    else{
                        alert("Please select a MIDI file.");
                    }
                    }}>
                    <label htmlFor="midi">Upload a MIDI file with a sequence of notes (only one instrument):</label><br></br>
                    <input type="file" accept=".mid, .midi" id="midi" name="midi"/><br></br>
                    <button type="submit">Find Matching Songs</button>
                </form>
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