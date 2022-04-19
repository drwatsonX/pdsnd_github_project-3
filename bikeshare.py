import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    city = input('Enter the city you want see data for Chicago , New York City or Washington : ')
    #.casefold() method - https://www.programiz.com/python-programming/methods/string/casefold
    city = city.casefold()
    """ .casefold() is used for caseless matching, it ignores upper/lower cases when comparing."""
    while city not in CITY_DATA:
        city = input('Invalid city name.Please Try Again!')
        city = city.casefold()
        """ .casefold() is used in the loop in case first inputs are invalid, we want the matching to continue ignoring upper and lower cases."""


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter the month from January to June OR Enter "all" for no month filter : ')
    #.casefold() method - https://www.programiz.com/python-programming/methods/string/casefold
    month = month.casefold()
    """ .casefold() is used for caseless matching, it ignores upper/lower cases when comparing."""
    while month not in MONTH_LIST:
        month = input('Invalid month name.Please Try Again!')
        month = month.casefold()
        """ .casefold() is used in the loop in case first inputs are invalid, we want the matching to continue ignoring upper and lower cases."""


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day from Monday to Sunday OR Enter "all" for no day filter : ')
    #.casefold() method - https://www.programiz.com/python-programming/methods/string/casefold
    day = day.casefold()
    """ .casefold() is used for caseless matching, it ignores upper/lower cases when comparing."""
    while day not in DAY_LIST:
        day = input('Invalid day name.Please Try Again!')
        day = day.casefold()
        """ .casefold() is used in the loop in case first inputs are invalid, we want the matching to continue ignoring upper and lower cases."""


    print('='*50)
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
    # Loading data file into a dataframe.
    df = pd.read_csv(CITY_DATA[city])



    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])



    # Extracting month day and hour from Start Time to create new columns for further requests below
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour



    # Filtering by month if applicable
    if month != 'all':
        # Indexing of the MONTH_LIST to get corresponding int, no adjustment needed as [0] is associated with 'all', January starts at [1] 
        month = MONTH_LIST.index(month)

        # Filtering by month to create new dataframe
        df = df[df['month'] == month]



    # Filtering by day of week if applicable
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    
    # TO DO: display the most common month
    peak_month = df['month'].mode()[0]
    print("The most common month based on your selection: " + MONTH_LIST[peak_month].title())



    # TO DO: display the most common day of week
    peak_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week based on your selection: " + peak_day_of_week)



    # TO DO: display the most common start hour
    peak_start_hour = df['hour'].mode()[0]
    print("The most common start hour based on your selection: " + str(peak_start_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()



    # TO DO: display most commonly used start station
    # https://towardsdatascience.com/9-pandas-value-counts-tricks-to-improve-your-data-analysis-7980a2b46536 Pandas .value_counts() Method
    # https://www.w3schools.com/python/pandas/ref_df_idxmax.asp#:~:text=The%20idxmax()%20method%20returns,maximum%20value%20for%20each%20row.Pandas DataFrame .idxmax() Method
    # Taking a break from .mode() for a change by combining .value_counts() and .idxmax() --- Same results achieved
    print('Most commonly used Start Station: ', df['Start Station'].value_counts().idxmax())



    # TO DO: display most commonly used start station
    # https://towardsdatascience.com/9-pandas-value-counts-tricks-to-improve-your-data-analysis-7980a2b46536 Pandas .value_counts() Method
    # https://www.w3schools.com/python/pandas/ref_df_idxmax.asp#:~:text=The%20idxmax()%20method%20returns,maximum%20value%20for%20each%20row.Pandas DataFrame .idxmax() Method
    # Taking a break from .mode() for a change by combining .value_counts() and .idxmax() --- Same results achieved
    print('Most commonly used End Station: ', df['End Station'].value_counts().idxmax())



    # TO DO: display most frequent combination of start station and end station trip
    # pandas.DataFrame.nlargest - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html#pandas-dataframe-nlargest
    print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()



    # TO DO: display total travel time
    # Convert total travel time into weeks for ease of reference
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', int(Total_Travel_Time/604800), " Weeks")



    # TO DO: display mean travel time
    # Convert mean travel time into minutes for ease of reference
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', int(Mean_Travel_Time/60), " Minutes")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()



    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
    # https://towardsdatascience.com/9-pandas-value-counts-tricks-to-improve-your-data-analysis-7980a2b46536 Pandas .value_counts() Method
        user_types = df['User Type'].value_counts()
        print(user_types,'\n')
    else:
        print("No User Type data available based on your selection")
    



    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
    # https://towardsdatascience.com/9-pandas-value-counts-tricks-to-improve-your-data-analysis-7980a2b46536 Pandas .value_counts() Method    
        gender = df['Gender'].value_counts()
        print(gender,'\n')
    else:
        print("No Gender Type data available based on your selection")



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthyear = int(df['Birth Year'].min())
        most_recent_birthyear = int(df['Birth Year'].max())
        most_common_birthyear = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth out of all users based on your selection: {}\n'.format(earliest_birthyear))
        print('Most recent year of birth out of all users based on your selection: {}\n'.format(most_recent_birthyear))
        print('Most common year of birth out of all users based on your selection: {}\n'.format(most_common_birthyear))
    else:
        print("Some Birth Year data unavailable based on your selection")
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        #To prompt the user whether they would like want to see the raw data
        enter = ['yes','no']
        user_input = input('Would you like to see more data? (Enter:Yes/No).\n')

        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0
        while True :
            if user_input.lower() == 'yes':

                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break



        restart = input('\nWould you like to restart? (Enter:Yes/No).\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('BYE! or..... Apu would say Thank you Come Again!!!')
            break


if __name__ == "__main__":
	main()