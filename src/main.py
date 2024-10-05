import markupsafe
import subprocess
import os

os.mkdir("testdir")
subprocess.run(["uv", "venv", ".venv"], cwd="./testdir")
subprocess.run(["uv", "pip", "install", "markupsafe"], cwd="./testdir")
subprocess.run(["pwsh", "-Command", "{Remove-Item -Recurse -Force testdir}"])

print(markupsafe.escape("Hello, <world>!"))
