import requests
from bs4 import BeautifulSoup
import os

def publier(token):
    os.chdir(os.path.expanduser("~/Desktop/SNIPER_IMMO"))
    os.system("git add index.html sniper.py")
    os.system("git commit -m 'Final UX'")
    os.system(f"git push -f https://{token}@github.com/sniperimmobilier/sniper-immo.git main")

def generer_page(annonces):
    chemin = os.path.expanduser("~/Desktop/SNIPER_IMMO/index.html")
    html = f"""<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>
    body {{ background: #050505; color: #fff; font-family: sans-serif; margin: 0; scroll-behavior: smooth; }}
    .hero {{ height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border-bottom: 1px solid #222; }}
    .logo {{ font-size: 20vw; font-weight: 900; letter-spacing: -10px; line-height: 0.8; margin: 0; }}
    .count {{ color: #ef4444; font-size: 1.5rem; margin-top: 20px; font-weight: bold; letter-spacing: 5px; }}
    .container {{ max-width: 800px; margin: 3cm auto 100px auto; padding: 0 20px; }}
    .card {{ background: #111; border-radius: 12px; padding: 30px; margin-bottom: 30px; border-left: 8px solid #ef4444; transition: 0.3s; }}
    .btn {{ display: inline-block; color: #ef4444; text-decoration: none; font-weight: bold; border: 2px solid #ef4444; padding: 12px 30px; border-radius: 8px; }}
    </style></head><body><div class="hero"><h1 class="logo">SNIPER</h1><div class="count">{len(annonces)} CIBLES DETECTEES</div><p style="margin-top:50px;color:#444;">SCROLLEZ ↓</p></div><div class="container">"""
    for a in annonces:
        html += f"<div class='card'><h3>{a['t']}</h3><a href='{a['l']}' target='_blank' class='btn'>CONSULTER L’OFFRE</a></div>"
    html += "</div></body></html>"
    with open(chemin, "w", encoding="utf-8") as f: f.write(html)

def run():
    t = "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"
    print("🎯 Scan en cours...")
    try:
        r = requests.get("https://www.lkeria.com/vente-encheres-immobilier", timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        offres = []
        for a in soup.find_all("a"):
            txt = a.get_text().strip()
            if len(txt) > 25:
                link = a.get("href")
                if link and not link.startswith("http"): link = "https://www.lkeria.com" + link
                offres.append({"t": txt, "l": link})
        generer_page(offres[:15])
        publier(t)
        print("✅ SITE DEPLOYE AVEC SUCCES !")
    except Exception as e: print(f"Erreur : {e}")

run()
