#include <stdio.h>
#include <stdlib.h>
#include "server.h"

#ifdef WIN32

    #include <winsock2.h>

#else
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>

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

    const int MAX_CLIENT = 5;
    const int PORT = 1337;
    SOCKADDR_IN serv_addr, cli_addr;
    SOCKET sock, cli_sock;
    char buffer[1024];
    char keyWord[255];
    char param[255];

    //to use TCP/IPV4
    serv_addr.sin_family = AF_INET;
    //to use the port 1337
    serv_addr.sin_port = htons(PORT);
    //to use all network interface
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);

    //bind server
    sock = socket(AF_INET, SOCK_STREAM, 0);
    bind(sock, (SOCKADDR *) &serv_addr, sizeof(serv_addr));
    listen(sock, MAX_CLIENT);

    printf("FTP Server - Port:%d\n", PORT);

    int clilen = sizeof(cli_addr);
    cli_sock = accept(sock,(SOCKADDR *) &cli_addr,&clilen);
    printf("[!] New connection - Client\n", cli_sock);
    while(1){
        recv(cli_sock, buffer, sizeof(buffer), 0);
        printf("[?] Message receive from Client: %s\n", buffer);
        if (analizeCommand(buffer, keyWord, param)){
            printf("[!] Right Command\n", keyWord, param);
            //exCommand(keyWord, param, &cli_sock);
            if (strcmp(keyWord, "help") == 0){
                char help[] = "server:# list of commands: \nserver:# - help: list all available commands \nserver:# - cd: change the current directory \nserver:# - get: download a file \nserver:# - ls: list files and directories \nserver:# - delete: delete a file or a directory \nserver:# - mkdir: create a directory \nserver:# - put: send a file \nserver:# - status: list numbers of connected users \nserver:# - quit: logout the client\n";
                send(cli_sock, help, sizeof(help), 0);
            }
            else if (strcmp(keyWord, "cd") == 0){
                send(cli_sock, "server:# function not available\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "get") == 0){
                send(cli_sock, "server:# function not available\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "ls") == 0){
                send(cli_sock, "server:# function not available\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "delete") == 0){
                send(cli_sock, "server:# function not available\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "mkdir") == 0){
                send(cli_sock, "server:# function not available\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "put") == 0){
                send(cli_sock, "server:# function not available\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "status") == 0){
                send(cli_sock, "server:# device connected (1/1)\n", sizeof(buffer), 0);
            }
            else if (strcmp(keyWord, "quit") == 0){
                send(cli_sock, "server:# bye;)\n", sizeof(buffer), 0);
                closesocket(cli_sock);
                printf("[!] Leave connection - Client\n");
                printf("[?] Waiting new connection...\n");
                cli_sock = accept(sock,(SOCKADDR *) &cli_addr,&clilen);
                printf("[!] New connection - Client\n");
            }
        }
        else{
            printf("[!] Unknown command\n", keyWord, param);
            send(cli_sock, "server:# unknown command\n", sizeof(buffer), 0);
        }
        buffer[0]= '\0';
    }

    #ifdef WIN32
        WSACleanup();
    #endif
    return 0;
}
