EMI 的工程师指南

> 转自 [EMI 的工程师指南](https://e2echina.ti.com/blogs_/b/power_house/archive/2019/08/06/emi-1)by [Kevin Chen1](https://e2echina.ti.com/members/6063996)



[TOC]



## **第1部分 — 规范与测量**

### **简介**

多数电源应用必须减少电磁干扰 (EMI) 以满足相关要求，系统设计人员必须尝试各种方法来减少传导和辐射发射。

电磁兼容性 (EMC) 标准的合规性（例如，针对多媒体设备的 CISPR 32，针对汽车应用的 CISPR 25）是一项非常重要的任务，与产品开发成本和上市时间息息相关。

对于 DC/DC 转换器而言，虽然采用开关更快的电源器件可以提升开关频率并缩小尺寸，但在开关转换期间出现的开关电压和电流转换率（dv/dt 和 di/dt）有所提升，通常引起 EMI 加剧，导致整个系统出现问题。

例如，氮化镓 (GaN) 电源器件的开关速度极快，导致高频条件下的 EMI 增加 10dB。EMI 滤波器是电力电子系统不可或缺的组成部分，在总体积和总重量方面占比相对较大。因此，必须非常关注系统的 EMI 降噪和抑制，不仅要满足 EMC 规范，还需降低解决方案成本并提高系统功率密度。

本文是 EMI 系列文章的第一部分，回顾了相关标准和测量技术，主要侧重于传导发射。表 1 列出了与 EMI 有关的常用缩写和命名法。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_4.54.02.png" alt=" " style="zoom: 67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_4.54.02.png)

表 1：与 EMI 和 EMC 相关的常见缩略语、缩写和单位

### **EMC** **监管规范**

EMC 指系统或内含元器件在其电磁环境中按要求运行，不会对环境中的任何设备产生超出容限的电磁干扰的能力。此类干扰可能造成严重后果，因此各种国内和国际[监管规范](https://en.wikipedia.org/wiki/List_of_common_EMC_test_standards)中均设立了 EMC 条款。

在欧盟区域内，通信市场销售的电源产品多年来通常采用 EN 55022/CISPR 22 产品标准，从而在传导和辐射发射两方面满足合规性要求，欧盟之外参照此标准的电源产品使用 CE 符合性声明 (DoC)，满足欧盟[ EMC 指令 2014/30/EU ](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0030&locale=en)的合规性。

针对北美市场设计的产品符合 FCC 第 15 部分 的限值。IEC 61000-6-3 和 IEC 61000-6-4 通用 EMC 标准分别适用于轻工业和工业环境。

然而，在辐射方面，EN 55032 产品标准已取代 EN 55022 (ITE)、EN 55013（广播接收器和相关设备）和 EN 55103-1（音视频设备）。这一新标准正式成为符合 EMC 指令的统一辐射标准 [8]。更具体地说，之前根据 EN 55022 进行测试并在 2017 年 3 月 2 日后运往欧盟的所有产品，必须符合 EN 55032 的要求。

随着 EN 55022 标准撤销并由 EN 55032 取代，电源制造商和供应商需要按照新标准更新其 DoC 证书，从而合法地使用 CE 认证徽标。图 1 显示了在 150kHz 至 30MHz 的适用频率范围内，使用准峰值 (QP) 和平均值 (AVG) 信号检测器进行的传导发射的 EN 55022/32 A 类和 B 类限值。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_4.57.15.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_4.57.15.png)



图 1：使用准峰值和平均值检测器的 EN 55022 A 类和 B 类传导发射限值

对于汽车终端设备，未来 EMC 合规性的主要推动力无疑来自于通过车辆间通信支持的自主车辆。针对“板载接收器保护”的 CISPR 25 规范已针对传导发射设置了严格的限制，在 FM 频带（76MHz 至 108MHz）的限制尤为严格。

从监管角度而言，UNECE 10 号法规在 2014 年 11 月取代了欧盟的汽车 EMC 指令 2004/104/EC，其中要求制造商必须取得所有车辆、电子元器件 (ESA)、元器件和独立技术单元的型式认证。

CISPR 25 测试的传导发射均在 150kHz 至 108MHz 频率范围的特定频带内进行测量。具体而言，调节频率范围分布在 AM 广播、FM 广播和移动服务频带之间，如图 2 中的图象和表格所示。图 2 还绘制了 CISPR 25 5 类（最严苛的要求）的相关限值图象。尽管频带之间的带隙允许更高的噪声尖峰，但汽车制造商可能会根据其特定的内部 EMC 要求选择扩展这些频率范围。这些要求通常基于国际 IEC 标准，仅更改不同测试或限值的少量参数，其核心内容保持不变。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_4.57.34.png" alt=" " style="zoom:67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_4.57.34.png)

图 2：CISPR 25 5 类传导发射限值

为了应对 CISPR 25 限值带来的挑战，尤其是 FM 频带方面，请注意，50Ω 测量电阻产生的 18dBμV 对应的噪声电流仅为 159nA。

### **测量传导** **EMI**

LISN 测量 EUT 产生的传导发射。它是插入 EMI 源和电源之间测量点的接口，确保 EMI 测量结果的可重复性和可比较性。图 3 所示为根据 CISPR 16-1-2或 ANSI C63.4。标准定义的标准 50μH LISN 的功能等效电路（并非完整原理图）。

LISN 提供：

- 在给定频率范围内，产生经过校准的稳定信号源阻抗。
- 在该频率范围内，将 EUT 和测量设备与输入电源隔离。
- 与测量设备建立安全适用的连接。
- 单独测量两条线路的总噪声级别，图 3 中以 L 和 N 表示。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.02.41.png" alt=" " style="zoom:67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.02.41.png)

图 3：使用 V 型 LISN 进行的传导发射测量

简而言之，使用信号源阻抗已知的预定义测试方案能够获得可重复性结果。注：LISN 可能包含一个或多个独立 LISN 电路。

LISN 的实质是 pi 滤波器网络。通过低通电感-电容 (LC) 滤波器，EUT 与输入电源线 L 和 N 相连，如图 3 所示。LISN 电感值基于在产品理想安装状态下，电源线的预期电感。

CISPR 16 和 ANSI C63.4 为 LISN 指定了一个 50μH 电感，该值与电信设备中约 50 米的配电布线系统的电感相符。相反，CISPR 25 指定 5μH LISN，与汽车线束的近似电感相对应。 

LISN 为噪声发射信号提供明确定义的阻抗。LISN 制造商通常提供校准曲线，指示特定测量频率范围内的标称阻抗。根据 CISPR 16-1-2，允许的容差是 ±20% 的幅值和 ±11.5° 的相位。

对于使用 EMI 接收器或频谱分析仪进行的测量，噪声信号可通过高通滤波器网络（如图 3 所示）获得，该网络的耦合电容为 0.1μF，放电电阻为 1kΩ，测量端口的端接电阻为  50Ω 。图 4 显示了在 150kHz 至 30MHz 的频率范围，(50μH + 5Ω) || 50Ω LISN 的模拟阻抗图。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.04.59.png" alt=" " style="zoom:67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.04.59.png)

图 4：在 150kHz 至 30MHz 的调节频率范围内，测量端口处的 50Ω，50μH LISN 标称阻抗特性

### **针对汽车应用的** **CISPR 25** **测试装置**



图 5 显示了 CISPR 25 推荐的传导发射测试装置。该标准定义了待测系统的处理方式以及测量方案和设备。根据 CISPR 25 规范，LISN 在此处指定为 AN。当汽车功率回流线超过 200mm 时，EUT 远程接地，需要两个 AN：二者分别用于正电源线和功率回流线。相反，如果汽车功率回流线不超过 200mm，则 EUT 本地接地，只需将一个 AN 应用于正电源。

AN 直接安装在基准接地平面之上，AN 外壳与接地平面相连。电源回流线还与电源和 AN 之间的接地平面相连。将 EMI 接收器连接到相应 AN 的测量端口可确保成功测量每条电源线上的传导发射。与此同时，插入另一条电源线的 AN 的测量端口端接 50Ω 负载。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.06.04.png" alt=" " style="zoom:67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.06.04.png)

图 5：CISPR 25 传导 EMI 测试方案（电压法）概述

图 6 显示了用于预合规测试的 CISPR 25 传导发射试验室 [11]。LISN 是右侧的蓝色箱体，锂离子汽车电池位于其后，DUT 位于左侧的绝缘材料上。为了在特定电源电压下（例如 13.5V）进行测试，使用可变电压源从试验室外部通过隔板馈电。结果通过各自的 LISN 在线路端（热回路）和返回端（接地）获取。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.07.33.png" alt=" " style="zoom:67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.07.33.png)

图 6：使用两个单极 LISN 和铜箔接地平面的 CISPR 25 传导 EMI 测试装置

图 7 显示了典型的 CISPR 25 传导 EMI 扫描结果，黄色和蓝色分别表示峰值和平均测量值。我们可以看到 DC/DC 转换器安静地运行，传导发射远低于严格的 5 类限值。这种测量技术在 30MHz 以上发生改变，因为 EMI 接收器的 RBW 从 9kHz 调整为 120kHz，可能导致测量噪底发生变化。

[<img src="https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.08.54.png" alt=" " style="zoom:67%;" />](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.08.54.png)



图 7：典型的 CISPR 25 传导 EMI 测量

### **总结**



有意或者无意产生的电磁能量均对其他设备造成电磁干扰。商业产品需要在正常运行过程中将产生的电磁能量降至最低水平。

世界各地的许多管理机构均对允许最终产品产生的传导和辐射 EMI 的等级进行了规定。采用适用的测量技术可以定量分析此类发射，以便采取适当的措施符合法规的合规性。

EMC 要求通常事关在 AC 电源线（和信号线）所测量系统的整体情况，而 DC/DC 转换器作为子元器件，并没有具体的 EMC 限值。然而，用户可以执行预合规性测试，确定 EMI 是否造成不良影响。

## **第2部分 — 噪声传播和滤波**

### **简介**

高开关频率是在电源转换技术发展过程中促进尺寸减小的主要因素。为了符合相关法规，通常需要采用电磁干扰 (EMI) 滤波器，而该滤波器通常在系统总体尺寸和体积中占据很大一部分，因此了解高频转换器的 EMI 特性至关重要。

在本系列文章的第 2 部分，您将了解差模 (DM) 和共模 (CM) 传导发射噪声分量的噪声源和传播路径，从而深入了解 DC/DC 转换器的传导 EMI 特性。本部分将介绍如何从总噪声测量结果中分离出 DM/CM 噪声，并将以升压转换器为例，重点介绍适用于汽车应用的主要 CM 噪声传导路径。

### **DM** **和** **CM** **传导干扰**

DM 和 CM 信号代表两种形式的传导发射。DM 电流通常称为对称模式信号或横向信号，而 CM 电流通常称为非对称模式信号或纵向信号。图 1 显示了同步降压和升压 DC/DC 拓扑中的 DM 和 CM 电流路径。Y 电容 CY1 和 CY2 分别从正负电源线连接到 GND，轻松形成了完整的 CM 电流传播路径。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.17.00.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.17.00.png)

图 1：同步降压 (a) 和升压 (b) 转换器 DM 和 CM 传导噪声路径

### **DM** **传导噪声**

DM 噪声电流 (IDM) 由转换器固有开关动作产生，并在正负电源线 L1 和 L2 中以相反方向流动。DM 传导发射为“电流驱动型”，与开关电流 (di/dt)、磁场和低阻抗相关。DM 噪声通常在较小的回路区域流动，返回路径封闭且紧凑。

例如，在连续导通模式 (CCM) 下，降压转换器会产生一种梯形电流，且这种电流中谐波比较多。这些谐波在电源线上会表现为噪声。降压转换器的输入电容（图 1 中的 CIN）有助于滤除这些高阶电流谐波，但由于电容的非理想寄生特性（等效串联电感 (ESL) 和等效串联电阻 (ESR)），有些谐波难免会以 DM 噪声形式出现在电源电流中，即使在添加实用的 EMI 输入滤波器级之后也于事无补。

### **CM** **传导噪声**

另一方面，CM 噪声电流 (ICM) 会流入接地 GND 线并通过 L1 和 L2 电源线返回。CM 传导发射为“电压驱动型”，与高转换率电压 (dv/dt)、电场和高阻抗相关。在非隔离式 DC/DC 开关转换器中，由于 SW 节点处的 dv/dt 较高，产生了 CM 噪声，从而导致产生位移电流。该电流通过与 MOSFET 外壳、散热器和 SW 节点走线相关的寄生电容耦合到 GND 系统。与转换器输入或输出端的接线较长相关的耦合电容也可能构成 CM 噪声路径。

图 1 中的 CM 电流通过输入 EMI 滤波器的 Y 电容（CY1 和 CY2）返回。另一条返回路径为，通过 LISN 装置（在本系列文章的第 1 部分中讨论过）的 50Ω 测量阻抗返回，这显然是不合需要的。尽管 CM 电流的幅值远小于 DM 电流，但相对来说更难以处理，因为它通常在较大的传导回路区域流动，如同天线一般，可能增加辐射 EMI。

图 2 显示了 Fly-Buck（隔离式降压）转换器的 DM 和 CM 传导路径。CM 电流通过变压器 T1 的集总绕组间电容（图 2 中的 CPS）流到二次侧，并通过接地 GND 连接返回。图 2 还显示了 CM 传播的简化等效电路。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.25.59.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.25.59.png)

图 2：Fly-Buck 隔离式转换器 DM 和 CM 传导噪声传播路径 (a)；CM 等效电路 (b)

在实际的转换器中，以下元件寄生效应均会影响电压和电流波形以及 CM 噪声：

- MOSFET 输出电容 (COSS)。
- 整流二极管结电容 (CD)。
- 主电感绕组的等效并联电容 (EPC)。
- 输入和输出电容的等效串联电感 (ESL)。

相关内容，我将在第 3 部分中进一步详细介绍。

### **噪声源和传播路径**

正如第 1 部分所述，测量 DC/DC 转换器传导发射（对于 CISPR 32 标准，规定带宽范围为 150kHz 至 30MHz；对于 CISPR 25 标准，则规定频率范围为更宽的 150kHz 至 108MHz）时，测量的是每条电源线上 50Ω LISN 电阻两端相对于接地 GND 的**总噪声**电压或“非对称”干扰。

图 3 显示了 EMI 噪声的产生、传播和测量模型。噪声源电压用 VN 表示，噪声源和传播路径阻抗分别用 ZS 和 ZP 表示。LISN 和 EMI 接收器的高频等效电路仅为两个 50Ω 电阻。图 3 还显示了相应的 DM 和 CM 噪声电压 VDM 和 VCM，它们由两条电源线的总噪声电压 V1 和 V2 计算得出。DM（或“对称”）电压分量定义为 V1 和 V2 矢量差的一半；而 CM（或“非对称”）电压分量定义为 V1 和 V2 矢量和的一半。请注意，本文提供的 VDM 通用定义与 CISPR 16 标准规定的值相比，可能存在 6dB 的偏差。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.28.05.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.28.05.png)

图 3：传导 EMI 发射模型，其中显示了噪声源电压、噪声传播路径和 LISN 等效电路

