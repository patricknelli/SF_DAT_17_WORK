'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to
import pylab as plt

killings = pd.read_csv('data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)
killings.head()

# 2. Show the count of missing values in each column

killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"

killings.fillna("Unknown", inplace = True)

# 4. How many killings were there so far in 2015?

killings[killings.year == 2015].shape[0]

# 5. Of all killings, how many were male and how many female?

killings.gender.value_counts()

# 6. How many killings were of unarmed people?

#answer 
killings[killings.armed == 'No'].shape[0]

#NOTE - there are other categories (e.g. other, unknown, etc.) that I excluded 
killings.armed.value_counts()

# 7. What percentage of all killings were unarmed?
percentage = killings[killings.armed == 'No'].shape[0] * 100 / float(killings.shape[0])
print "%.2f percent of all killings were unarmed" % percentage

# 8. What are the 5 states with the most killings?

#answer with counts of each of top 5 states
killings.state.value_counts(sort = True, ascending = False).head(5)

#state text answer
killings.state.value_counts(sort = True, ascending = False).head(5).index

# 9. Show a value counts of deaths for each race
killings.race.value_counts()

# 10. Display a histogram of ages of all killings

killings.age.hist()
plt.suptitle("Count of Killings by Age Group")
plt.xlabel("Age")
plt.ylabel("Count of Killings")
plt.show();

# 11. Show 6 histograms of ages by race

killings.age.hist(by = killings.race, sharex = True, sharey = True)
plt.suptitle("Count of Killings by Age Group by Race")
plt.show();

# 12. What is the average age of death by race?

killings.age.groupby(killings.race).mean()

# 13. Show a bar chart with counts of deaths every month

months = ['January','February','March','April','May','June']
killings.month = pd.Categorical(killings.month, months)
killings.month.value_counts(sort = False).plot(kind='bar')


###################
### Less Morbid ###
###################

majors = pd.read_csv('data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)

del majors['Employed_full_time_year_round']
del majors['Major_code']
majors.head()

# 2. Show the cout of missing values in each column

majors.isnull().sum()

# 3. What are the top 10 highest paying majors?

#based on median salaries, with Median salary shown
majors[['Major', 'Median']].sort(columns = 'Median', ascending = False).head(10).set_index('Major')

#simple list of majors
majors[['Major', 'Median']].sort(columns = 'Median', ascending = False).Major.head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!

majors[['Major', 'Median']].sort(columns = 'Median', ascending = False).head(10).set_index('Major').plot(kind='bar')
plt.title("Median Salary by Major")
plt.xlabel("Major")
plt.ylabel("Median Salary")
plt.show();


# 5. What is the average median salary for each major category?

majors.groupby('Major_category').Median.mean()

# 6. Show only the top 5 paying major categories

majors.groupby('Major_category').Median.mean().order(ascending = False).head(5)

# 7. Plot a histogram of the distribution of median salaries

majors.Median.hist()
plt.title("Median Salary Count For All Majors")
plt.xlabel("Median Salary")
plt.ylabel("Major Count")
plt.show();

# 8. Plot a histogram of the distribution of median salaries by major category

#Is this what they want?  
majors.groupby('Major_category').Median.mean().hist()
plt.title("Count by Average Median Salary for Each Major Category")
plt.xlabel("Average Median Salary by Major Category")
plt.ylabel("Major Category Count")
plt.show();

#or something like this?
majors.Median.hist(by = majors.Major_category, sharex = True, sharey = True, bins=10)

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?
majors[['Major', 'Unemployment_rate']].sort(columns = 'Unemployment_rate', ascending = False).head(10).set_index('Major')

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?

majors.groupby('Major_category').Unemployment_rate.mean().order(ascending = False).head(10)

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

majors['sample_employment_rate'] = majors.Employed / majors.Total
majors.head(10)

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"

majors['sample_unemployment_rate'] = 1- majors.sample_employment_rate
majors.head(10)
