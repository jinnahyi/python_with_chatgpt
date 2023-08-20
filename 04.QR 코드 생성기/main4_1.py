import qrcode

# QR 코드로 변환할 데이터
data = "https://www.example.com"

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,  # QR 코드의 크기와 복잡도 조절 (1부터 40까지)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 정정 수준 설정
    box_size=10,  # 각 QR 코드 모듈의 크기
    border=4,  # QR 코드 주위의 여백
)

qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 이미지 저장
img.save("qrcode_example.png")
