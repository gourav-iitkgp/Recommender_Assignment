def spearman_correlation_similarity(ratings, user_similarity):
    num_users, num_items = ratings.shape
    ranks = np.apply_along_axis(rankdata, 0, ratings)
    mean_ranks = ranks.mean(axis=1)
    item_similarity = np.zeros((num_items, num_items))
    
    for i in range(num_items):
        for j in range(num_items):
            adjusted_ranks_i = ranks[:, i] - mean_ranks
            adjusted_ranks_j = ranks[:, j] - mean_ranks
            
            numerator = np.sum(user_similarity**2 * adjusted_ranks_i * adjusted_ranks_j)
            denominator = np.sqrt(np.sum((user_similarity * adjusted_ranks_i)**2) * np.sum((user_similarity * adjusted_ranks_j)**2))
            
            item_similarity[i][j] = numerator / denominator if denominator != 0 else 0
    return item_similarity
