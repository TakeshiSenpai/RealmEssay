from google.cloud import texttospeech
import os

os.environ["GOOGLE_APP_CREDENTIALS"]="testservices-437021-9f204df463fb.json"


client = texttospeech.TextToSpeechClient()

synthesis_input=texttospeech.types.SynthesisInput(text="Cloudflare Workers")

voice=texttospeech.types.voiceSelectionParams(
    language_code="en-US",
    name="en-US-Standard-G",
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE
)

audio_config=texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3
)

response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

