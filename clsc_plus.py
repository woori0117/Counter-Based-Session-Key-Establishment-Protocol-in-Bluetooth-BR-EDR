#!/usr/bin/python
# -*- coding: utf-8 -*-



import logging

from e1 import e1
from es import Kc_to_Kc_prime
from e3 import e3

from constants import log

log.setLevel(logging.INFO)


def mac(LK, CTR, BTADDR):
    """Generate a 16 Byte diversifier message authentication code (MAC)."""
    assert type(LK) == bytearray and len(LK) == 16
    assert type(CTR) == bytearray and len(CTR) == 8
    assert type(BTADDR) == bytearray and len(BTADDR) == 6

    #pad CTR to 16 bytes to use e1
    CTR = CTR + bytearray(8)
    a, b = e1(LK, CTR, BTADDR)
    ctr_mac = a + b

    return ctr_mac



def clsc_plus_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, MAC):


    assert type(LK) == bytearray and len(LK) == 16
    assert type(AU_RAND) == bytearray and len(AU_RAND) == 16
    assert type(MAC) == bytearray and len(MAC) == 16
    assert type(BTADDR) == bytearray and len(BTADDR) == 6
    assert type(KEY_SIZE) == int and KEY_SIZE <= 16 and KEY_SIZE > 0


    BTADDR.reverse()
    _, COF = e1(LK, AU_RAND, BTADDR)
    BTADDR.reverse()


    Kc = e3(LK, MAC, COF)
    Kc.reverse()

    KcPrime = Kc_to_Kc_prime(Kc, KEY_SIZE)
    KcPrime.reverse()

    return KcPrime