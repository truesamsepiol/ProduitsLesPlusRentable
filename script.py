#!/bin/python3
import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


def usage():
    print("\nUsage:\n\tpython3 " + sys.argv[0] + " <cheminVersFichier>")
    print("\n\tLe fichier doit etre au format CSV")

def traitement(fichier, numero):
    print("Debut de traitement du fichier")
    
    designations = [] 
    benefices = []
    nomFichierSortieImage = "RentabiliteDesProduits." + str(numero) + ".png"
    nomFichierSortiePdf = "RentabiliteDesProduits." + str(numero) + ".pdf"
    donnees = csv.reader(fichier)
    for ligne in donnees:
        prixDeVente    = int(ligne[3])
        quantiteAchete = int(ligne[2])
        prixDachat     = int(ligne[1])
        # Benefice par casier vendu dans le cadre d'une buvette
        benefice       = prixDeVente * quantiteAchete - prixDachat 
        print(ligne[0]  + ": " + str(benefice))
        designations.append(ligne[0])
        benefices.append(benefice)

    # Generation d'un diagramme en baton
    plt.figure(figsize=(10, 13)) # baton vertical
    plt.grid(axis = "x", color = "black", linestyle="--")
    plt.title("Bénéfices par casier vendu")
    plt.xlabel("Bénéfices en FCFA")
    plt.barh(designations, benefices)
    #plt.bar(designations, benefices) # baton horizontal
    plt.savefig(nomFichierSortieImage)
    plt.savefig(nomFichierSortiePdf)
    print("Fin de traitement du fichier\n\n")

if __name__ == "__main__":
  
    # Verification de l'usage du programme
    if len(sys.argv) < 2:
        usage()
        exit(1)

    # Boucle principale
    for id in range(len(sys.argv)):
        if id != 0:
            with open(sys.argv[id], "rt") as fichier:
                traitement(fichier, id)
