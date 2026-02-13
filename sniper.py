import requests
from bs4 import BeautifulSoup
import os
import time

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Force Update Titres {int(time.time())}' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

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
    .header {{ background: #000; padding: 15px 20px; border-bottom: 1px solid #1a1a1a; display: flex; align-items: center; }}
    .logo-img {{ background: #d4af37; color: #000; padding: 5px 12px; border-radius: 4px; font-weight: 900; font-size: 1.4rem; margin-right: 12px; }}
    .logo-text h1 {{ font-size: 0.9rem; color: #fff; margin: 0; letter-spacing: 1px; text-transform: uppercase; }}
    .logo-text span {{ font-size: 0.6rem; color: #d4af37; font-weight: bold; }}

    .hero {{ 
        height: 45vh; 
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png');
        background-size: cover; background-position: center;
        display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
    }}
    .hero h2 {{ 
        color: #d4af37; font-size: 1.4rem; font-weight: 800; margin: 5px 0; 
        text-transform: uppercase; letter-spacing: 2px; width: 100%;
    }}

    .container {{ padding: 20px; }}
    .card {{ background: #0a0a0a; border: 1px solid #1a1a1a; margin-bottom: 20px; border-radius: 8px; padding: 20px; text-align: center; }}
    .btn-action {{ display: block; background: #d4af37; color: #000; text-decoration: none; padding: 12px; font-weight: bold; border-radius: 4px; text-transform: uppercase; font-size: 0.8rem; }}
    </style></head><body>
    <header class="header">
        <div class="logo-img">S</div>
        <div class="logo-text"><h1>SNIPER</h1><span>IMMOBILIER</span></div>
    </header>
    <div class="hero">
        <h2>IMMOBILIER INDUSTRIEL</h2>
        <h2>&</h2>
        <h2>VILLA DE LUXE</h2>
    </div>
    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'><h3>{o['t']}</h3><a href='{o['l']}' target='_blank' class='btn-action'>Consulter</a></div>"""
    
    html += """</div></body></html>"""
    with open("index.html", "w") as f: f.write(html)
    publier()
run()
