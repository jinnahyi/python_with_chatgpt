#파이썬으로 컴퓨터의 외부 IP를 확인하는 코드를 작성해줘
import socket

def get_external_ip():
    try:
        # 호스트 이름을 얻어옴
        host_name = socket.gethostname()
        # 호스트 이름을 통해 IP 주소 얻어옴
        external_ip = socket.gethostbyname(host_name)
        return external_ip
    except Exception as e:
        return str(e)

external_ip = get_external_ip()
print("외부 IP 주소:", external_ip)
