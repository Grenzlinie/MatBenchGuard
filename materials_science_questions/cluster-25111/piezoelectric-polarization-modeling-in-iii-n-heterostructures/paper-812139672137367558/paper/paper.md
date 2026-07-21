# Effects of polarisation on solar-blind AlGaN UV photodiodes

J.J. Kuek¹, D.L. Pulfrey¹, B.D. Nener¹, J.M. Dell¹, G. Parish³ and U.K. Mishra³

¹ Dept. EEE, University of Western Australia, Crawley, WA 6009, Australia
² Dept. ECE, University of British Columbia, Vancouver, BC V6T1Z4, Canada
³ Dept. ECE, University of California, Santa Barbara, CA 93106, USA

Abstract - The effects of spontaneous and strain induced polarisation, and incomplete dopant ionisation on the spectral responsivity of a Ga-faced p-GaN/i-Al₀.₃₃Ga₀.₆₇N/n- GaN photodiode structure are determined using a commercial finite element modelling package. It is shown that polarisation induced interface charges increase the barrier to carriers generated in the GaN regions of the diode, improving the solar-blindness of the diode by more than three orders of magnitude. In contrast, incomplete dopant ionisation has only a minor effect.

## A. Introduction

AlₓGa₁₋ₓN shows great promise as a material for UV photodetectors as a result of its composition-dependent cutoff wavelength that is tuneable between 200-365 nn. In particular, this allows fabrication of p-i-n UV photodetectors that are insensitive to terrestrial background solar radiation at wavelengths greater than 300 nm. Such solar-blind detectors are important in a number of aerospace applications and obviate the need for bulky and expensive optical filtering components. Current technology requires the GaN layers to be included in the photodiode structure to overcome difficulties in growing an all-Al₀.₃₃Ga₀.₆₇N structure and in making good ohmic p-Al₀.₃₃Ga₀.₆₇N contacts [1].

The use of Al₀.₃₃Ga₀.₆₇N/GaN heterostructures in UV photodiodes leads to piezoelectric polarisation in the strained layer as a result of lattice mismatch. This, combined with spontaneous polarisation caused by imbalanced charge distribution between the cation and anion along the material growth axis, modifies the energy band profile, which is the primary factor controlling current transport within the photodiode. In this paper, the effect of piezoelectric and spontaneous polarisation on the solar responsivity of a Ga-faced p-GaN/i- AlGaN/n-GaN photodiode structure is investigated. In addition, the effect of incomplete dopant ionisation is included.

## B. Model

The structure of the p-GaN/i-Al₀.₃₃Ga₀.₆₇N/n-GaN photodiode is shown in Figure 1(b). The thicknesses of each layer in the p-GaN/i-Al₀.₃₃Ga₀.₆₇N/n-GaN structure are 20 nm, 60 nm and 300 nm, respectively. A one-dimensional model has been implemented using MEDICI [2]. The incoming photon flux is incident onto the exposed top p-GaN layer. The flux at each incident wavelength is kept constant at a low value to maintain low-level injection conditions. Saturation of photocurrent may occur at a high photon flux levels [3] and lead to an erroneously reduced responsivity. The lower limit of the flux depends on numerical accuracy. Simulated photocurrent of a similar photodiode shows a linear dependence on the input flux of a monochrome wavelength for flux density higher than $5×10^{14}$ photons/cm², as in Figure 1(a). At this input flux value, the lowest possible simulated photocurrent at wavelengths just shorter than the cutoff wavelength of GaN, namely 365 nm, is about two orders of magnitude higher than the dark current of $10^{-12}$ A/cm² and at the same time well above the "noise" level of the numerical computation. In this study, we have selected an input photon flux value of $5×10^{14}$ photons/cm²s for this reason.

---

0-7803-6698-0/00/$10.00 ©2000 IEEE

![](./images/812139672137367558_1.jpg)

Fig. 1. (a) Photocurrent density vs input photon flux and (b) room temperature spectral responsivity of a p-GaN/i- $Al_{0.33}Ga_{0.67}N$ /n-GaN diode structure. The simulated responsivity includes incomplete ionisation (II) and polarisation effect (PE) and is obtained at an input photon flux of $5×10^{14}$ photons/cm²s. The z-axis is defined as the direction into the device from the illuminated

