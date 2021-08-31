import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month = "all"
day = "all"
city = ""
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    month ="all"
    day ="all"
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
            assert (city=='chicago' or city == 'new york' or city == 'washington' or city =="new york city")
            if city == 'new york':
                city = "new york city"
            break
        except:
            print("Please, enter a valid city")

    while True:
        try:
            filter = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter ' ).lower()
            assert (filter == "month" or filter=="day" or filter=="both" or filter=="none")
            break
        except:
            print('Please, choose "month", "day", "both" or "none"!')




    # TO DO: get user input for month (all, january, february, ... , june)
    if filter == "month" or filter =="both":
        while True:
            try:
                month = input('Which month - January, February, March, April, May, or June? ' ).lower()
                assert (month in months)
                break
            except:
                print('Please, choose "January", "February", "March", "April", "May", or "June"! ')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter == "day" or filter =="both":
        while True:
            try:
                day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
                assert (day in days)
                break
            except:
                print('Please, choose "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", or "Sunday"')


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

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
    if  month == "all":
        popular_month = df['month'].mode()[0]
        count = df[df['month']==popular_month].count()[0]
        print("Most popular month: {}, Count: {}, Filter: {} ".format(months[popular_month-1].title(),count,filter))

    # TO DO: display the most common day of week
    if day == "all":
        popular_day = df['day_of_week'].mode()[0]
        count = df[df['day_of_week']==popular_day].count()[0]
        print("Most popular day of week: {}, Count: {}, Filter{}".format(popular_day,count,filter))

    # TO DO: display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour.mode()[0]
    count = df[df['Start Time'].dt.hour==popular_start_hour].count()[0]
    print("Most popular hour: {}, Count: {}, Filter: {}".format(popular_start_hour,count,filter))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    comman_start_station = df['Start Station'].mode()[0]
    count1 = df[df['Start Station']==comman_start_station].count()[0]
    print("Most popular start station: {}, Count: {} , Filter: {}".format(comman_start_station, count1, filter))


    # TO DO: display most commonly used end station
    comman_end_station = df['End Station'].mode()[0]
    count2 =  df[df['End Station']==comman_end_station].count()[0]
    print("Most popular end station: {}, Count: {} , Filter: {}".format(comman_end_station, count2, filter))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip
    print("\nCalculating Most Common Trip...\n")
    start_time = time.time()
    most_common_trip = df.groupby(['Start Station','End Station']).size().idxmax()
    count3 = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)[0]
    print("Most popular trip: {}, count: {}, filter: {}".format(most_common_trip, count3,filter))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =df['Trip Duration'].sum()
    total_trips = df.count()[0]

    # TO DO: display mean travel time
    average_trip = df['Trip Duration'].mean()
    print("Total distance traveled: {}, Total trips: {}, Average Trip duration: {}, Filter: {}".
    format(total_travel_time, total_trips, average_trip, filter))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    city
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Types...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print ("Number of subscribers: {}, filter: {}".format(user_types['Subscriber'], filter))
    print ("Number of users: {}, filter: {}".format(user_types['Customer'],filter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display counts of gender
    if (city !="washington"):
        print('\nCalculating Gender...\n')
        start_time = time.time()
        Gender = df.groupby(['Gender'])['User Type'].count()
        print ("Number of Female: {}, filter: {}".format(Gender['Female'],filter))
        print ("Number of Male: {}, filter: {}".format(Gender['Male'], filter))
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print("No Gender data to share ;)")
    print('-'*40)


    # TO DO: Display earliest, most recent, and most common year of birth
    if (city !="washington"):
        start_time = time.time()
        birth_year = df['Birth Year']
        print("The youngest birth year: {}". format(birth_year.max()))
        print("The oldest birth year: {}".format(birth_year.min()))
        print("Most popular birth year: {}".format(birth_year.mode()[0]))
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print("Also no birth year data. (Y)")
    print('-'*40)


def main():

    while True:
        global city
        global month
        global day
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show = input('\nWould you like to see raw data? Enter yes or no.\n')
        whereat = 0
        maxsize=(len(df.index)-1)
        while True:
            if show.lower() == 'yes':
                if whereat<maxsize-5:
                    print(df[whereat:whereat+5])
                    whereat+=5
                    show = input('\nWould you like to see more raw data? Enter yes or no.\n')
                else:
                    print(df[whereat:maxsize+1])
                    break
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
