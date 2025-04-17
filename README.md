# 🗺️ Google Maps Reviews Scraper

This project is a **Python** script that uses **Selenium** to automatically scrape user reviews from a Google Maps page and save them into a CSV file.

## 🌟 Features

- Automated navigation to Google Maps locations
- Cookie consent bypass
- Automatic display and scrolling of all available reviews
- Expansion of truncated reviews ("More" button click)
- Extraction of reviewer name, review text, and rating
- Deduplication of reviews
- Export of results to a CSV file (`avis_data.csv`)

## 🚀 Quick Start

### 🛠️ Prerequisites

- Python 3.11
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KuriKhalil/py-maps.git
2. Install the required Python packages:
   ```bash
   pip install selenium


### 📂 Fichiers

- `maps.py` : Script principal de scraping
- `avis_data.csv` : Fichier généré contenant les avis les pseudonymes de ceux ayant laissé l'avis anisi que la note.
