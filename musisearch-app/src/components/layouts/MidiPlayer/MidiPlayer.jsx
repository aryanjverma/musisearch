import React from 'react';
import 'html-midi-player';
import styles from './MidiPlayer.module.css'
import { useEffect, useRef, useState } from 'react';
import play from '../../../assets/play.svg';
import pause from '../../../assets/pause.svg';

function MidiPlayer({ midiUrl, startTime=0 }) {
  const playerRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const image = isPlaying ? pause : play
  useEffect(() => {
    const player = playerRef.current;
    if (!player) return;
    if (isPlaying) {
      player.start();
    } else {
      player.stop();
    }
  }, [isPlaying]);
  
  useEffect(() => {
    const player = playerRef.current;
    if (!player) return;

    const handleLoad = () => {
      player.currentTime = startTime;
    };

    player.addEventListener("load", handleLoad);

    return () => {
      player.removeEventListener("load", handleLoad);
    };
  }, [startTime, midiUrl]);

  useEffect(() => {
    const player = playerRef.current;
    if (!player) return;
    const updateSliderStyle = () => {
      const shadow = player.shadowRoot;
      if (!shadow) return;
      const slider = shadow.querySelector("input[type=range]");
      if (slider) {
        slider.style.accentColor = "#2300B2";
        slider.style.height = "100%";
        slider.style.borderRadius = "4px";
        slider.style.backgroundColor = "transparent";
      }
    };

    updateSliderStyle();
    player.addEventListener("load", updateSliderStyle);

    return () => {
      player.removeEventListener("load", updateSliderStyle);
    };
  }, []);
  return (
      <div className={styles.container}>
        <img src={image} onClick={()=>{
          setIsPlaying(!isPlaying);
        }} title ={isPlaying ? "Pause" : "Play"}/>
        <midi-player ref={playerRef} src={midiUrl} sound-font></midi-player>
      </div>
  );
}
export default MidiPlayer;