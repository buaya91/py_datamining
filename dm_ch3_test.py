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
    users_ratings = data_generator.create_multi_dimension_data(2,'pyint',('name',10),('company',5))


    def test_adjust_cosine_similarity(self):
        username = list(self.users_ratings.keys())[0]
        l1 = self.users_ratings[username]
        itema = list(l1.keys())[0]
        itemb = list(l1.keys())[1]
        acs = dm_ch3.adjusted_cosine_similarity(itema,itemb,self.users_ratings)
        print(acs)
        self.assertTrue(-1<=acs<=1)

    #def test_prob_user_rate_item(self):



if __name__ == '__main__':
    unittest.main()
