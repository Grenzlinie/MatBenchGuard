# Analysis of Cooling a Microprocessor using Embedded Thermoelectric Coolers

Won Ho Park and C.K. Ken Yang

University of California, Los Angeles, 56-147A Engineering IV Building, Los Angeles, CA 90095

Tel: 310.206.3665 Fax: 310.206.8495 E-mail: whpark@ee.ucla.edu

## ABSTRACT

Recently, advanced embedded thermoelectric coolers (eTECs) have been demonstrated for mitigating thermal problems. Operating IC at a lower temperature can result in reduced electronic power, improved reliability and potentially improved speed. However, total power dissipation must include both the electronic power and the cooling power. This study explores the amount of total power reduction using eTECs. We present a model that incorporates both a real-world microprocessor and thermoelectric cooling systems. The analysis indicates that an optimal operating point exists and depends on the parameters of electronics and cooling systems. Using the thermoelectric element of ZT=1, we demonstrate that power savings of at least 15% is realizable when the electronic components have leakage power ratio that are greater than 50%. The analysis also shows that the amount of power saving is projected to improve with technology due to increased leakage, reaching up to 16% for 32nm technology and beyond.

## I. INTRODUCTION

Recently, advanced embedded thermoelectric coolers (eTECs) that allow integration with IC processing have been studied for localized cooling that might offer solutions to both the power and thermal problems [1] - [3]. A thermoelectric cooler (Fig. 1) is a small electronic heat pump that uses the Peltier effect to create a heat flux between the junctions of dissimilar materials. By adjusting DC current, heat flow can be proportionally modified allowing precise control of the junction temperature. Recent interest is in using eTEC to locally and selectively cool an area with high power density to resolve thermal problems in integrated circuits.

Localized cooling of an IC may result in reduced power consumption since lowering the temperature can reduce power consumption. However, there remains a question of whether localized spot cooling can also lead to an *overall system power saving* when the cooling cost of eTECs is factored in. How much of an effect cooling has upon different types of blocks in terms of overall system power and temperature also remains to be answered. This study explores the optimal operating temperatures and the amount of total power reduction achievable from localized cooling. We focus on developing a complete and realistic system-level model that includes both the electronic characteristics of various functional blocks and the realistic performance of eTECs.

## II. SOURCES OF ELECTRONIC POWER

The mechanisms for power dissipation of digital CMOS ICs are well understood [4]. The total power dissipation can be estimated by the sum of the active power and leakage power. With lower temperatures, the delay performance of functional blocks improves.

![](./images/813343552519012354_1.jpg)

Fig. 1 Schematic of a thermoelectric cooler.

![](./images/813343552519012354_2.jpg)

Fig. 2 Electronic parameters of three different types of processors with (a) power density of core and last-level cache block at 70°C and 100°C and (b) leakage power ratio of core and last-level cache block at 70°C and 100°C

A common trend in the current power-limited design environment is to trade the improved delay for a reduction in power. This underlying approach is the basis of the power analysis in this paper.

The percentage of electronic power due to its leakage and active components depend on the functionality of digital blocks. The functionality impacts this ratio through the average activity factor, $\alpha$. Due to high-levels of logic activity under smaller area, logic blocks tend to have high power density with small percentage of leakage power. On the other hand, memory blocks attribute a large portion of

![](./images/813343552519012354_3.jpg)

Fig. 3 Electronic parameters of major function components in the core block of the Xeon processor with (a) power density at 70°C and 100°C and (b) leakage power ratio at 70°C and 100°C

its power to leakage. In this paper, McPAT, an integrated power, area, and timing modeling framework simulator, is used to explore to verify these electric characteristics [5].

Fig. 2 illustrates power density and leakage percentage of a microprocessor's execution core and last level cache units for the 180nm Alpha 21364 processor [6], the 90nm Niagara processor [7], and the 65nm Xeon processor [8]. Clearly, core blocks have higher power density that is approximately 4 to 10 times higher than the last level cache blocks. Due to lower level of activity, last level cache dissipates a significant portion of its power to leakage with at least 30% and up to 60% of leakage at 100°C.

A more fine-grained breakdown of power density and leakage percentage of major functional components in the core block of the Xeon processor are shown in Fig. 3. As expected, different functional blocks operate with different leakage and power density. Similarly, in general, blocks with high power density tend to have low leakage power percentage.

## III. THERMOELECTRIC COOLERS

