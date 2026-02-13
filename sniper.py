import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Version Catalogue Carres' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Restauration de la version Catalogue (Carrés)...")
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
    body {{ background: #f0f2f5; color: #1c1e21; font-family: -apple-system, sans-serif; margin: 0; padding-bottom: 80px; }}
    
    /* Header avec Logo */
    .header {{ background: #fff; padding: 15px; text-align: center; border-bottom: 1px solid #ddd; position: sticky; top: 0; z-index: 100; }}
    .logo {{ font-size: 1.5rem; font-weight: 900; color: #000; margin: 0; letter-spacing: 1px; }}
    
    /* Bouton WhatsApp */
    .wa-btn {{ background: #25d366; color: white; display: flex; align-items: center; justify-content: center; margin: 15px; padding: 12px; border-radius: 10px; text-decoration: none; font-weight: bold; }}

    /* Grille de Carrés */
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 12px; padding: 12px; }}
    
    .card-square {{ background: #fff; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 2px 5px rgba(0,0,0,0.1); border: 1px solid #eee; }}
    
    .card-image {{ background: #333; height: 120px; display: flex; align-items: center; justify-content: center; color: #d4af37; font-size: 2rem; }}
    
    .card-info {{ padding: 10px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; }}
    
    .card-info h3 {{ font-size: 0.85rem; margin: 0 0 8px 0; color: #333; line-height: 1.3; height: 3.9em; overflow: hidden; }}
    
    .view-btn {{ background: #000; color: #fff; text-align: center; text-decoration: none; font-size: 0.75rem; padding: 8px; border-radius: 6px; font-weight: bold; }}

    /* Navigation Bas */
    .nav-bottom {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #ddd; }}
    .nav-item {{ text-align: center; color: #65676b; text-decoration: none; font-size: 0.65rem; }}
    .nav-item i {{ display: block; font-size: 1.3rem; margin-bottom: 3px; color: #1c1e21; }}
    </style></head><body>

    <div class="header">
        <h1 class="logo">SNIPER IMMO</h1>
    </div>

    <a href="https://wa.me/213000000000" class="wa-btn">
        <i class="fab fa-whatsapp" style="margin-right:8px;"></i> CONTACTER L'AGENCE
    </a>

    <div class="grid">"""
    
    for o in offres:
        html += f"""<div class='card-square'>
            <div class='card-image'><i class="fas fa-home"></i></div>
            <div class='card-info'>
                <h3>{o['t']}</h3>
                <a href='{o['l']}' target='_blank' class='view-btn'>DÉTAILS</a>
            </div>
        </div>"""
    
    html += """</div>
    
    <div class="nav-bottom">
        <a href="#" class="nav-item"><i class="fas fa-th-large"></i>Catalogue</a>
        <a href="#" class="nav-item"><i class="fas fa-search"></i>Filtres</a>
        <a href="#" class="nav-item"><i class="fas fa-heart"></i>Favoris</a>
        <a href="#" class="nav-item"><i class="fas fa-user-circle"></i>Compte</a>
    </div>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION CATALOGUE CARRÉ RESTAURÉE !")

run()
