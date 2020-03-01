__autor__ = "Max Begue"
__date__ = "11/02/2020"
__file_name__ = "hmm.py"

import random as rdm
import numpy as np


class Hmm:

    def __init__(self, S, O, pi, T, E):
        self.S = S
        self.O = O
        self.pi = pi
        self. T = T
        self.E = E

    def gen_rand(self, longueur):
        if longueur < 1 :
            return 'tes une pute'
        else:
            liste_sortie = []
            p = rdm.random()
            i = 0
            trouve = False
            proba_tot = 0
            while i < len(self.pi) and trouve == False :
                proba_tot += self.pi[i]
                if p <= proba_tot:
                    trouve = True
                else:
                    i += 1

            etat = self.S[i]

            p = rdm.random()
            i = 0
            trouve = False
            proba_tot = 0
            while i < len(self.E[etat]) and trouve == False:
                proba_tot += self.E[etat][i]
                if p <= proba_tot:
                    trouve = True
                else:
                    i += 1

            liste_sortie += [self.O[i]]

            for j in range(longueur - 1):
                p = rdm.random()
                i = 0
                trouve = False
                proba_tot = 0
                while i < len(self.T[etat]) and trouve == False:
                    proba_tot += self.T[etat][i]
                    if p <= proba_tot:
                        trouve = True
                    else:
                        i += 1

                etat = self.S[i]

                p = rdm.random()
                i = 0
                trouve = False
                proba_tot = 0
                while i < len(self.E[etat]) and trouve == False:
                    proba_tot += self.E[etat][i]
                    if p <= proba_tot:
                        trouve = True
                    else:
                        i += 1

                liste_sortie += [self.O[i]]

        return liste_sortie

    def proba_forward(self, sequence):

        """sequence is a list of emissions, return the probability for the HMM self
         to produce sequence, forward version"""

        # initialisation

        mat = np.zeros((len(self.S), len(sequence)))

        index_char = self.O.index(sequence[0])

        for k in range(len(self.S)):

            mat[k][0] = self.pi[k] * self.E[k][index_char]

        # filling the matrix

        for i in range(1, len(sequence)):
            index_char2 = self.O.index(sequence[i])

            for k in range(len(self.S)):
                somme = 0
                for l in range(len(self.S)):
                    somme += mat[l][i - 1] * self.T[l][k] * self.E[k][index_char2]

                mat[k][i] = somme

        # computing the result

        res = 0
        for j in range(len(self.S) - 1):
            res += mat[j][-1]

        return res

    # proba bacward a un probleme ou forward (je pense plutot à backward

    def proba_backward(self, sequence):

        """sequence is a list of emissions, return the probability for the HMM self
         to produce sequence, forward version"""

        # initialisation

        mat = np.zeros((len(self.S), len(sequence)))

        for k in range(len(self.S)):
            mat[k][-1] = 1

        print(mat, "len mat = ", len(mat[0]))

        for i in range(len(sequence) - 2, - 1,  - 1):
            print(i)
            index_char2 = self.O.index(sequence[i])
            for k in range(len(self.S)):
                somme = 0
                for l in range(len(self.S)):
                    somme += self.T[l][k] * self.E[l][index_char2] * mat[l][i + 1]


                mat[k][i] = somme

        res = 0

        # indice ????? là j'ai pris i = 0 et k varie

        for k in range(len(self.S)):
            res += self.pi[k] * self.E[k][self.O.index(sequence[0])] * mat[k][0]

        return res



    def pred_next_symbol(self, sequence):

        """compute the next symbol of the given sequence (in probability) for a given HMM"""

        #initialisation

        mat = np.zeros((len(self.S), len(sequence) + 1))

        for k in range(len(self.S)):
            mat[k][0] = self.pi[k]

        #filling the matrix

        for i in range(1, len(sequence) + 1):
            for k in range(len(self.S)):
                hhat = 0
                symb_index = self.O.index(sequence[i-1])

                for l in range(len(self.S)):
                    hhat += self.T[l][k] * self.E[l][symb_index] * mat[l][i-1]

                mat[k][i] = hhat

            somme = 0
            for p in range(len(self.S)):
                somme += mat[p][i]

            for y in range(len(self.S)):
                mat[y][i] = mat[y][i] / somme

        # reconstruction

        probas = [0 for c in range(len(self.O))]

        for j in range(len(self.O)):
            somme2 = 0
            for k2 in range(len(self.S)):
                somme2 += self.E[k2][j] * mat[k2][-1]

            probas[j] = somme2



        res_index = np.argmax(probas)

        return self.O[res_index]


    def viterbi(self, sequence):

        """return the sequence of state the most likely (according to proba) to produce the given
        sequence given an HMM"""

        T = np.array(self.T)

        # initialisation

        mat_etat = [[[] for j in range(len(sequence))] for p in range(len(self.S))]

        mat_probas = np.zeros((len(self.S), len(sequence)))

        index_char = self.O.index(sequence[0])

        for k in range(len(self.S)):

            mat_etat[k][0] = [k]
            mat_probas[k][0] = self.E[k][index_char] * self.pi[k]

        # print("mat_etea = ")
        # print(mat_etat)
        # print("mat_probas")
        # print(mat_probas)

        # filling the matrix

        for i in range(1, len(sequence)):

            ind_char = self.O.index(sequence[i])

            for k2 in range(len(self.S)):
                l = int(np.argmax(T.take([k2], axis=1) * mat_probas.take([i - 1], axis=1)))

                mat_etat[k2][i] = mat_etat[l][i - 1] + [self.S[k2]]

                mat_probas[k2][i] = self.E[k2][ind_char] * T[l][k2] * mat_probas[l][i - 1]

        k3 = int(np.argmax(mat_probas.take([len(sequence) - 1], axis=1)))

        return mat_etat[k3][-1]


    def 



















