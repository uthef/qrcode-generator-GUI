import qrcode
import time
from fsutils import QR_CODES_DIR, make_sure_directory_exists
from os import system

class ConsoleApp:
    # Startup Animation
    def __startup(self, t):
        print("                                  .___                                                  __")
        time.sleep(t) 
        print("  _____________    ____  ____   __| _/____      ____   ____   ____   ________________ _/  |_  ___________")
        time.sleep(t)  
        print(" / ____/\_  __ \ _/ ___\/  _ \ / __ |/ __ \    / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \ ")
        time.sleep(t) 
        print("< <_|  | |  | \/ \  \__(  <_> ) /_/ \  ___/   / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/ ")
        time.sleep(t) 
        print(" \__   | |__|     \___  >____/\____ |\___  >  \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|")
        time.sleep(t) 
        print("    |__|              \/           \/    \/  /_____/      \/     \/     \/           \/")
        time.sleep(t) 
        print("")
        time.sleep(t)
        print("by Adrian Ceku ")
        print("\n \n \n")


    def run(self):
        self.__startup(0.1)

        # Programexit when set to false false 
        Running = True

        # Console application
        while Running:
            filename = input("Filename: ")
            content = input("Content: ")
            img = qrcode.make(content)

            make_sure_directory_exists(QR_CODES_DIR)
            
            img.save(f"{QR_CODES_DIR}/{filename}.png")
            print(f"File saved as {filename}.png in .../qrcode-generator/QR-Codes/")
            exit = input("Generate another file? (y/n): ")
            if exit == "n":
                print("Bye")
                time.sleep(0.1)
                Running = False
