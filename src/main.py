import markupsafe
import subprocess
import shutil
import os

os.mkdir("testdir")
subprocess.run(["uv", "venv", "-v", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "-v", "markupsafe"], cwd="./testdir")
shutil.rmtree("testdir")

print(markupsafe.escape("Hello, <world>!"))