CM 噪声源阻抗主要是容性阻抗，并且 ZCM 随频率的增大而减小。而 DM 噪声源阻抗通常为阻性和感性阻抗，并且 ZDM 随频率的增大而增大。 

要降低传导噪声水平，确保噪声源本身产生较少的噪声是其中的一种方法。对于噪声传播路径，可以通过滤波或其他方法调整阻抗，从而减小相应的电流。例如，要降低降压或升压转换器中的 CM 噪声，需要降低 SW 节点 dv/dt（噪声源）、通过减小接地寄生电容来增大阻抗、或者使用 Y 电容和/或 CM 扼流器进行滤波。本系列文章的第 4 部分将详细介绍 EMI 抑制技术分类。

### **DM** **和** **CM EMI** **滤波**



无源 EMI 滤波是最常用的 EMI 噪声抑制方法。顾名思义，这类滤波器仅采用无源元件。将这类滤波器设计用于电力电子设备时特别具有挑战性，因为滤波器端接的噪声源（开关转换器）和负载（电线线）阻抗是不断变化的。

图 4a 显示了传统的 p 型 EMI 输入滤波器，以及整流和瞬态电压钳位功能（为直流/交流输入供电的 DC/DC 转换器提供 EMC 保护）。此外，图 4 还包括本系列文章第 1 部分中的 LISN 高频等效电路。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.29.57.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.29.57.png)

图 4：传统的 EMC 输入滤波器 (a)，包括 DM 等效电路 (b) 和 CM 等效电路 (c)

典型 EMI 滤波器的两个 CM 绕组相互耦合，这两个绕组的 CM 电感分别为 LCM1 和 LCM2。DM 电感 LDM1 和 LDM2 分别是两个耦合的 CM 绕组的漏电感，并且还可能包括分立的 DM 电感。CX1 和 CX2 为 DM 滤波器电容，而 CY1 和 CY2 为 CM 滤波器电容。

通过将 EMI 滤波器去耦为 DM 等效电路和 CM 等效电路，可简化其设计。然后，可以分别分析滤波器的 DM 和 CM 衰减。去耦基于这样的假设，即 EMI 滤波器具有完美对称的电路结构。在实现的对称滤波器中，假设 LCM1 = LCM2 = LCM，CY1 = CY2 = CY，LDM1 = LDM2 = LDM，并且印刷电路板 (PCB) 布局也完美对称。DM 等效电路和 CM 等效电路分别如图 4b 和图 4c 所示。

但是，严格来说，实际情况下并不存在完美对称，因此 DM 和 CM 滤波器并不能完全去耦。而结构不对称可能导致 DM 噪声转变成 CM 噪声，或者 CM 噪声转变成 DM 噪声。通常，与转换器噪声源和 EMI 滤波器参数相关的不平衡性可能导致这种模式转变。 

### **DM** **和** **CM** **噪声分离**

传导 EMI 的初始测量结果通常显示 EMI 滤波器衰减不足。为了获得适当的 EMI 滤波器设计，必须独立研究待测设备 (EUT) 产生的传导发射的 DM 和 CM 噪声电压分量。 

将 DM 和 CM 分开处理有助于确定相关 EMI 源并对其进行故障排除，从而简化 EMI 滤波器设计流程。正如我在上一部分强调的那样，EMI 滤波器采用了截然不同的滤波器元件来抑制 DM 和 CM 发射。在这种情况下，一种常见的诊断检查方法是将传导噪声分离为 DM 噪声电压和 CM 噪声电压。

图 5 显示了无源和有源两种实现形式的 DM/CM 分离器电路，该电路有助于直接同时测量 DM 和 CM 发射。图 5a 中的无源分离器电路 [4] 使用宽带 RF 变压器（如 Coilcraft 的 SWB1010 系列）在 EMI 覆盖的频率范围内实现可接受的分离结果，其中 T1 和 T2 的特征阻抗 (ZO) 分别为 50Ω 和 100Ω。将一个 50Ω 的电阻与 DM 输出端口的频谱分析仪的输入阻抗串联，实现图 3 中提供的 VDM 表达式的“除 2”功能。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.31.34.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.31.34.png)

图 5：实现的用于分离 DM/CM 噪声的无源 (a) 和有源 (b) 电路

图 5b 展示的是使用低噪声、高带宽运算放大器的有源分离器电路。U1 和 U2 实现了 LISN 输出的理想输入阻抗矩阵，而 U3 和 U4 分别提供 CM 和 DM 电压。LCM 是一个 CM 线路滤波器（例如 Würth Elektronik 744222），位于差分放大器 U4 的输入端，用于增大 DM 结果的 CM 抑制比（共模抑制比 [CMRR] ® - ¥dB）并最大限度地减少 CM/DM 交叉耦合。

### **实际电路示例** **-** **汽车同步升压转换器**

考虑图 6 中所示的同步升压转换器。该电路在汽车应用中很常见，通常作为预升压稳压器在冷启动或瞬态欠压条件下保持电池电压供应。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.33.53.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.33.53.png)

图 6：汽车同步升压转换器（采用 50Ω/5μH LISN，用于 CISPR 25 EMI 测试）

在车辆底盘接地端直接连接一个 MOSFET 散热器，可以提高转换器的热性能和可靠性，但共模 EMI 性能会受到影响。图 6 所示的原理图中，包含升压转换器以及 CISPR 25 建议采用的两个 LISN 电路（分别连接在 L1 和 L2 输入线上）。 

考虑到升压转换器的 CM 噪声传播路径，图 7 将 MOSFET Q1 和 Q2 替换为等效的交流电压流和电流源。图 7 中，还呈现了与升压电感 LF、输入电容 CIN 和输出电容 COUT 相关的寄生分量部分。特别是 CRL-GND，它是负载电路与底盘 GND 之间的寄生电容，包括长负载线和布线以及下游负载配置（例如，二次侧输出连接到底盘接地的隔离式转换器，或者用大型金属外壳固定到底盘上的电机驱动系统）所产生的寄生电容。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.35.14.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.35.14.png)

图 7：具有 LISN 的同步升压拓扑的高频等效电路，只有在 LISN 中流动的 CM 电流路径与 CM 发射测量相关

漏源开关（SW 节点）电压的上升沿和下降沿代表主要的 CM 噪声源。CP1 和 CP2 分别代表 SW 与底盘之间以及 SW 与散热器之间的有效寄生电容。图 8 显示了 SW 节点电容（电场）耦合为主要 CM 传播路径时简化的 CM 噪声等效电路。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.35.25.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.35.25.png)

图 8：连有 LISN 的同步升压电路及其简化 CM 等效电路

### **总结**



对于电力电子工程师而言，了解各种电源级拓扑中 DM 和 CM 电流的相关传播路径（包括与高 dv/dt 和 di/dt 开关相关的电容（电场）和电感（磁场）耦合）非常重要。在 EMI 测试过程中，将 DM 和 CM 发射分开处理有助于对相关 EMI 源进行故障排除，从而简化 EMI 滤波器设计流程。

在即将发表的本系列文章第三部分中，将全面介绍影响转换器开关性能和 EMI 信号的电路元件寄生部分。

## **第3部分 — 了解功率级寄生效应**

### 简介

DC/DC 转换器中半导体器件的高频开关特性是主要的传导和辐射发射源。本文章系列的第 2 部分回顾了 DC/DC 转换器的差模 (DM) 和共模 (CM) 传导噪声干扰。在电磁干扰 (EMI) 测试期间，如果将总噪声测量结果细分为 DM 和 CM 噪声分量，可以确定 DM 和 CM 两种噪声各自所占的比例，从而简化 EMI 滤波器的设计流程。高频下的传导发射主要由 CM 噪声产生，该噪声的传导回路面积较大，进一步推动辐射发射的产生。

在第 3 部分中，我将全面介绍降压稳压器电路中影响 EMI 性能和开关损耗的感性和容性寄生元素。通过了解相关电路寄生效应的影响程度，可以采取适当的措施将影响降至最低并减少总体 EMI 信号。一般来说，采用一种经过优化的紧凑型功率级布局可以降低 EMI，从而符合相关法规，还可以提高效率并降低解决方案的总成本。

### **检验具有高转换率电流的关键回路**

根据电源原理图进行电路板布局时，其中一个重要环节是准确找到高转换率电流（高 di/dt）回路，同时密切关注布局引起的寄生或杂散电感。这类电感会产生过大的噪声和振铃，导致过冲和地弹反射。图 1 中的功率级原理图显示了一个驱动高侧和低侧 MOSFET（分别为 Q1 和 Q2）的同步降压控制器。

以 Q1 的导通转换为例。在输入电容 CIN 供电的情况下，Q1 的漏极电流迅速上升至电感电流水平，与此同时，从 Q2 的源极流入漏极的电流降为零。MOSFET 中红色阴影标记的回路和输入电容（图 1 中标记为“1”）是降压稳压器的高频换向功率回路或“热”回路 。功率回路承载着幅值和 di/dt 相对较高的高频电流，特别是在 MOSFET 开关期间。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.42.51.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.42.51.png)

图 1：具有高转换率电流的重要高频开关回路

图 1 中的回路“2”和“3”均归类为功率 MOSFET 的栅极回路。具体来说，回路 2 表示高侧 MOSFET 的栅极驱动器电路（由自举电容 CBOOT 供电）。回路 3 表示低侧 MOSFET 栅极驱动器电路（由 VCC 供电）。这两条回路中均使用实线绘制导通栅极电流路径，以虚线绘制关断栅极电流路径。

### **寄生组分和辐射** **EMI**

EMI 问题通常涉及三大要素：干扰源、受干扰者和耦合机制。干扰源是指 dv/dt 和/或 di/dt 较高的噪声发生器，受干扰者指易受影响的电路（或 EMI 测量设备）。耦合机制可分为导电和非导电耦合。非导电耦合可以是电场（E 场）耦合、磁场（H 场）耦合或两者的组合 - 称为远场 EM 辐射。近场耦合通常由寄生电感和电容引起，可能对稳压器的 EMI 性能起到决定性作用，影响显著。

### **功率级寄生电感**

功率 MOSFET 的开关行为以及波形振铃和 EMI 造成的后果均与功率回路和栅极驱动电路的部分电感相关。图 2 综合显示了由元器件布局、器件封装和印刷电路板 (PCB) 布局产生的寄生元素，这些寄生元素会影响同步降压稳压器的 EMI 性能。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.45.27.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.45.27.png)

图 2：降压功率级和栅极驱动器的“剖析原理图”（包含感性和容性寄生元素）

有效高频电源回路电感 (LLOOP) 是总漏极电感 (LD)、共源电感 (LS)（即输入电容和 PCB 走线的等效串联电感 (ESL)）和功率 MOSFET 的封装电感之和。按照预期，LLOOP 与输入电容 MOSFET 回路（图 1 中的红色阴影区域）的几何形状布局密切相关。

与此同时，栅极回路的自感 LG 由 MOSFET 封装和 PCB 走线共同产生。从图 2 中可以看出，高侧 MOSFET Q1 的共源电感同时存在于电源和栅极回路中。Q1 的共源电感产生效果相反的两种反馈电压，分别控制 MOSFET 栅源电压的上升和下降时间，因此降低功率回路中的 di/dt。然而，这样通常会增加开关损耗，因此并非理想方法。

### **功率级寄生电容**

公式 1 为影响 EMI 和开关行为的功率 MOSFET 输入电容、输出电容和反向传输电容三者之间的关系表达式（以图 2 中的终端电容符号表示）。在 MOSFET 开关转换期间，这种寄生电容需要幅值较高的高频电流。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.47.58.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.47.58.png)

公式 2 的近似关系表达式表明，COSS 与电压之间存在高度非线性的相关性。公式 3 给出了特定输入电压下的有效电荷 QOSS，其中 COSS-TR 是与时间相关的有效输出电容，与部分新款功率 FET 器件的数据表中定义的内容一致。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.48.04.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.48.04.png)

图 2 中的另一个关键参数是体二极管 DB2 的反向恢复电荷 (QRR)，该电荷导致 Q1 导通期间出现显著的电流尖峰。QRR 取决于许多参数，包括恢复前的二极管正向电流、电流转换速度和芯片温度。一般来说，MOSFET QOSS 和体二极管 MOSFET QOSS 会为分析和测量过程带来诸多难题。在 Q1 导通期间，为 Q2 的 COSS2 充电的前沿电流尖峰和为 QRR2 供电以恢复体二极管 DB2 的前沿电流尖峰具有类似的曲线图，因此二者常被混淆。

### **EMI** **频率范围和耦合模式**

表 1 列出了三个粗略定义的频率范围，开关模式电源转换器在这三种频率范围内激励和传播 EMI [5]。在功率 MOSFET 开关期间，当换向电流的转换率超过 5A/ns 时，2nH 寄生电感会导致 10V 的电压过冲。此外，功率回路中的电流具有快速开关边沿（可能存在与体二极管反向恢复和 MOSFET COSS 充电相关的前沿振铃），其中富含谐波成分，产生负面影响严重的 H 场耦合，导致传导和辐射 EMI 增加。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.51.26.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.51.26.png)

表 1：开关转换器噪声源和常规 EMI 频率分类

噪声耦合路径主要有以下三种：通过直流输入线路传导的噪声、来自功率回路和电感的 H 场耦合以及来自开关节点铜表面的 E 场耦合。

### **转换器开关波形分析建模**



如第 2 部分所述，开关节点电压的上升沿和下降沿分别是非隔离式转换器中 CM 噪声和 E 场耦合的主要来源。在EMI 分析中，设计者最关注电源转换器噪声发射的谐波含量上限或“频谱包络”，而非单一谐波分量的幅值。借助简化的开关波形分析模型，我们可以轻松确定时域波形参数对频谱结果的影响。

为了解与开关节点电压相关的谐波频谱包络，图 3 给出了近似的时域波形。每一部分均由其幅值 (VIN)、占空比 (D)、上升和下降时间（tR 和 tF）以及脉宽 (t1) 来表示。其中，脉宽的定义为上升沿中点与下降沿中点的间距。

傅立叶分析结果表明，谐波幅值包络为双 sinc 函数，转角频率为 f1 和 f2，具体取决于时域波形的脉宽和上升/下降时间。对于降压开关单元的各个输入电流波形，可以应用类似的处理方法。测得的电压和电流波形中相应的频率分量可以表示开关电压和电流波形边沿处的振铃特性（分别由寄生回路电感和体二极管反向恢复产生）。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.52.45.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.52.45.png)

图 3：开关节点电压梯形波形及其频谱包络（受脉宽和上升/下降时间影响）

一般来说，电感 LLOOP 会增加 MOSFET 漏源峰值电压尖峰，并且还会加剧开关节点的电压振铃，影响 50MHz 至 200MHz 范围内的宽带 EMI。在这种情况下，最大限度缩减功率回路的有效长度和闭合区域显得至关重要。这样不仅可减小寄生电感，而且还可以减少环形天线结构发出的磁耦合辐射能量，从而实现磁场自消除。

