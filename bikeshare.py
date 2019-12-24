import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
filters = ['month', 'day', 'none']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:  
        try:
            city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n\n").lower()
            if city in cities:
                print('\nYou have entered {}!!\n'.format(city.title()))
                break
            else:
                print('\nYou have entered invalid city, please try again!\n\n')
        except:
            print('Your city entry caused an error, exiting program!!\n\n')
            break
            
    while True:
        try:
            month_or_day = input("\nWould you like to filter the data by month, day, or not at all? Enter \'None\' for not at all!\n\n").lower()
            if month_or_day in filters:
                break
            else:
                print('\nYou have entered invalid filters, please try again!\n\n')
        except:
            print('Your filter entry caused an error, exiting program!!\n\n')
            break
# TO DO: get user input for month (all, january, february, ... , june)            
    if month_or_day == filters[0]:
        day = 'all'
        while True:
            try:
                month = input("\nWhich month - January, February, March, April, May, or June? Enter the full month!\n\n").lower()
                if month in months:
                    break
                else:
                    print('\nYou have entered invalid month, please try again!\n\n')
            except:
                print('Your month entry caused an error, exiting program!!\n\n')
                break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif month_or_day == filters[1]:
        month = 'all'
        while True:  
            try:
                day = input("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Enter the day fully!\n\n").lower()
                if day in days:                  
                    break
                else:
                    print('\nYou have entered invalid day, please try again!\n\n')
            except:
                print('Your day entry caused an error, exiting program!!\n\n')
                break
                
    else:
        month = 'all'
        day = 'all'

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
       # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    
    print('Most Common Month:', months[popular_month].title())    
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:{}:00Hours'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # The most commonly used start station using mode function
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    # The most commonly used end station using mode function
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['SS_ES'] = df['Start Station'] + ',' + df['End Station']
    popular_SS_ES = df['SS_ES'].mode()[0]
    popular_SS = popular_SS_ES.split(',')[0]
    popular_ES = popular_SS_ES.split(',')[1]
    
    print('\nMost Frequent Combination of Start Station and End Station Trip:')
    print('Start Station:',popular_SS)
    print('End Station:',popular_ES)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time:',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The mean travel time:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of different user types: \n',user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\n\nThe counts of different genders: \n\n',gender)
    else:
        print('\nNo Gender Data is available!\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth: ',earliest_yob)
        print('The most recent year of birth: ',most_recent_yob)
        print('The most common year of birth: ',most_common_yob)
    else: 
        print('No Birth Year Data is available!\n')
        

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
        """This section will ask the user if they want to see 5 rows of raw data and repeat display 5 lines of additional data at a time!"""
        try:
            display_data = input('\n Would you like to see first 5 rows of data? Type yes or no!\n')
            for i in range (0, df.shape[0], 5):
                if display_data.lower() == 'yes':
                    print(df.iloc[i:i+5,0:9])
                else:
                    break
                display_data = input('\nWould you like to see 5 more rows of data? Type yes or no!\n')      
        except:
            print('Your entry caused an error, exiting the program')
            break
            
        """This section will ask the user if they want to restart the whole program!"""    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
