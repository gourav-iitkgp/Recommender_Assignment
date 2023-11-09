import numpy as np

def adjusted_cosine_similarity(ratings, user_similarity):
    num_users, num_items = ratings.shape
    mean_user_ratings = ratings.mean(axis=1)
    
    # Create a zero-filled matrix for the item similarities
    item_similarity = np.zeros((num_items, num_items))
    
    for i in range(num_items):
        for j in range(num_items):
            if i != j:
                # Extract ratings for items i and j
                ratings_i = ratings[:, i]
                ratings_j = ratings[:, j]

                # Calculate the adjusted ratings
                adjusted_ratings_i = ratings_i - mean_user_ratings
                adjusted_ratings_j = ratings_j - mean_user_ratings

                # Calculate the similarity
                numerator = np.sum(user_similarity * adjusted_ratings_i * adjusted_ratings_j)
                denominator = np.sqrt(np.sum(user_similarity * adjusted_ratings_i ** 2) * np.sum(user_similarity * adjusted_ratings_j ** 2))
                
                item_similarity[i][j] = numerator / denominator if denominator != 0 else 0
    return item_similarity
