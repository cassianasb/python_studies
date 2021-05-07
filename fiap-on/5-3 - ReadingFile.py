with open("text.txt", "r") as file:
    content=file.read()
print("Tipo de dado da variável",type(content))
print("\n Conteúdo do arquivo:", content)