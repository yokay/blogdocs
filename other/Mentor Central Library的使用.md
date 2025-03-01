# Mentor Xepdition的使用技巧

# 1. Supply rename

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image001.png)

Signal区域标注隐藏管脚的管脚号。使用时需要用Supply rename重定义。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image002.png)

两者都使用**空格**分开不同的管脚。

# 2. Part number



库中使用IPN作为物料编码，Part number为软件内部使用，需要匹配Parts名称才能调出带封装的symbol。PKG_TYPE仅用于标识封装名称，用于BOM。即Part number内容为Parts中的元器件名称。

# 3. 运放的调用

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image003.png)

对于这种集成多个运放的symbol不是合体后的，而是分开为独立的多个symbol。调用时要注意，需从以下调用。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image004.png)

# 4. 封装说明

- QFN16-3R0X3R0X0R8-0R5

| QNF16            | 3R0X3R0X0R8           | 0R5          |
| ---------------- | --------------------- | ------------ |
| QFN封装16个pin脚 | 长宽高：3.0X3.0X0.8mm | Pitch：0.5mm |

- BGA25-2R5X2R5X0R5-0R4

| BGA25            | 2R5X2R5X0R5           | 0R4          |
| ---------------- | --------------------- | ------------ |
| BGA封装25个pin脚 | 长宽高：2.5X2.5X0.5mm | Pitch：0.4mm |

- SOT23-3R0X2R5X1R1-L

| SOT23       | 3R0X2R5X1R1           | L                            |
| ----------- | --------------------- | ---------------------------- |
| 封装为SOT23 | 长宽高：3.0X2.5X1.1mm | 焊盘不一样，设置的多封装标记 |

# 5. 封装库导入

使用Library Loader软件导入封装库。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image005.png)

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image006.png)

搜索需要的器件名称。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image007.png)

  ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image008.png)

下载库文件。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image009.png)

打开下载的模型库。

首先导入焊盘padstacks。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image010.png)

 

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image011.png)

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image012.png)

然后导入封装cell。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image013.png)

最后导入器件Part

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image014.png)

最后导入symbol

   ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image015.png)

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image016.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image017.png)



在parts里面调整下symbol，先删除掉现有的symbol和pin对应关系，重新选择。

# 6. 封装边框说明

组装边框：实物长宽

布局边框：PCB布局时边框，≥布局边框，提供安全间距，布局时能自动防止距离太近导致的贴片不良。

丝印边框：PCB丝印边框，印在PCB上。≥布局边框，一般大于布局边框相同，因为本体会覆盖住丝印。

# 7. Part number等说明

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image018.png)

Part number、Part name、Part label如上表所示，分别为编号、名称和标签。故数据库中的Part number一定要与中心库中的编号一致，否则调用补了Part。

# 8. 封装丝印大小

高：0.635mm，宽：0mm。与gerber字体一致。HDI高密度丝印绘制参考设置。

高：1mm，宽：0mm。Arial字体。JLC丝印绘制参考设置

# 9. 封装丝印设置可调

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image019.png)

勾选以上两个后丝印大小和位置就可以变动了。

 

# 10.    封装大小

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image020.jpg)

# 11.    开槽设置

首先建立1个NPTH或者PTH，直径设置为0.01mm。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image021.png)

在PCB中画一个槽或者任意多边形，属性设置为Contour，Hole选择刚才建立的0.01mm直径的孔。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image022.png)

Geber导出时设置下DrillDrawingThrough，选择Countours和Drill Drawing Thru

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image023.png)

Geber中Npth层可以看到开槽。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image024.png)

# 12.    铺铜设置

在“平面分配”中“平面数据状态”表示，平面是否是动态变化还是固定不动。一般设置为动态，这样走线时铺铜形状会适时变化。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image025.png)

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image026.png)

在里面选择要铺铜的网络。

   ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image027.png)

<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image028.png"  />

阴影区为GND静态层，不会变化。改为动态后就变化了。

Note:一旦设定为铺铜层则飞线消失，因为软件认为是通过铺铜连接的。

# 13.    刚柔板叠层设置

   ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image029.png)

 

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image030.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image031.png)

Copper：铜皮。

Prepreg：Prepreg是PCB的薄片绝缘材料。Prepreg在被层压前未[半固化片](https://www.baidu.com/s?wd=半固化片&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)，又称为预浸材料，主要用于多层印制板的内层导电图形的粘合材料及绝缘材料。

Adhesive：接着剂或粘合剂，

Polyimide：聚酰亚胺（PI）。可以作为基底（substrate），黄色。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image032.png)

在上图中可以指定柔性部分，且内制定叠层。

# 14.    CES设置

**单位注意以英制为准！**

布线边界：12mil~20mil

最小线宽：4mil

最小线距：8mil（铜皮边间距4mil）

Hatch铺铜：线宽4mil，线距6mil

通孔：16mil外径，6mil内径（直径）

