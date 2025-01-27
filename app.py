import streamlit as st

# State management
if "step" not in st.session_state:
    st.session_state.step = 1
if "salary" not in st.session_state:
    st.session_state.salary = None
if "state" not in st.session_state:
    st.session_state.state = None



# Streamlit flow
st.title("Tax Impact Estimator")
if st.session_state.step == 1:
    st.session_state.salary = st.number_input("What is your current salary?", min_value=0)
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 2:
    st.session_state.state = st.selectbox("What state do you live in?", ["Oklahoma", "Texas"])
    if st.button("Calculate"):
        federal_tax, state_tax, total_tax = calculate_tax(st.session_state.salary, st.session_state.state)
        st.write(f"Federal Tax: ${federal_tax:,.2f}")
        st.write(f"State Tax: ${state_tax:,.2f}")
        st.write(f"Total Tax: ${total_tax:,.2f}")
