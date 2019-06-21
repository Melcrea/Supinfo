#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void inputUser(char tag[], char str[]){
    printf("%s", tag);
    scanf("%[^\n]", str);
    clearBuffer();
}

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
    char allKw[2][6] = {"open"};
    char amountP[] = {1};
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

void clearBuffer(){
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }
}
