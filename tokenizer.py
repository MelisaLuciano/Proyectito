from typing import Text
import docx
import json
def indexCapital(str):
    for x in range(len(str)):
        if str[x].isupper():
            return x


#doc = docx.Document("./token_word.docx")
f = open("./nuevo_text.txt","r",encoding="utf-8")
total = f.readlines()

salida=""
archivo=[]
for x in range(0,int(len(total))-1,2):
    mixe= total[x].replace("\n","").replace("  "," ")
    esp=total[x+1].replace("\n","").replace("  "," ")
    salida=salida+mixe+"\t"+esp+"\n"
    archivo.append(
        {
            "mixe":mixe,
            "esp":esp
        }
    )


    
numero = len(archivo)

print("Numero de frases {0}".format(numero))
with open('data.json', 'w',encoding="utf-8") as outfile:
    json.dump(archivo, outfile,ensure_ascii=False)

with open('mixe-esp.txt', 'w',encoding="utf-8") as salidaTxT:
    salidaTxT.write(salida)