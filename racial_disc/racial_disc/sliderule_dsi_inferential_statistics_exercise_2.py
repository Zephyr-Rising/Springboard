
# coding: utf-8

# # Examining Racial Discrimination in the US Job Market
# 
# ### Background
# Racial discrimination continues to be pervasive in cultures throughout the world. Researchers examined the level of racial discrimination in the United States labor market by randomly assigning identical résumés to black-sounding or white-sounding names and observing the impact on requests for interviews from employers.
# 
# ### Data
# In the dataset provided, each row represents a resume. The 'race' column has two values, 'b' and 'w', indicating black-sounding and white-sounding. The column 'call' has two values, 1 and 0, indicating whether the resume received a call from employers or not.
# 
# Note that the 'b' and 'w' values in race are assigned randomly to the resumes when presented to the employer.

# <div class="span5 alert alert-info">
# ### Exercises
# You will perform a statistical analysis to establish whether race has a significant impact on the rate of callbacks for resumes.
# 
# Answer the following questions **in this notebook below and submit to your Github account**. 
# 
#    1. What test is appropriate for this problem? Does CLT apply?
#    2. What are the null and alternate hypotheses?
#    3. Compute margin of error, confidence interval, and p-value.
#    4. Write a story describing the statistical significance in the context or the original problem.
#    5. Does your analysis mean that race/name is the most important factor in callback success? Why or why not? If not, how would you amend your analysis?
# 
# You can include written notes in notebook cells using Markdown: 
#    - In the control panel at the top, choose Cell > Cell Type > Markdown
#    - Markdown syntax: http://nestacms.com/docs/creating-content/markdown-cheat-sheet
# 
# 
# #### Resources
# + Experiment information and data source: http://www.povertyactionlab.org/evaluation/discrimination-job-market-united-states
# + Scipy statistical methods: http://docs.scipy.org/doc/scipy/reference/stats.html 
# + Markdown syntax: http://nestacms.com/docs/creating-content/markdown-cheat-sheet
# </div>
# ****

# In[1]:

import pandas as pd
import numpy as np
from scipy import stats


# In[2]:

data = pd.io.stata.read_stata('data/us_job_market_discrimination.dta')


# ### What test is appropriate for this problem? Does CLT apply?
# 
# As gender should be a independent variable, we can use the ttest_ind function from scipy, with a significance value of 0.05.  
# 
# ### What are the null and alternate hypotheses?
# 
# This test compares two means for two independent samples.
# 
# * Null hypothesis: The two samples have an equal mean. 
# * Alternate hypothesis: The two samples have a different mean.
# 
# ### Compute margin of error, confidence interval, and p-value.

# In[19]:

bcall = data[data.race=='b'].call
wcall = data[data.race=='w'].call
mean_dif = bcall.mean() - wcall.mean()
b_sigma = (bcall.std() ** 2) / bcall.count()
w_sigma = (wcall.std() ** 2) / wcall.count()
moe = b_sigma + w_sigma * 1.96
ci = (mean_dif - moe , mean_dif + moe)
print("Margin of Error: %f" %moe)
print("Confidence Interval:")
print(ci)


# ### Write a story describing the statistical significance in the context or the original problem.
# 
# Given the p-value, we must reject the null hypothesis, and accept the alternate hypothesis that the two samples have a different mean.  This hypothesis test shows that, given that the resumes are the same, that there  is a significant difference between the amount of callbacks between black and white-sounding names.  

# In[22]:

data.groupby(['call', 'race']).mean()

