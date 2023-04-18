# keiis
### Enhancing your piano practice sessions with machine learning.

#### Feature list: 
https://www.notion.so/bc6bfb8ff4f34ae4b0e050b117570f42?v=503bffb3330d4ce59d3b53945e48a833
#### Gantt Chart/Development Timeline: 
https://www.notion.so/outvision/10a8b4d4d1fc48f89fd2ab8f07a5fb55?v=596318bbdc24493ebb037eac4d52ac4f&pvs=4

# Installation

## For all devices:

#### Install Python Version 3.9 or later:
#### https://www.python.org/downloads
#### Install the Java SE Development Kit 11.0.17 from the Oracle website: 
#### https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html
If you are using:
- a **M1/M2 (ARM) powered _Apple_** device, download and run the "macOS Arm 64 DMG Installer".	
- an **Intel powered _Apple_** device, download and run the "macOS x64 DMG Installer". 
- a **Windows** device, download and run the "Windows x64 Installer".
- a **Linux** device, you should know which one to download :)

### Now follow your operating system's specific procedure:

## MacOS:
#### 1. Install Homebrew by entering this line in Terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
#### 2. After installing Homebrew, enter these lines in Terminal one by one:
```
brew install ffmpeg musescore git fluidsynth wget
```
```
pip install -r requirements.txt
```
<!---
(defunct midi playback)
```
mkdir -p ~/.fluidsynth
```
```
ln -s soundfonts/salamander_grand_piano.sf2 ~/.fluidsynth/default_sound_font.sf2
```
-->

## Linux
We are finalizing installations procedures for linux, keiis may still not fully work after these instructions.


#### 1. In Terminal, enter:
```
sudo apt-get install ffmpeg git fluidsynth wget
```
```
pip install -r requirements.txt
```

## Windows
Work in progress


#### 1. Install ffmepg through the first link, follow the steps in the second link:
```
https://ffmpeg.org/download.html
```
```
https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
```
#### 2. Install Chocolatey with either Command Prompt/Powershell:
```
https://docs.chocolatey.org/en-us/choco/setup
```

#### 3. After installing Chocolatey, enter these lines in Command Prompt/Powershell:
```
choco install musescore git fluidsynth wget
```
```
pip install -r requirements.txt
```

# Using keiis

### Keiis is run via command line interface (Terminal/Command Prompt). 
### To start keiis, enter this in your CLI:
```
cd <directory of your keiis installation>
```
The directory of your keiis installation is usually in your home folder.
### Practice Mode:
In your CLI, enter:
```
python3 keiis/main.py -p <file>
```
Then enter the path of your practice sheet music (pdf/png/jpg) or original song (common audio/video formats) or MIDI file.\
If you provided sheet music, a Musescore window will open soon. Edit the sheet music till it looks/sounds like your original song.\
Once finished editing, on Musescore go to File > Export, and then change format to MIDI file. DO NOT CHANGE THE FILE NAME.Click export, and then close the Musescore window. You will be prompted to save the Musescore (.mscz) file. Save the file.DO NOT CHANGE THE FILE NAME.\
Follow the instructions prompt thereafter.

### Audio To Midi:
Used to obtain a MIDI file from your audio recording. (Accepts most audio and video file formats)\
In your CLI, enter:
```
python3 keiis/main.py -a2m <file>
```
### Sheet Music To Midi:
Used to obtain a MIDI file from your sheet music. (Accepts PDF and most image file formats)\
In your CLI, enter:
```
python3 keiis/main.py -s2m <file>
```
### Midi To Piano Roll:
Used to obtain a piano roll from your MIDI file.\
In your CLI, enter:
```
python3 keiis/main.py -m2pr <Midi file>
```

<!---
### Midi Playback:
Used to play audio from your MIDI file.\
In your CLI, enter:
```
python3 keiis/main.py -pm <Mp3 file>
```
-->

### Midi Comparison:
Used to obtain comparisons of two or more MIDI files.\
In your CLI, run:
```
python3 keiis/main.py -mc
```
This opens a website that compares midi files.\
Press the "Add Midi" button and add the midi files that you want to compare.




### Youtube Import:

Run to obtain mp3 file:
```
yt-dlp -x --audio-format mp3 <video URL>
```
We will integrate this feature into keiis in the future.
