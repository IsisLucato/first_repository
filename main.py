meme_dict = {
            "CRINGE: "algo vergonhoso ou constrangedor",
            "STALKEAR: "investigar a vida de alguém on-line",
            "FLOPAR: "fracassar ou não alcançar o sucesso na mídia",
            "RANÇO: "desprezo ou ódio por algo ou alguém",
            "RED FLAG: "usada para identificar sinais de alerta ou indícios de algo negativo"
            }
word = input("Digite uma palavra usada atualmente que você não entende o significado (em letras maiúsculas!)")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Essa palavra não está no nosso banco de palavras!")
