import re

def getline(line):
    index = line.find('/')#该行是否为有效数据
    chars = []
    tags = []
    if index!=-1:#包含信息
        line = line.strip()#去除换行
        line = line[index+2:]#去除时间信息
        line = line.strip(' ')
        temp = ""
        #print(line.split())
        for word in line.split():
            #print(word)
            w,tag = word.split('/')
            #print(w)
            #print(tag)
            if temp=="":
                if(w[0]=='['):
                    #print(w[1:])
                    temp = w[1:]
                    continue
                chars.extend(w)
                l = len(w)
                if(tag=='ns'):#匹配地名
                    if(l==1):#单个字符
                        tags+='S'
                    else:
                        tags+=('B'+'M'*(l-2)+'E')
                else:
                    tags+='O'*l
            else:#合并括号信息
                i = tag.find(']')
                temp+=w
                if i != -1:
                    tag = tag[i+1:]
                    chars.extend(temp)
                    l = len(temp)
                    if(tag=='ns'):
                        if(l==1):
                            tags+='S'
                        else:
                            tags+=('B'+'M'*(l-2)+'E')
                    else:
                        tags+='O'*l
                    temp=""
            #print(chars)
            #print(tags)
    return (chars,tags)

def writeTofile(file,chars,tags):
    for iter in range(len(chars)):
        file.write(chars[iter]+'\t'+tags[iter]+'\n')


def readText(filePath):
    file = open(filePath)
    trainFile = open("train.txt","w")#训练集
    testFile = open("test.txt","w")#测试集
    test = 0
    for line in file:
        #print(line)
        chars,tags = getline(line)
        if(test%4==0):
            writeTofile(testFile,chars,tags)
        else:
            writeTofile(trainFile,chars,tags)
        test+=1


#getline("19980103-02-003-020/m  １９９４年/t  江/nr  泽民/nr  总书记/n  视察/v  [吕梁/ns  地区/n]ns \n")
readText("renmin.txt")
