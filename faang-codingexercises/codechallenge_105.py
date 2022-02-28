'''
Problem description:
====================
Networking is a big topic in computer science.  
IP addresses are used to identify computers on the internet.  
IP addresses are represented as strings of binary digits.  
The IP address consists of four parts, separated by periods.
Each part is a decimal number between 0 and 255 called octet.
Example: 137.99.255.123

Tasks:
======
Decimal to binary:

Byte 8 bits -- has a value of 0 to 255
Example: convert 174 to binary.
| bit   |  8        |  7    |  6    |  5    |  4    |  3  |  2  |  1  |
|-------|-----------|-------|-------|-------|-------|-----|-----|-----|
| Value | 128       |  64   |  32   |  16   |   8   |   4 |   2 |   1 |
|-------|-----------|-------|-------|-------|-------|-----|-----|-----|
| 174   |174>=128   |46>=64 |46>=32 |14>=16 |14>=8  |6>=4 |2>=2 |0>=1 |
|-------|-----------|-------|-------|-------|-------|-----|-----|-----|
|> or = |   Yes     | No    |  Yes  |  No   |  Yes  | Yes | Yes | No  |
|-------|-----------|-------|-------|-------|-------|-----|-----|-----|
|Result |     1     |  0    |  1    |  0    |  1    |  1  |  1  |  0  |


Decimal to Hexadecimal:
| 0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13  | 14 |  15 |
|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  A  |  B  |  C  |  D  |  E  |  F  |
|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|

Example: convert 192.145.19.234 to hexadecimal.
| Decimal    | 192       |  145      |    19    |   234    |
|------------|-----------|-----------|----------|----------|
| Binary     | 11000000  | 10010001  | 00010011 | 11101010 |
|------------|-----------|-----------|----------|----------|
|4-bit octet |1100 0000  |1001 0001  |0001 0011 |1110 1010 |
|------------|-----------|-----------|----------|----------|
|            | 12   0    | 9    1    | 1   3    | 14   10  |
|------------|-----------|-----------|----------|----------|
| Hexadecial | C    0    | 9    1    | 1   3    | E    A   |
|------------|-----------|-----------|----------|----------|

'''
import os
import unittest
import HtmlTestRunner
import time
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        if decimal >= 128:
            binary += '1'
            decimal = decimal - 128
        else:
            binary += '0'
            
        if decimal >= 64:
            binary += '1'
            decimal = decimal - 64
        else:
            binary += '0'
            
        if decimal >= 32:
            binary += '1'
            decimal = decimal - 32
        else:
            binary += '0'
            
        if decimal >= 16:
            binary += '1'
            decimal = decimal - 16
        else:
            binary += '0'
        
        if decimal >= 8:
            binary += '1'
            decimal = decimal - 8
        else:
            binary += '0'   
        
        if decimal >= 4:
            binary += '1'
            decimal = decimal - 4
        else:
            binary += '0'
            
        if decimal >= 2:
            binary += '1'
            decimal = decimal - 2
        else:
            binary += '0'
            
        if decimal >= 1:
            binary += '1'
            decimal = decimal - 1
        else:
            binary += '0'                
    return binary

def decimalIP_to_BinaryIP(decimalIP):
    # strip the decimal IP address to get the four octets
    octets = decimalIP.split('.')
    binaryOctets = [decimal_to_binary(int(octet)) for octet in octets]
    binaryIP = []
    for oct in binaryOctets:
        binaryIP.append(oct)
        
    return "{}.{}.{}.{}".format(binaryIP[0], binaryIP[1], binaryIP[2], binaryIP[3])
    

def decimalIP_to_HexIP(decimalIP):
    # strip the decimal IP address to get the four octets
    octets = decimalIP.split('.')
    hexVals = []
    binaryOctets = [decimal_to_binary(int(octet)) for octet in octets]
    for oct in binaryOctets:
        # convert each 4-bit binary octet to hexadecimal
        hexVal = hex(int(oct[0:4], 2))[2:] + hex(int(oct[4:8], 2))[2:]
        hexVals.append(hexVal)
        
    return str("{}.{}.{}.{}".format(hexVals[0], hexVals[1], hexVals[2], hexVals[3])).upper()

def hexIP_to_DecimalIP(hexIP):
    # strip the hex IP address to get the four octets
    octets = hexIP.split('.')
    decimalOctets = []
    for oct in octets:
        # convert each 2-character hexadecimal octet to decimal
        decimalOctets.append(int(oct[0:2], 16) * 16 + int(oct[2:4], 16))
        
    return "{}.{}.{}.{}".format(decimalOctets[0], decimalOctets[1], decimalOctets[2], decimalOctets[3])


class TestCodeChallenge105(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    # run all test methods                
    def test_IpAddresses(self):
        IPAddress = '192.168.100.22'
        time.sleep(1)
        self.assertEqual(decimal_to_binary(174), '10101110')
        self.assertEqual(decimalIP_to_BinaryIP(IPAddress), '11000000.10101000.01100100.00010110')        
        self.assertEqual(decimalIP_to_HexIP(IPAddress), 'C0.A8.64.16')
        
        
if __name__ == '__main__':
    print(type(os.environ.get('UNITTEST_ONLY')), type('True'))
    
    if os.environ.get('UNITTEST_ONLY') != 'True':
        IPAddress = '192.145.19.234'
        print("IP address: {} is {} in binary".format(IPAddress, decimalIP_to_BinaryIP(IPAddress)))
        print("IP address: {} is {} in hex".format(IPAddress, decimalIP_to_HexIP(IPAddress)))
        IPAddress = '192.168.100.22'
        print("IP address: {} is {} in binary".format(IPAddress, decimalIP_to_BinaryIP(IPAddress)))
        print("IP address: {} is {} in hex".format(IPAddress, decimalIP_to_HexIP(IPAddress)))
        IPAddress = 'C0.A8.64.16'
        print("IP address: {} is {} in decimal".format(IPAddress, hexIP_to_DecimalIP(IPAddress)))
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCodeChallenge105)
        unittest.TextTestRunner(verbosity=0).run(suite)
        # read the htlm output path from environment variable. e.g. local .env file.
        html_report_path = os.environ['HTML_REPORT_PATH']
        testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_path, report_title='Test Report for codechallenge_105.py')
        
        test_suite = unittest.TestSuite()
        all_test = unittest.makeSuite(TestCodeChallenge105)
        test_suite.addTest(all_test)
        test_suite.addTest(TestCodeChallenge105("test_IpAddresses")) 

        unittest.main(testRunner.run(test_suite))