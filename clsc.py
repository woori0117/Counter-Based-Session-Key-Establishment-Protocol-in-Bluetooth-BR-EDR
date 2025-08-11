#!/usr/bin/python
# -*- coding: utf-8 -*-



import logging

from e1 import e1
from es import Kc_to_Kc_prime
from e3 import e3

from constants import log

log.setLevel(logging.INFO)


def mac(LK, CTR_C, CTR_P, BTADDR):
    assert type(LK) == bytearray and len(LK) == 16
    assert type(CTR_C) == bytearray and len(CTR_C) == 8
    assert type(CTR_P) == bytearray and len(CTR_P) == 8
    assert type(BTADDR) == bytearray and len(BTADDR) == 6
    
    CTR_CP = CTR_C + CTR_P
    a, b = e1(LK, CTR_CP, BTADDR)
    ctr_mac = a + b

    return ctr_mac



def clsc_kdf(LK, AU_RAND, BTADDR, KEY_SIZE, MAC):


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