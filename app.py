import streamlit as st

def hello_world():
    return "Atualizei o return da minha função do hello_world() para testar o auto deploy CI/CD do render"

def main():
    st.write(hello_world())

if __name__ == '__main__':
    main()