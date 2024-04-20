#ifndef DETAILSSCREENVIEW_HPP
#define DETAILSSCREENVIEW_HPP

#include <gui_generated/detailsscreen_screen/DetailsScreenViewBase.hpp>
#include <gui/detailsscreen_screen/DetailsScreenPresenter.hpp>
#include "stm32h7xx_hal.h"

class DetailsScreenView : public DetailsScreenViewBase
{
public:
    DetailsScreenView();
    virtual ~DetailsScreenView() {}
    virtual void setupScreen();
    virtual void tearDownScreen();

    void updateSpeed(uint32_t speed);
	void updateRPM(uint32_t RPM);
	void updateEngineLoad(float engineLoad);
	void updateCoolantTemp(uint32_t coolantTemp);
	void updateIntakeAirTemp(uint32_t intakeAirTemp);
	void updateAmbientAirTemp(uint32_t ambientAirTemp);
	void updateManifoldPressure(uint32_t manifoldPressure);
	void updateCatalystTemp(float catalystTemp);
	void updateBarometricPressure(uint32_t pressure);

protected:
};

#endif // DETAILSSCREENVIEW_HPP
