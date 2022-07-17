# TracePro在可穿戴设备的应用案例

## 一．可穿戴设备应用的背景 [^1][^2]

如今，人们对追踪健康和健身的“可穿戴设备”的兴趣日益浓厚，脉搏血氧仪因此走出了医院，进入了普通消费者市场。如上肢类可穿戴设备，主要有智能手环、智能手表等。除了传统的时间显示和闹钟提醒功能，这些设备还通过各类传感器实时检查使用者的心率、脉搏、步速、血氧等，从而获得用户运动或睡眠时的身体数据。例如现在市场上的小米手环、苹果 iWatch、三星 GalaxyWatch、华为 Watch。



![华为手表.jpg](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABACGAAg9-Od8wUo_s_B3QUw3wM4mAM.jpg)   ![苹果手表.jpg](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABACGAAg-POd8wUooLfP5wcw3wM4mAM.jpg)

图（1）华为手表             图（2）苹果手表





  对于可穿戴设备，在光学方面我们要测量脉搏血氧饱和度可以利用氧合血红蛋白与还原血红蛋白有不同的吸收光谱这个特点，前者对可见红光（660nm）吸收较多，而后者对红外线（940nm）吸收较多，即SpO2的值在不同的氧合状况下值不同，然后，将SpO2比值与基于健康受试者校准曲线的查表进行比较。

<table>
    <tr>
        <td>SpO2</td>
        <td>状况</td>
    </tr>
    <tr>
        <td>90%-95%</td>
        <td>氧合良好</td>
    </tr>
    <tr>
        <td>≤90%</td>
        <td>低氧血症</td>
    </tr>
    <tr>
        <td>≤85%</td>
        <td>严重低氧血症</td>
    </tr>
</table>

表（3）SpO2的值和表明的状况

人体血液呈现红色，主要是因为对绿色吸收比较强。由于血管周期性起搏，使得血管到光电传感器的距离发生周期性变化，只要传感器不停的发射绿光，接收端会收到一组周期性的吸收峰，对信号进行一定的处理就可以得到心率曲线。所以绿光LED对于心率的测量必不可少。

## 二．利用[TracePro](https://www.fulllightcn.cn/product-item-12.html)进行仿真及结果分析

而在设计方面，现在就有两种设计方式，一种是反射式，一种是透射式，对于这两种方法的仿真后的分析下文将做解释。

（一）反射法仿真

对于可穿戴设备，需要具备红光LED，红外LED，绿光LED和光电二极管如图的器件来进行测量：

![仿真.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAgxfWd8wUoz7Pj5AQwyAc46QM.png)

图（4）仿真前需要的器件

进行TracePro中的仿真建模如下图（5）：

![三个发光.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg0PWd8wUo6v-SsAEw-QY4qgM.png)

图（5）三个发光二极管的TracePro通用生物传感器模型

*用940nm（作为红外光波长）、655nm（作为红光波长）和530nm（作为绿光波长），同时也有一块挡板尺寸为5mm*2.5mm*1mm用来防止光串扰。

设定好各种参数后，先可以设定一个光源来测试，进行光线的追踪，如下图：

![红光.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg0PWd8wUolsnrrwUwkAU4qwM.png)

图（6）红光LED的TracePro仿真

TracePro仿真出红光LED的发射，进行人体皮肤组织后杂散光又被光电二极管接收到，同时，中间的挡板也很好的阻挡了从光源直接发出被二极管检测到的光线，这样子我们就可以利用这些得到的光线的条数等参数来估计出人体的血氧含量。我们可以通过多次改变如挡板的几何参数来比较不同的几何参数的减少光串扰效果，TracePro中还可以自动进行优化来找到最佳的参数。

通过分别点亮三个一开始设置的光源，通过TracePro可以分析进入到皮肤组织接收到的光线的辐照度图（7）：

![皮肤.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg0-Wd8wUo0MOGxwUw3gc45gI.png)

