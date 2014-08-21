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

    data_generator = None
    users_ratings = None

    def setup(self):
        self.data_generator = test_data.TestDataGenerator()
        self.users_ratings = (self.data_generator.
                        create_multi_dimension_data(2,'pyint',('name',10),('company',5)))


    def test_adjust_cosine_similarity(self):
        self.setup()
        username = list(self.users_ratings.keys())[0]
        l1 = self.users_ratings[username]
        itema = list(l1.keys())[0]
        itemb = list(l1.keys())[1]
        acs = dm_ch3.adjusted_cosine_similarity(itema,itemb,self.users_ratings)
        self.assertTrue(-1<=acs<=1)

    def test_prob_user_rate_item(self):
        run = False
        while run is False:
            self.setup()
            for u in self.users_ratings:
                for i in self.users_ratings[u]:
                    if self.users_ratings[u][i] == None:
                        run = True
                        ex = dm_ch3.prob_user_rate_item(u,i,self.users_ratings)
                        self.assertTrue(1<=ex<=5)


if __name__ == '__main__':
    unittest.main()
