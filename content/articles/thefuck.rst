The fucking script !!!!
#######################

:date: 2015-08-20
:tags: bash, thefuck
:category: Linux
:author: Gnupyx
:status: published
:lang: fr

Ne vous inquiétez pas je n'ai pas la haine après un script, bien le contraire.   Si vous êtes comme moi à toujours à oublier ce petit fripon de sudo devant apt-get alors thefuck_ peut résoudre facilement votre problème. Ainsi que d'autres problèmes de commandes :)

Thefuck est un script python. Il fonctionne avec bash, zsh ou tout autre shell.

.. _thefuck: https://github.com/nvbn/thefuck

.. image:: images/thefuck.gif
   :alt: the fuck command line


Installation
------------

Le reflex à avoir lorsque l'on veut installer un programme en python est de voir si il est disponible dans pip_ et installer le programme avec 


.. _pip: https://pypi.python.org/pypi/pip

Sur Debian ou dérivés:

.. code-block:: bash

    sudo apt-get install python-pip

Sur Redhat et dérives:

.. code-block:: bash 

    sudo yum install python-pip

Sur Arch
Il y'a déjà un paquet pour Arch

.. code-block:: bash
  
    sudo pacman -S thefuck

Ou avec pip

.. code-block:: bash

    sudo pacman -Suy python-pip

Puis avec pip

.. code-block:: bash

    sudo pip install thefuck


Shell
-----

Dans votre shell, il faut ajouter les lignes suivantes, par exemple dans votre **.bashrc**:

.. code-block:: bash

    eval "$(thefuck --alias)"
    # Et si fuck vous plait pas vous pouvez préciser un alias
    eval "$(thefuck --alias tux)"

Recharger le .bashrc

.. code-block:: bash

    source ~/.bashrc
    
Thefuck corrige pas mal de commande comme cp, git, grep, ls, mercurial, mkdir, pip, sudo, apt-get, yum, rm etc

Il est même possible de créer ces propres règles simplement

.. code-block:: bash

  match(command: Command, settings: Settings) -> bool
  get_new_command(command: Command, settings: Settings) -> str | list[str]


Plus d'infos ici_

.. _ici: https://github.com/nvbn/thefuck#creating-your-own-rules

Conclusion
----------

Thefuck: tout simplement magique.  A utiliser et abuser! 
