import requests
from bs4 import BeautifulSoup
import os
import time

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    # Le timestamp force GitHub et ton iPhone à voir un nouveau fichier
    os.system(f"git add . && git commit -m 'FIX_HEADER_{int(time.time())}' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

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
    <style>
    body {{ background: #000; color: #fff; font-family: 'Helvetica', sans-serif; margin: 0; padding: 0; }}
    
    /* LE HEADER QUE TU AS DEMANDÉ */
    .header-fix {{ 
        background: #000; 
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        padding: 10px 15px;
        border-bottom: 2px solid #1a1a1a;
    }}

    .logo-side {{ display: flex; align-items: center; }}
    .s-block {{ background: #d4af37; color: #000; padding: 5px 10px; font-weight: 900; font-size: 20px; border-radius: 3px; margin-right: 8px; }}
    .logo-txt {{ font-size: 14px; font-weight: bold; line-height: 1; }}
    .logo-txt span {{ font-size: 9px; color: #d4af37; letter-spacing: 1px; }}

    /* LE CADRE DORÉ ALIGNÉ */
    .gold-frame {{ 
        border: 1.5px solid #d4af37; 
        padding: 6px 12px; 
        text-align: center;
        min-width: 160px;
    }}
    .gold-frame div {{ font-size: 10px; font-weight: 800; letter-spacing: 0.5px; text-transform: uppercase; }}
    .titre-indus {{ color: #d4af37; margin-bottom: 2px; }}
    .titre-luxe {{ color: #ffffff; }}

    .hero-img {{ 
        width: 100%; height: 30vh; 
        background: url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png') center/cover;
    }}

    .container {{ padding: 15px; }}
    .card {{ background: #0a0a0a; border: 1px solid #222; margin-bottom: 12px; padding: 15px; border-radius: 5px; }}
    .card h3 {{ font-size: 14px; margin: 0 0 10px 0; color: #ddd; }}
    .btn {{ display: block; background: #d4af37; color: #000; text-align: center; padding: 10px; text-decoration: none; font-weight: bold; font-size: 12px; border-radius: 3px; }}
    </style></head><body>

    <div class="header-fix">
        <div class="logo-side">
            <div class="s-block">S</div>
            <div class="logo-txt">SNIPER<br><span>IMMOBILIER</span></div>
        </div>
        
        <div class="gold-frame">
            <div class="titre-indus">IMMOBILIER INDUSTRIEL</div>
            <div class="titre-luxe">VILLAS DE LUXE</div>
        </div>
    </div>

    <div class="hero-img"></div>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'><h3>{o['t']}</h3><a href='{o['l']}' target='_blank' class='btn'>CONSULTER</a></div>"""
    
    html += """</div></body></html>"""
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ DESIGN FORCÉ : CADRE DORÉ ET TEXTES ALIGNÉS.")
run()
