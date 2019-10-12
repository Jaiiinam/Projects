#pragma once

#include <string>
#include <iostream>
#include <sstream>
using namespace std;

#ifndef PACKET_H
#define PACKET_H
//Creating a packet class 

class packet
{
public:
	packet();	// Default Constructor

	//Defining all set functions
	void setSourceMAC(string);
	void setDestMAC(string);
	void setVlan(string);
	void setPriority(string);
	void setData(string);
	void setPayload(string);
	void setVlanNum(string);

	//Defining all get functions
	string getSourceMAC();
	string getDestMAC();
	char getVlan();
	char getPriority();
	string getData();
	string getPayload();
	string getVlanNum();

private:
	// Packet Variables
	string packetData;
	string payload;
	string vlanNum;
	char vlan;
	char priority;
	string sourceMAC;
	string destMAC;
	char array[80];

};
#endif


