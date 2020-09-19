import os, time

class Tournaments:

    def title(self):
        print("""

		***** TORNEIGS - CLUB TENNIS SANTPEDOR *****""")

    def tournamentsMenu(self, dataClass, data):
        os.system('clear')
        self.title()
        for index, options in enumerate(data["menu-options"][2][1]):
            print("""
                        {}. {}""".format(index, options[0]))
        option = input("""
                Selecciona una opció: """)
        if option == '1':
            self.manageRank(dataClass, data)
        elif option == '2':
            self.manageTournamentMenu(dataClass, data)
        elif option == '3':
            self.createTournamentMenu(dataClass, data)
        elif option == '4':
            self.removeTournament(dataClass, data)
        elif option == '0':
            return 1
        else:
            print("""
                        Opció NO vàlida!""")
            time.sleep(1)
        self.tournamentsMenu(dataClass, data)

    def manageRank(self, dataClass, data):
        os.system('clear')
        self.title()
        infoMembers = ""
        for member in data["members"]:
            infoMember = "{}({})     ".format(member["name"], member["id"])
            infoMembers = infoMembers + infoMember
        print("""
                    *** Llistat de Sòcis | Total: {} ***

        {}""".format(len(data["members"]), infoMembers))

        print("""
                    **** RÀNQUING - CLUB TENNIS SANTPEDOR ****""")
        print("""
                            Total Socis al Rànquing: {}""".format(len(data["rank"])))
        for index, member in enumerate(data["rank"]):
            print("""
                        {}. {}({})""".format(index+1, member, dataClass.getMemberByName(data["members"], member)["id"]))

        option = input("""
		Escriu +(ID) per afegir un soci al rànquing.
		Escriu -(ID) per el·liminar un socis del rànquing.
		Escriu *(ID) per modificar la posició d'un soci al rànquing.
		Prem ENTER per continuar: """)
        if option == "":
            return
        elif (option[0] == "+") and (option[1:].isnumeric()) and dataClass.checkIfMemberExistsById(data["members"], option[1:]):
            self.addRankMember(option[1:], dataClass, data)
        elif (option[0] == "-") and (option[1:].isnumeric()) and dataClass.checkIfMemberExistsById(data["members"], option[1:]):
            self.removeRankMember(option[1:], dataClass, data)
        elif (option[0] == "*") and (option[1:].isnumeric()) and dataClass.checkIfMemberExistsById(data["members"], option[1:]):
            self.changePosRankMember(option[1:], dataClass, data)
        else:
            print("""
                    Opció NO vàlida!""")

        time.sleep(2)
        self.manageRank(dataClass, data)

    def addRankMember(self, id, dataClass, data):
        memberName = dataClass.getMemberById(data["members"], id)["name"]
        if memberName in data["rank"]:
            print("""
                    ERROR! El soci {} ja està al Rànquing!""".format(memberName))
            time.sleep(1)
        else:
            data["rank"] += [memberName]
            dataClass.saveData(data)
            print("""
                    Soci {} afegit al Rànquing!""".format(memberName))

    def removeRankMember(self, id, dataClass, data):
        memberName = dataClass.getMemberById(data["members"], id)["name"]
        if memberName in data["rank"]:
            del data["rank"][data["rank"].index(memberName)]
            dataClass.saveData(data)
            print("""
                    Soci {} el·liminat del Rànquing!""".format(memberName))
        else:
            print("""
                    ERROR! El soci {} no està apuntat al Rànquing!""".format(memberName))
            time.sleep(1)

    def changePosRankMember(self, id, dataClass, data):
        memberName = dataClass.getMemberById(data["members"], id)["name"]
        newPosition = input("""
                Indica a quina posició vols canviar al Soci {}: """.format(memberName))
        if newPosition.isnumeric() and (0 < int(newPosition) <= len(data["rank"])):
            oldPosition = data["rank"].index(memberName)
            del data["rank"][oldPosition]
            data["rank"].insert(int(newPosition)-1, memberName)
            dataClass.saveData(data)
            print("""
                    Posició del Soci {} canviada de {} -> {}!""".format(memberName, oldPosition, newPosition))
        else:
            print("""
                    ERROR! No existeix aquesta posició!""")
            time.sleep(1)

    def manageTournamentMenu(self, dataClass, data):
        pass


    def titleCreateTournament(self):
        print("""

		***** CREAR TORNEIG - CLUB TENNIS SANTPEDOR *****""")

    def createTournamentMenu(self, dataClass, data):
        os.system('clear')
        self.titleCreateTournament()

        checkIfCurrentTournament = input("""
                Vols seleccionar un torneig existent (y/n o ENTER per tirar enrere)?: """)
        if checkIfCurrentTournament == "y":
            for index, tournament in enumerate(data["tournaments"]):
                print("""
                        {}({})""".format(next(iter(tournament)), index))
            currentTournamentIndex = input("""
                Selecciona una (ID) de torneig: """)

            if currentTournamentIndex.isnumeric() and (0 <= int(currentTournamentIndex) < len(data["tournaments"])):
                tournament = data["tournaments"][int(currentTournamentIndex)]
                print("""
                        Has seleccionat el torneig {}!""".format(next(iter(tournament))))
            else:
                print("""
                            Opció NO vàlida!""")
                time.sleep(1)
                return 1

        elif checkIfCurrentTournament == "n":
            tournamentName = input("""
                    Escriu el nom del torneig que vols començar: """)
            if dataClass.checkifTournamentExists(data["tournaments"], tournamentName):
                print("""
                        El torneig {} ja existeix!""".format(tournamentName))
                time.sleep(1)
                return 1
            tournament = { tournamentName: { "groups": {}, "brackets": {}} }
            data["tournaments"] += [tournament]
            print("""
                        Torneig {} creat!""".format(tournamentName))
        elif checkIfCurrentTournament == "":
            return 1
        else:
            print("""
                        Opció NO vàlida!""")
            time.sleep(1)

        if checkIfCurrentTournament == "y" or checkIfCurrentTournament == "n":
            for index, options in enumerate(data["menu-options"][2][1][3][1]):
                print("""
                            {}. {}""".format(index, options))
            option = input("""
                    Selecciona una opció: """)
            if option == '1':
                self.createGroups(self, dataClass, data, tournament)
                return 1
            elif option == '0':
                dataClass.saveData(data)
                return 1
            else:
                print("""
                            Opció NO vàlida!""")
                time.sleep(1)

        self.createTournamentMenu(dataClass, data)

    def createGroups(self, dataClass, data, tournament):
        os.system('clear')
        self.title()

    def titleRemoveTournament(self):
        print("""

		***** EL·LIMINAR TORNEIG - CLUB TENNIS SANTPEDOR *****""")

    def removeTournament(self, dataClass, data):
        os.system('clear')
        self.titleRemoveTournament()

        for index, tournament in enumerate(data["tournaments"]):
            print("""
                        {}({})""".format(next(iter(tournament)), index))
        currentTournamentIndex = input("""
                Selecciona una (ID) de torneig a el·liminar: """)

        if currentTournamentIndex.isnumeric() and (0 <= int(currentTournamentIndex) < len(data["tournaments"])):
            print("""
                        El torneig {} s'ha el·liminat!""".format(next(iter(data["tournaments"][int(currentTournamentIndex)]))))
            del data["tournaments"][int(currentTournamentIndex)]
            dataClass.saveData(data)
        else:
            print("""
                        Opció NO vàlida!""")
        time.sleep(2)
