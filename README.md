# linux-discord-update
Simple python script to update (or install) Discord.

This will install and update Discord to /opt/Discord/
If you use this to install, you will probably want to create a .desktop file.

Open terminal and run:
nano /usr/share/applications/discord.desktop

Paste the following:
[Desktop Entry]
Name=Discord
StartupWMClass=discord
Comment=All-in-one voice and text chat for gamers that's free, secure, and works on both your desktop and phone.
GenericName=Internet Messenger
Exec=/opt/Discord/Discord/Discord
Icon=/opt/Discord/Discord/discord.png
Type=Application
Categories=Network;InstantMessaging;
Path=/opt/Discord/Discord/
