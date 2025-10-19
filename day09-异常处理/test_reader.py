import builtins
import os
import io
import pytest

from reader import read_file_content, EmptyFileError, cli

def test_read_file_content_nonexistent():
    with pytest.raises(FileNotFoundError):
        read_file_content("definitely_not_exists_12345.txt")

