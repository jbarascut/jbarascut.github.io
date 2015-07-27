Powerline-shell
###############

:date: 2015-07-27
:tags: bash, powerline
:category: Linux
:author: Gnupyx
:status: draft
:lang: fr

Si vous êtes un fanatique de la ligne de commandes, alors Powerline-shell_ est fait pour vous.

Powerline-shell est un script python remplaçant votre prompt shell par quelque chose de plus évolué.

Powerline améliore votre prompt shell si vous utilisez Bash, ZSH ou Fish

.. _Powerline-shell: https://github.com/milkbikis/powerline-shell

Installation
------------

J'ai pris l'habitude de mettre les scripts et autres logiciels dans un dossier ~/App

Les fonts:
~~~~~~~~~~

Pour utiliser Powerline, il faut télécharger un pack de police adapté.

.. code-block:: bash

    mkdir App && cd App
    
    git clone https://github.com/powerline/fonts.git

    cd fonts
    
    ./install.sh
    
Sur Debian les fonts seront installées sous ~/.fonts

Powerline-shell:
~~~~~~~~~~~~~~~~

.. code-block:: bash

    git clone https://github.com/milkbikis/powerline-shell
  
    cd powerline-shell
  
    ./install.py

L'installation de powerline-shell est terminée.

Bash:
~~~~~
Avec Bash, il faut ajouter les lignes suivantes à votre **.bashrc**:

.. code-block:: bash

    function _update_ps1() {
       export PS1="$(~/App/powerline-shell/powerline-shell.py $? 2> /dev/null)"
    }

    export PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"

Recharger le .bashrc

.. code-block:: bash

    source ~/.bashrc
    

ZSH:
~~~~
Avec ZSH, il faut ajouter les lignes suivantes à votre **.zshrc**:


.. code-block:: bash

    function powerline_precmd() {
      export PS1="$(~/App/powerline-shell/powerline-shell.py $? --shell zsh 2> /dev/null)"
    }

    function install_powerline_precmd() {
      for s in "${precmd_functions[@]}"; do
        if [ "$s" = "powerline_precmd" ]; then
          return
        fi
      done
      precmd_functions+=(powerline_precmd)
    }

    install_powerline_precmd


Fish:
~~~~~
Avec Fish, il faut redefinir le prompt dans **~/config/fish/config.fish**:

.. code-block:: bash

    function fish_prompt
        ~/powerline-shell.py $status --shell bare ^/dev/null
    end


Terminator:
~~~~~~~~~~~

Utilisation
-----------

User simple ou root
Droit d'accès interdit
Virtualenv
Branch git/svn/hg 
Couleur en cas de commande incorrecte
Facilement extensible et customisable

Conclusion
----------

Powerline-shell est devenu pour moi indispensable, un peu comme git l'est devenu quand j'ai débuté le dev.
