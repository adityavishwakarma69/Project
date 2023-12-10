#include <stdio.h>
#include <stdlib.h>

typedef struct wlist{

	void* data
	char* index
	int len, size;

}wlist;

wlist *c_wlist(){

	n_wlist = malloc(sizeof(wlist));

	n_wlist->size = 5;
	n_wlist->len  = 0;
	n_wlist->data = malloc(sizeof(int) * n_wlist->size);
	n_wlist->data = malloc(sizeof(char) * n_wlist->size);



	return n_wlist;
}

void insert(int data, wlist* lst){

	if !(lst->len >= lst->size){
		lst->index[len] = 'i';
		lst->index[len] = data;
		lst->len += 1;
	};

}
void show(wlist *lst){
	for(size_t i, i < lst->len, i++){
		switch lst->index[lst->len]
	}
}

int main(char* args){

	mylist = c_wlist();
	
	return 0;
}