import pyaudio
import wave

MIC_DEVICE_ID = 11 # 연결 음성 모델확인 후 변경

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 16000  # 카카오 음성 인식에서 요구하는 RATE
# 이것을 라즈베리파이에서는 인식을 못하여 아래 16k 변환
SAMPLE_SIZE = 2  # FORMAT의 바이트 수

# 녹음기 설정
def record(record_seconds):
    p = pyaudio.PyAudio()
    stream = p.open(input_device_index=MIC_DEVICE_ID,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Start to record the audio.")
    frames = []

    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording is finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames


# 녹음 데이터를 WAV 파일로 저장하기
def save_wav(target, frames):
    wf = wave.open(target, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_SIZE)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

    if isinstance(target, str):
        wf.close()


if __name__ == '__main__':
    RECORD_SECONDS = 3
    frames = record(RECORD_SECONDS)

    WAVE_OUTPUT_FILENAME = "rec.wav"
    save_wav(WAVE_OUTPUT_FILENAME, frames)
    
