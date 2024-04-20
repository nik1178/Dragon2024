#include <gui/detailsscreen_screen/DetailsScreenView.hpp>

DetailsScreenView::DetailsScreenView()
{

}

void DetailsScreenView::setupScreen()
{
    DetailsScreenViewBase::setupScreen();
}

void DetailsScreenView::tearDownScreen()
{
    DetailsScreenViewBase::tearDownScreen();
}

void DetailsScreenView::updateSpeed(uint32_t speed)
{
	Unicode::snprintf(textSpeedBuffer, TEXTSPEED_SIZE, "%d", speed);
	textSpeed.resizeHeightToCurrentText();
	textSpeed.invalidate();
}

void DetailsScreenView::updateRPM(uint32_t RPM)
{
	Unicode::snprintf(textRPMsBuffer, TEXTRPMS_SIZE, "%d", RPM);
	textRPMs.resizeHeightToCurrentText();
	textRPMs.invalidate();
}

void DetailsScreenView::updateEngineLoad(float engineLoad)
{
	Unicode::snprintfFloat(textEngLoadBuffer, TEXTENGLOAD_SIZE, "%3.1f", engineLoad);
	textEngLoad.resizeHeightToCurrentText();
	textEngLoad.invalidate();
}

void DetailsScreenView::updateCoolantTemp(uint32_t coolantTemp)
{
	Unicode::snprintf(textCoolTempBuffer, TEXTCOOLTEMP_SIZE, "%d", coolantTemp);
	textCoolTemp.resizeHeightToCurrentText();
	textCoolTemp.invalidate();
}

void DetailsScreenView::updateIntakeAirTemp(uint32_t intakeAirTemp)
{
	Unicode::snprintf(textIntakeTempBuffer, TEXTINTAKETEMP_SIZE, "%d", intakeAirTemp);
	textIntakeTemp.resizeHeightToCurrentText();
	textIntakeTemp.invalidate();
}

void DetailsScreenView::updateAmbientAirTemp(uint32_t ambientAirTemp)
{
	Unicode::snprintf(textAmbientTempBuffer, TEXTAMBIENTTEMP_SIZE, "%d", ambientAirTemp);
	textAmbientTemp.resizeHeightToCurrentText();
	textAmbientTemp.invalidate();
}

void DetailsScreenView::updateCatalystTemp(float catalystTemp)
{
	Unicode::snprintfFloat(textCatalystTempBuffer, TEXTCATALYSTTEMP_SIZE, "%3.1f", catalystTemp);
	textCatalystTemp.resizeHeightToCurrentText();
	textCatalystTemp.invalidate();
}

void DetailsScreenView::updateBarometricPressure(uint32_t pressure)
{
	Unicode::snprintf(textBarometricPressureBuffer, TEXTBAROMETRICPRESSURE_SIZE, "%d", pressure);
	textBarometricPressure.resizeHeightToCurrentText();
	textBarometricPressure.invalidate();
}

void DetailsScreenView::updateManifoldPressure(uint32_t manifoldPressure)
{
	Unicode::snprintf(textIntakeManifoldPressureBuffer, TEXTINTAKEMANIFOLDPRESSURE_SIZE, "%d", manifoldPressure);
	textIntakeManifoldPressure.resizeHeightToCurrentText();
	textIntakeManifoldPressure.invalidate();
}



