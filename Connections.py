import os

# 定义Mumu模拟器的ADB端口（默认16384）
MUMU_ADB_PORT = "127.0.0.1:16384"

def connect_adb():
    os.system(f"adb kill-server")
    status = os.system(f"adb connect {MUMU_ADB_PORT}")
    if status == 0:
        print(f"✅ Successfully connected to adb at {MUMU_ADB_PORT}")
    else:
        print(f"❌ Connection to adb at {MUMU_ADB_PORT} failed, please check and try again.")

def disconnect_adb():
    os.system(f'adb disconnect {MUMU_ADB_PORT}')
