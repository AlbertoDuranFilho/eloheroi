nomeHeroi = input("Digite o nome do Herói: ")
xpHeroi = int(input("Digite a quantidade de XP do Héroi: "))
patenteHeroi = ''

if(xpHeroi < 1000):
    patenteHeroi = 'Ferro'

elif(1001 <= xpHeroi < 2000):
    patenteHeroi = 'Bronze'

elif(2000 <= xpHeroi < 5000):
    patenteHeroi = 'Prata'

elif(5000 <= xpHeroi < 7000):
    patenteHeroi = 'Ouro'

elif(7000 <= xpHeroi < 8000):
    patenteHeroi = 'Platina'

elif(8000 <= xpHeroi < 9000):
    patenteHeroi = 'Ascendente'

elif(9000 <= xpHeroi < 10000):
    patenteHeroi = 'Imortal'

elif(xpHeroi > 10000):
    patenteHeroi = 'Radiante'

else:
    print("Valor do XP do Herói inválido! Por favor digite um valor válido.")

if(patenteHeroi != ''): 
    print(f"O Herói de nome {nomeHeroi} está no nível de {patenteHeroi}")