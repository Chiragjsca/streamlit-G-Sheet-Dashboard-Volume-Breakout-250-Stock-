LA='#6a1b9a'
L9='#f3e5f5'
L8='#2e7d32'
L7='#3949ab'
L6='#e8eaf6'
L5='180 Days'
L4='90 Days'
L3='Newest First'
L2='Today Only'
L1='Past 7 Days'
L0='540222'
K_='532480'
Kz='532209'
Ky='513377'
Kx='500420'
Kw='540175'
Kv='502525'
Ku='500260'
Kt='508869'
Ks='532488'
Kr='524715'
Kq='500209'
Kp='DALMIA'
Ko='APOLLOHOSP'
Kn='SUNPHARMA'
Km='lower limit'
Kl='upper limit'
Kk='title_raw'
Kj="\n            function(params) {\n                let v = String(params.value).toLowerCase();\n                if (v.includes('strong uptrend') || v.includes('bullish') || v.includes('strong buy')) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (v.includes('uptrend') || v.includes('buy') || v.includes('high') || v.includes('yes')) return { 'backgroundColor': '#a5d6a733', 'color': '#000' };\n                if (v.includes('sideways') || v.includes('watch') || v.includes('normal')) return { 'backgroundColor': '#f4b40033', 'color': '#000' };\n                if (v.includes('bearish') || v.includes('avoid') || v.includes('low') || v.includes('downtrend')) return { 'backgroundColor': '#ea433533', 'color': '#000' };\n                return null;\n            }\n            "
Ki="\n            function(params) {\n                let val = parseFloat(params.value);\n                if (val >= 75) return { 'backgroundColor': '#16e37f33', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 55) return { 'backgroundColor': '#f4b40033', 'color': '#000', 'fontWeight': 'bold' };\n                if (val >= 35) return { 'backgroundColor': '#ff990033', 'color': '#000' };\n                return { 'backgroundColor': '#ea433533', 'color': '#000' };\n            }\n            "
Kh='Automatically adjust column widths based on text length of the selected row.'
Kg=' (100%)'
Kf='Other Assets (unspecified)'
Ke='Cash & Equivalents'
Kd='#00897b'
Kc='Trade Receivables'
Kb='Inventory'
Ka='#5e35b1'
KZ='Fixed Assets / Net PPE'
KY='#5c6bc0'
KX='#8d6e63'
KW='Trade Payables'
KV='Total Debt'
KU='Reserves'
KT='Equity Capital'
KS='gauge+number'
KR='institutional'
KQ='institutional %'
KP='delivery %'
KO='% delivery'
KN='Last Close'
KM='rgba(0,0,0,0.08)'
KL='RSI(14)'
KK='system-ui, sans-serif'
KJ='rgba(0,0,0,0.06)'
KI='#31333F'
KH='tonexty'
KG='circle'
KF='#EF6C00'
KE='top right'
KD='#7C3AED'
KC='#FFD600'
KB='Candle'
KA='%d %b %Y %H:%M'
K9='⚠️ No AI configured. Add `GEMINI_API_KEY` or `GROQ_API_KEY` to Streamlit secrets.'
K8='stock name'
K7='company name'
K6='Type symbol name...'
K5='Search symbol:'
K4='Stocks'
K3='%{customdata}: %{y:.2f}%<extra></extra>'
K2='% Above 52W Low'
K1='% Below 52W High'
K0='displaylogo'
J_='#e3f2fd'
Jz='close price'
Jy='%Y%m%d_%H%M'
Jx='52w low date'
Jw='52w high date'
Jv='Market Cap'
Ju='RONW %'
Jt='Face Value'
Js='Institutional %'
Jr='Promoters %'
Jq='50 DMA < 200 DMA'
Jp='50 DMA > 200 DMA'
Jo='50 DMA > 100 DMA > 200 DMA'
Jn='50 DMA < 100 DMA < 200 DMA'
Jm='All (No Filter)'
Jl='macd crossover'
Jk='start gtt order'
Jj='output'
Ji='🎨 Custom Hex: '
Jh='#ff9900'
Jg='#f4b400'
Jf='bf_search'
Je='perf_matrix_search'
Jd='main_matrix_search'
Jc='search_query'
Jb='50 dma'
Ja='d/e ratio'
JZ='52w low'
JY='vol_val'
JX='official nse'
JW='market smith'
JV='chartlink'
JU='zerodha'
JT='screener'
JS='history data'
JR='trading view'
JQ='1SFhuZbLLlwwFsNo1k2RRx_Zp6bAkRR20W0F_zTwgdwU'
JP='https://www.googleapis.com/auth/drive'
JO='https://spreadsheets.google.com/feeds'
JN="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; font-family: system-ui, -apple-system, sans-serif;'>"
JM='Output'
JL='Price %'
JK='GROQ_API_KEY'
JJ='GEMINI_API_KEY'
Go='concalls'
Gn='credit_ratings'
Gm='annual_reports'
Gl='announcements'
Gk='1 Year'
Gj='30 Days'
Gi='total assets'
Gh='net ppe'
Gg='fixed assets'
Gf='trade payables'
Ge='trade receivables'
Gd='cash equivalent'
Gc='cash and equiv'
Gb='cash & equiv'
Ga='inventory'
GZ='total debt'
GY='reserves'
GX='total equity capital'
GW='Sector'
GV='rgba(0,0,0,0.3)'
GU='dash'
GT='#FF5252'
GS='#00E676'
GR='type'
GQ='#D50000'
GP='#00C853'
GO='🚨 **[ALERT]** '
GN='Recent'
GM='Grade'
GL='Strategy'
GK='% Gain'
GJ='Target'
GI='last_pine_result'
GH='last_ai_result'
GG='100%'
GF='streamlit'
GE='Default'
GD='📏 Column Width Adjustment:'
GC='Difference from 200 DMA column not detected for this sheet.'
GB='#fff8e1'
GA='#1b5e20'
G9='market cap'
G8='buy signal'
G7='trend'
G6='breakout signal'
G5='volume trend'
G4='industry'
G3='52w_low'
G2='52w_high'
G1='Watchlist'
G0='pledged'
F_='pledged %'
Fz='promoter'
Fy='promoters %'
Fx='200 dma'
Fw='#ef5350'
Fv='Error'
Fu='Loading...'
Ft='⚡ Groq (Fast)'
Fs=getattr
Fr=TypeError
ES='ppt'
ER='#9e9e9e'
EQ='#FFFFFF'
EP='system-ui, -apple-system, sans-serif'
EO='skip'
EN='lines'
EM='Low'
EL='High'
EK='locked in circuit'
EJ='hits circuit'
EI='lower circuit'
EH='upper circuit'
EG='52-week low'
EF='52-week high'
EE='%d %b %Y'
ED='Use Case'
EC='% Risk'
EB='Type'
EA='model'
E9='markers'
E8='52'
E7='sector'
E6='atr_approx'
E5='Added On'
E4='BF Grade'
E3='delivery'
E2='net sales'
E1='net profit'
E0='Pct_Change'
D_='value'
Dz='stock'
Dy='stock symbol'
Dx='ticker'
Dw='<[^>]*>'
Dv='gcp_service_account'
Du='No Data'
Dt=range
Ds=enumerate
DI='#c62828'
DH='dot'
DG='.//item'
DF='result'
DE='sym'
DD='left'
DC='% Diff from 200 DMA'
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
Cc='#37474f'
Cb='Mozilla/5.0'
Ca='User-Agent'
CZ='✅✅ Fit to Row 2'
CY='✅ Fit to Row 1'
CX='<br>'
CW='#e8f5e9'
CV='bf_score'
CU='52 week low'
CT='Value'
CS='turnover'
CR='%Y-%m-%d %H:%M:%S'
CQ='-%'
CP='+%'
CO='Diff @ 200 DMA'
CN='Final List 2'
CM='Final List'
Bw='rgba(0,0,0,0.2)'
Bv='Arial Black, Arial, sans-serif'
Bu='snap'
Bt='Buy Signal'
Bs='MACD Crossover'
Br='Trend'
Bq='Breakout Signal'
Bp='Volume Trend'
Bo='_'
Bn='📱 If frame is blank on mobile, tap the link above to open directly.'
Bm='#ffebee'
Bl='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
Bk='%Y%m%d'
Bj='bf_grade'
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
Ao='#0a1758'
An='pubDate'
Am=1.
Al='52W Low'
Ak='52W High'
Aj='% Delivery'
Ad='sec'
Ac='hour'
Ab='min'
Aa='#16e37f'
AZ='symbol'
AY='_txt_'
AX='_bg_'
AW=any
AV=ValueError
AR='bold'
AQ='normal'
AP='#ea4335'
AO='None'
AN='coerce'
AM='CMP'
AL=list
AI='timestamp'
AH='Just now'
AE='#1565C0'
AD='display_title'
AC='%'
AB=','
AA=max
A5='title'
A4='cmp'
A3='nan'
y='change'
x='#0f9d58'
w='Volume'
q='plotly_white'
n='_raw_symbol_'
k='-'
j='Symbol'
i=.0
g=Exception
f='link'
c='---'
b=round
U=next
T=int
Q=len
M=float
L='time_ago'
J=False
F=str
E=dict
D=None
C=''
B=True
import streamlit as A,pandas as H,numpy as A6,gspread as ET
from google.oauth2.service_account import Credentials as Gp
from google.auth.transport.requests import AuthorizedSession as LB
import json as EU,urllib.parse
from datetime import datetime as l
from st_aggrid import AgGrid as EV,GridOptionsBuilder as EW,JsCode as B2
from st_aggrid.shared import GridUpdateMode as LC
import streamlit.components.v1 as P,re,io,google.generativeai as Gq,plotly.graph_objects as O
from plotly.subplots import make_subplots as LD
A.set_page_config(page_title='Top 250 NSE Stock-Volume Breakout Dashboard',layout='wide',page_icon='📊')
if hasattr(A,'fragment'):DJ=A.fragment
elif hasattr(A,'experimental_fragment'):DJ=A.experimental_fragment
else:
	def DJ(func=D,**B):
		if func is not D:return func
		def A(f):return f
		return A
A.markdown('\n<style>\n    /* Force EVERY tab-bar container to wrap onto multiple lines instead of\n       staying on one scrollable line. Multiple selector variants are used\n       (data-baseweb, role, and Streamlit\'s own class) because Streamlit\'s\n       internal DOM/class names have changed across versions. */\n    div[data-testid="stTabs"],\n    div[data-testid="stTabs"] > div,\n    .stTabs,\n    .stTabs > div {\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        max-width: 100% !important;\n    }\n\n    div[data-baseweb="tab-list"],\n    div[role="tablist"] {\n        display: flex !important;\n        flex-wrap: wrap !important;\n        overflow-x: visible !important;\n        overflow-y: visible !important;\n        white-space: normal !important;\n        row-gap: 4px !important;\n        column-gap: 6px !important;\n        height: auto !important;\n        max-width: 100% !important;\n        width: 100% !important;\n        scrollbar-width: none !important;\n    }\n    div[data-baseweb="tab-list"]::-webkit-scrollbar {\n        display: none !important;\n    }\n\n    /* Each tab button: allow shrinking/wrapping instead of forcing one line */\n    button[data-baseweb="tab"],\n    div[role="tablist"] > button,\n    div[role="tablist"] [role="tab"] {\n        flex: 0 0 auto !important;\n        white-space: normal !important;\n        margin-top: 1px !important;\n        margin-bottom: 1px !important;\n        padding-top: 6px !important;\n        padding-bottom: 6px !important;\n        height: auto !important;\n    }\n\n    /* Hide the "‹ ›" scroll-arrow buttons Streamlit shows when a tab bar overflows */\n    button[data-testid="stTabsScrollButton"],\n    div[data-baseweb="tab-list"] ~ button,\n    div[data-baseweb="tab-list"] + button,\n    button[kind="tabScroll"],\n    button[aria-label*="scroll" i] {\n        display: none !important;\n    }\n\n    div[data-baseweb="tab-highlight"] {\n        display: none !important;\n    }\n    div[data-baseweb="tab"][aria-selected="true"],\n    [role="tab"][aria-selected="true"] {\n        background-color: rgba(31, 119, 180, 0.1) !important;\n        border-radius: 5px !important;\n        border-bottom: 2px solid #1f77b4 !important;\n    }\n</style>\n',unsafe_allow_html=B)
Cd=J
BN=J
if JJ in A.secrets:Gq.configure(api_key=A.secrets[JJ]);Cd=B
if JK in A.secrets:
	try:from groq import Groq as LE;LF=LE(api_key=A.secrets[JK]);BN=B
	except ImportError:BN=J
EX=Cd or BN
def EY(prompt,model_choice):
	A=prompt
	if model_choice==Ft and BN:B=LF.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{'role':'user','content':A}],max_tokens=2048);return B.choices[0].message.content
	elif Cd:C=Gq.GenerativeModel('gemini-2.5-flash');return C.generate_content(A).text
	else:raise RuntimeError('No AI model is configured. Add GEMINI_API_KEY or GROQ_API_KEY to secrets.')
def EZ(key_suffix=C):
	D='🧠 Gemini';C,E=[],0
	if BN:C.append(Ft)
	if Cd:C.append(D)
	if not C:C=[Ft,D]
	return A.radio('🤖 AI Model:',C,index=0,horizontal=B,key=f"ai_model_sel_{key_suffix}")
LG=['Based on the current data provided, give me a quick summary of the technical performance and trend for {sym}. Also give me all other details and calculate if this company is profitable or not.','Analyze the 52-week high and low data for {sym}. Is the stock closer to its peak or bottom? What does this imply for entry or exit timing? Identify the ideal buy zone.','Examine the 50 DMA, 100 DMA, and 200 DMA data for {sym}. Is the stock in a bullish crossover, bearish zone, or consolidation phase? Explain the trend strength and momentum.','Using the volume data for {sym}, identify if there is unusual volume activity. Does the current volume indicate institutional buying, selling, or accumulation? What does it signal?','Evaluate the full fundamentals of {sym} — EPS, RONW%, D/E ratio, Net Profit (Cr.), Book Value, and Market Cap. Is this company financially healthy and worth long-term investment?','What is the risk profile of {sym} based on its Pledged %, Promoters Holding %, Institutional Holding %, and Debt-to-Equity ratio? Should a retail investor be cautious right now?',"Compare {sym}'s current CMP vs its 200 DMA. Is the stock overbought, oversold, or fairly valued based on the Difference from 200 DMA metric? What is the ideal risk-reward entry zone?",'Give a complete Buy / Hold / Sell recommendation for {sym} using all available technical and fundamental data. Include specific price targets, support levels, and a stop-loss level.','Based on the CAR Rating and Output signal for {sym}, what is the system suggesting? Does the historical price action and current data support this signal? How reliable is it?',"Summarize {sym}'s sector positioning, market cap, enterprise value, book value, and promoter holding. How does this stock compare to typical benchmarks in its sector in the Indian market?"]
LH="Strategy 1 — Volume Breakout with Dynamic Stop Loss\n  Rule 1: Enter long when today's volume > 2× the 20-day average volume AND price closes above the prior day's high; set stop loss at 1.5× ATR below entry price.\n  Rule 2: Add a false breakout filter — price must hold above the breakout level for 2 consecutive candles before confirming entry; trail stop at the lowest low of the last 3 bars.\n  Rule 3: Set profit target at 2:1 risk-reward ratio; plot a volume histogram overlay to identify surge bars visually; include an alert condition for live breakout detection.\n\nStrategy 2 — Moving Average Crossover (50/100/200 DMA)\n  Rule 4: Buy when 50 DMA crosses above 100 DMA with price trading above the 200 DMA; exit when 50 DMA crosses back below 100 DMA; use 200 DMA as the hard stop-loss floor.\n  Rule 5: Add RSI confirmation — only enter when RSI is between 50–70 at the crossover candle; plot all three DMAs on the chart with distinct colours for visual clarity.\n  Rule 6: Allow a re-entry if 50 DMA pulls back to 100 DMA without breaking below 200 DMA; set stop loss 2% below the 50 DMA value at the time of entry.\n\nStrategy 3 — Trend Following with Trailing Stop\n  Rule 7: Enter long when price breaks a 20-day high with above-average volume and ADX > 25; apply a Chandelier Exit trailing stop set at 3× ATR from the highest close after entry.\n  Rule 8: Use 200 DMA direction as the trend filter — only take long trades when price is above 200 DMA; tighten trailing stop to 2× ATR once profit exceeds 10% from entry.\n  Rule 9: Add a re-entry condition: if stopped out but price remains above 200 DMA, re-enter on the next pullback to the 50 DMA; limit to a maximum of 2 re-entries per trend leg.\n\nStrategy 4 — Mean Reversion from 52W High/Low\n  Rule 10: Buy when price is within 15% of the 52-week low AND RSI < 35; set profit target at the 52-week midpoint; place hard stop loss 5% below the 52-week low level.\n  Rule 11: Exit/short signal when price is within 5% of the 52-week high with RSI > 70; use Bollinger Band upper band touch as secondary confirmation; target the middle Bollinger Band as exit.\n  Rule 12: Apply a volume reversal filter — only enter when the reversal candle's volume is ≥ 1.5× the 20-day average; plot the 52-week high and low as horizontal reference lines on the chart."
LI='\n### 💡 Core Rules\n- **Sheet Convention:** Always use **NSE Code** instead of *Symbol* in the Google Sheet — this keeps NSE chart links working correctly.\n- **No Compromise:** Follow the Rules. Never compromise on Rules — Rules are better than any single Buy/Sell decision.\n- **Timing Edge:** Take advantage of time — buy when a stock is at its lower end (near 52W Low) and sell at a higher price when momentum kicks in (e.g. an Upper Circuit move).\n\n---\n\n### 🟢 Rule 1 — Near 52 Week High\nCMP / Close Price is highlighted **Green** when it is near the 52-Week High (within ~8%).\n\n### 🟠 Rule 2 — Near 52 Week Low (Buy Zone)\nCMP / Close Price is highlighted **Orange** when it is near the 52-Week Low (within ~8%) — **this is the type of stock to look at buying.**\n\n**52W Low / High Date column — color meaning:**\n| Signal | Meaning |\n|---|---|\n| 🟢 Green in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 18 days** |\n| 🟢 Green in *52 Week High Date* | Stock touched its 52-Week High within the **last 18 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low within the **last 30 days** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High within the **last 30 days** |\n| Plain in *52 Week Low Date* | Stock touched its 52-Week Low **about 1 year ago** |\n| Plain in *52 Week High Date* | Stock touched its 52-Week High **about 1 year ago** |\n\n### 🔵 Rule 3 — Diff @ 200 DMA Strategy\nOnly buy **52-Week Low** stocks, ranked by the **Difference from 200 DMA** column on the **Diff @ 200 DMA** tab — biggest fall first.\n\n**Path:**\n1. Open the **Diff @ 200 DMA** tab (Main sheet).\n2. Refer to the **Difference from 200 DMA** column.\n3. Sort results **−40% → −30% → −20% → −10%** (most negative first).\n\n**Mind Map:**\n```\nRule 3 → Buy Only 52-Week Low Stocks\n│\n├── Main Sheet → Open Tab "Diff @ 200 DMA"\n├── Check Column → "Difference from 200 DMA"\n├── Sort Logic → Biggest Fall First (-40% → -30% → -20% → -10%)\n├── Meaning → Stock is trading below its 200 DMA\n├── Priority → More negative % = higher priority\n├── Selection Criteria\n│     ├── Only 52-Week Low stocks\n│     ├── Negative Difference from 200 DMA\n│     └── Deep-discount stocks preferred\n└── Final Action → Analyze & buy quality stocks\n```\n\n---\n\n### 🔗 Useful NSE Reference Links\n- **All Reports (Bhavcopy / Market Activity):** Bhavcopy (PR)(zip), Market Activity Report (csv), Full Bhavcopy & security delivery data, MCAP, PD, PR, SME → https://www.nseindia.com/all-reports/\n- **Securities Available for Trading** (ETF, Close-Ended MF Schemes, SME) → https://www.nseindia.com/static/market-data/securities-available-for-trading\n- **52-Week Low — Equity Market** → https://www.nseindia.com/market-data/52-week-low-equity-market#capital_market_link\n\n---\n\n### 🛑 Risk Management — No Compromise\n- **Stop Loss (Max 1–2%), no compromise.** બીજો chance મળશે કમાવાનો — પૈસા 10% ઓછા થયા તો 15% કમાવા પડશે.\n- **Risk-Reward Ratio:** max 5 trades, max 10% loss — never lose all your money in a single trade.\n- **Target / Profit Booking:** Max 10–20%.\n- Don\'t trade emotionally — the share market is a mind game.\n- Know everything related to a share before moving ahead.\n- Stay calm, serious, and stick to the decision you\'ve made.\n- **Clear Vision, no compromise:** Focus → Stop Loss → Risk-Reward Ratio → Target/Profit → 52-Week Low Buy.\n- **Priority order:** IPO → F&O → 52-Week Low Shares.\n'
LJ={BD:['50 DMA','100 DMA','200 DMA','NSE 1','Trading View 1','History Data 1','Screener 1','Zerodha 1','Chartlink 1','Market smith india 1','Official NSE URL 1'],BE:[],CM:[],CN:[],CO:[],CP:[],CQ:[]}
LK={BD:['E','F','G','AA','AB','AC','AD','AE','AF','AG','AH'],BE:[],CM:[],CN:[],CO:[],CP:[],CQ:[]}
def Gr(letter):
	A=letter;A=F(A).strip().upper()
	if not A or not A.isalpha():return-1
	B=0
	for C in A:B=B*26+(ord(C)-ord('A')+1)
	return B-1
def LL(sheet_name,ordered_columns):
	C=sheet_name;A=ordered_columns;A=AL(A);B=set()
	for D in LJ.get(C,[]):
		if D in A:B.add(D)
	for F in LK.get(C,[]):
		E=Gr(F)
		if 0<=E<Q(A):B.add(A[E])
	return B
LM={BD:D,BE:D,CM:D,CN:D,CO:D,CP:D,CQ:D}
LN={BD:[w,Aj,'Close Price',AM,JL,Ak,Al,JM,'Differance from 200 DMA','Cumulative Average Rule (CAR) Rating'],BE:[],CM:[],CN:[],CO:[],CP:[],CQ:[]}
LO={BD:['B','C','D','L'],BE:[],CM:[],CN:[],CO:[],CP:[],CQ:[]}
def LP(sheet_name,ordered_columns):
	D=sheet_name;A=ordered_columns;A=AL(A);B=[]
	for G in LO.get(D,[]):
		E=Gr(G)
		if 0<=E<Q(A):
			F=A[E]
			if F not in B:B.append(F)
	for C in LN.get(D,[]):
		if C in A and C not in B:B.append(C)
	return B
