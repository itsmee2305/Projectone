import os
import difflib

start_path = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    r"C:\Users\chima\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
]
app_path = {}
for menu_path in start_path:
    for root, dirs, files in os.walk(menu_path):
        for file in files:
            if file.endswith(".lnk"):
                app_name = file[:-4]  # Remove the ".lnk" extension
                app_name = app_name.lower()  # Convert to lowercase for case-insensitive matching
                app_path[app_name] = os.path.join(root, file)

# Convert user input to lowercase for case-insensitive matching
command = input("Which app should I open? ").lower()

matches = []

for app_name, app_link in app_path.items():
    if command in app_name:
        matches.append((app_name, app_link))

# If no matches found, checks for fuzzy matching
if len(matches) == 0:
    # Pass the ENTIRE list of app keys all at once!
    close_names = difflib.get_close_matches(
        command, list(app_path.keys()), n=5, cutoff=0.4)
    for name in close_names:
        matches.append((name, app_path[name]))

if len(matches) == 0:
    print(f"App not found.")
elif len(matches) == 1:
    os.startfile(matches[0][1])  # Open the app using the path
    print(f"Opening {matches[0][0]}...")
else:
    print("Multiple matches found:")

    for i, match in enumerate(matches, start=1):
        # match[0] gets the clean name of the app
        print(f"{i}: {match[0]}")

    while True:
        try:
            choice_num = int(input("Type the number of the app you want: "))

            # Check if the number they typed is actually on our menu list
            if 1 <= choice_num <= len(matches):
                break  # Valid number! Break the loop and proceed
            else:
                print(f"Please pick a number between 1 and {len(matches)}.")

        except ValueError:
            # This triggers if int() crashes because they typed words/letters
            print("Invalid input. Please enter a valid number.")

    chosen_match = matches[choice_num - 1]

    os.startfile(chosen_match[1])
    print(f"Opening {chosen_match[0]}...")
