Projet Veille AI

Description:

Le Projet Veille AI est une application Python qui récupère automatiquement des articles à partir de plusieurs sources d'actualités en ligne et génère des résumés concis de ces articles. En utilisant des bibliothèques telles que feedparser et langchain, cette application collecte des flux RSS à partir de diverses sources sélectionnées, puis utilise un modèle de langue pré-entraîné (llama2) pour générer des résumés informatifs des articles récupérés. 

Démarrage:

Prérequis:
- Python (version 3) doit être installé sur votre système. 
  Si ce n'est pas le cas, téléchargez et installez Python depuis le site officiel.


Installation:

1. Clonez ce dépôt sur votre machine locale :
    
	git clone https://github.com/nicolasna77/Projet_Veille_AI.git

2. Accédez au répertoire de votre projet :

   		cd Projet_Veille_AI

4. Créez un environnement virtuel à l'aide de venv :

    		python -m venv venv

5. Activez l'environnement virtuel :
    - Sur Windows :
        
    		source venv\Scripts\activate

    - Sur Linux/macOS :
       
		  source venv/bin/activate

6. Installez les dépendances requises à partir du fichier requirements.txt :

   		pip install -r requirements.txt

7. Téléchargez le modèle llama2 en utilisant ollama :
    
		ollama pull llama2

Utilisation:

Une fois que vous avez suivi les étapes d'installation, vous pouvez exécuter le script principal avec la commande suivante :

    python main.py

Cela lancera votre application et vous affichera les résumés des articles actuels des différentes sources d'actualités.
