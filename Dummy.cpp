#include <iostream>
#include <string>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <stdexcept>
#include <thread>

using namespace std;

class Ticket {
    int Ticket_ID;
    std::string Customer_name;
    int Priority;
    std::string Service_Request_Description;
    time_t Creation_Time;
    bool Status; // True is closed, False is Open
    time_t Ticket_Close_Time;

public:
    Ticket() : Ticket_ID(0), Customer_name(""), Priority(-1), Service_Request_Description(""), 
               Creation_Time(std::time(nullptr)), Status(false), Ticket_Close_Time(0) {}

    Ticket(int ID, std::string name, int prior, std::string desc) 
        : Ticket_ID(ID), Customer_name(name), Service_Request_Description(desc),
          Creation_Time(std::time(nullptr)), Status(false), Ticket_Close_Time(0) {
        if (prior > 3 || prior < 1) throw std::invalid_argument("Invalid Priority Entered\n");
        else Priority = prior;
        // this_thread::sleep_for(chrono::seconds(1));
    }

    // Destructor
    ~Ticket() {}

    // Getters
    int getTicketID() const { return Ticket_ID; }
    std::string getCustomerName() const { return Customer_name; }
    int getPriority() const { return Priority; }
    std::string getServiceRequestDescription() const { return Service_Request_Description; }
    bool getStatus() const { return Status; }
    time_t getCreationTime() const { return Creation_Time; }
    time_t getTicketCloseTime() const { return Ticket_Close_Time; }

    // Setters
    void setTicketID(int id) { Ticket_ID = id; }
    void setCustomerName(const std::string& name) { Customer_name = name; }
    void setPriority(int priority) { Priority = priority; }
    void setServiceRequestDescription(const std::string& description) { Service_Request_Description = description; }
    void setCreationTime(time_t creationTime) { Creation_Time = creationTime; }
    void setStatus(bool status) { Status = status; }
    void setTicketCloseTime(time_t closeTime) { Ticket_Close_Time = closeTime; }

    void Close_Ticket() {
        this_thread::sleep_for(chrono::seconds(1));
        if (Status) return; // Already closed
        Ticket_Close_Time = std::time(nullptr); // Set close time to current time
        Status = true; // Mark as closed
    }

    void display() const {
        std::cout << "Ticket ID: " << Ticket_ID << std::endl;
        std::cout << "Customer Name: " << Customer_name << std::endl;
        std::cout << "Priority: " << Priority << std::endl;
        std::cout << "Service Request Description: " << Service_Request_Description << std::endl;
        std::cout << "Creation Time: " << std::put_time(std::localtime(&Creation_Time), "%Y-%m-%d %H:%M:%S") << std::endl;
        std::cout << "Status: " << (Status ? "Closed" : "Open") << std::endl;

        if (Status) {
            std::cout << "Ticket Close Time: " << std::put_time(std::localtime(&Ticket_Close_Time), "%Y-%m-%d %H:%M:%S") << std::endl;
        } else {
            std::cout << "Ticket Close Time: Not Applicable (Ticket is still Open)" << std::endl;
        }
    }

    // Copy assignment operator
    Ticket& operator=(const Ticket& tick2) {
        if (this != &tick2) { // Check for self-assignment
            this->Ticket_ID = tick2.getTicketID();
            this->Customer_name = tick2.getCustomerName();
            this->Priority = tick2.getPriority();
            this->Service_Request_Description = tick2.getServiceRequestDescription();
            this->Creation_Time = tick2.getCreationTime();
            this->Status = tick2.getStatus();
            this->Ticket_Close_Time = tick2.getTicketCloseTime();
        }
        return *this;
    }
};

struct Node {

    Ticket ticket;
    Node* next;
    Node(Ticket ticket) : ticket(ticket) , next(nullptr) {}
};

class LinkedList {

    Node* head;

    public:

    LinkedList() : head(nullptr) {}

