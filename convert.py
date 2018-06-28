import os
from pydub import AudioSegment


for x in os.listdir('./resources/ITSD_Calls'):
    if x.endswith('.wav'):
        print(x)
        file_to_mp3 = os.path.join(
            os.path.dirname(__file__),
            'resources/ITSD_Calls',
            x)
        song = AudioSegment.from_wav(file_to_mp3)
        song.export("./resources/ITSD_Calls_copy/"+x, format="wav")


    # if os.path.isfile(x): print 'f-', x
    # elif os.path.isdir(x): print 'd-', x
    # elif os.path.islink(x): print 'l-', x
    # else: print '---', x



