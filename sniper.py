import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Version Villa Prestige' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Restauration de la version Prestige avec Villa...")
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
    body, html {{ margin: 0; padding: 0; height: 100%; font-family: 'Helvetica Neue', sans-serif; background: #000; }}
    
    /* Background Image */
    .hero {{
        background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.6)), url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}

    .top-logo {{ text-align: center; padding-top: 50px; }}
    .top-logo h1 {{ color: #fff; font-size: 3rem; font-weight: 900; letter-spacing: 10px; margin: 0; text-shadow: 2px 2px 10px rgba(0,0,0,0.8); }}

    /* Logo spécial en bas à gauche (celui de la photo) */
    .bottom-identity {{ position: absolute; bottom: 80px; left: 20px; text-align: left; }}
    .visor-logo {{ width: 120px; filter: drop-shadow(0 0 5px rgba(0,0,0,0.5)); }}

    /* Container des offres */
    .content {{ background: rgba(255,255,255,0.95); padding: 20px; border-radius: 20px 20px 0 0; margin-top: -50px; position: relative; z-index: 10; }}
    .card {{ background: #fff; border-radius: 12px; padding: 15px; margin-bottom: 15px; border-left: 5px solid #d4af37; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
    .card h3 {{ font-size: 1rem; margin: 0 0 10px 0; color: #333; }}
    .btn-wa {{ background: #25d366; color: #fff; display: flex; align-items: center; justify-content: center; padding: 12px; border-radius: 50px; text-decoration: none; font-weight: bold; margin-bottom: 20px; }}

    /* Nav Bas */
    .nav-bar {{ position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #eee; z-index: 100; }}
    .nav-item {{ text-align: center; color: #888; text-decoration: none; font-size: 0.7rem; }}
    .nav-item i {{ display: block; font-size: 1.5rem; margin-bottom: 4px; color: #333; }}
    </style></head><body>

    <div class="hero">
        <div class="top-logo">
            <h1>SNIPER</h1>
        </div>
        
        <div class="bottom-identity">
            <div style="color: #d4af37; font-weight: bold; font-size: 1.2rem;">
                <i class="fas fa-crosshairs"></i> SNIPER IMMO
            </div>
            <div style="color: #fff; font-size: 0.6rem; letter-spacing: 1px;">Expertise & Performance</div>
        </div>
    </div>

    <div class="content">
        <a href="https://wa.me/213000000000" class="btn-wa">
            <i class="fab fa-whatsapp" style="margin-right:10px;"></i> CONTACTER L'AGENCE
        </div>
        
        <h2 style="font-size: 1.2rem; border-bottom: 2px solid #d4af37; padding-bottom: 10px;">{len(offres)} Opportunités</h2>
        
        """
    for o in offres:
        html += f"""<div class='card'>
            <h3>{o['t']}</h3>
            <a href='{o['l']}' target='_blank' style='color:#d4af37; font-weight:bold; text-decoration:none; font-size:0.8rem;'>VOIR L'OFFRE <i class="fas fa-external-link-alt"></i></a>
        </div>"""
    
    html += """</div>

    <div class="nav-bar">
        <a href="#" class="nav-item"><i class="fas fa-home"></i>Accueil</a>
        <a href="#" class="nav-item"><i class="fas fa-search"></i>Recherche</a>
        <a href="#" class="nav-item"><i class="fas fa-bell"></i>Alertes</a>
        <a href="#" class="nav-item"><i class="fas fa-user"></i>Profil</a>
    </div>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION VILLA PRESTIGE RESTAURÉE !")

run()
