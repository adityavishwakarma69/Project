#include<stdio.h>
#include<stdlib.h>

typedef struct queue{
  int * data;
  int front, rear;
  int len;
}queue;

queue* new_queue(){
  queue* new = malloc(sizeof(queue));
  new->front = -1;
  new->rear = -1;
  new->len = 4;
  new->data = malloc(new->len * sizeof(int));
  return new;
}

void enqueue(queue * que, int num){
  if (que->front != 0 && que->front != -1){
    for (size_t i = que->front; i < que->rear + 1; i++){
      que->data[i - que->front] = que->data[i];
    }
    que->rear -= que->front;
    que->front = 0;
  };
  if (que->rear == que->len){
    //fprintf(stderr, "%s", "queue is full\n");
    //exit(-1);
    que->len += 5;
    que->data = realloc(que->data, sizeof(int) * que->len);
  };

  if (que->front == -1){
    que->front = 0;
    que->rear = 0;
  }
  else{
    que->rear += 1;
  };

  que->data[que->rear] = num;
}

int dequeue(queue * que){
  if (que->front == -1){
    fprintf(stderr, "%s", "queue is empty\n");
    exit(-1);
  };

  int num; num = que->data[que->front];
  
  if (que->front == que->rear){
    que->front = -1;
    que->rear = -1;
  }
  else{
    que->front += 1;
  };
  return num;
}

void print_queue(queue * que){
  for (size_t i = que->front; i < que->rear + 1; i++){
    printf("%d  ", que->data[i]);
  }
  printf("\n");
}

int main(){

  queue * myqueue = new_queue();
  

  enqueue(myqueue, 10);
  enqueue(myqueue, 20);
  enqueue(myqueue, 30);
  enqueue(myqueue, 40);
  enqueue(myqueue, 50);
  enqueue(myqueue, 60);
  enqueue(myqueue, 70);
  enqueue(myqueue, 80);
  enqueue(myqueue, 90);
  enqueue(myqueue, 100);
  enqueue(myqueue, 120);
  enqueue(myqueue, 130);
  print_queue(myqueue);
  printf("dequeued %d\n", dequeue(myqueue));
  printf("dequeued %d\n", dequeue(myqueue));
  printf("dequeued %d\n", dequeue(myqueue));
  print_queue(myqueue);

  return 0;
}
