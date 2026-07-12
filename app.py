LS='#6a1b9a'
LR='#f3e5f5'
LQ='#2e7d32'
LP='#3949ab'
LO='#e8eaf6'
LN='180 Days'
LM='90 Days'
LL='Newest First'
LK='Today Only'
LJ='Past 7 Days'
LI='540222'
LH='532480'
LG='532209'
LF='513377'
LE='500420'
LD='540175'
LC='502525'
LB='500260'
LA='508869'
L9='532488'
L8='524715'
L7='500209'
L6='DALMIA'
L5='APOLLOHOSP'
L4='SUNPHARMA'
L3='lower limit'
L2='upper limit'
L1='title_raw'
L0="\n            function(params) {\n                let v = String(params.value).toLowerCase();\n                if (v.includes('strong uptrend') || v.includes('bullish') || v.includes('strong buy')) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (v.includes('uptrend') || v.includes('buy') || v.includes('high') || v.includes('yes')) return { 'backgroundColor': '#a5d6a733', 'color': '#000' };\n                if (v.includes('sideways') || v.includes('watch') || v.includes('normal')) return { 'backgroundColor': '#f4b40033', 'color': '#000' };\n                if (v.includes('bearish') || v.includes('avoid') || v.includes('low') || v.includes('downtrend')) return { 'backgroundColor': '#ea433533', 'color': '#000' };\n                return null;\n            }\n            "
K_="\n            function(params) {\n                let val = parseFloat(params.value);\n                if (val >= 75) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 55) return { 'backgroundColor': '#f4b40033', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 35) return { 'backgroundColor': '#ff990033', 'color': '#000' };\n                return { 'backgroundColor': '#ea433533', 'color': '#000' };\n            }\n            "
Kz='Automatically adjust column widths based on text length of the selected row.'
Ky='gauge+number'
Kx=' (100%)'
Kw='Other Assets (unspecified)'
Kv='Cash & Equivalents'
Ku='#00897b'
Kt='Trade Receivables'
Ks='Inventory'
Kr='#5e35b1'
Kq='Fixed Assets / Net PPE'
Kp='#8d6e63'
Ko='Trade Payables'
Kn='Total Debt'
Km='Reserves'
Kl='Equity Capital'
Kk='institutional'
Kj='institutional %'
Ki='delivery %'
Kh='% delivery'
Kg='Last Close'
Kf='rgba(0,0,0,0.08)'
Ke='RSI(14)'
Kd='system-ui, sans-serif'
Kc='rgba(0,0,0,0.06)'
Kb='#31333F'
Ka='tonexty'
KZ='circle'
KY='#EF6C00'
KX='top right'
KW='#7C3AED'
KV='#FFD600'
KU='Candle'
KT='%d %b %Y %H:%M'
KS='⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.'
KR='stock name'
KQ='company name'
KP='Type symbol name...'
KO='Search symbol:'
KN='%{customdata}: %{y:.2f}%<extra></extra>'
KM='% Above 52W Low'
KL='% Below 52W High'
KK='#AB47BC'
KJ='% Change'
KI='displaylogo'
KH='#e3f2fd'
KG='close price'
KF='%Y%m%d_%H%M'
KE='52w low date'
KD='52w high date'
KC='Market Cap'
KB='RONW %'
KA='Face Value'
K9='Institutional %'
K8='Promoters %'
K7='50 DMA < 200 DMA'
K6='50 DMA > 200 DMA'
K5='50 DMA > 100 DMA > 200 DMA'
K4='50 DMA < 100 DMA < 200 DMA'
K3='All (No Filter)'
K2='macd crossover'
K1='start gtt order'
K0='output'
J_='🎨 Custom Hex: '
Jz='#ff9900'
Jy='#f4b400'
Jx='bf_search'
Jw='perf_matrix_search'
Jv='main_matrix_search'
Ju='search_query'
Jt='50 dma'
Js='d/e ratio'
Jr='52w low'
Jq='vol_val'
Jp='official nse'
Jo='market smith'
Jn='chartlink'
Jm='zerodha'
Jl='screener'
Jk='history data'
Jj='trading view'
Ji='1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU'
Jh='https://www.googleapis.com/auth/drive'
Jg='https://spreadsheets.google.com/feeds'
Jf="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
Je='Output'
Jd='Price %'
Jc='GROQ_API_KEY'
Jb='GEMINI_API_KEY'
Gy='concalls'
Gx='credit_ratings'
Gw='annual_reports'
Gv='announcements'
Gu='1 Year'
Gt='30 Days'
Gs='total assets'
Gr='net ppe'
Gq='fixed assets'
Gp='trade payables'
Go='trade receivables'
Gn='cash equivalent'
Gm='cash and equiv'
Gl='cash & equiv'
Gk='inventory'
Gj='total debt'
Gi='reserves'
Gh='total equity capital'
Gg='Sector'
Gf='rgba(0,0,0,0.3)'
Ge='dash'
Gd='#FF5252'
Gc='#00E676'
Gb='type'
Ga='🚨 **[ALERT]** '
GZ='Recent'
GY='Grade'
GX='Strategy'
GW='% Gain'
GV='Target'
GU='last_pine_result'
GT='last_ai_result'
GS='100%'
GR='streamlit'
GQ='Default'
GP='📏 Column Width Adjustment:'
GO='No % change column detected.'
GN='Stocks'
GM='#fff8e1'
GL='#1b5e20'
GK='market cap'
GJ='RSI'
GI='buy signal'
GH='trend'
GG='breakout signal'
GF='volume trend'
GE='industry'
GD='52w_low'
GC='52w_high'
GB='Watchlist'
GA='pledged'
G9='pledged %'
G8='promoter'
G7='promoters %'
G6='200 dma'
G5='#ef5350'
G4='Error'
G3='Loading...'
G2='⚡ Groq (Fast)'
G1=getattr
G0=TypeError
Ee='ppt'
Ed='#9e9e9e'
Ec='#FFFFFF'
Eb='system-ui, -apple-system, sans-serif'
Ea='skip'
EZ='lines'
EY='Low'
EX='High'
EW='locked in circuit'
EV='hits circuit'
EU='lower circuit'
ET='upper circuit'
ES='52-week low'
ER='52-week high'
EQ='%d %b %Y'
EP='Use Case'
EO='% Risk'
EN='Type'
EM='model'
EL='markers'
EK='#5c6bc0'
EJ='Change %'
EI='#D50000'
EH='#00C853'
EG='52'
EF='sector'
EE='atr_approx'
ED='Added On'
EC='BF Grade'
EB='delivery'
EA='net sales'
E9='net profit'
E8='Pct_Change'
E7='value'
E6='stock'
E5='stock symbol'
E4='ticker'
E3='<[^>]*>'
E2='gcp_service_account'
E1='No Data'
E0=range
D_=enumerate
DO='#c62828'
DN='dot'
DM='.//item'
DL='result'
DK='sym'
DJ='left'
DI='N/A'
DH='#b71c1c'
DG='openpyxl'
DF='trail_sl_50dma'
DE='52 week high'
DD='added'
DC='BF Score'
DB='Note'
DA='Turnover'
D9='price %'
D8='id'
D7='nse code'
D6='#ffffff'
D5='</div>'
D4='#66bb6a'
Cf='#37474f'
Ce='Mozilla/5.0'
Cd='User-Agent'
Cc='✅✅ Fit to Row 2'
Cb='✅ Fit to Row 1'
Ca='<br>'
CZ='#e8f5e9'
CY='bf_score'
CX='52 week low'
CW='Value'
CV='turnover'
CU='%Y-%m-%d %H:%M:%S'
CT='-%'
CS='+%'
CR='Diff @ 200 DMA'
CQ='Final List 2'
CP='Final List'
By='rgba(0,0,0,0.2)'
Bx='Arial Black, Arial, sans-serif'
Bw='snap'
Bv='Buy Signal'
Bu='MACD Crossover'
Bt='Trend'
Bs='Breakout Signal'
Br='Volume Trend'
Bq='_'
Bp='📱 If frame is blank on mobile, tap the link above to open directly.'
Bo='#ffebee'
Bn='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
Bm='%Y%m%d'
Bl='bf_grade'
BR='UTC'
BQ='RSI (14)'
BP='Price (₹)'
BO='h'
BN='date'
BM='note'
BL='volume'
BK='[%,]'
BJ='Close'
BI='NSE Fundamentals'
BH='Top 250 Stocks'
B3='Diff. from 200 DMA'
B2='gray'
B1='price'
B0=isinstance
Ap='#0a1758'
Ao='pubDate'
An='#f9a825'
Am=1.
Al='52W Low'
Ak='52W High'
Ae='sec'
Ad='hour'
Ac='min'
Ab='#16e37f'
Aa='symbol'
AZ='_txt_'
AY='_bg_'
AX=any
AW=ValueError
AS='bold'
AR='normal'
AQ='None'
AP='coerce'
AO='CMP'
AN='% Delivery'
AM=list
AJ='timestamp'
AI='Just now'
AH='#ea4335'
AE='#1565C0'
AD='display_title'
AC='%'
AB=','
AA=max
A5='title'
A4='cmp'
A0='nan'
z='change'
u='#0f9d58'
r='Volume'
p='_raw_symbol_'
l='-'
k='plotly_white'
j=.0
h=Exception
g='link'
f='Symbol'
c='---'
b=round
U=next
T=int
Q=len
N=float
M='time_ago'
J=False
F=str
E=None
D=dict
C=''
B=True
import streamlit as A,pandas as G,numpy as A6,gspread as Ef
from google.oauth2.service_account import Credentials as Gz
from google.auth.transport.requests import AuthorizedSession as LT
import json as Eg,urllib.parse
from datetime import datetime as m
from st_aggrid import AgGrid as Eh,GridOptionsBuilder as Ei,JsCode as B4
from st_aggrid.shared import GridUpdateMode as LU
import streamlit.components.v1 as P,re,io,google.generativeai as G_,plotly.graph_objects as K
from plotly.subplots import make_subplots as LV
A.set_page_config(page_title='Top 250 NSE Stock-Volume Breakout Dashboard',layout='wide',page_icon='📊')
if hasattr(A,'fragment'):DP=A.fragment
elif hasattr(A,'experimental_fragment'):DP=A.experimental_fragment
else:
	def DP(func=E,**B):
		if func is not E:return func
		def A(f):return f
		return A
A.markdown('\n<style>\n    /* Force EVERY tab-bar container to wrap onto multiple lines instead of\n       staying on one scrollable line. Multiple selector variants are used\n       (data-baseweb, role, and Streamlit\'s own class) because Streamlit\'s\n       internal DOM/class names have changed across versions. */\n    div[data-testid="stTabs"],\n    div[data-testid="stTabs"] > div,\n    .stTabs,\n    .stTabs > div {\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        max-width: 100% !important;\n    }\n\n    div[data-baseweb="tab-list"],\n    div[role="tablist"] {\n        display: flex !important;\n        flex-wrap: wrap !important;\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        white-space: normal !important;\n        row-gap: 4px !important;\n        column-gap: 6px !important;\n        height: auto !important;\n        max-width: 100% !important;\n        width: 100% !important;\n        scrollbar-width: none !important;\n    }\n    div[data-baseweb="tab-list"]::-webkit-scrollbar {\n        display: none !important;\n    }\n\n    /* Each tab button: allow shrinking/wrapping instead of forcing one line */\n    button[data-baseweb="tab"],\n    div[role="tablist"] > button,\n    div[role="tablist"] [role="tab"] {\n        flex: 0 0 auto !important;\n        white-space: normal !important;\n        margin-top: 1px !important;\n        margin-bottom: 1px !important;\n        padding-top: 6px !important;\n        padding-bottom: 6px !important;\n        height: auto !important;\n    }\n\n    /* Hide the "‹ ›" scroll-arrow buttons Streamlit shows when a tab bar overflows */\n    button[data-testid="stTabsScrollButton"],\n    div[data-baseweb="tab-list"] ~ button,\n    div[data-baseweb="tab-list"] + button,\n    button[kind="tabScroll"],\n    button[aria-label*="scroll" i] {\n        display: none !important;\n    }\n\n    div[data-baseweb="tab-highlight"] {\n        display: none !important;\n    }\n    div[data-baseweb="tab"][aria-selected="true"],\n    [role="tab"][aria-selected="true"] {\n        background-color: rgba(31, 119, 180, 0.1) !important;\n        border-radius: 5px !important;\n        border-bottom: 2px solid #1f77b4 !important;\n    }\n</style>\n',unsafe_allow_html=B)
Cg=J
BS=J
if Jb in A.secrets:G_.configure(api_key=A.secrets[Jb]);Cg=B
if Jc in A.secrets:
	try:from groq import Groq as LW;LX=LW(api_key=A.secrets[Jc]);BS=B
	except ImportError:BS=J
Ej=Cg or BS
def Ek(prompt,model_choice):
	A=prompt
	if model_choice==G2 and BS:B=LX.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{'role':'user','content':A}],max_tokens=2048);return B.choices[0].message.content
	elif Cg:C=G_.GenerativeModel('gemini-2.5-flash');return C.generate_content(A).text
	else:raise RuntimeError('No AI model is configured. Add GEMINI_API_KEY or GROQ_API_KEY to secrets.')
def El(key_suffix=C):
	D='🧠 Gemini';C,E=[],0
	if BS:C.append(G2)
	if Cg:C.append(D)
	if not C:C=[G2,D]
	return A.radio('🤖 AI Model:',C,index=0,horizontal=B,key=f"ai_model_sel_{key_suffix}")
