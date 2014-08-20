import math

#this file contains functions needed to perform data analysis
#functions are coded for creator's understanding purpose
#list of functions includes

#this chapter introduce user-based filtering, to find nearest neighbour
#Pros : effective, by finding most similar users, we can deduce they would have similar preference
#Cons : Not good in handling sparse data, as sometime it cannot find similar user
#       Scalability is low as for every new rating, user or item, the similarity need to be compute again

# Similarity measure
    # 1. manhattan_distance(dict, dict)
    # 2. euclidean_distance(dict dict)
    # 3. pearson_correlation_coefficient(dict,dict)
    # 4. cosine_similarity(dict,dict)
    # 5. minkowski_distance(dict,dict,r)

# Helper functions
    # 1. find_common_keys(dict, dict)
    # 2. covariance(dict,dict)
    # 3. mean(dict)
    # 4. standard_deviation(dict)

def manhattan_distance(dict_a, dict_b):
    """Compute Manhattan distance.

    Pre-condition : dict_a and dict_b are dictionary
    Post-condition : distance between 2 dictionaries are returned, non-negative"""

    m_distance = 0

    for key in dict_a:
        if key in dict_b:
            m_distance += abs(dict_a[key]-dict_b[key])


    return m_distance


def euclidean_distance(dict_a, dict_b):
    """Compute Euclidean distance.

    Pre-condition : dict_a and dict_b are dictionary
    Post-condition : distance between 2 dictionaries are returned, non-negative
    """

    m_distance = 0

    for key in dict_a:
        if key in dict_b:
            m_distance += abs(dict_a[key]-dict_b[key])**2



    return math.sqrt(m_distance)

def minkowski_distance(dict_a, dict_b, r):
    """compute Minkowski distance

    Pre-condition : dict_a and dict_b are dictionary
    Post-condition : distance between 2 dictionaries are returned, non-negative
    """
    m_distance = 0

    for key in dict_a:
        if key in dict_b:
            m_distance += abs(dict_a[key]-dict_b[key])**r

    return m_distance**(1/r)

def mean(dict_a):
    """compute average mean

    Pre-condition : all values of dict_a is non-null
    Post-condition : mean is returned"""

    sum = 0

    for key in dict_a:
        if dict_a[key] != None:
            sum += dict_a[key]

    return sum/len(dict_a)

def standard_deviation(dict_a):
    """
    Pre-condition : dict_a is of type dictionary, all values is non-null
    Post-condition : return standard_deviation, non-negative
    """
    sum = 0
    m = mean(dict_a)

    for key in dict_a:
        sum += (dict_a[key]-m)**2


    return (sum/len(dict_a))**0.5

def covariance(dict_a, dict_b):
    """
    Pre-condition : dict_a is of type dictionary, all values is non-null
    Post-condition : return covariance, non-negative
    """
    xmean = mean(dict_a)
    ymean = mean(dict_b)
    sum = 0

    for key in dict_a:
        if key in dict_b:
            sum += ((dict_a[key]-xmean)*(dict_b[key]-ymean))


    return sum/len(dict_a)

def pearson_correlation_coefficient(dict_a, dict_b):
    """Compute strength of correlation between 2 set of data.

    Pre-condition : 2 dictionary must not have zero-values
    Post-condition : strength of correlation is returned, not bigger than 1 and not lesser than -1
    """

    return covariance(dict_a, dict_b)/(standard_deviation(dict_a)*standard_deviation(dict_b))

def dot_product(x, y):
    """
    Pre-condition : 2 dictionary with same keys are passed in
    Post-condition : dot_product is return
    """
    if len(x) != len(y):
        return None

    else:
        sum = 0
        for key in x:
            sum += x[key]*y[key]

        return sum

def magnitude(x):
    """
    Pre-condition : data passed in is dictionary type
    Post-condition : magnitude is return, non-negative
    """
    sum = 0
    for key in x:
        sum += x[key]**2

    return sum**0.5

def cosine_similarity(dict_a, dict_b):
    """
    compute similarity where it is not affected by zero-values
    Pre-condition :
    """
    return dot_product(dict_a,dict_b)/(magnitude(dict_a)*magnitude(dict_b))

def k_nearest_neighbour(k,similarity_index,user,*all_user):
    """computer k nearest neighbour
    Pre-condition : k is positive int, similarity_index is string, user is a user's rating, and the rest will be other users' rating
    Post-condition : return a list of neighbour
    """

    similarity_indexes = {
        "manhattandistance":manhattan_distance,
        "euclideandistance":euclidean_distance,
        "pearsoncorrelationcoefficient":pearson_correlation_coefficient,
        "cosinesimilarity":cosine_similarity
        }
    s_index = similarity_indexes["".join(similarity_index.split())]
    knearest = []

    for u in all_user:
        s = s_index(user,u)
        knearest.append((u,s))
        knearest.sort()
        knearest = knearest[:k]

    return knearest

def recommend(no,similarity_index,user,*all_user):
    """
    give recommendations of entity, can be anything depends on data insert
    Pre-condition : all user are comparable, having same key, and using same rating scheme, eg. 0-10 or 0-5
    Post-condition : a list of recommendations are returned
    """
    k = 3
    k_nearest = k_nearest_neighbour(k,similarity_index,user,all_user)

    recommendations = {}

    for i in range(k):
        ratings = k_nearest[i][0]
        for key,val in ratings.items():
            if key not in recommendations.keys():
                recommendations[key] = val
            else:
                recommendations[key] += val


    return sorted(recommendations.items(),key=lambda x: x[1])


def adjusted_cosine_similarity(dict_a,dict_b, users_rating):
    """
    compute adjusted cosine similarity which not affected by grade inflation

    Pre-condition : users_rating is a dict of dict with username as key, and ratings as values
                    dict_a and dict_b is ratings of items by different user
    Post-condition : a similarity range from -1 to 1 is return
    """

    average = {}
    for key in users_rating:
        average[key] = sum(users_rating[key].values())/len(users_rating[key])

    adjusted_dicta = {key: value-average[key] for key,value in dict_a}
    adjusted_dictb = {key: value-average[key] for key,value in dict_b}

    return cosine_similarity(adjusted_dicta,adjusted_dictb)
