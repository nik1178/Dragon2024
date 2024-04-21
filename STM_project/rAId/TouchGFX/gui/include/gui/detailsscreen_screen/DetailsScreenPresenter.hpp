#ifndef DETAILSSCREENPRESENTER_HPP
#define DETAILSSCREENPRESENTER_HPP

#include <gui/model/ModelListener.hpp>
#include <mvp/Presenter.hpp>
#include "stm32h7xx_hal.h"
#include "obd2.h"

using namespace touchgfx;

class DetailsScreenView;

class DetailsScreenPresenter : public touchgfx::Presenter, public ModelListener
{
public:
    DetailsScreenPresenter(DetailsScreenView& v);

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

    virtual ~DetailsScreenPresenter() {}

    // we will update particular parts, not the whole screen
    void updateDetailsScreen(OBDQueueElement_t* pOBD2Data);
    void sendBackSpeed(uint32_t newSpeed);
    void sendBackRPM(uint32_t newRPM);
    void sendBackEngLoad(uint32_t newEngLoad);
    void sendBackOilTemp(uint32_t newOilTemp);


private:
    DetailsScreenPresenter();

    DetailsScreenView& view;
};

#endif // DETAILSSCREENPRESENTER_HPP
