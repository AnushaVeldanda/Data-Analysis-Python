#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()


# In[2]:


#Loading the CSV file to Pandas DataFrame
df_complaints = pd.read_csv('Comcast_telecom_complaints_data.csv')


# In[3]:


#Viewing the dataframe
df_complaints


# In[4]:


#Viewing top 30 rows of the data frame
df_complaints.head(30)


# In[5]:


#viewing the bottom 30 rows of the data frame
df_complaints.tail(30)


# In[6]:


#Printing the column names
df_complaints.columns


# In[7]:


#Displays number of rows and columns
df_complaints.shape


# In[8]:


#Finding if there are any null values in the data frame (displays column wise results)
df_complaints.isnull().sum()


# In[9]:


#Finding if there are any null values in the whole dataframe
df_complaints.isnull().sum().sum()


# In[10]:


#Displays the column Date_month_year and its type
df_complaints['Date_month_year']


# In[11]:


#converting Date_month_year column of type object to datetime type column with name Months
df_complaints['Months'] = pd.to_datetime(df_complaints['Date_month_year'])


# In[12]:


#Checking the new column added and its entries.
df_complaints.head()


# In[13]:


#Displays the newly added column and its type datetime.
df_complaints['Months']


# In[15]:


#Setting Months column as index to group complaints based on months
ComplaintsPerMonth = df_complaints.set_index('Months').groupby(pd.Grouper(freq='M'))


# In[45]:


# Trend chart to display number of complaints per month
plt.figure(figsize=(8,6))
ComplaintsPerMonth.size().plot()
plt.title("Number of Complaints per Month")
plt.ylabel('Number of Complaints')
plt.show()


# In[ ]:


#The above monthly trend chart shows that there was a spike during the month of June. 
#Also more number of complaints are registered through April to June months.


# In[17]:


#Displays the number of complaints for each month
ComplaintsPerMonth.size()


# In[18]:


#Setting Months column as index to group complaints based on each day
ComplaintsPerDay = df_complaints.set_index('Months').groupby(pd.Grouper(freq='D'))


# In[46]:


#Trend chart to display frequency of complaints each day
plt.figure(figsize=(8,6))
ComplaintsPerDay.size().plot()
plt.title('Frequency of Complaints each day')
plt.ylabel('Number of Complaints')
plt.show()


# In[ ]:


#The above daily trend chart shows that at the end of june there was a spike in complaints registered with maximum of 218 per day.


# In[20]:


#Displays the count of complaint frequency each day
ComplaintsPerDay.size()


# In[21]:


#To get the day with the maximum complaint count
ComplaintsPerDay.size().max()


# In[22]:


#Function for classifying complaints into different categories based on complaint text 
def complaint_type(text):
    if 'bill' in text.lower():
        return 'Billing'
    elif 'charg' in text.lower():
        return 'Charges'
    elif 'internet' in text.lower():
        return 'Internet'
    elif 'network' in text.lower():
        return 'Network'
    elif 'email' in text.lower():
        return 'Email'
    else:
        return 'Other' 


# In[23]:


#Creating a new column Complaint Type 
df_complaints['Complaint Type'] = df_complaints['Customer Complaint'].apply(complaint_type)


# In[24]:


#Displays dataframe with newly added column Complaint Type
df_complaints


# In[25]:


#Displays a table with the frequencies of different complaint types
df_complaints['Complaint Type'].value_counts()


# In[47]:


#Bar Chart to show the frequency of Complaint Types
plt.figure(figsize=(8,6))
df_complaints.groupby('Complaint Type').size().plot(kind='bar')
plt.ylabel('Number of Complaints')
plt.title('Frequency of Complaint Types')


# In[ ]:


#Since unknown complaints are classified as others with the remaining we can clearly say that complaints related to Internet were high.


# In[27]:


#Function to classify the complaint status
def complaint_status(text):
    if text.lower() == 'open' or text.lower() == 'pending':
        return 'Open'
    elif text.lower() == 'closed' or text.lower() == 'solved':
        return 'Closed'


# In[28]:


#Creating new column Complaint Status 
df_complaints['Complaint Status'] = df_complaints['Status'].apply(complaint_status)


# In[29]:


#Displays dataframe with newly added column Complaint Status
df_complaints


# In[30]:


#Grouping based on Status and Complaint Status
Status = df_complaints.groupby(['State','Complaint Status'], as_index=False)


# In[48]:


Status.size()


# In[ ]:


var = df_complaints


# In[ ]:





# In[44]:


#Stacked bar graph to display the Complaint status count for each state
Status.size().unstack().plot(kind='bar', stacked =True, figsize=(30,10))
plt.title('Complaint Status for Each State')
plt.ylabel('Number of Complaints')


# In[ ]:


#Georgia state clearly has high number of complaints registered followed by Florida in the second place.
#Georgia state the highest number of unresolved complaints.


# In[38]:


#Count of Complaint status for each state
Status.size()


# In[34]:


#Pie Chart to display percentage of complaint status open and solved.
df_complaints.groupby('Complaint Status').size().plot.pie(label="",figsize=(5,5),autopct = '%.2f%%', textprops={'size' : 'x-large', 'fontweight':'bold','color':'white'})
plt.legend()
plt.title("Total No of Complaints Open & Closed")
plt.show()


# In[35]:


#Grouping Complaint Statuts based on the mode of complaint received
Status_grp = df_complaints.groupby(['Complaint Status','Received Via'],as_index=False)


# In[36]:


#Pie chart to display complaint status open & closed received via two modes.
Status_grp.size().plot.pie(label ="", figsize=(8,8), autopct='%.2f%%')
plt.title('Complaint status received through different modes')
plt.legend(loc = 'lower left')
plt.show()


# In[ ]:




