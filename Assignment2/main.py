from pandas import *
from LinkedList import LinkedList
from stack import  Stack
from queue1 import Queue
from func import generate_random_datetimes
from PIL import Image
import numpy as np
import streamlit as st;
import numpy as np
from datetime import datetime

col1,col2,col3 =st.columns([2,2,1]) #FOR DIVISION





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
q_items = [str(item) for item in queue.items]


st.write(" -> ".join(q_items) + " -> None")
with st.expander("🔗 View Queue"):
    st.dataframe(DataFrame(q_items,columns=["ITEMS"]), use_container_width=True)


