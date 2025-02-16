import re
from typing import List, Optional

from google_url_utils.pb_utils.pb_type import PBType

class PBValue:
    _VALUE_REGEX = re.compile(f"(\d+)({PBType.get_values_regex()})([^!]*)")

    def __init__(self, id: int, type: PBType, value, contained: List['PBValue'] = None, depth: Optional[int] = None):
        self.id = id
        self.type = type
        self.value = value
        self.depth = depth
        self.contained = contained if contained is not None else []

    @classmethod
    def from_text_value(cls, text_value, depth: Optional[int] = None):
        matched_groups = cls._VALUE_REGEX.match(text_value)

        value_id = int(matched_groups.group(1))
        value_type = PBType(matched_groups.group(2))
        any_value = matched_groups.group(3)

        return PBValue(value_id, value_type, value_type.cast_value(any_value), None, depth)

    @classmethod
    def recursively_package_split_values(cls, start: int, end: int, split_values: List[str], depth: int = 0) -> List['PBValue']:
        packaged_values = []

        index = start
        while index <= end:
            split_value = split_values[index]
            pb_value = cls.from_text_value(split_value, depth)

            if pb_value.type == PBType.MATRIX:
                new_start = start + (index - start) + 1
                new_end = new_start + pb_value.value - 1

                nested_pb_values = cls.recursively_package_split_values(new_start, new_end, split_values, depth + 1)
                pb_value.contained = nested_pb_values
                index = new_end

            packaged_values.append(pb_value)
            index += 1

        return packaged_values

    def to_string(self, pretty: bool = False, prefix: str = "") -> str:
        indent = "  " * (self.depth if self.depth is not None else 0) if pretty else ""
        indent = prefix + indent
        eol_char = "\n" if pretty else ""
        join_char = ", \n" if pretty else ", "

        if self.type != PBType.MATRIX:
            return f"{indent}{self.id}{self.type.value}: {self.value}"
        else:
            str_values = join_char.join([pb_value.to_string(pretty, prefix) for pb_value in self.contained])
            return f"{indent}{self.id}{self.type.value}: [{eol_char}{str_values}{eol_char}{indent}]"

    @classmethod
    def to_string_from_arr(cls, pb_values: List['PBValue'], pretty: bool = False) -> str:
        eol_char = "\n" if pretty else ""
        join_char = ", \n" if pretty else ", "

        str_values = join_char.join([pb_value.to_string(pretty, "  " if pretty else "") for pb_value in pb_values])
        return f"[{eol_char}{str_values}{eol_char}]{eol_char}"
