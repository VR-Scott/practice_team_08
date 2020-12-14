#!/bin/bash
# setopt extendedglob
# create a new home directory
# mkdir ~/code_clinics_team8

# copy code_clinics directory to the new home directory
# cp -r !(.git) ~/code_clinics_team8

# install neccesary packages and modules
python3 -m pip install pip

python3 -m pip install google-api-python-client 

python3 -m pip install google_auth_oauthlib

python3 -m pip install bcrypt

# these will configure all the aliases
echo "alias cs8='python3 main_for_commandline.py'" >> ~/.zshrc # this cmd will add the alias to the zsh terminal

echo "alias cs8='python3 main_for_commandline.py'" >> ~/.bashrc # this cmd will add the alias to the bash terminal

# all parkages have been installed
# execute the programme

echo "-"
echo "Installation complete!"
echo "-"
echo "Restart the terminal and type: cs8"
