# A Unique AC Coupled Solution with Configurability

In [last month's blog post](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-signal-chains-to-ac-or-not-to-ac-couple-that-is-the-question) we discussed the tradeoffs between AC and DC coupled signal chains when measuring small signals in the presence of much larger DC offsets and  low frequency interferers. We also showed that the location of the  high-pass filter in an AC coupled signal chain matters and can influence performance metrics such as CMRR, input impedance, and the amount of  gain that can be applied in the front-end. Another interesting way to  implement a high-pass filter function is shown in Figure 1 below. The  integrator circuit senses the output of the in-amp and will drive the  reference pin to whatever it needs to keep the in-amp output DC biased  at VREF. By feeding back a low-pass filtered version of the output and inverting, a high-pass filter transfer function is realized.

![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652271870724v1.png)

Figure 1 – High-Pass Filter implemented with Integrator Feedback Loop

## An Improved Variation

One unfortunate result of the circuit in Figure 1 is that for most  conventionally available in-amp architectures (2 or 3 op-amp) the offset cancellation happens after the gain is applied, so the gain is still  limited by the supply voltage and size of offset to prevent saturation  of internal nodes. Figure 2 shows a variation using an indirect current feedback architecture which enables offset correction prior to gain [1] and is at the core of the [AD8233](https://www.analog.com/en/products/ad8233.html) analog front-end design. This allows for high gain (100x) and higher  offset correction (+/-300mV) on low supply voltages (1.7-3.5V). By  including an additional gain/low-pass filter stage on the [AD8233](https://www.analog.com/en/products/ad8233.html), all the signal conditioning can be done with external passives around a single low power IC (50uA). With features such as a reference buffer,  right leg drive, lead-off detection, shutdown, and fast restore, the [AD8233](https://www.analog.com/en/products/ad8233.html) provides a complete solution for battery-powered biopotential applications (See Figure 3 below).



![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652271273754v1.png)

Figure 2 – High-Pass Filter implemented with Indirect Current Feedback Architecture [1]

![ ](https://ez.analog.com/resized-image/__size/746x726/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652214570521v3.png)

Figure 3 – AD8233 with 2 pole high and low pass filters and additional gain

## Flexibility for Different Filter Configurations

Since passive components are placed external to the [AD8233](https://www.analog.com/en/products/ad8233.html), there are several configurations for setting the high and low pass  cutoff frequencies, the number of poles for each, and additional gain  that can be tailored to the target application. Figures 4 and 5 show  different ECG configurations for the [AD8233](https://www.analog.com/en/products/ad8233.html) in the frequency and time domains respectively. You can see for the  sports bandwidth, a very narrow bandpass filter with high gain is  applied and the resulting distorted signal. This works well as a heart  rate monitor since there is higher frequency content in the QRS  complex. For the wider monitoring and diagnostic bandwidths, the gain  is limited to avoid saturation of in band interferers. 

![ ](https://ez.analog.com/resized-image/__size/864x500/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652214717464v4.png)

Figure 4 – Frequency domain information for three AD8233 ECG configurations

![ ](https://ez.analog.com/resized-image/__size/810x608/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652214742376v5.png)

Figure 5 – Time domain information for three AD8233 ECG configurations

Different filter/gain configurations could be implemented for EMG or  EEG as well. Figure 6 shows different types of EEG signals and their  corresponding bandwidths. It is worth noting the high-pass filter can  also assist with filtering of 1/F noise. A dedicated [AD8233](https://www.analog.com/en/products/ad8233.html) filter design tool is available to assist with optimization of the bandpass filters.

![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652214804188v6.png)Figure 6 – EEG signal types and bandwidths [2]

## Fast Restore Overview

Have you ever been on a piece of exercise equipment, attempted to  take your heart rate, and proceeded to wait a frustratingly long time  for that number to show up? Chances are this is due to the very slow  time constants that come with AC coupling. For events such as power up, a fast step, or initial electrode connection the large capacitors need  some time to charge.  A fast restore circuit speeds up this charging and can be done manually (on demand) or automatically. The [AD8233](https://www.analog.com/en/products/ad8233.html) does this automatically by sensing the event and switching a smaller  on-chip resistor in parallel with the larger external resistor to  effectively reduce the time constant of the high-pass filter for a  predetermined amount of time. Figure 7 shows the improvement using fast restore for an electrode that is removed and reconnected after three  seconds.

![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652215389953v1.png)

Figure 7 – Comparison of ECG settling for AD8233 with and without fast restore enabled

## What About the ADC?

As we showed in last month’s blog, AC coupling reduces the resolution requirements of the ADC. If cost and board area is a concern, then  running the [AD8233](https://www.analog.com/en/products/ad8233.html) directly to a microcontroller with an embedded ADC may be an option.   If electrode/channel count and routing is important, the [AD4695](https://www.analog.com/en/products/ad4695.html), an easy to drive, 16-channel, 16-bit SAR ADC can be used to multiplex up to 32 electrode inputs. This is done by locating an [AD8233](https://www.analog.com/en/products/ad8233.html) near each pair of electrodes and routing it’s single-ended outputs to  the multiplexed ADC, which can be preferable to routing multiple  electrodes long distances. See example signal chain in Figure 8 below.

![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1652214897031v8.png)

Figure 8 – Multi-channel signal chain example for high electrode counts

Next time we will discuss an example of an ultra-low power DC coupled solution.

[1] Alexander, et al. (2013). *Apparatus and method for amplification with high front-end gain in presence of large DC offsets* (U.S. Patent No. 8,390,374). U.S. Patent and Trademark Office. [URL](https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=8390374.PN.&OS=PN/8390374&RS=PN/8390374)

[2] Abhang, Priyanka & Gawali, Bharti. 2015. “Correlation of EEG Images and Speech Signals for Emotion Analysis.” *British Journal of Applied Science & Technology.* 10. 1-13.