
# Isotope quantum effects in the metallization transition in liquid hydrogen

Sebastiaan van de Bund, \( ^{1} \)  Heather Wiebe \( ^{1} \)   \( ^{1} \) , Graeme J. Ackland \( ^{1} \) 

School of Physics & Astronomy, The University of Edinburgh, Edinburgh, EH9 3FD, United Kingdom. (Dated: May 13, 2021)

Quantum effects in condensed matter normally only occur at low temperatures. Here we show a large quantum effect in high-pressure liquid hydrogen at thousands of Kelvins. We show that the metallization transition in hydrogen is subject to a very large isotope effect, occurring hundreds of degrees lower than the equivalent transition in deuterium. We examined this using path integral molecular dynamics simulations which identify a liquid-liquid transition involving atomization, metallization, and changes in viscosity, specific heat and compressibility. The difference between  \( H_{2} \)  and  \( D_{2} \)  is a quantum mechanical effect which can be associated with the larger zero-point energy in  \( H_{2} \)  weakening the covalent bond. Our results mean that experimental results on deuterium must be corrected before they are relevant to understanding hydrogen at planetary conditions.

Hydrogen, despite being the simplest element on the periodic table, exhibits rich physics at high pressures. Of particular interest is the insulator-to-metal transition, wherein the system transforms from an insulating molecular phase to a conducting phase. Extremely high static compression is required to reach the metallic solid \( ^{[1, 2]} \) , but transition to a metallic liquid has been observed in both static \( ^{[3-6]} \)  and dynamic \( ^{[7-9]} \)  compression experiments. This liquid-liquid phase transition (LLPT) is of vital importance to the modelling of the interior of Jovian-like planets \( ^{[10-12]} \) , as the metallization of hydrogen is thought to cause the demixing of hydrogen and helium at pressure \( ^{[13]} \) . Despite this importance, the nature of the LLPT is not fully understood. The prevailing hypothesis is that the LLPT is a first order transition between an insulating molecular liquid and a conducting atomic one, terminating at a critical point between 1000 and 1500 K. This is supported by density functional theory (DFT) \( ^{[14-18]} \)  and quantum Monte Carlo \( ^{[19-22]} \)  simulations. However, a quantitative agreement between theory and experiment has not yet been achieved, and the consensus in modelling was recently challenged \( ^{[23]} \) .

The hydrogen phase diagram exhibits features which are impossible in classical physics. Such features are typically only seen at low temperatures and involve nuclear quantum effects (NQE). One example is the solid "Phase I" of hydrogen, which extends to zero temperature but involves freely-rotating molecules. Then there is a significant difference between  \( H_{2} \)  and  \( D_{2} \)  in the low temperature phase boundary between Phase I and the broken-symmetry Phase II, in which both isotope mass and quantum spin statistics play a role \( ^{[24]} \) .

However, "Low-temperature" begs the question "Low compared to what?" No isotope effect is known for the melting line in hydrogen, and nuclear quantum effects are often ignored at the kiloKelvin temperatures of liquid hydrogen. The melting transition involves changes in intermolecular bonding, which is a relatively weak interaction. The LLPT, on the other hand, involves breaking the covalent bonds. The zero-point energy of  \( H_{2} \)  is 78.46 meV ( \( \sim 910 \)  K) higher than that of  \( D_{2} \) , \( ^{[25]} \)  and so the covalent bonding in  \( H_{2} \)  is significantly weaker. Consequently, isotope effects at an unprecedentedly high temperature could be manifested in the experimentally observable difference in the LLPT phase boundary. Indeed, a 700 K difference in the LLPT has lines of  \( H_{2} \)  and  \( D_{2} \)  was reported by Zaghoo et al. by monitoring reflectivity in a laser-heated diamond anvil cell \( ^{[5]} \) . Interestingly, a spectroscopic study conducted by Jiang et al. one year later did not detect an appreciable isotope effect \( ^{[6]} \) .

There are numerous pitfalls in calculating the hydrogen LLPT (see Supplementary Material for further discussion \( ^{[26]} \) ). Cheng et al. recently demonstrated how many previous studies with less than 250 atoms and trajectories several ps in length were stuck in a solid rather than molecular-liquid phase.  \( \Gamma \) -only k-point sampling leads to unphysical chain-like "polyhydrogen" structures  \( [27] \)  and inclusion of NQE \( ^{[19, 21, 22, 28]} \)  is essential to finding any isotope effect because in classical theory, the phase boundaries of hydrogen and deuterium are identical \( ^{[29]} \) . Such a difference undermines the relevance of experiments on deuterium to determine the hydrogen equation of state - a crucial component of planetary and exoplanetary science.

Another challenge for DFT is that most exchange-correlation functionals cannot describe both molecular and metallic phases well, further contributing to the wide spread of results for the LLPT line from DFT (see Table S1 in Supplementary Material \( ^{[26]} \) ). Functionals which do not correctly describe the high density limit of the exchange energy are particularly poor for describing molecule-atom transitions \( ^{[30]} \) . Here we adopt the BLYP functional for the majority of our results \( ^{[31, 32]} \)  which has been shown to be the closest to Quantum Monte Carlo for molecular systems, including molecular metals which are problematic with PBE \( ^{[33]} \) . Nevertheless, by comparing to additional simulations performed using PBE \( ^{[34]} \)  and vdw-DF \( ^{[35]} \)  we also show that while the location of the phase boundary strongly depends on the functional, the isotope effect is not nearly as sensitive.

In this paper we use the ring polymer path integral molecular dynamics (PIMD) technique \( ^{[36]} \)  in combina-
 

tion with DFT to calculate the LLPT boundary for classical  \( H_{2} \)  and quantum  \( H_{2}/D_{2} \) . We demonstrate the large isotopic shift by monitoring various properties of the system along five isotherms ranging from 1000 to 2500 K for both  \( H_{2} \)  and  \( D_{2} \) . This isotope shift is impossible in classical physics, and is conclusive evidence of important NQEs at kiloKelvin temperatures.

One measure of the LLPT is the fraction of  \( H_{2} \)  molecules present in the system. This can be obtained by tracking the height of the first peak in the radial distribution function (RDF), which corresponds to the molecular bond length. The results in Fig. 1a) clearly show dissociation occurring for both  \( H_{2} \)  and  \( D_{2} \) , as evidenced by a drop in peak height with increasing pressure. The relative sharpness and magnitude of this drop are temperature-dependent, with the low temperature isotherms exhibiting the sharpest, largest drop and high temperature isotherms exhibiting smooth, small changes in peak height. The isotope effect is observed here as a shift in the phase boundary between  \( H_{2} \)  and  \( D_{2} \) . This shift is on the order of 250 K.

![](./images/867751696124609123_1.jpg)

![](./images/867751696124609123_2.jpg)

