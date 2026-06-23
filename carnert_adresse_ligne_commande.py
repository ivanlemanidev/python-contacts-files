import string
import os
import json

def ajouter_contact():
    nom_contact = input("Entrer votre nom de contact: ").replace(" ","")
    while len(nom_contact) <= 0:
        nom_contact = input("Entrer votre nom de contact valable : ").replace(" ","")
    prenom_contact = input("Entrer votre prenom de contact : ").replace(" ","")
    while len(prenom_contact) <= 0:
        prenom_contact = input("Entrer votre prenom de contact valable : ").replace(" ","")
    numero_contact = input("Entrer votre numero de contact : ").replace(" ","")
    liste_nct = [i for i in string.digits]
    liste_num = [k for k in numero_contact]
    liste_numero = [j for j in numero_contact if j in liste_nct]
    while (len(numero_contact) <= 0) or (liste_num != liste_numero):
        numero_contact = input("Entrer votre numero de contact valable : ").replace(" ","") 
        liste_num = [k for k in numero_contact]
        liste_numero = [j for j in numero_contact if j in liste_nct]
    infos_contact = {"NOM":nom_contact,"PRENOM":prenom_contact,"NUMERO_CONTACT":numero_contact}
    if infos_contact in contacts:
        print("Ces informantions existent déjà")
        resultat = False
    else:
        print("Les informations de contact ont été enregistré avec succès")
        resultat = infos_contact
    return resultat

def recherche_contact():
    liste_rc = []
    mot_recherche = input("Entrer le nom ou prenom du contact : ").replace(" ","")   
    for c in contacts:
        liste_rech = []
        for key in c:
            liste_rc.append(c[key])
            liste_rech.append(c[key])
        if mot_recherche in liste_rech:
            print(f"Informations trouvées avec succès : \n {c}") 
    if mot_recherche not in liste_rc:
        print("Aucune informations trouvées")    

def suppression_contact():
    liste_rmv = []
    rmv_contact = input("Entrer le nom ou prénom du contact à supprimer : ").replace(" ","") 
    for ct in contacts:
        liste_rv = []
        for key in ct:
            liste_rmv.append(ct[key])
            liste_rv.append(ct[key])
        if rmv_contact in liste_rv:
            contacts.remove(ct)
            print("Informations de contact supprimées avec succès") 
    if rmv_contact not in liste_rmv:
        print("Aucune informations trouvées")

def modifier_contact():
    liste_mod = []
    mod_contact = input("Entrer le nom ou prénom du contact à supprimer : ").replace(" ","") 
    for cmd in contacts:
        liste_md = []
        for key in cmd:
            liste_mod.append(cmd[key])
            liste_md.append(cmd[key])
        if mod_contact in liste_md:
            md_nom = input("Entrer un nouveau nom : ").replace(" ","")
            cmd["NOM"] = md_nom
            md_prenom = input("Entrer un nouveau prenom : ").replace(" ","")
            cmd["PRENOM"] = md_prenom
            md_numero = input("Entrer un nouveau numero de contact : ").replace(" ","") 
            cmd["NUMERO_CONTACT"] = md_numero
            print("Informations de contacts modifiées avec succès")
    if mod_contact not in liste_mod:
        print("Aucune informations trouvées")

contacts = []
if os.path.exists("contacts.json") and os.path.isfile("contacts.json"):
    with open("contacts.json", "r", encoding = "utf-8") as f:
        contacts = json.load(f)
while True:
    print("\n")
    print(" ====== CARNET D'ADRESSE EN LIGNE DE COMMANDE ====== \n")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Modifier un contact")
    print("6. Quitter \n")
    liste_choix = ["1","2","3","4","5","6"]
    x = False
    choix = input("Quel est votre choix : ")
    while choix not in liste_choix:
        choix = input("Quel est votre choix : ").replace(" ","") 
    if choix == "1":
        x = ajouter_contact()
    elif choix == "2":
        if len(contacts) == 0:
            print("Aucun contacts trouvés pour l'instant")
        else:
            print("liste des informations de contacts : ")
            for i, contact in enumerate(contacts):
                print(f"-- Contact N_0{i + 1} : {contact} ;")
    elif choix == "3":
        recherche_contact() 
    elif choix == "4":
        suppression_contact()
    elif choix == "5":
        modifier_contact()
    else:
        break
    if x == False:
        pass
    else:
        contacts.append(x) 
with open("contacts.json", "w", encoding = "utf-8") as f:
    json.dump(contacts, f, indent = 4, ensure_ascii = False)