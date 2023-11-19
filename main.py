meme_dict = {"CRINGE":"garip ya da utandırıcı bir şey",
"LOL":"komik bi şeye verilen cevap",
"ROFL":"bir şakaya karşılık cevap",
"AGGRO":"agresifleşmek"}

word =input("bilmediğiniz bir kelime yazın").upper()
if word in meme_dict.keys():
 print(meme_dict[word]) 
else:
    print("bu kelime bizde yok")
