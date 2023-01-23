 gcc -c .\AngrySpeaker\AngrySpeaker.c -o AngrySpeaker.o
 gcc -c .\FastPrinter\FastPrinter.c -o FastPrinter.o
 gcc -c .\MathGeek\MathGeek.c -o MathGeek.o
 gcc -c .\ScanningEye\ScanningEye.c -o ScanningEye.o
 gcc -c .\TheOldWise\TheOldWise.c -o TheOldWise.o
 gcc -c .\main.c -o main.o
 gcc .\AngrySpeaker.o .\FastPrinter.o .\main.o  .\ScanningEye.o .\TheOldWise.o .\MathGeek.o -o main.exe
 
 pause