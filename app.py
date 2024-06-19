import streamlit as st
import pickle
import pandas as pd

# Setting the background image
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://static.theprint.in/wp-content/uploads/2023/11/IMG_1019-min-scaled-e1700672378753.jpeg");
        background-size: cover;
    }
    .prediction {
        font-size: 24px;
        font-weight: bold;
        color: white;
        padding: 10px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        text-align: center;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Delhi Capitals',
    'Punjab Kings',
    'Chennai Super Kings',
    'Rajasthan Royals'
]

cities = [
    'Chennai', 'Bangalore', 'Delhi', 'Durban', 'Chandigarh',
    'Ahmedabad', 'Jaipur', 'Visakhapatnam', 'Hyderabad', 'Mumbai',
    'Kolkata', 'Cape Town', 'Pune', 'Nagpur', 'Kimberley',
    'Johannesburg', 'Mohali', 'Sharjah', 'Port Elizabeth', 'Centurion',
    'Abu Dhabi', 'Bengaluru', 'Bloemfontein', 'Raipur', 'Ranchi',
    'Dharamsala', 'Indore', 'Cuttack', 'East London'
]

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Win Predictor')

# Sidebar for team selection with dynamic filtering
st.sidebar.header('Select Teams')

# Initially set batting_team and bowling_team to None
batting_team = None
bowling_team = None

# Team selection logic
if 'batting_team' not in st.session_state:
    st.session_state.batting_team = 'Select Team'
if 'bowling_team' not in st.session_state:
    st.session_state.bowling_team = 'Select Team'

if st.sidebar.selectbox('First Select', ['Batting Team', 'Bowling Team']) == 'Batting Team':
    batting_team = st.sidebar.selectbox('Select Batting team', ['Select Team'] + sorted(teams))
    if batting_team != 'Select Team':
        st.session_state.batting_team = batting_team
        bowling_team_options = [team for team in sorted(teams) if team != batting_team]
        bowling_team = st.sidebar.selectbox('Select Bowling team', ['Select Team'] + bowling_team_options)
        if bowling_team != 'Select Team':
            st.session_state.bowling_team = bowling_team
else:
    bowling_team = st.sidebar.selectbox('Select Bowling team', ['Select Team'] + sorted(teams))
    if bowling_team != 'Select Team':
        st.session_state.bowling_team = bowling_team
        batting_team_options = [team for team in sorted(teams) if team != bowling_team]
        batting_team = st.sidebar.selectbox('Select Batting team', ['Select Team'] + batting_team_options)
        if batting_team != 'Select Team':
            st.session_state.batting_team = batting_team

# Main Page Inputs
st.header('Match Details')
selected_venue = st.selectbox('Select Stadium', sorted(cities))
Target = st.number_input('Target to Chase')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Runs Scored')
with col4:
    overs = st.number_input('Overs Bowled')
with col5:
    wickets = st.number_input('Wickets Fallen')

if st.button('Predict'):
    if st.session_state.batting_team == 'Select Team' or st.session_state.bowling_team == 'Select Team':
        st.error("Please select both batting and bowling teams.")
    else:
        # Calculation of runs_required
        runs_left = Target - score

        # Calculation of balls_left (10.5 = 10 overs + 5 balls)
        balls_left = 120
        if 1 <= (overs * 10) % 10 <= 5:
            balls_left -= ((overs * 10) % 10) + ((overs * 10) // 10) * 6
        else:
            balls_left = (120 - overs * 6)

        # Calculation of wickets_left
        wickets_left = 10 - wickets

        # Current run rate calculation
        if overs > 0:
            crr = score / overs
        else:
            crr = 0

        # Required run rate calculation
        if balls_left > 0:
            overs_left = balls_left / 6
        else:
            overs_left = 0

        if overs_left > 0:
            rrr = runs_left / overs_left
        else:
            rrr = runs_left

        input_df = pd.DataFrame({
            'batting_team': [st.session_state.batting_team],
            'bowling_team': [st.session_state.bowling_team],
            'city': [selected_venue],
            'runs_required': [runs_left],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'rrr': [rrr],
        })

        # Display result
        try:
            result = pipe.predict_proba(input_df)
        except Exception as e:
            st.error(f"Error during prediction: {e}")

        bowling_team_win_percent = result[0][0] * 100
        batting_team_win_percent = result[0][1] * 100

        st.header('Win Prediction:')
        col6, col7 = st.columns(2)

        with col6:
            st.markdown(
                f'<div class="prediction">{st.session_state.batting_team}<br>{round(batting_team_win_percent, 2)}%</div>',
                unsafe_allow_html=True
            )
        with col7:
            st.markdown(
                f'<div class="prediction">{st.session_state.bowling_team}<br>{round(bowling_team_win_percent, 2)}%</div>',
                unsafe_allow_html=True
            )
