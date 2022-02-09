"""
Example of Abstract Class
"""
from abc import ABC
from singleton import Singleton

class Silicon(metaclass=Singleton):
    def __init__(self, name=None):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None:
            self.__name = name
        else:
            self.__name = ""


class CPU(Silicon):
    def __init__(self, name=None):
        super().__init__(name)


class PCH(Silicon):
    def __init__(self, name=None):
        super().__init__(name)
    
intel = CPU("Intel")
print(intel, intel.name)

amd = CPU("AMD")
amd.name = "AMD"  # have to declare explicitly..
print(amd, amd.name)


intel_pch = PCH("Intel")
print(intel_pch, intel_pch.name)

amd_pch = PCH("AMD")
amd_pch.name = "AMD"  # have to declare explicitly..
print(amd_pch, amd_pch.name)