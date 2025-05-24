# include<iostream>
#include <stack>
# include<queue>
using namespace std;
class Node{
    public:
        int data;
        Node*next;
        Node(){
            next=NULL;
        }
};
void append(Node*&head,Node*&tail,int d){
    Node*temp;
    temp->data=d;
    if(head==NULL){
        head=temp;
        tail=temp;
        return;
    }
    tail->next=temp;
    temp=tail;
    return;
}


int main(){
    stack <int>st;
    st.push(2);
    st.push(3);
    st.push(4);
    st.top();
    cout<<"STACK: ";
    while(!st.empty()){
        cout<<st.top()<<" ";
        st.pop();
    }
    cout<<endl;
    queue<int>q;
    q.push(2);
    q.push(3);
    q.push(4);
    cout<<"QUEUE: ";
    cout<<q.front();
    while(!q.empty()){
        cout<<q.front()<<" ";
        q.pop();
    }

}


/*
LEARNED ABOUT EXPANDER,DID DATAFRAME LONG TIME BACK SO HAD A FLASKBACK
BASIC STREAMLIT KEYWORDS Especially markdown
*/
