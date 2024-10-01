from google.cloud import texttospeech
import os

os.environ["GOOGLE_APP_CREDENTIALS"]="auth/testservices-437021-9f204df463fb.json"


client = texttospeech.TextToSpeechClient()

synthesis_input=texttospeech.SynthesisInput(text="Cloudflare Workers")

voice=texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Standard-G",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

audio_config=texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

