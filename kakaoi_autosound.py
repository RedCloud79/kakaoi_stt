import requests
import json

# 음성 데이터는 Mono Channel 16000 Hz samplerate 16bit depth의 rawpcm포맷만 지원.

#sample rate : 현실 세계의 아날로그 소리를 잘게 쪼갠 비율(속도). 잘게 쪼개진 하나를 샘플이라 부른다.
#  == 1초당 추출되는 샘플 개수 ex:) 44100 Hz - 1초당 44100개의 샘플
#- channel : 스피커 수와 연관 있다.
#- bits per sample : 하나의 샘플을 표현하기 위해 사용되는 bit 수.
#- bit rate : 1초당 비트 전송 수. (sample rate * channel * bits per sample)
#- RAW PCM 포맷 :  PCM(Pulse code modulation)로 표현한 오디오 데이터를 압축하지 않은 RAW 형태(wav 등)

#stt파트
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com" #카카오 개발자서버연결 "https://developers.kakao.com/"

rest_api_key = 'API KEY CODE' # 카카오 개발자서버 연결 코드

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}

def dictation(audio):
    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    
    result_json_string = res.text[
                         res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1
                         ]
    
    result = json.loads(result_json_string)
    return result['value']

if __name__ == "__main__":
    with open('rec.wav', 'rb') as fp: #파일명을 설정하여 mp3파일명을 가져옴
        audio = fp.read()
        result = dictation(audio)
        print(result) #text 출력
