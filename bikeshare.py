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
    while True:    
        print ('Enter "all" to skip day filtering or enter a digit 1 to 31')
        d_input = input("Enter your choice: ")
        d_input = d_input.lower()
        day = ''
        if d_input == 'all':
            day = 'all'
        else:
            try: 
                d_input = int(d_input)
            except:
                print ('Invalid value, try again')      
                d_input = 0      
            if(1 <= d_input <= 31):
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
    filename = 'data/'+ city + '.csv'

    # load data file into a dataframe
    df = pd.read_csv(filename)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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
	#main()
    load_data('chicago', '2', '2')
