import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data into a pandas DataFrame
data = pd.read_csv("bike_data.csv")

# Count the number of occurrences of each bike model
bike_counts = data["model"].value_counts()

# Convert to a new DataFrame
df_counts = pd.DataFrame({'model':bike_counts.index, 'count':bike_counts.values})

# Create a bar plot of the counts
sns.barplot(x='model', y='count', data=df_counts, order=df_counts.sort_values('count', ascending=False)['model'])

# Set labels and title for the plot
sns.set(rc={'figure.figsize':(10,8)})
sns.set_style("whitegrid")
sns.set_palette("bright")
sns.despine()
plt.xlabel('Bike Model')
plt.ylabel('Number of Bikes')
plt.title('Most Popular Bike Among All Bikes')
plt.show()
