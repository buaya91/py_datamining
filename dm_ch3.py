
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
    item_a_ratings = get_list_from_table(item_a_name,users_ratings)
    item_b_ratings = get_list_from_table(item_b_name,users_ratings)

    ##
    ##    for u_name in users_ratings:
    ##        for i_name in users_ratings[u_name]:
    ##            if users_ratings[u_name][i_name] != None:
    ##                if i_name == item_a_name:
    ##                    item_a_ratings[u_name] = users_ratings[u_name][i_name]
    ##                if i_name == item_b_name:
    ##                    item_b_ratings[u_name] = users_ratings[u_name][i_name]


    numerator_sum = 0
    denominator_sum_a = 0
    denominator_sum_b = 0

    # compute adjusted cosine similarity
    for user in item_a_ratings:
        if (user in item_b_ratings and item_a_ratings[user] != None
                                    and item_b_ratings[user] != None):
            user_mean = dm_ch2.mean(users_ratings[user])
            a = item_a_ratings[user] - user_mean
            b = item_b_ratings[user] - user_mean
            numerator_sum += a*b
            denominator_sum_a += a*a
            denominator_sum_b += b*b

    return round(numerator_sum/((denominator_sum_a**0.5)*(denominator_sum_b**0.5)),5)

def prob_user_rate_item(user_name,item_name,users_ratings):
    """
    Pre-condition :
        user_name is string of username
        item_name is string of itemname
        user_ratings is dict containing item:ratings pair of username
    Post-condition :
        return expected rating for username to item
    """
    if users_ratings[user_name][item_name] != None:
        print('item already rated by user')
        return

    numerator_sum = 0
    denominator_sum = 0
    for item in users_ratings[user_name]:
        if users_ratings[user_name][item] != None:
            similarity = adjusted_cosine_similarity(item,item_name,users_ratings)
            numerator_sum += (similarity*
                change_rating_scale(1,5,-1,1,users_ratings[user_name][item]))
            denominator_sum += abs(similarity)


    return change_rating_scale(-1,1,1,5,numerator_sum/denominator_sum)

def change_rating_scale(old_min,old_max,new_min,new_max,rating):
    """
    change rating scale
    Pre-condition :
        old_min must be smaller than old_max
        new_min must be smaller than new_max
        rating must between old_min and old_max
    Post-condition :
        return the modified rating
    """
    rounded_new_rating = round((((rating-old_min)/(old_max-old_min))*(new_max-new_min)+new_min),5)
    return rounded_new_rating

def get_list_from_table(key,users_ratings):
    """
    Pre-condition :
        key is the name of col we want
        users_ratings is a 2-dimension data consisting username as row and item as column, with rating as data

        key should only either appear in row or col, but not both
    """
    d = dict()
    for i in users_ratings:
        if i == key:
            d = users_ratings[i]
            return d
        for j in users_ratings[i]:
            if j == key:
                d[i] = users_ratings[i][j]
                break
    return d



def compute_deviation_from_a_to_b(item_a,item_b,users_ratings):
    """
    compute deviation of 2 items by finding the difference of ratings on both
    items by different user, and compute its average

    Pre-condition :
        item a and b is name of item we want to compute deviation
        users_ratings is 2D data consist all users' rating on all items
    Post-condition :
        return deviation between a and b

    """

    item_a_ratings = get_list_from_table(item_a,users_ratings)
    item_b_ratings = get_list_from_table(item_b,users_ratings)
    no_user_rated_both = 0
    sum_of_deviation = 0

    for user in item_a_ratings:
        if (item_a_ratings[user] != None
            and item_b_ratings[user] != None):
            no_user_rated_both += no_user_rated_both+1
            sum_of_deviation += item_a_ratings[user] - item_b_ratings[user]

    return round(sum_of_deviation/no_user_rated_both,2)

