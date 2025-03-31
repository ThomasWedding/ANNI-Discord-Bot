## README WIP
<h1 align="center">
  Childhood Cancer Society Discord Bot
</h1>

ANNI is a Discord bot created for the Childhood Cancer Society non-profit organization to help manage team members in the Childhood Cancer Society Discord Server.

## ⚙ Features

* Gather progress reports
* Answer common questions from organization members
* Send meeting links at designated times

## 🏛️ PROJECT STRUCTURE:
📂 ANNI-Discord-Bot
┃ ┣ 📂 cache            # Local data saved by the bot
┃ ┃ ┣ 📂 GoogleAPI         # API tokens and credentials for Google services
┃ ┃ ┣ 📂 Links             # YAML files for the link COG that store meeting link URLs
┃ ┃ ┗ 📂 MemberData        # Server and member data file(s) (created by view COG)
┃ ┣ 📂 config           # Configuration files for COGs
┃ ┣ 📂 cogs             # COG files, which are loaded on startup
┃ ┣ 📂 doc              # Command documentation files. Used by the help COG
┃ ┣ 📂 utils            # Python helper scripts for use by COGs
┃ ┃ ┗ 📙 helpers.py        # Main helper file with functions used by COGs
┃ ┣ 📄 requirements.txt # Project dependencies
┗ ┗ 📙 main.py          # Setup file that starts and configures the bot

## 📝 Prerequisites:
* Requires `python 3.11`
* Project dependencies are specified in the `requirements.txt` file. 
* This project currently uses YAML to save data to files.

## ✨ GETTING STARTED:
1. Clone the repository:
   - `git clone https://github.com/ChildhoodCancerSociety/ANNI-Discord-Bot`
2. Create a Python virtual environment in the root of the project directory(BASH/UNIX):
   - `python -m venv .venv`
3. Activate the virtual environment(BASH/UNIX):
   - `. .venv/bin/activate`
4. Install the dependencies specified in the requirements.txt file (BASH/UNIX):
   - `.venv/bin/pip install -r requirements.txt`
5. Create a `.env` in the root directory and add your bot token using the following format:
   - `token=YOUR_BOT_TOKEN`
6. Obtain your `credentials.json` file from your Google Cloud account and place it into the `cache` directory
7. Obtain your `GoogleSheetID.yaml` file with the following contents and place it into the `config` directory:
   - `SPREADSHEET_ID : "YOUR_SHEET_ID"`
8. Start the bot inside of the Python virtual environment:
   - `.venv/bin/python main.py`

## 🪛 GENERAL USAGE:
The command prefix for this bot is `!`.  
With the bot installed and active, use the `!how` command to list all available commands alongside brief descriptions of their functionality. Instructions can also be found in the `/doc` directory.