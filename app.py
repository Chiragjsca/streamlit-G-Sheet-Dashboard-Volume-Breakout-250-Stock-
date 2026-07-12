L2='#6a1b9a'
L1='#f3e5f5'
L0='#2e7d32'
K_='#3949ab'
Kz='#e8eaf6'
Ky='180 Days'
Kx='90 Days'
Kw='Newest First'
Kv='Today Only'
Ku='Past 7 Days'
Kt='540222'
Ks='532480'
Kr='532209'
Kq='513377'
Kp='500420'
Ko='540175'
Kn='502525'
Km='500260'
Kl='508869'
Kk='532488'
Kj='524715'
Ki='500209'
Kh='DALMIA'
Kg='APOLLOHOSP'
Kf='SUNPHARMA'
Ke='lower limit'
Kd='upper limit'
Kc='title_raw'
Kb="\n            function(params) {\n                let v = String(params.value).toLowerCase();\n                if (v.includes('strong uptrend') || v.includes('bullish') || v.includes('strong buy')) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (v.includes('uptrend') || v.includes('buy') || v.includes('high') || v.includes('yes')) return { 'backgroundColor': '#a5d6a733', 'color': '#000' };\n                if (v.includes('sideways') || v.includes('watch') || v.includes('normal')) return { 'backgroundColor': '#f4b40033', 'color': '#000' };\n                if (v.includes('bearish') || v.includes('avoid') || v.includes('low') || v.includes('downtrend')) return { 'backgroundColor': '#ea433533', 'color': '#000' };\n                return null;\n            }\n            "
Ka="\n            function(params) {\n                let val = parseFloat(params.value);\n                if (val >= 75) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 55) return { 'backgroundColor': '#f4b40033', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 35) return { 'backgroundColor': '#ff990033', 'color': '#000' };\n                return { 'backgroundColor': '#ea433533', 'color': '#000' };\n            }\n            "
KZ='Automatically adjust column widths based on text length of the selected row.'
KY=' (100%)'
KX='Other Assets (unspecified)'
KW='Cash & Equivalents'
KV='#00897b'
KU='Trade Receivables'
KT='Inventory'
KS='#5e35b1'
KR='Fixed Assets / Net PPE'
KQ='#5c6bc0'
KP='#8d6e63'
KO='Trade Payables'
KN='Total Debt'
KM='Reserves'
KL='Equity Capital'
KK='gauge+number'
KJ='institutional'
KI='institutional %'
KH='delivery %'
KG='% delivery'
KF='Last Close'
KE='rgba(0,0,0,0.08)'
KD='RSI(14)'
KC='system-ui, sans-serif'
KB='rgba(0,0,0,0.06)'
KA='#31333F'
K9='tonexty'
K8='circle'
K7='#EF6C00'
K6='top right'
K5='#7C3AED'
K4='#FFD600'
K3='Candle'
K2='%d %b %Y %H:%M'
K1='⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.'
K0='stock name'
J_='company name'
Jz='Type symbol name...'
Jy='Search symbol:'
Jx='Stocks'
Jw='%{customdata}: %{y:.2f}%<extra></extra>'
Jv='% Above 52W Low'
Ju='% Below 52W High'
Jt='displaylogo'
Js='#e3f2fd'
Jr='close price'
Jq='%Y%m%d_%H%M'
Jp='52w low date'
Jo='52w high date'
Jn='Market Cap'
Jm='RONW %'
Jl='Face Value'
Jk='Institutional %'
Jj='Promoters %'
Ji='50 DMA < 200 DMA'
Jh='50 DMA > 200 DMA'
Jg='50 DMA > 100 DMA > 200 DMA'
Jf='50 DMA < 100 DMA < 200 DMA'
Je='All (No Filter)'
Jd='macd crossover'
Jc='start gtt order'
Jb='output'
Ja='🎨 Custom Hex: '
JZ='#ff9900'
JY='#f4b400'
JX='bf_search'
JW='perf_matrix_search'
JV='main_matrix_search'
JU='search_query'
JT='50 dma'
JS='d/e ratio'
JR='52w low'
JQ='vol_val'
JP='official nse'
JO='market smith'
JN='chartlink'
JM='zerodha'
JL='screener'
JK='history data'
JJ='trading view'
JI='1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU'
JH='https://www.googleapis.com/auth/drive'
JG='https://spreadsheets.google.com/feeds'
JF="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
JE='Output'
JD='Price %'
JC='GROQ_API_KEY'
JB='GEMINI_API_KEY'
Gj='concalls'
Gi='credit_ratings'
Gh='annual_reports'
Gg='announcements'
Gf='1 Year'
Ge='30 Days'
Gd='total assets'
Gc='net ppe'
Gb='fixed assets'
Ga='trade payables'
GZ='trade receivables'
GY='cash equivalent'
GX='cash and equiv'
GW='cash & equiv'
GV='inventory'
GU='total debt'
GT='reserves'
GS='total equity capital'
GR='Sector'
GQ='rgba(0,0,0,0.3)'
GP='dash'
GO='#FF5252'
GN='#00E676'
GM='type'
GL='#D50000'
GK='#00C853'
GJ='🚨 **[ALERT]** '
GI='Recent'
GH='Grade'
GG='Strategy'
GF='% Gain'
GE='Target'
GD='last_pine_result'
GC='last_ai_result'
GB='100%'
GA='streamlit'
G9='Default'
G8='📏 Column Width Adjustment:'
G7='#fff8e1'
G6='#1b5e20'
G5='market cap'
G4='buy signal'
G3='trend'
G2='breakout signal'
G1='volume trend'
G0='industry'
F_='52w_low'
Fz='52w_high'
Fy='Watchlist'
Fx='pledged'
Fw='pledged %'
Fv='promoter'
Fu='promoters %'
Ft='200 dma'
Fs='#ef5350'
Fr='Error'
Fq='Loading...'
Fp='⚡ Groq (Fast)'
Fo=getattr
Fn=TypeError
EQ='ppt'
EP='#9e9e9e'
EO='#FFFFFF'
EN='system-ui, -apple-system, sans-serif'
EM='skip'
EL='lines'
EK='Low'
EJ='High'
EI='locked in circuit'
EH='hits circuit'
EG='lower circuit'
EF='upper circuit'
EE='52-week low'
ED='52-week high'
EC='%d %b %Y'
EB='Use Case'
EA='% Risk'
E9='Type'
E8='model'
E7='markers'
E6='52'
E5='sector'
E4='atr_approx'
E3='Added On'
E2='BF Grade'
E1='delivery'
E0='net sales'
D_='net profit'
Dz='Pct_Change'
Dy='value'
Dx='stock'
Dw='stock symbol'
Dv='ticker'
Du='<[^>]*>'
Dt='gcp_service_account'
Ds='No Data'
Dr=range
Dq=enumerate
DH='#c62828'
DG='dot'
DF='.//item'
DE='result'
DD='sym'
DC='left'
DB='N/A'
DA='#b71c1c'
D9='openpyxl'
D8='trail_sl_50dma'
D7='52 week high'
D6='added'
D5='BF Score'
D4='Note'
D3='Turnover'
D2='price %'
D1='id'
D0='nse code'
C_='#ffffff'
Cz='</div>'
Cy='#66bb6a'
Cb='#37474f'
Ca='Mozilla/5.0'
CZ='User-Agent'
CY='✅✅ Fit to Row 2'
CX='✅ Fit to Row 1'
CW='<br>'
CV='#e8f5e9'
CU='bf_score'
CT='52 week low'
CS='Value'
CR='turnover'
CQ='%Y-%m-%d %H:%M:%S'
CP='-%'
CO='+%'
CN='Diff @ 200 DMA'
CM='Final List 2'
CL='Final List'
Bv='rgba(0,0,0,0.2)'
Bu='Arial Black, Arial, sans-serif'
Bt='snap'
Bs='Buy Signal'
Br='MACD Crossover'
Bq='Trend'
Bp='Breakout Signal'
Bo='Volume Trend'
Bn='_'
Bm='📱 If frame is blank on mobile, tap the link above to open directly.'
Bl='#ffebee'
Bk='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
Bj='%Y%m%d'
Bi='bf_grade'
BM='UTC'
BL='RSI (14)'
BK='Price (₹)'
BJ='date'
BI='note'
BH='volume'
BG='[%,]'
BF='Close'
BE='NSE Fundamentals'
BD='Top 250 Stocks'
B1='Diff. from 200 DMA'
B0='gray'
A_='#f9a825'
Az='price'
Ay=isinstance
An='#0a1758'
Am='pubDate'
Al=1.
Ak='52W Low'
Aj='52W High'
Ai='% Delivery'
Ac='sec'
Ab='hour'
Aa='min'
AZ='#16e37f'
AY='#ea4335'
AX='symbol'
AW='_txt_'
AV='_bg_'
AU=any
AT=ValueError
AP='bold'
AO='normal'
AN='None'
AM='coerce'
AL='CMP'
AK=list
AH='timestamp'
AG='Just now'
AC='#1565C0'
AB='display_title'
AA='%'
A9=','
A8=max
A3='title'
A2='cmp'
A1='nan'
x='plotly_white'
w='#0f9d58'
v='change'
u='Volume'
n='Symbol'
m='_raw_symbol_'
j='-'
i=.0
g=Exception
f='link'
c='---'
b=round
U=next
T=int
P=len
M=float
L='time_ago'
J=False
F=str
E=dict
D=None
C=''
B=True
import streamlit as A,pandas as H,numpy as A4,gspread as ER
from google.oauth2.service_account import Credentials as Gk
from google.auth.transport.requests import AuthorizedSession as L3
import json as ES,urllib.parse
from datetime import datetime as k
from st_aggrid import AgGrid as ET,GridOptionsBuilder as EU,JsCode as B2
from st_aggrid.shared import GridUpdateMode as L4
import streamlit.components.v1 as O,re,io,google.generativeai as Gl,plotly.graph_objects as Q
from plotly.subplots import make_subplots as L5
A.set_page_config(page_title='Top 250 NSE Stock-Volume Breakout Dashboard',layout='wide',page_icon='📊')
if hasattr(A,'fragment'):DI=A.fragment
elif hasattr(A,'experimental_fragment'):DI=A.experimental_fragment
else:
	def DI(func=D,**B):
		if func is not D:return func
		def A(f):return f
		return A
A.markdown('\n<style>\n    /* Force EVERY tab-bar container to wrap onto multiple lines instead of\n       staying on one scrollable line. Multiple selector variants are used\n       (data-baseweb, role, and Streamlit\'s own class) because Streamlit\'s\n       internal DOM/class names have changed across versions. */\n    div[data-testid="stTabs"],\n    div[data-testid="stTabs"] > div,\n    .stTabs,\n    .stTabs > div {\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        max-width: 100% !important;\n    }\n\n    div[data-baseweb="tab-list"],\n    div[role="tablist"] {\n        display: flex !important;\n        flex-wrap: wrap !important;\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        white-space: normal !important;\n        row-gap: 4px !important;\n        column-gap: 6px !important;\n        height: auto !important;\n        max-width: 100% !important;\n        width: 100% !important;\n        scrollbar-width: none !important;\n    }\n    div[data-baseweb="tab-list"]::-webkit-scrollbar {\n        display: none !important;\n    }\n\n    /* Each tab button: allow shrinking/wrapping instead of forcing one line */\n    button[data-baseweb="tab"],\n    div[role="tablist"] > button,\n    div[role="tablist"] [role="tab"] {\n        flex: 0 0 auto !important;\n        white-space: normal !important;\n        margin-top: 1px !important;\n        margin-bottom: 1px !important;\n        padding-top: 6px !important;\n        padding-bottom: 6px !important;\n        height: auto !important;\n    }\n\n    /* Hide the "‹ ›" scroll-arrow buttons Streamlit shows when a tab bar overflows */\n    button[data-testid="stTabsScrollButton"],\n    div[data-baseweb="tab-list"] ~ button,\n    div[data-baseweb="tab-list"] + button,\n    button[kind="tabScroll"],\n    button[aria-label*="scroll" i] {\n        display: none !important;\n    }\n\n    div[data-baseweb="tab-highlight"] {\n        display: none !important;\n    }\n    div[data-baseweb="tab"][aria-selected="true"],\n    [role="tab"][aria-selected="true"] {\n        background-color: rgba(31, 119, 180, 0.1) !important;\n        border-radius: 5px !important;\n        border-bottom: 2px solid #1f77b4 !important;\n    }\n</style>\n',unsafe_allow_html=B)
Cc=J
BN=J
if JB in A.secrets:Gl.configure(api_key=A.secrets[JB]);Cc=B
if JC in A.secrets:
	try:from groq import Groq as L6;L7=L6(api_key=A.secrets[JC]);BN=B
	except ImportError:BN=J
EV=Cc or BN
def EW(prompt,model_choice):
	A=prompt
	if model_choice==Fp and BN:B=L7.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{'role':'user','content':A}],max_tokens=2048);return B.choices[0].message.content
	elif Cc:C=Gl.GenerativeModel('gemini-2.5-flash');return C.generate_content(A).text
	else:raise RuntimeError('No AI model is configured. Add GEMINI_API_KEY or GROQ_API_KEY to secrets.')
def EX(key_suffix=C):
	D='🧠 Gemini';C,E=[],0
	if BN:C.append(Fp)
	if Cc:C.append(D)
	if not C:C=[Fp,D]
	return A.radio('🤖 AI Model:',C,index=0,horizontal=B,key=f"ai_model_sel_{key_suffix}")
