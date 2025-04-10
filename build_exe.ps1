pyinstaller -w --onefile --paths .venv/Lib/site-packages main.py -n qrcode-generator-GUI.exe
cp icon.ico dist/icon.ico
