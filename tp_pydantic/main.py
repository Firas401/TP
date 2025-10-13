
from models import User
from pydantic import ValidationError

# Exemple valide
user = User(name="Salah", email="salah@gmail.com", account_id=12345)
print("✅ Utilisateur valide :", user)
print("Dictionnaire :", user.model_dump())
print("JSON :", user.model_dump_json())

# Exemple invalide
try:
    bad_user = User(name="amin", email="Amin", account_id=-12)
except ValidationError as e:
    print("\n❌ Erreur de validation détectée :")
    print(e)

json_str = '{"name":"amin","email":"aminnajjar3@gmail.com","account_id":1234}'
u2 = User.model_validate_json(json_str)
print("\n🧩 Objet créé à partir de JSON :", u2)