稳压器输入端基于回路电感比率发生传导噪声耦合，而输入电容 ESL 决定滤波要求。减小 LLOOP 会增加输入滤波器的衰减要求。幸运的是，如果降压输出电感的自谐振频率 (SRF) 较高，传导至输出的噪声可降至最低。换言之，电感应具有较低的有效并联电容 (EPC)，以便在从开关节点到 VOUT 的网络中获得较高的传输阻抗。此外，还会通过低阻抗输出电容对输出噪声进行滤波。

### **等效谐振电路**

根据图 4 所示的同步降压稳压器时域开关节点的电压波形可知，MOSFET 开关期间传输的寄生能量会激发 RLC 谐振。右侧的简化等效电路用于分析 Q1 导通和关断时的开关行为。从电压波形中可以看出，上升沿的开关节点电压明显超出 VIN，而下降沿的开关节点电压明显低于接地端 (GND)。

振荡幅值取决于部分电感在回路内的分布，回路的有效交流电阻会抑制随后产生的振铃。这不仅为 MOSFET 和栅极驱动器提供电压应力，还会影响宽带辐射 EMI 的中心频率。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.54.11.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.54.11.png)



**图** 4：MOSFET 导通和关断开关转换期间的同步降压开关节点电压波形及等效RLC 电路

根据图 4 中的上升沿电压过冲计算可得，振铃周期为 6.25ns，对应的谐振频率为 160MHz。此外，将一个近场 H 探头直接放在开关回路区域上方也可以识别该频率分量。利用计算型 EM 场仿真工具，可以推导出与高频谐振和辐射发射相关的部分回路电感值。不过，还有一种更简单的方法。这种方法需要测量谐振周期 *TRing1* 并从 MOSFET 数据表中获取输入电压工作点的 COSS2，然后利用公式 4 计算总回路电感。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.55.30.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_5.55.30.png)

其中两个重要因素是谐振频率以及谐振固有的损耗或阻尼因子 a。主要设计目标是通过最大限度减小回路电感尽可能提升谐振频率。这样可以降低存储的无功能量总值，减少谐振开关节点电压峰值过冲。此外，在趋肤效应的作用下，较高频率处的阻尼因子增大，提升 RLOOP 的有效值。

### **总结**

尽管氮化镓 (GaN) 功率级同步降压转换器通常在低于 3MHz 的频率下切换开关状态，但产生的宽带噪声和 EMI 往往高达 1GHz 甚至更高。EMI 主要由其快速开关的电压和电流特性所致。实际上，器件开关波形的高频频谱成分是获取 EMI 产生电位指示的另一种途径，它能够指明 EMI 与开关损耗达到良好权衡的结果。

首先从原理图中确定关键的转换器开关回路，然后在 PCB 转换器布局设计过程中尽量缩减这些回路的面积，从而减少寄生电感和相关的 H 场耦合，降低传导和辐射 EMI。 

在这篇系列文章的后续章节中，我将通过多种 DC/DC 转换器电路重点介绍改善 EMI 性能矢量的系统级和集成电路 (IC) 的特定功能。缓解传导 EMI 的措施通常也可以改善辐射 EMI，这两方面经常相互促进的。

## **第4部分 — 辐射发射**

### 简介

这篇系列文章的第 4 部分针对电源转换器（特别是工业和汽车领域使用的电源转换器）在开关时产生的辐射排放阐述了一些观点。

辐射电磁干扰 (EMI) 是一种在特定环境中动态出现的问题，与电源转换器内部的寄生效应、电路布局和元器件排布及其在运行时所处的整体系统相关。因此，从设计工程师的角度出发，辐射 EMI 的问题通常更具挑战性，复杂度更高，在系统主板使用多个 DC/DC 功率级时尤为如此。了解辐射 EMI 的基本机制以及测量要求、频率范围和相应限制条件至关重要。本文重点介绍这些方面的内容，展示辐射 EMI 测量装置以及两个 DC/DC 降压转换器的结果。

### **近场耦合**

图 1 概略介绍了噪声源与受干扰电路之间基本 EMI 耦合模式特别是电感或 H 场耦合需要 di/dt 较高的时变电流源和两条磁耦合回路（或带有返回路径的平行导线）。另一方面，电容或 E 场耦合需要 dv/dt 较高的时变电压源和两块紧邻的金属板。这两种机制均属于近场耦合，其中的噪声源与受干扰电路非常接近，可使用近场嗅探器进行测量。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.02.13.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.02.13.png)

图 1：EMI 耦合模式 

例如，现代电源开关，特别是氮化镓 (GaN) 和碳化硅 (SiC) 基晶体管，其输出电容 COSS 较低，栅极电荷 QG 较少，能够以极高的 dv/dt 和 di/dt 转换率进行开关。相邻电路发生 H 场和 E 场耦合以及串扰的可能性很高。然而，随着互感或电容减小，耦合结构的间距增大，近场耦合显著减弱。 

### **远场耦合**

典型的电磁 (EM) 波以 E 场和 H 场组合的形式传播。辐射天线源附近的场结构为复杂的三维模式。从辐射源进一步分析，远场区域中的 EM 波由彼此正交并且与传播方向正交的 E 场和 H 场分量组成。图 2 展示了这种平面波，它代表辐射 EMI 的主要基准，受到各种辐射标准的约束。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.03.20.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.03.20.png)

图 2：电磁平面波传播

图 3 所示的波阻抗等于电场强度与磁场强度之比。远场区域中的 E 和 H 分量同相，因此远场阻抗呈阻性，具体值可通过麦克斯韦方程（如方程 1 所示）的平面波解决方案计算：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.03.36.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.03.36.png)如果 λ 是波长，F 是所需频率，方程 2 通常表示近场和远场区域之间的边界：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.03.51.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.03.51.png)然而，该边界不是精确的标准，仅用于指示一般性过渡区域（图 3 中描述为 l/16 至 3l），其中的场从复杂的分布形态演变为平面波。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.06.32.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.06.32.png)

图 3： 麦克斯韦定律中近场和远场区域的波阻抗

 鉴于多数天线设计用于检测和响应电场，辐射的电磁波通常称为垂直或水平极化，具体取决于电场方向。测量 E 场天线一般应与传播的 E 场在同一平面中定向，从而检测最大场强。因此，辐射 EMI 测试标准通常介绍接收天线以垂直和水平极化方式安装时的测量。

### **工业和多媒体设备中的辐射** **EMI**

表 1 列出了联邦通信委员会 (FCC) 第 15 部分 B 子节针对无意辐射体规定的 A 类和 B 类辐射发射限值。此外，本规范第 15.109(g) 条允许在使用美国国家标准协会 (ANSI) C63.4-2014 规定的测量方法时，使用国际无线电干扰特别委员会 (CISPR) 22 规定的辐射发射限值（如表 2 所述）。表 1 和表 2 中规定的限值均针对低于 1GHz 的频率，使用 CISPR 准峰值 (QP) 检测器功能，分辨率带宽 (RBW) 为 120kHz。表 3 和表 4 规定的限值针对 1GHz 以上的频率，此时使用峰值 (PK) 和平均 (AVG) 检测器以及分辨率带宽为 1MHz 的接收器。

对于指定的测量距离，B 类民用或家用应用限制通常比 A 类商用或工业应用限制更严格，通常高出 6dB 至 10dB。另请注意，表 1 和表 2 还包括一个按照 15.31(f)(1) 使用的 20 dB/dec 的反向线性距离 (1/d) 比例系数，针对 3m 和 10m 天线测量距离对应的限值进行归一化处理，从而确定合规性。例如，如果将天线放置在 3 米而非 10 米的位置，从而保持在测试设备边界内，则限制幅值调整约 10.5dB。

表 1：按照 47 CFR 15.109(a) 和 (b) 标准规定的 30MHz 到 1GHz 范围的辐射发射场强 QP 限值

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.12.58.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.12.58.png)

表 2：按照 47 CFR 15.109(g)/CISPR 22/32 标准规定的 30MHz 到 1GHz 范围的辐射发射场强 QP 限值

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.11.28.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.11.28.png)

表 3：按照 47 CFR 15.109(a) 和 (b) 标准规定的 1GHz 到 6GHz 范围的辐射发射场强限值

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.12.49.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.12.49.png)

表 4：按照 47 CFR 15.109(g)/CISPR 22/32 标准规定的 1GHz 到 6GHz 范围的辐射发射场强限值

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.13.07.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.13.07.png)

图 4 展示了当天线距离为 3m 时，A 类和 B 类相关限值的图象。符合 FCC 的设计包括采用 *Bluetooth®* 低能耗技术的气体传感器实施方案，其由电池供电，可从德州仪器 (TI) 购买。用户可下载有关此设计的FCCA类合规性报告，其中列出辐射发射测试数据和图象，以便查阅相关信息。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.19.58.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.19.58.png)

图 4：FCC 第 15 部分和 CISPR 22 的 A 类和 B 类辐射限值（对于低于和高于 1GHz 这两种条件，分别使用 QP 和 AVG 检测器）

如图 5 所示，辐射 EMI 测试程序包括将待测设备 (EUT) 和支持设备放置在半消声室 (SAC) 或开阔试验场 (OATS) 内的非导电转盘（高出基准接地平面 0.8m）之上，遵循 CISPR 16-1 中所定义。EUT 设置在与安装于天线塔上的接收天线相距 3m 的位置。 

使用经校准的宽带天线（双锥形天线和对数周期天线组合，或者 Bilog 天线）的 PK 检测器预扫描功能，沿水平和垂直两种天线极化方向对 30MHz 到 1GHz 的辐射发射进行检测。这种探究性测试可以确定所有重要发射的频率。执行该测试后，使用 QP 检测器检查相关的故障点，记录最终合规测量值。

在测试期间，EMI 接收器的 RBW 设置为 120kHz。配置天线的水平和垂直极化方向（将其相对于接地平面旋转 90°），并将高度调整为高出接地平面 1m 到 4m，以便在考虑地面反射时，将每个测试频率对应的场强读数最大化。在测量期间，可将转盘上的 EUT 在 0 到 360° 之间旋转，使天线与 EUT 之间的方位角发生变化，以便根据 EUT 的方位获得最大场强读数。天线位于 EUT 的远场区，对应于 3m 天线距离，频率为 15.9MHz。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.22.09.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.22.09.png)

图 5：FCC 第 15 部分和 CISPR 22/32 对应的辐射发射测量装置

可以使用喇叭天线针对 1GHz 以上的频率执行 PK 检测器预扫描，然后在接近限制时使用 AVG 检测器。EMI 接收器的 RBW 设置为 1MHz。天线方向明确，因此无需执行高度扫描，接地平面和暗室壁的反射也很难造成干扰。然而，EUT 在这些频率下的辐射发射方向性更强，因此转盘再次旋转 360 度，确定天线极化方向以获得最大响应。根据表 5，测量频率的上限范围随 EUT 的最高内部频率发生变化。

表5：辐射发射最大测量频率（基于 EUT 内部时钟源的最高频率）

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.23.30.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.23.30.png)

辐射发射测试以每米若干分贝/微伏 (dB/mV) 为单位校准电场强度。天线因子 (AF) 是天线平面产生的电场 (mV/m) 与频谱分析仪 (SA) 或扫描 EMI 接收器测得的电压 (dB/mV) 之比。一般而言，校正的发射电平由方程 3 推导得出，推导时将 AF、电缆损耗 (CL)、衰减器和 RF 限制器损耗因子 (AL) 以及放大器预增益 (AG) 考虑在内。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.24.11.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.24.11.png)

图 6 所示为 [LMR16030](http://www.ti.com.cn/product/cn/LMR16030) 60V/3A 降压转换器辐射发射测试装置的照片和结果。测量条件为 24V 输入、5V 输出、3A 负载电流和 400kHz 开关频率。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.25.50.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.25.50.png)

图 6：CISPR 22 辐射 EMI 测试：测试装置照片 (a)；水平和垂直极化天线的辐射 EMI 结果 (b)

### **汽车系统中的辐射** **EMI**

尽管屏蔽电缆可以削弱汽车系统中的干扰效应，但 EMI 可通过串扰“有效地”在易受影响的电路中耦合。在场线耦合效应的作用下，对于体积相对较小但电源分布密集、信号通过电缆束的车辆，辐射排放还可能导致信号互连出现辐射抗扰问题。基于上述原因，评估 EMI 性能便成为汽车工程师在设计和测试电动汽车时重点关注的问题。

### **UNECE 10** **号法规和** **CISPR 25**

CISPR 12 和 CISPR 25 均为国际标准，提供无线电干扰测量的限值和程序，分别为汽车的车载和非车载接收器提供保护。CISPR 25 特别适用于汽车级别，也适用于所有车用电子组件 (ESA)。与其他标准相比，CISPR 25 通常作为汽车制造商及其供应商定义产品规格的基础，但不是评定合规性和遵从情况的基准。自欧盟电动汽车 EMC 指令废止后，联合国欧洲经济委员会 (UNECE) 第 10 条规定中出现这一差别。

CISPR 25 针对车辆元器件排放测量定义了数种方法和限值类别，兼顾宽带 (BB) 源和窄带 (NB) 源。图 7 说明了针对元器件/模块使用 PK 和 AVG 检测器的 5 类限值。测量对象为车辆中工作在广播和移动服务频带中的接收器。最低测量频率涉及 150kHz 至 300kHz 的欧洲长波 (LW) 广播频带，最高频率为 2.5GHz（考虑蓝牙传输）。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.27.51.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.27.51.png)

图 7：使用内衬吸收器的屏蔽外壳 (ALSE) 方法，通过峰值和平均值检测器（线性频率标度）测得的元器件/模块的 CISPR 25 5 类辐射限值

对于 30MHz 以下和以上两种条件下的检测，扫描接收器的 RBW 分别为 9kHz 和 120kHz。例外情况是 GPS L1 民用（1.567GHz 至 1.583GHz）和全球导航卫星系统 (GLONASS) L1（1.591GHz 至 1.613GHz）频段。在这两种频段下，需要 9kHz 的 RBW 和 5kHz 的最大步长，从而在仅使用 AVG 检测器的情况下检测出相应的 NB 发射。

### **CISPR 25** **的天线系统**

使用额定输出阻抗为 50Ω 的线性极化电场天线进行测量。表 6 和图 8 显示了 CISPR 25 建议使用的天线，可提升不同实验室所提供结果的一致性。

表 6：根据 CISPR 25，建议使用电场天线；双锥形天线和对数周期天线存在叠加频率，而 Bilog 天线覆盖了二种天线各自的频率范围。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.29.47.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.29.47.png)

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.30.07.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.30.07.png)

图 8：符合 CISPR 25 规范的测量天线 

对于低频测量，使用带地网的无源/有源拉杆单极天线。双锥形和对数周期偶极子阵列 (LPDA) 天线通常分别覆盖 30MHz 至 200MHz 和 200MHz 至 1GHz 的频率范围。最后，双脊喇叭天线 (DRHA) 通常用于 1GHz 至 2.5GHz。宽带 Bilog 天线的外型比双锥形或对数周期天线更大，有时用于覆盖 30MHz 至 1GHz 的频率范围。 

### **使用** **ALSE** **进行辐射** **EMI** **测试**

图 9、10 和 11 所示为使用 CISPR 25 ALSE 方法（也称天线方法）的典型装置，针对表 6 中规定的频率范围进行辐射发射测量。

