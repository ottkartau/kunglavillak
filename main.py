from appJar import gui
import threading
import random

def hõbevillak():
        random_teema = random.choice(["teema1_", "teema2_", "teema3_", "teema4_", "teema5_"])
        random_punktid = random.choice(["100", "200", "300", "400"])
        boonusruut = str(random_teema + random_punktid)
        print (boonusruut)




def buttonCallback(buttonName):
        print(buttonName)

        if buttonName == "boonusruut" :
                appGui.removeButton("boonusruut")
                appGui.infoBox("Hõbevillak", "Mis on teie panus?")
        questions = open("kysimused.txt", "r")
        if buttonName == "teema1_100":
                appGui.removeButton("teema1_100")
                appGui.infoBox("Küsimus", str(questions.readlines()[0]))
                
        if buttonName == "teema1_200":
                appGui.removeButton("teema1_200")
                appGui.infoBox("Küsimus", str(questions.readlines()[1]))

        if buttonName == "teema1_300":
                appGui.removeButton("teema1_300")
                appGui.infoBox("Küsimus", str(questions.readlines()[2]))

        if buttonName == "teema1_400":
                appGui.removeButton("teema1_400")
                appGui.infoBox("Küsimus", str(questions.readlines()[3]))

        if buttonName == "teema2_100":
                appGui.removeButton("teema2_100")
                appGui.infoBox("Küsimus", str(questions.readlines()[5]))
                
        if buttonName == "teema2_200":
                appGui.removeButton("teema2_200")
                appGui.infoBox("Küsimus", str(questions.readlines()[6]))

        if buttonName == "teema2_300":
                appGui.removeButton("teema2_300")
                appGui.infoBox("Küsimus", str(questions.readlines()[7]))

        if buttonName == "teema2_400":
                appGui.removeButton("teema2_400")
                appGui.infoBox("Küsimus", str(questions.readlines()[8]))

        if buttonName == "teema3_100":
                appGui.removeButton("teema3_100")
                appGui.infoBox("Küsimus", str(questions.readlines()[10]))
                
        if buttonName == "teema3_200":
                appGui.removeButton("teema3_200")
                appGui.infoBox("Küsimus", str(questions.readlines()[11]))

        if buttonName == "teema3_300":
                appGui.removeButton("teema3_300")
                appGui.infoBox("Küsimus", str(questions.readlines()[12]))

        if buttonName == "teema3_400":
                appGui.removeButton("teema3_400")
                appGui.infoBox("Küsimus", str(questions.readlines()[13]))

        if buttonName == "teema4_100":
                appGui.removeButton("teema4_100")
                appGui.infoBox("Küsimus", str(questions.readlines()[15]))
                
        if buttonName == "teema4_200":
                appGui.removeButton("teema4_200")
                appGui.infoBox("Küsimus", str(questions.readlines()[16]))

        if buttonName == "teema4_300":
                appGui.removeButton("teema4_300")
                appGui.infoBox("Küsimus", str(questions.readlines()[17]))

        if buttonName == "teema4_400":
                appGui.removeButton("teema4_400")
                appGui.infoBox("Küsimus", str(questions.readlines()[18]))

        if buttonName == "teema5_100":
                appGui.removeButton("teema5_100")
                appGui.infoBox("Küsimus", str(questions.readlines()[20]))
                
        if buttonName == "teema5_200":
                appGui.removeButton("teema5_200")
                appGui.infoBox("Küsimus", str(questions.readlines()[21]))

        if buttonName == "teema5_300":
                appGui.removeButton("teema5_300")
                appGui.infoBox("Küsimus", str(questions.readlines()[22]))

        if buttonName == "teema5_400":
                appGui.removeButton("teema5_400")
                appGui.infoBox("Küsimus", str(questions.readlines()[23]))
                
        questions.close()

def setupGui():
        global appGui

        appGui.setPadX(1)
        appGui.setPadY()

        appGui.addStatusbar(fields = 2)
        appGui.setStatusbarBg("gray", 0)
        appGui.setStatusbarFg("black", 0)

        appGui.addLabel("VillakLabel", "Kuldvillak", 0, 0, 5)        
        appGui.addLabel("teema1Label", "Fauna", 1, 0)
        appGui.addLabel("teema2Label", "Flora", 1, 1)
        appGui.addLabel("teema3Label", "Autod", 1, 2)
        appGui.addLabel("teema4Label", "Beibed", 1,3)
        appGui.addLabel("teema5Label", "Mehed", 1,4)
        
        appGui.addNamedButton("100", "teema1_100", buttonCallback, 2, 0)
        appGui.addNamedButton("200", "teema1_200", buttonCallback, 3, 0)
        appGui.addNamedButton("300", "teema1_300", buttonCallback, 4, 0)
        appGui.addNamedButton("400", "teema1_400", buttonCallback, 5, 0)

        appGui.addNamedButton("100", "teema2_100", buttonCallback, 2, 1)
        appGui.addNamedButton("200", "teema2_200", buttonCallback, 3, 1)
        appGui.addNamedButton("300", "teema2_300", buttonCallback, 4, 1)
        appGui.addNamedButton("400", "teema2_400", buttonCallback, 5, 1)

        appGui.addNamedButton("100", "teema3_100", buttonCallback, 2, 2)
        appGui.addNamedButton("200", "teema3_200", buttonCallback, 3, 2)
        appGui.addNamedButton("300", "teema3_300", buttonCallback, 4, 2)
        appGui.addNamedButton("400", "teema3_400", buttonCallback, 5, 2)

        appGui.addNamedButton("100", "teema4_100", buttonCallback, 2, 3)
        appGui.addNamedButton("200", "teema4_200", buttonCallback, 3, 3)
        appGui.addNamedButton("300", "teema4_300", buttonCallback, 4, 3)
        appGui.addNamedButton("400", "teema4_400", buttonCallback, 5, 3)

        appGui.addNamedButton("100", "teema5_100", buttonCallback, 2, 4)
        appGui.addNamedButton("200", "teema5_200", buttonCallback, 3, 4)
        appGui.addNamedButton("300", "teema5_300", buttonCallback, 4, 4)
        appGui.addNamedButton("400", "teema5_400", buttonCallback, 5, 4)
        
        appGui.setFont("40")
        appGui.setBg("blue")
        appGui.setGeom("fullscreen")
        appGui.setTitle("Villak")       
        appGui.setTransparency(98)
        appGui.setButtonFont(20, "Arial")

def one_minute():
        appGui.infoBox("1 minut", "Mänguosa lõpuni on jäänud 1 minut!")
        print("1 minut")

def stop():
        appGui.infoBox("lõpp", "Mänguosa on lõppenud!")
        print("lõpp")
        appGui.removeAllWidgets()
        appGui.addNamedButton("hõbevillak","Hõbevillak")
        
        


minute = threading.Timer(240, one_minute)
end = threading.Timer(300, stop)

hõbevillak()
minute.start()
end.start()
appGui = gui()
setupGui()
appGui.go()







