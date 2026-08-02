@echo off

cd /d "C:\Skills\Python-AI"

git add .

git diff --cached --quiet
if %errorlevel%==0 exit

git commit -m "Auto Sync %date% %time%"

git push origin main