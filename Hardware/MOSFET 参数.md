# MOSFET参数

## 静态参数
### Idss  

==D→S漏电流==  

饱和漏源电流，栅极电压VGS=0时VDS为一定值并产生预夹断时的漏源电流。一般在uA级。   

### Vth
==GS开启电压==  

Vgs>Vth时导通沟道形成

### Rds  
在特定的 VGS （一般为10V）、结温及漏极电流的条件下，==MOSFET导通时漏源间的最大阻抗==。它是一个非常重要的参数，决定了 MOSFET导通时的消耗功率。此参数一般会随结温度的上升而有所增大。故应以此参数在最高工作结温条件下的值作为损耗及压降计算。  
### V(br)ds   
漏源击穿电压。是指栅源电压 VGS为0时，场效应管正常工作所能承受的最大漏源电压，Vds超过此值会使管子损坏。  

### Id
==最大漏源电流==  

场效应管正常工作时，漏源间所允许通过的最大电流。  

### gfs  
==低频跨导==  

是指漏极输出电流的变化量与栅源电压变化量之比，是栅源电压对漏极电流控制能力大小的量度。其曲线如下图所示。  
<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210906223042678.png" alt="" style="zoom:50%;" />

## 动态参数  
MOS管的动态特性与寄生电容有关，其等效模型如下所示。 
<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210906223337044.png" alt="" style="zoom:67%;" />

其中  

- Input capacitance:Ciss = Cgd + Cgs      
- Output capacitance:Coss = Cgd + Cds  
- Reverse transfer capacitance:Crss = Cgd  

整个NMOS管导通时如下图所示。  
<img src="https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210906223439633.png" alt="" style="zoom:67%;" />

分解开来如下图所示。  
![](https://mythidea.oss-cn-beijing.aliyuncs.com/undefinedimage-20210906223522421.png)


t0-t1：驱动电压瞬间拉高时，Vgs从0上升到Vth，上升的时间常数t=Rg(Cgs+Cgdlow)。就是说Vgs上电时，RC电路充放电，给GS、GD电容充电。其中R为G极电阻，电容有Cgs和Cgd的一部分。此时的VDD是已经加在上面的稳定电源，当驱动电压加上时，Vds>Vgs，故导通前Cgd由DG之间充电，Vgs上升过程中Vgs给Cgd充电。由于MOS管没导通，所以DS之间电压不变，而Ig随着电容的充电而慢慢降低，该区域为夹断区。      

t1-t2：Vgs达到Vth后，形成导电沟道，开始有Id电流，但电流比较小。Id与Vgs之间成线性关系（如上面图gfs所示），当Vgs增大时，DS处于导通状态，Vds降低，但是Vds降低使Cgd增加，这又反过来导致Vgs分了部分电流给增加的电容充电，使Vds趋于恒定，形成一种负反馈。另外一种解释，Vgs增大时，反型层靠近S端随Vgs而变宽，靠近D端变窄，导致gd电容变大。当形成预夹断时Id的电流接近最大值。该区域为电阻区。  

t2-t4：Id达到最大值保持不变，导电沟道达到最大。由于上电时VDD已给Cgd充满电，当Vgs开启时，在t1~t2阶段，Cgd电容增大，驱动电流补电，导致Vds不变，当预夹断形成时Cdg基本不变，驱动电流不再补电，Cgd快速放电，Cgd放电时Vgs给它补电，故gs之间电流基本不变，Cgd放电与Vgs充电形成平衡，Vgs不变，形成平台。这个平台就是密勒平台。  

为什么Cgd在t2时刻开始快速放电，因为t1时刻放电电流小，没有形成最大的导电沟道，导通电阻大，放电缓慢，当导电沟道完全成型后，放电最大化，Cgd开始快速放电，在放电过程中，Cgs的电被Cgd吸取部分，同时Vgs又补充部分，形成平衡，故密勒平台时期Vgs不变，Ig不变。  

t4：Cgd放电完成，VDD通过沟道提供电流给负载，此时Vgs继续给Cgs、Cgd充电直到两者饱和。  

总的来说就是：VDD上电后Vgd已充满，Vgs开启时，Ig先给Cgs、Cgd充电直到导电通道形成，然后Cgd、Cgs放电（密勒平台），然后Vgs继续上升给Cgd、Cgs充电直到Vgs达到设定值。  

## 参考资料
[MOSFET驱动电路设计参考](https://www.cypress.com/file/64076/download)  