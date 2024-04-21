#include <gui/model/Model.hpp>
#include <gui/model/ModelListener.hpp>


// A queue to send the data from backend to gui
extern "C" {
	osMessageQueueId_t mid_2Model_Queue;
	osMessageQueueId_t hitrost_Queue;
	osMessageQueueId_t obrati_Queue;
	osMessageQueueId_t engLoad_Queue;
	osMessageQueueId_t oilTemp_Queue;
}

OBDQueueElement_t OBD2Data;

Model::Model() : modelListener(0)
{
	// create message queue
	mid_2Model_Queue = osMessageQueueNew(10, sizeof(OBDQueueElement_t), NULL);
	hitrost_Queue = osMessageQueueNew(10, sizeof(uint32_t), NULL);
	obrati_Queue = osMessageQueueNew(10, sizeof(uint32_t), NULL);
	engLoad_Queue = osMessageQueueNew(10, sizeof(uint32_t), NULL);
	oilTemp_Queue = osMessageQueueNew(10, sizeof(uint32_t), NULL);
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
	uint8_t vrednost = (uint8_t) crrSpeed;
	osMessageQueuePut(hitrost_Queue, &vrednost, 0U, 0U);
}

void Model::setRPM(uint32_t newRPM)
{
	crrRPM = newRPM;
	uint8_t vrednost = (uint8_t) (crrRPM/255);
	osMessageQueuePut(obrati_Queue, &vrednost, 0U, 0U);
}

void Model::setEngLoad(uint32_t newEngLoad)
{
	crrEngLoad = newEngLoad;
	uint8_t vrednost = (uint8_t) crrEngLoad;
	osMessageQueuePut(engLoad_Queue, &vrednost, 0U, 0U);
}

void Model::setOilTemp(uint32_t newOilTemp)
{
	crrOilTemp = newOilTemp;
	uint8_t vrednost = (uint8_t) crrOilTemp;
	osMessageQueuePut(oilTemp_Queue, &vrednost, 0U, 0U);
}
