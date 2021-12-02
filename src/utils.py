from pathlib import Path


def get_input(filepath):
    with Path(filepath).open() as f:
        for line in f.readlines():
            yield line.rstrip('\n')
