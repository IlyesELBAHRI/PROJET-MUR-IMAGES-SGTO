all: enetServer

enetServer: enetServer.o
	g++ -o enetServer enetServer.o -std=c++11 -L/usr/local/lib -lenet

enetServer.o: enetServer.cpp enetServer.h
	g++ -c -I/usr/local/include -std=c++11 enetServer.cpp

clean:
	rm enetServer enetServer.o jeu.o
