from gtts import gTTS
import os

def text_to_speech(text, output_file):
    tts = gTTS(text, lang='ko')
    tts.save(output_file)
    os.system(output_file)  # 음성 파일 실행

if __name__ == "__main__":
    input_text = "안녕하세요. 반갑습니다."
    output_file = "output.mp3"
    text_to_speech(input_text, output_file)
##대화형으로 실행해야함