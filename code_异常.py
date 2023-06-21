try:
    fp=open('tt.txt','r')
    fp.read()
except FileNotFoundError:
    print('没有此文件。')