图（7）皮肤组织接收到的光线的辐照度

最左边是绿色，中间是红色，右边是IR（红外）。绿色LED的总辐射通量为0.015W，如图所示，中间的红色为0.0153W，最右边的IR为0.016W。从上图可以仿真分析得到：当波长从可见光增加到红外波段时，光在组织中传输得更好。

另外一方面，还可以考虑到太阳光等外部光源，皮肤表面出汗，设备老化等对设备测量的影响，也可以通过TracePro进行仿真：

![太阳光.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg0PWd8wUogPmRkAUwwwc4jQM.png)

图（8）太阳光影响的仿真

![外部光源.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg1fWd8wUo5vSKdzCJBDjHAw.png)

图（9）外部光源进入组织的光线的辐照度图

可以分析出：这种杂散光的贡献与绿色、红色和红外LED的贡献是相同的量级，这个信号是很大的干扰源，导致脉搏血氧饱和度报告是完全无效的，而此时，就可以利用TracePro来修改挡板的几何参数或者通过其它辅助结构让穿戴设备与手指更加贴近等来减少外来光源对结果造成的影响。

（二）透射法仿真

通过红外LED和红光LED透过手指进行的仿真图（10）如下：

![透射法.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg1fWd8wUo3Jayvgcw2gc46AM.png)

图（10）透射法通过指甲测量的TracePro仿真

透射法则需要被探测的光线与发射光源处于垂直方向，使光通过皮肤组织到达手指甲，光线在手指当中的光线轨迹也可以很清晰的看出。我们还可以通过另外的一个方向来观察光线，从末端观察到达手指的射线的轨迹，如图（11）

![手指.png](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedABUIABAEGAAg0PWd8wUogODwkwcwkgM43QI.png)

图（11）手指末端观察光线轨迹

我们可以很容易地看到射线的路径。这可能看起来不像，但实际上是件好事，因为手指上的骨头挡住了光线。这条射线轨迹表明，由于组织中的大量散射，光可以绕过骨骼到达光电二极管。

## 三．TracePro的优点以及可实现的功能

从以上的光学仿真中，我们可以看出TracePro具有以下优点：

1）能够很精确的仿真光线的轨迹和其它参数如辐照度等的测量。

2）该软件具有很简便的程序，对于初学者可以很快上手。

3）TracePro软件的界面各个窗口都很人性化，能够利用最短的时间学习来收获满满的效果；

4）TracePro在照明设计中能够为照明设计者带来很好的投资回报，用少量的金钱就能够很快的学习到一门技术。



[TracePro](https://www.fulllightcn.cn/product-item-12.html)的分析功能为设计师提供了创造更好产品的工具，TracePro可以很好的实现如下常用功能分析：

1）可以用通量的报告分析出任何表面的吸收和辐射量，来验证设计的合理性；

2）使用三维辐照度/照度图来显示功率流或通过光学部分或光波导；

3）使用可视化的光线追踪来查看光线在与部件交互时的逃逸、反射、传输或散射情况，以验证路径；

4）使用高级路径排序来分析和最小化光波导中的串扰路径



## Reference

[^1]:https://www.fulllightcn.cn/article-item-66.html
[^2]:[New_Wearable_Designs_with_Pulse_Oximetry_Dont](https://www.photonics.com/Articles/New_Wearable_Designs_with_Pulse_Oximetry_Dont/a58289)
[^3]:https://www.lambdares.com/biomedical-applications-using-tracepro/
[^4]:https://www.lambdares.com/support/virtual-simulation-pulse-oximetry-wearables/
[^5]:https://www.lambdares.com/support/accurately-predict-pulse-oximetry-device-performance/
[^6]:https://www.lambdares.com/wp-content/uploads/support/LambdaVids/TracePro/LFW%20Pulse%20Oximetry%20Webinar-sw8q8lbrQNw.mp4

