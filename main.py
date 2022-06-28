log_func = print


def enable_imports_from_project():
    """Добавляет проект в список путей из которых можно импортировать"""
    from sys import path
    from pathlib import Path

    ROOT_DIR = str(Path(__file__).parent)
    if ROOT_DIR not in path:
        path.append(ROOT_DIR)


#TODO: замеры памяти другой функцией на больших графах и этой функцией на больших графах
#TODO: импорт модулей
#TODO: исправить help (сделать понятнее использование внутренних парсеров + help без -- во внутренних парсерах)
if __name__ == '__main__':
    enable_imports_from_project()
    from src.interface.parser import make_parser

    parser = make_parser()
    args = parser.parse_args()

    from src.interface.command_handlers import \
        handle_report_cmd, handle_find_path_cmd, handle_test_cmd

    if args.name == 'report':
        handle_report_cmd(args)
    elif args.name == 'test':
        from tests import *

        handle_test_cmd()
    else:
        handle_find_path_cmd(args)
