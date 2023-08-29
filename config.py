import os, time, json
from dotenv import load_dotenv

print("""
Måtta Discord Bot - CONFIG

GitHub repo: 
- https://github.com/luqmanity/matta

Nytra Discord server:
- https://discord.gg/7w8b6MMXBy\n""")
time.sleep(3)

load_dotenv("data/.env") # Loading the .env

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#   Setup function (only for fresh inits)
def setup():
    run = True

    if not os.path.exists("data"):
        print("Missing data folder.")
        os.mkdir("data")
        run = False
    else:
        print("data folder exists.")

    if not os.path.exists("data/.env"):
        print("Missing .env file. Please open and include the bot token later")

        with open("data/.env", "w") as file:
            file.write("")
            run = False
    else:
        print("data/.env exists.")

    if not os.path.exists("data/responses.json"):
        print("Missing data/responses.json")

        with open("data/responses.json", "w") as file:
            responses = {}

            json.dump(responses, file)
            run = False
    else:
        print("data/responses.json exists.")

    if not os.path.exists("data/settings.json"):
        print("Missing data/settings.json")

        with open("data/settings.json", "w") as file:
            settings = {
                "basic settings": {
                    "status": "do_not_disturb",
                    "statusMessage": "Måtta | /help",
                    "statusType": "playing"
                }
            }

            json.dump(settings, file)
            run = False
    else:
        print("data/settings.json exists.")
    
    print("\nSetup complete.")
    return run

run = input("Open Config panel? (y/n): ")

if run == "y":
    print("\n\n\n")
    page = "home"
    page_list = [
            "home"
    ]

    #Config Panel
    while True:
        title = f"{page.upper()} - Måtta Config Panel\n\nChanges only take place after the bot restarts!\n\nActions                 Description\n"

        #   Home
        if page == "home":
            print(f"""
{title}
- basic settings        |   Open BOT basic settings
- setup                 |   Run setup

- home                  |   Return home
- quit                  |   Quit this panel\n""")
            
        #   Basic Settings
        if page == "basic settings":
            print(f"""
{title}
- status                |   Edit the status of the bot
- status msg            |   Edit the message of the RPC
- status type           |   Edit the status type of the bot (playing, watching, etc)

- home                  |   Return home
- quit                  |   Quit this panel\n""")
            
        action = input("Execute action: ")
        clear_console()

        if action in page_list:
            page = action

            #General Actions
        elif action == "home":
            page = "home"

        elif action == "quit":
            confirm = input("Running this from main.py will result in the bot starting after termination. Confirm action? (y/n): ")
            if confirm == "y":
                break

        elif action == "setup" and page == "home":
            setup()
            time.sleep(3)
        
        else:
            print(f"Action ({action}) doesn't exist!")
            time.sleep(3)

    print("Panel closed.")