# amc_workflow_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# --- App Setup ---
st.set_page_config(
    page_title="NAVIS | AMC Workflow Automation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Role Selection ---
roles = [
    "Investor", "Relationship Manager", "Fund Manager", "Operations",
    "Compliance Officer", "Customer Support", "Fund Accounting",
    "Admin", "Auditor"
]

st.sidebar.title("Login")
role = st.sidebar.selectbox("Select Your Role", roles)

# --- Common Light UI Theme ---
st.markdown("""
    <style>
        body {
            background-color: #f7f9fb;
        }
        .main {
            background-color: #ffffff;
            color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# --- Mock Dashboards ---
def investor_dashboard():
    st.title("Investor Dashboard")
    st.subheader("Your Portfolio")
    portfolio_data = pd.DataFrame({
        "Scheme": ["Equity Fund", "Debt Fund", "Hybrid Fund"],
        "Current Value (₹ Lakhs)": [2.4, 1.5, 0.9],
        "Returns (%)": [12.3, 5.2, 7.8]
    })
    st.dataframe(portfolio_data, use_container_width=True)

    st.subheader("Goal Tracker")
    fig = px.pie(portfolio_data, names="Scheme", values="Current Value (₹ Lakhs)", title="Asset Allocation")
    st.plotly_chart(fig, use_container_width=True)


def rm_dashboard():
    st.title("Relationship Manager Dashboard")
    st.subheader("Investor Pipeline")
    st.metric("New Leads", 24)
    st.metric("KYC Pending", 5)
    st.metric("Active SIPs", 40)


def fund_manager_dashboard():
    st.title("Fund Manager Dashboard")
    st.subheader("Scheme Performance Snapshot")
    fund_data = pd.DataFrame({
        "Scheme": ["Growth Fund", "Income Fund"],
        "AUM (₹ Cr)": [520, 340],
        "YTD Return (%)": [8.2, 6.5]
    })
    st.dataframe(fund_data, use_container_width=True)


def operations_dashboard():
    st.title("Operations Dashboard")
    st.subheader("Transaction Monitoring")
    st.write("Processed Transactions Today: 1,542")
    st.write("Failed Transactions: 8")


def compliance_dashboard():
    st.title("Compliance Dashboard")
    st.subheader("Alerts")
    st.warning("2 STR alerts flagged today")
    st.info("All FATCA/CRS reports submitted")


def support_dashboard():
    st.title("Customer Support Dashboard")
    st.subheader("Service Requests")
    st.write("Open Tickets: 12")
    st.write("Resolved Today: 18")


def accounting_dashboard():
    st.title("Fund Accounting Dashboard")
    st.subheader("NAV & Distributions")
    st.write("Today's NAVs published for 18 schemes")
    st.write("Pending Dividend Payouts: 2")


def admin_dashboard():
    st.title("Admin Panel")
    st.subheader("User Access Management")
    st.write("Active Users: 84")
    st.write("Recent Logins: 23 Today")


def auditor_dashboard():
    st.title("Auditor Dashboard")
    st.subheader("Audit Trails")
    st.write("Downloadable logs for last 30 days")
    st.button("Generate Audit Report")

# --- Role-Based Routing ---
if role == "Investor":
    investor_dashboard()
elif role == "Relationship Manager":
    rm_dashboard()
elif role == "Fund Manager":
    fund_manager_dashboard()
elif role == "Operations":
    operations_dashboard()
elif role == "Compliance Officer":
    compliance_dashboard()
elif role == "Customer Support":
    support_dashboard()
elif role == "Fund Accounting":
    accounting_dashboard()
elif role == "Admin":
    admin_dashboard()
elif role == "Auditor":
    auditor_dashboard()

# Footer
st.markdown("---")
st.markdown("© 2025 NAVIS Mutual AMC | All rights reserved")
