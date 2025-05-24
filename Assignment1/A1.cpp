#include<iostream>
#include<stack>
#include<queue>
using namespace std;
class Node{
    public:
    string data;
    Node*next;
    Node(int d){
        this->data=d;
        this->next=NULL;
    }
    Node(){
        this->next=NULL;
    }
};
void add_ALL(Node*&head_ALL,Node*&tail_ALL,string task){
    Node*temp=head_ALL;
    while(temp!=NULL){
        if(temp->data==task){
            return;
        }
        temp=temp->next;
    }
    if(head_ALL==NULL){
        Node*newtask=new Node();
        newtask->data=task;
        head_ALL=newtask;
        tail_ALL=head_ALL;
        }
    else{
        Node*newtask=new Node();
        newtask->data=task;
        tail_ALL->next=newtask;
        tail_ALL=newtask;
    }
}
void add(int n,Node*&head_ALL,Node*&tail_ALL,queue<string>&High,stack<string>&recent,queue<string>&process,string task){
    if(n==2){
        queue<string>temp=High;
        while(!temp.empty()){
            if(temp.front()==task){
                cout<<"Already added!"<<endl;
                return;
            }
            temp.pop();
        }
        High.push(task);
        process.push(task);
        add_ALL(head_ALL,tail_ALL,task);
    }
    else if(n==3){
        stack<string>temp;
        while(!temp.empty()){
            if(temp.top()==task){
                cout<<"Already added!"<<endl;
                return;
            }
            temp.pop();
        }
        recent.push(task);
        add_ALL(head_ALL,tail_ALL,task);
    }
    else if(n==4){
        queue<string>temp=process;
        while(!temp.empty()){
            if(temp.front()==task){
                cout<<"Already added!"<<endl;
                return;
            }
            temp.pop();
        }
        process.push(task);
        add_ALL(head_ALL,tail_ALL,task);
    }
    
}
void tasks(int n,Node*&head_ALL,Node*&tail_ALL,queue<string>High,stack<string>recent,queue<string>process){
    if(n==1){
        Node*temp=head_ALL;
        if(temp==NULL){
            cout<<"Empty!"<<endl;
        }
        while(temp!=NULL){
            cout<<temp->data<<endl;
            temp=temp->next;
        }
        delete temp;
    }
    else if(n==2){
        if(High.empty()){
            cout<<"Empty!"<<endl; 
        }
        while(!High.empty()){
            cout<<High.front()<<endl;
            High.pop();
        }
    }
    else if(n==3){
        if(recent.empty()){
            cout<<"Empty!"<<endl; 
        }
        while(!recent.empty()){
            cout<<recent.top()<<endl;
            recent.pop();
        }
    }
    else if(n==4){
        if(process.empty()){
            cout<<"Empty!"<<endl; 
        }
        while(!process.empty()){
            cout<<process.front()<<endl;
            process.pop();
        }
    }
}
void Delete_ALL(Node*&head_ALL,Node*&tail_ALL,string task){
    if(head_ALL==NULL){
        return;
    }
    
    if(head_ALL->data==task){
        Node*del=head_ALL;
        head_ALL=head_ALL->next;
        if(head_ALL==NULL){
            tail_ALL=NULL;
        }
        delete del;
    }
    Node*temp=head_ALL;
    while(temp->next!=NULL){
        if(temp->next->data==task){
            if(temp->next->next==NULL){
                tail_ALL=temp;
            }
            Node*del=temp->next;
            temp->next=del->next;
            delete del;
            
        }
        else{
            temp=temp->next;
        }
        
    }
            


}

void delete_process(queue<string>&process,string task){
    queue<string>temp1;
    while(!process.empty()){
        if(process.front()!=task){
            temp1.push(process.front());
        }
        process.pop();
    }
    process=temp1;
}
void Delete(int n,Node*&head_ALL,Node*&tail_ALL,queue<string>&High,stack<string>&recent,queue<string>&process,string task){
    if(n==2){
        queue<string>temp;
        while(!High.empty()){
            if(High.front()!=task){
                temp.push(High.front());
            }
            High.pop();
        }
        High=temp;
        delete_process(process,task);
        Delete_ALL(head_ALL,tail_ALL,task);
    }
    else if(n==3){
        stack<string>temp;
        while(!recent.empty()){
            if(recent.top()!=task){
                temp.push(recent.top());
                
            }
            recent.pop();
        }
        recent=temp;
        Delete_ALL(head_ALL,tail_ALL,task);

    }
    else if(n==4){
        delete_process(process,task);
        Delete_ALL(head_ALL,tail_ALL,task);
    }
}
int main(){
    cout<<endl;
    cout<<endl;
    Node All();
    Node*head_All=NULL;
    Node*tail_ALL=NULL;
    stack<string>Recent_task;
    queue<string>process_queue;
    queue<string>High;
    cout<<"_________________________________________YOUR TASK MANAGER APPLICATION_______________________________________________"<<endl;
    cout<<"TASK OVERVIEW"<<endl;
    cout<<endl<<"View Tasks: "<<endl;
    cout<<"1) All Tasks"<<endl;
    cout<<"2) High Priority Tasks"<<endl;
    cout<<"3) Recent Tasks"<<endl;
    cout<<"4) Proces Task Queue"<<endl;
    int n;
    string ans;
    cout<<"DO YOU WANT TO START WITH THE TASK MANAGER APPLICATION WALKTHROUGH?(Y/N): ";
    cin>>ans;
    while(ans=="Y"){
        cout<<"TASK MANANGER has following features-SEE||ADD||DELETE!"<<endl;
        string what;
        cout<<"What do you want to do? ";
        cin>>what;
        if(what=="SEE"){
            cout<<"Choose 1/2/3/4 To see the respective tasks: ";
            cin>>n;
            tasks(n,head_All,tail_ALL,High,Recent_task,process_queue);
            
        }
        else if(what=="ADD"){
            cout<<endl<<"Choose 2/3/4 To add in the  respective tasks: ";
            cin>>n;
            string task;
            cout<<"Enter the task: ";
            cin>>task;
            add(n,head_All,tail_ALL,High,Recent_task,process_queue,task);
          
        }
        else if(what=="DELETE"){
            cout<<"Choose 2/3/4 To delete the respective tasks: ";
            cin>>n;
            cout<<"Enter the description of the task: ";
            string task;
            cin>>task;
            Delete(n,head_All,tail_ALL,High,Recent_task,process_queue,task);
            
        }
        cout<<"Do you wish to continue?(Y/N): ";
        cin>>ans;
    }
    cout<<"_________________________________________Thank youuu for your time...Hope to see you soon!_______________________________________________";
    

}
