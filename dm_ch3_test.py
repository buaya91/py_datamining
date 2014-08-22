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

    def test_change_rating_scale(self):
        for i in range(11):
            self.assertEqual(dm_ch3.change_rating_scale(0,10,-1,1,i),round((-1+(i*0.2)),5))

    def test_get_list_from_table_using_row_as_key(self):
        # create 2d table
        self.setup()

        # get 1st key from table
        key1 = list(self.users_ratings.keys())[0]
        l = dm_ch3.get_list_from_table(key1,self.users_ratings)
        # use function to extract and compare with table[key]
        self.assertDictEqual(self.users_ratings[key1],l)

        #test for col
        key1 = list(l.keys())[0]
        l = dm_ch3.get_list_from_table(key1,self.users_ratings)
        self.assertEqual(len(l),len(self.users_ratings))

    def test_compute_deviation_from_a_to_b(self):
        self.setup()
        k1 = list(self.users_ratings.keys())[0]
        k2 = list(self.users_ratings[k1].keys())[0]
        k3 = list(self.users_ratings[k1].keys())[1]
        a_to_b = dm_ch3.compute_deviation_from_a_to_b(k3,k2,self.users_ratings)
        b_to_a = dm_ch3.compute_deviation_from_a_to_b(k2,k3,self.users_ratings)
        self.assertEqual(a_to_b,-b_to_a)

        a_to_b = dm_ch3.compute_deviation_from_a_to_b(k2,k2,self.users_ratings)
        self.assertEqual(a_to_b,0)

    def test_card_func(self):
        test_dict = {}
        for i in range(1,11):
            test_dict[str(i)] = {}
            for j in range(11,16):
                if j>13 and i<3:
                    test_dict[str(i)][str(j)] = i*j
                else:
                    test_dict[str(i)][str(j)] = None
        print(test_dict)
        self.assertEqual(dm_ch3.user_no_rated_both_item('14','15',test_dict),2)

    def test_slope_one_prediction(self):
        run = False
        while run is False:
            self.setup()
            for u in self.users_ratings:
                for i in self.users_ratings[u]:
                    if self.users_ratings[u][i] == None:
                        run = True
                        ex = dm_ch3.slope_one_prediction(u,i,self.users_ratings)
                        self.assertTrue(1<=ex<=5)

if __name__ == '__main__':
    unittest.main()
