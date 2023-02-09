import pandas as pd
import streamlit as st
import babel.numbers
import plotly.graph_objects as go

# set page config
st.set_page_config( 'Mutual Fund Calculator',page_icon=':bar_chart:',layout='centered')

# set tabs
tab1, tab2 = st.tabs(tabs=['SIP Calculator', 'Lumpsump Investment Calculator'])

# with tab 1
with tab1:

    # input SIP amount, expected rate of return & duration of investment
    sip_amount = st.number_input('SIP Amount',100,100000,1000)
    rate_of_return = st.number_input('Expected Rate of Return (in %)',0.0,100.0,12.0,0.01)
    duration = st.number_input('Duration of Investment (in years)',1,100,10)

    st.markdown('##')
    # checkbox for adjusting inflation
    checkbox = st.checkbox('Adjust SIP for Inflation ? (Assumed annual inflation rate is 6%)',False)

    # if inflation checkbox if off
    if checkbox == False:

        monthly_rate = rate_of_return/12/100
        months = duration * 12
        
        invested_value = sip_amount*months
        invested_value_inwords = babel.numbers.format_currency(invested_value,'INR',locale='en_IN')

        future_value = sip_amount * ((((1 + monthly_rate)**(months))-1) * (1 + monthly_rate))/monthly_rate
        future_value_inwords = babel.numbers.format_currency(future_value,'INR',locale='en_IN')

        gain = float(future_value) - float(invested_value)
        gain_inwords = babel.numbers.format_currency(gain,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {invested_value_inwords}')
        st.subheader(f'Final Amount: {future_value_inwords}')
        st.subheader(f'Gain: {gain_inwords}')

        # plot pie chart
        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[invested_value,gain])])
        fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)

    elif checkbox == True:

        monthly_rate = (rate_of_return-6)/12/100
        months = duration * 12
        
        invested_value = sip_amount*months
        invested_value_inwords = babel.numbers.format_currency(sip_amount*months,'INR',locale='en_IN')

        future_value = sip_amount * ((((1 + monthly_rate)**(months))-1) * (1 + monthly_rate))/monthly_rate
        future_value_inwords = babel.numbers.format_currency(future_value,'INR',locale='en_IN')

        gain_after_inflation = float(future_value) - float(invested_value)
        gain_after_inflation_inwords = babel.numbers.format_currency(gain_after_inflation,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {invested_value_inwords}')
        st.subheader(f'After Inflation: {future_value_inwords}')
        st.subheader(f'Gain: {gain_after_inflation_inwords}')

        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[invested_value,gain_after_inflation])])
        fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)

    st.subheader('About SIP & SIP Calculator')
    st.write('''
    Systematic Investment Plan (SIP) is a kind of investment scheme offered by mutual fund companies. Using SIP one can invest small amount peridically (weekly, monthly, quaterly) into a selected mutual fund. For retail investors, SIP offers a well disciplined and passive approach to investing, to create wealth in long term (using the power of compounding). Since, the amount is invested on regular intervals (usually on monthly basis), it also reduces the impact of market volatility.

This calculator helps you calculate the wealth gain and expected returns for your monthly SIP investment.''')



# with tab 2 - lumpsum investment
with tab2:
    
    lumpsum_amount = st.number_input('Investment Amount',100,9999999999,1000)
    lumpsum_amount_inwords = babel.numbers.format_currency(lumpsum_amount,'INR',locale='en_IN')

    lumpsum_rate_of_return = st.number_input('Expected Rate of Return (in %)',1.00,100.0,12.0,0.01)
    lumpsum_duration = st.number_input('Duration of Investment (in years)',1,99,10)

    cagr = lumpsum_amount * (pow((1 + lumpsum_rate_of_return/100),lumpsum_duration))
    cagr_inwords = babel.numbers.format_currency(cagr,'INR',locale='en_IN')

    st.markdown('##')
    lumpsum_checkbox = st.checkbox('Adjust Investment for Inflation ? (Assumed annual inflation rate is 6%)',False)
    
    if lumpsum_checkbox == False:
        
        lumpsum_gain = float(cagr) - float(lumpsum_amount)
        lumpsum_gain_inwords = babel.numbers.format_currency(lumpsum_gain,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {lumpsum_amount_inwords}')
        st.subheader(f'Final Amount: {cagr_inwords}')
        st.subheader(f'Gain: {lumpsum_gain_inwords}')

        # plot pie chart
        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[lumpsum_amount,lumpsum_gain])])
        fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)
    
    if lumpsum_checkbox == True:
        cagr_after_inflation = lumpsum_amount * (pow((1 + (lumpsum_rate_of_return-6)/100),lumpsum_duration))
        cagr_after_inflation_inwords = babel.numbers.format_currency(cagr_after_inflation,'INR',locale='en_IN')
        
        lumpsum_gain_after_inflation = float(cagr_after_inflation) - float(lumpsum_amount)
        lumpsum_gain_after_inflation_inwords = babel.numbers.format_currency(lumpsum_gain_after_inflation,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {lumpsum_amount_inwords}')
        st.subheader(f'After Inflation: {cagr_after_inflation_inwords}')
        st.subheader(f'Gain: {lumpsum_gain_after_inflation_inwords}')

        # plot pie chart
        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[lumpsum_amount,lumpsum_gain_after_inflation])])
        fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)


# credits
st.markdown('##')
st.markdown('##')
st.write('Created with ❤️ by Shubham Harwani')

website = 'https://www.trademadaari.in/about-us'
instagram = 'https://instagram.com/oyesindhi_'
github = 'https://github.com/oyesindhi'

st.markdown(f'''<a href={website}><button style="background-color:#FF4B4B;">Visit Our Website</button></a> 

<a href={instagram}><button style="background-color:#FF4B4B;">Follow Me on Instagram</button></a> 

<a href={github}><button style="background-color:#FF4B4B;">Follow Me on GitHub</button></a>''',unsafe_allow_html=True)

#this is the css code to hide main menu button, stream logo at the bottom, top header colored ribbon

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
