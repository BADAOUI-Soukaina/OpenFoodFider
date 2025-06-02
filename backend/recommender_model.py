import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Charger les données et le modèle
df_pandas = pd.read_csv("C:/Users/Lamar/Desktop/TDIA2 - S2/Big DATA/sysrecomm/backend/data/open_food_facts_cleaned.csv")
vectorizer = joblib.load("C:/Users/Lamar/Desktop/TDIA2 - S2/Big DATA/sysrecomm/backend/data/model1.pkl")

def recommend_by_each_ingredient(ingredients_list, filters={}, top_k=5):
    results = []
    for ingredient in ingredients_list:
        sub_df = df_pandas.copy()
        for key, value in filters.items():
            if value:
                sub_df = sub_df[sub_df[key].astype(str).str.contains(str(value), case=False, na=False)]
        input_vec = vectorizer.transform([ingredient])
        tfidf_sub = vectorizer.transform(sub_df["ingredients_text"])
        similarities = cosine_similarity(input_vec, tfidf_sub).flatten()
        top_indices = similarities.argsort()[::-1][:top_k]
        top_products = sub_df.iloc[top_indices].copy()
        top_products["matched_ingredient"] = ingredient
        results.append(top_products)
    return pd.concat(results)
