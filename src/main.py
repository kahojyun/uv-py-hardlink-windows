import time
import markupsafe
import subprocess
import shutil
import os

os.mkdir("testdir")
subprocess.run(["uv", "venv", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "markupsafe"], cwd="./testdir")
time.sleep(2)
shutil.rmtree("testdir")

print(markupsafe.escape("Hello, <world>!"))
