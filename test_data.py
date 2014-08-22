#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS-PC
#
# Created:     17/08/2014
# Copyright:   (c) ASUS-PC 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from faker import Faker
import random

class TestDataGenerator():
    """
    a class to create test data

    a) create_list(type,no_of_elements)
    b) create_multi_d_data(dimension, value_type, *dimension_info)
    """

    faker = Faker()

    def create_list(self, value_type, no_of_elements):
        """
        return list of specified value type and no of elements

        expected input type:
            1. value_type should be string of Faker.providers
                example :
                    name
                    text
                    pyint
                    address
                    random_letter
                    company
                    job
            2. no_of_elements should be positive integer
        """

        if no_of_elements < 1:
            print("no of elements should be positive")
            return

        l = list()
        a = getattr(self.faker,value_type)

        for i in range(no_of_elements):
            l.append(a())

        return l

    def randomize_dict_values(self,types,dic):
        """
        it can go to the lowest level of nested dictionary and assign random integer
        value to it, the value is
        """

        if type(dic) is dict:       # if it is dictionary then we will go deeper
            # go through dictionary and update all elements of dictionary
            for key in dic:
                dic[key] = self.randomize_dict_values(types,dic[key])

        else:           #when we reach lowest level, which is not dictionary anymore
            a = getattr(self.faker,types)
            if type(a()) is int:
                dic = a()%6     #we want it to be within [1,5]
                if dic == 0:    #when it is 0, it means it is not rated, set to None
                    dic = None
            else:
                dic = a()

        return dic


    def create_multi_dimension_data(self,dimension, value_type='pyint', *dimension_info):
        """
        return multi-dimension dictionary data

        expected input type :
            1. dimension is int,
            2. value_type is string indicates values' type, eg, name, address, pyint
            3. *dimension_info is a list of tuples, (dimension_key_type,dimension_length)
        """
        key_matrix = list()
        key_pair_matrix = list()
        data = dict()

        # generate a list containing lists of keys for all dimension
        for i in range(dimension):
            list_of_keys = self.create_list(dimension_info[i][0],dimension_info[i][1])
            key_matrix.append(list_of_keys)


        value = 0
        value_holder = {}

        # create a multidimension dictionary using lists of dimension key
        for i in range(dimension):
            value_holder.clear()
            for key in key_matrix[dimension-i-1]:
                if hasattr(value,'copy'):
                    value_holder[key] = value.copy()
                else:
                    value_holder[key] = value
            value = value_holder.copy()

        # self.randomize_dict_values(value_type,value_holder)
        return self.randomize_dict_values(value_type,value_holder)


