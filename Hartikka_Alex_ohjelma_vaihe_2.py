# Ohjelmointiprojekti - Matti Meikäläinen
from math import e
import random
from typing import NoReturn
# Osion 1 funktio


def Osio1():
    print("-- Osio 1 --")
    num1 = int(input("Give num 1: "))
    num2 = int(input("Give num 2: "))
    # Kahden numeron summa
    numSum = num1 + num2
    print(f"Tulos {numSum}")

# Osion 2 funktio


def Osio2():
    print("-- Osio 2 --")
    months = int(input("Kuinka monelta kuukaudelta saat opintotukea? "))
    amount = float(input("Kuinka paljon rahaa saat per kuukaus? "))
    amountYears = months * amount
    print(f"You get {amountYears: 3} in a year.")

    # en oppinut mitään uutta muuttujista ja tyypestä mitään uutta.


# Osion 3 funktio
def Osio3():
    print("-- Osio 3 --")

    def menu():
        print(""""
    =======================
    | 1 - Plus-laskin     |
    | 2 - Opintotuki      |
    | 3 - Ohjeet          |
    | 4 - Nelilaskin      |
    | 5 - Prime number    |
    | 6 - IP address      |
    | 7 - Random numbers  |
    | 8 - Init file       |
    | 9 - IPAddress       |
    | 10 - Sysmonitor     |
    =======================
    """)

    def main3():
        menu()
        try:
            userInput = int(input("Valitse toiminto 1-10: "))
        except Exception as e:
            print("ANNA NUMERO!!!!!!!!!!!!")
            main3()

        if(userInput == 1):
            Osio1()

        elif (userInput == 2):
            Osio2()

        elif (userInput == 3):
            menu()

        elif (userInput == 4):
            powerInput = int(input("Anna luku: "))
            outNum = powerInput**2
            print(f"Luvun {powerInput} neliö {outNum}")

        elif (userInput == 5):
            Osio5()
        elif (userInput == 6):
            Osio6()
        elif (userInput == 7):
            Osio7()
        elif (userInput == 8):
            Osio8()
        elif (userInput == 9):
            Osio9()
        elif (userInput == 10):
            Osio10()
        else:
            print("Anna 1-10")
            main3()


# Osion 4 funktio
def Osio4():
    print("-- Osio 4 --")

    userInput1 = int(input("Anna luku 1: "))
    userInput2 = int(input("Anna luku 2: "))

    # Käyttäjän annetuille numeroille tehdään erinlaisia matemaattisia operaatioita
    sumNum = userInput1 + userInput2

    difNum1 = userInput1 - userInput2
    difNum2 = userInput2 - userInput1

    timesNum = userInput1 * userInput2

    revNum1 = userInput1 / userInput2
    revNum2 = userInput2 / userInput1

    divNum1 = userInput1 % userInput2
    divNum2 = userInput2 % userInput1

    print(f"""
{userInput1} + {userInput2} = {sumNum}
{userInput1} - {userInput2} = {difNum1}
{userInput2} - {userInput1} = {difNum2}
{userInput1} * {userInput2} = {timesNum}
{userInput1} / {userInput2} = {revNum2: 2}
{userInput2} / {userInput1} = {revNum1: 2}
{userInput1} % {userInput2} = {divNum2}
{userInput2} % {userInput1} = {divNum1}
	""")


# Osion 5 funktio
def Osio5():
    print("-- Osio 5 --")

# Aina unohtuu miten alkuluvun tarkistus tehdään.

    userInput = int(input("Anna alkuluku: "))
    if userInput > 1:

        for i in range(2, userInput):
            if (userInput % i == 0):
                print(f"{userInput} ei ole alkuluku")
                break
        else:
            print(f"{userInput} on alkuluku")


def Osio6():
    nigerianIPs = []
    ipAddresses = {
        "1.172.152.0 / 21": "Finland",
        "31.204.64.96 / 27": "Finland",
        "31.204.65.64 / 27": "Finland",
        "41.57.120.0 / 22": "Nigeria",
        "31.204.66.96 / 27": "Finland",
        "41.58.0.0 / 16": "Nigeria",
        "31.217.192.0 / 21": "Finland",
        "32.42.29.136 / 29": "Finland",
        "32.106.148.0 / 24": "Finland",
        "41.67.128.0 / 18": "Nigeria",
        "32.106.181.0 / 24": "Finland",
        "32.106.182.0 / 24": "Finland"
    }

    # listat on tuttuja
    # Käydään lista läpi
    for ip, country in ipAddresses.items():
        # Jos maa on Nigeria niin lisätään ip uuteen listaan
        if country == "Nigeria":
            nigerianIPs.append(ip)

    for i in nigerianIPs:
        print(i)


