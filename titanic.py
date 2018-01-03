
# coding: utf-8

# ## 导入数据

# In[49]:



#加载项目所需库
import numpy as np
import pandas as pd

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# In[50]:


#载入titanic数据
# PassengerId:乘客ID
# Survived:是否生还
# Pclass:乘客等级(1/2/3等舱位)
# Name:乘客姓名
# Sex:性别
# Age:年龄
# SibSp:堂兄弟/妹个数
# Parch:父母与小孩个数
# Ticket:船票信息
# Fare:票价
# Cabin:客舱
# Embarked:登船港口remote "origin"
data = pd.read_csv('titanic-data.csv')
len(data)


# ## 了解数据

# In[51]:


#粗略查看信息
data.info()


# 数据中有891<br>
# Age(年龄)、Cabin(客舱)、Embarked(登船港口)信息有所缺失,其中Age、Embarked信息缺失较少,Cabin缺失严重

# In[52]:


#平均值填充Age
age_mean = data.Age.mean()
data.Age = data.Age.fillna(age_mean)
data.info()


# In[53]:


#众数填充Embarked
data.Embarked = data.Embarked.fillna(data.Embarked.mode().values[0])
data.info()


# In[54]:


#去除Cabin
data = data.dropna(axis=1, how='any')
data.info()


# In[55]:


#获救情况
survived_nums = data.Survived.value_counts()
print survived_nums
survived_nums.plot(kind='bar')


# 549人死亡，342人获救

# In[56]:


#仓位
pclass_num = data.Pclass.value_counts()
print pclass_num
pclass_num.plot(kind='bar')


# 3等仓人最多491人，
# 2等仓人最少184人
# 1等仓216人
# 

# In[57]:


#性别
sex_nums=data.Sex.value_counts()
print sex_nums
sex_nums.plot(kind='bar')


# 男性577人，女性314人
# 男性人数约为女性人数2倍

# In[58]:


#年龄
data.Age.plot(kind='kde')


# 乘客中大部分人的年龄都小于40，20到30岁之间人数最多

# In[59]:


#堂兄弟/妹个数
data.SibSp.value_counts().plot(kind='bar')


# In[60]:


# Parch:父母与小孩个数
data.Parch.value_counts().plot(kind='bar')


# In[61]:


# Fare:票价
data.Fare.hist(bins=10)


# 票价基本在100以内

# In[62]:


# Embarked:登船港口remote "origin"
embarked_nums = data.Embarked.value_counts()
print embarked_nums
embarked_nums.plot(kind='bar')


# S港口登船人数最多646人，元多于其他港口
# Q港口人数最少77人
# C港口登船人数168人

# ## 数据探索

# In[11]:


#仓位与获救
Survived_0 = data.Pclass[data.Survived == 0].value_counts()
Survived_1 = data.Pclass[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Pclass") 
plt.ylabel("persion number") 
plt.show()


# 1号仓获救几率更大些，1号仓可能为头等舱

# In[12]:


#性别与获救
Survived_0 = data.Sex[data.Survived == 0].value_counts()
Survived_1 = data.Sex[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Sex") 
plt.ylabel("persion number") 
plt.show()



# 女性获救几率远高于男性

# In[67]:


#年龄与获救
bins = np.arange(0,90,10)
data['Age_group'] = pd.cut(data['Age'],bins)
data.groupby(['Age_group'])['PassengerId'].count()


# In[70]:


plt.figure(figsize=(12,5))
f,(ax1,ax2) = plt.subplots(1,2)
f.set_size_inches((20,8))
data.groupby(['Age_group','Survived'])['PassengerId']    .count().unstack().plot(kind='bar',ax = ax1,stacked = True)
ax1.set_title('Age VS Count')
ax1.set_ylabel('Count')
data.groupby('Age_group')['Survived'].mean().plot(kind = 'bar',ax = ax2)
ax2.set_title('Age VS Survival Rate')
ax2.set_ylabel('Survival Rate')
plt.show()


# 0-10岁获救率最高，10-60岁之间获救率相差不大，60岁以上获救率最低

# In[71]:


# Parch:父母与小孩个数
Survived_0 = data.Parch[data.Survived == 0].value_counts()
Survived_1 = data.Parch[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Parch") 
plt.ylabel("persion number") 
plt.show()


# 有1到3个亲人会有较大几率获救

# In[80]:


# 票价与获救
bins = np.arange(0,600,50)
data['Fare_group'] = pd.cut(data['Fare'],bins)
data.groupby(['Fare_group'])['PassengerId'].count()


# In[81]:




plt.figure(figsize=(12,5))
f,(ax1,ax2) = plt.subplots(1,2)
f.set_size_inches((20,8))
data.groupby(['Fare_group','Survived'])['PassengerId']    .count().unstack().plot(kind='bar',ax = ax1,stacked = True)
ax1.set_title('Fare VS Count')
ax1.set_ylabel('Count')
data.groupby('Fare_group')['Survived'].mean().plot(kind = 'bar',ax = ax2)
ax2.set_title('Fare VS Survival Rate')
ax2.set_ylabel('Survival Rate')
plt.show()


# 票价高获救几率会大一些，富人更可能获救

# In[82]:


#登船港口与获救
Survived_0 = data.Embarked[data.Survived == 0].value_counts()
Survived_1 = data.Embarked[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Embarked") 
plt.ylabel("persion number") 
plt.show()


# C港口登船的获救几率远大于S港口登船

# # 结论
# 泰坦尼克号出事载客量2224人，报告中使用了其中部分数据891人约为总人数的40%，大体上可以代表泰坦尼克号上的整体人口，但不能完全代表。在数据清洗时，Age的填充可能会改变20-30岁的获救率和年龄的分布，Embarked的填充可能会改变S港口的获救率。朋友的个数，遇难前是在睡觉还是清醒状态，身体是否有残疾也会影响存活率
