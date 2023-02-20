import os

def a2m(input_file):

    from piano_transcription_inference import (
            PianoTranscription,
            sample_rate,
            load_audio,
        )

    # Load audio
    (audio, _) = load_audio(input_file, sr=sample_rate, mono=True)

    # Transcriptor
    transcriptor = PianoTranscription(device="cpu")  # 'cuda' | 'cpu'

    # extract name of file without file extension
    file_full_name = os.path.basename(input_file)
    file_name = os.path.splitext(file_full_name)[0]  

    # Transcribe and write out to MIDI file
    transcribed_dict = transcriptor.transcribe(audio, "transcribed/" + str(file_name)+ ".mid")


