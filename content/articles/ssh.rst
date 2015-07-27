Configurer son serveur ssh
############################

:date: 2014-05-04
:tags: ssh
:category: Sécurité
:author: Gnupyx


Introduction
---------------------------
D'après futura_sciences_ :

.. _futura_sciences: http://www.futura-sciences.com/magazines/high-tech/infos/dico/d/internet-ssh-494/

  Ssh est un protocole qui permet de se connecter à une machine distante avec une liaison sécurisée. Les données sont cryptées entre machines. Il permet d'exécuter des commandes sur un serveur distant.


Règles de base
--------------
Ssh est un protocole très utilisé ce qui en fait une cible de choix pour les pirates informatiques. La plupart des administrateurs installent OpenSSH en laissant la configuration par défaut ce qui n'est pas recommandé.

 
How to
--------------
1. Installer ssh_
2. Créer un nouvel utilisateur_
3. Empêcher l'accès à root_
4. Changer le port_

.. _ssh:

Installer ssh
-------------

.. code-block:: bash
  
  sudo aptitude install ssh
  
  ssh root@serveur.com

Si votre connexion est réussie, alors votre serveur ssh fonctionne.

.. _utilisateur:

Créer un nouvel utilisateur
---------------------------
 
Avant d'interdire root, il faut créer un utilisateur. Nous utiliserons cet utilisateur pour nous connecter en ssh à la place de root.

.. code-block:: bash

  sudo useradd -m -d /home/monutilisateur -s /bin/bash monutilisateur

Afin d'avoir un serveur mieux sécurisé, vous allez mettre un mot de passe fort à notre nouvel utilisateur.

.. code-block:: bash

  sudo passwd monutilisateur
  Enter new UNIX password: 
  Retype new UNIX password:
  passwd : le mot de passe a été mis à jour avec succès

Avant de bloquer root, nous allons tester la connexion avec notre utilisateur.

.. code-block:: bash
  
  ssh monutilisateur@serveur.con
  passwd: 


Si tout est ok, nous pouvons aller bloquer la connexion ssh en tant que root

..  _root:

Empêcher l'accès à root
-----------------------


Pour bloquer l'utilisateur root, il faut aller configurer le démon ssh pour qu'il n'accepte plus les connexions de l'utilisateur root.

Le demon ssh est sshd

.. code-block:: bash

  sudo vim /etc/ssh/sshd_config

Remplacer: 

.. code-block:: bash

  PermitRootLogin yes

Par:

.. code-block:: bash

  PermitRootLogin no

Une fois la modification effectué, il ne nous reste plus qu'à tester le refus de connexion pour l'utilisateur root.

.. code-block:: bash
  
  ssh root@serveur.com

Si vous n'arrivez pas à vous connecter, alors que vous tapez le bon mot de passe, celà signifie que l'utilisateur root n'a pas le droit de se connecter.

.. _port:

Changer le port
---------------

Le port SSH par défaut est le 22. Il est là cible de multiples attaques principalement faites par des bots. Afin de réduire le nombre d'attaques par bot, nous allons modifier le port de connexion ssh

Et remplacer le port 22 par un autre port de votre choix: 

.. code-block:: bash
  
  sudo vim /etc/ssh/sshd_config
  
  Port 2345
  
  :wq

  sudo /etc/init.d/ssh restart

Pour se connecter en ssh, il faut préciser le nouveau port lors de la connexion

.. code-block:: bash

  ssh monutilisateur@serveur.com -p 2345


Conclusion
----------

Nous avons vu rapidement comment rendre notre connexion ssh un peu plus sécurisée. Si vous désirez sécuriser encore plus votre connexion ssh, vous pouvez utiliser une connexion par clé à la place des mots de passe, ou alors renforcer la sécurté et les accès en mettant en place Fail2ban.
