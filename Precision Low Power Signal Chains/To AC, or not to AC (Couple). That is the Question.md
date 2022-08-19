# To AC, or not to AC (Couple). That is the Question

In [last month's blog post](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-intro-to-biopotentials) we started to discuss the many interferers associated with making  biopotential measurements.  Since these interferers can have much higher amplitudes than the signal of interest and overlap with the signal  frequency ranges, the signal chain design should take this into  account. AC and DC coupled solutions are two approaches to consider  with performance tradeoffs that may depend on the design requirements  and application use case. For example, the power requirements of a  continuous monitoring system such as a body worn patch may be quite  different than a spot check measurement made with a wrist worn device.

Just to clarify, when we refer to AC or DC coupled signal chains in this series:

**AC coupled:** A high-pass filter/transfer function is located somewhere in the signal chain prior to ADC sampling.

**DC coupled:** No high-pass filter/transfer function  exists in the analog domain prior to ADC sampling, however digital  high-pass filters may be implemented after the ADC.

Sometimes the term “AC coupled” is associated with the circuit shown  in Figure 1, where the DC blocking capacitors are at the very front-end  of the signal chain. While this is certainly an option, it has some  weaknesses to consider. The resistor chosen will limit the input  impedance, which can lead to attenuation of the input signal in the case of high impedance sensors or dry electrodes. A filter is needed at each input to keep the circuit balanced differentially, therefore the  tolerances of these components will affect how well the filters match  and degrade common mode rejection vs. frequency due to common mode to  differential conversion. The plot in Figure 1 shows that at a worst case 5% tolerance mismatch of all passive components, the CMRR at 50/60Hz is already less than 60dB and this is prior to considering any additional  electrode mismatch or performance of the Instrumentation Amplifier  (In-Amp).
![ ](https://ez.analog.com/resized-image/__size/640x480/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/0576.ACcouplefront3.png)![ ](https://ez.analog.com/resized-image/__size/706x424/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1648148329632v6.png)



Figure 1 – Example of high-pass filter at  front-end and corresponding CMRR vs Frequency plot for worst case  component tolerances at the filter output

Now let’s walk through two example signal chains. In both cases the  very front-end will include an In-Amp, taking advantage of features such as high input impedance, high CMRR, and differential to single-ended  conversion.

## AC Coupled Signal Chain

Figure 2 shows an example AC coupled signal chain for measuring a  small biopotential signal in presence of much larger DC offset. The size of this DC offset and supply voltage limits the gain of the In-Amp. A  single-ended high pass filter can then be applied to reject the  gained-up offset allowing for an additional gain stage for the signal of interest.  Further application-specific low pass filtering could also  be applied to remove higher frequency interferers such as EMG or  50/60Hz. From a noise perspective, the more gain you can apply to the  front-end relaxes the noise requirements of subsequent stages in the  signal chain. The referred-to-input (RTI) noise of the second gain  stage is divided by the gain of the In-Amp, and the RTI noise of the ADC is divided by both gain stages. This allows for a lower resolution and lower power ADC. The final signal being sampled by the ADC is primarily the gained up biopotential signal since the undesired interferers have  been filtered.  See KWIK Circuit [Amplifying AC signals with large DC offsets for Low Power Designs](https://ez.analog.com/precision-technology-signal-chains/precision-low-power-signal-chains/w/documents/17127/amplifying-ac-signals-with-large-dc-offsets-for-low-power-designs)for a detailed design example.

![ ](https://ez.analog.com/resized-image/__size/1168x438/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/ACcoupledchain.png)

Figure 2 – Example of AC coupled signal chain and frequency domain information at different stages

##  DC Coupled Signal Chain

Figure 3 shows an example of a DC coupled signal chain. The DC  offset limits the total system gain that can be applied, which means a  higher resolution ADC would be needed to achieve the desired noise  performance. Not shown in the figure is an anti-aliasing low pass  filter prior to ADC at a higher cutoff frequency than in the previous AC coupled example. In this case, the target biopotential signal is a  much smaller percent of the total signal sampled by the ADC, and further post processing and filtering can be done in the digital domain. 
![ ](https://ez.analog.com/resized-image/__size/1100x558/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/DCCoupledChain.png)

Figure 3 – Example of DC coupled signal chain and frequency domain information at different stages

The table in Figure 4 shows a summary of tradeoffs to consider when  designing an AC or DC coupled signal chain. Also, note this signal  chain discussion can apply to any application where the target signal is higher frequency than the interferers. For example, electromagnetic  flow meter solutions can be analogous to biopotential measurements with  similar performance requirements.



![ ](https://ez.analog.com/resized-image/__size/1080x354/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/ACvsDCtable.png)

Figure 4 – Summary table for AC and DC coupled signal chains

Stay tuned for the next blog where we will discuss a unique AC coupled solution and the “fast restore” concept.