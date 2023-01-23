@echo off
rem /****************************************************************************/
rem /****************************************************************************/
rem /**************************		Author: SAHER GHANEM 	*********************/
rem /**************************		   ITI-INTAKE43         *********************/
rem /**************************		   Batch_Script		    *********************/
rem /**************************		   Version:1.00 	    *********************/
rem /**************************		DATE: 01/08/2022       	*********************/
rem /****************************************************************************/
rem /****************************************************************************/


setlocal EnableDelayedExpansion

if not exist "Text files" (
mkdir "Text Files"
)
if not exist "Source files" (
mkdir "Source Files"
)
if not exist "Header files" (
mkdir "Header Files"
)

for /f "tokens=1-4" %%a in (Input.txt) do (

if not exist %%a (
mkdir %%a
)

cd %%a
if not exist %%b (
echo 0 >%%b
) else (
set /p count=<%%b
set /a count+=1
echo !count!>%%b
)

if not exist %%c (
echo 0 >%%c
) else (
set /p count=<%%c
set /a count+=1
echo !count!>%%c
)

if not exist %%d (
echo 0 >%%d
) else (
set /p count=<%%d
set /a count+=1
echo !count!>%%d
)
cd ..
copy /y %%a\*.txt "Text Files">nul
copy /y %%a\*.c "Source Files">nul
copy /y %%a\*.h "Header Files">nul

)