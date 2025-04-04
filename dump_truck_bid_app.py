import streamlit as st

def calculate_bid(
    material_type: str,
    total_volume: float,
    haul_distance: float,
    num_loads: int,
    truck_type: str,
    fuel_price: float,
    dump_fee_per_load: float,
    driver_rate_per_hour: float,
    trip_time_per_load: float,
    mpg: float,
    overhead_per_load: float,
    markup_percent: float
) -> dict:
    # Fuel cost per mile
    fuel_cost_per_mile = fuel_price / mpg

    # Cost per load calculation
    fuel_cost = haul_distance * 2 * fuel_cost_per_mile
    driver_cost = trip_time_per_load * driver_rate_per_hour
    per_load_cost = fuel_cost + driver_cost + dump_fee_per_load + overhead_per_load

    # Total cost and final bid
    total_cost = per_load_cost * num_loads
    markup = total_cost * (markup_percent / 100)
    total_bid = total_cost + markup

    return {
        "Material Type": material_type,
        "Truck Type": truck_type,
        "Loads": num_loads,
        "Cost per Load": round(per_load_cost, 2),
        "Total Cost": round(total_cost, 2),
        "Final Bid": round(total_bid, 2)
    }

st.title("Dump Truck Bid Assistant")

st.sidebar.header("Enter Job Details")

material_type = st.sidebar.text_input("Material Type", "Gravel")
total_volume = st.sidebar.number_input("Total Volume (yards)", value=200.0)
haul_distance = st.sidebar.number_input("Haul Distance (miles)", value=18.0)
num_loads = st.sidebar.number_input("Number of Loads", value=15)
truck_type = st.sidebar.text_input("Truck Type", "Tri-axle")
fuel_price = st.sidebar.number_input("Fuel Price per Gallon", value=4.25)
dump_fee_per_load = st.sidebar.number_input("Dump Fee per Load", value=75.0)
driver_rate_per_hour = st.sidebar.number_input("Driver Rate per Hour", value=35.0)
trip_time_per_load = st.sidebar.number_input("Trip Time per Load (hours)", value=1.5)
mpg = st.sidebar.number_input("Miles per Gallon (MPG)", value=5.0)
overhead_per_load = st.sidebar.number_input("Overhead per Load", value=50.0)
markup_percent = st.sidebar.number_input("Markup Percentage", value=20.0)

if st.sidebar.button("Calculate Bid"):
    result = calculate_bid(
        material_type,
        total_volume,
        haul_distance,
        num_loads,
        truck_type,
        fuel_price,
        dump_fee_per_load,
        driver_rate_per_hour,
        trip_time_per_load,
        mpg,
        overhead_per_load,
        markup_percent
    )

    st.subheader("Bid Summary")
    for key, value in result.items():
        st.write(f"**{key}:** {value}")
