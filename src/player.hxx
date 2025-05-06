#pragma once
#include <raylib.h>

class Player {
public:
    Player();
    const Camera3D &getCam();
    void tick();

private:
    Camera3D _cam;
    int _camMode;
};