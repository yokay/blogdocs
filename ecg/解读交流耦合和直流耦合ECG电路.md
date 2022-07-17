> 来源于ADI的一篇文档[^1]，关于交流耦合和直流耦合电路的介绍



心电信号的采集电路，从信号链的架构上可以分为两类：交流耦合、直流耦合。

## 交流耦合

交流耦合电路使用分立器件，使用电容的隔直功能将心电信号提取出来。基本架构如下图所示。

![交流耦合建构](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E5%BB%BA%E6%9E%84.png)



信号通过抗除颤、抗静电保护，经过低通滤除高频干扰，进入全差分放大电路低倍放大后，使用高通滤除低频干扰，然后经过高倍放大，最后进入低精度ADC转换为数字信号。

由于使用了电容的交流耦合功能，对于低频的肌电干扰、工频干扰和基线漂移抑制作用较低。因为高通的截止频率设置的为心电的最低频率0.1Hz左右，对于50Hz/60Hz、1Hz这种信号无法滤除，电路本身的缺点导致信号的质量不佳。

上面的架构，为了提高信号质量，也要做屏蔽驱动、右腿驱动电路，甚至需要做WCT（威尔逊中心点）。

使用TI-TINA对该架构进行仿真，如下图所示。

![交流耦合仿真电路](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF.png)



将皮肤阻抗，线缆分布电容、电阻都考虑在内，使用屏蔽驱动和右腿驱动，通过差分放大（此时输出的信号为直流耦合信号），经过大电容耦合（此时为交流耦合信号），最终经过高倍放大输出信号。

差分放大11倍，后级放大80倍，总共880倍。

使用真实信号进行仿真，结果如下图所示。

![交流耦合仿真电路-结果](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF-%E7%BB%93%E6%9E%9C.png)



VG1为共模工频干扰，经过屏蔽驱动和右腿驱动后输出反相信号VF2，正好与VG1抵消。从结果上看工频干扰已被滤除，心电信号经过前级匹配电路时有衰减，但是经过后级放大，信号范围为：2~4V，已达到常规ADC的识别范围。

再来分析下CMRR，将差分的正相、反相输出短路，使用VG1作为共模输入信号，仿真VF1的频率特性，对右腿电路中的RG进行扫描仿真（设置值范围为100K~10M）。如下图所示。

![交流耦合仿真电路-CMRR结果](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF-CMRR%E7%BB%93%E6%9E%9C.png)



可见，对于1kHz以下的信号，CMRR<-100dB，抑制能力很高。

下面对稳定性进行仿真（将屏蔽驱动去掉），如下图所示。

![交流耦合仿真电路-震荡](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF-%E9%9C%87%E8%8D%A1.png)





可见，使用初始条件（1mV）进行仿真会出现震荡，说明右腿不稳定。

给右腿加上相位补偿后，如下图所示。

![交流耦合仿真电路-补偿后不震荡](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF-%E8%A1%A5%E5%81%BF%E5%90%8E%E4%B8%8D%E9%9C%87%E8%8D%A1.png)

通过稳定性分析，如下图所示（这里使用[^4]的仿真方式，与TI教程中所述不同，后续会对稳定性分析进行说明）。

![交流耦合仿真电路-稳定性分析](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF-%E7%A8%B3%E5%AE%9A%E6%80%A7%E5%88%86%E6%9E%90.png)

Aol与1/β的幅频曲线滚降差值小于40dB/Decade，系统为稳定状态。至于相位补偿的值可以参考[^2]来设定。

对于消费类电子，上面的优化可以省略，右腿驱动直接接地，然后对地取各肢体导联的信号，最终通过加减法算出通道的值。

![交流耦合建构2](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E5%BB%BA%E6%9E%842.png)

在ADI的文档中如下图所示。

![交流耦合电路](https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E7%94%B5%E8%B7%AF.png)

该消费类对于干扰抑制较低，只有在平静且空旷的环境或者家居环境下才能达到较好的效果。

交流耦合电路需要将心电信号放大到MCU内部ADC的识别要求，一般需要放到800~1000倍甚至更高，以达到ADC采样要求。当然放大倍数越高导致噪声放大越高，共模抑制比相应降低，而低精度的ADC转换后的信号质量也会降低。

## 直流耦合

直流耦合电路相对来说简单许多，其通过保护电路后，直接经过低通滤波，然后进入集成芯片中。

![直流耦合建构](https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%9B%B4%E6%B5%81%E8%80%A6%E5%90%88%E5%BB%BA%E6%9E%84.png)

当然，集成芯片内部的电路架构跟交流的相似，都是内部差分放大、内部WCT和RLD。但是直流耦合不适用高通滤波器来拾取心电信号，而是直接获取整个带直流的信号，经过算法处理来达到基线纠偏、高频滤波等功能。

直流耦合内部使用ΣΔ ADC，可以达到很高位数（高精度），可以获取到uV甚至nV级别的信号。而心电信号本身只有mV，高精度的ADC采样能获取准确的心电信号。多余的工作交给算法来处理，可以极大的降低硬件成本，而效果还可以得到提高。

直流耦合和交流耦合比较如下表所示。

![直流交流耦合建构比较](https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%9B%B4%E6%B5%81%E4%BA%A4%E6%B5%81%E8%80%A6%E5%90%88%E5%BB%BA%E6%9E%84%E6%AF%94%E8%BE%83.png)



目前，大部分心电电路使用直流耦合架构，然后使用专业的算法来处理数据。



以上仿真文件，见[^3]

[^1]: [心电图(ECG)解决方案](https://www.analog.com/media/cn/technical-documentation/apm-pdf/adi-ecg_solutions_cn.pdf)

[^2]: [TI 高精度实验室](http://www.ti.com.cn/ww/seminars/PLAB/Operational-Amplifiers.html)
[^3]: [仿真文件](http://www.ivixivi.com/f/198b12984e034de9b281/?dl=1)
[^4]: [Signal chain basics Analyzing RL drive in ECG front end with SPICE](http://www.mythbird.com:8000/f/e8467125345f4caca930/?dl=1)

