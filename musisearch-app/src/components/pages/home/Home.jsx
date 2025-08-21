import React from "react";
import styles from "./Home.module.css"; 
import Nav from "../../layouts/Nav/Nav.jsx";
import Intro from "./Intro/Intro.jsx";
import Input from "./Input/Input.jsx";
import Results from "./Results/Results.jsx";
import MidiPlayer from '../../layouts/MidiPlayer/MidiPlayer.jsx'

import { FileContext, FileDispatchContext } from "./FileContext.jsx";
import { useReducer } from "react";

function Home() {
    const [file, dispatchFile] = useReducer((state, action) => {
        switch (action.type){
            case 'SET':
                return action.payload;
            case 'RESET':
                return null;
            default:
                return state;
        }
    },null)
    return (
        <>
            <Nav />
            <Intro />
            <FileContext value ={file}>
                <FileDispatchContext value={dispatchFile}>
                    <Input />
                    <Results />
                </FileDispatchContext>
            </FileContext>
            <MidiPlayer midiUrl="/Happy-Birthday-To-You-1.mid" startTime={6}/>
        </>
    )
}
export default Home;