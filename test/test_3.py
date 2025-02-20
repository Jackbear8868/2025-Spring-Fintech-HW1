import pytest
import subprocess
from cryptography.fernet import Fernet

def test_student_output():
    key = 'ErGgr5hOLD0q3IoFvkt7j0b2YFakr6ihREZLRNhIO5M='
    ans = b'gAAAAABnt1sBM2Zr6q8PoDR-z5tpkX4NKDSMep05ByHf2u73Me9ogy3vDFwrAAf_mCzbXsZZzuD5nFV40JoooOGImv86KP1tB_5LTsqhblm-D5VlOHy7eyZcnHxuvF-JxMBdBC59swSLRbJBhrdnzQxNEtxAmdGpK030HaimdkWGeB9VfuYu_UvpjkEF9yrM6z97HFZvn1G8h4Je_CpBC7VFT_QXOW5TYZQCDlwXWE4mhJvJFYVWtBlViBKs-MUMsHmeQF02G4Rq9CT5k9Bya1WZlUm3TDbJFrAwhzc3sGHuPyPNQ6s01iJKLyr2wrMpEHyzeccMV_TdRSV6UIH3vsPleIwSaAMWDrl55VuM5owE99uy0xKmRoahZH-CvBSybkKwdm777t0ZQa5TpmnGXOx3OFTbEEs7wLbBUXfZBGfRT-wMoSw4hpKUfT3pfUnEgrlkDHiDRVhubGvxRBjV0QK3qkVNrvEh3_JF1ZFJa1NFGCJXFJHFXQI='
    cipher = Fernet(key)
    decrypted_ans = cipher.decrypt(ans).decode()

    result = subprocess.run(["python", "3.py"], capture_output=True, text=True)

    message = result.stdout.replace("\n", "")

    assert decrypted_ans == message, f"❌ Wrong Answer"

    print("✅ You got 20 points.")
