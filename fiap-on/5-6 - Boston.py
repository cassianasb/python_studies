with open("indicators.csv", "r") as indicators:
    internationalFlights = 0
    biggerDate = 0
    passangers = 0
    mediaDaily = 0
    userYear = input("Qual ano deseja pesquisar? ")
    for line in indicators.readlines[1:-1]:
        infos = line.split(",")
        internationalFlights += int(infos[3])
        if userYear == infos[0]:
            passangers += int(infos[2])
            if float(infos[5]) > mediaDaily:
                mediaDaily = infos[5]
                monthMediaDaily = info[1]
        if int(infos[2]) > int(biggerDate):
            biggerDate = infos[2]
            year = infos[0]
            month = infos[1]
    print("O total de voos internacionais é ", internationalFlights)
    print("O total de passageiros do ano ", userYear, " foi de ", passangers)
    print("O mês/ano mais movimentado no aeroporto foi: ", str(month),"/", str(year))
    print("O mês do ano ", userYear, " com maior médiapara diária de hotel foi ", monthMediaDaily)