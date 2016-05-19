# coding: utf-8

from bs4 import BeautifulSoup
from os.path import exists

class Lecteur:

    def __init__(self):
        pass

    def lire(self, filepath):
        '''
        :param filepath:
        :return: dictionary of list

        >>> Lecteur().lire('')
        {}

        >>> Lecteur().lire('../ressources/EOLE_FormationProject.melodymodeller')
        {'Operational Activities': [u'Make Weather', u'Collect Met Data', u'Elaborate Current Situation', u'Forecast Weather', u'Publish Forecast', u'Consulte Forecast', u'Subscribe', u'Manage Subscriptions'], 'Actors': [u'Broadcaster', u'Measurement Engineer', u'Forecaster', u'Atmosphere', u'Scientific User']}
        '''

        content = {}

        if exists(filepath):
            with open(filepath) as f:
                soup = BeautifulSoup(f, 'xml')

                # Acteurs
                resultats = soup.findAll('ownedActors')
                acteurs = [res['name'].strip() for res in resultats]

                # Operational Activities
                resultats = soup.find('ownedOperationalActivities').findAll('ownedFunctions')
                fonctions = [res['name'].strip() for res in resultats]

                # Storage
                content = {'Actors': acteurs, 'Operational Activities': fonctions}

        return content
