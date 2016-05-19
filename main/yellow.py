# coding: utf-8

"""
    Module principal
"""

import afficheur
import lecteur

import glob
from argparse import ArgumentParser

class Yellow(object):
    """ Class Yellow, manage afficheur and lecteur """

    def __init__(self, srcdir):
        """ Constructor - run getfiles() """
        self.srcdir = srcdir
        self.fichiers = []
        self.content = {}
        self.getfiles()

        self.afficheur = afficheur.Afficheur()
        self.lecteur = lecteur.Lecteur()

    def getfiles(self):
        """ fill self.fichiers with glob """
        self.fichiers = glob.glob("{}\*.melodymodeller".format(self.srcdir))

    def lire(self):
        """ fill self.content """
        self.content = {}
        for fichier in self.fichiers:
            self.content[fichier] = self.lecteur.lire(fichier)

    def afficher(self):
        """ display result """
        for contenu in self.content.values():
            self.afficheur.afficher(contenu)


if __name__ == '__main__':

    PARSER = ArgumentParser()
    # PARSER.add_argument('srcDir', nargs='?', default=os.getcwd())
    PARSER.add_argument('srcDir', nargs='?', default='../ressources')

    ARGS = PARSER.parse_args()
    OBJ = Yellow(ARGS.srcDir)

    OBJ.lire()
    OBJ.afficher()
