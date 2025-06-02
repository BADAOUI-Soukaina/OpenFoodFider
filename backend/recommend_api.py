from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Charger les modèles ou données prétraitées ici
# Exemple : model = joblib.load("recommender_model.pkl")

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    ingredients = data.get('ingredients', '')
    country = data.get('country', '')
    nutriscore = data.get('nutriscore', '')
    nova_group = data.get('nova_group', '')

    # Appelle ici ta fonction de recommandation, ex :
    # recommendations = recommend_products(ingredients, country, nutriscore, nova_group)

    # Pour tester : retourner des données simulées
    recommendations = [
        {"product_name": "Tomato Sauce", "score": 0.91},
        {"product_name": "Basil Pesto", "score": 0.87},
    ]

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
