import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')
st.set_page_config(page_title="Israeli Anesthesiologist Survey Analysis", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

STATEMENT_LABELS = {1: "Routine cricoid pressure in RSI", 2: "VL preferred for elective RSI", 3: "Check mask ventilation before NMB", 4: "RSI for GLP-1 agonist patients", 5: "LMA safe for GLP-1 agonist patients", 6: "LMA safe for simple laparoscopy", 7: "Routine intraoperative TOF monitoring", 8: "TOF-guided reversal", 9: "BIS-guided induction in patients >70 y", 10: "BIS-guided maintenance in patients >70 y", 11: "Avoid BP cuff on post–axillary dissection arm", 12: "Peripheral norepinephrine infusion", 13: "US for radial arterial line", 14: "US for central IJ line", 15: "Prefer opioid-sparing techniques", 16: "Epidural test dose with epinephrine", 17: "Epidural placement under GA", 18: "Peripheral block under GA", 19: "Routine post-PACU follow-up", 20: "Prefer green anesthesia techniques"}

@st.cache_data
def load_data():
    file_path = 'Data_02_26_nohospitalname.xlsx'
    df = pd.read_excel(file_path)
    return df

st.markdown("# 📊 Israeli Anesthesiologist Survey Analysis")
st.markdown("*Interactive exploration of clinical practice patterns*")