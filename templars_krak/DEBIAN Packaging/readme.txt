1- complete the file /DEBIAN/control

2- Place the elements of the application at their right places, lets say: /usr/bin

3- Give execution rights to the package :

sudo chmod 755 -R package_name

4- MUST ABSOLUTELY delete this readme.txt files dispathed all around here :P

5- Then create the package :

sudo dpkg-deb --build package_name

Done, now we have a nice .deb package installable :

sudo dpkg -i package_name.deb


