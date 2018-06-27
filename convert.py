from pydub import AudioSegment
from pydub.playback import play

audio_in_file = "./resources/22.wav"
audio_out_file = "./resources/23.wav"

# create 1 sec of silence audio segment
one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds

#read wav file to an audio segment
song = AudioSegment.from_wav(audio_in_file)

#Add above two audio segments
final_song = one_sec_segment + song

#Either save modified audio
final_song.export(audio_out_file, format="wav")

#Or Play modified audio
play(final_song)