import os
import subprocess
from pathlib import Path


def convert_ui_to_py(input_dir="./app/ui"):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".ui"):
                ui_path = Path(root) / file
                py_path = ui_path.with_suffix(".py")

                subprocess.run(["pyside6-uic", ui_path, "-o", py_path], check=True)
                subprocess.run(["pycln", py_path, "--all"])
                print(f"Converted: {ui_path} -> {py_path}")


if __name__ == "__main__":
    convert_ui_to_py()
