
#Exercise for Chapter 3
#Input Data Format :
#        user_ratings = {
#            "user_a":{"item_a":x, "item_b":x, "item_c":x, "item_d":x, "item_e":x, },
#            "user_b":{"item_a":x, "item_b":x, "item_c":x, "item_d":x, "item_e":x, },
#            "user_c":{"item_a":x, "item_b":x, "item_c":x, "item_d":x, "item_e":x, },
#            "user_d":{"item_a":x, "item_b":x, "item_c":x, "item_d":x, "item_e":x, },
#            }

#item-based filtering : find similarity between items instead of users
#we compute similarity between items ahead of time and store it, so when user rate itemA,
#we will find itemB which is most similar to itemA and expect user to like it

#we will implement several functions
#1. adjusted cosine similarity
#2. probability of user u would rate item i
#3. normalize rating
#4. slope one algorithm
#5. deviation between item i and j
#6.

import math
import dm_ch2

def adjusted_cosine_similarity(item_a_ratings, item_b_ratings, users_ratings):
    """
    to counter grade-inflation we will have to normalize the user rating, by subtracting average rating from each rating

    Pre-condition : argument 1 & 2 is ratings of items by all user, 3rd argument is a 2D matrix of all users' rating
    Post-condition : this function will return a similarity index of range [-1,1]
    """
    numerator_sum = 0
    denominator_sum_a = 0
    denominator_sum_b = 0

    for user in item_a_ratings:
        if user in item_b_ratings:
            user_mean = DataMiningCh2.mean(users_ratings[user])
            a = item_a_ratings[user] - user_mean
            b = item_b_ratings[user] - user_mean
            numerator_sum += a*b

            denominator_sum_a += a*a
            denominator_sum_b += b*b

    return numerator_sum/((denominator_sum_a**0.5)*(denominator_sum_b**0.5))

