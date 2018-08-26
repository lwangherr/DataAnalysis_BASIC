import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for city ?(chicago, new york city, washington)').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("You must input one of these options:chicago, new york city, washington! Please try again\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march' , 'april', 'may', 'june']
    while True:
        month = input('Would you like to filter data by month? (Type like all, january, february, ... , june)').lower()
        if month in months:
            break
        else:
            print("You must input one of these options:all, january, february, ... , june! Please try again\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('Would you like to filter data by day?(Type like all, monday, tuesday, ... sunday)').lower()
        if day in days:
            break
        else:
            print("You must input one of these options:all, monday, tuesday, ... sunday! Please try again\n")
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
    #filename = ' '.join(city.split(' '))
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_weekday'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
      months = ['january', 'february', 'march' , 'april', 'may', 'june']
      month = months.index(month) + 1
      df = df[df['month'] == month]
      
    if day != 'all':
      monthdf = df[df['day_of_weekday'] == day.title()]
      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
	
    # TO DO: display the most common month
    months = ['january', 'february', 'march' , 'april', 'may', 'june']
    most_month = pd.to_datetime(df['Start Time']).dt.month.value_counts().idxmax()
    print("The Most Frequent Month of Travel is :{}".format(months[most_month - 1]))

    # TO DO: display the most common day of week
    most_day_of_week = pd.to_datetime(df['Start Time']).dt.weekday_name.value_counts().idxmax()
    print("The Most Frequent Day of Week of Travel is :{}".format(most_day_of_week))

    # TO DO: display the most common start hour
    most_hour = pd.to_datetime(df['Start Time']).dt.hour.value_counts().idxmax()
    print("The Most Frequent Hours of Travel is :{}".format(most_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print("The Most Popular Start Station is: {}".format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print("The Most Popular End Station is: {}".format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_combine_station = (df['Start Station']+ ' to ' + df['End Station']).value_counts().idxmax()
    print("The Most Popular Start Station and End Station trip is: {}".format(most_combine_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is : {}".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time is : {}".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print('The counts of user types is:\n{}'.format(counts_of_user_type))

    try:
        counts_of_gender = df['Gender'].value_counts()
        print('The counts of gender is:\n{}'.format(counts_of_gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print('The earliest, most recent, and most common year of birth respectively is:{},{},{}'.format(earliest_year_of_birth,most_recent_year_of_birth,most_common_year_of_birth))
    except KeyError:
        print("This city have no data about 'Gender' and 'Birth Year'")
    finally:
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    # print(pd.read_csv(CITY_DATA['chicago']).colums())
    # print(pd.read_csv(CITY_DATA['new york city']).head())
    # print(pd.read_csv(CITY_DATA['washington']).head())

if __name__ == "__main__":
	main()