L8=['Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}. Also give me all other details and calculate if this company is profitable or not.','Analyze the 52-week high and low data for {sym}. Is the stock closer to its peak or bottom? What does this imply for entry or exit timing? Identify the ideal buy zone.','Examine the 50 DMA, 100 DMA, and 200 DMA data for {sym}. Is the stock in a bullish crossover, bearish zone, or consolidation phase? Explain the trend strength and momentum.','Using the volume data for {sym}, identify if there is unusual volume activity. Does the current volume indicate institutional buying, selling, or accumulation? What does it signal?','Evaluate the full fundamentals of {sym} — EPS, RONW%, D/E ratio, Net Profit (Cr.), Book Value, and Market Cap. Is this company financially healthy and worth long-term investment?','What is the risk profile of {sym} based on its Pledged %, Promoters Holding %, Institutional Holding %, and Debt-to-Equity ratio? Should a retail investor be cautious right now?',"Compare {sym}'s current CMP vs its 200 DMA. Is the stock overbought, oversold, or fairly valued based on the Difference from 200 DMA metric? What is the ideal risk-reward entry zone?",'Give a complete Buy / Hold / Sell recommendation for {sym} using all available technical and fundamental data. Include specific price targets, support levels, and a stop-loss level.','Based on the CAR Rating and Output signal for {sym}, what is the system suggesting? Does the historical price action and current data support this signal? How reliable is it?',"Summarize {sym}'s sector positioning, market cap, enterprise value, book value, and promoter holding. How does this stock compare to typical benchmarks in its sector in the Indian market?"]
L9="Strategy 1 — Volume Breakout with Dynamic Stop Loss\n  Rule 1: Enter long when today's volume > 2× the 20-day average volume AND price closes above the prior day's high; set stop loss at 1.5× ATR below entry price.\n  Rule 2: Add a false breakout filter — price must hold above the breakout level for 2 consecutive candles before confirming entry; trail stop at the lowest low of the last 3 bars.\n  Rule 3: Set profit target at 2:1 risk-reward ratio; plot a volume histogram overlay to identify surge bars visually; include an alert condition for live breakout detection.\n\nStrategy 2 — Moving Average Crossover (50/100/200 DMA)\n  Rule 4: Buy when 50 DMA crosses above 100 DMA with price trading above the 200 DMA; exit when 50 DMA crosses back below 100 DMA; use 200 DMA as the hard stop-loss floor.\n  Rule 5: Add RSI confirmation — only enter when RSI is between 50–70 at the crossover candle; plot all three DMAs on the chart with distinct colours for visual clarity.\n  Rule 6: Allow a re-entry if 50 DMA pulls back to 100 DMA without breaking below 200 DMA; set stop loss 2% below the 50 DMA value at the time of entry.\n\nStrategy 3 — Trend Following with Trailing Stop\n  Rule 7: Enter long when price breaks a 20-day high with above-average volume and ADX > 25; apply a Chandelier Exit trailing stop set at 3× ATR from the highest close after entry.\n  Rule 8: Use 200 DMA direction as the trend filter — only take long trades when price is above 200 DMA; tighten trailing stop to 2× ATR once profit exceeds 10% from entry.\n  Rule 9: Add a re-entry condition: if stopped out but price remains above 200 DMA, re-enter on the next pullback to the 50 DMA; limit to a maximum of 2 re-entries per trend leg.\n\nStrategy 4 — Mean Reversion from 52W High/Low\n  Rule 10: Buy when price is within 15% of the 52-week low AND RSI < 35; set profit target at the 52-week midpoint; place hard stop loss 5% below the 52-week low level.\n  Rule 11: Exit/short signal when price is within 5% of the 52-week high with RSI > 70; use Bollinger Band upper band touch as secondary confirmation; target the middle Bollinger Band as exit.\n  Rule 12: Apply a volume reversal filter — only enter when the reversal candle's volume is ≥ 1.5× the 20-day average; plot the 52-week high and low as horizontal reference lines on the chart."
LA='\n### 💡 Core Rules\n- **Sheet Convention:** Always use **NSE Code** instead of *Symbol* in the Google Sheet — this keeps NSE chart links working correctly.\n- **No Compromise:** Follow the Rules. Never compromise on Rules — Rules are better than any single Buy/Sell decision.\n- **Timing Edge:** Take advantage of time — buy when a stock is at its lower end (near 52W Low) and sell at a higher price when momentum kicks in (e.g. an Upper Circuit move).\n\n---\n\n### 🟢 Rule 1 — Near 52 Week High\nCMP / Close Price is highlighted **Green** when it is near the 52-Week High (within ~8%).\n\n### 🟠 Rule 2 — Near 52 Week Low (Buy Zone)\nCMP / Close Price is highlighted **Orange** when it is near the 52-Week Low (within ~8%) — **this is the type of stock to look at buying.**\n\n**52W Low / High Date column — color meaning:**\n| Signal | Meaning |\n|---|---|\n| 🟢 Green in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 18 days** |\n| 🟢 Green in *52 Week High Date* | Stock touched its 52-Week High within the **last 18 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 30 days** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High within the **last 30 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low **about 1 year ago** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High **about 1 year ago** |\n\n### 🔵 Rule 3 — Diff @ 200 DMA Strategy\nOnly buy **52-Week Low** stocks, ranked by the **Difference from 200 DMA** column on the **Diff @ 200 DMA** tab — biggest fall first.\n\n**Path:**\n1. Open the **Diff @ 200 DMA** tab (Main sheet).\n2. Refer to the **Difference from 200 DMA** column.\n3. Sort results **−40% → −30% → −20% → −10%** (most negative first).\n\n**Mind Map:**\n```\nRule 3 → Buy Only 52-Week Low Stocks\n│\n├── Main Sheet → Open Tab "Diff @ 200 DMA"\n├── Check Column → "Difference from 200 DMA"\n├── Sort Logic → Biggest Fall First (-40% → -30% → -20% → -10%)\n├── Meaning → Stock is trading below its 200 DMA\n├── Priority → More negative % = higher priority\n├── Selection Criteria\n│     ├── Only 52-Week Low stocks\n│     ├── Negative Difference from 200 DMA\n│     └── Deep-discount stocks preferred\n└── Final Action → Analyze & buy quality stocks\n```\n\n---\n\n### 🔗 Useful NSE Reference Links\n- **All Reports (Bhavcopy / Market Activity):** Bhavcopy (PR)(zip), Market Activity Report (csv), Full Bhavcopy & security delivery data, MCAP, PD, PR, SME → https://www.nseindia.com/all-reports/\n- **Securities Available for Trading** (ETF, Close-Ended MF Schemes, SME) → https://www.nseindia.com/static/market-data/securities-available-for-trading\n- **52-Week Low — Equity Market** → https://www.nseindia.com/market-data/52-week-low-equity-market#capital_market_link\n\n---\n\n### 🛑 Risk Management — No Compromise\n- **Stop Loss (Max 1–2%), no compromise.** બીજો chance મળશે કમાવાનો — પૈસા 10% ઓછા થયા તો 15% કમાવા પડશે.\n- **Risk-Reward Ratio:** max 5 trades, max 10% loss — never lose all your money in a single trade.\n- **Target / Profit Booking:** Max 10–20%.\n- Don\'t trade emotionally — the share market is a mind game.\n- Know everything related to a share before moving ahead.\n- Stay calm, serious, and stick to the decision you\'ve made.\n- **Clear Vision, no compromise:** Focus → Stop Loss → Risk-Reward Ratio → Target/Profit → 52-Week Low Buy.\n- **Priority order:** IPO → F&O → 52-Week Low Shares.\n'
LB={BD:['50 DMA','100 DMA','200 DMA','NSE 1','Trading View 1','History Data 1','Screener 1','Zerodha 1','Chartlink 1','Market smith india 1','Official NSE URL 1'],BE:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
LC={BD:['E','F','G','AA','AB','AC','AD','AE','AF','AG','AH'],BE:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
def Gm(letter):
	A=letter;A=F(A).strip().upper()
	if not A or not A.isalpha():return-1
	B=0
	for C in A:B=B*26+(ord(C)-ord('A')+1)
	return B-1
def LD(sheet_name,ordered_columns):
	C=sheet_name;A=ordered_columns;A=AK(A);B=set()
	for D in LB.get(C,[]):
		if D in A:B.add(D)
	for F in LC.get(C,[]):
		E=Gm(F)
		if 0<=E<P(A):B.add(A[E])
	return B
LE={BD:D,BE:D,CL:D,CM:D,CN:D,CO:D,CP:D}
LF={BD:[u,Ai,'Close Price',AL,JD,Aj,Ak,JE,'Differance from 200 DMA','Cumulative Average Rule (CAR) Rating'],BE:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
LG={BD:['B','C','D','L'],BE:[],CL:[],CM:[],CN:[],CO:[],CP:[]}
def LH(sheet_name,ordered_columns):
	D=sheet_name;A=ordered_columns;A=AK(A);B=[]
	for G in LG.get(D,[]):
		E=Gm(G)
		if 0<=E<P(A):
			F=A[E]
			if F not in B:B.append(F)
	for C in LF.get(D,[]):
		if C in A and C not in B:B.append(C)
	return B
import streamlit as A
LI='\n<style>\n    #MainMenu {visibility: show;}\n    header {visibility: show;}\n    [data-testid="stToolbar"] {visibility: show;}\n    footer {visibility: show;}\n</style>\n'
A.markdown(LI,unsafe_allow_html=B)
import streamlit as A
LJ='\n<style>\n    [data-testid="stToolbar"] {\n        right: 2rem;\n    }\n    [data-testid="stToolbar"]::before {\n        content: "";\n    }\n    button[kind="header"] {display: none;}\n</style>\n'
A.markdown(LJ,unsafe_allow_html=B)
LK='romo'
if'logged_in'not in A.session_state:A.session_state.logged_in=J
if'watchlist'not in A.session_state:A.session_state.watchlist={}
if'ai_history'not in A.session_state:A.session_state.ai_history=[]
if'grid_reset_token'not in A.session_state:A.session_state.grid_reset_token=0
if not A.session_state.logged_in:
	A.markdown("<p style='text-align: center; margin-top: 100px; color: Green; font-size: 18px;'>250-V Dashboard</p>",unsafe_allow_html=B);A.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 20px;'>🔐 Admin Login</h1>",unsafe_allow_html=B);Ow,LL,Ox=A.columns([1,1,1])
	with LL:
		with A.form('login_form'):
			LM=A.text_input('Enter Password',type='password');LN=A.form_submit_button('Login',use_container_width=B)
			if LN:
				if LM==LK:A.session_state.logged_in=B;A.rerun()
				else:import random;LO=['Password इल्ले! 😅 इल्ले!, खम्मा घणी भाईसा, सॉरी। तुमसे सब कुछ हो पाएगा! यहां बहुत 🤪 दिमाग मत लगाओ, इस वेबसाइट को नहीं, 😂 इस गलत पासवर्ड को छोड़ दो!','❌ Password इल्ले भाईसा! 😅 इल्ले! खम्मा घणी, सॉरी। तुम बाहुबली हो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। अपनी सुंदर वेबसाइट को नहीं, 😂 इस सड़े हुए गलत पासवर्ड को छोड़ दो!','❌ खम्मा घणी भाईसा, Password इल्ले! 😅 sorry! तुम तो मंगल ग्रह पर पानी खोज सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस सीधे-सादे वेबसाइट को नहीं, 😂 इस जाली पासवर्ड को छोड़ दो!','❌ Password इल्ले! 😅 इल्ले! खम्मा घणी भाईसा, सॉरी। लोड मत लो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। दुनिया छोड़ दो, मोक्ष पकड़ लो, पर पहले 😂 इस गलत पासवर्ड को छोड़ दो!','❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, सॉरी। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!'];A.error(random.choice(LO))
	LP=k.now().strftime(CQ);A.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {LP}</p>",unsafe_allow_html=B);A.stop()
A.markdown('\n<style>\n    /* Reduce ALL headings to 90% smaller size */\n    h1, h2, h3, h4, h5, h6, .stSubheader, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {\n        font-size: 0.85rem !important;\n        font-weight: bold !important;\n        margin-top: 0.5rem !important;\n        margin-bottom: 0.5rem !important;\n    }\n</style>\n',unsafe_allow_html=B)
import yfinance as Gn,streamlit as A
from datetime import datetime as k
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 Top 250 NSE Stock-Volume Breakout Dashboard</p>",unsafe_allow_html=B)
A.caption(f"Data refreshed: {k.now().strftime(CQ)}")
@A.cache_data(ttl=60)
def LQ():
	A='UNSUPPORTED';H={'NIFTY 50':'^NSEI','NIFTY NEXT 50':'^NN50','NIFTY MIDCAP 50':'^NSEMDCP50','NIFTY MIDCAP 100':'^CRSLMID','NIFTY MIDCAP 150':A,'NIFTY SMLCAP 50':A,'NIFTY SMLCAP 100':A,'NIFTY SMLCAP 250':A,'NIFTY MIDSML 400':A,'NIFTY 100':'^CNX100','NIFTY 200':'^CNX200','NIFTY500 MULTI...':A,'NIFTY LARGEMID...':A,'NIFTY MID SELE...':A,'NIFTY TOTAL MK...':A,'NIFTY MICROCAP...':A,'NIFTY 500':'^CRSLDX','NIFTY FPI 150':A,'NIFTY500 LMS E...':A,'NIFTY MIDSMALL...':A,'NIFTY SMALLCAP...':A};B={}
	for(C,E)in H.items():
		if E==A:B[C]={Az:Ds,v:i};continue
		try:
			I=Gn.Ticker(E);D=I.history(period='5d')
			if not D.empty and P(D)>=2:F=M(D[BF].iloc[-1]);G=M(D[BF].iloc[-2]);J=(F-G)/G*100;B[C]={Az:f"{F:,.2f}",v:J}
			else:B[C]={Az:Fq,v:i}
		except g:B[C]={Az:Fr,v:i}
	return B
LR=LQ()
Ao=JF
Go=0
for(Bw,AQ)in LR.items():
	if AQ[Az]in[Ds,Fq,Fr]:continue
	Go+=1;EY=Cy if AQ[v]>=0 else Fs;EZ='+'if AQ[v]>=0 else C;LS='https://www.nseindia.com/market-data/live-market-indices';Ao+=f"<a href='{LS}' target='_blank' style='text-decoration:none;'>";Ao+=f"<div style='background-color: {EY}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Ao+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bw}</div>";Ao+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Ao+=f"<span style='font-size: 15px; font-weight: 700;'>{AQ[Az]}</span>";Ao+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{EZ}{AQ[v]:.2f}%</span>";Ao+=f"</div></div></a>"
Ao+=Cz
with A.expander('📈 Click to view Live Market Indices',expanded=J):
	if Go==0:A.info('Market data is currently unavailable. Please check back later.')
	else:A.markdown(Ao,unsafe_allow_html=B)
A.write(c)
def Gp(color_dict):
	A=color_dict
	if not A:return C_
	B,C,D=T(A.get('red',0)*255),T(A.get('green',0)*255),T(A.get('blue',0)*255);return f"#{B:02x}{C:02x}{D:02x}"
@A.cache_data(ttl=300,show_spinner=J)
def LT(nse_symbol,period='1y'):
	try:
		C=F(nse_symbol).strip().upper()
		if not C:return H.DataFrame()
		E=C if C.endswith('.NS')else f"{C}.NS";A=Gn.download(E,period=period,interval='1d',progress=J,auto_adjust=B)
		if A is D or A.empty:return H.DataFrame()
		if Ay(A.columns,H.MultiIndex):A.columns=A.columns.get_level_values(0)
		A.index=H.to_datetime(A.index);return A
	except g:return H.DataFrame()
@A.cache_data(ttl=300)
def DJ(sheet_name):
	M='sheets'
	try:
		if Dt not in A.secrets:A.error("Missing 'gcp_service_account' in secrets.");return H.DataFrame()
		D=A.secrets[Dt]
		if Ay(D,F):D=ES.loads(D)
		Y=[JG,JH];N=Gk.from_service_account_info(D,scopes=Y);j=ER.authorize(N);Z=JI;a=urllib.parse.quote(sheet_name);b=L3(N);c=f"https://sheets.googleapis.com/v4/spreadsheets/{Z}?includeGridData=true&ranges={a}";d=b.get(c);E=d.json()
		if'error'in E:return H.DataFrame()
		if M not in E or not E[M]:return H.DataFrame()
		e=E[M][0]['data'][0];O=e.get('rowData',[])
		if not O:return H.DataFrame()
		J,Q,R=[],[],[]
		for f in O:
			h=f.get('values',[]);S,T,U=[],[],[]
			for V in h:S.append(V.get('formattedValue',C));W=V.get('effectiveFormat',{});T.append(Gp(W.get('backgroundColor',{})));U.append(Gp(W.get('textFormat',{}).get('foregroundColor',{})))
			J.append(S);Q.append(T);R.append(U)
		i=J[0];K=[];G={}
		for B in i:
			B=F(B).strip()
			if B==C:B='empty_column'
			if B in G:G[B]+=1;B=f"{B}_{G[B]}"
			else:G[B]=0
			K.append(B)
		L=H.DataFrame(J[1:],columns=K)
		for(I,X)in Dq(K):L[f"_bg_{X}"]=[A[I]if I<P(A)else C_ for A in Q[1:]];L[f"_txt_{X}"]=[A[I]if I<P(A)else'#000000'for A in R[1:]]
		return L
	except g as k:return H.DataFrame()
def LU(df,symbol_col):
	K=symbol_col;H='1';G='🔗 Link';I=df.copy();I[m]=I[K]
	for(L,M)in I.iterrows():
		A=F(M[m]).strip()
		if not A or A==A1:continue
		for J in I.columns:
			if J.startswith(AV)or J.startswith(AW)or J==m:continue
			B=J.lower();C,E=D,G
			if JJ in B:C,E=f"https://www.tradingview.com/symbols/{A}/",f"Tre {A}"if not B.endswith(H)else G
			elif JK in B:C,E=f"https://www.equitypandit.com/historical-data/{A}",f"History {A}"if not B.endswith(H)else G
			elif JL in B:C,E=f"https://www.screener.in/company/{A}",f"Scr {A}"if not B.endswith(H)else G
			elif JM in B:C,E=f"https://zerodha.com/markets/stocks/NSE/{A}",f"🪁 {A}"if not B.endswith(H)else G
			elif JN in B:C,E=f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={A}",f"CL {A}"if not B.endswith(H)else G
			elif JO in B:C,E=f"https://marketsmithindia.com/mstool/eval/{A}/evaluation.jsp",f"ms {A}"if not B.endswith(H)else G
			elif JP in B:C,E=f"https://www.nseindia.com/get-quotes/equity?symbol={A}",f"nse📰 {A}"if not B.endswith(H)else G
			elif'nse'in B or J==K:C,E=f"https://charting.nseindia.com/?symbol={A}-EQ",A if not B.endswith(H)else G
			if C:I.at[L,J]=f'<a href="{C}" target="_blank" style="text-decoration:none; color:#000000;">{E}</a>'
	return I
def DK(df,col_name,st_container,display_label=D):
	J=display_label;D=col_name
	if D in df.columns:
		A=df[D].astype(F).str.replace(BG,C,regex=B);A=H.to_numeric(A,errors=AM).replace([A4.inf,-A4.inf],A4.nan);E=A.dropna()
		if not E.empty:
			G,I=b(M(E.min()),2),b(M(E.max()),2)
			if G<I:L=J if J else f"{D} Range:";K=st_container.slider(L,min_value=G,max_value=I,value=(G,I),key=f"filter_num_{D}");return df[(A>=K[0])&(A<=K[1])]
	return df
def Gq(df,col_name,st_container):
	Q='Past 1 Year';P='Past 6 Months';O='Past 2 Months';N='Past 1 Month';M='Past 30 Days';L='Past 25 Days';K='Past 20 Days';J='Past 15 Days';I='Past 10 Days';G='Past 5 Days';F='All Time';E=col_name
	if E in df.columns:
		R=[F,G,I,J,K,L,M,N,O,P,Q];A=st_container.selectbox(f"{E}:",R,key=f"filter_date_{E}")
		if A!=F:
			S=H.to_datetime(df[E],errors=AM,dayfirst=B);C=H.Timestamp.now()
			if A==G:D=C-H.Timedelta(days=5)
			elif A==I:D=C-H.Timedelta(days=10)
			elif A==J:D=C-H.Timedelta(days=15)
			elif A==K:D=C-H.Timedelta(days=20)
			elif A==L:D=C-H.Timedelta(days=25)
			elif A==M:D=C-H.Timedelta(days=30)
			elif A==N:D=C-H.DateOffset(months=1)
			elif A==O:D=C-H.DateOffset(months=2)
			elif A==P:D=C-H.DateOffset(months=6)
			elif A==Q:D=C-H.DateOffset(years=1)
			return df[S>=D]
	return df
def Bx(val):
	if H.isna(val):return 0
	A=re.sub(Du,C,F(val));return P(A)
def Gr(df):
	A=df.copy();D=[A for A in A.columns if A.startswith(AV)or A.startswith(AW)or A==m];A=A.drop(columns=D,errors='ignore')
	for B in A.select_dtypes(include=['object']).columns:A[B]=A[B].apply(lambda x:re.sub(Du,C,F(x))if H.notnull(x)else x)
	return A
import streamlit.components.v1 as O
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>🌍 National Exchange Scanner (All NSE/BSE Stocks)</p>",unsafe_allow_html=B)
A.caption('Live market data covering 2,000+ equities. Powered by TradingView.')
with A.expander('🏆 Click to view Full-Market India Rankings',expanded=J):
	LV,LW,LX,LY,LZ=A.tabs(['🚀 Gainers & Losers','📦 Volume & Active','⭐ 52W High / Low','🔄 52W Reversals','📊 Top 100 Traded'])
	def Ap(screen_type):return f'''
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
          {{
          "width": "100%",
          "height": "500",
          "defaultColumn": "overview",
          "defaultScreen": "{screen_type}",
          "market": "india",
          "showToolbar": true,
          "colorTheme": "light",
          "locale": "en"
        }}
          </script>
        </div>
        '''
	with LV:
		Aq,Ar=A.columns(2)
		with Aq:A.markdown("<p style='font-size:14px; font-weight:bold;'>🚀 Top Gainers</p>",unsafe_allow_html=B);O.html(Ap('top_gainers'),height=520)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔻 Top Losers</p>",unsafe_allow_html=B);O.html(Ap('top_losers'),height=520)
	with LW:
		Aq,Ar=A.columns(2)
		with Aq:A.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Volume Leaders</p>",unsafe_allow_html=B);O.html(Ap('volume_leaders'),height=520)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Volume & Value)</p>",unsafe_allow_html=B);O.html(Ap('most_active'),height=520)
	with LX:
		Aq,Ar=A.columns(2)
		with Aq:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Highs</p>",unsafe_allow_html=B);O.html(Ap('new_52wk_high'),height=520)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Lows</p>",unsafe_allow_html=B);O.html(Ap('new_52wk_low'),height=520)
	with LY:
		Aq,Ar=A.columns(2)
		with Aq:A.markdown("<p style='font-size:14px; font-weight:bold;'>📈 Outperforming 52W High (Reversal Up)</p>",unsafe_allow_html=B);O.html(Ap('outperforming_52wk_high'),height=520)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>📉 Underperforming 52W Low (Reversal Down)</p>",unsafe_allow_html=B);O.html(Ap('underperforming_52wk_low'),height=520)
	with LZ:A.markdown("<p style='font-size:14px; font-weight:bold;'>📊 Top 100+ Stocks Traded (Full India Screener)</p>",unsafe_allow_html=B);O.html(Ap('general'),height=520)
A.write(c)
@A.cache_data(ttl=300)
def La():
	B=DJ(BD);A={}
	if B.empty:return A
	E=[A for A in B.columns if not A.startswith(AV)and not A.startswith(AW)];I=U((A for A in E if A.lower()in[D0,AX,Dv,Dw,D1,Dx]),D);J=U((A for A in E if A2 in A.lower()),D);K=U((A for A in E if D2 in A.lower()or v in A.lower()),D)
	if not I or not J:return A
	for(R,G)in B.iterrows():
		H=F(G.get(I,C)).strip()
		if not H or H==A1:continue
		O=F(G.get(J,C)).replace(A9,C).strip();P=F(G.get(K,'0')).replace(AA,C).replace(A9,C).strip()if K else'0'
		try:Q=M(O);L=f"{Q:,.2f}"
		except AT:L=Ds
		try:N=M(P)
		except AT:N=i
		A[H]={Az:L,v:N}
	return A
Lb=La()
As=JF
Gs=0
for(Bw,AQ)in Lb.items():
	if AQ[Az]in[Ds,Fq,Fr]:continue
	Gs+=1;EY=Cy if AQ[v]>=0 else Fs;EZ='+'if AQ[v]>=0 else C;Lc=f"https://www.nseindia.com/get-quotes/equity?symbol={Bw}";As+=f"<a href='{Lc}' target='_blank' style='text-decoration:none;'>";As+=f"<div style='background-color: {EY}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";As+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bw}</div>";As+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";As+=f"<span style='font-size: 15px; font-weight: 700;'>{AQ[Az]}</span>";As+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{EZ}{AQ[v]:.2f}%</span>";As+=f"</div></div></a>"
As+=Cz
with A.expander('📈 Click to view Top 250 Stocks Matrix',expanded=J):
	if Gs==0:A.info("Stock matrix data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:A.markdown(As,unsafe_allow_html=B)
A.write(c)
@A.cache_data(ttl=300)
def Ld():
	P='[a-zA-Z%, ]';E=DJ(BD)
	if E.empty:return H.DataFrame()
	G=[A for A in E.columns if not A.startswith(AV)and not A.startswith(AW)];I=U((A for A in G if A.lower()in[D0,AX,Dv,Dw,D1,Dx]),D);J=U((A for A in G if A2 in A.lower()),D);K=U((A for A in G if D2 in A.lower()or v in A.lower()),D);L=U((A for A in G if BH in A.lower()),D);M=U((A for A in G if Dy in A.lower()and'face'not in A.lower()and'enterprise'not in A.lower()),D);N=U((A for A in G if CR in A.lower()),D)
	if not I:return H.DataFrame()
	A=H.DataFrame();A[n]=E[I].astype(F).str.strip();A[AL]=H.to_numeric(E[J].astype(F).str.replace(BG,C,regex=B),errors=AM)if J else i;A[Dz]=H.to_numeric(E[K].astype(F).str.replace(BG,C,regex=B),errors=AM)if K else i;A[u]=H.to_numeric(E[L].astype(F).str.replace(BG,C,regex=B),errors=AM)if L else i;O=A[AL]*A[u]
	if M:A[CS]=H.to_numeric(E[M].astype(F).str.replace(P,C,regex=B),errors=AM)
	else:A[CS]=O
	if N:A[D3]=H.to_numeric(E[N].astype(F).str.replace(P,C,regex=B),errors=AM)
	else:A[D3]=O
	A=A.dropna(subset=[n,AL]).reset_index(drop=B);A=A[(A[n]!=A1)&(A[n]!=C)];return A
def B3(dataframe,metric_label=v):
	J=dataframe;G=metric_label;A="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-family: system-ui, -apple-system, sans-serif;'>"
	if J.empty:return"<p style='color: gray; font-size: 14px;'>No data available for this ranking.</p>"
	for(R,B)in J.iterrows():
		K=B[n];L=B[AL];H=B[Dz];M=Cy if H>=0 else Fs;N='+'if H>=0 else C
		if G==BH:D=B.get(u,0);F=f"Vol: {D/1000000:.1f}M"if D>=1000000 else f"Vol: {D:,.0f}"
		elif G==Dy:E=B.get(CS,0);F=f"Val: ₹{E/10000000:,.1f}Cr"if E>=10000000 else f"Val: ₹{E:,.0f}"
		elif G==CR:I=B.get(D3,0);F=f"T.O: ₹{I/10000000:,.1f}Cr"if I>=10000000 else f"T.O: ₹{I:,.0f}"
		elif G==JQ:D=B.get(u,0);E=B.get(CS,0);O=f"{D/1000000:.1f}M"if D>=1000000 else f"{D/1000:.1f}k";P=f"₹{E/10000000:,.1f}Cr"if E>=10000000 else f"₹{E:,.0f}";F=f"📦 {O} | 💰 {P}"
		else:F=f"{N}{H:.2f}%"
		Q=f"https://www.nseindia.com/get-quotes/equity?symbol={K}";A+=f"<a href='{Q}' target='_blank' style='text-decoration:none;'>";A+=f"<div style='background-color: {M}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";A+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{K}</div>";A+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";A+=f"<span style='font-size: 15px; font-weight: 700;'>{L:,.2f}</span>";A+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px; white-space: nowrap;'>{F}</span>";A+=f"</div></div></a>"
	A+=Cz;return A
Ad=Ld()
with A.expander('🏆 Click to view Advanced Ranking Dashboards (Top 250 Stocks)',expanded=J):
	if Ad.empty:A.info("Ranking data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:
		Le=Ad.nlargest(20,Dz);Lf=Ad.nsmallest(20,Dz);Lg=Ad.nlargest(20,u);Lh=Ad[Ad[u]>0].nsmallest(20,u);Li=Ad.nlargest(20,u);Lj=Ad.nlargest(20,CS);Lk=Ad.nlargest(20,D3);Ll=Ad.nlargest(20,CS);Lm,Ln,Lo,Lp,Lq,Lr=A.tabs(['📈 Gainers/Losers','📦 Volume Leaders','🔥 Active (Vol & Val)','💰 Top by Value','💎 Top by Turnover','💰 Most Active'])
		with Lm:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🚀 Top 20 Gainers</p>",unsafe_allow_html=B);A.markdown(B3(Le,v),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔻 Top 20 Losers</p>",unsafe_allow_html=B);A.markdown(B3(Lf,v),unsafe_allow_html=B)
		with Ln:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>📦 Top 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B3(Lg,BH),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💤 Bottom 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B3(Lh,BH),unsafe_allow_html=B)
		with Lo:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔥 Most Active Stocks (Volume & Traded Value)</p>",unsafe_allow_html=B);A.markdown(B3(Li,JQ),unsafe_allow_html=B)
		with Lp:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active by Traded Value</p>",unsafe_allow_html=B);A.markdown(B3(Lj,Dy),unsafe_allow_html=B)
		with Lq:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💎 Highest Market Turnover</p>",unsafe_allow_html=B);A.markdown(B3(Lk,CR),unsafe_allow_html=B)
		with Lr:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active (Highest Traded Value)</p>",unsafe_allow_html=B);A.markdown(B3(Ll,Dy),unsafe_allow_html=B)
