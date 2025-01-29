import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
url = st.secrets.spreadsheets.winnings

df = conn.read(spreadsheet=url)
# df = df.groupby(["Date", "MemberId"])["Winnings"].sum().reset_index()
# df = df.groupby(["MemberId"])["Winnings"].sum()
df = df.groupby("MemberId").Winnings.sum().sort_values(ascending=False).reset_index()
# st.dataframe(df, height=1500)

container = st.container()
with container:
    st.dataframe(df)  # Specify height here

# df = conn.read(
#     spreadsheet=url,
#     ttl="10m"
# )

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.Date} : {row.MemberId} : {row.Winnings}")
