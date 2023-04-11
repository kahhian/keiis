# kahhian  [ even though this thing is like 50 lines it took me 30 million hours to complete this because SO MANY ERRORS just trying to run stuff and documentation was so bad >:( ]

import os
import subprocess
import shlex
import sys

def s2m(input_file, mode):


    # extracting file name
    file_full_name = os.path.basename(input_file)
    file_name = os.path.splitext(file_full_name)[0]  # extracts name of file without file extension 


    # audiveris and musescore doesnt like whitespaces :/
    if " " in file_name:
        print(
            "ERROR: Poor file name\nPlease ensure that there are no whitespaces (empty spaces) in the name of your file before trying again."
        )
        return
    

    # check if folder exists
    new_path = mode+"/" + file_name
    print("Writing to " +new_path)

    if os.path.exists(new_path):
        cont = input(
            "WARNING: A file with the same name has been transcribed before. " +
            "\nPlease rename your file and try again, or enter [r] to rewrite transcription and continue. "
        )
        print(cont)
        if cont != "r" and cont != "R":
            print("Transcription aborted.")
            return 
        else:
            print("Rewriting transcription...")

    # create new folder
    else:
        os.makedirs(new_path)


    # audiveris cli
    subprocess.run(
        shlex.split(
            "java -cp 'Audiveris-5.2.5/lib/*' Audiveris -batch -output " + mode + " -export -transcribe "
            + input_file
        )
    )

    if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        # mac and linux/bsd/unix
        try:
            subprocess.run(
                shlex.split("mscore " + mode + "/{name}/{name}.mxl".format(name=file_name))
            )
        except Exception:
            
            # linux/bsd/unix
            try:
                subprocess.run(
                    shlex.split("musescore " + mode + "/{name}/{name}.mxl".format(name=file_name))
                )
            except Exception:

                # linux appimage mscore 4
                try:
                    subprocess.run(
                        shlex.split("mscore4portable " + mode + "/{name}/{name}.mxl".format(name=file_name))
                    )
                except Exception:
                    subprocess.run(
                        shlex.split("mscore-portable " + mode + "/{name}/{name}.mxl".format(name=file_name))
                    )
    
    # windows
    elif sys.platform.startswith('win32'):

        try:

            subprocess.run(
                shlex.split("MuseScore4.exe " + mode + "/{name}/{name}.mxl".format(name=file_name))
            )
        except Exception:
            subprocess.run(
                shlex.split("MuseScore3.exe " + mode + "/{name}/{name}.mxl".format(name=file_name))
            )

    # musescore cli
    # subprocess.run(
    #     shlex.split("mscore " + mode + "/{name}/{name}.mxl".format(name=file_name))
    # )

    # # musescore cli
    # subprocess.run(
    #     shlex.split(
    #         "mscore -o lessons/{name}/{name}.mid lessons/{name}/{name}.mxl".format(
    #             name=file_name
    #         )
    #     )
    # )

