from pandas import *
from PIL import Image
import numpy as np
import streamlit as st;
import numpy as np
from datetime import datetime

col1,col2,col3 =st.columns([2,2,1]) #FOR DIVISION
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Stack class using Python list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack (top to bottom):")
        for item in reversed(self.items):
            print(item)

# Queue class using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        print("Queue (front to back):")
        while current:
            print(current.data)
            current = current.next


st.title("CWB-ASSIGNMENT-2")
st.markdown(
    "<h1 style='text-align:center;color:grey'>Data Analytics Dashboard With Data Structures Implementation</h1>",
    unsafe_allow_html=True
)
img=Image.open(r"C:\Users\Anushree Jain\Desktop\th.jpeg")
with col3:
    st.image(img,width=150)

num = st.slider("No. of entries", 1, 100) 

#GPT WANTED TOO INCREASE THE WIDTH OF THE TABLE
st.markdown("""    
    <style>
    .element-container:has(.stDataFrame) {
        width: 100% !important;
    }
    .stDataFrame > div {
        max-width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

#HAD NO IDEA HOW TO GENERATE RANDOM DATES
def generate_random_datetimes(n):
    start_timestamp = int(datetime(2000, 1, 1).timestamp()) 
    end_timestamp = int(datetime(2025, 1, 1).timestamp())

    # Use int64-safe random generator
    rng = np.random.default_rng()
    random_timestamps = rng.integers(low=start_timestamp, high=end_timestamp, size=n, dtype='int64')
    return to_datetime(random_timestamps, unit='s')

# Generate DataFrame
df = DataFrame({
    'Numerical': np.arange(num),
    'Category': np.random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), size=num),
    'Date': generate_random_datetimes(num)
})

# Show DataFrame
st.dataframe(df, use_container_width=True)

# Initialize data structures
ll = LinkedList()
stack = Stack()
queue = Queue()


for _, row in df.iterrows():
  
    value = (row['Numerical'], row['Category'], row['Date'])

    ll.append(value)
    stack.push(value)
    queue.enqueue(value)

# HAVE VERYY LESS IDEA  OF PYTHON AND STREAMLIT 
st.subheader("Linked List Display")
ll_items = []
current = ll.head
while current:
    ll_items.append(str(current.data))

    current = current.next
st.write(" -> ".join(ll_items) + " -> None")

with st.expander("🔗 View Linked List"):
    st.dataframe(DataFrame(ll_items,columns=["ITEMS"]), use_container_width=True)

# Stack Display as text
st.subheader(" Stack Display (Top to Bottom)")
st.write("\n".join([str(item) for item in reversed(stack.items)]))

# Stack Display as Table
with st.expander('🔗 View Stack'):
    if stack.items:
        # Unpack the tuple data into separate lists
        numerical = [item[0] for item in reversed(stack.items)]
        category = [item[1] for item in reversed(stack.items)]
        date = [item[2] for item in reversed(stack.items)]

        stack_df = DataFrame({
            'Numerical': numerical,
            'Category': category,
            'Date': date
        })

        st.dataframe(stack_df, use_container_width=True)
   

st.subheader("Queue Display (Front to Rear)")
q_items = []
current = queue.front
while current:
    q_items.append(str(current.data))
    current = current.next
st.write(" -> ".join(q_items) + " -> None")
with st.expander("🔗 View Queue"):
    st.dataframe(DataFrame(q_items,columns=["ITEMS"]), use_container_width=True)


