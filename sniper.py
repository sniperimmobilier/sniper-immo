import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Final Branding' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    r = requests.get("https://www.lkeria.com/vente-encheres-immobilier")
    soup = BeautifulSoup(r.text, "html.parser")
    offres = []
    for a in soup.find_all("a"):
        txt = a.get_text().strip()
        if len(txt) > 25: offres.append({"t": txt, "l": "https://www.lkeria.com" + a.get("href")})
    
    html = f"""<html><head><meta charset='UTF-8'><style>
    body {{ background: #000; color: #fff; font-family: sans-serif; text-align: center; margin: 0; }}
    .hero {{ height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; }}
    .logo {{ font-size: 18vw; font-weight: 900; margin: 0; }}
    .card {{ background: #111; padding: 20px; margin: 20px auto; max-width: 600px; border-left: 5px solid red; text-align: left; }}
    a {{ color: red; text-decoration: none; font-weight: bold; }}
    </style></head><body>
    <div class='hero'><h1 class='logo'>SNIPER</h1><p>{len(offres)} CIBLES</p></div>"""
    for o in offres[:15]: html += f"<div class='card'><h3>{o['t']}</h3><a href='{o['l']}'>VOIR L'OFFRE</a></div>"
    html += "</body></html>"
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("🚀 VICTOIRE ! SITE MIS A JOUR.")

run()
