import markupsafe
import subprocess
import os

os.mkdir("testdir")
subprocess.run(["uv", "venv", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "markupsafe"], cwd="./testdir")
res = os.system("rmdir /S /Q testdir")
if res != 0:
    raise RuntimeError("rm failed")

print(markupsafe.escape("Hello, <world>!"))
