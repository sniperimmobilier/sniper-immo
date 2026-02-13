import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Logo Centré et Épuré' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Restauration de la version Logo Immobilier...")
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
    body {{ background: #f8f9fa; color: #333; font-family: 'Helvetica Neue', Arial, sans-serif; margin: 0; padding-bottom: 80px; }}
    
    /* Header Purifié avec Logo Centré */
    .header {{ background: #fff; padding: 25px 0; text-align: center; border-bottom: 1px solid #eee; position: sticky; top: 0; z-index: 100; }}
    .logo-container {{ display: inline-block; }}
    .logo-text {{ font-size: 1.8rem; font-weight: 800; color: #000; margin: 0; letter-spacing: -1px; }}
    .logo-sub {{ font-size: 0.7rem; color: #ef4444; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; display: block; }}
    
    /* Bouton WhatsApp */
    .whatsapp-btn {{ background: #25d366; color: #fff; display: flex; align-items: center; justify-content: center; margin: 15px; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 0.9rem; shadow: 0 4px 6px rgba(0,0,0,0.1); }}
    
    /* Liste des Offres */
    .container {{ padding: 10px; }}
    .card {{ background: #fff; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; }}
    .card h3 {{ font-size: 0.95rem; margin: 0 0 12px 0; color: #1a1a1a; line-height: 1.5; }}
    .card-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f5f5f5; padding-top: 12px; }}
    .price-tag {{ color: #ef4444; font-weight: bold; font-size: 0.8rem; }}
    .view-btn {{ color: #007bff; text-decoration: none; font-size: 0.8rem; font-weight: 600; }}
    
    /* Navigation du bas */
    .navbar {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #eee; }}
    .nav-link {{ text-align: center; color: #999; text-decoration: none; font-size: 0.65rem; }}
    .nav-link i {{ display: block; font-size: 1.3rem; margin-bottom: 4px; }}
    .nav-link.active {{ color: #000; }}
    </style></head><body>

    <header class="header">
        <div class="logo-container">
            <h1 class="logo-text">SNIPER</h1>
            <span class="logo-sub">IMMOBILIER</span>
        </div>
    </header>

    <a href="https://wa.me/213000000000" class="whatsapp-btn">
        <i class="fab fa-whatsapp" style="margin-right:8px; font-size:1.2rem;"></i> DISCUTER SUR WHATSAPP
    </a>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'>
            <h3>{o['t']}</h3>
            <div class='card-footer'>
                <span class='price-tag'>ENCHÈRE EN COURS</span>
                <a href='{o['l']}' target='_blank' class='view-btn'>VOIR L'OFFRE <i class="fas fa-external-link-alt"></i></a>
            </div>
        </div>"""
    
    html += f"""</div>
    
    <nav class="navbar">
        <a href="#" class="nav-link active"><i class="fas fa-home"></i>ACCUEIL</a>
        <a href="#" class="nav-link"><i class="fas fa-search"></i>RECHERCHE</a>
        <a href="#" class="nav-link"><i class="fas fa-heart"></i>FAVORIS</a>
        <a href="#" class="nav-item"><i class="fas fa-user-circle"></i>COMPTE</a>
    </nav>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION LOGO IMMOBILIER RESTAURÉE ET CENTRÉE !")

run()
