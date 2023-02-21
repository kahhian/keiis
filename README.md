# keiis
A helpful friend for piano practice.

## Feature list: https://www.notion.so/bc6bfb8ff4f34ae4b0e050b117570f42?v=503bffb3330d4ce59d3b53945e48a833

### General:
In terminal run to install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
In terminal run to install ffmpeg, musescore, and git:
```
brew install ffmpeg musescore git
```
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
Dependencies that need to be downloaded:

Java Development Kit (JDK) Version 11

Tesseract OCR Version 3.04 https://github.com/tesseract-ocr/tesseract/releases/tag/3.04.00

Then in terminal run:
```
git clone https://github.com/Audiveris/audiveris.git
```
cd audiveris
```
```
./gradlew build
```
cd <directory of the keiis file>
```
Then run to obtain midi file:
```
python3 sheet2midi.py -s2m <PDF file>
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
python3 main.py -pm <Midi file>
```
### Youtube Import:
In terminal run:
```
python3 -m pip install -U yt-dlp
```
Then run to obtain mp3 file:
```
yt-dlp -x --audio-format mp3 <video URL>
```


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

