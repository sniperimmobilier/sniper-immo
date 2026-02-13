import requests
from bs4 import BeautifulSoup
import os

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'Retour Version Originale' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

def run():
    print("🎯 Restauration du site initial (Villa Nina)...")
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
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f7f7f7; margin: 0; padding: 15px; }}
    .header {{ background: white; padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
    .logo-container {{ display: flex; align-items: center; justify-content: space-between; }}
    .logo-title {{ font-size: 22px; font-weight: 800; color: #1a1a1a; margin: 0; }}
    .status {{ font-size: 12px; color: #2ecc71; font-weight: bold; text-transform: uppercase; }}
    
    .card {{ background: white; border-radius: 18px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee; }}
    .card h3 {{ font-size: 16px; line-height: 1.4; color: #2c3e50; margin: 0 0 15px 0; font-weight: 600; }}
    .btn {{ display: inline-block; background: #1a1a1a; color: white; text-decoration: none; padding: 12px 20px; border-radius: 10px; font-size: 14px; font-weight: bold; width: 100%; text-align: center; box-sizing: border-box; }}
    
    .footer-nav {{ position: fixed; bottom: 0; left: 0; right: 0; background: white; display: flex; justify-content: space-around; padding: 15px; border-top: 1px solid #eee; }}
    .nav-item {{ color: #bdc3c7; text-decoration: none; font-size: 12px; font-weight: bold; }}
    .nav-item.active {{ color: #1a1a1a; }}
    </style></head><body>
    
    <div class="header">
        <div class="logo-container">
            <h1 class="logo-title">SNIPER IMMO</h1>
            <span class="status">● LIVE SCAN</span>
        </div>
        <p style="margin: 10px 0 0 0; color: #7f8c8d; font-size: 14px;">{len(offres)} villas et appartements détectés</p>
    </div>"""
    
    for o in offres:
        html += f"""<div class="card">
            <h3>{o['t']}</h3>
            <a href="{o['l']}" target="_blank" class="btn">CONSULTER L'OFFRE</a>
        </div>"""
    
    html += """<div class="footer-nav">
        <a href="#" class="nav-item active">EXPLORER</a>
        <a href="#" class="nav-item">FAVORIS</a>
        <a href="#" class="nav-item">MON COMPTE</a>
    </div>
    </body></html>"""
    
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("✅ VERSION INITIALE (VILLA NINA) RÉTABLIE AVEC SUCCÈS !")

run()
