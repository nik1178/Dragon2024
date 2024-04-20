/*********************************************************************************/
/********** THIS FILE IS GENERATED BY TOUCHGFX DESIGNER, DO NOT MODIFY ***********/
/*********************************************************************************/
#ifndef DETAILSSCREENVIEWBASE_HPP
#define DETAILSSCREENVIEWBASE_HPP

#include <gui/common/FrontendApplication.hpp>
#include <mvp/View.hpp>
#include <gui/detailsscreen_screen/DetailsScreenPresenter.hpp>
#include <touchgfx/widgets/Box.hpp>
#include <touchgfx/widgets/Image.hpp>
#include <touchgfx/widgets/BoxWithBorder.hpp>
#include <touchgfx/widgets/TextArea.hpp>
#include <touchgfx/widgets/ButtonWithIcon.hpp>
#include <touchgfx/widgets/TextAreaWithWildcard.hpp>
#include <touchgfx/containers/ModalWindow.hpp>
#include <touchgfx/widgets/ButtonWithLabel.hpp>
#include <touchgfx/widgets/ScalableImage.hpp>

class DetailsScreenViewBase : public touchgfx::View<DetailsScreenPresenter>
{
public:
    DetailsScreenViewBase();
    virtual ~DetailsScreenViewBase();
    virtual void setupScreen();

protected:
    FrontendApplication& application() {
        return *static_cast<FrontendApplication*>(touchgfx::Application::getInstance());
    }

    /*
     * Member Declarations
     */
    touchgfx::Box __background;
    touchgfx::Image background;
    touchgfx::BoxWithBorder boxWithBorder1;
    touchgfx::BoxWithBorder boxWithBorder2;
    touchgfx::BoxWithBorder boxWithBorder3;
    touchgfx::BoxWithBorder boxWithBorder4;
    touchgfx::BoxWithBorder boxWithBorder5;
    touchgfx::BoxWithBorder boxWithBorder6;
    touchgfx::BoxWithBorder boxWithBorder7;
    touchgfx::BoxWithBorder boxWithBorder8;
    touchgfx::BoxWithBorder boxWithBorder9;
    touchgfx::TextArea title;
    touchgfx::ButtonWithIcon homeScreenButton;
    touchgfx::ButtonWithIcon ModalWindowButton;
    touchgfx::TextArea textArea3;
    touchgfx::TextAreaWithOneWildcard textSpeed;
    touchgfx::TextArea textArea4;
    touchgfx::TextArea textArea5;
    touchgfx::TextAreaWithOneWildcard textRPMs;
    touchgfx::TextAreaWithOneWildcard textEngLoad;
    touchgfx::TextAreaWithOneWildcard textCatalystTemp;
    touchgfx::TextAreaWithOneWildcard textIntakeManifoldPressure;
    touchgfx::TextAreaWithOneWildcard textBarometricPressure;
    touchgfx::TextArea textArea6;
    touchgfx::TextArea textArea7;
    touchgfx::TextArea textArea11;
    touchgfx::TextArea textArea15;
    touchgfx::TextArea textArea16;
    touchgfx::TextArea textArea17;
    touchgfx::TextAreaWithOneWildcard textCoolTemp;
    touchgfx::TextAreaWithOneWildcard textIntakeTemp;
    touchgfx::TextAreaWithOneWildcard textAmbientTemp;
    touchgfx::ModalWindow modalWindow1;
    touchgfx::TextArea textArea12;
    touchgfx::ButtonWithLabel closeModalButton;
    touchgfx::ScalableImage endava;
    touchgfx::ScalableImage Sellestial;
    touchgfx::ScalableImage zero;
    touchgfx::ScalableImage leanix;
    touchgfx::ScalableImage landis_gyr;
    touchgfx::ScalableImage qlector;
    touchgfx::ScalableImage celtra;
    touchgfx::ScalableImage plume;
    touchgfx::ScalableImage ixtlant;
    touchgfx::ScalableImage scalableImage1;

    /*
     * Wildcard Buffers
     */
    static const uint16_t TEXTSPEED_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textSpeedBuffer[TEXTSPEED_SIZE];
    static const uint16_t TEXTRPMS_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textRPMsBuffer[TEXTRPMS_SIZE];
    static const uint16_t TEXTENGLOAD_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textEngLoadBuffer[TEXTENGLOAD_SIZE];
    static const uint16_t TEXTCATALYSTTEMP_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textCatalystTempBuffer[TEXTCATALYSTTEMP_SIZE];
    static const uint16_t TEXTINTAKEMANIFOLDPRESSURE_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textIntakeManifoldPressureBuffer[TEXTINTAKEMANIFOLDPRESSURE_SIZE];
    static const uint16_t TEXTBAROMETRICPRESSURE_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textBarometricPressureBuffer[TEXTBAROMETRICPRESSURE_SIZE];
    static const uint16_t TEXTCOOLTEMP_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textCoolTempBuffer[TEXTCOOLTEMP_SIZE];
    static const uint16_t TEXTINTAKETEMP_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textIntakeTempBuffer[TEXTINTAKETEMP_SIZE];
    static const uint16_t TEXTAMBIENTTEMP_SIZE = 10;
    touchgfx::Unicode::UnicodeChar textAmbientTempBuffer[TEXTAMBIENTTEMP_SIZE];

private:

    /*
     * Callback Declarations
     */
    touchgfx::Callback<DetailsScreenViewBase, const touchgfx::AbstractButton&> buttonCallback;

    /*
     * Callback Handler Declarations
     */
    void buttonCallbackHandler(const touchgfx::AbstractButton& src);

};

#endif // DETAILSSCREENVIEWBASE_HPP
