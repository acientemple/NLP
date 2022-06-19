s=''' 侵蚀;锈corrupt a．腐化的,贪污的 v．腐蚀;贿赂cortex n．皮质cosmetic n．化妆品 a．化妆用的,美容的cosmic a．宇宙的,广大无边的cosmos n．宇宙;秩序,
 和谐costal a.肋骨的costume   n.服装,戏装cottage   n.村舍,别墅council n．理事会,委员会,议事机构counsel n．商议;忠告;法律顾问,辩护人 v．劝告,忠告countenance 
 a．面部表情;脸色countyn;郡,县courteous a．有礼貌的courtesy n．礼貌;殷勤;好意cousin n．堂(表)兄弟,堂(表)姐妹covert a．隐藏的;暗地里的coward n．懦夫cozy 
 n．暖和舒服的;舒适的crack n．裂纹,龟裂 v．破裂,砸开;发爆炸声cradle n．摇篮;婴儿时期cramp n．夹,钳;(病性)痉挛,绞痛crane n．鹤;起重机 '''
import re
def ch_n_en(s): #中文和英文之间插入回车键
    pattern='[\u4e00-\u9fa5][a-zA-Z]'
    while re.search(pattern,s):
        start=re.search(pattern,s).span()[0]+1
        end=re.search(pattern,s).span()[1]-1
        s=s[:start]+'\n'+s[end:]
    return s
def delete_n(s):
    pattern='\n[ ][a-z].|\n[ ][\u4e00-\u9fa5]|\n[\u4e00-\u9fa5]'
    while re.search(pattern,s):
        start=re.search(pattern,s).span()[0]
        end=re.search(pattern,s).span()[0]+1
        s=s[:start]+s[end:]
    return s
print(delete_n(s))