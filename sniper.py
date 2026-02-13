import requests
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime, timedelta

USER = "sniperimmobilier"
TOKEN = "SECRET_TOKEN"
DUREE_VALIDITE = 48 
base_donnees_opportunites = []

def publier_sur_github():
    print("🚀 Publication sur le site internet...")
    os.chdir(os.path.expanduser("~/Desktop/SNIPER_IMMO"))
    os.system("git add index.html")
    os.system('git commit -m "Mise a jour automatique"')
    os.system("git push origin main")

def generer_page_web(opportunites):
    chemin_html = os.path.expanduser("~/Desktop/SNIPER_IMMO/index.html")
    html_content = f"<html><head><meta charset='UTF-8'><title>Sniper Immo</title></head><body style='background:#1a1a1a;color:white;font-family:sans-serif;text-align:center;'><h1>🎯 OFFRES BOUINAN</h1>"
    for opp in opportunites:
        html_content += f"<div style='background:#2c3e50;margin:10px;padding:15px;border-radius:10px;'><h3>{opp['Titre']}</h3><a href='{opp['Lien']}' style='color:#e74c3c;'>VOIR L'OFFRE</a></div>"
    html_content += "</body></html>"
    with open(chemin_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✨ Site local mis à jour ({len(opportunites)} annonces).")

def scanner():
    global base_donnees_opportunites
    print(f"🔍 Scan en cours...")
    try:
        r = requests.get("https://www.lkeria.com/vente-encheres-immobilier", timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        maintenant = datetime.now()
        for a in soup.find_all('a'):
            txt = a.get_text().strip()
            if any(m in txt.lower() for m in ["enchère", "bouinan", "saisie"]):
                if not any(o['Titre'] == txt for o in base_donnees_opportunites):
                    lien = a.get('href')
                    if lien and not lien.startswith('http'): lien = "https://www.lkeria.com" + lien
                    base_donnees_opportunites.append({"Titre": txt, "Lien": lien, "Objet_Date": maintenant})
        generer_page_web(base_donnees_opportunites)
        publier_sur_github()
    except Exception as e: print(f"Erreur : {e}")

while True:
    scanner()
    print("⌛ En veille 30 min...")
    time.sleep(1800)
