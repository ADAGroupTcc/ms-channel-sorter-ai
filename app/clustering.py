from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import pairwise_distances
from app.models import User
from typing import List
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def cluster_users(users: List[User], user_id: str) -> List[User]:
    users_to_cluster = [user for user in users]

    locations = np.array([user.location for user in users_to_cluster]) 

    categories = [set(cat for cat in user.categories) for user in users_to_cluster]
    
    if not categories or all(len(cat) == 0 for cat in categories):
        print(categories)
        raise ValueError("Categories are empty or not properly formatted.")
    
    mlb = MultiLabelBinarizer()
    encoded_categories = mlb.fit_transform(categories)

    if encoded_categories.shape[1] == 0:
        raise ValueError("Encoded categories array is empty.")
    
    category_distances = pairwise_distances(encoded_categories, metric="cosine")
    
    location_weight = 1
    category_weight = 1
    
    location_distances = np.linalg.norm(locations[:, np.newaxis] - locations, axis=2)

    scaler = MinMaxScaler()
    location_distances_scaled = scaler.fit_transform(location_distances)
    category_distances_scaled = scaler.fit_transform(category_distances)

    total_distances = location_weight * location_distances_scaled + category_weight * category_distances_scaled

    agg_clust = AgglomerativeClustering(n_clusters=10)
    clusters = agg_clust.fit_predict(total_distances)

    user_index = next(i for i, user in enumerate(users_to_cluster) if user.id == user_id)
    user_cluster = clusters[user_index]

    same_cluster_users = [user for i, user in enumerate(users_to_cluster) if clusters[i] == user_cluster]

    if len(same_cluster_users) < 4:
        if len(clusters) > 1:
            for i in range(len(users_to_cluster)):
                if len(same_cluster_users) >= 4:
                    break
                if clusters[i] != user_cluster:
                    same_cluster_users.append(users_to_cluster[i])

        selected_cluster = same_cluster_users[:4]
    else:
        if users_to_cluster[user_index] not in same_cluster_users[:4]:
            same_cluster_users.remove(users_to_cluster[user_index])
            same_cluster_users = [users_to_cluster[user_index]] + same_cluster_users[:3]
        selected_cluster = same_cluster_users[:4]

    return selected_cluster
