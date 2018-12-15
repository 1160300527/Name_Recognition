def test(path):
    file = open(path)
    tags = 0#被标记字的总数
    right = 0#标记正确的数目
    precisionTags = 0#所有标记出来的数目
    recallTags = 0#应该被标记的字的数目
    for line in file:
        line = line.strip()
        if(len(line)==0):
            continue
        tags += 1
        _word, tag_real, tag_point = line.split()
        if tag_point == tag_real and tag_point != 'O':
            right += 1
        if tag_point != 'O':#被标注的数据
            precisionTags += 1
        if tag_real != 'O':#应该被标注的数据
            recallTags += 1
    precision = float(right)/precisionTags
    recall = float(right)/recallTags
    f1Score = 2*precision*recall/(precision+recall)
    print("precision:%f, recall:%f, F1Score:%f\n"%(precision,recall,f1Score))


test('test.rst')
