#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, time, random

class Tennis:

    def __init__(self):
        self.playersList = []
        self.actualPlayersListFileName = ""
        self.groups = []
        self.actualGroupsFileName = ""
        self.fromMenu = False
        self.menu()

    def menu(self):
        os.system('clear')
        print("""
        1. Fer Grups
        2. Fer Eliminatories
        3. Veure Jugadors (fer opció de poder eliminar i enumerar-los)
        4. Afegir Jugadors
        5. Veure Grups
        0. Sortir!
        """)
        option = input("Selecciona una opció: ")
        if option == '1':
            self.fromMenu = True
            self.group()
        elif option == '2':
            self.bracket()
        elif option == '3':
            self.fromMenu = True
            self.showPlayers()
        elif option == '4':
            self.fromMenu = True
            self.addPlayers()
        elif option == '5':
            self.fromMenu = True
            self.showGroups()
        elif option == '0':
            return 1
        else:
            print('Opció NO vàlida!')
            time.sleep(1)
        self.menu()

    def group(self):
        if self.fromMenu:
            os.system('clear')
            self.fromMenu = False
        self.showPlayers()
        if self.addPlayers() == "OK":
            self.makeGroups()
            self.showGroups()
            # self.showFiles()
            name = input("Nom del fitxer a guardar: ")
            self.saveFile(self.groups, name, "groups")
            input("Prem ENTER per continuar.")
            return 1
        self.group()

    def makeGroups(self):
        nPlayers = len(self.playersList)
        if nPlayers < 12:
            print("No tens suficients jugadors per fer grups!")
            time.sleep(2)
            return 1
        elif 12 <= nPlayers <= 18:
            nGroups = 4
        elif 18 < nPlayers < 28:
            nGroups = 6
        elif 28 <= nPlayers:
            nGroups = 8
        self.groups = []
        self.prepareGroups(nGroups)
        self.insertPlayersInGroups(nGroups)

    def prepareGroups(self, nGroups):
        for i in range(nGroups):
            self.groups += [[]]

    def insertPlayersInGroups(self, nGroups):
        playersListCopy = self.playersList
        while not self.checkIfListIsEmpty(playersListCopy):
            hype = playersListCopy[:nGroups]
            lenHype = len(hype)
            for i in range(nGroups):
                if i < lenHype:
                    election = random.choice(hype)
                    self.groups[i] += [election]
                    hype.remove(election)
            playersListCopy = playersListCopy[nGroups:]


    def checkIfListIsEmpty(self, list):
        for i in list:
            if i:
                return False
        return True

    def bracket(self):
        os.system('clear')
        print("Opció Eliminatories:")

    def addPlayers(self):
        if self.fromMenu:
            os.system('clear')
            self.fromMenu = False
        opt = input("""
            Per acabar escriu OK!
            Per eliminar un jugador escriu DEL!
            Escriu un NOU jugador: """)
        if opt.upper() == "OK":
            name = input("Nom del fitxer a guardar: ")
            self.saveFile(self.playerList, name, "players")
            return "OK"
        elif opt.upper() == "DEL":
            self.removePlayer()
        else:
            self.playersList.append(opt.upper())

    def showPlayers(self):
        os.system('clear')
        if self.playersList == []:
            # self.showFiles()
            name = input("No tens cap fitxer de jugadors seleccionat, escull una ID: ")
            self.readFile(name, "players")
            return self.showPlayers()
        for index, player in enumerate(self.playersList):
            print("""{}. {}""".format(index+1, player))
        if self.fromMenu:
            input("Prem ENTER per continuar.")
            self.fromMenu = False

    def showGroups(self):
        os.system('clear')
        for group in range(len(self.groups)):
            print("""Grup {}""".format(group+1))
            for index, player in enumerate(self.groups[group]):
                print("""{}{} {}""".format(group, index, player))
            print("")
        if self.fromMenu:
            input("Prem ENTER per continuar.")
            self.fromMenu = False

    def saveFile(self, list, name, type):
        file = open("{}.txt".format(name),"w")
        if type == "players":
            file.write(','.join(list))
        elif type == "groups":
            for subList in list:
                file.write(','.join(subList))
                file.write('\n')
        file.close()

    def readFile(self, name, type):
        file = open("{}.txt".format(name),"r")
        if type == "players":
            self.playersList = []
            for line in file.readlines():
                print("hola")
                self.playersList += [line.replace('\n',"").split(',')]
        elif type == "goups":
            self.groups = []
            for line in file.readlines():
                self.groups += [line.replace('\n',"").split(',')]
        file.close()

    def removePlayer(self):
        self.showGroups()
        id = input("ID del jugador a eliminar: ")
        del self.groups[int(id[0])][int(id[1])]
        print("{} eliminat!", self.groups[id[0]][id[1]])
        input("Prem ENTER per continuar.")

    def showFiles(self, name, type):
        pass

if __name__ == '__main__':
    Tennis()
