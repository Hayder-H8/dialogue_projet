

from pathlib import Path

from google.auth.credentials import Credentials
from google.cloud import texttospeech

Dict1 = {"1" : "fr-FR", "2" : "en-US", "3" : "de-DE", "4" : "ar-XA","5" : "esp-ESP", "6" : "ru-RU", "7" : "fr-FR", "8" : "en-US", "9" : "ger-GER", "10" : "ar-AR","11" : "esp-ESP", "12" : "ru-RU","13" : "fr-FR","14" : "fr-FR","15" : "fr-FR","16" : "fr-FR","17" : "fr-FR","18" : "fr-FR"}
Dict2 = {"1" : "fr-FR-Standard-B", "2" : "en-GB-Standard-B", "3" : "de-DE-Standard-B", "4" : "ar-XA-Standard-B","5" : "esp-ESP-Standard-B","6" : "ru-RU-Standard-B",
         "7" : "fr-FR-Standard-A", "8" : "en-GB-Standard-A", "9" : "de-DE-Standard-A", "10" : "ar-XA-Standard-A","11" : "esp-ESP-Standard-A","12" : "ru-RU-Standard-A",
         "13" : "fr-FR-Standard-D","14" : "fr-FR-Wavenet-B","15" : "fr-FR-Wavenet-D","16" : "fr-FR-Standard-C","17" : "fr-FR-Standard-E","18" : "fr-FR-Wavenet-A"}

credentials_path = Path(__file__).parent.parent / "TTS_credentials.json"
# Instantiates a client
# client = texttospeech.TextToSpeechClient()
client = texttospeech.TextToSpeechClient.from_service_account_json(str(credentials_path))

# Set the text input to be synthesized
#synthesis_input = []
#for i in range(1, 6):
#    synthesis_input.append(texttospeech.SynthesisInput(text=""))
synthesis_input1 = texttospeech.SynthesisInput(text="Le programme marche, le parle français .")
synthesis_input2 = texttospeech.SynthesisInput(text="The programm works, I speak english")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
#voice = []
#for i in range(1, 6):
#    voice.append(texttospeech.VoiceSelectionParams(language_code="", name="", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL))
voice1 = texttospeech.VoiceSelectionParams(language_code="fr-FR", name="fr-FR-Standard-B", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
voice2 = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Standard-A", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
#response =[]
#for i in range(1, 6):
  #  response.append(client.synthesize_speech(
  #      input=synthesis_input[i], voice=voice[i], audio_config=audio_config
 #   ))
response1 = client.synthesize_speech(
    input=synthesis_input1, voice=voice1, audio_config=audio_config
)
response2  = client.synthesize_speech(
    input=synthesis_input2, voice=voice2, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response1.audio_content)
    print("C:\user\guipa\output.mp3")
    print('Audio content written to file "output.mp3"')