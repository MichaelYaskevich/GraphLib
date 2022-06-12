from sys import path
from pathlib import Path


log_func = print


def enable_imports_from_project():
    """Добавляет проект в список путей из которых можно импортировать"""

    ROOT_DIR = str(Path(__file__).parent)
    if ROOT_DIR not in path:
        path.append(ROOT_DIR)


def run():
    """Выолняет произвольную команду из командной строки"""

    from GraphLib.interface.parser import make_parser
    from GraphLib.interface.command_handlers import \
        handle_report_cmd, handle_find_path_cmd, handle_test_cmd

    try:
        parser = make_parser()
        args = parser.parse_args()

        if args.name == 'report':
            handle_report_cmd(args)
        elif args.name == 'test':
            handle_test_cmd()
        else:
            handle_find_path_cmd(args)
    except Exception as e:
        log_func(e.args[0])


if __name__ == '__main__':
    enable_imports_from_project()

    from Tests import *

    run()
