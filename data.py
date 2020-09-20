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

	def showDataPretty(self, data):
		os.system('clear')
		self.title()
		print(json.dumps(data, indent=8))
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

	def checkIfListIsEmpty(self, list):
		for i in list:
			if i:
				return False
		return True

	def getTournamentIdByName(self, dataClass, data, tournamentName):
		return(next((index for (index, tournament) in enumerate(data["tournaments"]) if next(iter(tournament)) == tournamentName), None))

	def addMembersToTournament(self, dataClass, data, tournamentName):
		os.system('clear')
		signedMembers = data["tournaments"][dataClass.getTournamentIdByName(dataClass, data, tournamentName)][tournamentName]["signedMembers"]
		print("""
                **** CREANT INSCRIPCIONS A "{}" - CLUB TENNIS SANTPEDOR ****""".format(tournamentName))

		infoMembers = ""
		for member in data["members"]:
			infoMember = "{}({})     ".format(member["name"], member["id"])
			infoMembers = infoMembers + infoMember
		print("""
				*** Llistat de Sòcis | Total: {} ***

	{}""".format(len(data["members"]), infoMembers))
		print("""
				**** SOCIS INSCRITS A "{}" - CLUB TENNIS SANTPEDOR ****""".format(tournamentName))
		print("""
							Total Socis Inscrits: {}""".format(len(signedMembers)))
		for memberId in signedMembers:
			print("""
					{}({})""".format(dataClass.getMemberById(data["members"], memberId)["name"], dataClass.getMemberById(data["members"], memberId)["id"]))

		memberId = input("""
		Escriu (ID) per inscriure un soci al torneig!.
		Escriu -(ID) per esborrar un soci del torneig!.
		Escriu OK per finalitzar i crear grups: """)
		if memberId == "":
			self.addMembersToTournament(dataClass, data, tournamentName)
		elif not memberId.isnumeric() and memberId.upper() == "OK":
			return signedMembers
		elif memberId.isnumeric() and dataClass.checkIfMemberExistsById(data["members"], memberId):
			if int(memberId) in signedMembers:
				print("""
					El soci {} ja està inscrit al torneig!""".format(self.getMemberById(data["members"], memberId)["name"]))
			else:
				print("""
					Soci {} inscrit al torneig!""".format(self.getMemberById(data["members"], memberId)["name"]))
				data["tournaments"][dataClass.getTournamentIdByName(dataClass, data, tournamentName)][tournamentName]["signedMembers"] += [int(memberId)]
				dataClass.saveData(data)
		elif (memberId[0] == "-") and (memberId[1:].isnumeric()) and dataClass.checkIfMemberExistsById(data["members"], memberId[1:]):
			if int(memberId[1:]) in signedMembers:
				print("""
					Soci {} esborrat del torneig!""".format(self.getMemberById(data["members"], memberId[1:])["name"]))
				signedMemberIndex = signedMembers.index(int(memberId[1:]))
				del signedMembers[signedMemberIndex]
			else:
				print("""
					El soci {} no està inscrit al torneig!""".format(self.getMemberById(data["members"], memberId[1:])["name"]))
		else:
			print("""
					Opció NO vàlida!""")
		time.sleep(1)


		self.addMembersToTournament(dataClass, data, tournamentName)

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
