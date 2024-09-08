from app import model_pred

# Nouveau jeu de données avec toutes les variables nécessaires, y compris 'customer_id'
new_data = {
    'customer_id': 123456,  # Ajout de 'customer_id' pour correspondre aux données d'entraînement
    'credit_lines_outstanding': 5,
    'loan_amt_outstanding': 1958.928726,
    'total_debt_outstanding': 8228.75252,
    'income': 26648.43525,
    'years_employed': 2,
    'fico_score': 572
}

def test_predict():
    # Appel de la fonction de prédiction avec les nouvelles données
    prediction = model_pred(new_data)
    
    # Vérification du résultat attendu
    assert prediction in [0, 1], "La prédiction doit être 0 ou 1"
