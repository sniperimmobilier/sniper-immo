import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Update Textes: Industriel et Luxe' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🚀 Mise à jour des textes en cours...")
    r = requests.get("https://www.lkeria.com/vente-encheres-immobilier")
    soup = BeautifulSoup(r.text, "html.parser")
    offres = []
    for a in soup.find_all("a"):
        txt = a.get_text().strip()
        if len(txt) > 25:
            link = a.get("href")
            if not link.startswith("http"): link = "https://www.lkeria.com" + link
            offres.append({"t": txt, "l": link})
    
    html = """<html><head><meta charset='UTF-8'><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
    body { background: #000; color: #fff; font-family: 'Inter', sans-serif; margin: 0; padding-bottom: 80px; }
    
    .header { background: #000; padding: 15px 20px; display: flex; align-items: center; border-bottom: 1px solid #1a1a1a; position: sticky; top: 0; z-index: 1000; }
    .logo-box { display: flex; align-items: center; }
    .logo-img { background: #d4af37; color: #000; padding: 5px 12px; border-radius: 4px; font-weight: 900; font-size: 1.4rem; margin-right: 12px; }
    .logo-text h1 { font-size: 0.9rem; color: #fff; margin: 0; letter-spacing: 1px; font-weight: 800; }
    .logo-text span { font-size: 0.6rem; color: #d4af37; text-transform: uppercase; font-weight: bold; }

    .hero { position: relative; height: 55vh; background-image: url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png'); background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center; text-align: center; }
    .hero-overlay { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); }
    .hero-content { position: relative; z-index: 10; border: 1px solid #d4af37; padding: 25px; background: rgba(0,0,0,0.7); max-width: 85%; }
    .hero-content h2 { color: #d4af37; font-size: 1.2rem; text-transform: uppercase; letter-spacing: 2px; margin: 0 0 10px 0; }
    .hero-content p { color: #fff; font-size: 1.5rem; font-weight: bold; margin: 0; text-transform: uppercase; }

    .container { padding: 20px; }
    .card { background: #0a0a0a; border: 1px solid #1a1a1a; margin-bottom: 25px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .card-body { padding: 20px; text-align: center; }
    .card-body h3 { font-size: 1rem; margin-bottom: 15px; color: #fff; line-height: 1.4; }
    .btn-action { display: block; background: #d4af37; color: #000; text-decoration: none; padding: 12px; font-size: 0.8rem; font-weight: bold; border-radius: 4px; text-transform: uppercase; }

    .nav-bottom { position: fixed; bottom: 0; width: 100%; background: #000; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #1a1a1a; }
    .nav-item { color: #555; text-decoration: none; font-size: 0.7rem; text-align: center; }
    .nav-item i { display: block; font-size: 1.4rem; margin-bottom: 4px; color: #d4af37; }
    </style></head><body>

    <header class="header">
        <div class="logo-box">
            <div class="logo-img">S</div>
            <div class="logo-text">
                <h1>SNIPER</h1>
                <span>IMMOBILIER</span>
            </div>
        </div>
    </header>

    <div class="hero">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h2>IMMOBILIER INDUSTRIEL</h2>
            <p>VILLA DE LUXE</p>
        </div>
    </div>

    <div class="container">"""
    
    for o in offres:
        html += f"""<div class='card'>
            <div class='card-body'>
                <h3>{o['t']}</h3>
                <a href='{o['l']}' target='_blank' class='btn-action'>Consulter l'offre</a>
            </div>
        </div>"""
    
    html += """</div>
    
    <div class="nav-bottom">
        <a href="#" class="nav-item"><i class="fas fa-industry"></i>Industriel</a>
        <a href="#" class="nav-item"><i class="fas fa-gem"></i>Luxe</a>
        <a href="#" class="nav-item"><i class="fas fa-user-tie"></i>Contact</a>
    </div>

    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ TEXTES MIS À JOUR : INDUSTRIEL & LUXE.")

run()
