def s2m(input_file):
    import os
    import subprocess
    import shlex

    # input_file = input("Enter pathname of pdf: ")

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
    new_path = "lessons/" + file_name
    print(new_path)
    count = 0
    if os.path.exists(new_path):
        cont = input(
            "WARNING: A file with the same name has been transcribed before. " +
            "\nPlease rename your file and try again, or enter [r] to rewrite transcription and continue. "
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
        shlex.split("mscore lessons/{name}/{name}.mxl".format(name=file_name))
    )

    # # musescore cli
    # subprocess.run(
    #     shlex.split(
    #         "mscore -o lessons/{name}/{name}.mid lessons/{name}/{name}.mxl".format(
    #             name=file_name
    #         )
    #     )
    # )

