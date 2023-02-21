import os
import argparse
import sys
import subprocess
import shlex

from sheet2midi import s2m
from audio2midi import a2m
from short_features import play_midi, midi_web

# kahhian
def sheet2midi(args):

    input_file = sys.argv[-1]

    s2m(input_file, "transcribed_s2m")
    
# kahhian
def midi_comparison(args):  
    midi_web()

# kahhian
def practice(args):

    from music21 import converter
    import mimetypes


    print("Hello! Welcome to practice mode.")

    bad_file = True

    while bad_file == True:
        
        input_file = input("- Enter the filepath to your sheet music/audio/video/midi file [formats supported: mid/midi/pdf/png/jpeg/common audio or video formats]\n- Or enter [e] to exit.\nEnter: ")
        if input_file == "e" or input_file == "E":
            print("See ya soon big baboon :D")
            exit()
        # extract file type 
        file_base_name = os.path.basename(input_file)
        file_name = os.path.splitext(file_base_name)[0] 
        file_type = os.path.splitext(file_base_name)[1] 


        #check if file is midi
        if file_type == ".mid" or file_type == ".midi":
            print("MIDI file {} uploaded.".format(file_base_name))
            bad_file = False

            print("Loading piano roll...")
            stream = converter.parse(input_file)
            stream.id = "stream"
            stream.plot("pianoroll")


        # check if file is sheet music
        elif file_type == ".pdf" or file_type == ".png" or file_type == ".jpg" or file_type == ".jpeg":

            print("Sheet music file {} uploaded.".format(file_base_name))
            bad_file = False

            # convert to midi
            try:

                s2m(input_file, "lessons")

            # prevent crash
            except Exception:

                print("Seems like something went wrong T_T\nPlease try again or check if there is something wrong with your input file.")
                bad_file = True
                continue

            # conversion is successful
            print("Conversion complete :)")


        # check if file is audio/video
        else:
            mimetypes.init()

            mimestart = mimetypes.guess_type(file_base_name)[0]

            if mimestart != None:
                mimestart = mimestart.split('/')[0]
                
                # if file format is invaild
                if mimestart not in ['audio', 'video']:

                    print("\nInvaild file format! Let's try again.")

                # file is audio/video
                else:

                    print("Audio/video file {} uploaded.".format(file_base_name))
                    bad_file = False

                    # convert to midi
                    try:

                        a2m(input_file, "lessons")

                    # prevent crash
                    except Exception:

                        print("Seems like something went wrong T_T\nPlease try again or check if there is something wrong with your input file.")
                        bad_file = True
                        continue

                    # conversion successful
                    print("Conversion complete :)")

                    # show piano roll
                    print("Loading piano roll...")
                    stream = converter.parse("lessons/{0}/{0}.mid".format(file_name))
                    stream.id = "stream"
                    stream.plot("pianoroll")
                    bad_file = False

    # show on piano roll

    # multitrack = pypianoroll.read("lessons/{0}/{0}.mid".format(file_name))
    # print(multitrack)
    # pypianoroll.save("lessons/{0}/{0}.npz".format(file_name), multitrack)
    # pypianoroll.load("lessons/{0}/{0}.npz".format(file_name))
    # print("HIH")
    # multitrack.plot()



    # midi comparison
    end_practice = input("Once you're done practicing, enter [s] to submit your recording or enter anything else to exit.\nCommand: ")
    if end_practice == "s":

        # input file
        input_file = input("- Enter the filepath to your audio/video.\nFile: ")
        # extract file type 
        file_base_name = os.path.basename(input_file)
        file_name = os.path.splitext(file_base_name)[0] 
        file_type = os.path.splitext(file_base_name)[1] 

        bad_file2 = True
        while bad_file2 == True:
            print("Audio/video file {} uploaded.".format(file_base_name))
            bad_file2 = False

            # convert to midi
            try:

                a2m(input_file, "lessons")

            # prevent crash
            except Exception:

                print("Seems like something went wrong T_T\nPlease try again or check if there is something wrong with your input file or its format.")
                bad_file2 = True
                continue

                # conversion successful
                print("Conversion complete :)")

        print("To exit practice mode, just close the website.")
    
        midi_web()
        print("See you soon :D")
    
    else:

        print("Exiting... See you next time :D")
        
# kahhian
def midi2pianoroll(args):
    from music21 import converter
    input_file = sys.argv[-1]
    print("Loading piano roll...")
    stream = converter.parse(input_file)
    stream.id = "stream"
    stream.plot("pianoroll")


# kahhian
def audio2midi(args):

    input_file = sys.argv[-1]

    a2m(input_file,"transcribed_a2m")

# seng hin
'''
def youtube2mp3():
    subprocess.run(
        shlex.split(
            "yt-dlp -x --audio-format mp3 "
            + input_file
        )
    )
'''

# seng hin
# cli
def main():
	# create parser object
    parser = argparse.ArgumentParser(description = "keiis")

	# defining arguments for parser object
    parser.add_argument("-mc", "--midi_comparison", type = str, nargs = "*",
						metavar = "Input multiple midi files",
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

    # parser.add_argument("-pm", "--play_midi", type = str, nargs = 1,
	# 					metavar = "Input a midi file",
    #                     help = "Midi Player")

    parser.add_argument("-m2pr", "--midi2pianoroll", type = str, nargs = 1,
						metavar = "Input a midi file",
                        help = "Midi To Piano Roll")

    # practice mode
    parser.add_argument(
        "-p",
        "--practice",
        type=str,
        nargs="*",
        metavar="Practice Mode",
        help="Practice Mode",
    )



	# parse the arguments from standard input
    args = parser.parse_args()
	
    # calling functions depending on type of argument
    '''
	if args.midi2sheet != None:
		midi2sheet(args)
	'''
    if args.sheet2midi != None:
        sheet2midi(args)
    elif args.audio2midi != None:
        audio2midi(args)
    elif args.midi_comparison != None:
        midi_comparison(args)
    elif args.practice != None:
        practice(args)
    elif args.midi2pianoroll != None:
        midi2pianoroll(args)

if __name__ == "__main__":
	# calling the main function
	main()
