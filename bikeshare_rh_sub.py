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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('What city would you like to filter by: \n (Chicago, New York City or Washington)\n').lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('Sorry, I have no data for that input. Please select from the list of cites')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('What month would you like to filter by: \n (January, February, March, April, May, June or all)\n').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print('Sorry, I have no data for that input. Please select from the list of months')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('What day would you like to filter by: \n (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all)\n').lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all'):
            break
        else:
            print('Sorry, I have no data for that input. Please select from the list of days')

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
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0] - 1
    print('The most common month Bikeshare is used to travel is {}'.format(most_common_month))

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day Bikeshare is used to travel is {}'.format(most_common_day))

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour Bikeshare is used to travel is {}:00'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_station = df['Start Station'].mode()[0]
    print('The most common starting station is {}'.format(most_common_station))

    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print()
    print('The most common ending station is {}'.format(most_common_end))

    # display most frequent combination of start station and end station trip
    df['combo_station'] = df['Start Station'] + '||' + df['End Station']
    most_common_combo = df['combo_station'].mode()[0]
    print()
    print('The most common route is {}'.format(most_common_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total time traveled is {}'.format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print()
    print('The average time traveled is {}'.format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    total_user = df['User Type'].value_counts()
    print('The total number of users were {}'.format(total_user))
    print()

    # Display counts of gender
    if'Gender' in df.columns:
        gender = df['Gender']
        gender_count = gender.value_counts()
        print('Gender Distribution:\n{}'.format(gender_count))
        print()
    else:
        print('Gender data is not available')
        print()


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        common_birth_year =df['Birth Year'].mode()[0]
        print('The youngest user was born in {}'.format(earliest_birth_year))
        print('The oldest user was born in {}'.format(latest_birth_year))
        print('The most common Birth Year of all users is {}'.format(common_birth_year))
    else:
        print('Birth year data is not available')


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

# Course tutor assisted with this code via submission feedback

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
