from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Charger le modèle
model = pickle.load(open("loan-predictor-model.pkl", "rb"))

def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Récupérer les données depuis le formulaire HTML
        customer_id = int(request.form.get("customer_id", 123456))  # Ajout d'un customer_id avec une valeur par défaut
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])
        loan_amt_outstanding = float(request.form["loan_amt_outstanding"])
        total_debt_outstanding = float(request.form["total_debt_outstanding"])
        income = float(request.form["income"])
        years_employed = int(request.form["years_employed"])
        fico_score = int(request.form["fico_score"])

        # Créer un dictionnaire des données avec customer_id
        features = {
            'customer_id': customer_id,  # Colonne ajoutée pour correspondre au nombre de colonnes attendu par le modèle
            'credit_lines_outstanding': credit_lines_outstanding,
            'loan_amt_outstanding': loan_amt_outstanding,
            'total_debt_outstanding': total_debt_outstanding,
            'income': income,
            'years_employed': years_employed,
            'fico_score': fico_score
        }

        # Faire la prédiction en utilisant le modèle chargé
        prediction = model_pred(features)

        # Afficher le résultat de la prédiction
        if prediction == 1:
            return render_template("index.html", prediction_text="Attention ! Le client est susceptible de faire défaut.")
        else:
            return render_template("index.html", prediction_text="Le client est peu susceptible de faire défaut.")

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
