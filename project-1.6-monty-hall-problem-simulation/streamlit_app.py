import streamlit as st
import time
from src.simulation import run_simulation
from src.game import simulate_game_manual


# Set title
st.title("🚪 Monty Hall Problem Simulator")

# Select mode
mode = st.radio("Select a mode:", ["Simulation (Auto)", "Manual (Play Yourself)"])

# -------------------
# 🎯 Auto Simulation Mode
# -------------------
if mode == "Simulation (Auto)":
    # Reset manual state
    st.session_state.clear()

    num_trials = st.number_input(
        "How many times do you want to run the simulation?",
        min_value=100, max_value=100000, value=1000, step=100
    )

    if st.button("Run Simulation"):
        with st.spinner("Running simulation..."):
            time.sleep(1.5)
        switch_rate, stay_rate = run_simulation(num_trials=num_trials)

        st.success(f"Win rate when switching: **{switch_rate * 100:.2f}%**")
        st.info(f"Win rate when staying: **{stay_rate * 100:.2f}%**")

        st.subheader("Comparison Chart")
        st.bar_chart({
            "Win Rate": {
                "Switch": switch_rate,
                "Stay": stay_rate
            }
        })

# -------------------
# 🎮 Manual Mode
# -------------------
elif mode == "Manual (Play Yourself)":
    st.subheader("🎮 Play the Monty Hall Game Yourself")

    # Door selection
    player_choice = st.radio("Choose a door (0, 1, or 2):", [0, 1, 2], key="manual_choice")

    # Step 1: Reveal
    if st.button("Reveal Goat 🐐"):
        st.session_state.result = simulate_game_manual(player_choice, switch=False)
        st.session_state.revealed = True
        st.session_state.player_choice = player_choice

    # Step 2: Ask to switch (after reveal)
    if st.session_state.get("revealed"):
        host = st.session_state.result["host_reveal"]
        st.info(f"Host reveals a goat behind door {host}")
        switch_decision = st.radio("Do you want to switch your choice?", ["Yes", "No"])

        # Step 3: Show result
        if st.button("Show Result 🎉"):
            switch_bool = switch_decision == "Yes"
            final_result = simulate_game_manual(
                st.session_state.player_choice, switch=switch_bool
            )
            if final_result["won"]:
                st.success("🎉 You won the 🚗 car!")
            else:
                st.error("🐐 You got a goat! Better luck next time.")

            # Reset after result shown
            st.session_state.revealed = False
