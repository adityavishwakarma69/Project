#include "raylib.h"
#include "random.h"
#define GRID_SIZE 20

typedef struct{
	int x;
	int y;
}Vec2D;

typedef struct{
	Vec2D arr[GRID_SIZE * GRID_SIZE];
	int len = 0;
}Vec2DList;

void append(Vec2DList *list, int x, int y){
	list->arr[list->len].x = x;
	list->arr[list->len].y = y;
	list->len += 1;
}
Vec2D pop(Vec2DList *list){
	Vec2D temp = list->arr[list->len - 1];
	list->len -= 1;
	return temp;
}
Vec2D pop(Vec2DList *list, int n){
	Vec2D temp = list->arr[n];
	for(int i = n; i < list->len - 1; i++){
		list->arr[i] = list->arr[i + 1];
	}
	list->len -= 1;
	return temp;
}

void RenderGrid(int grid[GRID_SIZE][GRID_SIZE], int spacex = 500, int spacey = 500, int offsetx = 0, int offsety = 0){
	for(unsigned int i = 0; i < GRID_SIZE; i++){
		for(unsigned int j = 0; j < GRID_SIZE; j++){
			if(grid[i][j] == 1){
				DrawRectangle(j * spacex/GRID_SIZE + offsetx, i * spacey/GRID_SIZE + offsety, 500/GRID_SIZE, 500/GRID_SIZE, GREEN);
			}
			else if(grid[i][j] == 2){
				DrawRectangle(j * spacex/GRID_SIZE + offsetx, i * spacey/GRID_SIZE + offsety, 500/GRID_SIZE, 500/GRID_SIZE, RED);
			}
			else{
				DrawRectangleLines(j * spacex/GRID_SIZE + offsetx, i * spacey/GRID_SIZE + offsety, 500/GRID_SIZE, 500/GRID_SIZE, BLUE);
			};
		}
	}
}

int main(){

	randinit();

	int grid[GRID_SIZE][GRID_SIZE];
	for(unsigned int i = 0; i < 25; i++){
		for(unsigned int j = 0; j < 25; j++){
			grid[i][j] = 0;
		}
	}

	Vec2D snake, dir, food;
	snake.x = 0;
	snake.y = 0;
	dir.x = 0;
	dir.y = 0;
	Vec2DList tail;
	int taillen = 0;
	bool move = false;

	double timer = 0.0d;
	float gamespeed = 0.30f;

	grid[snake.y][snake.x] = 1;
	food.x = randint(0, GRID_SIZE - 1);
	food.y = randint(0, GRID_SIZE - 1);

	const int screen_width = 500;
	const int screen_height = 600;
	InitWindow(screen_width, screen_height, "HELLO");
	SetTargetFPS(60);

	while(!WindowShouldClose()){

		timer += GetFrameTime();

		if(timer >= gamespeed){
			timer = timer - gamespeed;
			move = true;
		};

		if(IsKeyPressed(68) && !dir.x){
			dir.x = 1;
			dir.y = 0;
		}
		else if(IsKeyPressed(65) && !dir.x){
			dir.x = -1;
			dir.y = 0;
		}
		else if(IsKeyPressed(83) && !dir.y){
			dir.y = 1;
			dir.x = 0;
		}
		else if(IsKeyPressed(87) && !dir.y){
			dir.y = -1;
			dir.x = 0;
		};

		if(move){
			if(tail.len > taillen){
				Vec2D erase = pop(&tail, 0);
				grid[erase.y][erase.x] = 0;
			}
			snake.x += dir.x;
			snake.y += dir.y;
			move = false;
			append(&tail, snake.x, snake.y);

			if(snake.x == food.x && snake.y == food.y){
				food.x = randint(0, GRID_SIZE - 1);
				food.y = randint(0, GRID_SIZE - 1);
				taillen += 1;
			};
			if(snake.x < 0 || snake.x >= GRID_SIZE || snake.y < 0 || snake.y >= GRID_SIZE){
				return 0;
			};
			grid[food.y][food.x] = 2;
			for(unsigned int i = 0; i < tail.len; i++){
				grid[tail.arr[i].y][tail.arr[i].x] = 1;
				if((i != tail.len - 1 && snake.x == tail.arr[i].x && snake.y == tail.arr[i].y)){
					return 0;
				};
			}
		};

		BeginDrawing();

		ClearBackground(RAYWHITE);

		RenderGrid(grid);
		DrawRectangleLines(0, 0, screen_width, screen_height - 100, BLUE);
		DrawRectangleLines(1, 1, screen_width - 2, screen_height - 100 -2, RED);

		EndDrawing();


	}



	return 0;
} 