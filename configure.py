import json
import shutil
import subprocess as sp
from pathlib import Path

shutil.copy2("CMakeLists.txt.disabled", "CMakeLists.txt")
sp.run(["cmake", "--preset", "default"], check=True)
Path("CMakeLists.txt").unlink()
Path("build/CMakeCache.txt").unlink()
Path("build/compile_commands.json").rename("compile_commands.json")

with open("compile_commands.json", "r", encoding="utf-8") as fd:
    data = json.load(fd)

for item in data:
    directory = Path(item["directory"]).resolve()
    if not directory.exists():
        assert directory.is_relative_to(Path.cwd() / "build")
        directory.mkdir(parents=True)
