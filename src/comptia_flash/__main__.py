import argparse
import random
from typing import Any, Optional

from comptia_flash import constants
from comptia_flash.comptia import get_comptia_data


def get_choices():
    return ["a1", "a2", "net", "sec", "pen", "cysa", "casp"]


def main(argv: Optional[list[Any]] = None) -> None:
    parser = argparse.ArgumentParser(
        prog="CompTIA flash cards",
        description="Provides a quick insight into the required acronyms from CompTIA source.",
    )
    parser.add_argument("--comptia-test", choices=get_choices(), required=True)
    args = parser.parse_args(argv)
    data: list
    if args.comptia_test == "a1":
        data = get_comptia_data(constants.APlusOne)
    elif args.comptia_test == "a2":
        data = get_comptia_data(constants.APlusTwo)
    elif args.comptia_test == "net":
        data = get_comptia_data(constants.NetPlus)
    elif args.comptia_test == "sec":
        data = get_comptia_data(constants.SecPlus)
    elif args.comptia_test == "pen":
        data = get_comptia_data(constants.PenPlus)
    elif args.comptia_test == "cysa":
        data = get_comptia_data(constants.CysaPlus)
    elif args.comptia_test == "casp":
        data = get_comptia_data(constants.CaspPlus)
    random.shuffle(data)
    print("\nPress <ENTER> to progress.\n")
    for data_item in data:
        input(f"\n{data_item.acronym}")
        print(data_item.value)


if __name__ == "__main__":
    main()
