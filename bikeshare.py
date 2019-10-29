# First for Loading Time
import time

# Second for Loading Pandas
import pandas as pd

# Defining Data Files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Defining Cities Names
CITIES = ['chicago', 'new york', 'washington']

# Defining Months Names
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

# Defining Days Names
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday', 'all' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data in an interactive way!')

    while True:
       city = input('Choose a city to explore like (chicago, new york or washington? \n> ').lower()
       if city in CITIES:
           break
    while True:      
       month = input('Please provide a month name like the following (e.eg. january, february, ... , june) or \"all" for all months data \n> ').lower()
       if month in MONTHS:
           break
    while True:    
       day = input('Please provide a week day, (e.g. monday, sunday) or all for all days data \n> ').lower()
       if day in DAYS:
           break
        
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
        
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Displaying the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)
    
    # Displaying the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)
    
    # Display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nWait Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displaying most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    # Displaying most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    # Displaying most frequent combination of start station and end station trip    
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nNOTE: This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displaying total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # Display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displaying counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    print()
    
    if 'Gender' in df.columns:
        user_gender(df)

    if 'Birth Year' in df.columns:
        user_birth(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_gender(df):
    """Displays statistics of analysis based on the gender of bikeshare users."""

    # Displaying counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    for index,gender_count   in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))
  
    print()
def user_birth(df):
    """Displays statistics of analysis based on the birth years of bikeshare users."""

    # Displaying earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # Displaying the most common birth year
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    # Displaying the most recent birth year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # Displaying the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)
 
def display_five(df):
    """" Displaying 1st five lines of row data if the user need to see."""
    
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    start = 0
    end = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view row data in this screen? enter "yes" or "no" \n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print('Please type "yes" or "no".')
            
    if display.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[start:end])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more raw data in this screen? enter "yes" or "no".\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print('Please type "yes" or "no"')
            if display_more.lower() == 'yes':
                start += 5
                end += 5
                print(df[df.columns[0:-1]].iloc[start:end])
            elif display_more.lower() == 'no':
                break
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_five(df)
        
        restart = input('\n would you like to restart the process from the beggining? enter "yes" or any other word to close.\n').lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
