from sys import path
from pathlib import Path


log_func = print


def enable_imports_from_project():
    """Добавляет проект в список путей из которых можно импортировать"""

    ROOT_DIR = str(Path(__file__).parent)
    if ROOT_DIR not in path:
        path.append(ROOT_DIR)


if __name__ == '__main__':
    enable_imports_from_project()
    from graphLib.interface.parser import make_parser

    try:
        parser = make_parser()
        args = parser.parse_args()

        from graphLib.interface.command_handlers import \
            handle_report_cmd, handle_find_path_cmd, handle_test_cmd

        if args.name == 'report':
            handle_report_cmd(args)
        elif args.name == 'test':
            from tests import *
            handle_test_cmd()
        else:
            handle_find_path_cmd(args)
    except Exception as e:
        log_func(e.args[0])
