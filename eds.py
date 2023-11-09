def euclidean_distance_similarity(ratings, user_similarity):
    num_users, num_items = ratings.shape
    item_similarity = np.zeros((num_items, num_items))
    
    for i in range(num_items):
        for j in range(num_items):
            squared_difference = np.sum((user_similarity * (ratings[:, i] - ratings[:, j]))**2)
            item_similarity[i][j] = 1 / (1 + np.sqrt(squared_difference))
    return item_similarity
