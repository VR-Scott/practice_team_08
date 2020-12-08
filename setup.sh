#!/bin/bash

# create a new home directory
mkdir ~/team8

# copy code_clinics directory to the new home directory
cp -r code_clinics ~/team8

# install neccesary packages and modules
python3 -m pip install pip

python3 -m pip install google-api-python-client 

python3 -m pip install google_auth_oauthlib

python3 -m pip install bcrypt

python3 -m pip install prettytable

# these will configure all the aliases
echo "alias cs8='cd ~/team8/code_clinics/ && python3 main_for_commandline.py'" >> ~/.zshrc # this cmd will add the alias to the zsh terminal

echo "alias cs8='cd ~/team8/code_clinics/ && python3 main_for_commandline.py'" >> ~/.bashrc # this cmd will add the alias to the bash terminal


# this variable will only be used for the functionality of the while loop
_install_commands="C"


while [ $_install_commands = "C" ]
do
# changing the value of this variable prevents the while loop from recuring.
_install_commands="B"

# if the user decides to configure the cs8 shortcuts after the installation of # the application, they can do so by typing cs8-cuts on their terminal
echo "alias cs8-cuts='cd ~/team8/code_clinics/ && ./config_8cuts.sh'" >> ~/.zshrc

echo "alias cs8-cuts='cd ~/team8/code_clinics/ && ./config_8cuts.sh'" >> ~/.bashrc

echo -n "Do you want to configure these code clinics shortcuts?

                        cs8-su   >|<   cs8 switch user

                        cs8-a    >|<   cs8 add

                        cs8-vs   >|<   cs8 view slot

                        cs8-bs   >|<   cs8 book slot

                        cs8-cs   >|<   cs8 cancel slot

                        cs8-cb   >|<   cs8 cancel booking

                        cs8-out  >|<   cs8 logout

note: This action will add more commands to your terminal scripts [.bashrc & .zshrc].
 
optional* [Y/N]: "

read -n1 Input
echo

case $Input in
([Yy]):
_install_commands="Y"

# These aliasies will cater for the zsh terminal
 
echo "alias cs8-su='cs8 switch user'" >> ~/.zshrc
echo "alias cs8-a='cs8 add'" >> ~/.zshrc
echo "alias cs8-vs='cs8 view slots'" >> ~/.zshrc
echo "alias cs8-bs='cs8 book slot'" >> ~/.zshrc
echo "alias cs8-cs='cs8 cancel slot'" >> ~/.zshrc
echo "alias cs8-cb='cs8 cancel booking'" >> ~/.zshrc
echo "alias cs8-out='cs8 logout'" >> ~/.zshrc
echo "alias cs8-h='cs8 help'" >> ~/.zshrc

# These aliasies will cater for the bash terminal

echo "alias cs8-su='cs8 switch user'" >> ~/.bashrc
echo "alias cs8-a='cs8 add'" >> ~/.bashrc
echo "alias cs8-vs='cs8 view slots'" >> ~/.bashrc
echo "alias cs8-bs='cs8 book slot'" >> ~/.bashrc
echo "alias cs8-cs='cs8 cancel slot'" >> ~/.bashrc
echo "alias cs8-cb='cs8 cancel booking'" >> ~/.bashrc
echo "alias cs8-out='cs8 logout'" >> ~/.bashrc
echo "alias cs8-h='cs8 help'" >> ~/.bashrc

# To show that the Aliasies were successfully configured 
echo "you have successfully configured cs8 shortcuts for fast and reliable usage!"
;;
esac
done

# all parkages have been installed
# execute the programme

echo "-"
echo "Installation complete!"
echo "-"
echo "Restart the terminal and type: cs8"