盲埋孔：9mil外径，4mil内径（直径）

盲埋孔孔间距： 9mil+4mil=13mil

通孔孔间距：16mil+4mil=20mil

导线到平面：4mil（导线中心到平面边为6mil）

导线到焊盘：6mil（导线中心到焊盘边8mil）

导线到盲埋孔：2mil+4mil+4.5mil=10.5mil

导线到过孔：2mil+4mil+8mil=14mil

过孔到平面：6mil

平面到平面：8mil

平面到焊盘：6mil

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image033.png)

10mil宽度，6mil间隙。

封装与封装的间距：6 th或4 th

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image034.png)

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image035.png)

- 设置网络类的安全间距

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image036.png)

首先新建网络类，并分配网络。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image037.png)

然后新建安全间距规则。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image038.png)

然后在设置类与类的安全间距规则

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image039.png)

最后选择网络类与其他类使用的安全间距规则。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image040.png)

# 15.    封装高度设置

修改封装属性，定义高度。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image041.png)

# 16.    原理图封装属性更新

通过PCB中反向标注，可以将PCB的封装属性更新到原理图中。

# 17.    原理图non-common property修复

   ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image042.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image043.png)

# 18.    铜皮厚度

制板厂对铜箔厚度的处理是表层1OZ（1.4mil）,内层0.5OZ（0.7mil）

# 19.    网格铜设置

厚度为：铜厚度。间距为铜中心间距。

# 20.    器件类型

Annotate are used for symbols such as on/off-sheet connectors and sheet borders, they are used to provide documentation information (cross-references, drawing info etc). They do not get packaged for layout or compiled for simulation. Pin types are used for hierarchical ports and global signals. The hierarchical ports link the lower level schematic to the I/O definition of a hierarchical block symbol, hierarchical blocks are Composite type components, that is they are made up of underlying schematics, generally they're simple hierarchical blocks with connections that traverse from the pa rent sheet to the child schematic. They are used to drive connectivity and do not have a Part or cell in layout. Module type components are symbols that get mapped to parts and are passed to layout. They are 'PCB' symbols and may have associated simulation models for SPICE or HDL.

# 21.    PCB层说明

Solder Mask：阻焊层。该区域（洞）以外的地方，都不允许有焊锡，即只能涂绿油。说白了就是绿油镂空区域。

Solder paste：钢网层。即涂焊锡的区域，露铜的区域。

# 22.    PCB生产文件

- 丝印生成

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image044.png)

 

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image045.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image046.png)

现在建议不生成元件外框丝印图，容易贴片时丝印顶到。

新建用户自定义层TOPSILK和BOTSILK，用于生成丝印。比如文字或者图形放在相应层。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image047.png)

- NC Drill

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image048.png)

- DXF导出

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image049.png)

 

- 坐标文件

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image050.png)

- Geber

2层：

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image051.png)

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image052.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image053.png)



 

# 23.    3D文件

添加3D视图。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image054.png)

点选器件，然后导入STEP 3D模型。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image055.png)

选择所需模型。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image056.png)

根据实际情况，调整模型位置、方向。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image057.png)

导出板卡的STEP 模型

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image058.png)

根据情况选择导出的东西。

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image059.png)

3D Step可用于结构堆叠。

# 24.    支持远程

将LICENSE.DAT中的SIGN2替换成TS_OK_SIGN2。

# 25.    Symbol显示位号

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image060.png)  

Symbols的显示属性改为位号，还可以将提示信息加上器件描述或者值，即Description和Value。

# 26.    默认新建Symbol属性信息

 

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image061.png)

 

# 27.    默认设置

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image062.png)

 

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image063.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image064.png)

# 28.    JLC和华强PCB通用设置

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image065.png)

多层板孔：VIA16C0X8C0th（默认VIA18C0X12C0th）

双层板孔：VIA20C0X12C0th（默认VIA18C0X12C0th）

线宽最小：3.5mil（默认设置为4mil）

线距：3.5mil（默认设置为4mil）

线距焊盘：5mil

 

# 29.    原理图网络走线颜色设置

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image066.png)

勾选Color by Net

 ![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/image067.png)

点击走线，弹出箭头后选择颜色，之后所有该网络走线颜色就会改变。

# 30.多symbol器件建立

首先建立多个子symbol，跟新建symbol一样，只是不同的symbol代表一部分管脚。

然后再Part里面进行关联，将多个symbol都加入进去。

比如这里建立了2个CC2340的子symbol。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/cc2340-1.png)

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/cc2340-2.png)

添加就去后，就是多个symbol。

建立symbol最好将Part Number设置为相同值。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/cc2340-3.png)

最终出来的效果如下图所示。

![](https://mythidea.oss-cn-beijing.aliyuncs.com/Library/cc2340-4.png)





# reference

[^1]: [Central Library](https://gitee.com/letsgomass/CentralLib)

