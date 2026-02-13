import requests
from bs4 import BeautifulSoup
import os
import time

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'XL_HEADER_{int(time.time())}' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

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
    
    html = f"""<html><head><meta charset='UTF-8'><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
    <body style="background:#000; color:#fff; margin:0; font-family:sans-serif;">
        
        <div style="background:#000; height:140px; display:flex; align-items:center; padding:0 20px; border-bottom:2px solid #d4af37; position:relative;">
            
            <div style="display:flex; align-items:center; position:relative; z-index:10;">
                <div style="background:#d4af37; color:#000; padding:10px 20px; font-weight:900; font-size:35px; border-radius:5px; margin-right:12px;">S</div>
                <div style="font-size:22px; font-weight:bold; line-height:1.1; letter-spacing:1px;">SNIPER<br><span style="font-size:14px; color:#d4af37; letter-spacing:3px;">IMMOBILIER</span></div>
            </div>

            <div style="position:absolute; left:50%; top:50%; transform:translate(-50%, -50%); border:2px solid #d4af37; padding:15px 25px; text-align:center; min-width:250px; background: rgba(0,0,0,0.5);">
                <div style="font-size:16px; font-weight:900; color:#d4af37; text-transform:uppercase; letter-spacing:2px;">IMMOBILIER INDUSTRIEL</div>
                <div style="font-size:16px; font-weight:900; color:#fff; text-transform:uppercase; letter-spacing:2px; margin-top:5px;">VILLAS DE LUXE</div>
            </div>
        </div>

        <div style="width:100%; height:30vh; background:url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png') center/cover;"></div>

        <div style="padding:20px;">"""
    
    for o in offres:
        html += f"""<div style="background:#0a0a0a; border:1px solid #1a1a1a; margin-bottom:20px; padding:20px; border-radius:8px;">
            <h3 style="font-size:16px; margin:0 0 15px 0; color:#eee; line-height:1.4;">{o['t']}</h3>
            <a href="{o['l']}" target="_blank" style="display:block; background:#d4af37; color:#000; text-align:center; padding:15px; text-decoration:none; font-weight:bold; border-radius:4px; font-size:14px; text-transform:uppercase;">Consulter le dossier</a>
        </div>"""
    
    html += "</div></body></html>"
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("🚀 FORMAT XL DÉPLOYÉ. LE LOGO ET LE BANDEAU SONT DOUBLÉS.")

run()
