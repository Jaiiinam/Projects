/*

ITSW ALGORITHMS AND DATA STRUCTURES/OPERATING SYSTEM FINAL PROJECT

Rushi Patel	
Yash Patel 
Jeet Desai 

*/

#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <conio.h>
#include <list>
#include "Queue.h"
#include <thread>
#include "packet.h"
#include <mutex>
#include <csignal>
#include <vector>
#include "Heap.h"

using namespace std;

//Function declaration

void part1(); //Thread 1

void part2(string, string); //Thread 2

void part3(); //Thread 3

			  //Initilaize intial queue to store all packets after reading from packet file
Queue FIFO;
Queue dataQ100;
Queue dataQ101;
Heap pq100;
Heap pq101;


//Initialize locking mechanism for thread 2/3
mutex mtx;

sig_atomic_t signalled = 0;

//main function
int main()
{
	clock_t starttime = clock();
	part1();
	//start time
	
	for (int i = 0; i < pq100.getSize(); i++) 
	{

		dataQ100.Enqueue(pq100.getDataAt(i));
	}

	for (int i = 0; i < pq101.getSize(); i++) {

		dataQ101.Enqueue(pq101.getDataAt(i));
	}
	//initialize thread 1 and join part1 function to execute
	thread number1(part1);
	number1.join(); //executing thread 1


	//initialize thread 3 and join part3 function to execute
	thread number3(part3);
	number3.join();//executing thread 3


				   //end time
	clock_t endtime = clock();

	//calculate total elapsed time of thread 1
	long double elapsedtime = (long double(endtime - starttime) / (CLOCKS_PER_SEC));

	cout << "Elapsed TIme: " << elapsedtime << endl;
	
	system("pause");
	return 0;

}//end main


void signalhandler(int priority)
{
	signalled = 1;
}

void registersignal()
{

	signal(SIGINT, signalhandler);
	raise(SIGINT);
	if (signalled)
	{
		cout << "Priority 2 packet has been detected " << endl;
	}
	else
	{
		cout << "Signal is not handled " << endl;
	}

}

//Thread 1 implementation 
void part1()
{
	//read each packet from packet file and make it equal to this string
	string packetLine = " ";

	//I/O object
	fstream my_stream;

	//open packet file
	my_stream.open("packets.capture");


	//Queueing Process into FIFO queue
	for (int i = 0; i < 9999; i++)
	{
		//read each packet line by line and add into FIFO queue using Enqueue function 
		getline(my_stream, packetLine);
		FIFO.Enqueue(packetLine);
	}

	//close packet file
	my_stream.close();

	// Empty FIFO queue and allocate each packet to its corrosponding vlan

	cout << "Thread 2\n" << endl; //Thread 2 Process
	while (!FIFO.IsEmpty())
	{
		//Read first packet from fifo queue as a copy 
		packet packet;

		//After taking the packet header as a copy assign characteristics from the packer header to the set function
		packet.setPriority(FIFO.Front()); //set Vlan priority
		packet.setVlan(FIFO.Front()); //set vlan 
		packet.setSourceMAC(FIFO.Front()); //set source mac address
		packet.setDestMAC(FIFO.Front()); //set destination mac address

										 //checking for vlan 100 packet that has a priority of 2
		if ((packet.getVlan()) == '0' && (packet.getPriority()) == '2')
		{
			pq100.insertHeap(FIFO.Front());
			pq100.bubbleUp();

			registersignal(); //signal to the screen that prority detected for 101

			//calling this thread everytime as child and executing part2(), which prints packet data to screen and log file
			thread thread2(part2, packet.getSourceMAC(), packet.getDestMAC()); //initialize thread 2 and join part2 function to execute
			thread2.join(); //execute thread 2
		}

		//checking for vlan 100 packet that has a priority of 0
		if ((packet.getVlan()) == '0' && (packet.getPriority()) == '0')
		{
			pq100.insertHeap(FIFO.Front());
		}

		//checking for vlan 101 packet that has a priority of 2
		if ((packet.getVlan()) == '1' && (packet.getPriority()) == '2')
		{
			pq101.insertHeap(FIFO.Front());
			pq101.bubbleUp();

			registersignal(); //signal to the screen that prority detected for vlan 101

			//calling this thread everytime as child and executing part2(), which prints packet data to screen and log file
			thread thread2(part2, packet.getSourceMAC(), packet.getDestMAC()); //initialize thread 2 and join part2 function to execute
			thread2.join(); //execute thread 2
		}
		//checking for vlan 101 packet that has a priority of 0
		if ((packet.getVlan()) == '1' && (packet.getPriority()) == '0')
		{
			pq101.insertHeap(FIFO.Front());
		}

		//Dequeue packet from FIFO after allocated in respective vlan queue
		FIFO.Dequeue();

	}

	

}//end part1() 


 //thread 2 implementation 
