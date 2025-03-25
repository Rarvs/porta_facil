@echo off
REM Navega até a pasta do projeto (ajuste o caminho!)
cd /d "C:\Users\Tetas\Documents\GitHub\porta_facil_fora\porta_facil"

REM Inicia o Waitress na porta 8000
waitress-serve --port=8000 porta_facil.wsgi:application

REM Mantém o terminal aberto após erro (opcional)
pause