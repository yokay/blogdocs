这里主要针对增强型MOS管进行讲解。其结构如下所示。  
<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210906220106784.png" alt="image-20210906220106784" style="zoom:50%;" />
上图为一个NMOSFET，G、S、D为3个金属电极，其中S、D的电极接到N+切被P-包围，G极与其他两极绝缘，N+为衬底（高掺浓度），N-为外延层（地掺浓度)。 判断是否为NMOS管主要看衬底是否为N型。   

N沟道MOSFET衬底为高掺杂的N+衬底，高掺杂沟道部分的体电阻小。然后上面为为N-的epi层，上面有两个连续的扩散区P-，沟道在P-区形成。在P-区内部，扩散形成的N+为源极。硅片表面形成栅极氧化物，多晶硅栅极材料沉积后，在连接到栅极的多晶硅层下面，就会形成一个薄的高质量的氧化层，从而产生沟道。  

栅极和源极间加正向电压，P-区中的少数载流子，即“少子”，也就是电子，被电场吸引到栅极下面的表面，随着栅极和源极正向偏置电压的增加，更多的电子被吸引到这个区域，这样本地的电子密度要大于空穴，从而出现“反转”，即在栅极下面的P-区的材料从P型变成N型，形成N型“沟道”，电流可以直接通过漏极的N+型区、N-型区、栅极下面N型沟道，流到源极N+型区。 

简化的NMOS管驱动结构如图所示。千万不要被这个"P区“干扰误认为是PMOS    

在GS上加上正向电压后，P-慢慢形成反型层（N型）即导电通道。如下图所示。  

![](https://ts1.cn.mm.bing.net/th/id/R-C.0eb12cac93a52d0ef41b38b4bbcb8df2?rik=J%2bGmWbTC51a6pw&riu=http%3a%2f%2fwww.jingyeic.com%2fuserfiles%2f202069144146738.jpg&ehk=1MdF48GAj5uG4qbQMQsOEYLCK3a1alr%2f1crhQsO382g%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1)

形成导电沟道后，D、S之间可以有电流通过，此时的Vgs为Vth，即形成导电沟道的阈值电压。  

当Vgs>Vth，Vds>0时，DS之间产生电场，由于导通沟道有电阻，S->D方向的电阻增大，假设为Vc(x)，x为S->D方向长度，x处到S的电压为Vgs-Vox-Vc(x)，则靠近S处电压较高，D处较低，导致S处电子比D处多，形成楔形沟道。当Vds较小时，沟道主要受Vgs控制，当Vgs不变时，沟道电阻不变，id与Vds成线性关系，这就是电阻区（线性区）。

当Vds增大时，Ids增大，反型层上的电压由x→L线性增大，当Vgs-Vox(L)-Vcx(L)=Vth时，D处的反型层最薄，出现预夹断。此时Vds=Vgs-Vth=Vox(L)+Vcx(L)，之后Ids几乎不变。  
下图中Vdd的正极即是D，负极是S，Vgs的正极是G。  
![](https://tse1-mm.cn.bing.net/th/id/R-C.4ab4ab7ab1f21879e714b295d24f4e3a?rik=fPVSa%2f208bGSzw&riu=http%3a%2f%2fwww.szyxwkj.com%2fUploadFiles%2fFCK%2f2019-12%2f6371287900176685666471599.jpg&ehk=1I%2bRIn%2ffFqpfXcaoxw9NtCaPDzcwzD506Ru5wzS3jfk%3d&risl=&pid=ImgRaw&r=0)

总结如下：  

+ 夹断区：Vgs < Vth  
+ 电阻区：Vds < Vgs-Vth  & Vgs > Vth
+ 恒流区：Vgs > Vth & Vds > Vgs-Vth    

==GS导通→DS导通==