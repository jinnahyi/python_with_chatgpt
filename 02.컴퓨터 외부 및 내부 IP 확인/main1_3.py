#내부 IP,외부 IP 한 번에 출력하기
import socket
import urllib.request

def get_internal_ip():
    try:
        # 호스트 이름을 얻어옴
        host_name = socket.gethostname()
        # 호스트 이름을 통해 IP 주소 얻어옴
        internal_ip = socket.gethostbyname(host_name)
        return internal_ip
    except Exception as e:
        return str(e)

def get_external_ip():
    try:
        url = "https://api64.ipify.org?format=json"
        response = urllib.request.urlopen(url)
        data = response.read().decode("utf-8")
        external_ip = data.split(':')[1].split('"')[1]
        return external_ip
    except Exception as e:
        return str(e)

internal_ip = get_internal_ip()
external_ip = get_external_ip()

print("내부 IP 주소:", internal_ip)
print("외부 IP 주소:", external_ip)
