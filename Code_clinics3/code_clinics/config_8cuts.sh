#!/bin/bash

# this variable will only be used for the functionality of the while loop
_install_commands="C"


while [ $_install_commands = "C" ]
do
# changing the value of this variable prevents the while loop from recuring.
_install_commands="B"


echo -n "Do you want to configure these code clinics shortcuts?

                        cs8-su   >|<   cs8 switch user

                        cs8-a    >|<   cs8 add

                        cs8-vs   >|<   cs8 view slot

                        cs8-bs   >|<   cs8 book slot

                        cs8-cs   >|<   cs8 cancel slot

                        cs8-cb   >|<   cs8 cancel booking

                        cs8-h    >|<   cs8 help

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
