# 静噪基础教程 第1部分 第1章 需要EMI静噪滤波器(EMIFIL)的原因

### 1-1. 简介

EMI静噪滤波器 (EMIFIL) 是为电子设备提供电磁噪声抑制的电子元件，配合屏蔽罩和其他保护装置一起使用。这种滤波器仅从通过连线传导的电流中提取并移除引起电磁噪声的元件。第1章说明了电子设备中使用EMI静噪滤波器(EMIFIL)的原因，还概述了通常电磁噪声抑制所用的典型屏蔽和滤波器的操作。

![Fig. 1-1 EMI suppression filters (EMIFIL)](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0001.ashx?la=zh-CN&h=197&w=640&cvid=20150203102349570600)

图1-1 EMI静噪滤波器 (EMIFIL)

------



### 1-2. 什么是电磁噪声干扰？

电子设备收到强电磁波时，电路中会感应到不想要的电流，这会产生非预想的操作或对预想的操作形成干扰。如果外部施加的能量过于强大，电子设备可能会损坏。即使外部施加的能量较小，如果混入广播和通信所使用的电波中，在广播和通信的无线电波信号较弱的区域内，也可能会造成无法接收、声音中出现异常噪声或视频被破坏。外部电磁波造成的这些干扰称为电磁噪声干扰，而造成干扰的电磁波称为电磁噪声（下文称为噪声）。



![Fig. 1-2 Emission and immunity](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0002.ashx?la=zh-CN&h=722&w=640&cvid=20150203102355358200)

图1-2 发射和抗扰



噪声会干扰到各种电子设备。噪声源也各有不同。对有些设备（例如洗衣机和冰箱）完全不起作用的噪声，却可能会严重干扰其他设备（例如AM收音机）。因此，需要一定的规则把电子设备产生的噪声抑制到某个水平，并确保这些电子设备在某个噪声水平下正确运行，这样我们才能安全地使用这些电子设备。这些规则称为噪声规定。
如果一台电子设备视为噪声源，则噪声的产生称为发射（噪声发射）。相应地，如果一台电子设备视为噪声受体，则噪声容忍度称为抗扰度（噪声容忍度）。噪声规定指定了电子设备的发射和抗扰度。（抗扰度也称为EMS: 电磁敏感度）



![Fig. 1-3 Examples of European noise regulations](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0003.ashx?la=zh-CN&h=293&w=640&cvid=20150203102401754200)

图1-3 欧洲噪声规定示例

#### 1-2-1. 电磁噪声分类

如图所示，根据电磁噪声的来源，可分为自然噪声和人为噪声。 自然噪声是电子设备出现之前就存在的噪声，例如闪电和静电。电子设备要求对自然噪声有抗扰性。
人为噪声是电子设备开始使用后出现的噪声，要用发射和抗扰度进行处理。随着电子设备越来越广泛的使用，人为噪声引起的干扰逐渐增加。这一点将在后续章节中详细讲述。



![Fig. 1-4 Classification of noise](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0004.ashx?la=zh-CN&h=304&w=640&cvid=20150203102407822600)

图1-4 噪声的分类

#### 1-2-2. 噪声问题因电子设备密集而出现变化

我们周围使用的电子设备过于密集，噪声干扰的内容和程度在随着每个电子设备的性能增加而变化。例如，1970年之前（数字电路还未流行之前），我们考虑的是无线电波之间的干扰问题（无线电干扰）。但随着个人计算机等家用数字电子设备的流行，我们开始关注这些电子设备产生的无线电波对收音机和电视接收无线电波的干扰。
通常，随着电子设备的密集度增加，噪声源和噪声受体之间的距离在缩短，而噪声干扰的程度在上升。此外，随着电子设备的性能提升，工作电路频率增加，会产生更高频率的噪声，扩大了受影响的频率范围。而且，由于电子设备的省电功能，更多的电路可以按更低的电压运行，这样低能量噪声影响的情形在增多。
今后随着电子设备进一步的高密集化、高性能化及小型化，预期噪声干扰问题会更加严重。

![Fig. 1-5 Expanding use of electronic devices and effects on noise issues](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0005.ashx?la=zh-CN&h=368&w=640&cvid=20150203102413766200)

图1-5 扩大使用电子设备和对噪声问题的影响

#### 1-2-3. “系统内EMC”, 电子设备自体中毒

没有任何外部噪声，电子设备本身就可能出现噪声干扰。电子设备内部电路中产生的噪声可能会干扰电子设备本身内部的其他电路。这称为系统内EMC。例如，如果手机设有内置数字电路，数字电路的噪声会令手机的接收器性能下降（降低接收器灵敏度），如下图所示。这种情况下，噪声源和噪声受体之间的距离明显小于常规噪声源之间的距离，会产生更严重的干扰。视具体情形而定，提供的噪声抑制水平要远比噪声规定的限制更加严格。

