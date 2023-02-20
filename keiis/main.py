# importing the required modules
import os
import argparse
import sys

from sheet2midi import s2m
from audio2midi import a2m

input_file = sys.argv[-1]

def play_midi(midi_filename):
        
    from midi2audio import FluidSynth
    FluidSynth('soundfonts/salamander_grand_piano.sf2')

    FluidSynth().play_midi(midi_filename)

# kahhian
def sheet2midi(args):
    s2m(input_file)
    


# kahhian
def audio2midi(args):

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


def main():
    # create parser object
    parser = argparse.ArgumentParser(description="keiis")

    # defining arguments for parser object
    parser.add_argument(
        "-mc",
        "--midicomparison",
        type=str,
        nargs="*",
        metavar="",
        help="Midi Comparison Accuracy Test",
    )

    parser.add_argument(
        "-m2s",
        "--midi2sheet",
        type=str,
        nargs="*",
        metavar="",
        help="Midi To Sheet Music",
    )

    parser.add_argument(
        "-s2m",
        "--sheet2midi",
        type=str,
        nargs="*",
        metavar="",
        help="Sheet Music To Midi",
    )

    parser.add_argument(
        "-a2m", "--audio2midi", type=str, nargs="*", metavar="", help="Audio To Midi"
    )

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    """
	if args.midicomparison != None:
		midicomparison(args)
	elif args.midi2sheet != None:
		midi2sheet(args)
	elif args.sheet2midi != None:
		sheet2midi(args)
	elif args.audio2midi != None:
		audio2midi(args)
	"""
    if args.sheet2midi != None:
        sheet2midi(args)
    elif args.audio2midi != None:
        audio2midi(args)


if __name__ == "__main__":
    # calling the main function
    main()
