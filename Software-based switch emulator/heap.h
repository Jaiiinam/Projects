#pragma once

#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include "packet.h"

using namespace std;

class Heap
{

public:

	// Default constructor
	Heap();

	// Get member function values for the heap
	int getParent(int parent);
	int getLeftChild(int parent);
	int getRightChild(int parent);
	int getSize();

	// Other public member funcions for heap class
	void insertHeap(string packet);
	void swap(int child, int parent);
	void bubbleUp();
	void printHeapData();
	bool isHeapEmpty();
	string getDataAt(int index);

private:
	// The vector to store the heap implementation
	vector<string> priorityQ;

};
