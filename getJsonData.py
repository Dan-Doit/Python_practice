#         영화 1         영화 3        영화 3
arr = {'data': {'allUsers': [{'id': 'ckkf1dp6x003i07110mxjth9e', 'username': '정소윤', 'likes': [{'post': {'id': 'ckkf5b3jp00750737u6hxkoal'}}, {'post': {'id': 'ckkghlm83007p079338mfw3yw'}}, {'post': {'id': 'ckkf59ps200630737q585orrh'}}, {'post': {'id': 'ckkf59ps200630737q585orrh'}}, {'post': {'id': 'ckkg6iecs000e0743on42hu1u'}}, {'post': {'id': 'ckkf4uqje001007373do8p3pg'}}, {'post': {'id': 'ckkjdqdwq03ht07591f1med64'}}, {'post': {'id': 'ckknxfmop03wp0763jrytuxnq'}}, {'post': {'id': 'ckkf7fx1v00ji07374at73dck'}}]}, {'id': 'ckkf4vjh3001k0737w4xsnags', 'username': 'HAEiNee', 'likes': [{'post': {'id': 'ckkf4uqje001007373do8p3pg'}}]}, {'id': 'ckkf50x7200470737wt2tt8k9', 'username': '강동훈', 'likes': [{'post': {'id': 'ckkf5b3jp00750737u6hxkoal'}}, {'post': {'id': 'ckkf59ps200630737q585orrh'}}, {'post': {'id': 'ckkf4uqje001007373do8p3pg'}}, {'post': {'id': 'ckkf7gbru00l70737n02pk9xs'}}, {'post': {'id': 'ckkf7fx1v00ji07374at73dck'}}, {'post': {'id': 'ckkf7a5qd00g40737342i2ozp'}}, {'post': {'id': 'ckkf6wx1f00dt0737i72futyg'}}, {'post': {'id': 'ckkf66a7h00bq0737lexi8zs8'}}, {'post': {'id': 'ckkf65wld00ax073746ax8mmq'}}, {'post': {'id': 'ckkf64g3r008k0737iwgxbfya'}}, {'post': {'id': 'ckkghlm83007p079338mfw3yw'}}]}, {'id': 'ckkf5a31c006n0737mn3pd4iw', 'username': '조단', 'likes': [{'post': {'id': 'ckkf5b3jp00750737u6hxkoal'}}]}, {'id': 'ckkf64qqq00950737wyt8znay', 'username': '김종 훈', 'likes': [{'post': {'id': 'ckkf7fx1v00ji07374at73dck'}}, {'post': {'id': 'ckkf4uqje001007373do8p3pg'}}, {'post': {'id': 'ckkf65wld00ax073746ax8mmq'}}, {'post': {'id': 'ckkf5b3jp00750737u6hxkoal'}}, {'post': {'id': 'ckkf5b3jp00750737u6hxkoal'}}, {'post': {'id': 'ckkghlm83007p079338mfw3yw'}}, {'post': {'id': 'ckkjdqdwq03ht07591f1med64'}}, {'post': {'id': 'ckknxhanb03xu076334zqt03r'}}, {'post': {'id': 'ckkp4g1np023b0702bs2569qc'}}]}, {'id': 'ckkna71b800890763mltm7mmt', 'username': 'win.ha_95', 'likes': [{'post': {'id': 'ckkf64g3r008k0737iwgxbfya'}}, {'post': {'id': 'ckkf65wld00ax073746ax8mmq'}}, {'post': {'id': 'ckkf7a5qd00g40737342i2ozp'}}]}, {'id': 'ckkp6xw0800160767yh4uoq6w', 'username': '정소윤짱', 'likes': []}, {'id': 'ckkp74anh001r0767sxeqqz2c', 'username': '강동훈짱', 'likes': []}, {'id': 'ckkp77wc8002o07675ytsbosf', 'username': '종훈짱', 'likes': []}]}}
parr = {'data': {'posts': [{'id': 'ckkf4uqje001007373do8p3pg'}, {'id': 'ckkf59ps200630737q585orrh'}, {'id': 'ckkf5b3jp00750737u6hxkoal'}, {'id': 'ckkf64g3r008k0737iwgxbfya'}, {'id': 'ckkf65wld00ax073746ax8mmq'}, {'id': 'ckkf66a7h00bq0737lexi8zs8'}, {'id': 'ckkf6wx1f00dt0737i72futyg'}, {'id': 'ckkf7a5qd00g40737342i2ozp'}, {'id': 'ckkf7fx1v00ji07374at73dck'}, {'id': 'ckkf7gbru00l70737n02pk9xs'}, {'id': 'ckkg6iecs000e0743on42hu1u'}, {'id': 'ckkghlm83007p079338mfw3yw'}, {'id': 'ckkjdqdwq03ht07591f1med64'}, {'id': 'ckknxfmop03wp0763jrytuxnq'}, {'id': 'ckknxhanb03xu076334zqt03r'}, {'id': 'ckkp2puaw01q80702bpl2c173'}, {'id': 'ckkp4g1np023b0702bs2569qc'}, {'id': 'ckkqob7ag002z0716jteupeuu'}, {'id': 'ckkqop8ac008o07160q5yr4bb'}]}}

arr = arr['data']['allUsers']
print(arr)
users = []
posts = []
isLike = []
result = []
for i in arr:
    users.append(i['id'])
#모든 유저값
print(users)

for i in parr['data']['posts']:
    posts.append(i['id'])
#모든 포스트값
print(posts)

# 좋아하는지 체크
for i in arr:
    for j in i['likes']:
        isLike.append([i['id'],j['post']['id']])
print(isLike)

for i in range(len(users)):
    for j in range(len(posts)):
        for z in isLike:
            if z[0] == users[i] and z[1] == posts[j]:
                count = 1
                break
            else:
                count = 0
        result.append([users[i],posts[j],count])

for i in result:
    print(i)


# for i in newArr:
#     print(i)
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if(arr[i][j] > 3.5) :
#             print(str(i)+","+str(j)+","+str(arr[i][j]))
#     print()