EUT 和电缆束放置在高出接地平面 50mm 的非导体介电材料（相对介电常数 εr 较低，不高于 1.4）之上。与接地平面前部平行的线束长度为 1.5m，EUT 与负载模拟器之间测试线束的总长度不超过 2m。测试线束的长段平行于接地平面朝向天线的边缘，与边缘相距 100mm。接地平面的要求是最小宽度和长度分别为 1m 和 2m，或者在整个设备下方加上 200mm，取其中的较大值。根据方程式 2 给定的近远场转换以及 1m 天线距离，在 EUT 的近场区域进行测量时，频率必须低于 48MHz。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.31.45.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.31.45.png)

图 9：单极拉杆天线（150kHz 至 30MHz）的 CISPR 25 辐射发射测量装置

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/3348._4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.32.02.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/3348._4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.32.02.png)

图 10：双锥形天线（30MHz 至 300MHz）或对数周期天线（200MHz 至 1GHz）的 CISPR 25 辐射发射测量装置

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.34.12.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.34.12.png)

图 11：喇叭天线（1GHz 以上）的 CISPR 25 辐射发射测量装置

喇叭天线与 EUT 对齐，其他天线则放置在线束中点。执行所有测量时，天线距离均为 1 米。频率范围为 150kHz 至 30MHz 的测量仅针对垂直天线极化执行。频率范围为 30MHz 至 2.5GHz 的扫描同时针对水平极化和垂直极化执行。

如前文所述，EMI 接收器与 AF 结合所检测到的天线电压可在天线位置产生电场强度。请注意，独立的 AF 可用于水平和垂直极化，因此可以使用相应的 AF 值对每个极化方向进行测量。 

### **辐射** **EMI** **预合规测试及结果**

图 12 为 [LM53635-Q1](http://www.ti.com.cn/product/cn/LM53635-Q1) 汽车级同步降压转换器 [9] 辐射发射测试装置的照片。EUT 由汽车电池供电，正负供电线路均连接线路阻抗稳定网络 (LISN)。3.5A 阻性负载下的输出为 3.3V。开关频率为 2.1MHz，高于许多汽车系统所需的 AM 频带，同时启用了扩频调频 (SSFM)。图 13 至 16 显示了使用各种测试天线通过 CISPR 25 5 类限值要求的测量结果。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.26.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.26.png)

图 12：CISPR 25 预合规测量装置照片

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.36.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.36.png)

图 13：辐射发射结果：150kHz 至 30MHz，拉杆天线，垂直极化

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.43.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.43.png)

图 14：辐射发射结果：30MHz 至 300MHz，双锥形天线，水平和垂直极化

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.53.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.36.53.png)

图 15：辐射发射结果：200MHz 至 1GHz，对数周期天线，水平和垂直极化

*[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.37.03.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_6.37.03.png)*

图 16：辐射发射结果：1GHz 至 2.5GHz，喇叭天线，水平极化 

### **结论**

辐射发射影响电源转换器在高频条件的 EMI 特性 [10]。辐射测试的上限频率扩展到 1GHz 甚至更高（取决于规范），远高于传导发射。虽然不像传导发射测试那样简单直接，但辐射发射测量对于合规测试不可或缺，很容易成为产品开发过程中的瓶颈。

对于汽车应用，由于长度原因，电缆束在低频条件下主要采用辐射结构。测得的辐射发射曲线主要来源于所连接电缆中的共模电流，由印刷电路板 (PCB) 与电缆之间的近场电耦合驱动。我将在本文的后续章节探讨辐射 EMI 减弱技术。

## **第5部分 — 采用集成 FET 设计的 EMI 抑制技术**

### **简介**

本系列文章的第 1 部分至第 4 部分详细介绍了开关电源稳压器引起的传导发射和辐射发射，包括噪声产生机制、测量要求、频率范围、适用的测试限值、传播模式和寄生效应。在第 5 部分中，我将基于这一理论基础介绍抑制电磁干扰 (EMI) 的实用电路技术。 

一般来说，电路原理图和印刷电路板 (PCB) 对于实现出色的 EMI 性能至关重要。第 3 部分重点强调通过谨慎的元器件选型和 PCB 布局尽量减小“功率回路”寄生电感的重要性。电源转换器集成电路 (IC) 的封装技术及其提供的 EMI 特定功能对此产生了巨大的影响。如第 2 部分所述，必须使用差模 (DM) 滤波方可将输入纹波电流的幅值充分降低至满足 EMI 合规性要求的水平。与此同时，如果需要抑制约 10MHz 以上的发射，通常使用共模 (CM) 滤波。在高频条件下，使用屏蔽也可以获得优异的结果。 

本文主要介绍这些方面的内容，专门聚焦于带有集成功率 MOSFET 和控制器的转换器解决方案，提供抑制 EMI 的实例和应用指导。一般来说，转换器应在合理范围内超出传导 EMI 一定的裕度，为达到辐射限值预留空间。幸运的是，多数减少传导发射的步骤对于抑制辐射 EMI 同样有效。 

### **了解** **EMI** **的相关挑战**

DC/DC 转换器中的 EMI 主要由其快速开关的电压和电流特性所致。与转换器的不连续输入或输出电流相关的 EMI 相对容易处理，但更大的问题是开关电压 dv/dt 和电流 di/dt 中的谐波成分，以及与开关波形相关的振铃。

图 1 所示为存在噪声的同步降压转换器的开关 (SW) 电压波形。振铃频率范围为 50MHz 至 200MHz，具体取决于寄生效应。此类高频成分可以通过近场耦合传播到输入电源线、周边元器件或输出总线（如 USB 电缆）。体二极管反向恢复存在类似的问题，随着恢复电流流入寄生回路电感，振铃电压升高。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.09.20.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.09.20.png)

图 1：同步降压转换器在 MOSFET 导通和关断开关转换期间的开关节点电压波形和等效电路

图 2 的原理图标识了降压转换器电路的两条重要回路。最大限度缩减电源回路的面积至关重要，原因是该参数与寄生电感和相关 H 场传播成正比。主要设计目标是通过减小寄生电感最大程度提升寄生 LC 谐振电路的谐振频率。此举可以降低存储的无功能量总值，减少开关电压峰值过冲。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.09.44.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.09.44.png)

图 2：简化的同步降压转换器原理图（针对 EMI 标出了关键回路和走线）

在图 2 所示的自举电容回路中，高侧 MOSFET 的导通速度由一个标记为 RBOOT 的可选串联自举电阻进行控制。自举电阻会改变驱动电流瞬变率，降低 MOSFET 导通期间的开关电压和电流转换率。另一种方法是在 SW 和 GND 之间添加一个缓冲电路。同理，该缓冲电路应根据每次开关转换时的瞬态电流尖峰，占用最小的回路面积。当然，缓冲电路和栅极电阻会增加开关功率损耗，需要在效率和 EMI 之间进行权衡。如果效率和散热性能同样非常重要，则需要使用其他技术解决 EMI 相关的挑战。

### **转换器的** **PCB** **布局**

表 1 至表 5 总结了通过优化 PCB 布局及元器件排布削弱 DC/DC 转换器 EMI 信号的基本准则。我将在本文的后续部分提供一项 PCB 布局案例研究，探讨如何优化降压转换器的 EMI 特性。

表 1：布线及元器件排布。

| 1    | 将所有功率级元器件排布在 PCB 顶部。- 避免将电感放在底部，以免对 EMI 测试装置的基准平面产生辐射。 |
| ---- | ------------------------------------------------------------ |
| 2    | 将 VCC 或 BIAS 的旁路电容（从输出端）放置于靠近各自引脚的位置。– 在将 AGND 引脚与 GND 相连之前，首先电路中连入 CVCC 和 CBIAS 电容。 |
| 3    | 将自举电容与邻近的 BOOT 和 SW 引脚相连接。- 利用邻近的接地覆铜屏蔽 CBOOT 电容和开关节点，降低 CM 噪声。 |

表 2：GND 平面设计。

| 1    | 将 PCB 分层板中的第 2 层 GND 平面尽可能固定在靠近顶层的位置。- 消除 H 场、降低寄生电感并屏蔽噪声。 |
| ---- | ------------------------------------------------------------ |
| 2    | 使用位于顶层与第二层之间的低 z 轴间距获得最佳映像平面效果。- 在 PCB 分层规范中将层间距定义为 6 mil。 |

表 3：输入和输出电容。

| 1    | 放置 CIN，尽量减小将 CIN 连接到 VIN 和 PGND 引脚所形成的回路面积。 |
| ---- | ------------------------------------------------------------ |
| 2    | CIN 和 COUT 的接地返回路径应由集中放置的顶层平面组成。- 使用多个外部或内部 GND 平面连接 DC 电流路径。 |
| 3    | 在 VIN 和 PGND 附近使用外壳尺寸为 0402 或 0603 的陶瓷输入电容，以便最大限度减小寄生回路电感。 |

表 4.电感和开关节点布局。

| 1    | 将电感放置在 IC 的 SW 引脚附近。- 尽量减小开关节点覆铜区域的表面积，避免电容过度耦合。 |
| ---- | ------------------------------------------------------------ |
| 2    | 使用邻近的接地保护并通过屏蔽限制开关节点噪声。               |
| 3    | 检查电感点位置，确保与 SW 相连的绕组末端位于电感绕组几何结构内部的底部，由连接到 VOUT 的绕组的外层绕线提供屏蔽。 |
| 4    | 尽可能使用电场屏蔽电感。将屏蔽端子与 PCB 接地平面相连。      |
| 5    | 选择在封装下方设有端子的电感。- 避免使用可能产生天线辐射效应的大型侧壁式端接。 |

 表 5.EMI 管理。

| 1    | 将 EMI 滤波器元器件排布在远离开关节点的位置。- 如果 EMI 滤波器与功率级的分隔距离不足，可将 EMI 滤波器放在电路板上转换器的对侧。 |
| ---- | ------------------------------------------------------------ |
| 2    | 在 EMI 滤波器下方的所有层上开口，以防寄生电容路径影响滤波器的衰减特性。 |
| 3    | 根据需要，可添加一个与 CBOOT 串联的电阻（最好小于 10Ω），限制高侧 MOSFET 导通速度，从而降低开关节点电压转换率，减少过冲和振铃。 |
| 4    | 如果需要开关节点 RC 缓冲电路，可将封装最小的元器件与 SW（通常为电容）相连。 |
| 5    | 使用具有内部接地平面的四层 PCB，与双层设计相比，其性能得到显著提升。- 避免阻断 IC 附近的高频电流路径。 |

### **EMI** **输入滤波器**



图 3 所示为典型的多级 EMI 输入滤波器。低频和高频部分可提供 DM 噪声衰减，也可选择 p 级，通过 CM 扼流器提供 CM 衰减。标记为 CBULK 的电解电容具有固有的串联电阻 (ESR)，可用于设置所需阻尼，降低转换器输入的有效品质因子，保持输入滤波器的稳定性。

DM 电感的自谐振频率 (SRF) 限制滤波器第一级可实现的高频 DM 衰减。滤波器第二级通常至关重要，其使用铁氧体磁珠在高频条件下提供附加的 DM 衰减，此时额定阻抗通常为 100MHz。标记为 CF1 和 CF2 的陶瓷电容可将噪声分流到接地端。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.19.19.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.19.19.png)

图 3：具有 DM 和 CM 级的三级 EMI 输入滤波器

DM 滤波器的电感一般设置为削弱基波和低频谐波的值。应使用尽可能小的电感来满足低频滤波要求，因为匝数较多的大电感具有较高的等效并联电容 (EPC)，导致其 SRF 较高，影响其在高频下的性能。

标记为 LCM 的 CM 扼流器针对 CM 电流提供较高的阻抗，其泄漏电感也可提供 DM 衰减。然而，在部分要求接地连接必须保持完好的应用中，该元器件不适用，这些应用需要更安静的转换器设计，CM 扼流器不再是首选。

为了演示 CM 扼流器的效果，图 4 展示了德州仪器 (TI) [LM53603](http://www.ti.com.cn/product/cn/LM53603)，这是一款采用双层 PCB 的 36V、3A DC/DC 转换器解决方案 [7]。该器件的功率级位于顶层，EMI 输入滤波器则放置于底部。如图 4 中的布局所示，滤波器附近的接地平面覆铜区可借助过孔缝合提供屏蔽效果。此外，在滤波器级以下的所有层中插入敷铜层切口，可避免 VIN 和 GND 走线之间产生寄生电容，从而为噪声电流提供绕过 CM 扼流器的路径并让步于滤波器的阻抗特性。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.20.39.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.20.39.png)图 4：DC/DC 转换器原理图和 PCB 布局实施方案

图 5 所示为国际无线电干扰特别委员会 (CISPR) 25 针对图 4 的转换器设计在 150kHz 至 108MHz 之间进行的传导发射测量。我们提供了使用与不使用 CM 扼流器两种情况下的测量结果。使用 Rohde & Schwarz 的频谱分析仪，所得检测器扫描结果的峰值和平均值分别以黄色和蓝色表示。红色限值图象为 5 类峰值和平均值限值（峰值限值通常比平均值限值高出 20dB）。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.22.04.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.22.04.png)图 5：CISPR 25 在使用 CM 扼流器 (a) 与不使用 CM 扼流器 (b) 情况下进行的传导 EMI 测量

### **金属外壳屏蔽**



另一种优化高频 EMI 性能的有效方式是添加金属外壳屏蔽层，从而阻挡辐射电场。外壳通常由铝制成，采用框架（敞开式）或封闭式设计实施方案。屏蔽外壳可覆盖除 EMI 滤波器之外的所有功率级元器件，外壳与 PCB 上的 GND 相连，基本形成了一个带有 PCB 接地平面的法拉第笼。

这使得从开关单元到 EMI 滤波器或长输入线连接（也用作天线）的辐射噪声耦合显著减少。当然，这会产生额外的元器件和装配成本，导致散热管理和散热测试的难度增加。铝电解电容的外壳也可以提供电场屏蔽，为实现此目的，可在电路板上针对性地放置该电容。

### **DC/DC** **转换器案例研究**

图 6 为 60V、1.5A 单片式集成同步降压转换器电路的原理图，该电路通过多项功能实现最佳 EMI 性能。该原理图还显示了一个两级 EMI 输入滤波器级，旨在满足汽车或噪声敏感型工业应用的 EMI 规范。为了帮助实现最佳的 PCB 布局，原理图中将高电流走线（VIN、PGND、SW 连接）、噪声敏感型网络 (FB) 和高 dv/dt 电路节点（SW、BOOT）突出显示。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.23.44.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.23.44.png)图 6：采用 EMI 优化型封装和引脚布局的 DC/DC 转换器。内置一个两级 EMI 输入滤波器

### **a.**  **引脚布局设计**