The effect of incomplete ionisation is modelled by assuming acceptor and donor ionisation energies of 220 meV and 35 meV, respectively [4]. The donor densities in the n- GaN and unintentionally doped $Al_{0.33}Ga_{0.67}N$ are $5×10^{18} cm^{-3}$ and $1 ×10^{14} cm^{-3}$, respectively, while the acceptor density in the p-GaN, $N_A$, is used as a parameter in the following analysis. In all cases, a valence band offset value of 0.228 eV at the GaN/AIGaN interface is used. Other material properties remain as per previous publications [5, 6].

The combined effects of the spontaneous and piezoelectric polarisation are modelled by introducing the induced sheet charges at the heterointerfaces as well as at the top surface. The amount of charge is calculated from $\sigma = P_{bottom}$-$P_{top}$, where $P_{bottom}$ and $P_{top}$ are the total polarisation of the layer below and above the interface of interest, respectively. Spontaneous polarisation is included for all the layers while only the i-$Al_{0.33}Ga_{0.67}N$ layer is assumed to be strained [7].

### C. Results and Discussion

Simulated room temperature short-circuit current responsivity of the structure is shown in Figure 1(b). Incomplete ionisation for $N_A$ of $1 ×10^{18} cm^{-3}$ results in a small increase in the spectral responsivity even though the field in the depletion region is reduced, leading to a wider tunnelling barrier, as shown in Figure 2(a), and hence lower tunnel current due to generation in the GaN layers. We attribute this increase in the photocurrent to the reduction in the dominating radiative recombination rate described by $R_c = npB$, where $B$ is the probability of radiative recombination given by the van Roosbroeck-Shockley relation [8] and $n$ and $p$ are the electron and hole concentration, respectively. This agrees well with the simulated recombination profiles shown in Figure 2(b). A similar argument can be applied to the decrease in the spectral responsivity obtained, as in Figure 1 (b), for the structure with incompletely ionised $N_A$ of $1 ×10^{20} cm^{-3}$.

The piezoelectric polarisation in the i-$Al_{0.33}Ga_{0.67}N$ layer can be derived using [7]

$$
P_{PE}=2 \frac{a-a_{0}}{a_{0}}\left(e_{31}-e_{33} \frac{C_{13}}{C_{33}}\right) \tag{1}
$$

where $a$ and $a_0$ are in-plane lattice constants of GaN and $Al_{0.33}Ga_{0.67}N$ layers, respectively. The Al mole fraction dependence of the lattice constant, elastic constants $C_{13}(x)$ and $C_{33}(x)$ and the piezoelectric constants $e_{31}(x)$ and $e_{33}(x)$ are found by linear interpolation of the values

![](./images/812139672137367558_2.jpg)

Figure 2: Simulated (a) energy band diagram and (b) recombination rate distribution of the p-GaN/i-
Al₀.₃₃Ga₀.₆₇N/n-GaN photodiode with and without the effect of incomplete ionisation under
illumination at 310 nm. The p-GaN layer is indicated by p.

![](./images/812139672137367558_3.jpg)

Figure 3: The distribution of (a) hole density and (b) electron density for the photodiode at an incident
wavelength of 310 nm.

![](./images/812139672137367558_4.jpg)

Figure 4: (a) Energy band diagram of the photodiode illustrating the band bending effect due to
polarisation; (b) Current responsivity for the case where all polarisation induced charges at the p/i
interface, or, are assumed to be compensated. Also shown is the responsivity data of a p-i-n

for AlN and GaN using values from references [4],[9] and [10]. Including the linearly
interpolated value of spontaneous polarisation in all the layers gives the induced charges of -
$1.8 ×10^{13} \mathrm{~cm}^{-2}$, $-1.86 ×10^{13} \mathrm{~cm}^{-2}$ and $1.86 ×10^{13} \mathrm{~cm}^{-2}$ at the top surface, p/i and i/n interface,
respectively. The inclusion of polarisation charges at the heterointerfaces causes band

