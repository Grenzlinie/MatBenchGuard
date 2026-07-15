# Electronic and Transport Properties of LaNi₄Sb₁₂ Skutterudite: Modified Becke-Johnson Approach

TAHIR MOHIUDDIN BHAT,¹,² SRISHTI SINGH,¹
and DINESH C. GUPTA¹,³

1.—Condensed Matter Theory Group, School of Studies in Physics, Jiwaji University, Gwalior 474 011, India. 2.—e-mail: bhattahir682@gmail.com. 3.—e-mail: sosfizix@gmail.com

We carried out an *ab initio* study of structural, electronic, thermodynamic, and thermoelectric properties of the lanthanum-filled skutterudite, LaNi₄Sb₁₂. Generalized gradient approximation and modified Becke–Johnson potentials were employed for the exchange–correlation potential. The electronic structure calculations display the metallic behavior of the compound. The alloy offers low lattice thermal conductivity along with a high Seebeck coefficient with a value of – 158 ($\mu$VK⁻¹) at room temperature. The effect of high pressure and temperature on thermal properties like thermal expansion coefficient, heat capacity, and Grüneisen parameter are also investigated by means of a quasi-harmonic Debye model. The large Seebeck coefficient and high power factor exhibited by LaNi₄Sb₁₂ make it an attractive candidate for thermoelectric materials.

**Key words:** Electronic, Seebeck coefficient, Grüneisen parameter, skutterudite, power factor

## INTRODUCTION

Thermoelectric materials have acknowledged worldwide attention as they are important in converting waste heat into useful electricity and hence are seen as future sources of green energy.¹⁻⁵ At present, the world is in need of materials to decrease the dependence on vanishing fossil fuels. Materials with a useful thermoelectric performance like Bi₂Te₃, clathrates, skutterudites and Heusler alloys are promising aspirants for thermoelectric devices.⁶⁻⁸ The skutterudites have been most extensively studied for their thermoelectric properties as they show a comparatively larger thermoelectric performance⁹,¹⁰ than traditionally used thermoelectrics. Binary skutterudites are generally represented by MX₃ (where M = transition metal atom, X = pnicogen metal atom). One of the major drawbacks of binary skutterudites is that they inherit high thermal conductivity in contrast to conventional thermoelectric materials.¹¹ Therefore, to qualify as a robust thermoelectric material, it is necessary to reduce the thermal conductivity. Since the skutterudite structure comprises two fairly large voids, nourishing these voids by pertinent impurity atoms to form fully or partially filled skutterudites, commonly signified as R₂M₈X₂₄ and RM₄X₁₂ (R = rare earth atom and MX represents a filler atom), effectively reduces the thermal conductivity of these materials.¹²⁻¹⁴

The competence of a thermoelectric material is categorized by its dimensionless figure-of-merit ($ZT$),¹⁵⁻¹⁸ and is expressed as:

$$
ZT = \frac{S^2\sigma T}{\kappa} \tag{1}
$$

Here, $S$ is the Seebeck coefficient, $\sigma$ the electrical conductivity, $\kappa$ the thermal conductivity, and $T$ the temperature. To enhance $ZT$, Seebeck coefficient and electrical conductivity must be higher with low thermal conductivity at the same instant. The interconnection among various transport properties makes it difficult to maximize the $ZT$. In order to enhance the $ZT$ of the materials, we either have to increase the power factor or decrease the thermal

---
(Received February 12, 2018; accepted April 20, 2018)

Published online: 02 May 2018

conductivity. By introducing the resonance level in the valence band, one can increase the power factor, while by transferring materials from bulk to nanostructures, lattice thermal conductivity can be suppressed by scattering the longer wavelength heat-carrying phonons. $^{19-21}$ Quantum confinement effects can similarly improve the Seebeck coefficient, and the electrical conductivity can be miproved by adjusting the carrier concentration through doping. $^{22}$ Alternatively, we can achieve low thermal conductivity through scattering of heat-carrying phonons by atomic-scale point defects, and native lattice anharmonicity. $^{16}$

## COMPUTATIONAL METHODS

The present self-consistent calculations were carried out by means of density functional theory using the full-potential linearly augmented plane wave method (FPLAPW) $^{23}$ employed in WEIN2k. $^{24}$ The exchange-correlation function has been treated by using the GGA $^{25}$ and modified Becke-Johnson (mBJ) models. $^{26}$ The inclusion of the mBJ potential was essential to exactly predict the band gap. Energy convergence is controlled by the cut-off parameter, $K_{\text{Max}}R_{\text{MT}}=7$. The energy threshold between the core and valence states was set to $-$ 6.0 Ry. For Brillouin zone integration, a mesh of $12\times12\times12$ containing 2,000 k-points was used. The thermodynamic properties of the $\text{LaNi}_4\text{Sb}_{12}$ compound have been calculated by applying the quasi-harmonic Debye model $^{27-29}$ in the temperature range of 0–400 K, while the pressure has been varied from 0 GPa to 10 GPa. In this model, the Gibbs function is defined as:

$$
G^{*}(V;P,T)=E(V)+PV+F_{\text{vib}}(\theta(V),T)\tag{2}
$$

where $E(V)$ signifies the total energy per unit cell, $PV$ is the constant hydrostatic pressure condition, $\theta(V)$ the Debye temperature and $F_{\text{vib}}$ the lattice vibration expressed as

$$
F_{\text{vib}}(\theta,T)=nk_{\text{B}}T\left[\frac{9\theta}{8T}+3\ln\left(1-e^{\frac{\theta}{T}}\right)-D(\theta/T)\right]\tag{3}
$$

where $n$ is the number of atoms per unit cell, $D(\theta/T)$ represents the Debye integral, the anisotropic solid, $\theta$ is stated by

$$
\theta=\frac{\hbar}{K}[6\pi^{2}V^{1/2}n]^{1/3}f(v)\sqrt{\frac{B_{\text{s}}}{M}}\tag{4}
$$

in which $M$ gives the molecular mass, $B_{\text{s}}$ is the adiabatic bulk modulus, and $f(v)$ is

$$
f(v)=\left\{3\left[2\left(\frac{21+\sigma}{31-2\sigma}\right)^{(3/2)}+\left(\frac{11+\sigma}{31-\sigma}\right)^{(3/2)}\right]^{(-1)}\right\}^{(1/3)}\tag{5}
$$

Here, $\sigma$ is the Poisson ratio.

Thus, to contract the non-equilibrium Gibbs function with respect to volume at constant pressure and temperature is obtained as

$$
\left(\frac{\partial G^{*}(V;P,T)}{\partial V}\right)_{(P,T)}=0\tag{6}
$$

After solving the above equation, one can obtain a relationship for $V(P,T)$, i.e., the thermal equation of state. Using Eq. 6 for different thermal properties, i.e., specific heat capacity values at constant volume $(C_{\text{V}})$, the thermal expansion coefficient $(\alpha)$ can be evaluated using the following formulae:

$$
C_{\text{V}}=3nk_{\text{B}}\left[4D\frac{\theta}{T}-\frac{3\theta/T}{e^{\theta/T}-1}\right]\tag{7}
$$

$$
\alpha=\frac{\gamma C_{\text{V}}}{B_{\text{T}}V}\tag{8}
$$

where $\gamma$ is the Grüneisen parameter and is calculated from the following expression

$$
\gamma=-\frac{d\ln\theta(V)}{d\ln V}\tag{9}
$$

The transport properties were calculated using the semi-classical Boltzmann theory incorporated within BoltzTraP code. $^{30,31}$ In order to analyze the transport coefficients, we have used the constant relaxation time approximation $(\tau=5\times10^{-15})$ value. Since the transport properties are very dependent on the k-point sampling, a dense mesh of 1,000,000 k-points was used to obtain reliable results.

## RESULTS AND DISCUSSION

### Structural and Electronic Properties

The $\text{LaNi}_4\text{Sb}_{12}$ compound crystallizes in a body-centered cubic structure having space group Im3 (204), where one La atom is seated at the atomic position of 2a (0, 0, 0) and one Ni atom is positioned at 8c (0.25, 0.25, 0.25), whereas one Sb atom is placed at the position of 24 g (0, 0.35, 0.16). The atomic positions of residual atoms are self-adjusted by symmetry operations associated with the space group. $^{32}$ The unit cell crystal structure of $\text{LaNi}_4\text{Sb}_{12}$ is presented in Fig. 1.

Estimating the ground state properties of $\text{LaNi}_4\text{Sb}_{12}$, the optimized lattice constant for $\text{LaNi}_4\text{Sb}_{12}$ calculated using the GGA and mBJ are almost equal. The present $\text{LaNi}_4\text{Sb}_{12}$ compound justifies its stability in the non-magnetic phase with the equilibrium lattice constant of $9.36$ Å.

In order to demonstrate the electronic structure, the total densities of states (DOS) and partial densities of states (PDOS) were calculated in the stable phase of $\text{LaNi}_4\text{Sb}_{12}$ and are shown in Fig. 2a and b. Almost the same DOS is found from both mBJ and GGA methods. On applying the mBJ potential, the bands shift fractionally towards the Fermi level in the valence band. The DOS and PDOS also explain the contribution of different