图 6 所示的转换器 IC 优势在于，其 VIN 和 PGND 采用对称且均衡的引脚排布。该转换器利用两个并联的输入回路使寄生回路电感成功减半。上述回路在 PCB 布局中标记为“IN1”和“IN2”，如图 7 所示。两个外壳尺寸为 0402 或 0603 的小型电容（在图 6 中分别标记为 CIN1 和 CIN3）放置在尽可能靠近 IC 的位置，最大限度减小输入回路面积。两个回路中的环流产生相反的磁矩，消除 H 场并降低有效电感。为了进一步降低寄生电感，PCB 第 2 层（紧靠顶层电源电路的下方）的 IN1 和 IN2 回路下方设有返回电流的连续接地平面，可使场效应自行消除。

在电感两侧各使用一个陶瓷输出电容（COUT1 和 COUT2）同样能够优化输出电流回路。在输出端引出两个并联的接地返回路径可以将返回电流分成两部分，有助于减弱“地弹反射”效应。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.25.24.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.25.24.png)

图 7：仅部署在 PCB 顶层的功率级布局

SW 引脚位于 IC 中心，因此辐射电场会由 IC 两侧相邻的 VIN 和 PGND 引脚屏蔽。GND 平面覆铜区可对将 IC 的 SW 引脚连接到电感端子的多边形覆层施加屏蔽。SW 和 BOOT 的单层布局意味着 PCB 的底侧不会有 dv/dt 较高的过孔。这样可以避免在 EMI 测试期间，电场与基准接地平面耦合。

###  **b.**   **封装设计**

与优化的引脚排布类似，电源转换器 IC 封装设计也是改善 EMI 信号的关键属性。例如，德州仪器 (TI) 的 HotRodÔ 封装技术采用引线框上倒装芯片 (FCOL) 的方式，规避了功率器件线焊导致封装寄生电感过高的情况。如图 8 所示，IC 以上下翻转的形式放置，IC 上的铜柱（也称为凸点或支柱）直接焊接到引线框架。这种构造方法能够提升密度并较薄的外型，因为每个引脚都与引线框架直接相连。从 EMI 角度来看，最重要的一点是，与传统线焊封装相比，HotRod 封装降低了封装的寄生电感。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.26.06.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.26.06.png)图 8：QFN 线焊封装 (a) 和 HotRod FCOL (b) 封装的结构对比

HotRod 封装不仅可以在开关换向（50MHz 至 200MHz 频率范围）期间减少振铃，还可以降低导通和开关损耗。图 9 所示为开关节点电压振铃随之得到改善的情况。图 8 所示为图 6 中的转换器在 150kHz 至 108MHz 下测得的传导发射。测量结果符合 CISPR 25 5 类要求。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.38.26.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.38.26.png)

图 9：使用传统线焊封装的转换器 (a) 和 HotRod FCOL 转换器 (b) 时的开关节点电压波形

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.38.39.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.38.39.png)

图 10：CISPR 25 传导发射测量结果，(a) 频率范围为 150kHz 至 30MHz，(b) 频率范围为 30MHz 至 108MHz

### **总结**

在本文中，我讨论了使用电源转换器 IC 的 DC/DC 稳压器电路可以采用的 EMI 抑制技术。减弱 EMI 的 PCB 布局步骤包括尽量减小布局中的电流“热回路”面积、避免阻断电流路径、采用具有内部接地平面的四层 PCB 结构实现屏蔽（屏蔽效果远超双层 PCB），以及通过尽量减小开关节点覆铜区域面积来降低电场辐射耦合。

转换器封装类型是一项重要的选择标准，新一代器件的开关节点振铃和引脚设计得到显著提升，有助于实现最优的电容放置方案。从输入滤波的角度而言，抑制低频噪声（通常小于 10MHz）相对容易，使用传统的 LC 滤波器级即可实现。然而，抑制高频噪声（10MHz 以上）通常需要额外使用 CM 扼流器和/或铁氧体磁珠滤波器级。焊接到 PCB 接地平面的金属外壳屏蔽层也能有效减轻高频发射。

在本系列文章的下一部分中，我将探讨使用控制器驱动分立式功率 MOSFET 的 DC/DC 稳压器电路适用的 EMI 抑制技术。根据 EMI 进行分析，这些技术更具挑战性。

## **第6部分 —采用离散 FET 设计的 EMI 抑制技术**

### **简介**

本系列文章的第 1 部分至第 5 部分中，介绍了抑制传导和辐射电磁干扰 (EMI) 的实用指南和示例，尤其是针对采用单片集成功率 MOSFET 的 DC/DC 转换器解决方案进行了详细介绍。在此基础上，本文继续探讨使用控制器驱动分立式高、低侧功率 MOSFET 对的 DC/DC 稳压器电路适用的 EMI 的抑制技术。使用控制器（例如图 1 所示同步降压稳压器电路中的控制器）的实现方案具有诸多优点，包括能够增强电流性能，改善散热性能，以及提高设计选择、元器件选型和所实现功能的灵活性。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.43.40.png)图 1：驱动功率 MOSFET Q1 和 Q2 的同步降压控制器的原理图

然而，从 EMI 角度来看，采用分立式 FET 的控制器解决方案与采用集成 FET 的转换器相比，更具挑战性。主要有两方面的考量因素。首先，在紧凑性方面，采用 MOSFET 和控制器的功率级的印刷电路板 (PCB) 布局比不上采用优化引脚布局和内部栅极驱动器的功率转换器集成电路 (IC) 。其次，对于死区时间管理，在 MOSFET 开关时间在额定范围的转换器中通常更精确。因此，体二极管导通时间更短，从而能够改善开关性能并降低与反向恢复相关的噪声。

本文提供与采用 MOSFET 和控制器及半桥设计的多层 PCB 相关指南，以实现出色的 EMI 性能。当务之急是谨慎选择功率级元器件和适合的 PCB 布局，最大程度地减小关键回路寄生电感。布局示例表明，可以在不牺牲效率或热性能指标的情况下减少传导电磁辐射。

### **迎接** **EMI** **相关挑战**

产生 EMI 的三个基本要素包括：电噪声源、耦合路径及受扰接收器。应对其中一个或所有基本要素，可以实现干扰抑制，从而实现合电磁兼容性 (EMC)。在实践中，可以采用多种技术中断耦合路径和/或强化可能的受扰电路，例如插入 EMI 滤波器来抑制传导干扰，借助屏蔽来降低辐射干扰等。

对于与降压稳压器的不连续输入电流（或升压稳压器的不连续输出电流）相关的低频 EMI 频谱幅值，采用传统的滤波器级进行处理相对容易。然而，与开关换向期间电压和电流的尖锐边缘相关的高 dv/dt 以及 di/dt 会产生谐波分量，从而导致出现更大的问题。高电流栅极驱动器（在电压低于 100V 时，通常集成在控制器中）可以以极高的速度开关功率 MOSFET。传统硅 FET 的转换率通常大于 10V/ns和 1A/ns，基于氮化镓 (GaN) 的器件转换率可能更高。我对本文第 2 部分中梯形开关波形的时域特性与其频谱成分之间的关系进行了研究，阐述了波形的最陡斜率决定高频频谱的渐近包络，因此，采用降低 dv/dt 和 di/dt 的方法有助于降低产生 EMI 的可能性。

除了电压和电流的尖锐边沿之外，与开关波形相关的过冲/下冲及随后产生的振铃也非常棘手。图 2 显示了硬开关同步降压稳压器的开关节点电压波形。开关节点电压振铃频率范围为 50MHz 至 250MHz，具体取决于寄生功率回路电感的谐振 (LLOOP)及 MOSFET 输出电容 (COSS)。此类高频分量可以通过近场耦合传播到输出总线、周边元器件或输入电源线，并且难以通过传统滤波衰减。同步 MOSFET 体二极管反向恢复存在类似的负面作用，当二极管恢复电流流入寄生回路电感时，振铃电压升高。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.45.43.png)图 2：同步降压稳压器在 MOSFET 导通和关断转换期间的开关节点电压波形和等效电路

图 3 的原理图标出了降压调节器电路 [6] 的关键高频功率回路，代表了具有高转换率电流的电路元件。可以对升压、反相降压-升压、单端初级侧电感转换器 (SEPIC) 和其他拓扑进行类似检查。最大限度缩减功率回路的面积至关重要，原因是该参数与寄生电感和相关 H 场传播成正比。主要设计目标是通过减小寄生电感最大程度提升寄生 LC 谐振电路的谐振频率。由此，降低存储的无功能量总值，减少开关节点电压峰值过冲和振铃。此外，达到临界阻尼因子的等效电阻实际上更低，因此任何振铃都会更早衰减 - 在高频时的趋肤效应增大回路的寄生电阻时更是如此。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.47.52.png)图 3：标出了同步降压稳压器中对 EMI 至关重要的高频电流回路

图 3 中，还显示了导通和关断期间高侧和低侧 MOSFET 的栅极驱动器回路。务必遵从功率级布局期间的特殊注意事项（下文讨论），确保功率回路、栅极回路和共源寄生电感都尽可能低。

### **实现低** **EMI** **的** **PCB** **布局设计**

以下步骤总结了 DC/DC 稳压器中元器件位置和 PCB 布局的基本准则，以帮助尽可能降低噪声和 EMI 信号。其中一些步骤类似于第 5 部分中针对采用集成 MOSFET 的基于转换器的设计所介绍的步骤。在后续部分，我将提供 PCB 布局案例研究，探讨如何优化降压稳压器 EMI 特性。

- **布线及元器件排布**

  - 将所有功率级元器件排布在 PCB 顶部。

  ​      — 避免将开关节点覆铜和电感放在底部，以免对 EMI 测试装置的基准平面产生辐射。

  - 将 VCC 或 BIAS 的旁路电容放置于靠近各自引脚的位置。

  ​      — 在将 AGND 引脚与 GND 相连之前，首先电路中连入 CVCC 和 CBIAS 电容。

  - 将临近的自举电容与控制器的 BOOT 和 SW 引脚相连接。

  ​       — 利用邻近的接地覆铜屏蔽 CBST 电容和开关节点，降低共模噪声。

- **GND** **平面设计**

  - 将 PCB 分层板中的第 2 层接地平面尽可能放在靠近顶层功率级元器件的位置，以消除 H 场、降低寄生电感及屏蔽噪声。
  - 使用位于顶层与第二层接地平面之间的低 z 轴间距获得最佳映像平面效果。

  ​       — 在 PCB 分层规范中将层间距指定为 6 mil。 

- **输入和输出电容**

  - 放置降压稳压器的 CIN，尽量减小将 CIN 连接到功率 MOSFET 所形成的回路面积。对于升压稳压器和 SEPIC 稳压器的 COUT，同样建议如此操作。

  ​      — 功率回路分类为横向或纵向，具体取决于电容相对于 MOSFET 的放置位置。

  - CIN 和 COUT 的接地返回路径应由集中放置的顶层平面组成。

  ​      — 使用多个外部或内部 GND 平面连接 DC 电流路径。

  - 使用外壳尺寸为 0402 或 0603 的低等效串联电感 (ESL) 陶瓷电容，并放在 MOSFET 附近，以最大限度地减小功率回路寄生电感。

- **电感和开关节点布局**

  - 将电感放置在靠近 MOSFET 的位置。       

  ​      — 尽量减小开关节点覆铜多边形面积，从而尽量避免电容耦合及减小共模电流。覆铜区应仅覆盖电感焊盘并仅占用连接 MOSFET 端子所需的最小面积。

  - 使用邻近的接地保护并通过屏蔽限制开关节点噪声。
  - 检查电感点位置，确保与开关节点相连的绕组末端位于绕组几何结构内部的底部，由连接到 VOUT（降压稳压器）或 VIN（升压稳压器）的绕组的外层绕线提供屏蔽。
  - 选择在封装下方设有端子的电感。

  ​      — 避免使用可能产生天线辐射效应的大型侧壁式端子。

  - 尽可能使用电场屏蔽电感。将屏蔽端子与 PCB 接地平面相连。

- **栅极驱动器布线**

  - 将控制器放置在尽可能靠近功率 MOSFET 的位置。

  ​      — 连接 HO 和 SW 的栅极驱动器时，应分别采用最小的布线长度和最小的回路面积，直接连接到高侧 MOSFET 栅极和源极端子。

  ​      — 将 LO 的栅极驱动器直接连接到接地平面上方的低侧 MOSFET 栅极，并尽量减小介电间距。

  ​      — 对栅极驱动器进行正交布线，尽量减少功率回路与栅极回路之间的耦合。

- **EMI** **管理**

  - 连接 EMI 滤波器元器件时，应避免由电感和开关节点辐射产生的电场形成耦合。

  ​      — 如果 EMI 滤波器与功率级的分隔距离不足，可将 EMI 滤波器放在电路板上转换器的对侧。

  - 在 EMI 滤波器下方的所有层上开口，以防寄生耦合路径影响滤波器的衰减特性。
  - 根据需要，可添加一个与 CBOOT 串联的电阻（最好小于 10Ω），限制 MOSFET 导通速度，从而降低开关节点电压转换率，减少过冲和振铃。

  ​      — 自举电阻会改变驱动电流瞬变率，从而降低 MOSFET 导通期间的开关节点电压和电流转换率。

  ​      — 为提高灵活性，可以考虑使用具有栅极驱动器专用源极引脚和漏极引脚的控制器。

  - 任何所需的开关节点缓冲电路都应根据每次开关转换时的瞬态电流峰值，占用最小的回路面积。

  ​      — 将封装尺寸最小的元器件连接到 SW（通常是电容），尽量降低其天线效应。

  - 使用具有内部接地平面的多层 PCB，与双层设计相比，其性能得到显著提升。

  ​      — 避免阻断 MOSFET 附近的高频电流路径。

  - 考虑采用金属外壳屏蔽优化辐射 EMI 性能。

  ​       — 屏蔽外壳可覆盖除 EMI 滤波器之外的所有功率级元器件，外壳与 PCB 上的 GND 相连，基本形成了一个带有 PCB 接地平面的法拉第笼。

### **DC/DC** **同步降压控制器案例研究**

图 4 显示用于汽车应用或噪声敏感型工业应用的同步降压转换器电路 [6] 的原理图。其中融合了有助于改善 EMI 性能的多项特性，包括恒定开关频率操作、外部时钟同步以及通过高侧 MOSFET 受控导通实现的开关节点整形（转换率控制）。为了帮助实现最佳的 PCB 布局，原理图中将高电流走线（VIN、PGND、SW 连接）、噪声敏感型网络（FB、COMP、ILIM）和高 dv/dt 电路节点（SW、BST、HO、LO、SYNC）突出显示。高 di/dt 回路类似于图 3 中标示的回路。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.55.24.png)

图 4：DC/DC 降压稳压器原理图，其中标示出 PCB 布局的重要节点和走线

图 5 显示了功率 MOSFET 及输入电容的两种横向回路布局。功率级位于 PCB 顶层，控制器放置于底部。横向回路设计在顶层存在循环电流（图 5 中用白框表示），该电流在第二层接地平面上感应出映像电流，以抵消磁通，从而降低寄生回路电感。

更具体来说，修改图 5b 中的布局，使高侧 FET (Q1) 旋转 90 度。这样可以改善 Q1 的散热效果，从而更好地进行热管理，并可以在 MOSFET 附近方便地放置外壳尺寸为 0603 的低 ESL 电容 (Cin1)，以实现高频去耦。考虑到功率级元器件的 U 型布局方向，较短返回连接的输出电容将放置在低侧 MOSFET。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.58.14.png)图 5：两种传统的横向回路布局设计

