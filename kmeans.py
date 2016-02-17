#coding=utf-8
from __future__ import division
from __future__ import print_function
from random import choice
import numpy as np
from pprint import pprint
import operator

data = [[2.0, 3.0],  [3.0, 1.0],  [4.0, 2.0], [11.0, 5.0],
        [12.0, 4.0], [12.0, 6.0], [7.0, 5.0], [8.0, 4.0],
        [8.0, 6.0]]
        
def choose_initiale(data, k) :
    list_initiale = []
    while(len(list_initiale)!=k):
        tmp = choice(data)
        if not tmp in list_initiale :
            list_initiale.append(tmp)
    return list_initiale


def sortes(ma_list):
    result = sorted(ma_list.items(), key=operator.itemgetter(1))
    return result


def distance (x,y) :
	return np.linalg.norm(np.array(x) - np.array(y))

def moyenne_element(liste,k,taille):
    taille = len(liste)
    finale = [0 for i in range(taille)]
    for element in liste:
        finale = np.add(finale,element)
    for i in range(len(finale)):
        finale[i] = np.divide(finale[i],taille)
    return finale

def kmeans(data, k, t, maxiter) :
    '''for i in range(len(data)):
        data[i] = list(data[i])'''
    taille = len(data[0])
    points = choose_initiale(data, k)
    count = 0
    dict_result = {}
    finale = {}
    sigma = 0.0
    finale = {}
    for point in data :
        dict_result[tuple(point)] = -1
    for i in range(len(points)):
        dict_result[tuple(points[i])] = i
        finale[i] = points[i] 
    error = 9999
    nbIter = 1
    while(error>t and nbIter < maxiter):
        nbIter+= 1
        classes = {}
        for i in range(k):
            classes[i] = []
        for element in data:
            tmp = {}
            for classe in range(k):
                #print("debug ", distance(finale[classe],element), classe , element, finale[classe])
                tmp[classe] = distance(finale[classe],element)
                #print(tmp)
            tmp = sortes(tmp)
            cle = tmp[0][0]
            valeur = tmp[0][1]
            #print("la cle :",cle)
            dict_result[tuple(element)] = cle
            #print("MMMMMMMMMMMMMMMMMMMMM",dict_result)
            classes[cle].append(element)
            #print("mes classes,",classes)
		#pprint(classes)
        for classe in range(k):
            finale[classe] = moyenne_element(classes[classe],k,taille)
        taux_Erreur = 0.0
        for element in data:
			#print("valeur moyenne ; ",dict_result[tuple(element)]," point actuel",element)
            taux_Erreur += distance(finale[dict_result[tuple(element)]],element)
        error  = abs(taux_Erreur-error)
		#print("taux derrrr",error)
    tab1 = []
    for element in dict_result:
        tab1.append((list(element),dict_result[element]))
    tab2 = []
    for element in finale:
        tab2.append((list(finale[element])))
    return 	(tab1,tab2)
		

#res = kmeans(data, 2, 1, 12)


#print(res)

