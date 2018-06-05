# -*- coding: utf-8 -*-
#!/usr/bin/python

# 导入模块
import csv
import re
import os

from snownlp import SnowNLP
import jieba.analyse
import itchat

import numpy as np
import pandas as pd
from collections import defaultdict
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import TencentYoutuyun as TencentYoutuyun
from pylab import *
# from TencentYoutuyun import FaceAPI

# pip install requests
# please get these values from http://open.youtu.qq.com
appid = '10135067'
secret_id = 'AKIDKXgfT6sR4cpsjQ4TnvrnbIp16ztcmTM7'
secret_key = 'pY6gBYjiV6Vkw46Yw88z0umbOVZWJzUL'
userid = '348169652'

#choose a end_point
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

print youtu

# sig = "开心快乐"
# nlp = SnowNLP(sig)
# print nlp.sentiments

mpl.rcParams['font.sans-serif'] = ['SimHei']

itchat.login()

#爬取自己好友相关信息， 返回一个json文件
friends = itchat.get_friends(update=True)[0:]

print friends

'''
def analyseHeadImage(frineds):
    # Init Path
    basePath = os.path.abspath('.')
    baseFolder = basePath + '\\HeadImages\\'
    if (os.path.exists(baseFolder) == False):
        os.makedirs(baseFolder)
    #
    # # Analyse Images
    # faceApi = TencentYoutuyun.FaceAPI()
    use_face = 0
    not_use_face = 0

    male_use_face = 0
    male_not_use_face = 0
    female_use_face = 0
    female_not_use_face = 0

    male_use_child_face = 0
    female_use_child_face = 0

    image_tags = ''
    #
    print "friends num is: " + str(len(friends))
    # for index in range(1, 50):
    for index in range(1, len(friends)):
        friend = friends[index]
        gender = friend['Sex']
        print index
        print "gender is:" + str(gender)
        # Save HeadImages
        imgFile = baseFolder + '\\Image%s.jpg' % str(index)
        imgData = itchat.get_head_img(userName=friend['UserName'])
        if (os.path.exists(imgFile) == False):
            with open(imgFile, 'wb') as file:
                file.write(imgData)

        # Detect Faces
        # time.sleep(1)

        ret = youtu.DetectFace(image_path=imgFile, mode=0, data_type=0)
        print (len(ret["face"]))
        print (ret)

        if len(ret["face"]) > 0:
            use_face += 1
            if gender == 2:
                female_use_face += 1
                for j in ret["face"]:
                    if j["age"] < 10:
                        female_use_child_face += 1
            elif gender == 1:
                male_use_face += 1
                for j in ret["face"]:
                    if j["age"] < 10:
                        male_use_child_face += 1
        else:
            not_use_face += 1
            if gender == 2:
                female_not_use_face += 1
            elif gender == 1:
                male_not_use_face += 1




        ret1 = youtu.imagetag(image_path=imgFile)
        # print (len(ret["face"]))
        print (ret1)
        for j in ret1["tags"]:
            # name = j[u"tag_name"]
            name = j[u"tag_name"].encode('iso8859-1').decode('utf-8')
            print name
            # image_tags += ','.join(name)
            image_tags += name
            image_tags += ','
            print image_tags

    print use_face
    print not_use_face
    print female_use_face
    print male_use_face
    print female_not_use_face
    print male_not_use_face
    print male_use_child_face
    print female_use_child_face

    # Extract Tags
        # result = faceApi.extractTags(imgFile)
        # image_tags += ','.join(list(map(lambda x:x['tag_name'],result)))


    labels = [u'使用人脸头像', u'不使用人脸头像']
    counts = [use_face, not_use_face]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,  # 性别统计结果
            labels=labels,  # 性别展示标签
            colors=colors,  # 饼图区域配色
            labeldistance=1.1,  # 标签距离圆点距离
            autopct='%3.1f%%',  # 饼图区域文本格式
            shadow=False,  # 饼图是否显示阴影
            startangle=90,  # 饼图起始角度
            pctdistance=0.6  # 饼图区域文本距离圆点距离
            )
    plt.legend(loc='upper right', )
    plt.title(u'%s的微信好友使用人脸头像情况' % friends[0]['NickName'])
    plt.show()


    labels = [u'男性好友使用人脸头像', u'男性好友不使用人脸头像']
    counts = [male_use_face, male_not_use_face]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,  # 性别统计结果
            labels=labels,  # 性别展示标签
            colors=colors,  # 饼图区域配色
            labeldistance=1.1,  # 标签距离圆点距离
            autopct='%3.1f%%',  # 饼图区域文本格式
            shadow=False,  # 饼图是否显示阴影
            startangle=90,  # 饼图起始角度
            pctdistance=0.6  # 饼图区域文本距离圆点距离
            )
    plt.legend(loc='upper right', )
    plt.title(u'%s的微信男性好友使用人脸头像情况' % friends[0]['NickName'])
    plt.show()


    labels = [u'女性好友使用人脸头像', u'女性好友不使用人脸头像']
    counts = [female_use_face, female_not_use_face]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,  # 性别统计结果
            labels=labels,  # 性别展示标签
            colors=colors,  # 饼图区域配色
            labeldistance=1.1,  # 标签距离圆点距离
            autopct='%3.1f%%',  # 饼图区域文本格式
            shadow=False,  # 饼图是否显示阴影
            startangle=90,  # 饼图起始角度
            pctdistance=0.6  # 饼图区域文本距离圆点距离
            )
    plt.legend(loc='upper right', )
    plt.title(u'%s的微信女性好友使用人脸头像情况' % friends[0]['NickName'])
    plt.show()


    labels = [u'使用儿童人脸作为头像', u'不使用儿童人脸作为头像']
    counts = [male_use_child_face, male_use_face - male_use_child_face]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,  # 性别统计结果
            labels=labels,  # 性别展示标签
            colors=colors,  # 饼图区域配色
            labeldistance=1.1,  # 标签距离圆点距离
            autopct='%3.1f%%',  # 饼图区域文本格式
            shadow=False,  # 饼图是否显示阴影
            startangle=90,  # 饼图起始角度
            pctdistance=0.6  # 饼图区域文本距离圆点距离
            )
    plt.legend(loc='upper right', )
    plt.title(u'%s的微信男性好友使用儿童人脸头像情况' % friends[0]['NickName'])
    plt.show()


    labels = [u'使用儿童人脸作为头像', u'不使用儿童人脸作为头像']
    counts = [female_use_child_face, female_use_face - female_use_child_face]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8, 5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts,  # 性别统计结果
            labels=labels,  # 性别展示标签
            colors=colors,  # 饼图区域配色
            labeldistance=1.1,  # 标签距离圆点距离
            autopct='%3.1f%%',  # 饼图区域文本格式
            shadow=False,  # 饼图是否显示阴影
            startangle=90,  # 饼图起始角度
            pctdistance=0.6  # 饼图区域文本距离圆点距离
            )
    plt.legend(loc='upper right', )
    plt.title(u'%s的微信女性好友使用儿童人脸头像情况' % friends[0]['NickName'])
    plt.show()

    # image_tags = image_tags.encode('iso8859-1').decode('utf-8')
    # image_tags = image_tags.encode('iso8859-1').decode('utf-8')
    back_coloring = np.array(Image.open('flower.jpg'))
    wordcloud = WordCloud(
        font_path='simfang.ttf',
        background_color="white",
        max_words=1200,
        mask=back_coloring,
        max_font_size=75,
        random_state=45,
        width=800,
        height=480,
        margin=15
    )

    wordcloud.generate(image_tags)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


analyseHeadImage(friends)


#初始化计数器
male = female = other = 0
#friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other +=1
#计算朋友总数
total = len(friends[1:])
#打印出自己的好友性别比例
print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
"不明性别好友： %.2f%%" % (float(other) / total * 100))


def analyseSex(firends):
    sexs = list(map(lambda x:x['Sex'],friends[1:]))
    counts = list(map(lambda x:x[1],Counter(sexs).items()))
    # plt.title(u'朋友圈男女性别比例',fontproperties='SimHei')
    labels = [u'性别未设置',u'男性',u'女性']
    colors = ['red','yellowgreen','lightskyblue']
    plt.figure(figsize=(12,8), dpi=80)
    plt.axes(aspect=1)
    # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0, 0.03, 0)
    plt.pie(counts, #性别统计结果
            explode=explode,
            labels=labels, #性别展示标签
            colors=colors, #饼图区域配色
            labeldistance = 1.1, #标签距离圆点距离
            autopct = '%3.2f%%', #饼图区域文本格式
            shadow = False, #饼图是否显示阴影
            startangle = 90, #饼图起始角度
            pctdistance = 0.6 #饼图区域文本距离圆点距离
    )
    plt.legend(loc='upper right',)
    plt.title(u'%s的微信好友性别组成' % friends[0]['NickName'])
    plt.show()

# analyseSex(friends)

def analyseLocation(friends):
    headers = ['NickName','Province','City']
    with open('location.csv','w') as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName'].encode('utf-8')
           row['Province'] = friend['Province'].encode('utf-8')
           row['City'] = friend['City'].encode('utf-8')
           writer.writerow(row)


# analyseLocation(friends)
'''

