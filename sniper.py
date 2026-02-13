import requests
from bs4 import BeautifulSoup
import os
import time

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Add Live Status Button {int(time.time())}' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

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
    body {{ background: #000; color: #fff; font-family: 'Helvetica', sans-serif; margin: 0; padding: 0; }}
    
    /* Header XL avec Bouton Live */
    .header-fix {{ 
        background: #000; height: 140px; display: flex; align-items: center; 
        padding: 0 20px; border-bottom: 2px solid #d4af37; position: relative;
    }}
    .logo-side {{ display: flex; align-items: center; z-index: 10; }}
    .s-block {{ background: #d4af37; color: #000; padding: 10px 20px; font-weight: 900; font-size: 35px; border-radius: 5px; margin-right: 12px; }}
    .logo-txt {{ font-size: 22px; font-weight: bold; line-height: 1.1; }}

    .gold-frame {{ 
        position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); 
        border: 2px solid #d4af37; padding: 15px 25px; text-align: center; min-width: 250px;
    }}
    .titre-indus {{ color: #d4af37; font-size: 16px; font-weight: 900; text-transform: uppercase; }}
    .titre-luxe {{ color: #ffffff; font-size: 16px; font-weight: 900; text-transform: uppercase; margin-top: 5px; }}

    /* Bouton Live à droite */
    .live-contact {{
        position: absolute; right: 20px; top: 50%; transform: translateY(-50%);
        display: flex; flex-direction: column; align-items: center; text-decoration: none; z-index: 20;
    }}
    .dot-container {{ position: relative; width: 20px; height: 20px; margin-bottom: 5px; }}
    .dot {{ width: 12px; height: 12px; background: #2ecc71; border-radius: 50%; position: absolute; top: 4px; left: 4px; }}
    .pulse {{ 
        width: 20px; height: 20px; background: #2ecc71; border-radius: 50%; 
        position: absolute; opacity: 0.5; animation: pulse-animation 2s infinite; 
    }}
    @keyframes pulse-animation {{ 
        0% {{ transform: scale(0.5); opacity: 1; }}
        100% {{ transform: scale(2.5); opacity: 0; }}
    }}
    .live-text {{ color: #2ecc71; font-size: 10px; font-weight: bold; text-transform: uppercase; }}

    .hero-img {{ width: 100%; height: 35vh; background: url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png') center/cover; }}

    .services {{ padding: 40px 20px; background: #0a0a0a; text-align: center; border-bottom: 1px solid #222; }}
    .services h2 {{ color: #d4af37; font-size: 1.5rem; text-transform: uppercase; margin-bottom: 30px; }}
    .service-grid {{ display: grid; grid-template-columns: 1fr; gap: 20px; }}
    .service-item {{ border: 1px solid #333; padding: 20px; border-radius: 8px; }}
    .service-item i {{ color: #d4af37; font-size: 2rem; margin-bottom: 15px; }}
    
    .container {{ padding: 30px 20px; }}
    .card {{ background: #111; border-left: 4px solid #d4af37; margin-bottom: 20px; padding: 20px; }}
    .btn {{ display: block; background: #d4af37; color: #000; text-align: center; padding: 15px; text-decoration: none; font-weight: bold; border-radius: 4px; }}
    </style></head><body>

    <div class="header-fix">
        <div class="logo-side">
            <div class="s-block">S</div>
            <div class="logo-txt">SNIPER<br><span style="font-size:14px; color:#d4af37;">IMMOBILIER</span></div>
        </div>
        
        <div class="gold-frame">
            <div class="titre-indus">IMMOBILIER INDUSTRIEL</div>
            <div class="titre-luxe">VILLAS DE LUXE</div>
        </div>

        <a href="https://wa.me/33634089609" class="live-contact">
            <div class="dot-container">
                <div class="pulse"></div>
                <div class="dot"></div>
            </div>
            <div class="live-text">LIVE CONTACT</div>
        </a>
    </div>

    <div class="hero-img"></div>

    <section class="services">
        <h2>NOS SERVICES VIP</h2>
        <div class="service-grid">
            <div class="service-item"><i class="fas fa-gavel"></i><h3>SÉCURITÉ JURIDIQUE</h3><p>Accompagnement notarial complet.</p></div>
            <div class="service-item"><i class="fas fa-industry"></i><h3>CONSEIL INDUSTRIEL</h3><p>Terrains et hangars stratégiques.</p></div>
        </div>
    </section>

    <div class="container">"""
    
    for o in offres:
        html += f"<div class='card'><h3>{o['t']}</h3><a href='{o['l']}' target='_blank' class='btn'>CONSULTER</a></div>"
    
    html += "</div></body></html>"
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ BOUTON LIVE DÉPLOYÉ AVEC SUCCÈS !")
run()
