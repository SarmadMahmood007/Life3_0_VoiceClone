import requests

API_KEY = "sk_c48dd1bae500f0d3bd36fda3f21741a32f46ecd33f51dff1"
RANDOM_VOICE = "21m00Tcm4TlvDq8ikWAM"  # Use a valid default voice

def text_to_random_speech(text_file_path, output_audio_path):
    with open(text_file_path, 'r', encoding='utf-8') as f:
        text = f.read()[:5000]  # Chunk for limits
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{RANDOM_VOICE}"
    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "output_format": "mp3_44100_128"
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open(output_audio_path, "wb") as f:
            f.write(response.content)
        print(f"Random speech audio saved to {output_audio_path}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Usage
text_to_random_speech("life_3.0_extracted.txt", "random_speech.mp3")