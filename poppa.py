from Settings.Program.Config.Config import *
from Settings.Program.Config.Util import *

try:
   import webbrowser
   import re
except:
   ErrorModule()
   

   
option_01 = "Tool-Info"
option_02 = "Tool-Website"
option_03 = "Builder-Stealer"
option_04 = "Sql-Vulnerability"
option_05 = "Illegal-Website"
option_06 = "Search-In-DataBase"
option_07 = "Dox-Tracker"
option_08 = "Dox-Create"
option_09 = "Number-Info"
option_10 = "Email-Info"
option_11 = "Email-OSINT"
option_12 = "Ip-Info"
option_13 = "Ip-Pinger"
option_14 = "Ip-Website"
option_15 = "Ip-Port-Scanner"
option_16 = "Ip-Generator"
option_17 = "Get-Your-Ip"
option_18 = "Get-Your-Token-Discord"
option_19 = "Discord-Token-Info"
option_20 = "Discord-Token-Nuker"
option_21 = "Discord-Token-Joiner"
option_22 = "Discord-Token-Leaver"
option_23 = "Discord-Token-Login"
option_24 = "Discord-Token-To-Id-And-Brute"
option_25 = "Discord-Token-Server-Raid"
option_26 = "Discord-Token-Spammer"
option_27 = "Discord-Token-Delete-Friends"
option_28 = "Discord-Token-Block-Friends"
option_29 = "Discord-Token-Mass-Dm"
option_32 = "Discord-Token-Delete-Dm"
option_33 = "Discord-Token-Status-Changer"
option_34 = "Discord-Token-Language-Changer"
option_35 = "Discord-Token-House-Changer"
option_36 = "Discord-Token-Theme-Changer"
option_37 = "Discord-Token-Generator"
option_38 = "Discord-Bot-Server-Nuker"
option_39 = "Discord-Bot-Invite-To-Id"
option_40 = "Discord-Server-Info"
option_41 = "Discord-Nitro-Generator"
option_42 = "Discord-Webhook-Info"
option_43 = "Discord-Webhook-Delete"
option_44 = "Discord-Webhook-Spammer"
option_45 = "Discord-Webhook-Generator"
option_46 = "Roblox-Cookie-Login"
option_47 = "Roblox-Cookie-Info"
option_48 = "Roblox-User-Info"
option_49 = "Roblox-Id-Info"

option_next = "Next Page >>"
option_previous = "<< Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = option_29.ljust(30)[:30].replace("-", " ")

option_32_txt = option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = option_39.ljust(30)[:30].replace("-", " ")
option_40_txt = option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = option_49.ljust(30)[:30].replace("-", " ")

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

page1 = f"""{white}⌈{green}Page 1{white}⌋
   {white}⌈{green}01{white}⌋ {green}⊳{white} {option_01_txt} {white}⌈{green}11{white}⌋ {green}⊳{white} {option_11_txt} {white}⌈{green}21{white}⌋ {green}⊳{white} {option_21_txt}
   {white}⌈{green}02{white}⌋ {green}⊳{white} {option_02_txt} {white}⌈{green}12{white}⌋ {green}⊳{white} {option_12_txt} {white}⌈{green}22{white}⌋ {green}⊳{white} {option_22_txt}
   {white}⌈{green}03{white}⌋ {green}⊳{white} {option_03_txt} {white}⌈{green}13{white}⌋ {green}⊳{white} {option_13_txt} {white}⌈{green}23{white}⌋ {green}⊳{white} {option_23_txt}
   {white}⌈{green}04{white}⌋ {green}⊳{white} {option_04_txt} {white}⌈{green}14{white}⌋ {green}⊳{white} {option_14_txt} {white}⌈{green}24{white}⌋ {green}⊳{white} {option_24_txt}
   {white}⌈{green}05{white}⌋ {green}⊳{white} {option_05_txt} {white}⌈{green}15{white}⌋ {green}⊳{white} {option_15_txt} {white}⌈{green}25{white}⌋ {green}⊳{white} {option_25_txt}
   {white}⌈{green}06{white}⌋ {green}⊳{white} {option_06_txt} {white}⌈{green}16{white}⌋ {green}⊳{white} {option_16_txt} {white}⌈{green}26{white}⌋ {green}⊳{white} {option_26_txt}
   {white}⌈{green}07{white}⌋ {green}⊳{white} {option_07_txt} {white}⌈{green}17{white}⌋ {green}⊳{white} {option_17_txt} {white}⌈{green}27{white}⌋ {green}⊳{white} {option_27_txt}
   {white}⌈{green}08{white}⌋ {green}⊳{white} {option_08_txt} {white}⌈{green}18{white}⌋ {green}⊳{white} {option_18_txt} {white}⌈{green}28{white}⌋ {green}⊳{white} {option_28_txt}
   {white}⌈{green}09{white}⌋ {green}⊳{white} {option_09_txt} {white}⌈{green}19{white}⌋ {green}⊳{white} {option_19_txt} {white}⌈{green}29{white}⌋ {green}⊳{white} {option_29_txt}
   {white}⌈{green}10{white}⌋ {green}⊳{white} {option_10_txt} {white}⌈{green}20{white}⌋ {green}⊳{white} {option_20_txt} {white}⌈{green}30{white}⌋ {green}⊳ {option_next_txt}"""

