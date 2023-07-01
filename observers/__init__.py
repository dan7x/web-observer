# Via https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
# DO NOT MODIFY THIS FILE -- THE SCANNER MAY BREAK!

import os
for scanner in os.listdir(os.path.dirname(__file__)):
    if scanner == '__init__.py':
        continue
    elif scanner[-3:] != '.py':
        print(f"Error at scanner file '{scanner}': all scanner files must be Python scripts.\n"
              f"Please remove this file, or change it to a valid Python script.")

    __import__("observers." + scanner[:-3], locals(), globals())
del scanner
