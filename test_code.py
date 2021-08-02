from typing import List, Tuple
from mypy import api
from pycodestyle import StyleGuide, StandardReport  # type: ignore


def test_types_consistency(py_files_list: List[str]) -> None:
    """
    Test the conformity of variable types
    :param py_files_list: list of full python file paths
    :return: None
    """
    args: List[str] = list()
    args.extend(py_files_list)
    result: Tuple[str, str, int] = api.run(args)

    if result[0]:
        print('\nType checking report:\n')
        print(result[0])  # stdout

    if result[1]:
        print('\nError report:\n')
        print(result[1])  # stderr

    print('\nExit status:', result[2])

    assert result[2] != 2  # mypy can't run test
    assert result[2] == 0  # 0 errors and warnings

    return None


def test_code_format(py_files_list: List[str]) -> None:
    """
    Test that we conform to PEP-8.
    :param py_files_list: list of full python file paths
    :return: None
    """
    style: StyleGuide = StyleGuide(quiet=True, reporter=StandardReport)
    report: StandardReport = style.check_files(py_files_list)

    print(f'\nFound {report.total_errors} errors in test code format\n')
    assert report.total_errors == 0

    return None
