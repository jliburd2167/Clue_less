# Clue_less

## Description:
JHU Foundations of Software Engineering Team Project

## Prequisites:
-[Anaconda]

## Setting Up the Environment
### Clone the Repository:
1. Clone the repository to your local machine using Git.

    eg. git clone git@github.com:jliburd2167/Clue_less.git

2. Navigate to the root of the directory

### Create and Activate a Conda Environment:

 Create a new conda environment using the clue_release_env.yml file.

    conda env create -f clue_release_env.yml -n clue_release

note: This step only needs to be done once.

    conda activate clue_release

### Leaving the Conda Environment
When you are done working, you can deactivate the Conda evironment.

	conda deactivate

## Updating environment dependencies
If you make any changes to the dependencies, remember to update the clue_env_release.yml file using:

	conda env export > clue_env_release.yml

## Launching the Environment

Navigate to the root directory of the repository and type the following command from inside the cl hue_release environment to lauch the server application:

	daphne clue_less.asgi:application

In a new terminal, navigate to the Client directory and type the following command to launch the client Command Line Interface:

	python ClientCli.py
