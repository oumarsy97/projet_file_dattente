#not /usr/bin/python
# -*- coding: latin-1 -*-

from datetime import datetime

"""
	Classe représentative des clients
"""
class Client:
	"""
		Constructeur publique d'un objet de la classe
	"""
	def __init__(self, number, arrival):
		self.number = number
		self.arrival = arrival
		self.nextClient = None
		self.previousClient = None
	
	"""
		Méthode publique pour récupérer le numéro de ticket du client
	"""
	def getNumber(self):
		return self.number
	
	"""
		Méthode publique pour définir le numéro de ticket du client
	"""
	def setNumber(self, number):
		self.number = number
	
	"""
		Méthode publique pour récupérer l'heure d'arrivée du client
	"""
	def getArrival(self):
		return self.arrival
	
	"""
		Méthode publique pour définir l'heure d'arrivée du client
	"""
	def setArrival(self, number):
		self.arrival = arrival
	
	"""
		Méthode publique d'auto-insertion du client courant dans la file d'attente. La tête de file lui est transmise en paramètre
	"""
	def insertIntoQueue(self, headOfTheQueue):
		# S'il n'y a personne en tête de file. Autrement dit la file est vide
		if(headOfTheQueue == None):
			return self # La cliente devient la tête de file. Et c'est terminé.
		# Sinon, on cherche le dernier client ...
		currentClient = headOfTheQueue
		while(currentClient.nextClient != None):
			currentClient = currentClient.nextClient
		# ... et on se met derrière lui
		currentClient.nextClient = self
		self.previousClient = currentClient
		# On informe l'instance de la file d'attente de la tête de file retenue après traitement
		return headOfTheQueue
	
	"""
		Méthode publique d'affichage d'un client
	"""
	def show(self):
		# On récupère le numéro du client courant
		text = "N° " + str(self.number) + " (" + self.arrival + ")\n"
		# Et on demande à l'éventuel client qui suit dans la file d'attente de s'afficher
		if(self.nextClient != None):
			text += self.nextClient.show()
		return text
	
	def __str__(self):
		return "N° " + str(self.number) + " (" + self.arrival + ")"

"""
	Classe représentative des clientes en état de grossesse
"""
class PregnantClient(Client):
	"""
		Classe représentative des clientes en état de grossess
	"""
	def __init__(self, number, arrival):
		Client.__init__(self, number, arrival)
	
	"""
		Redéfinition de la méthode publique d'auto-insertion de la cliente enceinte courant dans la file d'attente. La tête de file lui est transmise en paramètre
	"""
	def insertIntoQueue(self, headOfTheQueue):
		# S'il n'y a personne en tête de file. Autrement dit la file est vide
		if(headOfTheQueue == None):
			return self # La cliente devient la tête de file. Et c'est terminé.
		# Sinon, on parcourt les clients de la file d'attente à partir du début
		currentClient = headOfTheQueue
		# Si la tête de file n'est pas une cliente enceinte. On se met en tête de file.
		if(not isinstance(currentClient, PregnantClient)):
			currentClient.previousClient = self
			self.nextClient = currentClient
			return self
		# Sinon, on cherche la position de la dernière client enceinte
		r = currentClient
		while(currentClient != None):
			if(isinstance(currentClient, PregnantClient)):
				r = currentClient
				currentClient = currentClient.nextClient
			else:
				break
		# Et on se met derrière elle
		self.nextClient = r.nextClient
		if(self.nextClient != None):
			self.nextClient.previousClient = self
		self.previousClient = r
		r.nextClient = self
		# On informe l'instance de la file d'attente de la tête de file retenue après traitement
		return headOfTheQueue
	
	"""
		Redéfinition de la méthode publique d'affichage d'une cliente en état de grossesse
	"""
	def show(self):
		# On récupère le numéro du client courant
		text = "Femme enceinte N° " + str(self.number) + " (" + self.arrival + ")\n"
		# Et on demande à l'éventuel client qui suit dans la file d'attente de s'afficher
		if(self.nextClient != None):
			text += self.nextClient.show()
		return text

