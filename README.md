# 5BDDD

Projet pour utilisation de _FastAPI_


## Installation
Lien documentation : https://fastapi.tiangolo.com/virtual-environments ou https://docs.python.org/3/library/venv.html

```bash
# Création environnement virtuel & activation
python3 -m venv venv
.\venv\Scripts\activate
# Installation librairies listées dans 'requirements.txt'
pip install -r requirements.txt
pip freeze
```
Desactivation de l'environnement virtuel (si besoin)
```bash
deactivate
```

## Demarrage application
```bash
fastapi dev main.py
````
Accès au swagger sur http://127.0.0.1:8000/docs
Accès à la page index : http://127.0.0.1:8000/static/index.html