![](./images/813037746510626817_1.jpg)

Fig. 1. Crystal structure of the filled skutterudite LaNi4Sb12 compound.

states in the band structures. As seen from the partial DOS, strong overlapping of $f$ and $d$-bands of La is found around the Fermi level with little hybridization with Sb-bands in a conduction band. While in the valence band, e.g., states and $t_{2g}$ states of the Ni atom contribute towards the hybridization process. It can be clearly observed that the $f$-electrons of La are dominant in the conduction band, while the $d$-electrons of the Ni atoms greatly dominate the valence band, as the major peak in the conduction band emerges due to $f$-electrons of La and in the valence band the peak is due to the $d$-electrons of the Ni atoms.

### Thermodynamic Properties

We have calculated the thermal properties of the $\text{LaNi}_4\text{Sb}_{12}$ compound under high temperature and pressure by employing the quasi-harmonic Debye model in the temperature range 0–370 K, while the pressure has been kept constant at 0 GPa, 5 GPa and 10 GPa.

In order to discover the vibrational properties, the heat capacity at constant volume ($C_\text{V}$) was calculated for $\text{LaNi}_4\text{Sb}_{12}$, which is required for many applications. The variation of $C_\text{V}$ in the temperature range of 0–370 K and pressure from 0 GPa to 10 GPa is depicted in Fig. 3. It can be seen that the $C_\text{V}$ curve shows a sharp increase up to 200 K, then increases slowly and approaches a constant value, the so-called Dulong-Petit limit, at a high temperature range which is almost common to all solids at high temperatures. We accomplish that at low temperature when $C_\text{V}$ becomes proportional to $T^3$ and at high temperature when it approaches the Dulong-Petit law which is common to all solids.$^{33}$

![](./images/813037746510626817_2.jpg)

Fig. 2. Spin-polarized (a) total density of states (DOS) and (b) partial density of states (PDOS) at the equilibrium lattice constant for La-Ni4Sb12. The Fermi level is set to zero energy.

The consequence of the temperature and pressure on the thermal expansion coefficient ($\alpha$) is depicted in Fig. 4. The thermal expansion coefficient increases with increasing temperature at a specific pressure. But the effect of the increasing pressure is rather adverse, i.e., $\alpha$ decreases abruptly with increasing pressure and decreases at higher pressures. The effect of temperature is more significant at the lower temperatures, whereas at higher temperatures $\alpha$ increases slowly. The value of $\alpha$ at room temperature (at 0 GPa pressure) is $0.67 \times 10^{-5}\ \text{K}^{-1}$ which is very low and makes it proficient for higher temperature uses.

We have also studied the effect of pressure and temperature on the Grüneisen parameter ($\gamma$) which is plotted in Fig. 5, form which it can be seen that at constant temperature there is radical decrease in $\gamma$ with the increase in pressure. At constant pressure, the Grüneisen parameter remains at a fixed value with the increase in temperature. Thus, it may be

![](./images/813037746510626817_3.jpg)

Fig. 3. Variation of specific heat at constant volume ($C_V$) with temperature and pressure.

![](./images/813037746510626817_4.jpg)

Fig. 4. Variation of thermal expansion coefficient ($\alpha$) with temperature and pressure.

![](./images/813037746510626817_5.jpg)

Fig. 5. Variation of Grüneisen parameter as a function of temperature and pressure.

![](./images/813037746510626817_6.jpg)

Fig. 6. Calculated electrical conductivity as a function of temperature.

concluded that the increase in pressure has a superior effect as compared to temperature, i.e., the temperature has a weaker effect than pressure on $\gamma$. Since $LaNi_4Sb_{12}$ presents a $\gamma$ value of 2.12 at 0 GPa pressure, this specifies a robust anharmonicity in the compound which authenticates the low lattice thermal conductivity.

## Thermoelectric Properties

In order to investigate the electronic transport properties of the $LaNi_4Sb_{12}$ compound under a constant relaxation time approximation for the charge carriers, we have employed Boltzmann's theory. The thermoelectric properties include the electrical conductivity ($\sigma/\tau$) where $\tau$ is the relaxation time, with the thermal conductivity ($\kappa$), Seebeck coefficient ($S$) and power factor (PF).

