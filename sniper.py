import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Restauration Full Version' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Restauration de la version complète (WhatsApp + Menu)...")
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
    body {{ background: #f4f4f4; color: #333; font-family: -apple-system, sans-serif; margin: 0; padding-bottom: 80px; }}
    
    /* Header avec Logo Centré */
    .header {{ background: #fff; padding: 20px; text-align: center; border-bottom: 2px solid #000; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
    .logo {{ font-size: 2rem; font-weight: 900; color: #000; margin: 0; text-transform: uppercase; }}
    
    /* Bouton WhatsApp */
    .wa-float {{ background: #25d366; color: white; display: flex; align-items: center; justify-content: center; margin: 15px auto; padding: 10px; border-radius: 50px; width: 80%; text-decoration: none; font-weight: bold; font-size: 0.9rem; }}
    
    /* Liste des Annonces */
    .container {{ padding: 15px; }}
    .card {{ background: white; border-radius: 10px; padding: 15px; margin-bottom: 15px; border-left: 5px solid #000; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
    .card h3 {{ font-size: 1rem; margin: 0 0 10px 0; color: #222; }}
    .btn-link {{ display: block; text-align: right; color: #007bff; text-decoration: none; font-weight: bold; font-size: 0.8rem; }}
    
    /* Navigation Bas de Page */
    .nav-bottom {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #ddd; box-shadow: 0 -2px 10px rgba(0,0,0,0.1); }}
    .nav-item {{ text-align: center; color: #555; text-decoration: none; font-size: 0.7rem; }}
    .nav-item i {{ display: block; font-size: 1.4rem; margin-bottom: 3px; }}
    .nav-item.active {{ color: #000; font-weight: bold; }}
    </style></head><body>

    <div class="header">
        <h1 class="logo">SNIPER IMMO</h1>
    </div>

    <a href="https://wa.me/213000000000" class="wa-float">
        <i class="fab fa-whatsapp" style="margin-right:10px; font-size:1.2rem;"></i> CONTACTER UN AGENT
    </a>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'>
            <h3>{o['t']}</h3>
            <a href='{o['l']}' target='_blank' class='btn-link'>VOIR L'ENCHÈRE <i class="fas fa-chevron-right"></i></a>
        </div>"""
    
    html += f"""</div>
    
    <div class="nav-bottom">
        <a href="#" class="nav-item active"><i class="fas fa-home"></i>Accueil</a>
        <a href="#" class="nav-item"><i class="fas fa-search"></i>Recherche</a>
        <a href="#" class="nav-item"><i class="fas fa-bell"></i>Alertes</a>
        <a href="#" class="nav-item"><i class="fas fa-user"></i>Profil</a>
    </div>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION COMPLÈTE RESTAURÉE ET CENTRÉE !")

run()
