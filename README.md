# Smart Finder ( With. kakao_Api )

## 목차
*  📝 [개요](#-개요)
*  🛠 [기술 및 도구](#-기술-및-도구)
*  ✨ [기능 구현](#-기능-구현)

## **📝 개요**
> **프로젝트** : 스마트 파인더
>
> **인원** : 4인
> 
> **주제** : Kakao api의 stt를 활용하여 음성을 통한 수납함 위치 알림
> 
> **제작 기간** : 2022.3 ~ 2022.06
> 
> **주요 기능**   
> > * kakao api를 활용한 음성인식 데이터 처리
> > * 음성데이터를 활용한 하드웨어 제어
> > * 간단한 구조의 어플을 활용한 하드웨어 제어   
>
> **참고 포트폴리오**
> > * 링크 : https://drive.google.com/drive/folders/1Gude16PK_coomayESFHUlMIvitmLCzWT?usp=sharing



## **🛠 기술 및 도구**   
> **언어** : <img alt="python" src ="https://img.shields.io/badge/python-3776AB.svg?&style=flat-square&logo=python&logoColor=white"/>   
> **환경** : <img alt="raspberrypi" src ="https://img.shields.io/badge/raspberrypi-A22846.svg?&style=flat-square&logo=raspberrypi&logoColor=white"/>   
> **라이브러리** : <img alt="kakao" src ="https://img.shields.io/badge/kakao-FFCD00.svg?&style=flat-square&logo=kakao&logoColor=white"/>   
> **도구** : <img alt="github" src ="https://img.shields.io/badge/github-181717.svg?&style=flat-square&logo=github&logoColor=white"/>     


## **✨ 기능 구현**
### **블록도**
<img width="100%" alt="간단 블록도" src="https://github.com/RedCloud79/kakaoi_stt/blob/main/%EB%B8%94%EB%A1%9D%EB%8F%84.png" />

> * 작품의 유,무선의 연결에 대한 전체적인 구성을 표현한 블록도이다.

### **작품 구조**
<img width="70%" alt="작품의 구조" src="https://github.com/RedCloud79/kakaoi_stt/blob/main/%EC%9E%91%ED%92%88%EA%B5%AC%EC%A1%B0.PNG" />

> * 라프제리파이를 사용하여 led, usb마이크, button과 연결하였다.
> * 어플과 ip통신을 하여 연결을 해놨으며, 해당값에 따라 동작을 한다.
> * 상단에 마이크의 입력유무와 에러에대한 검출을 확인하는 led가 있다.

### **음성 플로우 차트**
<img width="100%" alt="플로우 차트" src="https://github.com/RedCloud79/kakaoi_stt/blob/main/%EC%9D%8C%EC%84%B1%EC%A0%9C%EC%96%B4%20%ED%94%8C%EB%A1%9C%EC%9A%B0%EC%B0%A8%ED%8A%B8.png" />

> * 동작스위치의 입력값이 들어올경우 마이크의 기능이 활성화된다.
> * 녹음기능을 통해 음성파일을 생성 후 .wav파일을 통해 텍스트로 변환하는 동작을 수행한다.
> * 조건문에 일치하는 값에 따른 GPIO핀의 제어를 통해 결과가 출력된다.
> * 결과동작 이후 오류 검출에대한 led의 동작을 수행하는 구조로 이루어져있다.

### **어플 플로우 차트**
<img width="100%" alt="플로우 차트" src="https://github.com/RedCloud79/kakaoi_stt/blob/main/%ED%94%8C%EB%A1%9C%EC%9A%B0%EC%B0%A8%ED%8A%B8.png" />

> * App inventer를 통해 간단한 어플을 구성하였다.
> * 연결은 라즈베리파이에서 서버를 열어서 핸드폰과 ip를 통한 통신을 사용한다. 이때 동일네트워크 상에서 이루어진다.
> * 어플에서 보내오는 이름에 따른 led on/off의 동작을 수행한다.

### **어플 블록코딩**
<img width="100%" alt="작품의 구조" src="https://github.com/RedCloud79/kakaoi_stt/blob/main/%EC%96%B4%ED%94%8C%20%EB%B8%94%EB%A1%9D%EC%BD%94%EB%94%A9.png" />

> * 어플 내부에서 송신하는 값을 확인할 수 있는 그림이다.
> * 라즈베리파이에서 열어주는 서버를 통해서 지정 url값을 전송하여 led를 제어한다.











