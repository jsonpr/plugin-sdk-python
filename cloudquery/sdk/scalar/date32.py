from cloudquery.sdk.scalar import Scalar, ScalarInvalidTypeError, NULL_VALUE
from datetime import datetime, time
from typing import Any


class Date32(Scalar):
    def __eq__(self, scalar: Scalar) -> bool:
        if scalar is None:
            return False
        if type(scalar) == Date32:
            return self._value == scalar._value and self._valid == scalar._valid
        return False

    @property
    def value(self):
        return self._value

    def set(self, value: Any):
        if value is None:
            self._valid = False
            return

        if isinstance(value, Date32):
            self._valid = value.is_valid
            self._value = value.value
            return

        if type(value) == datetime:
            self._value = value
        elif type(value) == str:
            self._value = datetime.strptime(value, "%Y-%m-%d")
        elif type(value) == time:
            self._value = datetime.combine(datetime.today(), value)
        else:
            raise ScalarInvalidTypeError(
                "Invalid type {} for Date32 scalar".format(type(value))
            )

        self._valid = True
