# coding: utf-8

import matplotlib.pyplot as plt


class Afficheur:
    def __init__(self):
        pass

    def afficher(self, content):
        keys = []
        values = []
        disp = ''
        for key, value in content.iteritems():
            disp = disp + '\n' + key + '\n\t\t' + '\n\t\t'.join(value)
            keys.append(key)
            values.append(len(value))

        plt.pie(values, labels=keys, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
        print disp
        return disp

