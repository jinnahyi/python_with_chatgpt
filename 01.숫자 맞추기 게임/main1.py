import random

def main():
    target_number = random.randint(1, 100)
    attempts = 0

    print("1부터 100까지의 숫자 맞추기 게임을 시작합니다.")

    while True:
        user_guess = int(input("숫자를 입력하세요: "))
        attempts += 1

        if user_guess < target_number:
            print("숫자가 너무 작습니다.")
        elif user_guess > target_number:
            print("숫자가 너무 큽니다.")
        else:
            print(f"축하합니다! {attempts}회만에 숫자를 맞추셨습니다.")
            break

    print("게임이 종료되었습니다.")

if __name__ == "__main__":
    main()
