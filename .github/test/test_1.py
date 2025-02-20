import pytest
import subprocess

def test_student_output():
    # 執行學生的 1.py，擷取標準輸出
    result = subprocess.run(["python", "1.py"], capture_output=True, text=True)

    # 獲取學生的 print 輸出
    message = result.stdout.replace("\n", "").split("UsingLLMtolearncodingissoeasy!!!")

    # 檢查是否有 100 次
    if message.count("") == 100 + 1:
        print("Pass!")
    else:
        print("Fail!")