Fig. 1 Evidence of molecular dissociation. (a) Height of first (normalized) RDF peak, which corresponds to the molecular bond length. While the peak becomes relatively small, it does not disappear even in the atomic phase. (b) Fractions of  \( H_{2} \)  and  \( D_{2} \)  dimers present, where a stable dimer is defined as two H or D atoms that are less than  \( 0.9\AA \)  apart for at least 85 fs. Example RDFs are shown in the supplementary materials.

The change in RDF provides clear evidence of a transition, but does not explicitly consider the existence of molecules and does not distinguish between possible  \( H_{n} \)  clusters for n higher than 2. A more intuitive description of the dissociation can be found by considering the fraction of atoms that form a molecule. This is extracted from the interatomic distances, noting that the molecules continually break apart and reform, akin to a chemical reaction  \( H_{2} \rightleftharpoons 2H \) , which naturally introduces the idea of a molecular lifetime. We define a molecule to be two hydrogen or deuterium atoms less than 0.9 Å apart for at least 85 fs. This allows for at least 10 vibrations in the case of hydrogen. This choice is motivated by the limits of experimental detectability: it corresponds to a spectroscopic natural linewidth of 400 cm \( ^{-1} \) .

The resulting dimer fraction across the PIMD runs is shown in Fig. 1b). The limiting cases of high and low temperatures show that the dimer fraction tends to the expected values of 0 and 1 in the atomic and molecular limits, although pressures near the transition here will have a sizeable fraction of the liquid already dissociated. Like the RDF peak height, the dimer fraction drops steeply across the transition pressure for all isotherms. However, this drop can only be considered to be discontinuous around 1000 K for hydrogen and up to around 1250 K for deuterium; at higher temperatures the transitions become a crossover. This suggests that the critical point of the LLPT likely lies between 1000 and 1500 K for both isotopes, and is higher in deuterium.

![](./images/867751696124609123_3.jpg)

Fig. 2 Diffusion constant D as calculated from mean square displacements for  \( H_{2} \)  and  \( D_{2} \) , showing evidence of increasing diffusivity across the dissociation with a clear isotope effect.

The onset of dissociation is also marked by an increase in the diffusivity. Fig. 2 shows calculated diffusion constants D for all isotherms, where it can be seen that D markedly increases in the high pressure atomic phase. The curves are qualitatively similar, allowing for the two-times larger deuterium mass, but an isotope effect is seen in that the  \( H_{2} \)  transition is shifted towards lower pressures. The results are qualitatively similar to results obtained previously in AIMD calculations \( ^{[16, 18]} \)  which showed that the proton diffusivity increases rather than decreases with increasing pressure, meaning that the high pressure phase has lower viscosity. The diffusion constant remain nonzero in all simulations above the melt line and
 

a close look at the mean squared displacement for these trajectories (shown in the Supplementary Materials) indicates that even at low temperatures, the simulations are indeed of a flowing liquid.

The LLPT is perhaps best thought of as a chemical reaction between distinct species H and  \( H_{2} \) . This is in part because the transition is anomalous compared to first order transitions usually encountered, as there is no phase separation in the coexistence region: atomic and molecular hydrogen are continually interconverting, and therefore appear miscible \( ^{[18]} \) . Nevertheless, the location of the phase boundary can be established by considering various thermodynamic quantities. Since the system undergoes a small volume change across the isotherm either abruptly or gradually depending on the temperature, this will create a clear signature in the isothermal compressibility  \( \kappa_{T} = -\left(\partial V/\partial P\right)_{T}/V \) . Here, it is estimated using the equilibrated NVT volumes and pressures using finite differences. These results are shown in Fig. 3a), along with a fit to obtain the location of the peak. In theory,  \( \kappa_{T} \)  should diverge at a first-order transition and show a peak along an extension of the phase boundary beyond the critical point (the “Widom line”). While this cannot happen in a finite sized system, the peaks can still be seen to be very sharp for both isotopes at low temperatures. For both isotopes the peaks also widen at higher temperatures, which is indicative of a crossover rather than a phase transition.

The other thermodynamic quantity considered is the heat capacity at constant volume  \( C_{V} \) , as this can be calculated directly from fluctuations in the internal energy. This should also diverge at a first-order transition and show a peak along the Widom line, due to the energy required to break the bonds. To calculate  \( C_{V} \)  in the PIMD formalism, some modifications must be made to account for interactions between beads. For these results, the centroid virial heat capacity is employed (see Supplementary Materials) to calculate the heat capacity of the full PIMD ring polymer system \( ^{[37]} \) . The results are shown in Fig. 3b) for the various isotherms for both  \( H_{2} \)  and  \( D_{2} \) . The heat capacity is also clearly peaked like  \( \kappa_{T} \) , but noisier due to it being a quantity obtained from fluctuations.

In both the quantities considered, the  \( D_{2} \)  peaks are shifted compared to  \( H_{2} \)  which further identifies the isotope effect. The magnitude of the peaks in both the heat capacity and compressibility is also larger in deuterium than hydrogen at lower temperatures. Both the quantities also show broadening of their respective peaks at higher temperatures, clearest in the compressibility, where the transition becomes a crossover rather than a thermodynamic phase transition.

The prevailing belief about the LLPT is that metallization and dissociation occur together, \( ^{[20, 21]} \)  but in principle there is no reason that these two phenomena must coincide exactly. Furthermore, metallization can be observed at a distinctive pressure even beyond the crit-

![](./images/867751696124609123_4.jpg)

![](./images/867751696124609123_5.jpg)

Fig. 3 (a) Estimated isothermal compressibility  \( \kappa_{T} = -\left(\Delta V/\Delta P\right)_{T}/V \)  calculated using fixed volumes and equilibrated pressures for both isotopes. Solid lines are fits consisting of an exponential plus a Gaussian function. The centre of the Gaussian peak was then used to establish the location of the phase boundary and Widom line. (b) Heat capacities of the full ring polymer systems for  \( H_{2} \)  and  \( D_{2} \)  established from fluctuations in energy estimators. Solid lines are a guide to the eye.

![](./images/867751696124609123_6.jpg)

Fig. 4 Calculated DC electrical conductivity for  \( H_{2} \)  and  \( D_{2} \)  showing the onset of metallization. Scatter points are conductivities of individual samples. A tolerance of 2000 S/cm for metallization is indicated by dotted lines.
 

ical point, perhaps by a percolation transition \( ^{[38]} \) . Onset of metallization in our simulations was monitored by calculating the Kubo-Greenwood conductivity \( ^{[39]} \)  from snapshots taken from the PIMD trajectories. These results are shown in Fig. 4, where a minimum conductivity of 2000 S/cm was used to distinguish the metallic phase \( ^{[7, 40]} \) . The conductivity steeply increases by two orders of magnitude at the transition pressure, coinciding very closely with dissociation in Fig. 1: hydrogen metallizes at lower temperature than deuterium. Our results show that at all temperatures hydrogen has higher conductivity than deuterium. Interestingly, this was noted experimentally by Weir et al. \( ^{[7]} \)  but ascribed to a large difference in density, and the exact values remain uncertain \( ^{[41]} \) .

