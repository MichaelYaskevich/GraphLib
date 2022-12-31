log_func = print


def enable_imports_from_project():
    """Добавляет проект в список путей из которых можно импортировать"""
    from sys import path
    from pathlib import Path

    ROOT_DIR = str(Path(__file__).parent)
    if ROOT_DIR not in path:
        path.append(ROOT_DIR)


if __name__ == '__main__':
    enable_imports_from_project()
    from src.interface.parser import make_parser

    parser = make_parser()
    args = parser.parse_args()

    from src.interface.command_handlers import handle_report_cmd, \
        handle_find_path_cmd, handle_test_cmd, handle_visualization

    if args.name == 'report':
        handle_report_cmd(args)
    elif args.name == 'test':
        from Tests import *
        handle_test_cmd()
    elif args.name == 'visualize':
        handle_visualization(args)
    else:
        handle_find_path_cmd(args)
