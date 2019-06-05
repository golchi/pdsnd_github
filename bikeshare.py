import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def choose_city() :
    """
    Asks user to specify a city
    """
    while True:    
        print ('MENU - Choose a city')
        print ('- C: for Chicago')
        print ('- N: for New York')
        print ('- W: for Washington')
        name = input("Enter your choice: ")
        name = name.upper()
        if name == 'C':
            city = 'chicago'
        elif name == 'N':
            city = 'new york city'
        elif name == 'W':
            city = 'washington'        
        if name  in ['C','N','W']:
            break           
    return city


def choose_month() :
    """
    Asks user to specify a month
    """
    while True:    
        print ('Enter "all" to skip month filtering or enter a digit 1-January .. to .. 12- December')
        m_input = input("Enter your choice: ")
        m_input = m_input.lower()
        month = ''
        if m_input == 'all':
            month = 'all'
        else:
            try: 
                m_input = int(m_input)
            except:
                print ('Invalid value, try again')      
                m_input = 0      
            if(1 <= m_input <= 12):
                month = m_input     
        if month != '':
            break           
    return month


def choose_day() :
    """
    Asks user to specify a day
    """
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:    
        print ('Enter "all" to skip day filtering or enter the day (monday..sunday)')
        d_input = input("Enter your choice: ")
        d_input = d_input.lower()
        day = ''
        if d_input == 'all':
            day = 'all'
        elif d_input in days:
            day = d_input     
        if day != '':
            break           
    return day


def get_filters():
    """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = choose_city()

    # get user input for month (all, january, february, ... , june)
    month = choose_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = choose_day()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = 'data/'+ CITY_DATA[city]

    # load data file into a dataframe
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable to create the new dataframe
    if month != 'all':
        df = df[df['month'] == month]

    # filter by day of week if applicable to create the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df): 
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    
    # display the most common month
    print ('Most common month: ',popular_month)

    # display the most common day of week
    print ('Most common day of week: ', popular_day)
    
    # display the most common start hour
    print ('Most common hour: ', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    
    popular_combination = df.groupby(['Start Station','End Station']).size().idxmax()

    # display most commonly used start station
    print ('Most commonly used start station: ',popular_start_station)

    # display most commonly used end station
    print ('Most commonly used end station: ',popular_end_station)

    # display most frequent combination of start station and end station trip
    print ('Most frequent combination of start station and end station trip: ',popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time : ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time : ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('User types stats')
    for u_type, u_type_count in user_types_count.items():
        print(u_type,' -', u_type_count)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('Gender : ', gender_count)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode())
        print('Earliest year of birth: ', earliest_year)
        print('Most recent year of birth:', most_recent_year)
        print('Most common year of birth:', most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart ? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    