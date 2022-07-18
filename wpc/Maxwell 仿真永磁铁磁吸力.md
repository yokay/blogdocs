# Maxwell 仿真永磁铁磁吸力

## 选择Magnetostatic

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806004718400.png" alt="" style="zoom:50%;" />

## 建立一个Project variable

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010204712.png" alt="" style="zoom:50%;" />

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010226823.png" alt="" style="zoom:80%;" />

这个**offset**作为磁铁距离偏移的变量。

## 新建2个圆柱体磁铁

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010055266.png)

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010019947.png" alt="" style="zoom:67%;" />

第2个圆柱体磁体为小磁体。完成后如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010422756.png" alt="" style="zoom:50%;" />

## 新建一个空间

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010524357.png)

也可以新建region。

## 给磁体定义材料

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010625638.png" alt="" style="zoom:67%;" />

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010715995.png)

在材料里面打开Arnold的磁性库，选择N52（20°）的材料，作为2个圆柱体磁铁的材料。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010838618.png)

在材料查看中，定义磁化方向为Z轴正向。

## 选择Force目标

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806010959965.png" alt="" style="zoom:67%;" />

选择小磁铁作为磁吸力仿真的目标。此处仿真的是小磁铁的受力情况，注意不要选择2个磁体。

## 新建分析设置

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011121372.png)

使用默认设置。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011156829.png" alt="" style="zoom:67%;" />

## 添加变量参数

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011225684.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011329324.png)

选择offset变量作为变化的参数，设置变化值。可以在table中查看结果。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011422613.png)

## 开始仿真

选择不带参数仿真，从Analysis中选择Setup1进行Analyze。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011504222.png)

选择带参数仿真，从Optimetrics中选择ParametricSteup1进行Analyze。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011451091.png)

## 查看仿真结果

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011624236.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011700070.png)

可见Z方向offset=0mm时，小磁铁所受到的力为1.9365N。

## 查看offset和磁吸力的关系

新建一个方框图表。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011824665.png)

选择吸力作为数据显示。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011907929.png)

结果如下图所示。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210806011947452.png)

可见距离越远吸力越小。



## Reference

[^1]:[源文件](http://www.ivixivi.com/f/64f0c668461641cbadc2/?dl=1)

