import os, time

class Members:

	def title(self):
		print("""

		***** SOCIS - CLUB TENNIS SANTPEDOR *****""")

	def membersMenu(self, dataClass, data):
		os.system('clear')
		self.title()
		for index, options in enumerate(data["menu-options"][1][1]):
			print("""
			{}. {}""".format(index, options))
		option = input("""
		Selecciona una opció: """)
		if option == '1':
		    self.manageMembers(dataClass, data)
		elif option == '0':
			return 1
		else:
			print("""
			Opció NO vàlida!""")
			time.sleep(1)
		self.membersMenu(dataClass, data)

	def manageMembers(self, dataClass, data):
		os.system('clear')
		self.title()
		for id, member in enumerate(data["members"]):
			print("""
			{} {}""".format(id, member))

		option = input("""
		Escriu +Nom Cognom per afegir un soci.
		Escriu -ID per el·liminar un socis.
		Escriu *ID per modificar el nom d'un soci.
		Prem ENTER per continuar: """)
		if option == "":
			return
		elif (option[0] == "+") and (option[1:] != ""):
		 	self.addMember(option[1:], dataClass, data)
		elif (option[0] == "-") and (option[1:].isnumeric()) and (int(option[1:]) in range(len(data["members"]))):
			self.removeMember(option[1:], dataClass, data)
		else:
			print("""
			Opció NO vàlida!""")

		time.sleep(2)
		self.manageMembers(dataClass, data)

	def addMember(self, newMember, dataClass, data):
		data["members"] += [newMember]
		dataClass.saveData(data)
		print("""
			Soci {} afegit!""".format(newMember))

	def removeMember(self, id, dataClass, data):
		print("""
			Soci {} el·liminat!""".format(data["members"][int(id)]))
		del data["members"][int(id)]
		dataClass.saveData(data)

	def editMember(self):
		pass
