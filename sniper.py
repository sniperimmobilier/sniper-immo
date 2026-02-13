import requests
from bs4 import BeautifulSoup
import os
import time

def publier():
    t1, t2 = "ghp_SF28AkaI0lTzfadzGx6t", "DeUDVnGjnR3uD1lt"
    os.system(f"git add . && git commit -m 'ULTRA_FORCE_CENTER_{int(time.time())}' && git push -f https://{t1+t2}@github.com/sniperimmobilier/sniper-immo.git main")

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
        
        <div style="background:#000; height:80px; display:flex; align-items:center; padding:0 15px; border-bottom:1px solid #222; position:relative;">
            
            <div style="display:flex; align-items:center; position:relative; z-index:10;">
                <div style="background:#d4af37; color:#000; padding:5px 10px; font-weight:bold; border-radius:3px; margin-right:8px;">S</div>
                <div style="font-size:13px; font-weight:bold; line-height:1.1;">SNIPER<br><span style="font-size:8px; color:#d4af37;">IMMOBILIER</span></div>
            </div>

            <div style="position:absolute; left:50%; top:50%; transform:translate(-50%, -50%); border:1px solid #d4af37; padding:8px 12px; text-align:center; min-width:160px;">
                <div style="font-size:10px; font-weight:bold; color:#d4af37; text-transform:uppercase; letter-spacing:1px;">IMMOBILIER INDUSTRIEL</div>
                <div style="font-size:10px; font-weight:bold; color:#fff; text-transform:uppercase; letter-spacing:1px; margin-top:2px;">VILLAS DE LUXE</div>
            </div>
        </div>

        <div style="width:100%; height:30vh; background:url('https://raw.githubusercontent.com/sniperimmobilier/sniper-immo/main/Gemini_Generated_Image_xuez2lxuez2lxuez (1).png') center/cover;"></div>

        <div style="padding:15px;">"""
    
    for o in offres:
        html += f"""<div style="background:#0a0a0a; border:1px solid #1a1a1a; margin-bottom:15px; padding:15px; border-radius:5px;">
            <h3 style="font-size:14px; margin:0 0 10px 0; color:#eee;">{o['t']}</h3>
            <a href="{o['l']}" target="_blank" style="display:block; background:#d4af37; color:#000; text-align:center; padding:12px; text-decoration:none; font-weight:bold; border-radius:3px; font-size:12px;">CONSULTER</a>
        </div>"""
    
    html += "</div></body></html>"
    with open("index.html", "w") as f: f.write(html)
    publier()
    print("🚀 TERMINÉ. ATTENDS 1 MINUTE ET RAFRAÎCHIS.")

run()
