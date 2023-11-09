def cosine_similarity(ratings, user_similarity):
    num_users, num_items = ratings.shape
    item_similarity = np.zeros((num_items, num_items))
    
    for i in range(num_items):
        for j in range(num_items):
            numerator = np.sum(user_similarity**2 * ratings[:, i] * ratings[:, j])
            denominator = np.sqrt(np.sum((user_similarity * ratings[:, i])**2) * np.sum((user_similarity * ratings[:, j])**2))
            
            item_similarity[i][j] = numerator / denominator if denominator != 0 else 0
    return item_similarity