![Fig. 1-6 Example of intra-system EMC](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0006.ashx?la=zh-CN&h=317&w=640&cvid=20150203102419507000)

图1-6 系统内EMC示例

------



### 1-3. 噪声抑制

三种因素（噪声源、噪声受体和传输路径）如图1-7的原理图所示存在时，会产生噪声干扰。如果可以消除其中一个因素，就可以消除噪声干扰。
因此，可以在噪声源侧或噪声受体侧采取措施。例如，如果未使用数字电路、开关电源或发射器（例如白炽灯），电子设备产生的噪声会非常小。另一个例子是在噪声受体一侧于软件中设置冗余处理。
因此，即使信息稍有改变，也可以恢复信号。这些措施可以作为基本解决方案。但许多这些情形会造成较大的次级效应，比如明显降低电子设备的性能或增加其尺寸，从而使这些措施不切实际。



![Fig. 1-7 Principle of noise interference](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0007.ashx?la=zh-CN&h=356&w=640&cvid=20150203102425060600)

图1-7 噪声干扰的原理





通常，噪声会如图1-8所示排除在传输路径之外。存在两种噪声传导（空间传导和导体传导）。如图所示，空间传导由屏蔽进行处理，而导体传导由滤波器进行处理。
如图1-7所示，空间传导和导体传导倾向于通过用作天线的导线进行相互转化。因此，即使导体传导只是一个位置的问题，但不能完全忽略空间传导的可能性。



![Fig. 1-8 Measures for noise suppression](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0008.ashx?la=zh-CN&h=356&w=640&cvid=20150203102431285000)

图1-8 噪声抑制的措施

#### 1-3-1. 屏蔽

屏蔽指的是通过用如图1-9所示的金属板或其他保护装置封闭目标物体，把周围的电磁场排除在外。
尽管屏蔽的效果通常取决于所用材料的传导性、导磁率和厚度，但用铝箔等极薄的金属板会令常规电子设备的噪声抑制更有效果。您必须意识到电子设备的噪声抑制效果会因形成外壳的连接方法（间隙、接触阻抗等）而异，而与材料规格无关。
在散热所用的屏蔽罩上制作开口时，限制每个开口的超大尺寸比限制开口的总面积更加重要。如图1-10所示，如果存在细长的开口或狭缝，这个部分可以起到狭缝天线的作用（特别是图中的长度l 超过了波长1/2时的高频范围），且无线电波可以进出屏蔽罩。为了避免这样，应保持每个开口较小。由此看来，带许多小孔的板材（例如冲孔的金属和延展的金属）是很好的材料，既有利于通风，又有利于屏蔽。



![Fig. 1-9 Shield](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0009.ashx?la=zh-CN&h=314&w=640&cvid=20150203102437088200)

图1-9 屏蔽

![Fig. 1-10 Examples of different shielding effects by three different opening shapes with the same area](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0010.ashx?la=zh-CN&h=410&w=640&cvid=20150203102442844600)

图1-10 相同区域内三个不同开口形状产生不同屏蔽效果示例
（假设高频噪声受电磁屏蔽限制。
某些情况下（例如电磁屏蔽等），这个顺序可能不适用。）

#### 1-3-2. 滤波器

滤波器指的是一个元件或功能，在导体中流动的电流内，可以让必需的成分通过，而消除不想要的成分。尽管噪声分流到了图1-12所示的接地，但噪声能量会被这些元件内部吸收，或返回到噪声源（增加阻抗）。



![Fig. 1-11 Filter](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0011.ashx?la=zh-CN&h=250&w=640&cvid=20150203102448148600)

图1-11滤波器



![Fig. 1-12 How a filter works](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0012.ashx?la=zh-CN&h=202&w=640&cvid=20150203102453998600)

图1-12 滤波器工作方式

因为噪声往往分布在如图1-13所示的相对较高的频率范围内，所以电子设备的噪声抑制通常使用低通滤波器来消除高频成分。可以把电感器（线圈）、电阻和电容等通用元件用作低通滤波器。但是为了完全隔离噪声，可以使用EMI静噪滤波器等专用的元件。EMI静噪滤波器会在本文档的第6章进行详细说明。
除了这些利用噪声不均匀频率分布的滤波器以外，还有些滤波器是利用压差（变阻器等）或利用传导模式差异（共模扼流线圈等）。
除了这些滤波器，变压器、光缆或光隔离器均可用作一种滤波器。尽管某些情况下这些元件可以获得优异的降噪效果，但适用的情形很有限。



