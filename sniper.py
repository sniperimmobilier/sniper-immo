import requests
from bs4 import BeautifulSoup
import time
import os

TOKEN = "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"

def publier():
    os.chdir(os.path.expanduser("~/Desktop/SNIPER_IMMO"))
    os.system("git add index.html sniper.py")
    os.system("git commit -m 'Full Brand Experience'")
    os.system(f"git push -f https://{TOKEN}@github.com/sniperimmobilier/sniper-immo.git main")

def generer_page(annonces):
    chemin = os.path.expanduser("~/Desktop/SNIPER_IMMO/index.html")
    html = f"""<html><head><meta charset="UTF-8"><style>
    body {{ background: #0a0a0a; color: #fff; font-family: -apple-system, sans-serif; margin: 0; padding: 0; scroll-behavior: smooth; }}
    .hero {{ height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border-bottom: 1px solid #333; }}
    .logo {{ font-size: 15vw; font-weight: 900; letter-spacing: -10px; line-height: 0.8; margin: 0; }}
    .count {{ color: #ef4444; font-size: 1.5rem; margin-top: 20px; font-weight: bold; letter-spacing: 5px; }}
    .container {{ max-width: 800px; margin: 2cm auto 100px auto; padding: 0 20px; }}
    .card {{ background: #141414; border-radius: 12px; padding: 30px; margin-bottom: 30px; border-left: 8px solid #ef4444; }}
    .card h3 {{ font-size: 1.4rem; margin: 0 0 20px 0; }}
    .btn {{ display: inline-block; color: #ef4444; text-decoration: none; font-weight: bold; border: 2px solid #ef4444; padding: 12px 30px; border-radius: 8px; }}
    </style></head><body>
    <div class="hero">
        <h1 class="logo">SNIPER</h1>
        <div class="count">{len(annonces)} CIBLES DÉTECTÉES</div>
        <p style="margin-top:50px; color:#444; letter-spacing: 2px;">SCROLLEZ ↓</p>
    </div>
    <div class="container">"""
    for a in annonces:
        html += f"<div class='card'><h3>{a['t']}</h3><a href='{a['l']}' target='_blank' class='btn'>VOIR L’OFFRE</a></div>"
    html += "</div></body></html>"
    with open(chemin, "w", encoding="utf-8") as f: f.write(html)

def run():
    print("🎯 Scan en cours et mise à jour du design...")
    try:
        r = requests.get("https://www.lkeria.com/vente-encheres-immobilier", timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        offres = []
        for a in soup.find_all("a"):
            txt = a.get_text().strip()
            if len(txt) > 25:
                link = a.get("href")
                if link and not link.startswith("http"): link = "https://www.lkeria.com" + link
                offres.append({"t": txt, "l": link})
        generer_page(offres[:15])
        publier()
        print("✅ Site déployé ! Rafraîchis ton navigateur.")
    except Exception as e: print(f"Erreur : {e}")

while True:
    run()
    time.sleep(1800)
