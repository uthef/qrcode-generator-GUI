import sys
from application import Application
from console_app import ConsoleApp


if "--no-gui" in sys.argv:
    console_app = ConsoleApp()
    console_app.run()
else:
    gui_app = Application()
    gui_app.run()
