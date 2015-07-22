Désactiver le bluetooth au démarrage du PC.
#############################################

:date: 2014-07-14
:tags: bluetooth, ubuntu
:category: Sécurité
:author: Barascut Jérémy


Par défaut, lorsque j'allume mon PC portable, le bluetooth est démarré. Vu que je ne m'en sers pas et que je désire gagner en autonomie, j'ai décidé de le désactiver dès le démarrage.

Pour désactiver le bluetooth c'est très simple, il suffit de rajouter une commande dans le fichier rc.local


.. code-block:: bash

  # vim /etc/rc.local

  rfkill block bluetooth
  exit 0

Lors du prochain démarrage du PC, le bluetooth sera désactivé par défaut.
Il est bien entendu possible de le réactiver via l'icône.
