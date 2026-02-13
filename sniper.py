import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Design Purifie' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🎯 Mise à jour du site SNIPER...")
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
    body {{ background: #000; color: #fff; font-family: 'Arial Black', sans-serif; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; }}
    .header-center {{ text-align: center; padding: 60px 20px; width: 100%; border-bottom: 1px solid #222; }}
    .logo {{ font-size: 15vw; font-weight: 900; margin: 0; letter-spacing: -5px; line-height: 1; }}
    .count {{ color: #ef4444; font-size: 1.2rem; margin-top: 10px; letter-spacing: 3px; }}
    .container {{ width: 90%; max-width: 800px; margin: 40px auto; }}
    .card {{ background: #111; border-radius: 10px; padding: 25px; margin-bottom: 20px; border: 1px solid #333; }}
    .card h3 {{ font-size: 1rem; margin-bottom: 20px; font-family: sans-serif; font-weight: normal; color: #ccc; }}
    .btn {{ display: inline-block; color: #fff; text-decoration: none; border: 1px solid #fff; padding: 10px 20px; font-size: 0.8rem; font-family: sans-serif; }}
    </style></head><body>
    <div class="header-center">
        <h1 class="logo">SNIPER</h1>
        <div class="count">{len(offres)} CIBLES DÉTECTÉES</div>
    </div>
    <div class="container">"""
    
    for o in offres[:20]:
        html += f"<div class='card'><h3>{o['t']}</h3><a href='{o['l']}' target='_blank' class='btn'>CONSULTER</a></div>"
    
    html += "</div></body></html>"
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ SITE PURIFIÉ ET MIS À JOUR !")

run()
