import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/i5262602/Downloads/Spech-to-text-5863c2fd7a05.json"

#call convert.py to convert wav files to the right format

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    '20.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
      speech_contexts=[speech.types.SpeechContext(
            phrases=['hi', 'good afternoon'],
        )],
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))