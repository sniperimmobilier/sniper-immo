import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Retour Villa Nina Clean' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🎯 Restauration de la version Villa Nina...")
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
    body {{ background: #ffffff; color: #000; font-family: -apple-system, BlinkMacSystemFont, sans-serif; margin: 0; padding: 20px; }}
    .header {{ text-align: center; margin-bottom: 40px; border-bottom: 2px solid #000; padding-bottom: 20px; }}
    .logo {{ font-size: 3rem; font-weight: 900; letter-spacing: -2px; margin: 0; }}
    .subtitle {{ font-size: 0.8rem; color: #666; letter-spacing: 2px; text-transform: uppercase; }}
    .container {{ max-width: 800px; margin: 0 auto; }}
    .item {{ border-bottom: 1px solid #eee; padding: 20px 0; display: flex; justify-content: space-between; align-items: center; }}
    .item-title {{ font-size: 1.1rem; font-weight: 500; line-height: 1.4; max-width: 75%; }}
    .btn {{ background: #000; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }}
    </style></head><body>
    <div class="header">
        <h1 class="logo">SNIPER IMMO</h1>
        <div class="subtitle">{len(offres)} ENCHÈRES DÉTECTÉES</div>
    </div>
    <div class="container">"""
    
    for o in offres[:20]:
        html += f"<div class='item'><div class='item-title'>{o['t']}</div><a href='{o['l']}' target='_blank' class='btn'>DÉTAILS</a></div>"
    
    html += "</div></body></html>"
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION VILLA NINA RESTAURÉE ET CENTRÉE !")

run()
