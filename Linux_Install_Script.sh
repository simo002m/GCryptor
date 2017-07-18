#Copy the file to /usr/local/bin and change permissions to match the other files 
#in that directory.
sudo cp gcryptor.py /usr/local/bin/gcryptor
sudo chown root:root /usr/local/bin/gcryptor
sudo chmod a-rwx /usr/local/bin/gcryptor
sudo chmod a+rx /usr/local/bin/gcryptor
sudo chmod u+w /usr/local/bin/gcryptor

#Make a .desktop file so it's easily accesable in the menu and will appear as an icon.
#Then copy it to /usr/share/applications and change permissions
sudo cp gcryptor.desktop /usr/share/applications
sudo chown root:root /usr/share/applications/gcryptor.desktop
sudo chmod a-rwx /usr/share/applications/gcryptor.desktop
sudo chmod a+r /usr/share/applications/gcryptor.desktop
sudo chmod u+w /usr/share/applications/gcryptor.desktop

#Copy the image into /usr/share/icons
sudo cp gcryptor_icon.gif /usr/share/icons