bending in the direction that repels minority carriers in the GaN away from the heterojunctions as illustrated in Figure 4(a). This is a favourable outcome for solarblind photodetectors as there is significantly less contribution to the photocurrent between the shortest background solar radiation of 300 nm and the GaN cutoff wavelength of 365 nm. The spectral responsivity of the structure with an $N_A$ of $1 \times 10^{20}\ \text{cm}^{-3}$ including the incomplete ionisation and polarisation effect is also plotted in Figure 1(b).

An interesting observation of the polarisation-modified energy band diagram is the existence of a two-dimensional hole gas (2DHG) at the p-GaN/i-Al$_{0.33}$Ga$_{0.67}$N heterointerface. Hole accumulation layers with sheet densities $4.5 \times 10^{12}\ \text{cm}^{-2}$ at room temperature have been demonstrated in p-GaN/I-AlGaN junctions [11]. However, observation of such phenomena has not been reported for a p-i-n heterojunction photodiodes. A recent proposition by Ibbetson *et al.* suggests the presence of surface donor states in their studies of two-dimensional electron gas (2DEG) on unintentionally doped Al$_x$Ga$_{1-x}$N/GaN heterostructures [12]. If such donor states are also present at the Al$_{0.33}$Ga$_{0.67}$N interface with the p-layer, compensation of the polarisation charges may occur, removing the 2DHG. Supposing all the induced negative charge at the p/i interface is compensated such that $\sigma = 0$, only a slight increase in the responsivity between 300 nm and 365 nm is expected as shown in Figure 4(b). The experimental characteristics of a MOCVD grown front-illuminated p-i-n AlGaN/GaN photodiode [1] is also plotted on this diagram.

### D. Conclusion

Incomplete ionisation and polarisation effects have been incorporated into a finite element model used to simulate Al$_{0.33}$Ga$_{0.67}$N based UV heterojunction photodiodes. Using this model, the peak responsivity of a p-GaN/i-Al$_{0.33}$Ga$_{0.67}$N/n-GaN photodiode to wavelengths shorter than 300 nm is more than 3 orders of magnitude greater than the peak responsivity to the background solar radiation.

### Acknowledgement

The authors wish to thank the Australian Research Council for their support of this work.

### References

[1] E.J. Tarsa, P. Kozodoy, J. Ibbetson, 13.P. Keller, G. Parish and U.K. Mishra, Appl. Phys. Lett. **77** (2000) 316.
[2] Avant! Corporation, Fremont, California.
[3] E. Monroy, M. Hamilton, D. Walker, P. Kung, F.J. SAnchez and M. Razeghi, Appl. Phys. Lett. **74** (1999) 1171.
[4] J.H. Edgar, S. Strite, 1. Akasaki, H. Amano and C. Wetzel. *Gallium Nitride and Related Semiconductors*. INSPEC, London, UK, 1999.
[5] D.L. Pulfrey, J.J. Kuek, B.D. Nener, G. Parish, U.K. Mishra and E. Tarsa, Phys. Stat. Sol. A **176** (1999) 169.
[6] J.J. Kuek, D.L. Pulfrey, B.D. Nener and J.M. Dell, in "SIMC-XI Proceedings" (Canberra, Australia, 2000). Accepted for publication.
[7] O. Ambacher, J. Smart, J.R. Shealy, N.G. Weimann, K. Chu, M. Murphy, W.J. Schaff, L.F. Eastman, R. Dimitrov, L. Wittmer, M. Stutzmann, W. Rieger and J. Hilsenbeck, J. Appl. Phys. **85** (1999) 3222.
[8] J.I. Pankove. "Optical Processes in Semiconductors."Dover Publications, Inc., New York, 1971.
[9] F. Wright, J. Appl. Phys. **82** (1997) 2833.
[10] F. Bernardini, V. Fiorentini and D. Vanderbilt, Phys. Rev. B **56** (1997) R10024.
[11] M.S. Shur, A.D. Bykhovski, R. Gaska, J.W. Yang, G. Simin and M.A. Khan, Appl. Phys. Lett. **76** (2000) 3061.
[12] J.P. Ibbetson, P.T. Fini, K.D. Ness, S.P. DenBaars, J.S. Speck and U.K. Mishra, Appl. Phys. Lett. **77** (2000) 250.

462