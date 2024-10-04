import time
import markupsafe
import subprocess
import shutil
import os

os.mkdir("testdir")
subprocess.run(["uv", "venv", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "markupsafe"], cwd="./testdir")
time.sleep(2)
res = subprocess.run(
    [
        "cmd",
        "/C",
        'openfiles /query /fo table | find /I "testdir\\.venv\\Lib\\site-packages\\markupsafe\\_speedups.cp312-win_amd64.pyd"',
    ],
    capture_output=True,
)
shutil.rmtree("testdir")

print(markupsafe.escape("Hello, <world>!"))
