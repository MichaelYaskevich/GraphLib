import sys
from pathlib import Path
ROOT_DIR = ''
if __name__ == '__main__':
    ROOT_DIR = Path(__file__).parent.parent.parent
    sys.path.append(str(ROOT_DIR))
    from GraphLib.interface.parser import run
    run()
