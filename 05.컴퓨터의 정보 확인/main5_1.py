import psutil
import time

def print_system_usage():
    while True:
        # CPU 사용량 및 코어 수 가져오기
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        num_cores = psutil.cpu_count()

        # RAM 사용량 가져오기
        ram = psutil.virtual_memory()
        ram_percent = ram.percent

        # 네트워크 정보 가져오기
        network = psutil.net_io_counters()
        sent_bytes = network.bytes_sent
        received_bytes = network.bytes_recv

        # 정보 출력
        print(f"CPU 사용량 (%): {cpu_percent}")
        print(f"총 CPU 코어 수: {num_cores}")
        print(f"RAM 사용량 (%): {ram_percent}")
        print(f"전송된 데이터 (bytes): {sent_bytes}")
        print(f"수신된 데이터 (bytes): {received_bytes}")
        print("=" * 40)

        time.sleep(1)

if __name__ == "__main__":
    print_system_usage()
