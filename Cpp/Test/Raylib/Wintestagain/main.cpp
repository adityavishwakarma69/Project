#include<raylib.h>

int main(void){

  const int screenWidth = 500;
  const int screenHeight = 500;

  InitWindow(screenWidth, screenHeight, "WINDOW");

  SetTargetFPS(60);

  while (!WindowShouldClose()){

    BeginDrawing();

    ClearBackground(BLACK);

    DrawText("Hello, World!", screenHeight / 2, screenWidth / 2, 20, RED);

    EndDrawing();
  
  }

  CloseWindow();

  return 0;
}
