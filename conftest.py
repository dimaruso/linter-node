import pytest

from typing import List

from os import listdir
from os.path import isfile, join

from _pytest.fixtures import FixtureRequest
from _pytest.config.argparsing import Parser


def need_skip_dir(dir_name: str) -> bool:
    """
    Directory name check
    :param dir_name: directory name
    :return: directory skip bool flag
    """
    need_skip: bool = \
        dir_name == "venv" or \
        dir_name[0] == "."

    return need_skip


def get_py_files_from_dir(project_dir: str) -> List[str]:
    """
    Get all python files (*.py) from a directory
    :param project_dir: project directory with python files
    :return: list of paths for python files
    """
    dir_list: List[str] = [project_dir]
    py_files: List[str] = list()

    while len(dir_list):
        cur_dir: str = dir_list.pop()
        for f_name in listdir(cur_dir):
            f_path: str = join(cur_dir, f_name)
            if isfile(f_path):
                if f_name[-3:] == ".py":
                    py_files.append(f_path)
            else:
                if not need_skip_dir(f_name):
                    dir_list.append(f_path)

    return py_files


def pytest_addoption(parser: Parser) -> None:
    """
    Add options '--dir' into pytest
    :param parser: pytest argparser class
    :return: None
    """
    parser.addoption(
        "--dir", action="store", help="set project dir path"
    )
    return None


@pytest.fixture(scope='session')
def py_files_list(request: FixtureRequest) -> List[str]:
    """
    Return list of full python file paths
    :param request: pytest FixtureRequest class
    :return: List of full python file paths
    """
    return get_py_files_from_dir(request.config.getoption("--dir"))
