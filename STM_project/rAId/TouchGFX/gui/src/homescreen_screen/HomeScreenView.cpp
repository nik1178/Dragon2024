#include <gui/homescreen_screen/HomeScreenView.hpp>

HomeScreenView::HomeScreenView()
{

}

void HomeScreenView::setupScreen()
{
    HomeScreenViewBase::setupScreen();
    // last saved data is displaying
    gaugeRPM.setValue(presenter->getRPM());
    Unicode::snprintf(speedTextBuffer, SPEEDTEXT_SIZE, "%d", presenter->getSpeed());
    gaugeSpeed.setValue(presenter->getSpeed());

}

void HomeScreenView::tearDownScreen()
{
    HomeScreenViewBase::tearDownScreen();
    // save data for displaying next time
    presenter->saveSpeed(gaugeSpeed.getValue());
    presenter->saveRPM(gaugeRPM.getValue());
}

void HomeScreenView::updateSpeed(uint32_t speed)
{
	// update speed gauge and text
	gaugeSpeed.setValue(speed);
	Unicode::snprintf(speedTextBuffer, SPEEDTEXT_SIZE, "%d", speed);
	speedText.resizeHeightToCurrentText();
	speedText.invalidate();
	presenter->saveSpeed(speed);
}

void HomeScreenView::updateRPMs(uint32_t RPM)
{
	gaugeRPM.setValue(RPM);
	presenter->saveRPM(RPM);
}

void HomeScreenView::updateCoolantTemp(uint32_t coolantTemp)
{
	coolantTempProgressBar.setValue(coolantTemp);
}

void HomeScreenView::updateFuelTankLevel(uint32_t fuelTankLevel)
{
	fuelTankLevelProgressBar.setValue(fuelTankLevel);
}
