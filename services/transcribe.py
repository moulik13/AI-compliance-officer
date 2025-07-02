from pydub import AudioSegment
import torchaudio
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import tempfile

# Load once
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
model.config.forced_decoder_ids = None  # Avoid forcing language

def convert_to_wav(audio_file_path: str) -> str:
    audio = AudioSegment.from_file(audio_file_path)
    audio = audio.set_frame_rate(16000).set_channels(1)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as wav_file:
        audio.export(wav_file.name, format="wav")
        return wav_file.name

def transcribe_audio(audio_path: str, language: str = "en") -> str:
    waveform, sample_rate = torchaudio.load(audio_path)

    input_features = processor(
        waveform.squeeze().numpy(),
        sampling_rate=sample_rate,
        return_tensors="pt"
    ).input_features

    # Force language (optional)
    forced_ids = processor.get_decoder_prompt_ids(language=language, task="transcribe")
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_ids)

    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription
