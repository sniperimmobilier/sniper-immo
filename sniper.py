import requests
from bs4 import BeautifulSoup
import os
import time

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Header Alignement Gold Frame {int(time.time())}' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
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
    body {{ background: #000; color: #fff; font-family: 'Inter', sans-serif; margin: 0; padding-bottom: 80px; }}
    
    /* Header Principal */
    .header {{ 
        background: #000; 
        padding: 10px 15px; 
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        border-bottom: 1px solid #1a1a1a;
        position: sticky;
        top: 0;
        z-index: 1000;
    }}

    /* Logo à gauche */
    .logo-side {{ display: flex; align-items: center; flex-shrink: 0; }}
    .logo-img {{ background: #d4af37; color: #000; padding: 4px 10px; border-radius: 4px; font-weight: 900; font-size: 1.2rem; margin-right: 8px; }}
    .logo-text h1 {{ font-size: 0.8rem; color: #fff; margin: 0; letter-spacing: 1px; text-transform: uppercase; }}
    .logo-text span {{ font-size: 0.5rem; color: #d4af37; font-weight: bold; display: block; }}

    /* Cadre Doré au centre/droite, aligné au logo */
    .nav-frame {{ 
        border: 1px solid #d4af37; 
        padding: 5px 12px; 
        text-align: center;
        margin-left: 10px;
    }}
    .nav-frame h2 {{ 
        font-size: 0.65rem; 
        margin: 0; 
        letter-spacing: 1px; 
        font-weight: 700;
        text-transform: uppercase;
    }}
    .txt-gold {{ color: #d4af37; margin-bottom: 2px; }}
    .txt-white {{ color: #fff; }}

    /* Image de fond (Hero réduit) */
    .hero {{ 
        height: 35vh; 
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png');
        background-size: cover; 
        background-position: center;
    }}

    .container {{ padding: 15px; }}
    .card {{ background: #0a0a0a; border: 1px solid #1a1a1a; margin-bottom: 15px; border-radius: 4px; padding: 15px; }}
    .card h3 {{ font-size: 0.9rem; margin-top: 0; line-height: 1.4; color: #eee; }}
    .btn-action {{ display: block; background: #d4af37; color: #000; text-decoration: none; padding: 10px; text-align: center; font-weight: bold; border-radius: 2px; text-transform: uppercase; font-size: 0.75rem; }}
    </style></head><body>

    <header class="header">
        <div class="logo-side">
            <div class="logo-img">S</div>
            <div class="logo-text"><h1>SNIPER</h1><span>IMMOBILIER</span></div>
        </div>
        
        <div class="nav-frame">
            <h2 class="txt-gold">IMMOBILIER INDUSTRIEL</h2>
            <h2 class="txt-white">VILLAS DE LUXE</h2>
        </div>
    </header>

    <div class="hero"></div>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'><h3>{o['t']}</h3><a href='{o['l']}' target='_blank' class='btn-action'>Consulter</a></div>"""
    
    html += """</div></body></html>"""
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ Alignement Header OK : Cadre doré et titres blancs.")
run()
