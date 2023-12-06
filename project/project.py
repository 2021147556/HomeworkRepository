import pandas as pd
import matplotlib.pyplot as plt

# Read data from a CSV file
df = pd.read_csv('Survey_AI.csv')
print(df.head())

# Remove rows with missing values
df.dropna(inplace=True)
# Demove columns are not utilized
# Keep only the necessary columns
columns_to_keep = ['Q1.AI_knowledge', 'Q15.Passed_exams', 'Q16.GPA']
df = df[columns_to_keep]

# Display the processed dataset
print(df.head())


# Create two subsets: one for students who participated in AI education and one for those who didn't
ai_education_students = df[df['Q1.AI_knowledge'] >= 5]['Q16.GPA']
non_ai_education_students = df[df['Q1.AI_knowledge'] < 5]['Q16.GPA']

# Create a boxplot to compare the GPA distributions between the two groups
plt.figure(figsize=(8, 6))
plt.boxplot([ai_education_students, non_ai_education_students], labels=['AI Education', 'Non-AI Education'])
plt.xlabel('Student Group')
plt.ylabel('GPA')
plt.title('Comparison of GPA between AI Education and Non-AI Education Groups')
plt.grid(True)
plt.savefig('gpa_comparison_boxplot.png')  # Save the plot
plt.show()

# Create a density plot to compare the GPA distributions between the two groups
plt.figure(figsize=(8, 6))
ai_education_students.plot(kind='density', label='AI Education')
non_ai_education_students.plot(kind='density', label='Non-AI Education')
plt.xlabel('GPA')
plt.ylabel('Density')
plt.title('Comparison of GPA Distribution between AI Education and Non-AI Education Groups')
plt.legend()
plt.grid(True)
plt.savefig('gpa_comparison_density.png')  # Save the plot
plt.show()

# Calculate the average GPAs for both groups
mean_ai = ai_education_students.mean()
mean_non_ai = non_ai_education_students.mean()

# Create a bar chart to compare the average GPAs
plt.figure(figsize=(8, 6))
plt.bar(['AI Education', 'Non-AI Education'], [mean_ai, mean_non_ai], color=['blue', 'orange'])
plt.xlabel('Student Group')
plt.ylabel('Average GPA')
plt.title('Comparison of Average GPA between AI Education and Non-AI Education Groups')
plt.grid(axis='y')
plt.savefig('average_gpa_comparison.png')  # Save the plot
plt.show()

# Divide students into two groups based on AI education participation and exam pass status
exams_ai = df[(df['Q1.AI_knowledge'] >= 5) & (df['Q15.Passed_exams'] == 1)]
exams_non = df[(df['Q1.AI_knowledge'] < 5) & (df['Q15.Passed_exams'] == 1)]

# Calculate the number of students passing exams in both groups
num_ai = len(exams_ai)
num_non = len(exams_non)

# Plot a pie chart to compare the proportion of students passing exams between the two groups
labels = ['AI Education', 'Non-AI Education']
sizes = [num_ai, num_non]
colors = ['lightskyblue', 'lightcoral']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Passing Exams between AI Education and Non-AI Education Groups')
plt.savefig('exam_passing_pie_chart.png')  # Save the plot
plt.show()