import React from 'react';
import 'html-midi-player';
import styles from './MidiPlayer.module.css'
import { useEffect, useRef } from 'react';

function MidiPlayer({ midiUrl, startTime=0 }) {
  const playerRef = useRef(null);

  console.log(startTime);
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
      const player = document.querySelector("midi-player");
      const shadow = player.shadowRoot;
      const slider = shadow.querySelector("input[type=range]");

      if (slider) {
        slider.style.accentColor = "#2300B2"; // modern browsers
        slider.style.height = "8px";
        slider.style.borderRadius = "4px";
      }
  }, []);
  return (
      <midi-player ref={playerRef} src={midiUrl} sound-font></midi-player>
  );
}
export default MidiPlayer;