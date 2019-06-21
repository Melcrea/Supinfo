#include "tk.h"

int analizeCommand(char str[], char kw[], char p[]){
    strcut(str, kw, p);
    return verifyCmd(kw, p);
}

/*void exCommand(char kw[], char p[], SOCKET *sock){
    if (strcmp(kw, "help") == 0){
       displayHelp(sock);
    }
    else if (strcmp(kw, "cd") == 0){

    }
    else if (strcmp(kw, "get") == 0){

    }
    else if (strcmp(kw, "ls") == 0){

    }
    else if (strcmp(kw, "put") == 0){

    }
    else if (strcmp(kw, "status") == 0){

    }
    else if (strcmp(kw, "quit") == 0){

    }
}*/
