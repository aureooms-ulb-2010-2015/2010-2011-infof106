# -*- coding: utf-8 -*-

import sys

def lecture_fichier(path):

    
    
    fichier=open(path)
    liste_de_lignes = fichier.readlines()
    list_to_return = []
    for line in liste_de_lignes:
        line = line.strip()
        if line != '':
            if '#' in line:
                line = line[:line.index('#')]
            list_to_return += line.split()
            
    list_to_return = list_to_return[:int(list_to_return[1])*int(list_to_return[2])*3+4]        
    
    while (len(list_to_return)-4) < int(list_to_return[1])*int(list_to_return[2])*3:
        list_to_return += '0'

    
    
    return list_to_return



def recuperer_organiser_donnees(path):


    
    liste_de_donnees = lecture_fichier(path)
    indicateurs = liste_de_donnees[0:4]

    M = []
    i=4
    for lignes in range(int(indicateurs[2])):
        ligne = []
        
        for colonnes in range(int(indicateurs[1])):
            ligne +=[liste_de_donnees[i:i+3]]            
                
            i += 3
            
            
        M += [ligne]
                   
        
    return indicateurs,M



def save_picture(l,path_out):

    fichier_ou_ecrire = open(path_out,'w')
    fichier_ou_ecrire.write(l[0][0]+'\n')
    fichier_ou_ecrire.close()
    fichier_ou_ecrire = open(path_out,'a')
    for nombre in l[0][1:]:
        fichier_ou_ecrire.write(nombre+'\n')
    for ligne in l[1]:
        for pixel in ligne:
            for RVB in pixel:
                fichier_ou_ecrire.write(RVB+'\n')
    fichier_ou_ecrire.close()
                
    

    
def ROTG(In):
    
    Out = In[0]
    
    Out[1],Out[2] = Out[2],Out[1]
    
    M = []
    
    for k in range(int(Out[2]),0,-1):
        ligne = []
        for l in range(int(Out[1])):
            ligne += [In[1][l][k-1]]
        M += [ligne]
    
    return Out,M
            


def ROTD(In):
    
    Out = In[0]
	
    Out[1],Out[2] = Out[2],Out[1]
    
    M = []
    
    for k in range(int(Out[2])):
        ligne = []
        for l in range(int(Out[1]),0,-1):
            ligne += [In[1][l-1][k]]
        M += [ligne]
    
    return Out,M


def SYMV(In):
    
    Out = In[0]
	
    
    M = []
    
    for l in range(int(Out[2])):
        ligne = []
        for k in range(int(Out[1]),0,-1):
            ligne += [In[1][l][k-1]]
        M += [ligne]
    
    return Out,M
    



def SYMH(In):
    
    Out = In[0]

    M = []
    
    for l in range(int(Out[2]),0,-1):
        ligne = []
        for k in range(int(Out[1])):
            ligne += [In[1][l-1][k]]
        M += [ligne]
    
    return Out,M


def FLOU(dataIn,blurIntensity):

    indicators = dataIn[0]
    startingMatrix = dataIn[1]
    nbrOfLines = int(indicators[2])
    nbrOfColumns = int(indicators[1])

    workingMatrix = []
    for a in range(nbrOfLines):
        newLine = []
        for b in range(nbrOfColumns):
            newPixel = []
            for c in [0,1,2]:
                newPixel += [int(startingMatrix[a][b][c])]
            newLine += [newPixel]
        workingMatrix += [newLine]

    timesDone = 0

    while timesDone < blurIntensity:            
            
        M = []
    
        for i in range(nbrOfLines):
            ligne = []
            o = 0
        
            for j in range(nbrOfColumns):            

                m,n,p = -1,2,2
                
                if i == 0:
                    
                    m = 0    

                if i == nbrOfLines-1:
                    
                    n = 1

                if j == nbrOfColumns-1:
                    
                    p = 1
                    
                blurRed   = 0
                blurGreen = 0
                blurBlue  = 0
                usedPixels = 0
                
                for k in range(m,n):
                    
                    for l in range(o,p):
                                                
                        blurRed   += workingMatrix[i+k][j+l][0]
                        blurGreen += workingMatrix[i+k][j+l][1]
                        blurBlue  += workingMatrix[i+k][j+l][2]

                        
                        usedPixels += 1
                        
                ligne += [[(blurRed/usedPixels),(blurGreen/usedPixels),(blurBlue/usedPixels)]]
    
                o = -1
            
            M += [ligne]
        workingMatrix = M
        timesDone += 1

    M = []
    for a in range(nbrOfLines):
        newLine = []
        for b in range(nbrOfColumns):
            newPixel = []
            for c in [0,1,2]:
                newPixel += [str(workingMatrix[a][b][c])]
            newLine += [newPixel]
        M += [newLine]
        

    return indicators,M


