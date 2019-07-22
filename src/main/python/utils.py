from typing import List


def validate_nip(nip: List[int]) -> bool:
    if len(nip) != 10:
        return False

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]

    sum = 0
    for i in range(9):
        sum += nip[i] * weights[i]

    checksum = sum % 11
    return checksum == nip[9]


def validate_regon(regon: List[int]) -> bool:
    if len(regon) != 9:
        return False

    weights = [8, 9, 2, 3, 4, 5, 6, 7]

    sum = 0
    for i in range(8):
        sum += regon[i] * weights[i]

    checksum = sum % 11
    if checksum == 10:
        checksum = 0

    return checksum == regon[8]