"""
	Classe représentative des clients seniors
"""
class SeniorClient(Client):
	"""
		Classe représentative des clientes en état de grossess
	"""
	def __init__(self, number, arrival):
		Client.__init__(self, number, arrival)
	
	"""
		Redéfinition de la méthode publique d'auto-insertion du client senior courant dans la file d'attente. La tête de file lui est transmise en paramètre
	"""
	def insertIntoQueue(self, headOfTheQueue):
		# S'il n'y a personne en tête de file. Autrement dit la file est vide
		if(headOfTheQueue == None):
			return self # La cliente devient la tête de file. Et c'est terminé.
		# Sinon, on parcourt les clients de la file d'attente à partir du début
		currentClient = headOfTheQueue
		# Si la tête de file n'est pas une cliente enceinte ou un client senior. On se met en tête de file.
		print("--> ", currentClient, " : ", isinstance(currentClient, PregnantClient), " -- ", isinstance(currentClient, SeniorClient))
		if(not isinstance(currentClient, PregnantClient) and not isinstance(currentClient, SeniorClient)):
			currentClient.previousClient = self
			self.nextClient = currentClient
			return self
		# Tant qu'on voit une cliente enceinte ou un client senior, on regarde le client suivant
		r = currentClient
		while(currentClient != None):
			if(isinstance(currentClient, PregnantClient) or isinstance(currentClient, SeniorClient)):
				r = currentClient
			currentClient = currentClient.nextClient
		# On se place tout auprès à trois clients derrière le dernier client senior ou la dernière clients enceinte
		# s'il y a plusieurs autres clients derrière lui
		currentClient = r.nextClient
		count = 1
		while((currentClient != None) and (count < 4)):
			r = currentClient
			currentClient = currentClient.nextClient
			count += 1
		# On s'insère à cette position
		self.nextClient = r.nextClient
		if(self.nextClient != None):
			self.nextClient.previousClient = self
		self.previousClient = r
		r.nextClient = self
		# On informe l'instance de la file d'attente de la tête de file retenue après traitement
		return headOfTheQueue
	
	"""
		Redéfinition de la méthode publique d'affichage d'un client senior
	"""
	def show(self):
		# On récupère le numéro du client courant
		text = "3ème âge N° " + str(self.number) + " (" + self.arrival + ")\n"
		# Et on demande à l'éventuel client qui suit dans la file d'attente de s'afficher
		if(self.nextClient != None):
			text += self.nextClient.show()
		return text

"""
	Classe représentative de la file d'attente
"""
class FileDattente:
	"""
		Constructeur publique d'un objet de la classe
	"""
	def __init__(self, next_client_number = 1, next_pregnant_client_number = 10000, next_senior_client_number = 15000):
		self.headOfTheQueue = None
		self.next_client_number = next_client_number
		self.next_pregnant_client_number = next_pregnant_client_number
		self.next_senior_client_number = next_senior_client_number
	
	"""
		Méthode publique d'ajout d'un client dans la file d'attente
	"""
	def addClient(self):
		# Affectation d'un numéro de ticket au client
		number = self.next_client_number
		# Sauvegarde de l'heure d'arrivée du client
		now = datetime.now()
		arrival = now.strftime("%d/%m/%Y %H:%M:%S")
		# Création d'une nouvelle instance de la classe <Client> avec le numéro de ticket et l'heure d'arrivée
		client = Client(number, arrival)
		# Si la file est vide, le nouveau client devient la tête de la file d'attente
		if(self.headOfTheQueue == None):
			self.headOfTheQueue = client
		# Sinon la méthode <insertIntoQueue> de la classe <Client> est appelée
		else:
			self.headOfTheQueue = client.insertIntoQueue(self.headOfTheQueue)
		# Incrémentation du numéro de ticket pour le positionnement du prochain client
		self.next_client_number += 1
		return number, arrival
	
	"""
		Méthode publique d'ajout d'une client enceinte dans la file d'attente
	"""
	def addPregnantClient(self):
		# Affectation d'un numéro de ticket à la cliente enceinte
		number = self.next_pregnant_client_number
		# Sauvegarde de l'heure d'arrivée de la cliente enceinte
		now = datetime.now()
		arrival = now.strftime("%d/%m/%Y %H:%M:%S")
		# Création d'une nouvelle instance de la classe <PregnantClient> avec le numéro de ticket et l'heure d'arrivée
		client = PregnantClient(number, arrival)
		# Si la file est vide, la nouvelle cliente devient la tête de la file d'attente
		if(self.headOfTheQueue == None):
			self.headOfTheQueue = client
		# Sinon la méthode <insertIntoQueue> de la classe <PregnantClient> est appelée
		else:
			self.headOfTheQueue = client.insertIntoQueue(self.headOfTheQueue)
		# Incrémentation du numéro de ticket pour le positionnement de la prochaine cliente enceinte
		self.next_pregnant_client_number += 1
		return number, arrival
	
	"""
		Méthode publique d'ajout d'un client senior dans la file d'attente 
	"""
	def addSeniorClient(self):
		# Affectation d'un numéro de ticket au client senior
		number = self.next_senior_client_number
		# Sauvegarde de l'heure d'arrivée du client senior
		now = datetime.now()
		arrival = now.strftime("%d/%m/%Y %H:%M:%S")
		# Création d'une nouvelle instance de la classe <SeniorClient> avec le numéro de ticket et l'heure d'arrivée
		client = SeniorClient(number, arrival)
		# Si la file est vide, la nouvelle cliente devient la tête de la file d'attente
		if(self.headOfTheQueue == None):
			self.headOfTheQueue = client
		# Sinon la méthode <insertIntoQueue> de la classe <SeniorClient> est appelée
		else:
			self.headOfTheQueue = client.insertIntoQueue(self.headOfTheQueue)
		# Incrémentation du numéro de ticket pour le positionnement du prochain client senior
		self.next_senior_client_number += 1
		return number, arrival
	
	"""
		Méthode publique de récupération du nombre de clients dans la file 
	"""
	def countNumberOfClients(self):
		# Initialisation du compteur du nombre de clients à zéro
		count = 0
		# On parcourt la file d'attente à partir de la tête 
		currentClient = self.headOfTheQueue
		# Tant qu'on n'a pas atteint la fin de la file d'attente ...
		while(currentClient != None):
			# ... on incrémente le compteur d'un pas
			count += 1
			# on se déplace sur le client suivant
			currentClient = currentClient.nextClient
		# On retourne le nombre de clients compté
		return count
	
	"""
		Méthode publique de récupération du nombre de clients dans la file 
	"""
	def getNextClient(self):
		# On récupére l'instance de la classe <Client> en tête de la file d'attente
		topClient = self.headOfTheQueue
		# On place le deuxième de la file en tête
		if(topClient != None):
			self.headOfTheQueue = self.headOfTheQueue.nextClient
			self.headOfTheQueue.previousClient = None
		# On retourne le client en tête de file
		return topClient
	
	"""
		Méthode publique d'affichage de la file d'attente 
	"""
	def showQueue(self):
		# Si la file n'est pas vide, on affiche la tête de la file d'attente
		if(self.headOfTheQueue != None):
			return self.headOfTheQueue.show()
		# Sinon, on informe que la file est vide
		else:
			return "La file est vide."

