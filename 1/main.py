import sys

def lecture_fichier(path):

    
    
    fichier=open(path)
    list_to_return=[]
    for ligne in fichier:
        liste_de_ligne = ligne.split()
        if len(liste_de_ligne)>0:
            comment=False
            for element in liste_de_ligne:
                if not comment and not ('#' in element):               
                    list_to_return.append(element)
                elif not comment and '#' in element:
                    start_comment_at = element.index('#')
                    if len(element[:start_comment_at])>0:
                        list_to_return.append(element[:start_comment_at])
                    comment=True
    fichier.close()

    del list_to_return[int(list_to_return[1])*int(list_to_return[2])*3+4:]  #supprime lignes en trop
    
    list_to_return += ['0']*((int(list_to_return[1])*int(list_to_return[2])*3)+4-len(list_to_return))

    #rajoute les 0 qui manquent en fin de fichier
            
    return list_to_return



def recuperer_organiser_donnees(path):


    
    liste_de_donnees=lecture_fichier(path)
    
    for i in range(4,((len(liste_de_donnees)-4)/3+4)):
        liste_de_donnees[i]=liste_de_donnees[i:i+3]
        del liste_de_donnees[i+1:i+3]
    for i in range(4,((len(liste_de_donnees)-4)/int(liste_de_donnees[1])+4)):
        liste_de_donnees[i]=liste_de_donnees[i:i+int(liste_de_donnees[1])]
        del liste_de_donnees[i+1:i+int(liste_de_donnees[1])]
        
    return liste_de_donnees[:4],liste_de_donnees[4:]



def save_picture(l,path_out):

    

    to_write=''
    for element in l[0]:
        to_write += element+'\n'
    for ligne in l[1]:
        for pixel in ligne:
            for RVB in pixel:
                to_write += RVB+'\n'

    fichier=open(path_out,'w')
    fichier.write(to_write)
    fichier.close()
    


def ROTG(In):
    
    Out = []
    for element in In[0]:
        Out += element
	
    Out[0] = Out[0]+Out[1]
    del Out[1]
	

    Out[1],Out[2] = Out[2],Out[1]
    
    M = []
    
    for k in range(int(Out[2]),0,-1):
        ligne = []
        for l in range(int(Out[1])):
            ligne += [In[1][l][k-1]]
        M += [ligne]
    
    return Out,M
            


def ROTD(In):
    
    Out = []
    for element in In[0]:
        Out += element
	
    Out[0] = Out[0]+Out[1]
    del Out[1]

    Out[1],Out[2] = Out[2],Out[1]
    
    M = []
    
    for k in range(int(Out[2])):
        ligne = []
        for l in range(int(Out[1]),0,-1):
            ligne += [In[1][l-1][k]]
        M += [ligne]
    
    return Out,M


def SYMV(In):
    
    Out = []
    for element in In[0]:
        Out += element
	
    Out[0] = Out[0]+Out[1]
    del Out[1]

    M = []
    
    for l in range(int(Out[2])):
        ligne = []
        for k in range(int(Out[1]),0,-1):
            ligne += [In[1][l][k-1]]
        M += [ligne]
    
    return Out,M
    



def SYMH(In):
    
    Out = []
    for element in In[0]:
        Out += element
	
    Out[0] = Out[0]+Out[1]
    del Out[1]

    M = []
    
    for l in range(int(Out[2]),0,-1):
        ligne = []
        for k in range(int(Out[1])):
            ligne += [In[1][l-1][k]]
        M += [ligne]
    
    return Out,M
    
if sys.argv[1] == 'ROTG':
    imagein=recuperer_organiser_donnees(sys.argv[2])
    imageout=ROTG(imagein)
    save_picture(imageout,sys.argv[3])

if sys.argv[1] == 'ROTD':
    imagein=recuperer_organiser_donnees(sys.argv[2])
    imageout=ROTD(imagein)
    save_picture(imageout,sys.argv[3])

if sys.argv[1] == 'SYMH':
    imagein=recuperer_organiser_donnees(sys.argv[2])
    imageout=SYMH(imagein)
    save_picture(imageout,sys.argv[3])

if sys.argv[1] == 'SYMV':
    imagein=recuperer_organiser_donnees(sys.argv[2])
    imageout=SYMV(imagein)
    save_picture(imageout,sys.argv[3])