Figure 6 shows the temperature variation of electrical conductivity ($\sigma/\tau$) for $LaNi_4Sb_{12}$. The value of $\sigma/\tau$ does not vary much up to room temperature, while subsequently it decreases with increasing temperature. The decreasing character of $\sigma/\tau$ demonstrates that the material should behave as a metal because of supplementary DOS present at the Fermi level, and $\sigma/\tau$ decreases from $5.8 \times 10^{19}$ ($\Omega^{-1} \text{m}^{-1} \text{s}^{-1}$) at 50 K and reaches a value $5.22 \times 10^{19}$ ($\Omega^{-1} \text{m}^{-1} \text{s}^{-1}$) at 800 K.

The variation of total thermal conductivity ($\kappa_{\text{tot}}$), which is the actual sum of electronic thermal conductivity ($\kappa_{\text{e}}$) and lattice thermal conductivity ($\kappa_{\text{L}}$), with the temperature is shown in Fig. 7. The lattice thermal conductivity ($\kappa_{\text{L}}$) is estimated by using Slack's equation, while $\kappa_{\text{e}}$ is attained by employing the BoltzTraP code. $\kappa_{\text{L}}$ shows the

![](./images/813037746510626817_7.jpg)

Fig. 7. Calculated thermal conductivity (κ) as a function of temperature.

reducing inclination with temperature, which possibly may be due to strong phonon scattering by the La atoms (filler atoms), as these filler atoms are loosely bound in the voids of the skutterudite structure and rattle in a harmonic manner in the cage-like structure. This rattling motion strongly scatters the phonons resulting in lowering the lattice conductivity. Meanwhile, the $\kappa_{\rm e}$ increases with temperature while the total thermal conductivity shows a decreasing trend with temperature. $\kappa_{\rm tot}$ varies from 10 W/mK at 50 K to 1.8 W/mK at room temperature (300 K), while beyond this temperature the variation is fairly small.

The Seebeck coefficient for the compound has been reported as a function of temperature and is depicted in Fig. 8. It is seen from these plots that the calculated values of the Seebeck coefficient are negative in the entire temperature range, suggesting the presence of $n$-type charge carriers, i.e., electrons. The value of $S$ increases from $-76\ \mu{\rm VK}^{-1}$ at 50 K to $-158\ \mu{\rm VK}^{-1}$ at 300 K, then decreases smoothly with further increases in temperature. We have compared the room-temperature Seebeck coefficient of LaNi₄Sb₁₂ with those reported previously³⁴ which show that LaNi₄Sb₁₂ has a remarkably higher value of Seebeck coefficient compared to the other materials of this family.

![](./images/813037746510626817_8.jpg)

Fig. 8. Calculated transport Seebeck coefficient ($S$) as a function of temperature.

The PF is one of the significant parameters to evaluate the efficiency of a material. It is actually the product of the Seebeck coefficient and electrical conductivity. Figure 9 shows the variation of the calculated PF with temperature demonstrating that the PF increases from $0.25\times10^{14}\ \mu{\rm W\ cm^{-1}K^{-2}s^{-1}}$ to $3.72\times10^{14}\ \mu{\rm W\ cm^{-1}K^{-2}s^{-1}}$ from 50 K to 800 K. The reason for a high PF is the very large Seebeck coefficient and moderate electrical conductivity offered by LaNi₄Sb₁₂. Since the investigations showed that the LaNi₄Sb₁₂ presents high values for the Seebeck coefficient and PF, this reveals that the material will possibly be a convenient material for thermoelectric applications at room temperature.

![](./images/813037746510626817_9.jpg)

Fig. 9. Calculated power factor ($PF$) as a function of temperature.

## CONCLUSIONS

We have used first-principle calculations to investigate the structural, electronic, thermodynamic, and thermoelectric properties of a lanthanum-filled skutterudite, LaNi₄Sb₁₂. The compound crystallizes in a body-centered cubic structure with space group $Im3$ having an optimized lattice constant of 9.36 Å. The quasi-harmonic Debye model was used to understand the thermodynamic properties including the thermal expansion coefficient, heat capacity, and Grüneisen parameter in the pressure range 0.0–10.0 GPa, while the temperature was varied from 50 K to 370 K. The thermoelectric properties were calculated by using the BoltzTraP code. The

negative value of $S$ suggests that the compound behaves as $n$-type material. Meanwhile, $\text{LaNi}_4\text{Sb}_{12}$ skutterudite presents a high Seebeck coefficient of $\sim -158$ ($\mu\text{VK}^{-1}$) which resulting in a very large PF of to $2.13 \times 10^{14}\ \mu\ \text{W cm}^{-1}\text{K}^{-2}\text{s}^{-1}$ at room temperature. The material shows large values of Seebeck coefficient and PF at room temperature which makes it a feasible candidate for thermoelectric device applications.

