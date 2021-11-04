import re
f = open("./texto.txt","r",encoding="utf-8")
pat = re.compile(r'([A-Z|Ë][^\.!?]*[\.])', re.M)

texto = ' '.join(f.readlines()).replace("—","qqq")
result = pat.findall(texto)
result=[x.replace("\n"," ") for x in result]

out = open("./nuevo_text.txt","w+",encoding="utf-8")
out.write('\n'.join(result))