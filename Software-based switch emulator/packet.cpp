#include "packet.h"
#include <iostream>
#include <csignal>
#include "signal.h"
using namespace std;


// Default Constructor
packet::packet()
{

	//Initializing Variables

	string sourceMAC = " ";
	string destMAC = " ";


	char vlan = ' ';
	char priority = ' ' ;
	string vlanNum = " ";

}

//set function to get source mac address from a packet 
void packet::setSourceMAC(string source)
{
	//Copying specific substring from the packet
	 sourceMAC = source.substr(16, 12);
	
}

//set function to get destination mac address from a packet 
void packet::setDestMAC(string destination)
{
	//Copying specific substring from the packet
	 destMAC = destination.substr(28, 12);
}

//set function to get VLANID from a packet 
void packet::setVlan(string vlanNumber)
{
	// Copying a packet into a char array
	strcpy_s(array, vlanNumber.c_str());

	//Assigning priority value to the priority variable
	char vlans = array[47];
	vlan = vlans;
}

//set function to get priority from a packet
void packet::setPriority(string priorityNumber)
{
	// Copying a packet into a char array
	strcpy_s(array, priorityNumber.c_str());

	//Assigning priority value to the priority variable
	char priorities = array[44];
	priority = priorities;
}

//Setting a function to get a packet
void packet::setData(string packet)
{
	//Copying packet into a variable
	packetData = packet;
}


//Set function to receive payload
void packet::setPayload(string payLoad)
{
	//Copying specific substring from the packet
	payload = payLoad.substr(58, 16);
}

//Set function to receive VLANID
void packet::setVlanNum(string vlan)
{
	//Copying specific substring from the packet
	vlanNum = vlan.substr(45, 3);
}


//returns VLANID
char packet::getVlan()
{
	return vlan;
}

//returns priority number
char packet::getPriority()
{
	return priority;

}

// returns source mac address
string packet::getSourceMAC()
{
	return sourceMAC;
}

// returns destination mac address
string packet::getDestMAC()
{
	return destMAC;
}

//returns packet 
string packet::getData()
{
	return packetData;
}

//returns payload of the packet
string packet::getPayload()
{
	return payload;
}

//returns VLANID of the packet 
string packet::getVlanNum()
{
	return vlanNum;
}