A configuration of microelectronic system with localized cooling is composed of a silicon wafer, a thermal interface material (TIM) with eTECs, a heat spreader, and a heatsink (Fig. 4). Conceptually, it is possible for the eTEC to be applied with fine granularity for each functional block of a processor. More realistically, the eTEC can be applied across coarse regions on an IC.

Thermoelectric materials are characterized by their figure of merit ZT, defined by

$$
ZT = \frac{S^2T}{RK} \tag{1}
$$

where S=Seebeck constant, R=electrical resistivity, K=thermal conductivity, and T=temperature. Thermoelectric material needs to obtain low thermal conductivity in order to prevent heat losses through heat conduction between the hot and cold side. The material also needs high electrical conductivity to minimize Joule heating. A TEC absorbs dissipated electric power (P<sub>electric</sub>) that is compensated by the heat conduction and Joule heating losses.

![](./images/813343552519012354_4.jpg)

Fig. 4 View of a microelectronic system with embedded TEC locally cooling a functional block.

Coefficient of Performance (COP) is a performance metric of any refrigerator cycle and it is defined as the ratio of the refrigeration effect (P<sub>electric</sub>) to the net work input (P<sub>cooling</sub>) to obtain that effect.

$$
\mathrm{COP} = \frac{\mathrm{P}_{\text{electric}}}{\mathrm{P}_{\text{cooling}}} \tag{2}
$$

These parameters that characterize the performance of the eTEC are merged into a single model with the electronic power dissipation of a microprocessor as shown in Section II. With this model, this paper evaluates the impact of localized cooling on the power dissipation of functional blocks.

We first perform our analysis using parameters provided by [5] which has effective ZT of 0.5. We also extrapolate from this data to model a hypothetical eTEC with higher performance that have effective ZT of 1.0 and 2.0 to explore the potential improvement through a better eTEC [1] - [3].

## IV. ANALYSIS OF COOLING A MICROPROCESSOR USING ETECS

Using the performance curve from an eTEC with ZT=0.5 [2], the total power is analyzed while sweeping the junction temperature and keeping the operating frequency constant. Our first example considers the impact of cooling the *Branch Predictor* unit and the *L-3 Cache unit* of the Xeon processor from Section II.

The result of the analysis is shown in Fig. 5. Localized cooling allows T<sub>junction</sub> to operate at a lower temperature at the expense of cooling power. Total electric power decreases at lower temperature, but total power consumption increases when including the cooling cost. Due to the sharp increase in cooling cost at lower temperatures, cooling the *Branch Predictor* unit does not provide any system power benefits. On the other hand, *L-3 Cache* unit dissipates the minimum total power of 1.41W with 2°C of cooling effect. This performance is only marginally (3%) better than the reference design. The amount of power reduction is limited by the obtainable COP. This particular example indicates that for localized cooling to work in terms of overall power perspective, both high COP and high cooling effect eTECs are required. Otherwise, due to the increase in cooling power cost, localized cooling does not yield significant system power and thermal benefits.

![](./images/813343552519012354_5.jpg)

Fig. 5 Optimization results of localized cooling (a) Branch Predictor and (b) L-3 Cache

To account for different functional blocks, Fig. 6 illustrates overall power performance for different $\mathrm{P_{leakage}/P_{electric}}$ ratios and amounts of power density. The figure shows contours of the power savings [%] as well as the amount of cooling effect [$^\circ$C] at various optimal power points. It can be shown from the figure that the amount of power savings and cooling effect depends on the characteristics of each functional block. Because of the exponential relationship between leakage power and temperature, the power saving of using TEC increases when the system has a large leakage component. Simulation shows that more noticeable power savings of 5-10% start to appear for systems with high leakage ratio. The amount of power saving is limited to 14% even for blocks entirely dominated by leakage. This analysis also indicates that the power saving has a dependence on power consumption. Note also that the amount of cooling effect increases with leakage percentage and power consumption but ranges only from 4 to 14 degrees at each optimal power point. Most functional blocks have leakage percentage that is <40% (Fig.3). This implies that the use of this particular eTEC for cooling the processor core does not result in overall system power saving and may not be worth the design overhead.

It is important to recognize that temperature reductions of $10^\circ$C can be important in cooling local hotspots to reduce the junction temperature for higher reliability. For this purposes, some amount of power penalty can be tolerated. We extend the analysis to consider the respective power penalty when obtaining 10 degrees of cooling effect for different $\mathrm{P_{leakage}/P_{electric}}$ ratios and power. The simulation result is shown in Fig. 7. We chose three possible hot spots with different amounts of power density: $0.16\mathrm{W/mm^2}$, $0.32\mathrm{W/mm^2}$, and $0.64\mathrm{W/mm^2}$. The results indicate that the block with large power density and high leakage power percentage gives the least amount of power penalty. In fact, in the case of leakage ratio of >45% with power consumption of $0.64\mathrm{W/mm^2}$, we see that no extra power is required to obtain 10 degree of cooling.

