# keiis
A helpful friend for piano practice.

## Feature list: https://www.notion.so/bc6bfb8ff4f34ae4b0e050b117570f42?v=503bffb3330d4ce59d3b53945e48a833
## Gantt Chart/Development Timeline: https://www.notion.so/outvision/10a8b4d4d1fc48f89fd2ab8f07a5fb55?v=596318bbdc24493ebb037eac4d52ac4f&pvs=4

### General:
In terminal run to install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
In terminal run to install ffmpeg, musescore, and git:
```
brew install ffmpeg musescore git
```
In terminal run to install music21:
```
pip install music21
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
*Note: Dependencies from the other features have to be installed for practice mode to work

### Audio To Midi:
Install dependencies:
```
pip install -r requirements.txt

pip install piano_transcription_inference
```
In terminal run:
```
cd <directory of the keiis file>
```
Then run to obtain midi file:
```
python3 audio2midi.py -a2m <Mp3 file>
```
### Sheet Music To Midi:
Install dependencies:

Java Development Kit (JDK) Version 11

Tesseract OCR Version 3.04 https://github.com/tesseract-ocr/tesseract/releases/tag/3.04.00

Then in terminal run these commands one at a time:
```
git clone https://github.com/Audiveris/audiveris.git

cd audiveris

./gradlew build
```
Then run after reopening terminal:
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
In terminal run these commands one at a time:
```
pip install midi2audio

brew install fluidsynth

mkdir -p ~/.fluidsynth

ln -s soundfonts/salamander_grand_piano.sf2 ~/.fluidsynth/default_sound_font.sf2
```
Then run:
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

