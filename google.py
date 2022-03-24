from fileinput import filename
import pickle

print("""
        
                             Google Scraper         Coded By :                                                                
        ,--,                                                                                 ,----, 
      ,--.'|                                          ,-.                 ,---,            .'   .`| 
   ,--,  | :                                      ,--/ /|               .'  .' `\       .'   .'   ; 
,---.'|  : '   __  ,-.                          ,--. :/ |             ,---.'     \    ,---, '    .' 
|   | : _' | ,' ,'/ /|                          :  : ' /              |   |  .`\  |   |   :     ./  
:   : |.'  | '  | |' |    ,--.--.       ,---.   |  '  /       ,---.   :   : |  '  |   ;   | .'  /   
|   ' '  ; : |  |   ,'   /       \     /     \  '  |  :      /     \  |   ' '  ;  :   `---' /  ;    
'   |  .'. | '  :  /    .--.  .-. |   /    / '  |  |   \    /    /  | '   | ;  .  |     /  ;  /     
|   | :  | ' |  | '      \__\/: . .  .    ' /   '  : |. \  .    ' / | |   | :  |  '    ;  /  /--,   
'   : |  : ; ;  : |      ," .--.; |  '   ; :__  |  | ' \ \ '   ;   /| '   : | /  ;    /  /  / .`|   
|   | '  ,/  |  , ;     /  /  ,.  |  '   | '.'| '  : |--'  '   |  / | |   | '` ,/   ./__;       :   
;   : ;--'    ---'     ;  :   .'   \ |   :    : ;  |,'     |   :    | ;   :  .'     |   :     .'    
|   ,/                 |  ,     .-./  \   \  /  '--'        \   \  /  |   ,.'       ;   |  .'       
'---'                   `--`---'       `----'                `----'   '---'         `---'           
                                                                                                    
                                    Telegram : https://t.me/kickflap
                                    website : https://hrackedz.com  
                                      
                                       """)

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# Variables 
query = input('Enter your dork or search : ')
number = int(input('How much sites you want ? MAX 100 : '))
print('***********************************GRABBING URLS***********************************')
#list
arr = [] 
for j in search(query, tld="co.in", num=number, stop=number, pause=10):
    arr.append(j)
    jeez ='\n'.join([str(item) for item in arr])


data = input('Done,Do You Want to save results ? : YES / NO ')
if data.lower() == 'yes' or 'y':
    textfile = input('What do u wanna name the file ? : ')
    text_file = open(f"{textfile}.txt", "w")
    #Opens or creates the .txt file, sharing the directory of the script#
    text_file.write(jeez)
        #Writes the variable into the .txt file#
    text_file.close()
    print(f'Text File {textfile}.txt Saved In PATH BYEE')
    quit()
else:
    quit()






