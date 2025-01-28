from typing import List

def bool_to_bytes(bits: List[bool]) -> bytes:
    """Convert list of bools to bytes"""
    result = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(bits):
                byte |= bits[i + j] << (7 - j)
        result.append(byte)
    return bytes(result)

def bytes_to_bool(data: bytes) -> List[bool]:
    """Convert bytes to list of bools"""
    result = []
    for byte in data:
        for i in range(8):
            result.append(bool((byte >> (7 - i)) & 1))
    return result