def Osio7():

    randNumList = []

    def randomInt():
        # luo 40 numeroa -10 ja 10 väliltä.
        for i in range(40):
            randInt = random.randrange(-10, 10)
            randNumList.append(randInt)
    # Funktiot tarkastaa onko numero parillinen,pariton jne

    def Odds(randList):
        for i in randList:
            if(i % 2 != 0):
                print(i)

    def Evens(randList):
        for i in randList:
            if(i % 2 == 0):
                print(i)

    def Positives(randList):
        for i in randList:
            if(i > 0):
                print(i)

    def Negatives(randList):
        for i in randList:
            if(i < 0):
                print(i)

    def HowManyZeros(randList):
        count = 0
        for i in randList:
            if (i == 0):
                count += 1
        print(count)

    def main():
        randomInt()
        print(randNumList)
        Odds(randNumList)
        Evens(randNumList)
        Positives(randNumList)
        Negatives(randNumList)
        HowManyZeros(randNumList)

    main()


def Osio8():
    import time

    # Ei isompia ongelmia.
    # print(fileName)
    # Milloin tiedostoa muokataan.
    modTime = time.strftime("%d %I %Y")
    # kysyy erinlaisia tietoja käyttäjältä
    fileNameInput = input("File name: ") or "program"
    nameInput = input("Name: ")
    orgInput = input("Org: ")
    serverIpInput = input("Server IP: ")
    portInput = input("Port Number: ")
    databaseNameInput = input("database file name: ")

    writeToFileString = f"""; last modified {modTime} by {nameInput}
[owner]
name={nameInput}
organization={orgInput}

[database]
; use IP address in case network name resolution is not working
server={serverIpInput}
port={portInput}
file='{databaseNameInput}'"""
    # Tallentaa tiedoston
    fileName = f"{fileNameInput}.ini"
    with open(fileName, "w") as f:
        f.write(writeToFileString)


def Osio9():
    IPAddressList = []

    def askInfo():
        while True:
            addIP = input("Do you want to add IP address? y or n ")
            if addIP.lower() == "y":
                ipaddress = input("IP address: ")
                hostname = input("Hostname: ")
                asn = input("ASN: ")
                isp = input("ISP: ")
                ipObject = IPAddress(ipaddress, hostname, asn, isp)
                IPAddressList.append(ipObject)
                for i in IPAddressList:
                    print(i.showInfo())

            elif addIP.lower() == "n":
                break

    # Luodaan IPAddress luokka

    class IPAddress():

        def __init__(self, ipaddress, hostname, asn, isp):
            self.ipaddress = ipaddress
            self.hostname = hostname
            self.asn = asn
            self.isp = isp

        # Printataan tiedot
        def showInfo(self):
            print("=======================")
            print(f"IP address {self.ipaddress}")
            print(f"Hostname {self.hostname}")
            print(f"ASN {self.asn}")
            print(f"ISP {self.isp}")
            print("=======================")

    askInfo()


def Osio10():

    # importit on hallussa.

    import psutil
    print("=======================")
    print(psutil.net_io_counters(pernic=True))
    print("=======================")
    print(psutil.net_connections())
    print("=======================")
    print(psutil.net_if_addrs())
    print("=======================")
    print(psutil.net_if_stats())
    print("=======================")


def Osio11():
    import pandas as pd

    # En tiedä miksi tämä on tässä mutta antaa sen nyt olla.

    df = pd.read_csv("geoip2-ipv4_csv.csv")
    # Etsitään ip-osoiteet jossa on 91.226
    df = df[df["network"].str.contains("^91.226")]
    # print(df.filter(["network", "country_name"]).shape)
    # Etsitään Aasiassa olevat ip osoitteet
    df.query("continent_name == 'Asia'", inplace=True)
    filteredData = df.filter(["network", "country_name"])
    print(filteredData)
    filteredData.to_csv("Hartikka_Alex_filtered_ips.csv",
                        encoding="utf-8", index=False)


Osio3()

# NOW WITH COMMENTS!!!
