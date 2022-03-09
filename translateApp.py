## Practise challenge from Topcoder:
##  https://www.topcoder.com/challenges/030bdfc4-37d1-4b71-80a4-cbc6173a7a06
## required HTTP request be found at:
##  https://github.com/statickidz/node-google-translate-skidz/blob/master/lib/translate.js

## This app will translate the text in source.txt from English to Chinese
## The result will be in target.txt, and there will be a preview shows the first 60 chars

import requests
print("Tranlating the text in source.txt from English to Chinese")
f = open("source.txt","r")
origStr = f.read()
f.close()
pload = {"sl":"en", "tl":"zh", "q":origStr}
r =requests.post('https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e', data =pload)

if (r.status_code!=200):
    print("Error requesting google API: statue code="+str(r.status_code))
    exit()

transStr = ""
for transDict in r.json()["sentences"]:
    if("trans" in transDict):
        transStr = transStr+transDict["trans"]

f = open("target.txt", "w")
f.write(transStr)
f.close()
print("Success, translated text is in target.txt")
print("Below is a preview of translated text:\n",transStr[:60])

#print(r.text)