def analyseSignature(friends):
    signatures = ''
    emotions = []
    pattern = re.compile("1f\d.+")
    for friend in friends:
        signature = friend['Signature'].encode('utf-8')
        # print signature
        if(signature != None):
            signature = signature.strip().replace('span', '').replace('class', '').replace('emoji', '')
            signature = re.sub(r'1f(\d.+)','',signature)
            if(len(signature)>0):
                nlp = SnowNLP(signature.decode('utf-8'))
                emotions.append(nlp.sentiments)
                print signature
                print nlp.sentiments
                print emotions

                signatures += ' '.join(jieba.analyse.extract_tags(signature,5))
    with open('signatures.txt','w') as file:
        signatures = signatures.encode('utf-8')
        file.write(signatures)

    print emotions

    # Sinature WordCloud
    back_coloring = np.array(Image.open('flower.jpg'))
    wordcloud = WordCloud(
        font_path='D:\python\project\ichatpro\simfang.ttf',
        background_color="white",
        max_words=2000,
        mask=back_coloring,
        max_font_size=75,
        random_state=45,
        width=960,
        height=720,
        scale=2,
        margin=15
    )

    wordcloud.generate(signatures.decode("utf-8"))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('signatures.jpg')


    # Signature Emotional Judgment
    count_good = len(list(filter(lambda x:x>0.66,emotions)))
    count_normal = len(list(filter(lambda x:x>=0.33 and x<=0.66,emotions)))
    count_bad = len(list(filter(lambda x:x<0.33,emotions)))
    print count_bad
    print count_normal
    print count_good



    labels = [u'负面消极',u'中性',u'正面积极']
    values = (count_bad,count_normal,count_good)
    plt.rcParams['font.sans-serif'] = ['simHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel(u'情感判断')
    plt.ylabel(u'频数')
    plt.xticks(range(3),labels)
    plt.legend(loc='upper right',)
    plt.bar(range(3), values, color = 'rgb')
    plt.title(u'%s的微信好友签名信息情感分析' % friends[0]['NickName'])
    plt.show()


analyseSignature(friends)


