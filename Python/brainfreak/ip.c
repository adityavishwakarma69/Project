#include <stdio.h>
#include <stdlib.h>

typedef struct code{
	char *string;
	int size; 

}code;

typedef struct stack{
	int *data;
	int last;
	int size;

}stack;

code *loadcode(const char* filename){
	code* cd = malloc(sizeof(code));

	FILE* fp = fopen(filename, "r");

	if (fp == NULL){
		printf("FILE DOES NOT EXISTS\n");
		exit(1);
	}

	fseek(fp, 0, SEEK_END);
	cd->size = ftell(fp);
	rewind(fp);

	cd->string = malloc(sizeof(char) * (cd->size));

	for(size_t i = 0; i < cd->size; i++){
		cd->string[i] = fgetc(fp);
	}
	cd->string[cd->size] = '~';

	return cd;
}

stack* nstack(){


	stack* ns = malloc(sizeof(stack));
	ns->size = 10;
	ns->last = -1;
	ns->data = malloc(sizeof(int) * ns->size);

	return ns;

}

void push(stack* s, int elm){

	s->last += 1;
	s->data[s->last] = elm;

	if(s->last >= s->size){
		s->size = 20;
		s->data = realloc(s->data, sizeof(int) * s->size);
	}

}

int pop(stack* s){
	s->last -= 1;
	return s->data[s->last - 1];
}

int last(stack* s){
	return s->data[s->last];
}

int main(int argl, char *args[]){

	code* currcode = loadcode(args[1]);
	stack* st = nstack();

	int run[1000];

	for(size_t i = 0; i < 1000; i++){
		run[i] = 0;
	}

	int p = 500;

	for(size_t i = 0 ; i < currcode->size; i++){

		if(currcode->string[i] == '+'){
			run[p] += 1;
		}
		else if(currcode->string[i] == '-'){
			run[p] -= 1;
		}
		else if(currcode->string[i] == '<'){
			p -= 1;
		}
		else if(currcode->string[i] == '>'){
			p += 1;
		}
		else if(currcode->string[i] == '.'){
			printf("%c", run[p]);
		}
		else if(currcode->string[i] == ','){
			scanf("%c", &run[p]);
		}
		else if(currcode->string[i] == '['){
			if(run[p] != 0){
				push(st, i);
			}
			else{
				while(currcode->string[i] != ']'){
					i += 1;
				}
			};
		}
		else if(currcode->string[i] == ']'){
			if(run[p] != 0){
				i = last(st);
			}
			else{
				pop(st);
			}
		}

	}

	return 0;
}