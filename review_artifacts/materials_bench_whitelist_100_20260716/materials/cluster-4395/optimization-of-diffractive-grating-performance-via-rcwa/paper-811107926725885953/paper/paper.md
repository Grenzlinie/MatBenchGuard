# Analytical strategy to achieve optimized grating couplers with high precision for both TE and TM polarizations on SOI platform

Roberto Alejandro Larrea-Luzuriaga*, Ana Maria Gutierrez and Pablo Sanchis⁺
Nanophotonics Technology Center, Universitat Politècnica de València, Camino de Vera s/n, 46022 Valencia, Spain
*rolarlu@ntc.upv.es, +pabsanki@ntc.upv.es

Abstract— Diffraction elements are periodic structures that whose performance is based on the light diffraction principle. One application of this structure the are grating couplers which consist in coupling light on or off plane between two propagation means, in our case between a subwavelength waveguide and a single mode fiber optic. Optimized gratings are required to ensure a maximum coupling efficiency. Gratings on silicon on insulator (SOI) platform can be optimized in a few steps analyzing its behavior and linking some structure parameters. But advanced computational calculations and algorithms are used to optimize its design. Period and fill-factor are essential parameters in the optimization. In this paper, several analytical expressions based on the fundamental grating equation are proposed to accurately obtain the optimal period and fill-factor for a polarization transversal-electric and starting with the optimal values for this polarization get analytically the optimal parameters for polarization transversal-magnetic through a relation between both polarizations, avoiding simulation time.

Index Terms— Nanophotonics, gratings, coupling, diffraction.

## I. INTRODUCTION

The information transmission in the communications infrastructure has been increasing in an exponential manner due to development of new technologies and applications for the generation and transmission of contents that each time requires better performance like bigger transmission velocity and bandwidth not only over the communication links of long distance but also in short links like communications between devices, between photonic integrated circuits (PIC) or even inside of them like processing units and high velocity memories. Silicon Photonics is the key technology to solve this need due to its compatibility with CMOS technology fabrication process. Whereby, SOI is presented as a platform of high contrast of refraction index that enables the design of more complex and smaller structures. However, the reduced size of submicron waveguides of a PIC sets the challenge to propagate light to or from a single-mode fiber optic with small losses.

Uniform grating couplers on SOI have been reported with experimental coupling efficiency achieved of about 43% for an operational wavelength of $1.55\mu$m [1]. Other works for the same operational wavelength and TE polarization report a coupling efficiency about 37% with conventional gratings [2]. In this work for an operational wavelength of $1.55\mu$m it has achieved an experimental coupling efficiency about 38.43% for TE polarization using the analytical strategy proposed to obtain the optimal parameters for its design. Moreover, starting with the optimal parameters obtained for TE polarization, it has obtained the TM polarization optimal parameters achieving an experimental coupling efficiency about 34.41%.

## II. GRATING COUPLING DESIGN

Grating couplers are periodic structures that have been amply studied to face the challenge of coupling light with a fiber optic.[3] In this way, several studies have been presented based on Geometric Optics with wave vectors to predict the direction of the diffracted mode but not the amount of power, such it can be seen in the Bragg equation (Eq.1), where $n_{inc}$ is the refractive index of the medium upon which the incident wave is propagating, $\theta_{inc}$ is the angle of the incident wave with the normal of the incident plane, $m$ is the order of diffracted modes, $\Lambda$ is the period of the periodic structure, and $neff_g$ is effective refractive index of the two materials for which the periodic structure is formed. [4]

$$
\Lambda = \frac{m\lambda}{neff_{g}-n_{inc}\sin\theta_{inc}} \tag{1}
$$

With Bragg equation we can design a periodic structure for a coupling out of plane determining the direction of diffraction modes. In our case, grating couplers on a SOI platform are designed on a propagating waveguide, so the incident wave over the surface of the grating is diffracted in several modes that they will be coupled in a propagation mode in the waveguide. Due to the reciprocity theorem we can considered the same results in the coupling from the waveguide to the fiber optic [5]. Grating coupler is a tridimensional structure (Fig 1(a)). However we can study it in a bi-dimensional plane (Fig 1(b)) due that the width of wavelength is much longer that the wavelength of the propagation mode, so we can considered a waveguide with an infinite width. [6]

![](./images/811107926725885953_1.jpg)

