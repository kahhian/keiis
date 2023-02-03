# importing the required modules
import os
import argparse
import sys

input_file = sys.argv[-1]
def play_midi(midi_filename):
    import pygame

    # mixer config
    freq = 44100  # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024   # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    '''Stream music_file in a blocking manner'''
    clock = pygame.time.Clock()
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30) # check if playback has finished
    
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)

    # try:
    #     # use the midi file saved
    #     play_music(midi_filename)
    # except KeyboardInterrupt:
    #     # if user hits Ctrl/C then exit
    #     # (works only in console mode)
    #     pygame.mixer.music.fadeout(1000)
    #     pygame.mixer.music.stop()
    #     raise SystemExit


# kahhian
def sheet2midi(args):
    import subprocess
    import shlex

    input_file = input("Enter pathname of pdf: ")

    # extracting file name
    file_full_name = os.path.basename(input_file)
    file_name = os.path.splitext(file_full_name)[
        0
    ]  # extracts name of file without file extension name

    # audiveris and musescore doesnt like whitespaces :/
    if " " in file_name:
        print(
            "ERROR: Poor file name\nPlease ensure that there are no whitespaces (empty spaces) in the name of your file before trying again."
        )
        return

    # check if folder exists
    new_path = "lessons/" + file_name
    print(new_path)
    count = 0
    if os.path.exists(new_path):
        cont = input(
            "WARNING: A file with the same name has been transcribed before. \nPlease rename your file and try again, or enter [r] to rewrite transcription and continue. "
        )
        print(cont)
        if cont != "r" and cont != "R":
            return
        else:
            print("Rewriting transcription...")
    # create new folder
    else:
        os.makedirs(new_path)

    # audiveris cli
    subprocess.run(
        shlex.split(
            "java -cp 'Audiveris-5.2.5/lib/*' Audiveris -batch -output lessons -export -transcribe "
            + input_file
        )
    )

    subprocess.run(
        shlex.split(
            "mscore lessons/{name}/{name}.mxl".format(
                name=file_name
            )
        )
    )


    # # musescore cli
    # subprocess.run(
    #     shlex.split(
    #         "mscore -o lessons/{name}/{name}.mid lessons/{name}/{name}.mxl".format(
    #             name=file_name
    #         )
    #     )
    # )





# kahhian
def audio2midi(args):

    from piano_transcription_inference import (
        PianoTranscription,
        sample_rate,
        load_audio,
    )

    # Load audio
    (audio, _) = load_audio(input_file, sr=sample_rate, mono=True)

    # Transcriptor
    transcriptor = PianoTranscription(device="cpu")  # 'cuda' | 'cpu'

    # Transcribe and write out to MIDI file
    transcribed_dict = transcriptor.transcribe(audio, "cut_liszt.mid")


def main():
	# create parser object
	parser = argparse.ArgumentParser(description = "keiis")

	# defining arguments for parser object
	parser.add_argument("-mc", "--midicomparison", type = str, nargs = "*",
						metavar = "",
						help = "Midi Comparison Accuracy Test")
	
	parser.add_argument("-m2s", "--midi2sheet", type = str, nargs = "*",
						metavar = "", 
						help = "Midi To Sheet Music")
	
	parser.add_argument("-s2m", "--sheet2midi", type = str, nargs = "*",
						metavar = "yo",
						help = "Sheet Music To Midi")
	
	parser.add_argument("-a2m", "--audio2midi", type = str, nargs = "*",
						metavar = "hi", 
                        help = "Audio To Midi")



	# parse the arguments from standard input
	args = parser.parse_args()
	
	# calling functions depending on type of argument
	'''
	if args.midicomparison != None:
		midicomparison(args)
	elif args.midi2sheet != None:
		midi2sheet(args)
	elif args.sheet2midi != None:
		sheet2midi(args)
	elif args.audio2midi != None:
		audio2midi(args)
	'''
	if args.sheet2midi != None:
		sheet2midi(args)
	elif args.audio2midi != None:
		audio2midi(args)
	

if __name__ == "__main__":
	# calling the main function
	main()
