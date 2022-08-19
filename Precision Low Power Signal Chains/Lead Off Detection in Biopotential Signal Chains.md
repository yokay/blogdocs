# Lead Off Detection in Biopotential Signal Chains

In the [last blog post](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-dry-electrode-challenges-in-biopotential-signal-chains), I discussed electrode models and the challenges of managing dry  electrodes. Building off this information, let’s shift to the topic of  electrode or lead (pair of electrodes) off detection and how this  feature can impact the power and performance of the signal chain.  Lead off detection is a method for providing some indication (typically a  logic signal or interrupt) that a user is sufficiently connected to the  electrodes such that a biopotential signal measurement can be made.

So how does this affect the power? For one, when a device such as a  watch or chest strap is not being used, you wouldn’t want to burn power  unnecessarily. Some indication of a “leads off” condition could enable  the power down of components in the signal chain while in this state.  Similarly a “leads on” condition could act as a wake-up signal to alert  the microprocessor to power up components and/or start taking  measurements again. See an example of this type of sequence using the  lead off detection (LOD) and shutdown (SDN) pins of the [AD8233](https://www.analog.com/en/products/ad8233.html#product-overview) in Figure 1. The lead off detection circuitry also adds to the total  power consumption. This may be more important if the function is still  active during power down. 

![ ](https://ez.analog.com/resized-image/__size/796x632/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1663615350480v1.png)

Figure 1 – Electrode connection and system wakeup sequence for the AD8233

Implementation of lead off detection will depend on the use of two or three electrodes and can also provide input biasing (see [fifth blog](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-understanding-cmrr-and-rld-in-biopotential-signal-chains)).  From a performance perspective, any circuitry touching the electrodes  can affect the input impedance and input currents can lead to electrode  polarization and an increase in differential offsets.

## Two Electrode DC Lead Off Detection

Figure 2 shows a DC lead off detection implementation for a two-electrode solution. A pull-up resistor (RPU) is tied to supply voltage on one input and an equal pull-down resistor (RPD) is tied to ground on the other input. Rtotal represents the body  impedance and the contact impedances for the two electrodes. A  simplified way of looking at this, is if Rtotal is an open, the inputs  to the instrumentation amplifier will pull apart and rail the output  indicating “lead off”. This would happen if either electrode were  disconnected. When both electrodes are connected, and Rtotal is  approximated as a short, then the inputs will be biased to mid supply  (+Vs/2). 

![ ](https://ez.analog.com/resized-image/__size/880x498/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1663615449270v2.png)

Figure 2 – DC lead off detection and biasing for a two-electrode solution

In actuality, the electrode contact impedances will contribute to some differential offset and RPU and RPD should be made sufficiently large (say 10MΩ to start) to minimize current  through the electrodes. The fact that the current is flowing through  electrodes in equal and opposite directions means their polarization  will be different. This is one reason I prefer the three-electrode  solution discussed in the next section. The “lead off” indicator could  also come from low power comparators. The comparators are used to  monitor the voltages at the instrumentation amplifier inputs and allow  for preset threshold voltages.

## Three Electrode DC Lead Off Detection

In the three-electrode solution shown in Figure 3, the input bias  (Vbias) is provided from a third electrode. Now each input has a  pull-up resistor to the high supply such that if there is a loss of  contact on electrodes 1 to 3 (Rc1-Rc3), separate comparators can detect  which input electrode is compromised. By having the current flow in the same direction in Rc1 and Rc2, the polarization of the electrodes  should track better and lead to a common mode shift rather than a large  differential offset.

![ ](https://ez.analog.com/resized-image/__size/730x506/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1663615862551v6.png)

Figure 3 – DC lead off detection and biasing for a three-electrode solution

DC current sources could be used instead of pull-up resistors as  well.  This helps to take out the current dependency on the supply  voltage and Vbias while also decoupling the input impedance from the  current amplitude. The programmability of these currents as well as the comparator threshold voltage adds flexibility for different electrode  types. The ability to disconnect the current sources enables a spot  check vs. an always on approach.

## AC Lead Off Detection

The use of AC Lead Off Detection can take advantage of the fact that  the electrode model includes a capacitor in parallel with a resistor.  This means the electrode impedance is frequency dependent and can be  smaller at higher frequencies.  AC current sources as shown in the [ADPD6000](https://www.analog.com/en/products/adpd6000.html) block diagram in Figure 4 allow for zero DC current (no electrode  polarization) and can be set at a frequency outside the bipotential  signal bandwidth (4kHz in this case). A source and sink current are  switched back and forth between the two ECG channel inputs to generate  the AC current. The amplitude of the corresponding voltage signal can  be measured by the same ECG channel and synchronously demodulated for  comparison against a programmable threshold voltage.

![ ](https://ez.analog.com/resized-image/__size/1118x486/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1663615772763v5.png)

Figure 4 – AC lead off detection in ADPD6000

Other integrated solutions such as the [ADAS1021](https://www.analog.com/en/products/adas1021.html) and [MAX30003](https://www.maximintegrated.com/en/products/analog/data-converters/analog-front-end-ics/MAX30003.html) include a number of different options to consider for implementation of lead off detection as well.

This is the last in the series of biopotential signal chain  focused blogs, however we hope to bring more Precision Low Power topics  in the future. In the meantime, continue to visit our [Signal Chain page](https://www.analog.com/en/applications/technology/precision-technology/precision-low-power.html) as well as our dedicated [EngineerZone page](https://ez.analog.com/precision-technology-signal-chains/precision-low-power-signal-chains/) for the latest content and collateral.

### 