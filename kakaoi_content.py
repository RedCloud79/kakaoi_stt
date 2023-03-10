# -*- coding: utf-8 -*-

from __future__ import print_function

import pyaudio
import wave
import io
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setup (17, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)
GPIO.setup (22, GPIO.OUT)
GPIO.setup (5, GPIO.OUT)
GPIO.setup (6, GPIO.OUT)
GPIO.setup (26, GPIO.OUT)

from pydub import AudioSegment
from kakaoi_autosound import *
from kakaoi_record import *

CHUNK = 1024
FORMAT = pyaudio.paInt16
SAMPLE_WIDTH = 2
CHANNELS = 1
RATE = 16000

# -*- coding: utf-8 -*-
def record(record_seconds=3): # 3초간 녹음기 활성화
    p = pyaudio.PyAudio()
    stream = p.open(input_device_index=10,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start to record the audio.") #녹음기 시작 출력 안내

    frames = []
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    print("Recording is finished.") #녹음이 끝났다는 출력 안내
    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames


def convertTo16K(file):
    # 16000 으로 변환
    sound = AudioSegment.from_file(file)
    sound = sound.set_frame_rate(16000)
    rec_data = io.BytesIO()
    sound.export(rec_data, format="wav")
    sound.export("rec.wav", format="wav")
    return rec_data


# wav 파일 저장
def getWav(frames):
    wavfile = io.BytesIO()
    wf = wave.open(wavfile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wavfile.seek(0)
    return wavfile


if __name__ == "__main__":
    audio_data = record()
    wav_data = getWav(audio_data)
    wav_data = convertTo16K(wav_data)
    # wav_data 처리
    result = dictation (wav_data.getvalue())  # wav 파일 내용 전달
    print('인식결과', result)
    #LED 제어
    if result.find('가디건') !=-1: #'가디건'이 들어왔을 때
        print('led on')
        GPIO.output(17, True) #LED를 켭니다.
        time.sleep(5)
        GPIO.output(17, False) #LED를 끕니다.
    if result.find('스타킹') !=-1: #'스타킹'이 들어왔을 때
        print('led on')
        GPIO.output(27, True) #LED를 켭니다.
        time.sleep(5)
        GPIO.output(27, False)  # LED를 끕니다.
    if result.find('레깅스') !=-1: #'레깅스'이 들어왔을 때
        print('led on')
        GPIO.output(22, True) #LED를 켭니다.
        time.sleep(5)
        GPIO.output(22, False)  # LED를 끕니다.
    if result.find('청바지') !=-1: #'청바지'이 들어왔을 때
        print('led on')
        GPIO.output(5, True) #LED를 켭니다.
        time.sleep(5)
        GPIO.output(5, False)  # LED를 끕니다.
    if result.find('목도리') !=-1: #'목도리'이 들어왔을 때
        print('led on')
        GPIO.output(6, True) #LED를 켭니다.
        time.sleep(5)
        GPIO.output(6, False)  # LED를 끕니다.
    if result.find('반바지') !=-1: #'반바지'이 들어왔을 때
        print('led on')
        GPIO.output(26, True) #LED를 켭니다.
        time.sleep(5)
        GPIO.output(26, False)  # LED를 끕니다.
        
        GPIO.cleanup()


