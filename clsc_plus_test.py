#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
clsc_plus_tests.py

Test vectors for C-LSC+ KDF

This code is for testing C-LSC+ Session Key Refreshness.
"""

import logging

from clsc_plus import clsc_plus_kdf, mac
from constants import log
from es import bytearray_to_hexstring

log.setLevel(logging.INFO)


def test_clsc_plus():


    # CTR_C = 0x03
    # CTR_P = 0x08
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000004") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000009") # Update CTR_P += 1
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    mac_c = mac(LK, CTR_C, BTADDR)
    mac_p = mac(LK, CTR_P, BTADDR)
    computed_mac = mac_c[8:16] + mac_p[8:16]
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_plus_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC+ SK 01: %s", bytearray_to_hexstring(computed_SK))




    # CTR_C = 0x01
    # CTR_P = 0x04
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("0000000000000002") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000005") # Update CTR_P += 1
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    mac_c = mac(LK, CTR_C, BTADDR)
    mac_p = mac(LK, CTR_P, BTADDR)
    computed_mac = mac_c[8:16] + mac_p[8:16]
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_plus_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC+ SK 02: %s", bytearray_to_hexstring(computed_SK))



    # CTR_C = 0x1A
    # CTR_P = 0x08
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("000000000000001B") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("0000000000000009") # Update CTR_P += 1
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    mac_c = mac(LK, CTR_C, BTADDR)
    mac_p = mac(LK, CTR_P, BTADDR)
    computed_mac = mac_c[8:16] + mac_p[8:16]
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_plus_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC+ SK 03: %s", bytearray_to_hexstring(computed_SK))



    # CTR_C = 0xBD
    # CTR_P = 0xEA
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("00000000000000BE") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("00000000000000EB") # Update CTR_P += 1
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    mac_c = mac(LK, CTR_C, BTADDR)
    mac_p = mac(LK, CTR_P, BTADDR)
    computed_mac = mac_c[8:16] + mac_p[8:16]
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_plus_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC+ SK 04: %s", bytearray_to_hexstring(computed_SK))




    # CTR_C = 0xAB
    # CTR_P = 0xCD
    LK = bytearray.fromhex("55811EA673113F166E8411283F1D4E48")
    AU_RAND = bytearray.fromhex("00000000000000000000000000000000")
    CTR_C = bytearray.fromhex("00000000000000AC") # Update CTR_C += 1
    CTR_P = bytearray.fromhex("00000000000000CE") # Update CTR_P += 2
    BTADDR = bytearray.fromhex("ACFEDB9848D6")
    KEY_SIZE = 7

    # Generate MAC
    mac_c = mac(LK, CTR_C, BTADDR)
    mac_p = mac(LK, CTR_P, BTADDR)
    computed_mac = mac_c[8:16] + mac_p[8:16]
    log.info("MAC: %s", bytearray_to_hexstring(computed_mac))

    # Generate SK
    computed_SK = clsc_plus_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, computed_mac)
    log.info("C-LSC+ SK 05: %s", bytearray_to_hexstring(computed_SK))



if __name__ == "__main__":
    print("")
    test_clsc_plus()
    print("")

