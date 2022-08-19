# Understanding CMRR and RLD in Biopotential Signal Chains

In the [last blog post](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-introducing-an-ultra-low-power-dc-coupled-input-signal-chain) we showed a DC coupled biopotential configuration using the [AD4130-8](https://www.analog.com/en/products/ad4130-8.html) and referenced a third electrode used to bias the body to midsupply.  We mentioned this was not a true Right Leg Drive (RLD) and that this may be acceptable for battery powered solutions. Today’s post will provide some clarity to why that is and what are some of the benefits of using  three vs. two electrodes for a single channel biopotential measurement.

## Input Biasing

First let’s talk about the third electrode’s use in biasing. Since  biopotential signals and interferers are fully differential, ideally the circuit measuring the electrodes would need to be biased somewhere near mid-supply. The circuit’s common mode input range should also be taken into account. In a two electrode solution, the body is floating to  some unknown potential, so resistors must be added to provide the DC  bias to the inputs as well as an input bias current return path. This  results in a reduced input impedance of the circuit measuring the  electrodes. With the addition of a third electrode, the inputs can be  set to this same DC bias via a low impedance path through the body  without the need for extra components, thus maintaining a high input  impedance. See this comparison in Figure 1 below.

![ ](https://ez.analog.com/resized-image/__size/968x354/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1657656782932v1.png)

Figure 1 – Biasing inputs with 2 and 3 electrodes

## Common Mode Rejection Ratio (CMRR)

In a bipotential signal chain, the typical common mode interferer of  concern is the 50/60Hz that comes from the AC Mains. The body acts as  an antenna and this 50/60Hz signal can show up at the electrodes.   While the CMRR specification found on a datasheet for a component like  an Instrumentation Amplifier is important, it is only one part of the  System CMRR. This datasheet specification is a figure of merit that  compares the gain of common-mode signals (ACM) to the gain of differential-mode signals (ADM):

![ ](https://ez.analog.com/resized-image/__size/390x104/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1657657058598v2.png)

Ideally, the common-mode gain is very small and the CMRR should be  high (100dB for example). Make sure to look at the Typical Performance  Curve (TPC) as well to see the CMRR vs Frequency (See [AD8237](https://www.analog.com/en/products/ad8237.html) example in Figure 2). Sometimes the datasheet specification table only provides the CMRR at DC.

![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1657657118180v3.png)

Figure 2 – CMRR vs Frequency of AD8237 for different gains

## System CMRR

Other factors that affect the overall system CMRR include common mode (CM) to differential mode (DM) conversion and isolated vs non-isolated  solutions.  We touched on CM to DM conversion in the [second blog](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-signal-chains-to-ac-or-not-to-ac-couple-that-is-the-question) when discussing AC coupling at the very frontend. When making a  differential measurement, anything that touches the inputs needs to be  balanced. This includes bias resistors, RFI filters, cables,  connectors, the pc board, and even the electrodes themselves. Figure 3  shows an example and how CMRR vs Frequency can be affected. 

![ ](https://ez.analog.com/resized-image/__size/1092x540/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1657657439211v4.png)Figure 3 – Example of mismatch effects on System CMRR vs Frequency

To model the 50/60Hz injection into the body, a simple capacitive  divider can be used and represented by a capacitance from the body to  the AC mains (Ct) and a capacitance from the body to earth ground (Cb).  A non-isolated circuit would have a direct short between system ground  and earth ground. Isolated circuits such as battery powered solutions  have some stray capacitance (Cstray) between an isolated ground and  earth ground as shown in the Figure 4 models. You can see the benefit  of the third electrode (Ze3), as it provides a direct path from the body to ground, shunting around the capacitive divider and reducing the  50/60Hz voltage picked up at the measurement electrodes (Ze1, Ze2).  Otherwise, in the 2-electrode solution, the 50/60Hz current path is  through the Zc1 and Zc2 common mode input impedances. This leads to a  larger common mode voltage at the input electrodes which can then be  converted to differential mode due to mismatch.

![ ](https://ez.analog.com/resized-image/__size/1058x466/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1657657793370v5.png)

Figure 4 – Models for Isolated 2 and 3 Electrode Biopotential Measurements

## Right Leg Drive

The name Right Leg Drive comes from the location of where the third  electrode was typically placed (furthest from the heart) for an ECG  measurement. The third electrode is not limited to this location  however. This circuit is built by sensing the common mode at the inputs (Vcm), buffering, inverting (usually with an integrator circuit) and  driving back into the body.  This creates a feedback loop, where higher loopgain at 50/60Hz improves common mode rejection. See example  circuit and integrator transfer function recommended for the [AD8233](https://www.analog.com/en/products/ad8233.html) in Figure 5. The integrator crossover frequency is set at ~1kHz.  Pushing to higher frequencies can increase risk of instability, so there is a tradeoff here.

![ ](https://ez.analog.com/resized-image/__size/1124x428/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1657757327060v1.png)

Figure 5 – Example AD8233 RLD Integrator Circuit and Transfer Function

Note that this circuit will be more effective for a non-isolated  solution or larger values of Cstray (such as AC mains powered solutions  with isolation). An isolated solution will also improve system CMRR as  Cstray becomes smaller, allowing the battery powered measurement circuit to move up and down with the common mode.

Next time we’ll talk about electrodes including their models, and the challenges of making good contact with dry electrodes. 



[1] B. Winter. & J. Webster, “*Driven-Right-Leg Circuit Design,”* IEEE Transactions on Biomedical Engineering, vol. BME-30, no. 1, pp. 62-66, Jan. 1983.