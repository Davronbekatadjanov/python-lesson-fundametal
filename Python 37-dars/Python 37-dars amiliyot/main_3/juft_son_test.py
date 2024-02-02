import unittest
from juft_son import juftSonmi
class Juft_son_test(unittest.TestCase):
    def juft_test(self):
        # Test 1
        raqamlar1 = [1,2,3,4,5,6,7,8,9,10]
        natija1 = juftSonmi(raqamlar1)
        kutilgan_natija1 = [2,4,6,8,10]
        self.assertEqual(natija1, kutilgan_natija1)
        # Test 2
        raqamlar2 = [11,12,13,14,15,16,17,18,19,20]
        natija2 = juftSonmi(raqamlar2)
        kutilgan_natija2 = [12,14,16,18,20]
        self.assertEqual(natija2,kutilgan_natija2)
if __name__ == '__main__':
    unittest.main()
    
    