LY=['Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}. Also give me all other details and calculate if this company is profitable or not.','Analyze the 52-week high and low data for {sym}. Is the stock closer to its peak or bottom? What does this imply for entry or exit timing? Identify the ideal buy zone.','Examine the 50 DMA, 100 DMA, and 200 DMA data for {sym}. Is the stock in a bullish crossover, bearish zone, or consolidation phase? Explain the trend strength and momentum.','Using the volume data for {sym}, identify if there is unusual volume activity. Does the current volume indicate institutional buying, selling, or accumulation? What does it signal?','Evaluate the full fundamentals of {sym} — EPS, RONW%, D/E ratio, Net Profit (Cr.), Book Value, and Market Cap. Is this company financially healthy and worth long-term investment?','What is the risk profile of {sym} based on its Pledged %, Promoters Holding %, Institutional Holding %, and Debt-to-Equity ratio? Should a retail investor be cautious right now?',"Compare {sym}'s current CMP vs its 200 DMA. Is the stock overbought, oversold, or fairly valued based on the Difference from 200 DMA metric? What is the ideal risk-reward entry zone?",'Give a complete Buy / Hold / Sell recommendation for {sym} using all available technical and fundamental data. Include specific price targets, support levels, and a stop-loss level.','Based on the CAR Rating and Output signal for {sym}, what is the system suggesting? Does the historical price action and current data support this signal? How reliable is it?',"Summarize {sym}'s sector positioning, market cap, enterprise value, book value, and promoter holding. How does this stock compare to typical benchmarks in its sector in the Indian market?"]
LZ="Strategy 1 — Volume Breakout with Dynamic Stop Loss\n  Rule 1: Enter long when today's volume > 2× the 20-day average volume AND price closes above the prior day's high; set stop loss at 1.5× ATR below entry price.\n  Rule 2: Add a false breakout filter — price must hold above the breakout level for 2 consecutive candles before confirming entry; trail stop at the lowest low of the last 3 bars.\n  Rule 3: Set profit target at 2:1 risk-reward ratio; plot a volume histogram overlay to identify surge bars visually; include an alert condition for live breakout detection.\n\nStrategy 2 — Moving Average Crossover (50/100/200 DMA)\n  Rule 4: Buy when 50 DMA crosses above 100 DMA with price trading above the 200 DMA; exit when 50 DMA crosses back below 100 DMA; use 200 DMA as the hard stop-loss floor.\n  Rule 5: Add RSI confirmation — only enter when RSI is between 50–70 at the crossover candle; plot all three DMAs on the chart with distinct colours for visual clarity.\n  Rule 6: Allow a re-entry if 50 DMA pulls back to 100 DMA without breaking below 200 DMA; set stop loss 2% below the 50 DMA value at the time of entry.\n\nStrategy 3 — Trend Following with Trailing Stop\n  Rule 7: Enter long when price breaks a 20-day high with above-average volume and ADX > 25; apply a Chandelier Exit trailing stop set at 3× ATR from the highest close after entry.\n  Rule 8: Use 200 DMA direction as the trend filter — only take long trades when price is above 200 DMA; tighten trailing stop to 2× ATR once profit exceeds 10% from entry.\n  Rule 9: Add a re-entry condition: if stopped out but price remains above 200 DMA, re-enter on the next pullback to the 50 DMA; limit to a maximum of 2 re-entries per trend leg.\n\nStrategy 4 — Mean Reversion from 52W High/Low\n  Rule 10: Buy when price is within 15% of the 52-week low AND RSI < 35; set profit target at the 52-week midpoint; place hard stop loss 5% below the 52-week low level.\n  Rule 11: Exit/short signal when price is within 5% of the 52-week high with RSI > 70; use Bollinger Band upper band touch as secondary confirmation; target the middle Bollinger Band as exit.\n  Rule 12: Apply a volume reversal filter — only enter when the reversal candle's volume is ≥ 1.5× the 20-day average; plot the 52-week high and low as horizontal reference lines on the chart."
La='\n### 💡 Core Rules\n- **Sheet Convention:** Always use **NSE Code** instead of *Symbol* in the Google Sheet — this keeps NSE chart links working correctly.\n- **No Compromise:** Follow the Rules. Never compromise on Rules — Rules are better than any single Buy/Sell decision.\n- **Timing Edge:** Take advantage of time — buy when a stock is at its lower end (near 52W Low) and sell at a higher price when momentum kicks in (e.g. an Upper Circuit move).\n\n---\n\n### 🟢 Rule 1 — Near 52 Week High\nCMP / Close Price is highlighted **Green** when it is near the 52-Week High (within ~8%).\n\n### 🟠 Rule 2 — Near 52 Week Low (Buy Zone)\nCMP / Close Price is highlighted **Orange** when it is near the 52-Week Low (within ~8%) — **this is the type of stock to look at buying.**\n\n**52W Low / High Date column — color meaning:**\n| Signal | Meaning |\n|---|---|\n| 🟢 Green in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 18 days** |\n| 🟢 Green in *52 Week High Date* | Stock touched its 52-Week High within the **last 18 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 30 days** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High within the **last 30 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low **about 1 year ago** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High **about 1 year ago** |\n\n### 🔵 Rule 3 — Diff @ 200 DMA Strategy\nOnly buy **52-Week Low** stocks, ranked by the **Difference from 200 DMA** column on the **Diff @ 200 DMA** tab — biggest fall first.\n\n**Path:**\n1. Open the **Diff @ 200 DMA** tab (Main sheet).\n2. Refer to the **Difference from 200 DMA** column.\n3. Sort results **−40% → −30% → −20% → −10%** (most negative first).\n\n**Mind Map:**\n```\nRule 3 → Buy Only 52-Week Low Stocks\n│\n├── Main Sheet → Open Tab "Diff @ 200 DMA"\n├── Check Column → "Difference from 200 DMA"\n├── Sort Logic → Biggest Fall First (-40% → -30% → -20% → -10%)\n├── Meaning → Stock is trading below its 200 DMA\n├── Priority → More negative % = higher priority\n├── Selection Criteria\n│     ├── Only 52-Week Low stocks\n│     ├── Negative Difference from 200 DMA\n│     └── Deep-discount stocks preferred\n└── Final Action → Analyze & buy quality stocks\n```\n\n---\n\n### 🔗 Useful NSE Reference Links\n- **All Reports (Bhavcopy / Market Activity):** Bhavcopy (PR)(zip), Market Activity Report (csv), Full Bhavcopy & security delivery data, MCAP, PD, PR, SME → https://www.nseindia.com/all-reports/\n- **Securities Available for Trading** (ETF, Close-Ended MF Schemes, SME) → https://www.nseindia.com/static/market-data/securities-available-for-trading\n- **52-Week Low — Equity Market** → https://www.nseindia.com/market-data/52-week-low-equity-market#capital_market_link\n\n---\n\n### 🛑 Risk Management — No Compromise\n- **Stop Loss (Max 1–2%), no compromise.** બીજો chance મળશે કમાવાનો — પૈસા 10% ઓછા થયા તો 15% કમાવા પડશે.\n- **Risk-Reward Ratio:** max 5 trades, max 10% loss — never lose all your money in a single trade.\n- **Target / Profit Booking:** Max 10–20%.\n- Don\'t trade emotionally — the share market is a mind game.\n- Know everything related to a share before moving ahead.\n- Stay calm, serious, and stick to the decision you\'ve made.\n- **Clear Vision, no compromise:** Focus → Stop Loss → Risk-Reward Ratio → Target/Profit → 52-Week Low Buy.\n- **Priority order:** IPO → F&O → 52-Week Low Shares.\n'
Lb={BH:['50 DMA','100 DMA','200 DMA','NSE 1','Trading View 1','History Data 1','Screener 1','Zerodha 1','Chartlink 1','Market smith india 1','Official NSE URL 1'],BI:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
Lc={BH:['E','F','G','AA','AB','AC','AD','AE','AF','AG','AH'],BI:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
def H0(letter):
	A=letter;A=F(A).strip().upper()
	if not A or not A.isalpha():return-1
	B=0
	for C in A:B=B*26+(ord(C)-ord('A')+1)
	return B-1
def Ld(sheet_name,ordered_columns):
	C=sheet_name;A=ordered_columns;A=AM(A);B=set()
	for D in Lb.get(C,[]):
		if D in A:B.add(D)
	for F in Lc.get(C,[]):
		E=H0(F)
		if 0<=E<Q(A):B.add(A[E])
	return B
Le={BH:E,BI:E,CP:E,CQ:E,CR:E,CS:E,CT:E}
Lf={BH:[r,AN,'Close Price',AO,Jd,Ak,Al,Je,'Differance from 200 DMA','Cumulative Average Rule (CAR) Rating'],BI:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
Lg={BH:['B','C','D','L'],BI:[],CP:[],CQ:[],CR:[],CS:[],CT:[]}
def Lh(sheet_name,ordered_columns):
	D=sheet_name;A=ordered_columns;A=AM(A);B=[]
	for G in Lg.get(D,[]):
		E=H0(G)
		if 0<=E<Q(A):
			F=A[E]
			if F not in B:B.append(F)
	for C in Lf.get(D,[]):
		if C in A and C not in B:B.append(C)
	return B
import streamlit as A
Li='\n<style>\n    #MainMenu {visibility: show;}\n    header {visibility: show;}\n    [data-testid="stToolbar"] {visibility: show;}\n    footer {visibility: show;}\n</style>\n'
A.markdown(Li,unsafe_allow_html=B)
import streamlit as A
Lj='\n<style>\n    [data-testid="stToolbar"] {\n        right: 2rem;\n    }\n    [data-testid="stToolbar"]::before {\n        content: "";\n    }\n    button[kind="header"] {display: none;}\n</style>\n'
A.markdown(Lj,unsafe_allow_html=B)
Lk='romo'
if'logged_in'not in A.session_state:A.session_state.logged_in=J
if'watchlist'not in A.session_state:A.session_state.watchlist={}
if'ai_history'not in A.session_state:A.session_state.ai_history=[]
if'grid_reset_token'not in A.session_state:A.session_state.grid_reset_token=0
if not A.session_state.logged_in:
	A.markdown("<p style='text-align: center; margin-top: 100px; color: Green; font-size: 18px;'>250-V Dashboard</p>",unsafe_allow_html=B);A.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 20px;'>🔐 Admin Login</h1>",unsafe_allow_html=B);PS,Ll,PT=A.columns([1,1,1])
	with Ll:
		with A.form('login_form'):
			Lm=A.text_input('Enter Password',type='password');Ln=A.form_submit_button('Login',use_container_width=B)
			if Ln:
				if Lm==Lk:A.session_state.logged_in=B;A.rerun()
				else:import random;Lo=['Password इल्ले! 😅 इल्ले!, खम्मा घणी भाईसा, सॉरी। तुमसे सब कुछ हो पाएगा! यहां बहुत 🤪 दिमाग मत लगाओ, इस वेबसाइट को नहीं, 😂 इस गलत पासवर्ड को छोड़ दो!','❌ Password इल्ले भाईसा! 😅 इल्ले! खम्मा घणी, सॉरी। तुम बाहुबली हो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। अपनी सुंदर वेबसाइट को नहीं, 😂 इस सड़े हुए गलत पासवर्ड को छोड़ दो!','❌ खम्मा घणी भाईसा, Password इल्ले! 😅 sorry! तुम तो मंगल ग्रह पर पानी खोज सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस सीधे-सादे वेबसाइट को नहीं, 😂 इस जाली पासवर्ड को छोड़ दो!','❌ Password इल्ले! 😅 इल्ले! खम्मा घणी भाईसा, सॉरी। लोड मत लो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। दुनिया छोड़ दो, मोक्ष पकड़ लो, पर पहले 😂 इस गलत पासवर्ड को छोड़ दो!','❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, सॉरी। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!'];A.error(random.choice(Lo))
	Lp=m.now().strftime(CU);A.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {Lp}</p>",unsafe_allow_html=B);A.stop()
A.markdown('\n<style>\n    /* Reduce ALL headings to 90% smaller size */\n    h1, h2, h3, h4, h5, h6, .stSubheader, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {\n        font-size: 0.85rem !important;\n        font-weight: bold !important;\n        margin-top: 0.5rem !important;\n        margin-bottom: 0.5rem !important;\n    }\n</style>\n',unsafe_allow_html=B)
import yfinance as H1,streamlit as A
from datetime import datetime as m
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 Top 250 NSE Stock-Volume Breakout Dashboard</p>",unsafe_allow_html=B)
A.caption(f"Data refreshed: {m.now().strftime(CU)}")
@A.cache_data(ttl=60)
def Lq():
	A='UNSUPPORTED';H={'NIFTY 50':'^NSEI','NIFTY NEXT 50':'^NN50','NIFTY MIDCAP 50':'^NSEMDCP50','NIFTY MIDCAP 100':'^CRSLMID','NIFTY MIDCAP 150':A,'NIFTY SMLCAP 50':A,'NIFTY SMLCAP 100':A,'NIFTY SMLCAP 250':A,'NIFTY MIDSML 400':A,'NIFTY 100':'^CNX100','NIFTY 200':'^CNX200','NIFTY500 MULTI...':A,'NIFTY LARGEMID...':A,'NIFTY MID SELE...':A,'NIFTY TOTAL MK...':A,'NIFTY MICROCAP...':A,'NIFTY 500':'^CRSLDX','NIFTY FPI 150':A,'NIFTY500 LMS E...':A,'NIFTY MIDSMALL...':A,'NIFTY SMALLCAP...':A};B={}
	for(C,E)in H.items():
		if E==A:B[C]={B1:E1,z:j};continue
		try:
			I=H1.Ticker(E);D=I.history(period='5d')
			if not D.empty and Q(D)>=2:F=N(D[BJ].iloc[-1]);G=N(D[BJ].iloc[-2]);J=(F-G)/G*100;B[C]={B1:f"{F:,.2f}",z:J}
			else:B[C]={B1:G3,z:j}
		except h:B[C]={B1:G4,z:j}
	return B
Lr=Lq()
Aq=Jf
H2=0
for(Bz,AT)in Lr.items():
	if AT[B1]in[E1,G3,G4]:continue
	H2+=1;Em=D4 if AT[z]>=0 else G5;En='+'if AT[z]>=0 else C;Ls='https://www.nseindia.com/market-data/live-market-indices';Aq+=f"<a href='{Ls}' target='_blank' style='text-decoration:none;'>";Aq+=f"<div style='background-color: {Em}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Aq+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bz}</div>";Aq+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Aq+=f"<span style='font-size: 15px; font-weight: 700;'>{AT[B1]}</span>";Aq+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{En}{AT[z]:.2f}%</span>";Aq+=f"</div></div></a>"
Aq+=D5
with A.expander('📈 Click to view Live Market Indices',expanded=J):
	if H2==0:A.info('Market data is currently unavailable. Please check back later.')
	else:A.markdown(Aq,unsafe_allow_html=B)
A.write(c)
def H3(color_dict):
	A=color_dict
	if not A:return D6
	B,C,D=T(A.get('red',0)*255),T(A.get('green',0)*255),T(A.get('blue',0)*255);return f"#{B:02x}{C:02x}{D:02x}"
@A.cache_data(ttl=300,show_spinner=J)
def Lt(nse_symbol,period='1y'):
	try:
		C=F(nse_symbol).strip().upper()
		if not C:return G.DataFrame()
		D=C if C.endswith('.NS')else f"{C}.NS";A=H1.download(D,period=period,interval='1d',progress=J,auto_adjust=B)
		if A is E or A.empty:return G.DataFrame()
		if B0(A.columns,G.MultiIndex):A.columns=A.columns.get_level_values(0)
		A.index=G.to_datetime(A.index);return A
	except h:return G.DataFrame()
@A.cache_data(ttl=300)
def DQ(sheet_name):
	M='sheets'
	try:
		if E2 not in A.secrets:A.error("Missing 'gcp_service_account' in secrets.");return G.DataFrame()
		D=A.secrets[E2]
		if B0(D,F):D=Eg.loads(D)
		Y=[Jg,Jh];N=Gz.from_service_account_info(D,scopes=Y);j=Ef.authorize(N);Z=Ji;a=urllib.parse.quote(sheet_name);b=LT(N);c=f"https://sheets.googleapis.com/v4/spreadsheets/{Z}?includeGridData=true&ranges={a}";d=b.get(c);E=d.json()
		if'error'in E:return G.DataFrame()
		if M not in E or not E[M]:return G.DataFrame()
		e=E[M][0]['data'][0];O=e.get('rowData',[])
		if not O:return G.DataFrame()
		J,P,R=[],[],[]
		for f in O:
			g=f.get('values',[]);S,T,U=[],[],[]
			for V in g:S.append(V.get('formattedValue',C));W=V.get('effectiveFormat',{});T.append(H3(W.get('backgroundColor',{})));U.append(H3(W.get('textFormat',{}).get('foregroundColor',{})))
			J.append(S);P.append(T);R.append(U)
		i=J[0];K=[];H={}
		for B in i:
			B=F(B).strip()
			if B==C:B='empty_column'
			if B in H:H[B]+=1;B=f"{B}_{H[B]}"
			else:H[B]=0
			K.append(B)
		L=G.DataFrame(J[1:],columns=K)
		for(I,X)in D_(K):L[f"_bg_{X}"]=[A[I]if I<Q(A)else D6 for A in P[1:]];L[f"_txt_{X}"]=[A[I]if I<Q(A)else'#000000'for A in R[1:]]
		return L
	except h as k:return G.DataFrame()
def Lu(df,symbol_col):
	K=symbol_col;H='1';G='🔗 Link';I=df.copy();I[p]=I[K]
	for(L,M)in I.iterrows():
		A=F(M[p]).strip()
		if not A or A==A0:continue
		for J in I.columns:
			if J.startswith(AY)or J.startswith(AZ)or J==p:continue
			B=J.lower();C,D=E,G
			if Jj in B:C,D=f"https://www.tradingview.com/symbols/{A}/",f"Tre {A}"if not B.endswith(H)else G
			elif Jk in B:C,D=f"https://www.equitypandit.com/historical-data/{A}",f"History {A}"if not B.endswith(H)else G
			elif Jl in B:C,D=f"https://www.screener.in/company/{A}",f"Scr {A}"if not B.endswith(H)else G
			elif Jm in B:C,D=f"https://zerodha.com/markets/stocks/NSE/{A}",f"🪁 {A}"if not B.endswith(H)else G
			elif Jn in B:C,D=f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={A}",f"CL {A}"if not B.endswith(H)else G
			elif Jo in B:C,D=f"https://marketsmithindia.com/mstool/eval/{A}/evaluation.jsp",f"ms {A}"if not B.endswith(H)else G
			elif Jp in B:C,D=f"https://www.nseindia.com/get-quotes/equity?symbol={A}",f"nse📰 {A}"if not B.endswith(H)else G
			elif'nse'in B or J==K:C,D=f"https://charting.nseindia.com/?symbol={A}-EQ",A if not B.endswith(H)else G
			if C:I.at[L,J]=f'<a href="{C}" target="_blank" style="text-decoration:none; color:#000000;">{D}</a>'
	return I
def DR(df,col_name,st_container,display_label=E):
	J=display_label;D=col_name
	if D in df.columns:
		A=df[D].astype(F).str.replace(BK,C,regex=B);A=G.to_numeric(A,errors=AP).replace([A6.inf,-A6.inf],A6.nan);E=A.dropna()
		if not E.empty:
			H,I=b(N(E.min()),2),b(N(E.max()),2)
			if H<I:L=J if J else f"{D} Range:";K=st_container.slider(L,min_value=H,max_value=I,value=(H,I),key=f"filter_num_{D}");return df[(A>=K[0])&(A<=K[1])]
	return df
def H4(df,col_name,st_container):
	Q='Past 1 Year';P='Past 6 Months';O='Past 2 Months';N='Past 1 Month';M='Past 30 Days';L='Past 25 Days';K='Past 20 Days';J='Past 15 Days';I='Past 10 Days';H='Past 5 Days';F='All Time';E=col_name
	if E in df.columns:
		R=[F,H,I,J,K,L,M,N,O,P,Q];A=st_container.selectbox(f"{E}:",R,key=f"filter_date_{E}")
		if A!=F:
			S=G.to_datetime(df[E],errors=AP,dayfirst=B);C=G.Timestamp.now()
			if A==H:D=C-G.Timedelta(days=5)
			elif A==I:D=C-G.Timedelta(days=10)
			elif A==J:D=C-G.Timedelta(days=15)
			elif A==K:D=C-G.Timedelta(days=20)
			elif A==L:D=C-G.Timedelta(days=25)
			elif A==M:D=C-G.Timedelta(days=30)
			elif A==N:D=C-G.DateOffset(months=1)
			elif A==O:D=C-G.DateOffset(months=2)
			elif A==P:D=C-G.DateOffset(months=6)
			elif A==Q:D=C-G.DateOffset(years=1)
			return df[S>=D]
	return df
def B_(val):
	if G.isna(val):return 0
	A=re.sub(E3,C,F(val));return Q(A)
def H5(df):
	A=df.copy();D=[A for A in A.columns if A.startswith(AY)or A.startswith(AZ)or A==p];A=A.drop(columns=D,errors='ignore')
	for B in A.select_dtypes(include=['object']).columns:A[B]=A[B].apply(lambda x:re.sub(E3,C,F(x))if G.notnull(x)else x)
	return A
import streamlit.components.v1 as P
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>🌍 National Exchange Scanner (All NSE/BSE Stocks)</p>",unsafe_allow_html=B)
A.caption('Live market data covering 2,000+ equities. Powered by TradingView.')
with A.expander('🏆 Click to view Full-Market India Rankings',expanded=J):
	Lv,Lw,Lx,Ly,Lz=A.tabs(['🚀 Gainers & Losers','📦 Volume & Active','⭐ 52W High / Low','🔄 52W Reversals','📊 Top 100 Traded'])
	def Ar(screen_type):return f'''
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
	with Lv:
		As,At=A.columns(2)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>🚀 Top Gainers</p>",unsafe_allow_html=B);P.html(Ar('top_gainers'),height=520)
		with At:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔻 Top Losers</p>",unsafe_allow_html=B);P.html(Ar('top_losers'),height=520)
	with Lw:
		As,At=A.columns(2)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Volume Leaders</p>",unsafe_allow_html=B);P.html(Ar('volume_leaders'),height=520)
		with At:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Volume & Value)</p>",unsafe_allow_html=B);P.html(Ar('most_active'),height=520)
	with Lx:
		As,At=A.columns(2)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Highs</p>",unsafe_allow_html=B);P.html(Ar('new_52wk_high'),height=520)
		with At:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Lows</p>",unsafe_allow_html=B);P.html(Ar('new_52wk_low'),height=520)
	with Ly:
		As,At=A.columns(2)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>📈 Outperforming 52W High (Reversal Up)</p>",unsafe_allow_html=B);P.html(Ar('outperforming_52wk_high'),height=520)
		with At:A.markdown("<p style='font-size:14px; font-weight:bold;'>📉 Underperforming 52W Low (Reversal Down)</p>",unsafe_allow_html=B);P.html(Ar('underperforming_52wk_low'),height=520)
	with Lz:A.markdown("<p style='font-size:14px; font-weight:bold;'>📊 Top 100+ Stocks Traded (Full India Screener)</p>",unsafe_allow_html=B);P.html(Ar('general'),height=520)
A.write(c)
@A.cache_data(ttl=300)
def L_():
	B=DQ(BH);A={}
	if B.empty:return A
	D=[A for A in B.columns if not A.startswith(AY)and not A.startswith(AZ)];I=U((A for A in D if A.lower()in[D7,Aa,E4,E5,D8,E6]),E);J=U((A for A in D if A4 in A.lower()),E);K=U((A for A in D if D9 in A.lower()or z in A.lower()),E)
	if not I or not J:return A
	for(R,G)in B.iterrows():
		H=F(G.get(I,C)).strip()
		if not H or H==A0:continue
		O=F(G.get(J,C)).replace(AB,C).strip();P=F(G.get(K,'0')).replace(AC,C).replace(AB,C).strip()if K else'0'
		try:Q=N(O);L=f"{Q:,.2f}"
		except AW:L=E1
		try:M=N(P)
		except AW:M=j
		A[H]={B1:L,z:M}
	return A
M0=L_()
Au=Jf
H6=0
for(Bz,AT)in M0.items():
	if AT[B1]in[E1,G3,G4]:continue
	H6+=1;Em=D4 if AT[z]>=0 else G5;En='+'if AT[z]>=0 else C;M1=f"https://www.nseindia.com/get-quotes/equity?symbol={Bz}";Au+=f"<a href='{M1}' target='_blank' style='text-decoration:none;'>";Au+=f"<div style='background-color: {Em}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Au+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bz}</div>";Au+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Au+=f"<span style='font-size: 15px; font-weight: 700;'>{AT[B1]}</span>";Au+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{En}{AT[z]:.2f}%</span>";Au+=f"</div></div></a>"
Au+=D5
with A.expander('📈 Click to view Top 250 Stocks Matrix',expanded=J):
	if H6==0:A.info("Stock matrix data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:A.markdown(Au,unsafe_allow_html=B)
A.write(c)
@A.cache_data(ttl=300)
def M2():
	P='[a-zA-Z%, ]';D=DQ(BH)
	if D.empty:return G.DataFrame()
	H=[A for A in D.columns if not A.startswith(AY)and not A.startswith(AZ)];I=U((A for A in H if A.lower()in[D7,Aa,E4,E5,D8,E6]),E);J=U((A for A in H if A4 in A.lower()),E);K=U((A for A in H if D9 in A.lower()or z in A.lower()),E);L=U((A for A in H if BL in A.lower()),E);M=U((A for A in H if E7 in A.lower()and'face'not in A.lower()and'enterprise'not in A.lower()),E);N=U((A for A in H if CV in A.lower()),E)
	if not I:return G.DataFrame()
	A=G.DataFrame();A[f]=D[I].astype(F).str.strip();A[AO]=G.to_numeric(D[J].astype(F).str.replace(BK,C,regex=B),errors=AP)if J else j;A[E8]=G.to_numeric(D[K].astype(F).str.replace(BK,C,regex=B),errors=AP)if K else j;A[r]=G.to_numeric(D[L].astype(F).str.replace(BK,C,regex=B),errors=AP)if L else j;O=A[AO]*A[r]
	if M:A[CW]=G.to_numeric(D[M].astype(F).str.replace(P,C,regex=B),errors=AP)
	else:A[CW]=O
	if N:A[DA]=G.to_numeric(D[N].astype(F).str.replace(P,C,regex=B),errors=AP)
	else:A[DA]=O
	A=A.dropna(subset=[f,AO]).reset_index(drop=B);A=A[(A[f]!=A0)&(A[f]!=C)];return A
def B5(dataframe,metric_label=z):
	J=dataframe;G=metric_label;A="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-family: system-ui, -apple-system, sans-serif;'>"
	if J.empty:return"<p style='color: gray; font-size: 14px;'>No data available for this ranking.</p>"
	for(R,B)in J.iterrows():
		K=B[f];L=B[AO];H=B[E8];M=D4 if H>=0 else G5;N='+'if H>=0 else C
		if G==BL:D=B.get(r,0);F=f"Vol: {D/1000000:.1f}M"if D>=1000000 else f"Vol: {D:,.0f}"
		elif G==E7:E=B.get(CW,0);F=f"Val: ₹{E/10000000:,.1f}Cr"if E>=10000000 else f"Val: ₹{E:,.0f}"
		elif G==CV:I=B.get(DA,0);F=f"T.O: ₹{I/10000000:,.1f}Cr"if I>=10000000 else f"T.O: ₹{I:,.0f}"
		elif G==Jq:D=B.get(r,0);E=B.get(CW,0);O=f"{D/1000000:.1f}M"if D>=1000000 else f"{D/1000:.1f}k";P=f"₹{E/10000000:,.1f}Cr"if E>=10000000 else f"₹{E:,.0f}";F=f"📦 {O} | 💰 {P}"
		else:F=f"{N}{H:.2f}%"
		Q=f"https://www.nseindia.com/get-quotes/equity?symbol={K}";A+=f"<a href='{Q}' target='_blank' style='text-decoration:none;'>";A+=f"<div style='background-color: {M}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";A+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{K}</div>";A+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";A+=f"<span style='font-size: 15px; font-weight: 700;'>{L:,.2f}</span>";A+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px; white-space: nowrap;'>{F}</span>";A+=f"</div></div></a>"
	A+=D5;return A
Af=M2()
with A.expander('🏆 Click to view Advanced Ranking Dashboards (Top 250 Stocks)',expanded=J):
	if Af.empty:A.info("Ranking data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:
		M3=Af.nlargest(20,E8);M4=Af.nsmallest(20,E8);M5=Af.nlargest(20,r);M6=Af[Af[r]>0].nsmallest(20,r);M7=Af.nlargest(20,r);M8=Af.nlargest(20,CW);M9=Af.nlargest(20,DA);MA=Af.nlargest(20,CW);MB,MC,MD,ME,MF,MG=A.tabs(['📈 Gainers/Losers','📦 Volume Leaders','🔥 Active (Vol & Val)','💰 Top by Value','💎 Top by Turnover','💰 Most Active'])
		with MB:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🚀 Top 20 Gainers</p>",unsafe_allow_html=B);A.markdown(B5(M3,z),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔻 Top 20 Losers</p>",unsafe_allow_html=B);A.markdown(B5(M4,z),unsafe_allow_html=B)
		with MC:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>📦 Top 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B5(M5,BL),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💤 Bottom 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B5(M6,BL),unsafe_allow_html=B)
		with MD:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔥 Most Active Stocks (Volume & Traded Value)</p>",unsafe_allow_html=B);A.markdown(B5(M7,Jq),unsafe_allow_html=B)
		with ME:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active by Traded Value</p>",unsafe_allow_html=B);A.markdown(B5(M8,E7),unsafe_allow_html=B)
		with MF:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💎 Highest Market Turnover</p>",unsafe_allow_html=B);A.markdown(B5(M9,CV),unsafe_allow_html=B)
		with MG:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active (Highest Traded Value)</p>",unsafe_allow_html=B);A.markdown(B5(MA,E7),unsafe_allow_html=B)
A.write(c)
def DS(row,actual_cols):
	B=0;A=[]
	def D(col_keywords,negate=J):
		for D in col_keywords:
			A=U((A for A in actual_cols if D.lower()in A.lower()),E)
			if A and A in row:
				try:B=N(F(row[A]).replace(AC,C).replace(AB,C).strip());return-B if negate else B
				except:pass
	M=D([A4]);Q=D([Jr,CX,'52wlow'])
	if M and Q and Q>0:
		I=(M-Q)/Q*100
		if 8<=I<=15:B+=30;A.append(f"✅ CMP +{I:.1f}% from 52W Low (sweet zone)")
		elif I<8:B+=15;A.append(f"⚠️ CMP +{I:.1f}% from 52W Low (still bottoming)")
		elif I<=25:B+=10;A.append(f"🟡 CMP +{I:.1f}% from 52W Low (extended)")
		else:A.append(f"❌ CMP +{I:.1f}% from 52W Low (too far)")
	O=D([G6])
	if M and O and O>0:
		if M>O:B+=15;A.append('✅ CMP above 200 DMA (uptrend confirmed)')
		else:
			T=(M-O)/O*100
			if T>-10:B+=7;A.append(f"🟡 CMP {T:.1f}% below 200 DMA (near support)")
			else:A.append(f"❌ CMP {T:.1f}% below 200 DMA (downtrend)")
	K=D([BL])
	if K and K>0:
		if K>=10000000:B+=10;A.append(f"✅ High volume: {K:,.0f}")
		elif K>=1000000:B+=6;A.append(f"🟡 Moderate volume: {K:,.0f}")
		else:B+=2;A.append(f"⚠️ Low volume: {K:,.0f}")
	G=D([Js,'debt','d/e'])
	if G is not E:
		if G<=.1:B+=10;A.append(f"✅ Debt-Free / Zero Debt (D/E={G:.2f})")
		elif G<=.5:B+=7;A.append(f"✅ Very Low Debt (D/E={G:.2f})")
		elif G<=Am:B+=4;A.append(f"🟡 Manageable Debt (D/E={G:.2f})")
		else:A.append(f"❌ High Debt (D/E={G:.2f})")
	R=D([E9])
	if R is not E:
		if R>0:B+=10;A.append(f"✅ Profitable: Net Profit ₹{R:.1f} Cr")
		else:A.append(f"❌ Loss Making: Net Profit ₹{R:.1f} Cr")
	H=D(['ronw'])
	if H is not E:
		if H>=15:B+=10;A.append(f"✅ Strong RONW: {H:.1f}%")
		elif H>=8:B+=6;A.append(f"🟡 Moderate RONW: {H:.1f}%")
		elif H>0:B+=2;A.append(f"⚠️ Low RONW: {H:.1f}%")
		else:A.append(f"❌ Negative RONW: {H:.1f}%")
	L=D([G7,G8])
	if L is not E:
		if L>=50:B+=8;A.append(f"✅ Promoter Holding: {L:.1f}%")
		elif L>=35:B+=5;A.append(f"🟡 Promoter Holding: {L:.1f}%")
		else:A.append(f"⚠️ Low Promoter: {L:.1f}%")
	P=D([G9,GA])
	if P is not E:
		if P==0:B+=7;A.append('✅ Zero Pledged Shares')
		elif P<=5:B+=4;A.append(f"🟡 Low Pledge: {P:.1f}%")
		else:A.append(f"❌ High Pledge: {P:.1f}%")
	V=D([EA,'net sale'])
	if V and V>0:A.append(f"📊 Net Sales: ₹{V:.1f} Cr")
	W=D([EB])
	if W is not E:A.append(f"📦 % Delivery: {W:.1f}%")
	if B>=75:S='🟢 STRONG BUY'
	elif B>=55:S='🟡 WATCHLIST'
	elif B>=35:S='🟠 CAUTION'
	else:S='🔴 AVOID'
	return B,S,A
H7=GB
def H8():
	if E2 not in A.secrets:return
	B=A.secrets[E2]
	if B0(B,F):B=Eg.loads(B)
	C=[Jg,Jh];D=Gz.from_service_account_info(B,scopes=C);return Ef.authorize(D)
MH=Ji
def H9(client):
	try:
		A=client.open_by_key(MH)
		try:return A.worksheet(H7)
		except Ef.WorksheetNotFound:B=A.add_worksheet(title=H7,rows=500,cols=6);B.append_row([f,AO,DB,DC,EC,ED]);return B
	except h:return
def MI():
	D=H8()
	if not D:return
	E=H9(D)
	if not E:return
	try:
		I=E.get_all_records();G={}
		for B in I:
			H=F(B.get(f,C)).strip()
			if H:G[H]={BM:F(B.get(DB,C)),A4:F(B.get(AO,C)),CY:F(B.get(DC,C)),Bl:F(B.get(EC,C)),DD:F(B.get(ED,C))}
		A.session_state.watchlist=G
	except h:pass
def Eo():
	F=H8()
	if not F:A.warning('⚠️ Google Sheet write failed — check secrets.');return J
	E=H9(F)
	if not E:return J
	try:
		E.clear();E.append_row([f,AO,DB,DC,EC,ED])
		for(G,D)in A.session_state.watchlist.items():E.append_row([G,D.get(A4,C),D.get(BM,C),D.get(CY,C),D.get(Bl,C),D.get(DD,C)])
		return B
	except h as H:A.warning(f"⚠️ Sheet write error: {H}");return J
def MJ(sym,cmp=C,note=C,bf_score=C,bf_grade=C):A.session_state.watchlist[sym]={A4:cmp,BM:note,CY:bf_score,Bl:bf_grade,DD:m.now().strftime('%Y-%m-%d %H:%M')}
def HA(sym):A.session_state.watchlist.pop(sym,E)
if'watchlist_loaded'not in A.session_state:MI();A.session_state.watchlist_loaded=B
def MK(row_data,cols):
	M='sl_standard'
	def D(keys):
		for B in keys:
			for A in cols:
				if B in A.lower():
					try:D=F(row_data.get(A,C)).replace(AB,C).replace(AC,C).strip();return N(D)
					except(AW,G0):pass
	B=D([A4]);I=D(['52w high',DE,'52wk high']);J=D([Jr,CX,'52wk low']);K=D([Jt,'50dma']);L=D([G6,'200dma']);A={A4:B,GC:I,GD:J,'dma50':K,'dma200':L}
	if B and I and J:G=(I-J)/52;A[EE]=b(G,2);A['sl_tight']=b(B-Am*G,2);A[M]=b(B-1.5*G,2);A['sl_wide']=b(B-2.*G,2);O=2.;H=B-A[M];A['target_1r']=b(B+H*Am,2);A['target_2r']=b(B+H*O,2);A['target_3r']=b(B+H*3.,2);A[DF]=b(K,2)if K else E;A['trail_sl_200dma']=b(L,2)if L else E;A['risk_pct']=b(H/B*100,2)if B else E
	return A
def Ep(history):
	E='AI Analysis';B=history
	if not B:return b''
	F=G.DataFrame(B,columns=[f,'Model','Query','AI Result','Timestamp']);C=io.BytesIO()
	with G.ExcelWriter(C,engine=DG)as D:F.to_excel(D,index=J,sheet_name=E);A=D.sheets[E];A.column_dimensions['A'].width=12;A.column_dimensions['B'].width=14;A.column_dimensions['C'].width=40;A.column_dimensions['D'].width=80;A.column_dimensions['E'].width=20
	return C.getvalue()
if A.sidebar.button('🧹 Clear All Filters',use_container_width=B):
	for Eq in AM(A.session_state.keys()):
		if Eq.startswith('filter_')or Eq in(Ju,Jv,Jw,Jx):del A.session_state[Eq]
	A.session_state.grid_reset_token+=1;A.rerun()
A.sidebar.markdown(c)
A.sidebar.header('🔍 Global Search')
HB=A.sidebar.text_input('Search by Symbol, Name, etc...',key=Ju)
A.sidebar.markdown(c)
A.sidebar.header('📑 Select a Tab')
ML=[BH,BI,CP,CQ,CR,CS,CT]
n=A.sidebar.selectbox('Choose sheet',ML,key='filter_sheet')
A.markdown(f"<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📄 {n}</p>",unsafe_allow_html=B)
with A.spinner('Downloading data from Google API...'):Er=DQ(n)
if not Er.empty:
	Es=0;R=[A for A in Er.columns if not A.startswith(AY)and not A.startswith(AZ)];MM=Ld(n,R);Et=Le.get(n)
	if Et and Et in R:Es=R.index(Et)
	else:
		for(BT,MN)in D_(R):
			if MN.lower()in[D7,Aa,E4,E5,D8,E6]:Es=BT;break
	A.sidebar.markdown(c);A.sidebar.header('⚙️ Settings');C0=A.sidebar.selectbox('Symbol Column (locked):',R,index=Es,key='filter_symbol_col',disabled=B,help='Locked for consistency across sheets. To change it, edit LOCKED_SYMBOL_COLUMN near the top of the .py file.');HC=Lu(Er,C0);L=HC.copy()
	if HB:MO=L[R].astype(F).apply(lambda x:x.str.contains(HB,case=J,na=J)).any(axis=1);L=L[MO]
	A.sidebar.markdown(c);A.sidebar.header('🎨 Color Filters');Eu=A.sidebar.selectbox('Select Column to Filter by Color:',[AQ]+R,key='filter_color_col')
	if Eu!=AQ:
		Ev=f"_bg_{Eu}"
		if Ev in L.columns:
			MP=L[Ev].unique();Ew={D6:'⚪ White (Default)',u:'🟢 Green',AH:'🔴 Red',Jy:'🟡 Yellow','#4285f4':'🔵 Blue',Jz:'🟠 Orange','#b6d7a8':'🟩 Light Green','#f4cccc':'🟥 Light Red','#d9d2e9':'🟪 Light Purple'};Ex=[]
			for MQ in MP:
				Ey=F(MQ).lower()
				if Ey in Ew:Ex.append(Ew[Ey])
				else:Ex.append(f"🎨 Custom Hex: {Ey}")
			HD=A.sidebar.multiselect(f"Select Colors in '{Eu}':",sorted(Ex),key='filter_color_selections')
			if HD:
				Ez=[]
				for E_ in HD:
					for(MR,Bz)in Ew.items():
						if Bz==E_:Ez.append(MR)
					if E_.startswith(J_):Ez.append(E_.replace(J_,C))
				L=L[L[Ev].str.lower().isin(Ez)]
	A.sidebar.markdown(c);A.sidebar.header('🎯 Categorical Filters');MS=[A for A in R if AX(B in A.lower()for B in['cumulative average',GE,EF,K0,K1,GF,GG,GH,K2,GI])]
	for DT in MS:
		MT=sorted([A for A in HC[DT].unique()if F(A).strip()!=C]);HE=A.sidebar.multiselect(f"Filter by {DT}:",options=MT,key=f"filter_cat_{DT}")
		if HE:L=L[L[DT].isin(HE)]
	A.sidebar.markdown(c);A.sidebar.header('📈 DMA Trend Filter');Ch=A.sidebar.selectbox('Select DMA Condition:',[K3,K4,K5,K6,K7],key='filter_dma_trend')
	if Ch!=K3:
		HF=U((A for A in R if Jt in A.lower()),E);HG=U((A for A in R if'100 dma'in A.lower()),E);HH=U((A for A in R if G6 in A.lower()),E)
		if HF and HH:
			DU=G.to_numeric(L[HF].astype(F).str.replace(BK,C,regex=B),errors=AP);DV=G.to_numeric(L[HH].astype(F).str.replace(BK,C,regex=B),errors=AP)
			if Ch==K6:L=L[DU>DV]
			elif Ch==K7:L=L[DU<DV]
			elif HG:
				DW=G.to_numeric(L[HG].astype(F).str.replace(BK,C,regex=B),errors=AP)
				if Ch==K4:L=L[(DU<DW)&(DW<DV)]
				elif Ch==K5:L=L[(DU>DW)&(DW>DV)]
	A.sidebar.markdown(c);A.sidebar.header('📊 Numeric Range Filters');F0=U((A for A in R if'diff'in A.lower()and'200'in A.lower()),E)
	if F0:L=DR(L,F0,A.sidebar,'Diff. from 200 DMA Range:')
	F1=U((A for A in R if EG in A.lower()and'low'in A.lower()and(AC in A.lower()or'per'in A.lower())),E)
	if F1:L=DR(L,F1,A.sidebar,'From 52W Low Range:')
	F2=U((A for A in R if EG in A.lower()and'high'in A.lower()and(AC in A.lower()or'per'in A.lower())),E)
	if F2:L=DR(L,F2,A.sidebar,'From 52W High Range:')
	MU=[r,AO,Jd,K8,K9,KA,'Net Profit','EPS',KB,KC,'Enterprise Value',GJ,'Delivery'];HI={F0,F1,F2}
	for Ci in MU:
		F3=U((A for A in R if Ci.lower()in A.lower()and A not in HI),E)
		if F3:L=DR(L,F3,A.sidebar);HI.add(F3)
	A.sidebar.markdown(c);A.sidebar.header('📅 Date Filters');HJ=U((A for A in R if KD in A.lower()),E);HK=U((A for A in R if KE in A.lower()),E)
	if HJ:L=H4(L,HJ,A.sidebar)
	if HK:L=H4(L,HK,A.sidebar)
	A.sidebar.markdown(c);A.sidebar.header('📊 My Watchlist')
	if A.session_state.watchlist:
		HL=Q(A.session_state.watchlist);A.sidebar.caption(f"🔖 {HL} stock{"s"if HL>1 else C} saved")
		for(DX,F4)in AM(A.session_state.watchlist.items()):
			MV,MW=A.sidebar.columns([3,1]);MV.markdown(f"**{DX}** {"`"+F4[A4]+"`"if F4[A4]else C}<br><small style='color:gray'>{F4.get(BM,C)[:35]}</small>",unsafe_allow_html=B)
			if MW.button('❌',key=f"wl_rm_{DX}",help=f"Remove {DX}"):HA(DX);Eo();A.rerun()
		A.sidebar.markdown(C);MX=G.DataFrame([{f:B,AO:A[A4],DB:A[BM],DC:A.get(CY,C),EC:A.get(Bl,C),ED:A[DD]}for(B,A)in A.session_state.watchlist.items()]);HM=io.BytesIO()
		with G.ExcelWriter(HM,engine=DG)as MY:MX.to_excel(MY,index=J,sheet_name=GB)
		A.sidebar.download_button('📥 Download Watchlist Excel',data=HM.getvalue(),file_name=f"Watchlist_{m.now().strftime(Bm)}.xlsx",mime=Bn,use_container_width=B)
	else:A.sidebar.info('No stocks in watchlist yet.\nAdd from the workspace panel below.')
	if A.session_state.ai_history:
		A.sidebar.markdown(c);A.sidebar.header('🤖 AI History Export');A.sidebar.caption(f"{Q(A.session_state.ai_history)} analyses saved this session");MZ=Ep(A.session_state.ai_history);A.sidebar.download_button('📥 Download All AI Results (Excel)',data=MZ,file_name=f"AI_Analysis_{m.now().strftime(KF)}.xlsx",mime=Bn,use_container_width=B)
		if A.sidebar.button('🗑️ Clear AI History',use_container_width=B):A.session_state.ai_history=[];A.rerun()
	BU=[]
	if C0 in L.columns:BU.append(C0)
	C1=U((A for A in R if BL in A.lower()),E);Ma=U((A for A in R if KG in A.lower()or'prev'in A.lower()),E);A7=U((A for A in R if A4 in A.lower()),E);AK=U((A for A in R if D9 in A.lower()),E);B6=U((A for A in R if EG in A.lower()and'high'in A.lower()and BN not in A.lower()and AC not in A.lower()),E);B7=U((A for A in R if EG in A.lower()and'low'in A.lower()and BN not in A.lower()and AC not in A.lower()),E);BV=U((A for A in R if EB in A.lower()),E);BW=U((A for A in R if'rsi'in A.lower()),E);Cj=U((A for A in R if GF in A.lower()),E);B8=U((A for A in R if GG in A.lower()),E);Ck=U((A for A in R if GH in A.lower()and A!=Cj and'dma'not in A.lower()),E);DY=U((A for A in R if'macd'in A.lower()),E);B9=U((A for A in R if GI in A.lower()),E);BX=U((A for A in R if'diff'in A.lower()and'200'in A.lower()),E);HN=Lh(n,R)
	if HN:
		for s in HN:
			if s not in BU:BU.append(s)
	else:
		for Ci in(C1,Ma,A7,AK,B6,B7):
			if Ci and Ci not in BU:BU.append(Ci)
	Mb=[A for A in L.columns if A not in BU and not A.startswith(AY)and not A.startswith(AZ)and A!=p];Mc=[A for A in L.columns if A.startswith(AY)or A.startswith(AZ)or A==p];Md=BU+Mb+Mc;L=L[Md];A.markdown(c);A.subheader(f"🚀 Executive Dashboard — {n}");A.caption('Live snapshot of the currently filtered stock universe. Adjust sidebar filters to update instantly.')
	def Ag(series):
		A=series
		if A is E:return G.Series(dtype=N)
		return G.to_numeric(A.astype(F).str.replace('[%,₹\\s]',C,regex=B),errors=AP)
	V=L;Me=Q(V);t=Ag(V[AK])if AK and AK in V.columns else G.Series(dtype=N);Cl=Ag(V[C1])if C1 and C1 in V.columns else G.Series(dtype=N);AU=Ag(V[A7])if A7 and A7 in V.columns else G.Series(dtype=N);BY=Ag(V[B6])if B6 and B6 in V.columns else G.Series(dtype=N);Av=Ag(V[B7])if B7 and B7 in V.columns else G.Series(dtype=N);DZ=Ag(V[BW])if BW and BW in V.columns else G.Series(dtype=N);Cm=Ag(V[BV])if BV and BV in V.columns else G.Series(dtype=N);F5=U((A for A in R if GK in A.lower()),E);HO=Ag(V[F5])if F5 and F5 in V.columns else G.Series(dtype=N);Aw=Ag(V[BX])if BX and BX in V.columns else G.Series(dtype=N);F6=U((A for A in R if CV in A.lower()),E);HP=Ag(V[F6])if F6 and F6 in V.columns else G.Series(dtype=N);Da=T((t>0).sum())if not t.empty else 0;Cn=T((t<0).sum())if not t.empty else 0;F7=T((t==0).sum())if not t.empty else 0;PU=N(t.mean())if t.notna().any()else j;PV=Da/Cn if Cn>0 else E;PW=N(t.median())if t.notna().any()else E;PX=N(Cl.sum())if Cl.notna().any()else j;PY=N(HO.sum())if HO.notna().any()else j;PZ=N(HP.sum())if HP.notna().any()else j;Pa=N(DZ.mean())if DZ.notna().any()else E;Pb=N(Cm.mean())if Cm.notna().any()else E;Mf=T((Aw>0).sum())if Aw.notna().any()else 0;Mg=T((Aw<0).sum())if Aw.notna().any()else 0;HQ=0
	if B8 and B8 in V.columns:HQ=T(V[B8].astype(F).str.contains('breakout|buy|bullish',case=J,na=J).sum())
	HR=0
	if B9 and B9 in V.columns:HR=T(V[B9].astype(F).str.contains('buy',case=J,na=J).sum())
	HS,HT=0,0;HU=0
	if AU.notna().any()and BY.notna().any():Mh=AU/BY.replace(0,A6.nan)*100;HS=T((Mh>=95).sum())
	if AU.notna().any()and Av.notna().any():HV=AU/Av.replace(0,A6.nan)*100;HT=T((HV<=105).sum());HU=T((HV<=115).sum())
	def AV(container,label,value,bg='#f5f7fa',fg='#1a1a1a'):container.markdown(f"<div style='background:{bg}; border-radius:10px; padding:12px 8px; text-align:center; border:1px solid rgba(0,0,0,0.06);'><div style='font-size:0.70em; color:#666; font-weight:700; letter-spacing:0.2px;'>{label}</div><div style='font-size:1.30em; font-weight:800; color:{fg}; margin-top:2px;'>{value}</div></div>",unsafe_allow_html=B)
	BZ=A.columns(7);AV(BZ[0],'📦 TOTAL STOCKS',f"{Me:,}");AV(BZ[1],'🟢 ADVANCES',f"{Da:,}",bg=CZ,fg=GL);AV(BZ[2],'🔴 DECLINES',f"{Cn:,}",bg=Bo,fg=DH);AV(BZ[3],'⚪ UNCHANGED',f"{F7:,}");AV(BZ[4],'🕳️ NEAR 52W LOW (≤15%)',f"{HU:,}"if AU.notna().any()and Av.notna().any()else DI,bg=Bo,fg=DH);AV(BZ[5],'🚀 BREAKOUTS',f"{HQ:,}",bg=GM,fg='#e65100');AV(BZ[6],'✅ BUY SIGNALS',f"{HR:,}",bg=KH,fg='#0d47a1');A.markdown("<div style='margin-top:8px;'></div>",unsafe_allow_html=B);Db=A.columns(4);AV(Db[0],'🏔️ NEAR 52W HIGH (≥95%)',f"{HS:,}",bg=CZ,fg=GL);AV(Db[1],'🕳️ NEAR 52W LOW (≤5%)',f"{HT:,}",bg=Bo,fg=DH);AV(Db[2],'📉 BELOW 200 DMA',f"{Mg:,}"if Aw.notna().any()else DI,bg=Bo,fg=DH);AV(Db[3],'🎯 ABOVE 200 DMA',f"{Mf:,}"if Aw.notna().any()else DI,bg=CZ,fg=GL);A.markdown(Ca,unsafe_allow_html=B);Ah={KI:J,'modeBarButtons':[['toImage']]}
	def Mi(frac):
		B=frac;B=AA(j,min(Am,B));D=[(j,(234,67,53)),(.5,(249,168,37)),(Am,(15,157,88))]
		for H in E0(Q(D)-1):
			C,A=D[H];E,F=D[H+1]
			if C<=B<=E:G=(B-C)/(E-C)if E>C else j;I=T(A[0]+(F[0]-A[0])*G);J=T(A[1]+(F[1]-A[1])*G);K=T(A[2]+(F[2]-A[2])*G);return f"#{I:02x}{J:02x}{K:02x}"
		return'#999999'
	def Pc(title_text,points,y_min,y_max,y_label,height=340):
		G=height;F=y_max;D=points;B=y_min
		if not D:A.info('No data available for this chart.');return
		N=Q(D);O=F-B or Am;H=C
		for(R,(S,I,T))in D_(D):U=(I-B)/O;K=AA(j,min(Am,U));V=Mi(K);W=R/AA(N-1,1)*100;X=(1-K)*100;H+=f'<a href="{T}" target="_blank" title="{S}: {I:.2f}{y_label}" style="position:absolute; left:{W:.3f}%; top:{X:.3f}%; width:11px; height:11px; margin:-6px 0 0 -6px; border-radius:50%; background:{V}; display:block; border:1px solid rgba(255,255,255,0.75); box-shadow:0 0 1px rgba(0,0,0,0.35); cursor:pointer;"></a>'
		L=C
		for(Y,M)in[(0,F),(25,E),(50,(B+F)/2),(75,E),(100,B)]:Z=f"{M:.0f}"if M is not E else C;L+=f'<div style="position:absolute; left:0; right:0; top:{Y}%; border-top:1px dashed rgba(0,0,0,0.08); height:0;"><span style="position:absolute; left:-2px; top:-8px; font-size:10px; color:#9aa0a6;">{Z}</span></div>'
		a=f'<div style="font-family:\'Source Sans Pro\',sans-serif;"><div style="font-weight:700; font-size:14px; margin-bottom:2px;">{title_text}</div><div style="font-size:11px; color:#9aa0a6; margin-bottom:8px;">Click any dot to open its NSE chart in a new tab</div><div style="position:relative; width:calc(100% - 26px); height:{G}px; margin-left:26px; background:#fff; border:1px solid rgba(0,0,0,0.08); border-radius:6px; overflow:hidden;">{L}{H}</div><div style="display:flex; justify-content:space-between; margin-left:26px; margin-top:4px;"><span style="font-size:10px; color:#ea4335;">● low</span><span style="font-size:10px; color:#f9a825;">● mid</span><span style="font-size:10px; color:#0f9d58;">● high</span></div></div>';P.html(a,height=G+90,scrolling=J)
	Mj,Mk,Ml=A.columns([1,1.3,1.3])
	with Mj:
		if Da or Cn or F7:HW=K.Figure(data=[K.Pie(labels=['Advances','Declines','Unchanged'],values=[Da,Cn,F7],hole=.55,marker=D(colors=[u,AH,'#bdbdbd']))]);HW.update_layout(title='Market Breadth',template=k,height=300,margin=D(t=40,b=10,l=10,r=10),showlegend=B);A.plotly_chart(HW,use_container_width=B,key=f"dash_breadth_{n}",config=Ah)
		else:A.info('No % change column detected for breadth chart.')
	with Mk:
		if t.notna().any():HX=K.Figure(data=[K.Histogram(x=t.dropna(),nbinsx=30,marker_color='#1f77b4')]);HX.update_layout(title='% Change Distribution',template=k,height=300,margin=D(t=40,b=10,l=10,r=10),xaxis_title=KJ,yaxis_title=GN);A.plotly_chart(HX,use_container_width=B,key=f"dash_pcthist_{n}",config=Ah)
		else:A.info(GO)
	with Ml:
		if DZ.notna().any():Dc=K.Figure(data=[K.Histogram(x=DZ.dropna(),nbinsx=25,marker_color=KK)]);Dc.add_vrect(x0=0,x1=30,fillcolor=EH,opacity=.08,line_width=0,annotation_text='Oversold');Dc.add_vrect(x0=70,x1=100,fillcolor=EI,opacity=.08,line_width=0,annotation_text='Overbought');Dc.update_layout(title='RSI(14) Distribution',template=k,height=300,margin=D(t=40,b=10,l=10,r=10),xaxis_title=GJ);A.plotly_chart(Dc,use_container_width=B,key=f"dash_rsihist_{n}",config=Ah)
		else:A.info('No RSI column detected for this sheet.')
	Mm,Mn,Mo=A.columns(3)
	if C0 in V.columns:Ax=V[C0].astype(F)
	elif p in V.columns:Ax=V[p].astype(F)
	else:Ax=V.index.astype(F).to_series(index=V.index)
	if p in V.columns:C2=V[p].astype(F).str.strip()
	else:C2=Ax.astype(F).str.replace('<[^>]+>',C,regex=B).str.strip()
	def HY(fig,chart_key):
		O='customdata';N='points';M='selection';K=chart_key;H=fig;H.update_layout(clickmode='event+select')
		try:I=A.plotly_chart(H,use_container_width=B,key=K,on_select='rerun')
		except G0:A.plotly_chart(H,use_container_width=B,key=K);A.caption('⚠️ Click-to-open needs Streamlit ≥ 1.35 — update `streamlit` in requirements.txt to enable it.');return
		C=E;F=I.get(M)if B0(I,D)else G1(I,M,E)
		if F:
			L=F.get(N)if B0(F,D)else G1(F,N,E)
			if L:
				J=L[-1];G=J.get(O)if B0(J,D)else G1(J,O,E)
				if G:C=G[0]if B0(G,(AM,tuple))else G
		if C:
			P=f"https://charting.nseindia.com/?symbol={C}-EQ";Q,R=A.columns([3,1])
			with Q:A.success(f"Selected: **{C}**")
			with R:A.link_button('📈 Open on NSE',P,use_container_width=B)
			A.markdown(f"🔗 **More links for {C}:** [Trading View (🔗)](https://www.tradingview.com/symbols/{C}/) &nbsp;|&nbsp; [History Data (🔗)](https://www.equitypandit.com/historical-data/{C}) &nbsp;|&nbsp; [Screener (🔗)](https://www.screener.in/company/{C}) &nbsp;|&nbsp; [Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{C}) &nbsp;|&nbsp; [Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={C}) &nbsp;|&nbsp; [Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{C}/evaluation.jsp) &nbsp;|&nbsp; [NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={C})")
		else:A.caption('Click any dot above to select a stock — its NSE chart button and quick-links will appear here.')
	with Mm:
		if t.notna().any():HZ=t.dropna().sort_values(ascending=J).head(10).index;Ha=G.DataFrame({f:Ax.loc[HZ].values,EJ:t.loc[HZ].values}).iloc[::-1];Hb=K.Figure(K.Bar(x=Ha[EJ],y=Ha[f],orientation=BO,marker_color=u));Hb.update_layout(title='🏆 Top 10 Gainers',template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(Hb,use_container_width=B,key=f"dash_topgain_{n}",config=Ah)
		else:A.info(GO)
	with Mn:
		if t.notna().any():Hc=t.dropna().sort_values(ascending=B).head(10).index;Hd=G.DataFrame({f:Ax.loc[Hc].values,EJ:t.loc[Hc].values}).iloc[::-1];He=K.Figure(K.Bar(x=Hd[EJ],y=Hd[f],orientation=BO,marker_color=AH));He.update_layout(title='📉 Top 10 Losers',template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(He,use_container_width=B,key=f"dash_toplose_{n}",config=Ah)
		else:A.info(GO)
	with Mo:
		if Cl.notna().any():Hf=Cl.dropna().sort_values(ascending=J).head(10).index;Hg=G.DataFrame({f:Ax.loc[Hf].values,r:Cl.loc[Hf].values}).iloc[::-1];Hh=K.Figure(K.Bar(x=Hg[r],y=Hg[f],orientation=BO,marker_color=An));Hh.update_layout(title='🔥 Top 10 by Volume',template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(Hh,use_container_width=B,key=f"dash_topvol_{n}",config=Ah)
		else:A.info('No Volume column detected for this sheet.')
	Mp,Mq,Mr=A.columns(3)
	with Mp:
		if AU.notna().any()and BY.notna().any():Hi=(BY-AU)/BY.replace(0,A6.nan)*100;Hj=Hi.dropna().sort_values(ascending=B).head(10).index;Hk=G.DataFrame({f:Ax.loc[Hj].values,KL:Hi.loc[Hj].values}).iloc[::-1];Hl=K.Figure(K.Bar(x=Hk[KL],y=Hk[f],orientation=BO,marker_color=u));Hl.update_layout(title='🏔️ Top 10 Nearest 52W High',template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(Hl,use_container_width=B,key=f"dash_nearhigh_{n}",config=Ah)
		else:A.info('52-Week High column not detected for this sheet.')
	with Mq:
		if AU.notna().any()and Av.notna().any():Hm=(AU-Av)/Av.replace(0,A6.nan)*100;Hn=Hm.dropna().sort_values(ascending=B).head(10).index;Ho=G.DataFrame({f:Ax.loc[Hn].values,KM:Hm.loc[Hn].values}).iloc[::-1];Hp=K.Figure(K.Bar(x=Ho[KM],y=Ho[f],orientation=BO,marker_color=AH));Hp.update_layout(title='🕳️ Top 10 Nearest 52W Low',template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(Hp,use_container_width=B,key=f"dash_nearlow_{n}",config=Ah)
		else:A.info('52-Week Low column not detected for this sheet.')
	with Mr:
		if Cm.notna().any():Hq=Cm.dropna().sort_values(ascending=J).head(10).index;Hr=G.DataFrame({f:Ax.loc[Hq].values,AN:Cm.loc[Hq].values}).iloc[::-1];Hs=K.Figure(K.Bar(x=Hr[AN],y=Hr[f],orientation=BO,marker_color=EK));Hs.update_layout(title='🚚 Top 10 by Delivery %',template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(Hs,use_container_width=B,key=f"dash_topdeliv_{n}",config=Ah)
		else:A.info('No Delivery % column detected for this sheet.')
	Ms,Mt=A.columns(2)
	with Ms:
		if AU.notna().any()and BY.notna().any()and Av.notna().any():Mu=(BY-Av).replace(0,A6.nan);Ht=((AU-Av)/Mu*100).clip(0,100);Hu=Ht.notna()&C2.notna();Hv=C2[Hu].str.strip().values;Hw=Ht[Hu].values;Hx=K.Figure(K.Scatter(x=Hv,y=Hw,mode=EL,marker=D(size=9,color=Hw,colorscale=[[0,AH],[.5,An],[1,u]],cmin=0,cmax=100,showscale=B,colorbar=D(title='% of Range')),customdata=Hv,hovertemplate=KN));Hx.update_layout(title='📍 Position within 52-Week Range (0% = Low, 100% = High)',template=k,height=340,margin=D(t=40,b=10,l=10,r=10),xaxis=D(showticklabels=J,title=GN),yaxis_title='% of 52W Range');HY(Hx,f"dash_range_{n}")
		else:A.info('52-Week High/Low columns not detected for this sheet.')
	with Mt:
		if Aw.notna().any()and C2 is not E:Hy=Aw.notna()&C2.notna();Hz=C2[Hy].str.strip().values;Dd=Aw[Hy].values;H_=AA(abs(N(A6.nanmin(Dd))),abs(N(A6.nanmax(Dd))),1e-09);I0=K.Figure(K.Scatter(x=Hz,y=Dd,mode=EL,marker=D(size=9,color=Dd,colorscale=[[0,AH],[.5,An],[1,u]],cmin=-H_,cmax=H_,showscale=B,colorbar=D(title='% Diff')),customdata=Hz,hovertemplate=KN));I0.update_layout(title='📐 Difference from 200 DMA (0% = at 200 DMA)',template=k,height=340,margin=D(t=40,b=10,l=10,r=10),xaxis=D(showticklabels=J,title=GN),yaxis_title='% Diff from 200 DMA');HY(I0,f"dash_diff200_{n}")
		else:A.info('Difference from 200 DMA column not detected for this sheet.')
	Mv,Pd=A.columns([1,1.4])
	with Mv:
		De=Ck or B9 or B8
		if De and De in V.columns:
			C3=V[De].astype(F).str.strip();C3=C3[(C3!=C)&(C3.str.lower()!=A0)]
			if not C3.empty:I1=C3.value_counts().head(8);I2=K.Figure(K.Bar(x=I1.values,y=I1.index.astype(F),orientation=BO,marker_color=EK));I2.update_layout(title=f"📶 {De} Breakdown",template=k,height=340,margin=D(t=40,b=10,l=10,r=10));A.plotly_chart(I2,use_container_width=B,key=f"dash_signal_{n}",config=Ah)
			else:A.info('No signal data available.')
		else:A.info('No Trend/Signal column detected for this sheet.')
	A.markdown(c);Mw,Mx,My=A.columns([3,1,2.2])
	with Mw:I3=A.radio(GP,[GQ,Cb,Cc],horizontal=B,help='Automatically adjust the column widths based on the text length of the selected row.')
	with My:A.markdown("<div style='margin-top: 2px; font-size:0.9rem;'>🔍 Filter stocks inside this matrix...</div>",unsafe_allow_html=B);I4=A.text_input(KO,placeholder=KP,key=Jv,label_visibility='collapsed')
	if I4:L=L[L[p].astype(F).str.contains(I4,case=J,na=J)]
	Mz=H5(L);I5=io.BytesIO()
	with G.ExcelWriter(I5,engine=DG)as M_:N0=n[:31].replace(':',C).replace('/',C);Mz.to_excel(M_,index=J,sheet_name=N0)
	with Mx:A.markdown("<div style='margin-top: 28px;'></div>",unsafe_allow_html=B);A.download_button(label='📥 Download as Excel',data=I5.getvalue(),file_name=f"{n}_Export_{m.now().strftime(Bm)}.xlsx",mime=Bn,use_container_width=J)
	N1,N2=A.columns([1,4])
	with N1:A.write(f"**Rows:** {L.shape[0]} | **Columns:** {Q(R)}")
	with N2:N3=A.empty()
	Df=B4("\n    class HtmlRenderer {\n        init(params) {\n            this.eGui = document.createElement('span');\n            this.eGui.innerHTML = params.value ? String(params.value) : '';\n        }\n        getGui() {\n            return this.eGui;\n        }\n    }\n    ");I6=B4('\n    function(params) {\n        let colName = params.colDef.field;\n        let c_low = colName.toLowerCase();\n\n        let bgCol = "_bg_" + colName;\n        let txtCol = "_txt_" + colName;\n\n        let bgColor = params.data[bgCol];\n        let txtColor = params.data[txtCol];\n\n        let isTargetCol = c_low.includes("cmp") || c_low.includes("close price") || c_low.includes("prev");\n\n        if (isTargetCol) {\n            if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') return null;\n            return {\n                \'backgroundColor\': bgColor,\n                \'color\': txtColor || \'#000000\',\n                \'fontWeight\': (txtColor === \'#ffffff\' || bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n            };\n        }\n\n        if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') {\n            return { \'color\': \'#000000\' };\n        }\n\n        return {\n            \'backgroundColor\': bgColor,\n            \'color\': \'#000000\',\n            \'fontWeight\': (bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n        };\n    }\n    ');BA=Ei.from_dataframe(L);BA.configure_selection(selection_mode='single',use_checkbox=B);BA.configure_side_bar(filters_panel=J,columns_panel=B);N4=[D7,D8,KQ,KR,Aa,GE,EF];Co=B
	for s in L.columns:
		if s.startswith(AY)or s.startswith(AZ)or s==p:BA.configure_column(s,hide=B);continue
		if s in MM:BA.configure_column(s,hide=B);continue
		if I3==Cb and Q(L)>0:
			F8=B_(L.iloc[0][s]);F9=Q(F(s));Cp=T(AA(F8,F9)*7+22)
			if Co:Cp+=30
			Dg,Dh=Cp,40
		elif I3==Cc and Q(L)>1:
			F8=B_(L.iloc[1][s]);F9=Q(F(s));Cp=T(AA(F8,F9)*7+22)
			if Co:Cp+=30
			Dg,Dh=Cp,40
		else:Dg,Dh=(220,150)if s.lower()in N4 else(120,80)
		Cq=s==C0;I7=DJ if Cq or Co else E
		if Co:Co=J
		N5=s.lower()
		if Cq or AX(A in N5 for A in[Jj,Jk,Jl,Jm,Jn,Jo,Jp,'nse']):BA.configure_column(s,width=Dg,minWidth=Dh,sortable=B,filter=B,resizable=B,editable=J,pinned=I7,lockPinned=Cq,suppressMovable=Cq,checkboxSelection=Cq,cellRenderer=Df,cellStyle=I6)
		else:BA.configure_column(s,width=Dg,minWidth=Dh,sortable=B,filter=B,resizable=B,editable=J,pinned=I7,cellStyle=I6)
	BA.configure_grid_options(domLayout=AR,rowHeight=35,headerHeight=45,enableCellTextSelection=B,ensureDomOrder=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);N6=BA.build();N7=Eh(L,gridOptions=N6,theme=GR,update_mode=LU.SELECTION_CHANGED,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,enable_enterprise_modules=J,height=400,width=GS,key=f"primary_stock_table_grid_{A.session_state.grid_reset_token}");Ba=N7.get('selected_rows',[])
	if Ba is not E and Q(Ba)>0 or Q(L)>0:
		if Ba is not E and Q(Ba)>0:S=Ba.iloc[0]if B0(Ba,G.DataFrame)else Ba[0]
		else:S=L.iloc[0]
		H=F(S.get(p,C)).strip()
		if H:
			with N3.container():A.markdown(f"**⚡ {H} Links:** [Trading View (🔗)](https://www.tradingview.com/symbols/{H}/) &nbsp;|&nbsp; [History Data (🔗)](https://www.equitypandit.com/historical-data/{H}) &nbsp;|&nbsp; [Screener (🔗)](https://www.screener.in/company/{H}) &nbsp;|&nbsp; [Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{H}) &nbsp;|&nbsp; [Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={H}) &nbsp;|&nbsp; [Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{H}/evaluation.jsp) &nbsp;|&nbsp; [NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={H})")
			A.markdown(f"---");A.subheader(f"🛠️ Live Workspace Panel: {H}");A8=A.slider('📏 Adjust Panel Box Height (px):',min_value=300,max_value=1000,value=500,step=50,key='panel_height_slider');A9=A.tabs(['🕯️ Price Chart (EMA + RSI)','📈 Chart & Trade Info (NSE Component)','📋 History Data (EquityPandit)','🎯 Bullish/Bearish Zone','📁 Screener Documents','🪁 Zerodha Portal','📊 MarketSmith India','📉 TradingView Symbol Profile','🤖 AI Stock Analysis','💻 AI Pine Script Builder','🔬 Bottom Fishing Score','🎯 GTT Order Calculator','📊 Watchlist Manager','📰 News Feed'])
			with A9[1]:I8=f"https://charting.nseindia.com/?symbol={H}-EQ";A.markdown(f"**NSE Interactive Chart Frame** &nbsp;|&nbsp; [🌐 Open in Browser]({I8})",unsafe_allow_html=J);A.caption(Bp);P.html(f'<iframe src="{I8}" width="100%" height="{A8}" style="border:none; border-radius:5px;"></iframe>',height=A8+20)
			with A9[2]:I9=f"https://www.equitypandit.com/historical-data/{H.lower()}";A.markdown(f"**EquityPandit Historical Matrix Data** &nbsp;|&nbsp; [🌐 Open in Browser]({I9})");A.caption(Bp);P.html(f'<iframe src="{I9}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[3]:IA=f"https://www.equitypandit.com/share-price/{H.lower()}#chart";A.markdown(f"**Bullish / Bearish Zone Indicator** &nbsp;|&nbsp; [🌐 Open in Browser]({IA})");A.caption(Bp);P.html(f'<iframe src="{IA}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[4]:IB=f"https://www.screener.in/company/{H}/consolidated/";A.markdown(f"**Screener Corporate Filings** &nbsp;|&nbsp; [🌐 Open in Browser]({IB})");A.caption(Bp);P.html(f'<iframe src="{IB}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[5]:IC=f"https://zerodha.com/markets/stocks/NSE/{H}/";A.markdown(f"**Zerodha Markets Financial Performance Metrics** &nbsp;|&nbsp; [🌐 Open in Browser]({IC})");A.caption(Bp);P.html(f'<iframe src="{IC}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[6]:ID=f"https://marketsmithindia.com/mstool/eval/{H.lower()}/evaluation.jsp";A.markdown(f"**MarketSmith India Institutional Trading Evaluation Engine** &nbsp;|&nbsp; [🌐 Open in Browser]({ID})");A.caption(Bp);P.html(f'<iframe src="{ID}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[7]:IE=f"https://www.tradingview.com/symbols/{H}/";A.markdown(f"**TradingView Comprehensive Asset Market Registry Summary Profile** &nbsp;|&nbsp; [🌐 Open in Browser]({IE})");A.caption(Bp);P.html(f'<iframe src="{IE}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[8]:
				A.markdown(f"### 🤖 Ask AI About **{H}**")
				if not Ej:A.warning(KS)
				else:
					Di=El('analysis');A.caption('⚡ Groq = llama-3.3-70b (free, fast) &nbsp;|&nbsp; 🧠 Gemini = gemini-2.5-flash'if BS and Cg else'⚡ Groq connected'if BS else'🧠 Gemini connected');A.write('Using the live data pulled from your dashboard, the AI can analyze technicals, ranges, and context.');FA=A.text_area('Your Query:',value=f"Based on the current data provided, give me a quick summary of the technical performance and trend for {H}.",height=80,key='ai_query_analysis')
					if A.button('✨ Generate AI Analysis',use_container_width=B,key='btn_ai_analysis'):
						with A.spinner(f"Analyzing {H} with {Di}..."):
							try:FB={A:B for(A,B)in S.items()if not F(A).startswith(Bq)};Cr=f"""
You are a professional stock market analyst evaluating Indian NSE stocks.
The user is asking about the stock: {H}.

Here is the live data extracted directly from the user's dashboard for this stock:
{FB}

User Query: {FA}

Please provide a clear, concise, and professional response.
""";FC=Ek(Cr,Di);A.session_state[GT]={DK:H,EM:Di,'query':FA,DL:FC};A.session_state.ai_history.append([H,Di,FA,FC,m.now().strftime(CU)]);A.info(FC)
							except h as Bb:A.error(f"AI error: {Bb}")
					if A.session_state.get(GT,{}).get(DK)==H:
						Cs=A.session_state[GT];Dj=Cs[DL];A.markdown(c);N8,N9,NA=A.columns(3)
						with N8:NB=Ep([[H,Cs[EM],Cs['query'],Dj,m.now().strftime(CU)]]);A.download_button('📥 Save as Excel',data=NB,file_name=f"AI_{H}_{m.now().strftime(KF)}.xlsx",mime=Bn,use_container_width=B,key='dl_ai_excel_analysis')
						with N9:NC=urllib.parse.quote(f"📊 *{H} AI Analysis* ({Cs[EM]})\n\n{Dj[:800]}"+('\n\n_(truncated)_'if Q(Dj)>800 else C));A.markdown(f"<a href='https://wa.me/?text={NC}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
						with NA:ND=urllib.parse.quote(f"📊 {H} AI Analysis ({Cs[EM]})\n\n{Dj[:800]}");A.markdown(f"<a href='https://t.me/share/url?url=NSEDashboard&text={ND}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
					A.markdown(c);A.markdown('**💡 Suggested Prompts** — copy any prompt below and paste it into the query box above:');NE='\n'.join([f"{A+1}. {B.replace("{sym}",H)}"for(A,B)in D_(LY)]);A.text(NE)
			with A9[9]:
				A.markdown(f"### 💻 AI Pine Script Generator for **{H}**")
				if not Ej:A.warning(KS)
				else:
					NF=El('pine');A.write("Generate a custom TradingView Pine Script v5 strategy tailored to this stock's current metrics.");IF=A.selectbox('Select Strategy Focus:',['Volume Breakout with Dynamic Stop Loss','Moving Average Crossover (50/100/200 DMA)','Trend Following with Trailing Stop','Mean Reversion from 52W High/Low'],key='pine_strategy_focus');NG=A.text_area('Additional Custom Rules (Optional):',value=f"Include risk management parameters and plot signals on the chart.",height=60,key='pine_query')
					if A.button('⚙️ Generate TradingView Pine Script',use_container_width=B,key='btn_pine'):
						with A.spinner(f"Writing Pine Script v5 code for {H}..."):
							try:FB={A:B for(A,B)in S.items()if not F(A).startswith(Bq)};Cr=f'''
You are an expert quantitative developer specializing in TradingView Pine Script v5.

Write a complete, ready-to-copy Pine Script v5 strategy for the stock: {H}.

Strategy Focus: {IF}
Custom Rules: {NG}

Here is the live fundamental and technical data for {H} to incorporate as baseline context or threshold values if relevant:
{FB}

Formatting Requirements:
1. Start with `//@version=5` and `strategy("{H} Custom Script", overlay=true)`
2. Include clear comments explaining the logic.
3. Provide ONLY the Pine Script code inside a markdown code block, no other conversational text.
''';IG=Ek(Cr,NF);A.session_state[GU]={DK:H,DL:IG};A.markdown('### 📋 Your Custom Strategy Code:');A.write('Copy the code below and paste it into the TradingView Pine Editor.');A.markdown(IG)
							except h as Bb:A.error(f"AI error: {Bb}")
					if A.session_state.get(GU,{}).get(DK)==H:NH=A.session_state[GU][DL];NI=Ep([[H,'Pine Script',IF,NH,m.now().strftime(CU)]]);A.download_button('📥 Save Pine Script as Excel',data=NI,file_name=f"PineScript_{H}_{m.now().strftime(Bm)}.xlsx",mime=Bn,key='dl_pine_excel')
					A.markdown(c);A.markdown('**📋 Custom Rules Reference** — copy any rule and paste it into the Additional Custom Rules box above:');A.text(LZ)
			with A9[10]:
				A.markdown(f"### 🔬 Bottom Fishing Analysis: **{H}**");A.caption('Scores this stock on 8 key criteria for buying from the bottom. Based entirely on your live sheet data.');IH={A:B for(A,B)in S.items()if not F(A).startswith(Bq)};C4,FD,FE=DS(IH,R);FF=Ab if C4>=75 else Jy if C4>=55 else Jz if C4>=35 else AH;A.markdown(f'''
                <div style="background:{FF}22; border-left:6px solid {FF}; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
                    <div style="font-size:2rem; font-weight:bold; color:{FF};">{C4}/100</div>
                    <div style="font-size:1.3rem; font-weight:bold;">{FD}</div>
                    <div style="font-size:0.85rem; color:#555; margin-top:4px;">Bottom Fishing Composite Score for {H}</div>
                </div>
                ''',unsafe_allow_html=B);A.markdown('#### 📋 Detailed Scoring Breakdown')
				for NJ in FE:A.markdown(f"- {NJ}")
				A.markdown(c);A.markdown('#### 📖 Scoring Criteria');NK='\n| # | Criteria | Max Points | Description |\n|---|----------|-----------|-------------|\n| 1 | **52W Low Proximity** | 30 | CMP is 8–15% above 52W Low (ideal entry zone) |\n| 2 | **Uptrend (200 DMA)** | 15 | CMP above 200 DMA = confirmed uptrend |\n| 3 | **Volume Activity** | 10 | High trading volume = institutional interest |\n| 4 | **Low/Zero Debt** | 10 | D/E ratio ≤ 0.1 is ideal (no loan burden) |\n| 5 | **Net Profitability** | 10 | Positive net profit confirms fundamental health |\n| 6 | **RONW %** | 10 | Return on Net Worth ≥ 15% = strong business |\n| 7 | **Promoter Holding** | 8 | ≥ 50% shows management confidence |\n| 8 | **Zero Pledge** | 7 | No pledged shares = no financial stress |\n';A.markdown(NK);A.info('💡 **Buy Strategy:** Look for scores ≥ 55 (Watchlist) or ≥ 75 (Strong Buy). The sweet zone is CMP at 8–15% above 52W Low with uptrend confirmed (CMP > 200 DMA), backed by positive profits, low debt, and high promoter holding. This combination maximizes probability of a bull run from the bottom.')
				if Ej:
					A.markdown(c);FG=El('bf')
					if A.button('🤖 Get AI Deep Analysis for Bottom Buy',use_container_width=B,key='bf_ai_btn'):
						with A.spinner(f"Running deep bottom-fishing analysis for {H} with {FG}..."):
							try:Cr=f"""
You are an expert Indian stock market analyst specializing in bottom-fishing and value investing.

Stock: {H}
Live Data from Dashboard: {IH}
Bottom Fishing Score: {C4}/100
Grade: {FD}
Scoring Breakdown: {chr(10).join(FE)}

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
""";FH=Ek(Cr,FG);A.session_state['last_bf_ai_result']={DK:H,DL:FH};A.session_state.ai_history.append([H,FG,'Bottom Fishing Deep Analysis',FH,m.now().strftime(CU)]);A.success('✅ AI Analysis Complete');A.markdown(FH)
							except h as Bb:A.error(f"AI error: {Bb}")
					A.markdown(c);A.markdown('#### 📤 Share BF Score Card');II=f"""🔬 *Bottom Fishing Score: {H}*

📊 Score: *{C4}/100*
📈 Grade: {FD}

"""+'\n'.join(FE[:5])+f"\n\n🕒 {m.now().strftime(KT)}\n📌 NSE Stock Dashboard";NL=urllib.parse.quote(II);NM=urllib.parse.quote(II);NN,NO=A.columns(2)
					with NN:A.markdown(f"<a href='https://wa.me/?text={NL}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
					with NO:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={NM}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
			with A9[11]:
				A.markdown(f"### 🎯 GTT Order Calculator: **{H}**");A.caption('Auto-suggest Stop-Loss, Targets & ATR-based GTT levels from your live sheet data.');NP={A:B for(A,B)in S.items()if not F(A).startswith(Bq)};AF=MK(NP,R)
				if not AF.get(A4):A.warning('⚠️ CMP column not found in sheet data. Cannot compute GTT levels.')
				else:
					W=AF[A4];NQ,NR,NS,NT=A.columns(4);NQ.metric('📍 CMP',f"₹{W:,.2f}")
					if AF.get(GC):NR.metric('⬆️ 52W High',f"₹{AF[GC]:,.2f}")
					if AF.get(GD):NS.metric('⬇️ 52W Low',f"₹{AF[GD]:,.2f}")
					if AF.get(EE):NT.metric('📊 ATR (approx)',f"₹{AF[EE]:,.2f}")
					A.markdown(c);A.markdown('#### ⚙️ Customize ATR Multiplier');NU,NV=A.columns(2);IJ=NU.number_input('Manual ATR Override (₹) — leave 0 to use auto',min_value=j,value=j,step=.5,key='gtt_manual_atr');Dk=NV.selectbox('Risk-Reward Ratio:',['1:1','1:1.5','1:2','1:2.5','1:3'],index=2,key='gtt_rr_ratio');NW=N(Dk.split(':')[1]);C5=IJ if IJ>0 else AF.get(EE,0)
					if C5 and C5>0:
						IK=b(W-Am*C5,2);C6=b(W-1.5*C5,2);IL=b(W-2.*C5,2);Dl=W-C6;Dm=b(W+Dl*Am,2);Dn=b(W+Dl*NW,2);Do=b(W+Dl*3.,2);NX=b(Dl/W*100,2);A.markdown('#### 🛡️ Stop-Loss Levels');FI=G.DataFrame([{EN:'Tight SL (1× ATR)',BP:IK,EO:b((W-IK)/W*100,2),EP:'Intraday / Scalp'},{EN:'Standard SL (1.5× ATR)',BP:C6,EO:b((W-C6)/W*100,2),EP:'Swing / BTST'},{EN:'Wide SL (2× ATR)',BP:IL,EO:b((W-IL)/W*100,2),EP:'Positional'}])
						if AF.get(DF):FI=G.concat([FI,G.DataFrame([{EN:'Trail SL @ 50 DMA',BP:AF[DF],EO:b((W-AF[DF])/W*100,2)if AF[DF]<W else 0,EP:'Trailing Stop'}])],ignore_index=B)
						A.dataframe(FI,use_container_width=B,hide_index=B);A.markdown(f"#### 🎯 Target Levels (based on {Dk} R:R)");NY=G.DataFrame([{GV:'T1 (1R)',BP:Dm,GW:b((Dm-W)/W*100,2),GX:'Book 30–40%'},{GV:f"T2 ({Dk} R:R)",BP:Dn,GW:b((Dn-W)/W*100,2),GX:'Book 40–50%'},{GV:'T3 (3R — runner)',BP:Do,GW:b((Do-W)/W*100,2),GX:'Hold remainder'}]);A.dataframe(NY,use_container_width=B,hide_index=B);A.markdown('#### 💰 Position Sizing Helper');NZ,Na=A.columns(2);Nb=NZ.number_input('Capital (₹):',min_value=1000,value=100000,step=5000,key='gtt_capital');IM=Na.number_input('Max Risk % of Capital:',min_value=.5,max_value=1e1,value=2.,step=.5,key='gtt_risk_pct');IN=Nb*IM/100;FJ=T(IN/(W-C6))if W-C6>0 else 0;IO=FJ*W;A.success(f"📦 Suggested Qty: **{FJ} shares** &nbsp;|&nbsp; Investment: **₹{IO:,.0f}** &nbsp;|&nbsp; Max Loss: **₹{IN:,.0f}** ({IM}%)");A.markdown(c);A.markdown('#### 📋 GTT Order Summary (Copy-Ready)');FK=f"""🎯 *GTT Order: {H}*

📍 Entry CMP: ₹{W:,.2f}
🛡️ Stop-Loss: ₹{C6:,.2f} ({NX:.1f}% risk)
🎯 Target 1:  ₹{Dm:,.2f} (+{b((Dm-W)/W*100,1)}%)
🎯 Target 2:  ₹{Dn:,.2f} (+{b((Dn-W)/W*100,1)}%)
🎯 Target 3:  ₹{Do:,.2f} (+{b((Do-W)/W*100,1)}%)
📦 Qty: {FJ} shares | ₹{IO:,.0f}
📊 ATR: ₹{C5:.2f} | R:R {Dk}
🕒 {m.now().strftime(KT)}""";A.code(FK,language=C);Nc=urllib.parse.quote(FK);Nd=urllib.parse.quote(FK);Ne,Nf=A.columns(2)
						with Ne:A.markdown(f"<a href='https://wa.me/?text={Nc}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share GTT on WhatsApp</button></a>",unsafe_allow_html=B)
						with Nf:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={Nd}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share GTT on Telegram</button></a>",unsafe_allow_html=B)
					else:A.warning('⚠️ Could not compute ATR — 52W High/Low columns not found in sheet. Please enter ATR manually above.')
			with A9[12]:
				A.markdown(f"### 📊 Watchlist Manager");IP={A:B for(A,B)in S.items()if not F(A).startswith(Bq)};Ng,Nh,_=DS(IP,R);Ni=F(IP.get(A7,C))if A7 else C;FL=H in A.session_state.watchlist;A.markdown(f"**Current Stock: {H}** {"✅ Already in Watchlist"if FL else C}");Nj=A.text_input('📝 Note (optional):',value=A.session_state.watchlist.get(H,{}).get(BM,C),placeholder='e.g. Near 52W low, watching for breakout',key=f"wl_note_{H}");Nk,Nl=A.columns(2)
				with Nk:
					if A.button(f"{"🔄 Update"if FL else"➕ Add"} {H} to Watchlist",use_container_width=B,key='wl_add_btn'):
						MJ(H,cmp=Ni,note=Nj,bf_score=F(Ng),bf_grade=Nh);Nm=Eo()
						if Nm:A.success(f"✅ {H} saved to Watchlist (Google Sheet updated!)")
						else:A.info(f"✅ {H} added to session Watchlist (Sheet write failed — check secrets).")
						A.rerun()
				with Nl:
					if FL:
						if A.button(f"❌ Remove {H} from Watchlist",use_container_width=B,key='wl_rm_btn'):HA(H);Eo();A.rerun()
				A.markdown(c);A.markdown('#### 🗂️ Your Full Watchlist')
				if A.session_state.watchlist:
					Nn=[{f:B,'CMP (₹)':A[A4],DC:A.get(CY,C),GY:A.get(Bl,C),DB:A.get(BM,C),'Added':A.get(DD,C)}for(B,A)in A.session_state.watchlist.items()];IQ=G.DataFrame(Nn);A.dataframe(IQ,use_container_width=B,hide_index=B);IR=io.BytesIO()
					with G.ExcelWriter(IR,engine=DG)as No:IQ.to_excel(No,index=J,sheet_name=GB)
					A.download_button('📥 Download Watchlist as Excel',data=IR.getvalue(),file_name=f"Watchlist_{m.now().strftime(Bm)}.xlsx",mime=Bn,use_container_width=B,key='dl_wl_excel_tab');Np='\n'.join([f"• {B} — Score:{A.get(CY,C)} {A.get(Bl,C).split()[0]if A.get(Bl)else C} — {A.get(BM,C)[:30]}"for(B,A)in AM(A.session_state.watchlist.items())[:15]]);IS=f"📊 *My NSE Watchlist*\n\n{Np}\n\n🕒 {m.now().strftime(EQ)}";Nq=urllib.parse.quote(IS);Nr=urllib.parse.quote(IS);A.markdown(C);Ns,Nt=A.columns(2)
					with Ns:A.markdown(f"<a href='https://wa.me/?text={Nq}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share Watchlist on WhatsApp</button></a>",unsafe_allow_html=B)
					with Nt:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={Nr}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share Watchlist on Telegram</button></a>",unsafe_allow_html=B)
				else:A.info('Your watchlist is empty. Add stocks using the button above!')
			with A9[13]:
				A.markdown(f"### 📰 Latest News & Alerts: **{H}**");import urllib.request,urllib.parse,xml.etree.ElementTree as C7,datetime as m,email.utils
				def Nu(pubdate_str):
					try:
						E=email.utils.parsedate_to_datetime(pubdate_str);F=m.datetime.now(m.timezone.utc);G=F-E;A=G.total_seconds()
						if A<0:return AI
						if A<60:return f"{T(A)} secs ago"
						if A<3600:B=T(A/60);return f"{B} min{"s"if B!=1 else C} ago"
						if A<86400:D=T(A/3600);return f"{D} hour{"s"if D!=1 else C} ago"
						if A<172800:return'Yesterday'
						H=T(A/86400);return f"{H} days ago"
					except h:return GZ
				@A.cache_data(ttl=600)
				def Nv(target_symbol,limit=10):
					try:
						I=urllib.parse.quote(f'"{target_symbol}" stock share news NSE India');J=f"https://news.google.com/rss/search?q={I}&hl=en-IN&gl=IN&ceid=IN:en";K=urllib.request.Request(J,headers={Cd:Ce})
						with urllib.request.urlopen(K)as L:N=L.read()
						O=C7.fromstring(N);P=[DE,ER,CX,ES,ET,EU,EV,EW];D=[]
						for A in O.findall(DM):
							F=A.find(A5).text;Q=A.find(g).text;G=A.find(Ao).text if A.find(Ao)is not E else C;R=AX(A in F.lower()for A in P);S=Ga if R else C
							try:H=email.utils.parsedate_to_datetime(G)
							except h:H=m.datetime.min.replace(tzinfo=m.timezone.utc)
							D.append({AD:f"{S}{F}",g:Q,M:Nu(G),AJ:H})
						D.sort(key=lambda x:x[AJ],reverse=B);return D[:limit]
					except h:return[]
				with A.spinner(f"Fetching today's latest news for {H}..."):
					IT=Nv(H,limit=10)
					if IT:
						for O in IT:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.5em 0; opacity: 0.2;'>",unsafe_allow_html=B)
					else:A.info(f"No recent news found for {H}.")
			with A9[0]:
				with A.expander(f"🕯️ Price Chart & Technical Indicators — {H}",expanded=B):
					Nw=A.select_slider('History range:',options=['3mo','6mo','1y','2y','5y'],value='1y',key=f"chart_period_{H}")
					with A.spinner(f"Loading price history for {H}..."):o=Lt(H,period=Nw)
					if o.empty or BJ not in o.columns:A.warning(f"⚠️ No historical price data available for **{H}** via Yahoo Finance (tried `{H}.NS`). The symbol may be delisted, renamed, or not tracked by Yahoo.")
					else:
						Ai=o[BJ].squeeze().dropna();AL=N(Ai.iloc[-1]);Bc=N(Ai.iloc[-2])if Q(Ai)>1 else AL;Dp=(AL-Bc)/Bc*100 if Bc else j;IU=Ai.diff();Nx=IU.clip(lower=0).rolling(14).mean();Ny=(-IU.clip(upper=0)).rolling(14).mean();FM=100-100/(1+Nx/Ny.replace(0,N(A0)));Ct=FM.dropna().iloc[-1]if not FM.dropna().empty else E;Nz,N_=A.tabs(['Price + EMAs',GJ])
						with Nz:
							O0=A.radio('Chart type',[KU,'Line'],horizontal=B,key=f"chart_type_{H}");IV=Ai.diff();O1=IV.clip(lower=0).rolling(9).mean();O2=(-IV.clip(upper=0)).rolling(9).mean();Ay=100-100/(1+O1/O2.replace(0,N(A0)));FN=Ay.ewm(span=3,adjust=J).mean();IW=A6.arange(1,22,dtype=N);FO=Ay.rolling(21).apply(lambda x:N(A6.dot(x,IW)/IW.sum()),raw=B);x=AM(o.index);IX=Ay.values;Cu,IY=[],[];FP,IZ=[],[]
							for BT in E0(22,Q(Ay)):
								FQ,Ia=IX[BT],IX[BT-1]
								if A6.isnan(FQ)or A6.isnan(Ia):continue
								if FQ>=50 and Ia<50:
									Dq=Ay.index[BT]
									if Dq in Ai.index:Cu.append(Dq);IY.append(N(Ai.loc[Dq])*.993);FP.append(Dq);IZ.append(N(FQ))
							if not FN.dropna().empty and not FO.dropna().empty:FR=FN.dropna().iloc[-1];FS=FO.dropna().iloc[-1];FT=EH if FR>FS else EI;O3='🟢 H-M: POSITIVE (Bullish)'if FR>FS else'🔴 H-M: NEGATIVE (Bearish)';A.markdown(f"<div style='background:{FT}22;border-left:4px solid {FT};padding:6px 12px;border-radius:4px;margin-bottom:6px;font-size:13px;font-weight:700;color:{FT}'>{O3} — EMA3: {FR:.1f} | WMA21: {FS:.1f}</div>",unsafe_allow_html=B)
							e=LV(rows=3,cols=1,shared_xaxes=B,row_heights=[.55,.25,.2],vertical_spacing=.03,specs=[[{Gb:'xy'}],[{Gb:'xy'}],[{Gb:'xy'}]])
							if O0==KU:
								try:e.add_trace(K.Candlestick(x=x,open=o['Open'].squeeze(),high=o[EX].squeeze(),low=o[EY].squeeze(),close=o[BJ].squeeze(),name='OHLC',increasing_line_color=Gc,decreasing_line_color=Gd,increasing_fillcolor=Gc,decreasing_fillcolor=Gd,line=D(width=1.6),whiskerwidth=.9),row=1,col=1)
								except h:e.add_trace(K.Scatter(x=x,y=Ai,name=BJ,line=D(color=AE,width=2)),row=1,col=1)
							else:e.add_trace(K.Scatter(x=x,y=Ai,name=BJ,line=D(color=AE,width=2)),row=1,col=1)
							for(O4,O5,O6)in[(20,KV,'EMA20'),(50,'#FF6D00','EMA50'),(200,'#2979FF','EMA200')]:O7=Ai.ewm(span=O4,adjust=J).mean();e.add_trace(K.Scatter(x=x,y=O7,name=O6,line=D(color=O5,width=1.8)),row=1,col=1)
							Ib=N(o[EX].max());Ic=N(o[EY].min());e.add_hline(y=Ib,line_dash=Ge,line_color=KW,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W High ₹{Ib:,.2f}",annotation_position=KX,annotation_font=D(color=KW,size=13));e.add_hline(y=Ic,line_dash=Ge,line_color=KY,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W Low ₹{Ic:,.2f}",annotation_position='bottom right',annotation_font=D(color=KY,size=13))
							if Cu:e.add_trace(K.Scatter(x=Cu,y=IY,mode=EL,name='H-M Entry (RSI>50)',marker=D(color='lime',size=12,symbol=KZ,line=D(color='white',width=1.5))),row=1,col=1)
							try:Id=o[r].squeeze();O8=o['Open'].squeeze();O9=o[BJ].squeeze();OA=[Gc if B>=A else Gd for(A,B)in zip(O8.tolist(),O9.tolist())];e.add_trace(K.Bar(x=x,y=Id.tolist(),name=r,marker=D(color=OA,line=D(width=0)),opacity=.85,showlegend=J),row=3,col=1);OB=Id.rolling(20).mean();e.add_trace(K.Scatter(x=x,y=OB.tolist(),name='Vol Avg(20)',line=D(color='#616161',width=1.2,dash=DN)),row=3,col=1)
							except h:pass
							Dr=Ay.reindex(Ay.index);Ie=G.Series(5e1,index=Ay.index);OC=Dr.where(Dr>=50,5e1);e.add_trace(K.Scatter(x=x,y=Ie.tolist(),line=D(width=0),mode=EZ,showlegend=J,hoverinfo=Ea),row=2,col=1);e.add_trace(K.Scatter(x=x,y=OC.tolist(),fill=Ka,fillcolor='rgba(38,166,154,0.35)',line=D(width=0),mode=EZ,showlegend=J,hoverinfo=Ea),row=2,col=1);OD=Dr.where(Dr<=50,5e1);e.add_trace(K.Scatter(x=x,y=Ie.tolist(),line=D(width=0),mode=EZ,showlegend=J,hoverinfo=Ea),row=2,col=1);e.add_trace(K.Scatter(x=x,y=OD.tolist(),fill=Ka,fillcolor='rgba(239,83,80,0.35)',line=D(width=0),mode=EZ,showlegend=J,hoverinfo=Ea),row=2,col=1);e.add_trace(K.Scatter(x=x,y=Ay.tolist(),name='RSI(9)',line=D(color='#1976D2',width=1.5)),row=2,col=1);e.add_trace(K.Scatter(x=x,y=FN.tolist(),name='EMA3',line=D(color='#4CAF50',width=1.5)),row=2,col=1);e.add_trace(K.Scatter(x=x,y=FO.tolist(),name='WMA21',line=D(color='#EF5350',width=1.5)),row=2,col=1)
							if FP:e.add_trace(K.Scatter(x=FP,y=IZ,mode=EL,name='Entry (RSI panel)',showlegend=J,marker=D(color='lime',size=6,symbol=KZ,line=D(color='white',width=1))),row=2,col=1)
							e.add_hline(y=70,line_dash=DN,line_color=EI,opacity=.5,row=2,col=1);e.add_hline(y=50,line_dash=Ge,line_color='#888888',row=2,col=1,annotation_text='50',annotation_position='right');e.add_hline(y=30,line_dash=DN,line_color=KV,opacity=.8,row=2,col=1,annotation_text='30',annotation_position='right');e.update_layout(template=k,height=950,title=D(text=f"{H} — Ultra HD Chart (Price, EMAs, H-M, Volume)",font=D(size=12,color='#0E1117',family=Eb)),margin=D(t=60,b=80,l=20,r=20),xaxis_rangeslider_visible=J,xaxis2_rangeslider_visible=J,xaxis3_rangeslider_visible=J,legend=D(orientation=BO,y=-.15,x=.5,xanchor='center',yanchor='top',font=D(size=13,color=Kb,family=Eb)),hovermode='x unified',font=D(size=13,color=Kb,family=Eb),hoverlabel=D(font_size=14,font_family=Eb,bgcolor='rgba(255,255,255,0.95)'),plot_bgcolor=Ec,paper_bgcolor=Ec,bargap=.15);e.update_xaxes(showspikes=B,spikemode='across+toaxis',spikesnap='cursor',spikethickness=1.5,spikedash='solid',spikecolor='#808495',gridcolor=Kc,linecolor=Gf,tickfont=D(size=12,family=Kd));e.update_yaxes(gridcolor=Kc,zeroline=J,linecolor=Gf,tickfont=D(size=12,family=Kd));e.update_yaxes(range=[0,100],row=2,col=1);e.update_yaxes(title_text=BP,title_font=D(size=14,weight=AS),row=1,col=1);e.update_yaxes(title_text='RSI / H-M',title_font=D(size=14,weight=AS),row=2,col=1);e.update_yaxes(title_text=r,title_font=D(size=14,weight=AS),row=3,col=1);OE={KI:J,'responsive':B,'toImageButtonOptions':{'format':'png','filename':f"{H}_Ultra_HD_Analysis",'height':1080,'width':1920,'scale':6},'modeBarButtonsToAdd':['drawline','drawopenpath','drawrect','eraseshape']};A.plotly_chart(e,use_container_width=B,key=f"price_ema_chart_{H}",config=OE)
							if Cu:A.caption(f"🟢 {Q(Cu)} H-M entry signal(s) — RSI(9) crossed above 50 (bottom-catch). **H-M panel:** Green fill = RSI above 50 (momentum). Red fill = RSI below 50 (pullback). For informational purposes only.")
							else:A.caption('**H-M panel:** Green fill = RSI above 50. Red fill = RSI below 50 (pullback zone). 🟢 circles = RSI(9) cross above 50 (entry). For informational purposes only.')
							X={}
							if n!=BI:
								Ds=DQ(BI)
								if not Ds.empty:
									OF=[A for A in Ds.columns if not A.startswith(AY)and not A.startswith(AZ)];If=U((A for A in OF if A.lower()in[D7,Aa,E4,E5,D8,E6]),E)
									if If:
										Ig=Ds[Ds[If].astype(F).str.strip()==H]
										if not Ig.empty:OG=Ig.iloc[0].to_dict();X={A:B for(A,B)in OG.items()if not F(A).startswith(AY)and not F(A).startswith(AZ)and F(A)!=p}
							def Y(row,primary_dict,*K):
								def B(r_data):
									J='n/a';B=r_data
									if B is E or Q(B)==0:return l
									try:H=AM(B.keys())if B0(B,D)else AM(B.index)
									except h:return l
									H=[A for A in H if not F(A).startswith(AY)and not F(A).startswith(AZ)and F(A)!=p]
									for L in K:
										I=L.lower().strip()
										for G in H:
											if F(G).strip().lower()==I:
												A=B.get(G,C);A=C if A is E else F(A).strip()
												if A not in(C,A0,AQ,DI,J,l):return A
										for G in H:
											if I in F(G).strip().lower():
												A=B.get(G,C);A=C if A is E else F(A).strip()
												if A not in(C,A0,AQ,DI,J,l):return A
									return l
								A=B(primary_dict)
								if A==l:A=B(row)
								return A
							def Ih(label,value):return f"<div style='background:var(--secondary-background-color,#F0F2F6);border:1px solid rgba(128,128,128,0.35);border-radius:6px;padding:8px 10px;min-width:150px;flex:1 1 150px;'><div style='font-size:11px;color:var(--text-color,#31333F);opacity:0.65;margin-bottom:3px;'>{label}</div><div style='font-size:14px;font-weight:700;color:var(--text-color,#0E1117);word-break:break-word;'>{value}</div></div>"
							def FU(title,fields):D=C.join(Ih(A,Y(S,X,*B))for(A,B)in fields);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
						with N_:OH=AM(o.index);BB=K.Figure();BB.add_trace(K.Scatter(x=OH,y=FM,name=Ke,line=D(color=KK,width=2)));BB.add_hline(y=70,line_dash=DN,line_color=EI,opacity=.6);BB.add_hline(y=30,line_dash=DN,line_color=EH,opacity=.6);BB.add_hrect(y0=45,y1=65,fillcolor=EH,opacity=.06,line_width=0,annotation_text='Ideal entry 45-65',annotation_position=KX);BB.update_layout(template=k,height=280,yaxis=D(range=[0,100]),margin=D(t=30,b=20),plot_bgcolor=Ec,paper_bgcolor=Ec,font=D(color='#1A1A1A'));BB.update_xaxes(gridcolor=Kf);BB.update_yaxes(gridcolor=Kf);A.plotly_chart(BB,use_container_width=B,key=f"rsi14_chart_{H}")
				A.markdown("<hr style='margin:16px 0 4px 0;opacity:0.25;'>",unsafe_allow_html=B)
				with A.expander(f"📋 {H} — Google Sheet Data",expanded=B):
					def OI(title,items):D=C.join(Ih(A,B)for(A,B)in items);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
					OJ='▲'if Dp>=0 else'▼';OK='#00A152'if Dp>=0 else'#D32F2F';OI('📊 Price Snapshot',[(Kg,f"₹{AL:,.2f} <span style='color:{OK};font-size:12px;'>{OJ} {Dp:+.2f}%</span>"),(Ak,f"₹{N(o[EX].max()):,.2f}"),(Al,f"₹{N(o[EY].min()):,.2f}"),(Ke,f"{Ct:.1f}"if Ct is not E else'–')])
					with A.expander('📋 Company Price Dashboard',expanded=J):FU('🏢 Company Info',[('Company Name',[KQ,KR]),(Gg,[EF,GE]),(AN,[Kh,Ki,EB]),('52W High Date',[KD,'52 week high date']),('52W Low Date',[KE,'52 week low date']),(r,[BL]),(DA,[CV])]);FU('📡 Signals & System Output',[(Je,[K0]),('Difference from 200 DMA',['difference from 200 dma','differance from 200 dma']),('CAR Rating',['cumulative average rule (car) rating','car rating']),('Start GTT Order',[K1,'gtt order']),(Br,[GF]),(Bs,[GG]),(Bt,[GH]),(Bu,[K2]),(Bv,[GI])]);FU('💰 Fundamentals',[(KA,['face value']),('Total Equity Capital',[Gh]),(KC,[GK]),('EPS',['eps']),(KB,['ronw']),(K8,[G7,G8]),(K9,[Kj,Kk]),('Pledged %',[G9,GA]),('D/E Ratio',[Js,'de ratio']),('Net Sales (Cr)',[EA]),('Net Profit (Cr.)',[E9]),('Reserves (Cr)',[Gi]),('Total Debt (Cr)',[Gj]),('Inventory (Cr)',[Gk]),('Cash & Equiv (Cr)',[Gl,Gm,Gn]),('Operating Cash Flow (Cr)',['operating cash flow']),('Trade Receivables (Cr)',[Go]),('Trade Payables (Cr)',[Gp]),('Fixed Assets/Net PPE (Cr)',[Gq,Gr]),('Total Assets (Cr)',[Gs]),('Open (₹)',['open price','open (','open']),('High (₹)',['day high','high price','high (']),('Low (₹)',['day low','low price','low (']),('Prev Close (₹)',['prev close','previous close',KG]),('Price Change (₹)',['price change','change (','change in price']),(KJ,['% change',D9,'change %']),('Shares Outstanding (Cr)',['shares outstanding']),('Book Value (₹/share)',['book value']),('Public %',['public %','public holding']),('FII %',['fii %','fii holding','fii']),('DII %',['dii %','dii holding','dii'])])
					def d(raw):
						if raw in(E,l,C,A0,AQ):return
						try:return N(F(raw).replace(AB,C).replace('₹',C).strip())
						except(AW,G0):return
					def A1(h,alpha=.35):return f"rgba({T(h[1:3],16)},{T(h[3:5],16)},{T(h[5:7],16)},{alpha})"
					Bd=d(Y(S,X,EA));BC=d(Y(S,X,E9))
					if Bd is not E and BC is not E and 0<BC<Bd:Ii=Bd-BC;FV=BC/Bd*100;Ij=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=30,thickness=18,line=D(color=By,width=.5),label=[f"Net Sales<br>₹{Bd:,.2f} Cr (100%)",f"Net Profit<br>₹{BC:,.2f} Cr ({FV:.1f}%)",f"Total Expenses<br>₹{Ii:,.2f} Cr ({100-FV:.1f}%)"],color=[AE,u,AH]),link=D(source=[0,0],target=[1,2],value=[BC,Ii],color=['rgba(15,157,88,0.35)','rgba(234,67,53,0.35)'])));Ij.update_layout(title=f"💰 Revenue & Expenses Flow — {H} (Net Margin {FV:.1f}%)",template=k,height=320,margin=D(t=45,b=10,l=10,r=10),font=D(size=12));A.plotly_chart(Ij,use_container_width=B,key=f"sankey_{H}");A.caption('Based on Net Sales / Net Profit from the Fundamentals data above. "Total Expenses" is the remainder (Net Sales − Net Profit) — your sheet doesn\'t carry a Cost-of-Revenue/Opex breakdown, so a multi-stage flow (Gross → Operating → Net) isn\'t available for this stock.')
					elif Bd is not E and BC is not E:A.info(f"Revenue & Expenses flow needs a normal profitable split (0 < Net Profit < Net Sales). {H} currently shows Net Sales ₹{Bd:,.2f} Cr and Net Profit ₹{BC:,.2f} Cr, which doesn't fit a simple flow diagram (e.g. a net loss).")
					else:A.info("Net Sales / Net Profit not available for this stock, so the Revenue & Expenses flow can't be built.")
					OL=d(Y(S,X,Gh));OM=d(Y(S,X,Gi));ON=d(Y(S,X,Gj));OO=d(Y(S,X,Gp));OP=[(Kl,OL,AE),(Km,OM,u),(Kn,ON,AH),(Ko,OO,Kp)];BD=[(B,A,C)for(B,A,C)in OP if A is not E and A>0]
					if Q(BD)>=2:Ik=sum(B for(A,B,A)in BD);Il=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=30,thickness=18,line=D(color=By,width=.5),label=[f"Total Financing<br>₹{Ik:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/Ik*100:.1f}%)"for(B,A,C)in BD],color=[EK]+[B for(A,A,B)in BD]),link=D(source=[0]*Q(BD),target=AM(E0(1,Q(BD)+1)),value=[B for(A,B,A)in BD],color=[A1(B)for(A,A,B)in BD])));Il.update_layout(title=f"🏗️ Capital Structure — How {H} Is Financed",template=k,height=300,margin=D(t=45,b=10,l=10,r=10),font=D(size=12));A.plotly_chart(Il,use_container_width=B,key=f"sankey_capstruct_{H}");A.caption('Equity Capital + Reserves + Total Debt + Trade Payables, from the Fundamentals data above.')
					else:A.info('Not enough of Total Equity Capital / Reserves / Total Debt / Trade Payables available to build a Capital Structure flow.')
					C8=d(Y(S,X,Gs));OQ=[(Kq,d(Y(S,X,Gq,Gr)),Kr),(Ks,d(Y(S,X,Gk)),An),(Kt,d(Y(S,X,Go)),Ku),(Kv,d(Y(S,X,Gl,Gm,Gn)),AE)];FW=[(B,A,C)for(B,A,C)in OQ if A is not E and A>=0]
					if C8 is not E and C8>0 and FW:
						Im=sum(B for(A,B,A)in FW);FX=C8-Im
						if FX>=0:C9=FW+([(Kw,FX,Ed)]if FX>0 else[]);In=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=30,thickness=18,line=D(color=By,width=.5),label=[f"Total Assets<br>₹{C8:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/C8*100:.1f}%)"for(B,A,C)in C9],color=[Cf]+[B for(A,A,B)in C9]),link=D(source=[0]*Q(C9),target=AM(E0(1,Q(C9)+1)),value=[B for(A,B,A)in C9],color=[A1(B)for(A,A,B)in C9])));In.update_layout(title=f"📦 Asset Deployment — Where {H}'s Assets Sit",template=k,height=340,margin=D(t=45,b=10,l=10,r=10),font=D(size=12));A.plotly_chart(In,use_container_width=B,key=f"sankey_assets_{H}");A.caption('Fixed Assets, Inventory, Trade Receivables and Cash & Equivalents from the Fundamentals data above. "Other Assets" is the gap versus reported Total Assets (e.g. intangibles, investments, or other items your sheet doesn\'t itemize).')
						else:A.info(f"{H}'s itemized asset categories (₹{Im:,.2f} Cr) add up to more than the reported Total Assets (₹{C8:,.2f} Cr) — likely a data mismatch between sheet rows, so the Asset Deployment flow isn't shown to avoid a misleading chart.")
					else:A.info("Total Assets / asset-category data not available for this stock, so the Asset Deployment flow can't be built.")
					FY,Io,Dt=[],[],[];CA,CB,CC,CD=[],[],[],[]
					def Be(label,color,col_x):FY.append(label);Io.append(color);Dt.append(col_x);return Q(FY)-1
					OR,OS,Ip,FZ=.001,.24,.5,.999;OT=[(Kl,d(Y(S,X,Gh)),AE),(Km,d(Y(S,X,Gi)),u),(Kn,d(Y(S,X,Gj)),AH),(Ko,d(Y(S,X,Gp)),Kp)];Fa=[(B,A,C)for(B,A,C)in OT if A is not E and A>0];Iq=Q(Fa)>=2;BE=E
					if Iq:
						Du=sum(B for(A,B,A)in Fa);BE=Be(f"Total Financing<br>₹{Du:,.2f} Cr (100%)",EK,OS)
						for(Az,AG,Cv)in Fa:x=Be(f"{Az}<br>₹{AG:,.2f} Cr ({AG/Du*100:.1f}%)",Cv,OR);CA.append(x);CB.append(BE);CC.append(AG);CD.append(A1(Cv))
					Bf=d(Y(S,X,Gs));OU=[(Kq,d(Y(S,X,Gq,Gr)),Kr),(Ks,d(Y(S,X,Gk)),An),(Kt,d(Y(S,X,Go)),Ku),(Kv,d(Y(S,X,Gl,Gm,Gn)),AE)];Fb=[(B,A,C)for(B,A,C)in OU if A is not E and A>=0];Dv=Bf is not E and Bf>0 and bool(Fb)
					if Dv:OV=sum(B for(A,B,A)in Fb);Fc=Bf-OV;Dv=Fc>=0
					if Dv:
						OW=Fb+([(Kw,Fc,Ed)]if Fc>0 else[]);OX=f" ({Bf/Du*100:.1f}%)"if BE is not E else Kx;Ir=Be(f"Total Assets<br>₹{Bf:,.2f} Cr{OX}",Cf,Ip)
						if BE is not E:CA.append(BE);CB.append(Ir);CC.append(Bf);CD.append(A1(Cf))
						for(Az,AG,Cv)in OW:x=Be(f"{Az}<br>₹{AG:,.2f} Cr ({AG/Bf*100:.1f}%)",Cv,FZ);CA.append(Ir);CB.append(x);CC.append(AG);CD.append(A1(Cv))
					Bg=d(Y(S,X,EA));CE=d(Y(S,X,E9));Is=Bg is not E and CE is not E and 0<CE<Bg
					if Is:
						It=Bg-CE;OY=f" ({Bg/Du*100:.1f}%)"if BE is not E else Kx;Fd=Be(f"Net Sales<br>₹{Bg:,.2f} Cr{OY}",AE,Ip)
						if BE is not E:CA.append(BE);CB.append(Fd);CC.append(Bg);CD.append(A1(AE))
						Iu=CE/Bg*100;OZ=Be(f"Net Profit<br>₹{CE:,.2f} Cr ({Iu:.1f}%)",u,FZ);Oa=Be(f"Total Expenses<br>₹{It:,.2f} Cr ({100-Iu:.1f}%)",AH,FZ);CA+=[Fd,Fd];CB+=[OZ,Oa];CC+=[CE,It];CD+=[A1(u),A1(AH)]
					Ob=sum([Iq,Dv,Is])
					if Ob>0:
						from collections import defaultdict as Iv;Iw=Iv(T)
						for Cw in Dt:Iw[Cw]+=1
						Ix=Iv(T);Iy=[]
						for Cw in Dt:Az=Iw[Cw];BT=Ix[Cw];Ix[Cw]+=1;Iy.append(b((BT+.5)/Az,4)if Az>1 else .5)
						Iz=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=22,thickness=18,line=D(color=By,width=.5),label=FY,color=Io,x=Dt,y=Iy),link=D(source=CA,target=CB,value=CC,color=CD)));Iz.update_layout(title=f"💎 Combined Money Flow — {H} (Financing → Assets / Revenue, merged)",template=k,height=560,margin=D(t=45,b=10,l=10,r=10),font=D(size=12));A.plotly_chart(Iz,use_container_width=B,key=f"sankey_merged_{H}");A.caption("All money-related flows merged into one chart: financing sources (Equity + Reserves + Debt + Trade Payables) feed Total Financing, which splits into two parallel paths — Total Assets (incl. Trade Receivables) and Net Sales → Net Profit / Total Expenses. It's drawn as two branches off one hub, rather than one long chain, because Total Assets and Net Sales are different kinds of totals (balance sheet vs. P&L) that don't feed into each other. Trade Payables now also appears in the 🏗️ Capital Structure chart above.")
					else:A.info('Not enough financing / assets / revenue data available for this stock to build the Combined Money Flow chart.')
					CF=d(Y(S,X,GK));CG=d(Y(S,X,G7,G8));CH=d(Y(S,X,Kj,Kk));Fe=d(Y(S,X,G9,GA))
					if CF is not E and CF>0 and(CG is not E or CH is not E):
						CG=CG or j;CH=CH or j;I_=AA(j,1e2-CG-CH);Cx=CF*CG/100;J0=CF*CH/100;J1=CF*I_/100;J2=[f"Market Cap<br>₹{CF:,.2f} Cr",f"Promoters<br>₹{Cx:,.2f} Cr ({CG:.1f}%)",f"Institutional<br>₹{J0:,.2f} Cr ({CH:.1f}%)",f"Public / Other<br>₹{J1:,.2f} Cr ({I_:.1f}%)"];J3=[Cf,AE,u,Ed];J4=[0,0,0];J5=[1,2,3];J6=[Cx,J0,J1];J7=[A1(A)for A in[AE,u,Ed]];J8=C
						if Fe is not E and Cx>0:Ff=Cx*Fe/100;J9=Cx-Ff;J2+=[f"Pledged (of Promoters)<br>₹{Ff:,.2f} Cr ({Fe:.1f}%)",f"Free / Unpledged<br>₹{J9:,.2f} Cr"];J3+=[DO,D4];J4+=[1,1];J5+=[4,5];J6+=[Ff,J9];J7+=[A1(DO),A1(D4)];J8=" Promoters' holding is further split into Pledged vs Free based on Pledged %."
						JA=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=30,thickness=18,line=D(color=By,width=.5),label=J2,color=J3),link=D(source=J4,target=J5,value=J6,color=J7)));JA.update_layout(title=f"🧾 Shareholding Pattern — Who Owns {H}",template=k,height=380,margin=D(t=45,b=10,l=10,r=10),font=D(size=12));A.plotly_chart(JA,use_container_width=B,key=f"sankey_shareholding_{H}");A.caption(f'Market Cap × holding % from the Fundamentals data above. "Public / Other" absorbs whatever isn\'t reported as Promoters/Institutional (Public %, FII %, DII % show "-" for stocks where your sheet doesn\'t break those out separately).{J8}')
					else:A.info("Market Cap / shareholding % data not available for this stock, so the Shareholding Pattern flow can't be built.")
					Oc=Y(S,X,BL);Aj=d(Y(S,X,Kh,Ki,EB));CI=d(Oc)
					if CI is not E and Aj is not E and 0<=Aj<=100:Fg=CI*Aj/100;JB=CI-Fg;JC=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=30,thickness=18,line=D(color=By,width=.5),label=[f"Volume<br>{CI:,.0f} shares",f"Delivered<br>{Fg:,.0f} shares ({Aj:.1f}%)",f"Intraday / Non-Delivery<br>{JB:,.0f} shares ({100-Aj:.1f}%)"],color=[Cf,u,An]),link=D(source=[0,0],target=[1,2],value=[Fg,JB],color=[A1(u),A1(An)])));JC.update_layout(title=f"📦 Volume → Delivery Split — {H}",template=k,height=300,margin=D(t=45,b=10,l=10,r=10));A.plotly_chart(JC,use_container_width=B,key=f"sankey_volume_{H}");A.caption('Total Volume split by % Delivery into shares actually delivered (genuine buying/holding) vs. shares traded intraday and squared off same day.')
					else:A.info("Volume / % Delivery not available for this stock, so the Volume → Delivery split can't be built.")
					CJ=d(Y(S,X,CV));Fh=J
					if CJ is E and CI is not E and AL:CJ=CI*AL/1e7;Fh=B
					if CJ is not E and Aj is not E and 0<=Aj<=100:Fi=CJ*Aj/100;JD=CJ-Fi;JE=K.Figure(K.Sankey(arrangement=Bw,textfont=D(color=Ap,size=13,family=Bx),node=D(pad=30,thickness=18,line=D(color=By,width=.5),label=[f"{"Est. "if Fh else C}Turnover<br>₹{CJ:,.2f} Cr",f"Delivered Value<br>₹{Fi:,.2f} Cr ({Aj:.1f}%)",f"Intraday Value<br>₹{JD:,.2f} Cr ({100-Aj:.1f}%)"],color=[Cf,u,An]),link=D(source=[0,0],target=[1,2],value=[Fi,JD],color=[A1(u),A1(An)])));JE.update_layout(title=f"💵 Turnover → Delivery Split — {H}",template=k,height=300,margin=D(t=45,b=10,l=10,r=10));A.plotly_chart(JE,use_container_width=B,key=f"sankey_turnover_{H}");Od=" Your sheet's Turnover field is blank for this stock, so this uses an estimate (Volume × Last Close) — the same fallback this app already uses elsewhere."if Fh else C;A.caption(f"Turnover split by % Delivery, mirroring the Volume split above in ₹ terms.{Od}")
					else:A.info("Turnover / % Delivery / Volume not available for this stock, so the Turnover → Delivery split can't be built.")
					if Bc and AL is not E:JF=AL-Bc;JG=K.Figure(K.Waterfall(orientation='v',measure=['absolute','relative','total'],x=['Prev Close','Change',Kg],y=[Bc,JF,AL],text=[f"₹{Bc:,.2f}",f"{JF:+.2f}",f"₹{AL:,.2f}"],textposition='outside',textfont=D(color=Ap,size=13),increasing=D(marker=D(color=u)),decreasing=D(marker=D(color=AH)),totals=D(marker=D(color=AE)),connector=D(line=D(color=Gf))));JG.update_layout(title=f"📈 Price Change Bridge — {H} ({Dp:+.2f}%)",template=k,height=300,showlegend=J,margin=D(t=45,b=10,l=10,r=10));A.plotly_chart(JG,use_container_width=B,key=f"waterfall_price_{H}");A.caption("Prev Close → today's Price Change → Last Close. Shown as a Waterfall, not a Sankey, since a price drop can't be a negative flow.")
					else:A.info("Prev Close / Last Close not available for this stock, so the Price Change bridge can't be built.")
					if Ct is not E:JH=K.Figure(K.Indicator(mode=Ky,value=N(Ct),number=D(font=D(color=Ap,size=28)),title=D(text=f"RSI(14) — {H}",font=D(size=14)),gauge=D(axis=D(range=[0,100]),bar=D(color=AE),steps=[D(range=[0,30],color=KH),D(range=[30,70],color='#f5f5f5'),D(range=[70,100],color=Bo)],threshold=D(line=D(color=DO,width=3),value=N(Ct)))));JH.update_layout(template=k,height=260,margin=D(t=50,b=10,l=30,r=30));A.plotly_chart(JH,use_container_width=B,key=f"gauge_rsi_{H}");A.caption("Below 30 = oversold, above 70 = overbought. A gauge, not a Sankey — RSI doesn't split into parts.")
					else:A.info('RSI(14) not available for this stock.')
					Dw=N(o[EX].max())if not o.empty else E;Cy=N(o[EY].min())if not o.empty else E
					if Dw and Cy is not E and Dw>Cy and AL is not E:JI=AA(j,min(1e2,(AL-Cy)/(Dw-Cy)*100));JJ=K.Figure(K.Indicator(mode=Ky,value=JI,number=D(suffix=AC,font=D(color=Ap,size=28)),title=D(text=f"52W Range Position — {H}<br><span style='font-size:11px'>Low ₹{Cy:,.2f} · Last ₹{AL:,.2f} · High ₹{Dw:,.2f}</span>",font=D(size=14)),gauge=D(axis=D(range=[0,100]),bar=D(color=AE),steps=[D(range=[0,33],color=Bo),D(range=[33,66],color=GM),D(range=[66,100],color=CZ)],threshold=D(line=D(color=DO,width=3),value=JI))));JJ.update_layout(template=k,height=280,margin=D(t=65,b=10,l=30,r=30));A.plotly_chart(JJ,use_container_width=B,key=f"gauge_52wrange_{H}");A.caption("0% = at the 52-week low, 100% = at the 52-week high. A gauge, not a Sankey — price levels aren't a splittable quantity.")
					else:A.info('52-week High/Low/Last Close not available for this stock.')
	A.markdown(c);A.subheader('📊 National Live Market Analytics Portal Framework');Z=A.tabs(['🔥 Most Active','🚀 Volume Gainers','🏆 Top Gainers/Losers','⭐ 52W Boundaries','📦 Stocks Traded','⚖️ Advances/Declines','🕒 Pre-Open Market','⚡ Price Band Hitters','🗺️ Index Ticker Heatmap','🎫 IPO Tracker','⚠️ Volume Shockers','📂 Document Reports','🖋️ TV Script Engine','🔮 MunafaSutra Tickers','🎯 Dhan Asset Registry','💎 Weekly Activity Metrics','🔧 ScanX Core Screener','🚦 ScanX Live Engine','🎨 Screener Exploration','📈 IPO Chittorgarh','🏷️ IPO Watch Panel','💓 NSE Pulse','📊 Chartink Screeners','📋 Chartink Dashboard','🗾 Chartink Atlas','📚 Mahesh Kaushik','💰 EFTI Wealth','✅ Securities Available','🏛️ Corporate Filings','📉 52W Low Market'])
	def a(url,label='Open in Browser'):return f"<div style='margin-bottom:8px;'><a href='{url}' target='_blank' style='display:inline-block; background:#1976d2; color:#fff; font-size:14px; font-weight:600;padding:8px 18px; border-radius:6px; text-decoration:none;'>🌐 {label}</a><span style='font-size:12px; color:#888; margin-left:12px;'>📱 Mobile: tap button if frame is blank</span></div>"
	with Z[0]:I='https://www.nseindia.com/market-data/most-active-equities';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[1]:I='https://www.nseindia.com/market-data/volume-gainers-spurts';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[2]:I='https://www.nseindia.com/market-data/top-gainers-losers';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[3]:I='https://www.nseindia.com/market-data/52-week-high-equity-market';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[4]:I='https://www.nseindia.com/market-data/stocks-traded';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[5]:I='https://www.nseindia.com/market-data/advance';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[6]:I='https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[7]:I='https://www.nseindia.com/market-data/upper-band-hitters';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[8]:I='https://www.nseindia.com/index-tracker/NIFTY%2050';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[9]:I='https://www.nseindia.com/market-data/all-upcoming-issues-ipo';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[10]:I='https://www.moneycontrol.com/stocks/market-stats/volume-shockers-nse/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[11]:I='https://www.nseindia.com/all-reports/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[12]:I='https://www.tradingview.com/scripts/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[13]:I='https://munafasutra.com/nse/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[14]:I='https://dhan.co/all-stocks-list/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[15]:I='https://dhan.co/stocks/market/most-active-stocks-this-week/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[16]:I='https://scanx.trade/create-custom-screener';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[17]:I='https://scanx.trade/stock-screener/live-market-screener';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[18]:I='https://www.screener.in/explore/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[19]:I='https://www.chittorgarh.com/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[20]:I='https://ipowatch.in/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[21]:I='https://nsepulse.streamlit.app/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[22]:I='https://chartink.com/screeners';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[23]:I='https://chartink.com/scan_dashboard';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[24]:I='https://chartink.com/atlas';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[25]:I='https://www.maheshkaushik.com/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[26]:I='https://eftiwealth.com/';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none; background-color:white;"></iframe>',height=520)
	with Z[27]:I='https://www.nseindia.com/static/market-data/securities-available-for-trading';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[28]:I='https://www.nseindia.com/companies-listing/corporate-filings-announcements';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	with Z[29]:I='https://www.nseindia.com/market-data/52-week-low-equity-market';A.markdown(a(I),unsafe_allow_html=B);P.html(f'<iframe src="{I}" width="100%" height="500" style="border:none;"></iframe>',height=520)
	@DP
	def Oe():
		y='0.00%';x='Worst -> Best';w='1 Day';e='RANK';d='📊 BF Grade';b='🔬 BF Score';a='CURRENT PRICE';W='STOCK NAME';A.markdown(c);A.markdown('### 📈 Multi-Horizon Performance Summary Matrix');z,AP=A.columns([4,1])
		with z:f=A.radio(GP,[GQ,Cb,Cc],horizontal=B,help=Kz,key='perf_matrix_sizing_mode')
		g=[w,'2 Day','3 Day','5 Day','7 Day','10 Day','12 Day','15 Days','20 Days','25 Days',Gt,'2 Months','3 Months','4 Months','5 Months','6 Months','7 Months','8 Months','9 Months','10 Months','11 Months',Gu,'18 Months','1.5 Years','2 Years','2.5 Years','3 Years',r];A1,A2,A3=A.columns([2,2,3])
		with A1:h=A.selectbox('🎯 Base Horizon for Performance Ranking:',g,index=0)
		with A2:A4=A.radio('排序 Sorting Order Type:',['Best -> Worst',x],index=0,horizontal=B)
		with A3:i=A.text_input('🔍 Filter stocks inside this matrix...',placeholder=KP,key=Jw)
		V={}
		for K in g:
			if K==r:
				if C1:V[K]=C1
				continue
			k=[K.lower(),K.lower().replace(' ',C),K.lower().replace('s',C)]
			if K==w:k.append(D9)
			for X in R:
				if AX(A in X.lower()for A in k)and AC in X.lower():V[K]=X;break
		if V:
			m=[]
			for(AS,M)in L.iterrows():
				n=F(M.get(p,C)).strip();A5=M.get(A7,C)if A7 else C;A6=f"https://charting.nseindia.com/?symbol={n}-EQ";A8=f'<a href="{A6}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{n}</a>';H={W:A8,a:A5}
				for(K,A9)in V.items():
					o=F(M.get(A9,'0')).replace(AC,C).replace(AB,C).strip()
					try:H[K]=N(o)if o not in[C,A0,AQ]else j
					except AW:H[K]=j
				if BV:
					q=F(M.get(BV,'0')).replace(AC,C).replace(AB,C).strip()
					try:H[AN]=N(q)if q not in[C,A0,AQ]else j
					except AW:H[AN]=j
				if BW:
					s=F(M.get(BW,C)).replace(AC,C).replace(AB,C).strip()
					try:H[BQ]=N(s)if s not in[C,A0,AQ]else E
					except AW:H[BQ]=E
				if BX:
					t=F(M.get(BX,C)).replace(AC,C).replace(AB,C).strip()
					try:H[B3]=N(t)if t not in[C,A0,AQ]else E
					except AW:H[B3]=E
				if B6:
					u=F(M.get(B6,C)).replace(AB,C).strip()
					try:H[Ak]=N(u)if u not in[C,A0,AQ]else E
					except AW:H[Ak]=E
				if B7:
					v=F(M.get(B7,C)).replace(AB,C).strip()
					try:H[Al]=N(v)if v not in[C,A0,AQ]else E
					except AW:H[Al]=E
				if Cj:H[Br]=F(M.get(Cj,C)).strip()
				if B8:H[Bs]=F(M.get(B8,C)).strip()
				if Ck:H[Bt]=F(M.get(Ck,C)).strip()
				if DY:H[Bu]=F(M.get(DY,C)).strip()
				if B9:H[Bv]=F(M.get(B9,C)).strip()
				AD={A:B for(A,B)in M.items()if not F(A).startswith(Bq)};AE,AF,_=DS(AD,R);H[b]=AE;H[d]=AF;m.append(H)
			P=G.DataFrame(m)
			if i:P=P[P[W].str.replace(E3,C,regex=B).str.contains(i,case=J,na=J)]
			AG=h if h in P.columns else P.columns[2];AH=A4==x;P=P.sort_values(by=AG,ascending=AH).reset_index(drop=B);P.insert(0,e,P.index+1);D=P.copy()
			for K in V.keys():
				if K in D.columns:
					if K==r:D[K]=D[K].apply(lambda x:f"{T(x):,}"if G.notnull(x)else l)
					else:D[K]=D[K].apply(lambda x:f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)
			if AN in D.columns:D[AN]=D[AN].apply(lambda x:f"{x:.2f}%"if G.notnull(x)else l)
			if BQ in D.columns:D[BQ]=D[BQ].apply(lambda x:f"{x:.2f}"if G.notnull(x)else l)
			if B3 in D.columns:D[B3]=D[B3].apply(lambda x:(f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)if G.notnull(x)else l)
			if Ak in D.columns:D[Ak]=D[Ak].apply(lambda x:f"{x:,.2f}"if G.notnull(x)else l)
			if Al in D.columns:D[Al]=D[Al].apply(lambda x:f"{x:,.2f}"if G.notnull(x)else l)
			O=Ei.from_dataframe(D);O.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);O.configure_column(e,width=70,pinned=DJ);O.configure_column(W,width=140,pinned=DJ,cellRenderer=Df);AI=B4('\n            function(params) {\n                if (params.value === undefined || params.value === null || params.colDef.field === "Volume") return null;\n                let val = parseFloat(String(params.value).replace(/[+%,]/g, \'\'));\n                if (val > 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#e6f4ea\', \'fontWeight\': \'bold\' };\n                if (val < 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#fce8e6\', \'fontWeight\': \'bold\' };\n                return null;\n            }\n            ');AJ=B4(K_);AK=B4("\n            function(params) {\n                let v = String(params.value);\n                if (v.includes('STRONG BUY')) return { 'backgroundColor': '#16e37f44', 'fontWeight': 'bold' };\n                if (v.includes('WATCHLIST')) return { 'backgroundColor': '#f4b40044', 'fontWeight': 'bold' };\n                if (v.includes('CAUTION')) return { 'backgroundColor': '#ff990044' };\n                return { 'backgroundColor': '#ea433544' };\n            }\n            ");AL=B4(L0)
			for I in D.columns:
				if I in(e,):continue
				if f==Cb and Q(D)>0:Y=B_(D.iloc[0][I]);Z=Q(F(I));S=T(AA(Y,Z)*7+22)
				elif f==Cc and Q(D)>1:Y=B_(D.iloc[1][I]);Z=Q(F(I));S=T(AA(Y,Z)*7+22)
				else:AM={W:140,a:130,AN:110,b:110,d:160,BQ:100,B3:140,Ak:110,Al:110,Br:120,Bs:130,Bt:130,Bu:130,Bv:130};S=AM.get(I,130)
				U=AA(70,min(S,90))
				if I==W:O.configure_column(I,width=S,minWidth=U,pinned=DJ,cellRenderer=Df)
				elif I==a:O.configure_column(I,width=S,minWidth=U)
				elif I==b:O.configure_column(I,width=S,minWidth=U,cellStyle=AJ)
				elif I==d:O.configure_column(I,width=S,minWidth=U,cellStyle=AK)
				elif I in(Br,Bs,Bt,Bu,Bv):O.configure_column(I,width=S,minWidth=U,cellStyle=AL)
				elif I in V or I==B3:O.configure_column(I,width=S,minWidth=U,cellStyle=AI)
				else:O.configure_column(I,width=S,minWidth=U)
			O.configure_grid_options(domLayout=AR,rowHeight=38,headerHeight=45,enableCellTextSelection=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AO=O.build();Eh(D,gridOptions=AO,theme=GR,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=450,width=GS,key='horizon_perf_grid')
	Oe()
	@DP
	def Of():
		m='Key Reasons';k='Score (High→Low)';W='Score';A.markdown(c);A.markdown('### 🔬 Bottom Fishing Scanner — Buy from Bottom Candidates');A.caption('Stocks that are 8–15% above 52W Low, in uptrend, with high volume + strong fundamentals');n,AI=A.columns([4,1])
		with n:a=A.radio(GP,[GQ,Cb,Cc],horizontal=B,help=Kz,key='bf_scanner_sizing_mode')
		o,q,r=A.columns([2,2,2])
		with o:X=A.slider('Minimum BF Score:',min_value=0,max_value=100,value=55,step=5,key='bf_min_score')
		with q:s=A.radio('Sort by:',[k,'Score (Low→High)'],horizontal=B,key='bf_sort')
		with r:b=A.text_input(KO,placeholder='e.g. WIPRO',key=Jx)
		K=[]
		for(AJ,d)in L.iterrows():
			D={A:B for(A,B)in d.items()if not F(A).startswith(Bq)};e,t,u=DS(D,R)
			if e>=X:
				g=F(d.get(p,C)).strip();v=D.get(A7,C)if A7 else C;h=U((A for A in R if EF in A.lower()),E);w=D.get(h,C)if h else C;x=f"https://charting.nseindia.com/?symbol={g}-EQ";y=f'<a href="{x}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{g}</a>';P=E
				if BV:
					i=F(D.get(BV,C)).replace(AC,C).replace(AB,C).strip()
					try:P=N(i)if i not in[C,A0,AQ]else E
					except AW:P=E
				z=F(D.get(BW,C)).strip()if BW else l;A1=F(D.get(BX,C)).strip()if BX else l;A2=F(D.get(B6,C)).strip()if B6 else l;A3=F(D.get(B7,C)).strip()if B7 else l;A4=F(D.get(Cj,C)).strip()if Cj else l;A5=F(D.get(B8,C)).strip()if B8 else l;A6=F(D.get(Ck,C)).strip()if Ck else l;A8=F(D.get(DY,C)).strip()if DY else l;A9=F(D.get(B9,C)).strip()if B9 else l;K.append({f:y,W:e,GY:t,AO:v,BQ:z,AN:f"{P:.2f}%"if P is not E else l,B3:A1,Ak:A2,Al:A3,Br:A4,Bs:A5,Bt:A6,Bu:A8,Bv:A9,Gg:F(w)[:30],m:' | '.join(u[:3])})
		if b:K=[A for A in K if b.upper()in re.sub(E3,C,A[f]).upper()]
		K.sort(key=lambda x:x[W],reverse=s==k)
		if K:
			A.success(f"✅ Found **{Q(K)}** stocks matching your bottom-fishing criteria (score ≥ {X})");I=G.DataFrame(K);M=Ei.from_dataframe(I);M.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);AD=B4(K_);AE=B4(L0);AF={f:120,W:90,GY:160,AO:100,AN:110,Gg:200,m:400,BQ:100,B3:140,Ak:110,Al:110,Br:120,Bs:130,Bt:130,Bu:130,Bv:130}
			for H in I.columns:
				if a==Cb and Q(I)>0:Y=B_(I.iloc[0][H]);Z=Q(F(H));O=T(AA(Y,Z)*7+22)
				elif a==Cc and Q(I)>1:Y=B_(I.iloc[1][H]);Z=Q(F(H));O=T(AA(Y,Z)*7+22)
				else:O=AF.get(H,120)
				S=DJ if H==f else E;V=AA(70,min(O,90))
				if H==W:M.configure_column(H,width=O,minWidth=V,pinned=S,cellStyle=AD)
				elif H==f:M.configure_column(H,width=O,minWidth=V,pinned=S,cellRenderer=Df)
				elif H in(Br,Bs,Bt,Bu,Bv):M.configure_column(H,width=O,minWidth=V,pinned=S,cellStyle=AE)
				else:M.configure_column(H,width=O,minWidth=V,pinned=S)
			M.configure_grid_options(domLayout=AR,rowHeight=40,headerHeight=45,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AG=M.build();Eh(I,gridOptions=AG,theme=GR,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=400,width=GS,key='bf_scanner_grid');j=io.BytesIO()
			with G.ExcelWriter(j,engine=DG)as AH:H5(I).to_excel(AH,index=J,sheet_name='Bottom Fishing')
			A.download_button('📥 Download BF Scanner Results',data=j.getvalue(),file_name=f"BottomFishing_{G.Timestamp.now().strftime(Bm)}.xlsx",mime=Bn)
		else:A.info(f"No stocks found with BF Score ≥ {X}. Try lowering the minimum score.")
	Of()
	if AK:
		A.markdown(c);A.markdown('### 🏆 Top 10 & Bottom 10 Performers (Daily badges)');CK=L.copy();CK[AK]=G.to_numeric(CK[AK].astype(F).str.replace(BK,C,regex=B),errors=AP);CK=CK.dropna(subset=[AK]);Og=CK.nlargest(10,AK);Oh=CK.nsmallest(10,AK);As,At=A.columns(2)
		with As:
			JK="<h4 style='margin-top:0px; margin-bottom:8px;'>⬆️ Top 10 (Daily)</h4>"
			for(_,Bh)in Og.iterrows():
				Cz=F(Bh.get(p,C)).strip();AG=Bh[AK];C_=Bh.get(A7,C)if A7 else C
				try:Bi=N(F(C_).replace(AB,C).strip());Fj=N(AG);Fk=Bi/(1+Fj/100);Fl=Bi-Fk;D0=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>+{Fl:,.2f}</span>";D1=f"₹{Bi:,.2f}"
				except:D1=f"₹{C_}";D0=C
				Fm=f"https://charting.nseindia.com/?symbol={Cz}-EQ";JK+=f"<a href='{Fm}' target='_blank' style='text-decoration:none;'><div style='background-color:#16e37f; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cz}: +{AG}%</span><span>{D0}{D1}</span></div></a>"
			A.markdown(JK,unsafe_allow_html=B)
		with At:
			JL="<h4 style='margin-top:0px; margin-bottom:8px;'>⬇️ Bottom 10 (Daily)</h4>"
			for(_,Bh)in Oh.iterrows():
				Cz=F(Bh.get(p,C)).strip();AG=Bh[AK];C_=Bh.get(A7,C)if A7 else C
				try:Bi=N(F(C_).replace(AB,C).strip());Fj=N(AG);Fk=Bi/(1+Fj/100);Fl=Bi-Fk;D0=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>{Fl:,.2f}</span>";D1=f"₹{Bi:,.2f}"
				except:D1=f"₹{C_}";D0=C
				Fm=f"https://charting.nseindia.com/?symbol={Cz}-EQ";JL+=f"<a href='{Fm}' target='_blank' style='text-decoration:none;'><div style='background-color:#f39991; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cz}: {AG}%</span><span>{D0}{D1}</span></div></a>"
			A.markdown(JL,unsafe_allow_html=B)
	A.markdown(c);A.markdown('### 📰 Global Market News, Alerts & Corporate Announcements');import urllib.request,urllib.parse,xml.etree.ElementTree as C7,pandas as G
	def Dx(pubdate_str):
		try:
			D=G.to_datetime(pubdate_str,utc=B);H=G.Timestamp.now(tz=BR);A=(H-D).total_seconds()
			if A<0:return AI
			if A<60:return f"{T(A)} secs ago"
			if A<3600:E=T(A/60);return f"{E} min{"s"if E!=1 else C} ago"
			if A<86400:F=T(A/3600);return f"{F} hour{"s"if F!=1 else C} ago"
			if A<172800:return f"Yesterday ({D.strftime(EQ)})"
			I=T(A/86400);return f"{I} days ago ({D.strftime(EQ)})"
		except h:return GZ
	@A.cache_data(ttl=600)
	def Oi(symbol,limit=10):
		try:
			J=f'"{symbol}" NSE AND ("52 week high" OR "52 week low" OR "upper circuit" OR "lower circuit")';K=urllib.parse.quote(J);L=f"https://news.google.com/rss/search?q={K}&hl=en-IN&gl=IN&ceid=IN:en";N=urllib.request.Request(L,headers={Cd:Ce})
			with urllib.request.urlopen(N)as O:P=O.read()
			Q=C7.fromstring(P);R=[DE,ER,CX,ES,ET,EU,EV,EW];D=[]
			for A in Q.findall(DM):
				F=A.find(A5).text
				if not AX(A in F.lower()for A in R):continue
				S=A.find(g).text;I=A.find(Ao).text if A.find(Ao)is not E else C
				try:H=G.to_datetime(I,utc=B)
				except h:H=G.Timestamp.now(tz=BR)-G.Timedelta(days=100)
				T=G.Timestamp.now(tz=BR);U=(T-H).total_seconds()/86400
				if U<=15.:V=Dx(I);D.append({AD:f"🚨 **[ALERT]** {F}",g:S,M:V,AJ:H,L1:F})
			D.sort(key=lambda x:x[AJ],reverse=B);return D[:limit]
		except h:return[]
	@A.cache_data(ttl=600)
	def Oj(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";L=urllib.request.Request(K,headers={Cd:Ce})
			with urllib.request.urlopen(L)as N:O=N.read()
			P=C7.fromstring(O);D=[];Q=[DE,ER,CX,ES,ET,EU,EV,EW,L2,L3]
			for A in P.findall(DM):
				H=A.find(A5).text;R=A.find(g).text;I=A.find(Ao).text if A.find(Ao)is not E else C;S=AX(A in H.lower()for A in Q);T=Ga if S else C;U=f"{T}{H}"
				try:F=G.to_datetime(I,utc=B)
				except h:F=G.Timestamp.now(tz=BR)-G.Timedelta(days=100)
				V=G.Timestamp.now(tz=BR);W=(V-F).total_seconds()/86400
				if W<=Am:X=Dx(I);D.append({AD:U,g:R,M:X,AJ:F})
			D.sort(key=lambda x:x[AJ],reverse=B);return D[:limit]
		except h:return[]
	@A.cache_data(ttl=600)
	def Ok(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";L=urllib.request.Request(K,headers={Cd:Ce})
			with urllib.request.urlopen(L)as N:O=N.read()
			P=C7.fromstring(O);D=[];Q=[DE,ER,CX,ES,ET,EU,EV,EW,L2,L3]
			for A in P.findall(DM):
				F=A.find(A5).text;R=A.find(g).text;H=A.find(Ao).text if A.find(Ao)is not E else C;S=AX(A in F.lower()for A in Q);T=Ga if S else C;U=f"{T}{F}"
				try:I=G.to_datetime(H,utc=B)
				except h:I=G.Timestamp.now(tz=BR)-G.Timedelta(days=100)
				V=Dx(H);D.append({AD:U,g:R,M:V,AJ:I})
			D.sort(key=lambda x:x[AJ],reverse=B);return D[:limit]
		except h:return[]
	@A.cache_data(ttl=600)
	def Ol(symbol,limit=6):
		try:
			I=f'"{symbol}" AND ("Regulation 30" OR "LODR" OR "Board Meeting" OR "AGM" OR "Analyst Meet" OR "Financial Results" OR "Corporate Action" OR "Dividend")';J=urllib.parse.quote(I);K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";L=urllib.request.Request(K,headers={Cd:Ce})
			with urllib.request.urlopen(L)as N:O=N.read()
			P=C7.fromstring(O);D=[]
			for A in P.findall(DM):
				Q=A.find(A5).text;R=A.find(g).text;F=A.find(Ao).text if A.find(Ao)is not E else C
				try:H=G.to_datetime(F,utc=B)
				except h:H=G.Timestamp.now(tz=BR)-G.Timedelta(days=100)
				S=Dx(F);D.append({AD:f"📢 {Q}",g:R,M:S,AJ:H})
			D.sort(key=lambda x:x[AJ],reverse=B);return D[:limit]
		except h:return[]
	Om={'RELIANCE':'500325','TCS':'532540','HDFCBANK':'500180','INFY':L7,'ICICIBANK':'532174','HINDUNILVR':'500696','SBIN':'500112','BHARTIARTL':'532454','BAJFINANCE':'500034','KOTAKBANK':'500247','LT':'500510','HCLTECH':'532281','AXISBANK':'532215','ASIANPAINT':'500820','MARUTI':'532500',L4:L8,'TITAN':'500114','ULTRACEMCO':'532538','ONGC':'500312','NTPC':'532555','POWERGRID':'532898','WIPRO':'507685','NESTLEIND':'500790','JSWSTEEL':'500228','TATASTEEL':'500470','TATAMOTORS':'500570','TECHM':'532755','GRASIM':'500300','ADANIENT':'512599','ADANIPORTS':'532921','COALINDIA':'533278','DIVISLAB':L9,'DRREDDY':'500124','EICHERMOT':'505200','BAJAJFINSV':'532978','BAJAJ-AUTO':'532977','CIPLA':'500087','BRITANNIA':'500825','HEROMOTOCO':'500182',L5:LA,'HINDALCO':'500440','UPL':'512070','TATACONSUM':'500800','SBILIFE':'540719','HDFCLIFE':'540777','INDUSINDBK':'532187','BPCL':'500547','IOC':'530965','M&M':'500520','PIDILITIND':'500331','SIEMENS':'500550','HAVELLS':'517354','VOLTAS':'500575','AMBUJACEM':'500425','ACC':'500410','SHREECEM':'500387','RAMCOCEM':LB,L6:LC,'JKCEMENT':'532644','STAR':LD,'TVSMOTOR':'532343','BOSCHLTD':'500530','MUTHOOTFIN':'533398','CHOLAFIN':'500443','BAJAJHLDNG':'500490','TORNTPHARM':LE,'AUROPHARMA':'524208','LUPIN':'500257','BIOCON':'532523','ALKEM':'539523','IPCALAB':'530827','GLAXO':'500660','ABBOTINDIA':'500488','PFIZER':'500680','SANOFI':'500674','MCDOWELL-N':'532432','ITC':'500875','GODFRYPHLP':'500163','COLPAL':'500830','DABUR':'500096','MARICO':'531642','GODREJCP':'532424','HINDPETRO':'500104','CASTROLIND':'500870','INDIGO':'521737','INTERGLOBE':'539448','SPICEJET':'500285','IRCTC':'542830','CONCOR':'531344','ADANIGREEN':'541450','ADANITRANS':'539254','TATAPOWER':'500400','TORNTPOWER':'532779','CESC':'500084','NHPC':'533098','SJVN':'533206','PFC':'532810','RECLTD':'532955','IRFC':'543257','ZOMATO':'543320','NYKAA':'543384','PAYTM':'543396','POLICYBZR':'543390','DELHIVERY':'543529','CARTRADE':'543202','RVNL':'542649','IRCON':'541956','NBCC':'534309','HUDCO':'540530','MMTC':LF,'MTNL':'500108','BEL':'500049','HAL':'541154','COCHINSHIP':'526235','MAZAGON':'543237','GRSE':'542351','MIDHANI':'541195','BEML':'500048','BHEL':'500103','SAIL':'500113','NMDC':'526371','MOIL':'533286','NATIONALUM':'532234','HINDZINC':'500188','VEDL':'500295','GMRINFRA':'532754','NHAI':'500253','IRB':'532947','ASHOKLEY':'500477','ESCORTS':'500495','FORCE':'517168','SML':'513275','MOTHERSON':'517334','MINDAIND':'532539','ENDURANCE':'540350','BALKRISIND':'502355','APOLLOTYRE':'500877','MRF':'500290','CEATLTD':'500878','JK TYRE':'530007','INOXWIND':'539083','SUZLON':'532667','RPOWER':'500390','JPPOWER':'532627','FEDERALBNK':'500469','IDFCFIRSTB':'539437','BANDHANBNK':'541153','RBLBANK':'540065','DCBBANK':'532772','KTKBANK':LG,'SOUTHBANK':'532218','CANBK':'532483','BANKBARODA':'532134','UNIONBANK':'532477','INDIANB':'532814','UCOBANK':'532505','CENTRALBK':'532885','MAHABANK':'532525','J&KBANK':LG,'PNB':'532461','IOB':'532388','BANKINDIA':'532149','DENABANK':'532121','SYNDIBANK':'532276','VIJAYABANK':'532245','ORIENTBANK':'500315','CORPBANK':'532179','ANDHRABANK':'532418','ALLAHABAD':LH,'ALBK':LH,'MFSL':'542299','HDFCAMC':'541530','NIPPONLIFE':'543171','UTIAMC':'543238','ABCAPITAL':'540691','ANGELONE':'543235','ICICIGI':'540716','GICRE':'540755','NIACL':'540769','STAR':LD,'CROMPTON':'539876','ORIENTELEC':'531637','BLUESTAR':'500067','WHIRLPOOL':'500238','VGUARD':'532953','BAJAJEL':'500031','CERA':'532443','HINDWARE':'509820','HSIL':'509675','KAJARIACER':'500233','SOMANYCER':'532622','GRINDWELL':'506076','CARBORUNIV':'513375','ASTRAL':'532830','FINOLEX':'500940','SUPREMEIND':'509930','BERGER':'509480','KANSAINER':'500165','AKZOINDIA':'500710','INDIACEM':'530005','RAMCOIND':LB,L6:LC,'HEIDELBERG':'500292','PRISM':'500338','BIRLACORPN':'500335','ORIENTCEM':'502420','SAGCEM':'502090','STARCEMENT':'540575','JKLAKSHMI':'500380','NUVOCO':'543334','ZYDUSLIFE':'532321','TORNTPHAR':LE,'NATCOPHAR':'524816','GRANULES':'532482','LAURUS':LI,'STRIDES':'532531','AJANTPHAR':'532331','CAPLIPOINT':'539266','DIVI':L9,L4:L8,'GLAND':'543245','SEQUENT':'543225','METROPOLIS':'542650','DRLAL':'532259','THYROCARE':'539871','KRSNAA':'543328','VIJAYA':'532542','MAXHEALTH':'543220','KIMS':'543308','ASTER':'540975','FORTIS':'532843','NHOSPIT':'532526',L5:LA,'NARAYANA':'539551','YATHARTH':'544120','RAINBOW':'543524','SUVENPHAR':'530239','LAURUSLABS':LI,'SOLARA':'541540','SHILPAMED':'530879','PERSISTENT':'533179','MINDTREE':'532819','MPHASIS':'526299','HEXAWARE':'532861','NIIT':'500304','KPIT':'542651','LTTS':'540115','COFORGE':'532541','ZENSAR':'504067','RAMSYSTEMS':'532370','MASTEK':'523704','SASKEN':'532663','TATAELXSI':'500408','CYIENT':'532175','SONATSOFTW':'532221','TANLA':'532790','LTIM':'540005','INFY':L7,'ROUTE':'543228','BSOFT':'526301','NEWGEN':'540900','INTELLECT':'538835','NUCLEUS':'531209','NELCO':'504112','DELTACORP':'532840','WONDERLA':'538268','MAHINDCIE':'532756','STARHLTH':'543412','NAUKRI':'532777','JUSTDIAL':'535648','MATRIMONY':'539846','MAKEMYTRIP':LF,'IXIGO':'544229','RATEGAIN':'543417','TEAMLEASE':'539658','QUESS':'539978','SIS':'540673','SECURKLOUD':'539963','HAPPYFORGE':'543532','KALYANKJIL':'543278','SENCO':'543456','THANGAMAYL':'531509','TRIBHOVAND':'512415','PC JEWELLER':'534809','RAJESHEXPO':'531500'}
	@A.cache_data(ttl=600)
	def On(bse_code,days_back=90):
		L='SUBCATNAME';A={Gv:[],Gw:[],Gx:[],Gy:[],Ee:[]}
		try:
			import datetime as F;H=F.date.today();M=H-F.timedelta(days=days_back);N=M.strftime(Bm);O=H.strftime(Bm);P=f"https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w?pageno=1&strCat=-1&strPrevDate={N}&strScrip={bse_code}&strSearch=P&strToDate={O}&strType=C&subcategory=-1";Q={Cd:Ce,'Referer':'https://www.bseindia.com/','Accept':'application/json'};R=urllib.request.Request(P,headers=Q)
			with urllib.request.urlopen(R,timeout=8)as S:T=Eg.loads(S.read())
			for B in(T.get('Table')or[])[:30]:
				U=B.get('HEADLINE',C)or B.get(L,C);I=B.get('NEWS_DT',C)or B.get('DT_TM',C);J=B.get('NEWSID',C);V=f"https://www.bseindia.com/xml-data/corpfiling/AttachLive/{J}.pdf"if J else C
				try:K=G.to_datetime(I).strftime(EQ)
				except h:K=I[:10]
				E=(B.get(L)or C).lower();D={A5:U,g:V,BN:K}
				if AX(A in E for A in['annual report','annual rep']):A[Gw].append(D)
				elif AX(A in E for A in['credit rat','rating']):A[Gx].append(D)
				elif AX(A in E for A in['concall','con call','earnings call','analyst']):A[Gy].append(D)
				elif AX(A in E for A in['investor presentation','presentation',Ee]):A[Ee].append(D)
				else:A[Gv].append(D)
		except h:pass
		return A
try:
	CL=L[p].dropna().unique()
	if Q(CL)>0:
		Oo,Op,Oq,Or,Os,Ot,Ou=A.tabs(['🚨 Latest Alerts Timeline','🏢 Alerts by Stock','📰 Smart News Engine (1 Day)','📰 Smart News Engine (All News)','📢 Corporate Announcements','📢 DOCUMENTS HUB','📜 Rules']);D2=[];JM=CL[:30]
		with A.spinner('Scanning Top 30 stocks for Circuit & 52-Week Breakouts (15 Days)...'):
			for H in JM:
				A2=F(H).strip();BF=Oi(A2,limit=15)
				for Az in BF:Az[Aa]=A2;D2.append(Az)
		Ov={A[Aa]for A in D2};JN={A[Aa]for A in D2 if Ac in A[M]or Ad in A[M]or Ae in A[M]or AI in A[M]}
		def Ow(sym):
			A=sym
			if A in JN:B,C,D=Ab,'#003300','#0fbf62'
			elif A in Ov:B,C,D='#1a7a45',D6,'#145e34'
			else:B,C,D='#444',D6,'#333'
			return f"<span style='background:{B}; color:{C}; padding:2px 9px; border-radius:5px; font-weight:700; font-size:0.82em; border:1px solid {D}; white-space:nowrap;'>⚡ {A}</span>"
		with Oo:
			Ox,Oy,Oz=A.columns([2,1,1]);JO=Ox.text_input('🔍 Search Alerts:',placeholder='e.g. ICICIBANK, circuit...',key='global_news_search');JP=Oy.selectbox('⏳ Time Filter:',['All (Up to 15 Days)',LJ,LK],key='global_news_time');O_=Oz.radio('↕️ Sort By Time:',[LL,'Oldest First'],horizontal=B,key='global_news_sort');A_=D2.copy()
			if JO:JQ=JO.lower();A_=[A for A in A_ if JQ in A[Aa].lower()or JQ in A[L1].lower()]
			if JP==LK:A_=[A for A in A_ if Ac in A[M]or Ad in A[M]or Ae in A[M]or AI in A[M]]
			elif JP==LJ:P0=G.Timestamp.now(tz=BR);A_=[A for A in A_ if(P0-A[AJ]).total_seconds()/86400<=7.]
			A_.sort(key=lambda x:x[AJ],reverse=O_==LL);A.markdown(Ca,unsafe_allow_html=B)
			if A_:
				for O in A_:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;P1=Ow(O[Aa]);A.markdown(f"- {P1}&nbsp; <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.4em 0; opacity: 0.15;'>",unsafe_allow_html=B)
			else:A.info('No circuit or 52-week alerts match your search or filter criteria.')
		with Op:
			P2=A.columns(2);Fn=0
			for A2 in[F(A).strip()for A in JM]:
				Dy=[A for A in D2 if A[Aa]==A2];Dy.sort(key=lambda x:x[AJ],reverse=B)
				if Dy:
					with P2[Fn%2]:
						P3='🟢'if A2 in JN else'🟡'
						with A.expander(f"{P3} {A2} Action Alerts (0 Sec to 15 Days)",expanded=B):
							P4=Dy[:3];Fo=Dy[3:]
							for O in P4:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B)
							if Fo:
								with A.expander(f"🔽 Show {Q(Fo)} more older alerts",expanded=J):
									for O in Fo:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B)
					Fn+=1
			if Fn==0:A.info('No circuit breakouts or 52-week boundary alerts for the currently filtered stocks in the last 15 days.')
		with Oq:
			A.markdown('### Latest News & Action Alerts (Past 24 Hours)');P5=A.columns(2);Fp=0
			for D3 in CL[:10]:
				A2=F(D3).strip();BF=Oj(A2,limit=5)
				if BF:
					with P5[Fp%2]:
						with A.expander(f"📰 {A2} News Feed (0 Sec to 1 Day)",expanded=B):
							for O in BF:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B)
					Fp+=1
			if Fp==0:A.info('No general news found for the currently filtered stocks in the last 24 hours.')
		with Or:
			A.markdown('### Latest News & Action Alerts (All Time)');P6=A.columns(2);Fq=0
			for D3 in CL[:10]:
				A2=F(D3).strip();BF=Ok(A2,limit=6)
				if BF:
					with P6[Fq%2]:
						with A.expander(f"📰 {A2} News Feed (All News)",expanded=B):
							P7=BF[:3];Fr=BF[3:]
							for O in P7:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B)
							if Fr:
								with A.expander(f"🔽 Show {Q(Fr)} more articles",expanded=J):
									for O in Fr:i=Ac in O[M]or Ad in O[M]or Ae in O[M]or AI in O[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{O[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{O[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {O[M]}</span>",unsafe_allow_html=B)
					Fq+=1
			if Fq==0:A.info('No general news found for the currently filtered stocks.')
		with Os:
			A.markdown('### 📢 Official Exchange Filings & Corporate Announcements');A.markdown("<span style='font-size: 0.9em; color: gray;'>Tracks Regulation 30, LODR, Board Meetings, AGMs, and Analyst Meets.</span>",unsafe_allow_html=B);A.markdown(Ca,unsafe_allow_html=B);P8=A.columns(2);Fs=0
			for D3 in CL[:15]:
				A2=F(D3).strip();Ft=Ol(A2,limit=7)
				if Ft:
					with P8[Fs%2]:
						with A.expander(f"📢 {A2} Filings & Announcements",expanded=B):
							P9=Ft[:3];Fu=Ft[3:]
							for A3 in P9:i=Ac in A3[M]or Ad in A3[M]or Ae in A3[M]or AI in A3[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{A3[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{A3[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {A3[M]}</span>",unsafe_allow_html=B)
							if Fu:
								with A.expander(f"🔽 Show {Q(Fu)} more filings",expanded=J):
									for A3 in Fu:i=Ac in A3[M]or Ad in A3[M]or Ae in A3[M]or AI in A3[M];v=Ab if i else B2;w=AS if i else AR;A.markdown(f"- <a href='{A3[g]}' target='_blank' style='text-decoration: none; color: inherit;'>{A3[AD]}</a> <span style='color: {v}; font-weight: {w}; font-size: 0.85em;'>— 🕒 {A3[M]}</span>",unsafe_allow_html=B)
					Fs+=1
			if Fs==0:A.info('No recent corporate filings or official announcements found for the filtered stocks.')
		with Ot:
			A.markdown('### 📄 Documents Hub — Announcements · Annual Reports · Credit Ratings · Concalls · PPT · REC');A.markdown("<span style='font-size:0.88em; color:#888;'>Live BSE India filings (public API, no key needed). Annual Reports & Concalls also link to Screener.in.</span>",unsafe_allow_html=B);A.markdown(Ca,unsafe_allow_html=B);PA,PB,PC=A.columns([3,1.2,1.2])
			with PA:JR=[F(A).strip()for A in CL[:60]];JS=A.multiselect('🔍 Stocks to view:',options=JR,default=JR[:4],key='doc_hub_stocks_v2')
			with PB:PD=A.selectbox('📅 Date range:',[Gt,LM,LN,Gu],index=1,key='doc_days_v2')
			with PC:JT=A.selectbox('📋 Rows per section:',[3,5,8,12],index=1,key='doc_limit_v2')
			PE={Gt:30,LM:90,LN:180,Gu:365};PF=PE[PD]
			if not JS:A.info('Select at least one stock above to view its documents.')
			else:
				for q in JS:
					y=Om.get(q.upper(),C)
					with A.expander(f"📁  {q}   {"· BSE "+y if y else"· BSE code not mapped — Screener links shown"}",expanded=B):
						Fv="<div style='display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;'>";PG=[('📢 BSE Announcements',f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={y}"if y else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={q}",LO,LP),('📑 Annual Reports',f"https://www.screener.in/company/{q}/",CZ,LQ),('⭐ Credit Ratings',f"https://www.screener.in/company/{q}/",GM,'#f57f17'),('🎙️ Concalls',f"https://www.screener.in/company/{q}/",'#fce4ec',DO),('📊 Investor PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={y}"if y else f"https://www.screener.in/company/{q}/",LR,LS),('🏛️ NSE Filings',f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={q}",'#e0f7fa','#00695c'),('📈 Screener',f"https://www.screener.in/company/{q}/",'#fffde7',An)]
						for(Fw,Fx,Fy,Fz)in PG:Fv+=f"<a href='{Fx}' target='_blank' style='background:{Fy}; color:{Fz}; padding:5px 12px; border-radius:6px; font-size:0.78em; font-weight:600; text-decoration:none; white-space:nowrap;'>{Fw}</a>"
						Fv+=D5;A.markdown(Fv,unsafe_allow_html=B);CM={}
						if y:
							with A.spinner(f"Fetching BSE filings for {q}…"):CM=On(y,days_back=PF)
						PH,PI,PJ,PK=A.columns([3,2,2,3])
						with PH:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #5c6bc0; padding-bottom:4px; color:#5c6bc0;'>📢 Announcements</p>",unsafe_allow_html=B);JU=CM.get(Gv,[])
							if JU:
								PL,PM=A.tabs([GZ,'All ↗'])
								with PL:
									for CN in JU[:JT]:BG=CN[A5][:85]+'…'if Q(CN[A5])>85 else CN[A5];Bj=f"<a href='{CN[g]}' target='_blank' style='color:#5c6bc0; text-decoration:none;'>{BG}</a>"if CN[g]else f"<span>{BG}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:6px; border-left:3px solid #c5cae9; padding-left:6px;'>{Bj}<br><span style='color:#aaa; font-size:0.85em;'>{CN[BN]}</span></div>",unsafe_allow_html=B)
								with PM:PN=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={y}"if y else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={q}";A.markdown(f"<a href='{PN}' target='_blank' style='color:#5c6bc0; font-size:0.85em;'>🔗 Open full announcements page →</a>",unsafe_allow_html=B)
							else:PO=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={y}"if y else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={q}";A.markdown(f"<a href='{PO}' target='_blank' style='color:#5c6bc0; font-size:0.83em;'>🔗 View on {"BSE"if y else"NSE"} →</a>",unsafe_allow_html=B);A.caption('No announcements in selected date range.')
						with PI:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #43a047; padding-bottom:4px; color:#43a047;'>📑 Annual Reports</p>",unsafe_allow_html=B);JV=CM.get(Gw,[])
							if JV:
								for Dz in JV[:6]:JW=Dz[BN][:4]if Dz[BN]else'Report';Bj=f"<a href='{Dz[g]}' target='_blank' style='color:#43a047; text-decoration:none;'>📄 Annual Report {JW}</a>"if Dz[g]else f"<span>📄 Annual Report {JW}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px;'>{Bj}</div>",unsafe_allow_html=B)
							else:
								if y:A.markdown(f"<a href='https://www.bseindia.com/AnnualReports.html?scripcd={y}' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 BSE Annual Reports →</a>",unsafe_allow_html=B)
								A.markdown(f"<a href='https://www.screener.in/company/{q}/' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 View on Screener →</a>",unsafe_allow_html=B);A.caption('Not found in selected range — try 1 Year.')
						with PJ:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #f57f17; padding-bottom:4px; color:#f57f17;'>⭐ Credit Ratings</p>",unsafe_allow_html=B);JX=CM.get(Gx,[])
							if JX:
								for CO in JX[:4]:BG=CO[A5][:70]+'…'if Q(CO[A5])>70 else CO[A5];Bj=f"<a href='{CO[g]}' target='_blank' style='color:#f57f17; text-decoration:none;'>{BG}</a>"if CO[g]else f"<span>{BG}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffe0b2; padding-left:6px;'>{Bj}<br><span style='color:#aaa; font-size:0.85em;'>{CO[BN]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{q}/' target='_blank' style='color:#f57f17; font-size:0.83em;'>⭐ Ratings on Screener →</a>",unsafe_allow_html=B);A.markdown("<div style='font-size:0.78em; margin-top:8px; color:#888;'><a href='https://www.careratings.com' target='_blank' style='color:#888;'>CARE</a> · <a href='https://www.icra.in' target='_blank' style='color:#888;'>ICRA</a> · <a href='https://www.crisil.com' target='_blank' style='color:#888;'>CRISIL</a> · <a href='https://www.infomerics.com' target='_blank' style='color:#888;'>Infomerics</a></div>",unsafe_allow_html=B);A.caption('Not found via BSE — check links above.')
						with PK:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #e53935; padding-bottom:4px; color:#e53935;'>🎙️ Concalls &amp; Investor Docs</p>",unsafe_allow_html=B);PP=CM.get(Gy,[]);JY=CM.get(Ee,[]);JZ=JY+PP
							if JZ:
								for Bk in JZ[:JT]:PQ=Bk in JY;Ja='📊'if PQ else'🎙️';BG=Bk[A5][:70]+'…'if Q(Bk[A5])>70 else Bk[A5];Bj=f"<a href='{Bk[g]}' target='_blank' style='color:#e53935; text-decoration:none;'>{Ja} {BG}</a>"if Bk[g]else f"<span>{Ja} {BG}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffcdd2; padding-left:6px;'>{Bj}<br><span style='color:#aaa; font-size:0.85em;'>{Bk[BN]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{q}/' target='_blank' style='color:#e53935; font-size:0.83em;'>🎙️ Concalls on Screener →</a>",unsafe_allow_html=B);A.caption('No concalls/PPT in selected date range.')
							A.markdown(Ca,unsafe_allow_html=B);F_="<div style='display:flex; gap:6px; flex-wrap:wrap;'>";PR=[('📝 Transcript',f"https://www.screener.in/company/{q}/",LO,LP),('🤖 AI Summary',f"https://www.screener.in/company/{q}/",CZ,LQ),('📊 PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={y}"if y else f"https://www.screener.in/company/{q}/",LR,LS),('▶️ REC',f"https://www.youtube.com/results?search_query={q}+concall+earnings",Bo,DH)]
							for(Fw,Fx,Fy,Fz)in PR:F_+=f"<a href='{Fx}' target='_blank' style='background:{Fy}; color:{Fz}; padding:3px 10px; border-radius:4px; font-size:0.76em; font-weight:600; text-decoration:none;'>{Fw}</a>"
							F_+=D5;A.markdown(F_,unsafe_allow_html=B)
		with Ou:A.markdown('### 📜 Trading Rules');A.markdown("<span style='font-size:0.88em; color:#888;'>Edit the <code>TRADING_RULES_LIBRARY</code> constant near the top of the .py file to change anything shown below — same pattern as the AI Prompt Library &amp; Pine Script Custom Rules Library.</span>",unsafe_allow_html=B);A.markdown(Ca,unsafe_allow_html=B);A.markdown(La)
	else:A.info('No stocks currently filtered to check.')
except h as Bb:A.error(f"⚠️ Could not load the News Engine. Error details: {Bb}")
else:A.warning('No data loaded. Check sheet sharing and secrets.')
