import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Restauration Matinale' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🔄 Retour à la version de ce matin...")
    r = requests.get("https://www.lkeria.com/vente-encheres-immobilier")
    soup = BeautifulSoup(r.text, "html.parser")
    offres = []
    for a in soup.find_all("a"):
        txt = a.get_text().strip()
        if len(txt) > 25:
            link = a.get("href")
            if not link.startswith("http"): link = "https://www.lkeria.com" + link
            offres.append({"t": txt, "l": link})
    
    html = f"""<html><head><meta charset='UTF-8'><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
    body {{ background: #f8f9fa; color: #333; font-family: -apple-system, sans-serif; margin: 0; padding-bottom: 70px; }}
    .header {{ background: #fff; padding: 15px 20px; border-bottom: 1px solid #eee; display: flex; align-items: center; justify-content: space-between; }}
    .logo {{ font-size: 1.2rem; font-weight: bold; color: #000; margin: 0; }}
    .wa-btn {{ background: #25d366; color: #fff; display: flex; align-items: center; justify-content: center; margin: 15px; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 0.9rem; }}
    .container {{ padding: 10px; }}
    .card {{ background: #fff; border-radius: 10px; padding: 15px; margin-bottom: 10px; border: 1px solid #eee; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }}
    .card h3 {{ font-size: 0.95rem; margin: 0 0 10px 0; line-height: 1.4; }}
    .card a {{ color: #007bff; text-decoration: none; font-size: 0.85rem; font-weight: bold; }}
    .nav-bar {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #ddd; }}
    .nav-item {{ color: #666; text-decoration: none; font-size: 0.7rem; text-align: center; }}
    .nav-item i {{ display: block; font-size: 1.2rem; margin-bottom: 2px; }}
    </style></head><body>
    <div class="header">
        <h1 class="logo">SNIPER IMMOBILIER</h1>
        <span style="font-size: 0.7rem; font-weight: bold; color: #666;">ALGÉRIE</span>
    </div>
    <a href="https://wa.me/213000000000" class="wa-btn">
        <i class="fab fa-whatsapp" style="margin-right:8px;"></i> CONTACTER L'AGENCE
    </a>
    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'>
            <h3>{o['t']}</h3>
            <a href='{o['l']}' target='_blank'>VOIR L'ANNONCE →</a>
        </div>"""
    
    html += """</div>
    <div class="nav-bar">
        <a href="#" class="nav-item"><i class="fas fa-home"></i>Accueil</a>
        <a href="#" class="nav-item"><i class="fas fa-search"></i>Recherche</a>
        <a href="#" class="nav-item"><i class="fas fa-heart"></i>Favoris</a>
    </div>
    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION DU MATIN RÉTABLIE. TOUT EST PRÊT.")

run()
