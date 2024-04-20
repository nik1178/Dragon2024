#ifndef HOMESCREENVIEW_HPP
#define HOMESCREENVIEW_HPP

#include <gui_generated/homescreen_screen/HomeScreenViewBase.hpp>
#include <gui/homescreen_screen/HomeScreenPresenter.hpp>

class HomeScreenView : public HomeScreenViewBase
{
public:
    HomeScreenView();
    virtual ~HomeScreenView() {}
    virtual void setupScreen();
    virtual void tearDownScreen();

    void updateSpeed(uint32_t speed);
	void updateRPMs(uint32_t RPM);
	void updateCoolantTemp(uint32_t coolantTemp);
	void updateFuelTankLevel(uint32_t fuelTankLevel);

protected:
};

#endif // HOMESCREENVIEW_HPP