The results are summarized in Fig. 5 on a PT phase diagram, established using peaks in the isothermal compressibility as this was found to give the most distinctive peaks. The Clapeyron slope is observed to be negative, which is consistent with the small but negative volume change across the transition. The volume change and Clapeyron slope are slightly larger for  \( D_{2} \) ; configurational entropy cannot be calculated precisely, but from volume and slope we estimate it to be about  \( k_{B}/2 \)  per molecule, consistent with the extra degree of freedom from breaking the bond. The isotope effect can be clearly observed as a shift in the transition pressure, which is largest in magnitude at lower temperatures where NQE effects are most significant.

The location of the phase boundary is largely influenced by two contributions. Firstly, including NQE significantly lowers the transition pressure. This be seen from complementary AIMD runs using BLYP and classical H nuclei shown in Fig. 5b), where the phase boundary is obtained from the isothermal compressibility using identical methods to the PIMD runs.

Secondly, the location of the LLPT is very sensitive to the choice of exchange-correlation functional, which can shift the whole phase boundary by as much as 100 GPa \( ^{[18]} \) . This is mainly due to the well-known tendency of the PBE-based functionals \( ^{[34]} \)  towards easy metallization compared with functionals which correctly describe the high density-gradient limit \( ^{[30]} \) . Additional PIMD runs, shown in Fig. 5b (further discussed in the Supplementary Material \( ^{[26]} \) ), reveal a similarly significant spread in the location of the phase boundary.

Nevertheless, the isotope shift is found to be far less sensitive to the choice of functional (in contrast to other systems with significant NQE such as liquid water \( ^{[21]} \) ), giving a shift of almost 30 GPa at 1000 K. The magnitude of the isotope effect is smaller than observed in experiments by Zaghoo et al. \( ^{[5]} \) , but more similar to CEIMC simulations.

The critical point is difficult to locate with MD. The discontinuous changes in thermodynamic properties below the critical print are blurred by finite size effects, and anomalous peaks remain along the Widom lines beyond  \( T_{c} \) . Both the molecular dissociation and metallization curves match up with the thermodynamic phase boundary below the critical point, and thus also exhibit a quantitatively similar isotope effect, but beyond this the dissociation line in particular occurs at slightly lower pressures than the Widom line.

We have shown the existence of a strong isotope effect of several hundred Kelvins in the liquid-liquid transition in hydrogen, with the transformation occurring at lower temperatures and pressures in hydrogen than deuterium, and much lower than in previous work using classical nuclei. There is no such effect at the melt line, nor (by definition) in Born-Oppenheimer dynamics. So we can confidently ascribe it to the different zero-point energy of hydrogen and deuterium vibrations; the difference in these  \( \frac{1}{2}\hbar(\omega_{H}-\omega_{D}) \)  has the appropriate order of magnitude of hundreds of Kelvin.

The strong dependence of the calculated LLPT line on the exchange-correlation functional makes it impossible to confidently state the precise location of the LLPT. Moreover, above the critical point the transition becomes a crossover and the associated Widom lines depend on the precise quantity being measured. In this work, the magnitude of the isotope effect is likely to be more accurate than the exact location of the LLPT line. While the exact location of the boundary will likely remain contentious until experimental results can pin it down more accurately, ab initio PIMD methods are clearly effective in showing that an isotope effect is indeed present the LLPT. They also emphasize that experiments on deuterium cannot be used as a proxy for the hydrogen phase diagram.

It is well known the quantum effects are only important at "low" temperatures. We show here that low temperature must be interpreted in terms of the relevant quantum energy scales, which for molecular vibration modes can mean shifts in phase boundaries of hundreds of Kelvins at temperatures of thousands of Kelvins. These conclusions have general applicability to other molecular-dissociation transitions, such as nitrogen and superionic ammonia and water \( ^{[9, 44-46]} \) , meaning that experiments on deuterated samples will significantly overestimate the transition pressures and temperatures compared with the natural material.

## ACKNOWLEDGEMENTS