void part2(string Smac, string Dmac)
{

	//locking the printing capability to screen and log file for one thread at a time only. Protecting shared resources and mitigating race condition.
	mtx.lock();

	// I/O object
	ofstream myfile;

	cout << "Packets with priority 2" << endl;

	//open log file to write to file
	myfile.open("log.txt", ios::in | ios::out | ios::ate);

	//set timestamp to allocate to each packet
	auto clock = chrono::system_clock::now();
	time_t time = chrono::system_clock::to_time_t(clock);

	//write packet content to log file (timestamp, source mac address and destination mac address)
	myfile << "Time: " << time << " | Source MAC Address: " << Smac << " | Destination MAC Address: " << Dmac << endl;

	//write packet content to screen (timestamp, source mac address and destination mac address)
	cout << "Time: " << time << " | Source MAC Address: " << Smac << " | Destination MAC Address: " << Dmac << " \n" << endl;

	//unlock locking mechanism after allowing the thread to print 
	mtx.unlock();

	//close file
	myfile.close();

} //part2() end

  //thread 3 implementation 
void part3()
{
	//Print VLAN 100 Packets with "2" priority
	cout << "\nThread 3 Output--------------------------------------------------" << endl;
	cout << "Queue of VLAN 100" << endl;

	//while priority queue is not empty, copy packet data to screen/log file
	while (!dataQ100.IsEmpty())
	{
		//read first packet from queue as a copy
		packet data;

		//After taking the packet header as a copy assign characteristics from the packer header to the set function
		data.setPriority(dataQ100.Front()); //set priority
		data.setVlan(dataQ100.Front()); //set vlan
		data.setSourceMAC(dataQ100.Front()); //set source mac address 
		data.setDestMAC(dataQ100.Front()); //set destination mac address
		data.setPayload(dataQ100.Front()); //set payload 
		data.setVlanNum(dataQ100.Front()); //set vlan number

											//locking the printing capability to screen and log file for one thread at a time only. Protecting shared resources and mitigating race condition.
		mtx.lock();

		// I/O object
		ofstream file;

		//open log file to write the packet content log file
		file.open("log.txt", ios::in | ios::out | ios::ate);

		//write packet content to log file (vlan, priority, source/destination mac address, and payload)
		file << "Vlan: " << data.getVlanNum() << " - Priority: " << data.getPriority() << " | Source MAC Address: " << data.getSourceMAC() << " | Destination MAC Address: " << data.getDestMAC() << " | Payload: " << data.getPayload() << endl;

		//write packet content to screen (vlan, priority, source/destination mac address, and payload)
		cout << "Vlan: " << data.getVlanNum() << " - Priority: " << data.getPriority() << " | Source MAC Address: " << data.getSourceMAC() << " | Destination MAC Address: " << data.getDestMAC() << " | Payload: " << data.getPayload() << endl;

		//unlock locking mechanism after thread finishes printing 
		mtx.unlock();

		//close file
		file.close();

		//remove packet from file after printing to screen/log file
		dataQ100.Dequeue();
		this_thread::sleep_for(std::chrono::seconds(1));
	}


	cout << "Queue of VLAN 101" << endl;

	while (!dataQ101.IsEmpty())
	{
		//read first packet from queue as a copy
		packet data2;

		//After taking the packet header as a copy assign characteristics from the packer header to the set function
		data2.setPriority(dataQ101.Front()); //set priority
		data2.setVlan(dataQ101.Front()); //set vlan
		data2.setSourceMAC(dataQ101.Front()); //set source mac address 
		data2.setDestMAC(dataQ101.Front()); //set destination mac address
		data2.setPayload(dataQ101.Front()); //set payload 
		data2.setVlanNum(dataQ101.Front()); //set vlan number

											 //locking the printing capability to screen and log file for one thread at a time only. Protecting shared resources and mitigating race condition.
		mtx.lock();

		// I/O object
		ofstream file;

		//open log file to write packet content to log file
		file.open("log.txt", ios::in | ios::out | ios::ate);

		//write packet content to log file (vlan, priority, source/destination mac address, and payload)
		file << "Vlan: " << data2.getVlanNum() << " - Priority: " << data2.getPriority() << " | Source MAC Address: " << data2.getSourceMAC() << " | Destination MAC Address: " << data2.getDestMAC() << " | Payload: " << data2.getPayload() << endl;

		//write packet content to screen (vlan, priority, source/destination mac address, and payload)
		cout << "Vlan: " << data2.getVlanNum() << " - Priority: " << data2.getPriority() << " | Source MAC Address: " << data2.getSourceMAC() << " | Destination MAC Address: " << data2.getDestMAC() << " | Payload: " << data2.getPayload() << endl;

		//unlock locking mechanism after thread finishes printing 
		mtx.unlock();

		//close file
		file.close();

		//remove packet from file after printing to screen/log file
		dataQ101.Dequeue();
		this_thread::sleep_for(std::chrono::seconds(1));
	}


} //end part3


