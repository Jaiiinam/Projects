#pragma once
#include <string>
#include <iostream>
#include <sstream>
using namespace std;
#define MAX_SIZE 10000  //maximum size of the array that will store Queue. 

#ifndef QUEUE_H
#define QUEUE_H

//Creating Class for Queue
class Queue
{
public:

	// Default Constructor
	Queue();
	
	//Defining public functions 
	bool IsEmpty();
	bool IsFull();
	void Enqueue(string x);
	void Dequeue();
	string Front();
private:
	// Packet Variables
	string queue[MAX_SIZE];
	char packetArray[80];
	int front, rear;
};
#endif