    void Add_Ticket(Ticket ticket) {
        Node* newnode = new Node(ticket);
        if (head == nullptr) { head = newnode; return; }

        Node* current = head;
        while(current->next != nullptr) {
            current = current->next;
        }

        current->next = newnode;
    }

    Node* getHead() {
        return head;
    }

    void Remove_Ticket(int Ticket_ID) {

        if (head == nullptr) {
            cout << "There are no Tickets in the system\n";
            return;
        }
        Node* current = head;
        while (current->next != nullptr && current->next->ticket.getTicketID() != Ticket_ID) {
            current = current->next;
        }

        if (current->next == nullptr) {
            cout << "The Ticket with ID " << Ticket_ID << " is not present in the system\n";
            return;
        }

        Node* temp = current->next;
        current->next = current->next->next;
        delete temp;
    }

    Ticket Search_Ticket(int Ticket_ID) {
        if (head == nullptr) { cout << "System has no Tickets"; return Ticket();}
        Node* current = head;
        while (current != nullptr && current->ticket.getTicketID() != Ticket_ID) {
            current = current->next;
        }

        if (current == nullptr) { 
        cout << "The Ticket with ID " << Ticket_ID << " is not present in the system\n";
        return Ticket();
        }
        return current->ticket;
    }

    void NodeSwap(Node* node1, Node* node2) {
        if (node1 == node2) return;

        Node* prev1 = Before_Node(node1);
        Node* prev2 = Before_Node(node2);

        if (prev1) prev1->next = node2;
        else head = node2;

        if (prev2) prev2->next = node1;
        else head = node1;

        Node* temp = node1->next;
        node1->next = node2->next;
        node2->next = temp;
    }

    void NodeSwapData(Node* node1, Node* node2) {
        swap(node1->ticket, node2->ticket);
    }

    void Bubble_sort_Priority() {

        if (head == nullptr) return;

        bool swapped = true;
        while (swapped) {
            swapped = false;
            Node* cur1 = head;
            while (cur1 && cur1->next) {
                Node* cur2 = cur1->next;
                if (cur1->ticket.getPriority() > cur2->ticket.getPriority()) {
                    NodeSwap(cur1,cur2);
                    swapped = true;
                }
                cur1 = cur1->next;
            }
        }
    }

    void Selection_sort_Creation_Time() {
        if (head == nullptr) {
            cout << "System is empty";
            return;
        }
        Node* cur1 = head;
        while (cur1) {
            Node* cur2 = cur1->next;
            Node* minnode = cur1;
            while(cur2) {
                if(cur2->ticket.getCreationTime() < minnode->ticket.getCreationTime()) {
                    minnode = cur2;
                }
                cur2 = cur2->next;
            }
            if (!(minnode == cur1)) NodeSwapData(cur1,minnode);
            cur1 = cur1->next;
        }
    }

    Node* tailnode() {
        Node* current = head;
        while (current != nullptr && current->next != nullptr) {
            current = current->next;
        }
        return current;
    }

    Node* Before_Node(Node* node) {
        if (node == head) return nullptr;
        Node* current = head;
        while(current && !(current->next == node) && current->next) {
            current = current->next;
        }
        return current;
    }

    Node* partition(Node* low, Node* high) {
        Node* pivot = low;
        Node* left = high;
        Node* right = high;

        while (right != low->next) {
            if (right->ticket.getCustomerName().size() < pivot->ticket.getCustomerName().size()) {
                NodeSwapData(right, left);
                left = left->next;
            }
            right = right->next;
        }

        NodeSwapData(pivot, left);
        return left;
    }

    void Quick_sort_Customer_Name(Node* low, Node* high) {
        if (head == nullptr || high == low) {
            (head == low) ? cout << "System has only one ticket" : cout << "System is empty";
            return;
        }

        Node* pivot = partition(low,high);

        if (high != low) {
            Node* current = head;
            while (current->next != pivot) {
                current = current->next;
            }
            Quick_sort_Customer_Name(current,high);
        }
        Quick_sort_Customer_Name(low,pivot->next);
    }

