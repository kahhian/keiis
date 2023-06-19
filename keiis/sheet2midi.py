# kahhian  [ even though this thing is like 50 lines it took me 30 million hours to complete this because SO MANY ERRORS just trying to run stuff and documentation was so bad >:( ]

import os
import subprocess
import shlex
import sys

def s2m(input_file, mode):

    # whitespaces in file name
    if " " in input_file:
        print(
            'ERROR: Poor file name\nPlease use quotation marks around file name if it contains spaces. i.e "my file.pdf"'
        )
        return
    
    # extracting file name
    file_full_name = os.path.basename(input_file)
    file_name = os.path.splitext(file_full_name)[0]  # extracts name of file without file extension 
    

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
        except FileNotFoundError:
            
            # linux/bsd/unix
            try:
                subprocess.run(
                    shlex.split("musescore " + mode + "/{name}/{name}.mxl".format(name=file_name))
                )
            except FileNotFoundError:

                # linux appimage mscore 4
                try:
                    subprocess.run(
                        shlex.split("mscore4portable " + mode + "/{name}/{name}.mxl".format(name=file_name))
                    )
                except FileNotFoundError:
                    # linux appimage mscore 3
                    try:
                        subprocess.run(
                            shlex.split("mscore-portable " + mode + "/{name}/{name}.mxl".format(name=file_name))
                        )
                    except FileNotFoundError:
                        print("ERROR: MuseScore not found. Please install MuseScore and try again. https://musescore.org/en/download")
    
    # windows
    elif sys.platform.startswith('win32'):

        try:

            subprocess.run(
                shlex.split("MuseScore4.exe " + mode + "\{name}\{name}.mxl".format(name=file_name))
            )
        except Exception:

            try:
                subprocess.run(
                    shlex.split("MuseScore3.exe " + mode + "\{name}\{name}.mxl".format(name=file_name))
                )
            except FileNotFoundError:
                print("ERROR: MuseScore not found. Please install MuseScore and try again. https://musescore.org/en/download")

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

