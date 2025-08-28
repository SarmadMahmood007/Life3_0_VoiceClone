import requests

API_KEY = "sk_c48dd1bae500f0d3bd36fda3f21741a32f46ecd33f51dff1"  # Your API key
TARGET_VOICE_ID = "W5apb94Jun9oTQuzFJsM"  # Replace with your cloned voice ID
INPUT_AUDIO_PATH = "random_speech.mp3"  # Path to your 6-min audio
OUTPUT_AUDIO_PATH = "my_voice_speech.mp3"  # Output file

def convert_speech_to_own_voice(input_audio_path, output_audio_path):
    url = f"https://api.elevenlabs.io/v1/speech-to-speech/{TARGET_VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": API_KEY
    }
    files = {
        "audio": open(input_audio_path, "rb")
    }
    data = {
        "model_id": "eleven_english_sts_v2",  # STS model
        "voice_settings": '{"stability": 0.5, "similarity_boost": 0.75}'  # Adjust for naturalness
    }
    
    response = requests.post(url, headers=headers, files=files, data=data)
    if response.status_code == 200:
        with open(output_audio_path, "wb") as f:
            f.write(response.content)
        print(f"Converted audio saved to {output_audio_path}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Usage
convert_speech_to_own_voice(INPUT_AUDIO_PATH, OUTPUT_AUDIO_PATH)