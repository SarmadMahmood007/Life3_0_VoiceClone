Project Title: Life3_0_VoiceClone
Overview:
This project brings Life 3.0: Being Human in the Age of Artificial Intelligence by Max Tegmark to life through voice cloning technology! Inspired by the book’s stunning cover—a digital human figure rising from a DNA helix, symbolizing the fusion of humanity and AI—I extracted text from the PDF and used ElevenLabs to create a personalized audio narration. The book, published in 2017 by Alfred A. Knopf, explores the evolution of intelligence, the future of humanity, and AI’s impact, with chapters like "Welcome to the Most Important Conversation of Our Time" and "Intelligence Explosion?"
What I Did:

Extracted text from the 440-page PDF using Python (pypdf).
Converted it to a 6-minute speech using ElevenLabs’ Text-to-Speech API with a default voice (e.g., Rachel).
Cloned my own voice with ElevenLabs VoiceLab and transformed the audio to sound like me using Speech-to-Speech conversion.
Overcame challenges like quota limits by splitting the audio into manageable chunks and upgrading to a paid plan.

Tech Stack:

Python: For text extraction and API integration (requests, elevenlabs SDK).
ElevenLabs: For TTS and STS voice cloning.
Audacity/FFmpeg: For audio splitting and merging.
