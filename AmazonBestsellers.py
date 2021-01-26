import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bs = pd.read_csv('/Users/louietran/Downloads/bestsellers with categories.csv')

women = pd.read_csv('/Users/louietran/Downloads/Dataset3.csv',sep=';')

stu = pd.read_csv('/Users/louietran/Downloads/StudentsPerformance.csv')
cols = ['sex','race','par_edu','lunch','prep_course','math_score','read_score','write_score']

stu.columns = cols



order = ['some high school', 'high school', "associate's degree",'some college',"bachelor's degree","master's degree"]
order_type = pd.CategoricalDtype(categories=order, ordered=True)
stu['par_edu'] = stu.par_edu.astype(order_type) 

mapping = {'none': False, 'completed':True}
stu.prep_course = stu.prep_course.map(mapping)
stu['avg_score']=stu[['math_score','read_score','write_score']].mean(axis=1)

def letter_grade(df,str_col):
    
    col = str_col.replace('_score','_let')
    df[col] = df[str_col]
    bins = [-1,60,70,80,90,100]
    group_names = ['F','D','C','B','A']
    stu[col] = pd.cut(stu[col], bins, labels=group_names)
    stu[col] = st[col]
    return(df.info())


fig, ax = plt.subplots(2,3,figsize=(25,15))
plt.subplots_adjust(left = 0.1, wspace=0.2, hspace=0.1)


ax[0,0].pie(stu['par_edu'].value_counts(),labels=stu['par_edu'].unique(), 
        autopct='%1.1f%%',startangle=90,textprops={'fontsize':8})
ax[0,0].legend(ncol=2,loc='lower center',bbox_to_anchor =(0.5,-0.2),fontsize='x-small')
ax[0,0].set_title('Parental Level of Education')


ax[0,1].pie(stu['race'].value_counts(),labels=stu['race'].unique(), 
        autopct='%1.1f%%',startangle=90,textprops={'fontsize':8})
ax[0,1].legend(ncol=2,loc='lower center',bbox_to_anchor =(0.5,-0.2),fontsize='x-small')
ax[0,1].set_title('Race')
ax[0,2].bar(stu['sex'].unique(),stu['sex'].value_counts())

plt.show()

#How gender affects students' performance on exam
stu1 = stu.melt(id_vars='sex',value_vars=['math_score','read_score','write_score','avg_score'],var_name='subject',value_name='score')
stu1.groupby(['subject','sex'])['score'].mean().unstack().plot(kind='bar', title ="How gender affects students' performance")
plt.xticks(rotation=360)
plt.show()

#How race affects students' performance on exam
stu2 = stu.melt(id_vars='race',value_vars=['math_score','read_score','write_score','avg_score'],var_name='subject',value_name='score')
stu2.groupby(['subject','race'])['score'].mean().unstack().plot(kind='bar', title ="How gender affects students' performance")
plt.xticks(rotation=360)
plt.show()

#Parents education
stu_par_edu_2 = stu.groupby('race')['par_edu'].value_counts().unstack()
stu_par_edu_2.plot(kind='bar', title="parents' education among races", stacked=True,rot=45)
plt.show()

#How parents education affects students' performance on exam
stu3 = stu.melt(id_vars='par_edu',value_vars=['math_score','read_score','write_score','avg_score'],var_name='subject',value_name='score')
stu3.groupby(['subject','par_edu'])['score'].mean().unstack().plot(kind='bar', title ="How parents' education affect students' performance")
plt.xticks(rotation=45)
plt.show()

#Lunch
stu4 = stu.melt(id_vars='lunch',value_vars=['math_score','read_score','write_score','avg_score'],var_name='subject',value_name='score')
stu4.groupby(['subject','lunch'])['score'].mean().unstack().plot(kind='bar', title ="How lunchffects students' performance")
plt.xticks(rotation=360)
plt.show()

#prep_course
stu5 = stu.melt(id_vars='prep_course',value_vars=['math_score','read_score','write_score','avg_score'],var_name='subject',value_name='score')
stu5.groupby(['subject','prep_course'])['score'].mean().unstack().plot(kind='bar', title ="How preparation courses affects students' performance")
plt.xticks(rotation=360)
plt.show()
