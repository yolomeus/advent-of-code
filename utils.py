from os import PathLike


def read_file_as_lines(filepath: str | PathLike) -> tuple[str]:
    with open(filepath, "r", encoding="utf-8") as fp:
        return tuple(map(lambda x: x.strip(), fp.readlines()))


def read_file_as_tuples(filepath: str | PathLike) -> tuple[tuple[str, ...], ...]:
    with open(filepath, "r", encoding="utf-8") as fp:
        return tuple(map(lambda x: tuple(x.strip()), fp.readlines()))


def read_file(filepath: str | PathLike) -> str:
    with open(filepath, "r", encoding="utf-8") as fp:
        return fp.read().strip()
