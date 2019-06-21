#include "tk.h"

void logIn(char ip[]){
    char command[255];
    char keyWord[255];
    char param[255];
    do{
        inputUser("quest:~$ ", command);
        strcut(command, keyWord, param);
    }while(!verifyCmd(keyWord, param));
    strcpy(ip, param);
}