def showMenu():
	print("---------- Menu ----------")
	print(" c | C : Add a client.")
	print(" p | P : Add a pregnant client.")
	print(" o | O : Add a senior client.")
	print(" g | G : Get the first client.")
	print(" s | S : Show the list of clients.")
	print(" l | L : Give the length of the queue.")
	print(" q | Q : Quit and close.")
	print("--------------------------")

def isBadCommand(command):
	if((command == 'm') or (command == 'M')  # Si 'm' ou 'M' : Affichage du menu utilisateur
		or (command == 'c') or (command == 'C')  # Si 'c' ou 'C' : Ajout d'une nouveau client à la file d'attente
		or (command == 'p') or (command == 'P')  # Si 'p' ou 'P' : Ajout d'une cliente enceinte à la file d'attente
		or (command == 'o') or (command == 'O')  # Si 'o' ou 'O' : Ajout d'un client âgé à la file d'attente
		or (command == 'g') or (command == 'G')  # Si 'g' ou 'G' : Récupération au client en tête de la file d'attente
		or (command == 's') or (command == 'S')  # Si 's' ou 'S' : Affichage de la liste des clients en attente
		or (command == 'l') or (command == 'L')  # Si 'l' ou 'L' : Affichag de la longueur de la file d'attente
		or (command == 'q') or (command == 'Q')): # Si 'q' ou 'Q' : Quitter le programme
		return False
	else: # Sinon : commande invalide
		return True

def main():
	# Création de l'objet "file d'attente"
	fileDattente = FileDattente()
	# Affichage du menu initial pour guider l'utilisateur
	showMenu()
	
	while True :
		# Demande du choix de l'utilisateur et contrôle de saisie
		while True:
			# Demande à l'utilisateur de faire un choix en tapant une commande
			command = input("-- Faites un choix: ")
			# Récupération de la première caractère correspondant au choix
			command = command[0]
			# Tant que la commande est inconnue, on lui redemande de faire un choix
			if(not isBadCommand(command)):
				break
		
		if((command == 'c') or (command == 'C')):  # Choix d'ajout d'un client dans la file d'attente  
			fileDattente.addClient()
			print("Le client a été ajouté.")
		elif((command == 'p') or (command == 'P')):  # Choix d'ajout d'une cliente en état de grossesse dans la file d'attente
			fileDattente.addPregnantClient()
			print("La cliente en état de grosses a été ajoutée.")
		elif((command == 'o') or (command == 'O')):  # Choix d'ajout d'un client senior dans la file d'attente
			fileDattente.addSeniorClient()
			print("La client senior a été ajouté.")  
		elif((command == 'g') or (command == 'G')): # Choix de récupération du client en tête de la file d'attente
			client = fileDattente.getNextClient() # Appel de la fonction de récupération de la tête de liste
			client.show()
		elif((command == 's') or (command == 'S')): # Choix d'affichage des clients de la file d'attente
			text = fileDattente.showQueue() # Affichage de la liste
			print(text) # Saut de ligne à l'affichage
		elif((command == 'l') or (command == 'L')): # Choix d'affichage du nombre de clients dans la file d'attente
			print("La taille de la file = ", fileDattente.countNumberOfClients()) # Affichage de la taille de la liste
		elif((command == 'm') or (command == 'M')): # Choix de raffichage du menu
			showMenu() # Affichage du menu
		else: #((command != 'q') and (command != 'Q')) # Ou choix de quitter et fermer l'application
			break
	print("Bye not ")


# main()