    void sort(string const choice) {
        if (choice == "Priority") Bubble_sort_Priority();
        else if (choice == "Creation Time") Selection_sort_Creation_Time();
        else if (choice == "Customer Name") Quick_sort_Customer_Name(head,tailnode());
        else {
            cout << "Choice does not correspond to available options\n";
            return;
        }
    }

    Node* Find_Open_Tickets() {
        Node* current = head;
        Node* Open_Tickets = nullptr;
        Node* Last_Found = nullptr;
        while (current != nullptr) {
            if (current->ticket.getStatus()) {
                Node* newNode = new Node(current->ticket);
                if (!Open_Tickets) Open_Tickets = newNode;
                else Last_Found->next = newNode;
                Last_Found = newNode;
            }
            current = current->next;
        }
        return Open_Tickets;
    }

    void Display_Tickets() {
        Node* current = head;
        while (current != nullptr) {
            current->ticket.display();
            current = current->next;
        }
    }

    int size() {
        int length = 0;
        Node* current = head;
        while (current != nullptr) {
            current = current->next;
            length++;
        }
        return length;
    }
};

class Agent {
    int Agent_ID;
    string Agent_Name;
    LinkedList Ticket_List;
    bool Availability; // True is Available and False is Unavailable

    public:

    Agent() : Agent_ID(-1), Agent_Name(""), Availability(NULL) {}
    Agent(int id, string name) : Agent_ID(id), Agent_Name(name), Availability(true) {}

    void Assign_Tickets(LinkedList tickets) {
        if (!Availability) { cout << "Agent is at max capacity\n"; return; }
        tickets.sort("Priority");
        Node* current = tickets.getHead();
        while (Ticket_List.size() < 5 && current) {
            Ticket_List.Add_Ticket(current->ticket);
            current = current->next;
        }
        if (Ticket_List.size() == 5) Availability = false;
        return;
    }

    string const Status() {
        return (Availability ? "Available" : "Unavailable");
    }

    int getAgentID() { return Agent_ID; }
    string getAgentName() { return Agent_Name; }
    LinkedList getAgentTicketList() { return Ticket_List; }

    void display_details() {
        cout << "Agent ID: " << getAgentID() << endl
             << "Agent Name: " << getAgentName() << endl
             << "Status: " << Status() << endl
             << "Details of Tickets assigned to Agent:\n";
        if (getAgentTicketList().size() == 0) cout << "Agent has no Tickets to process at the moment\n";
        else getAgentTicketList().Display_Tickets();
    }
};

class Agent_Management {

    Agent *Agents;
    int size;
    int capacity;

    public:

    Agent_Management() : size(0), capacity(2) {
        Agents = new Agent[2];
    }

    private:

    void resize() {

        capacity = capacity*2;

        Agent *newagents = new Agent[capacity];

        for (int i = 0; i < size; i++) {
            newagents[i] = Agents[i];
        }
        delete[] Agents;
        Agents = newagents;
    }

    public:

    void Add_Agent(Agent agent) {

        Agents[size++] = agent;
        if (size >= capacity-1) resize();
    }

    void Assign_Tickets(LinkedList tickets) {

        if (size == 0) { cout << "No Agents in the System"; return; }
        int Number_of_tickets = tickets.size();
        Agent* Agent_with_Minimum_Tickets = nullptr;

        for (int i = 0; i < size; i++) {
            
            if (5 - Agents[i].getAgentTicketList().size() >= Number_of_tickets) {
                if (Agent_with_Minimum_Tickets == nullptr || 
                    Agents[i].getAgentTicketList().size() < Agent_with_Minimum_Tickets->getAgentTicketList().size()) {
                    Agent_with_Minimum_Tickets = &Agents[i];
                }
            }
        }
        if (Agent_with_Minimum_Tickets == nullptr) {
        cout << "No Agent is available who can process this number of tickets\n";
        return;
        }

        Agent_with_Minimum_Tickets->Assign_Tickets(tickets);
    }

    void display() {
        cout << "Overview of the Agents: \n";
        for (int i = 0; i < size; i++) {
            Agents[i].display_details();
        }
    }