page2 = f"""{white}⌈{green}Page 2{white}⌋
   {white}⌈{green}31{white}⌋ {green}⊳ {option_previous_txt} {white}⌈{green}41{white}⌋ {green}⊳{white} {option_41_txt}
   {white}⌈{green}32{white}⌋ {green}⊳{white} {option_32_txt} {white}⌈{green}42{white}⌋ {green}⊳{white} {option_42_txt}
   {white}⌈{green}33{white}⌋ {green}⊳{white} {option_33_txt} {white}⌈{green}43{white}⌋ {green}⊳{white} {option_43_txt}
   {white}⌈{green}34{white}⌋ {green}⊳{white} {option_34_txt} {white}⌈{green}44{white}⌋ {green}⊳{white} {option_44_txt}
   {white}⌈{green}35{white}⌋ {green}⊳{white} {option_35_txt} {white}⌈{green}45{white}⌋ {green}⊳{white} {option_45_txt}
   {white}⌈{green}36{white}⌋ {green}⊳{white} {option_36_txt} {white}⌈{green}46{white}⌋ {green}⊳{white} {option_46_txt}
   {white}⌈{green}37{white}⌋ {green}⊳{white} {option_37_txt} {white}⌈{green}47{white}⌋ {green}⊳{white} {option_47_txt} 
   {white}⌈{green}38{white}⌋ {green}⊳{white} {option_38_txt} {white}⌈{green}48{white}⌋ {green}⊳{white} {option_48_txt}
   {white}⌈{green}39{white}⌋ {green}⊳{white} {option_39_txt} {white}⌈{green}49{white}⌋ {green}⊳{white} {option_49_txt}
   {white}⌈{green}40{white}⌋ {green}⊳{white} {option_40_txt} """

def Menu():
   try:
      with open("./Settings/Program/Config/Page.txt", "r") as file:
         page = file.read()
      if page in ["1"]:
         page = page1
         Title("Page 1")
      elif page in ["2"]:
         page = page2
         Title("Page 2")
      else:
         page = page1
         Title("Page 1")
   except:
      page = page1
      Title("Page 1")

   menu = f"""{green}                                                                                                  
 
{blue}   ▄███████▄  ▄██████▄     ▄███████▄    ▄███████▄    ▄████████      ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄ 
{red}  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███     ███    ███     ███    ███ ███    ███   ███ ▄███▀ 
{green}  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███     ███    ███     ███    ███ ███    █▀    ███▐██▀   
{blue}  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███    ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    
{red}▀█████████▀  ███    ███ ▀█████████▀  ▀█████████▀  ▀███████████   ▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    
{green}  ███        ███    ███   ███          ███          ███    ███     ███    ███     ███    ███ ███    █▄    ███▐██▄   
{blue}  ███        ███    ███   ███          ███          ███    ███     ███    ███     ███    ███ ███    ███   ███ ▀███▄ 
{red} ▄████▀       ▀██████▀   ▄████▀       ▄████▀        ███    █▀      ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ 

{green}《{blue}Logged in as {username_pc}{green} 》

   {page}
   """
   return menu

Clear()
Slow(banner + Menu())

