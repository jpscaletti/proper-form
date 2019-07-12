from ..types import type_hex_color

from .field import Field


__all__ = ("HexColor", )


class HexColor(Field):
    """Accepts a color in hex, rgb, or rgba color and normalize it to a hex value
    of 6 digits or 6 digits plus one for alpha.

    Examples:

    - "#f2e" -> "#ff22ee"
    - "rgb(255, 0, 255)" -> "#ff00ff"
    - "rgb(221, 96, 89)" -> "#dd6059"
    - "rgba(221, 96, 89, 0.3)" -> "#dd60594c"
    """

    type = type_hex_color
