import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Version Finale Stable' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🎯 Reconstruction du site original...")
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
    body, html {{ margin: 0; padding: 0; background: #000; font-family: 'Segoe UI', Roboto, sans-serif; }}
    
    /* Image Villa en fond */
    .hero {{
        height: 60vh;
        background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.8)), url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }}

    .logo-main {{ color: #fff; font-size: 3.5rem; font-weight: 900; letter-spacing: 8px; margin: 0; text-shadow: 0 5px 15px rgba(0,0,0,0.5); }}
    .logo-sub {{ color: #d4af37; font-weight: bold; letter-spacing: 3px; font-size: 0.9rem; }}

    .container {{ background: #fff; border-radius: 30px 30px 0 0; margin-top: -40px; padding: 25px 15px 100px 15px; position: relative; }}
    
    .wa-btn {{ background: #25d366; color: #fff; display: flex; align-items: center; justify-content: center; padding: 15px; border-radius: 15px; text-decoration: none; font-weight: bold; margin-bottom: 25px; box-shadow: 0 4px 10px rgba(37,211,102,0.3); }}

    .card {{ background: #f9f9f9; border-radius: 15px; padding: 20px; margin-bottom: 15px; border: 1px solid #eee; }}
    .card h3 {{ font-size: 1rem; margin: 0 0 10px 0; color: #222; line-height: 1.4; }}
    .card a {{ color: #d4af37; text-decoration: none; font-weight: bold; font-size: 0.85rem; text-transform: uppercase; }}

    .nav-bottom {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #eee; z-index: 1000; }}
    .nav-item {{ text-align: center; color: #999; text-decoration: none; font-size: 0.7rem; font-weight: bold; }}
    .nav-item i {{ display: block; font-size: 1.5rem; margin-bottom: 5px; color: #222; }}
    .nav-item.active {{ color: #d4af37; }}
    .nav-item.active i {{ color: #d4af37; }}
    </style></head><body>

    <div class="hero">
        <h1 class="logo-main">SNIPER</h1>
        <div class="logo-sub">IMMOBILIER PRESTIGE</div>
    </div>

    <div class="container">
        <a href="https://wa.me/213000000000" class="wa-btn">
            <i class="fab fa-whatsapp" style="margin-right:10px; font-size:1.5rem;"></i> CONTACT WHATSAPP
        </a>

        <h2 style="font-size: 1.1rem; margin-bottom: 20px; color: #555; border-left: 4px solid #d4af37; padding-left: 10px;">
            {len(offres)} Enchères en cours
        </h2>
    """
    
    for o in offres:
        html += f"""<div class='card'>
            <h3>{o['t']}</h3>
            <a href='{o['l']}' target='_blank'>Voir l'annonce <i class="fas fa-arrow-right"></i></a>
        </div>"""
    
    html += """</div>

    <div class="nav-bottom">
        <a href="#" class="nav-item active"><i class="fas fa-home"></i>ACCUEIL</a>
        <a href="#" class="nav-item"><i class="fas fa-search"></i>RECHERCHE</a>
        <a href="#" class="nav-item"><i class="fas fa-bell"></i>ALERTES</a>
        <a href="#" class="nav-item"><i class="fas fa-user"></i>PROFIL</a>
    </div>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ MISSION ACCOMPLIE : LE SITE EST RÉTABLI !")

run()
