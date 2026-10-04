```markdown
## Créer un environnement virtuel

```bash
python -m venv .venv
```

Activer :

### Windows PowerShell
```bash
.\.venv\Scripts\activate
```

### macOS / Linux
```bash
source .venv/bin/activate
```

---

## 📦Installer les dépendances

```bash
pip install -r requirements.txt
```

Pour régénérer ce fichier :

```bash
pip freeze > requirements.txt
```

---

## 🗄️ Créer la base de données

```bash
python manage.py migrate
```

---

## ▶️ Lancer le serveur

```bash
python manage.py runserver
```

Puis ouvrir :  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📁 Structure du projet

```
form-etape2/
    manage.py
    form/
        settings.py
        urls.py
        wsgi.py
        asgi.py
    myapp/
        models.py
        forms.py
        views.py
        urls.py
        templates/
            myapp/
                person_list.html
                person_create.html
```

---

## 🧩 Code pédagogique — Étape 2

### Formulaire Django

```python
class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
```

### Vue

```python
form = PersonForm(request.POST)
if form.is_valid():
    Person.objects.create(**form.cleaned_data)
```

### Avantages par rapport à l’étape 1

- plus besoin d’écrire les `<input>` à la main  
- validation automatique  
- gestion des erreurs intégrée  
- code plus court  
- données validées via `cleaned_data`

---

## ❗ Fichiers ignorés

Le `.gitignore` exclut :

- `.venv/`
- `db.sqlite3`
- `__pycache__/`
- fichiers temporaires
- fichiers système

---

## 📝 Notes

Cette étape prépare la transition vers :

- **Étape 3 : ModelForm**  
- **Étape 4 : Generic Views**
```
