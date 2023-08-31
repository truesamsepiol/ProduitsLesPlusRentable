#!/bin/python3
import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


def usage():
    print("\nUsage:\n\tpython3 " + sys.argv[0] + " <cheminVersFichier>")
    print("\n\tLe fichier doit etre au format CSV")

def generationDiagramme(nomFichier, tailleX, tailleY, titre, labelX, valeursX, valeursY):

    nomFichierPdf = nomFichier + ".pdf"
    nomFichierPng = nomFichier + ".png"
    # Generation d'un diagramme en baton
    plt.figure(figsize=(tailleX, tailleY)) 
    plt.grid(axis = "x", color = "black", linestyle="--")
    plt.title(titre)
    plt.xlabel(labelX)
    plt.barh(valeursX, valeursY) # baton horizontal
    #plt.bar(valeursX, valeursY) # baton verticale
    plt.savefig(nomFichierPdf)
    plt.savefig(nomFichierPng)

def traitement(fichier, numero):
    print("Debut de traitement du fichier")
    
    designations = [] 
    benefices    = []
    pourcentages = []
    donnees = csv.reader(fichier)
    for ligne in donnees:
        prixDeVente    = int(ligne[3])
        quantiteAchete = int(ligne[2])
        prixDachat     = int(ligne[1])
        # Benefice par casier vendu dans le cadre d'une buvette
        benefice       = prixDeVente * quantiteAchete - prixDachat 
        # Pourcentage par casier vendu 
        pourcentage    = 100*(float(benefice) / float(prixDachat))
        print(ligne[0]  + ": " + str(benefice) + " " + str(pourcentage))
        designations.append(ligne[0])
        benefices.append(benefice)
        pourcentages.append(pourcentage)

    generationDiagramme("beneficeParCasier", 10, 30, "Benefice par casier vendu", "Benefice en FCFA", designations, benefices)
    generationDiagramme("pourcentageBeneficeParCasier", 10, 30, "Benefice en pourcentage par casier vendu", "Benefice en %", designations, pourcentages)
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
