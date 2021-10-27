# Processor hex value get from http://www.jaist.ac.jp/iscenter-new/mpc/altix/altixdata/opt/intel/vtune/doc/users_guide/mergedProjects/analyzer_ec/mergedProjects/reference_olh/mergedProjects/instructions/instruct32_hh/vc46.htm
import unittest

cpuid_processor_string = {
    "0x80000002": {"eax": "0x20202020", 
                    "ebx": "0x20202020", 
                    "ecx": "0x20202020",
                    "edx": "0x6E492020"},
    "0x80000003": {"eax": "0x286c6574", 
                    "ebx": "0x50202952", 
                    "ecx": "0x69746e65",
                    "edx": "0x52286d75"},
    "0x80000004": {"eax": "0x20342029", 
                    "ebx": "0x20555043", 
                    "ecx": "0x30303531",
                    "edx": "0x007a484d"},
}

"""
Ref: https://stackoverflow.com/a/27506699
Swap little endian to big endian or vice versa

msb             lsb
+------------------+
| 12 | 34 | 56 | 78|
+------------------+

lsb             msb
+------------------+
| 78 | 56 | 34 | 12|
+------------------+
"""
def swap_endian32(x):
    return (((x << 24) & 0xFF000000) |
            ((x <<  8) & 0x00FF0000) |
            ((x >>  8) & 0x0000FF00) |
            ((x >> 24) & 0x000000FF))

class Test_swap_endian32(unittest.TestCase):
    def test_swap_endian32(self):
        self.assertEqual(0xefbeadde, swap_endian32(0xdeadbeef))



def hex_str_to_ascii(hex_str, swap=True):
    if swap is True:
        hex_str = hex(swap_endian32(int(hex_str, base=16)))
    hex_ = hex_str[2:]  # Remove "0x"
    hex_byte = bytes.fromhex(hex_)
    ascii_byte = hex_byte.decode("ASCII")
    return ascii_byte


def get_processor_string():
    str_ = ""
    for cpuid in cpuid_processor_string:
        for register, value in cpuid_processor_string[cpuid].items():
            str_ += hex_str_to_ascii(value)
    return str_

print(get_processor_string())


if __name__ == '__main__':
    unittest.main()