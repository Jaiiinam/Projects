#include "Queue.h"
#include <iostream>
using namespace std;

// Default Constructor
Queue::Queue()
{

	//At the start no pointer is front or rear
	front = -1;
	rear = -1;

}

// To check wheter Queue is empty or not
bool Queue::IsEmpty()
{
	//If front and rear is -1 means they are back to start position which says array is empty
	return (front == -1 && rear == -1);
}

// To check whether Queue is full or not
bool Queue::IsFull()
{
	//Making rear point to the next space of the array if it can point then return false or else return true
	return (rear + 1) % MAX_SIZE == front ? true : false;
}

// Inserts an element in queue at rear end
void Queue::Enqueue(string packet)
{
	//Checking if the array is full or not before inserting an element
	if (IsFull())
	{
		cout << "Error: Queue is Full\n";
	}

	//Checking if the array is completey empty which means front and rear will be at -1 
	//If it is then make them put to 0th position of the array
	if (IsEmpty())
	{
		front = rear = 0;
	}
	//If none of the above condition works then create an extra space at the end of the array and make rear point to it
	else
	{
		rear = (rear + 1) % MAX_SIZE;
	}

	//This inserts that element in the space which was created 
	queue[rear] = packet;
}

// Removes an element in Queue from front end. 
void Queue::Dequeue()
{
	//Check if the array is empty
	if (IsEmpty())
	{
		cout << "Error: Queue is Empty\n";
	}
	//If the element which needs to be removed 
	//is the same element where both front and rear points 
	//make front and rear point to -1 to remove that only one element
	else if (front == rear)
	{
		rear = front = -1;
	}

	//Make front point to the next array position to remove that element 
	else
	{
		front = (front + 1) % MAX_SIZE;
	}
}

// Returns element at front of queue. 
string Queue::Front()
{
	//If front is point to -1 position which means array is empty and there is no front value
	if (front == -1)
	{
		cout << "Error: cannot return front from empty queue\n";

	}

	//Otherwise just return element which is front pointing to
	return queue[front];
}





  