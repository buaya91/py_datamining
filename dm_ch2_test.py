import DataMiningCh2
import unittest
import math

class SimilarityMeasureTest(unittest.TestCase):

    a = {'a':3,'b':4,'c':2,'d':1,'e':5}
    b = {'a':3,'b':2,'c':1,'d':1,'e':4}
    users_rating = {
        'John':{},
        'Tom':{},
        'Jerry':{},
        'Jennifer':{},
        'Jane':{}
        }

    def test_manhattan_distance(self):
        self.assertEqual(DataMining.manhattan_distance(self.a,self.b),4)

    def test_euclidean_distance(self):
        self.assertEqual(DataMining.euclidean_distance(self.a,self.b),6**0.5)

    def test_minkowski_distance(self):
        self.assertEqual(DataMining.minkowski_distance(self.a,self.b,3),10**(1/3))

    def test_pearson_correlation_coefficient(self):
        self.assertTrue(-1<=DataMining.pearson_correlation_coefficient(self.a,self.b)<=1)

    def test_cosine_similarity(self):
        self.assertTrue(-1<=DataMining.cosine_similarity(self.a,self.b)<=1)

    def test_k_nearest_neighbour(self):
        k=1
        self.assertEqual(len(DataMining.k_nearest_neighbour(1,"cosine similarity",self.a,self.b)),k)

    def test_adjusted_cosine_similarity(self):
        self.assertTrue(-1<=DataMining.adjusted_cosine_similarity(self.a,self.b)<=1)

if __name__ == '__main__':
    unittest.main()
