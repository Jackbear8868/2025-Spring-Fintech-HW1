import pytest
import subprocess
import json
from cryptography.fernet import Fernet

def test_student_output():
    key = 'P8aD5Do4T7ZY8riXis8YtlqngheLieIy22cvskvp17I='
    cipher = Fernet(key)

    ans = b'gAAAAABnt11n2AsQQVThOD6z5Y8xdvuUwJCx-xy0PscioSsAjJxIJrtvBtOunw7CgIJHCDCeax16dzJ7XsR-7jE6DOY2dOHxjT_69r2NJl-sYHuCSgIm5c-GMOdaFTs8GAiTFhqxm7vbIf5V_bZsX9amo9VuSH32jh2vpwlB2vfhyBRx5jbSmcfU4CxiSSJj9Bd9TIPoFpJmJH9XElRTNCm3WI9MjQnhPEQGm4PqJ6raqSRgQvfdH8js3sJcg04QtOPw7FbBSC1JJQv7ri2TocPaH4_mJ2HiGYvrTNL9dbJdjd2dvgbivFUXwxZ42bsuqxI8k7U3e3XBgrc6G_gCYVA15r0vsuDDXd_jGciJevhiGojhLWZSiuojaDJSpfuOXfozBQADzDn-O5pTFk3iXfFDyO_7VxxXQ14nsELGpcUDauNlICdcdbXn218VoclcMb9wVWlQ2zp3PvCxO-mXGgyP0IUBU3wTUg=='
    decrypted_ans = json.loads(cipher.decrypt(ans).decode())

    result = subprocess.run(["python", "4.py"], capture_output=True, text=True)

    message = result.stdout.split("\n")

    for i in range(len(decrypted_ans)):
        if message[i] != str(ans[i]):
            assert False, f"Wrong Answer"

    print("✅ You got 20 points.")
