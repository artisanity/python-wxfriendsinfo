# -*- coding: utf-8 -*-
#!/usr/bin/python

import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import sys

print sys.path


itchat.login()

friends = itchat.get_friends(update=True)
print friends

NickName = friends[0].NickName #获取自己的昵称
# os.mkdir(NickName) #为自己创建一个文件夹

file = '\%s' %NickName #刚刚创建的那个文件夹的相对路径
cp = os.getcwd() #当前路径
path = os.path.join(cp+file) #刚刚创建的那个文件夹的绝对路径
os.chdir(path) #切换路径

print path

number_of_friends = len(friends)

df_friends = pd.DataFrame(friends)

def get_count(Sequence):
    counts = defaultdict(int) #初始化一个字典
    for x in Sex:
        counts[x] += 1
    return counts

Sex = df_friends.Sex
Sex_count = get_count(Sex)

print Sex_count

Sex_count = Sex.value_counts()                  #defaultdict(int, {0: 31, 1: 292, 2: 245})
Sex_count.plot(kind = 'bar')






