#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS-PC
#
# Created:     18/08/2014
# Copyright:   (c) ASUS-PC 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import test_data
import dm_ch3
import unittest


class DataMiningCh3Test(unittest.TestCase):


    data_generator = test_data.TestDataGenerator()
    users_ratings = data_generator.create_2d_dict(20,10)


    def test_adjust_cosine_similarity(self):
        self.assertTrue()


if __name__ == '__main__':
    unittest.main()
