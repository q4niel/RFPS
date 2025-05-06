#include <raylib.h>
#include "player.hxx"

int main(int argc, char *argv[]) {
    InitWindow(1920, 1080, "rfps");
    SetTargetFPS(60);

    Player player;

    while (!WindowShouldClose()) {
        player.tick();

        BeginDrawing();
        ClearBackground(RAYWHITE);
        BeginMode3D(player.getCam());

        DrawCube({0.0f, 0.0f, 0.0f}, 2.0f, 2.0f, 2.0f, RED);
        DrawCubeWires({0.0f, 0.0f, 0.0f}, 2.0f, 2.0f, 2.0f, BLACK);
        DrawGrid(10, 1.0f);

        EndMode3D();
        EndDrawing();
    }

    CloseWindow();
    return 0;
}