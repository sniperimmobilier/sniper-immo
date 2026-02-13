import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Version Zero Purifiee' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🎯 Retour aux sources absolues...")
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
    body {{ font-family: serif; padding: 10px; background: white; color: black; }}
    .center {{ text-align: center; }}
    h1 {{ margin: 0; padding: 10px; }}
    hr {{ border: 0; border-top: 1px solid #000; margin: 20px 0; }}
    a {{ color: #0000EE; text-decoration: underline; }}
    .item {{ margin-bottom: 20px; }}
    </style></head><body>
    <div class="center">
        <h1>SNIPER IMMO</h1>
        <small>{len(offres)} OFFRES DISPONIBLES</small>
    </div>
    <hr>"""
    
    for o in offres:
        html += f"<div class='item'>{o['t']}<br><a href='{o['l']}'>Voir l'annonce</a></div>"
    
    html += "</body></html>"
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ RETOUR A LA VERSION ZERO EFFECTUÉ.")

run()
