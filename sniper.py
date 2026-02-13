import requests
from bs4 import BeautifulSoup
import time
import os

def publier_sur_github():
    print("🚀 Publication sur le site internet...")
    os.chdir(os.path.expanduser("~/Desktop/SNIPER_IMMO"))
    os.system("git add index.html sniper.py")
    os.system('git commit -m "Mise a jour automatique"')
    os.system("git push -f origin main")

def generer_page_web(opportunites):
    chemin_html = os.path.expanduser("~/Desktop/SNIPER_IMMO/index.html")
    html_content = f"<html><head><meta charset='UTF-8'><title>Sniper Immo</title></head><body style='background:#1a1a1a;color:white;font-family:sans-serif;text-align:center;'><h1>🎯 SNIPER IMMO : DERNIÈRES OPPORTUNITÉS</h1>"
    if not opportunites:
        html_content += "<p>Recherche en cours sur Lkeria... Revenez dans quelques minutes.</p>"
    for opp in opportunites:
        html_content += f"<div style='background:#2c3e50;margin:10px;padding:15px;border-radius:10px;'><h3>{opp['Titre']}</h3><a href='{opp['Lien']}' target='_blank' style='color:#e74c3c;'>VOIR L'OFFRE</a></div>"
    html_content += "</body></html>"
    with open(chemin_html, "w", encoding="utf-8") as f: f.write(html_content)
    print(f"✨ Site local mis à jour ({len(opportunites)} annonces).")

def scanner():
    print(f"🔍 Scan en cours...")
    opps = []
    try:
        r = requests.get("https://www.lkeria.com/vente-encheres-immobilier", timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        # On prend les 10 premières annonces d'enchères, peu importe la ville, pour remplir le site
        links = soup.find_all('a')
        for a in links:
            txt = a.get_text().strip()
            if len(txt) > 20 and ("enchère" in txt.lower() or "saisie" in txt.lower() or "appartement" in txt.lower()):
                lien = a.get('href')
                if lien and not lien.startswith('http'): lien = "https://www.lkeria.com" + lien
                if {"Titre": txt, "Lien": lien} not in opps:
                    opps.append({"Titre": txt, "Lien": lien})
                if len(opps) >= 15: break
        generer_page_web(opps)
        publier_sur_github()
    except Exception as e: print(f"Erreur : {e}")

while True:
    scanner()
    print("⌛ En veille 30 min...")
    time.sleep(1800)
