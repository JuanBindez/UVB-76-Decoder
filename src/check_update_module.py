import time
import json

import tkinter as tk
from tkinter import messagebox
import urllib.request
import webbrowser


def check_new_version(current_version):
    version_url = "https://raw.githubusercontent.com/JuanBindez/UVB-76-Decoder/main/version.json"

    try:
        with urllib.request.urlopen(version_url) as response:
            version_info = response.read().decode().strip()

        version_data = json.loads(version_info)
        latest_version = version_data.get("version", "")

        if latest_version != current_version:
            message = f"UVB-76 Decoder {latest_version} Available!\n\n"
            message += f"Release Date: {version_data.get('release_date', '')}\n"
            message += f"\nNew:\n{version_data.get('new', '')}"

            link_update = version_data.get('link', '')

            link = link_update[0]

            ask = messagebox.askokcancel("PGPurge", message + "\n\n\n\nwant to download the new version?")
            if ask == True:
                print(link)
                webbrowser.open(link)
                exit()
            elif ask == False:
                exit()

    except urllib.error.URLError:
        messagebox.showerror("Caution", "without Internet! could not check for updates")
