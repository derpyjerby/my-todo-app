import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    # gets st.session_state values, which keeps the data that your user enters in your app.
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",
         # This reads the text above as html.
         # If this is set to False, it will write what is in the parenthesis.
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    # key is going to hold the value of the checkbox if it is checked or not.
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # removes the to do from the session_state variable
        del st.session_state[todo]
        # this reruns the code to refresh the page once the checkbox is checked.
        st.experimental_rerun()

# We added on_change as a listener to let the input interact with the program
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# Uploaded a deployed version of this code
# Link: https://my-todo-app-fkmldy6ymxcuvmq24gyxfa.streamlit.app/
# Github Repo: https://github.com/derpyjerby/my-todo-app.git