Fig. 1 (a) Grating coupler 3D view and (b) cross section with design parameters

The effective refractive index of the grating has high relevance in the optimal period calculation. This parameter has

978-1-5090-1629-7/16/$31.00 ©2016 IEEE

not an exact value and can be interpreted. Some studies with a very good approximation to get the optimal period use the effective refractive index of both parts etched $n_{effep}$ and no-etched $neff_{nep}$ to obtain the refractive index of the grating as the average of both, in this case assuming a fill-factor of 50% [7]. However with this approximation of fill-factor is possible that we cannot get the maximum coupling efficiency.

$$
n_{effg} = \frac{(n_{effep}+neff_{nep})}{2} \tag{2}
$$

Thereby, analyzing the variation of the effective refractive index of a waveguide on a standard SOI wafer, and assuming values as an etching depth of 70nm [8], and a layer of SiO₂ to cover it, it is possible to find a factor to ensure the calculation of the optimal period and fill-factor in an analytical manner avoiding time consuming simulations.

### III. ANALYTICAL METHODOLOGY

With the use of a full vectorial mode solver based on the beam propagation method (BPM), the effective refractive indexes of etched and no-etched part, have been calculated to get the refractive effective index of the grating. The grating is covered with a layer of SiO2 and a fill-factor of 50% has been assumed initially using the Eq. 2. In this way, for different wavelengths and an incidence angle of $10^o$, and initially for a TE polarization, the theoretical period has been obtained for a range of wavelengths between $1.26\mu m$ and $1.60\mu m$ using Eq.1, for a diffraction mode of order 1. After, the obtained period in theoretical form and the fill-factor initially assumed of 50% have been optimized by multiples simulations for each wavelength.

With the theoretical and optimized values of the period for each wavelength before calculated, the effective refractive index of the grating has been obtained using the Eq. 1 for each case. In this manner, the effective refractive index of the grating has been represented as a function of the theoretical and optimized period such as it can be seen in the Fig.2.

![](./images/811107926725885953_2.jpg)

In the Fig.2 it can see that for a same period a different effective refractive index of the grating can be obtained. Moreover, since both theoretical and optimal period have been calculated in each point for a same wavelength, the range of wavelengths can be represented in function of the effective refractive index of the grating obtained for the theoretical and optimized period such as it can be seen in the Fig.3.

![](./images/811107926725885953_3.jpg)

In the Fig.3, it can observe that the optimized period can be achieved in the point where both the optimized and theoretical period has the same effective refractive index of the grating in different wavelengths. In this manner the optimal period can be approximated in an analytical way when the effective refractive index of the grating is calculated for the operational wavelength minus a factor. This factor is calculated as the average of the wavelength difference in each point where both functions have the same effective refractive index of the grating (Eq. 3). The factor has been calculated as $\overline{\Delta\lambda}_{TE} = 36nm$.

$$
\overline{\Delta\lambda}_{TE} = \frac{\Delta\lambda_1+\Delta\lambda_2+\dots+\Delta\lambda_n}{n} \tag{3}
$$

### IV. SIMULATION RESULTS

For a wavelength of $\lambda = 1.55\mu m$, silicon refractive index $n_{Si}=3.4764$, and silica refractive index $n_{SiO_2}=1.4440$, the effective refractive index of the grating obtained is $neff_g$=2.6939 by Eq. 2 and the theoretical period is $\Lambda=615nm$. If the calculated factor is used to calculate the effective refractive index of the grating $neff_g'$=2.7157 then the resulted period is $\Lambda=610nm$, while the period optimized by several simulations is $\Lambda=609nm$ that is a very good agreement with the obtained with our factor.

Now the fill-factor is a parameter necessary to ensure a major coupling efficiency. A fill-factor of 50% is assumed for the calculation of the refractive index of the grating in the Eq. 2, now the same equation can be used to find the optimal fill-factor using the effective refractive index of the grating $n_{effg}'$ and the effective refractive index of etched $n_{effep}'$ and not etched $n_{effnep}'$ parts, so that these effective refractive indexes are calculated for the operational wavelength minus the factor before calculated, resulting the next expressions:

$$
neff_g' = \frac{(n_{effep}'+n_{effnep}')}{2}
$$

