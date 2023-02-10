import pandas as pd
import streamlit as st
import babel.numbers
import plotly.graph_objects as go

# set page config
st.set_page_config( 'Mutual Fund Calculator',page_icon=':bar_chart:',layout='centered')

# set tabs
tab1, tab2, tab3, tab4 = st.tabs(tabs=['SIP Calculator', 'Lumpsump Investment Calculator','Quick Tools','MF Guide'])

# with tab 1
with tab1:

    # input SIP amount, expected rate of return & duration of investment
    sip_amount = st.number_input('SIP Amount',100,100000,1000)
    #rate_of_return = st.number_input('Expected Rate of Return (in %)',0.0,100.0,12.0,0.01)
    rate_of_return = st.slider('Expected Rate of Return (in %)',1,30,12)
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

        gain = round(float(future_value) - float(invested_value),2)
        gain_inwords = babel.numbers.format_currency(gain,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {invested_value_inwords}')
        st.subheader(f'Final Amount: {future_value_inwords}')
        st.subheader(f'Gain: {gain_inwords}')

        # plot pie chart
        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[invested_value,gain])])
        fig.update_traces(hoverinfo='value', textinfo='label+value', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)

    elif checkbox == True:

        monthly_rate = (rate_of_return-6)/12/100
        months = duration * 12
        
        invested_value = sip_amount*months
        invested_value_inwords = babel.numbers.format_currency(sip_amount*months,'INR',locale='en_IN')

        future_value = sip_amount * ((((1 + monthly_rate)**(months))-1) * (1 + monthly_rate))/monthly_rate
        future_value_inwords = babel.numbers.format_currency(future_value,'INR',locale='en_IN')

        gain_after_inflation = round(float(future_value) - float(invested_value),2)
        gain_after_inflation_inwords = babel.numbers.format_currency(gain_after_inflation,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {invested_value_inwords}')
        st.subheader(f'Final Amount: {future_value_inwords}')
        st.subheader(f'Gain: {gain_after_inflation_inwords}')

        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[invested_value,gain_after_inflation])])
        fig.update_traces(hoverinfo='value', textinfo='label+value', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)

    st.subheader('About SIP & SIP Calculator')
    st.write('''
    Systematic Investment Plan (SIP) is a kind of investment scheme offered by mutual fund companies. Using SIP one can invest small amount peridically (weekly, monthly, quaterly) into a selected mutual fund. For retail investors, SIP offers a well disciplined and passive approach to investing, to create wealth in long term (using the power of compounding). Since, the amount is invested on regular intervals (usually on monthly basis), it also reduces the impact of market volatility.

This calculator helps you calculate the wealth gain and expected returns for your monthly SIP investment.''')



