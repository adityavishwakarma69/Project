#include <cstdlib>
#include <cstdio>
#include <ctime>

char used = (char)0;

void randinit(){
	time_t ct;
	time(&ct);
	srand(ct);
}

void reset(){
	if ((int)used > 10){
		used = (char)0;
		randinit();
		return;
	}
	srand(rand());
}

int randint(int low, int high){
	int range = high - low + 1;
	return low + rand() % range;
	randinit();
}

int randintexc(int low, int high, int exc){
	int ran;
	do{
		ran = randint(low, high);
	}while(ran == exc);
	return ran;
}