import pytest
import subprocess

def test_student_output():
    result = subprocess.run(["python", "1.py"], capture_output=True, text=True)

    message = result.stdout.replace("\n", "").split("UsingLLMtolearncodingissoeasy!!!")

    if message.count("") == 100 + 1:
        print("✅ You got 20 points.")
    else:
        assert message.count("") == 100 + 1, "❌ Wrong Answer."


