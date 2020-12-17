import pandas as pd
pd.set_option('display.max_colwidth', -1)

# load data and investigate it
jeopardy_data = pd.read_csv('jeopardy.csv')
# print(jeopardy_data.columns)

# rename misformatted columns
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
#print(jeopardy_data.columns)
#print(jeopardy_data['Question'])

# filtering a dataset by a list of words
def filter_data(data, words):
  # lowercases the words that appear in the list as well as in the questions. Returns true if all of the words in the list appear in the questions
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # applies the lambda function to the question column and returns rows where the function returned true
  return data.loc[data['Question'].apply(filter)]
# test the filter function
filtered = filter_data(jeopardy_data, ['King', 'England']) 
####print(filtered['Question']) 

# Add a new column to compute aggregate stats on the Value column. New column should have float data. If the value is currently not "None", cut of $ sign, replace commas with nothing and cast the value as a float. Alternatively, if it was "None", cast that value as a 0
jeopardy_data['Float Value']  = jeopardy_data['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)

# Filtering the dataset and finding the average value of those questions
filtered = filter_data(jeopardy_data, ["King"])
####print(filtered["Float Value"].mean())

# define a function to find the number of unique answers to a set of data
def get_answer_counts(data):
  return data['Answer'].value_counts()
# Testing the answer count function
print(get_answer_counts(filtered))
