#include "enetServer.h"

ENetAddress address;
ENetHost *server;
ENetPeer *peer;
ENetEvent event;
int count=0;
int cpt=0;
int idx;

char recMess[200];
char mess[200];

int nbConnectes;
int estConnecte[4];

int fsm;

int num;

void sendBroadcast(char *mess)
{
	char buffer[500];

	//for (int i=0;i<12;i++)
	for (int i=0;i<8;i++)
		buffer[i]=0;
	//buffer[8]=1;
	buffer[8]=4;

	int len=strlen(mess);
	int cpt=0;
	for (cpt=0;cpt<len;cpt++)
		buffer[9+cpt]=mess[cpt];
	buffer[9+cpt]=0;

	printf("len=%d %s\n",len,mess);

	ENetPacket * packet = enet_packet_create (buffer, 10+len, ENET_PACKET_FLAG_RELIABLE);
	enet_host_broadcast (server, 1, packet);
}

void sendCoonecte()
{
	char mess[500];

	sprintf(mess,"YES");
	sendBroadcast(mess);
}

void handleIncomingMessage()
{
	printf("fsm=%d\n",fsm);
	int dir;
	switch (fsm)
	{
		case 0:
			if (recMess[0]=='C')
			{
				sendCoonecte();
				dir=static_cast<int>(recMess[1])-48;
				printf("dir=%d\n",dir);
				if (estConnecte[dir]==0)
				{
					nbConnectes++;
					estConnecte[dir]=1;
					printf("nbConnectes=%d\n",nbConnectes);
					for (int i=0;i<4;i++)
						printf("estConnecte[%d]=%d\n",i,estConnecte[i]);
					//sendEstConnecte(dir);
				}
			}
			if (recMess[0]=='I'){
				char mess[500];
				sprintf(mess,"AFFICHE");
				sendBroadcast(mess);
			}
			if (recMess[0]=='T'){
				printf("recMess=%s\n",recMess);
				char mess[1000];
				if (recMess[1]=='0')
					sprintf(mess,"E 0 I src/i1.jpg 10 I src/i2.png 5 V src/v2.ogg V src/v1.webm");
				if (recMess[1]=='1')
					sprintf(mess,"E 1 I src/i1.jpg 10 I src/i2.png 5 V src/v1.webm");
				sendBroadcast(mess);
				printf("envoi de %s\n",mess);
			}


			break;
		default:
			break;
	}
	printf("en sortant fsm=%d\n",fsm);
}

int main (int argc, char ** argv) 
{
	printf("enet_initialize()\n");

	if (enet_initialize () != 0) // Initialisation de la librairie
	{
        	fprintf (stderr, "An error occurred while initializing ENet.\n");
        	return EXIT_FAILURE;
    	}

	address.host = ENET_HOST_ANY; // On écoute sur toutes les interfaces

	address.port = 4242; // On écoute sur le port 4242
	printf("enet_host_create()\n");

	server = enet_host_create (& address, 32, 2, 0, 0);
	if (server == NULL)
	{
       		fprintf (stderr, 
			"An error occurred while trying to create an ENet server host.\n");
       		exit (EXIT_FAILURE);
    	}

    	printf("before while() mainloop\n");
 
	fsm=0;


   	while (1)
   	{

    		while (enet_host_service (server, &event, TOMAX) > 0)
    		{
       			switch (event.type)
       			{
          			case ENET_EVENT_TYPE_CONNECT:
             				printf ("A new client connected from %x:%u.\n", 
							event.peer -> address.host, event.peer -> address.port);
             			break;
          			case ENET_EVENT_TYPE_RECEIVE:
								//printf ("A packet of length %u containing %s was received from %s on channel %u.\n", 
						//	(int)event.packet -> dataLength, 
						//	(char*)event.packet -> data, 
						//	(char*)event.peer -> data, (int)event.channelID);
						peer=event.peer;
						//strcpy(recMess,(char*)(event.packet->data)+9);
						idx=0;
						for (int i=9;i<(int)event.packet->dataLength;i++)
						{
							//printf("%c",(char)event.packet->data[i]);
							recMess[idx++]=(char)event.packet->data[i];
						}
						recMess[idx++]='\0';
						printf("recMess=|%s|\n",recMess);
						enet_packet_destroy (event.packet);
						handleIncomingMessage();
             		break;
          			case ENET_EVENT_TYPE_DISCONNECT:
             				printf ("%s disconnected FPX.\n", (char*)event.peer -> data);
             				event.peer -> data = NULL;
       			}
    		}
	}

	atexit (enet_deinitialize);
}