![](./images/813343552519012354_6.jpg)

Fig. 6 Contours of the percentage of power reduction and amount of cooling effect for different $\mathrm{P_{leakage}/P_{electric}}$ and power before any refrigeration.

![](./images/813343552519012354_7.jpg)

Fig. 7 Effect on the overall system performance to obtain 10 degree of cooling effect using eTEC with thermoelectric material of ZT=0.5.

We repeat the analysis using a hypothetical thermoelectric material with ZT=1. Other parameters associated with the analyses remain the same. Fig. 8 shows the maximum power savings and their associated cooling effect for different $\mathrm{P_{leakage}/P_{electric}}$ ratios and power density. When compared to the results in the previous section, power savings of at least 15% is realizable when the components have leakage ratio that are greater than 50% with power density of $0.5\mathrm{W/mm^2}$ or greater. This performance is 7X better than the performance obtained with thermoelectric element of ZT=0.5.

Moreover, the cooling effect at each optimal power point has increased substantially. In the case of components with high leakage and power, it is possible to lower the temperature by 10 without requiring a higher total power. In fact, for most of the different functional blocks in a microprocessor only a small amount of extra power is required to obtain 10 degrees of cooling. As apparent from these simulations, by using an eTEC with higher ZT, cooling can be used without power cost to improve reliability and localized cooling can actually result in reduced overall system power.

### V. RESULT OF COOLING A PROCESSOR

The eTECs are assumed to be locally applied with fine granularity to each functional block in the processor for spot cooling. Each block is cooled to its optimal temperature setting. Our results of cooling the functional blocks from Fig 3 using ZT of 1 are summarized in Table 1. Cooling the *Level-2 Cache* unit *Level-3*

![](./images/813343552519012354_8.jpg)

Fig. 8 Contours of the percentage of power reduction and amount of cooling effect for different $P_{leakage}/P_{electric}$ and power before any refrigeration with ZT=1.

Cache unit resulted in the maximum power saving of 2% and 7%, respectively. Associated cooling effects at their optimal operating points are 8 and 6°C. On the other hand, cooling other components does not provide any power benefits, and extra power would be needed to obtain temperature reductions. Table 1 shows the respective power penalty to obtain 10 degrees of cooling effect, represented by the negative percentage. For an example, cooling hotspots like the Rename unit would require extra 20% of power to reduce the junction temperature by 10 degrees. These results demonstrate that cooling with fine granularity is not necessary. Analyses provide a subtle conclusion that cooling the cache blocks result in the performance that is better than logic based blocks. This observation counteracts the underlying assumption of using eTEC for cooling hot spots. Compared to non-cooled processor, cooling only the cache units result in total power performance that is 2% better. Power savings from localized cooling is not as significant as from chip level cooling where chip level cooling using vapor compression refrigeration system would result in total power saving of >30% [9]. Nevertheless, localized cooling the right element can give some worthwhile improvements while providing the benefit of full integration.

<table>
<caption>TABLE I<br>Simulation result of fine-grain cooling each of the functional blocks from Fig. 3.</caption>
<thead>
<tr>
<th>ZT=1</th>
<th>Power Saving [%]</th>
<th>Cooling Effect [°C]</th>
</tr>
</thead>
<tbody>
<tr>
<td>L-3 Cache</td>
<td>7</td>
<td>6</td>
</tr>
<tr>
<td>L-2 Cache</td>
<td>2</td>
<td>8</td>
</tr>
<tr>
<td>I-Cache</td>
<td>-5</td>
<td>10</td>
</tr>
<tr>
<td>BRED</td>
<td>-2</td>
<td>10</td>
</tr>
<tr>
<td>I-Decoder</td>
<td>-3</td>
<td>10</td>
</tr>
<tr>
<td>Rename</td>
<td>-20</td>
<td>10</td>
</tr>
<tr>
<td>LdStQ</td>
<td>-11</td>
<td>10</td>
</tr>
<tr>
<td>ITB</td>
<td>-21</td>
<td>10</td>
</tr>
<tr>
<td>DTB</td>
<td>-8</td>
<td>10</td>
</tr>
<tr>
<td>Register File</td>
<td>-12</td>
<td>10</td>
</tr>
<tr>
<td>I-Scheduler</td>
<td>-12</td>
<td>10</td>
</tr>
<tr>
<td>Integer ALU</td>
<td>-8</td>
<td>10</td>
</tr>
</tbody>
</table>

