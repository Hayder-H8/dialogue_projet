from pathlib import Path

from google.auth.credentials import Credentials
from google.cloud import texttospeech

credentials_path = Path(__file__).parent.parent / "TTS_credentials.json"
# Instantiates a client
# client = texttospeech.TextToSpeechClient()
client = texttospeech.TextToSpeechClient.from_service_account_json(str(credentials_path))

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Le programme marche")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(language_code="fr-FR", name="fr-FR-Standard-A", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')