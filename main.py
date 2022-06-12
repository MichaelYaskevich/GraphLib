from sys import path
from pathlib import Path


def enable_imports_from_project():
    ROOT_DIR = str(Path(__file__).parent)
    if ROOT_DIR not in path:
        path.append(ROOT_DIR)


if __name__ == '__main__':
    enable_imports_from_project()

    from GraphLib.interface.parser import run
    from Tests import *

    run()