A.write(c)
def DL(row,actual_cols):
	B=0;A=[]
	def E(col_keywords,negate=J):
		for E in col_keywords:
			A=U((A for A in actual_cols if E.lower()in A.lower()),D)
			if A and A in row:
				try:B=M(F(row[A]).replace(AA,C).replace(A9,C).strip());return-B if negate else B
				except:pass
	N=E([A2]);Q=E([JR,CT,'52wlow'])
	if N and Q and Q>0:
		I=(N-Q)/Q*100
		if 8<=I<=15:B+=30;A.append(f"✅ CMP +{I:.1f}% from 52W Low (sweet zone)")
		elif I<8:B+=15;A.append(f"⚠️ CMP +{I:.1f}% from 52W Low (still bottoming)")
		elif I<=25:B+=10;A.append(f"🟡 CMP +{I:.1f}% from 52W Low (extended)")
		else:A.append(f"❌ CMP +{I:.1f}% from 52W Low (too far)")
	O=E([Ft])
	if N and O and O>0:
		if N>O:B+=15;A.append('✅ CMP above 200 DMA (uptrend confirmed)')
		else:
			T=(N-O)/O*100
			if T>-10:B+=7;A.append(f"🟡 CMP {T:.1f}% below 200 DMA (near support)")
			else:A.append(f"❌ CMP {T:.1f}% below 200 DMA (downtrend)")
	K=E([BH])
	if K and K>0:
		if K>=10000000:B+=10;A.append(f"✅ High volume: {K:,.0f}")
		elif K>=1000000:B+=6;A.append(f"🟡 Moderate volume: {K:,.0f}")
		else:B+=2;A.append(f"⚠️ Low volume: {K:,.0f}")
	G=E([JS,'debt','d/e'])
	if G is not D:
		if G<=.1:B+=10;A.append(f"✅ Debt-Free / Zero Debt (D/E={G:.2f})")
		elif G<=.5:B+=7;A.append(f"✅ Very Low Debt (D/E={G:.2f})")
		elif G<=Al:B+=4;A.append(f"🟡 Manageable Debt (D/E={G:.2f})")
		else:A.append(f"❌ High Debt (D/E={G:.2f})")
	R=E([D_])
	if R is not D:
		if R>0:B+=10;A.append(f"✅ Profitable: Net Profit ₹{R:.1f} Cr")
		else:A.append(f"❌ Loss Making: Net Profit ₹{R:.1f} Cr")
	H=E(['ronw'])
	if H is not D:
		if H>=15:B+=10;A.append(f"✅ Strong RONW: {H:.1f}%")
		elif H>=8:B+=6;A.append(f"🟡 Moderate RONW: {H:.1f}%")
		elif H>0:B+=2;A.append(f"⚠️ Low RONW: {H:.1f}%")
		else:A.append(f"❌ Negative RONW: {H:.1f}%")
	L=E([Fu,Fv])
	if L is not D:
		if L>=50:B+=8;A.append(f"✅ Promoter Holding: {L:.1f}%")
		elif L>=35:B+=5;A.append(f"🟡 Promoter Holding: {L:.1f}%")
		else:A.append(f"⚠️ Low Promoter: {L:.1f}%")
	P=E([Fw,Fx])
	if P is not D:
		if P==0:B+=7;A.append('✅ Zero Pledged Shares')
		elif P<=5:B+=4;A.append(f"🟡 Low Pledge: {P:.1f}%")
		else:A.append(f"❌ High Pledge: {P:.1f}%")
	V=E([E0,'net sale'])
	if V and V>0:A.append(f"📊 Net Sales: ₹{V:.1f} Cr")
	W=E([E1])
	if W is not D:A.append(f"📦 % Delivery: {W:.1f}%")
	if B>=75:S='🟢 STRONG BUY'
	elif B>=55:S='🟡 WATCHLIST'
	elif B>=35:S='🟠 CAUTION'
	else:S='🔴 AVOID'
	return B,S,A
Gt=Fy
def Gu():
	if Dt not in A.secrets:return
	B=A.secrets[Dt]
	if Ay(B,F):B=ES.loads(B)
	C=[JG,JH];D=Gk.from_service_account_info(B,scopes=C);return ER.authorize(D)
Ls=JI
def Gv(client):
	try:
		A=client.open_by_key(Ls)
		try:return A.worksheet(Gt)
		except ER.WorksheetNotFound:B=A.add_worksheet(title=Gt,rows=500,cols=6);B.append_row([n,AL,D4,D5,E2,E3]);return B
	except g:return
def Lt():
	D=Gu()
	if not D:return
	E=Gv(D)
	if not E:return
	try:
		I=E.get_all_records();G={}
		for B in I:
			H=F(B.get(n,C)).strip()
			if H:G[H]={BI:F(B.get(D4,C)),A2:F(B.get(AL,C)),CU:F(B.get(D5,C)),Bi:F(B.get(E2,C)),D6:F(B.get(E3,C))}
		A.session_state.watchlist=G
	except g:pass
def Ea():
	F=Gu()
	if not F:A.warning('⚠️ Google Sheet write failed — check secrets.');return J
	E=Gv(F)
	if not E:return J
	try:
		E.clear();E.append_row([n,AL,D4,D5,E2,E3])
		for(G,D)in A.session_state.watchlist.items():E.append_row([G,D.get(A2,C),D.get(BI,C),D.get(CU,C),D.get(Bi,C),D.get(D6,C)])
		return B
	except g as H:A.warning(f"⚠️ Sheet write error: {H}");return J
def Lu(sym,cmp=C,note=C,bf_score=C,bf_grade=C):A.session_state.watchlist[sym]={A2:cmp,BI:note,CU:bf_score,Bi:bf_grade,D6:k.now().strftime('%Y-%m-%d %H:%M')}
def Gw(sym):A.session_state.watchlist.pop(sym,D)
if'watchlist_loaded'not in A.session_state:Lt();A.session_state.watchlist_loaded=B
def Lv(row_data,cols):
	N='sl_standard'
	def E(keys):
		for B in keys:
			for A in cols:
				if B in A.lower():
					try:D=F(row_data.get(A,C)).replace(A9,C).replace(AA,C).strip();return M(D)
					except(AT,Fn):pass
	B=E([A2]);I=E(['52w high',D7,'52wk high']);J=E([JR,CT,'52wk low']);K=E([JT,'50dma']);L=E([Ft,'200dma']);A={A2:B,Fz:I,F_:J,'dma50':K,'dma200':L}
	if B and I and J:G=(I-J)/52;A[E4]=b(G,2);A['sl_tight']=b(B-Al*G,2);A[N]=b(B-1.5*G,2);A['sl_wide']=b(B-2.*G,2);O=2.;H=B-A[N];A['target_1r']=b(B+H*Al,2);A['target_2r']=b(B+H*O,2);A['target_3r']=b(B+H*3.,2);A[D8]=b(K,2)if K else D;A['trail_sl_200dma']=b(L,2)if L else D;A['risk_pct']=b(H/B*100,2)if B else D
	return A
def Eb(history):
	E='AI Analysis';B=history
	if not B:return b''
	F=H.DataFrame(B,columns=[n,'Model','Query','AI Result','Timestamp']);C=io.BytesIO()
	with H.ExcelWriter(C,engine=D9)as D:F.to_excel(D,index=J,sheet_name=E);A=D.sheets[E];A.column_dimensions['A'].width=12;A.column_dimensions['B'].width=14;A.column_dimensions['C'].width=40;A.column_dimensions['D'].width=80;A.column_dimensions['E'].width=20
	return C.getvalue()
if A.sidebar.button('🧹 Clear All Filters',use_container_width=B):
	for Ec in AK(A.session_state.keys()):
		if Ec.startswith('filter_')or Ec in(JU,JV,JW,JX):del A.session_state[Ec]
	A.session_state.grid_reset_token+=1;A.rerun()
