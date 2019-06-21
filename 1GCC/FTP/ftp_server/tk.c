#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

void strcut(char str[], char kw[], char p[]){
    int count = 0;
    int word = 0;
    for (int i=0; i<strlen(str); i++){
        //printf("%d, %d", word, count);
        //printf("\t%c\t%d\n", str[i], str[i] != ' ');
        if (str[i] != ' '){
            if (word == 0){kw[count] = str[i]; kw[count+1] = '\0';}
            if (word == 1){p[count] = str[i]; p[count+1] = '\0';}
            count++;
            if (str[i+1] == ' '){
                word++;
                p[0] = '\0';
                count = 0;
            }
        }
    }
}

int verifyCmd(char kw[], char p[]){
    char allKw[15][15] = {"help", "cd", "get", "ls", "delete", "mkdir", "put", "status", "quit"};
    char amountP[] = {0,1,1,0,1,1,1,0,0};
    int kwLen = sizeof(allKw)/sizeof(allKw[0]);
    for (int i=0; i<kwLen; i++){
        if (strcmp(kw, allKw[i]) == 0){
            if (amountP[i] == 0 && p[0] == '\0'){
                return 1;
            }
            if (amountP[i] == 1 && p[0] != '\0'){
                return 1;
            }
        }
    }
    kw[0] = '\0';
    p[0] = '\0';
    return 0;
}

/*void displayHelp(SOCKET *sock){
    char help[] = "server:# list of commands: \nserver:# - help: list all available commands \nserver:# - cd: change the current directory \nserver:# - get: download a file \nserver:# - ls: list files and directories \nserver:# - delete: delete a file or a directory \nserver:# - mkdir: create a directory \nserver:# - put: send a file \nserver:# - status: list numbers of connected users \nserver:# - quit: logout the client";
    printf("%s", help);
    send(*sock, help, sizeof(help), 0);
}*/
