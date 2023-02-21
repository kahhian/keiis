# importing the required modules
import os
import argparse
import sys
import subprocess
import shlex

from sheet2midi import s2m
from audio2midi import a2m

input_file = sys.argv[-1]

def play_midi(midi_filename):
        
    from midi2audio import FluidSynth
    FluidSynth('soundfonts/salamander_grand_piano.sf2')

    FluidSynth().play_midi(midi_filename)

# kahhian
def sheet2midi():
    s2m(input_file)
    


# kahhian
def audio2midi():

    a2m(input_file)

    # from piano_transcription_inference import (
    #     PianoTranscription,
    #     sample_rate,
    #     load_audio,
    # )

    # # Load audio
    # (audio, _) = load_audio("cut_liszt.mp3", sr=sample_rate, mono=True)

    # # Transcriptor
    # transcriptor = PianoTranscription(device="cpu")  # 'cuda' | 'cpu'

    # # Transcribe and write out to MIDI file
    # transcribed_dict = transcriptor.transcribe(audio, "cut_liszt.mid")

'''
def youtube2mp3():
    subprocess.run(
        shlex.split(
            "yt-dlp -x --audio-format mp3 "
            + input_file
        )
    )
'''

#cli
def main():
	# create parser object
    parser = argparse.ArgumentParser(description = "keiis")

	# defining arguments for parser object
    parser.add_argument("-mc", "--midicomparison", type = str, nargs = 2,
						metavar = "Input 2 midi files",
						help = "Midi Comparison Accuracy Test")
	
    parser.add_argument("-m2s", "--midi2sheet", type = str, nargs = 1,
						metavar = "Input a midi file",
						help = "Midi To Sheet Music")
	
    parser.add_argument("-s2m", "--sheet2midi", type = str, nargs = 1,
						metavar = "Input a pdf file",
						help = "Sheet Music To Midi")
	
    parser.add_argument("-a2m", "--audio2midi", type = str, nargs = 1,
						metavar = "Input a mp3 file",
                        help = "Audio To Midi")

    parser.add_argument("-pm", "--play_midi", type = str, nargs = 1,
						metavar = "Input a midi file",
                        help = "Midi Player")

    parser.add_argument("-m2pr", "--midi2pianoroll", type = str, nargs = 1,
						metavar = "Input a midi file",
                        help = "Midi To Piano Roll")



	# parse the arguments from standard input
    args = parser.parse_args()
	
    # calling functions depending on type of argument
    '''
	if args.midicomparison != None:
		midicomparison(args)
	elif args.midi2sheet != None:
		midi2sheet(args)
	'''
    if args.sheet2midi != None:
        sheet2midi(args)
    elif args.audio2midi != None:
        audio2midi(args)
    elif args.play_midi != None:
        play_midi(args)
    '''
    elif args.midi2pianoroll != None:
        midi2pianoroll(args)
	'''

if __name__ == "__main__":
	# calling the main function
	main()
