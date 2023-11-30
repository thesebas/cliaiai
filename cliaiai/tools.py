from contextlib import contextmanager
import sys


@contextmanager
def file_or_stdout(file_name):
    if file_name is None:
        yield sys.stdout
    else:
        with open(file_name, 'w') as out_file:
            yield out_file


@contextmanager
def file_or_stdin(file_name):
    if file_name is None:
        yield sys.stdin
    else:
        with open(file_name, 'r') as in_file:
            yield in_file
