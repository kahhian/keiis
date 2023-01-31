def audio2midi():

    from piano_transcription_inference import PianoTranscription, sample_rate, load_audio

    # Load audio
    (audio, _) = load_audio('cut_liszt.mp3', sr=sample_rate, mono=True)

    # Transcriptor
    transcriptor = PianoTranscription(device='cpu')    # 'cuda' | 'cpu'

    # Transcribe and write out to MIDI file
    transcribed_dict = transcriptor.transcribe(audio, 'cut_liszt.mid')

def sheet2midi():

    '''
    import subprocess

    test = subprocess.Popen(["java","-cp",'"Audiveris-5.2.5/lib/*"',"Audiveris", "-batch", "-transcribe", "-export", "/Users/kahhian/Downloads/darlingfullscore.pdf"], stdout=subprocess.PIPE)
    output = test.communicate()[0]

    print(output)
    '''
    input_pdf = input("Enter pathname of pdf: ")
    import os
    os.system('java -cp "Audiveris-5.2.5/lib/*" Audiveris -batch -transcribe -export ' + input_pdf)
    
    
