with open("page.html", "w") as page:
    page.write("<body> <h1> Esta é um teste para página WEB </h1>")
    page.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:  </h2>")
    page.write("<h3>")
    text=""
    while text!="SAIR":
        text = input("Digite um nome ou SAIR: ").upper()
        if text!="SAIR":
            page.write("<br>"+text)
    page.write("</h3></body>")

with open("page.html", "r") as page:
    print(page.read())