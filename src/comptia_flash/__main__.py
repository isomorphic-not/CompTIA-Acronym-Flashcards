import argparse
import random
from typing import Any, Optional

from comptia_flash import constants
from comptia_flash.comptia import get_comptia_data


def get_choices():
    return [
        "a1",
        "a2",
        "cloud",
        "casp",
        "cysa",
        "data",
        "itf",
        "linux",
        "net",
        "pen",
        "project",
        "sec",
        "server",
    ]


def main(argv: Optional[list[Any]] = None) -> None:
    parser = argparse.ArgumentParser(
        prog="CompTIA flash cards",
        description="Provides a quick insight into the required acronyms from CompTIA source.",
    )
    parser.add_argument("--comptia-test", choices=get_choices(), required=True)
    args = parser.parse_args(argv)
    data = []
    if args.comptia_test == "a1":
        data = get_comptia_data(constants.APlusOne)
    elif args.comptia_test == "a2":
        data = get_comptia_data(constants.APlusTwo)
    elif args.comptia_test == "casp":
        data = get_comptia_data(constants.CaspPlus)
    elif args.comptia_test == "cloud":
        data = get_comptia_data(constants.CloudPlus)
    elif args.comptia_test == "cysa":
        data = get_comptia_data(constants.CysaPlus)
    elif args.comptia_test == "data":
        data = get_comptia_data(constants.DataPlus)
    elif args.comptia_test == "itf":
        data = get_comptia_data(constants.ITFPlus)
    elif args.comptia_test == "linux":
        data = get_comptia_data(constants.LinuxPlus)
    elif args.comptia_test == "net":
        data = get_comptia_data(constants.NetPlus)
    elif args.comptia_test == "pen":
        data = get_comptia_data(constants.PenPlus)
    elif args.comptia_test == "project":
        data = get_comptia_data(constants.ProjectPlus)
    elif args.comptia_test == "sec":
        data = get_comptia_data(constants.SecPlus)
    elif args.comptia_test == "server":
        data = get_comptia_data(constants.ServerPlus)
    random.shuffle(data)
    print("\nPress <ENTER> to progress.\n")
    for data_item in data:
        input(f"\n{data_item.acronym}")
        print(data_item.value)


if __name__ == "__main__":
    main()