def ENC(dataIn,message):

    indicators = dataIn[0]
    M = dataIn[1]
    nbrOfLetters = len(message)
    nbrOfLines = int(indicators[2])
    nbrOfColumns = int(indicators[1])

    
    code = ''
    for indexLetter in range(nbrOfLetters):
        
        codeLetter = bin(ord(message[indexLetter]))[2:]
        
        while len(codeLetter)<8:
            codeLetter = '0' + codeLetter
            
        codeLetter = codeLetter + '0'
        
        if message[indexLetter+1:] == '':
            codeLetter = codeLetter[:8] + '1'
            
        code += codeLetter
    


    nbrOfPlacedBits = 0
    nbrOfBits = nbrOfLetters * 9
    line = 0
    
    while line < nbrOfLines and nbrOfPlacedBits < nbrOfBits:
        column = 0
        
        while column < nbrOfColumns and nbrOfPlacedBits < nbrOfBits:
            color = 0
            
            while color < 3:
                rOrVOrB = int(M[line][column][color])
                if rOrVOrB%2 == 0:
                    M[line][column][color] = str(rOrVOrB + int(code[nbrOfPlacedBits]))
                else:
                    M[line][column][color] = str(rOrVOrB + int(code[nbrOfPlacedBits]) -1)
                nbrOfPlacedBits += 1
                color+=1
            column+=1
        line+=1

    return indicators,M

def DEC(dataIn):

    indicators = dataIn[0]
    M = dataIn[1]
    nbrOfLines = int(indicators[2])
    nbrOfColumns = int(indicators[1])

    decoded = False
    binCode =''
    line = 0

    
    while (not decoded) and line < nbrOfLines:
        column = 0
        
        while (not decoded) and column < nbrOfColumns :
            
            if int(M[line][column][0])%2==0:
                binCode += '0'
            else:
                binCode += '1'

            if int(M[line][column][1])%2==0:
                binCode += '0'
            else:
                binCode += '1'

            if int(M[line][column][2])%2==0:
                binCode += '0'
            else:
                binCode += '1'

            if len(binCode)%9 == 0:
                if binCode[len(binCode)-1] == '1':
                    decoded = True
            column += 1
        line += 1

    message =''
    for i in range(len(binCode)/9):
        letterbinCode = binCode[i*9:i*9+8]
        letterAsciiCode=0
        strength = 128
        for number in letterbinCode:
            letterAsciiCode += strength * int(number)
            strength /= 2
        message += chr(letterAsciiCode)

    print 'Message:' + message
                    
                    
        

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

if sys.argv[1] == 'FLOU':
    imageIn=recuperer_organiser_donnees(sys.argv[3])    
    imageout=FLOU(imageIn,int(sys.argv[2]))
    save_picture(imageout,sys.argv[4])

if sys.argv[1] == 'ENC':
    message = raw_input('Message à cacher?:')
    imageIn = recuperer_organiser_donnees(sys.argv[2])
    imageOut = ENC(imageIn,message)
    save_picture(imageOut,sys.argv[3])

if sys.argv[1] == 'DEC':
    dataIn = recuperer_organiser_donnees(sys.argv[2])
    DEC(dataIn)

