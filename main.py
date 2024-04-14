import requests

# URL de l'API que vous souhaitez interroger
url = 'https://pokeapi.co/api/v2/pokemon/pikachu'

# Envoi d'une requête GET à l'URL spécifiée
response = requests.get(url)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    # Si la requête est réussie (code de statut 200), vous pouvez accéder au contenu de la réponse
    data = response.json()  # Convertir la réponse JSON en un objet Python
    print(data)  # Afficher les données de la réponse
else:
    # Si la requête échoue, afficher un message d'erreur avec le code de statut 404
    print('La requête a échoué avec le code de statut:', response.status_code)
