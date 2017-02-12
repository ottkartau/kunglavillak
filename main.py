from appJar import gui

def buttonCallback(buttonName):
	global appGui
	print(buttonName)
	if buttonName == "teema4_100":
		appGui.infoBox("Question", "When did Britney Spears release \"Oops, I did it again?\"")
		appGui.setButtonState("teema4_100", "disabled")


def setupGui():
	global appGui  
	appGui.addStatusbar(fields = 2)
	appGui.setStatusbarBg("gray", 0)
	appGui.setStatusbarFg("black", 0)

	appGui.addLabel("villakLabel", "Kuldvillak", 0, 0, 5)
	appGui.addLabel("teema1Label", "Fauna", 1, 0)
	appGui.addLabel("teema2Label", "Flora", 1, 1)
	appGui.addLabel("teema3Label", "Autod", 1, 2)
	appGui.addLabel("teema4Label", "Naised", 1, 3)
	appGui.addLabel("teema5Label", "Mehed", 1, 4)

	appGui.addNamedButton("100", "teema1_100", buttonCallback, 2, 0)
	appGui.setButtonBg("teema1_100", "yellow")
	appGui.setButtonActiveBg("teema1_100", "yellow")
	appGui.setButtonInactiveBg("teema1_100", "yellow")

	appGui.addNamedButton("200", "teema1_200", buttonCallback, 3, 0)
	appGui.addNamedButton("300", "teema1_300", buttonCallback, 4, 0)
	appGui.addNamedButton("400", "teema1_400", buttonCallback, 5, 0)
	appGui.addNamedButton("500", "teema1_500", buttonCallback, 6, 0)

	appGui.addNamedButton("100", "teema2_100", buttonCallback, 2, 1)
	appGui.addNamedButton("200", "teema2_200", buttonCallback, 3, 1)
	appGui.addNamedButton("300", "teema2_300", buttonCallback, 4, 1)
	appGui.addNamedButton("400", "teema2_400", buttonCallback, 5, 1)
	appGui.addNamedButton("500", "teema2_500", buttonCallback, 6, 1)

	appGui.addNamedButton("100", "teema3_100", buttonCallback, 2, 2)
	appGui.addNamedButton("200", "teema3_200", buttonCallback, 3, 2)
	appGui.addNamedButton("300", "teema3_300", buttonCallback, 4, 2)
	appGui.addNamedButton("400", "teema3_400", buttonCallback, 5, 2)
	appGui.addNamedButton("500", "teema3_500", buttonCallback, 6, 2)

	appGui.addNamedButton("100", "teema4_100", buttonCallback, 2, 3)
	appGui.setButtonDisabledBg("teema4_100", "yellow")
	appGui.addNamedButton("200", "teema4_200", buttonCallback, 3, 3)
	appGui.addNamedButton("300", "teema4_300", buttonCallback, 4, 3)
	appGui.addNamedButton("400", "teema4_400", buttonCallback, 5, 3)
	appGui.addNamedButton("500", "teema4_500", buttonCallback, 6, 3)

	appGui.addNamedButton("100", "teema5_100", buttonCallback, 2, 4)
	appGui.addNamedButton("200", "teema5_200", buttonCallback, 3, 4)
	appGui.addNamedButton("300", "teema5_300", buttonCallback, 4, 4)
	appGui.addNamedButton("400", "teema5_400", buttonCallback, 5, 4)
	appGui.addNamedButton("500", "teema5_500", buttonCallback, 6, 4)

	appGui.setPadding([20,20])
	appGui.setInPadding([20,20])
	appGui.setFont(40)
	appGui.setTitle("KunglaVillak")
	appGui.setGeometry("fullscreen")
	appGui.setBg("blue")
	appGui.setAllButtonWidths(500)

appGui = gui()
setupGui()
appGui.go()