import streamlit as A
LQ='\n<style>\n    #MainMenu {visibility: show;}\n    header {visibility: show;}\n    [data-testid="stToolbar"] {visibility: show;}\n    footer {visibility: show;}\n</style>\n'
A.markdown(LQ,unsafe_allow_html=B)
import streamlit as A
LR='\n<style>\n    [data-testid="stToolbar"] {\n        right: 2rem;\n    }\n    [data-testid="stToolbar"]::before {\n        content: "";\n    }\n    button[kind="header"] {display: none;}\n</style>\n'
A.markdown(LR,unsafe_allow_html=B)
LS='romo'
if'logged_in'not in A.session_state:A.session_state.logged_in=J
if'watchlist'not in A.session_state:A.session_state.watchlist={}
if'ai_history'not in A.session_state:A.session_state.ai_history=[]
if'grid_reset_token'not in A.session_state:A.session_state.grid_reset_token=0
if not A.session_state.logged_in:
	A.markdown("<p style='text-align: center; margin-top: 100px; color: Green; font-size: 18px;'>250-V Dashboard</p>",unsafe_allow_html=B);A.markdown("<h1 style='text-align: center; margin-top: 0px; font-size: 20px;'>🔐 Admin Login</h1>",unsafe_allow_html=B);P5,LT,P6=A.columns([1,1,1])
	with LT:
		with A.form('login_form'):
			LU=A.text_input('Enter Password',type='password');LV=A.form_submit_button('Login',use_container_width=B)
			if LV:
				if LU==LS:A.session_state.logged_in=B;A.rerun()
				else:import random;LW=['Password इल्ले! 😅 इल्ले!, खम्मा घणी भाईसा, सॉरी। तुमसे सब कुछ हो पाएगा! यहां बहुत 🤪 दिमाग मत लगाओ, इस वेबसाइट को नहीं, 😂 इस गलत पासवर्ड को छोड़ दो!','❌ Password इल्ले भाईसा! 😅 इल्ले! खम्मा घणी, सॉरी। तुम बाहुबली हो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। अपनी सुंदर वेबसाइट को नहीं, 😂 इस सड़े हुए गलत पासवर्ड को छोड़ दो!','❌ खम्मा घणी भाईसा, Password इल्ले! 😅 sorry! तुम तो मंगल ग्रह पर पानी खोज सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस सीधे-सादे वेबसाइट को नहीं, 😂 इस जाली पासवर्ड को छोड़ दो!','❌ Password इल्ले! 😅 इल्ले! खम्मा घणी भाईसा, सॉरी। लोड मत लो, तुमसे सब कुछ हो पाएगा! पर यहाँ फालतू 🤪 दिमाग मत लगाओ। दुनिया छोड़ दो, मोक्ष पकड़ लो, पर पहले 😂 इस गलत पासवर्ड को छोड़ दो!','❌ अरे भाईसा! Password इल्ले! 😅 खम्मा घणी, सॉरी। तुम चाहो तो सिस्टम हिला सकते हो, तुमसे सब कुछ हो पाएगा! पर यहाँ ज़्यादा 🤪 दिमाग मत लगाओ। इस निर्दोष वेबसाइट को नहीं, 😂 इस भूतिया गलत पासवर्ड को छोड़ दो!'];A.error(random.choice(LW))
	LX=l.now().strftime(CR);A.markdown(f"<p style='text-align: center; color: gray; font-size: 14px; margin-top: 20px;'>Data refreshed: {LX}</p>",unsafe_allow_html=B);A.stop()
A.markdown('\n<style>\n    /* Reduce ALL headings to 90% smaller size */\n    h1, h2, h3, h4, h5, h6, .stSubheader, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {\n        font-size: 0.85rem !important;\n        font-weight: bold !important;\n        margin-top: 0.5rem !important;\n        margin-bottom: 0.5rem !important;\n    }\n</style>\n',unsafe_allow_html=B)
import yfinance as Gs,streamlit as A
from datetime import datetime as l
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📊 Top 250 NSE Stock-Volume Breakout Dashboard</p>",unsafe_allow_html=B)
A.caption(f"Data refreshed: {l.now().strftime(CR)}")
@A.cache_data(ttl=60)
def LY():
	A='UNSUPPORTED';H={'NIFTY 50':'^NSEI','NIFTY NEXT 50':'^NN50','NIFTY MIDCAP 50':'^NSEMDCP50','NIFTY MIDCAP 100':'^CRSLMID','NIFTY MIDCAP 150':A,'NIFTY SMLCAP 50':A,'NIFTY SMLCAP 100':A,'NIFTY SMLCAP 250':A,'NIFTY MIDSML 400':A,'NIFTY 100':'^CNX100','NIFTY 200':'^CNX200','NIFTY500 MULTI...':A,'NIFTY LARGEMID...':A,'NIFTY MID SELE...':A,'NIFTY TOTAL MK...':A,'NIFTY MICROCAP...':A,'NIFTY 500':'^CRSLDX','NIFTY FPI 150':A,'NIFTY500 LMS E...':A,'NIFTY MIDSMALL...':A,'NIFTY SMALLCAP...':A};B={}
	for(C,E)in H.items():
		if E==A:B[C]={Az:Du,y:i};continue
		try:
			I=Gs.Ticker(E);D=I.history(period='5d')
			if not D.empty and Q(D)>=2:F=M(D[BF].iloc[-1]);G=M(D[BF].iloc[-2]);J=(F-G)/G*100;B[C]={Az:f"{F:,.2f}",y:J}
			else:B[C]={Az:Fu,y:i}
		except g:B[C]={Az:Fv,y:i}
	return B
LZ=LY()
Ap=JN
Gt=0
for(Bx,AS)in LZ.items():
	if AS[Az]in[Du,Fu,Fv]:continue
	Gt+=1;Ea=Cy if AS[y]>=0 else Fw;Eb='+'if AS[y]>=0 else C;La='https://www.nseindia.com/market-data/live-market-indices';Ap+=f"<a href='{La}' target='_blank' style='text-decoration:none;'>";Ap+=f"<div style='background-color: {Ea}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";Ap+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bx}</div>";Ap+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";Ap+=f"<span style='font-size: 15px; font-weight: 700;'>{AS[Az]}</span>";Ap+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{Eb}{AS[y]:.2f}%</span>";Ap+=f"</div></div></a>"
Ap+=Cz
with A.expander('📈 Click to view Live Market Indices',expanded=J):
	if Gt==0:A.info('Market data is currently unavailable. Please check back later.')
	else:A.markdown(Ap,unsafe_allow_html=B)
A.write(c)
def Gu(color_dict):
	A=color_dict
	if not A:return C_
	B,C,D=T(A.get('red',0)*255),T(A.get('green',0)*255),T(A.get('blue',0)*255);return f"#{B:02x}{C:02x}{D:02x}"
@A.cache_data(ttl=300,show_spinner=J)
def Lb(nse_symbol,period='1y'):
	try:
		C=F(nse_symbol).strip().upper()
		if not C:return H.DataFrame()
		E=C if C.endswith('.NS')else f"{C}.NS";A=Gs.download(E,period=period,interval='1d',progress=J,auto_adjust=B)
		if A is D or A.empty:return H.DataFrame()
		if Ay(A.columns,H.MultiIndex):A.columns=A.columns.get_level_values(0)
		A.index=H.to_datetime(A.index);return A
	except g:return H.DataFrame()
@A.cache_data(ttl=300)
def DK(sheet_name):
	M='sheets'
	try:
		if Dv not in A.secrets:A.error("Missing 'gcp_service_account' in secrets.");return H.DataFrame()
		D=A.secrets[Dv]
		if Ay(D,F):D=EU.loads(D)
		Y=[JO,JP];N=Gp.from_service_account_info(D,scopes=Y);j=ET.authorize(N);Z=JQ;a=urllib.parse.quote(sheet_name);b=LB(N);c=f"https://sheets.googleapis.com/v4/spreadsheets/{Z}?includeGridData=true&ranges={a}";d=b.get(c);E=d.json()
		if'error'in E:return H.DataFrame()
		if M not in E or not E[M]:return H.DataFrame()
		e=E[M][0]['data'][0];O=e.get('rowData',[])
		if not O:return H.DataFrame()
		J,P,R=[],[],[]
		for f in O:
			h=f.get('values',[]);S,T,U=[],[],[]
			for V in h:S.append(V.get('formattedValue',C));W=V.get('effectiveFormat',{});T.append(Gu(W.get('backgroundColor',{})));U.append(Gu(W.get('textFormat',{}).get('foregroundColor',{})))
			J.append(S);P.append(T);R.append(U)
		i=J[0];K=[];G={}
		for B in i:
			B=F(B).strip()
			if B==C:B='empty_column'
			if B in G:G[B]+=1;B=f"{B}_{G[B]}"
			else:G[B]=0
			K.append(B)
		L=H.DataFrame(J[1:],columns=K)
		for(I,X)in Ds(K):L[f"_bg_{X}"]=[A[I]if I<Q(A)else C_ for A in P[1:]];L[f"_txt_{X}"]=[A[I]if I<Q(A)else'#000000'for A in R[1:]]
		return L
	except g as k:return H.DataFrame()
def Lc(df,symbol_col):
	K=symbol_col;H='1';G='🔗 Link';I=df.copy();I[n]=I[K]
	for(L,M)in I.iterrows():
		A=F(M[n]).strip()
		if not A or A==A3:continue
		for J in I.columns:
			if J.startswith(AX)or J.startswith(AY)or J==n:continue
			B=J.lower();C,E=D,G
			if JR in B:C,E=f"https://www.tradingview.com/symbols/{A}/",f"Tre {A}"if not B.endswith(H)else G
			elif JS in B:C,E=f"https://www.equitypandit.com/historical-data/{A}",f"History {A}"if not B.endswith(H)else G
			elif JT in B:C,E=f"https://www.screener.in/company/{A}",f"Scr {A}"if not B.endswith(H)else G
			elif JU in B:C,E=f"https://zerodha.com/markets/stocks/NSE/{A}",f"🪁 {A}"if not B.endswith(H)else G
			elif JV in B:C,E=f"https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={A}",f"CL {A}"if not B.endswith(H)else G
			elif JW in B:C,E=f"https://marketsmithindia.com/mstool/eval/{A}/evaluation.jsp",f"ms {A}"if not B.endswith(H)else G
			elif JX in B:C,E=f"https://www.nseindia.com/get-quotes/equity?symbol={A}",f"nse📰 {A}"if not B.endswith(H)else G
			elif'nse'in B or J==K:C,E=f"https://charting.nseindia.com/?symbol={A}-EQ",A if not B.endswith(H)else G
			if C:I.at[L,J]=f'<a href="{C}" target="_blank" style="text-decoration:none; color:#000000;">{E}</a>'
	return I
def DL(df,col_name,st_container,display_label=D):
	J=display_label;D=col_name
	if D in df.columns:
		A=df[D].astype(F).str.replace(BG,C,regex=B);A=H.to_numeric(A,errors=AN).replace([A6.inf,-A6.inf],A6.nan);E=A.dropna()
		if not E.empty:
			G,I=b(M(E.min()),2),b(M(E.max()),2)
			if G<I:L=J if J else f"{D} Range:";K=st_container.slider(L,min_value=G,max_value=I,value=(G,I),key=f"filter_num_{D}");return df[(A>=K[0])&(A<=K[1])]
	return df
def Gv(df,col_name,st_container):
	Q='Past 1 Year';P='Past 6 Months';O='Past 2 Months';N='Past 1 Month';M='Past 30 Days';L='Past 25 Days';K='Past 20 Days';J='Past 15 Days';I='Past 10 Days';G='Past 5 Days';F='All Time';E=col_name
	if E in df.columns:
		R=[F,G,I,J,K,L,M,N,O,P,Q];A=st_container.selectbox(f"{E}:",R,key=f"filter_date_{E}")
		if A!=F:
			S=H.to_datetime(df[E],errors=AN,dayfirst=B);C=H.Timestamp.now()
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
def By(val):
	if H.isna(val):return 0
	A=re.sub(Dw,C,F(val));return Q(A)
def Gw(df):
	A=df.copy();D=[A for A in A.columns if A.startswith(AX)or A.startswith(AY)or A==n];A=A.drop(columns=D,errors='ignore')
	for B in A.select_dtypes(include=['object']).columns:A[B]=A[B].apply(lambda x:re.sub(Dw,C,F(x))if H.notnull(x)else x)
	return A
