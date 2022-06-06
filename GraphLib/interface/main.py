import sys
from pathlib import Path


if __name__ == '__main__':
    ROOT_DIR = Path(__file__).parent.parent.parent
    if str(ROOT_DIR) not in sys.path:
        sys.path.append(str(ROOT_DIR))

    from GraphLib.interface.parser import run

    run()
