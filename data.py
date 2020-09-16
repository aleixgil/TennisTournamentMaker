#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json, os

class Data:

	def __init__(self):
		# self.resetData()
		self.data = self.readData()
		# self.showDataPretty()
		# self.data["prova"] = []
		# self.saveData(self.data)
		# self.showDataPretty()

	def title(self):
		print("""

		***** DADES LOCALS | CLUB TENNIS SANTPEDOR *****""")

	def readData(self):
		with open('data.txt') as json_file:
			data = json.load(json_file)
			json_file.close()
		return data

	def saveData(self, data):
		with open('data.txt', 'w') as outfile:
			json.dump(data, outfile)
			outfile.close()

	def getData(self):
		return self.data

	def resetData(self):
		data = {}
		data["menu-options"] = [
			["Sortir!"],
			["Gestionar Socis", [
				"Tornar al Menú Principal",
				"Afegir/El·liminar/Modificar Socis",
				"Ordre Rànquing"
				]
			]
		]
		data["members"] = []
		data["tournaments"] = []

		with open('data.txt', 'w') as outfile:
			json.dump(data, outfile)
			outfile.close()

	def showDataPretty(self):
		os.system('clear')
		self.title()
		print(json.dumps(self.data, indent=8))
		input("""
		Prem ENTER per continuar: """)


# storage = {
# 	"menu-options": [
# 		"Sortir!",
# 		"Gestionar Socis"
# 	],
# 	"members": ["PLAYER 1", "PLAYER 2", "PLAYER 3", "PLAYER 4"],
# 	"tournaments": {
# 		"especial-2020": {
# 			"players": ["PLAYER 1", "PLAYER 2", "PLAYER 3"],
# 			"groups": ["GROUP1", "GROUP2"]
# 		}
# 	}
# }
