import requests
import subprocess
import shutil
import os

url = 'https://discord.com/api/download?platform=linux&format=tar.gz'
discord_archive = '/dev/shm/discord.tar.gz'
discord_directory = '/opt/Discord/'
launcher_file = '/usr/share/applications/discord.desktop'
desktop_contents = """
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
"""

def download_discord(url, discord_archive):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(discord_archive, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("Successfully downloaded Discord.")
        else:
            print(f"Failed to Download. Status code: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during download: {str(e)}")

def create_directory():
    try:
        isExist = os.path.exists(discord_directory)
        if not isExist:
            os.makedirs(discord_directory)
            print("Successfully created install directory")
    except Exception as e:
        print(f"Failed to create directory: {str(e)}")

def clean_directory(discord_directory):
    try:
        for filename in os.listdir(discord_directory):
            file_path = os.path.join(discord_directory, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print("Successfully cleaned directory")
    except Exception as e:
        print(f"An error occurred while cleaning the directory: {str(e)}")

def extract_discord(discord_archive, discord_directory):
    try:
        result = subprocess.run(['tar', '-xzf', discord_archive, '-C', discord_directory], check=True)
        if result.returncode == 0:
            print("Successfully extracted files")
        else:
            print(f"Failed to extract files: {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during extraction: {str(e)}")
    except Exception as e:
        print(f"Error during extraction: {str(e)}")

def clean_temp(discord_archive):
    try:
        os.remove(discord_archive)
        print("Successfully removed temporary files.")
    except Exception as e:
        print(f"Failed to remove temporary files: {str(e)}")
        
def check_launcher():
    if not os.path.exists(launcher_file):
        try:
            with open(launcher_file, 'w') as file:
                file.write(desktop_contents.strip())
            print("Desktop entry created successfully.")
        except Exception as e:
            print(f"Failed to create desktop entry: {str(e)}")
    else:
        print("Desktop entry already exists.")  

download_discord(url, discord_archive)
create_directory()
clean_directory(discord_directory)
extract_discord(discord_archive, discord_directory)
clean_temp(discord_archive)
check_launcher()