while True:
   Clear()
   print(Menu())
   choice = input(f"""{green}┌───({white}{username_pc}@PoppaHack{green})─[{white}~{green}]
└──{green}➔ {reset}""")

   if choice in ['1', '01']:
      StartProgram(f"{option_01}.py")

   elif choice in ['2', '02']:
      StartProgram(f"{option_02}.py")

   elif choice in ['3', '03']:
      StartProgram(f"{option_03}.py")

   elif choice in ['4', '04']:
      StartProgram(f"{option_04}.py")

   elif choice in ['5', '05']:
      StartProgram(f"{option_05}.py")

   elif choice in ['6', '06']:
      StartProgram(f"{option_06}.py")

   elif choice in ['7', '07']:
      StartProgram(f"{option_07}.py")

   elif choice in ['8', '08']:
      StartProgram(f"{option_08}.py")

   elif choice in ['9', '09']:
      StartProgram(f"{option_09}.py")

   elif choice in ['10']:
      StartProgram(f"{option_10}.py")

   elif choice in ['11']:
      StartProgram(f"{option_11}.py")

   elif choice in ['12']:
      StartProgram(f"{option_12}.py")

   elif choice in ['13']:
      StartProgram(f"{option_13}.py")

   elif choice in ['14']:
      StartProgram(f"{option_14}.py")

   elif choice in ['15']:
      StartProgram(f"{option_15}.py")

   elif choice in ['16']:
      StartProgram(f"{option_16}.py")

   elif choice in ['17']:
      StartProgram(f"{option_17}.py")

   elif choice in ['18']:
      StartProgram(f"{option_18}.py")

   elif choice in ['19']:
      StartProgram(f"{option_19}.py")
      
   elif choice in ['20']:
      StartProgram(f"{option_20}.py")
      
   elif choice in ['21']:
      StartProgram(f"{option_21}.py")
      
   elif choice in ['22']:
      StartProgram(f"{option_22}.py")
      
   elif choice in ['23']:
      StartProgram(f"{option_23}.py")
      
   elif choice in ['24']:
      StartProgram(f"{option_24}.py")
      
   elif choice in ['25']:
      StartProgram(f"{option_25}.py")
      
   elif choice in ['26']:
      StartProgram(f"{option_26}.py")
      
   elif choice in ['27']:
      StartProgram(f"{option_27}.py")
      
   elif choice in ['28']:
      StartProgram(f"{option_28}.py")
      
   elif choice in ['29']:
      StartProgram(f"{option_29}.py")
      

   elif choice in ['30']:
      page = page2
      with open("./Settings/Program/Config/Page.txt", "w") as file:
         file.write("2")
         Title("Page 2")

   elif choice in ['31']:
      page = page1
      with open("./Settings/Program/Config/Page.txt", "w") as file:
         file.write("1")
         Title("Page 1")


   elif choice in ['32']:
      StartProgram(f"{option_32}.py")
      
   elif choice in ['33']:
      StartProgram(f"{option_33}.py")
      
   elif choice in ['34']:
      StartProgram(f"{option_34}.py")

   elif choice in ['35']:
      StartProgram(f"{option_35}.py")

   elif choice in ['36']:
      StartProgram(f"{option_36}.py")

   elif choice in ['37']:
      StartProgram(f"{option_37}.py")

   elif choice in ['38']:
      StartProgram(f"{option_38}.py")

   elif choice in ['39']:
      StartProgram(f"{option_39}.py")

   elif choice in ['40']:
      StartProgram(f"{option_40}.py")

   elif choice in ['41']:
      StartProgram(f"{option_41}.py")

   elif choice in ['42']:
      StartProgram(f"{option_42}.py")

   elif choice in ['43']:
      StartProgram(f"{option_43}.py")
   
   elif choice in ['44']:
      StartProgram(f"{option_44}.py")

   elif choice in ['45']:
      StartProgram(f"{option_45}.py")

   elif choice in ['46']:
      StartProgram(f"{option_46}.py")

   elif choice in ['47']:
      StartProgram(f"{option_47}.py")

   elif choice in ['48']:
      StartProgram(f"{option_48}.py")

   elif choice in ['49']:
      StartProgram(f"{option_49}.py")

   else:
      ErrorChoiceStart()