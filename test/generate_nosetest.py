# http://www.saltycrane.com/blog/2012/04/test-coverage-nose-and-coveragepy/

# pylint ../main/yellow.py
# nosetests --with-coverage --cover-erase --cover-package=main --cover-html


from subprocess import call

command = 'nosetests --with-coverage --cover-erase --cover-package=main --cover-html'
call(command)

command = 'pyreverse  -o png {0}/yellow.py {0}/yellowGUI.py {0}/lecteur.py {0}/afficheur.py -Smy -p Yellow'.format('../main')
call(command)