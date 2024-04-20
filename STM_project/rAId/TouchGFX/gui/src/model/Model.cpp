#include <gui/model/Model.hpp>
#include <gui/model/ModelListener.hpp>


// A queue to send the data from backend to gui
extern "C" {
	osMessageQueueId_t mid_2Model_Queue;
}

OBDQueueElement_t OBD2Data;

Model::Model() : modelListener(0)
{
	// create message queue
	mid_2Model_Queue = osMessageQueueNew(10, sizeof(OBDQueueElement_t), NULL);
}

void Model::tick()
{
	// if received new message update the screens
	if (osMessageQueueGet(mid_2Model_Queue, &OBD2Data, NULL, 0U) == osOK)
	{
		modelListener->updateDetailsScreen(&OBD2Data);
		modelListener->updateHomeScreen(&OBD2Data);
	}
}

uint32_t Model::getSpeed()
{
	return crrSpeed;
}

uint32_t Model::getRPM()
{
	return crrRPM;
}

void Model::setSpeed(uint32_t newSpeed)
{
	crrSpeed = newSpeed;
}

void Model::setRPM(uint32_t newRPM)
{
	crrRPM = newRPM;
}
