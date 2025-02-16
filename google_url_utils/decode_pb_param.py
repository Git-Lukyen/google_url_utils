#!/usr/bin/env python3
import argparse

from google_url_utils.pb_utils.pb_value import PBValue


def _parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--input', '-i', required=True, help='the value from the url pb parameter')
    args.add_argument("--pretty_print", "-pp", required=False, default=False, action='store_true', help="pretty print the result or not")

    args = args.parse_args()
    return args


def main():
    args = _parse_args()
    pb_entries: list[str] = args.input.split("!")

    try:
        pb_entries.remove("")
    except ValueError:
        pass

    pb_values = PBValue.recursively_package_split_values(0, len(pb_entries) - 1, pb_entries, 0)
    print(PBValue.to_string_from_arr(pb_values, args.pretty_print))


if __name__ == '__main__':
    main()