The processor designed in 65-nm technology is scaled down to 45nm, 32nm, and 22nm technology nodes by assuming the area is proportional to the square of the feature size using the device parameters from the ITRS [10]. Table 2 provides the amount of power saving for the Level-2 Cache unit Level-3 Cache unit using thermoelectric material with ZT of 1 and 2. Due to the increase in leakage percentage with technology scaling, amount of power saving increases. Using eTECs of ZT=1 for cooling the Level 3 Cache is projected to improve the amount of power saving with technology scaling, reaching up to 16% for 32nm technology and beyond. Table 2 also summarizes the result of using higher ZT of 2. As expected, significant increase in power savings can be obtained.

<table>
<caption>TABLE II<br>Overall power saving [%] of cooling L-2 and L-3 cache at different technology nodes.</caption>
<thead>
<tr>
<th>Tech Node (nm)</th>
<th colspan="2">Level-2 Cache</th>
<th colspan="2">Level-3 Cache</th>
</tr>
<tr>
<th></th>
<th>ZT=1</th>
<th>ZT=2</th>
<th>ZT=1</th>
<th>ZT=2</th>
</tr>
</thead>
<tbody>
<tr>
<td>65</td>
<td>2</td>
<td>5</td>
<td>7</td>
<td>37</td>
</tr>
<tr>
<td>45</td>
<td>7</td>
<td>17</td>
<td>10</td>
<td>50</td>
</tr>
<tr>
<td>32</td>
<td>13</td>
<td>27</td>
<td>16</td>
<td>60</td>
</tr>
<tr>
<td>22</td>
<td>14</td>
<td>29</td>
<td>18</td>
<td>62</td>
</tr>
</tbody>
</table>

### VI. CONCLUSION
A complete system-level model that includes both the realistic electronic characteristics of various functional blocks and the performance of eTECs has been developed to obtain optimal operating temperatures and amount of total power reduction. Analysis indicates that the performance primarily relies on the amount of leakage power and the ratio of leakage to total electronic power. Power savings using eTECs are not as significant as cooling using other means such as a vapor compression cycle at the chip level but they have the benefit of allowing a fully integrated solution. The analysis shows that with ZT=0.5, cooling the right element (the cache) can give a modest 3% improvement. Enhancing the performance of the eTEC provides a much more compelling performance improvement in terms of both power (>10%) and reliability. Finally, since the amount of leakage power increases with technology scaling, using eTECs may be a possible power/thermal solution for future electronics.

### REFERENCES
[1] S. Krishnan, S. V. Garimella, G. M. Chrysler, and R. V. Mahajan, "Towards a Thermal Moore's Law," Proceedings of InterPACK 2005, pp.73409, 2005.

[2] G. J. Snyder, M. Soto, R. Alley, D. Koester, and B. Conner, "Hot Spot Cooling using Embedded Thermoelectric Coolers," in IEEE SEMI-THERM Symposium, 2006.

[3] Chowdhury, I., et al., "On-Chip Cooling by Superlattice-Based Thin-Film Thermoelectrics," Nature Nanotechnology, 2009, 4: p.235-238.

[4] A. P. Chandrakasan, S. Sheng, and R. W. Brodersen, "Low-Power CMOS Digital Design," IEEE Journal of Solid-State Circuits, vol. 27, no. 4. pp 473-484, April 1992.

[5] Li, Sheng, et al., "McPAT: An Integrated Power, Area, and Timing Modeling Framework for Multicore and Manycore Architectures," in IEEE MICRO, pages 469-480, 2009.

[6] A. Jain, et al., "A 1.2GHz Alpha Microprocessor with 44.8 GB/s Chip Pin Bandwidth," in ISSCC, 2001.

[7] A. S. Leon, K. W. Tam, J. L. Shin, D. Weisner, and F. Schumacher, "A Power-Efficient High-Throughput 32-Tread SPARC Processor," JSSC, vol. 42, 2007.

[8] S. Rusu, et al., "A Dual-Core Multi-Threaded Xeon Processor with 16MB L3 Cache," in ISSCC, 2006.

[9] Won Ho Park, et al., "Analysis of Refrigeration Requirements of Digital Processors in Sub-ambient Temperatures," Journal of Microelectronics and Electronic Packaging, vol. 7, no. 4, 4ᵗʰ Qtr 2010.

[10] International Technology Roadmap for Semiconductors (ITRS), 2010 edition, http:// public.itrs.net/