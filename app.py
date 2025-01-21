import streamlit as st 

def hello_wold():
    return "Aula de Docker :)"

def main():
    st.write(hello_wold())

if __name__ == "__main__":
    main()