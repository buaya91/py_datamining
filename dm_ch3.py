
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

def adjusted_cosine_similarity(item_a_name, item_b_name, users_ratings):
    """
    to counter grade-inflation we will have to normalize the user rating, by subtracting average rating from each rating

    Pre-condition : argument 1 & 2 is items we want to compare, 3rd argument is a 2D matrix of all users' rating
                    the format will be {user_name:{item:rating,....},user_name2:{item:rating,....},....}

    Post-condition : this function will return a similarity index of range [-1,1]
    """

    # preprocess of data
    # extract ratings for specified items, and discard None which
    # indicate user did not rate the item
    item_a_ratings = {}
    item_b_ratings = {}

    for u_name in users_ratings:
        for i_name in users_ratings[u_name]:
            if users_ratings[u_name][i_name] != None:
                if i_name == item_a_name:
                    item_a_ratings[u_name] = users_ratings[u_name][i_name]
                if i_name == item_b_name:
                    item_b_ratings[u_name] = users_ratings[u_name][i_name]


    numerator_sum = 0
    denominator_sum_a = 0
    denominator_sum_b = 0

    # compute adjusted cosine similarity
    for user in item_a_ratings:
        if user in item_b_ratings:
            user_mean = dm_ch2.mean(users_ratings[user])
            a = item_a_ratings[user] - user_mean
            b = item_b_ratings[user] - user_mean
            numerator_sum += a*b
            denominator_sum_a += a*a
            denominator_sum_b += b*b

    return round(numerator_sum/((denominator_sum_a**0.5)*(denominator_sum_b**0.5)),5)

def prob_user_rate_item(user_name,item_name):
    pass

def change_rating_scale(old_min,old_max,new_min,new_max,rate):
    return ((rate-old_min)/(old_max-old_min))*(new_max-new_min)+new_min

