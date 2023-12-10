#include "raylib.h"

int main(void)
{

    const int screenWidth = 450;
    const int screenHeight = 700;

    InitWindow(screenWidth, screenHeight, "sand tetris");

    SetTargetFPS(60);

    while (!WindowShouldClose())
    {

        BeginDrawing();

            ClearBackground(RAYWHITE);

            DrawText("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY);

        EndDrawing();

    }

    CloseWindow();

    return 0;
}