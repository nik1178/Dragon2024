#include <gui/detailsscreen_screen/DetailsScreenView.hpp>
#include <gui/detailsscreen_screen/DetailsScreenPresenter.hpp>

DetailsScreenPresenter::DetailsScreenPresenter(DetailsScreenView& v)
    : view(v)
{

}

void DetailsScreenPresenter::activate()
{

}

void DetailsScreenPresenter::deactivate()
{

}

void DetailsScreenPresenter::updateDetailsScreen(OBDQueueElement_t* pOBD2Data)
{
	switch(pOBD2Data->pid){
		case OBD2_PID_VEHICLE_SPEED:
			view.updateSpeed(pOBD2Data->uwData);
			model->setSpeed(pOBD2Data->uwData);
			break;

		case OBD2_PID_ENGINE_SPEED:
			view.updateRPM(pOBD2Data->uwData);
			model->setRPM(pOBD2Data->uwData);
			break;

		case OBD2_PID_ENGINE_LOAD:
			view.updateEngineLoad(pOBD2Data->fData);
			model->setEngLoad(pOBD2Data->fData);
			break;

		case OBD2_PID_ENGINE_COOLANT_TEMP:
			view.updateCoolantTemp(pOBD2Data->uwData);
			model->setOilTemp(pOBD2Data->uwData);
			break;

		case OBD2_PID_INTAKE_AIR_TEMP:
			view.updateIntakeAirTemp(pOBD2Data->uwData);
			break;

		case OBD2_PID_AMBIENT_AIR_TEMP:
			view.updateAmbientAirTemp(pOBD2Data->uwData);
			break;

		case OBD2_PID_ABS_BARO_PRESSURE:
			view.updateBarometricPressure(pOBD2Data->uwData);
			break;

		case OBD2_PID_INTAKE_MANIFOLD_PRESSURE:
			view.updateManifoldPressure(pOBD2Data->uwData);
			break;

		case OBD2_PID_ABS_CATALYST_TEMP:
			view.updateCatalystTemp(pOBD2Data->fData);
			break;

		// don't need to update anything on this screen
		default:
			break;
	}
}
