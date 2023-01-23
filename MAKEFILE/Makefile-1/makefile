MasterApplication.exe : main.o MathGeek\MathGeek.o \
			FastPrinter\FastPrinter.o ScanningEye\ScanningEye.o \
			AngrySpeaker\AngrySpeaker.o TheOldWise\TheOldWise.o
	gcc main.o MathGeek\MathGeek.o FastPrinter\FastPrinter.o \
		ScanningEye\ScanningEye.o AngrySpeaker\AngrySpeaker.o \
		TheOldWise\TheOldWise.o -o MasterApplication

main.o : main.c
	gcc -c main.c -o main.o

MathGeek\MathGeek.o : MathGeek\MathGeek.c
	gcc -c MathGeek\MathGeek.c -o MathGeek\MathGeek.o 

FastPrinter\FastPrinter.o : Fast