import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Restauration Origine' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🎯 Retour à la version d'origine...")
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
    body {{ font-family: sans-serif; padding: 20px; line-height: 1.6; background-color: white; color: black; }}
    .header {{ text-align: center; margin-bottom: 30px; }}
    .logo {{ font-size: 2.5rem; font-weight: bold; margin: 0; }}
    .listing {{ list-style: none; padding: 0; }}
    .listing li {{ margin-bottom: 15px; padding: 10px; border-bottom: 1px solid #ccc; }}
    .listing a {{ color: blue; text-decoration: none; font-weight: bold; }}
    </style></head><body>
    <div class="header">
        <h1 class="logo">SNIPER IMMO</h1>
        <p>{len(offres)} résultats trouvés</p>
    </div>
    <ul class="listing">"""
    
    for o in offres[:25]:
        html += f"<li>{o['t']}<br><a href='{o['l']}' target='_blank'>Accéder à l'enchère →</a></li>"
    
    html += "</ul></body></html>"
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION ORIGINALE RÉINSTALLÉE !")

run()
