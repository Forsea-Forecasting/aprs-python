from aprslib.exceptions import UnknownFormat
from aprslib.exceptions import ParseError

__all__ = [
        'parse_thirdparty',
        ]

def parse_thirdparty(body):
    # Imported lazily to avoid a circular import with aprslib.parsing,
    # which imports this module via ``import *``.
    from aprslib.parsing import parse

    parsed = {'format':'thirdparty'}

    # Parse sub-packet
    try:
        subpacket = parse(body)
    except (UnknownFormat,ParseError) as ukf:
        raise

    parsed.update({'subpacket':subpacket})

    return('',parsed)