![Fig. 1-13 Separation of noise by low-pass filters](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0013.ashx?la=zh-CN&h=248&w=640&cvid=20150203102459708200)

图1-13 用低通滤波器隔离噪声

------

### 1-4. 如何使用屏蔽和滤波器

#### 1-4-1. 在某一点使用屏蔽和滤波器

滤波器用于通过导体传导的噪声，而屏蔽用于通过空间传导的噪声。但是，因为传导噪声的导体也会用作天线，所以这两类传导也会通过作为天线导体而互相转换。因此，为了完全隔离噪声，需要在一个位置同时使用滤波器和屏蔽。
例如，当屏蔽用于隔离空间传导时，如果如图1-14所示存在一个导体穿过屏蔽，这个导体会拾取屏蔽内的噪声并吸到屏蔽之外，造成噪声发射。因此，使用屏蔽不能完全隔离空间传导。
同样，当滤波器用于隔离导体传导时，通过如图1-15所示的空间传导，在滤波器前后的导线彼此耦合。因此，只用滤波器也无法完全隔离导体传导。



![Fig. 1-14 Conductor conduction causes loophole in a shield](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0014.ashx?la=zh-CN&h=288&w=640&cvid=20150203102505495800)

图1-14 导体传导会在屏蔽罩上造成漏洞



![Fig. 1-15 Filter is bypassed by spatial conduction](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0015.ashx?la=zh-CN&h=262&w=640&cvid=20150203102511361400)

图1-15 空间传导会绕过滤波器



如图1-16所示在一个位置同时使用屏蔽罩和滤波器时，隔离空间传导和导体传导两者将完全消除噪声。
如果噪声源和滤波器之间的导体长度如图1-17所示明显较短，导体作为天线的影响可以忽略，且只用滤波器就可以一定程度消除噪声。因此，如果可以在靠近噪声源的位置使用滤波器，只用滤波器就能实现噪声抑制。

![Fig. 1-16 Noise can be shut out by the combination of a filter and shield](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0016.ashx?la=zh-CN&h=284&w=640&cvid=20150203102516837000)

图1-16 通过滤波器和屏蔽组合可以隔离噪声



![Fig. 1-17 If conductor is short, noise suppression can be achieved only with a filter](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0017.ashx?la=zh-CN&h=221&w=640&cvid=20150203102522796200)

图1-17 如果导体短，只用滤波器就能实现噪声抑制

#### 1-4-2. 滤波器和接地

为了有效使用滤波器和屏蔽，通常需要良好接地。
如果滤波器内存在内置的旁路电容，接地会成为噪声电流返回噪声源的通道，如图1-18所示。您需要考虑保持此元件具有很低的阻抗。
如果对地阻抗如图1-19(a)所示一样大，由于噪声电流，接地会产生电压，因此无法彻底消除噪声。如果这个接地与连接到另一个滤波器的另一条导线共享，接地处产生的电压会通过滤波器电容转回其他线路。
通过接地阻抗耦合的这个噪声类型称为公共阻抗耦合。接地处具有噪声的这个状态也称为共模噪声发生。共模噪声会在后续章节中说明。公共阻抗耦合是造成共模噪声的机制之一。
因为具有内置电容的滤波器效果容易受到相连接地状况的影响，所以需要使用具有低阻抗的稳定接地。



![Fig. 1-18 Current pathway of noise](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0018.ashx?la=zh-CN&h=236&w=640&cvid=20150203102528365400)

图1-18 噪声的电流路径



![Effect of impedance in ground](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0019.ashx?la=zh-CN&h=808&w=640&cvid=20150203102534371400)

图1-19 接地中阻抗的影响

#### 1-4-3. 屏蔽和接地

屏蔽也需要接地。
静态屏蔽必须连接到接地，原则上是外部接地（零电压）。由于被屏蔽电场中的变化而使连接到接地的导线中有电流，所以导线必须低阻抗。
许多情况下，使用屏蔽的电缆时，屏蔽层也会成为已流过内部导体电流的回路（例如同轴电缆的外部导体）。因此，需要连接到可以返回此电流的接地处（屏蔽信号时，连接到电路接地）。
类似图1-19的情形，噪声已经引导到大地时，如果屏蔽连接到接地，屏蔽延长，然后就像天线一样从接地发出噪声，可能会增加噪声。连接屏蔽时，需要选择电压稳定、阻抗低的接地。
外壳屏蔽罩实际上是相对良好的接地。如果有一个屏蔽罩盖住了整个电子设备，则这个屏蔽罩本身就可能是噪声抑制的良好接地，即使未与大地相连（如果放电电流因需要抑制静电或其他电流而排放到大地，则需要接地）。因此，我们称这个接地为外壳屏蔽接地。
这个外壳屏蔽接地也可以用作屏蔽电缆的接地。但是，为了把这个屏蔽罩用作上述信号的回路，需要用电路接地进行连接。因此，如果外壳屏蔽接地和电路接地已经隔离，则连接会变复杂。

