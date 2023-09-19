        #WetterInAmerika 
        #Sagiv Salmanov
    #input temperatur solange Antwort eine Zahl ist
temperaturF = input("Geben sie die Temperatur in F ein: ")
while not temperaturF.isdigit():
    temperaturF = input("Antwort muss eine Zahl sein.\nGeben sie die Temperatur in F ein: ")
temperaturF = int(temperaturF)
    #input scheint die sonne solange es y oder n ist
sonne = input("Scheint die Sonne (y/n)?: ")
while sonne != "y" and sonne != "n":
    sonne = input("Antwort muss entweder 'y' oder 'n' sein.\nScheint die Sonne (y/n)?: ")
    #inout niederschlag zu erwarten solange es y oder n ist
niederschlag = input("Ist Niederschlag zu erwarten (y/n)?: ")
while niederschlag != "y" and niederschlag != "n":
    niederschlag = input("Antwort muss entweder 'y' oder 'n' sein.\nIst Niederschlag zu erwarten (y/n)?: ")
    #temperatur umrechnung
temperaturC = (temperaturF - 32) * 5/9
print(f"Die Temperatur {temperaturF}F beträgt {round(temperaturC,2)}C.")
    #wenn niederschlag zu erwarten ist, dann soll am ende 'und ein Regenschirm' stehen
if niederschlag=="n":
    regenschirm=''
    komma=' und'
else:
    regenschirm='und ein Regenschirm '
    komma=','
    #wenn sonne zu erwarten ist, dann soll 'und ein hut', oder ', ein hut' stehen
if sonne=='y':
    hut=f'{komma} ein Hut'
    komma=', '
else:
    hut=''
    #kleidungsempfehlung nach temperatur
if(temperaturC<=0):
    kleidung=f'Eine Winterjacke{komma} eine lange Hose{hut}'
elif(temperaturC>0 and temperaturC<20):
    kleidung=f'Ein Hemd{komma} eine Lange Hose{hut}'
else:
    kleidung=f'Ein Tshirt{komma} eine kurze Hose{hut}'
    #ausgabe
print(f"Es wird {kleidung} {regenschirm}empfehlt")

#wenn niederschlag zu erwarten ist, dann sollte in der mitte kein 'und' stehen, also wird es zu einem ', ' umgewandelt.
# Es wird Eine Winterjacke,  eine lange Hose und ein Hut empfehlt ---> Es wird Eine Winterjacke,  eine lange Hose, ein Hut und ein Regenschirm empfehlt
#                                             ^                                                                  ^