import streamlit.components.v1 as P
A.markdown("<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>🌍 National Exchange Scanner (All NSE/BSE Stocks)</p>",unsafe_allow_html=B)
A.caption('Live market data covering 2,000+ equities. Powered by TradingView.')
with A.expander('🏆 Click to view Full-Market India Rankings',expanded=J):
	Ld,Le,Lf,Lg,Lh=A.tabs(['🚀 Gainers & Losers','📦 Volume & Active','⭐ 52W High / Low','🔄 52W Reversals','📊 Top 100 Traded'])
	def Aq(screen_type):return f'''
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
	with Ld:
		Ar,As=A.columns(2)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>🚀 Top Gainers</p>",unsafe_allow_html=B);P.html(Aq('top_gainers'),height=520)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔻 Top Losers</p>",unsafe_allow_html=B);P.html(Aq('top_losers'),height=520)
	with Le:
		Ar,As=A.columns(2)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>📦 Volume Leaders</p>",unsafe_allow_html=B);P.html(Aq('volume_leaders'),height=520)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>🔥 Most Active (Volume & Value)</p>",unsafe_allow_html=B);P.html(Aq('most_active'),height=520)
	with Lf:
		Ar,As=A.columns(2)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Highs</p>",unsafe_allow_html=B);P.html(Aq('new_52wk_high'),height=520)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>⭐ New 52-Week Lows</p>",unsafe_allow_html=B);P.html(Aq('new_52wk_low'),height=520)
	with Lg:
		Ar,As=A.columns(2)
		with Ar:A.markdown("<p style='font-size:14px; font-weight:bold;'>📈 Outperforming 52W High (Reversal Up)</p>",unsafe_allow_html=B);P.html(Aq('outperforming_52wk_high'),height=520)
		with As:A.markdown("<p style='font-size:14px; font-weight:bold;'>📉 Underperforming 52W Low (Reversal Down)</p>",unsafe_allow_html=B);P.html(Aq('underperforming_52wk_low'),height=520)
	with Lh:A.markdown("<p style='font-size:14px; font-weight:bold;'>📊 Top 100+ Stocks Traded (Full India Screener)</p>",unsafe_allow_html=B);P.html(Aq('general'),height=520)
A.write(c)
@A.cache_data(ttl=300)
def Li():
	B=DK(BD);A={}
	if B.empty:return A
	E=[A for A in B.columns if not A.startswith(AX)and not A.startswith(AY)];I=U((A for A in E if A.lower()in[D0,AZ,Dx,Dy,D1,Dz]),D);J=U((A for A in E if A4 in A.lower()),D);K=U((A for A in E if D2 in A.lower()or y in A.lower()),D)
	if not I or not J:return A
	for(R,G)in B.iterrows():
		H=F(G.get(I,C)).strip()
		if not H or H==A3:continue
		O=F(G.get(J,C)).replace(AB,C).strip();P=F(G.get(K,'0')).replace(AC,C).replace(AB,C).strip()if K else'0'
		try:Q=M(O);L=f"{Q:,.2f}"
		except AV:L=Du
		try:N=M(P)
		except AV:N=i
		A[H]={Az:L,y:N}
	return A
Lj=Li()
At=JN
Gx=0
for(Bx,AS)in Lj.items():
	if AS[Az]in[Du,Fu,Fv]:continue
	Gx+=1;Ea=Cy if AS[y]>=0 else Fw;Eb='+'if AS[y]>=0 else C;Lk=f"https://www.nseindia.com/get-quotes/equity?symbol={Bx}";At+=f"<a href='{Lk}' target='_blank' style='text-decoration:none;'>";At+=f"<div style='background-color: {Ea}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";At+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{Bx}</div>";At+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";At+=f"<span style='font-size: 15px; font-weight: 700;'>{AS[Az]}</span>";At+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px;'>{Eb}{AS[y]:.2f}%</span>";At+=f"</div></div></a>"
At+=Cz
with A.expander('📈 Click to view Top 250 Stocks Matrix',expanded=J):
	if Gx==0:A.info("Stock matrix data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:A.markdown(At,unsafe_allow_html=B)
A.write(c)
@A.cache_data(ttl=300)
def Ll():
	P='[a-zA-Z%, ]';E=DK(BD)
	if E.empty:return H.DataFrame()
	G=[A for A in E.columns if not A.startswith(AX)and not A.startswith(AY)];I=U((A for A in G if A.lower()in[D0,AZ,Dx,Dy,D1,Dz]),D);J=U((A for A in G if A4 in A.lower()),D);K=U((A for A in G if D2 in A.lower()or y in A.lower()),D);L=U((A for A in G if BH in A.lower()),D);M=U((A for A in G if D_ in A.lower()and'face'not in A.lower()and'enterprise'not in A.lower()),D);N=U((A for A in G if CS in A.lower()),D)
	if not I:return H.DataFrame()
	A=H.DataFrame();A[j]=E[I].astype(F).str.strip();A[AM]=H.to_numeric(E[J].astype(F).str.replace(BG,C,regex=B),errors=AN)if J else i;A[E0]=H.to_numeric(E[K].astype(F).str.replace(BG,C,regex=B),errors=AN)if K else i;A[w]=H.to_numeric(E[L].astype(F).str.replace(BG,C,regex=B),errors=AN)if L else i;O=A[AM]*A[w]
	if M:A[CT]=H.to_numeric(E[M].astype(F).str.replace(P,C,regex=B),errors=AN)
	else:A[CT]=O
	if N:A[D3]=H.to_numeric(E[N].astype(F).str.replace(P,C,regex=B),errors=AN)
	else:A[D3]=O
	A=A.dropna(subset=[j,AM]).reset_index(drop=B);A=A[(A[j]!=A3)&(A[j]!=C)];return A
def B3(dataframe,metric_label=y):
	J=dataframe;G=metric_label;A="<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; font-family: system-ui, -apple-system, sans-serif;'>"
	if J.empty:return"<p style='color: gray; font-size: 14px;'>No data available for this ranking.</p>"
	for(R,B)in J.iterrows():
		K=B[j];L=B[AM];H=B[E0];M=Cy if H>=0 else Fw;N='+'if H>=0 else C
		if G==BH:D=B.get(w,0);F=f"Vol: {D/1000000:.1f}M"if D>=1000000 else f"Vol: {D:,.0f}"
		elif G==D_:E=B.get(CT,0);F=f"Val: ₹{E/10000000:,.1f}Cr"if E>=10000000 else f"Val: ₹{E:,.0f}"
		elif G==CS:I=B.get(D3,0);F=f"T.O: ₹{I/10000000:,.1f}Cr"if I>=10000000 else f"T.O: ₹{I:,.0f}"
		elif G==JY:D=B.get(w,0);E=B.get(CT,0);O=f"{D/1000000:.1f}M"if D>=1000000 else f"{D/1000:.1f}k";P=f"₹{E/10000000:,.1f}Cr"if E>=10000000 else f"₹{E:,.0f}";F=f"📦 {O} | 💰 {P}"
		else:F=f"{N}{H:.2f}%"
		Q=f"https://www.nseindia.com/get-quotes/equity?symbol={K}";A+=f"<a href='{Q}' target='_blank' style='text-decoration:none;'>";A+=f"<div style='background-color: {M}; color: white; padding: 12px 16px; border-radius: 8px; flex: 1 1 calc(16.66% - 10px); min-width: 140px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>";A+=f"<div style='font-size: 11px; font-weight: 700; letter-spacing: 0.5px; opacity: 0.95; margin-bottom: 6px; text-transform: uppercase;'>{K}</div>";A+=f"<div style='display: flex; justify-content: space-between; align-items: baseline;'>";A+=f"<span style='font-size: 15px; font-weight: 700;'>{L:,.2f}</span>";A+=f"<span style='font-size: 11px; font-weight: 600; background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 4px; white-space: nowrap;'>{F}</span>";A+=f"</div></div></a>"
	A+=Cz;return A
Ae=Ll()
with A.expander('🏆 Click to view Advanced Ranking Dashboards (Top 250 Stocks)',expanded=J):
	if Ae.empty:A.info("Ranking data is currently unavailable. Please check the 'Top 250 Stocks' sheet.")
	else:
		Lm=Ae.nlargest(20,E0);Ln=Ae.nsmallest(20,E0);Lo=Ae.nlargest(20,w);Lp=Ae[Ae[w]>0].nsmallest(20,w);Lq=Ae.nlargest(20,w);Lr=Ae.nlargest(20,CT);Ls=Ae.nlargest(20,D3);Lt=Ae.nlargest(20,CT);Lu,Lv,Lw,Lx,Ly,Lz=A.tabs(['📈 Gainers/Losers','📦 Volume Leaders','🔥 Active (Vol & Val)','💰 Top by Value','💎 Top by Turnover','💰 Most Active'])
		with Lu:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🚀 Top 20 Gainers</p>",unsafe_allow_html=B);A.markdown(B3(Lm,y),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔻 Top 20 Losers</p>",unsafe_allow_html=B);A.markdown(B3(Ln,y),unsafe_allow_html=B)
		with Lv:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>📦 Top 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B3(Lo,BH),unsafe_allow_html=B);A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💤 Bottom 20 by Volume</p>",unsafe_allow_html=B);A.markdown(B3(Lp,BH),unsafe_allow_html=B)
		with Lw:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>🔥 Most Active Stocks (Volume & Traded Value)</p>",unsafe_allow_html=B);A.markdown(B3(Lq,JY),unsafe_allow_html=B)
		with Lx:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active by Traded Value</p>",unsafe_allow_html=B);A.markdown(B3(Lr,D_),unsafe_allow_html=B)
		with Ly:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💎 Highest Market Turnover</p>",unsafe_allow_html=B);A.markdown(B3(Ls,CS),unsafe_allow_html=B)
		with Lz:A.markdown("<p style='font-size:14px; font-weight:bold; margin-top:10px;'>💰 Most Active (Highest Traded Value)</p>",unsafe_allow_html=B);A.markdown(B3(Lt,D_),unsafe_allow_html=B)
A.write(c)
def DM(row,actual_cols):
	B=0;A=[]
	def E(col_keywords,negate=J):
		for E in col_keywords:
			A=U((A for A in actual_cols if E.lower()in A.lower()),D)
			if A and A in row:
				try:B=M(F(row[A]).replace(AC,C).replace(AB,C).strip());return-B if negate else B
				except:pass
	N=E([A4]);Q=E([JZ,CU,'52wlow'])
	if N and Q and Q>0:
		I=(N-Q)/Q*100
		if 8<=I<=15:B+=30;A.append(f"✅ CMP +{I:.1f}% from 52W Low (sweet zone)")
		elif I<8:B+=15;A.append(f"⚠️ CMP +{I:.1f}% from 52W Low (still bottoming)")
		elif I<=25:B+=10;A.append(f"🟡 CMP +{I:.1f}% from 52W Low (extended)")
		else:A.append(f"❌ CMP +{I:.1f}% from 52W Low (too far)")
	O=E([Fx])
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
	G=E([Ja,'debt','d/e'])
	if G is not D:
		if G<=.1:B+=10;A.append(f"✅ Debt-Free / Zero Debt (D/E={G:.2f})")
		elif G<=.5:B+=7;A.append(f"✅ Very Low Debt (D/E={G:.2f})")
		elif G<=Am:B+=4;A.append(f"🟡 Manageable Debt (D/E={G:.2f})")
		else:A.append(f"❌ High Debt (D/E={G:.2f})")
	R=E([E1])
	if R is not D:
		if R>0:B+=10;A.append(f"✅ Profitable: Net Profit ₹{R:.1f} Cr")
		else:A.append(f"❌ Loss Making: Net Profit ₹{R:.1f} Cr")
	H=E(['ronw'])
	if H is not D:
		if H>=15:B+=10;A.append(f"✅ Strong RONW: {H:.1f}%")
		elif H>=8:B+=6;A.append(f"🟡 Moderate RONW: {H:.1f}%")
		elif H>0:B+=2;A.append(f"⚠️ Low RONW: {H:.1f}%")
		else:A.append(f"❌ Negative RONW: {H:.1f}%")
	L=E([Fy,Fz])
	if L is not D:
		if L>=50:B+=8;A.append(f"✅ Promoter Holding: {L:.1f}%")
		elif L>=35:B+=5;A.append(f"🟡 Promoter Holding: {L:.1f}%")
		else:A.append(f"⚠️ Low Promoter: {L:.1f}%")
	P=E([F_,G0])
	if P is not D:
		if P==0:B+=7;A.append('✅ Zero Pledged Shares')
		elif P<=5:B+=4;A.append(f"🟡 Low Pledge: {P:.1f}%")
		else:A.append(f"❌ High Pledge: {P:.1f}%")
	V=E([E2,'net sale'])
	if V and V>0:A.append(f"📊 Net Sales: ₹{V:.1f} Cr")
	W=E([E3])
	if W is not D:A.append(f"📦 % Delivery: {W:.1f}%")
	if B>=75:S='🟢 STRONG BUY'
	elif B>=55:S='🟡 WATCHLIST'
	elif B>=35:S='🟠 CAUTION'
	else:S='🔴 AVOID'
	return B,S,A
Gy=G1
def Gz():
	if Dv not in A.secrets:return
	B=A.secrets[Dv]
	if Ay(B,F):B=EU.loads(B)
	C=[JO,JP];D=Gp.from_service_account_info(B,scopes=C);return ET.authorize(D)
L_=JQ
def G_(client):
	try:
		A=client.open_by_key(L_)
		try:return A.worksheet(Gy)
		except ET.WorksheetNotFound:B=A.add_worksheet(title=Gy,rows=500,cols=6);B.append_row([j,AM,D4,D5,E4,E5]);return B
	except g:return
def M0():
	D=Gz()
	if not D:return
	E=G_(D)
	if not E:return
	try:
		I=E.get_all_records();G={}
		for B in I:
			H=F(B.get(j,C)).strip()
			if H:G[H]={BI:F(B.get(D4,C)),A4:F(B.get(AM,C)),CV:F(B.get(D5,C)),Bj:F(B.get(E4,C)),D6:F(B.get(E5,C))}
		A.session_state.watchlist=G
	except g:pass
def Ec():
	F=Gz()
	if not F:A.warning('⚠️ Google Sheet write failed — check secrets.');return J
	E=G_(F)
	if not E:return J
	try:
		E.clear();E.append_row([j,AM,D4,D5,E4,E5])
		for(G,D)in A.session_state.watchlist.items():E.append_row([G,D.get(A4,C),D.get(BI,C),D.get(CV,C),D.get(Bj,C),D.get(D6,C)])
		return B
	except g as H:A.warning(f"⚠️ Sheet write error: {H}");return J
def M1(sym,cmp=C,note=C,bf_score=C,bf_grade=C):A.session_state.watchlist[sym]={A4:cmp,BI:note,CV:bf_score,Bj:bf_grade,D6:l.now().strftime('%Y-%m-%d %H:%M')}
def H0(sym):A.session_state.watchlist.pop(sym,D)
if'watchlist_loaded'not in A.session_state:M0();A.session_state.watchlist_loaded=B
def M2(row_data,cols):
	N='sl_standard'
	def E(keys):
		for B in keys:
			for A in cols:
				if B in A.lower():
					try:D=F(row_data.get(A,C)).replace(AB,C).replace(AC,C).strip();return M(D)
					except(AV,Fr):pass
	B=E([A4]);I=E(['52w high',D7,'52wk high']);J=E([JZ,CU,'52wk low']);K=E([Jb,'50dma']);L=E([Fx,'200dma']);A={A4:B,G2:I,G3:J,'dma50':K,'dma200':L}
	if B and I and J:G=(I-J)/52;A[E6]=b(G,2);A['sl_tight']=b(B-Am*G,2);A[N]=b(B-1.5*G,2);A['sl_wide']=b(B-2.*G,2);O=2.;H=B-A[N];A['target_1r']=b(B+H*Am,2);A['target_2r']=b(B+H*O,2);A['target_3r']=b(B+H*3.,2);A[D8]=b(K,2)if K else D;A['trail_sl_200dma']=b(L,2)if L else D;A['risk_pct']=b(H/B*100,2)if B else D
	return A
def Ed(history):
	E='AI Analysis';B=history
	if not B:return b''
	F=H.DataFrame(B,columns=[j,'Model','Query','AI Result','Timestamp']);C=io.BytesIO()
	with H.ExcelWriter(C,engine=D9)as D:F.to_excel(D,index=J,sheet_name=E);A=D.sheets[E];A.column_dimensions['A'].width=12;A.column_dimensions['B'].width=14;A.column_dimensions['C'].width=40;A.column_dimensions['D'].width=80;A.column_dimensions['E'].width=20
	return C.getvalue()
if A.sidebar.button('🧹 Clear All Filters',use_container_width=B):
	for Ee in AL(A.session_state.keys()):
		if Ee.startswith('filter_')or Ee in(Jc,Jd,Je,Jf):del A.session_state[Ee]
	A.session_state.grid_reset_token+=1;A.rerun()
A.sidebar.markdown(c)
A.sidebar.header('🔍 Global Search')
H1=A.sidebar.text_input('Search by Symbol, Name, etc...',key=Jc)
A.sidebar.markdown(c)
A.sidebar.header('📑 Select a Tab')
M3=[BD,BE,CM,CN,CO,CP,CQ]
z=A.sidebar.selectbox('Choose sheet',M3,key='filter_sheet')
A.markdown(f"<p style='font-size:0.85rem; font-weight:bold; margin:0; padding:0;'>📄 {z}</p>",unsafe_allow_html=B)
with A.spinner('Downloading data from Google API...'):Ef=DK(z)
if not Ef.empty:
	Eg=0;R=[A for A in Ef.columns if not A.startswith(AX)and not A.startswith(AY)];M4=LL(z,R);Eh=LM.get(z)
	if Eh and Eh in R:Eg=R.index(Eh)
	else:
		for(BO,M5)in Ds(R):
			if M5.lower()in[D0,AZ,Dx,Dy,D1,Dz]:Eg=BO;break
	A.sidebar.markdown(c);A.sidebar.header('⚙️ Settings');Bz=A.sidebar.selectbox('Symbol Column (locked):',R,index=Eg,key='filter_symbol_col',disabled=B,help='Locked for consistency across sheets. To change it, edit LOCKED_SYMBOL_COLUMN near the top of the .py file.');H2=Lc(Ef,Bz);K=H2.copy()
	if H1:M6=K[R].astype(F).apply(lambda x:x.str.contains(H1,case=J,na=J)).any(axis=1);K=K[M6]
	A.sidebar.markdown(c);A.sidebar.header('🎨 Color Filters');Ei=A.sidebar.selectbox('Select Column to Filter by Color:',[AO]+R,key='filter_color_col')
	if Ei!=AO:
		Ej=f"_bg_{Ei}"
		if Ej in K.columns:
			M7=K[Ej].unique();Ek={C_:'⚪ White (Default)',x:'🟢 Green',AP:'🔴 Red',Jg:'🟡 Yellow','#4285f4':'🔵 Blue',Jh:'🟠 Orange','#b6d7a8':'🟩 Light Green','#f4cccc':'🟥 Light Red','#d9d2e9':'🟪 Light Purple'};El=[]
			for M8 in M7:
				Em=F(M8).lower()
				if Em in Ek:El.append(Ek[Em])
				else:El.append(f"🎨 Custom Hex: {Em}")
			H3=A.sidebar.multiselect(f"Select Colors in '{Ei}':",sorted(El),key='filter_color_selections')
			if H3:
				En=[]
				for Eo in H3:
					for(M9,Bx)in Ek.items():
						if Bx==Eo:En.append(M9)
					if Eo.startswith(Ji):En.append(Eo.replace(Ji,C))
				K=K[K[Ej].str.lower().isin(En)]
	A.sidebar.markdown(c);A.sidebar.header('🎯 Categorical Filters');MA=[A for A in R if AW(B in A.lower()for B in['cumulative average',G4,E7,Jj,Jk,G5,G6,G7,Jl,G8])]
	for DN in MA:
		MB=sorted([A for A in H2[DN].unique()if F(A).strip()!=C]);H4=A.sidebar.multiselect(f"Filter by {DN}:",options=MB,key=f"filter_cat_{DN}")
		if H4:K=K[K[DN].isin(H4)]
	A.sidebar.markdown(c);A.sidebar.header('📈 DMA Trend Filter');Ce=A.sidebar.selectbox('Select DMA Condition:',[Jm,Jn,Jo,Jp,Jq],key='filter_dma_trend')
	if Ce!=Jm:
		H5=U((A for A in R if Jb in A.lower()),D);H6=U((A for A in R if'100 dma'in A.lower()),D);H7=U((A for A in R if Fx in A.lower()),D)
		if H5 and H7:
			DO=H.to_numeric(K[H5].astype(F).str.replace(BG,C,regex=B),errors=AN);DP=H.to_numeric(K[H7].astype(F).str.replace(BG,C,regex=B),errors=AN)
			if Ce==Jp:K=K[DO>DP]
			elif Ce==Jq:K=K[DO<DP]
			elif H6:
				DQ=H.to_numeric(K[H6].astype(F).str.replace(BG,C,regex=B),errors=AN)
				if Ce==Jn:K=K[(DO<DQ)&(DQ<DP)]
				elif Ce==Jo:K=K[(DO>DQ)&(DQ>DP)]
	A.sidebar.markdown(c);A.sidebar.header('📊 Numeric Range Filters');Ep=U((A for A in R if'diff'in A.lower()and'200'in A.lower()),D)
	if Ep:K=DL(K,Ep,A.sidebar,'Diff. from 200 DMA Range:')
	Eq=U((A for A in R if E8 in A.lower()and'low'in A.lower()and(AC in A.lower()or'per'in A.lower())),D)
	if Eq:K=DL(K,Eq,A.sidebar,'From 52W Low Range:')
	Er=U((A for A in R if E8 in A.lower()and'high'in A.lower()and(AC in A.lower()or'per'in A.lower())),D)
	if Er:K=DL(K,Er,A.sidebar,'From 52W High Range:')
	MC=[w,AM,JL,Jr,Js,Jt,'Net Profit','EPS',Ju,Jv,'Enterprise Value','RSI','Delivery'];H8={Ep,Eq,Er}
	for Cf in MC:
		Es=U((A for A in R if Cf.lower()in A.lower()and A not in H8),D)
		if Es:K=DL(K,Es,A.sidebar);H8.add(Es)
	A.sidebar.markdown(c);A.sidebar.header('📅 Date Filters');H9=U((A for A in R if Jw in A.lower()),D);HA=U((A for A in R if Jx in A.lower()),D)
	if H9:K=Gv(K,H9,A.sidebar)
	if HA:K=Gv(K,HA,A.sidebar)
	A.sidebar.markdown(c);A.sidebar.header('📊 My Watchlist')
	if A.session_state.watchlist:
		HB=Q(A.session_state.watchlist);A.sidebar.caption(f"🔖 {HB} stock{"s"if HB>1 else C} saved")
		for(DR,Et)in AL(A.session_state.watchlist.items()):
			MD,ME=A.sidebar.columns([3,1]);MD.markdown(f"**{DR}** {"`"+Et[A4]+"`"if Et[A4]else C}<br><small style='color:gray'>{Et.get(BI,C)[:35]}</small>",unsafe_allow_html=B)
			if ME.button('❌',key=f"wl_rm_{DR}",help=f"Remove {DR}"):H0(DR);Ec();A.rerun()
		A.sidebar.markdown(C);MF=H.DataFrame([{j:B,AM:A[A4],D4:A[BI],D5:A.get(CV,C),E4:A.get(Bj,C),E5:A[D6]}for(B,A)in A.session_state.watchlist.items()]);HC=io.BytesIO()
		with H.ExcelWriter(HC,engine=D9)as MG:MF.to_excel(MG,index=J,sheet_name=G1)
		A.sidebar.download_button('📥 Download Watchlist Excel',data=HC.getvalue(),file_name=f"Watchlist_{l.now().strftime(Bk)}.xlsx",mime=Bl,use_container_width=B)
	else:A.sidebar.info('No stocks in watchlist yet.\nAdd from the workspace panel below.')
	if A.session_state.ai_history:
		A.sidebar.markdown(c);A.sidebar.header('🤖 AI History Export');A.sidebar.caption(f"{Q(A.session_state.ai_history)} analyses saved this session");MH=Ed(A.session_state.ai_history);A.sidebar.download_button('📥 Download All AI Results (Excel)',data=MH,file_name=f"AI_Analysis_{l.now().strftime(Jy)}.xlsx",mime=Bl,use_container_width=B)
		if A.sidebar.button('🗑️ Clear AI History',use_container_width=B):A.session_state.ai_history=[];A.rerun()
	BP=[]
	if Bz in K.columns:BP.append(Bz)
	B_=U((A for A in R if BH in A.lower()),D);MI=U((A for A in R if Jz in A.lower()or'prev'in A.lower()),D);A7=U((A for A in R if A4 in A.lower()),D);AJ=U((A for A in R if D2 in A.lower()),D);B4=U((A for A in R if E8 in A.lower()and'high'in A.lower()and BJ not in A.lower()and AC not in A.lower()),D);B5=U((A for A in R if E8 in A.lower()and'low'in A.lower()and BJ not in A.lower()and AC not in A.lower()),D);BQ=U((A for A in R if E3 in A.lower()),D);BR=U((A for A in R if'rsi'in A.lower()),D);Cg=U((A for A in R if G5 in A.lower()),D);BS=U((A for A in R if G6 in A.lower()),D);DS=U((A for A in R if G7 in A.lower()and A!=Cg and'dma'not in A.lower()),D);DT=U((A for A in R if'macd'in A.lower()),D);BT=U((A for A in R if G8 in A.lower()),D);BU=U((A for A in R if'diff'in A.lower()and'200'in A.lower()),D);HD=LP(z,R)
	if HD:
		for p in HD:
			if p not in BP:BP.append(p)
	else:
		for Cf in(B_,MI,A7,AJ,B4,B5):
			if Cf and Cf not in BP:BP.append(Cf)
	MJ=[A for A in K.columns if A not in BP and not A.startswith(AX)and not A.startswith(AY)and A!=n];MK=[A for A in K.columns if A.startswith(AX)or A.startswith(AY)or A==n];ML=BP+MJ+MK;K=K[ML];A.markdown(c)
	with A.expander(f"🚀 Executive Dashboard — {z}",expanded=B):
		A.caption('Live snapshot of the currently filtered stock universe. Adjust sidebar filters to update instantly.')
		def Af(series):
			A=series
			if A is D:return H.Series(dtype=M)
			return H.to_numeric(A.astype(F).str.replace('[%,₹\\s]',C,regex=B),errors=AN)
		W=K;MM=Q(W);Ag=Af(W[AJ])if AJ and AJ in W.columns else H.Series(dtype=M);HE=Af(W[B_])if B_ and B_ in W.columns else H.Series(dtype=M);AT=Af(W[A7])if A7 and A7 in W.columns else H.Series(dtype=M);BV=Af(W[B4])if B4 and B4 in W.columns else H.Series(dtype=M);Au=Af(W[B5])if B5 and B5 in W.columns else H.Series(dtype=M);HF=Af(W[BR])if BR and BR in W.columns else H.Series(dtype=M);HG=Af(W[BQ])if BQ and BQ in W.columns else H.Series(dtype=M);Eu=U((A for A in R if G9 in A.lower()),D);HH=Af(W[Eu])if Eu and Eu in W.columns else H.Series(dtype=M);r=Af(W[BU])if BU and BU in W.columns else H.Series(dtype=M);Ev=U((A for A in R if CS in A.lower()),D);HI=Af(W[Ev])if Ev and Ev in W.columns else H.Series(dtype=M);HJ=T((Ag>0).sum())if not Ag.empty else 0;Ew=T((Ag<0).sum())if not Ag.empty else 0;MN=T((Ag==0).sum())if not Ag.empty else 0;P7=M(Ag.mean())if Ag.notna().any()else i;P8=HJ/Ew if Ew>0 else D;P9=M(Ag.median())if Ag.notna().any()else D;PA=M(HE.sum())if HE.notna().any()else i;PB=M(HH.sum())if HH.notna().any()else i;PC=M(HI.sum())if HI.notna().any()else i;PD=M(HF.mean())if HF.notna().any()else D;PE=M(HG.mean())if HG.notna().any()else D;MO=T((r>0).sum())if r.notna().any()else 0;MP=T((r<0).sum())if r.notna().any()else 0;HK=0
		if BS and BS in W.columns:HK=T(W[BS].astype(F).str.contains('breakout|buy|bullish',case=J,na=J).sum())
		HL=0
		if BT and BT in W.columns:HL=T(W[BT].astype(F).str.contains('buy',case=J,na=J).sum())
		HM,HN=0,0;HO=0
		if AT.notna().any()and BV.notna().any():MQ=AT/BV.replace(0,A6.nan)*100;HM=T((MQ>=95).sum())
		if AT.notna().any()and Au.notna().any():HP=AT/Au.replace(0,A6.nan)*100;HN=T((HP<=105).sum());HO=T((HP<=115).sum())
		def AU(container,label,value,bg='#f5f7fa',fg='#1a1a1a'):container.markdown(f"<div style='background:{bg}; border-radius:10px; padding:12px 8px; text-align:center; border:1px solid rgba(0,0,0,0.06);'><div style='font-size:0.70em; color:#666; font-weight:700; letter-spacing:0.2px;'>{label}</div><div style='font-size:1.30em; font-weight:800; color:{fg}; margin-top:2px;'>{value}</div></div>",unsafe_allow_html=B)
		BW=A.columns(7);AU(BW[0],'📦 TOTAL STOCKS',f"{MM:,}");AU(BW[1],'🟢 ADVANCES',f"{HJ:,}",bg=CW,fg=GA);AU(BW[2],'🔴 DECLINES',f"{Ew:,}",bg=Bm,fg=DA);AU(BW[3],'⚪ UNCHANGED',f"{MN:,}");AU(BW[4],'🕳️ NEAR 52W LOW (≤15%)',f"{HO:,}"if AT.notna().any()and Au.notna().any()else DB,bg=Bm,fg=DA);AU(BW[5],'🚀 BREAKOUTS',f"{HK:,}",bg=GB,fg='#e65100');AU(BW[6],'✅ BUY SIGNALS',f"{HL:,}",bg=J_,fg='#0d47a1');A.markdown("<div style='margin-top:8px;'></div>",unsafe_allow_html=B);DU=A.columns(4);AU(DU[0],'🏔️ NEAR 52W HIGH (≥95%)',f"{HM:,}",bg=CW,fg=GA);AU(DU[1],'🕳️ NEAR 52W LOW (≤5%)',f"{HN:,}",bg=Bm,fg=DA);AU(DU[2],'📉 BELOW 200 DMA',f"{MP:,}"if r.notna().any()else DB,bg=Bm,fg=DA);AU(DU[3],'🎯 ABOVE 200 DMA',f"{MO:,}"if r.notna().any()else DB,bg=CW,fg=GA);A.markdown(CX,unsafe_allow_html=B);DV={K0:J,'modeBarButtons':[['toImage']]}
		def MR(frac):
			B=frac;B=AA(i,min(Am,B));D=[(i,(234,67,53)),(.5,(249,168,37)),(Am,(15,157,88))]
			for H in Dt(Q(D)-1):
				C,A=D[H];E,F=D[H+1]
				if C<=B<=E:G=(B-C)/(E-C)if E>C else i;I=T(A[0]+(F[0]-A[0])*G);J=T(A[1]+(F[1]-A[1])*G);K=T(A[2]+(F[2]-A[2])*G);return f"#{I:02x}{J:02x}{K:02x}"
			return'#999999'
		def PF(title_text,points,y_min,y_max,y_label,height=340):
			G=height;F=y_max;E=points;B=y_min
			if not E:A.info('No data available for this chart.');return
			N=Q(E);O=F-B or Am;H=C
			for(R,(S,I,T))in Ds(E):U=(I-B)/O;K=AA(i,min(Am,U));V=MR(K);W=R/AA(N-1,1)*100;X=(1-K)*100;H+=f'<a href="{T}" target="_blank" title="{S}: {I:.2f}{y_label}" style="position:absolute; left:{W:.3f}%; top:{X:.3f}%; width:11px; height:11px; margin:-6px 0 0 -6px; border-radius:50%; background:{V}; display:block; border:1px solid rgba(255,255,255,0.75); box-shadow:0 0 1px rgba(0,0,0,0.35); cursor:pointer;"></a>'
			L=C
			for(Y,M)in[(0,F),(25,D),(50,(B+F)/2),(75,D),(100,B)]:Z=f"{M:.0f}"if M is not D else C;L+=f'<div style="position:absolute; left:0; right:0; top:{Y}%; border-top:1px dashed rgba(0,0,0,0.08); height:0;"><span style="position:absolute; left:-2px; top:-8px; font-size:10px; color:#9aa0a6;">{Z}</span></div>'
			a=f'<div style="font-family:\'Source Sans Pro\',sans-serif;"><div style="font-weight:700; font-size:14px; margin-bottom:2px;">{title_text}</div><div style="font-size:11px; color:#9aa0a6; margin-bottom:8px;">Click any dot to open its NSE chart in a new tab</div><div style="position:relative; width:calc(100% - 26px); height:{G}px; margin-left:26px; background:#fff; border:1px solid rgba(0,0,0,0.08); border-radius:6px; overflow:hidden;">{L}{H}</div><div style="display:flex; justify-content:space-between; margin-left:26px; margin-top:4px;"><span style="font-size:10px; color:#ea4335;">● low</span><span style="font-size:10px; color:#f9a825;">● mid</span><span style="font-size:10px; color:#0f9d58;">● high</span></div></div>';P.html(a,height=G+90,scrolling=J)
		if Bz in W.columns:BX=W[Bz].astype(F)
		elif n in W.columns:BX=W[n].astype(F)
		else:BX=W.index.astype(F).to_series(index=W.index)
		if n in W.columns:C0=W[n].astype(F).str.strip()
		else:C0=BX.astype(F).str.replace('<[^>]+>',C,regex=B).str.strip()
		def HQ(fig,chart_key):
			O='customdata';N='points';M='selection';K=chart_key;H=fig;H.update_layout(clickmode='event+select')
			try:I=A.plotly_chart(H,use_container_width=B,key=K,on_select='rerun')
			except Fr:A.plotly_chart(H,use_container_width=B,key=K);A.caption('⚠️ Click-to-open needs Streamlit ≥ 1.35 — update `streamlit` in requirements.txt to enable it.');return
			C=D;F=I.get(M)if Ay(I,E)else Fs(I,M,D)
			if F:
				L=F.get(N)if Ay(F,E)else Fs(F,N,D)
				if L:
					J=L[-1];G=J.get(O)if Ay(J,E)else Fs(J,O,D)
					if G:C=G[0]if Ay(G,(AL,tuple))else G
			if C:
				P=f"https://charting.nseindia.com/?symbol={C}-EQ";Q,R=A.columns([3,1])
				with Q:A.success(f"Selected: **{C}**")
				with R:A.link_button('📈 Open on NSE',P,use_container_width=B)
				A.markdown(f"🔗 **More links for {C}:** [Trading View (🔗)](https://www.tradingview.com/symbols/{C}/) &nbsp;|&nbsp; [History Data (🔗)](https://www.equitypandit.com/historical-data/{C}) &nbsp;|&nbsp; [Screener (🔗)](https://www.screener.in/company/{C}) &nbsp;|&nbsp; [Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{C}) &nbsp;|&nbsp; [Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={C}) &nbsp;|&nbsp; [Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{C}/evaluation.jsp) &nbsp;|&nbsp; [NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={C})")
			else:A.caption('Click any dot above to select a stock — its NSE chart button and quick-links will appear here.')
		MS,MT=A.columns(2)
		with MS:
			if AT.notna().any()and BV.notna().any():HR=(BV-AT)/BV.replace(0,A6.nan)*100;HS=HR.dropna().sort_values(ascending=B).head(20).index;HT=H.DataFrame({j:BX.loc[HS].values,K1:HR.loc[HS].values}).iloc[::-1];HU=O.Figure(O.Bar(x=HT[K1],y=HT[j],orientation='h',marker_color=x));HU.update_layout(title='🏔️ Top 20 Nearest 52W High',template=q,height=560,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(HU,use_container_width=B,key=f"dash_nearhigh_{z}",config=DV)
			else:A.info('52-Week High column not detected for this sheet.')
		with MT:
			if AT.notna().any()and Au.notna().any():HV=(AT-Au)/Au.replace(0,A6.nan)*100;HW=HV.dropna().sort_values(ascending=B).head(20).index;HX=H.DataFrame({j:BX.loc[HW].values,K2:HV.loc[HW].values}).iloc[::-1];HY=O.Figure(O.Bar(x=HX[K2],y=HX[j],orientation='h',marker_color=AP));HY.update_layout(title='🕳️ Top 20 Nearest 52W Low',template=q,height=560,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(HY,use_container_width=B,key=f"dash_nearlow_{z}",config=DV)
			else:A.info('52-Week Low column not detected for this sheet.')
		MU,MV=A.columns(2)
		with MU:
			if AT.notna().any()and BV.notna().any()and Au.notna().any():MW=(BV-Au).replace(0,A6.nan);HZ=((AT-Au)/MW*100).clip(0,100);Ha=HZ.notna()&C0.notna();Hb=C0[Ha].str.strip().values;Hc=HZ[Ha].values;Hd=O.Figure(O.Scatter(x=Hb,y=Hc,mode=E9,marker=E(size=9,color=Hc,colorscale=[[0,AP],[.5,A_],[1,x]],cmin=0,cmax=100,showscale=B,colorbar=E(title='% of Range')),customdata=Hb,hovertemplate=K3));Hd.update_layout(title='📍 Position within 52-Week Range (0% = Low, 100% = High)',template=q,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=K4),yaxis_title='% of 52W Range');HQ(Hd,f"dash_range_{z}")
			else:A.info('52-Week High/Low columns not detected for this sheet.')
		with MV:
			if r.notna().any()and C0 is not D:He=r.notna()&C0.notna();Hf=C0[He].str.strip().values;DW=r[He].values;Hg=AA(abs(M(A6.nanmin(DW))),abs(M(A6.nanmax(DW))),1e-09);Hh=O.Figure(O.Scatter(x=Hf,y=DW,mode=E9,marker=E(size=9,color=DW,colorscale=[[0,AP],[.5,A_],[1,x]],cmin=-Hg,cmax=Hg,showscale=B,colorbar=E(title='% Diff')),customdata=Hf,hovertemplate=K3));Hh.update_layout(title='📐 Difference from 200 DMA (0% = at 200 DMA)',template=q,height=340,margin=E(t=40,b=10,l=10,r=10),xaxis=E(showticklabels=J,title=K4),yaxis_title=DC);HQ(Hh,f"dash_diff200_{z}")
			else:A.info(GC)
		MX,MY=A.columns(2)
		with MX:
			if r.notna().any():
				Hi=r[r<0].dropna().sort_values(ascending=B).head(20).index;Ex=H.DataFrame({j:BX.loc[Hi].values,DC:r.loc[Hi].values}).iloc[::-1]
				if not Ex.empty:Hj=O.Figure(O.Bar(x=Ex[DC],y=Ex[j],orientation='h',marker_color=AP));Hj.update_layout(title='📉 Top 20 Below 200 DMA',template=q,height=560,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(Hj,use_container_width=B,key=f"dash_below200_{z}",config=DV)
				else:A.info('No stocks currently below 200 DMA.')
			else:A.info(GC)
		with MY:
			if r.notna().any():
				Hk=r[r>0].dropna().sort_values(ascending=J).head(20).index;Ey=H.DataFrame({j:BX.loc[Hk].values,DC:r.loc[Hk].values}).iloc[::-1]
				if not Ey.empty:Hl=O.Figure(O.Bar(x=Ey[DC],y=Ey[j],orientation='h',marker_color=x));Hl.update_layout(title='🎯 Top 20 Above 200 DMA',template=q,height=560,margin=E(t=40,b=10,l=10,r=10));A.plotly_chart(Hl,use_container_width=B,key=f"dash_above200_{z}",config=DV)
				else:A.info('No stocks currently above 200 DMA.')
			else:A.info(GC)
	A.markdown(c);MZ,Ma,Mb=A.columns([3,1,2.2])
	with MZ:Hm=A.radio(GD,[GE,CY,CZ],horizontal=B,help='Automatically adjust the column widths based on the text length of the selected row.')
	with Mb:A.markdown("<div style='margin-top: 2px; font-size:0.9rem;'>🔍 Filter stocks inside this matrix...</div>",unsafe_allow_html=B);Hn=A.text_input(K5,placeholder=K6,key=Jd,label_visibility='collapsed')
	if Hn:K=K[K[n].astype(F).str.contains(Hn,case=J,na=J)]
	Mc=Gw(K);Ho=io.BytesIO()
	with H.ExcelWriter(Ho,engine=D9)as Md:Me=z[:31].replace(':',C).replace('/',C);Mc.to_excel(Md,index=J,sheet_name=Me)
	with Ma:A.markdown("<div style='margin-top: 28px;'></div>",unsafe_allow_html=B);A.download_button(label='📥 Download as Excel',data=Ho.getvalue(),file_name=f"{z}_Export_{l.now().strftime(Bk)}.xlsx",mime=Bl,use_container_width=J)
	Mf,Mg=A.columns([1,4])
	with Mf:A.write(f"**Rows:** {K.shape[0]} | **Columns:** {Q(R)}")
	with Mg:Mh=A.empty()
	DX=B2("\n    class HtmlRenderer {\n        init(params) {\n            this.eGui = document.createElement('span');\n            this.eGui.innerHTML = params.value ? String(params.value) : '';\n        }\n        getGui() {\n            return this.eGui;\n        }\n    }\n    ");Hp=B2('\n    function(params) {\n        let colName = params.colDef.field;\n        let c_low = colName.toLowerCase();\n\n        let bgCol = "_bg_" + colName;\n        let txtCol = "_txt_" + colName;\n\n        let bgColor = params.data[bgCol];\n        let txtColor = params.data[txtCol];\n\n        let isTargetCol = c_low.includes("cmp") || c_low.includes("close price") || c_low.includes("prev");\n\n        if (isTargetCol) {\n            if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') return null;\n            return {\n                \'backgroundColor\': bgColor,\n                \'color\': txtColor || \'#000000\',\n                \'fontWeight\': (txtColor === \'#ffffff\' || bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n            };\n        }\n\n        if (!bgColor || bgColor.toLowerCase() === \'#ffffff\') {\n            return { \'color\': \'#000000\' };\n        }\n\n        return {\n            \'backgroundColor\': bgColor,\n            \'color\': \'#000000\',\n            \'fontWeight\': (bgColor === \'#0f9d58\' || bgColor === \'#ea4335\') ? \'bold\' : \'normal\'\n        };\n    }\n    ');B6=EW.from_dataframe(K);B6.configure_selection(selection_mode='single',use_checkbox=B);B6.configure_side_bar(filters_panel=J,columns_panel=B);Mi=[D0,D1,K7,K8,AZ,G4,E7];Ch=B
	for p in K.columns:
		if p.startswith(AX)or p.startswith(AY)or p==n:B6.configure_column(p,hide=B);continue
		if p in M4:B6.configure_column(p,hide=B);continue
		if Hm==CY and Q(K)>0:
			Ez=By(K.iloc[0][p]);E_=Q(F(p));Ci=T(AA(Ez,E_)*7+22)
			if Ch:Ci+=30
			DY,DZ=Ci,40
		elif Hm==CZ and Q(K)>1:
			Ez=By(K.iloc[1][p]);E_=Q(F(p));Ci=T(AA(Ez,E_)*7+22)
			if Ch:Ci+=30
			DY,DZ=Ci,40
		else:DY,DZ=(220,150)if p.lower()in Mi else(120,80)
		Cj=p==Bz;Hq=DD if Cj or Ch else D
		if Ch:Ch=J
		Mj=p.lower()
		if Cj or AW(A in Mj for A in[JR,JS,JT,JU,JV,JW,JX,'nse']):B6.configure_column(p,width=DY,minWidth=DZ,sortable=B,filter=B,resizable=B,editable=J,pinned=Hq,lockPinned=Cj,suppressMovable=Cj,checkboxSelection=Cj,cellRenderer=DX,cellStyle=Hp)
		else:B6.configure_column(p,width=DY,minWidth=DZ,sortable=B,filter=B,resizable=B,editable=J,pinned=Hq,cellStyle=Hp)
	B6.configure_grid_options(domLayout=AQ,rowHeight=35,headerHeight=45,enableCellTextSelection=B,ensureDomOrder=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);Mk=B6.build();Ml=EV(K,gridOptions=Mk,theme=GF,update_mode=LC.SELECTION_CHANGED,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,enable_enterprise_modules=J,height=400,width=GG,key=f"primary_stock_table_grid_{A.session_state.grid_reset_token}");BY=Ml.get('selected_rows',[])
	if BY is not D and Q(BY)>0 or Q(K)>0:
		if BY is not D and Q(BY)>0:S=BY.iloc[0]if Ay(BY,H.DataFrame)else BY[0]
		else:S=K.iloc[0]
		G=F(S.get(n,C)).strip()
		if G:
			with Mh.container():A.markdown(f"**⚡ {G} Links:** [Trading View (🔗)](https://www.tradingview.com/symbols/{G}/) &nbsp;|&nbsp; [History Data (🔗)](https://www.equitypandit.com/historical-data/{G}) &nbsp;|&nbsp; [Screener (🔗)](https://www.screener.in/company/{G}) &nbsp;|&nbsp; [Zerodha (🔗)](https://zerodha.com/markets/stocks/NSE/{G}) &nbsp;|&nbsp; [Chartlink (🔗)](https://chartink.com/stocks-new?load-snapshot=exponential-moving-average-simple-moving-average-simple-moving-average-moving-average-convergence-divergence-chart-snapshot-175&symbol={G}) &nbsp;|&nbsp; [Market Smith (🔗)](https://marketsmithindia.com/mstool/eval/{G}/evaluation.jsp) &nbsp;|&nbsp; [NSE URL (🔗)](https://www.nseindia.com/get-quotes/equity?symbol={G})")
			A.markdown(f"---");A.subheader(f"🛠️ Live Workspace Panel: {G}");A8=A.slider('📏 Adjust Panel Box Height (px):',min_value=300,max_value=1000,value=500,step=50,key='panel_height_slider');A9=A.tabs(['🕯️ Price Chart (EMA + RSI)','📈 Chart & Trade Info (NSE Component)','📋 History Data (EquityPandit)','🎯 Bullish/Bearish Zone','📁 Screener Documents','🪁 Zerodha Portal','📊 MarketSmith India','📉 TradingView Symbol Profile','🤖 AI Stock Analysis','💻 AI Pine Script Builder','🔬 Bottom Fishing Score','🎯 GTT Order Calculator','📊 Watchlist Manager','📰 News Feed'])
			with A9[1]:Hr=f"https://charting.nseindia.com/?symbol={G}-EQ";A.markdown(f"**NSE Interactive Chart Frame** &nbsp;|&nbsp; [🌐 Open in Browser]({Hr})",unsafe_allow_html=J);A.caption(Bn);P.html(f'<iframe src="{Hr}" width="100%" height="{A8}" style="border:none; border-radius:5px;"></iframe>',height=A8+20)
			with A9[2]:Hs=f"https://www.equitypandit.com/historical-data/{G.lower()}";A.markdown(f"**EquityPandit Historical Matrix Data** &nbsp;|&nbsp; [🌐 Open in Browser]({Hs})");A.caption(Bn);P.html(f'<iframe src="{Hs}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[3]:Ht=f"https://www.equitypandit.com/share-price/{G.lower()}#chart";A.markdown(f"**Bullish / Bearish Zone Indicator** &nbsp;|&nbsp; [🌐 Open in Browser]({Ht})");A.caption(Bn);P.html(f'<iframe src="{Ht}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[4]:Hu=f"https://www.screener.in/company/{G}/consolidated/";A.markdown(f"**Screener Corporate Filings** &nbsp;|&nbsp; [🌐 Open in Browser]({Hu})");A.caption(Bn);P.html(f'<iframe src="{Hu}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[5]:Hv=f"https://zerodha.com/markets/stocks/NSE/{G}/";A.markdown(f"**Zerodha Markets Financial Performance Metrics** &nbsp;|&nbsp; [🌐 Open in Browser]({Hv})");A.caption(Bn);P.html(f'<iframe src="{Hv}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[6]:Hw=f"https://marketsmithindia.com/mstool/eval/{G.lower()}/evaluation.jsp";A.markdown(f"**MarketSmith India Institutional Trading Evaluation Engine** &nbsp;|&nbsp; [🌐 Open in Browser]({Hw})");A.caption(Bn);P.html(f'<iframe src="{Hw}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[7]:Hx=f"https://www.tradingview.com/symbols/{G}/";A.markdown(f"**TradingView Comprehensive Asset Market Registry Summary Profile** &nbsp;|&nbsp; [🌐 Open in Browser]({Hx})");A.caption(Bn);P.html(f'<iframe src="{Hx}" width="100%" height="{A8}" style="border:none; border-radius:5px; background-color:white;"></iframe>',height=A8+20)
			with A9[8]:
				A.markdown(f"### 🤖 Ask AI About **{G}**")
				if not EX:A.warning(K9)
				else:
					Da=EZ('analysis');A.caption('⚡ Groq = llama-3.3-70b (free, fast) &nbsp;|&nbsp; 🧠 Gemini = gemini-2.5-flash'if BN and Cd else'⚡ Groq connected'if BN else'🧠 Gemini connected');A.write('Using the live data pulled from your dashboard, the AI can analyze technicals, ranges, and context.');F0=A.text_area('Your Query:',value=f"Based on the current data provided, give me a quick summary of the technical performance and trend for {G}.",height=80,key='ai_query_analysis')
					if A.button('✨ Generate AI Analysis',use_container_width=B,key='btn_ai_analysis'):
						with A.spinner(f"Analyzing {G} with {Da}..."):
							try:F1={A:B for(A,B)in S.items()if not F(A).startswith(Bo)};Ck=f"""
You are a professional stock market analyst evaluating Indian NSE stocks.
The user is asking about the stock: {G}.

Here is the live data extracted directly from the user's dashboard for this stock:
{F1}

User Query: {F0}

Please provide a clear, concise, and professional response.
""";F2=EY(Ck,Da);A.session_state[GH]={DE:G,EA:Da,'query':F0,DF:F2};A.session_state.ai_history.append([G,Da,F0,F2,l.now().strftime(CR)]);A.info(F2)
							except g as BZ:A.error(f"AI error: {BZ}")
					if A.session_state.get(GH,{}).get(DE)==G:
						Cl=A.session_state[GH];Db=Cl[DF];A.markdown(c);Mm,Mn,Mo=A.columns(3)
						with Mm:Mp=Ed([[G,Cl[EA],Cl['query'],Db,l.now().strftime(CR)]]);A.download_button('📥 Save as Excel',data=Mp,file_name=f"AI_{G}_{l.now().strftime(Jy)}.xlsx",mime=Bl,use_container_width=B,key='dl_ai_excel_analysis')
						with Mn:Mq=urllib.parse.quote(f"📊 *{G} AI Analysis* ({Cl[EA]})\n\n{Db[:800]}"+('\n\n_(truncated)_'if Q(Db)>800 else C));A.markdown(f"<a href='https://wa.me/?text={Mq}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
						with Mo:Mr=urllib.parse.quote(f"📊 {G} AI Analysis ({Cl[EA]})\n\n{Db[:800]}");A.markdown(f"<a href='https://t.me/share/url?url=NSEDashboard&text={Mr}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-size:14px;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
					A.markdown(c);A.markdown('**💡 Suggested Prompts** — copy any prompt below and paste it into the query box above:');Ms='\n'.join([f"{A+1}. {B.replace("{sym}",G)}"for(A,B)in Ds(LG)]);A.text(Ms)
			with A9[9]:
				A.markdown(f"### 💻 AI Pine Script Generator for **{G}**")
				if not EX:A.warning(K9)
				else:
					Mt=EZ('pine');A.write("Generate a custom TradingView Pine Script v5 strategy tailored to this stock's current metrics.");Hy=A.selectbox('Select Strategy Focus:',['Volume Breakout with Dynamic Stop Loss','Moving Average Crossover (50/100/200 DMA)','Trend Following with Trailing Stop','Mean Reversion from 52W High/Low'],key='pine_strategy_focus');Mu=A.text_area('Additional Custom Rules (Optional):',value=f"Include risk management parameters and plot signals on the chart.",height=60,key='pine_query')
					if A.button('⚙️ Generate TradingView Pine Script',use_container_width=B,key='btn_pine'):
						with A.spinner(f"Writing Pine Script v5 code for {G}..."):
							try:F1={A:B for(A,B)in S.items()if not F(A).startswith(Bo)};Ck=f'''
