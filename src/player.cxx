#include "player.hxx"

Player::Player() :
    _cam({
        {0.0f, 2.0f, 4.0f},
        {0.0f, 2.0f, 0.0f},
        {0.0f, 1.0f, 0.0f},
        60.0f,
        CAMERA_PERSPECTIVE
    }),
    _camMode(CAMERA_FIRST_PERSON)
{
    DisableCursor();
}

const Camera3D &Player::getCam() { return _cam; };

void Player::tick() {
    UpdateCameraPro (
        &_cam,
        (Vector3) {
            (IsKeyDown(KEY_PERIOD)) * 0.1f -
            (IsKeyDown(KEY_E)) * 0.1f,
            (IsKeyDown(KEY_U)) * 0.1f -
            (IsKeyDown(KEY_O)) * 0.1f,
            0.0f
        },
        (Vector3) {
            GetMouseDelta().x * 0.05f,
            GetMouseDelta().y * 0.05f,
            0.0f
        },
        0.0f
    );
}