### **改进后的** **PCB** **布局设计**

图 6 所示为改进后的布局，其优势是可减小功率回路面积，使多层结构达到高效率。该设计将 PCB 的第 2 层用作功率回路返回路径。该返回路径位于顶层的紧下方，形成小尺寸物理回路。垂直回路中的反向电流可使磁场自行消除，从而进一步减小寄生电感。图 6 中的侧视图展示了在多层 PCB 结构中形成小尺寸自行消除回路的概念。

将四个 0603 输入电容放置在尽可能接近高侧 MOSFET 的位置（位于图 6 中大容量输入去耦电容 CIN1 与 CIN2 之间），这四个电容具有较小的 0402 或 0603 外壳尺寸及较低的 ESL。这些电容的返回连接通过多个 12 mil 的过孔连接到第 2 层接地平面。第 2 层接地平面在 MOSFET 的紧下方提供了至低侧 MOSFET 源极端子的电流返回路径。

![](http://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_10.59.34.png)

图 6：采用垂直功率回路设计的功率级和控制器的布局

此外，开关节点覆铜多边形区域只包含电感焊盘以及连接 MOSFET 所需的最小面积。接地平面覆铜区可屏蔽将 MOSFET 连接到电感端子的多边形覆铜区。SW 和 BST 的单层布局意味着 PCB 的底侧不会有 dv/dt 较高的过孔。这样可以避免在 EMI 测试期间，电场与基准接地平面耦合。最后，在电感两侧各使用一个陶瓷输出电容 COUT1 和 COUT2，优化输出电流回路。在输出端引出两个并联的返回路径可以将返回电流分成两部分，有助于减弱“地弹反射”效应。

图 7a 所示为，图 4 中的稳压器采用图 6 中的优化布局时，使用宽带探头测得的开关节点电压波形。振铃不明显，只存在低幅度过冲和下冲，表示 50MHz 以上时 EMI 性能良好。为进行对比，图 7b 显示了采用图 5b 所示横向回路布局的类似测量结果。优化布局的峰值过冲降低约 8V。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.00.53.png)图 7：VIN = 48V，IOUT = 8A 时的开关节点电压波形，(a) 为优化布局，(b) 为横向回路布局

图 8 所示为图 6 中的转换器在 150kHz 至 108MHz 下测得的传导发射。使用 Rohde & Schwarz 的频谱分析仪，所得检测器扫描结果的峰值和平均值分别以黄色和蓝色表示。结果符合国际无线电干扰特别委员会 (CISPR) 25 5 类要求。红色限值图象为 5 类峰值和平均值限值（峰值限值通常比平均值限值高出 20dB）。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.01.58.png)

图 8：CISPR 25 传导发射测量结果，(a) 频率范围为 150kHz 至 30MHz，(b) 频率范围为 30MHz 至 108MHz 

### **总结**

功率半导体器件的开关瞬变是传导 EMI 和辐射 EMI 的主要来源。本文重点介绍在使用控制器和外部 MOSFET 的 DC/DC 稳压器电路中，有助于降低 EMI 的 PCB 布局。关于布局的主要建议包括，尽量减小布局中的电流“热回路”面积，避免阻断电流路径，采用具有内部接地平面的多层 PCB 结构实现屏蔽（性能远超双层 PCB），以差分对形式敷设短而直接的栅极驱动器走线，以及通过尽量减小开关节点覆铜区域面积来降低电场辐射耦合。

优化后的 PCB 布局有助于改善稳压器的 EMI 信号（与降低 EMI 的其他常用“修复”手段不同，不会牺牲效率或热性能）。尽管本文围绕 EMI 敏感的同步降压功率级进行论述，但只要能确定关键回路并实施文中建议采用的布局方法，通常可以将这些概念推广至任何 DC/DC 稳压器。

## **第7部分 —反激式转换器的共模噪声**

### 简介

本系列文章的第 5 和第 6 部分[1-7] 介绍有助于抑制非隔离 DC-DC 稳压器电路传导和辐射电磁干扰 (EMI) 的实用指南和示例。当然，如果不考虑电隔离设计，DC-DC 电源 EMI 的任何处理方式都不全面，因为在这些电路中，电源变压器的 EMI 性能对于整体 EMI 性能至关重要。

特别是，了解变压器绕组间电容对共模 (CM) 发射噪声的影响尤其重要。共模噪声主要是由变压器绕组间寄生电容以及电源开关与底盘/接地端之间的寄生电容内的位移电流所导致的。DC-DC 反激式转换器已被广泛用作隔离电源，本文专门对其 CM 噪声进行了分析。

### **反激式拓扑**

DC-DC 反激式电路[8-9] 在工业与汽车市场领域应用广泛，由于可轻松配置成单个或多个输出，尤为适合低成本隔离式偏置轨。需要进行隔离的应用包括用于单相及三相电机驱动器的高压 MOSFET 栅极驱动器，以及工厂自动化和过程控制所用的回路供电传感器和可编程逻辑控制器。 

反激式实现方案如图 1 中的原理图所示，该实现方案提供了一种结构简单、元件器数量少的可靠解决方案。如果可以采用初级侧稳压 (PSR) 技术，则反馈稳压无需使用光耦合器及其相关电路[8]，从而能够进一步减少元器件数量，简化变压器设计。具有功能型隔离的变压器可直接实现电路接地隔离，而增强型隔离则用于安全要求极高的高压应用。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.10.40.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.10.40.png)图 1：采用典型的 24V 电源或 12V/48V 输入（分别用于工业或汽车电池应用）的 DC-DC 反激式稳压器。图中已明确标出具有磁化作用的反激式变压器、漏电感以及电路寄生电容

### **反激式开关波形特性**

图 2 所示为以非连续模式 (DCM) 和边界导通模式 (BCM) 运行的反激式功率级（如图 1 所示）的初级侧 MOSFET 和次级侧整流二极管电压波形[8]。图 2a 突出显示了 DCM 模式下的开关波形，其中初级侧 MOSFET 在开关节点谐振电压摆幅的谷值附近导通。图 2b 所示为 BCM 开关波形，其中准谐振 MOSFET 在从二次侧绕组电流衰减到零起约半个谐振周期延迟之后导通。在 DCM 和 BCM 模式下，初级侧 MOSFET 均在零电流时导通。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.10.54.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.10.54.png)

图 2：以 DCM (a) 和 BCM (b) 模式运行的反激式转换器初级侧 MOSFET 和次级侧二极管电压波形；跨越初级侧绕组的 DZ 电路可钳位与漏电感相关的电压尖峰

 除了开关期间尖锐的电压和电流边沿，对于 EMI，电压尖峰过冲以及随后产生的振铃特性尤为棘手。每次换向都会激励开关与二极管寄生电容和变压器漏电感之间的阻尼电压和电流振荡。图 2 所示为 MOSFET 关断时的开关节点电压前沿尖峰和高频振铃。振铃特性取决于与 MOSFET 输出电容 (COSS) 谐振的初级侧漏电感 (LLK-P) 以及变压器初级侧绕组电容 (CP)。类似地，二极管电压振铃取决于与二极管结电容 (CD) 谐振的二次侧漏电感 (LLK-SEC) 及二次侧绕组电容 (CS)。过冲和振铃都会产生较高的瞬态电压 (dv/dt)，因此任何至接地端的电容耦合都会导致产生感应位移电流和 CM 噪声。

以连续导通模式 (CCM) 工作时，主开关导通时反激二极管的反向恢复会产生额外的负面作用，使振铃电压升高并产生前沿尖峰电流，随着恢复电流反映到初级侧而流入初级侧 MOSFET。注意，反激式磁性元器件主要相当于耦合电感，因为电流通常不会同时流入初级侧和次级侧绕组。只有在开关转换期间才能出现真正的变压器行为[10]，此时电流同时流入初级侧和次级侧绕组（漏电感中的电流逐渐增大）。

### **隔离式** **DC/DC** **反激式转换器中的** **CM EMI**

图 3 所示为反激式稳压器的原理图，其中连接有用于测量 EMI 的线路阻抗稳定网络 (LISN)。红色虚线表示穿过寄生电容到达接地端并返回到 LISN 的 CM 噪声电流主要传播路径。电容 CZ 从初级侧接地端 (PGND) 连接到次级侧接地端 (SGND)，将次级侧的 CM 电流分流回初级侧，其作用是分流流经 CSE 并通过 LISN 返回的 CM 电流。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.13.37.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.13.37.png)

图 3：双线 DC-DC 反激式稳压器（输入端连接有 LISN）的 CM 噪声电流传播路径。同时，还显示了初级侧基准的辅助输出端

尽管初级侧 MOSFET 漏极端子的高转换率电压是主要的 CM 噪声源，但变压器及其寄生电容是传导 EMI 从初级侧传播到次级侧的耦合通道，并且噪声通过阻抗从输出电路传播到接地端。CM 电流主路径（在图 3 中由 ICM-SEC 表示）为，从变压器的初级侧流到次级侧，并通过阻抗从输出电路流到接地端。与非隔离转换器类似，使用较小的开关节点覆铜面积，将 MOSFET 散热器（如果需要）连接到 PGND，同时避免开关节点完全通过过孔连接到电路板底部[7]，这些措施都能消除从 MOSFET 漏极到接地端的耦合（在图 3 中用 ICM-PRI 表示）。 

对于此处所述的情况，与变压器相关的以下三大考量因素适用。

首先，紧密耦合变压器绕组可以最大限度地降低漏电感，从而实现高效率和高可靠性，同时降低开关电压应力。交错设计是降低漏电感和绕组交流电阻的常用技术，因此，绕组间电容会相对变大。此外，对于具有印刷电路板 (PCB) 嵌入式绕组的平面变压器，由于各个层堆叠紧密，各层的表面积大，因此，绕组间电容比传统的绕线型设计更高。在任何情况下，将脉冲噪声电压源施加到这种分布式寄生电容，都会产生相对高的位移电流。该电流从初级侧绕组流向次级侧绕组，然后返回到接地端，从而产生较大的 CM 噪声[11]。

其次，与寄生绕组间电容谐振的漏电感可能导致测得的 EMI 频谱中出现明显的高频 CM 噪声峰值。 

第三，由于磁芯材料介电常数较高，对电场的阻抗低，因此，由高 dv/dt 节点产生的杂散近电场很容易通过变压器磁芯耦合。然而，如果将磁芯包上铜箔并将铜箔连接到 PGND，则磁芯与地之间的寄生电容 (CME) 会很小。

通常，反激式变压器设计的优化不仅关乎解决方案尺寸、外形、效率和热性能，对 CM 噪声性能也有巨大影响。

### **CM** **噪声分析模型**

图 4a 所示为双绕组变压器，初级侧端子和次级侧端子分别由（A、B）和（C、D）表示。端子 A 根据输入总线电容等效连接到 PGND，在 CM 噪声分析的适用频率下表现为有效短路。图 4b 显示的是变压器的传统静电模型。从节能角度来看，可建立包含六个电容的双绕组变压器的寄生电容模型，其中包括四个绕组间电容（C1、C2、C3、C4）和两个绕组内电容（CP、CS）。

