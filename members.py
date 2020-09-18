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
		print("""
				Total Socis: {}""".format(len(data["members"])))
		for member in data["members"]:
			print("""
			{}({}) - {}""".format(member["name"], member["id"], member["phone"]))

		option = input("""
		Escriu +Nom Cognom per afegir un soci.
		Escriu -(ID) per el·liminar un socis.
		Escriu *(ID) per modificar el nom d'un soci.
		Prem ENTER per continuar: """)
		if option == "":
			return
		elif (option[0] == "+") and (option[1:] != ""):
		 	self.addMember(option[1:], dataClass, data)
		elif (option[0] == "-") and (option[1:].isnumeric()) and dataClass.checkIfMemberExistsById(data["members"], option[1:]):
			self.removeMember(option[1:], dataClass, data)
		elif (option[0] == "*") and (option[1:].isnumeric()) and dataClass.checkIfMemberExistsById(data["members"], option[1:]):
			self.editMember(option[1:], dataClass, data)
		else:
			print("""
			Opció NO vàlida!""")

		time.sleep(2)
		self.manageMembers(dataClass, data)

	def addMember(self, newMember, dataClass, data):
		phone = input("""
		Afegeix un Núm. de Telèfon o prem ENTER per no afegir-lo ara: """)
		data["members"] += [{"id": self.addNewId(data), "name": newMember, "phone": phone if len(phone) == 9 else ""}]
		dataClass.saveData(data)
		print("""
			Soci {} afegit!""".format(newMember))
		if len(phone) == 9:
			print("""
			Telèfon {} afegit!""".format(phone))
		else:
			print("""
			La llargada del Telèfon {} és incorrecta. No s'ha afegit cap Telèfon!""".format(phone))
		time.sleep(2)

	def addNewId(self, data):
		if data["members"] == []:
			return 1
		return (data["members"][-1]["id"] + 1)

	def removeMember(self, id, dataClass, data):
		print("""
			Soci {} el·liminat!""".format(dataClass.getMemberById(data["members"], id)["name"]))
		for index in range(len(data["members"])):
			if data["members"][index]['id'] == int(id):
				del data["members"][index]
				break
		dataClass.saveData(data)

	def editMember(self, id, dataClass, data):
		print("""
			Vol modificar el soci {}. {}!""".format(id, dataClass.getMemberById(data["members"], id)["name"]))
		name = input("""
		Escriu el nou Nom Cognom o prem ENTER per deixar-ho com està: """)
		phone = input("""
		Escriu el nou Núm. de Telèfon o prem ENTER per deixar-ho com està: """)
		for index in range(len(data["members"])):
			if data["members"][index]['id'] == int(id):
				if name != "":
					data["members"][index]["name"] = name
					print("""
			Nom Cognom modificat correctament: {}.""".format(name))
				if phone != "":
					if len(phone) == 9:
						data["members"][index]["phone"] = phone
						print("""
			Telèfon modificat correctament: {}.""".format(phone))
					else:
						print("""
			La llargada del Telèfon {} és incorrecta""".format(phone))
				time.sleep(2)
				break
		dataClass.saveData(data)