$$
Ff = \frac{neff_g'-n_{effep}}{n_{effnep}-n_{effep}} \tag{4}
$$

Using the Eq. 4 for the period calculated $\Lambda=610nm$ with our factor for a wavelength of $\lambda=1.55\mu m$, the fill-factor would be $Ff=57\%$ obtaining a coupling efficiency about 57% while that for an optimized by simulation period $\Lambda=$

$609nm$ and a $Ff=58\%$ the coupling efficiency is about $57.8\%$, as it can be seen in the Fig. 4(a).

For other wavelength of $\lambda=1.31\mu m$, using the factor calculated, the effective refractive index of the grating is $neff_{g}'=2.8774$, then the resulting period is $\Lambda=485nm$ and the fill-factor of $Ff=58.5\%$, obtaining a coupling efficiency about $59\%$, while the period and fill-factor optimized by several simulations are $\Lambda=485nm$ and $Ff=53\%$ , with a coupling efficiency about $60\%$, as it can be seen in the Fig. 4(b). Again, it is confirmed that our factor and the equations to calculate both the period and the fill-factor is an outstanding way to obtain the optimal values of such parameters, avoiding time consuming simulations.

![](./images/811107926725885953_4.jpg)

Fig. 4 Optimal value of the period and fill-factor using the calculated factor for an operational wavelength of (a) $\lambda$=1.55$\mu m$ and (b) $\lambda$=1.31$\mu m$, TE polarization

Using this procedure for other operational wavelengths we can get the optimal values of both period and fill-factor to ensure a major coupling efficiency, but now for a broad wavelength range such it can be observed in the Fig 5.

![](./images/811107926725885953_5.jpg)

Fig. 5 Spectra for the gratings for a wavelengths separated in intervals of 10nm TE polarization

If we analyze the variation of period in the range before calculated, this is approximately lineal for a range of operational wavelengths separated on intervals of 10nm Fig.6.

![](./images/811107926725885953_6.jpg)

Fig. 6 Optimal Period obtained for a range of wavelengths TE polarization

In this manner, the increment of the optimal period of one wavelength respect to other is approximately the half of the separation interval.

$$
\begin{cases}
\Delta\lambda=10nm \\
\Delta\Lambda_{TE}=\frac{\Delta\lambda}{2}
\end{cases} \tag{5}
$$

Now we can make the same analysis for a TM polarization with the calculation of the theoretical period for a same range of wavelengths. In this way, we can see that the theoretical period obtained also is approximately lineal, so the increment of the period of one respect to other operational wavelength in this interval is approximately the same separation of the interval.

$$
\begin{cases}
\Delta\lambda=10nm \\
\Delta\Lambda_{TM}=\Delta\lambda
\end{cases} \tag{6}
$$

With the Eq. 5 and Eq. 6 we can link the interval of the period for a TE and TM polarization, and conclude that the interval of the period for a TM polarization is equal to two times the interval of the period for a TE polarization. So, to achieve the optimal period with theoretical equation for TM polarization, we can use the factor before calculated in TE polarization by two (Eq.7).

$$
\overline{\Delta\lambda}_{TM}=2\overline{\Delta\lambda}_{TE} \tag{7}
$$

The same manner, that for TE polarization, the optimal fill-factor can be achieved for TM polarization through Eq. 8.

$$
Ff=\frac{1}{2}\left[\frac{neff_{g}'-neff_{ep}}{neff_{nep}'-neff_{ep}}+\frac{neff_{g}'-neff_{ep}'}{neff_{nep}-neff_{ep}'}\right] \tag{8}
$$

In this case, the optimal parameters obtained for the TM polarization both period and fill-factor is of $\Lambda=900nm$ and $Ff=57.1\%$ reaching a coupling efficiency about $50\%$ for an operational wavelength of $\lambda=1.55\mu m$, as it can be seen in the Fig. 7(a), and for an operational wavelength of $\lambda=1.31\mu m$ the optimal parameters obtained are period of $\Lambda=$

$656nm$ and a fill-factor of $Ff = 57.2\%$ reaching a coupling efficiency about 59%, as it can be seen in the Fig.7 (b).

![](./images/811107926725885953_7.jpg)

Fig. 7 Optimal value of the period and fill-factor using the calculated factor for an operational wavelength of (a) λ=1.55μm and (b) λ=1.31μm, TM polarization

Thereby using the same procedure employed to find the optimal values of the period and fill-factor in TE polarization and considering the new factor of correspondence for the TM polarization, we can get the optimal values to ensure a major coupling efficiency in TM polarization, such as we can see in the Fig 8.

![](./images/811107926725885953_8.jpg)

Fig. 8 Spectra for the gratings for a wavelengths separated in intervals of 10nm TM polarization

### V. EXPERIMENTAL RESULTS

Gratings for an operational wavelength of $\lambda = 1.55\mu m$ have been fabricated for both TE and TM polarization. In the Fig. 9 can be observed the SEM images of the structures where the period and fill-factor correspond to the design parameters obtained with our equations.

![](./images/811107926725885953_9.jpg)

Fig. 9 (a) Image SEM of the grating coupler for TE and (b) TM polarization.

Experimental coupling results of the fabricated gratings are shown in the Fig. 10. For the characterization of each grating we have assumed no propagation losses and 1.4dB of setup losses. In this way, for both polarizations TE and TM we have obtained approximately efficiencies of coupling of $38.43\%$ centered in $\lambda=1.554\mu m$ and $34.41\%$ centered in $\lambda=1.541\mu m$ respectively.

![](./images/811107926725885953_10.jpg)

Fig. 10 Simulated and Experimental grating coupling results for TE and TM polarization.

The resultant bandwidth (3dB) for the simulation grating coupler is about 82nm while in the experimental characterization is about 51nm for TE polarization, and for the TM polarization in simulation is about 73nm and 54nm in experimental. The difference of the obtained resulting values both in simulation and experimental stage is produced by the shifting of spectra of experimental results respect to the design wavelength due to deviations in the fabrication process. These deviations has been evaluated by simulation and results show that with a small variation of period and fill-factor, the power coupling can be reduced and resulting spectra of the grating can be centered in other wavelengths.

### VI. CONCLUSIONS AND FUTURE WORK

The principal parameter considered in the Bragg condition is the effective refracting index of the grating, if the optimal value for this parameter is selected, then, the period and fill-factor can be optimized in analytical form. The study shows that the effective refractive index of the grating can be optimal when this is calculated for the operational wavelength minus a factor.

The results obtained in the simulation stage using this methodology shows that maximum coupling efficiency is obtained and the spectrum of the grating coupler is centered in the operational wavelength, avoiding to make several simulations for the optimization of the grating parameters in the design stage.

The results obtained in the experimental characterization stage are agreement to the results obtained in simulation. However, due to deviations of parameters in the fabrication process of the grating, the coupling efficiency can be less than in simulation.

The optimal values for the grating parameters in TM polarization can be obtained starting off the TE optimal values, where the factor utilized in which is fulfilled the optimal values in the operational wavelength is the double that for TE.

As future work it will fabricate the gratings for a wavelength operation $\lambda$=1.31$\mu$m.

# REFERENCES

[1] L. He, Y. He, A. Pomerene, C. Hill, S. Ocheltree, T. Baehr- Jones, and M. Hochberg, "Ultrathin silicon-on-insulator grating couplers," *IEEE Photonics Technol. Lett.*, vol. 24, no. 24, pp. 2247-2249, 2012.

[2] D. Taillaert, F. Van Laere, M. Ayre, W. Bogaerts, D. Van Thourhout, P. Bienstman, and R. Baets, "Grating couplers for coupling between optical fibers and nanophotonic waveguides," *Japanese J. Appl. Physics, Part 1 Regul. Pap. Short Notes Rev. Pap.*, vol. 45, no. 8 A, pp. 6071-6077, 2006.

[3] L. Vivien, "Handbook of Silicon Photonics." 2013.

[4] E. W. RAalmer and J. F. Verrill, "L9_Diffraction gratings," *Contemp. Phys.*, vol. 9, no. 3, pp. 257-276, 1968.

[5] K. Harper, "Theory, design, and fabrication of diffractive grating coupler for slab waveguide," no. December, p. 193, 2003.

[6] O. G. De Villasante, "Design and Simulation of Vertical Grating Coupler for Photonic Integrated System-in-Package," no. April, pp. 175-179, 2010.

[7] J. V. Galan, "Addressing Fiber-to-Chip Photonics," *PhD Thesis - Univ. Politec. Valencia*. December, 2010.

[8] C. A. Ramos, "Photonic chip interconnects and integrated polarization management for coherent communication," *PhD Thesis - Univ. de Malaga*. 2010.