除了影响脉冲开关电压波形的 dv/dt 之外，绕组内电容不影响从初级侧到次级侧的位移电流。此六电容此模型不必要地提高了复杂性，并增大了变压器等效电容的计算难度。但是，用等效噪声电压源代替非线性开关器件（根据 CM 噪声分析的替换定理[12]）时，会将一个独立或非独立的噪声电压源与变压器绕组并联，并且可以去除两个绕组内电容。绕组电容模型可简化为四个集总电容，如图 4c 所示，图中 *vSW* 和 *vSW/*NPS 分别是初级侧绕组和次级侧绕组上的开关电压源。假设漏电感较低，则绕组电压会如预期般根据变压器匝数比 NPS 变化。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.15.24.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.15.24.png)

图 4.(a) 用于 CM 噪声分析的双绕组变压器；(b) 六电容 CM 模型；(c) 四电容 CM 模型。

最后，当其中一个变压器绕组等效连接到独立电压源（以替代非线性开关）时，两个集总电容便足以表现出双绕组变压器绕组间寄生电容的特征。双电容模型的推导与位移电流守恒原则一致[12,13]。如图 5a 所示，可能的双电容绕组电容模型总共有六种。图 5b 显示了其中一种可能的双电容 CM 模型实现方案（使用电容 CAD 和 CBD）及其相应的戴维宁等效电路。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.16.22.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.16.22.png)图 5：(a) 六种可能的双电容 CM 模型；(b) 双电容 CM 模型及其戴维宁等效电路

双电容 CM 噪声模型可灵活地用于不同的隔离型稳压器拓扑，并有助于通过实验测量推导出变压器集总电容模型[13]。CTOTAL 是用阻抗分析仪测得的变压器结构化绕组间电容，测量时将初级侧和次级侧端子短接，然后将变压器用作单端口网络。对初级侧绕组端子（A、B）施加源阻抗为 50W 的开关频率正弦激励信号，并测量 VAD 与 VAB 的电压比，可由公式 1 推导出 CBD：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.17.37.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.17.37.png)

显然，该模型的优点是通过简单的实验测量即可轻松推导出寄生电容，而无需了解变压器结构或电位沿绕组的分布情况[13]。 

### **反激式稳压器** **CM** **噪声模型**

图 6 所示为具有初级侧、次级侧、辅助和屏蔽绕组的反激式变压器的 CM 模型（与图 3 类似，但包含一个初级侧接地屏蔽绕组）。NA 和 NSH 分别是初级侧绕组与辅助绕组以及初级侧绕组与屏蔽绕组的匝数比。对于初级侧绕组与辅助绕组的耦合以及初级侧绕组与屏蔽绕组的耦合，由于电流仅在初级侧流动，不会返回 LISN，因此对所测量的共模噪声不产生影响，因此不考虑这些耦合。这样，三个 4 电容电路便足以对初级侧到次级侧、辅助到次级侧以及屏蔽到次级侧绕组之间的耦合进行建模。根据用作 CM 噪声低阻抗的输入电容，初级侧绕组的端子 A 与 PGND 短接。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.19.06.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.19.06.png)

图 6：(a) 多绕组反激式变压器集总 CM 寄生电容模型；(b) 双电容 CM 模型；(c) 戴维宁等效电路

根据前面的讨论，只需要两个独立电容和一个电压源即可描述 CM 特性，表达式已包括在图 6 中。如前文所述，CTOTAL 是测得的短路初级侧基准绕组与短路次级侧绕组之间的电容。

为建立图 3 中反激式稳压器的 CM 噪声模型，图 7 中用方框突出表示了随后替换为适当双电容 CM 变压器模型的变压器（包括初级侧、次级侧、辅助和屏蔽绕组）。根据替换定理，将电路中的非线性开关器件替换为时域电压或电流波形与原始器件完全相同的电压或电流源时，电路中的所有电压和电流都不会发生变化。因此，电压波形与 MOSFET 的漏源极电压相同的电压源 (VSW) 将代替 MOSFET。同样，电流波形与二极管电流相同的电流源 (IDOUT 和 IDCL) 将代替两个二极管。替代后，电路中的电压和电流保持不变。

同时，输入和输出电容对 CM 噪声的阻抗非常小，因此可将其阻抗忽略。CM 扼流器串联阻抗表示为 ZCM-CHOKE，25W 测量电阻反映了 LISN 的特征。最后，去除了对流经 LISN 的 CM 噪声没有显著影响的寄生电容。图 7a 呈现了应用替换定理后反激式稳压器的 CM 噪声模型[14]。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.20.14.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.20.14.png)图 7：(a) 基于替换定理的反激式电路模型；(b) 应用叠加定理后反激式稳压器的最终 CM 模型



与电压源并联或与电流源串联的元器件对网络中的电压或电流无影响，因此可以去除。叠加定理可帮助分别分析 IDCL、IDOUT 和 VSW 的作用。显然，IDCL 和 IDOUT 已短路，不会产生 CM 噪声。图 7b 显示的是最终 CM 模型，公式 2 可计算在 LISN 测得的 CM 噪声电压：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.20.30.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.20.30.png)

随后，可以方便地应用包含测得的 VSW 波形的电路仿真，对 CM 噪声以及各个元器件所产生的影响进行分析。如果假设漏电感的阻抗远低于总寄生绕组电容 CTOTAL，则可以认为该模型是准确的。显然，减小 CBD 和增大 ZCM-CHOKE 或 CZ 都会导致噪声电压降低。注意，如果根据公式 1 测得的 VAD 为零，则 CBD 实际上是零，基本上消除了通过变压器的 CM 噪声。这是非常方便的测试变压器是否平衡的手段。

基于双电容变压器模型的 CM 噪声模型的一般推导过程遵循以下六个步骤：

1. 应用替换定理，将非线性半导体器件替换为等效电压源或电流源。替换的原则是，获得易于分析的 CM 噪声电路，同时避免电压回路和电流节点。电压源和电流源的时域波形应与原始器件相同。输入电容和输出电容对 CM 噪声的阻抗非常小，因此视为短路。
2. 如果将其中一个变压器绕组与电压源并联，则将所有其他绕组替换为受控电压源，因为绕组电压取决于变压器匝数比。
3. 去除所有与电压源并联或与电流源串联的元器件，简化模型。
4. 用图 5a 中最能简化 CM 噪声分析的其中一个双电容模型替换原来的变压器。
5. 根据叠加定理，分析由所有电压源和电流源产生的 CM 噪声。
6. 分析使用步骤 1 到 5 创建的电路，去除对流经 LISN 的 CM 噪声无影响的寄生电容。根据所得的 CM 噪声模型检查 CM 噪声电流。

### **总结**

从 EMI 的角度来看，传统的硬开关隔离式转换器与非隔离式转换器相比更具挑战。近来，业界对于隔离式 DC-DC 稳压器中高频变压器的性能要求愈发严苛，尤其是在 EMI 方面。变压器不断变化的绕组间电容相当于 CM 噪声的关键耦合路径。

所提出的变压器双电容模型应用广泛，使用简单，这是因为其集总电容可通过一种简单的测量方法轻松量化。在本 EMI 系列文章的下一部分，将采用该模型设计隔离型转换器的 EMI 抑制技术并对其进行表征，其中包括噪声平衡及噪声消除等内容。

## **第8部分 —隔离式 DC/DC 电路的共模噪声抑制方法**

### 简介

近来，业界对于隔离式 DC-DC 稳压器中高频变压器的性能要求愈发严苛，尤其是在抗电磁干扰 (EMI) 方面。在本系列文章的第 7 部分[1-7] 中，我们详细探讨了隔离式反激稳压器中共模 (CM) 噪声的主要来源和传播路径。

高瞬态电压 (dv/dt) 开关节点是共模噪声的主要来源，而变压器的绕组间分布电容则是共模噪声的主要耦合路径。在第 7 部分中，我们在简单方便的双电容变压器模型基础上，采用共模噪声等效电路来模拟流经变压器电容的位移电流。在此期间，仅需使用一个信号发生器和一个示波器即可提取寄生电容并确定变压器共模噪声性能的特征，而无需进行在线测试。

在第 8 部分，我们将探讨隔离式 DC/DC 电路的共模噪声抑制方法。工作在高输入电压下的转换器（例如，电动汽车车载充电系统、数据中心电源系统和射频功放电源中的相移式全桥转换器[8] 和 LLC 串联谐振转换器[9]）会产生较大的共模电流。在采用氮化镓开关器件时，这种情况更为明显，因为此类器件的开关速度 dv/dt 高于硅材质的同类器件。

对于隔离式设计，有多种抑制共模噪声的方法，包括采用对称的电路布局、在初级侧接地端与次级侧接地端之间连接一个电容、加入屏蔽层、增加平衡电容、优化变压器绕组设计以及使用可调节共模噪声消除辅助绕组。本文将以反激电路为重点，逐一解读这些方法。

### **对称式电路设计**



在对称式拓扑结构中，与地之间形成互补电势的开关节点成对出现。如果关联寄生电容相同，则产生的共模位移电流基本可以相互抵消。图 1a 为双开关正激转换器（例如德州仪器 (TI) 的 [LM5015](http://www.ti.com.cn/product/cn/LM5015)）的原理图[10,11]。图 1b 为采用分立式初级侧和次级侧绕组的反激转换器。这两种转换器的初级侧电路均采用对称式设计，具有异相电压开关波形（SW1 和 SW2），可产生相反极性的共模电流，从而降低总共模噪声。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.47.10.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.47.10.png)

图 1：平衡绕组拓扑结构，采用对称式初级侧电路和等幅异相 dv/dt 开关波形，具有更低共模噪声：(a) 双开关正激转换器；(b) 采用分立式初级和次级绕组的反激转换器

 图 1a 为双开关正激转换器的拓扑结构，尽管这种结构早已为人所熟知，但其在共模噪声抑制方面的优势却并未得到充分重视。图 1b 为平衡绕组反激转换器，其次级绕组同样采用对称式设计。分立式绕组通常可以交错缠绕，以降低漏电感。这种电路的主要缺点是需要一个以 SW2 为基准点的浮动栅极驱动器。

对于单开关正激转换器和 LLC 谐振转换器拓扑，也可以采用类似的对称式平衡绕组设计，如图 2 所示。改进后的对称电路需要额外增加一些元件，例如正激转换器中的浮动栅极驱动器和 LLC 谐振电路中的附加开关，并且只有在变压器的物理绕组结构产生对称的寄生电容时才会产生共模衰减的效果。因此通常情况下，需要采用其他方法来抑制共模噪声，并使用传统的隔离式拓扑电路。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.48.23.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.48.23.png)图 2：对单开关正激转换器 (a) 和 LLC 谐振转换器 (b) 采用对称式初级侧绕组设计

### **在初级地与次级地之间连接一个电容**



在三线 AC-DC 应用中，通常会在 EMI 输入滤波器中通过一个 Y 电容将火线和零线连接到机箱地，用以衰减共模噪声。但在双线 DC-DC 系统中，由于没有机箱地连接点，因此无法连接 Y 电容。在这类系统中，可以在初级侧接地端 (P-GND) 与次级侧接地端 (S-GND) 之间连接一个替代电容，将传播到次级侧的共模电流分流回初级侧。

请参见第 7 部分图 1 中的 CZ 电容。该元件是一种安全级电容，额定电压为 1 kV 或更高，远高于所需的隔离电压规格。然而这种电容一旦在故障状况下出现短路，就会大大影响电流隔离效果。此外，如果 S-GND 连接的共模电压摆幅相对于初级侧过大（例如在高侧栅极驱动器偏置电源应用中），电容传导的电流就会过大。同时，如果 DC-DC 级的前端是一个 AC-DC 前端整流器，则该电容可能会传导工频泄漏电流，这在实际应用中可能是不允许的，也是受到监管要求限制的[12-15]。

### **共模噪声的平衡与消除方法**



平衡方法分为变压器内部平衡和外部平衡，可以降低与变压器绕组电容相关的共模噪声。内部平衡方法包括应用屏蔽层[16-18]、优化绕组设计以及使用噪声消除绕组。而外部平衡方法最常见的是在所选初级和次级绕组端子之间加入一个平衡电容[12]。

### **屏蔽**

屏蔽方法通过插入导线或金属箔屏蔽层来降低流经绕组间电容的位移电流，从而阻止变压器初级侧绕组与次级侧绕组之间的近场耦合。

例如，图 3a 是一个反激转换器，其初级侧与次级侧之间加入了一个传统的单匝金属箔屏蔽绕组。图 3b 是 RM 型磁芯的示意图，磁芯配有带气隙的中柱和垂直放置的绕组。在这半个绕组窗口中，共有两个串联的初级层 (2 x 12T)、一个次级层 (1 x 8T) 和一个屏蔽层。绕组采用非交错式分层布局，分为 P1、P2、SH1 和 S1 四层。图中还显示了绕组层间寄生电容。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.50.13.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.50.13.png)图 3：(a) 反激转换器，其初级层与次级层之间带有传统的金属箔静电屏蔽绕组，该屏蔽层连接到 P-GND；(b) 变压器绕组窗口内的绕组层结构

在初级层 P2 与次级层 S1 之间，加入了一个单屏蔽层 SH1。该屏蔽层通常连接回初级侧电路中的静态电位点，例如图 3 所示的本地 P-GND 或输入电容的正极端子，即静态交流节点。这样可以阻止 P2 和 S1 之间的电耦合，并消除 P2 与 S1 之间的位移电流。

加入屏蔽层后，ipsh 将经由屏蔽层返回 P-GND，而不是流经输出端而返回机箱地。但是，屏蔽层与相邻次级绕组之间的电容依然存在。由于单匝屏蔽绕组与次级绕组的感应电压存在差异（单匝次级绕组除外），因此在屏蔽层与次级绕组之间必然存在共模电流。可改用辅助绕组的抽头来驱动屏蔽绕组，使屏蔽绕组的平均电压与次级绕组的平均电压相符，以实现共模平衡[18]。

注意，由于磁芯采用高介电常数材料，图 3 中 P1 层和 S1 层之间会存在耦合。所以，尽管单屏蔽层有助于减弱共模噪声，但并不能彻底消除。此外，还有一个缺点是，随着初级侧与次级侧间边界数量的增加，需要的屏蔽层也越来越多。重要的是，屏蔽层会增大绕组之间的空间，从而导致漏电感增加。通常而言，应尽可能减小铜箔屏蔽层的厚度，以减少因邻近效应引起的涡流损耗。在高开关频率下，屏蔽层中的损耗会变得过大，而且屏蔽层也会使反射到开关节点的总寄生电容增大。

### **平衡电容的值与位置**



图 4a 为带初级侧、次级侧和辅助变压器绕组的反激转换器的原理图。NPS 和 NAUX 分别代表初级侧与次级侧绕组匝数比以及初级侧与辅助绕组匝数比。对于初级侧绕组与辅助绕组而言，由于电流仅在初级侧流动，对共模噪声不产生影响，因此不考虑这两者之间的耦合。在第 7 部分中我们曾讨论过，通过两个 4 电容电路即可对初级侧绕组与次级侧绕组之间以及辅助绕组与次级侧绕组之间的耦合进行建模（如图 4b 所示）。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.51.58.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.51.58.png)图 4： (a) 带辅助绕组的反激转换器；(b) 三绕组反激变压器的集总共模寄生电容模型；(c) 使用双电容变压器模型的共模噪声等效电路

如果输入电容对共模噪声呈现低阻抗特性，则初级侧绕组的端子 A 与 P-GND 之间短路。可以使用简化的双电容变压器模型，再以 ZSE 模拟 S-GND 与大地之间的电容耦合，最终的共模噪声等效电路模型见图 4c（有关更多相关信息和描述，请参见第 7 部分）。

公式 1 用于计算线路阻抗稳定网络 (LISN) 中的共模噪声电压。从中可以看出，降低电容 CBD 可以使噪声电压降低。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.53.14.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.53.14.png)  

公式 2 是 CBD 的理论表达式，该值可使用第 7 部分介绍的方法基于公式 3 进行计算：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.56.20.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.56.20.png)  

可以通过增大公式 2 中各负项的值，将 CBD 平衡为零[13]。最简单的方法是在初级侧和次级侧间变压器端子 A 和 C 之间的 C3 上并联一个电容。这一外部平衡电容的值为 CEXT = NPSCBD。

同样，如果 CBD 为负值（VAD 和 VAB 电压异相），则在端子 B 与 D 之间的 C4 上并联一个等于 |CBD| 的平衡电容，可实现平衡。注意，根据公式 3，如果测得的 VAD 为零，则 CBD 也相当于零，基本消除了通过变压器的共模噪声。这是非常方便的测试变压器是否平衡的手段。

### **绕组设计**

除了使用平衡电容外，还可以通过调整变压器绕组层的位置，来优化共模平衡。根据成对绕组层的设计理念[12-15]，变压器初级侧和次级侧的层具有相似的 dv/dt，因此，这些层的交错重叠不会产生共模噪声。绕组间电容两端的平均电压具有相似的幅值和极性，也可以最大程度减小甚至消除流经电容的共模电流。

一个最基本的原则就是，确保相邻的初级侧绕组层与次级侧绕组层具有相似的电压分布。如果绕组间寄生电容均匀分布于两个成对绕组层之间，可以使电容的 dv/dt 保持为零，这样便不会产生共模电流。

以图 4a 的反激转换器为例，其变压器为交错式三绕组（初级侧、次级侧、辅助）变压器。尽管交错式设计会增大绕组间电容，但出于降低漏电感和邻近效应损耗的考虑，必须采用这种设计。图 5a 是反激变压器的半个绕组窗口，该变压器包含三个串联初级层 (3 x 12T)、两个并联次级层 (2 x 9T) 和一个辅助/偏置绕组层 (1 x 15T)。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.57.46.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.57.46.png)图 5： (a) 采用夹层绕组层结构的反激变压器；(b) 绕组窗口内各绕组层的电压分布

图 5b 为在电压沿绕组线性分布情况下的绕组电压分布图。为最大程度降低共模噪声，应使初级侧绕组层与次级侧绕组层之间相邻绕组层的平均电压差达到最低。因此如图 5a 所示，将交错绕组层的排列顺序设计为 S1-P1-S2-AUX-P2-P3。

采用如图 5a 所示的端子连接时，P1 与 S1 或 S2 之间的平均电压差最低。如图 5a 所示，P1 始于 VIN（静态节点），与两个并联次级层 S1 和 S2 相邻。与之类似，AUX 绕组与 S2 层相邻，因为 AUX 与 S2 之间的电压差小于 S2 与 P2 或 P3 之间的电压差。由于 AUX 与 P2 绕组均位于初级侧，因此两者之间的电压差不会产生共模噪声。两者之间的位移电流同样在转换器初级侧流动，不会被 LISN 视为 EMI。相反，如果采用 P1-S1-P2-S2-AUX-P3 这种完全交错的绕组结构，由于 S1 与 P2 以及 P2 与 S2 这两对绕组层之间的平均电压差增大，共模噪声将明显增强。

### **可调节噪声消除辅助绕组**

图 6 中的 AdjAUX 是一个可调节噪声消除辅助绕组层，缠绕在次级层 S1 的外侧，用以平衡绕组层内未完全消除的共模噪声[13,14]。AdjAUX 的一个端子连接到 P-GND，另一个端子处于悬浮状态。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.59.12.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_06-_0B4E4853_11.59.12.png)图 6： (a) 在外层增加可调节辅助绕组用以消除共模噪声的原理图；(b)绕组排列情况；(c) 电压和电流分布

由于 AdjAUX 与 S1 之间的电压差为负值，因此位移共模电流从 S1 流向 AdjAUX 绕组，再流回初级侧。由于 P1 与 S1、P1 与 S2 以及 AUX 与 S2 层之间的电压差为正值（本例中 P1 和 AUX 的匝数多于 S1 和 S2 的匝数），因此这样有助于消除从 P1 流向 S1 和 S2 以及从 AUX 流向 S2 的位移共模电流。如图 6b 所示，AdjAUX 绕组位于变压器绕组的外层，因此可以方便地通过调整匝数来有效消除噪声。

如图 6c 所示，当 AdjAUX 绕组始于绕组窗口的顶部时，AdjAUX 与 S1 层之间的电压差最大，需要较少匝数来达到消除噪声的效果，而如果 AdjAUX 绕组位于窗口底部，则需要的匝数就会更多。

由于 AdjAUX 绕组不靠近气隙，会产生零磁场，因而没有涡流功率损耗。这样，变压器交流绕组损耗低于采用传统屏蔽层时的损耗。同时，由于绕组层之间没有屏蔽层，绕组间的互耦增高，使得漏电感降低[18]。最后，可以结合第 7 部分介绍的变压器平衡检测技术，来方便地设计 AdjAUX 绕组层，无需任何在线测试。

### **总结**



共模噪声是高频隔离式 DC/DC 转换器设计中需要重点关注的问题。为了提高功率密度，设计师们往往会考虑增大开关频率。而随着开关频率的增大，初级侧开关节点的高 dv/dt 以及通过变压器绕组间电容的相关共模干扰已经给系统带来不利影响。要降低共模噪声，可以采用对称式拓扑设计、加入屏蔽层以及平衡电容等方法。在进行绕组设计时，也可以通过正确布置变压器层以及在绕组层端子与电路节点间选择最优的连接，来达到降噪的目的。此外，在变压器外侧缠绕辅助的噪声消除绕组也可以平衡共模噪声。对于某些拓扑结构，可以单独这些方法，而为了满足规范要求并解决复杂的共模噪声问题，也可以发挥这些方法的组合优势，以达到提高降噪效果的目的。

## **第9部分 —扩频调制**

### 简介

削弱电磁干扰 (EMI) 是所有电子系统中存在的问题。许多规范将电磁兼容性 (EMC) 与适应规定屏蔽下干扰功率谱级的能力相关联，恰恰证明了这一点 [1]。尤其是高频开关 DC/DC 转换器，开关换向过程中存在的高转换率电压和电流可能在稳压器自身（EMI 源）以及附近的敏感电路（受 EMI 干扰的设备）中产生严重的传导和辐射干扰。本系列文章 [1-8] 的第 5 部分和第 6 部分回顾了多种适用于非隔离稳压器设计的 EMI 抑制技术。第 7 部分和第 8 部分回顾了隔离设计中的共模 (CM) 噪声及其抑制技术。

一般而言，遵守电磁标准对于开关电源愈发重要，这不仅局限于总光谱能量过大，更多的原因是能量集中在基本开关频率及其谐波的特定窄带中。为此，第 9 部分提出通过扩频调频 (SSFM) 技术将频谱能量分配到频谱中，使基波和谐波噪声峰值幅值变得平整。图 1 所示的扩频效应可作为本系列文章前几部分中介绍的 EMI 抑制技术的补充降噪方法。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.04.33.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.04.33.png)  

图 1：扩频效应

### **扩频调制**

本系列文章第 5 部分和第 6 部分中探讨的 EMI 抑制技术重点关注减小天线因子，实现方式为谨慎使用高转换率电流 (di/dt) 回路布局以及采用适当的缓冲电路和栅极驱动电路设计来避免剧烈的瞬态电压 (dv/dt)。这些方法通过降低总功率来调整传导噪声和/或辐射噪声功率频谱的形状，主要对高频有效，对于低频的作用效果可能较为有限。

相反，1992 年首次针对 DC/DC 转换器提出的扩频调制（也称为抖动）[9] 希望在不影响总噪声功率的前提下针对传导和辐射干扰功率谱的形状进行调整。通过在时域中对基准时钟信号进行频率调制 (FM)，会根据调制信号在频域中对基波和谐波分量进行扫频 [9-14]。如图 1 所示，每个谐波均转化为若干个幅值较小的边带谐波。噪声频谱从大频谱峰值集中在开关频率及其谐波处的一系列频谱变为更加平缓、峰值更小并且更加连续的频谱。

从实际 EMC 的角度来看，当窄带 EMI 源的信号频率与受 EMI 干扰的敏感频率范围相匹配时，可在给定时间窗口内传输大量功率，受 EMI 干扰的设备受到干扰或发生故障的概率随之增大。如果将 EMI 源信号扩展到大于受 EMI 干扰设备的敏感带宽，耦合到受干扰设备的噪声功率随之减小，从整体改善 EMI 性能和可靠性。

### **周期性调制函数**



周期性扩频调制技术的主要作用是将各谐波扩展到预设频段，降低峰值幅值并减弱 EMI 水平。在这一背景下，公式 1 提供了通过扩频调制对正弦载波进行调频的一般分析表达式：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.05.59.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.05.59.png)

其中 *A* 是未调制信号的幅值，*fc* 为载波频率，Δ*f* 是频率偏差。

归一化周期调试函数为 *ξ*(*t*)，反映了扩频的频率变化。表 1 列出了正弦波、三角波和指数（也称为三次方或“好时之吻”）调制曲线 [10] 的数学表达式。其中，*kT* 是三角波曲线的对称指数，取值范围为 0 到 1，*p* 用于指定指数曲线的凹度系数。如果 *kT* 为 0.5，则三角波曲线具有对称的三角形图案。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.07.34.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.07.34.png)表 1：正弦波、三角波和指数调制曲线，其中 fm 和 Tm 分别为调制信号频率和周期

 图 2 所示为采用 10kHz 调制频率的正弦波、三角波和指数调制信号。图中还可以看出，通过调制 100kHz 正弦载波信号得出的相应扩频结果与公式 1 一致。每个图象的顶部均指出明显的瞬时载波工作频率。

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.09.24.png)图 2：*fc* = 100 kHz、Df = 50 kHz、fm = 10 kHz、kT = 0.5 和 p = 70 kHz 时的正弦波 (a)；三角波 (b) 和指数 (c) 调制曲线

其它相关项分别为公式 2 和 3 得出的调制系数与调制比：

![](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.11.37.png)   

*s(t)* 的总功率等于 *A*2 / 2。根据卡森带宽规则，总功率使用扩频技术分配，即扩频后的能量有 98% 包含在公式 4 中给出的带宽 B 中（请参见图 1）：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.11.43.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.11.43.png)

对于更为复杂的波形，比如开关节点电压波形或 DC/DC 转换器的输入电流波形，更改瞬时频率相当于对傅里叶级数展开的每个构成谐波应用公式 1。唯一的区别在于会将第 *n* 次谐波在 *n* 倍卡森带宽（由公式 5 得出）的带宽范围内进行扩频。 

*s*(*t*) 频谱的实际形状由 D*f* 和 *ξ*(*t*) 决定。如果 *ξ*(*t*) 是周期为 *Tm* 的周期函数，则 *s*(*t*) 的频谱呈离散状态，这意味着可将信号分解为一系列频率为 *fc* ± *k*/*Tm* 的正弦音调，每个信号的幅值为 *Ak*。可通过贝塞尔函数计算正弦调制的 *Ak* [9，10]，而三角波调制的频谱形状已通过 Matlab 仿真进行评估 [11]。