# with tab 2 - lumpsum investment
with tab2:
    
    lumpsum_amount = st.number_input('Investment Amount',100,9999999999,1000)
    lumpsum_amount_inwords = babel.numbers.format_currency(lumpsum_amount,'INR',locale='en_IN')

    #lumpsum_rate_of_return = st.number_input('Expected Rate of Return (in %)',1.00,100.0,12.0,0.01)
    lumpsum_rate_of_return = st.slider('Expected Rate of Return (in %) ',1,30,12)
    lumpsum_duration = st.number_input('Duration of Investment (in years)',1,99,10)

    cagr = lumpsum_amount * (pow((1 + lumpsum_rate_of_return/100),lumpsum_duration))
    cagr_inwords = babel.numbers.format_currency(cagr,'INR',locale='en_IN')

    st.markdown('##')
    lumpsum_checkbox = st.checkbox('Adjust Investment for Inflation ? (Assumed annual inflation rate is 6%)',False)
    
    if lumpsum_checkbox == False:
        
        lumpsum_gain = round(float(cagr) - float(lumpsum_amount),2)
        lumpsum_gain_inwords = babel.numbers.format_currency(lumpsum_gain,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {lumpsum_amount_inwords}')
        st.subheader(f'Final Amount: {cagr_inwords}')
        st.subheader(f'Gain: {lumpsum_gain_inwords}')

        # plot pie chart
        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[lumpsum_amount,lumpsum_gain])])
        fig.update_traces(hoverinfo='value', textinfo='label+value', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)
    
    elif lumpsum_checkbox == True:
        cagr_after_inflation = lumpsum_amount * (pow((1 + (lumpsum_rate_of_return-6)/100),lumpsum_duration))
        cagr_after_inflation_inwords = babel.numbers.format_currency(cagr_after_inflation,'INR',locale='en_IN')
        
        lumpsum_gain_after_inflation = round(float(cagr_after_inflation) - float(lumpsum_amount),2)
        lumpsum_gain_after_inflation_inwords = babel.numbers.format_currency(lumpsum_gain_after_inflation,'INR',locale='en_IN')

        st.subheader(f'Amount Invested: {lumpsum_amount_inwords}')
        st.subheader(f'Final Amount: {cagr_after_inflation_inwords}')
        st.subheader(f'Gain: {lumpsum_gain_after_inflation_inwords}')

        # plot pie chart
        fig = go.Figure(data=[go.Pie(labels=['Investment','Gain'], values=[lumpsum_amount,lumpsum_gain_after_inflation])])
        fig.update_traces(hoverinfo='value', textinfo='label+value', textfont_size=15,marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
        st.plotly_chart(fig)


# tab 3 - future & present value calculator
with tab3:
    calc1, calc2 = st.columns(2)

    with calc1:
        st.subheader('Future Value Calculator')

        principal_amount = st.number_input('Today\'s Value',1,1000000000,50000)
        after_years = st.number_input('After Years',1,100,10)
        expected_increase = st.number_input('Expected Rate of Increase (in %)',1,20,6)
        expected_increase = expected_increase/100

        future_value_calc = principal_amount * (pow(1+expected_increase,after_years))
        future_value_calc_inwords = babel.numbers.format_currency(future_value_calc,'INR',locale='en_IN')

        st.subheader(f'Future Value: {future_value_calc_inwords}')

    with calc2:
        st.subheader('Present Value Calculator')

        principal_amount1 = st.number_input('Future\'s Value',1,1000000000,100000)
        after_years1 = st.number_input('After Years ',1,100,5)
        expected_decrease = st.number_input('Expected Rate of Decrease (in %)',1,20,6)
        expected_decrease = expected_decrease/100

        present_value_calc = principal_amount1 / (pow(1+expected_decrease,after_years1))
        present_value_calc_inwords = babel.numbers.format_currency(present_value_calc,'INR',locale='en_IN')

        st.subheader(f'Present Value: {present_value_calc_inwords}')


# mf guide
with tab4:

    st.subheader('How to choose between so many mutual funds?')

    st.write('''
    Nowadays, investing in mutual funds isn't very easy because of unlimited options to categories and schemes and what not.
    However, these multiple categories and options doesn't make your investing journey any easier; rather more difficult and confusing, is what I believe.

    So, having spent more than 4 years in the industry, with my limited amount of knowledge and experience, I have set a few thumb rules to overcome this problem
    and make investing in mutual funds more easier.

    Now, mutual funds is not "one-size-fits-all" thing. However, it based on a very simple principle - common sense.
    Along with basic common sense, we need to analyze few different factors like age of the investor, time horizon of investment, product credibility
    and the risk taking abilities to decide which scheme is suitable for the investor.
    ''')

    st.subheader('Thumb Rule #1 - Time')

    st.write('''
    Mutual funds work on CAGR or compounding basis, so the 1st thumb rule is that "Only time is your holy grail strategy".
        
    Holy grail strategy means a method or a strategy that can earn you exciting returns with minimal efforts. But unfortunately, 
    there is no such strategy in the markets, because if there was one, everyone would be rich.

    But as the mutual funds work on compounding basis, only investing for longer periods of time can earn you mind boggling returns.

    You can invest in any category such as large cap, mid cap, small cap or even multi cap, but if you do not hold your investment for a 
    good amount of time, it is sad to say but you will not see any exciting growth.

    For the exercise and assesment, you can use SIP calculator with different periods of time and see how investing for more time is boosting your investment returns multifold.

    Remember, "time in the market" will earn you more returns than "timing the market".
    ''')

    st.subheader('Thumb Rule #2 - Understand your specefics')

    st.write('''
    Know your age, time horizon and goal.

    Let me simplify these things for you with an example.
    My age is 25 years. I am working and saving money for my retirement which I assume is going to be at 60 years of age.
    So I have 35 years to invest for my GOAL of saving for my retirement.

    Suppose, my monthly expenses as of now are 30,000/- INR. I will calculate the future value of my monthly expenses adjusted for 6% inflation
    for when I will be 60 years of age, i.e. 35 years from now.

    That comes to be 2,30,583/- INR. You can calculate this using the future value calculator in quick tools section of this app.

    Now, my monthly expenses after 35 years will be 2,30,583/-. And suppose, I will live for more 20 years i.e. till 80 years of age.
    So, now, I will need around 5.5 crores to spend for my monthly expenses for 20 years after my retirement (20 years * 12 months each year * 2,30,583/- monthly expense = 5.5 crores).

    So, now as I am investing for a long period i.e. 35 years of time, I can invest in riskier funds like small cap fund as we don't have to worry about the volatility
    and the ups & downs of the market being the time of investment very long.

    Small cap funds can give you around 15-18% CAGR from what I have seen and with a monthly SIP of 3750/- INR for 35 years, you can gain a final amount of 5.57 crores in the end
    which is more than our target money. During these 35 years, you invested only 15,75,000/- INR (3750 * 35 * 12) and the rest is your gain.

    Exciting! isn't it? But this will only happen if your time period is a long one like in this case.

    Case 2, suppose you are saving for your child's MBA college fees which is going to be 20 years from here.
    MBA from IIM Kanpur costs around 25 lakhs as of today. But it will not be the same after 20 years, right?

    So let us calculate the future value for it. The future value after 20 years with 6% inflation will be 80,17,839/- INR.

    So, now you need 80 lakhs for the same MBA course. Yes that's how inflation works.

    But with a monthly SIP of 5300/- INR with 15% CAGR return in the same small cap fund for next 20 years, you can gain final amount of 80 lakhs.
    Here, you invested around 12.7 lakhs and the rest is your gain.

    But did you notice one thing?
    
    To earn 5.5 crores in 35 years, you needed an SIP of 3750/- per month.
    
    But to earn only 80 lakhs (which is more than 6 times smaller amount), you need an SIP 5300/- per month.

    So, I guess now you know how the compounding works.
    ''')

    st.subheader('Thumb Rule #3 - KISS (Keep It Simple Stupid)')

    st.write('''
    There are lot of complicated jargons and terminologies that sales people use to sell you products.
    But do you really need those products?

    In mutual funds too, as per my personal experience, there are so many categories which are not very useful to a long term investor.
    But the sales people try very hard to sell you those schemes because of their targets and incentives.

    So as a thumb rule, I personally avoid complex categories like Flexi Cap funds (launched recently) which I find to be
    a simple alternative to multi cap funds or the New Fund Offerings (NFOs) which are sold to a retail investor saying that a new fund comes at a face NAV of 10 rs
    and it is cheaper than existing funds in the market and thus has more potential than others, which is clearly not the case.

    You can also avoid funds with higher expense ratio because in the longer term, these expenses will eat up a HUGE portion of your returns and you can
    also stick to passively managed index funds and ETFs as a lot of funds do not even beat the benchmark.

    You should also avoid churning of funds to avoid expenses, taxes, etc and to keep the investment objective simple.

    And if you ever find youself stuck somewhere, do not take uncalculated decisions or risks and always take advice from your financial advisor.
    ''')

    st.subheader('Disclaimer')

    st.write('''We are not SEBI registered and this article/guide is only for educations purposes. This is not an investment advice and we will not be liable for 
    any profits or losses made by following the content in this article. Please consult your financial advisor before taking any investment decisions.
    
For any query, corrections or updations in this article, call us at +91-7276691545.
    ''')


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
