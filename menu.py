from data import *
from members import *
import os, time

class Menu:
	def __init__(self):
		self.dataClass = Data()
		self.data = self.dataClass.readData()
		self.principalMenu()

	def title(self):
		print("""

		***** CLUB TENNIS SANTPEDOR *****""")

	def principalMenu(self):
		os.system('clear')
		self.title()
		for index, options in enumerate(self.data["menu-options"]):
			print("""
			{}. {}""".format(index, options[0]))
		option = input("""
		Selecciona una opció: """)
		if option == '1':
		    # self.fromMenu = True
		    Members().membersMenu(self.dataClass, self.data)
		elif option == '2':
			self.dataClass.showDataPretty()
		# elif option == '3':
		#     self.fromMenu = True
		#     self.showPlayers()
		# elif option == '4':
		#     self.fromMenu = True
		#     self.addPlayers()
		# elif option == '5':
		#     self.fromMenu = True
		#     self.showGroups()
		elif option == '0':
			return 1
		else:
			print("""
			Opció NO vàlida!""")
			time.sleep(1)
		self.principalMenu()

if __name__ == '__main__':
	Menu()
