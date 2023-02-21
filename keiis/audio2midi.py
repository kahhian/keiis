# kahhian

import os

def a2m(input_file, mode):
    
    # extract name of file without file extension
    file_full_name = os.path.basename(input_file)
    file_name = os.path.splitext(file_full_name)[0]  

    # check if folder exists
    new_path = mode+"/" + file_name + "/" + file_name + ".mid"
    print("Writing to "+new_path)

    if os.path.exists(new_path):
        cont = input(
            "WARNING: A file with the same name has been transcribed before. " +
            "\nPlease rename your file and try again, or enter [r] to rewrite transcription and continue. "
        )
        print(cont)
        if cont != "r" and cont != "R":
            print("Transcription aborted.")
            exit()
            return 
        else:
            print("Rewriting transcription...")

    # create new folder
    else:
        os.makedirs(new_path)

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
    transcribed_dict = transcriptor.transcribe(audio, "{}".format(new_path))