## REFERENCES

1.  L.E. Bell, *Science* 321, 1457 (2008).
2.  M. Gürth, G. Rogl, V.V. Romaka, A. Grytsiv, E. Bauer, and P. Rogl, *Acta Mater.* 104, 210 (2016).
3.  J.P. Heremans, B. Wiendlocha, and A.M. Chamoire, *Energy Environ. Sci.* 5, 5510 (2012).
4.  T.M. Bhat and D.C. Gupta, *RSC Adv.* 6, 80302 (2016).
5.  S. Yousuf and D.C. Gupta, *Mater. Sci. Eng. B* 221, 73 (2017).
6.  J.R. Sootsman, D.Y. Chung, and M.G. Kanatzidis, *Angew. Chem. Int. Ed.* 48, 8616 (2009).
7.  T.M. Bhat and D.C. Gupta, *J. Magn. Magn. Mater.* 435, 173 (2017).
8.  S. Yousuf and D.C. Gupta, *Mater. Chem. Phys.* 192, 33 (2017).
9.  J.S. Dyck, W. Chen, and C. Uher, *J. Appl. Phys.* 91, 3698 (2002).
10. X. Shi, W. Zhang, L.D. Chen, J. Yang, and C. Uher, *Acta Mater.* 56, 1733 (2008).
11. D. Morelli and G.P. Meisner, *J. Appl. Phys.* 77, 3777 (1995).
12. G.A. Slack and V.G. Tsoukala, *J. Appl. Phys.* 76, 1665 (1994).
13. R. Gumeniuk, et al., *Phys. Rev. Lett.* 100, 017002 (2008).
14. D.T. Morelli and G.P. Meisner, *J. Appl. Phys.* 77, 3777 (1995).

15. D.M. Rowe, *CRC Handbook of Thermoelectrics: Macro to Nano* (Boca Raton: CRC/Taylor & Francis, 2006).
16. K. Biswas, *Nature* 489, 414 (2012).
17. A. Banik, U.S. Shenoy, S. Saha, U.V. Waghmare, and K. Biswas, *J. Am. Chem. Soc.* 138, 13068 (2016).
18. T.M. Bhat and D.C. Gupta, *J. Electron. Mater.* 45, 6012 (2016).
19. E. Quarez, K.F. Hsu, R. Pcionek, N. Frangis, E.K. Polychroniadis, and M.G. Kanatzidis, *J. Am. Chem. Soc.* 127, 9177 (2005).
20. J. Androulakis, C.H. Lin, H.J. Kong, C. Uher, C.I. Wu, T. Hogan, B.A. Cook, T. Caillat, K.M. Paraskevopoulos, and M.G. Kanatzidis, *J. Am. Chem. Soc.* 129, 978 (2007).
21. D. Narducci, E. Selezneva, G. Cerofolini, S. Frabboni, and G. Ottaviani, *J. Solid State Chem.* 193, 19 (2012).
22. E.S. Toberer, A. Zevalkink, and G.J. Snyder, *J. Mater. Chem.* 21, 15843 (2011).
23. P. Hohenberg and W. Kohn, *Phys. Rev. B* 136, 864 (1964).
24. P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, and J. Luitz, *WIEN2k An Augmented Plane Wave Plus Local Orbitals Program for Calculating Crystal Properties* (Vienna: Vienna University of Technology, 2001).
25. J.P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* 77, 3865 (1996).
26. F. Tran and P. Blaha, *Phys. Rev. Lett.* 102, 226401 (2009).
27. M.A. Blanco, E. Francisco, and V. Luania, *Comput. Phys. Commun.* 158, 57 (2004).
28. S.A. Dar, V. Srivastava, and U.K. Sakalle, *J. Electron. Mater.* 46, 6870 (2017).
29. S.A. Dar, V. Srivastava, and U.K. Sakalle, *Mater. Res. Express* 4, 086304 (2017).
30. G.K.H. Madsen and D.J. Singh, *Comput. Phys. Commun.* 175, 67 (2006).
31. G.K.H. Madsen, *J. Am. Chem. Soc.* 128, 12140 (2006).
32. A. Shankar, D.P. Rai, R.Khenata, Sandeepa, and R.K. Thapa, *Phase Transit.* 88, 1062 (2015).
33. S.A. Dar, V. Srivastava, and U.K. Sakalle, *J. Supercond. Nov. Magn.* 30, 3055 (2017).
34. E.S. Toberer, A.F. May, C.J. Scanlon, and G.J. Snyder, *J. Appl. Phys.* 105, 063701 (2009).
