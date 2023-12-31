# ECG信号提取——前置滤波电路

由于ECG信号很微弱，处于mV级别，还有很多干扰信号，所以采集信号时需要进行滤波和放大处理，然后使用模数转换。为了滤波高频干扰和工频噪声，需要使用低通滤波器和陷波器抑制噪声，有时也要使用高通滤波器滤除低频噪声。信号滤除干净后有两种处理方式：

- 放大后进行ADC处理
- 使用高精度ADC采样

前者将信号放大几百倍，满足ADC的输入范围，这种情况用于低分辨率的ADC，比如16bit，大部分使用独立器件堆叠电路。

后者直接获取微弱信号，使用高分辨率ADC（一般为∑-ΔADC），比如24bit，精度可达到uV，一般使用集成器件。

在进入ADC之前的处理称为模拟前端。



根据ADI官网介绍，ECG信号的采集方式分为：交流耦合和直流耦合。具体资料见[^1]

ECG测量的基本电路框图如下所示。

![ecg基本电路](https://mythidea.oss-cn-beijing.aliyuncs.com/ecg%E5%9F%BA%E6%9C%AC%E7%94%B5%E8%B7%AF.png)

其原理可以参考[ECG信号](https://www.mythbird.com/ECG%E4%BF%A1%E5%8F%B7/)内容。

一般其技术指标类似：

1. 输入阻抗：≥5MΩ
2. 输入偏置电流：<2nA
3. 等效输入噪声：<30uVpp
4. 共模抑制比：50Hz正弦信号的共模抑制比≥90dB
5. 耐极化电压：±300mV
6. 漏电流：<30uA
7. 频带：0.05～100Hz



采集心电信号时，使用电极片贴在人体上，再连接到板卡上，通过滤波、放大后进入ADC，最终转换为电压信号。由于人体信号微弱，且人体存在一定的电阻，所以电极片与人体间会有极化电压[^2]；另外导联线通常是屏蔽线缆，线缆过长会有线缆阻抗，出现共模电压和差模电压，导致信号有直流量，影响放大电路的输入电压。故前端电路首先要处理的就是干扰、共模和差模信号，然后才是放大信号。

前置滤波多使用RC电路，根据ECG信号频率，可知心电信号截止频率为0.1Hz~200Hz处，通常将通带范围设定在该区域就可以保证获取到正常的心电信号。但是心电监护测量参数不仅仅包含心电信号，还有pace检测和呼吸波（呼吸阻抗测量）。

```html
Note:
人体呼吸运动时，胸壁肌肉运动导致胸廓交替变形，肌体组织的电阻抗也交替变化，  
变化量约为0.1ohm~3ohm，称为呼吸阻抗。
```

pace信号为起搏器（pace maker)所产生，形态上为脉冲信号，宽度为0.1ms~2ms，频率约为500Hz~1kHz。  

呼吸阻抗测量通常使用交流载波10kHz以上的信号。

综上，需要考虑是否需要测量pace和呼吸波，据此可以得出前置滤波电路截止频率设定一般为200Hz、1kHz、10kHz、30kHz、50kHz等。

使用TI TINA进行RC仿真，电路如下所示。

![LPecg](https://mythidea.oss-cn-beijing.aliyuncs.com/LPecg.png)



仿真结果如下所示。

![LPecgresult](https://mythidea.oss-cn-beijing.aliyuncs.com/LPecgresult.png)



可见三者截止频率（-3dB）分别为：2.37kHz，88kHz，4.8kHz。  

第一个使用二级RC滤波电路，需要测量pace信号。

第二个使用一级RC滤波，需要测量pace和呼吸波。

第三个使用一级RC滤波，需要测量pace信号。

可见对于高于100kHz的信号均有抑制作用。



## 抗高频干扰

ECG信号通过导联线连接到电极上，电极粘贴在人体上。这部分信号会引入很多干扰，包括高频和低频信号。由于ECG有效信号为低频信号，故使用低通滤波器滤除高频信号。常使用RC滤波电路，有时为了增加滚降率（增强高频衰减）使用多级RC滤波电路。

如上图所示，若使用一级RC，则只有20dB/Decade，二级则有40dB/Decade，可以增强低通滤波器的抑制能力。



## pace信号检测

标准对需要捕获的起搏器信号的高度和宽度等具体要求有所差异[^3]。

- AAMI EC11:1991/(R)2001/(R)2007
- EC13:2002/(R)2007, IEC60601-1 ed. 3.0b, 2005
- IEC60601-2-25 ed. 1.0b
- IEC60601-2-27 ed. 2.0, 2005
- IEC60601-2-51 ed. 1.0, 2005

IEC60601-2-27规定：

*设备须能够显示存在幅度为±2 mV至±700 mV、持续时间为0.5 ms至2.0 ms的起搏器脉冲的心电图信号。显示屏上的起搏器脉冲应清晰可见，折合到输入端(RTI)的幅度不得小于0.2 mV；*

AAMI EC11则规定：

*设备须能显示存在幅度为2 mV至250 mV、持续时间为0.1 ms至2.0 ms、上升时间少于100 µs且频率为100 脉冲/分的起搏器脉冲的心电图信号。对于持续时间为0.5 ms至2.0 ms（幅度、上升时间和频率参数如上一句所规定）的起搏器脉冲，必须在心电图中显示该起搏器脉冲；显示屏上应予以清晰的展现，折合到输入端的幅度不得小于0.2 mV。*



因为pace信号中心频率为5kHz，为了拾取pace信号，带宽不能太低。若不需要pace信号，可以降低带宽到200Hz。

对于pace信号，选择5kHz之前的需要对pace信号进行放大处理，因为会被低通滤波器衰减。不过pace脉冲可达100mV，即使被衰减也不会比心电信号还难拾取，例如上图中2.5kHz截止频率造成pace信号变弱为0.22*100mV=22mV，但是考虑到小幅度的pace信号还是要考虑后级放大处理，同时也要抑制原始ECG信号防止被放大从而干扰pace检测，这也决定了通过硬件上检测时要使用**带高通性质的微分电路**[^4]。

使用微分电路的优点：

- 滤除原始心电信号
- 检测脉冲上升沿和下降沿，而不是电平
- 隔离直流信号

能检测出脉冲波的形态，检测电平有可能会是阶跃信号，而阶跃信号不能识别为pace。

```html
Note:
最小pace信号：100us/2mV
最大pace信号：2ms/700mV或者2ms/250mV
```



#### 工作原理

具有放大功能的微分电路如下所示[^5]。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E5%BE%AE%E5%88%86%E7%94%B5%E8%B7%AF.png" alt="微分电路" style="zoom:50%;" />



高通的截止频率由C1和R1决定，C2进行相位补偿，R2调节比例。其中C1也可以称为“隔直电容”，用于通交流阻直流。脉冲信号的交流部分通过，直流部分被抑制。

在后面使用双路阈值（窗口阈值）比较电路进行输出（双阈值表示上升沿阈值和下降沿阈值），如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E5%8F%8C%E8%B7%AF%E9%98%88%E5%80%BC%E6%AF%94%E8%BE%83.png" alt="双路阈值比较" style="zoom:33%;" />

使用2mV/100us的方波进行仿真简单的微分电路（高通滤波器），如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/Snipaste_2020-04-06_17-57-55.png" alt="Snipaste_2020-04-06_17-57-55" style="zoom:25%;" />

![高通波形](https://mythidea.oss-cn-beijing.aliyuncs.com/%E9%AB%98%E9%80%9A%E6%B3%A2%E5%BD%A2.png)

![微分电路仿真结果](https://mythidea.oss-cn-beijing.aliyuncs.com/%E5%BE%AE%E5%88%86%E7%94%B5%E8%B7%AF%E4%BB%BF%E7%9C%9F%E7%BB%93%E6%9E%9C.png)



在方波上升沿和下降沿都有电容放电现象，结果为斜波。下降/上升的时间与RC（时间常数）有关。

分析比较电路。V1>V2。Vout>V1时，输出低电平。Vout<V2时，输出低电平。V2<Vout<V1时，输出高电平。平时输出高电平。可见检测的是“尖尖”。当然如果放大倍数过高，可能“尖尖”会被削顶。需要考虑的是“尖尖”的宽度是否能被比较器检测到，以及太宽后导致比较器一直输出高电平，两者或多或少都会对判断产生影响。

从图上所示，经过高通后波形会变为负的，中心电平为0V。为了方便电路使用单电源给运放供电，需要将电平拉高到0V以上，放大到负电压时会强制拉低。

假设运放为3.3V供电，则偏置电压选为3.3V/2=1.65V能保证输入范围最大。假设最小信号放大A倍，则最小信号放大后的输出电压为：A*±2mV+1.65V。当A=825时，最小信号会放大到3.3V和0V，从上图可知在低电平地方宽度会大一些，可以将放大倍数提高，因为比较器可能无法捕捉到小脉宽的信号。

完整的仿真电路如下图所示。

![pace检测电路](https://mythidea.oss-cn-beijing.aliyuncs.com/pace%E6%A3%80%E6%B5%8B%E7%94%B5%E8%B7%AF.png)

设定的阈值为2.7V/2.3V。

对2mV/100us脉冲进行时域仿真，结果如下图所示。

![pace检测电路仿真结果](https://mythidea.oss-cn-beijing.aliyuncs.com/pace%E6%A3%80%E6%B5%8B%E7%94%B5%E8%B7%AF%E4%BB%BF%E7%9C%9F%E7%BB%93%E6%9E%9C.png)

在低于2.3V后输出低电平，之后高于2.3V时输出高电平。

其幅频特性如下图所示。

![pace检测电路幅频特性](https://mythidea.oss-cn-beijing.aliyuncs.com/pace%E6%A3%80%E6%B5%8B%E7%94%B5%E8%B7%AF%E5%B9%85%E9%A2%91%E7%89%B9%E6%80%A7.png)

最大放大倍数为44.38dB=165，最小电压为2.5-165*2m=2.17V，与仿真结果相差不大。

仿真原始文件见[^6]。

#### 器件选择

##### 阻容

使用1%精度电阻，同时需要左WCA分析（Worst Case Analysis），看最差情况下的阈值范围。

##### 运放

小信号的pace幅度只有2mV，大信号有700mV，采用放大电路放大该斜波输入信号，则SR（压摆率）=V/t。放大电路中运放需要高带宽，高压摆率。

pace为高速信号，故宜采用高速比较器，同时tail-to-tail。

##### 第二种电路

完整电路如下图所示。采用双电源供电，能保证负脉冲信号能检测导。

![pace检测电路2](https://mythidea.oss-cn-beijing.aliyuncs.com/pace%E6%A3%80%E6%B5%8B%E7%94%B5%E8%B7%AF2.png)

同样，仿真结果如下图所示。

![pace检测电路2仿真结果](https://mythidea.oss-cn-beijing.aliyuncs.com/pace%E6%A3%80%E6%B5%8B%E7%94%B5%E8%B7%AF2%E4%BB%BF%E7%9C%9F%E7%BB%93%E6%9E%9C.png)

幅频特性如下图所示。

![pace2检测电路幅频特性](https://mythidea.oss-cn-beijing.aliyuncs.com/pace2%E6%A3%80%E6%B5%8B%E7%94%B5%E8%B7%AF%E5%B9%85%E9%A2%91%E7%89%B9%E6%80%A7.png)

最大放大倍数为46dB=200，最小电压为2.5-2m*200=2.1V，与仿真结果相差不大。

仿真原始文件见[^7]。

##### 第三种电路

使用单电源，但是信号来源于PGA的输出。基本电路如下图所示。

![image-20210208235549979](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210208235549979.png)

后面是将U2运放作为比较器使用，故当VM2为负电平时无法起到放大作用，而输出0（低电平）。该电路只能检测出pace信号上升沿，不能检测下降沿。R5为了保证输入信号平衡，为R4||R6=4.1k。

VM2处信号的幅频特性如下图所示。

![image-20210208235938981](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210208235938981.png)

最大放大倍数为48.48dB=265，最小电压为2m*265=0.53V，与仿真结果相差不大。

仿真原始文件见[^16]。

## 抗工频干扰

工频干扰来自常规用电中的交流电。由于市电为交流电，所有使用市电的设备都会与人体产生同频的干扰，导致干扰会通过导联线进入系统。如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E5%85%B1%E6%A8%A1%E5%B9%B2%E6%89%B0%E6%A8%A1%E5%9E%8B.jpg" alt="共模干扰模型" style="zoom:50%;" />

市电网络与人体，人体和大地都有等效电容存在，而市电为交流，则人体上会有分压，频率与市电一样。其产生的微弱电流为“位移电流”。

以单导测量为例，分析“位移电流”的影响。如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%B7%A5%E9%A2%91%E5%B9%B2%E6%89%B0%E5%B1%8F%E8%94%BD%E9%A9%B1%E5%8A%A8.jpg" alt="电缆工频干扰屏蔽驱动" style="zoom:50%;" />

位移电流*i*db会造成共模电位Vc=*i*db*ZG，该共模电压为Vc，阻抗为Zin。两个电极位置的阻抗分别为Z1和Z2，则Vout计算公式如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E4%BD%8D%E7%A7%BB%E7%94%B5%E6%B5%81%E8%AE%A1%E7%AE%97.png" alt="位移电流计算" style="zoom:33%;" />

先后为差模电压放大Gd倍，然后是屏蔽电缆共模差压放大Gd倍，最后是差分信号放大Gd倍。

从公式中可知，Vc对输出有影响，其与运放的CMRR有关，与电极位置的阻抗和运放的输入阻抗有关。为了减小影响，可以做以下措施：

- 提高CMRR
- 提高输入阻抗
- 降低电极位置的阻抗差异



对于浮地设备，电缆也会引入干扰。如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%B7%A5%E9%A2%91%E5%B9%B2%E6%89%B0.jpg" alt="电缆工频干扰" style="zoom:50%;" />

假定：引线1中的电流是*i*d1，引线2中的电流是*i*d2，接地回路的电流=*i*d1+ *i*d2。因Z1和Z2的不一致而转变为差模电位：V+ –V- = *i*d1*Z2 – *i*d2*Z1= *i*d (Z2 –Z1)。为了降低电缆造成的干扰，可以做以下措施：

- 降低电极位置的阻抗差异
- 降低id，将屏蔽线接地

电缆上得分布电容C1、C2一般为100pF/m。

如果直接使用市电供电，一定会引入工频干扰。



针对措施有以下几种：

##### 屏蔽驱动

电缆的干扰是由于市电与电缆，电缆和地之间有等效电容（屏蔽线接地），产生感应电流（或者也可以是电容分压）。如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%B7%A5%E9%A2%91%E5%B9%B2%E6%89%B0%E7%94%B5%E6%B5%81.jpg" alt="电缆工频干扰电流" style="zoom:50%;" />

加入共模电压为Vc，如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%85%B1%E6%A8%A1%E8%BD%AC%E5%B7%AE%E6%A8%A1jpg.png" alt="电缆共模转差模jpg" style="zoom:50%;" />

由于Rs、C不一样，导致进入运放得Uic1和Uic2不一样，产生差模电压Uid。其产生原因如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%85%B1%E6%A8%A1%E8%BD%AC%E5%B7%AE%E6%A8%A1%E7%94%B5%E6%B5%81%E5%8E%9F%E5%9B%A0.jpg" alt="电缆共模转差模电流原因" style="zoom:50%;" />

在屏蔽线上得电压因为Rs、C不一样而不同，产生了电流ic（即id），导致输入电压不同。计算公式如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%B7%A5%E9%A2%91%E5%B9%B2%E6%89%B0%E7%94%B5%E6%B5%81%E5%80%BC.jpg" alt="电缆工频干扰电流值" style="zoom:50%;" />

其分母为共模电压。

通过屏蔽驱动，将中心电平反馈导屏蔽线上，使分布为心电信号。如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%94%B5%E7%BC%86%E5%B7%A5%E9%A2%91%E5%B9%B2%E6%89%B0%E7%94%B5%E6%B5%81%E6%B6%88%E9%99%A4.png" alt="电缆工频干扰电流消除" style="zoom:50%;" />

最终，分母为Uid（Uic+Uid/2-Uic=Uid/2），即心电信号，极大得降低了因分布电容和电阻不同导致得差模电压，消除了共模电压产生得差模电压。

屏蔽驱动是将差分输出的中心电压通过缓冲输出导屏蔽现上。

##### 右腿驱动

右腿驱动电流消除人体“位移电流”产生的影响。原理图如下所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E5%8F%B3%E8%85%BF%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF.jpg" alt="右腿驱动电路" style="zoom:50%;" />

人体位移电流产生的共模电压Vc，通过放大电路反向放大后输出Vo，其相位与Vc相反，从而达到抵消的作用（电流也是相反）。上图的等效公式如下所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E5%8F%B3%E8%85%BF%E9%A9%B1%E5%8A%A8%E7%94%B5%E8%B7%AF%E8%AE%A1%E7%AE%97%E5%85%AC%E5%BC%8F.jpg.png" alt="右腿驱动电路计算公式.jpg" style="zoom:33%;" />

具体工作原理可参考[^8][^9]。

一般将屏蔽驱动的输出给右腿驱动的输入，进行反向放大。

使用过程中，要考虑整个系统因为屏蔽驱动和右腿驱动构成了二级反馈闭环系统，整个系统存在稳定性问题。其中右腿驱动电路为放大电路，需要做好相位补偿和稳定性分析。

TI提供了屏蔽驱动和右腿驱动的仿真电路，见[^10]

##### 电气隔离

使用隔离变压器、隔离放大器、光耦，将市电与板卡隔离，可以有效的降低工频干扰。



# 等效输入阻抗

输入阻抗是指一个电路的输入端的等效阻抗。可以理解为在输入端加上电压源U，测量输入端电流I，输入阻抗Rin就等于U/I（将所有电路元件作用的效果总和，等效到一个电阻Rin上）。

等效输入阻抗对于前级电路的滤波电容有一定的要求，这个要根据标准要求进行合理设置。根据标准要求，单端输入阻抗要大于2.5Mohm@（0.67~40Hz，交流阻抗）。由于RC后级电路的阻抗一般很高（100M以上），故输入阻抗跟小值相关，即与RC有关，则输入阻抗为Rf+Cf=Rf+1/2ΠfCf≥2.5M，则Cf≤1/（2.5M-Rf）2Πf≤1/（2.5M*2Πf）=0.0016uF=1.6nF=1600pF，即使预留一倍空间也是800pF（其中不考虑Rf可以算小值）。

故RC电路的电容总值不能高于1600pF。

输入阻抗的要求对运放的选择进行了限制，因为心电信号微弱，人体阻抗高，所以必须用高阻抗的运放才可以分压分到足够多。一般使用仪表放大器。



## ESD保护

在导联线连接板卡的入口加上ESD管对地或者对电源，进行静电保护。有时为了保护后端的放大器，需要使用TVS管进行钳位。

ESD保护和TVS管钳位都需要保证符合标准中对于人体漏电流的要求，即单个电极流入人体的电流为0.1uA和总电流为1uA。选择保护管时需保证反向漏电流为0.1uA以下。

ESD保护对于双电源结构的，需要正向和方向都进行保护。



## 抗除颤

除颤信号功率很大，会直接通过导联线进入系统，为了保护后端电路，有两种方式：

- 导联线接口上埋入抗除颤电路
- 板卡上在导联线接口出按照氖管

原理上都是尽量吸收掉除颤电流，前者通过电阻发热消耗掉，后者通过电容储能。

EC13关于除颤测试电路如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E9%99%A4%E9%A2%A4%E6%B5%8B%E8%AF%95%E7%94%B5%E8%B7%AF.png" alt="除颤测试电路" style="zoom:50%;" />

C=32uF L=25mH R+RL≤11ohm RL为DC的内阻。

测试步骤：Charge the capacitor to 5000 V, with switch S1 in position A and switch S2 closed. Discharge is
accomplished by actuating S1 to position B for a period of 200 ± 100 ms. The capacitor must be
disconnected to remove residual voltages and allow recovery to commence. The discharge test is applied
at 20 s intervals in those cases where more than one discharge is indicated 。

先S1拨到A，然后拨到B放电。测试过程中S2始终闭合保持10Hz信号源短路（用于多次除颤后测试设备是否正常的信号源）。持续100~300ms，间隔20s。

#### 除颤电阻的选择

使用抗除颤电阻时，使用该电路仿真[^15]，计算除颤电阻的功率。仿真图如下所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E6%8A%97%E9%99%A4%E9%A2%A4%E4%BB%BF%E7%9C%9F%E7%94%B5%E8%B7%AF.png" alt="抗除颤仿真电路" style="zoom:50%;" />

使用时控开关控制电源，从结果可以看出在抗除颤电阻R4上有个脉冲波形，产生了脉冲电流和电压。峰值功率为30W，峰值电压达到1.72kV，脉冲时间大概为20ms。电阻必须能耐受这样的条件，否则无法满足要求。

由于波形近似为三角波，需要等效为脉冲方波（一般Datasheet中会有脉冲方波与峰值功率的对于曲线）。等效原理如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E7%AD%89%E6%95%88%E6%96%B9%E6%B3%A2%E5%9B%BE.png" alt="等效方波图" style="zoom:67%;" />

其他波形等效如下图所示。

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E6%B3%A2%E5%BD%A2%E7%AD%89%E6%95%88%E5%9B%BE.png" alt="波形等效图" style="zoom: 67%;" />

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/%E6%94%BE%E7%94%B5%E6%97%B6%E9%97%B4%E5%B8%B8%E6%95%B0.png" alt="放电时间常数" style="zoom:67%;" />

示例中时间常数t=7.15ms，故等效脉冲宽度T=7.15ms/2=3.575ms。

峰值功率为P=(1.72kV)^2/100k=29.584W，仿真结果为30W。

则100k电阻需满足：1.72kV/3.575ms脉宽的脉冲信号峰值功率能达到30W。

若考虑降额，比如以60%为准。则脉冲电压为1.72kV/0.6=2.87kV，脉冲功率为30W/0.6=50W。

详细说，可参考[^11]。

#### 陶瓷气体放电管的选择

除颤脉冲信号峰值电压为5kV，可选择陶瓷气体放电管（氖管）将电压降低到几十伏，然后通过钳位二极管钳位到电源电压。（陶瓷气体放电管[^12]英文名称为`Gas Discharge Tubes`）

一般来说，当击穿电压超过系统绝缘的耐电强度时，放电管被击穿放电，从而在短时间内限制浪涌电压及减少干扰
能量。当具有大电流处理能力的弧光放电时，由于弧光电压低至几十伏，可以防止浪涌电压进一步上升。气体放电
管即利用这一自然原理实现了对浪涌电压的限制[^13]。

GDT电容容量一般为pF级别，将仿真文件中的100k电阻换成1pF电容，仿真得电容两端得脉冲信号最大值为700V/19.6ms，该值为需要考虑得脉冲击穿电压。

由于GDT最终电压会在10~35V，此时需要考虑该电压与系统电压差造成得最终电流，是否会导致弧光放电状态持续，弧光放电持续会导致GDT处于“短路”状态（弧光形成形成通路）。

在快速脉冲冲击下，陶瓷气体放电管气体电离需要一定的时间（一般为0.2～0.3μs，最快的也有0.1μs左右），因而有一个幅度较高的尖脉冲会泄漏到后面去。若要抑制这个尖脉冲，有以下几种方法：a、在放电管上并联电容器或压敏电阻；b、在放电管后串联电感或留一段长度适当的传输线，使尖脉冲衰减到较低的电平；c、采用两级保护电路，以放电管作为第一级，以TVS管或半导体过压保护器作为第二级，两级之间用电阻、电感或自恢复保险丝隔离[^14]。

由于除颤仿真电路一样，可知GDT得脉冲击穿电压在600~800V之间。而直流击穿电压应该大于系统电源电压，否则会导致其直流击穿导通。TVS管选择直流击穿电压作为反向击穿值，钳位电压为系统电源电压，防止直流情况下GDT直流击穿导通。



## 抗电刀

电刀为高频干扰，为几百KHz频率。常用的做法是，电缆中埋电感，使用低通滤波器抑制高频。同时电刀有辐射干扰，给模拟电路甚至整个板卡装上屏蔽罩都是需要的。



### Reference

[^1]: [心电图(ECG)解决方案](https://www.analog.com/media/cn/technical-documentation/apm-pdf/adi-ecg_solutions_cn.pdf)

[^2]: [极化电压](https://www.mythbird.com/polarization-voltage.html)

[^3]: [检测并区分心脏起搏伪像](https://www.analog.com/cn/analog-dialogue/articles/detecting-and-distinguishing-cardiac-pacing-artifacts.html)
[^4]: [积分电路和微分电路的工作原理](https://blog.csdn.net/weixin_42562514/article/details/97653660)

[^5]: [Hardware Pace using Slope Detection](http://www.ivixivi.com/f/1440b94ef81644f88543/?dl=1)

[^6]: [pace检测仿真文件](http://www.ivixivi.com/f/2d4811f003f24729a6e7/?dl=1)
[^7]: [pace检测仿真文件第二种](http://www.ivixivi.com/f/aba13a2343714ccfa818/?dl=1)
[^8]: [Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier](http://www.mythbird.com:8000/f/988a750cc96e4cfeb72f/?dl=1)
[^9]: [Driven-Right-Leg-Circuit-Design](http://www.mythbird.com:8000/f/405525168ab9470dbbc0/?dl=1)
[^10]: [TI右腿驱动仿真电路](http://www.ivixivi.com/f/9f275ef3cb1947a09a85/?dl=1)

[^11]: [金属氧化膜电阻的浪涌设计](http://www.mythbird.com:8000/f/c0b219c20e324ca7a28e/?dl=1)
[^12]: [ESD/浪涌保护器件使用方法：浪涌放电管](https://product.tdk.com/info/zh/products/protection/voltage/arrester/technote/apn-arrester.html)
[^13]: [气体放电管和开关放电器](https://www.tdk-electronics.tdk.com.cn/download/141146/cd5c162f22ef4033d690e30b4bc8e7cb/surge-arrester-pp--cn.pdf)
[^14]: [放电管如何有效防止瞬时过电压](http://www.ruilon-gdt.com/news_view.asp?id=298)

[^15]: [抗除颤仿真文件](http://www.ivixivi.com/f/4d1e6062aa594445a8a7/?dl=1)
[^16]: [pace仿真文件第三种](http://www.ivixivi.com/f/c720f57ae1284657924f/?dl=1)

