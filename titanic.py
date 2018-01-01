
# coding: utf-8

# ## 导入数据

# In[1]:



#加载项目所需库
import numpy as np
import pandas as pd

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# In[2]:


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

# In[3]:


#获救情况
survived_nums = data.Survived.value_counts()
print survived_nums
survived_nums.plot(kind='bar')


# 549人死亡，342人获救

# In[4]:


#仓位
pclass_num = data.Pclass.value_counts()
print pclass_num
pclass_num.plot(kind='bar')


# 3等仓人最多491人，
# 2等仓人最少184人
# 1等仓216人
# 

# In[5]:


#性别
sex_nums=data.Sex.value_counts()
print sex_nums
sex_nums.plot(kind='bar')


# 男性577人，女性314人
# 男性人数约为女性人数2倍

# In[6]:


#年龄
data.Age.plot(kind='kde')


# 乘客中大部分人的年龄都小于40，20到30岁之间人数最多

# In[7]:


#堂兄弟/妹个数
data.SibSp.value_counts().plot(kind='bar')


# In[8]:


# Parch:父母与小孩个数
data.Parch.value_counts().plot(kind='bar')


# In[9]:


# Fare:票价
data.Fare.hist(bins=10)


# 票价基本在100以内

# In[10]:


# Embarked:登船港口remote "origin"
embarked_nums = data.Embarked.value_counts()
print embarked_nums
embarked_nums.plot(kind='bar')


# S港口登船人数最多644人，元多于其他港口
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

# In[13]:


#性别与获救
Survived_0 = data.Sex[data.Survived == 0].value_counts()
Survived_1 = data.Sex[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Sex") 
plt.ylabel("persion number") 
plt.show()



# 女性获救几率远高于男性

# In[12]:


#年龄与获救
plt.subplot2grid((2,3),(0,2))
plt.scatter(data.Survived, data.Age)
plt.ylabel("Age")                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y') 
plt.title("Survived")


# In[14]:


#堂兄弟/妹个数与获救
Survived_0 = data.SibSp[data.Survived == 0].value_counts()
Survived_1 = data.SibSp[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("SibSp") 
plt.ylabel("persion number") 
plt.show()


# In[15]:


# Parch:父母与小孩个数
Survived_0 = data.Parch[data.Survived == 0].value_counts()
Survived_1 = data.Parch[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Parch") 
plt.ylabel("persion number") 
plt.show()


# 有1到3个亲人会有较大几率获救

# In[26]:


# 票价与获救
Survived_0 = data.Fare[data.Survived == 0].value_counts()
Survived_1 = data.Fare[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='kde', stacked=True)
plt.xlabel("Fare") 
plt.ylabel("persion number") 
plt.show()


# In[24]:


#登船港口与获救
Survived_0 = data.Embarked[data.Survived == 0].value_counts()
Survived_1 = data.Embarked[data.Survived == 1].value_counts()
df=pd.DataFrame({'life':Survived_1, 'death':Survived_0})
df.plot(kind='bar', stacked=True)
plt.xlabel("Embarked") 
plt.ylabel("persion number") 
plt.show()


# C港口登船的获救几率远大于S港口登船