    ~Agent_Management() { delete[] Agents; }
};

class Ticket_Resolution_Log {

    int top;
    Ticket *arr;
    int size;

    public:

    Ticket_Resolution_Log() : top(-1) , size(2) {
        arr = new Ticket[2];
    }

    void resize() {
        Ticket *newarr = new Ticket[size*2];
        size = size*2;
        for (int i = 0; i < top; i++) {
            arr[i] = newarr[i];
        }
        delete[] arr;
        arr = newarr;
    }

    Ticket peek() {
       return arr[top]; 
    }

    bool isEmpty() { return top == -1; }

    void pop() {
        if (top < 0) {
            std::cout << "Stack Underflow. Cannot pop" << std::endl;
        }
        arr[top--] = Ticket();
    }

    void push(Ticket ticket) {
        if(top+1 == size) resize();
        arr[++top] = ticket;
    }

    void display() {
        for (int i = top; i >= 0; i--) {
            arr[i].display();
        }
    }

    Ticket_Resolution_Log operator=(Ticket_Resolution_Log const &other) {
        if (&other == this) return *this;
        this->arr = other.arr;
        this->top = other.top;
        this->size = other.size;
        return *this;
    }
};

class Pending_Ticket_Queue {

    int head;
    int tail;
    Ticket* arr;
    int size;

    public:

    Pending_Ticket_Queue() : head(0), tail(0), size(1) {
        arr = new Ticket[1];
    }

    void resize() {
        Ticket* newarr = new Ticket[size*2];
        size = size*2;
        for (int i = 0; i < head; i++) {
            newarr[i] = arr[i];
        }
        delete[] arr;
        arr = newarr;
    }

    void enqueue(Ticket ticket) {
        if (tail == size) resize();
        arr[tail++] = ticket;
        sort();
    }

    void dequeue() {
        if (head == tail) {
            cout << "Queue is already empty\n";
            return;
        }
        
        head++;
    }

    void sort() {
        if (head >= tail) return;

        for (int i = head; i < tail - 1; i++) {
            for (int j = i + 1; j < tail; j++) {
                if (arr[i].getPriority() > arr[j].getPriority() ||
                    (arr[i].getPriority() == arr[j].getPriority() && 
                    arr[i].getCreationTime() > arr[j].getCreationTime())) {
                    swap(arr[i], arr[j]);
                }
            }
        }
    }
};

class Ticket_Resolution_Logs {

    Ticket_Resolution_Log stack;
    Pending_Ticket_Queue queue;

    public:

    Ticket_Resolution_Logs() {}

    void Log_Closed_Ticket(Ticket ticket) {
        stack.push(ticket);
    }

    void Add_Ticket_To_Pending_Queue(Ticket ticket) {
        queue.enqueue(ticket);
    }

    void View_Logs() {
        stack.display();
    }
};

