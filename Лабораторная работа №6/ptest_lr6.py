import pytest
import os
from lr6 import write_log, calculate


def test_creating_file_exception():
    args = [4, 8]
    log_file = '/2newoutput.txt'
    with pytest.raises(Exception) as context:
        write_log(*args, action='*', file=log_file)
    assert "Ошибка записи в файл" in str(context.value)


def test_calculate_division_by_zero():
    args = [8, 0]
    regex_text = "Division by zero is not possible"
    with pytest.raises(ValueError, match=regex_text):
        calculate(*args, operation='/')


def test_write_log_success():
    file_name = "test_log.txt"
    try:
        write_log(1, 2, action="test", result=3, file=file_name)
        with open(file_name, "r") as f:
            content = f.read()
        assert "test: (1, 2) = 3" in content
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)