You are an expert quantitative developer specializing in TradingView Pine Script v5.

Write a complete, ready-to-copy Pine Script v5 strategy for the stock: {G}.

Strategy Focus: {Hy}
Custom Rules: {Mu}

Here is the live fundamental and technical data for {G} to incorporate as baseline context or threshold values if relevant:
{F1}

Formatting Requirements:
1. Start with `//@version=5` and `strategy("{G} Custom Script", overlay=true)`
2. Include clear comments explaining the logic.
3. Provide ONLY the Pine Script code inside a markdown code block, no other conversational text.
''';Hz=EY(Ck,Mt);A.session_state[GI]={DE:G,DF:Hz};A.markdown('### 📋 Your Custom Strategy Code:');A.write('Copy the code below and paste it into the TradingView Pine Editor.');A.markdown(Hz)
							except g as BZ:A.error(f"AI error: {BZ}")
					if A.session_state.get(GI,{}).get(DE)==G:Mv=A.session_state[GI][DF];Mw=Ed([[G,'Pine Script',Hy,Mv,l.now().strftime(CR)]]);A.download_button('📥 Save Pine Script as Excel',data=Mw,file_name=f"PineScript_{G}_{l.now().strftime(Bk)}.xlsx",mime=Bl,key='dl_pine_excel')
					A.markdown(c);A.markdown('**📋 Custom Rules Reference** — copy any rule and paste it into the Additional Custom Rules box above:');A.text(LH)
			with A9[10]:
				A.markdown(f"### 🔬 Bottom Fishing Analysis: **{G}**");A.caption('Scores this stock on 8 key criteria for buying from the bottom. Based entirely on your live sheet data.');H_={A:B for(A,B)in S.items()if not F(A).startswith(Bo)};C1,F3,F4=DM(H_,R);F5=Aa if C1>=75 else Jg if C1>=55 else Jh if C1>=35 else AP;A.markdown(f'''
                <div style="background:{F5}22; border-left:6px solid {F5}; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
                    <div style="font-size:2rem; font-weight:bold; color:{F5};">{C1}/100</div>
                    <div style="font-size:1.3rem; font-weight:bold;">{F3}</div>
                    <div style="font-size:0.85rem; color:#555; margin-top:4px;">Bottom Fishing Composite Score for {G}</div>
                </div>
                ''',unsafe_allow_html=B);A.markdown('#### 📋 Detailed Scoring Breakdown')
				for Mx in F4:A.markdown(f"- {Mx}")
				A.markdown(c);A.markdown('#### 📖 Scoring Criteria');My='\n| # | Criteria | Max Points | Description |\n|---|----------|-----------|-------------|\n| 1 | **52W Low Proximity** | 30 | CMP is 8–15% above 52W Low (ideal entry zone) |\n| 2 | **Uptrend (200 DMA)** | 15 | CMP above 200 DMA = confirmed uptrend |\n| 3 | **Volume Activity** | 10 | High trading volume = institutional interest |\n| 4 | **Low/Zero Debt** | 10 | D/E ratio ≤ 0.1 is ideal (no loan burden) |\n| 5 | **Net Profitability** | 10 | Positive net profit confirms fundamental health |\n| 6 | **RONW %** | 10 | Return on Net Worth ≥ 15% = strong business |\n| 7 | **Promoter Holding** | 8 | ≥ 50% shows management confidence |\n| 8 | **Zero Pledge** | 7 | No pledged shares = no financial stress |\n';A.markdown(My);A.info('💡 **Buy Strategy:** Look for scores ≥ 55 (Watchlist) or ≥ 75 (Strong Buy). The sweet zone is CMP at 8–15% above 52W Low with uptrend confirmed (CMP > 200 DMA), backed by positive profits, low debt, and high promoter holding. This combination maximizes probability of a bull run from the bottom.')
				if EX:
					A.markdown(c);F6=EZ('bf')
					if A.button('🤖 Get AI Deep Analysis for Bottom Buy',use_container_width=B,key='bf_ai_btn'):
						with A.spinner(f"Running deep bottom-fishing analysis for {G} with {F6}..."):
							try:Ck=f"""
You are an expert Indian stock market analyst specializing in bottom-fishing and value investing.

Stock: {G}
Live Data from Dashboard: {H_}
Bottom Fishing Score: {C1}/100
Grade: {F3}
Scoring Breakdown: {chr(10).join(F4)}

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
""";F7=EY(Ck,F6);A.session_state['last_bf_ai_result']={DE:G,DF:F7};A.session_state.ai_history.append([G,F6,'Bottom Fishing Deep Analysis',F7,l.now().strftime(CR)]);A.success('✅ AI Analysis Complete');A.markdown(F7)
							except g as BZ:A.error(f"AI error: {BZ}")
					A.markdown(c);A.markdown('#### 📤 Share BF Score Card');I0=f"""🔬 *Bottom Fishing Score: {G}*

📊 Score: *{C1}/100*
📈 Grade: {F3}

"""+'\n'.join(F4[:5])+f"\n\n🕒 {l.now().strftime(KA)}\n📌 NSE Stock Dashboard";Mz=urllib.parse.quote(I0);M_=urllib.parse.quote(I0);N0,N1=A.columns(2)
					with N0:A.markdown(f"<a href='https://wa.me/?text={Mz}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share on WhatsApp</button></a>",unsafe_allow_html=B)
					with N1:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={M_}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share on Telegram</button></a>",unsafe_allow_html=B)
			with A9[11]:
				A.markdown(f"### 🎯 GTT Order Calculator: **{G}**");A.caption('Auto-suggest Stop-Loss, Targets & ATR-based GTT levels from your live sheet data.');N2={A:B for(A,B)in S.items()if not F(A).startswith(Bo)};AF=M2(N2,R)
				if not AF.get(A4):A.warning('⚠️ CMP column not found in sheet data. Cannot compute GTT levels.')
				else:
					V=AF[A4];N3,N4,N5,N6=A.columns(4);N3.metric('📍 CMP',f"₹{V:,.2f}")
					if AF.get(G2):N4.metric('⬆️ 52W High',f"₹{AF[G2]:,.2f}")
					if AF.get(G3):N5.metric('⬇️ 52W Low',f"₹{AF[G3]:,.2f}")
					if AF.get(E6):N6.metric('📊 ATR (approx)',f"₹{AF[E6]:,.2f}")
					A.markdown(c);A.markdown('#### ⚙️ Customize ATR Multiplier');N7,N8=A.columns(2);I1=N7.number_input('Manual ATR Override (₹) — leave 0 to use auto',min_value=i,value=i,step=.5,key='gtt_manual_atr');Dc=N8.selectbox('Risk-Reward Ratio:',['1:1','1:1.5','1:2','1:2.5','1:3'],index=2,key='gtt_rr_ratio');N9=M(Dc.split(':')[1]);C2=I1 if I1>0 else AF.get(E6,0)
					if C2 and C2>0:
						I2=b(V-Am*C2,2);C3=b(V-1.5*C2,2);I3=b(V-2.*C2,2);Dd=V-C3;De=b(V+Dd*Am,2);Df=b(V+Dd*N9,2);Dg=b(V+Dd*3.,2);NA=b(Dd/V*100,2);A.markdown('#### 🛡️ Stop-Loss Levels');F8=H.DataFrame([{EB:'Tight SL (1× ATR)',BK:I2,EC:b((V-I2)/V*100,2),ED:'Intraday / Scalp'},{EB:'Standard SL (1.5× ATR)',BK:C3,EC:b((V-C3)/V*100,2),ED:'Swing / BTST'},{EB:'Wide SL (2× ATR)',BK:I3,EC:b((V-I3)/V*100,2),ED:'Positional'}])
						if AF.get(D8):F8=H.concat([F8,H.DataFrame([{EB:'Trail SL @ 50 DMA',BK:AF[D8],EC:b((V-AF[D8])/V*100,2)if AF[D8]<V else 0,ED:'Trailing Stop'}])],ignore_index=B)
						A.dataframe(F8,use_container_width=B,hide_index=B);A.markdown(f"#### 🎯 Target Levels (based on {Dc} R:R)");NB=H.DataFrame([{GJ:'T1 (1R)',BK:De,GK:b((De-V)/V*100,2),GL:'Book 30–40%'},{GJ:f"T2 ({Dc} R:R)",BK:Df,GK:b((Df-V)/V*100,2),GL:'Book 40–50%'},{GJ:'T3 (3R — runner)',BK:Dg,GK:b((Dg-V)/V*100,2),GL:'Hold remainder'}]);A.dataframe(NB,use_container_width=B,hide_index=B);A.markdown('#### 💰 Position Sizing Helper');NC,ND=A.columns(2);NE=NC.number_input('Capital (₹):',min_value=1000,value=100000,step=5000,key='gtt_capital');I4=ND.number_input('Max Risk % of Capital:',min_value=.5,max_value=1e1,value=2.,step=.5,key='gtt_risk_pct');I5=NE*I4/100;F9=T(I5/(V-C3))if V-C3>0 else 0;I6=F9*V;A.success(f"📦 Suggested Qty: **{F9} shares** &nbsp;|&nbsp; Investment: **₹{I6:,.0f}** &nbsp;|&nbsp; Max Loss: **₹{I5:,.0f}** ({I4}%)");A.markdown(c);A.markdown('#### 📋 GTT Order Summary (Copy-Ready)');FA=f"""🎯 *GTT Order: {G}*

📍 Entry CMP: ₹{V:,.2f}
🛡️ Stop-Loss: ₹{C3:,.2f} ({NA:.1f}% risk)
🎯 Target 1:  ₹{De:,.2f} (+{b((De-V)/V*100,1)}%)
🎯 Target 2:  ₹{Df:,.2f} (+{b((Df-V)/V*100,1)}%)
🎯 Target 3:  ₹{Dg:,.2f} (+{b((Dg-V)/V*100,1)}%)
📦 Qty: {F9} shares | ₹{I6:,.0f}
📊 ATR: ₹{C2:.2f} | R:R {Dc}
🕒 {l.now().strftime(KA)}""";A.code(FA,language=C);NF=urllib.parse.quote(FA);NG=urllib.parse.quote(FA);NH,NI=A.columns(2)
						with NH:A.markdown(f"<a href='https://wa.me/?text={NF}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share GTT on WhatsApp</button></a>",unsafe_allow_html=B)
						with NI:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={NG}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share GTT on Telegram</button></a>",unsafe_allow_html=B)
					else:A.warning('⚠️ Could not compute ATR — 52W High/Low columns not found in sheet. Please enter ATR manually above.')
			with A9[12]:
				A.markdown(f"### 📊 Watchlist Manager");I7={A:B for(A,B)in S.items()if not F(A).startswith(Bo)};NJ,NK,_=DM(I7,R);NL=F(I7.get(A7,C))if A7 else C;FB=G in A.session_state.watchlist;A.markdown(f"**Current Stock: {G}** {"✅ Already in Watchlist"if FB else C}");NM=A.text_input('📝 Note (optional):',value=A.session_state.watchlist.get(G,{}).get(BI,C),placeholder='e.g. Near 52W low, watching for breakout',key=f"wl_note_{G}");NN,NO=A.columns(2)
				with NN:
					if A.button(f"{"🔄 Update"if FB else"➕ Add"} {G} to Watchlist",use_container_width=B,key='wl_add_btn'):
						M1(G,cmp=NL,note=NM,bf_score=F(NJ),bf_grade=NK);NP=Ec()
						if NP:A.success(f"✅ {G} saved to Watchlist (Google Sheet updated!)")
						else:A.info(f"✅ {G} added to session Watchlist (Sheet write failed — check secrets).")
						A.rerun()
				with NO:
					if FB:
						if A.button(f"❌ Remove {G} from Watchlist",use_container_width=B,key='wl_rm_btn'):H0(G);Ec();A.rerun()
				A.markdown(c);A.markdown('#### 🗂️ Your Full Watchlist')
				if A.session_state.watchlist:
					NQ=[{j:B,'CMP (₹)':A[A4],D5:A.get(CV,C),GM:A.get(Bj,C),D4:A.get(BI,C),'Added':A.get(D6,C)}for(B,A)in A.session_state.watchlist.items()];I8=H.DataFrame(NQ);A.dataframe(I8,use_container_width=B,hide_index=B);I9=io.BytesIO()
					with H.ExcelWriter(I9,engine=D9)as NR:I8.to_excel(NR,index=J,sheet_name=G1)
					A.download_button('📥 Download Watchlist as Excel',data=I9.getvalue(),file_name=f"Watchlist_{l.now().strftime(Bk)}.xlsx",mime=Bl,use_container_width=B,key='dl_wl_excel_tab');NS='\n'.join([f"• {B} — Score:{A.get(CV,C)} {A.get(Bj,C).split()[0]if A.get(Bj)else C} — {A.get(BI,C)[:30]}"for(B,A)in AL(A.session_state.watchlist.items())[:15]]);IA=f"📊 *My NSE Watchlist*\n\n{NS}\n\n🕒 {l.now().strftime(EE)}";NT=urllib.parse.quote(IA);NU=urllib.parse.quote(IA);A.markdown(C);NV,NW=A.columns(2)
					with NV:A.markdown(f"<a href='https://wa.me/?text={NT}' target='_blank'><button style='width:100%;padding:8px;background:#25D366;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>📱 Share Watchlist on WhatsApp</button></a>",unsafe_allow_html=B)
					with NW:A.markdown(f"<a href='https://t.me/share/url?url=Dashboard&text={NU}' target='_blank'><button style='width:100%;padding:8px;background:#229ED9;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold;'>✈️ Share Watchlist on Telegram</button></a>",unsafe_allow_html=B)
				else:A.info('Your watchlist is empty. Add stocks using the button above!')
			with A9[13]:
				A.markdown(f"### 📰 Latest News & Alerts: **{G}**");import urllib.request,urllib.parse,xml.etree.ElementTree as C4,datetime as l,email.utils
				def NX(pubdate_str):
					try:
						E=email.utils.parsedate_to_datetime(pubdate_str);F=l.datetime.now(l.timezone.utc);G=F-E;A=G.total_seconds()
						if A<0:return AH
						if A<60:return f"{T(A)} secs ago"
						if A<3600:B=T(A/60);return f"{B} min{"s"if B!=1 else C} ago"
						if A<86400:D=T(A/3600);return f"{D} hour{"s"if D!=1 else C} ago"
						if A<172800:return'Yesterday'
						H=T(A/86400);return f"{H} days ago"
					except g:return GN
				@A.cache_data(ttl=600)
				def NY(target_symbol,limit=10):
					try:
						I=urllib.parse.quote(f'"{target_symbol}" stock share news NSE India');J=f"https://news.google.com/rss/search?q={I}&hl=en-IN&gl=IN&ceid=IN:en";K=urllib.request.Request(J,headers={Ca:Cb})
						with urllib.request.urlopen(K)as M:N=M.read()
						O=C4.fromstring(N);P=[D7,EF,CU,EG,EH,EI,EJ,EK];E=[]
						for A in O.findall(DG):
							F=A.find(A5).text;Q=A.find(f).text;G=A.find(An).text if A.find(An)is not D else C;R=AW(A in F.lower()for A in P);S=GO if R else C
							try:H=email.utils.parsedate_to_datetime(G)
							except g:H=l.datetime.min.replace(tzinfo=l.timezone.utc)
							E.append({AD:f"{S}{F}",f:Q,L:NX(G),AI:H})
						E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
					except g:return[]
				with A.spinner(f"Fetching today's latest news for {G}..."):
					IB=NY(G,limit=10)
					if IB:
						for N in IB:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.5em 0; opacity: 0.2;'>",unsafe_allow_html=B)
					else:A.info(f"No recent news found for {G}.")
			with A9[0]:
				with A.expander(f"🕯️ Price Chart & Technical Indicators — {G}",expanded=B):
					NZ=A.select_slider('History range:',options=['3mo','6mo','1y','2y','5y'],value='1y',key=f"chart_period_{G}")
					with A.spinner(f"Loading price history for {G}..."):m=Lb(G,period=NZ)
					if m.empty or BF not in m.columns:A.warning(f"⚠️ No historical price data available for **{G}** via Yahoo Finance (tried `{G}.NS`). The symbol may be delisted, renamed, or not tracked by Yahoo.")
					else:
						Ah=m[BF].squeeze().dropna();AK=M(Ah.iloc[-1]);Ba=M(Ah.iloc[-2])if Q(Ah)>1 else AK;Dh=(AK-Ba)/Ba*100 if Ba else i;IC=Ah.diff();Na=IC.clip(lower=0).rolling(14).mean();Nb=(-IC.clip(upper=0)).rolling(14).mean();FC=100-100/(1+Na/Nb.replace(0,M(A3)));Cm=FC.dropna().iloc[-1]if not FC.dropna().empty else D;Nc,Nd=A.tabs(['Price + EMAs','RSI'])
						with Nc:
							Ne=A.radio('Chart type',[KB,'Line'],horizontal=B,key=f"chart_type_{G}");ID=Ah.diff();Nf=ID.clip(lower=0).rolling(9).mean();Ng=(-ID.clip(upper=0)).rolling(9).mean();Av=100-100/(1+Nf/Ng.replace(0,M(A3)));FD=Av.ewm(span=3,adjust=J).mean();IE=A6.arange(1,22,dtype=M);FE=Av.rolling(21).apply(lambda x:M(A6.dot(x,IE)/IE.sum()),raw=B);u=AL(m.index);IF=Av.values;Cn,IG=[],[];FF,IH=[],[]
							for BO in Dt(22,Q(Av)):
								FG,II=IF[BO],IF[BO-1]
								if A6.isnan(FG)or A6.isnan(II):continue
								if FG>=50 and II<50:
									Di=Av.index[BO]
									if Di in Ah.index:Cn.append(Di);IG.append(M(Ah.loc[Di])*.993);FF.append(Di);IH.append(M(FG))
							if not FD.dropna().empty and not FE.dropna().empty:FH=FD.dropna().iloc[-1];FI=FE.dropna().iloc[-1];FJ=GP if FH>FI else GQ;Nh='🟢 H-M: POSITIVE (Bullish)'if FH>FI else'🔴 H-M: NEGATIVE (Bearish)';A.markdown(f"<div style='background:{FJ}22;border-left:4px solid {FJ};padding:6px 12px;border-radius:4px;margin-bottom:6px;font-size:13px;font-weight:700;color:{FJ}'>{Nh} — EMA3: {FH:.1f} | WMA21: {FI:.1f}</div>",unsafe_allow_html=B)
							e=LD(rows=3,cols=1,shared_xaxes=B,row_heights=[.55,.25,.2],vertical_spacing=.03,specs=[[{GR:'xy'}],[{GR:'xy'}],[{GR:'xy'}]])
							if Ne==KB:
								try:e.add_trace(O.Candlestick(x=u,open=m['Open'].squeeze(),high=m[EL].squeeze(),low=m[EM].squeeze(),close=m[BF].squeeze(),name='OHLC',increasing_line_color=GS,decreasing_line_color=GT,increasing_fillcolor=GS,decreasing_fillcolor=GT,line=E(width=1.6),whiskerwidth=.9),row=1,col=1)
								except g:e.add_trace(O.Scatter(x=u,y=Ah,name=BF,line=E(color=AE,width=2)),row=1,col=1)
							else:e.add_trace(O.Scatter(x=u,y=Ah,name=BF,line=E(color=AE,width=2)),row=1,col=1)
							for(Ni,Nj,Nk)in[(20,KC,'EMA20'),(50,'#FF6D00','EMA50'),(200,'#2979FF','EMA200')]:Nl=Ah.ewm(span=Ni,adjust=J).mean();e.add_trace(O.Scatter(x=u,y=Nl,name=Nk,line=E(color=Nj,width=1.8)),row=1,col=1)
							IJ=M(m[EL].max());IK=M(m[EM].min());e.add_hline(y=IJ,line_dash=GU,line_color=KD,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W High ₹{IJ:,.2f}",annotation_position=KE,annotation_font=E(color=KD,size=13));e.add_hline(y=IK,line_dash=GU,line_color=KF,line_width=1.4,opacity=.85,row=1,col=1,annotation_text=f"52W Low ₹{IK:,.2f}",annotation_position='bottom right',annotation_font=E(color=KF,size=13))
							if Cn:e.add_trace(O.Scatter(x=Cn,y=IG,mode=E9,name='H-M Entry (RSI>50)',marker=E(color='lime',size=12,symbol=KG,line=E(color='white',width=1.5))),row=1,col=1)
							try:IL=m[w].squeeze();Nm=m['Open'].squeeze();Nn=m[BF].squeeze();No=[GS if B>=A else GT for(A,B)in zip(Nm.tolist(),Nn.tolist())];e.add_trace(O.Bar(x=u,y=IL.tolist(),name=w,marker=E(color=No,line=E(width=0)),opacity=.85,showlegend=J),row=3,col=1);Np=IL.rolling(20).mean();e.add_trace(O.Scatter(x=u,y=Np.tolist(),name='Vol Avg(20)',line=E(color='#616161',width=1.2,dash=DH)),row=3,col=1)
							except g:pass
							Dj=Av.reindex(Av.index);IM=H.Series(5e1,index=Av.index);Nq=Dj.where(Dj>=50,5e1);e.add_trace(O.Scatter(x=u,y=IM.tolist(),line=E(width=0),mode=EN,showlegend=J,hoverinfo=EO),row=2,col=1);e.add_trace(O.Scatter(x=u,y=Nq.tolist(),fill=KH,fillcolor='rgba(38,166,154,0.35)',line=E(width=0),mode=EN,showlegend=J,hoverinfo=EO),row=2,col=1);Nr=Dj.where(Dj<=50,5e1);e.add_trace(O.Scatter(x=u,y=IM.tolist(),line=E(width=0),mode=EN,showlegend=J,hoverinfo=EO),row=2,col=1);e.add_trace(O.Scatter(x=u,y=Nr.tolist(),fill=KH,fillcolor='rgba(239,83,80,0.35)',line=E(width=0),mode=EN,showlegend=J,hoverinfo=EO),row=2,col=1);e.add_trace(O.Scatter(x=u,y=Av.tolist(),name='RSI(9)',line=E(color='#1976D2',width=1.5)),row=2,col=1);e.add_trace(O.Scatter(x=u,y=FD.tolist(),name='EMA3',line=E(color='#4CAF50',width=1.5)),row=2,col=1);e.add_trace(O.Scatter(x=u,y=FE.tolist(),name='WMA21',line=E(color='#EF5350',width=1.5)),row=2,col=1)
							if FF:e.add_trace(O.Scatter(x=FF,y=IH,mode=E9,name='Entry (RSI panel)',showlegend=J,marker=E(color='lime',size=6,symbol=KG,line=E(color='white',width=1))),row=2,col=1)
							e.add_hline(y=70,line_dash=DH,line_color=GQ,opacity=.5,row=2,col=1);e.add_hline(y=50,line_dash=GU,line_color='#888888',row=2,col=1,annotation_text='50',annotation_position='right');e.add_hline(y=30,line_dash=DH,line_color=KC,opacity=.8,row=2,col=1,annotation_text='30',annotation_position='right');e.update_layout(template=q,height=950,title=E(text=f"{G} — Ultra HD Chart (Price, EMAs, H-M, Volume)",font=E(size=12,color='#0E1117',family=EP)),margin=E(t=60,b=80,l=20,r=20),xaxis_rangeslider_visible=J,xaxis2_rangeslider_visible=J,xaxis3_rangeslider_visible=J,legend=E(orientation='h',y=-.15,x=.5,xanchor='center',yanchor='top',font=E(size=13,color=KI,family=EP)),hovermode='x unified',font=E(size=13,color=KI,family=EP),hoverlabel=E(font_size=14,font_family=EP,bgcolor='rgba(255,255,255,0.95)'),plot_bgcolor=EQ,paper_bgcolor=EQ,bargap=.15);e.update_xaxes(showspikes=B,spikemode='across+toaxis',spikesnap='cursor',spikethickness=1.5,spikedash='solid',spikecolor='#808495',gridcolor=KJ,linecolor=GV,tickfont=E(size=12,family=KK));e.update_yaxes(gridcolor=KJ,zeroline=J,linecolor=GV,tickfont=E(size=12,family=KK));e.update_yaxes(range=[0,100],row=2,col=1);e.update_yaxes(title_text=BK,title_font=E(size=14,weight=AR),row=1,col=1);e.update_yaxes(title_text='RSI / H-M',title_font=E(size=14,weight=AR),row=2,col=1);e.update_yaxes(title_text=w,title_font=E(size=14,weight=AR),row=3,col=1);Ns={K0:J,'responsive':B,'toImageButtonOptions':{'format':'png','filename':f"{G}_Ultra_HD_Analysis",'height':1080,'width':1920,'scale':6},'modeBarButtonsToAdd':['drawline','drawopenpath','drawrect','eraseshape']};A.plotly_chart(e,use_container_width=B,key=f"price_ema_chart_{G}",config=Ns)
							if Cn:A.caption(f"🟢 {Q(Cn)} H-M entry signal(s) — RSI(9) crossed above 50 (bottom-catch). **H-M panel:** Green fill = RSI above 50 (momentum). Red fill = RSI below 50 (pullback). For informational purposes only.")
							else:A.caption('**H-M panel:** Green fill = RSI above 50. Red fill = RSI below 50 (pullback zone). 🟢 circles = RSI(9) cross above 50 (entry). For informational purposes only.')
							X={}
							if z!=BE:
								Dk=DK(BE)
								if not Dk.empty:
									Nt=[A for A in Dk.columns if not A.startswith(AX)and not A.startswith(AY)];IN=U((A for A in Nt if A.lower()in[D0,AZ,Dx,Dy,D1,Dz]),D)
									if IN:
										IO=Dk[Dk[IN].astype(F).str.strip()==G]
										if not IO.empty:Nu=IO.iloc[0].to_dict();X={A:B for(A,B)in Nu.items()if not F(A).startswith(AX)and not F(A).startswith(AY)and F(A)!=n}
							def Y(row,primary_dict,*K):
								def B(r_data):
									J='n/a';B=r_data
									if B is D or Q(B)==0:return k
									try:H=AL(B.keys())if Ay(B,E)else AL(B.index)
									except g:return k
									H=[A for A in H if not F(A).startswith(AX)and not F(A).startswith(AY)and F(A)!=n]
									for L in K:
										I=L.lower().strip()
										for G in H:
											if F(G).strip().lower()==I:
												A=B.get(G,C);A=C if A is D else F(A).strip()
												if A not in(C,A3,AO,DB,J,k):return A
										for G in H:
											if I in F(G).strip().lower():
												A=B.get(G,C);A=C if A is D else F(A).strip()
												if A not in(C,A3,AO,DB,J,k):return A
									return k
								A=B(primary_dict)
								if A==k:A=B(row)
								return A
							def IP(label,value):return f"<div style='background:var(--secondary-background-color,#F0F2F6);border:1px solid rgba(128,128,128,0.35);border-radius:6px;padding:8px 10px;min-width:150px;flex:1 1 150px;'><div style='font-size:11px;color:var(--text-color,#31333F);opacity:0.65;margin-bottom:3px;'>{label}</div><div style='font-size:14px;font-weight:700;color:var(--text-color,#0E1117);word-break:break-word;'>{value}</div></div>"
							def FK(title,fields):D=C.join(IP(A,Y(S,X,*B))for(A,B)in fields);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
						with Nd:Nv=AL(m.index);B7=O.Figure();B7.add_trace(O.Scatter(x=Nv,y=FC,name=KL,line=E(color='#AB47BC',width=2)));B7.add_hline(y=70,line_dash=DH,line_color=GQ,opacity=.6);B7.add_hline(y=30,line_dash=DH,line_color=GP,opacity=.6);B7.add_hrect(y0=45,y1=65,fillcolor=GP,opacity=.06,line_width=0,annotation_text='Ideal entry 45-65',annotation_position=KE);B7.update_layout(template=q,height=280,yaxis=E(range=[0,100]),margin=E(t=30,b=20),plot_bgcolor=EQ,paper_bgcolor=EQ,font=E(color='#1A1A1A'));B7.update_xaxes(gridcolor=KM);B7.update_yaxes(gridcolor=KM);A.plotly_chart(B7,use_container_width=B,key=f"rsi14_chart_{G}")
				A.markdown("<hr style='margin:16px 0 4px 0;opacity:0.25;'>",unsafe_allow_html=B)
				with A.expander(f"📋 {G} — Google Sheet Data",expanded=B):
					def Nw(title,items):D=C.join(IP(A,B)for(A,B)in items);A.markdown(f"<div style='font-size:13px;font-weight:700;color:#1565C0;margin:14px 0 6px 0;'>{title}</div><div style='display:flex;flex-wrap:wrap;gap:8px;'>{D}</div>",unsafe_allow_html=B)
					Nx='▲'if Dh>=0 else'▼';Ny='#00A152'if Dh>=0 else'#D32F2F';Nw('📊 Price Snapshot',[(KN,f"₹{AK:,.2f} <span style='color:{Ny};font-size:12px;'>{Nx} {Dh:+.2f}%</span>"),(Ak,f"₹{M(m[EL].max()):,.2f}"),(Al,f"₹{M(m[EM].min()):,.2f}"),(KL,f"{Cm:.1f}"if Cm is not D else'–')])
					with A.expander('📋 Company Price Dashboard',expanded=J):FK('🏢 Company Info',[('Company Name',[K7,K8]),(GW,[E7,G4]),(Aj,[KO,KP,E3]),('52W High Date',[Jw,'52 week high date']),('52W Low Date',[Jx,'52 week low date']),(w,[BH]),(D3,[CS])]);FK('📡 Signals & System Output',[(JM,[Jj]),('Difference from 200 DMA',['difference from 200 dma','differance from 200 dma']),('CAR Rating',['cumulative average rule (car) rating','car rating']),('Start GTT Order',[Jk,'gtt order']),(Bp,[G5]),(Bq,[G6]),(Br,[G7]),(Bs,[Jl]),(Bt,[G8])]);FK('💰 Fundamentals',[(Jt,['face value']),('Total Equity Capital',[GX]),(Jv,[G9]),('EPS',['eps']),(Ju,['ronw']),(Jr,[Fy,Fz]),(Js,[KQ,KR]),('Pledged %',[F_,G0]),('D/E Ratio',[Ja,'de ratio']),('Net Sales (Cr)',[E2]),('Net Profit (Cr.)',[E1]),('Reserves (Cr)',[GY]),('Total Debt (Cr)',[GZ]),('Inventory (Cr)',[Ga]),('Cash & Equiv (Cr)',[Gb,Gc,Gd]),('Operating Cash Flow (Cr)',['operating cash flow']),('Trade Receivables (Cr)',[Ge]),('Trade Payables (Cr)',[Gf]),('Fixed Assets/Net PPE (Cr)',[Gg,Gh]),('Total Assets (Cr)',[Gi]),('Open (₹)',['open price','open (','open']),('High (₹)',['day high','high price','high (']),('Low (₹)',['day low','low price','low (']),('Prev Close (₹)',['prev close','previous close',Jz]),('Price Change (₹)',['price change','change (','change in price']),('% Change',['% change',D2,'change %']),('Shares Outstanding (Cr)',['shares outstanding']),('Book Value (₹/share)',['book value']),('Public %',['public %','public holding']),('FII %',['fii %','fii holding','fii']),('DII %',['dii %','dii holding','dii'])])
					def d(raw):
						if raw in(D,k,C,A3,AO):return
						try:return M(F(raw).replace(AB,C).replace('₹',C).strip())
						except(AV,Fr):return
					def A0(h,alpha=.35):return f"rgba({T(h[1:3],16)},{T(h[3:5],16)},{T(h[5:7],16)},{alpha})"
					if Ba and AK is not D:IQ=AK-Ba;IR=O.Figure(O.Waterfall(orientation='v',measure=['absolute','relative','total'],x=['Prev Close','Change',KN],y=[Ba,IQ,AK],text=[f"₹{Ba:,.2f}",f"{IQ:+.2f}",f"₹{AK:,.2f}"],textposition='outside',textfont=E(color=Ao,size=13),increasing=E(marker=E(color=x)),decreasing=E(marker=E(color=AP)),totals=E(marker=E(color=AE)),connector=E(line=E(color=GV))));IR.update_layout(title=f"📈 Price Change Bridge — {G} ({Dh:+.2f}%)",template=q,height=300,showlegend=J,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IR,use_container_width=B,key=f"waterfall_price_{G}");A.caption("Prev Close → today's Price Change → Last Close. Shown as a Waterfall, not a Sankey, since a price drop can't be a negative flow.")
					else:A.info("Prev Close / Last Close not available for this stock, so the Price Change bridge can't be built.")
					Nz=Y(S,X,BH);Ai=d(Y(S,X,KO,KP,E3));C5=d(Nz)
					if C5 is not D and Ai is not D and 0<=Ai<=100:FL=C5*Ai/100;IS=C5-FL;IT=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Volume<br>{C5:,.0f} shares",f"Delivered<br>{FL:,.0f} shares ({Ai:.1f}%)",f"Intraday / Non-Delivery<br>{IS:,.0f} shares ({100-Ai:.1f}%)"],color=[Cc,x,A_]),link=E(source=[0,0],target=[1,2],value=[FL,IS],color=[A0(x),A0(A_)])));IT.update_layout(title=f"📦 Volume → Delivery Split — {G}",template=q,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IT,use_container_width=B,key=f"sankey_volume_{G}");A.caption('Total Volume split by % Delivery into shares actually delivered (genuine buying/holding) vs. shares traded intraday and squared off same day.')
					else:A.info("Volume / % Delivery not available for this stock, so the Volume → Delivery split can't be built.")
					if Cm is not D:IU=O.Figure(O.Indicator(mode=KS,value=M(Cm),number=E(font=E(color=Ao,size=28)),title=E(text=f"RSI(14) — {G}",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AE),steps=[E(range=[0,30],color=J_),E(range=[30,70],color='#f5f5f5'),E(range=[70,100],color=Bm)],threshold=E(line=E(color=DI,width=3),value=M(Cm)))));IU.update_layout(template=q,height=260,margin=E(t=50,b=10,l=30,r=30));A.plotly_chart(IU,use_container_width=B,key=f"gauge_rsi_{G}");A.caption("Below 30 = oversold, above 70 = overbought. A gauge, not a Sankey — RSI doesn't split into parts.")
					else:A.info('RSI(14) not available for this stock.')
					Dl=M(m[EL].max())if not m.empty else D;Co=M(m[EM].min())if not m.empty else D
					if Dl and Co is not D and Dl>Co and AK is not D:IV=AA(i,min(1e2,(AK-Co)/(Dl-Co)*100));IW=O.Figure(O.Indicator(mode=KS,value=IV,number=E(suffix=AC,font=E(color=Ao,size=28)),title=E(text=f"52W Range Position — {G}<br><span style='font-size:11px'>Low ₹{Co:,.2f} · Last ₹{AK:,.2f} · High ₹{Dl:,.2f}</span>",font=E(size=14)),gauge=E(axis=E(range=[0,100]),bar=E(color=AE),steps=[E(range=[0,33],color=Bm),E(range=[33,66],color=GB),E(range=[66,100],color=CW)],threshold=E(line=E(color=DI,width=3),value=IV))));IW.update_layout(template=q,height=280,margin=E(t=65,b=10,l=30,r=30));A.plotly_chart(IW,use_container_width=B,key=f"gauge_52wrange_{G}");A.caption("0% = at the 52-week low, 100% = at the 52-week high. A gauge, not a Sankey — price levels aren't a splittable quantity.")
					else:A.info('52-week High/Low/Last Close not available for this stock.')
					C6=d(Y(S,X,CS));FM=J
					if C6 is D and C5 is not D and AK:C6=C5*AK/1e7;FM=B
					if C6 is not D and Ai is not D and 0<=Ai<=100:FN=C6*Ai/100;IX=C6-FN;IY=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"{"Est. "if FM else C}Turnover<br>₹{C6:,.2f} Cr",f"Delivered Value<br>₹{FN:,.2f} Cr ({Ai:.1f}%)",f"Intraday Value<br>₹{IX:,.2f} Cr ({100-Ai:.1f}%)"],color=[Cc,x,A_]),link=E(source=[0,0],target=[1,2],value=[FN,IX],color=[A0(x),A0(A_)])));IY.update_layout(title=f"💵 Turnover → Delivery Split — {G}",template=q,height=300,margin=E(t=45,b=10,l=10,r=10));A.plotly_chart(IY,use_container_width=B,key=f"sankey_turnover_{G}");N_=" Your sheet's Turnover field is blank for this stock, so this uses an estimate (Volume × Last Close) — the same fallback this app already uses elsewhere."if FM else C;A.caption(f"Turnover split by % Delivery, mirroring the Volume split above in ₹ terms.{N_}")
					else:A.info("Turnover / % Delivery / Volume not available for this stock, so the Turnover → Delivery split can't be built.")
					C7=d(Y(S,X,G9));C8=d(Y(S,X,Fy,Fz));C9=d(Y(S,X,KQ,KR));FO=d(Y(S,X,F_,G0))
					if C7 is not D and C7>0 and(C8 is not D or C9 is not D):
						C8=C8 or i;C9=C9 or i;IZ=AA(i,1e2-C8-C9);Cp=C7*C8/100;Ia=C7*C9/100;Ib=C7*IZ/100;Ic=[f"Market Cap<br>₹{C7:,.2f} Cr",f"Promoters<br>₹{Cp:,.2f} Cr ({C8:.1f}%)",f"Institutional<br>₹{Ia:,.2f} Cr ({C9:.1f}%)",f"Public / Other<br>₹{Ib:,.2f} Cr ({IZ:.1f}%)"];Id=[Cc,AE,x,ER];Ie=[0,0,0];If=[1,2,3];Ig=[Cp,Ia,Ib];Ih=[A0(A)for A in[AE,x,ER]];Ii=C
						if FO is not D and Cp>0:FP=Cp*FO/100;Ij=Cp-FP;Ic+=[f"Pledged (of Promoters)<br>₹{FP:,.2f} Cr ({FO:.1f}%)",f"Free / Unpledged<br>₹{Ij:,.2f} Cr"];Id+=[DI,Cy];Ie+=[1,1];If+=[4,5];Ig+=[FP,Ij];Ih+=[A0(DI),A0(Cy)];Ii=" Promoters' holding is further split into Pledged vs Free based on Pledged %."
						Ik=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=Ic,color=Id),link=E(source=Ie,target=If,value=Ig,color=Ih)));Ik.update_layout(title=f"🧾 Shareholding Pattern — Who Owns {G}",template=q,height=380,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Ik,use_container_width=B,key=f"sankey_shareholding_{G}");A.caption(f'Market Cap × holding % from the Fundamentals data above. "Public / Other" absorbs whatever isn\'t reported as Promoters/Institutional (Public %, FII %, DII % show "-" for stocks where your sheet doesn\'t break those out separately).{Ii}')
					else:A.info("Market Cap / shareholding % data not available for this stock, so the Shareholding Pattern flow can't be built.")
					Bb=d(Y(S,X,E2));B8=d(Y(S,X,E1))
					if Bb is not D and B8 is not D and 0<B8<Bb:Il=Bb-B8;FQ=B8/Bb*100;Im=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Net Sales<br>₹{Bb:,.2f} Cr (100%)",f"Net Profit<br>₹{B8:,.2f} Cr ({FQ:.1f}%)",f"Total Expenses<br>₹{Il:,.2f} Cr ({100-FQ:.1f}%)"],color=[AE,x,AP]),link=E(source=[0,0],target=[1,2],value=[B8,Il],color=['rgba(15,157,88,0.35)','rgba(234,67,53,0.35)'])));Im.update_layout(title=f"💰 Revenue & Expenses Flow — {G} (Net Margin {FQ:.1f}%)",template=q,height=320,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Im,use_container_width=B,key=f"sankey_{G}");A.caption('Based on Net Sales / Net Profit from the Fundamentals data above. "Total Expenses" is the remainder (Net Sales − Net Profit) — your sheet doesn\'t carry a Cost-of-Revenue/Opex breakdown, so a multi-stage flow (Gross → Operating → Net) isn\'t available for this stock.')
					elif Bb is not D and B8 is not D:A.info(f"Revenue & Expenses flow needs a normal profitable split (0 < Net Profit < Net Sales). {G} currently shows Net Sales ₹{Bb:,.2f} Cr and Net Profit ₹{B8:,.2f} Cr, which doesn't fit a simple flow diagram (e.g. a net loss).")
					else:A.info("Net Sales / Net Profit not available for this stock, so the Revenue & Expenses flow can't be built.")
					O0=d(Y(S,X,GX));O1=d(Y(S,X,GY));O2=d(Y(S,X,GZ));O3=d(Y(S,X,Gf));O4=[(KT,O0,AE),(KU,O1,x),(KV,O2,AP),(KW,O3,KX)];B9=[(B,A,C)for(B,A,C)in O4 if A is not D and A>0]
					if Q(B9)>=2:In=sum(B for(A,B,A)in B9);Io=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Total Financing<br>₹{In:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/In*100:.1f}%)"for(B,A,C)in B9],color=[KY]+[B for(A,A,B)in B9]),link=E(source=[0]*Q(B9),target=AL(Dt(1,Q(B9)+1)),value=[B for(A,B,A)in B9],color=[A0(B)for(A,A,B)in B9])));Io.update_layout(title=f"🏗️ Capital Structure — How {G} Is Financed",template=q,height=300,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Io,use_container_width=B,key=f"sankey_capstruct_{G}");A.caption('Equity Capital + Reserves + Total Debt + Trade Payables, from the Fundamentals data above.')
					else:A.info('Not enough of Total Equity Capital / Reserves / Total Debt / Trade Payables available to build a Capital Structure flow.')
					CA=d(Y(S,X,Gi));O5=[(KZ,d(Y(S,X,Gg,Gh)),Ka),(Kb,d(Y(S,X,Ga)),A_),(Kc,d(Y(S,X,Ge)),Kd),(Ke,d(Y(S,X,Gb,Gc,Gd)),AE)];FR=[(B,A,C)for(B,A,C)in O5 if A is not D and A>=0]
					if CA is not D and CA>0 and FR:
						Ip=sum(B for(A,B,A)in FR);FS=CA-Ip
						if FS>=0:CB=FR+([(Kf,FS,ER)]if FS>0 else[]);Iq=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=30,thickness=18,line=E(color=Bw,width=.5),label=[f"Total Assets<br>₹{CA:,.2f} Cr (100%)"]+[f"{B}<br>₹{A:,.2f} Cr ({A/CA*100:.1f}%)"for(B,A,C)in CB],color=[Cc]+[B for(A,A,B)in CB]),link=E(source=[0]*Q(CB),target=AL(Dt(1,Q(CB)+1)),value=[B for(A,B,A)in CB],color=[A0(B)for(A,A,B)in CB])));Iq.update_layout(title=f"📦 Asset Deployment — Where {G}'s Assets Sit",template=q,height=340,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(Iq,use_container_width=B,key=f"sankey_assets_{G}");A.caption('Fixed Assets, Inventory, Trade Receivables and Cash & Equivalents from the Fundamentals data above. "Other Assets" is the gap versus reported Total Assets (e.g. intangibles, investments, or other items your sheet doesn\'t itemize).')
						else:A.info(f"{G}'s itemized asset categories (₹{Ip:,.2f} Cr) add up to more than the reported Total Assets (₹{CA:,.2f} Cr) — likely a data mismatch between sheet rows, so the Asset Deployment flow isn't shown to avoid a misleading chart.")
					else:A.info("Total Assets / asset-category data not available for this stock, so the Asset Deployment flow can't be built.")
					FT,Ir,Dm=[],[],[];CC,CD,CE,CF=[],[],[],[]
					def Bc(label,color,col_x):FT.append(label);Ir.append(color);Dm.append(col_x);return Q(FT)-1
					O6,O7,Is,FU=.001,.24,.5,.999;O8=[(KT,d(Y(S,X,GX)),AE),(KU,d(Y(S,X,GY)),x),(KV,d(Y(S,X,GZ)),AP),(KW,d(Y(S,X,Gf)),KX)];FV=[(B,A,C)for(B,A,C)in O8 if A is not D and A>0];It=Q(FV)>=2;BA=D
					if It:
						Dn=sum(B for(A,B,A)in FV);BA=Bc(f"Total Financing<br>₹{Dn:,.2f} Cr (100%)",KY,O7)
						for(Aw,AG,Cq)in FV:u=Bc(f"{Aw}<br>₹{AG:,.2f} Cr ({AG/Dn*100:.1f}%)",Cq,O6);CC.append(u);CD.append(BA);CE.append(AG);CF.append(A0(Cq))
					Bd=d(Y(S,X,Gi));O9=[(KZ,d(Y(S,X,Gg,Gh)),Ka),(Kb,d(Y(S,X,Ga)),A_),(Kc,d(Y(S,X,Ge)),Kd),(Ke,d(Y(S,X,Gb,Gc,Gd)),AE)];FW=[(B,A,C)for(B,A,C)in O9 if A is not D and A>=0];Do=Bd is not D and Bd>0 and bool(FW)
					if Do:OA=sum(B for(A,B,A)in FW);FX=Bd-OA;Do=FX>=0
					if Do:
						OB=FW+([(Kf,FX,ER)]if FX>0 else[]);OC=f" ({Bd/Dn*100:.1f}%)"if BA is not D else Kg;Iu=Bc(f"Total Assets<br>₹{Bd:,.2f} Cr{OC}",Cc,Is)
						if BA is not D:CC.append(BA);CD.append(Iu);CE.append(Bd);CF.append(A0(Cc))
						for(Aw,AG,Cq)in OB:u=Bc(f"{Aw}<br>₹{AG:,.2f} Cr ({AG/Bd*100:.1f}%)",Cq,FU);CC.append(Iu);CD.append(u);CE.append(AG);CF.append(A0(Cq))
					Be=d(Y(S,X,E2));CG=d(Y(S,X,E1));Iv=Be is not D and CG is not D and 0<CG<Be
					if Iv:
						Iw=Be-CG;OD=f" ({Be/Dn*100:.1f}%)"if BA is not D else Kg;FY=Bc(f"Net Sales<br>₹{Be:,.2f} Cr{OD}",AE,Is)
						if BA is not D:CC.append(BA);CD.append(FY);CE.append(Be);CF.append(A0(AE))
						Ix=CG/Be*100;OE=Bc(f"Net Profit<br>₹{CG:,.2f} Cr ({Ix:.1f}%)",x,FU);OF=Bc(f"Total Expenses<br>₹{Iw:,.2f} Cr ({100-Ix:.1f}%)",AP,FU);CC+=[FY,FY];CD+=[OE,OF];CE+=[CG,Iw];CF+=[A0(x),A0(AP)]
					OG=sum([It,Do,Iv])
					if OG>0:
						from collections import defaultdict as Iy;Iz=Iy(T)
						for Cr in Dm:Iz[Cr]+=1
						I_=Iy(T);J0=[]
						for Cr in Dm:Aw=Iz[Cr];BO=I_[Cr];I_[Cr]+=1;J0.append(b((BO+.5)/Aw,4)if Aw>1 else .5)
						J1=O.Figure(O.Sankey(arrangement=Bu,textfont=E(color=Ao,size=13,family=Bv),node=E(pad=22,thickness=18,line=E(color=Bw,width=.5),label=FT,color=Ir,x=Dm,y=J0),link=E(source=CC,target=CD,value=CE,color=CF)));J1.update_layout(title=f"💎 Combined Money Flow — {G} (Financing → Assets / Revenue, merged)",template=q,height=560,margin=E(t=45,b=10,l=10,r=10),font=E(size=12));A.plotly_chart(J1,use_container_width=B,key=f"sankey_merged_{G}");A.caption("All money-related flows merged into one chart: financing sources (Equity + Reserves + Debt + Trade Payables) feed Total Financing, which splits into two parallel paths — Total Assets (incl. Trade Receivables) and Net Sales → Net Profit / Total Expenses. It's drawn as two branches off one hub, rather than one long chain, because Total Assets and Net Sales are different kinds of totals (balance sheet vs. P&L) that don't feed into each other. Trade Payables now also appears in the 🏗️ Capital Structure chart above.")
					else:A.info('Not enough financing / assets / revenue data available for this stock to build the Combined Money Flow chart.')
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
	@DJ
	def OH():
		y='0.00%';x='Worst -> Best';v='1 Day';e='RANK';d='📊 BF Grade';b='🔬 BF Score';a='CURRENT PRICE';W='STOCK NAME';A.markdown(c);A.markdown('### 📈 Multi-Horizon Performance Summary Matrix');z,AP=A.columns([4,1])
		with z:f=A.radio(GD,[GE,CY,CZ],horizontal=B,help=Kh,key='perf_matrix_sizing_mode')
		g=[v,'2 Day','3 Day','5 Day','7 Day','10 Day','12 Day','15 Days','20 Days','25 Days',Gj,'2 Months','3 Months','4 Months','5 Months','6 Months','7 Months','8 Months','9 Months','10 Months','11 Months',Gk,'18 Months','1.5 Years','2 Years','2.5 Years','3 Years',w];A0,A1,A2=A.columns([2,2,3])
		with A0:h=A.selectbox('🎯 Base Horizon for Performance Ranking:',g,index=0)
		with A1:A4=A.radio('排序 Sorting Order Type:',['Best -> Worst',x],index=0,horizontal=B)
		with A2:j=A.text_input('🔍 Filter stocks inside this matrix...',placeholder=K6,key=Je)
		V={}
		for L in g:
			if L==w:
				if B_:V[L]=B_
				continue
			l=[L.lower(),L.lower().replace(' ',C),L.lower().replace('s',C)]
			if L==v:l.append(D2)
			for X in R:
				if AW(A in X.lower()for A in l)and AC in X.lower():V[L]=X;break
		if V:
			m=[]
			for(AR,N)in K.iterrows():
				o=F(N.get(n,C)).strip();A5=N.get(A7,C)if A7 else C;A6=f"https://charting.nseindia.com/?symbol={o}-EQ";A8=f'<a href="{A6}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{o}</a>';G={W:A8,a:A5}
				for(L,A9)in V.items():
					p=F(N.get(A9,'0')).replace(AC,C).replace(AB,C).strip()
					try:G[L]=M(p)if p not in[C,A3,AO]else i
					except AV:G[L]=i
				if BQ:
					q=F(N.get(BQ,'0')).replace(AC,C).replace(AB,C).strip()
					try:G[Aj]=M(q)if q not in[C,A3,AO]else i
					except AV:G[Aj]=i
				if BR:
					r=F(N.get(BR,C)).replace(AC,C).replace(AB,C).strip()
					try:G[BL]=M(r)if r not in[C,A3,AO]else D
					except AV:G[BL]=D
				if BU:
					s=F(N.get(BU,C)).replace(AC,C).replace(AB,C).strip()
					try:G[B1]=M(s)if s not in[C,A3,AO]else D
					except AV:G[B1]=D
				if B4:
					t=F(N.get(B4,C)).replace(AB,C).strip()
					try:G[Ak]=M(t)if t not in[C,A3,AO]else D
					except AV:G[Ak]=D
				if B5:
					u=F(N.get(B5,C)).replace(AB,C).strip()
					try:G[Al]=M(u)if u not in[C,A3,AO]else D
					except AV:G[Al]=D
				if Cg:G[Bp]=F(N.get(Cg,C)).strip()
				if BS:G[Bq]=F(N.get(BS,C)).strip()
				if DS:G[Br]=F(N.get(DS,C)).strip()
				if DT:G[Bs]=F(N.get(DT,C)).strip()
				if BT:G[Bt]=F(N.get(BT,C)).strip()
				AD={A:B for(A,B)in N.items()if not F(A).startswith(Bo)};AE,AF,_=DM(AD,R);G[b]=AE;G[d]=AF;m.append(G)
			P=H.DataFrame(m)
			if j:P=P[P[W].str.replace(Dw,C,regex=B).str.contains(j,case=J,na=J)]
			AG=h if h in P.columns else P.columns[2];AH=A4==x;P=P.sort_values(by=AG,ascending=AH).reset_index(drop=B);P.insert(0,e,P.index+1);E=P.copy()
			for L in V.keys():
				if L in E.columns:
					if L==w:E[L]=E[L].apply(lambda x:f"{T(x):,}"if H.notnull(x)else k)
					else:E[L]=E[L].apply(lambda x:f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)
			if Aj in E.columns:E[Aj]=E[Aj].apply(lambda x:f"{x:.2f}%"if H.notnull(x)else k)
			if BL in E.columns:E[BL]=E[BL].apply(lambda x:f"{x:.2f}"if H.notnull(x)else k)
			if B1 in E.columns:E[B1]=E[B1].apply(lambda x:(f"+{x:.2f}%"if x>0 else f"{x:.2f}%"if x<0 else y)if H.notnull(x)else k)
			if Ak in E.columns:E[Ak]=E[Ak].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else k)
			if Al in E.columns:E[Al]=E[Al].apply(lambda x:f"{x:,.2f}"if H.notnull(x)else k)
			O=EW.from_dataframe(E);O.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);O.configure_column(e,width=70,pinned=DD);O.configure_column(W,width=140,pinned=DD,cellRenderer=DX);AI=B2('\n            function(params) {\n                if (params.value === undefined || params.value === null || params.colDef.field === "Volume") return null;\n                let val = parseFloat(String(params.value).replace(/[+%,]/g, \'\'));\n                if (val > 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#e6f4ea\', \'fontWeight\': \'bold\' };\n                if (val < 0) return { \'color\': \'#000000\', \'backgroundColor\': \'#fce8e6\', \'fontWeight\': \'bold\' };\n                return null;\n            }\n            ');AJ=B2(Ki);AK=B2("\n            function(params) {\n                let v = String(params.value);\n                if (v.includes('STRONG BUY')) return { 'backgroundColor': '#16e37f44', 'fontWeight': 'bold' };\n                if (v.includes('WATCHLIST')) return { 'backgroundColor': '#f4b40044', 'fontWeight': 'bold' };\n                if (v.includes('CAUTION')) return { 'backgroundColor': '#ff990044' };\n                return { 'backgroundColor': '#ea433544' };\n            }\n            ");AL=B2(Kj)
			for I in E.columns:
				if I in(e,):continue
				if f==CY and Q(E)>0:Y=By(E.iloc[0][I]);Z=Q(F(I));S=T(AA(Y,Z)*7+22)
				elif f==CZ and Q(E)>1:Y=By(E.iloc[1][I]);Z=Q(F(I));S=T(AA(Y,Z)*7+22)
				else:AM={W:140,a:130,Aj:110,b:110,d:160,BL:100,B1:140,Ak:110,Al:110,Bp:120,Bq:130,Br:130,Bs:130,Bt:130};S=AM.get(I,130)
				U=AA(70,min(S,90))
				if I==W:O.configure_column(I,width=S,minWidth=U,pinned=DD,cellRenderer=DX)
				elif I==a:O.configure_column(I,width=S,minWidth=U)
				elif I==b:O.configure_column(I,width=S,minWidth=U,cellStyle=AJ)
				elif I==d:O.configure_column(I,width=S,minWidth=U,cellStyle=AK)
				elif I in(Bp,Bq,Br,Bs,Bt):O.configure_column(I,width=S,minWidth=U,cellStyle=AL)
				elif I in V or I==B1:O.configure_column(I,width=S,minWidth=U,cellStyle=AI)
				else:O.configure_column(I,width=S,minWidth=U)
			O.configure_grid_options(domLayout=AQ,rowHeight=38,headerHeight=45,enableCellTextSelection=B,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AN=O.build();EV(E,gridOptions=AN,theme=GF,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=450,width=GG,key='horizon_perf_grid')
	OH()
	@DJ
	def OI():
		m='Key Reasons';l='Score (High→Low)';W='Score';A.markdown(c);A.markdown('### 🔬 Bottom Fishing Scanner — Buy from Bottom Candidates');A.caption('Stocks that are 8–15% above 52W Low, in uptrend, with high volume + strong fundamentals');o,AI=A.columns([4,1])
		with o:a=A.radio(GD,[GE,CY,CZ],horizontal=B,help=Kh,key='bf_scanner_sizing_mode')
		p,q,r=A.columns([2,2,2])
		with p:X=A.slider('Minimum BF Score:',min_value=0,max_value=100,value=55,step=5,key='bf_min_score')
		with q:s=A.radio('Sort by:',[l,'Score (Low→High)'],horizontal=B,key='bf_sort')
		with r:b=A.text_input(K5,placeholder='e.g. WIPRO',key=Jf)
		L=[]
		for(AJ,d)in K.iterrows():
			E={A:B for(A,B)in d.items()if not F(A).startswith(Bo)};e,t,u=DM(E,R)
			if e>=X:
				f=F(d.get(n,C)).strip();v=E.get(A7,C)if A7 else C;g=U((A for A in R if E7 in A.lower()),D);w=E.get(g,C)if g else C;x=f"https://charting.nseindia.com/?symbol={f}-EQ";y=f'<a href="{x}" target="_blank" style="text-decoration:none; color:#000000; font-weight:bold;">{f}</a>';P=D
				if BQ:
					h=F(E.get(BQ,C)).replace(AC,C).replace(AB,C).strip()
					try:P=M(h)if h not in[C,A3,AO]else D
					except AV:P=D
				z=F(E.get(BR,C)).strip()if BR else k;A0=F(E.get(BU,C)).strip()if BU else k;A1=F(E.get(B4,C)).strip()if B4 else k;A2=F(E.get(B5,C)).strip()if B5 else k;A4=F(E.get(Cg,C)).strip()if Cg else k;A5=F(E.get(BS,C)).strip()if BS else k;A6=F(E.get(DS,C)).strip()if DS else k;A8=F(E.get(DT,C)).strip()if DT else k;A9=F(E.get(BT,C)).strip()if BT else k;L.append({j:y,W:e,GM:t,AM:v,BL:z,Aj:f"{P:.2f}%"if P is not D else k,B1:A0,Ak:A1,Al:A2,Bp:A4,Bq:A5,Br:A6,Bs:A8,Bt:A9,GW:F(w)[:30],m:' | '.join(u[:3])})
		if b:L=[A for A in L if b.upper()in re.sub(Dw,C,A[j]).upper()]
		L.sort(key=lambda x:x[W],reverse=s==l)
		if L:
			A.success(f"✅ Found **{Q(L)}** stocks matching your bottom-fishing criteria (score ≥ {X})");I=H.DataFrame(L);N=EW.from_dataframe(I);N.configure_default_column(filter=B,sortable=B,resizable=B,floatingFilter=J,flex=0);AD=B2(Ki);AE=B2(Kj);AF={j:120,W:90,GM:160,AM:100,Aj:110,GW:200,m:400,BL:100,B1:140,Ak:110,Al:110,Bp:120,Bq:130,Br:130,Bs:130,Bt:130}
			for G in I.columns:
				if a==CY and Q(I)>0:Y=By(I.iloc[0][G]);Z=Q(F(G));O=T(AA(Y,Z)*7+22)
				elif a==CZ and Q(I)>1:Y=By(I.iloc[1][G]);Z=Q(F(G));O=T(AA(Y,Z)*7+22)
				else:O=AF.get(G,120)
				S=DD if G==j else D;V=AA(70,min(O,90))
				if G==W:N.configure_column(G,width=O,minWidth=V,pinned=S,cellStyle=AD)
				elif G==j:N.configure_column(G,width=O,minWidth=V,pinned=S,cellRenderer=DX)
				elif G in(Bp,Bq,Br,Bs,Bt):N.configure_column(G,width=O,minWidth=V,pinned=S,cellStyle=AE)
				else:N.configure_column(G,width=O,minWidth=V,pinned=S)
			N.configure_grid_options(domLayout=AQ,rowHeight=40,headerHeight=45,alwaysShowHorizontalScroll=B,suppressColumnVirtualisation=B);AG=N.build();EV(I,gridOptions=AG,theme=GF,allow_unsafe_jscode=B,fit_columns_on_grid_load=J,height=400,width=GG,key='bf_scanner_grid');i=io.BytesIO()
			with H.ExcelWriter(i,engine=D9)as AH:Gw(I).to_excel(AH,index=J,sheet_name='Bottom Fishing')
			A.download_button('📥 Download BF Scanner Results',data=i.getvalue(),file_name=f"BottomFishing_{H.Timestamp.now().strftime(Bk)}.xlsx",mime=Bl)
		else:A.info(f"No stocks found with BF Score ≥ {X}. Try lowering the minimum score.")
	OI()
	if AJ:
		A.markdown(c);A.markdown('### 🏆 Top 10 & Bottom 10 Performers (Daily badges)');CH=K.copy();CH[AJ]=H.to_numeric(CH[AJ].astype(F).str.replace(BG,C,regex=B),errors=AN);CH=CH.dropna(subset=[AJ]);OJ=CH.nlargest(10,AJ);OK=CH.nsmallest(10,AJ);Ar,As=A.columns(2)
		with Ar:
			J2="<h4 style='margin-top:0px; margin-bottom:8px;'>⬆️ Top 10 (Daily)</h4>"
			for(_,Bf)in OJ.iterrows():
				Cs=F(Bf.get(n,C)).strip();AG=Bf[AJ];Ct=Bf.get(A7,C)if A7 else C
				try:Bg=M(F(Ct).replace(AB,C).strip());FZ=M(AG);Fa=Bg/(1+FZ/100);Fb=Bg-Fa;Cu=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>+{Fb:,.2f}</span>";Cv=f"₹{Bg:,.2f}"
				except:Cv=f"₹{Ct}";Cu=C
				Fc=f"https://charting.nseindia.com/?symbol={Cs}-EQ";J2+=f"<a href='{Fc}' target='_blank' style='text-decoration:none;'><div style='background-color:#16e37f; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cs}: +{AG}%</span><span>{Cu}{Cv}</span></div></a>"
			A.markdown(J2,unsafe_allow_html=B)
		with As:
			J3="<h4 style='margin-top:0px; margin-bottom:8px;'>⬇️ Bottom 10 (Daily)</h4>"
			for(_,Bf)in OK.iterrows():
				Cs=F(Bf.get(n,C)).strip();AG=Bf[AJ];Ct=Bf.get(A7,C)if A7 else C
				try:Bg=M(F(Ct).replace(AB,C).strip());FZ=M(AG);Fa=Bg/(1+FZ/100);Fb=Bg-Fa;Cu=f"<span style='font-size: 0.85em; opacity: 0.75; margin-right: 6px;'>{Fb:,.2f}</span>";Cv=f"₹{Bg:,.2f}"
				except:Cv=f"₹{Ct}";Cu=C
				Fc=f"https://charting.nseindia.com/?symbol={Cs}-EQ";J3+=f"<a href='{Fc}' target='_blank' style='text-decoration:none;'><div style='background-color:#f39991; padding:6px 12px; margin-bottom:4px; border-radius:5px; color:#000000; font-weight:bold; display:flex; justify-content:space-between;'><span>{Cs}: {AG}%</span><span>{Cu}{Cv}</span></div></a>"
			A.markdown(J3,unsafe_allow_html=B)
	A.markdown(c);A.markdown('### 📰 Global Market News, Alerts & Corporate Announcements');import urllib.request,urllib.parse,xml.etree.ElementTree as C4,pandas as H
	def Dp(pubdate_str):
		try:
			D=H.to_datetime(pubdate_str,utc=B);G=H.Timestamp.now(tz=BM);A=(G-D).total_seconds()
			if A<0:return AH
			if A<60:return f"{T(A)} secs ago"
			if A<3600:E=T(A/60);return f"{E} min{"s"if E!=1 else C} ago"
			if A<86400:F=T(A/3600);return f"{F} hour{"s"if F!=1 else C} ago"
			if A<172800:return f"Yesterday ({D.strftime(EE)})"
			I=T(A/86400);return f"{I} days ago ({D.strftime(EE)})"
		except g:return GN
	@A.cache_data(ttl=600)
	def OL(symbol,limit=10):
		try:
			J=f'"{symbol}" NSE AND ("52 week high" OR "52 week low" OR "upper circuit" OR "lower circuit")';K=urllib.parse.quote(J);M=f"https://news.google.com/rss/search?q={K}&hl=en-IN&gl=IN&ceid=IN:en";N=urllib.request.Request(M,headers={Ca:Cb})
			with urllib.request.urlopen(N)as O:P=O.read()
			Q=C4.fromstring(P);R=[D7,EF,CU,EG,EH,EI,EJ,EK];E=[]
			for A in Q.findall(DG):
				F=A.find(A5).text
				if not AW(A in F.lower()for A in R):continue
				S=A.find(f).text;I=A.find(An).text if A.find(An)is not D else C
				try:G=H.to_datetime(I,utc=B)
				except g:G=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				T=H.Timestamp.now(tz=BM);U=(T-G).total_seconds()/86400
				if U<=15.:V=Dp(I);E.append({AD:f"🚨 **[ALERT]** {F}",f:S,L:V,AI:G,Kk:F})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OM(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={Ca:Cb})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C4.fromstring(O);E=[];Q=[D7,EF,CU,EG,EH,EI,EJ,EK,Kl,Km]
			for A in P.findall(DG):
				G=A.find(A5).text;R=A.find(f).text;I=A.find(An).text if A.find(An)is not D else C;S=AW(A in G.lower()for A in Q);T=GO if S else C;U=f"{T}{G}"
				try:F=H.to_datetime(I,utc=B)
				except g:F=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				V=H.Timestamp.now(tz=BM);W=(V-F).total_seconds()/86400
				if W<=Am:X=Dp(I);E.append({AD:U,f:R,L:X,AI:F})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def ON(symbol,limit=5):
		try:
			J=urllib.parse.quote(f'"{symbol}" stock share news NSE India');K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={Ca:Cb})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C4.fromstring(O);E=[];Q=[D7,EF,CU,EG,EH,EI,EJ,EK,Kl,Km]
			for A in P.findall(DG):
				F=A.find(A5).text;R=A.find(f).text;G=A.find(An).text if A.find(An)is not D else C;S=AW(A in F.lower()for A in Q);T=GO if S else C;U=f"{T}{F}"
				try:I=H.to_datetime(G,utc=B)
				except g:I=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				V=Dp(G);E.append({AD:U,f:R,L:V,AI:I})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	@A.cache_data(ttl=600)
	def OO(symbol,limit=6):
		try:
			I=f'"{symbol}" AND ("Regulation 30" OR "LODR" OR "Board Meeting" OR "AGM" OR "Analyst Meet" OR "Financial Results" OR "Corporate Action" OR "Dividend")';J=urllib.parse.quote(I);K=f"https://news.google.com/rss/search?q={J}&hl=en-IN&gl=IN&ceid=IN:en";M=urllib.request.Request(K,headers={Ca:Cb})
			with urllib.request.urlopen(M)as N:O=N.read()
			P=C4.fromstring(O);E=[]
			for A in P.findall(DG):
				Q=A.find(A5).text;R=A.find(f).text;F=A.find(An).text if A.find(An)is not D else C
				try:G=H.to_datetime(F,utc=B)
				except g:G=H.Timestamp.now(tz=BM)-H.Timedelta(days=100)
				S=Dp(F);E.append({AD:f"📢 {Q}",f:R,L:S,AI:G})
			E.sort(key=lambda x:x[AI],reverse=B);return E[:limit]
		except g:return[]
	OP={'RELIANCE':'500325','TCS':'532540','HDFCBANK':'500180','INFY':Kq,'ICICIBANK':'532174','HINDUNILVR':'500696','SBIN':'500112','BHARTIARTL':'532454','BAJFINANCE':'500034','KOTAKBANK':'500247','LT':'500510','HCLTECH':'532281','AXISBANK':'532215','ASIANPAINT':'500820','MARUTI':'532500',Kn:Kr,'TITAN':'500114','ULTRACEMCO':'532538','ONGC':'500312','NTPC':'532555','POWERGRID':'532898','WIPRO':'507685','NESTLEIND':'500790','JSWSTEEL':'500228','TATASTEEL':'500470','TATAMOTORS':'500570','TECHM':'532755','GRASIM':'500300','ADANIENT':'512599','ADANIPORTS':'532921','COALINDIA':'533278','DIVISLAB':Ks,'DRREDDY':'500124','EICHERMOT':'505200','BAJAJFINSV':'532978','BAJAJ-AUTO':'532977','CIPLA':'500087','BRITANNIA':'500825','HEROMOTOCO':'500182',Ko:Kt,'HINDALCO':'500440','UPL':'512070','TATACONSUM':'500800','SBILIFE':'540719','HDFCLIFE':'540777','INDUSINDBK':'532187','BPCL':'500547','IOC':'530965','M&M':'500520','PIDILITIND':'500331','SIEMENS':'500550','HAVELLS':'517354','VOLTAS':'500575','AMBUJACEM':'500425','ACC':'500410','SHREECEM':'500387','RAMCOCEM':Ku,Kp:Kv,'JKCEMENT':'532644','STAR':Kw,'TVSMOTOR':'532343','BOSCHLTD':'500530','MUTHOOTFIN':'533398','CHOLAFIN':'500443','BAJAJHLDNG':'500490','TORNTPHARM':Kx,'AUROPHARMA':'524208','LUPIN':'500257','BIOCON':'532523','ALKEM':'539523','IPCALAB':'530827','GLAXO':'500660','ABBOTINDIA':'500488','PFIZER':'500680','SANOFI':'500674','MCDOWELL-N':'532432','ITC':'500875','GODFRYPHLP':'500163','COLPAL':'500830','DABUR':'500096','MARICO':'531642','GODREJCP':'532424','HINDPETRO':'500104','CASTROLIND':'500870','INDIGO':'521737','INTERGLOBE':'539448','SPICEJET':'500285','IRCTC':'542830','CONCOR':'531344','ADANIGREEN':'541450','ADANITRANS':'539254','TATAPOWER':'500400','TORNTPOWER':'532779','CESC':'500084','NHPC':'533098','SJVN':'533206','PFC':'532810','RECLTD':'532955','IRFC':'543257','ZOMATO':'543320','NYKAA':'543384','PAYTM':'543396','POLICYBZR':'543390','DELHIVERY':'543529','CARTRADE':'543202','RVNL':'542649','IRCON':'541956','NBCC':'534309','HUDCO':'540530','MMTC':Ky,'MTNL':'500108','BEL':'500049','HAL':'541154','COCHINSHIP':'526235','MAZAGON':'543237','GRSE':'542351','MIDHANI':'541195','BEML':'500048','BHEL':'500103','SAIL':'500113','NMDC':'526371','MOIL':'533286','NATIONALUM':'532234','HINDZINC':'500188','VEDL':'500295','GMRINFRA':'532754','NHAI':'500253','IRB':'532947','ASHOKLEY':'500477','ESCORTS':'500495','FORCE':'517168','SML':'513275','MOTHERSON':'517334','MINDAIND':'532539','ENDURANCE':'540350','BALKRISIND':'502355','APOLLOTYRE':'500877','MRF':'500290','CEATLTD':'500878','JK TYRE':'530007','INOXWIND':'539083','SUZLON':'532667','RPOWER':'500390','JPPOWER':'532627','FEDERALBNK':'500469','IDFCFIRSTB':'539437','BANDHANBNK':'541153','RBLBANK':'540065','DCBBANK':'532772','KTKBANK':Kz,'SOUTHBANK':'532218','CANBK':'532483','BANKBARODA':'532134','UNIONBANK':'532477','INDIANB':'532814','UCOBANK':'532505','CENTRALBK':'532885','MAHABANK':'532525','J&KBANK':Kz,'PNB':'532461','IOB':'532388','BANKINDIA':'532149','DENABANK':'532121','SYNDIBANK':'532276','VIJAYABANK':'532245','ORIENTBANK':'500315','CORPBANK':'532179','ANDHRABANK':'532418','ALLAHABAD':K_,'ALBK':K_,'MFSL':'542299','HDFCAMC':'541530','NIPPONLIFE':'543171','UTIAMC':'543238','ABCAPITAL':'540691','ANGELONE':'543235','ICICIGI':'540716','GICRE':'540755','NIACL':'540769','STAR':Kw,'CROMPTON':'539876','ORIENTELEC':'531637','BLUESTAR':'500067','WHIRLPOOL':'500238','VGUARD':'532953','BAJAJEL':'500031','CERA':'532443','HINDWARE':'509820','HSIL':'509675','KAJARIACER':'500233','SOMANYCER':'532622','GRINDWELL':'506076','CARBORUNIV':'513375','ASTRAL':'532830','FINOLEX':'500940','SUPREMEIND':'509930','BERGER':'509480','KANSAINER':'500165','AKZOINDIA':'500710','INDIACEM':'530005','RAMCOIND':Ku,Kp:Kv,'HEIDELBERG':'500292','PRISM':'500338','BIRLACORPN':'500335','ORIENTCEM':'502420','SAGCEM':'502090','STARCEMENT':'540575','JKLAKSHMI':'500380','NUVOCO':'543334','ZYDUSLIFE':'532321','TORNTPHAR':Kx,'NATCOPHAR':'524816','GRANULES':'532482','LAURUS':L0,'STRIDES':'532531','AJANTPHAR':'532331','CAPLIPOINT':'539266','DIVI':Ks,Kn:Kr,'GLAND':'543245','SEQUENT':'543225','METROPOLIS':'542650','DRLAL':'532259','THYROCARE':'539871','KRSNAA':'543328','VIJAYA':'532542','MAXHEALTH':'543220','KIMS':'543308','ASTER':'540975','FORTIS':'532843','NHOSPIT':'532526',Ko:Kt,'NARAYANA':'539551','YATHARTH':'544120','RAINBOW':'543524','SUVENPHAR':'530239','LAURUSLABS':L0,'SOLARA':'541540','SHILPAMED':'530879','PERSISTENT':'533179','MINDTREE':'532819','MPHASIS':'526299','HEXAWARE':'532861','NIIT':'500304','KPIT':'542651','LTTS':'540115','COFORGE':'532541','ZENSAR':'504067','RAMSYSTEMS':'532370','MASTEK':'523704','SASKEN':'532663','TATAELXSI':'500408','CYIENT':'532175','SONATSOFTW':'532221','TANLA':'532790','LTIM':'540005','INFY':Kq,'ROUTE':'543228','BSOFT':'526301','NEWGEN':'540900','INTELLECT':'538835','NUCLEUS':'531209','NELCO':'504112','DELTACORP':'532840','WONDERLA':'538268','MAHINDCIE':'532756','STARHLTH':'543412','NAUKRI':'532777','JUSTDIAL':'535648','MATRIMONY':'539846','MAKEMYTRIP':Ky,'IXIGO':'544229','RATEGAIN':'543417','TEAMLEASE':'539658','QUESS':'539978','SIS':'540673','SECURKLOUD':'539963','HAPPYFORGE':'543532','KALYANKJIL':'543278','SENCO':'543456','THANGAMAYL':'531509','TRIBHOVAND':'512415','PC JEWELLER':'534809','RAJESHEXPO':'531500'}
	@A.cache_data(ttl=600)
	def OQ(bse_code,days_back=90):
		L='SUBCATNAME';A={Gl:[],Gm:[],Gn:[],Go:[],ES:[]}
		try:
			import datetime as F;G=F.date.today();M=G-F.timedelta(days=days_back);N=M.strftime(Bk);O=G.strftime(Bk);P=f"https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w?pageno=1&strCat=-1&strPrevDate={N}&strScrip={bse_code}&strSearch=P&strToDate={O}&strType=C&subcategory=-1";Q={Ca:Cb,'Referer':'https://www.bseindia.com/','Accept':'application/json'};R=urllib.request.Request(P,headers=Q)
			with urllib.request.urlopen(R,timeout=8)as S:T=EU.loads(S.read())
			for B in(T.get('Table')or[])[:30]:
				U=B.get('HEADLINE',C)or B.get(L,C);I=B.get('NEWS_DT',C)or B.get('DT_TM',C);J=B.get('NEWSID',C);V=f"https://www.bseindia.com/xml-data/corpfiling/AttachLive/{J}.pdf"if J else C
				try:K=H.to_datetime(I).strftime(EE)
				except g:K=I[:10]
				E=(B.get(L)or C).lower();D={A5:U,f:V,BJ:K}
				if AW(A in E for A in['annual report','annual rep']):A[Gm].append(D)
				elif AW(A in E for A in['credit rat','rating']):A[Gn].append(D)
				elif AW(A in E for A in['concall','con call','earnings call','analyst']):A[Go].append(D)
				elif AW(A in E for A in['investor presentation','presentation',ES]):A[ES].append(D)
				else:A[Gl].append(D)
		except g:pass
		return A
try:
	CI=K[n].dropna().unique()
	if Q(CI)>0:
		OR,OS,OT,OU,OV,OW,OX=A.tabs(['🚨 Latest Alerts Timeline','🏢 Alerts by Stock','📰 Smart News Engine (1 Day)','📰 Smart News Engine (All News)','📢 Corporate Announcements','📢 DOCUMENTS HUB','📜 Rules']);Cw=[];J4=CI[:30]
		with A.spinner('Scanning Top 30 stocks for Circuit & 52-Week Breakouts (15 Days)...'):
			for G in J4:
				A1=F(G).strip();BB=OL(A1,limit=15)
				for Aw in BB:Aw[AZ]=A1;Cw.append(Aw)
		OY={A[AZ]for A in Cw};J5={A[AZ]for A in Cw if Ab in A[L]or Ac in A[L]or Ad in A[L]or AH in A[L]}
		def OZ(sym):
			A=sym
			if A in J5:B,C,D=Aa,'#003300','#0fbf62'
			elif A in OY:B,C,D='#1a7a45',C_,'#145e34'
			else:B,C,D='#444',C_,'#333'
			return f"<span style='background:{B}; color:{C}; padding:2px 9px; border-radius:5px; font-weight:700; font-size:0.82em; border:1px solid {D}; white-space:nowrap;'>⚡ {A}</span>"
		with OR:
			Oa,Ob,Oc=A.columns([2,1,1]);J6=Oa.text_input('🔍 Search Alerts:',placeholder='e.g. ICICIBANK, circuit...',key='global_news_search');J7=Ob.selectbox('⏳ Time Filter:',['All (Up to 15 Days)',L1,L2],key='global_news_time');Od=Oc.radio('↕️ Sort By Time:',[L3,'Oldest First'],horizontal=B,key='global_news_sort');Ax=Cw.copy()
			if J6:J8=J6.lower();Ax=[A for A in Ax if J8 in A[AZ].lower()or J8 in A[Kk].lower()]
			if J7==L2:Ax=[A for A in Ax if Ab in A[L]or Ac in A[L]or Ad in A[L]or AH in A[L]]
			elif J7==L1:Oe=H.Timestamp.now(tz=BM);Ax=[A for A in Ax if(Oe-A[AI]).total_seconds()/86400<=7.]
			Ax.sort(key=lambda x:x[AI],reverse=Od==L3);A.markdown(CX,unsafe_allow_html=B)
			if Ax:
				for N in Ax:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;Of=OZ(N[AZ]);A.markdown(f"- {Of}&nbsp; <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B);A.markdown("<hr style='margin: 0.4em 0; opacity: 0.15;'>",unsafe_allow_html=B)
			else:A.info('No circuit or 52-week alerts match your search or filter criteria.')
		with OS:
			Og=A.columns(2);Fd=0
			for A1 in[F(A).strip()for A in J4]:
				Dq=[A for A in Cw if A[AZ]==A1];Dq.sort(key=lambda x:x[AI],reverse=B)
				if Dq:
					with Og[Fd%2]:
						Oh='🟢'if A1 in J5 else'🟡'
						with A.expander(f"{Oh} {A1} Action Alerts (0 Sec to 15 Days)",expanded=B):
							Oi=Dq[:3];Fe=Dq[3:]
							for N in Oi:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fe:
								with A.expander(f"🔽 Show {Q(Fe)} more older alerts",expanded=J):
									for N in Fe:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fd+=1
			if Fd==0:A.info('No circuit breakouts or 52-week boundary alerts for the currently filtered stocks in the last 15 days.')
		with OT:
			A.markdown('### Latest News & Action Alerts (Past 24 Hours)');Oj=A.columns(2);Ff=0
			for Cx in CI[:10]:
				A1=F(Cx).strip();BB=OM(A1,limit=5)
				if BB:
					with Oj[Ff%2]:
						with A.expander(f"📰 {A1} News Feed (0 Sec to 1 Day)",expanded=B):
							for N in BB:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Ff+=1
			if Ff==0:A.info('No general news found for the currently filtered stocks in the last 24 hours.')
		with OU:
			A.markdown('### Latest News & Action Alerts (All Time)');Ok=A.columns(2);Fg=0
			for Cx in CI[:10]:
				A1=F(Cx).strip();BB=ON(A1,limit=6)
				if BB:
					with Ok[Fg%2]:
						with A.expander(f"📰 {A1} News Feed (All News)",expanded=B):
							Ol=BB[:3];Fh=BB[3:]
							for N in Ol:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
							if Fh:
								with A.expander(f"🔽 Show {Q(Fh)} more articles",expanded=J):
									for N in Fh:h=Ab in N[L]or Ac in N[L]or Ad in N[L]or AH in N[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{N[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{N[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {N[L]}</span>",unsafe_allow_html=B)
					Fg+=1
			if Fg==0:A.info('No general news found for the currently filtered stocks.')
		with OV:
			A.markdown('### 📢 Official Exchange Filings & Corporate Announcements');A.markdown("<span style='font-size: 0.9em; color: gray;'>Tracks Regulation 30, LODR, Board Meetings, AGMs, and Analyst Meets.</span>",unsafe_allow_html=B);A.markdown(CX,unsafe_allow_html=B);Om=A.columns(2);Fi=0
			for Cx in CI[:15]:
				A1=F(Cx).strip();Fj=OO(A1,limit=7)
				if Fj:
					with Om[Fi%2]:
						with A.expander(f"📢 {A1} Filings & Announcements",expanded=B):
							On=Fj[:3];Fk=Fj[3:]
							for A2 in On:h=Ab in A2[L]or Ac in A2[L]or Ad in A2[L]or AH in A2[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{A2[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A2[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {A2[L]}</span>",unsafe_allow_html=B)
							if Fk:
								with A.expander(f"🔽 Show {Q(Fk)} more filings",expanded=J):
									for A2 in Fk:h=Ab in A2[L]or Ac in A2[L]or Ad in A2[L]or AH in A2[L];s=Aa if h else B0;t=AR if h else AQ;A.markdown(f"- <a href='{A2[f]}' target='_blank' style='text-decoration: none; color: inherit;'>{A2[AD]}</a> <span style='color: {s}; font-weight: {t}; font-size: 0.85em;'>— 🕒 {A2[L]}</span>",unsafe_allow_html=B)
					Fi+=1
			if Fi==0:A.info('No recent corporate filings or official announcements found for the filtered stocks.')
		with OW:
			A.markdown('### 📄 Documents Hub — Announcements · Annual Reports · Credit Ratings · Concalls · PPT · REC');A.markdown("<span style='font-size:0.88em; color:#888;'>Live BSE India filings (public API, no key needed). Annual Reports & Concalls also link to Screener.in.</span>",unsafe_allow_html=B);A.markdown(CX,unsafe_allow_html=B);Oo,Op,Oq=A.columns([3,1.2,1.2])
			with Oo:J9=[F(A).strip()for A in CI[:60]];JA=A.multiselect('🔍 Stocks to view:',options=J9,default=J9[:4],key='doc_hub_stocks_v2')
			with Op:Or=A.selectbox('📅 Date range:',[Gj,L4,L5,Gk],index=1,key='doc_days_v2')
			with Oq:JB=A.selectbox('📋 Rows per section:',[3,5,8,12],index=1,key='doc_limit_v2')
			Os={Gj:30,L4:90,L5:180,Gk:365};Ot=Os[Or]
			if not JA:A.info('Select at least one stock above to view its documents.')
			else:
				for o in JA:
					v=OP.get(o.upper(),C)
					with A.expander(f"📁  {o}   {"· BSE "+v if v else"· BSE code not mapped — Screener links shown"}",expanded=B):
						Fl="<div style='display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;'>";Ou=[('📢 BSE Announcements',f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={v}"if v else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}",L6,L7),('📑 Annual Reports',f"https://www.screener.in/company/{o}/",CW,L8),('⭐ Credit Ratings',f"https://www.screener.in/company/{o}/",GB,'#f57f17'),('🎙️ Concalls',f"https://www.screener.in/company/{o}/",'#fce4ec',DI),('📊 Investor PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={v}"if v else f"https://www.screener.in/company/{o}/",L9,LA),('🏛️ NSE Filings',f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}",'#e0f7fa','#00695c'),('📈 Screener',f"https://www.screener.in/company/{o}/",'#fffde7',A_)]
						for(Fm,Fn,Fo,Fp)in Ou:Fl+=f"<a href='{Fn}' target='_blank' style='background:{Fo}; color:{Fp}; padding:5px 12px; border-radius:6px; font-size:0.78em; font-weight:600; text-decoration:none; white-space:nowrap;'>{Fm}</a>"
						Fl+=Cz;A.markdown(Fl,unsafe_allow_html=B);CJ={}
						if v:
							with A.spinner(f"Fetching BSE filings for {o}…"):CJ=OQ(v,days_back=Ot)
						Ov,Ow,Ox,Oy=A.columns([3,2,2,3])
						with Ov:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #5c6bc0; padding-bottom:4px; color:#5c6bc0;'>📢 Announcements</p>",unsafe_allow_html=B);JC=CJ.get(Gl,[])
							if JC:
								Oz,O_=A.tabs([GN,'All ↗'])
								with Oz:
									for CK in JC[:JB]:BC=CK[A5][:85]+'…'if Q(CK[A5])>85 else CK[A5];Bh=f"<a href='{CK[f]}' target='_blank' style='color:#5c6bc0; text-decoration:none;'>{BC}</a>"if CK[f]else f"<span>{BC}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:6px; border-left:3px solid #c5cae9; padding-left:6px;'>{Bh}<br><span style='color:#aaa; font-size:0.85em;'>{CK[BJ]}</span></div>",unsafe_allow_html=B)
								with O_:P0=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={v}"if v else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}";A.markdown(f"<a href='{P0}' target='_blank' style='color:#5c6bc0; font-size:0.85em;'>🔗 Open full announcements page →</a>",unsafe_allow_html=B)
							else:P1=f"https://www.bseindia.com/corporates/Corp_Annoucement.html?expandable=0&scripcd={v}"if v else f"https://www.nseindia.com/companies-listing/corporate-filings-announcements?symbol={o}";A.markdown(f"<a href='{P1}' target='_blank' style='color:#5c6bc0; font-size:0.83em;'>🔗 View on {"BSE"if v else"NSE"} →</a>",unsafe_allow_html=B);A.caption('No announcements in selected date range.')
						with Ow:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #43a047; padding-bottom:4px; color:#43a047;'>📑 Annual Reports</p>",unsafe_allow_html=B);JD=CJ.get(Gm,[])
							if JD:
								for Dr in JD[:6]:JE=Dr[BJ][:4]if Dr[BJ]else'Report';Bh=f"<a href='{Dr[f]}' target='_blank' style='color:#43a047; text-decoration:none;'>📄 Annual Report {JE}</a>"if Dr[f]else f"<span>📄 Annual Report {JE}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px;'>{Bh}</div>",unsafe_allow_html=B)
							else:
								if v:A.markdown(f"<a href='https://www.bseindia.com/AnnualReports.html?scripcd={v}' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 BSE Annual Reports →</a>",unsafe_allow_html=B)
								A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#43a047; font-size:0.83em;'>📑 View on Screener →</a>",unsafe_allow_html=B);A.caption('Not found in selected range — try 1 Year.')
						with Ox:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #f57f17; padding-bottom:4px; color:#f57f17;'>⭐ Credit Ratings</p>",unsafe_allow_html=B);JF=CJ.get(Gn,[])
							if JF:
								for CL in JF[:4]:BC=CL[A5][:70]+'…'if Q(CL[A5])>70 else CL[A5];Bh=f"<a href='{CL[f]}' target='_blank' style='color:#f57f17; text-decoration:none;'>{BC}</a>"if CL[f]else f"<span>{BC}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffe0b2; padding-left:6px;'>{Bh}<br><span style='color:#aaa; font-size:0.85em;'>{CL[BJ]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#f57f17; font-size:0.83em;'>⭐ Ratings on Screener →</a>",unsafe_allow_html=B);A.markdown("<div style='font-size:0.78em; margin-top:8px; color:#888;'><a href='https://www.careratings.com' target='_blank' style='color:#888;'>CARE</a> · <a href='https://www.icra.in' target='_blank' style='color:#888;'>ICRA</a> · <a href='https://www.crisil.com' target='_blank' style='color:#888;'>CRISIL</a> · <a href='https://www.infomerics.com' target='_blank' style='color:#888;'>Infomerics</a></div>",unsafe_allow_html=B);A.caption('Not found via BSE — check links above.')
						with Oy:
							A.markdown("<p style='font-weight:700; font-size:0.9em; border-bottom:2px solid #e53935; padding-bottom:4px; color:#e53935;'>🎙️ Concalls &amp; Investor Docs</p>",unsafe_allow_html=B);P2=CJ.get(Go,[]);JG=CJ.get(ES,[]);JH=JG+P2
							if JH:
								for Bi in JH[:JB]:P3=Bi in JG;JI='📊'if P3 else'🎙️';BC=Bi[A5][:70]+'…'if Q(Bi[A5])>70 else Bi[A5];Bh=f"<a href='{Bi[f]}' target='_blank' style='color:#e53935; text-decoration:none;'>{JI} {BC}</a>"if Bi[f]else f"<span>{JI} {BC}</span>";A.markdown(f"<div style='font-size:0.82em; margin-bottom:5px; border-left:3px solid #ffcdd2; padding-left:6px;'>{Bh}<br><span style='color:#aaa; font-size:0.85em;'>{Bi[BJ]}</span></div>",unsafe_allow_html=B)
							else:A.markdown(f"<a href='https://www.screener.in/company/{o}/' target='_blank' style='color:#e53935; font-size:0.83em;'>🎙️ Concalls on Screener →</a>",unsafe_allow_html=B);A.caption('No concalls/PPT in selected date range.')
							A.markdown(CX,unsafe_allow_html=B);Fq="<div style='display:flex; gap:6px; flex-wrap:wrap;'>";P4=[('📝 Transcript',f"https://www.screener.in/company/{o}/",L6,L7),('🤖 AI Summary',f"https://www.screener.in/company/{o}/",CW,L8),('📊 PPT',f"https://www.bseindia.com/corporates/Inv_Rel.aspx?scripcd={v}"if v else f"https://www.screener.in/company/{o}/",L9,LA),('▶️ REC',f"https://www.youtube.com/results?search_query={o}+concall+earnings",Bm,DA)]
							for(Fm,Fn,Fo,Fp)in P4:Fq+=f"<a href='{Fn}' target='_blank' style='background:{Fo}; color:{Fp}; padding:3px 10px; border-radius:4px; font-size:0.76em; font-weight:600; text-decoration:none;'>{Fm}</a>"
							Fq+=Cz;A.markdown(Fq,unsafe_allow_html=B)
		with OX:A.markdown('### 📜 Trading Rules');A.markdown("<span style='font-size:0.88em; color:#888;'>Edit the <code>TRADING_RULES_LIBRARY</code> constant near the top of the .py file to change anything shown below — same pattern as the AI Prompt Library &amp; Pine Script Custom Rules Library.</span>",unsafe_allow_html=B);A.markdown(CX,unsafe_allow_html=B);A.markdown(LI)
	else:A.info('No stocks currently filtered to check.')
except g as BZ:A.error(f"⚠️ Could not load the News Engine. Error details: {BZ}")
else:A.warning('No data loaded. Check sheet sharing and secrets.')
