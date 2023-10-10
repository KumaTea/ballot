pyinstaller --clean --noconsole --onefile --name ballot --icon .\icons\icon.ico .\main.py
Remove-Item .\dist\ballot-dev.exe
Move-Item -Force .\dist\ballot.exe .\dist\ballot-dev.exe

conda activate 37
python -m venv 37
.\37\Scripts\activate
pip install -r requirements.txt
pyinstaller --clean --noconsole --onefile --name ballot --icon .\icons\icon.ico .\main.py
Remove-Item -Recurse -Force 37
