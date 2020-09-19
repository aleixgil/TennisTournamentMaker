#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json, os, time

class Data:

	def __init__(self):
		self.initData()

	def title(self):
		print("""

		***** DADES LOCALS | CLUB TENNIS SANTPEDOR *****""")

	def initData(self):
		if not os.path.exists('data.txt'):
			self.resetData()
			os.system('clear')
			print("""
			Fitxer de dades creat!""")
			time.sleep(2)


	def readData(self):
		with open('data.txt') as json_file:
			data = json.load(json_file)
			json_file.close()
		return data

	def saveData(self, data):
		with open('data.txt', 'w') as outfile:
			json.dump(data, outfile)
			outfile.close()

	def resetData(self):
		data = {}
		data["menu-options"] = [
			["Sortir!"],
			["Gestionar Socis", [
				"Tornar al Menú Principal",
				"Afegir/El·liminar/Modificar Socis"
				]
			],
			["Gestionar Torneigs", [
				["Tornar al Menú Principal"],
				["Gestionar Rànquing"],
				["Gestionar Torneig", [
					"Tornar al Menú Anterior",
					"Gestionar Grups",
					"Gestionar Eliminatories"
					]
				],
				["Crear Torneig", [
					"Tornar al Menú Anterior",
					"Crear Grups",
					"Crear El·liminatories"
					]
				],
				["El·liminar Torneig"]]
			]
		]
		data["members"] = [] # [{id: 0, name: "player 1", phone: "123456789"}, {id: 1, name: "player 2", phone: "987654321"}]
		data["rank"] = [] # [id, id, id, ...]
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

	def getMemberById(self, members, id):
		return(next((member for member in members if member["id"] == int(id)), None))

	def getMemberByName(self, members, name):
		return(next((member for member in members if member["name"] == name), None))

	def checkIfMemberExistsById(self, members, id):
		if next((member for member in members if member["id"] == int(id)), None) == None:
			return False
		return True

	def checkifTournamentExists(self, tournaments, tournamentName):
		for tournament in tournaments:
			if next(iter(tournament)) == tournamentName:
				return True
		return False

# data = {
# 	"menu-options": [
# 		"Sortir!",
# 		"Gestionar Socis"
# 	],
# 	"members": ["PLAYER 1", "PLAYER 2", "PLAYER 3", "PLAYER 4"],
#	"actual-rank": [id, id, id, ...]
# 	"tournaments": {
# 		"especial-2020": {
# 			"players": [id, id, id, ...],
# 			"groups": ["GROUP1", "GROUP2"]
# 		}
# 	}
# }
