#include <gui/homescreen_screen/HomeScreenView.hpp>
#include <gui/homescreen_screen/HomeScreenPresenter.hpp>

HomeScreenPresenter::HomeScreenPresenter(HomeScreenView& v)
    : view(v)
{

}

void HomeScreenPresenter::activate()
{

}

void HomeScreenPresenter::deactivate()
{

}

void HomeScreenPresenter::updateHomeScreen(OBDQueueElement_t* pOBD2Data)
{
	switch(pOBD2Data->pid){
		case OBD2_PID_VEHICLE_SPEED:
			view.updateSpeed(pOBD2Data->uwData);
			break;

		case OBD2_PID_ENGINE_SPEED:
			view.updateRPMs(pOBD2Data->uwData);
			break;

		case OBD2_PID_ENGINE_COOLANT_TEMP:
			view.updateCoolantTemp(pOBD2Data->uwData);
			break;

		case OBD2_PID_FUEL_TANK_LEVEL_INPUT:
			view.updateFuelTankLevel(pOBD2Data->uwData);
			break;

		// don't need to update anything on this screen
		default:
			break;
	}
}

void HomeScreenPresenter::saveSpeed(uint32_t newSpeed)
{
	model->setSpeed(newSpeed);
}

void HomeScreenPresenter::saveRPM(uint32_t newRPM)
{
	model->setRPM(newRPM);
}

uint32_t HomeScreenPresenter::getRPM()
{
	return model->getRPM();
}

uint32_t HomeScreenPresenter::getSpeed()
{
	return model->getSpeed();
}
