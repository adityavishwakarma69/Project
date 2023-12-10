//g++ main.cpp -o main -lraylib -lGL -lm -lpthread -ldl -lrt

#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argl, char **args){
    char command[100];

    if(argl >= 3){
    sprintf(command, "g++ %s -o %s -lraylib -lGL -lm -lpthread -ldl -lrt", args[1], args[2]);
    }
    else if(argl == 2){
    sprintf(command, "g++ %s -lraylib -lGL -lm -lpthread -ldl -lrt", args[1]);        
    }
    else{
        return 0;
    };
    system(command);

    return 0;
}