图1-20显示了屏蔽电缆接地连接的示例。



![Fig. 1-20 shows an example of ground connection for shielded cables.](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0020.ashx?la=zh-CN&h=446&w=640&cvid=20150203102540174600)

图1-20 屏蔽电缆接地连接示例

#### 1-4-4. 接地加强

如上所述，有必要连接到稳定的接地，增强滤波器和屏蔽罩的效果。此外，当使用盖住了整个设备的屏蔽罩时，这个屏蔽罩本身可以用作稳定的接地。因此，屏蔽通常具有稳定接地的功能。
如果有导线穿过这个屏蔽罩，如图1-14所示提供了一个孔允许噪声进出屏蔽罩，会使屏蔽罩接地不稳定。这种情况下，可以在这根导线中使用滤波器阻止噪声进出，因此可以稳定屏蔽罩接地。
如上所述，合适的屏蔽罩和滤波器可以作为稳定的接地，因此屏蔽罩、滤波器和接地之间有互相协助的关系。
除上述屏蔽罩接地之外，电路接地也是接地类型，且经常会感应出比屏蔽罩接地更多的噪声电压。这种接地称为“稳定接地”。与此相反，未感应到噪声的接地称为“不稳定接地 ”。
较为理想的是连接屏蔽罩或滤波器的模块接地。但是，需要电路接地连线来返回信号回流，或把噪声电流返回到噪声源点。如果电路接地不稳定，应通过减少电路接地的阻抗，提供沿着电路板的接地层，或连接外壳屏蔽接地，尽量降低噪声电压。
通过以这种方式降低电压来稳定接地噪声的操作称为“接地加强”。用屏蔽罩盖住一部分电路板有助于接地加强。图1-21显示了接地加强的一些方法。



![Fig. 1-21 Example of ground reinforcement](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0021.ashx?la=zh-CN&h=590&w=640&cvid=20150203102545821800)

图1-21 接地加强示例

#### 1-4-5. 滤波器和接地

把电缆连接到屏蔽罩时，连接滤波器可防止噪声通过电缆进出。这个滤波器的接地会在电路板上形成。但是，为了稳定接地，经常被连接到屏蔽罩接地，而不是电路接地。因此，在连接电缆的区段处经常会形成与屏蔽罩接地连接的滤波器接地。此处，我们称这个接地为“滤波器接地”。
通常，滤波器接地不仅连接到屏蔽罩接地，而且连接到电路接地，以便把电路内生成的噪声返回到噪声源。这种情况下，同时还起到了电路接地的接地加强作用。使用屏蔽的电缆时，屏蔽层可以连接到滤波器接地。这种情况下，必须以极低的阻抗将其连接到屏蔽罩接地，因为屏蔽电缆的效果会因滤波器接地的质量而异。

图1-22 显示了滤波器接地的示例。关于屏蔽罩接地，最重要的是以极低的阻抗保持滤波器接地。

尽管第1-4-2节已经阐述了滤波器的接地要以低阻抗连接到噪声源（关于电路接地），图1-22显示了优先连接到屏蔽罩接地。这是因为实际上很难以低阻抗返回噪声源，因为电缆的连接点通常远离噪声源。此外，其他电路的噪声因电路接地不稳定的情况较多，即使连接低阻抗滤波器接地，也很难提升效果。
因此，当在接近噪声源的位置处为单个电路使用滤波器时，如1-4-2节所述把滤波器连接到电路接地。但是，当噪声源很远（例如在接线盒处）且需要考虑两个以上噪声源时，要实现此连接会很困难。一个实用的技巧是在接线盒处使用滤波器，如图1-22所示可以找到屏蔽罩接地等稳定的接地，并连接滤波器接地。



![Fig. 1-22 Example of connection using a filter ground](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0022.ashx?la=zh-CN&h=612&w=640&cvid=20150203102551718600)

图1-22 使用滤波器接地的连接示例

------

### ![Key points](https://www.murata.com/-/media/webrenewal/products/emc/emifil/knowhow/basic/chapter01-p1/chapter01-p1_img0024.ashx?la=zh-CN&h=27&w=33&cvid=20150203102603761800) 第1章的重点内容

- 干扰电子设备运行的电磁波称为噪声。
- 隔离噪声传输路径的方式包括屏蔽和滤波器。
- 为了使屏蔽和滤波器有效工作，接地很重要。