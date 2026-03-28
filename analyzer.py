import time
from collections import defaultdict

file_path = "logs.txt"

ip_count = defaultdict(int)

print("🔍 Monitoring logs in real-time...\n")

try:
    with open(file_path, "r") as file:
        # نروح لآخر الملف
        file.seek(0, 2)

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            ip = line.split()[0]
            ip_count[ip] += 1

            count = ip_count[ip]

            if count > 5:
                print(f"{ip} -> Brute Force Attack 🔴")
            elif count > 3:
                print(f"{ip} -> Scanning Attack 🟠")
            else:
                print(f"{ip} -> Normal Activity 🟢")

except:
    print("❌ حصل خطأ في قراءة الملف")