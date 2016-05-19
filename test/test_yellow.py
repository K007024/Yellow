import unittest

import os
from main.yellow import Yellow

class TestYellow(unittest.TestCase):

    def setUp(self):
        self.dirMain = os.getcwd()
        # self.dirRessources = '{}\\..\\ressources'.format(self.dirMain)
        self.dirRessources = '{}\\ressources'.format(self.dirMain)
        self.file = '{}\\{}'.format(self.dirRessources, 'EOLE_FormationProject.melodymodeller')
        
    def test_instance(self):
        obj = Yellow('')
        self.assertIsInstance(obj, Yellow)

    def test_nofiles(self):
        obj = Yellow('')
        self.assertTrue(obj.fichiers == [])
        
    def test_file(self):
        obj = Yellow(self.dirRessources)
        self.assertTrue(obj.fichiers == [self.file])

    def test_beforeRead(self):
        obj = Yellow(self.dirRessources)
        # obj.lire()
        self.assertTrue(obj.content == {})

    def test_afterRead1(self):
        obj = Yellow(self.dirRessources)
        obj.lire()
        dico = obj.content
        self.assertTrue(dico.keys, [self.file])

    def test_afterRead2(self):
        obj = Yellow(self.dirRessources)
        obj.lire()
        dico = obj.content[obj.content.keys()[0]]
        self.assertTrue(dico.keys, ['Operational Activities', 'Actors'])

    def test_afterDisplay(self):
        obj = Yellow(self.dirRessources)
        obj.lire()
        res = obj.afficher()
        self.assertTrue(res != '')