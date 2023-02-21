# kahhian
def play_midi(midi_file):

    from midi2audio import FluidSynth
    FluidSynth('soundfonts/salamander_grand_piano.sf2')

    FluidSynth().play_midi(midi_file)

# andrea
def midi_web():
    import webbrowser

    # midi comparison website
    url = "https://jrg94.github.io/JuxtaMIDI/midiviz/dashboard.html"

    # call open method 
    webbrowser.open(url)