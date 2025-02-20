import pytest
import subprocess
import hashlib

def test_student_output():
    answer = {'apple': 'bc52dd634277c4a34a2d6210994a9a5e2ab6d33bb4a3a8963410e00ca6c15a02',
    'banana': '1d0ebea552eb43d0b1e1561f6de8ae92e3de7f1abec52399244d1caed7dbdfa6',
    'grape': 'a512db2741cd20693e4b16f19891e72b9ff12cead72761fc5e92d2aaf34740c1',
    'mango': '9e6a72557ada15d02001f024f43f06edc4a31437e0e1bb3eeac36ca2d0c4fda7',
    'orange': '0a2d643bfd24a028cd236e76575d828424ccffbfa47392bd09d8ca9dc85e2f8d',
    'pineapple': '6af1f692e9496c6d0b668316eccb93276ae6b6774fa728aac31ff40a38318760',
    'strawberry': '4a8596a7790b5ca9e067da401c018b3206befbcf95c38121854d1a0158e7678a',
    'watermelon': '6c658ee83fb7e812482494f3e416a876f63f418a0b8a1f5e76d47ee4177035cb'}

    result = subprocess.run(["python", "2.py"], capture_output=True, text=True)

    message = result.stdout.split('\n')

    for key, value in answer.items():
        assert hashlib.sha256(str(value).encode()).hexdigest() == answer_hashes.get(key, ""), f"Wrong Answer"
    print("✅ You got 20 points.")
