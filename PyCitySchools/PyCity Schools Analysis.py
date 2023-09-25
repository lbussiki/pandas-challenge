#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd


# In[50]:


school_data = 'schools_complete.csv'


# In[51]:


Student_data = 'students_complete.csv'


# In[52]:


pd.read_csv(school_data)


# In[53]:


df1 = pd.read_csv(school_data)


# In[54]:


pd.read_csv(Student_data)


# In[55]:


df2 = pd.read_csv(Student_data)


# In[56]:


df1


# In[57]:


df2


# In[58]:


school_data_complete = pd.merge(df1, df2, how='left', on='school_name')


# In[59]:


school_data_complete.head()


# In[60]:


school_count =school_data_complete ['school_name'].nunique()
school_count


# In[61]:


student_count = len(school_data_complete)
student_count


# In[62]:


school_data_complete ['budget'].unique()


# In[63]:


budget_values=school_data_complete ['budget'].unique()


# In[64]:


budget_values


# In[65]:


df5=pd.DataFrame(budget_values)


# In[66]:


df5.columns = ['budget_values']


# In[67]:


total_budget = df5 ['budget_values'].sum()
total_budget


# In[68]:


avarange_math_score = school_data_complete ['math_score'].mean()
avarange_math_score


# In[69]:


avarange_reading_score = school_data_complete ['reading_score'].mean()
avarange_reading_score


# In[70]:


passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_math_percentage


# In[71]:


passing_reading_count = school_data_complete[(school_data_complete["reading_score"] >= 70)].count()["student_name"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100
passing_reading_percentage


# In[72]:


passing_math_reading_count = school_data_complete[
    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
overall_passing_rate


# In[73]:


dist_summary = {'Total Schools':[15], 
                    'Total Students':[39170],
                   'Total Budget':[24649428],
                   'Average Math Score':[78.98537145774827],
                   'Average Reading Score':[81.87784018381414],
                   '% Passing Math':[74.9808526933878],
                   '% Passing Reading':[81.87784018381414],
                   '% Overall Passing':[65.17232575950983]}


# In[74]:


district_summary = pd.DataFrame(dist_summary)


# In[75]:


district_summary


# In[76]:


district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)
district_summary 


# In[77]:


df1.head()


# In[78]:


School_Type=df1["type"].unique()
School_Type


# In[79]:


Total_Students =school_data_complete['school_name'].value_counts()
Total_Students


# In[80]:


Total_School_Budget = school_data_complete.groupby('school_name').budget.unique()
Total_School_Budget 


# In[81]:


Per_School_Budget= (Total_School_Budget)/(Total_Students)
Per_School_Budget


# In[82]:


per_school_math=school_data_complete.groupby('school_name').math_score.mean()
per_school_math


# In[83]:


per_school_reading=school_data_complete.groupby('school_name').reading_score.mean()
per_school_reading


# In[84]:


students_passing_math = school_data_complete[(school_data_complete["math_score"] >= 70)]
students_passing_math


# In[85]:


school_students_passing_math = students_passing_math.groupby('school_name').count()['student_name']
school_students_passing_math 


# In[86]:


students_passing_reading = school_data_complete[(school_data_complete["reading_score"] >= 70)]
students_passing_reading


# In[87]:


school_students_passing_reading =students_passing_reading.groupby('school_name').count()['student_name']
school_students_passing_reading 


# In[88]:


students_passing_math_and_reading = school_data_complete[
(school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)]


# In[89]:


school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size()
students_passing_math_and_reading


# In[90]:


overall_passing_rate1 = school_students_passing_math_and_reading / Total_Students * 100
overall_passing_rate1


# In[107]:


School_Type=df1.set_index(['school_name'])['type']
School_Type


# In[108]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary0 ={'School Type': School_Type,
    'Total Students': Total_Students, 
                      'Total School Budget' : Total_School_Budget, 
                     'Per Student Budget': Per_School_Budget,
                      'Average Math Score':per_school_math,
                      'Average Reading Score': per_school_reading,
                      '% Passing Math': school_students_passing_math,
                      '% Passing Reading': school_students_passing_reading,
                     '% Overall Passing': overall_passing_rate1}


# In[109]:


per_school_summary = pd.DataFrame(per_school_summary0)
per_school_summary


