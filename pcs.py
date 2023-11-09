def pearson_correlation_similarity(ratings, user_similarity):
    num_users, num_items = ratings.shape
    mean_user_ratings = ratings.mean(axis=1)
    item_similarity = np.zeros((num_items, num_items))
    
    for i in range(num_items):
        for j in range(num_items):
            adjusted_ratings_i = ratings[:, i] - mean_user_ratings
            adjusted_ratings_j = ratings[:, j] - mean_user_ratings
            
            numerator = np.sum(user_similarity**2 * adjusted_ratings_i * adjusted_ratings_j)
            denominator = np.sqrt(np.sum((user_similarity * adjusted_ratings_i)**2) * np.sum((user_similarity * adjusted_ratings_j)**2))
            
            item_similarity[i][j] = numerator / denominator if denominator != 0 else 0
    return item_similarity
