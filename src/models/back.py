import pandas as pd
import ast
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("dataset/movies_metadata.csv")

def KNN(x):
    
  
    ind = 0
    for i,name in enumerate(df['title']):
        if df['title'][i] == x:
            ind = i
            break
    def get_genres_list(genres_str):
        if pd.isna(genres_str) or genres_str == '[]':
            return []
        return [g['name'] for g in ast.literal_eval(genres_str)]

    df['genres_list'] = df['genres'].apply(get_genres_list)
    all_genres = sorted(list(set([genre for sublist in df['genres_list'] for genre in sublist])))
    df_new = df[['title', 'vote_average', 'vote_count', 'runtime', 'budget', 'revenue', 'genres_list']]
    df_new['genres_str'] = df_new['genres_list'].apply(lambda x: ', '.join(x))

    def genres_norm(l):
        temp = [0]*len(all_genres)
        for x in range(len(all_genres)):
            if all_genres[x] in l:
                temp[x] = 1
        return temp

    df_new['genres_vector'] = df_new['genres_list'].apply(genres_norm)
    df_new['budget'] = pd.to_numeric(df_new['budget'], errors='coerce')
    df_new['budget'] = df_new['budget'].astype(float)
    df_new = df_new.drop(['genres_list', 'genres_str'],axis =1)
    genres_matrix = np.array(df_new['genres_vector'].tolist())

    numeric_features = df_new[['vote_average', 'vote_count', 'runtime', 'budget', 'revenue']].values
    all_features = np.hstack([numeric_features, genres_matrix])
    print(all_features[0])
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('knn', NearestNeighbors(n_neighbors=5, metric='euclidean'))
    ])

    pipeline.fit(all_features)
    distances, indices = pipeline['knn'].kneighbors([pipeline['scaler'].transform([pipeline['imputer'].transform(all_features)[ind]])[0]])

    print("Indices vecinos:", indices)
    print("Distancias:", distances)
    res = []
    for x in indices:
            res.append(list((df_new['title'][x])+'----'))
    return res
