import streamlit as st
from src.simulation import run_simulation

# Set the title of the app
st.title("🚪 Monty Hall Problem Simulator")

# Let the usr choose between automatic simulation and manual play
mode = st.radio("Select a mode:", ["Simulation (Auto)", "Manual (Play Yourself)"])

if mode == "Simulation (Auto)":
    # Ask user how many times to run the simulation
    num_trials = st.number_input(
        "How many times do you want to run the simulation?",
        min_value=100, max_value=100000, value=1000, step=100
    )

# Run the simulation when the button is clicked
if st.button("Run Simulation"):
    switch_rate, stay_rate = run_simulation(num_trials=num_trials)

    # Show the win rate for each strategy
    st.success(f"Win rate when switching: **{switch_rate * 100:.2f}%**")
    st.info(f"Win rate when staying: **{stay_rate * 100:.2f}%**")

    # Display a bar chart comparing the two win rates
    st.subheader("Comparison Chart")
    st.bar_chart({
        "Win Rate": {
            "Switch": switch_rate,
            "Stay": stay_rate
        }
    })

else:
    # Placeholder for manual play mode (not implemented yet)
    st.warning("Manual mode not implemented yet. Stay tuned! 🚧")