真正连续的功率频谱只能通过非周期调制函数获得（如使用混沌序列发生器或随机序列发生器获得），并通过功率频谱密度进行描述。与周期扩频技术相反，非周期调制测得的频谱形状与测量仪器的分辨率带宽 (RBW) 设置无关 [15，16]。下一节将探讨 RBW 对于 EMI 测量的影响。

虽然正弦扩频技术更易于分析和实现，但无法获得最佳频谱形状并且谐波衰减未达到最大程度。如图 3 所示，调制波形频谱中的能量趋向于集中在调制波形中时间导数较小、靠近正弦波形波峰和波谷的各点对应的频率。另一方面，指数调制函数具有最平坦的频谱，可针对靠近卡森带宽两端出现的二阶效应而产生的峰值进行补偿，进一步减小 EMI。然而，指数波形在实践中难以实现，通常需要复杂的失真电路或查询表。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.13.38.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.13.38.png)图 3：正弦波 (a)、三角波 (b) 和指数 (c) 调制曲线及频域特性

线性三角形调制代表图 3 所示的调制曲线之间已达到良好的折中，很容易在模拟和数字域中实现。通过选择经过优化并且正确定义的三角波驱动信号频率，最大限度地降低测得的 EMI 频谱的峰值，可以为汽车等大批量、成本优化型应用提供稳健的设计。

### **通过扩频优化** **EMI** **抑制**



国际规定要求使用 EMI 接收器进行测量。EMI 接收器的本质是额外配备一些输入滤波器的模拟频谱分析仪。鉴于测量 EMI 的超外差频谱分析仪的复杂性 [16]（特别是解调包络检波器和峰值/准峰值/平均值检波器的非线性），[11] 中的研究人员使用 EMI 接收器的 Matlab 模型，通过基于三角波调制的扩频技术计算降低的 EMI，从而得出三角波扩频的优化曲线。举例来说，图 4 提供的噪声级下降曲线基于多个频率偏差值 D*f*，均为 EMI 接收器 RBW 设置的倍数。请注意，如果 *m* 超出某一特定值，EMI 抑制性能随之下降。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.14.58.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.14.58.png)图 4：与不同 RBW/Df 比的 EMI 接收器响应相一致的三角波调制功率频谱噪声级下降，其中固定 Df 并改变 fm 时，调制系数会发生变化。0dB 基准是未调制的情况

选择调制扩频参数 D*f* 和 *fm* 时，需要在两方面进行权衡。首先，D*f* 应足够大，减小 EMI 测量值并降低易受 EMI 影响的设备所受的干扰。例如，为了避免在 AM 无线频段内产生干扰，汽车 DC/DC 稳压器通常使用外部电阻将自由运行的开关频率设置为 2.1 MHz（容差为 5%-10%）。为了在 1.6 MHz 的最大 AM 频段中以足够的裕度运行，合理的方法是在 100kHz 至 150kHz 的范围内使用 D*f* 进行中心扩频调制，可避免对稳压器输出电压纹波幅值和效率性能造成过大干扰。

确定 D*f* 后，优化 EMI 性能的附加自由度取决于所选调制频率。根据图 4，调制系数 *m* 应具备一个适宜的中间值，大到可提供 EMI 衰减，同时小到 RBW 带通滤波器的时域效应不适用。具体而言，如果 *fm* 过低，瞬时干扰信号频率处于 RBW 滤波器响应时间内的时间间隔会增大。信号长时间以未调制状态出现在测量窗口中，可以有效测量未调制信号的幅值。这种短期时域效应同样应用于易受 EMI 干扰的电路及其敏感频段。

因此，在规定频率范围内使用指定 EMI 测量设置时，为了正确估计扩频技术的影响，务必考虑时域特性。例如，针对汽车应用的国际无线电干扰特别委员会 (CISPR) 25 等规定要求，在 150kHz 至 30MHz 以及 30MHz 至 1GHz 的频段进行测量时，RBW 设置应分别为 9kHz 和 120kHz。按照经验法则，如果将 *fm* 设置为与要求的 RBW 相近，则 EMI 接收器能够独立测量各个边带谐波，使测量结果与预期计算值相符。

### **实践案例研究**

图 5 为使用两个双相可堆叠控制器的四相同步降压稳压器电路 [17] 示意图。控制器采用多种功能降低 EMI，包括恒定开关频率操作、外部时钟同步以及通过分离各电源开关的栅极驱动输出实现开关节点整形（转换率控制）。

控制器工作时使用的电阻可调节开关频率高达 2.2MHz，进行外部同步后可达 2.5MHz。SSFM 可通过以下三种方法进行配置：

- 使用控制器的外部同步 (SYNCIN) 输入，施加采用所需调制技术的频率信号。
- 通过电阻将调制信号与 RT 引脚耦合。
- 使用 DITH 引脚上的电容设置调制频率，然后使用内置的 ±5% 三角波扩频（抖动）函数。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.16.31.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.16.31.png)图 5：采用三角波扩频调制的四相同步降压稳压器示意图

给定的标称开关频率为 2.1MHz，使用集成扩频功能时的频率偏差 Δ*f* 为 5% 或 105 kHz。EMI 接收器使用频率为 9kHz 的 RBW 滤波器，在 150kHz 至 30MHz 的范围内进行测量。频谱分析仪中的 EMI 滤波器带宽通常设定为 -6dB、具有四极并且波形接近高斯形状 [16]，因此应用校正因数后，9kHz RBW 滤波器的 -3dB 有效带宽认定为约 6kHz。基于与图 4 相似的优化曲线，使用公式 5 计算归一化分辨率，可得出优化的调制系数约为 10：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.16.55.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.16.55.png)  

此后，通过公式 6 推导出所需的调制频率：

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.16.59.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.16.59.png)  

图 6 显示的是启用和禁用扩频后的开关节点电压波形（使用图 5 中的稳压器测量）。图 6b 中的波形范围恒定不变，展示开关频率的变化情况。

[![ ](https://e2echina.ti.com/resized-image/__size/2460x0/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.19.53.png)](https://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.19.53.png)

图 6：禁用 (a) 和启用 (b) 扩频后的开关节点电压波形 (VIN = 13.5 V，VOUT = 5 V，IOUT = 20 A)

图 7 所示为在 10 kHz 处设置三角波调制后，在 150kHz 至 30MHz 的范围内测得的图 5 中稳压器的传导辐射。使用 Rohde & Schwarz 的频谱分析仪，所得检测器扫描结果的峰值和平均值分别以黄色和蓝色表示。测量结果符合 CISPR 25 5 类 的要求。红色的限值线对应 CISPR 25 5 类的峰值限值和平均限值（峰值限值通常比平均限值高出 20dB）。

![img](http://e2echina.ti.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-00-65/_4F5C555EEB5F6771_-2019_2D00_08_2D00_07-_0A4E4853_12.20.55.png)

图 8：禁用 (a) 和启用 (b) 扩频后，CISPR 25 5 类的传导辐射结果（150kHz 至 30MHz）



### **总结**

对于较为拥挤的电磁波谱，开关电源是导致电磁环境恶化的关键因素。扩频技术改变传导和辐射干扰功率谱的形状，降低峰值辐射水平，从而符合国际 EMC 规定的要求。选用经过优化的调制频率可实现一种系统级解决方案，其封装和体积更小，同时降低固有成本并提升功率密度。