int main() {

    LinkedList Ticket_Management;

    try {
        Ticket_Management.Add_Ticket(Ticket(1, "Alice", 2, "Issue with Wi-Fi"));
        Ticket_Management.Add_Ticket(Ticket(2, "Bob", 1, "Need password reset"));
        Ticket_Management.Add_Ticket(Ticket(3, "Charlie", 3, "Computer won't start"));
        Ticket_Management.Add_Ticket(Ticket(4, "David", 2, "Printer is jammed"));
        Ticket_Management.Add_Ticket(Ticket(5, "Eve", 1, "Cannot connect to VPN"));
        Ticket_Management.Add_Ticket(Ticket(6, "Frank", 3, "Software installation issue"));
        Ticket_Management.Add_Ticket(Ticket(7, "Grace", 2, "Need hardware upgrade"));
        Ticket_Management.Add_Ticket(Ticket(8, "Hannah", 1, "Email not syncing"));
        Ticket_Management.Add_Ticket(Ticket(9, "Isaac", 3, "Network connectivity issue"));
        Ticket_Management.Add_Ticket(Ticket(10, "Jack", 2, "Backup failure"));
        Ticket_Management.Add_Ticket(Ticket(11, "Kathy", 1, "File recovery request"));
        Ticket_Management.Add_Ticket(Ticket(12, "Leo", 3, "System performance issue"));
        Ticket_Management.Add_Ticket(Ticket(13, "Mona", 2, "Application crash"));
        Ticket_Management.Add_Ticket(Ticket(14, "Nina", 1, "Account lockout"));
        Ticket_Management.Add_Ticket(Ticket(15, "Oscar", 3, "Update required"));
    } 
    catch (const invalid_argument& e) {
        cout << e.what(); // Handle any invalid priority inputs
    }

    // Ticket_Management.Search_Ticket(3).Close_Ticket();
    // Ticket_Management.Search_Ticket(2).Close_Ticket();
    // Ticket_Management.Search_Ticket(1).Close_Ticket();
    // Ticket_Management.Search_Ticket(13).Close_Ticket();
    // Ticket_Management.Search_Ticket(9).Close_Ticket();
    // Ticket_Management.Search_Ticket(8).Close_Ticket();
    // Ticket_Management.Search_Ticket(7).Close_Ticket();
    // Ticket_Management.Search_Ticket(11).Close_Ticket();
    // Ticket_Management.Search_Ticket(10).Close_Ticket();

    // Node* Open_Tickets = Ticket_Management.Find_Open_Tickets();

    // while (Open_Tickets != nullptr) {
    //     Open_Tickets->ticket.display();
    //     Open_Tickets = Open_Tickets->next;
    // }
    cout << "Unsorted\n";
    Ticket_Management.Display_Tickets();
    // cout << "\nPriority Sorted\n";
    // Ticket_Management.sort("Priority");
    // Ticket_Management.Display_Tickets();
    // cout << "\nCreation Time Sorted\n";
    // Ticket_Management.sort("Creation Time");
    // Ticket_Management.Display_Tickets();
    cout << "\nCustomer Name Sorted\n";
    Ticket_Management.sort("Customer Name");
    Ticket_Management.Display_Tickets();

    // Agent_Management Management_System;

    // Management_System.Add_Agent(Agent(1, "Abser"));
    // Management_System.Add_Agent(Agent(2, "Umar"));
    // Management_System.Add_Agent(Agent(3, "Owais"));
    // Management_System.Add_Agent(Agent(4, "Ali"));
    // Management_System.Add_Agent(Agent(5, "Fasih"));

    // LinkedList tickets1;
    // tickets1.Add_Ticket(Ticket(101, "Alice", 1, "Issue with Wi-Fi")); // 1 ticket

    // LinkedList tickets2;
    // tickets2.Add_Ticket(Ticket(201, "Bob", 2, "Need password reset"));
    // tickets2.Add_Ticket(Ticket(202, "Charlie", 1, "Computer won't start"));
    // tickets2.Add_Ticket(Ticket(203, "David", 3, "Printer is jammed"));
    // tickets2.Add_Ticket(Ticket(204, "Eve", 2, "Cannot connect to VPN")); // 4 tickets

    // LinkedList tickets3;
    // tickets3.Add_Ticket(Ticket(301, "Frank", 2, "Software installation issue"));
    // tickets3.Add_Ticket(Ticket(302, "Grace", 1, "Need hardware upgrade"));
    // tickets3.Add_Ticket(Ticket(303, "Hannah", 3, "Network connectivity issue")); // 3 tickets

    // Management_System.Assign_Tickets(tickets1);
    // Management_System.Assign_Tickets(tickets2);
    // Management_System.Assign_Tickets(tickets3);

    // Management_System.display();

    // Ticket_Resolution_Logs TRL;

    // TRL.Log_Closed_Ticket(Ticket(301, "Frank", 2, "Software installation issue"));
    // TRL.Log_Closed_Ticket(Ticket(302, "Grace", 1, "Need hardware upgrade"));
    // TRL.Log_Closed_Ticket(Ticket(303, "Hannah", 3, "Network connectivity issue"));

    // TRL.View_Logs();

    return 0;
}