We acknowledge the support of the ERC grant HECATE and studentship funding from EPSRC under grant ref EP/L015110/1. This work used the Cirrus UK National Tier-2 HPC Service at EPCC (http://www.cirrus.ac.uk) funded by the University of Edinburgh and EPSRC (EP/P020267/1). We are grateful for computational support from the UK national high
 
![](./images/867751696124609123_7.jpg)

![](./images/867751696124609123_8.jpg)

Fig. 5 Summary of the results obtained in this work. (a) Location of the phase boundary as established from peaks in the compressibility. The isotope effect is largest in magnitude at lower temperatures. Melting curve \( ^{[42]} \)  and the likely continuation of the melting line beyond the I-IV-liquid triple point \( ^{[43]} \)  shows where the LLPT phase line is expected to rejoin the solid phase lines. (b) Comparison of the compressibility phase line to the dissociation curve established from peaks in the gradient of the dimer fraction and the metallization line along with MD runs using classical H nuclei, all using BLYP. Additional NPT runs using PBE and vdw-DF functionals at 1000 K are also shown. Snapshots on either side of the transition are PIMD runs of  \( H_{2} \)  at 1000 K using BLYP, for 100 GPa and 250 GPa, with bonds highlighted in red.

performance computing service, ARCHER, for which access was obtained via the UKCP consortium and funded by EPSRC grant ref EP/P022790/1.

## REFERENCES

[1] R. P. Dias and I. F. Silvera, Science 355, 715 (2017).

[2] P. Loubeyre, F. Occelli, and P. Dumas, Nature 577, 631 (2020).

[3] V. Dzyabura, M. Zaghoo, and I. F. Silvera, Proceedings of the National Academy of Sciences 110, 8040 (2013).

[4] M. Zaghoo, A. Salamat, and I. F. Silvera, Phys. Rev. B 93, 155128 (2016).

[5] M. Zaghoo, R. J. Husband, and I. F. Silvera, Phys. Rev. B 98, 104102 (2018).

[6] S. Jiang, N. Holtgrewe, Z. M. Geballe, S. S. Lobanov, M. F. Mahmood, R. S. McWilliams, and A. F. Goncharov, Advanced Science 7, 1901668 (2020).

[7] S. T. Weir, A. C. Mitchell, and W. J. Nellis, Phys. Rev. Letters 76, 1860 (1996).

[8] M. Knudson, M. Desjarlais, A. Becker, R. Lemke, K. Cochrane, M. Savage, D. Bliss, T. Mattsson, and R. Redmer, Science 348, 1455 (2015).

[9] P. M. Celliers, M. Millot, S. Brygoo, R. S. McWilliams, D. E. Fratanduono, J. R. Rygg, A. F. Goncharov, P. Loubeyre, J. H. Eggert, J. L. Peterson, N. B. Meezan, S. Le Pape, G. W. Collins, R. Jeanloz, and R. J. Hemley, Science 361, 677 (2018).

[10] A. Becker, N. Nettelmann, U. Kramm, W. Lorenzen, M. French, and R. Redmer, Proceedings of the International Astronomical Union 6, 473 (2010).

[11] D. C. Swift, J. Eggert, D. G. Hicks, S. Hamel, K. Caspersen, E. Schwegler, G. W. Collins, N. Nettelmann, and G. Ackland, The Astrophysical Journal 744, 59 (2011).

[12] G. Chabrier, S. Mazevet, and F. Soubiran, The Astrophysical Journal 872, 51 (2019).

[13] J. M. McMahon, M. A. Morales, C. Pierleoni, and D. M. Ceperley, Reviews of modern physics 84, 1607 (2012).

[14] S. Scandolo, Proceedings of the National Academy of Sciences 100, 3051 (2003).

[15] B. Holst, R. Redmer, and M. P. Desjarlais, Physical Review B 77, 184201 (2008).

[16] W. Lorenzen, B. Holst, and R. Redmer, Phys. Rev. B 82, 195107 (2010).

[17] M. A. Morales, J. M. McMahon, C. Pierleoni, and D. M. Ceperley, Phys. Rev. Letters 110, 065702 (2013).

[18] H. Y. Geng, Q. Wu, M. Marqués, and G. J. Ackland, Phys. Rev. B 100, 134109 (2019).

[19] M. A. Morales, C. Pierleoni, E. Schwegler, and D. Ceperley, Proceedings of the National Academy of Sciences 107, 12799 (2010).

[20] G. Mazzola and S. Sorella, Phys. Rev. Letters 114, 105701 (2015).

[21] C. Pierleoni, M. A. Morales, G. Rillo, M. Holzmann, and D. M. Ceperley, Proceedings of the National Academy of Sciences 113, 4953 (2016).

[22] G. Rillo, M. A. Morales, D. M. Ceperley, and C. Pierleoni, Proceedings of the National Academy of Sciences 116, 9770 (2019).

[23] B. Cheng, G. Mazzola, C. J. Pickard, and M. Ceriotti, Nature 585, 217 (2020).
 

[24] X.-D. Liu, P. Dalladay-Simpson, R. T. Howie, H.-C. Zhang, W. Xu, J. Binns, G. J. Ackland, H.-K. Mao, and E. Gregoryanz, Proceedings of the National Academy of Sciences (2020).

[25] K. K. Irikura, Journal of Physical and Chemical Reference Data 36, 389 (2007).

[26] See Supplemental Material at [url] for discussion of previous studies of the LLPT, a tabular comparison of major existing ab initio studies and their simulation parameters, details on the computational methods employed, PIMD bead convergence, sample radial distribution functions, sample mean square displacements, band gaps, PV equations of state, and additional simulations using other exchange-correlation functionals, including Refs. [5, 6, 8, 16–18, 21, 23, 28–35, 37, 39, 47–65].

[27] I. B. Magdau, F. Balm, and G. J. Ackland, Journal of Physics: Conference Series 950, 042059 (2017).

[28] M. A. Morales, C. Pierleoni, and D. M. Ceperley, Physical Review E 81, 021202 (2010).

[29] G. J. Ackland and I. B. Magdau, Cogent Physics 2, 1049477 (2015).

[30] S. Azadi and G. J. Ackland, Physical Chemistry Chemical Physics 19, 21829 (2017).

[31] A. D. Becke, Physical review A 38, 3098 (1988).

[32] C. Lee, W. Yang, and R. G. Parr, Physical review B 37, 785 (1988).

[33] R. C. Clay III, J. Mcminis, J. M. McMahon, C. Pierleoni, D. M. Ceperley, and M. A. Morales, Phys. Rev. B 89, 184106 (2014).

[34] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Letters 77, 3865 (1996).

[35] M. Dion, H. Rydberg, E. Schröder, D. C. Langreth, and B. I. Lundqvist, Physical review letters 92, 246401 (2004).

[36] D. Marx and J. Hutter, Ab Initio Molecular Dynamics: Basic Theory and Advanced Methods (Cambridge University Press, New York, 2009).

[37] K. R. Glaesemann and L. E. Fried, The Journal of chemical physics 117, 3020 (2002).

[38] I. B. Magdau, M. Marques, B. Borgulya, and G. J. Ackland, Phys. Rev. B 95, 094107 (2017).

[39] L. Calderin, V. V. Karasiev, and S. B. Trickey, Computer Physics Communications 221, 118 (2017).

[40] W. J. Nellis, S. T. Weir, and A. C. Mitchell, Physical Review B 59, 3434 (1999).

[41] M. Zaghoo and I. F. Silvera, Proceedings of the National Academy of Sciences 114, 11873 (2017).

[42] R. T. Howie, P. Dalladay-Simpson, and E. Gregoryanz, Nature materials 14, 495 (2015).

[43] P. Dalladay-Simpson, R. T. Howie, and E. Gregoryanz, Nature 529, 63 (2016).

[44] M. Millot, F. Coppari, J. R. Rygg, A. C. Barrios, S. Hamel, D. C. Swift, and J. H. Eggert, Nature 569, 251 (2019).

[45] S. Jiang, N. Holtgrewe, S. S. Lobanov, F. Su, M. F. Mahmood, R. S. McWilliams, and A. F. Goncharov, Nature communications 9, 1 (2018).

[46] V. N. Robinson and A. Hermann, Journal of Physics: Condensed Matter 32, 184004 (2020).

[47] S. Biermann, D. Hohl, and D. Marx, Journal of Low Temperature Physics 110, 97 (1998).

[48] S. Biermann, D. Hohl, and D. Marx, Solid state communications 108, 337 (1998).

[49] H. Y. Geng, H. X. Song, J. Li, and Q. Wu, Journal of Applied Physics 111, 063510 (2012).

[50] H. Y. Geng, R. Hoffmann, and Q. Wu, Phys. Rev. B 92, 104103 (2015).

[51] I. B. Magdau and G. J. Ackland, arXiv preprint arXiv:1511.05173 (2015).

[52] I. B. Magdau and G. J. Ackland, in Journal of Physics: Conference Series, Vol. 950 (IOP Publishing, 2017) p. 042058.

[53] B. Lu, D. Kang, D. Wang, T. Gao, and J. Dai, Chinese Physics Letters 36, 103102 (2019).

[54] J. Hinz, V. V. Karasiev, S. Hu, M. Zaghoo, D. Mejía-Rodríguez, S. Trickey, and L. Calderín, Phys. Rev. Research 2, 032065R (2020).

[55] C. Tian, F. Liu, H. Yuan, H. Chen, and Y. Gan, Journal of Physics: Condensed Matter 33, 015401 (2020).

[56] V. Kapil, M. Rossi, O. Marsalek, R. Petraglia, Y. Litman, T. Spura, B. Cheng, A. Cuzzocrea, R. H. Meißner, D. M. Wilkins, B. A. Helfrecht, P. Juda, S. P. Bienvenue, W. Fang, J. Kessler, I. Poltavsky, S. Vandenbrande, J. Wieme, C. Corminboeuf, T. D. Kühne, D. E. Manolopoulos, T. E. Markland, J. O. Richardson, A. Tkatchenko, G. A. Tribello, V. V. Speybroeck, and M. Ceriotti, Computer Physics Communications 236, 214 (2019).

[57] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carnimeo, A. D. Corso, S. de Gironcoli, P. Delugas, R. A. D. Jr, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. O. de-la Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N. Vast, X. Wu, and S. Baroni, Journal of Physics: Condensed Matter 29, 465901 (2017).

[58] A. Baldereschi, Phys. Rev. B 7, 5212 (1973).

[59] S. Azadi and W. M. C. Foulkes, Phys. Rev. B 88, 014115 (2013).

[60] M. Ceriotti, M. Parrinello, T. E. Markland, and D. E. Manolopoulos, The Journal of Chemical Physics 133, 124104 (2010).

[61] M. Ceriotti, J. More, and D. E. Manolopoulos, Computer Physics Communications 185, 1019 (2014).

[62] D. J. Chadi and M. L. Cohen, Physical Review B 8, 5747 (1973).

[63] D. Hamann, M. Schlüter, and C. Chiang, Physical Review Letters 43, 1494 (1979).

[64] K. Laasonen, A. Pasquarello, R. Car, C. Lee, and D. Vanderbilt, Physical Review B 47, 10142 (1993).

[65] L. Wang, M. Ceriotti, and T. E. Markland, The Journal of chemical physics 141, 104502 (2014).
 

# Supplementary materials for "Isotope quantum effects in the metallization transition in liquid hydrogen"

Sebastiaan van de Bund, \( ^{1} \)  Heather Wiebe \( ^{1} \)   \( \& \)  Graeme J. Ackland \( ^{1} \) 

1. School of Physics & Astronomy, The University of Edinburgh, Edinburgh, EH9 3FD, United Kingdom.

## Previous study of the LLPT

There have been numerous other studies of the LLPT, several of which were published after this manuscript was submitted. Determining the isotope effects was not the primary purpose of any of these papers, and all of these studies have significant problems which make them unsuitable for this purpose. The most obvious problem is failure to include nuclear quantum effects, which means there is no isotope effect on the phase diagram \( ^{[1, 2, 3]} \) . A more subtle problem identified by Cheng et al. \( ^{[4]} \)  is that the molecular liquid equilibrates slowly and freezes in small system sizes. Diffusivity is easily measured in molecular dynamics, and so we disregard studies which do not present this, and are smaller or shorter than the threshold identified by Cheng et al. A final problem is that  \( \Gamma \)  point simulations give rise to spurious "polyhydrogen" liquids, a problem which recurs frequently in the literature and preprints  \( [5, 6, 7, 8, 9, 10] \) .

Experimental studies are similarly problematic - there is a large spread in the reported transitions, and above the critical point, the LLPT line is not even uniquely defined. One cannot sensibly compare results from different types of experiment for hydrogen and deuterium, and hope to extract the isotope effect. Two recent studies \( ^{[11, 12]} \)  have treated both materials with the same approach, but even then dealing with different samples.

The scatter of phase line due to exchange correlation functional is a further problem. Previous work has shown that BLYP is the most reliable function for metallisation in hydrogen, but even so a large uncertainty remains \( ^{[13, 14, 15]} \) . We do not claim to solve this here, since our focus is on the isotope shift which is due to nuclear quantum effects, rather than the functional. In Supplementary Table 1, we summarise the previous work, demonstrating why it is unsuitable for determining the isotope effect.

## Methods

The Path Integral technique incorporates NQE by mapping the quantum nucleus onto a set of P classical replicas, termed "beads", which interact with each other through harmonic springs. Here, classical and Path Integral Molecular Dynamics simulations were performed using the i-Pi \( ^{[22]} \)  universal force engine in conjunction with Quantum Espresso. \( ^{[23]} \)  PIMD simulations consisted of 180 molecules of  \( H_{2} \)  or  \( D_{2} \)  (360 atoms) in a cubic periodic box with an electronic kinetic energy cutoff of 35 Ry and 234 bands. For k-point sampling, the Baldereschi mean value point \( ^{[24]} \)  was chosen due to the tendency of hydrogen to form spurious polymeric structures when sampling is done at the  \( \Gamma \)  point. \( ^{[9]} \)  The widely-used PBE \( ^{[25]} \)  functional is known to
 

Supplementary Table 1. Table listing major ab initio MD studies on the LLPT boundary (MLP = machine-learning potential), comparing the inconsistent range of both simulation parameters and predicted transition pressures. Listed transition pressures were calculated at 1500 K. Our results provide a comprehensive look at both hydrogen and deuterium with a sufficiently large system size and an appropriate choice of k-points.

<table><tr><td>Authors</td><td>XC-functional</td><td>Method</td><td>H2P T (GPa)</td><td>D2P T (G Pa)</td><td>System size</td><td>k-points</td></tr><tr><td rowspan="3">Lu et al.[16]</td><td>PBE0++rVV10</td><td></td><td>161</td><td>-</td><td></td><td></td></tr><tr><td>rVV10</td><td>PIMD</td><td>182</td><td>-</td><td>256</td><td>Γ</td></tr><tr><td>vdw-DF1</td><td></td><td>189</td><td>-</td><td></td><td></td></tr><tr><td>Hinz et al.[17]</td><td>SCAN+rVV10</td><td>PIMD (+MD)</td><td>~110</td><td>~130</td><td>256</td><td>Γ</td></tr><tr><td>Knudson et al.[18]</td><td>vdW-DF1</td><td>PIMD (+MD)</td><td>-</td><td>203</td><td>256</td><td>Baldereschi</td></tr><tr><td></td><td>vdW-DF2</td><td></td><td>-</td><td>292</td><td></td><td></td></tr><tr><td>Tian et al.[19]</td><td>PBE</td><td>MD</td><td>127</td><td>-</td><td>64</td><td>3x3x3</td></tr><tr><td>Lorenzen et al.[20]</td><td>PBE</td><td>MD</td><td>140</td><td>-</td><td>512</td><td>Baldereschi</td></tr><tr><td rowspan="2">Geng et al.[21]</td><td>PBE</td><td>MD</td><td>124</td><td>-</td><td>500-3456</td><td>4x4x4 and Baldereschi</td></tr><tr><td>revPBE-vdW</td><td></td><td>220</td><td>-</td><td></td><td></td></tr><tr><td>Cheng et al.[4]</td><td>PBE, BLYP, QMC</td><td>MLP-MD</td><td>-</td><td>-</td><td>128 (1728)</td><td>N/A</td></tr><tr><td>This work</td><td>BLYP</td><td>PIMD (+MD)</td><td>165</td><td>183</td><td>360</td><td>Baldereschi</td></tr></table>

erroneously favour metallization in hydrogen and so in this work the BLYP functional \( ^{[26, 27]} \)  was used as it has been shown to give a better agreement with experiment for the molecular phases of hydrogen \( ^{[28]} \) .

Trajectories consisted of an initial NPT equilibration period of 500 steps, followed by 2000 steps in the NVT ensemble which was then used for data analysis. A timestep of 0.5 fs was used in all cases. Temperature was kept constant using the stochastic PILE_L thermostat \( ^{[29]} \)  with a relaxation time of 10 fs, and for the NPT equilibration runs a constant pressure was maintained using the isotropic stochastic barostat \( ^{[30]} \)  as implemented in i-PI, with a relaxation time of 100 fs. Five different isotherms were used to locate the LLPT: 1000, 1250, 1500, 2000 and 2500 K. PIMD trajectories were obtained for hydrogen with 12 beads at 1000 and 1250 K, 8 beads at 1500 K and 2000 K and 4 beads at 2500 K. For deuterium 8 beads were used at 1000 and 1250 K, 4 beads at 1500 K, 2000 K and 2500 K. Convergence details are given in the Supplementary Materials below.

Classical simulations were performed by setting the number of beads to 1. These used identical parameters as above, but only considering four isotherms 1000 K, 1500 K, 2000 K and 2500 K using 1000 steps in the NVT ensemble.

Heat capacities were calculated using the centroid virial estimator, which provides improved convergence over the primitive energy estimator and is given by \( ^{[31]} \) :

 \[ \frac{C_{V}^{CV}}{k_{B}\beta^{2}}=\langle\epsilon_{T}\epsilon_{CV}\rangle-\langle\epsilon_{CV}\rangle^{2}-\frac{3N}{2\beta^{2}}, \quad (1) \] 

for N particles, where  \( \epsilon_{T} \)  and  \( \epsilon_{CV} \)  are the primitive energy and centroid virial energy estimators respectively. Because of its slower convergence, the primitive energy estimator was shifted by a small constant such that the average of the primitive and centroid virial energy estimators were equal.

The conductivities were calculated in the Kubo-Greenwood formalism using the KGEC code \( ^{[32]} \) . Averages we were calculated using 20 snapshots of each centroid trajectory. A generalisation of the Baldereschi point was used to sample the Brillouin zone, following the approach of Chadi and Cohen \( ^{[33]} \) , to obtain 4 k-points in the SCF calculation. Convergence for 10 independent snapshots at 1000 K and 250 GPa are shown in Fig. 1. The Chadi-Cohen grid is more consistent with previous calculations, and converges the average conductivity faster.
 
![](./images/867751696124609123_9.jpg)

![](./images/867751696124609123_10.jpg)

Supplementary Figure 1. Convergence of k point grid sizes in the SCF calculations used to calculate conductivities.

than a Monkhorst-Pack grid. To evaluate the Kubo-Greenwood conductivity, a width of 1 eV for the Lorentzian used by KGEC was found to give consistent results. Note that these calculations were performed using a local norm-conserving pseudopotential \( ^{[34]} \)  rather than an ultrasoft pseudopotential \( ^{}[35] \)  in the main trajectories.

## PIMD convergence

The number of beads P required to converge NQE is inversely related to temperature, and so we performed convergence tests to determine the optimum P for each isotherm. The goal was to maintain accuracy of the calculated NQE with a minimum of computational effort. For this, the total energy of the system was calculated as a function of P at 100 GPa for each temperature, and the optimal P was chosen as the beginning of the plateau. A sample convergence plot is shown in Fig. 2. The optimal P for hydrogen was chosen to be 12 for 1000 K and 1250 K, 8 for 1500 K and 2000 K, and 4 for 2500 K. For deuterium, where quantum effects are slightly weaker, fewer beads were required for convergence. 8 beads were used for deuterium at 1000 and 1250 K, and 4 beads at 1500 K, 2000 K and 2500 K. Note that convergence is slower at lower temperature, but is not significantly affected by pressure, as illustrated in Fig. 3.

## Radial distribution functions

The first peak of the radial distribution function (RDF), which corresponds to the covalent H-H bond length, provides an indicator of the amount of  \( H_{2} \)  molecules present in the system. Here we show sample RDFs for  \( H_{2} \)  at 1000 K which illustrate the transition between molecular and atomic phases.
 
![](./images/867751696124609123_11.jpg)

![](./images/867751696124609123_12.jpg)

Supplementary Figure 2. Convergence of total energy (potential plus kinetic) with respect to number of PIMD beads for liquid hydrogen (left) and liquid deuterium (right) at 100 GPa, 1250 K. The optimal P was chosen to be at the onset of the plateau, 12 for hydrogen and 8 for deuterium in this case.

![](./images/867751696124609123_13.jpg)

![](./images/867751696124609123_14.jpg)

Supplementary Figure 3. Convergence of total energy (potential plus kinetic) with respect to number of PIMD beads for liquid metallic hydrogen at 100GPa and 250 GPa, 1000 K.
 
![](./images/867751696124609123_15.jpg)

Supplementary Figure 4. Radial distribution functions for  \( H_{2} \)  at 1000 K as a function of pressure. The black and blue lines correspond to the molecular and atomic phases at 150 GPa and 250 GPa, respectively. The yellow dashed line represents the RDF of the solid phase I structure at 150 GPa. The transition between molecular and atomic phases can be clearly seen by the dramatic drop in the first peak of the RDF.

## Evidence of liquid phase

We watched animations of our trajectories to ensure that solidification was not observed. This is further evidenced by the mean squared displacements shown in Fig. 5 and 6. No solidification, layering, chain formation or other unphysical behaviour was observed in any of our classical or PIMD simulations above the melt line in Fig. 5. In the classical simulation at 600 K we observe a non-diffusing, glasslike state which we attribute to cooling below the melt line: this state can not be easily distinguished from the liquid using RDF data alone.

## Equation of state

Fig. 7 shows the PV equation of state for both isotopes. The first order phase transition is evidenced by a plateau or anomaly in the pressure, which is small and difficult to see in the equation of state. To emphasize it, we also plot the difference from a Vinet equation of state fitted to the molecular phase at 1000 K: this show a distinct step in the volume at 1000K and at 1250 K in deuterium. The situation is more equivocal for higher temperature, with a distinct change in PV slope across several densities - this suggests a crossover rather than a discontinuous phase transition.

The  \( H_{2} \)  volume change at 1000 K is  \( 0.025 \, \AA^{3}/atom \) . From the equation of state we see a Clapeyron slope of approximately 8 K/GPa, from which we can estimate an entropy change around  \( 0.5k_{B}/atom \) .

## Band gap

In addition to conductivities, band gap closure was also calculated as an additional measure of metallization. These were obtained from the electronic density of states using 20 snapshots
 
![](./images/867751696124609123_16.jpg)

![](./images/867751696124609123_17.jpg)

Supplementary Figure 5. Mean squared displacement from classical-ion simulations using the BLYP functional and 256 atoms. MSD is calculated from ensemble averages of all atoms and all start times,  \( \tau \) :  \( MSD(t) = \langle(\mathbf{r}(\tau) - \mathbf{r}(\tau - t)\rangle \) . These calculations are run in the NVT ensemble at 2.005 Å \( ^{3} \) /atom which corresponds to about 140 GPa. There is an initial steep increase as the molecules do hindered rotation, even in the solid phase. In the long-time limit, all the runs except 600 K show linear MSD with non-zero slope, and no evidence that diffusion is driven by specific rare events. We conclude that all simulations run above the melt curve are liquid-like. 600K is below the melt curve, but the simulation was initiated from a 1000 K run: the sample appears disordered. 950 K goes through a kind of plateau, which may suggest its getting stuck in a glassy phase: the simulation was restarted from a configuration near the start of this glassy behavior, hence two red lines are shown. Everything near the LLPT region is a good flowing liquid.

![](./images/867751696124609123_18.jpg)

Supplementary Figure 6. Mean squared displacement from PIMD simulations of  \( H_{2} \)  at 1000 K. The yellow dashed line represents the solid phase I at 150 GPa, which shows the expected plateau. The black and blue lines represent the molecular phase at 150 GPa, and the atomic phase at 250 GPa. Both curves show a linear MSD in the long-time limit, confirming that these simulations are liquid-like.
 
![](./images/867751696124609123_19.jpg)

![](./images/867751696124609123_20.jpg)

Supplementary Figure 7. Pressure-volume curves for hydrogen and deuterium. Insets are the same curves with the volume subtracted as obtained from a specific Vinet EoS fit to the molecular low pressure phase at 1000 K as a reference curve in order to emphasize the volume discontinuity at low temperatures.
 

of the centroid trajectory. These results are shown in Fig. 8, showing a similar isotope effect to previous results. They are also in agreement with conductivity calculations presented in the main text.

![](./images/867751696124609123_21.jpg)

Supplementary Figure 8. Gap at the Fermi level in the electronic density of states at various pressures, showing the closure of the gap associated with metallization.

## Comparison of exchange-correlation functionals

While the choice of exchange-correlation functional has a drastic effect on the location of the LLPT, the isotope effect is not found to be as significantly affected. Fig. 9 shows the calculated isothermal compressibility of a set of NPT runs of at least 0.5 ps using the PBE \( ^{[25]} \)  and vdw-DF \( ^{[36]} \)  functionals performed at 1000 K, which is where the isotope effect is expected to be strongest. The results are fitted using an exponential background and Gaussian function to obtain the location of the transition using identical methods as for the main results.

The resulting isotope shift on the transition pressures from Fig. 9 are found to be  \( \Delta P_{PBE} = 26 \)  GPa and  \( \Delta P_{vdw-DF} = 30 \)  GPa, compared to the main result of  \( \Delta P_{BLYP} = 27 \)  GPa. The spread is thus only a few GPa. Given the shorter length of these simulations and the spacing of the pressures considered, this supports the notion that the isotope effect not only exists even

![](./images/867751696124609123_22.jpg)

![](./images/867751696124609123_23.jpg)

Supplementary Figure 9. Isothermal compressibility with fits for PBE and vdw-DF exchange-correlation functionals, showing a similar isotopic pressure shift as for BLYP.
 

when using other functionals, other choices also yield a similar magnitude. The main effect of changing functional is therefore to significantly shift the location of the phase boundaries in PT space.

This contrasts with the case for other systems where NQE are significant such as liquid  \( H_{2}O \) . For such a system, the choice of functional can significantly affect the degree to which hydrogen is delocalised, thus creating marked differences in the hydrogen bond network \( ^{[37]} \) . In contrast, intermolecular interactions in liquid hydrogen are relatively weak: the transition is dominated by local energetics of the two distinct but interconvertible species, hydrogen atoms and hydrogen molecules \( ^{[21]} \) .

The choice of functional will feasibly lead to dissociation energies that differ both from each other, and from the true value. Regardless, these results suggest that any such deviations, including differences in the potential energy surface, will largely cancel out. This leaves the difference in ZPE as the main contribution to the magnitude of the isotopic shift, which is well-described in the PIMD formalism.
 

## References

[1] Miguel A Morales, Carlo Pierleoni, and David M Ceperley. Equation of state of metallic hydrogen from coupled electron-ion monte carlo simulations. Physical Review E, 81(2):021202, 2010.

[2] Miguel A Morales, Jeffrey M McMahon, Carlo Pierleoni, and David M Ceperley. Nuclear quantum effects and nonlocal exchange-correlation functionals applied to liquid hydrogen at high pressure. Phys. Rev. Letters, 110(6):065702, 2013.

[3] Carlo Pierleoni, Miguel A. Morales, Giovanni Rillo, Markus Holzmann, and David M. Ceperley. Liquid–liquid phase transition in hydrogen by coupled electron–ion monte carlo simulations. Proceedings of the National Academy of Sciences, 113(18):4953–4957, 2016.

[4] Bingqing Cheng, Guglielmo Mazzola, Chris J Pickard, and Michele Ceriotti. Evidence for supercritical behaviour of high-pressure liquid hydrogen. Nature, 585(7824):217–220, 2020.

[5] S Biermann, D Hohl, and D Marx. Proton quantum effects in high pressure hydrogen. Journal of Low Temperature Physics, 110(1-2):97–102, 1998.

[6] S Biermann, D Hohl, and D Marx. Quantum effects in solid hydrogen at ultra-high pressure. Solid state communications, 108(6):337–341, 1998.

[7] Hua Y Geng, Hong X Song, JF Li, and Q Wu. High-pressure behavior of dense hydrogen up to 3.5 tpa from density functional theory calculations. Journal of Applied Physics, 111(6):063510, 2012.

[8] Hua Y Geng, R Hoffmann, and Q Wu. Lattice stability and high-pressure melting mechanism of dense hydrogen up to 1.5 tpa. Phys. Rev. B, 92(10):104103, 2015.

[9] Ioan B Magdău and Graeme J Ackland. Charge density wave in hydrogen at high pressure. arXiv preprint arXiv:1511.05173, 2015.

[10] Ioan B Magdău and Graeme J Ackland. Charge density wave in hydrogen at high pressure. In Journal of Physics: Conference Series, volume 950, page 042058. IOP Publishing, 2017.

[11] Mohamed Zaghoo, Rachel J. Husband, and Isaac F. Silvera. Striking isotope effect on the metallization phase lines of liquid hydrogen and deuterium. Phys. Rev. B, 98:104102, Sep 2018.

[12] Shuqing Jiang, Nicholas Holtgrewe, Zachary M. Geballe, Sergey S. Lobanov, Mohammad F. Mahmood, R. Stewart McWilliams, and Alexander F. Goncharov. A spectroscopic study of the insulator–metal transition in liquid hydrogen and deuterium. Advanced Science, 7(2):1901668, 2020.

[13] Raymond C Clay III, Jeremy Mcminis, Jeffrey M McMahon, Carlo Pierleoni, David M Ceperley, and Miguel A Morales. Benchmarking exchange-correlation functionals for hydrogen at high pressures using quantum monte carlo. Phys. Rev. B, 89(18):184106, 2014.

[14] Sam Azadi and Graeme J Ackland. The role of van der waals and exchange interactions in high-pressure solid hydrogen. Physical Chemistry Chemical Physics, 19(32):21829–21839, 2017.

[15] Graeme J Ackland and Ioan B Magdău. Appraisal of the realistic accuracy of molecular dynamics of high-pressure hydrogen. Cogent Physics, 2(1):1049477, 2015.
 

[16] Binbin Lu, Dongdong Kang, Dan Wang, Tianyu Gao, and Jiayu Dai. Towards the same line of liquid–liquid phase transition of dense hydrogen from various theoretical predictions. Chinese Physics Letters, 36(10):103102, 2019.

[17] Joshua Hinz, Valentin V Karasiev, SX Hu, Mohamed Zaghoo, Daniel Mejía-Rodríguez, SB Trickey, and L Calderín. Fully consistent density functional theory determination of the insulator-metal transition boundary in warm dense hydrogen. Phys. Rev. Research, 2:032065R, 2020.

[18] MD Knudson, MP Desjarlais, Andeas Becker, RW Lemke, KR Cochrane, ME Savage, DE Bliss, TR Mattsson, and Ronald Redmer. Direct observation of an abrupt insulator-to-metal transition in dense liquid deuterium. Science, 348(6242):1455–1460, 2015.

[19] Chunling Tian, Fusheng Liu, Hongkuan Yuan, Hong Chen, and Yundan Gan. First-principles equation of state of liquid hydrogen and dissociative transition. Journal of Physics: Condensed Matter, 33(1):015401, 2020.

[20] Winfried Lorenzen, Bastian Holst, and Ronald Redmer. First-order liquid-liquid phase transition in dense hydrogen. Phys. Rev. B, 82(19):195107, 2010.

[21] Hua Y. Geng, Q. Wu, Miriam Marqués, and Graeme J. Ackland. Thermodynamic anomalies and three distinct liquid-liquid transitions in warm dense liquid hydrogen. Phys. Rev. B, 100:134109, Oct 2019.

[22] Venkat Kapil, Mariana Rossi, Ondrej Marsalek, Riccardo Petraglia, Yair Litman, Thomas Spura, Bingqing Cheng, Alice Cuzzocrea, Robert H. Meißner, David M. Wilkins, Benjamin A. Helfrecht, Przemysław Juda, Sébastien P. Bienvenue, Wei Fang, Jan Kessler, Igor Poltavsky, Steven Vandenbrande, Jelle Wieme, Clemence Corminboeuf, Thomas D. Kühne, David E. Manolopoulos, Thomas E. Markland, Jeremy O. Richardson, Alexandre Tkatchenko, Gareth A. Tribello, Veronique Van Speybroeck, and Michele Ceriotti. i-pi 2.0: A universal force engine for advanced molecular simulations. Computer Physics Communications, 236:214–223, 2019.

[23] P Giannozzi, O Andreussi, T Brumme, O Bunau, M Buongiorno Nardelli, M Calandra, R Car, C Cavazzoni, D Ceresoli, M Cococcioni, N Colonna, I Carnimeo, A Dal Corso, S de Gironcoli, P Delugas, R A DiStasio Jr, A Ferretti, A Floris, G Fratesi, G Fugallo, R Gebauer, U Gerstmann, F Giustino, T Gorni, J Jia, M Kawamura, H-Y Ko, A Kokalj, E Kükübenli, M Lazzeri, M Marsili, N Marzari, F Mauri, N L Nguyen, H-V Nguyen, A Otero de-la Roza, L Paulatto, S Poncé, D Rocca, R Sabatini, B Santra, M Schlipf, A P Seitsonen, A Smogunov, I Timrov, T Thonhauser, P Umari, N Vast, X Wu, and S Baroni. Advanced capabilities for materials modelling with quantum espresso. Journal of Physics: Condensed Matter, 29(46):465901, 2017.

[24] A. Baldereschi. Mean-value point in the brillouin zone. Phys. Rev. B, 7:5212–5215, Jun 1973.

[25] John P Perdew, Kieron Burke, and Matthias Ernzerhof. Generalized gradient approximation made simple. Phys. Rev. Letters, 77(18):3865, 1996.

[26] Axel D Becke. Density-functional exchange-energy approximation with correct asymptotic behavior. Physical review A, 38(6):3098, 1988.

[27] Chengethe Lee, Weitao Yang, and Robert G Parr. Development of the colle-salvetti correlation-energy formula into a functional of the electron density. Physical review B, 37(2):785, 1988.
 

[28] Sam Azadi and W M C Foulkes. Fate of density functional theory in the study of high-pressure solid hydrogen. Phys. Rev. B, 88(1):014115, 2013.

[29] Michele Ceriotti, Michele Parrinello, Thomas E. Markland, and David E. Manolopoulos. Efficient stochastic thermostatting of path integral molecular dynamics. The Journal of Chemical Physics, 133(12):124104, 2010.

[30] Michele Ceriotti, Joshua More, and David E. Manolopoulos. i-pi: A python interface for ab initio path integral molecular dynamics simulations. Computer Physics Communications, 185(3):1019–1026, 2014.

[31] Kurt R Glaesemann and Laurence E Fried. Improved heat capacity estimator for path integral simulations. The Journal of chemical physics, 117(7):3020–3026, 2002.

[32] Lucas Calderin, Valentin V Karasiev, and Samuel B Trickey. Kubo–greenwood electrical conductivity formulation and implementation for projector augmented wave datasets. Computer Physics Communications, 221:118–142, 2017.

[33] D Jetal Chadi and Marvin L Cohen. Special points in the brillouin zone. Physical Review B, 8(12):5747, 1973.

[34] DR Hamann, M Schlüter, and C Chiang. Norm-conserving pseudopotentials. Physical Review Letters, 43(20):1494, 1979.

[35] Kari Laasonen, Alfredo Pasquarello, Roberto Car, Changyol Lee, and David Vanderbilt. Car-parrinello molecular dynamics with vanderbilt ultrasoft pseudopotentials. Physical Review B, 47(16):10142, 1993.

[36] Max Dion, Henrik Rydberg, Elsebeth Schröder, David C Langreth, and Bengt I Lundqvist. Van der waals density functional for general geometries. Physical review letters, 92(24):246401, 2004.

[37] Lu Wang, Michele Ceriotti, and Thomas E Markland. Quantum fluctuations and isotope effects in ab initio descriptions of water. The Journal of chemical physics, 141(10):104502, 2014.
 
