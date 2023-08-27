import zipfile
import itertools

def find_zip_password(zip_filename, charset, min_length, max_length):
    """
    주어진 zip 파일의 암호를 찾는 함수입니다.
    
    :param zip_filename: 암호를 찾을 zip 파일의 경로
    :param charset: 사용할 문자셋 (영문 대소문자와 숫자 등)
    :param min_length: 최소 암호 길이
    :param max_length: 최대 암호 길이
    :return: 찾은 암호, 실패 시 None
    """
    # 모든 가능한 길이와 문자 조합을 생성하는 중첩된 for 루프
    for length in range(min_length, max_length + 1):
        # itertools.product를 사용하여 charset에서 길이 length의 모든 조합 생성
        for password in itertools.product(charset, repeat=length):
            # 조합된 암호를 문자열로 변환
            password_str = ''.join(password)
            
            try:
                # zip 파일 열기 시도
                with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                    # 암호를 사용하여 zip 파일 열기 시도
                    zip_ref.extractall(pwd=password_str.encode('utf-8'))
                # 암호를 찾았을 경우 찾은 암호 반환
                return password_str
            except zipfile.BadZipFile:
                # 암호가 틀렸을 경우 BadZipFile 예외 발생
                pass
            except Exception as e:
                # 다른 예외가 발생한 경우, 예를 들면 압축 해제 중 문제 발생 등
                print(f"An error occurred: {e}")
    
    # 암호를 찾지 못한 경우 None 반환
    return None

# 찾을 zip 파일 경로
zip_file_path = '06.압축 파일 암호 푸는 프로그램\암호.zip'
# 사용할 문자셋 (영문 대소문자와 숫자)
charset = 'a123456789'
# 최소 암호 길이와 최대 암호 길이 설정
min_length = 1
max_length = 5

# 함수 호출하여 암호 찾기 시도
found_password = find_zip_password(zip_file_path, charset, min_length, max_length)

if found_password:
    print(f"암호를 찾았습니다: {found_password}")
else:
    print("암호를 찾지 못했습니다.")
