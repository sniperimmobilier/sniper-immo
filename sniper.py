import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Base Originale Bouton Clignotant' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Restauration de la base : Logo Gauche + Bouton Clignotant...")
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
    body {{ background: #f4f7f6; color: #333; font-family: 'Segoe UI', sans-serif; margin: 0; padding-bottom: 80px; }}
    
    /* Header : Logo à gauche */
    .header {{ background: #fff; padding: 15px 20px; display: flex; align-items: center; border-bottom: 1px solid #eee; position: sticky; top: 0; z-index: 100; }}
    .logo-box {{ display: flex; align-items: center; }}
    .logo-img {{ background: #000; color: #fff; padding: 5px 10px; border-radius: 5px; font-weight: 900; font-size: 1.2rem; margin-right: 10px; }}
    .logo-text {{ font-weight: bold; font-size: 0.9rem; letter-spacing: 1px; color: #000; }}

    /* Bouton WhatsApp Clignotant */
    @keyframes pulse-green {{
        0% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }}
        70% {{ transform: scale(1.02); box-shadow: 0 0 0 10px rgba(37, 211, 102, 0); }}
        100% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
    }}
    .wa-btn-blink {{ 
        background: #25d366; color: white; display: flex; align-items: center; justify-content: center; 
        margin: 15px; padding: 15px; border-radius: 12px; text-decoration: none; font-weight: bold;
        animation: pulse-green 2s infinite; border: none;
    }}

    /* Liste des Villas */
    .container {{ padding: 10px; }}
    .villa-card {{ 
        background: #fff; border-radius: 15px; overflow: hidden; margin-bottom: 20px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); border: 1px solid #eee;
    }}
    .villa-img {{ background: #222; height: 180px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 3rem; }}
    .villa-info {{ padding: 15px; }}
    .villa-info h3 {{ font-size: 1.1rem; margin: 0 0 10px 0; color: #1a1a1a; }}
    .btn-details {{ 
        display: inline-block; background: #000; color: #fff; padding: 8px 20px; 
        border-radius: 5px; text-decoration: none; font-size: 0.8rem; font-weight: bold;
    }}

    /* Menu bas */
    .nav-bar {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #eee; }}
    .nav-item {{ color: #999; text-decoration: none; text-align: center; font-size: 0.7rem; }}
    .nav-item i {{ display: block; font-size: 1.4rem; margin-bottom: 3px; color: #333; }}
    </style></head><body>

    <header class="header">
        <div class="logo-box">
            <div class="logo-img">S</div>
            <div class="logo-text">SNIPER<br><span style="color:#ef4444; font-size:0.6rem;">IMMOBILIER</span></div>
        </div>
    </header>

    <a href="https://wa.me/213000000000" class="wa-btn-blink">
        <i class="fab fa-whatsapp" style="margin-right:10px; font-size:1.5rem;"></i> CONTACTER L'AGENT (LIVE)
    </a>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='villa-card'>
            <div class='villa-img'><i class="fas fa-home"></i></div>
            <div class='villa-info'>
                <h3>{o['t']}</h3>
                <a href='{o['l']}' target='_blank' class='btn-details'>VOIR LA FICHE TEST</a>
            </div>
        </div>"""
    
    html += """</div>

    <nav class="nav-bar">
        <a href="#" class="nav-item"><i class="fas fa-th-list"></i>Listes</a>
        <a href="#" class="nav-item"><i class="fas fa-star"></i>Favoris</a>
        <a href="#" class="nav-item"><i class="fas fa-plus-circle"></i>Ajouter</a>
        <a href="#" class="nav-item"><i class="fas fa-user"></i>Compte</a>
    </nav>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ BASE RÉTABLIE : LOGO À GAUCHE ET BOUTON CLIGNOTANT OK.")

run()
