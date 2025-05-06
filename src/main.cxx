#include <raylib.h>

int main(int argc, char *argv[]) {
    InitWindow(800, 450, "rfps");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}