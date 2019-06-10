def funcao():
    texto = input("html")
    novaString = ""
    for x in texto:
        if x=="<":
            novaString+="&lt"
        elif x==">":
            novaString+="&gt"
        else:
            novaString+=x

    print(novaString)

funcao()
