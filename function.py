import os

try:
    import snap7
except Exception as e:
    print(' Installing snap7 library from pip ')
    import pip
    print(pip.main(['install', 'python-snap7']))
    import snap7
finally:
    print('snap7 imported successfully')

import snap7.client
from snap7.util import *


class S7300():
    def __init__(self, ip, debug=False):
        self.debug = debug
        self.plc = snap7.client.Client()
        self.plc.connect(ip, 0, 2)
        self.ip = ip
        print("Plc connection =", self.plc.get_connected())

    def __isconnected__(self):
        return self.plc.get_connected()

    def mbit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.read_area(Areas.MK, 0, st_input, 1)

            ibit = get_bool(bytearray(res), 0, bit)
            if ibit == True:
                return True
            else:
                return False
        else:
            print("no connection")

    def ibit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.read_area(Areas.PE, 0, st_input, 1)
            ibit = get_bool(bytearray(res), 0, bit)
            if ibit == True:
                return True
            else:
                return False
        else:
            print("no connection")

    def qbit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.read_area(Areas.PA, 0, st_input, 1)
            ibit = get_bool(bytearray(res), 0, bit)
            if ibit == True:
                return True
            else:
                return False
        else:
            print("no connection")

    def set_mbit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.read_area(Areas.MK, 0, st_input, 1)
            value = int.from_bytes(res, byteorder='big')
            bits_21_to_8 = (value | (2 ** bit))                     # O|R
            bits_bytearray = bits_21_to_8.to_bytes(1, 'big')
            self.plc.write_area(Areas.MK, 0, st_input, bits_bytearray)

        else:
            print("no connection")

    def xor(x, y):
        return bool((x and not y))

    def clear_mbit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.read_area(Areas.MK, 0, st_input, 1)
            # print(res)
            value = int.from_bytes(res, byteorder='big')
            bits_21_to_8 = (value & (~(2 ** bit)))
            bits_bytearray = bits_21_to_8.to_bytes(1, 'big')               # O|R
            self.plc.write_area(Areas.MK, 0, st_input, bits_bytearray)

        else:
            print("no connection")

    def set_ibit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.read_area(Areas.PE, 0, st_input, 1)
            ibit = get_bool(bytearray(res), 0, bit)
            if ibit == True:
                return True
            else:
                return False
        else:
            print("no connection")

    def set_qbit(self, st_input, bit):
        if self.plc.get_connected() == True:
            res = self.plc.write_area(Areas.PA, 0, st_input, 1)
            ibit = get_bool(bytearray(res), 0, bit)
            if ibit == True:
                return True
            else:
                return False
        else:
            print("no connection")

    def disconnect(self):
        self.plc.disconnect()
