# MoveXMLs---XML-File-Management-Tool
MoveXMLs is a Python GUI tool for batch copying XML files based on a list of file IDs provided in a .txt file. This application helps users locate specific XML files, copy them to an output folder, and logs any missing files. Built with tkinter, the app offers an easy-to-use interface and gives fun, randomized messages upon completion.

Features

    Load ID List: Easily load a .txt file with XML file IDs for batch processing.
    XML File Check and Copy: Searches for XML files in a designated folder, copies existing files to an output folder, and logs missing files.
    Missing File Logging: Creates a Missing.txt log file listing all missing files for easy reference.
    Random Completion Messages: Displays a random “Done” or error message on completion for a fun user experience.

Requirements

    Python 3.x
    Required libraries:
        tkinter (usually included with Python)
        os, shutil, random

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/moveXMLs.git
cd moveXMLs

Run the script:

bash

    python moveXMLs.py

Usage

    Run Application: Start the tool by running python moveXMLs.py.
    Load ID List:
        Click Load Files in the GUI to select a .txt file containing XML file IDs. Each line should contain one ID (e.g., 12345).
        The script will search for XML files in the designated folder, named in the format asset-<ID>.xml.
    Results:
        Found Files: Existing files will be copied to the Output folder.
        Missing Files: Missing files are recorded in Missing.txt within the Output folder.
    Completion Message: A randomized message will indicate whether all files were found or if some files are missing.

Configuration

    File Directory:
        Update allXMLs to the directory containing your XML files. The default path is R:\\ITV\\All XML.
    Output Directory:
        By default, an Output folder is created in the script's current directory to store copied files and logs.

Example

    Load File: Click "Load Files" to choose a .txt file with file IDs.
    Output: View copied files in the Output folder. If any files were missing, check Missing.txt in the same folder.