A.sidebar.markdown(c)
A.sidebar.header('🔍 Global Search')
Gx=A.sidebar.text_input('Search by Symbol, Name, etc...',key=JU)
A.sidebar.markdown(c)
A.sidebar.header('📑 Select a Tab')
Lw=[BD,BE,CL,CM,CN,CO,CP]
AD=A.sidebar.selectbox('Choose sheet',Lw,key='filter_sheet')
A.markdown(f"<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📄 {AD}</p>",unsafe_allow_html=B)
with A.spinner('Downloading data from Google API...'):Ed=DJ(AD)
if not Ed.empty:
	Ee=0;R=[A for A in Ed.columns if not A.startswith(AV)and not A.startswith(AW)];Lx=LD(AD,R);Ef=LE.get(AD)
	if Ef and Ef in R:Ee=R.index(Ef)
	else:
		for(BO,Ly)in Dq(R):
			if Ly.lower()in[D0,AX,Dv,Dw,D1,Dx]:Ee=BO;break
	A.sidebar.markdown(c);A.sidebar.header('⚙️ Settings');By=A.sidebar.selectbox('Symbol Column (locked):',R,index=Ee,key='filter_symbol_col',disabled=B,help='Locked for consistency across sheets. To change it, edit LOCKED_SYMBOL_COLUMN near the top of the .py file.');Gy=LU(Ed,By);K=Gy.copy()
	if Gx:Lz=K[R].astype(F).apply(lambda x:x.str.contains(Gx,case=J,na=J)).any(axis=1);K=K[Lz]
	A.sidebar.markdown(c);A.sidebar.header('🎨 Color Filters');Eg=A.sidebar.selectbox('Select Column to Filter by Color:',[AN]+R,key='filter_color_col')
	if Eg!=AN:
		Eh=f"_bg_{Eg}"
		if Eh in K.columns:
			L_=K[Eh].unique();Ei={C_:'⚪ White (Default)',w:'🟢 Green',AY:'🔴 Red',JY:'🟡 Yellow','#4285f4':'🔵 Blue',JZ:'🟠 Orange','#b6d7a8':'🟩 Light Green','#f4cccc':'🟥 Light Red','#d9d2e9':'🟪 Light Purple'};Ej=[]
			for M0 in L_:
				Ek=F(M0).lower()
				if Ek in Ei:Ej.append(Ei[Ek])
				else:Ej.append(f"🎨 Custom Hex: {Ek}")
			Gz=A.sidebar.multiselect(f"Select Colors in '{Eg}':",sorted(Ej),key='filter_color_selections')
			if Gz:
				El=[]
				for Em in Gz:
					for(M1,Bw)in Ei.items():
						if Bw==Em:El.append(M1)
					if Em.startswith(Ja):El.append(Em.replace(Ja,C))
				K=K[K[Eh].str.lower().isin(El)]
	A.sidebar.markdown(c);A.sidebar.header('🎯 Categorical Filters');M2=[A for A in R if AU(B in A.lower()for B in['cumulative average',G0,E5,Jb,Jc,G1,G2,G3,Jd,G4])]
	for DM in M2:
		M3=sorted([A for A in Gy[DM].unique()if F(A).strip()!=C]);G_=A.sidebar.multiselect(f"Filter by {DM}:",options=M3,key=f"filter_cat_{DM}")
		if G_:K=K[K[DM].isin(G_)]
	A.sidebar.markdown(c);A.sidebar.header('📈 DMA Trend Filter');Cd=A.sidebar.selectbox('Select DMA Condition:',[Je,Jf,Jg,Jh,Ji],key='filter_dma_trend')
	if Cd!=Je:
		H0=U((A for A in R if JT in A.lower()),D);H1=U((A for A in R if'100 dma'in A.lower()),D);H2=U((A for A in R if Ft in A.lower()),D)
		if H0 and H2:
			DN=H.to_numeric(K[H0].astype(F).str.replace(BG,C,regex=B),errors=AM);DO=H.to_numeric(K[H2].astype(F).str.replace(BG,C,regex=B),errors=AM)
			if Cd==Jh:K=K[DN>DO]
			elif Cd==Ji:K=K[DN<DO]
			elif H1:
				DP=H.to_numeric(K[H1].astype(F).str.replace(BG,C,regex=B),errors=AM)
				if Cd==Jf:K=K[(DN<DP)&(DP<DO)]
				elif Cd==Jg:K=K[(DN>DP)&(DP>DO)]
	A.sidebar.markdown(c);A.sidebar.header('📊 Numeric Range Filters');En=U((A for A in R if'diff'in A.lower()and'200'in A.lower()),D)
	if En:K=DK(K,En,A.sidebar,'Diff. from 200 DMA Range:')
	Eo=U((A for A in R if E6 in A.lower()and'low'in A.lower()and(AA in A.lower()or'per'in A.lower())),D)
	if Eo:K=DK(K,Eo,A.sidebar,'From 52W Low Range:')
	Ep=U((A for A in R if E6 in A.lower()and'high'in A.lower()and(AA in A.lower()or'per'in A.lower())),D)
	if Ep:K=DK(K,Ep,A.sidebar,'From 52W High Range:')
	M4=[u,AL,JD,Jj,Jk,Jl,'Net Profit','EPS',Jm,Jn,'Enterprise Value','RSI','Delivery'];H3={En,Eo,Ep}
	for Ce in M4:
		Eq=U((A for A in R if Ce.lower()in A.lower()and A not in H3),D)
		if Eq:K=DK(K,Eq,A.sidebar);H3.add(Eq)
	A.sidebar.markdown(c);A.sidebar.header('📅 Date Filters');H4=U((A for A in R if Jo in A.lower()),D);H5=U((A for A in R if Jp in A.lower()),D)
	if H4:K=Gq(K,H4,A.sidebar)
	if H5:K=Gq(K,H5,A.sidebar)
	A.sidebar.markdown(c);A.sidebar.header('📊 My Watchlist')
	if A.session_state.watchlist:
		H6=P(A.session_state.watchlist);A.sidebar.caption(f"🔖 {H6} stock{"s"if H6>1 else C} saved")
		for(DQ,Er)in AK(A.session_state.watchlist.items()):
			M5,M6=A.sidebar.columns([3,1]);M5.markdown(f"**{DQ}** {"`"+Er[A2]+"`"if Er[A2]else C}<br><small style='color:gray'>{Er.get(BI,C)[:35]}</small>",unsafe_allow_html=B)
			if M6.button('❌',key=f"wl_rm_{DQ}",help=f"Remove {DQ}"):Gw(DQ);Ea();A.rerun()
		A.sidebar.markdown(C);M7=H.DataFrame([{n:B,AL:A[A2],D4:A[BI],D5:A.get(CU,C),E2:A.get(Bi,C),E3:A[D6]}for(B,A)in A.session_state.watchlist.items()]);H7=io.BytesIO()
		with H.ExcelWriter(H7,engine=D9)as M8:M7.to_excel(M8,index=J,sheet_name=Fy)
		A.sidebar.download_button('📥 Download Watchlist Excel',data=H7.getvalue(),file_name=f"Watchlist_{k.now().strftime(Bj)}.xlsx",mime=Bk,use_container_width=B)
	else:A.sidebar.info('No stocks in watchlist yet.\nAdd from the workspace panel below.')
	if A.session_state.ai_history:
		A.sidebar.markdown(c);A.sidebar.header('🤖 AI History Export');A.sidebar.caption(f"{P(A.session_state.ai_history)} analyses saved this session");M9=Eb(A.session_state.ai_history);A.sidebar.download_button('📥 Download All AI Results (Excel)',data=M9,file_name=f"AI_Analysis_{k.now().strftime(Jq)}.xlsx",mime=Bk,use_container_width=B)
		if A.sidebar.button('🗑️ Clear AI History',use_container_width=B):A.session_state.ai_history=[];A.rerun()
	BP=[]
	if By in K.columns:BP.append(By)
	Bz=U((A for A in R if BH in A.lower()),D);MA=U((A for A in R if Jr in A.lower()or'prev'in A.lower()),D);A5=U((A for A in R if A2 in A.lower()),D);AI=U((A for A in R if D2 in A.lower()),D);B4=U((A for A in R if E6 in A.lower()and'high'in A.lower()and BJ not in A.lower()and AA not in A.lower()),D);B5=U((A for A in R if E6 in A.lower()and'low'in A.lower()and BJ not in A.lower()and AA not in A.lower()),D);BQ=U((A for A in R if E1 in A.lower()),D);BR=U((A for A in R if'rsi'in A.lower()),D);Cf=U((A for A in R if G1 in A.lower()),D);BS=U((A for A in R if G2 in A.lower()),D);DR=U((A for A in R if G3 in A.lower()and A!=Cf and'dma'not in A.lower()),D);DS=U((A for A in R if'macd'in A.lower()),D);BT=U((A for A in R if G4 in A.lower()),D);BU=U((A for A in R if'diff'in A.lower()and'200'in A.lower()),D);H8=LH(AD,R)
	if H8:
		for p in H8:
			if p not in BP:BP.append(p)
	else:
		for Ce in(Bz,MA,A5,AI,B4,B5):
			if Ce and Ce not in BP:BP.append(Ce)
	MB=[A for A in K.columns if A not in BP and not A.startswith(AV)and not A.startswith(AW)and A!=m];MC=[A for A in K.columns if A.startswith(AV)or A.startswith(AW)or A==m];MD=BP+MB+MC;K=K[MD];A.markdown(c)
	with A.expander(f"🚀 Executive Dashboard — {AD}",expanded=B):
		A.caption('Live snapshot of the currently filtered stock universe. Adjust sidebar filters to update instantly.')
		def Ae(series):
			A=series
			if A is D:return H.Series(dtype=M)
			return H.to_numeric(A.astype(F).str.replace('[%,₹\\s]',C,regex=B),errors=AM)
		W=K;ME=P(W);Af=Ae(W[AI])if AI and AI in W.columns else H.Series(dtype=M);H9=Ae(W[Bz])if Bz and Bz in W.columns else H.Series(dtype=M);AR=Ae(W[A5])if A5 and A5 in W.columns else H.Series(dtype=M);BV=Ae(W[B4])if B4 and B4 in W.columns else H.Series(dtype=M);At=Ae(W[B5])if B5 and B5 in W.columns else H.Series(dtype=M);HA=Ae(W[BR])if BR and BR in W.columns else H.Series(dtype=M);HB=Ae(W[BQ])if BQ and BQ in W.columns else H.Series(dtype=M);Es=U((A for A in R if G5 in A.lower()),D);HC=Ae(W[Es])if Es and Es in W.columns else H.Series(dtype=M);Au=Ae(W[BU])if BU and BU in W.columns else H.Series(dtype=M);Et=U((A for A in R if CR in A.lower()),D);HD=Ae(W[Et])if Et and Et in W.columns else H.Series(dtype=M);HE=T((Af>0).sum())if not Af.empty else 0;Eu=T((Af<0).sum())if not Af.empty else 0;MF=T((Af==0).sum())if not Af.empty else 0;Oy=M(Af.mean())if Af.notna().any()else i;Oz=HE/Eu if Eu>0 else D;O_=M(Af.median())if Af.notna().any()else D;P0=M(H9.sum())if H9.notna().any()else i;P1=M(HC.sum())if HC.notna().any()else i;P2=M(HD.sum())if HD.notna().any()else i;P3=M(HA.mean())if HA.notna().any()else D;P4=M(HB.mean())if HB.notna().any()else D;MG=T((Au>0).sum())if Au.notna().any()else 0;MH=T((Au<0).sum())if Au.notna().any()else 0;HF=0
		if BS and BS in W.columns:HF=T(W[BS].astype(F).str.contains('breakout|buy|bullish',case=J,na=J).sum())
		HG=0
		if BT and BT in W.columns:HG=T(W[BT].astype(F).str.contains('buy',case=J,na=J).sum())
		HH,HI=0,0;HJ=0
		if AR.notna().any()and BV.notna().any():MI=AR/BV.replace(0,A4.nan)*100;HH=T((MI>=95).sum())
		if AR.notna().any()and At.notna().any():HK=AR/At.replace(0,A4.nan)*100;HI=T((HK<=105).sum());HJ=T((HK<=115).sum())
		def AS(container,label,value,bg='#f5f7fa',fg='#1a1a1a'):container.markdown(f"<div style='background:{bg}; border-radius:10px; padding:12px 8px; text-align:center; border:1px solid rgba(0,0,0,0.06);'><div style='font-size:0.70em; color:#666; font-weight:700; letter-spacing:0.2px;'>{label}</div><div style='font-size:1.30em; font-weight:800; color:{fg}; margin-top:2px;'>{value}</div></div>",unsafe_allow_html=B)
		BW=A.columns(7);AS(BW[0],'📦 TOTAL STOCKS',f"{ME:,}");AS(BW[1],'🟢 ADVANCES',f"{HE:,}",bg=CV,fg=G6);AS(BW[2],'🔴 DECLINES',f"{Eu:,}",bg=Bl,fg=DA);AS(BW[3],'⚪ UNCHANGED',f"{MF:,}");AS(BW[4],'🕳️ NEAR 52W LOW (≤15%)',f"{HJ:,}"if AR.notna().any()and At.notna().any()else DB,bg=Bl,fg=DA);AS(BW[5],'🚀 BREAKOUTS',f"{HF:,}",bg=G7,fg='#e65100');AS(BW[6],'✅ BUY SIGNALS',f"{HG:,}",bg=Js,fg='#0d47a1');A.markdown("<div style='margin-top:8px;'></div>",unsafe_allow_html=B);DT=A.columns(4);AS(DT[0],'🏔️ NEAR 52W HIGH (≥95%)',f"{HH:,}",bg=CV,fg=G6);AS(DT[1],'🕳️ NEAR 52W LOW (≤5%)',f"{HI:,}",bg=Bl,fg=DA);AS(DT[2],'📉 BELOW 200 DMA',f"{MH:,}"if Au.notna().any()else DB,bg=Bl,fg=DA);AS(DT[3],'🎯 ABOVE 200 DMA',f"{MG:,}"if Au.notna().any()else DB,bg=CV,fg=G6);A.markdown(CW,unsafe_allow_html=B);HL={Jt:J,'modeBarButtons':[['toImage']]}
		def MJ(frac):
			B=frac;B=A8(i,min(Al,B));D=[(i,(234,67,53)),(.5,(249,168,37)),(Al,(15,157,88))]
			for H in Dr(P(D)-1):
				C,A=D[H];E,F=D[H+1]
				if C<=B<=E:G=(B-C)/(E-C)if E>C else i;I=T(A[0]+(F[0]-A[0])*G);J=T(A[1]+(F[1]-A[1])*G);K=T(A[2]+(F[2]-A[2])*G);return f"#{I:02x}{J:02x}{K:02x}"
			return'#999999'
		def P5(title_text,points,y_min,y_max,y_label,height=340):
			G=height;F=y_max;E=points;B=y_min
			if not E:A.info('No data available for this chart.');return
			N=P(E);Q=F-B or Al;H=C
			for(R,(S,I,T))in Dq(E):U=(I-B)/Q;K=A8(i,min(Al,U));V=MJ(K);W=R/A8(N-1,1)*100;X=(1-K)*100;H+=f'<a href="{T}" target="_blank" title="{S}: {I:.2f}{y_label}" style="position:absolute; left:{W:.3f}%; top:{X:.3f}%; width:11px; height:11px; margin:-6px 0 0 -6px; border-radius:50%; background:{V}; display:block; border:1px solid rgba(255,255,255,0.75); box-shadow:0 0 1px rgba(0,0,0,0.35); cursor:pointer;"></a>'
			L=C
			for(Y,M)in[(0,F),(25,D),(50,(B+F)/2),(75,D),(100,B)]:Z=f"{M:.0f}"if M is not D else C;L+=f'<div style="position:absolute; left:0; right:0; top:{Y}%; border-top:1px dashed rgba(0,0,0,0.08); height:0;"><span style="position:absolute; left:-2px; top:-8px; font-size:10px; color:#9aa0a6;">{Z}</span></div>'
			a=f'<div style="font-family:\'Source Sans Pro\',sans-serif;"><div style="font-weight:700; font-size:14px; margin-bottom:2px;">{title_text}</div><div style="font-size:11px; color:#9aa0a6; margin-bottom:8px;">Click any dot to open its NSE chart in a new tab</div><div style="position:relative; width:calc(100% - 26px); height:{G}px; margin-left:26px; background:#fff; border:1px solid rgba(0,0,0,0.08); border-radius:6px; overflow:hidden;">{L}{H}</div><div style="display:flex; justify-content:space-between; margin-left:26px; margin-top:4px;"><span style="font-size:10px; color:#ea4335;">● low</span><span style="font-size:10px; color:#f9a825;">● mid</span><span style="font-size:10px; color:#0f9d58;">● high</span></div></div>';O.html(a,height=G+90,scrolling=J)
		if By in W.columns:Cg=W[By].astype(F)
		elif m in W.columns:Cg=W[m].astype(F)
		else:Cg=W.index.astype(F).to_series(index=W.index)
		if m in W.columns:B_=W[m].astype(F).str.strip()
		else:B_=Cg.astype(F).str.replace('<[^>]+>',C,regex=B).str.strip()
		def HM(fig,chart_key):
			O='customdata';N='points';M='selection';K=chart_key;H=fig;H.update_layout(clickmode='event+select')
			try:I=A.plotly_chart(H,use_container_width=B,key=K,on_select='rerun')
			except Fn:A.plotly_chart(H,use_container_width=B,key=K);A.caption('⚠️ Click-to-open needs Streamlit ≥ 1.35 — update `streamlit` in requirements.txt to enable it.');return
			C=D;F=I.get(M)if Ay(I,E)else Fo(I,M,D)
			if F:
				L=F.get(N)if Ay(F,E)else Fo(F,N,D)
				if L:
					J=L[-1];G=J.get(O)if Ay(J,E)else Fo(J,O,D)
					if G:C=G[0]if Ay(G,(AK,tuple))else G
			if C:
				P=f"https://charting.nseindia.com/?symbol={C}-EQ";Q,R=A.columns([3,1])
				with Q:A.success(f"Selected: **{C}**")
				with R:A.link_button('📈 Open on NSE',P,use_container_width=B)
				A.markdown(f"🔗 **More links for {C}:** [Trading View (🔗)](https://www.tradingview.com/symbols/{C}/) &nbsp;|&nbsp; [History Data (🔗)](https://www.equitypandit.com/historical-data/{C}) &nbsp;|&nbsp; [Screener (🔗)](https://www.screener.in/company/{C}) &nbsp;|&nbsp; [Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{C}) &nbsp;|&nbsp; [Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={C}) &nbsp;|&nbsp; [Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{C}/evaluation.jsp) &nbsp;|&nbsp; [NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={C})")
			else:A.caption('Click any dot above to select a stock — its NSE chart button and quick-links will appear here.')
		MK,ML=A.columns(2)
		with MK:
			if AR.notna().any()and BV.notna().any():HN=(BV-AR)/BV.replace(0,A4.nan)*100;HO=HN.dropna().sort_values(ascending=B).head(20).index;HP=H.DataFrame({n:Cg.loc[HO].values,Ju:HN.loc[HO].values}).iloc[::-1];HQ=Q.Figure(Q.Bar(x=HP[Ju],y=HP[n],orientation='h',marker_color=w));HQ.update_layout(title='🏔️ Top 20 Nearest 52W High',template=x,height=560,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(HQ,use_container_width=B,key=f"dash_nearhigh_{AD}",config=HL)
			else:A.info('52-Week High column not detected for this sheet.')
		with ML:
			if AR.notna().any()and At.notna().any():HR=(AR-At)/At.replace(0,A4.nan)*100;HS=HR.dropna().sort_values(ascending=B).head(20).index;HT=H.DataFrame({n:Cg.loc[HS].values,Jv:HR.loc[HS].values}).iloc[::-1];HU=Q.Figure(Q.Bar(x=HT[Jv],y=HT[n],orientation='h',marker_color=AY));HU.update_layout(title='🕳️ Top 20 Nearest 52W Low',template=x,height=560,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(HU,use_container_width=B,key=f"dash_nearlow_{AD}",config=HL)
			else:A.info('52-Week Low column not detected for this sheet.')
		MM,MN=A.columns(2)
		with MM:
			if AR.notna().any()and BV.notna().any()and At.notna().any():MO=(BV-At).replace(0,A4.nan);HV=((AR-At)/MO*100).clip(0,100);HW=HV.notna()&B_.notna();HX=B_[HW].str.strip().values;HY=HV[HW].values;HZ=Q.Figure(Q.Scatter(x=HX,y=HY,mode=E7,marker=E(size=9,color=HY,colorscale=[[0,AY],[.5,A_],[1,w]],cmin=0,cmax=100,showscale=B,colorbar=E(title='% of Range')),customdata=HX,hovertemplate=Jw));HZ.update_layout(title='📍 Position within 52-Week Range (0% = Low, 100% = High)',template=x,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=Jx),yaxis_title='% of 52W Range');HM(HZ,f"dash_range_{AD}")
			else:A.info('52-Week High/Low columns not detected for this sheet.')
		with MN:
			if Au.notna().any()and B_ is not D:Ha=Au.notna()&B_.notna();Hb=B_[Ha].str.strip().values;DU=Au[Ha].values;Hc=A8(abs(M(A4.nanmin(DU))),abs(M(A4.nanmax(DU))),1e-09);Hd=Q.Figure(Q.Scatter(x=Hb,y=DU,mode=E7,marker=E(size=9,color=DU,colorscale=[[0,AY],[.5,A_],[1,w]],cmin=-Hc,cmax=Hc,showscale=B,colorbar=E(title='% Diff')),customdata=Hb,hovertemplate=Jw));Hd.update_layout(title='📐 Difference from 200 DMA (0% = at 200 DMA)',template=x,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=Jx),yaxis_title='% Diff from 200 DMA');HM(Hd,f"dash_diff200_{AD}")
			else:A.info('Difference from 200 DMA column not detected for this sheet.')
	A.markdown(c);MP,MQ,MR=A.columns([3,1,2.2])
	with MP:He=A.radio(G8,[G9,CX,CY],horizontal=B,help='Automatically adjust the column widths based on the text length of the selected row.')
	with MR:A.markdown("<div style='margin-top: 2px; font-size:0.9rem;'>🔍 Filter stocks inside this matrix...</div>",unsafe_allow_html=B);Hf=A.text_input(Jy,placeholder=Jz,key=JV,label_visibility='collapsed')
	if Hf:K=K[K[m].astype(F).str.contains(Hf,case=J,na=J)]
	MS=Gr(K);Hg=io.BytesIO()
	with H.ExcelWriter(Hg,engine=D9)as MT:MU=AD[:31].replace(':',C).replace('/',C);MS.to_excel(MT,index=J,sheet_name=MU)
	with MQ:A.markdown("<div style='margin-top: 28px;'></div>",unsafe_allow_html=B);A.download_button(label='📥 Download as Excel',data=Hg.getvalue(),file_name=f"{AD}_Export_{k.now().strftime(Bj)}.xlsx",mime=Bk,use_container_width=J)
	MV,MW=A.columns([1,4])
	with MV:A.write(f"**Rows:** {K.shape[0]} | **Columns:** {P(R)}")
	with MW:MX=A.empty()
	DV=B2("\n    class HtmlRenderer {\n        init(params) {\n            this.eGui = document.createElement('span');\n            this.eGui.innerHTML = params.value ? String(params.value) : '';\n        }\n        getGui() {\n            return this.eGui;\n        }\n    }\n    ");Hh=B2('\n    function(params) {\n        let colName = params.colDef.field;\n        let c_low = colName.toLowerCase();\n\n        let bgCol = "_bg_" + colName;\n        let txtCol = "_txt_" + colName;\n\n        let bgColor = params.data[bgCol];\n        let txtColor = params.data[txtCol];\n\n        let isTargetCol = c_low.includes("cmp") || c_low.includes("close price") || c_low.includes("prev");\n\n        if (isTargetCol) {\n            if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') return null;\n            return {\n                \'backgroundColor\': bgColor,\n                \'color\': txtColor || \'#000000\',\n                \'fontWeight\': (txtColor === \'#ffffff\' || bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n            };\n        }\n\n        if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') {\n            return { \'color\': \'#000000\' };\n        }\n\n        return {\n            \'backgroundColor\': bgColor,\n            \'color\': \'#000000\',\n            \'fontWeight\': (bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n        };\n    }\n    ');B6=EU.from_dataframe(K);B6.configure_selection(selection_mode='single',use_checkbox=B);B6.configure_side_bar(filters_panel=J,columns_panel=B);MY=[D0,D1,J_,K0,AX,G0,E5];Ch=B
	for p in K.columns:
		if p.startswith(AV)or p.startswith(AW)or p==m:B6.configure_column(p,hide=B);continue
		if p in Lx:B6.configure_column(p,hide=B);continue
		if He==CX and P(K)>0:
			Ev=Bx(K.iloc[0][p]);Ew=P(F(p));Ci=T(A8(Ev,Ew)*7+22)
			if Ch:Ci+=30
			DW,DX=Ci,40
		elif He==CY and P(K)>1:
			Ev=Bx(K.iloc[1][p]);Ew=P(F(p));Ci=T(A8(Ev,Ew)*7+22)
			if Ch:Ci+=30
			DW,DX=Ci,40
		else:DW,DX=(220,150)if p.lower()in MY else(120,80)
		Cj=p==By;Hi=DC if Cj or Ch else D
		if Ch:Ch=J
		MZ=p.lower()
		if Cj or AU(A in MZ for A in[JJ,JK,JL,JM,JN,JO,JP,'nse']):B6.configure_column(p,width=DW,minWidth=DX,sortable=B,filter=B,resizable=B,editable=J,pinned=Hi,lockPinned=Cj,suppressMovable=Cj,checkboxSelection=Cj,cellRenderer=DV,cellStyle=Hh)
		else:B6.configure_column(p,width=DW,minWidth=DX,sortable=B,filter=B,resizable=B,editable=J,pinned=Hi,cellStyle=Hh)
	B6.configure_grid_options(domLayout=AO,rowHeight=35,headerHeight=45,enableCellTextSelection=B,ensureDomOrder=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);Ma=B6.build();Mb=ET(K,gridOptions=Ma,theme=GA,update_mode=L4.SELECTION_CHANGED,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,enable_enterprise_modules=J,height=400,width=GB,key=f"primary_stock_table_grid_{A.session_state.grid_reset_token}");BX=Mb.get('selected_rows',[])
	if BX is not D and P(BX)>0 or P(K)>0:
		if BX is not D and P(BX)>0:S=BX.iloc[0]if Ay(BX,H.DataFrame)else BX[0]
		else:S=K.iloc[0]
		G=F(S.get(m,C)).strip()
		if G:
			with MX.container():A.markdown(f"**⚡ {G} Links:** [Trading View (🔗)](https://www.tradingview.com/symbols/{G}/) &nbsp;|&nbsp; [History Data (🔗)](https://www.equitypandit.com/historical-data/{G}) &nbsp;|&nbsp; [Screener (🔗)](https://www.screener.in/company/{G}) &nbsp;|&nbsp; [Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{G}) &nbsp;|&nbsp; [Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={G}) &nbsp;|&nbsp; [Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{G}/evaluation.jsp) &nbsp;|&nbsp; [NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={G})")
			A.markdown(f"---");A.subheader(f"🛠️ Live Workspace Panel: {G}");A6=A.slider('📏 Adjust Panel Box Height (px):',min_value=300,max_value=1000,value=500,step=50,key='panel_height_slider');A7=A.tabs(['🕯️ Price Chart (EMA + RSI)','📈 Chart & Trade Info (NSE Component)','📋 History Data (EquityPandit)','🎯 Bullish/Bearish Zone','📁 Screener Documents','🪁 Zerodha Portal','📊 MarketSmith India','📉 TradingView Symbol Profile','🤖 AI Stock Analysis','💻 AI Pine Script Builder','🔬 Bottom Fishing Score','🎯 GTT Order Calculator','📊 Watchlist Manager','📰 News Feed'])
			with A7[1]:Hj=f"https://charting.nseindia.com/?symbol={G}-EQ";A.markdown(f"**NSE Interactive Chart Frame** &nbsp;|&nbsp; [🌐 Open in Browser]({Hj})",unsafe_allow_html=J);A.caption(Bm);O.html(f'<iframe src="{Hj}" width="100%" height="{A6}" style="border:none; border-radius:5px;"></iframe>',height=A6+20)
			with A7[2]:Hk=f"https://www.equitypandit.com/historical-data/{G.lower()}";A.markdown(f"**EquityPandit Historical Matrix Data** &nbsp;|&nbsp; [🌐 Open in Browser]({Hk})");A.caption(Bm);O.html(f'<iframe src="{Hk}" width="100%" height="{A6}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A6+20)
			with A7[3]:Hl=f"https://www.equitypandit.com/share-price/{G.lower()}#chart";A.markdown(f"**Bullish / Bearish Zone Indicator** &nbsp;|&nbsp; [🌐 Open in Browser]({Hl})");A.caption(Bm);O.html(f'<iframe src="{Hl}" width="100%" height="{A6}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A6+20)
			with A7[4]:Hm=f"https://www.screener.in/company/{G}/consolidated/";A.markdown(f"**Screener Corporate Filings** &nbsp;|&nbsp; [🌐 Open in Browser]({Hm})");A.caption(Bm);O.html(f'<iframe src="{Hm}" width="100%" height="{A6}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A6+20)
			with A7[5]:Hn=f"https://zerodha.com/markets/stocks/NSE/{G}/";A.markdown(f"**Zerodha Markets Financial Performance Metrics** &nbsp;|&nbsp; [🌐 Open in Browser]({Hn})");A.caption(Bm);O.html(f'<iframe src="{Hn}" width="100%" height="{A6}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A6+20)
			with A7[6]:Ho=f"https://marketsmithindia.com/mstool/eval/{G.lower()}/evaluation.jsp";A.markdown(f"**MarketSmith India Institutional Trading Evaluation Engine** &nbsp;|&nbsp; [🌐 Open in Browser]({Ho})");A.caption(Bm);O.html(f'<iframe src="{Ho}" width="100%" height="{A6}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A6+20)
			with A7[7]:Hp=f"https://www.tradingview.com/symbols/{G}/";A.markdown(f"**TradingView Comprehensive Asset Market Registry Summary Profile** &nbsp;|&nbsp; [🌐 Open in Browser]({Hp})");A.caption(Bm);O.html(f'<iframe src="{Hp}" width="100%" height="{A6}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A6+20)
			with A7[8]:
				A.markdown(f"### 🤖 Ask AI About **{G}**")
				if not EV:A.warning(K1)
				else:
					DY=EX('analysis');A.caption('⚡ Groq = llama-3.3-70b (free, fast) &nbsp;|&nbsp; 🧠 Gemini = gemini-2.5-flash'if BN and Cc else'⚡ Groq connected'if BN else'🧠 Gemini connected');A.write('Using the live data pulled from your dashboard, the AI can analyze technicals, ranges, and context.');Ex=A.text_area('Your Query:',value=f"Based on the current data provided, give me a quick summary of the technical performance and trend for {G}.",height=80,key='ai_query_analysis')
					if A.button('✨ Generate AI Analysis',use_container_width=B,key='btn_ai_analysis'):
						with A.spinner(f"Analyzing {G} with {DY}..."):
							try:Ey={A:B for(A,B)in S.items()if not F(A).startswith(Bn)};Ck=f"""
You are a professional stock market analyst evaluating Indian NSE stocks.
The user is asking about the stock: {G}.

Here is the live data extracted directly from the user's dashboard for this stock:
{Ey}

User Query: {Ex}

Please provide a clear, concise, and professional response.
""";Ez=EW(Ck,DY);A.session_state[GC]={DD:G,E8:DY,'query':Ex,DE:Ez};A.session_state.ai_history.append([G,DY,Ex,Ez,k.now().strftime(CQ)]);A.info(Ez)
							except g as BY:A.error(f"AI error: {BY}")
					if A.session_state.get(GC,{}).get(DD)==G:
						Cl=A.session_state[GC];DZ=Cl[DE];A.markdown(c);Mc,Md,Me=A.columns(3)
						with Mc:Mf=Eb([[G,Cl[E8],Cl['query'],DZ,k.now().strftime(CQ)]]);A.download_button('📥 Save as Excel',data=Mf,file_name=f"AI_{G}_{k.now().strftime(Jq)}.xlsx",mime=Bk,use_container_width=B,key='dl_ai_excel_analysis')
						with Md:Mg=urllib.parse.quote(f"📊 *{G} AI Analysis* ({Cl[E8]})\n\n{DZ[:800]}"+('\n\n_(truncated)_'if P(DZ)>800 else C));A.markdown(f"<a href='https://wa.me/?text={Mg}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
						with Me:Mh=urllib.parse.quote(f"📊 {G} AI Analysis ({Cl[E8]})\n\n{DZ[:800]}");A.markdown(f"<a href='https://t.me/share/url?url=NSEDashboard&text={Mh}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
					A.markdown(c);A.markdown('**💡 Suggested Prompts** — copy any prompt below and paste it into the query box above:');Mi='\n'.join([f"{A+1}. {B.replace("{sym}",G)}"for(A,B)in Dq(L8)]);A.text(Mi)
			with A7[9]:
				A.markdown(f"### 💻 AI Pine Script Generator for **{G}**")
				if not EV:A.warning(K1)
				else:
					Mj=EX('pine');A.write("Generate a custom TradingView Pine Script v5 strategy tailored to this stock's current metrics.");Hq=A.selectbox('Select Strategy Focus:',['Volume Breakout with Dynamic Stop Loss','Moving Average Crossover (50/100/200 DMA)','Trend Following with Trailing Stop','Mean Reversion from 52W High/Low'],key='pine_strategy_focus');Mk=A.text_area('Additional Custom Rules (Optional):',value=f"Include risk management parameters and plot signals on the chart.",height=60,key='pine_query')
					if A.button('⚙️ Generate TradingView Pine Script',use_container_width=B,key='btn_pine'):
						with A.spinner(f"Writing Pine Script v5 code for {G}..."):
							try:Ey={A:B for(A,B)in S.items()if not F(A).startswith(Bn)};Ck=f'''
You are an expert quantitative developer specializing in TradingView Pine Script v5.

Write a complete, ready-to-copy Pine Script v5 strategy for the stock: {G}.

Strategy Focus: {Hq}
Custom Rules: {Mk}

Here is the live fundamental and technical data for {G} to incorporate as baseline context or threshold values if relevant:
{Ey}

Formatting Requirements:
1. Start with `//@version=5` and `strategy("{G} Custom Script", overlay=true)`
2. Include clear comments explaining the logic.
3. Provide ONLY the Pine Script code inside a markdown code block, no other conversational text.
''';Hr=EW(Ck,Mj);A.session_state[GD]={DD:G,DE:Hr};A.markdown('### 📋 Your Custom Strategy Code:');A.write('Copy the code below and paste it into the TradingView Pine Editor.');A.markdown(Hr)
							except g as BY:A.error(f"AI error: {BY}")
					if A.session_state.get(GD,{}).get(DD)==G:Ml=A.session_state[GD][DE];Mm=Eb([[G,'Pine Script',Hq,Ml,k.now().strftime(CQ)]]);A.download_button('📥 Save Pine Script as Excel',data=Mm,file_name=f"PineScript_{G}_{k.now().strftime(Bj)}.xlsx",mime=Bk,key='dl_pine_excel')
					A.markdown(c);A.markdown('**📋 Custom Rules Reference** — copy any rule and paste it into the Additional Custom Rules box above:');A.text(L9)
			with A7[10]:
				A.markdown(f"### 🔬 Bottom Fishing Analysis: **{G}**");A.caption('Scores this stock on 8 key criteria for buying from the bottom. Based entirely on your live sheet data.');Hs={A:B for(A,B)in S.items()if not F(A).startswith(Bn)};C0,E_,F0=DL(Hs,R);F1=AZ if C0>=75 else JY if C0>=55 else JZ if C0>=35 else AY;A.markdown(f'''
                <div style="background:{F1}22; border-left:6px solid {F1}; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
                    <div style="font-size:2rem; font-weight:bold; color:{F1};">{C0}/100</div>
                    <div style="font-size:1.3rem; font-weight:bold;">{E_}</div>
                    <div style="font-size:0.85rem; color:#555; margin-top:4px;">Bottom Fishing Composite Score for {G}</div>
                </div>
                ''',unsafe_allow_html=B);A.markdown('#### 📋 Detailed Scoring Breakdown')
				for Mn in F0:A.markdown(f"- {Mn}")
				A.markdown(c);A.markdown('#### 📖 Scoring Criteria');Mo='\n| # | Criteria | Max Points | Description |\n|---|----------|-----------|-------------|\n| 1 | **52W Low Proximity** | 30 | CMP is 8–15% above 52W Low (ideal entry zone) |\n| 2 | **Uptrend (200 DMA)** | 15 | CMP above 200 DMA = confirmed uptrend |\n| 3 | **Volume Activity** | 10 | High trading volume = institutional interest |\n| 4 | **Low/Zero Debt** | 10 | D/E ratio ≤ 0.1 is ideal (no loan burden) |\n| 5 | **Net Profitability** | 10 | Positive net profit confirms fundamental health |\n| 6 | **RONW %** | 10 | Return on Net Worth ≥ 15% = strong business |\n| 7 | **Promoter Holding** | 8 | ≥ 50% shows management confidence |\n| 8 | **Zero Pledge** | 7 | No pledged shares = no financial stress |\n';A.markdown(Mo);A.info('💡 **Buy Strategy:** Look for scores ≥ 55 (Watchlist) or ≥ 75 (Strong Buy). The sweet zone is CMP at 8–15% above 52W Low with uptrend confirmed (CMP > 200 DMA), backed by positive profits, low debt, and high promoter holding. This combination maximizes probability of a bull run from the bottom.')
				if EV:
					A.markdown(c);F2=EX('bf')
					if A.button('🤖 Get AI Deep Analysis for Bottom Buy',use_container_width=B,key='bf_ai_btn'):
						with A.spinner(f"Running deep bottom-fishing analysis for {G} with {F2}..."):
							try:Ck=f"""
You are an expert Indian stock market analyst specializing in bottom-fishing and value investing.

Stock: {G}
Live Data from Dashboard: {Hs}
Bottom Fishing Score: {C0}/100
Grade: {E_}
Scoring Breakdown: {chr(10).join(F0)}

Please provide a comprehensive bottom-fishing analysis covering:
1. Is this stock in or near the 52-week low zone? What does this mean?
2. Is the stock entering an uptrend? Evidence from DMA data.
3. Volume analysis — is there accumulation visible?
4. Fundamental health — debt, profitability, revenue growth signals.
5. Bull run potential — sector tailwinds, promoter activity, institutional interest.
6. Specific entry price zone recommendation with stop loss and target.
7. Risk factors that could delay recovery.
8. Overall verdict: Strong Buy / Watchlist / Avoid for bottom-fishing strategy.

Be specific, data-driven, and actionable for a retail investor.
""";F3=EW(Ck,F2);A.session_state['last_bf_ai_result']={DD:G,DE:F3};A.session_state.ai_history.append([G,F2,'Bottom Fishing Deep Analysis',F3,k.now().strftime(CQ)]);A.success('✅ AI Analysis Complete');A.markdown(F3)
							except g as BY:A.error(f"AI error: {BY}")
					A.markdown(c);A.markdown('#### 📤 Share BF Score Card');Ht=f"""🔬 *Bottom Fishing Score: {G}*

📊 Score: *{C0}/100*
📈 Grade: {E_}

"""+'\n'.join(F0[:5])+f"\n\n🕒 {k.now().strftime(K2)}\n📌 NSE Stock Dashboard";Mp=urllib.parse.quote(Ht);Mq=urllib.parse.quote(Ht);Mr,Ms=A.columns(2)
					with Mr:A.markdown(f"<a href='https://wa.me/?text={Mp}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
					with Ms:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={Mq}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
			with A7[11]:
				A.markdown(f"### 🎯 GTT Order Calculator: **{G}**");A.caption('Auto-suggest Stop-Loss, Targets & ATR-based GTT levels from your live sheet data.');Mt={A:B for(A,B)in S.items()if not F(A).startswith(Bn)};AE=Lv(Mt,R)
				if not AE.get(A2):A.warning('⚠️ CMP column not found in sheet data. Cannot compute GTT levels.')
				else:
					V=AE[A2];Mu,Mv,Mw,Mx=A.columns(4);Mu.metric('📍 CMP',f"₹{V:,.2f}")
					if AE.get(Fz):Mv.metric('⬆️ 52W High',f"₹{AE[Fz]:,.2f}")
					if AE.get(F_):Mw.metric('⬇️ 52W Low',f"₹{AE[F_]:,.2f}")
					if AE.get(E4):Mx.metric('📊 ATR (approx)',f"₹{AE[E4]:,.2f}")
					A.markdown(c);A.markdown('#### ⚙️ Customize ATR Multiplier');My,Mz=A.columns(2);Hu=My.number_input('Manual ATR Override (₹) — leave 0 to use auto',min_value=i,value=i,step=.5,key='gtt_manual_atr');Da=Mz.selectbox('Risk-Reward Ratio:',['1:1','1:1.5','1:2','1:2.5','1:3'],index=2,key='gtt_rr_ratio');M_=M(Da.split(':')[1]);C1=Hu if Hu>0 else AE.get(E4,0)
					if C1 and C1>0:
						Hv=b(V-Al*C1,2);C2=b(V-1.5*C1,2);Hw=b(V-2.*C1,2);Db=V-C2;Dc=b(V+Db*Al,2);Dd=b(V+Db*M_,2);De=b(V+Db*3.,2);N0=b(Db/V*100,2);A.markdown('#### 🛡️ Stop-Loss Levels');F4=H.DataFrame([{E9:'Tight SL (1× ATR)',BK:Hv,EA:b((V-Hv)/V*100,2),EB:'Intraday / Scalp'},{E9:'Standard SL (1.5× ATR)',BK:C2,EA:b((V-C2)/V*100,2),EB:'Swing / BTST'},{E9:'Wide SL (2× ATR)',BK:Hw,EA:b((V-Hw)/V*100,2),EB:'Positional'}])
						if AE.get(D8):F4=H.concat([F4,H.DataFrame([{E9:'Trail SL @ 50 DMA',BK:AE[D8],EA:b((V-AE[D8])/V*100,2)if AE[D8]<V else 0,EB:'Trailing Stop'}])],ignore_index=B)
						A.dataframe(F4,use_container_width=B,hide_index=B);A.markdown(f"#### 🎯 Target Levels (based on {Da} R:R)");N1=H.DataFrame([{GE:'T1 (1R)',BK:Dc,GF:b((Dc-V)/V*100,2),GG:'Book 30–40%'},{GE:f"T2 ({Da} R:R)",BK:Dd,GF:b((Dd-V)/V*100,2),GG:'Book 40–50%'},{GE:'T3 (3R — runner)',BK:De,GF:b((De-V)/V*100,2),GG:'Hold remainder'}]);A.dataframe(N1,use_container_width=B,hide_index=B);A.markdown('#### 💰 Position Sizing Helper');N2,N3=A.columns(2);N4=N2.number_input('Capital (₹):',min_value=1000,value=100000,step=5000,key='gtt_capital');Hx=N3.number_input('Max Risk % of Capital:',min_value=.5,max_value=1e1,value=2.,step=.5,key='gtt_risk_pct');Hy=N4*Hx/100;F5=T(Hy/(V-C2))if V-C2>0 else 0;Hz=F5*V;A.success(f"📦 Suggested Qty: **{F5} shares** &nbsp;|&nbsp; Investment: **₹{Hz:,.0f}** &nbsp;|&nbsp; Max Loss: **₹{Hy:,.0f}** ({Hx}%)");A.markdown(c);A.markdown('#### 📋 GTT Order Summary (Copy-Ready)');F6=f"""🎯 *GTT Order: {G}*

📍 Entry CMP: ₹{V:,.2f}
🛡️ Stop-Loss: ₹{C2:,.2f} ({N0:.1f}% risk)
🎯 Target 1:  ₹{Dc:,.2f} (+{b((Dc-V)/V*100,1)}%)
🎯 Target 2:  ₹{Dd:,.2f} (+{b((Dd-V)/V*100,1)}%)
🎯 Target 3:  ₹{De:,.2f} (+{b((De-V)/V*100,1)}%)
📦 Qty: {F5} shares | ₹{Hz:,.0f}
📊 ATR: ₹{C1:.2f} | R:R {Da}
🕒 {k.now().strftime(K2)}""";A.code(F6,language=C);N5=urllib.parse.quote(F6);N6=urllib.parse.quote(F6);N7,N8=A.columns(2)
						with N7:A.markdown(f"<a href='https://wa.me/?text={N5}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share GTT on WhatsApp</button></a>",unsafe_allow_html=B)
						with N8:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={N6}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share GTT on Telegram</button></a>",unsafe_allow_html=B)
					else:A.warning('⚠️ Could not compute ATR — 52W High/Low columns not found in sheet. Please enter ATR manually above.')
			with A7[12]:
				A.markdown(f"### 📊 Watchlist Manager");H_={A:B for(A,B)in S.items()if not F(A).startswith(Bn)};N9,NA,_=DL(H_,R);NB=F(H_.get(A5,C))if A5 else C;F7=G in A.session_state.watchlist;A.markdown(f"**Current Stock: {G}** {"✅ Already in Watchlist"if F7 else C}");NC=A.text_input('📝 Note (optional):',value=A.session_state.watchlist.get(G,{}).get(BI,C),placeholder='e.g. Near 52W low, watching for breakout',key=f"wl_note_{G}");ND,NE=A.columns(2)
				with ND:
					if A.button(f"{"🔄 Update"if F7 else"➕ Add"} {G} to Watchlist",use_container_width=B,key='wl_add_btn'):
						Lu(G,cmp=NB,note=NC,bf_score=F(N9),bf_grade=NA);NF=Ea()
						if NF:A.success(f"✅ {G} saved to Watchlist (Google Sheet updated!)")
						else:A.info(f"✅ {G} added to session Watchlist (Sheet write failed — check secrets).")
						A.rerun()
				with NE:
					if F7:
						if A.button(f"❌ Remove {G} from Watchlist",use_container_width=B,key='wl_rm_btn'):Gw(G);Ea();A.rerun()
				A.markdown(c);A.markdown('#### 🗂️ Your Full Watchlist')
				if A.session_state.watchlist:
					NG=[{n:B,'CMP (₹)':A[A2],D5:A.get(CU,C),GH:A.get(Bi,C),D4:A.get(BI,C),'Added':A.get(D6,C)}for(B,A)in A.session_state.watchlist.items()];I0=H.DataFrame(NG);A.dataframe(I0,use_container_width=B,hide_index=B);I1=io.BytesIO()
					with H.ExcelWriter(I1,engine=D9)as NH:I0.to_excel(NH,index=J,sheet_name=Fy)
					A.download_button('📥 Download Watchlist as Excel',data=I1.getvalue(),file_name=f"Watchlist_{k.now().strftime(Bj)}.xlsx",mime=Bk,use_container_width=B,key='dl_wl_excel_tab');NI='\n'.join([f"• {B} — Score:{A.get(CU,C)} {A.get(Bi,C).split()[0]if A.get(Bi)else C} — {A.get(BI,C)[:30]}"for(B,A)in AK(A.session_state.watchlist.items())[:15]]);I2=f"📊 *My NSE Watchlist*\n\n{NI}\n\n🕒 {k.now().strftime(EC)}";NJ=urllib.parse.quote(I2);NK=urllib.parse.quote(I2);A.markdown(C);NL,NM=A.columns(2)
					with NL:A.markdown(f"<a href='https://wa.me/?text={NJ}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share Watchlist on WhatsApp</button></a>",unsafe_allow_html=B)
					with NM:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={NK}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share Watchlist on Telegram</button></a>",unsafe_allow_html=B)
				else:A.info('Your watchlist is empty. Add stocks using the button above!')
			with A7[13]:
				A.markdown(f"### 📰 Latest News & Alerts: **{G}**");import urllib.request,urllib.parse,xml.etree.ElementTree as C3,datetime as k,email.utils
				def NN(pubdate_str):
					try:
						E=email.utils.parsedate_to_datetime(pubdate_str);F=k.datetime.now(k.timezone.utc);G=F-E;A=G.total_seconds()
						if A<0:return AG
						if A<60:return f"{T(A)} secs ago"
						if A<3600:B=T(A/60);return f"{B} min{"s"if B!=1 else C} ago"
						if A<86400:D=T(A/3600);return f"{D} hour{"s"if D!=1 else C} ago"
						if A<172800:return'Yesterday'
						H=T(A/86400);return f"{H} days ago"
					except g:return GI
				@A.cache_data(ttl=600)
				def NO(target_symbol,limit=10):
					try:
						I=urllib.parse.quote(f'"{target_symbol}" stock share news NSE India');J=f"https://news.google.com/rss/search?q={I}&hl=en-IN&gl=IN&ceid=IN:en";K=urllib.request.Request(J,headers={CZ:Ca})
						with urllib.request.urlopen(K)as M:N=M.read()
						O=C3.fromstring(N);P=[D7,ED,CT,EE,EF,EG,EH,EI];E=[]
						for A in O.findall(DF):
							F=A.find(A3).text;Q=A.find(f).text;G=A.find(Am).text if A.find(Am)is not D else C;R=AU(A in F.lower()for A in P);S=GJ if R else C
							try:H=email.utils.parsedate_to_datetime(G)
							except g:H=k.datetime.min.replace(tzinfo=k.timezone.utc)
							E.append({AB:f"{S}{F}",f:Q,L:NN(G),AH:H})
						E.sort(key=lambda x:x[AH],reverse=B);return E[:limit]
					except g:return[]
				with A.spinner(f"Fetching today's latest news for {G}..."):
					I3=NO(G,limit=10)
					if I3:
						for N in I3:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.5em 0; opacity: 0.2;'>",unsafe_allow_html=B)
					else:A.info(f"No recent news found for {G}.")
			with A7[0]:
				with A.expander(f"🕯️ Price Chart & Technical Indicators — {G}",expanded=B):
					NP=A.select_slider('History range:',options=['3mo','6mo','1y','2y','5y'],value='1y',key=f"chart_period_{G}")
					with A.spinner(f"Loading price history for {G}..."):l=LT(G,period=NP)
					if l.empty or BF not in l.columns:A.warning(f"⚠️ No historical price data available for **{G}** via Yahoo Finance (tried `{G}.NS`). The symbol may be delisted, renamed, or not tracked by Yahoo.")
					else:
						Ag=l[BF].squeeze().dropna();AJ=M(Ag.iloc[-1]);BZ=M(Ag.iloc[-2])if P(Ag)>1 else AJ;Df=(AJ-BZ)/BZ*100 if BZ else i;I4=Ag.diff();NQ=I4.clip(lower=0).rolling(14).mean();NR=(-I4.clip(upper=0)).rolling(14).mean();F8=100-100/(1+NQ/NR.replace(0,M(A1)));Cm=F8.dropna().iloc[-1]if not F8.dropna().empty else D;NS,NT=A.tabs(['Price + EMAs','RSI'])
						with NS:
							NU=A.radio('Chart type',[K3,'Line'],horizontal=B,key=f"chart_type_{G}");I5=Ag.diff();NV=I5.clip(lower=0).rolling(9).mean();NW=(-I5.clip(upper=0)).rolling(9).mean();Av=100-100/(1+NV/NW.replace(0,M(A1)));F9=Av.ewm(span=3,adjust=J).mean();I6=A4.arange(1,22,dtype=M);FA=Av.rolling(21).apply(lambda x:M(A4.dot(x,I6)/I6.sum()),raw=B);s=AK(l.index);I7=Av.values;Cn,I8=[],[];FB,I9=[],[]
							for BO in Dr(22,P(Av)):
								FC,IA=I7[BO],I7[BO-1]
								if A4.isnan(FC)or A4.isnan(IA):continue
								if FC>=50 and IA<50:
									Dg=Av.index[BO]
									if Dg in Ag.index:Cn.append(Dg);I8.append(M(Ag.loc[Dg])*.993);FB.append(Dg);I9.append(M(FC))
							if not F9.dropna().empty and not FA.dropna().empty:FD=F9.dropna().iloc[-1];FE=FA.dropna().iloc[-1];FF=GK if FD>FE else GL;NX='🟢 H-M: POSITIVE (Bullish)'if FD>FE else'🔴 H-M: NEGATIVE (Bearish)';A.markdown(f"<div style='background:{FF}22;border-left:4px solid {FF};padding:6px 12px;border-radius:4px;margin-bottom:6px;font-size:13px;font-weight:700;color:{FF}'>{NX} — EMA3: {FD:.1f} | WMA21: {FE:.1f}</div>",unsafe_allow_html=B)
							e=L5(rows=3,cols=1,shared_xaxes=B,row_heights=[.55,.25,.2],vertical_spacing=.03,specs=[[{GM:'xy'}],[{GM:'xy'}],[{GM:'xy'}]])
							if NU==K3:
								try:e.add_trace(Q.Candlestick(x=s,open=l['Open'].squeeze(),high=l[EJ].squeeze(),low=l[EK].squeeze(),close=l[BF].squeeze(),name='OHLC',increasing_line_color=GN,decreasing_line_color=GO,increasing_fillcolor=GN,decreasing_fillcolor=GO,line=E(width=1.6),whiskerwidth=.9),row=1,col=1)
								except g:e.add_trace(Q.Scatter(x=s,y=Ag,name=BF,line=E(color=AC,width=2)),row=1,col=1)
							else:e.add_trace(Q.Scatter(x=s,y=Ag,name=BF,line=E(color=AC,width=2)),row=1,col=1)
							for(NY,NZ,Na)in[(20,K4,'EMA20'),(50,'#FF6D00','EMA50'),(200,'#2979FF','EMA200')]:Nb=Ag.ewm(span=NY,adjust=J).mean();e.add_trace(Q.Scatter(x=s,y=Nb,name=Na,line=E(color=NZ,width=1.8)),row=1,col=1)
							IB=M(l[EJ].max());IC=M(l[EK].min());e.add_hline(y=IB,line_dash=GP,line_color=K5,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W High ₹{IB:,.2f}",annotation_position=K6,annotation_font=E(color=K5,size=13));e.add_hline(y=IC,line_dash=GP,line_color=K7,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W Low ₹{IC:,.2f}",annotation_position='bottom right',annotation_font=E(color=K7,size=13))
							if Cn:e.add_trace(Q.Scatter(x=Cn,y=I8,mode=E7,name='H-M Entry (RSI>50)',marker=E(color='lime',size=12,symbol=K8,line=E(color='white',width=1.5))),row=1,col=1)
							try:ID=l[u].squeeze();Nc=l['Open'].squeeze();Nd=l[BF].squeeze();Ne=[GN if B>=A else GO for(A,B)in zip(Nc.tolist(),Nd.tolist())];e.add_trace(Q.Bar(x=s,y=ID.tolist(),name=u,marker=E(color=Ne,line=E(width=0)),opacity=.85,showlegend=J),row=3,col=1);Nf=ID.rolling(20).mean();e.add_trace(Q.Scatter(x=s,y=Nf.tolist(),name='Vol Avg(20)',line=E(color='#616161',width=1.2,dash=DG)),row=3,col=1)
							except g:pass
							Dh=Av.reindex(Av.index);IE=H.Series(5e1,index=Av.index);Ng=Dh.where(Dh>=50,5e1);e.add_trace(Q.Scatter(x=s,y=IE.tolist(),line=E(width=0),mode=EL,showlegend=J,hoverinfo=EM),row=2,col=1);e.add_trace(Q.Scatter(x=s,y=Ng.tolist(),fill=K9,fillcolor='rgba(38,166,154,0.35)',line=E(width=0),mode=EL,showlegend=J,hoverinfo=EM),row=2,col=1);Nh=Dh.where(Dh<=50,5e1);e.add_trace(Q.Scatter(x=s,y=IE.tolist(),line=E(width=0),mode=EL,showlegend=J,hoverinfo=EM),row=2,col=1);e.add_trace(Q.Scatter(x=s,y=Nh.tolist(),fill=K9,fillcolor='rgba(239,83,80,0.35)',line=E(width=0),mode=EL,showlegend=J,hoverinfo=EM),row=2,col=1);e.add_trace(Q.Scatter(x=s,y=Av.tolist(),name='RSI(9)',line=E(color='#1976D2',width=1.5)),row=2,col=1);e.add_trace(Q.Scatter(x=s,y=F9.tolist(),name='EMA3',line=E(color='#4CAF50',width=1.5)),row=2,col=1);e.add_trace(Q.Scatter(x=s,y=FA.tolist(),name='WMA21',line=E(color='#EF5350',width=1.5)),row=2,col=1)
							if FB:e.add_trace(Q.Scatter(x=FB,y=I9,mode=E7,name='Entry (RSI panel)',showlegend=J,marker=E(color='lime',size=6,symbol=K8,line=E(color='white',width=1))),row=2,col=1)
							e.add_hline(y=70,line_dash=DG,line_color=GL,opacity=.5,row=2,col=1);e.add_hline(y=50,line_dash=GP,line_color='#888888',row=2,col=1,annotation_text='50',annotation_position='right');e.add_hline(y=30,line_dash=DG,line_color=K4,opacity=.8,row=2,col=1,annotation_text='30',annotation_position='right');e.update_layout(template=x,height=950,title=E(text=f"{G} — Ultra HD Chart (Price, EMAs, H-M, Volume)",font=E(size=12,color='#0E1117',family=EN)),margin=E(t=60,b=80,l=20,r=20),xaxis_rangeslider_visible=J,xaxis2_rangeslider_visible=J,xaxis3_rangeslider_visible=J,legend=E(orientation='h',y=-.15,x=.5,xanchor='center',yanchor='top',font=E(size=13,color=KA,family=EN)),hovermode='x unified',font=E(size=13,color=KA,family=EN),hoverlabel=E(font_size=14,font_family=EN,bgcolor='rgba(255,255,255,0.95)'),plot_bgcolor=EO,paper_bgcolor=EO,bargap=.15);e.update_xaxes(showspikes=B,spikemode='across+toaxis',spikesnap='cursor',spikethickness=1.5,spikedash='solid',spikecolor='#808495',gridcolor=KB,linecolor=GQ,tickfont=E(size=12,family=KC));e.update_yaxes(gridcolor=KB,zeroline=J,linecolor=GQ,tickfont=E(size=12,family=KC));e.update_yaxes(range=[0,100],row=2,col=1);e.update_yaxes(title_text=BK,title_font=E(size=14,weight=AP),row=1,col=1);e.update_yaxes(title_text='RSI / H-M',title_font=E(size=14,weight=AP),row=2,col=1);e.update_yaxes(title_text=u,title_font=E(size=14,weight=AP),row=3,col=1);Ni={Jt:J,'responsive':B,'toImageButtonOptions':{'format':'png','filename':f"{G}_Ultra_HD_Analysis",'height':1080,'width':1920,'scale':6},'modeBarButtonsToAdd':['drawline','drawopenpath','drawrect','eraseshape']};A.plotly_chart(e,use_container_width=B,key=f"price_ema_chart_{G}",config=Ni)
							if Cn:A.caption(f"🟢 {P(Cn)} H-M entry signal(s) — RSI(9) crossed above 50 (bottom-catch). **H-M panel:** Green fill = RSI above 50 (momentum). Red fill = RSI below 50 (pullback). For informational purposes only.")
							else:A.caption('**H-M panel:** Green fill = RSI above 50. Red fill = RSI below 50 (pullback zone). 🟢 circles = RSI(9) cross above 50 (entry). For informational purposes only.')
							X={}
							if AD!=BE:
								Di=DJ(BE)
								if not Di.empty:
									Nj=[A for A in Di.columns if not A.startswith(AV)and not A.startswith(AW)];IF=U((A for A in Nj if A.lower()in[D0,AX,Dv,Dw,D1,Dx]),D)
									if IF:
										IG=Di[Di[IF].astype(F).str.strip()==G]
										if not IG.empty:Nk=IG.iloc[0].to_dict();X={A:B for(A,B)in Nk.items()if not F(A).startswith(AV)and not F(A).startswith(AW)and F(A)!=m}
							def Y(row,primary_dict,*K):
								def B(r_data):
									J='n/a';B=r_data
									if B is D or P(B)==0:return j
									try:H=AK(B.keys())if Ay(B,E)else AK(B.index)
									except g:return j
									H=[A for A in H if not F(A).startswith(AV)and not F(A).startswith(AW)and F(A)!=m]
									for L in K:
										I=L.lower().strip()
										for G in H:
											if F(G).strip().lower()==I:
												A=B.get(G,C);A=C if A is D else F(A).strip()
												if A not in(C,A1,AN,DB,J,j):return A
										for G in H:
											if I in F(G).strip().lower():
												A=B.get(G,C);A=C if A is D else F(A).strip()
												if A not in(C,A1,AN,DB,J,j):return A
									return j
								A=B(primary_dict)
								if A==j:A=B(row)
								return A
							def IH(label,value):return f"<div style='background:var(--secondary-background-color,#F0F2F6);border:1px solid rgba(128,128,128,0.35);border-radius:6px;padding:8px 10px;min-width:150px;flex:1 1 150px;'><div style='font-size:11px;color:var(--text-color,#31333F);opacity:0.65;margin-bottom:3px;'>{label}</div><div style='font-size:14px;font-weight:700;color:var(--text-color,#0E1117);word-break:break-word;'>{value}</div></div>"
							def FG(title,fields):D=C.join(IH(A,Y(S,X,*B))for(A,B)in fields);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
						with NT:Nl=AK(l.index);B7=Q.Figure();B7.add_trace(Q.Scatter(x=Nl,y=F8,name=KD,line=E(color='#AB47BC',width=2)));B7.add_hline(y=70,line_dash=DG,line_color=GL,opacity=.6);B7.add_hline(y=30,line_dash=DG,line_color=GK,opacity=.6);B7.add_hrect(y0=45,y1=65,fillcolor=GK,opacity=.06,line_width=0,annotation_text='Ideal entry 45-65',annotation_position=K6);B7.update_layout(template=x,height=280,yaxis=E(range=[0,100]),margin=E(t=30,b=20),plot_bgcolor=EO,paper_bgcolor=EO,font=E(color='#1A1A1A'));B7.update_xaxes(gridcolor=KE);B7.update_yaxes(gridcolor=KE);A.plotly_chart(B7,use_container_width=B,key=f"rsi14_chart_{G}")
				A.markdown("<hr style='margin:16px 0 4px 0;opacity:0.25;'>",unsafe_allow_html=B)
				with A.expander(f"📋 {G} — Google Sheet Data",expanded=B):
					def Nm(title,items):D=C.join(IH(A,B)for(A,B)in items);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
					Nn='▲'if Df>=0 else'▼';No='#00A152'if Df>=0 else'#D32F2F';Nm('📊 Price Snapshot',[(KF,f"₹{AJ:,.2f} <span style='color:{No};font-size:12px;'>{Nn} {Df:+.2f}%</span>"),(Aj,f"₹{M(l[EJ].max()):,.2f}"),(Ak,f"₹{M(l[EK].min()):,.2f}"),(KD,f"{Cm:.1f}"if Cm is not D else'–')])
					with A.expander('📋 Company Price Dashboard',expanded=J):FG('🏢 Company Info',[('Company Name',[J_,K0]),(GR,[E5,G0]),(Ai,[KG,KH,E1]),('52W High Date',[Jo,'52 week high date']),('52W Low Date',[Jp,'52 week low date']),(u,[BH]),(D3,[CR])]);FG('📡 Signals & System Output',[(JE,[Jb]),('Difference from 200 DMA',['difference from 200 dma','differance from 200 dma']),('CAR Rating',['cumulative average rule (car) rating','car rating']),('Start GTT Order',[Jc,'gtt order']),(Bo,[G1]),(Bp,[G2]),(Bq,[G3]),(Br,[Jd]),(Bs,[G4])]);FG('💰 Fundamentals',[(Jl,['face value']),('Total Equity Capital',[GS]),(Jn,[G5]),('EPS',['eps']),(Jm,['ronw']),(Jj,[Fu,Fv]),(Jk,[KI,KJ]),('Pledged %',[Fw,Fx]),('D/E Ratio',[JS,'de ratio']),('Net Sales (Cr)',[E0]),('Net Profit (Cr.)',[D_]),('Reserves (Cr)',[GT]),('Total Debt (Cr)',[GU]),('Inventory (Cr)',[GV]),('Cash & Equiv (Cr)',[GW,GX,GY]),('Operating Cash Flow (Cr)',['operating cash flow']),('Trade Receivables (Cr)',[GZ]),('Trade Payables (Cr)',[Ga]),('Fixed Assets/Net PPE (Cr)',[Gb,Gc]),('Total Assets (Cr)',[Gd]),('Open (₹)',['open price','open (','open']),('High (₹)',['day high','high price','high (']),('Low (₹)',['day low','low price','low (']),('Prev Close (₹)',['prev close','previous close',Jr]),('Price Change (₹)',['price change','change (','change in price']),('% Change',['% change',D2,'change %']),('Shares Outstanding (Cr)',['shares outstanding']),('Book Value (₹/share)',['book value']),('Public %',['public %','public holding']),('FII %',['fii %','fii holding','fii']),('DII %',['dii %','dii holding','dii'])])
					def d(raw):
						if raw in(D,j,C,A1,AN):return
						try:return M(F(raw).replace(A9,C).replace('₹',C).strip())
						except(AT,Fn):return
					def y(h,alpha=.35):return f"rgba({T(h[1:3],16)},{T(h[3:5],16)},{T(h[5:7],16)},{alpha})"
					if BZ and AJ is not D:II=AJ-BZ;IJ=Q.Figure(Q.Waterfall(orientation='v',measure=['absolute','relative','total'],x=['Prev Close','Change',KF],y=[BZ,II,AJ],text=[f"₹{BZ:,.2f}",f"{II:+.2f}",f"₹{AJ:,.2f}"],textposition='outside',textfont=E(color=An,size=13),increasing=E(marker=E(color=w)),decreasing=E(marker=E(color=AY)),totals=E(marker=E(color=AC)),connector=E(line=E(color=GQ))));IJ.update_layout(title=f"📈 Price Change Bridge — {G} ({Df:+.2f}%)",template=x,height=300,showlegend=J,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IJ,use_container_width=B,key=f"waterfall_price_{G}");A.caption("Prev Close → today's Price Change → Last Close. Shown as a Waterfall, not a Sankey, since a price drop can't be a negative flow.")
					else:A.info("Prev Close / Last Close not available for this stock, so the Price Change bridge can't be built.")
					Np=Y(S,X,BH);Ah=d(Y(S,X,KG,KH,E1));C4=d(Np)
					if C4 is not D and Ah is not D and 0<=Ah<=100:FH=C4*Ah/100;IK=C4-FH;IL=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=30,thickness=18,line=E(color=Bv,width=.5),label=[f"Volume<br>{C4:,.0f} shares",f"Delivered<br>{FH:,.0f} shares ({Ah:.1f}%)",f"Intraday / Non-Delivery<br>{IK:,.0f} shares ({100-Ah:.1f}%)"],color=[Cb,w,A_]),link=E(source=[0,0],target=[1,2],value=[FH,IK],color=[y(w),y(A_)])));IL.update_layout(title=f"📦 Volume → Delivery Split — {G}",template=x,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IL,use_container_width=B,key=f"sankey_volume_{G}");A.caption('Total Volume split by % Delivery into shares actually delivered (genuine buying/holding) vs. shares traded intraday and squared off same day.')
					else:A.info("Volume / % Delivery not available for this stock, so the Volume → Delivery split can't be built.")
					if Cm is not D:IM=Q.Figure(Q.Indicator(mode=KK,value=M(Cm),number=E(font=E(color=An,size=28)),title=E(text=f"RSI(14) — {G}",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AC),steps=[E(range=[0,30],color=Js),E(range=[30,70],color='#f5f5f5'),E(range=[70,100],color=Bl)],threshold=E(line=E(color=DH,width=3),value=M(Cm)))));IM.update_layout(template=x,height=260,margin=E(t=50,b=10,l=30,r=30));A.plotly_chart(IM,use_container_width=B,key=f"gauge_rsi_{G}");A.caption("Below 30 = oversold, above 70 = overbought. A gauge, not a Sankey — RSI doesn't split into parts.")
					else:A.info('RSI(14) not available for this stock.')
					Dj=M(l[EJ].max())if not l.empty else D;Co=M(l[EK].min())if not l.empty else D
					if Dj and Co is not D and Dj>Co and AJ is not D:IN=A8(i,min(1e2,(AJ-Co)/(Dj-Co)*100));IO=Q.Figure(Q.Indicator(mode=KK,value=IN,number=E(suffix=AA,font=E(color=An,size=28)),title=E(text=f"52W Range Position — {G}<br><span style='font-size:11px'>Low ₹{Co:,.2f} · Last ₹{AJ:,.2f} · High ₹{Dj:,.2f}</span>",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AC),steps=[E(range=[0,33],color=Bl),E(range=[33,66],color=G7),E(range=[66,100],color=CV)],threshold=E(line=E(color=DH,width=3),value=IN))));IO.update_layout(template=x,height=280,margin=E(t=65,b=10,l=30,r=30));A.plotly_chart(IO,use_container_width=B,key=f"gauge_52wrange_{G}");A.caption("0% = at the 52-week low, 100% = at the 52-week high. A gauge, not a Sankey — price levels aren't a splittable quantity.")
					else:A.info('52-week High/Low/Last Close not available for this stock.')
					C5=d(Y(S,X,CR));FI=J
					if C5 is D and C4 is not D and AJ:C5=C4*AJ/1e7;FI=B
					if C5 is not D and Ah is not D and 0<=Ah<=100:FJ=C5*Ah/100;IP=C5-FJ;IQ=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=30,thickness=18,line=E(color=Bv,width=.5),label=[f"{"Est. "if FI else C}Turnover<br>₹{C5:,.2f} Cr",f"Delivered Value<br>₹{FJ:,.2f} Cr ({Ah:.1f}%)",f"Intraday Value<br>₹{IP:,.2f} Cr ({100-Ah:.1f}%)"],color=[Cb,w,A_]),link=E(source=[0,0],target=[1,2],value=[FJ,IP],color=[y(w),y(A_)])));IQ.update_layout(title=f"💵 Turnover → Delivery Split — {G}",template=x,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IQ,use_container_width=B,key=f"sankey_turnover_{G}");Nq=" Your sheet's Turnover field is blank for this stock, so this uses an estimate (Volume × Last Close) — the same fallback this app already uses elsewhere."if FI else C;A.caption(f"Turnover split by % Delivery, mirroring the Volume split above in ₹ terms.{Nq}")
					else:A.info("Turnover / % Delivery / Volume not available for this stock, so the Turnover → Delivery split can't be built.")
					C6=d(Y(S,X,G5));C7=d(Y(S,X,Fu,Fv));C8=d(Y(S,X,KI,KJ));FK=d(Y(S,X,Fw,Fx))
					if C6 is not D and C6>0 and(C7 is not D or C8 is not D):
						C7=C7 or i;C8=C8 or i;IR=A8(i,1e2-C7-C8);Cp=C6*C7/100;IS=C6*C8/100;IT=C6*IR/100;IU=[f"Market Cap<br>₹{C6:,.2f} Cr",f"Promoters<br>₹{Cp:,.2f} Cr ({C7:.1f}%)",f"Institutional<br>₹{IS:,.2f} Cr ({C8:.1f}%)",f"Public / Other<br>₹{IT:,.2f} Cr ({IR:.1f}%)"];IV=[Cb,AC,w,EP];IW=[0,0,0];IX=[1,2,3];IY=[Cp,IS,IT];IZ=[y(A)for A in[AC,w,EP]];Ia=C
						if FK is not D and Cp>0:FL=Cp*FK/100;Ib=Cp-FL;IU+=[f"Pledged (of Promoters)<br>₹{FL:,.2f} Cr ({FK:.1f}%)",f"Free / Unpledged<br>₹{Ib:,.2f} Cr"];IV+=[DH,Cy];IW+=[1,1];IX+=[4,5];IY+=[FL,Ib];IZ+=[y(DH),y(Cy)];Ia=" Promoters' holding is further split into Pledged vs Free based on Pledged %."
						Ic=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=30,thickness=18,line=E(color=Bv,width=.5),label=IU,color=IV),link=E(source=IW,target=IX,value=IY,color=IZ)));Ic.update_layout(title=f"🧾 Shareholding Pattern — Who Owns {G}",template=x,height=380,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ic,use_container_width=B,key=f"sankey_shareholding_{G}");A.caption(f'Market Cap × holding % from the Fundamentals data above. "Public / Other" absorbs whatever isn\'t reported as Promoters/Institutional (Public %, FII %, DII % show "-" for stocks where your sheet doesn\'t break those out separately).{Ia}')
					else:A.info("Market Cap / shareholding % data not available for this stock, so the Shareholding Pattern flow can't be built.")
					Ba=d(Y(S,X,E0));B8=d(Y(S,X,D_))
					if Ba is not D and B8 is not D and 0<B8<Ba:Id=Ba-B8;FM=B8/Ba*100;Ie=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=30,thickness=18,line=E(color=Bv,width=.5),label=[f"Net Sales<br>₹{Ba:,.2f} Cr (100%)",f"Net Profit<br>₹{B8:,.2f} Cr ({FM:.1f}%)",f"Total Expenses<br>₹{Id:,.2f} Cr ({100-FM:.1f}%)"],color=[AC,w,AY]),link=E(source=[0,0],target=[1,2],value=[B8,Id],color=['rgba(15,157,88,0.35)','rgba(234,67,53,0.35)'])));Ie.update_layout(title=f"💰 Revenue & Expenses Flow — {G} (Net Margin {FM:.1f}%)",template=x,height=320,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ie,use_container_width=B,key=f"sankey_{G}");A.caption('Based on Net Sales / Net Profit from the Fundamentals data above. "Total Expenses" is the remainder (Net Sales − Net Profit) — your sheet doesn\'t carry a Cost-of-Revenue/Opex breakdown, so a multi-stage flow (Gross → Operating → Net) isn\'t available for this stock.')
					elif Ba is not D and B8 is not D:A.info(f"Revenue & Expenses flow needs a normal profitable split (0 < Net Profit < Net Sales). {G} currently shows Net Sales ₹{Ba:,.2f} Cr and Net Profit ₹{B8:,.2f} Cr, which doesn't fit a simple flow diagram (e.g. a net loss).")
					else:A.info("Net Sales / Net Profit not available for this stock, so the Revenue & Expenses flow can't be built.")
					Nr=d(Y(S,X,GS));Ns=d(Y(S,X,GT));Nt=d(Y(S,X,GU));Nu=d(Y(S,X,Ga));Nv=[(KL,Nr,AC),(KM,Ns,w),(KN,Nt,AY),(KO,Nu,KP)];B9=[(B,A,C)for(B,A,C)in Nv if A is not D and A>0]
					if P(B9)>=2:If=sum(B for(A,B,A)in B9);Ig=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=30,thickness=18,line=E(color=Bv,width=.5),label=[f"Total Financing<br>₹{If:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/If*100:.1f}%)"for(B,A,C)in B9],color=[KQ]+[B for(A,A,B)in B9]),link=E(source=[0]*P(B9),target=AK(Dr(1,P(B9)+1)),value=[B for(A,B,A)in B9],color=[y(B)for(A,A,B)in B9])));Ig.update_layout(title=f"🏗️ Capital Structure — How {G} Is Financed",template=x,height=300,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ig,use_container_width=B,key=f"sankey_capstruct_{G}");A.caption('Equity Capital + Reserves + Total Debt + Trade Payables, from the Fundamentals data above.')
					else:A.info('Not enough of Total Equity Capital / Reserves / Total Debt / Trade Payables available to build a Capital Structure flow.')
					C9=d(Y(S,X,Gd));Nw=[(KR,d(Y(S,X,Gb,Gc)),KS),(KT,d(Y(S,X,GV)),A_),(KU,d(Y(S,X,GZ)),KV),(KW,d(Y(S,X,GW,GX,GY)),AC)];FN=[(B,A,C)for(B,A,C)in Nw if A is not D and A>=0]
					if C9 is not D and C9>0 and FN:
						Ih=sum(B for(A,B,A)in FN);FO=C9-Ih
						if FO>=0:CA=FN+([(KX,FO,EP)]if FO>0 else[]);Ii=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=30,thickness=18,line=E(color=Bv,width=.5),label=[f"Total Assets<br>₹{C9:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/C9*100:.1f}%)"for(B,A,C)in CA],color=[Cb]+[B for(A,A,B)in CA]),link=E(source=[0]*P(CA),target=AK(Dr(1,P(CA)+1)),value=[B for(A,B,A)in CA],color=[y(B)for(A,A,B)in CA])));Ii.update_layout(title=f"📦 Asset Deployment — Where {G}'s Assets Sit",template=x,height=340,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ii,use_container_width=B,key=f"sankey_assets_{G}");A.caption('Fixed Assets, Inventory, Trade Receivables and Cash & Equivalents from the Fundamentals data above. "Other Assets" is the gap versus reported Total Assets (e.g. intangibles, investments, or other items your sheet doesn\'t itemize).')
						else:A.info(f"{G}'s itemized asset categories (₹{Ih:,.2f} Cr) add up to more than the reported Total Assets (₹{C9:,.2f} Cr) — likely a data mismatch between sheet rows, so the Asset Deployment flow isn't shown to avoid a misleading chart.")
					else:A.info("Total Assets / asset-category data not available for this stock, so the Asset Deployment flow can't be built.")
					FP,Ij,Dk=[],[],[];CB,CC,CD,CE=[],[],[],[]
					def Bb(label,color,col_x):FP.append(label);Ij.append(color);Dk.append(col_x);return P(FP)-1
					Nx,Ny,Ik,FQ=.001,.24,.5,.999;Nz=[(KL,d(Y(S,X,GS)),AC),(KM,d(Y(S,X,GT)),w),(KN,d(Y(S,X,GU)),AY),(KO,d(Y(S,X,Ga)),KP)];FR=[(B,A,C)for(B,A,C)in Nz if A is not D and A>0];Il=P(FR)>=2;BA=D
					if Il:
						Dl=sum(B for(A,B,A)in FR);BA=Bb(f"Total Financing<br>₹{Dl:,.2f} Cr (100%)",KQ,Ny)
						for(Aw,AF,Cq)in FR:s=Bb(f"{Aw}<br>₹{AF:,.2f} Cr ({AF/Dl*100:.1f}%)",Cq,Nx);CB.append(s);CC.append(BA);CD.append(AF);CE.append(y(Cq))
					Bc=d(Y(S,X,Gd));N_=[(KR,d(Y(S,X,Gb,Gc)),KS),(KT,d(Y(S,X,GV)),A_),(KU,d(Y(S,X,GZ)),KV),(KW,d(Y(S,X,GW,GX,GY)),AC)];FS=[(B,A,C)for(B,A,C)in N_ if A is not D and A>=0];Dm=Bc is not D and Bc>0 and bool(FS)
					if Dm:O0=sum(B for(A,B,A)in FS);FT=Bc-O0;Dm=FT>=0
					if Dm:
						O1=FS+([(KX,FT,EP)]if FT>0 else[]);O2=f" ({Bc/Dl*100:.1f}%)"if BA is not D else KY;Im=Bb(f"Total Assets<br>₹{Bc:,.2f} Cr{O2}",Cb,Ik)
						if BA is not D:CB.append(BA);CC.append(Im);CD.append(Bc);CE.append(y(Cb))
						for(Aw,AF,Cq)in O1:s=Bb(f"{Aw}<br>₹{AF:,.2f} Cr ({AF/Bc*100:.1f}%)",Cq,FQ);CB.append(Im);CC.append(s);CD.append(AF);CE.append(y(Cq))
					Bd=d(Y(S,X,E0));CF=d(Y(S,X,D_));In=Bd is not D and CF is not D and 0<CF<Bd
					if In:
						Io=Bd-CF;O3=f" ({Bd/Dl*100:.1f}%)"if BA is not D else KY;FU=Bb(f"Net Sales<br>₹{Bd:,.2f} Cr{O3}",AC,Ik)
						if BA is not D:CB.append(BA);CC.append(FU);CD.append(Bd);CE.append(y(AC))
						Ip=CF/Bd*100;O4=Bb(f"Net Profit<br>₹{CF:,.2f} Cr ({Ip:.1f}%)",w,FQ);O5=Bb(f"Total Expenses<br>₹{Io:,.2f} Cr ({100-Ip:.1f}%)",AY,FQ);CB+=[FU,FU];CC+=[O4,O5];CD+=[CF,Io];CE+=[y(w),y(AY)]
					O6=sum([Il,Dm,In])
					if O6>0:
						from collections import defaultdict as Iq;Ir=Iq(T)
						for Cr in Dk:Ir[Cr]+=1
						Is=Iq(T);It=[]
						for Cr in Dk:Aw=Ir[Cr];BO=Is[Cr];Is[Cr]+=1;It.append(b((BO+.5)/Aw,4)if Aw>1 else .5)
						Iu=Q.Figure(Q.Sankey(arrangement=Bt,textfont=E(color=An,size=13,family=Bu),node=E(pad=22,thickness=18,line=E(color=Bv,width=.5),label=FP,color=Ij,x=Dk,y=It),link=E(source=CB,target=CC,value=CD,color=CE)));Iu.update_layout(title=f"💎 Combined Money Flow — {G} (Financing → Assets / Revenue, merged)",template=x,height=560,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Iu,use_container_width=B,key=f"sankey_merged_{G}");A.caption("All money-related flows merged into one chart: financing sources (Equity + Reserves + Debt + Trade Payables) feed Total Financing, which splits into two parallel paths — Total Assets (incl. Trade Receivables) and Net Sales → Net Profit / Total Expenses. It's drawn as two branches off one hub, rather than one long chain, because Total Assets and Net Sales are different kinds of totals (balance sheet vs. P&L) that don't feed into each other. Trade Payables now also appears in the 🏗️ Capital Structure chart above.")
					else:A.info('Not enough financing / assets / revenue data available for this stock to build the Combined Money Flow chart.')
	A.markdown(c);A.subheader('📊 National Live Market Analytics Portal Framework');Z=A.tabs(['🔥 Most Active','🚀 Volume Gainers','🏆 Top Gainers/Losers','⭐ 52W Boundaries','📦 Stocks Traded','⚖️ Advances/Declines','🕒 Pre-Open Market','⚡ Price Band Hitters','🗺️ Index Ticker Heatmap','🎫 IPO Tracker','⚠️ Volume Shockers','📂 Document Reports','🖋️ TV Script Engine','🔮 MunafaSutra Tickers','🎯 Dhan Asset Registry','💎 Weekly Activity Metrics','🔧 ScanX Core Screener','🚦 ScanX Live Engine','🎨 Screener Exploration','📈 IPO Chittorgarh','🏷️ IPO Watch Panel','💓 NSE Pulse','📊 Chartink Screeners','📋 Chartink Dashboard','🗾 Chartink Atlas','📚 Mahesh Kaushik','💰 EFTI Wealth','✅ Securities Available','🏛️ Corporate Filings','📉 52W Low Market'])
	def a(url,label='Open in Browser'):return f"<div style='margin-bottom:8px;'><a href='{url}' target='_blank' style='display:inline-block; background:#1976d2; color:#fff; font-size:14px; font-weight:600;padding:8px 18px; border-radius:6px; text-decoration:none;'>🌐 {label}</a><span style='font-size:12px; color:#888; margin-left:12px;'>📱 Mobile: tap button if frame is blank</span></div>"
	with Z[0]:I='https://www.nseindia.com/market-data/most-active-equities';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[1]:I='https://www.nseindia.com/market-data/volume-gainers-spurts';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[2]:I='https://www.nseindia.com/market-data/top-gainers-losers';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[3]:I='https://www.nseindia.com/market-data/52-week-high-equity-market';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[4]:I='https://www.nseindia.com/market-data/stocks-traded';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[5]:I='https://www.nseindia.com/market-data/advance';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[6]:I='https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[7]:I='https://www.nseindia.com/market-data/upper-band-hitters';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[8]:I='https://www.nseindia.com/index-tracker/NIFTY%2050';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[9]:I='https://www.nseindia.com/market-data/all-upcoming-issues-ipo';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[10]:I='https://www.moneycontrol.com/stocks/market-stats/volume-shockers-nse/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[11]:I='https://www.nseindia.com/all-reports/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[12]:I='https://www.tradingview.com/scripts/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[13]:I='https://munafasutra.com/nse/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[14]:I='https://dhan.co/all-stocks-list/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[15]:I='https://dhan.co/stocks/market/most-active-stocks-this-week/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[16]:I='https://scanx.trade/create-custom-screener';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[17]:I='https://scanx.trade/stock-screener/live-market-screener';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[18]:I='https://www.screener.in/explore/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[19]:I='https://www.chittorgarh.com/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[20]:I='https://ipowatch.in/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[21]:I='https://nsepulse.streamlit.app/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[22]:I='https://chartink.com/screeners';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[23]:I='https://chartink.com/scan_dashboard';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[24]:I='https://chartink.com/atlas';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[25]:I='https://www.maheshkaushik.com/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[26]:I='https://eftiwealth.com/';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[27]:I='https://www.nseindia.com/static/market-data/securities-available-for-trading';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[28]:I='https://www.nseindia.com/companies-listing/corporate-filings-announcements';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[29]:I='https://www.nseindia.com/market-data/52-week-low-equity-market';A.markdown(a(I),unsafe_allow_html=B);O.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	@DI
	def O7():
		y='0.00%';x='Worst -> Best';w='1 Day';e='RANK';d='📊 BF Grade';b='🔬 BF Score';a='CURRENT PRICE';W='STOCK NAME';A.markdown(c);A.markdown('### 📈 Multi-Horizon Performance Summary Matrix');z,AQ=A.columns([4,1])
		with z:f=A.radio(G8,[G9,CX,CY],horizontal=B,help=KZ,key='perf_matrix_sizing_mode')
		g=[w,'2 Day','3 Day','5 Day','7 Day','10 Day','12 Day','15 Days','20 Days','25 Days',Ge,'2 Months','3 Months','4 Months','5 Months','6 Months','7 Months','8 Months','9 Months','10 Months','11 Months',Gf,'18 Months','1.5 Years','2 Years','2.5 Years','3 Years',u];A0,A2,A3=A.columns([2,2,3])
		with A0:h=A.selectbox('🎯 Base Horizon for Performance Ranking:',g,index=0)
		with A2:A4=A.radio('排序 Sorting Order Type:',['Best -> Worst',x],index=0,horizontal=B)
		with A3:k=A.text_input('🔍 Filter stocks inside this matrix...',placeholder=Jz,key=JW)
		V={}
		for L in g:
			if L==u:
				if Bz:V[L]=Bz
				continue
			l=[L.lower(),L.lower().replace(' ',C),L.lower().replace('s',C)]
			if L==w:l.append(D2)
			for X in R:
				if AU(A in X.lower()for A in l)and AA in X.lower():V[L]=X;break
		if V:
			n=[]
			for(AR,N)in K.iterrows():
				o=F(N.get(m,C)).strip();A6=N.get(A5,C)if A5 else C;A7=f"https://charting.nseindia.com/?symbol={o}-EQ";AB=f'<a href="{A7}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{o}</a>';G={W:AB,a:A6}
				for(L,AC)in V.items():
					p=F(N.get(AC,'0')).replace(AA,C).replace(A9,C).strip()
					try:G[L]=M(p)if p not in[C,A1,AN]else i
					except AT:G[L]=i
				if BQ:
					q=F(N.get(BQ,'0')).replace(AA,C).replace(A9,C).strip()
					try:G[Ai]=M(q)if q not in[C,A1,AN]else i
					except AT:G[Ai]=i
				if BR:
					r=F(N.get(BR,C)).replace(AA,C).replace(A9,C).strip()
					try:G[BL]=M(r)if r not in[C,A1,AN]else D
					except AT:G[BL]=D
				if BU:
					s=F(N.get(BU,C)).replace(AA,C).replace(A9,C).strip()
					try:G[B1]=M(s)if s not in[C,A1,AN]else D
					except AT:G[B1]=D
				if B4:
					t=F(N.get(B4,C)).replace(A9,C).strip()
					try:G[Aj]=M(t)if t not in[C,A1,AN]else D
					except AT:G[Aj]=D
				if B5:
					v=F(N.get(B5,C)).replace(A9,C).strip()
					try:G[Ak]=M(v)if v not in[C,A1,AN]else D
					except AT:G[Ak]=D
				if Cf:G[Bo]=F(N.get(Cf,C)).strip()
				if BS:G[Bp]=F(N.get(BS,C)).strip()
				if DR:G[Bq]=F(N.get(DR,C)).strip()
				if DS:G[Br]=F(N.get(DS,C)).strip()
				if BT:G[Bs]=F(N.get(BT,C)).strip()
				AD={A:B for(A,B)in N.items()if not F(A).startswith(Bn)};AE,AF,_=DL(AD,R);G[b]=AE;G[d]=AF;n.append(G)
			Q=H.DataFrame(n)
			if k:Q=Q[Q[W].str.replace(Du,C,regex=B).str.contains(k,case=J,na=J)]
			AG=h if h in Q.columns else Q.columns[2];AH=A4==x;Q=Q.sort_values(by=AG,ascending=AH).reset_index(drop=B);Q.insert(0,e,Q.index+1);E=Q.copy()
			for L in V.keys():
				if L in E.columns:
					if L==u:E[L]=E[L].apply(lambda x:f"{T(x):,}"if H.notnull(x)else j)
					else:E[L]=E[L].apply(lambda x:f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)
			if Ai in E.columns:E[Ai]=E[Ai].apply(lambda x:f"{x:.2f}%"if H.notnull(x)else j)
			if BL in E.columns:E[BL]=E[BL].apply(lambda x:f"{x:.2f}"if H.notnull(x)else j)
			if B1 in E.columns:E[B1]=E[B1].apply(lambda x:(f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)if H.notnull(x)else j)
			if Aj in E.columns:E[Aj]=E[Aj].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else j)
			if Ak in E.columns:E[Ak]=E[Ak].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else j)
			O=EU.from_dataframe(E);O.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);O.configure_column(e,width=70,pinned=DC);O.configure_column(W,width=140,pinned=DC,cellRenderer=DV);AI=B2('\n            function(params) {\n                if (params.value === undefined || params.value === null || params.colDef.field === "Volume") return null;\n                let val = parseFloat(String(params.value).replace(/[+%,]/g, \'\'));\n                if (val > 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#e6f4ea\', \'fontWeight\': \'bold\' };\n                if (val < 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#fce8e6\', \'fontWeight\': \'bold\' };\n                return null;\n            }\n            ');AJ=B2(Ka);AK=B2("\n            function(params) {\n                let v = String(params.value);\n                if (v.includes('STRONG BUY')) return { 'backgroundColor': '#16e37f44', 'fontWeight': 'bold' };\n                if (v.includes('WATCHLIST')) return { 'backgroundColor': '#f4b40044', 'fontWeight': 'bold' };\n                if (v.includes('CAUTION')) return { 'backgroundColor': '#ff990044' };\n                return { 'backgroundColor': '#ea433544' };\n            }\n            ");AL=B2(Kb)
			for I in E.columns:
				if I in(e,):continue
				if f==CX and P(E)>0:Y=Bx(E.iloc[0][I]);Z=P(F(I));S=T(A8(Y,Z)*7+22)
				elif f==CY and P(E)>1:Y=Bx(E.iloc[1][I]);Z=P(F(I));S=T(A8(Y,Z)*7+22)
				else:AM={W:140,a:130,Ai:110,b:110,d:160,BL:100,B1:140,Aj:110,Ak:110,Bo:120,Bp:130,Bq:130,Br:130,Bs:130};S=AM.get(I,130)
				U=A8(70,min(S,90))
				if I==W:O.configure_column(I,width=S,minWidth=U,pinned=DC,cellRenderer=DV)
				elif I==a:O.configure_column(I,width=S,minWidth=U)
				elif I==b:O.configure_column(I,width=S,minWidth=U,cellStyle=AJ)
				elif I==d:O.configure_column(I,width=S,minWidth=U,cellStyle=AK)
				elif I in(Bo,Bp,Bq,Br,Bs):O.configure_column(I,width=S,minWidth=U,cellStyle=AL)
				elif I in V or I==B1:O.configure_column(I,width=S,minWidth=U,cellStyle=AI)
				else:O.configure_column(I,width=S,minWidth=U)
			O.configure_grid_options(domLayout=AO,rowHeight=38,headerHeight=45,enableCellTextSelection=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AP=O.build();ET(E,gridOptions=AP,theme=GA,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=450,width=GB,key='horizon_perf_grid')
	O7()
	@DI
	def O8():
		l='Key Reasons';k='Score (High→Low)';W='Score';A.markdown(c);A.markdown('### 🔬 Bottom Fishing Scanner — Buy from Bottom Candidates');A.caption('Stocks that are 8–15% above 52W Low, in uptrend, with high volume + strong fundamentals');o,AI=A.columns([4,1])
		with o:a=A.radio(G8,[G9,CX,CY],horizontal=B,help=KZ,key='bf_scanner_sizing_mode')
		p,q,r=A.columns([2,2,2])
		with p:X=A.slider('Minimum BF Score:',min_value=0,max_value=100,value=55,step=5,key='bf_min_score')
		with q:s=A.radio('Sort by:',[k,'Score (Low→High)'],horizontal=B,key='bf_sort')
		with r:b=A.text_input(Jy,placeholder='e.g. WIPRO',key=JX)
		L=[]
		for(AJ,d)in K.iterrows():
			E={A:B for(A,B)in d.items()if not F(A).startswith(Bn)};e,t,u=DL(E,R)
			if e>=X:
				f=F(d.get(m,C)).strip();v=E.get(A5,C)if A5 else C;g=U((A for A in R if E5 in A.lower()),D);w=E.get(g,C)if g else C;x=f"https://charting.nseindia.com/?symbol={f}-EQ";y=f'<a href="{x}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{f}</a>';Q=D
				if BQ:
					h=F(E.get(BQ,C)).replace(AA,C).replace(A9,C).strip()
					try:Q=M(h)if h not in[C,A1,AN]else D
					except AT:Q=D
				z=F(E.get(BR,C)).strip()if BR else j;A0=F(E.get(BU,C)).strip()if BU else j;A2=F(E.get(B4,C)).strip()if B4 else j;A3=F(E.get(B5,C)).strip()if B5 else j;A4=F(E.get(Cf,C)).strip()if Cf else j;A6=F(E.get(BS,C)).strip()if BS else j;A7=F(E.get(DR,C)).strip()if DR else j;AB=F(E.get(DS,C)).strip()if DS else j;AC=F(E.get(BT,C)).strip()if BT else j;L.append({n:y,W:e,GH:t,AL:v,BL:z,Ai:f"{Q:.2f}%"if Q is not D else j,B1:A0,Aj:A2,Ak:A3,Bo:A4,Bp:A6,Bq:A7,Br:AB,Bs:AC,GR:F(w)[:30],l:' | '.join(u[:3])})
		if b:L=[A for A in L if b.upper()in re.sub(Du,C,A[n]).upper()]
		L.sort(key=lambda x:x[W],reverse=s==k)
		if L:
			A.success(f"✅ Found **{P(L)}** stocks matching your bottom-fishing criteria (score ≥ {X})");I=H.DataFrame(L);N=EU.from_dataframe(I);N.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);AD=B2(Ka);AE=B2(Kb);AF={n:120,W:90,GH:160,AL:100,Ai:110,GR:200,l:400,BL:100,B1:140,Aj:110,Ak:110,Bo:120,Bp:130,Bq:130,Br:130,Bs:130}
			for G in I.columns:
				if a==CX and P(I)>0:Y=Bx(I.iloc[0][G]);Z=P(F(G));O=T(A8(Y,Z)*7+22)
				elif a==CY and P(I)>1:Y=Bx(I.iloc[1][G]);Z=P(F(G));O=T(A8(Y,Z)*7+22)
				else:O=AF.get(G,120)
				S=DC if G==n else D;V=A8(70,min(O,90))
				if G==W:N.configure_column(G,width=O,minWidth=V,pinned=S,cellStyle=AD)
				elif G==n:N.configure_column(G,width=O,minWidth=V,pinned=S,cellRenderer=DV)
				elif G in(Bo,Bp,Bq,Br,Bs):N.configure_column(G,width=O,minWidth=V,pinned=S,cellStyle=AE)
				else:N.configure_column(G,width=O,minWidth=V,pinned=S)
			N.configure_grid_options(domLayout=AO,rowHeight=40,headerHeight=45,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AG=N.build();ET(I,gridOptions=AG,theme=GA,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=400,width=GB,key='bf_scanner_grid');i=io.BytesIO()
			with H.ExcelWriter(i,engine=D9)as AH:Gr(I).to_excel(AH,index=J,sheet_name='Bottom Fishing')
			A.download_button('📥 Download BF Scanner Results',data=i.getvalue(),file_name=f"BottomFishing_{H.Timestamp.now().strftime(Bj)}.xlsx",mime=Bk)
		else:A.info(f"No stocks found with BF Score ≥ {X}. Try lowering the minimum score.")
	O8()
	if AI:
		A.markdown(c);A.markdown('### 🏆 Top 10 & Bottom 10 Performers (Daily badges)');CG=K.copy();CG[AI]=H.to_numeric(CG[AI].astype(F).str.replace(BG,C,regex=B),errors=AM);CG=CG.dropna(subset=[AI]);O9=CG.nlargest(10,AI);OA=CG.nsmallest(10,AI);Aq,Ar=A.columns(2)
		with Aq:
			Iv="<h4 style='margin-top:0px; margin-bottom:8px;'>⬆️ Top 10 (Daily)</h4>"
			for(_,Be)in O9.iterrows():
				Cs=F(Be.get(m,C)).strip();AF=Be[AI];Ct=Be.get(A5,C)if A5 else C
				try:Bf=M(F(Ct).replace(A9,C).strip());FV=M(AF);FW=Bf/(1+FV/100);FX=Bf-FW;Cu=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>+{FX:,.2f}</span>";Cv=f"₹{Bf:,.2f}"
				except:Cv=f"₹{Ct}";Cu=C
				FY=f"https://charting.nseindia.com/?symbol={Cs}-EQ";Iv+=f"<a href='{FY}' target='_blank' style='text-decoration:none;'><div style='background-color:#16e37f; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cs}: +{AF}%</span><span>{Cu}{Cv}</span></div></a>"
			A.markdown(Iv,unsafe_allow_html=B)
		with Ar:
			Iw="<h4 style='margin-top:0px; margin-bottom:8px;'>⬇️ Bottom 10 (Daily)</h4>"
			for(_,Be)in OA.iterrows():
				Cs=F(Be.get(m,C)).strip();AF=Be[AI];Ct=Be.get(A5,C)if A5 else C
				try:Bf=M(F(Ct).replace(A9,C).strip());FV=M(AF);FW=Bf/(1+FV/100);FX=Bf-FW;Cu=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>{FX:,.2f}</span>";Cv=f"₹{Bf:,.2f}"
				except:Cv=f"₹{Ct}";Cu=C
				FY=f"https://charting.nseindia.com/?symbol={Cs}-EQ";Iw+=f"<a href='{FY}' target='_blank' style='text-decoration:none;'><div style='background-color:#f39991; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cs}: {AF}%</span><span>{Cu}{Cv}</span></div></a>"
			A.markdown(Iw,unsafe_allow_html=B)
	A.markdown(c);A.markdown('### 📰 Global Market News, Alerts & Corporate Announcements');import urllib.request,urllib.parse,xml.etree.ElementTree as C3,pandas as H
	def Dn(pubdate_str):
		try:
			D=H.to_datetime(pubdate_str,utc=B);G=H.Timestamp.now(tz=BM);A=(G-D).total_seconds()
			if A<0:return AG
			if A<60:return f"{T(A)} secs ago"
			if A<3600:E=T(A/60);return f"{E} min{"s"if E!=1 else C} ago"
			if A<86400:F=T(A/3600);return f"{F} hour{"s"if F!=1 else C} ago"
			if A<172800:return f"Yesterday ({D.strftime(EC)})"
			I=T(A/86400);return f"{I} days ago ({D.strftime(EC)})"
		except g:return GI
	@A.cache_data(ttl=600)
	def OB(symbol,limit=10):
		try:
			J=f'"{symbol}" NSE AND ("52 week high" OR "52 week low" OR "upper circuit" OR "lower circuit")';K=urllib.parse.quote(J);M=f"https://news.google.com/rss/search?q={K}&hl=en-IN&gl=IN&ceid=IN:en";N=urllib.request.Request(M,headers={CZ:Ca})
			with urllib.request.urlopen(N)as O:P=O.read()
			Q=C3.fromstring(P);R=[D7,ED,CT,EE,EF,EG,EH,EI];E=[]
			for A in Q.findall(DF):
				F=A.find(A3).text
				if not AU(A in F.lower()for A in R):continue
				S=A.find(f).text;I=A.find(Am).text if A.find(Am)is not D else C
				try:G=H.to_datetime(I,utc=B)
				except g:G=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				T=H.Timestamp.now(tz=BM);U=(T-G).total_seconds()/86400
				if U<=15.:V=Dn(I);E.append({AB:f"🚨 **[ALERT]** {F}",f:S,L:V,AH:G,Kc:F})
			E.sort(key=lambda x:x[AH],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OC(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={CZ:Ca})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C3.fromstring(O);E=[];Q=[D7,ED,CT,EE,EF,EG,EH,EI,Kd,Ke]
			for A in P.findall(DF):
				G=A.find(A3).text;R=A.find(f).text;I=A.find(Am).text if A.find(Am)is not D else C;S=AU(A in G.lower()for A in Q);T=GJ if S else C;U=f"{T}{G}"
				try:F=H.to_datetime(I,utc=B)
				except g:F=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				V=H.Timestamp.now(tz=BM);W=(V-F).total_seconds()/86400
				if W<=Al:X=Dn(I);E.append({AB:U,f:R,L:X,AH:F})
			E.sort(key=lambda x:x[AH],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OD(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={CZ:Ca})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C3.fromstring(O);E=[];Q=[D7,ED,CT,EE,EF,EG,EH,EI,Kd,Ke]
			for A in P.findall(DF):
				F=A.find(A3).text;R=A.find(f).text;G=A.find(Am).text if A.find(Am)is not D else C;S=AU(A in F.lower()for A in Q);T=GJ if S else C;U=f"{T}{F}"
				try:I=H.to_datetime(G,utc=B)
				except g:I=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				V=Dn(G);E.append({AB:U,f:R,L:V,AH:I})
			E.sort(key=lambda x:x[AH],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OE(symbol,limit=6):
		try:
			I=f'"{symbol}" AND ("Regulation 30" OR "LODR" OR "Board Meeting" OR "AGM" OR "Analyst Meet" OR "Financial Results" OR "Corporate Action" OR "Dividend")';J=urllib.parse.quote(I);K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={CZ:Ca})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C3.fromstring(O);E=[]
			for A in P.findall(DF):
				Q=A.find(A3).text;R=A.find(f).text;F=A.find(Am).text if A.find(Am)is not D else C
				try:G=H.to_datetime(F,utc=B)
				except g:G=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				S=Dn(F);E.append({AB:f"📢 {Q}",f:R,L:S,AH:G})
			E.sort(key=lambda x:x[AH],reverse=B);return E[:limit]
		except g:return[]
	OF={'RELIANCE':'500325','TCS':'532540','HDFCBANK':'500180','INFY':Ki,'ICICIBANK':'532174','HINDUNILVR':'500696','SBIN':'500112','BHARTIARTL':'532454','BAJFINANCE':'500034','KOTAKBANK':'500247','LT':'500510','HCLTECH':'532281','AXISBANK':'532215','ASIANPAINT':'500820','MARUTI':'532500',Kf:Kj,'TITAN':'500114','ULTRACEMCO':'532538','ONGC':'500312','NTPC':'532555','POWERGRID':'532898','WIPRO':'507685','NESTLEIND':'500790','JSWSTEEL':'500228','TATASTEEL':'500470','TATAMOTORS':'500570','TECHM':'532755','GRASIM':'500300','ADANIENT':'512599','ADANIPORTS':'532921','COALINDIA':'533278','DIVISLAB':Kk,'DRREDDY':'500124','EICHERMOT':'505200','BAJAJFINSV':'532978','BAJAJ-AUTO':'532977','CIPLA':'500087','BRITANNIA':'500825','HEROMOTOCO':'500182',Kg:Kl,'HINDALCO':'500440','UPL':'512070','TATACONSUM':'500800','SBILIFE':'540719','HDFCLIFE':'540777','INDUSINDBK':'532187','BPCL':'500547','IOC':'530965','M&M':'500520','PIDILITIND':'500331','SIEMENS':'500550','HAVELLS':'517354','VOLTAS':'500575','AMBUJACEM':'500425','ACC':'500410','SHREECEM':'500387','RAMCOCEM':Km,Kh:Kn,'JKCEMENT':'532644','STAR':Ko,'TVSMOTOR':'532343','BOSCHLTD':'500530','MUTHOOTFIN':'533398','CHOLAFIN':'500443','BAJAJHLDNG':'500490','TORNTPHARM':Kp,'AUROPHARMA':'524208','LUPIN':'500257','BIOCON':'532523','ALKEM':'539523','IPCALAB':'530827','GLAXO':'500660','ABBOTINDIA':'500488','PFIZER':'500680','SANOFI':'500674','MCDOWELL-N':'532432','ITC':'500875','GODFRYPHLP':'500163','COLPAL':'500830','DABUR':'500096','MARICO':'531642','GODREJCP':'532424','HINDPETRO':'500104','CASTROLIND':'500870','INDIGO':'521737','INTERGLOBE':'539448','SPICEJET':'500285','IRCTC':'542830','CONCOR':'531344','ADANIGREEN':'541450','ADANITRANS':'539254','TATAPOWER':'500400','TORNTPOWER':'532779','CESC':'500084','NHPC':'533098','SJVN':'533206','PFC':'532810','RECLTD':'532955','IRFC':'543257','ZOMATO':'543320','NYKAA':'543384','PAYTM':'543396','POLICYBZR':'543390','DELHIVERY':'543529','CARTRADE':'543202','RVNL':'542649','IRCON':'541956','NBCC':'534309','HUDCO':'540530','MMTC':Kq,'MTNL':'500108','BEL':'500049','HAL':'541154','COCHINSHIP':'526235','MAZAGON':'543237','GRSE':'542351','MIDHANI':'541195','BEML':'500048','BHEL':'500103','SAIL':'500113','NMDC':'526371','MOIL':'533286','NATIONALUM':'532234','HINDZINC':'500188','VEDL':'500295','GMRINFRA':'532754','NHAI':'500253','IRB':'532947','ASHOKLEY':'500477','ESCORTS':'500495','FORCE':'517168','SML':'513275','MOTHERSON':'517334','MINDAIND':'532539','ENDURANCE':'540350','BALKRISIND':'502355','APOLLOTYRE':'500877','MRF':'500290','CEATLTD':'500878','JK TYRE':'530007','INOXWIND':'539083','SUZLON':'532667','RPOWER':'500390','JPPOWER':'532627','FEDERALBNK':'500469','IDFCFIRSTB':'539437','BANDHANBNK':'541153','RBLBANK':'540065','DCBBANK':'532772','KTKBANK':Kr,'SOUTHBANK':'532218','CANBK':'532483','BANKBARODA':'532134','UNIONBANK':'532477','INDIANB':'532814','UCOBANK':'532505','CENTRALBK':'532885','MAHABANK':'532525','J&KBANK':Kr,'PNB':'532461','IOB':'532388','BANKINDIA':'532149','DENABANK':'532121','SYNDIBANK':'532276','VIJAYABANK':'532245','ORIENTBANK':'500315','CORPBANK':'532179','ANDHRABANK':'532418','ALLAHABAD':Ks,'ALBK':Ks,'MFSL':'542299','HDFCAMC':'541530','NIPPONLIFE':'543171','UTIAMC':'543238','ABCAPITAL':'540691','ANGELONE':'543235','ICICIGI':'540716','GICRE':'540755','NIACL':'540769','STAR':Ko,'CROMPTON':'539876','ORIENTELEC':'531637','BLUESTAR':'500067','WHIRLPOOL':'500238','VGUARD':'532953','BAJAJEL':'500031','CERA':'532443','HINDWARE':'509820','HSIL':'509675','KAJARIACER':'500233','SOMANYCER':'532622','GRINDWELL':'506076','CARBORUNIV':'513375','ASTRAL':'532830','FINOLEX':'500940','SUPREMEIND':'509930','BERGER':'509480','KANSAINER':'500165','AKZOINDIA':'500710','INDIACEM':'530005','RAMCOIND':Km,Kh:Kn,'HEIDELBERG':'500292','PRISM':'500338','BIRLACORPN':'500335','ORIENTCEM':'502420','SAGCEM':'502090','STARCEMENT':'540575','JKLAKSHMI':'500380','NUVOCO':'543334','ZYDUSLIFE':'532321','TORNTPHAR':Kp,'NATCOPHAR':'524816','GRANULES':'532482','LAURUS':Kt,'STRIDES':'532531','AJANTPHAR':'532331','CAPLIPOINT':'539266','DIVI':Kk,Kf:Kj,'GLAND':'543245','SEQUENT':'543225','METROPOLIS':'542650','DRLAL':'532259','THYROCARE':'539871','KRSNAA':'543328','VIJAYA':'532542','MAXHEALTH':'543220','KIMS':'543308','ASTER':'540975','FORTIS':'532843','NHOSPIT':'532526',Kg:Kl,'NARAYANA':'539551','YATHARTH':'544120','RAINBOW':'543524','SUVENPHAR':'530239','LAURUSLABS':Kt,'SOLARA':'541540','SHILPAMED':'530879','PERSISTENT':'533179','MINDTREE':'532819','MPHASIS':'526299','HEXAWARE':'532861','NIIT':'500304','KPIT':'542651','LTTS':'540115','COFORGE':'532541','ZENSAR':'504067','RAMSYSTEMS':'532370','MASTEK':'523704','SASKEN':'532663','TATAELXSI':'500408','CYIENT':'532175','SONATSOFTW':'532221','TANLA':'532790','LTIM':'540005','INFY':Ki,'ROUTE':'543228','BSOFT':'526301','NEWGEN':'540900','INTELLECT':'538835','NUCLEUS':'531209','NELCO':'504112','DELTACORP':'532840','WONDERLA':'538268','MAHINDCIE':'532756','STARHLTH':'543412','NAUKRI':'532777','JUSTDIAL':'535648','MATRIMONY':'539846','MAKEMYTRIP':Kq,'IXIGO':'544229','RATEGAIN':'543417','TEAMLEASE':'539658','QUESS':'539978','SIS':'540673','SECURKLOUD':'539963','HAPPYFORGE':'543532','KALYANKJIL':'543278','SENCO':'543456','THANGAMAYL':'531509','TRIBHOVAND':'512415','PC JEWELLER':'534809','RAJESHEXPO':'531500'}
	@A.cache_data(ttl=600)
	def OG(bse_code,days_back=90):
		L='SUBCATNAME';A={Gg:[],Gh:[],Gi:[],Gj:[],EQ:[]}
		try:
			import datetime as F;G=F.date.today();M=G-F.timedelta(days=days_back);N=M.strftime(Bj);O=G.strftime(Bj);P=f"https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w?pageno=1&strCat=-1&strPrevDate={N}&strScrip={bse_code}&strSearch=P&strToDate={O}&strType=C&subcategory=-1";Q={CZ:Ca,'Referer':'https://www.bseindia.com/','Accept':'application/json'};R=urllib.request.Request(P,headers=Q)
			with urllib.request.urlopen(R,timeout=8)as S:T=ES.loads(S.read())
			for B in(T.get('Table')or[])[:30]:
				U=B.get('HEADLINE',C)or B.get(L,C);I=B.get('NEWS_DT',C)or B.get('DT_TM',C);J=B.get('NEWSID',C);V=f"https://www.bseindia.com/xml-data/corpfiling/AttachLive/{J}.pdf"if J else C
				try:K=H.to_datetime(I).strftime(EC)
				except g:K=I[:10]
				E=(B.get(L)or C).lower();D={A3:U,f:V,BJ:K}
				if AU(A in E for A in['annual report','annual rep']):A[Gh].append(D)
				elif AU(A in E for A in['credit rat','rating']):A[Gi].append(D)
				elif AU(A in E for A in['concall','con call','earnings call','analyst']):A[Gj].append(D)
				elif AU(A in E for A in['investor presentation','presentation',EQ]):A[EQ].append(D)
				else:A[Gg].append(D)
		except g:pass
		return A
try:
	CH=K[m].dropna().unique()
	if P(CH)>0:
		OH,OI,OJ,OK,OL,OM,ON=A.tabs(['🚨 Latest Alerts Timeline','🏢 Alerts by Stock','📰 Smart News Engine (1 Day)','📰 Smart News Engine (All News)','📢 Corporate Announcements','📢 DOCUMENTS HUB','📜 Rules']);Cw=[];Ix=CH[:30]
		with A.spinner('Scanning Top 30 stocks for Circuit & 52-Week Breakouts (15 Days)...'):
			for G in Ix:
				z=F(G).strip();BB=OB(z,limit=15)
				for Aw in BB:Aw[AX]=z;Cw.append(Aw)
		OO={A[AX]for A in Cw};Iy={A[AX]for A in Cw if Aa in A[L]or Ab in A[L]or Ac in A[L]or AG in A[L]}
		def OP(sym):
			A=sym
			if A in Iy:B,C,D=AZ,'#003300','#0fbf62'
			elif A in OO:B,C,D='#1a7a45',C_,'#145e34'
			else:B,C,D='#444',C_,'#333'
			return f"<span style='background:{B}; color:{C}; padding:2px 9px; border-radius:5px; font-weight:700; font-size:0.82em; border:1px solid {D}; white-space:nowrap;'>⚡ {A}</span>"
		with OH:
			OQ,OR,OS=A.columns([2,1,1]);Iz=OQ.text_input('🔍 Search Alerts:',placeholder='e.g. ICICIBANK, circuit...',key='global_news_search');I_=OR.selectbox('⏳ Time Filter:',['All (Up to 15 Days)',Ku,Kv],key='global_news_time');OT=OS.radio('↕️ Sort By Time:',[Kw,'Oldest First'],horizontal=B,key='global_news_sort');Ax=Cw.copy()
			if Iz:J0=Iz.lower();Ax=[A for A in Ax if J0 in A[AX].lower()or J0 in A[Kc].lower()]
			if I_==Kv:Ax=[A for A in Ax if Aa in A[L]or Ab in A[L]or Ac in A[L]or AG in A[L]]
			elif I_==Ku:OU=H.Timestamp.now(tz=BM);Ax=[A for A in Ax if(OU-A[AH]).total_seconds()/86400<=7.]
			Ax.sort(key=lambda x:x[AH],reverse=OT==Kw);A.markdown(CW,unsafe_allow_html=B)
			if Ax:
				for N in Ax:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;OV=OP(N[AX]);A.markdown(f"- {OV}&nbsp; <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.4em 0; opacity: 0.15;'>",unsafe_allow_html=B)
			else:A.info('No circuit or 52-week alerts match your search or filter criteria.')
		with OI:
			OW=A.columns(2);FZ=0
			for z in[F(A).strip()for A in Ix]:
				Do=[A for A in Cw if A[AX]==z];Do.sort(key=lambda x:x[AH],reverse=B)
				if Do:
					with OW[FZ%2]:
						OX='🟢'if z in Iy else'🟡'
						with A.expander(f"{OX} {z} Action Alerts (0 Sec to 15 Days)",expanded=B):
							OY=Do[:3];Fa=Do[3:]
							for N in OY:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fa:
								with A.expander(f"🔽 Show {P(Fa)} more older alerts",expanded=J):
									for N in Fa:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					FZ+=1
			if FZ==0:A.info('No circuit breakouts or 52-week boundary alerts for the currently filtered stocks in the last 15 days.')
		with OJ:
			A.markdown('### Latest News & Action Alerts (Past 24 Hours)');OZ=A.columns(2);Fb=0
			for Cx in CH[:10]:
				z=F(Cx).strip();BB=OC(z,limit=5)
				if BB:
					with OZ[Fb%2]:
						with A.expander(f"📰 {z} News Feed (0 Sec to 1 Day)",expanded=B):
							for N in BB:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fb+=1
			if Fb==0:A.info('No general news found for the currently filtered stocks in the last 24 hours.')
		with OK:
			A.markdown('### Latest News & Action Alerts (All Time)');Oa=A.columns(2);Fc=0
			for Cx in CH[:10]:
				z=F(Cx).strip();BB=OD(z,limit=6)
				if BB:
					with Oa[Fc%2]:
						with A.expander(f"📰 {z} News Feed (All News)",expanded=B):
							Ob=BB[:3];Fd=BB[3:]
							for N in Ob:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fd:
								with A.expander(f"🔽 Show {P(Fd)} more articles",expanded=J):
									for N in Fd:h=Aa in N[L]or Ab in N[L]or Ac in N[L]or AG in N[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fc+=1
			if Fc==0:A.info('No general news found for the currently filtered stocks.')
		with OL:
			A.markdown('### 📢 Official Exchange Filings & Corporate Announcements');A.markdown("<span style='font-size: 0.9em; color: gray;'>Tracks Regulation 30, LODR, Board Meetings, AGMs, and Analyst Meets.</span>",unsafe_allow_html=B);A.markdown(CW,unsafe_allow_html=B);Oc=A.columns(2);Fe=0
			for Cx in CH[:15]:
				z=F(Cx).strip();Ff=OE(z,limit=7)
				if Ff:
					with Oc[Fe%2]:
						with A.expander(f"📢 {z} Filings & Announcements",expanded=B):
							Od=Ff[:3];Fg=Ff[3:]
							for A0 in Od:h=Aa in A0[L]or Ab in A0[L]or Ac in A0[L]or AG in A0[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{A0[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A0[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {A0[L]}</span>",unsafe_allow_html=B)
							if Fg:
								with A.expander(f"🔽 Show {P(Fg)} more filings",expanded=J):
									for A0 in Fg:h=Aa in A0[L]or Ab in A0[L]or Ac in A0[L]or AG in A0[L];q=AZ if h else B0;r=AP if h else AO;A.markdown(f"- <a href='{A0[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A0[AB]}</a> <span style='color: {q}; font-weight: {r}; font-size: 0.85em;'>— 🕒 {A0[L]}</span>",unsafe_allow_html=B)
					Fe+=1
			if Fe==0:A.info('No recent corporate filings or official announcements found for the filtered stocks.')
		with OM:
			A.markdown('### 📄 Documents Hub — Announcements · Annual Reports · Credit Ratings · Concalls · PPT · REC');A.markdown("<span style='font-size:0.88em; color:#888;'>Live BSE India filings (public API, no key needed). Annual Reports & Concalls also link to Screener.in.</span>",unsafe_allow_html=B);A.markdown(CW,unsafe_allow_html=B);Oe,Of,Og=A.columns([3,1.2,1.2])
			with Oe:J1=[F(A).strip()for A in CH[:60]];J2=A.multiselect('🔍 Stocks to view:',options=J1,default=J1[:4],key='doc_hub_stocks_v2')
			with Of:Oh=A.selectbox('📅 Date range:',[Ge,Kx,Ky,Gf],index=1,key='doc_days_v2')
			with Og:J3=A.selectbox('📋 Rows per section:',[3,5,8,12],index=1,key='doc_limit_v2')
			Oi={Ge:30,Kx:90,Ky:180,Gf:365};Oj=Oi[Oh]
			if not J2:A.info('Select at least one stock above to view its documents.')
			else:
				for o in J2:
					t=OF.get(o.upper(),C)
					with A.expander(f"📁  {o}   {"· BSE "+t if t else"· BSE code not mapped — Screener links shown"}",expanded=B):
						Fh="<div style='display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;'>";Ok=[('📢 BSE Announcements',f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={t}"if t else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}",Kz,K_),('📑 Annual Reports',f"https://www.screener.in/company/{o}/",CV,L0),('⭐ Credit Ratings',f"https://www.screener.in/company/{o}/",G7,'#f57f17'),('🎙️ Concalls',f"https://www.screener.in/company/{o}/",'#fce4ec',DH),('📊 Investor PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={t}"if t else f"https://www.screener.in/company/{o}/",L1,L2),('🏛️ NSE Filings',f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}",'#e0f7fa','#00695c'),('📈 Screener',f"https://www.screener.in/company/{o}/",'#fffde7',A_)]
						for(Fi,Fj,Fk,Fl)in Ok:Fh+=f"<a href='{Fj}' target='_blank' style='background:{Fk}; color:{Fl}; padding:5px 12px; border-radius:6px; font-size:0.78em; font-weight:600; text-decoration:none; white-space:nowrap;'>{Fi}</a>"
						Fh+=Cz;A.markdown(Fh,unsafe_allow_html=B);CI={}
						if t:
							with A.spinner(f"Fetching BSE filings for {o}…"):CI=OG(t,days_back=Oj)
						Ol,Om,On,Oo=A.columns([3,2,2,3])
						with Ol:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #5c6bc0; padding-bottom:4px; color:#5c6bc0;'>📢 Announcements</p>",unsafe_allow_html=B);J4=CI.get(Gg,[])
							if J4:
								Op,Oq=A.tabs([GI,'All ↗'])
								with Op:
									for CJ in J4[:J3]:BC=CJ[A3][:85]+'…'if P(CJ[A3])>85 else CJ[A3];Bg=f"<a href='{CJ[f]}' target='_blank' style='color:#5c6bc0; text-decoration:none;'>{BC}</a>"if CJ[f]else f"<span>{BC}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:6px; border-left:3px solid #c5cae9; padding-left:6px;'>{Bg}<br><span style='color:#aaa; font-size:0.85em;'>{CJ[BJ]}</span></div>",unsafe_allow_html=B)
								with Oq:Or=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={t}"if t else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}";A.markdown(f"<a href='{Or}' target='_blank' style='color:#5c6bc0; font-size:0.85em;'>🔗 Open full announcements page →</a>",unsafe_allow_html=B)
							else:Os=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={t}"if t else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}";A.markdown(f"<a href='{Os}' target='_blank' style='color:#5c6bc0; font-size:0.83em;'>🔗 View on {"BSE"if t else"NSE"} →</a>",unsafe_allow_html=B);A.caption('No announcements in selected date range.')
						with Om:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #43a047; padding-bottom:4px; color:#43a047;'>📑 Annual Reports</p>",unsafe_allow_html=B);J5=CI.get(Gh,[])
							if J5:
								for Dp in J5[:6]:J6=Dp[BJ][:4]if Dp[BJ]else'Report';Bg=f"<a href='{Dp[f]}' target='_blank' style='color:#43a047; text-decoration:none;'>📄 Annual Report {J6}</a>"if Dp[f]else f"<span>📄 Annual Report {J6}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px;'>{Bg}</div>",unsafe_allow_html=B)
							else:
								if t:A.markdown(f"<a href='https://www.bseindia.com/AnnualReports.html?scripcd={t}' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 BSE Annual Reports →</a>",unsafe_allow_html=B)
								A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 View on Screener →</a>",unsafe_allow_html=B);A.caption('Not found in selected range — try 1 Year.')
						with On:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #f57f17; padding-bottom:4px; color:#f57f17;'>⭐ Credit Ratings</p>",unsafe_allow_html=B);J7=CI.get(Gi,[])
							if J7:
								for CK in J7[:4]:BC=CK[A3][:70]+'…'if P(CK[A3])>70 else CK[A3];Bg=f"<a href='{CK[f]}' target='_blank' style='color:#f57f17; text-decoration:none;'>{BC}</a>"if CK[f]else f"<span>{BC}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffe0b2; padding-left:6px;'>{Bg}<br><span style='color:#aaa; font-size:0.85em;'>{CK[BJ]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#f57f17; font-size:0.83em;'>⭐ Ratings on Screener →</a>",unsafe_allow_html=B);A.markdown("<div style='font-size:0.78em; margin-top:8px; color:#888;'><a href='https://www.careratings.com' target='_blank' style='color:#888;'>CARE</a> · <a href='https://www.icra.in' target='_blank' style='color:#888;'>ICRA</a> · <a href='https://www.crisil.com' target='_blank' style='color:#888;'>CRISIL</a> · <a href='https://www.infomerics.com' target='_blank' style='color:#888;'>Infomerics</a></div>",unsafe_allow_html=B);A.caption('Not found via BSE — check links above.')
						with Oo:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #e53935; padding-bottom:4px; color:#e53935;'>🎙️ Concalls &amp; Investor Docs</p>",unsafe_allow_html=B);Ot=CI.get(Gj,[]);J8=CI.get(EQ,[]);J9=J8+Ot
							if J9:
								for Bh in J9[:J3]:Ou=Bh in J8;JA='📊'if Ou else'🎙️';BC=Bh[A3][:70]+'…'if P(Bh[A3])>70 else Bh[A3];Bg=f"<a href='{Bh[f]}' target='_blank' style='color:#e53935; text-decoration:none;'>{JA} {BC}</a>"if Bh[f]else f"<span>{JA} {BC}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffcdd2; padding-left:6px;'>{Bg}<br><span style='color:#aaa; font-size:0.85em;'>{Bh[BJ]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#e53935; font-size:0.83em;'>🎙️ Concalls on Screener →</a>",unsafe_allow_html=B);A.caption('No concalls/PPT in selected date range.')
							A.markdown(CW,unsafe_allow_html=B);Fm="<div style='display:flex; gap:6px; flex-wrap:wrap;'>";Ov=[('📝 Transcript',f"https://www.screener.in/company/{o}/",Kz,K_),('🤖 AI Summary',f"https://www.screener.in/company/{o}/",CV,L0),('📊 PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={t}"if t else f"https://www.screener.in/company/{o}/",L1,L2),('▶️ REC',f"https://www.youtube.com/results?search_query={o}+concall+earnings",Bl,DA)]
							for(Fi,Fj,Fk,Fl)in Ov:Fm+=f"<a href='{Fj}' target='_blank' style='background:{Fk}; color:{Fl}; padding:3px 10px; border-radius:4px; font-size:0.76em; font-weight:600; text-decoration:none;'>{Fi}</a>"
							Fm+=Cz;A.markdown(Fm,unsafe_allow_html=B)
		with ON:A.markdown('### 📜 Trading Rules');A.markdown("<span style='font-size:0.88em; color:#888;'>Edit the <code>TRADING_RULES_LIBRARY</code> constant near the top of the .py file to change anything shown below — same pattern as the AI Prompt Library &amp; Pine Script Custom Rules Library.</span>",unsafe_allow_html=B);A.markdown(CW,unsafe_allow_html=B);A.markdown(LA)
	else:A.info('No stocks currently filtered to check.')
except g as BY:A.error(f"⚠️ Could not load the News Engine. Error details: {BY}")
else:A.warning('No data loaded. Check sheet sharing and secrets.')
