#ifndef MODEL_HPP
#define MODEL_HPP

#include "stm32h7xx_hal.h"
#include "cmsis_os.h"
#include "obd2.h"

class ModelListener;

class Model
{
public:
    Model();

    void bind(ModelListener* listener)
    {
        modelListener = listener;
    }

    void tick();

    // getters
    uint32_t getSpeed();
    uint32_t getRPM();
    // setters
    void setSpeed(uint32_t newSpeed);
    void setRPM(uint32_t newRPM);

protected:
    ModelListener* modelListener;
    // we want to know the state of most important two parameters
    uint32_t crrSpeed;
    uint32_t crrRPM;

};

#endif // MODEL_HPP
