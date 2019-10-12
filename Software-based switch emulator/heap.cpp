#include "Heap.h"
#include "Queue.h"
#include "packet.h"
#include <iostream>
#include <fstream>

using namespace std;

// Default constructor in which we initialize a vector to store elements
Heap::Heap()
{
	vector<string> priorityQ;
}

// function which returns the parent of a given child
int Heap::getParent(int child)
{
	if (child % 2 == 0)
		return (child / 2) - 1;
	else
		return child / 2;
}

// similar to getParent function, except it returns the left child of given parent
int Heap::getLeftChild(int parent)
{
	return 2 * parent + 1;
}

// returns the right child of given parent
int Heap::getRightChild(int parent)
{
	return 2 * parent + 2;
}

// returns the size of the heap 
int Heap::getSize()
{
	return priorityQ.size();
}

// inserts an element to the very back of the vector
void Heap::insertHeap(string packet)
{
	priorityQ.push_back(packet);
}

// function swaps the child with it's parent
void Heap::swap(int child, int parent)
{
	string temp;
	temp = priorityQ[child];
	priorityQ[child] = priorityQ[parent];
	priorityQ[parent] = temp;
}

// This function is very similar to swap, as it keeps swapping the latestchild that was pushed
// at the back of the heap until it is in it's right postion
// in this case, if the priority is 2 of the element, then it will keep bubbling up until
// another element with priority 2 is found or higher
void Heap::bubbleUp()
{
	int latestChild = priorityQ.size() - 1;
	int parent = getParent(latestChild);

	packet a;
	packet b;
	a.setData(priorityQ[latestChild]);
	b.setData(priorityQ[parent]);

	a.setPriority(priorityQ[latestChild]);
	b.setPriority(priorityQ[parent]);


	while ((a.getPriority() > b.getPriority()) && latestChild >= 0 && parent >= 0) {
		swap(latestChild, parent);
		latestChild = parent;
		parent = getParent(latestChild);
	}
}

// function that prints the entire heap
void Heap::printHeapData()
{

	for (int i = 0; i < priorityQ.size(); i++)
	{
		cout << priorityQ[i];
		cout << endl;
	}
}

// function to check whether the heap is empty
bool Heap::isHeapEmpty() {
	if (priorityQ.size() == 0)
		return true;
	else
		return false;
}

// function which returns the data at any given index when needed
string Heap::getDataAt(int index)
{
	return priorityQ[index];
}