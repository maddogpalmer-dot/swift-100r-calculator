import math
import streamlit as st

st.set_page_config(page_title="Swift 100R Maintenance Cost Calculator", layout="centered")

st.title("Swift 100R Maintenance Cost Calculator")

# -----------------------------
# Master input
# -----------------------------
st.subheader("Annual Utilization")
annual_hours = st.number_input(
    "Total Hours Plane Flies in a Year?",
    min_value=0.0,
    value=200.0,
    step=10.0
)

st.divider()

def whole_events_per_year(hours_per_year, interval_hours):
    if hours_per_year <= 0:
        return 0
    return int(math.ceil(hours_per_year / interval_hours))

def money(x):
    return f"${x:,.2f}"

# =============================
# SECTION 1 — 100LL
# =============================
st.header("100LL Maintenance Cost Per Year")

oil_changes_100ll = whole_events_per_year(annual_hours, 50)
st.write(f"Number of 50 hour oil changes a year: **{oil_changes_100ll}**")

oil_price_100ll = st.number_input(
    "Price of a 50 hour oil change ($)",
    min_value=0.0,
    value=250.0,
    step=10.0
)
annual_oil_100ll = oil_changes_100ll * oil_price_100ll
st.write(f"50 hour oil change cost per year: **{money(annual_oil_100ll)}**")

st.markdown("---")

plug_interval_100ll = st.number_input(
    "At what hour are sparkplugs changed?",
    min_value=0.0,
    value=1000.0,
    step=50.0
)

plug_events_100ll = whole_events_per_year(annual_hours, plug_interval_100ll)
st.write(f"Number of sparkplug change events per year: **{plug_events_100ll}**")

plug_price_100ll = st.number_input("Price of spark plug ($)", 0.0, 1000.0, 1.0)
num_plugs_100ll = st.number_input("Number of spark plugs", 1, 8, 1)

annual_plugs_100ll = plug_events_100ll * plug_price_100ll * num_plugs_100ll
st.write(f"Sparkplug cost per year: **{money(annual_plugs_100ll)}**")

section1_total = annual_oil_100ll + annual_plugs_100ll
st.subheader("100LL Total")
st.metric("100LL Maintenance Cost Per Year", money(section1_total))

st.divider()

# =============================
# SECTION 2 — 100R
# =============================
st.header("100R Maintenance Cost Per Year")

oil_changes_100r = whole_events_per_year(annual_hours, 100)
st.write(f"Number of 100 hour oil changes a year: **{oil_changes_100r}**")

oil_price_100r = st.number_input(
    "Price of a 100 hour oil change ($)",
    min_value=0.0,
    value=250.0,
    step=10.0
)
annual_oil_100r = oil_changes_100r * oil_price_100r
st.write(f"100 hour oil change cost per year: **{money(annual_oil_100r)}**")

st.markdown("---")

plug_interval_100r = st.number_input(
    "At what hour are sparkplugs changed? ",
    min_value=1.0,
    value=1500.0,
    step=100.0
)

plug_events_100r = whole_events_per_year(annual_hours, plug_interval_100r)
st.write(f"Number of sparkplug change events per year: **{plug_events_100r}**")

plug_price_100r = st.number_input(
    "Price of spark plug ($)",
    min_value=0.0,
    value=35.0,
    step=1.0
)

num_plugs_100r = st.number_input(
    "Number of spark plugs",
    min_value=0,
    value=8,
    step=1
)

annual_plugs_100r = plug_events_100r * plug_price_100r * num_plugs_100r
st.write(f"Sparkplug cost per year: **{money(annual_plugs_100r)}**")
section2_total = annual_oil_100r + annual_plugs_100r
st.subheader("100R Total")
st.metric("100R Maintenance Cost Per Year", money(section2_total))


