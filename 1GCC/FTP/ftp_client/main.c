#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "client.h"
#include "tk.h"

#ifdef WIN32

    #include <winsock2.h>

#else
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>

    #include <netdb.h>

    #define INVALID_SOCKET -1
    #define SOCKET_ERROR -1
    #define closesocket(s) close(s)
    typedef int SOCKET;
    typedef struct sockaddr_in SOCKADDR_IN;
    typedef struct sockaddr SOCKADDR;
    typedef struct in_addr IN_ADDR;

#endif

int main()
{
    #ifdef WIN32
        WSADATA wsa;
        WSAStartup(MAKEWORD(2, 2), &wsa);
    #endif

    SOCKADDR_IN serv_addr;
    SOCKET sock;
    char buffer[1024];
    char bufferRcv[1024];
    char address[255];

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(1337);
    struct hostent *hostinfo;

    do{
        logIn(address); //Analise la validité du saisi de l'utilisateur

        hostinfo = gethostbyname(address); //Essaye de se connecter

        if (hostinfo == NULL) //S'il n'arrive pas à se connecter
        {
            printf("[!] Unknown host - %s\n", address);
        }
    }while(hostinfo == NULL); //Tant que l'on n'est pas connecté

    serv_addr.sin_addr = *(IN_ADDR *) hostinfo->h_addr;

    //connect to server
    sock = socket(AF_INET, SOCK_STREAM, 0);
    connect(sock, (SOCKADDR *) &serv_addr, sizeof(SOCKADDR));
    while(1) {
        inputUser("quest:~$ ", buffer);
        send(sock, buffer, sizeof(buffer), 0);
        recv(sock, bufferRcv, sizeof(bufferRcv), 0);
        printf("%s", bufferRcv);
        if(strcmp(buffer, "quit") == 0){
            closesocket(sock);
            printf("Press a enter to close...");
            scanf("%c", buffer);
            break;
        }
    }

    #ifdef WIN32
        WSACleanup();
    #endif

    return 0;
}
