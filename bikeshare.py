import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv', 'chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv', 'new york city': 'new_york_city.csv',
             'Washington': 'washington.csv', 'washington': 'washington.csv'}

MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'no filter': 7}

DAY_DATA = ['no filter', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None.
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "none" to apply no month filter was selected
        str (day): name of the day of week to filter by, or "none" to apply no day filter was selected
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Initializing an empty city variable to store city choice from user
    # You will see this repeat throughout the program
    city = ''
    # Running this loop to ensure the correct user input gets selected else repeat
    while city not in CITY_DATA.keys():
        print("\nPlease Select a City from the following options: ")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nAccepted input:\nFull name of city; please use the name formats - (Chicago or chiacgo).")
        # Taking user input and converting into lower to standardize them
        # You will find this happening at every stage of input throughout this
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nPlease check your input, it does not match any accepted input formats for this program.")
            print("\nRebooting...")

    print(f"\n Selected City : {city.title()}.")

    # Creating a dictionary to store all the months including the 'all' option
    month = ''
    while month not in MONTH_DATA:
        print("\nPlease select a month between January to June:")
        print("\nAccepted input:\n Please use the following format - (january or JANUARY).")
        print("\n(To select all months, please type No Filter.")
        month = input().lower()

        if month == 'no filter':
            print("\nYou have selected to not filter by a month.")
            print("\nLoading...")
        elif month not in MONTH_DATA:
            print("\nInvalid input, please select an accepted input value.")
            print("\nRebooting...")
    print(f"\n Selected month: {month.title()}.")

    # Creating a list to store all the days including the 'all' option
    day = ''
    while day not in DAY_DATA:
        print("\nPlease select a day between Sunday - Saturday.")
        print("\nPlease type 'no filter' to select all days.")
        day = input().lower()

        if day in DAY_DATA:
            print(f"\n Selected day: {day.title()}.")
        elif day == 'no filter':
            print("\nYou have selected to not filter by a day.")
            print("\nLoading...")
        else:
            print("\nInvalid input. Please try again using an accepted integer value.")
            print("\nRebooting...")

    if month == 'no filter':
        print(f"\nLoading data for City: {city.title()}, No Month was Selected and Day: {day.title()}.")
    elif day == 'no filter':
        print(f"\nLoading data for City: {city.title()}, Month: {month.title()} and No Day was Selected.")
    else:
        print(f"\nLoading data for City: {city.title()}, Month: {month.title()} and Day: {day.title()}.")

    print('-' * 40)
    # Returning the city, month and day that were selected by user input
    return city, month, day

# Function to load data for city, month, and day that was selected from user input.
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "no filter" to apply no month filter
        (str) day - name of the day of week to filter by, or "no filter" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day that was selected unless no filter was choosed.
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns in the df named month and day of the week.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'no filter':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'no filter':
        # Filter by day of week to create the new dataframe.
        df = df[df['day_of_week'] == day.title()]

    # Returns the selected file as a dataframe (df) with relevant columns
    return df
# Function to calculate the statistics regarding time from the selected data.
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame that was selected by the user input.
    Returns:
        None.
    """

    print('\nCalculating Time Statistics from the Selected Data...\n')
    start_time = time.time()

    #Mode method will allow to find the most popular month from the month column in the df.
    popular_month = (df['month'].mode()[0])

    print(f"Most Popular Month (1 = January,...,6 = June): {popular_month}")

    #Mode method will allow to find the most popular day from day of the week column in the df.
    popular_day = (df['day_of_week'].mode()[0])
    print(f"\nMost Popular Day: {popular_day}")

    # Extract hour from the Start Time column to create an hour column in the df.
    df['hour'] = df['Start Time'].dt.hour

    #Mode method will allow to find the most popular hour using the new column created in the df.
    popular_hour = (df['hour'].mode()[0])

    print(f"\n Most Popular  Hour: {popular_hour}")

    # Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-' * 40)

#Function to calculate the statistics for the stations.
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame that was selected by the user input.
    Returns:
        None.
    """

    print('\nCalculating Stations Statistics from the Selected Data...\n')
    start_time = time.time()

    # display most commonly used start station
    #Mode method will allow to find the most common value from the column.
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}.")

    # display most commonly used end station
    #Mode method will allow to find the most common value from the column.
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station: {common_end_station}.")

    #Str.cat will allow to combine the two columns (Start Station & End Station) in the df.
    #This will allow the two columns to be combined to a new column in the df named 'Combo of Start & End Stations.'
    df['Combo of Start & End Stations'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    #Mode method will allow to find the most frequent combination used of start and end stations.
    frequent_combo = df['Combo of Start & End Stations'].mode()[0]

    print(f"The most common combination of start and end stations: {frequent_combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Function for trp duration statistics.
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n...Calculating Trip Duration Statistics from the Selected Data...\n')
    start_time = time.time()

    # displaying total travel time, using the sum method on the column 'Trip Duration' from the dataframe to
    # calculate the total travel time.
    total_travel_time = df['Trip Duration'].sum()
    # calculate the total travel time in minutes and seconds format
    minute, second = divmod(total_travel_time, 60)
    # calculate the total travel time in hour and minutes formats
    hour, minute = divmod(minute, 60)
    print(f"The total travel time is {hour} hours, {minute} minutes and {second} seconds.")

    # displaying mean travel time using the mean method on the column 'Trip Duration' from the dataframe to calculate
    # the mean travel time and the number will be rounded due to the round method provided after.
    avg_travel_time = round(df['Trip Duration'].mean())
    # calculate the average travel time in minutes and seconds formats
    mins, secs = divmod(avg_travel_time, 60)
    #calculates the time in hours, mins, secs format if the mins exceed 60 minutes
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average travel time is {mins} minutes and {secs} seconds.")
    else:
        print(f"\nThe average travel time is {mins} minutes and {secs} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Function to calculate user statistics.
def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame that was selected by the user input.
    Returns:
        None.
    """

    print('\n...Calculating User Statistics from the Selected Data...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Number of user types are: {user_types}.")

    # Display counts of gender implemented a try and except block here to print out the count of gender if the file
    # has a "Gender" column, otherwise it will indicate no gender data is available in the file.
    try:
        gender = df['Gender'].value_counts()
        print(f"Number of gender are: {gender}.")
    except:
        print("There is no data for gender available in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year is: {earliest_birth_year}\n\nThe most recent birth year is: {recent_birth_year}\n\nThe most common birth year is: {common_birth_year}")
    except:
        print("There is no data for birth year available in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

# Function to display the data frame itself as per user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
    param1 (df): The data frame that the user selects to work with.
    Returns: None."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Created a list that contains yes and no which will be the response to view raw data from the input of the user.
    response_to_display = ['yes', 'no']
    responsedata = ''
    #Added a counter variable to ensure the raw data comes from a set point when displayed.
    counter = 0
    while responsedata not in response_to_display:
        print("\nWould you like to view the raw data from selected csv file?")
        print("\nPlease type 'yes' or 'no'")
        responsedata = input().lower()
        # responsedata will input user's response and added the lower method just in case the user's response does not match the values from response_to_display list.
        if responsedata == 'yes':
            print(df.head())
            # if statement will run if user response is yes to the question which will display the first five rows of data from the columns in the csv file due to the head method for Panda dataframes.
        elif responsedata not in responsedata:
            print("\nResponse is invalid, please try again using an accepted response.")
            print("\nRebooting...")

    # added a while loop in the script so user can keep viewing more data from the file at a rate of five rows if they choose to.
    while responsedata == 'yes':
        print("Would you like to view more data from the csv file?")
        #Counter variable is set to 0 and here we add five so everytime the user inputs to view more data, only 5 more rows will display.
        counter += 5
        responsedata = input().lower()

        #If user inputs yes then 5 more rows of raw data will display.
        if responsedata == 'yes':
            print(df[counter:counter + 5])
        #if user input does not equal yes then no more raw data will display and the while loop breaks.
        elif responsedata != 'yes':
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Main function to call all functions in the program.
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #order the functions will be called in the program.
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        #After all functions run, user can input yes to restart the program or no to end the program from running.
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
