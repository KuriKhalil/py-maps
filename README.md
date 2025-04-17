# py-maps
## 🗺️ Google Maps Reviews Scraper

Ce projet permet d'automatiser la récupération des avis sur une page Google Maps à l'aide de **Selenium** et **Python**. Les données extraites (nom de l'auteur, avis, note) sont ensuite enregistrées dans un fichier CSV.

### 🚀 Fonctionnalités

- Refus automatique des cookies
- Affichage de tous les avis disponibles
- Scroll automatique de la liste d'avis
- Dépliage des textes tronqués ("Plus")
- Suppression des doublons
- Export en CSV

### 📂 Fichiers

- `maps.py` : Script principal de scraping
- `avis_data.csv` : Fichier généré contenant les avis les pseudonymes de ceux ayant laissé l'avis anisi que la note.

### 🛠️ Prérequis

- Python 3.11
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
