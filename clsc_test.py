#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
clsc_tests.py

Test vectors for C-LSC KDF

This code is for testing C-LSC Session Key Refreshness.
"""

import logging

from clsc import clsc_kdf, mac
from constants import log
from es import bytearray_to_hexstring

log.setLevel(logging.INFO)


def test_clsc():


    # CTR_C and CTR_P = 0x00
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000001") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000002") # Update CTR_P += 2
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    computed_mac = mac(LK, CTR_C, CTR_P, BTADDR)
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC SK 01: %s", bytearray_to_hexstring(computed_SK))




    # CTR_C and CTR_P = 0x02
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000003") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000004") # Update CTR_P += 2
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    computed_mac = mac(LK, CTR_C, CTR_P, BTADDR)
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC SK 02: %s", bytearray_to_hexstring(computed_SK))



    # CTR_C and CTR_P = 0x04
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000005") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000006") # Update CTR_P += 2
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    computed_mac = mac(LK, CTR_C, CTR_P, BTADDR)
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC SK 03: %s", bytearray_to_hexstring(computed_SK))



    # CTR_C and CTR_P = 0x06
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000007") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000008") # Update CTR_P += 2
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    computed_mac = mac(LK, CTR_C, CTR_P, BTADDR)
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC SK 04: %s", bytearray_to_hexstring(computed_SK))




    # CTR_C and CTR_P = 0x08
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000009") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("000000000000000A") # Update CTR_P += 2
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    computed_mac = mac(LK, CTR_C, CTR_P, BTADDR)
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC SK 05: %s", bytearray_to_hexstring(computed_SK))



if __name__ == "__main__":
    print("")
    test_clsc()
    print("")

