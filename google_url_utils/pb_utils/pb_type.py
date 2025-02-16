from enum import Enum


class PBType(Enum):
    MATRIX = "m"
    BOOL = "b"
    INT = "i"
    UNSIGNED_INT = "u"
    FLOAT = "f"
    DOUBLE = "d"
    STRING = "s"
    ENUM = "e"

    @staticmethod
    def get_values_regex():
        concat_values = "".join([e.value for e in PBType])
        return f"[{concat_values}]"

    def cast_value(self, str_value: str):
        match self:
            case PBType.MATRIX:
                return int(str_value)

            case PBType.BOOL:
                return bool(int(str_value))

            case PBType.INT:
                return int(str_value)

            case PBType.UNSIGNED_INT:
                return int(str_value)

            case PBType.FLOAT:
                return float(str_value)

            case PBType.DOUBLE:
                return float(str_value)

            case PBType.STRING:
                return str(str_value)

            case PBType.ENUM:
                return int(str_value)
