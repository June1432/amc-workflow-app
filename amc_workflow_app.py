# amc_workflow_app.py – Final Integrated Version
import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- App Setup ---
st.set_page_config(
    page_title="NAVIS | AMC Workflow Automation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Light Theme Styling ---
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

# --- Sidebar Role Selector ---
st.sidebar.title("Login")
role = st.sidebar.selectbox("Select Your Role", [
    "Investor", "Relationship Manager", "Fund Manager", "Operations",
    "Compliance Officer", "Customer Support", "Fund Accounting",
    "Admin", "Auditor"
])

# --- Loading Spinner ---
with st.spinner("Loading dashboard..."):

    if role == "Investor":
        tab1, tab2, tab3 = st.tabs(["Portfolio", "Goal Tracker", "Insights"])

        with tab1:
            st.subheader("Your Portfolio")
            portfolio_data = pd.DataFrame({
                "Scheme": ["Equity Fund", "Debt Fund", "Hybrid Fund"],
                "Current Value (₹ Lakhs)": [2.4, 1.5, 0.9],
                "Returns (%)": [12.3, 5.2, 7.8]
            })
            st.dataframe(portfolio_data, use_container_width=True)

        with tab2:
            st.subheader("Goal Tracker")
            fig = px.pie(portfolio_data, names="Scheme", values="Current Value (₹ Lakhs)", title="Asset Allocation")
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            st.subheader("AI Insights")
            insights = [
                "Consider increasing SIP in Equity Fund for long-term growth.",
                "Your Hybrid Fund is underperforming; rebalancing recommended.",
                "You are on track to meet your 5-year retirement goal."
            ]
            st.info(random.choice(insights))

    elif role == "Relationship Manager":
        st.title("Relationship Manager Dashboard")
        st.metric("New Leads", 24)
        st.metric("KYC Pending", 5)
        st.metric("Active SIPs", 40)
        with st.expander("KYC Status Tracker"):
            st.write(pd.DataFrame({
                "Investor": ["Raj", "Anita", "John"],
                "Status": ["Pending", "Approved", "In Review"]
            }))

    elif role == "Fund Manager":
        st.title("Fund Manager Dashboard")
        tab1, tab2 = st.tabs(["Scheme Performance", "Benchmarking"])

        with tab1:
            fund_data = pd.DataFrame({
                "Scheme": ["Growth Fund", "Income Fund"],
                "AUM (₹ Cr)": [520, 340],
                "YTD Return (%)": [8.2, 6.5]
            })
            st.dataframe(fund_data, use_container_width=True)

        with tab2:
            st.info("Your Growth Fund outperformed Nifty50 by 1.3% this quarter.")

    elif role == "Operations":
        st.title("Operations Dashboard")
        st.write("Processed Transactions Today: 1,542")
        st.write("Failed Transactions: 8")
        st.success("99.5% success rate")

    elif role == "Compliance Officer":
        st.title("Compliance Dashboard")
        st.warning("2 STR alerts flagged today")
        st.info("All FATCA/CRS reports submitted")
        st.metric("Last Audit Passed", "Yes")

    elif role == "Customer Support":
        st.title("Customer Support Dashboard")
        st.write("Open Tickets: 12")
        st.write("Resolved Today: 18")
        with st.expander("Ticket Preview"):
            st.write("#1003: SIP delay complaint - Resolved")

    elif role == "Fund Accounting":
        st.title("Fund Accounting Dashboard")
        st.write("Today's NAVs published for 18 schemes")
        st.write("Pending Dividend Payouts: 2")
        with st.expander("Download NAV Statements"):
            st.download_button("Download (mock file)", "NAV123.csv")

    elif role == "Admin":
        st.title("Admin Panel")
        st.write("Active Users: 84")
        st.write("Recent Logins: 23 Today")
        st.success("All access logs backed up")

    elif role == "Auditor":
        st.title("Auditor Dashboard")
        st.write("Downloadable logs for last 30 days")
        st.button("Generate Audit Report")
        st.info("Audit module access confirmed")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 NAVIS Mutual AMC | All rights reserved")
