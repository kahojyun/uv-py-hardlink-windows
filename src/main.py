import markupsafe
import subprocess
import shutil
import os

os.mkdir("testdir")
subprocess.run(["uv", "venv", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "markupsafe"], cwd="./testdir")
n = 5
while n > 0:
    try:
        shutil.rmtree("testdir")
    except PermissionError:
        n -= 1
        if n == 0:
            raise
    else:
        break

print(markupsafe.escape("Hello, <world>!"))
