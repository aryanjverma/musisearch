# 🎵musisearch

musisearch is an engine that takes notes or MIDI files and searches for songs with similar melodies. It features a React-based frontend and a Python backend powered by FastAPI. 
**NOTE:** This project is still on-going and I'm still working on some features, like advanced melody recognition features and an accesible database of MIDI files.

## ⚙️Features
### Planned Features:
- Upload a MIDI file or enter notes to search for matching songs.
- See results with accuracy scores and listen to matches using an interactive MIDI player.
- Modern UI built with React and Vite.
- Extensible backend for melody analysis and comparison.
- A large database of MIDI files to search through.
### Implemented:
- Input tab to upload MIDI files.
- Results tab to view matches with accuracy scores, as well as an MIDI player to listen to the matches.
- Most of UI built.
- Python modules to convert MIDI files to arrays of pitches and rhythms.
### Yet to implement:
- Other means of input, including musical notes and humming.
- Database of MIDI files with a diverse song catalog.
- An algorithm to determine the similiarity of two melodies.
- A searching algorithm to find melodies within the songs.
- An API to connect the frontend and backend.
## 📂Project Structure
```
musisearch/
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── modules/        # Melody analysis modules
│   │   └── main.py         # FastAPI app entrypoint
│   └── requirements.txt    # Python dependencies
├── musisearch-app/         # React frontend
│   ├── public/             # Static assets (MIDI files, icons)
│   ├── src/                # React source code
│   ├── package.json        # Frontend dependencies
│   └── vite.config.js      # Vite config
├── *.mid                   # Example MIDI files
├── README.md               # Project documentation
```

## 🖼️Current Demonstration
<img width="1127" height="889" alt="musisearch-picture-demo" src="https://github.com/user-attachments/assets/a9fc06ca-e8a6-4fd8-a733-50fd7e6f2e73"></img>
### Usage:
- On the homepage, upload a MIDI file or select other input modes (notes/audio).
- Submit your melody to see matching songs and their accuracy.
- Click play to listen to the matching segment.

## ➡️How to Download

### 🔌Backend (not working right now)

1. Install Python dependencies:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
2. Run the FastAPI server:
   ```sh
   uvicorn app.main:app --reload
   ```

### 🎨Frontend

1. Install Node.js dependencies:
   ```sh
   cd musisearch-app
   npm install
   ```
2. Start the development server:
   ```sh
   npm run dev
   ```
3. Open [http://localhost:5173](http://localhost:5173) in your browser.

## 💻Technologies

- **Frontend:** React, Vite, html-midi-player
- **Backend:** FastAPI, pretty_midi, numpy

## License

MIT License

---
