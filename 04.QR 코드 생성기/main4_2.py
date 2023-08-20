import os
import qrcode

# QR 코드로 변환할 데이터
data = "https://www.example.com"

# 폴더 경로 설정
output_folder = "04.QR 코드 생성기"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 이미지 저장
output_path = os.path.join(output_folder, "qrcode_example2.png")
img.save(output_path)

print(f"QR 코드 이미지가 {output_path}에 저장되었습니다.")
