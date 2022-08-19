# Dry Electrode Challenges in Biopotential Signal Chains

In the [last blog post](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-understanding-cmrr-and-rld-in-biopotential-signal-chains),  I talked about the difference between two and three electrode  solutions when biasing the measurement inputs and managing CMRR  performance.  Now I’d like to focus a bit more on the electrodes  themselves. One question I have heard a few times with respect to  making biopotential measurements is “What is the sensor?”. I discussed a bit about how biopotential signals are generated in my [first blog](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-intro-to-biopotentials) and that they can be measured at the skin with electrodes.  These  electrodes act as transducers for ionic currents in the body and can be  as simple as placing a conductive material such as metal on the skin.

In fact, the first “electrodes” I ever used were two pairs of metal  scissors! It was a little over ten years ago and I was testing a first  prototype of the [AD8232](https://www.analog.com/en/products/ad8232.html) which was the precursor to the [AD8233](https://www.analog.com/en/products/ad8233.html) discussed in the [third blog](https://ez.analog.com/ez-blogs/b/engineerzone-spotlight/posts/precision-low-power-signal-chains-a-unique-ac-coupled-solution-with-configurability).  What better way to check the signal conditioning performance, than to  see your own ECG signal on the oscilloscope (isolated and battery  powered for safety of course).  I attached two wires to the evaluation  board, and then shorted those wires to the scissors. This made it  easier to make good contact when measuring ECG at the hands.  Eventually, I upgraded to a set of electrodes used in exercise equipment (see Figure 1). You can see that in this case, there are 4 electrodes  (2 per hand). The top pieces of metal are there for making the  differential biopotential measurement. The other two on the bottom are  used for biasing the body and/or right leg drive, demonstrating you can  do this at multiple points. The wires coming back from the electrodes  are shielded to minimize interference.

![ ](https://ez.analog.com/resized-image/__size/1260x354/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/jointpic.jpg)

Figure 1 – Scissors “electrodes” and exercise equipment electrodes

## Electrode Model

So how can we electrically model these electrodes? Figure 2 shows an example model where “Ehc” is the material dependent half-cell potential which is the result of  dissimilar electrolytic interfaces.  This is in series with an impedance (Rd in parallel with Cd) that represents the electrode-skin interface  and polarization at this location.  This is also in series with another  resistor (Rs) that takes into account other factors such as the  resistance of the electrode material.

![ ](https://ez.analog.com/resized-image/__size/1216x342/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/pastedimage1660566286639v1.png)

Figure 2 – Biopotential electrode model and location in measurement solution [1]

When referring to polarization, a perfectly “non-polarizable”  electrode behaves more like the resistor “Rd”. A close example of this  is the silver-silver chloride(Ag/AgCl) electrodes typically used in  medical applications where an electrolytic gel may be applied. These  are better for measuring, since they have lower contact impedance, lower noise, and reduced motion artifacts. Ag/AgCl electrodes also have a  lower half-cell potential relative to other materials as shown in Figure 3 below.

Perfectly “polarizable” electrodes behave more like the capacitor  “Cd”. A close example of this would be Platinum.  These electrodes are  better for stimulation and typically have higher noise and worse motion  artifacts. In reality it is difficult to manufacture a purely  polarizable or non-polarizable electrode so there will always be some Rd in parallel with Cd. 

One clarification on half-cell potentials is that this is not the DC  offset you are measuring differentially at the electrodes. Each  electrode has a half-cell potential, so what you are measuring is the  mismatch or difference between these.  For perfectly matched electrodes, the half-cell potential is part of the common mode voltage. Also, this half-cell potential changes as current flows through the electrode due  to polarization. This amount of change is called the overpotential. 

![ ](https://ez.analog.com/resized-image/__size/1156x614/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/halfcellpotentials.png)

Figure 3 – Table of half-cell potentials for various materials [1]

## Managing Dry Electrodes

One of the most frequent customer questions that comes up when  debugging biopotential signal chains usually comes back to difficulty  making good contact with dry electrodes. Sometimes this is just that  one person in the office that tested it and can’t seem to get a signal  out. Dry electrodes look more like a polarizable electrode and may take some time to settle while very small amounts of perspiration start to  build up. An easy check when having trouble getting a signal out is to  start by wetting the electrodes and/or skin (water or hand sanitizer  works just fine). If the signal shows up, then you know you are dealing with a contact issue.

A number of factors can lead to contact issues and should be considered as part of the design:

- Location of the electrodes, including any hair or dry skin (varies person to person)
- Electrode material and surface area making contact with skin (big  difference between exercise electrodes and a smaller form factor like  the [ADI VSM watch](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HCRWATCH4Z.html#eb-overview) shown in Figure 4)
- Pressure applied (like the tightness of a watch strap on the wrist)
- Leakage paths on the traces touching the electrodes (flux on the pcb)
- Input impedance of the measurement circuit as well as any other  circuits touching the electrodes such as lead off detection (for example the addition of a pull-up/pull-down resistor will change the input  impedance)

![ ](https://ez.analog.com/resized-image/__size/1312x386/__key/communityserver-blogs-components-weblogfiles/00-00-00-03-16/jointwatch.png)

Figure 4 – Analog Devices Vital Signs Monitoring (VSM) Watch with top and bottom electrodes

Stay tuned for the next month’s blog where I will discuss electrode/lead off detection methods.

[1] Neuman, M. R. “Biopotential Electrodes.” *The Biomedical Engineering Handbook: Second Edition.* Ed. Joseph D. Bronzino Boca Raton: CRC Press LLC, 2000.