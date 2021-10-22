> 以《YY 0885-2013 医用电气设备 第2部分：动态心电图系统安全和基本性能专用要求》为准
>
> 通过仿真分析，判断电路是否满足规范要求。

## 范例

引用一个Holter的技术指标，用于说明标准[^1]。部分技术指标如下图所示。

<img src="http://www.mythbird.com:8000/f/89da9cae6dd44a39aead/?dl=1" style="zoom:50%;" />



其频率响应为`0.05Hz~60Hz`。查看标准P15页（51.5.9）章，如下图所示。

<img src="http://www.mythbird.com:8000/f/35c9aec57b504e639714/?dl=1" style="zoom: 50%;" />

由于频率为带通，高通截止频率为0.67Hz或者0.05Hz，低通截止频率为40Hz或者55Hz。

先对0.67Hz和0.05Hz进行仿真[^2]。仿真电路如下图所示。

<img src="http://www.mythbird.com:8000/f/b603cafd38f84fe9bdf0/?dl=1" style="zoom:50%;" />

- 使用3mV/100ms方波信号，观察输出波形。仿真结果如下图所示。

![](http://www.mythbird.com:8000/f/7223fd17b9df4185ac67/?dl=1)

可见，由于20k的对地电容，放电较快，斜率较高。而300k对地电容放电慢，斜率低。

从图中可见300k电阻的斜率基本为0，计算得20k电阻得斜率为15.43mV/s，而300k电阻斜率为0.237mV/s，可见后者满足标准要求。

<img src="http://www.mythbird.com:8000/f/e3a16584baa848b4bcb7/?dl=1" style="zoom: 80%;" />

这也说明只有截止频率为0.05Hz时才能满足a）测试条件。

实际应用中心电信号本身的最低频率就是0.05Hz，如果高于该频率，会导致心电信号畸变。





## Reference:

[^1]: [**智能动态心电图分析系统**](http://beneware.com.cn/pages/product_detail01.html)
[^2]: [Why005Hz](http://www.mythbird.com:8000/f/27680b2909fc4b13a5aa/?dl=1)

