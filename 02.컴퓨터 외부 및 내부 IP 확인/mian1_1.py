#파이썬으로 컴퓨터의 내부 IP 확인하는 코드
import socket

def get_internal_ip():
    try:
        # 호스트 이름을 얻어옴
        host_name = socket.gethostname()
        # 호스트 이름을 통해 IP 주소 얻어옴
        internal_ip = socket.gethostbyname(host_name)
        return internal_ip
    except Exception as e:
        return str(e)

internal_ip = get_internal_ip()
print("내부 IP 주소:", internal_ip)
