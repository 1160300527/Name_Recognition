# Name_Recognition
中文名实体识别——地名识别（win10环境下使用CRF++完成）
采用1998年人民日报分词数据集，文件为renmin.txt
执行过程如下：
1.执行setTag.py文件(python setTag.py)，用以生成CRF++格式标注的训练集以及测试集数据
2.执行crf_learn -f 3 -p 8 template.txt train.txt model命令,生成模型（template可修改）
3.执行crf_test -m model  test.txt > test.rst命令，将该模型在测试集数据上进行测试，标注结果写到test.rst文件中
test.rst文件格式如下:
进行标记的字  完成的标记   真正的标记
4.执行testResult.py文件(python testResult.py)，查看识别效果
