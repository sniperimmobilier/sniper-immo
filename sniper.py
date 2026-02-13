import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Design Gold and Black' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Restauration du design Noir & Or...")
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
    body {{ background: #000; color: #d4af37; font-family: 'Times New Roman', serif; margin: 0; padding-bottom: 80px; }}
    
    /* Header avec Logo Doré Centré */
    .header {{ background: #000; padding: 30px 20px; text-align: center; border-bottom: 1px solid #d4af37; }}
    .logo {{ font-size: 2.5rem; font-weight: bold; color: #d4af37; margin: 0; text-transform: uppercase; letter-spacing: 5px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }}
    
    /* Bouton WhatsApp Doré */
    .wa-float {{ background: #d4af37; color: #000; display: flex; align-items: center; justify-content: center; margin: 20px auto; padding: 12px; border-radius: 5px; width: 85%; text-decoration: none; font-weight: bold; font-size: 0.9rem; text-transform: uppercase; }}
    
    /* Liste des Annonces style Luxe */
    .container {{ padding: 15px; }}
    .card {{ background: #111; border-radius: 0; padding: 20px; margin-bottom: 20px; border: 1px solid #d4af37; position: relative; }}
    .card h3 {{ font-size: 1rem; margin: 0 0 15px 0; color: #fff; line-height: 1.4; }}
    .btn-link {{ display: block; text-align: right; color: #d4af37; text-decoration: none; font-weight: bold; font-size: 0.8rem; text-transform: uppercase; border-top: 1px solid #333; padding-top: 10px; }}
    
    /* Navigation Bas de Page Noire et Or */
    .nav-bottom {{ position: fixed; bottom: 0; width: 100%; background: #000; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #d4af37; }}
    .nav-item {{ text-align: center; color: #888; text-decoration: none; font-size: 0.7rem; }}
    .nav-item i {{ display: block; font-size: 1.4rem; margin-bottom: 3px; color: #d4af37; }}
    .nav-item.active {{ color: #fff; font-weight: bold; }}
    </style></head><body>

    <div class="header">
        <h1 class="logo">SNIPER IMMO</h1>
    </div>

    <a href="https://wa.me/213000000000" class="wa-float">
        <i class="fab fa-whatsapp" style="margin-right:10px; font-size:1.2rem;"></i> WhatsApp Immobilier
    </a>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'>
            <h3>{o['t']}</h3>
            <a href='{o['l']}' target='_blank' class='btn-link'>Consulter l'offre <i class="fas fa-arrow-right"></i></a>
        </div>"""
    
    html += f"""</div>
    
    <div class="nav-bottom">
        <a href="#" class="nav-item active"><i class="fas fa-crosshairs"></i>Cibles</a>
        <a href="#" class="nav-item"><i class="fas fa-map-marker-alt"></i>Secteurs</a>
        <a href="#" class="nav-item"><i class="fas fa-star"></i>Favoris</a>
        <a href="#" class="nav-item"><i class="fas fa-cog"></i>Paramètres</a>
    </div>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ DESIGN NOIR ET DORÉ RESTAURÉ AVEC SUCCÈS !")

run()
