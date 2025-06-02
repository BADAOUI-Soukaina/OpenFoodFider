from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- AJOUTEZ CETTE LIGNE
from recommender_model import recommend_by_each_ingredient

app = Flask(__name__)
CORS(app)  # <-- AJOUTEZ CETTE LIGNE JUSTE APRÈS LA CRÉATION DE L'APP

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    ingredients_raw = data.get("ingredients", "") # Récupérez la chaîne brute
    # Split la chaîne en liste d'ingrédients
    # Gérer les guillemets et les espaces autour des éléments
    ingredients = [ing.strip().strip('"\'') for ing in ingredients_raw.split(',') if ing.strip()]

    # Récupérer les valeurs des filtres, en s'assurant de gérer les cas où ils sont "Pays", "nutriscore", etc.
    # ou des chaînes vides si rien n'est sélectionné.
    country_filter = data.get("country")
    nutriscore_filter = data.get("nutriscore")
    nova_group_filter = data.get("nova_group")

    filters = {}
    if country_filter and country_filter != "Pays": # Éviter d'envoyer "Pays" comme filtre
        filters["countries_en"] = country_filter
    if nutriscore_filter and nutriscore_filter != "nutriscore": # Éviter d'envoyer "nutriscore" comme filtre
        filters["nutriscore_grade"] = nutriscore_filter
    if nova_group_filter and nova_group_filter != "nova_group": # Éviter d'envoyer "nova_group" comme filtre
        filters["nova_group"] = nova_group_filter

    top_k = data.get("top_k", 5) # Ce champ n'est pas envoyé par votre frontend actuel, mais c'est bien de le garder

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    try:
        # Assurez-vous que les clés des filtres correspondent aux noms de colonnes dans votre DataFrame
        recommendations = recommend_by_each_ingredient(ingredients, filters, top_k)

        # Ajustez les colonnes retournées si nécessaire
        # `nutriscore_grade` et `countries_en` semblent corrects d'après votre `recommender_model.py` et le nom de colonne attendu
        results = recommendations[["product_name", "matched_ingredient", "nutriscore_grade", "countries_en", "brands"]].to_dict(orient="records") # Ajout de 'brands' ici pour l'affichage frontend

        return jsonify({"recommendations": results}) # Encapsulez la liste dans une clé 'recommendations'
    except Exception as e:
        # Imprimez l'erreur dans la console du serveur pour un meilleur débogage
        print(f"Error during recommendation: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Spécifiez explicitement le port