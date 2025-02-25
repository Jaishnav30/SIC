import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Engineering_Branch_Analytics.csv")
df2 = pd.read_csv("job_growth_by_branch.csv")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SECTION-1
# Which branch offers the best option for students seeking both stability and innovation? (Compare job market stability, emerging technologies, and startups in the field)

df["Sum"] = df["Startups in the Field"].values + df["Emerging Technologies"].apply(lambda x: len(x.split(',')))

tech_list = list(df["Emerging Technologies"].apply(lambda x: len(x.split(','))))

max_row = df[df["Sum"] == df["Sum"].max()]
result_branch = max_row["Branch Name"].values[0]

print(result_branch, "is the branch that offers the best option for students seeking both stability and innovation.")

x = np.arange(len(df.index))
width = 0.35

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, df['Startups in the Field'], width, color='red', edgecolor='black', label='Startups in the Field')
bars2 = ax.bar(x + width/2, tech_list, width, color='yellow', edgecolor='black', label='Emerging Technologies')

ax.bar_label(bars1, labels=[f'{v}%' for v in df["Startups in the Field"]], padding=3)  # Append '%'
ax.bar_label(bars2, labels=[f'{v} tech' for v in tech_list], padding=3)  # Append 'technologies'
ax.legend()
ax.set_xticks(x)
ax.set_xticklabels(df["Branch Name"])

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SECTION-2
# Growth rate of each Engineering Branch from 2010 to 2024 

df2.set_index('Year', inplace=True)
df2.transpose().plot(marker='o')
plt.xlabel('Year')
plt.ylabel('Number of People (Crores)')
plt.title('Job Growth by Branch (2010-2024)')
plt.legend(title='Branch')
plt.grid(True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SECTION-3
# Pie chart distribution of students enrolling into specific branches

fig = plt.figure(figsize=(10, 7))
val_list = df["Students Enrolled"].values
plt.pie(val_list, labels=df["Branch Name"], autopct='%1.1f%%', startangle=100)
plt.title('Student Enrollment in particular Branches (in %)')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------