# In[111]:


## Highest-Performing Schools (by % Overall Passing)
per_school_summary.sort_values('% Overall Passing', ascending=False).head(5)


# In[112]:


## Bottom Performing Schools (By % Overall Passing)
per_school_summary.sort_values('% Overall Passing').head(5)


# In[113]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
ninth_graders 


# In[114]:


tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]


# In[115]:


# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grade_math_scores = ninth_graders.groupby('school_name').math_score.mean()
ninth_grade_math_scores


# In[116]:


tenth_grader_math_scores = tenth_graders.groupby('school_name').math_score.mean()
tenth_grader_math_scores


# In[117]:


eleventh_grader_math_scores = eleventh_graders.groupby('school_name').math_score.mean()
eleventh_grader_math_scores


# In[118]:


twelfth_grader_math_scores = twelfth_graders.groupby('school_name').math_score.mean()
twelfth_grader_math_scores


# In[119]:


math_scores_by_grade0= {'9th': ninth_grade_math_scores,
                        '10th': tenth_grader_math_scores,
                        '11th': eleventh_grader_math_scores,
                        '12th': twelfth_grader_math_scores}


# In[120]:


math_scores_by_grade = pd.DataFrame(math_scores_by_grade0)
math_scores_by_grade


# In[121]:


math_scores_by_grade.index.name = None


# In[122]:


math_scores_by_grade


# In[123]:


ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]


# In[124]:


ninth_grade_reading_score = ninth_graders.groupby('school_name').reading_score.mean()
tenth_grader_reading_scores = tenth_graders.groupby('school_name').reading_score.mean()
eleventh_grader_reading_scores = eleventh_graders.groupby('school_name').reading_score.mean()
twelfth_grader_reading_scores = twelfth_graders.groupby('school_name').reading_score.mean()


# In[125]:


reading_scores_by_grade0= {'9th': ninth_grade_reading_score ,
                        '10th': tenth_grader_reading_scores,
                        '11th': eleventh_grader_reading_scores,
                        '12th': twelfth_grader_reading_scores}
reading_scores_by_grade = pd.DataFrame(reading_scores_by_grade0)
reading_scores_by_grade.index.name = None
reading_scores_by_grade


# In[126]:


spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[127]:


school_spending = per_school_summary.copy()


# In[128]:


school_spending["Spending Ranges (Per Student)"] = pd.cut(x=school_spending['Per Student Budget'], bins = [0, 585, 630, 645, 680], labels = ["<$585", "$585-630", "$630-645", "$645-680"])
school_spending


# In[129]:


spending_math_scores = school_spending.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean()


# In[130]:


# Assemble into DataFrame
spending_summary0 = {'Average Math Score':spending_math_scores,
                    'Average Reading Score':spending_reading_scores,
                    '% Passing Math':spending_passing_math,
                    '% Passing Reading':spending_passing_reading,
                    '% Overall Passing':overall_passing_spending}
spending_summary=pd.DataFrame(spending_summary0)
spending_summary


# In[131]:


size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[132]:


school_sizing = per_school_summary.copy()


# In[133]:


school_sizing["School Size"] = pd.cut(x=school_sizing['Total Students'], bins = [0, 1000, 2000, 5000], labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"])
school_sizing


# In[134]:


size_math_scores = school_sizing.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = school_sizing.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = school_sizing.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = school_sizing.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = school_sizing.groupby(["School Size"])["% Overall Passing"].mean()


# In[135]:


size_summary0 = {'Average Math Score':size_math_scores,
                    'Average Reading Score':size_reading_scores,
                    '% Passing Math':size_passing_math,
                    '% Passing Reading':size_passing_reading,
                    '% Overall Passing':size_overall_passing}
size_summary=pd.DataFrame(size_summary0)
size_summary


# In[136]:


average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Overall Passing"].mean()


# In[137]:


type_summary0 = {'Average Math Score':average_math_score_by_type,
                    'Average Reading Score':average_reading_score_by_type,
                    '% Passing Math':average_percent_passing_math_by_type,
                    '% Passing Reading':average_percent_passing_reading_by_type,
                    '% Overall Passing':average_percent_overall_passing_by_type}
type_summary=pd.DataFrame(type_summary0)

# Display results
type_summary


# In[ ]:




