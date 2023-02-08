import pandas as pd
import streamlit as st
import locale

# set local currency
locale.setlocale(locale.LC_ALL,'')

# set page config
st.set_page_config( 'Mutual Fund Calculator',page_icon=':bar_chart:',layout='centered')

# set tabs
tab1, tab2 = st.tabs(tabs=['SIP Calculator', 'Lumpsump Investment Calculator'])

# with tab 1
with tab1:
    sip_amount = st.number_input('SIP Amount',100,100000,1000)
    rate_of_return = st.number_input('Expected Rate of Return (in %)',0.0,100.0,12.0,0.01)
    duration = st.number_input('Duration of Investment (in years)',1,100,10)

    monthly_rate = rate_of_return/12/100
    months = duration * 12
    
    invested_value = sip_amount*months
    invested_value_inwords = locale.currency(sip_amount*months,grouping=True)

    future_value = sip_amount * ((((1 + monthly_rate)**(months))-1) * (1 + monthly_rate))/monthly_rate
    future_value_inwords = locale.currency(future_value,grouping=True)

    gain = float(future_value) - float(invested_value)
    gain_inwords = locale.currency(gain,grouping=True)

    st.subheader(f'Amount Invested: {invested_value_inwords}')
    st.subheader(f'Final Amount: {future_value_inwords}')
    st.subheader(f'Gain: {gain_inwords}')

    st.markdown('##')

    if st.checkbox('Adjust SIP for Inflation ? (Assumed annual inflation rate is 6%)',False) == True:

        monthly_rate = (rate_of_return-6)/12/100
        months = duration * 12
        
        invested_value = sip_amount*months
        invested_value_inwords = locale.currency(sip_amount*months,grouping=True)

        future_value = sip_amount * ((((1 + monthly_rate)**(months))-1) * (1 + monthly_rate))/monthly_rate
        future_value_inwords = locale.currency(future_value,grouping=True)

        st.subheader(f'After Inflation: {future_value_inwords}')


# with tab 2
with tab2:
    lumpsum_amount = st.number_input('Investment Amount',100,9999999999,1000)
    lumpsum_amount_inwords = locale.currency(lumpsum_amount,grouping=True)

    lumpsum_rate_of_return = st.number_input('Expected Rate of Return (in %)',1.00,100.0,12.0,0.01)
    lumpsum_duration = st.number_input('Duration of Investment (in years)',1,99,10)

    cagr = lumpsum_amount * (pow((1 + lumpsum_rate_of_return/100),lumpsum_duration))
    cagr_inwords = locale.currency(cagr,grouping=True)
    
    lumpsum_gain = float(cagr) - float(lumpsum_amount)
    lumpsum_gain_inwords = locale.currency(lumpsum_gain,grouping=True)

    st.subheader(f'Amount Invested: {lumpsum_amount_inwords}')
    st.subheader(f'Final Amount: {cagr_inwords}')
    st.subheader(f'Gain: {lumpsum_gain_inwords}')

    st.markdown('##')
    
    if st.checkbox('Adjust Investment for Inflation ? (Assumed annual inflation rate is 6%)',False) == True:
        lumpsum_present_value = cagr / (pow(1.06,duration))
        lumpsum_present_value_inwords = locale.currency(lumpsum_present_value,grouping=True)
        
        st.subheader(f'After Inflation: {lumpsum_present_value_inwords}')


st.markdown('##')
st.markdown('##')
st.write('✅ This tool is created by Shubham Harwani')

instagram = 'https://instagram.com/oyesindhi_'
st.markdown(f'<a href={instagram}><button style="background-color:#FF4B4B;">Follow Me on Instagram</button></a>',unsafe_allow_html=True)

instagram = 'https://github.com/oyesindhi'
st.markdown(f'<a href={instagram}><button style="background-color:#FF4B4B;">Follow Me on GitHub</button></a>',unsafe_allow_html=True)

#this is the css code to hide main menu button, stream logo at the bottom, top header colored ribbon

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
