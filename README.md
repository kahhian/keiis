# keiis
A helpful friend for piano practice.

## Feature list: https://www.notion.so/bc6bfb8ff4f34ae4b0e050b117570f42?v=503bffb3330d4ce59d3b53945e48a833
## Gantt Chart/Development Timeline: https://www.notion.so/outvision/10a8b4d4d1fc48f89fd2ab8f07a5fb55?v=596318bbdc24493ebb037eac4d52ac4f&pvs=4

### General:
In terminal run to install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
In terminal run to install ffmpeg, musescore, git:
```
brew install ffmpeg musescore git
```
In terminal run to install music21 and torch:
```
pip install music21

pip install torch
```
```
pip install -r requirements.txt

pip install piano_transcription_inference
```

Installing Audiveris Dependencies:\
 \
Please install Java Development Kit (JDK) Version 11 from Oracle.

Please install Tesseract OCR Version 3.04 from here: https://github.com/tesseract-ocr/tesseract/releases/tag/3.04.00

Then in terminal run these commands one at a time:
```
git clone https://github.com/Audiveris/audiveris.git

cd audiveris

./gradlew build
```

Installing MIDI playback dependencies:\
 \
In terminal run:
```
pip install midi2audio

brew install fluidsynth

mkdir -p ~/.fluidsynth

ln -s soundfonts/salamander_grand_piano.sf2 ~/.fluidsynth/default_sound_font.sf2
```
### Practice Mode:
In terminal run:
```
cd <directory of the keiis file>
```
Then run:
```
python3 main.py -p <file>
```
Then enter the path of your practice sheet music (pdf/png/jpg) or original song (common audio/video formats) or MIDI file.\
If you provided sheet music, a Musescore window will open soon. Edit the sheet music till it looks/sounds like your original song.\
Once finished editing, on Musescore go to File > Export, and then change format to MIDI file. DO NOT CHANGE THE FILE NAME.Click export, and then close the Musescore window. You will be prompted to save the Musescore (.mscz) file. Save the file.DO NOT CHANGE THE FILE NAME.\
Follow the instructions prompt thereafter.\

### Audio To Midi:
In terminal run:
```
cd <directory of the keiis file>
```
Then run to obtain midi file:
```
python3 audio2midi.py -a2m <Mp3 file>
```
### Sheet Music To Midi:
In terminal run:
```
cd <directory of the keiis file>
```
Then run to obtain midi file:
```
python3 sheet2midi.py -s2m <JPEG/JPG/PDF/PNG file>
```
### Midi To Piano Roll:
In terminal, run:
```
cd <directory of the keiis file>
```
Then run to obtain piano roll:
```
python3 main.py -m2pr <Midi file>
```
### Midi Playback:

In terminal run:
```
cd <directory of the keiis file>
```
Then run to obtain mp3 file:
```
python3 main.py -pm <Mp3 file>
```
### Midi Comparison:
In terminal, run:
```
cd <directory of the keiis file>
```
Then run to compare midi files:
```
python3 main.py -mc
```
This opens a website that compares midi files.

Press the "Add Midi" button and add the midi files that you want to compare.




### Youtube Import:
In terminal run:
```
python3 -m pip install -U yt-dlp
```
Then run to obtain mp3 file:
```
yt-dlp -x --audio-format mp3 <video URL>
```
We will integrate this feature into keiis in the future

### Known possible errors:
Error 1:\
![plot](./FileNotFoundError.jpeg)\
Run:
```
brew install wget
```
Error 2:\
![plot](./audioread.exception.NoBackendError.png) \
Run:
```
brew install ffmpeg
```

