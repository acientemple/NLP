import json
# fp=open('test.txt','w')
# name=['jame','henry']
# # fp.write('hello world!')
# name=json.dump(name,fp)
# # fp.write(name)
# fp.close()
fp=open('test.txt','r')
# data=fp.read()
# data=json.loads(data)
data1=json.load(fp)
fp.close()
print(data1)