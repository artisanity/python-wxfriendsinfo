# -*- coding: utf-8 -*-

import time
import TencentYoutuyun as TencentYoutuyun

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

#两张人脸比对，返回相似度
#session_id = id
#ret = youtu.FaceCompare(img1,img2)
#print (ret)

#新建个体ID
# ret = youtu.NewPerson(person_id="person1",image_path="zyx.jpg",group_ids="Students", person_name= 'zyx', tag='', data_type = 0)
# print(ret)

ret = youtu.DetectFace(image_path="yj13.jpg",mode = 0,data_type = 0)
print (len(ret["face"]))
print (ret)
#
for j in ret["face"]:
    print j["gender"]
    if j["gender"] > 50:
        print("性别:男")
    else:
        print("性别:女")

    print j["expression"]
    if j["expression"] >90:
        print("你在大笑")
    elif 50 <j["expression"] < 90:
        print("你在微笑")
    else:
        print("我没感觉你笑")

    print j["glasses"]
    if j["glasses"] == 1:
        print("你戴眼镜了")

    print j["beauty"]
    print("你的颜值:",j["beauty"])

    print j["age"]
    print("你的年龄:",j["age"])

ret1 = youtu.imagetag(image_path="yj15.jpg")
# print (len(ret["face"]))
print (ret1)
for j in ret1["tags"]:

    name = j[u"tag_name"].encode('iso8859-1').decode('utf-8')
    print name
    print j[u"tag_confidence"]


