#ifndef HOMESCREENPRESENTER_HPP
#define HOMESCREENPRESENTER_HPP

#include <gui/model/ModelListener.hpp>
#include <mvp/Presenter.hpp>
#include "stm32h7xx_hal.h"
#include "obd2.h"

using namespace touchgfx;

class HomeScreenView;

class HomeScreenPresenter : public touchgfx::Presenter, public ModelListener
{
public:
    HomeScreenPresenter(HomeScreenView& v);

    /**
     * The activate function is called automatically when this screen is "switched in"
     * (ie. made active). Initialization logic can be placed here.
     */
    virtual void activate();

    /**
     * The deactivate function is called automatically when this screen is "switched out"
     * (ie. made inactive). Teardown functionality can be placed here.
     */
    virtual void deactivate();

    virtual ~HomeScreenPresenter() {}

    // we will update some of the information, not the whole screen
    // data flow: model -> gui
	void updateHomeScreen(OBDQueueElement_t* pOBD2Data);
	uint32_t getSpeed();
	uint32_t getRPM();

	// methods to transfer data from view to model
	void saveSpeed(uint32_t newSpeed);
	void saveRPM(uint32_t newRPM);

private:
    HomeScreenPresenter();

    HomeScreenView& view;
};

#endif // HOMESCREENPRESENTER_HPP
