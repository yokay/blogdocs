# 自制TFrecords数据集训练

本文是将ECG的mat文件转换为TFrecords，并进行CNN训练[^1]。

## 数据集

TEST和TRAIN为格式为".mat"的心电数据，数据集来自中国心电智能大赛，共1000例常规心电图，训练集600例，测试集400例。该数据是从多个公开数据集中获取。有正常/异常两类标签的训练集数据，需要在没有标签的测试集上做出预测。

其中采样率为500 Hz，格式为MAT格式。该文件中存储了12个导联的电压信号。训练数据对应的标签存储在txt文件中，其中0代表正常，1代表异常。

文件数如下图所示。

![image-20230719220301069](https://s2.loli.net/2023/07/19/z8XC3RmQyxn2g74.png)

读取数据可知采样时间是10s，则每个mat文件的数据维度为（5000，12），即有12导，各5000个点。

TRAIN数据有600，TEST数据有400，则可建立的TRAIN_DATA维度为（600，5000，12），TEST_DATA维度为（400，5000，12）。

Label数据可用OneHot表示（1，2）。

这里建立2个TFrecord文件，一个TRAIN_DATA，一个TEST_DATA。

## 库文件

导入所需库文件，读取mat、csv文件，使用pandas处理数据。

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/1&cellId=0" title="Jovian Viewer" height="404" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

## 文件读取

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/5&cellId=1-4" title="Jovian Viewer" height="800" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

读取mat文件

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/6&cellId=5" title="Jovian Viewer" height="328" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

## 创建TRAIN的TFRecord 文件

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/6&cellId=6" title="Jovian Viewer" height="704" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

1. 创建writer
2. 创建存储类型tf_feature
3. 转换并序列化

这里，将mat数据data转换为numpy array再转换为bytes存储为string格式，name存储mat文件路径，label存储标签的OneHot，shape存储后续读取data格式时的维度信息。

## 读取TFRecord文件

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/7&cellId=8" title="Jovian Viewer" height="800" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

1. 导入TFRecord
2. 解析feature信息
3. 数据增强

这里，解析的feature信息的数据格式需要与之前的对应。tensorflow的dataset提供了`Dataset.map(func)`，将dataset中的所有条目按照`feature_description`进行映射。

然后进行重复、打乱、生成小样本。

获取TFrecord的数据内容进行确认。

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/7&cellId=9" title="Jovian Viewer" height="249" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

最后生成训练数据集和标签。

<iframe src="https://jovian.com/embed?url=https://jovian.com/yokay/ecgcnndataset-one/v/7&cellId=10-11" title="Jovian Viewer" height="354" width="100%" style="margin 0 auto; max-width: 800px;" frameborder="0" scrolling="auto"></iframe>

TEST数据集生成TFrecord格式文件方式一样，这里不再赘诉。



整个文件的生成和训练源码见[ecgcnndataset-one](https://jovian.com/yokay/ecgcnndataset-one)



[^1]: [Tensorflow 2.0 TFrecord的输出与读入]()https://blog.csdn.net/qq_42686721/article/details/98205816

