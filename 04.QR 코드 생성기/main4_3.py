import os
import qrcode

# 폴더 경로 설정
output_folder = "04.QR 코드 생성기"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# "qrdata.txt" 파일에서 데이터 읽어오기
data_file_path = "C:/Users/user/ptyhon_with_chatgpt/python_with_chatgpt/04.QR 코드 생성기/qrdata.txt"
with open(data_file_path, "r") as file:
    data_lines = file.readlines()

# 각 데이터별로 QR 코드 생성 및 이미지 저장
for index, data in enumerate(data_lines):
    data = data.strip()  # 공백 및 줄바꿈 문자 제거
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 이미지 저장
    image_filename = f"qrcode_{index + 1}.png"
    image_path = os.path.join(output_folder, image_filename)
    img.save(image_path)
    print(f"QR 코드 이미지 {image_filename}가 {output_folder}에 저장되었습니다.")
