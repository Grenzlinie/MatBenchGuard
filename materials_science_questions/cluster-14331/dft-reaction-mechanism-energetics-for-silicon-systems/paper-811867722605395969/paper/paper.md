# Simulation Study for HTCVD of SiC Using First-Principles Calculation and Thermo-Fluid Analysis

Yasuo Kitou$^{1,a}$, Emi Makino$^{1,b}$, Kenji Inaba$^{3,c}$, Norikazu Hosokawa$^{2,d}$, Hidehiko Hiramatsu$^{2,e}$, Jun Hasegawa$^{2,f}$, Shoichi Onda$^{1,g}$, Hideyuki Tsuboi$^{3,h}$, Hiromitsu Takaba$^{3,i}$ and Akira Miyamoto$^{3,j}$

$^{1}$ Research Laboratories, DENSO CORPORATION, 500-1, Minamiyama, Komenoki-cho, Nisshin-shi, Aichi 470-0111, Japan

$^{2}$ Corporate R & D Department, DENSO CORPORATION, 1-1, Showa-cho, Kariya-shi, Aichi 448-8661, Japan

$^{3}$ Department of Applied Chemistry, Graduate School of Engineering, Tohoku University, 6-6-11-1302 Aoba, Aramaki, Aoba-ku, Sendai 980-8579, Japan

$^{a}$yasuo_kitou@denso.co.jp, $^{b}$emi_makino@denso.co.jp, $^{c}$kenji@aki.che.tohoku.ac.jp, $^{d}$norikazu_hosokawa@denso.co.jp, $^{e}$hidehiko_hiramatsu@denso.co.jp, $^{f}$jun_hasegawa@denso.co.jp, $^{g}$sonda@rlab.denso.co.jp, $^{h}$tsuboi@aki.che.tohoku.ac.jp, $^{i}$takaba@aki.che.tohoku.ac.jp, $^{j}$miyamoto@aki.che.tohoku.ac.jp

**Keyword:** HTCVD, Bulk growth, First-principles calculation, Thermo-fluid analysis, Chlorinated species, Growth rate, Gas phase reaction, Free energy, Activation energy, Frequency factor

**Abstract.** A simulation study for high temperature chemical vapor deposition (HTCVD) of silicon carbide (SiC) is presented. Thermodynamic properties of the species were derived from the first-principles calculations in order to evaluate the activation energy ($E_{\text{a}}$) in the gas phase reaction. Pathways producing $\text{SiC}_{2}$ and $\text{Si}_{2}\text{C}$ from $\text{SiCl}_{4}$-$\text{C}_{3}\text{H}_{8}$-$\text{H}_{2}$ system were proposed to investigate the effect of chlorinated species on HTCVD. A thermo-fluid analysis was carried out to estimate the partial pressures of the species. It was found that the main sublimed species of $\text{Si}$, $\text{SiC}_{2}$, $\text{Si}_{2}\text{C}$ decreased in the $\text{SiCl}_{4}$-$\text{C}_{3}\text{H}_{8}$-$\text{H}_{2}$ system compared to the $\text{SiH}_{4}$-$\text{C}_{3}\text{H}_{8}$-$\text{H}_{2}$ system. This suggests that the growth rate would decrease in the atmosphere of chlorinated species at around $2500^\circ\text{C}$.

## Introduction

The growth technology of single crystal bulk silicon carbide (SiC) has been improved for the last decade. Four inch wafers with low micropipe density are commercially available. The modified Lely method is a standard method to grow SiC bulk crystal. Other growth techniques such as high temperature chemical vapor deposition (HTCVD) [1] and halide chemical vapor deposition (HCVD) [2] have also been developed for SiC bulk growth. These methods have advantage of stability of the stoichiometry, however, it is difficult to find an optimum condition because there are a lot of parameters to be determined in a growth process. Numerical simulation [3-6] could be a powerful tool to design a reactor and to determine growth conditions. In our previous study [4], the growth rate in HTCVD of $\text{SiH}_{4}$-$\text{C}_{3}\text{H}_{8}$-$\text{H}_{2}$ system was calculated using the reaction rates in the literature [3] and the sticking coefficients determined by the experiments. In order to deal with new reactions composed of new source gases such as silicon tetrachloride ($\text{SiCl}_{4}$), we try to estimate the reaction rates by calculations instead of experiments. The reaction rates derived from calculations can be used for the thermo-fluid analysis to calculate the growth rate in HTCVD and HCVD.

## Experimental

A vertical cylindrical reactor has been used in an RF inductive heating furnace. Silane ($\text{SiH}_{4}$), silicon tetrachloride ($\text{SiCl}_{4}$) and propane ($\text{C}_{3}\text{H}_{8}$) were used as source gases and hydrogen ($\text{H}_{2}$) as a carrier gas. The process pressure was 53 kPa and the growth temperature was $2200$-$2500^\circ\text{C}$. The graphite wall of the reactor was covered by tantalum carbide (TaC) in order to prevent the graphite wall from reacting with $\text{H}_{2}$ and $\text{SiH}_{4}$. The other conditions were the same of the Ref. [4].

## Simulation Method

### Gas Phase Reaction Rate.
The rate constant of the gas phase reaction for the thermo-fluid analysis is expressed in Eq. 1,
$$\mathrm{k}=\mathrm{A} \mathrm{T}^{\mathrm{n}} \exp \left(-\mathrm{E}_{\mathrm{a}} / \mathrm{RT}\right). \tag{1}$$
where k is the reaction rate constant, A is the frequency factor, T is the absolute temperature, n is the temperature exponential factor, $\mathrm{E}_{\mathrm{a}}$ is the activation energy and R is the molar gas constant. In order to deal with new chemical reactions whose reaction rates are not known, we tried to calculate the reaction rates. The activation energy $(\mathrm{E}_{\mathrm{a}})$ was evaluated by the free energy difference $(\Delta \mathrm{G})$ between reactant and product of each reaction. This is based on the Linear Free Energy Relation (LFER) in which the $\mathrm{E}_{\mathrm{a}}$ difference correlates with the $\Delta \mathrm{G}$. First, correlation of the $\mathrm{E}_{\mathrm{a}}$ with the $\Delta \mathrm{G}$ in $\mathrm{SiH}_{4}-\mathrm{C}_{3} \mathrm{H}_{8}-\mathrm{H}_{2}$ system was evaluated using the literature values. Then, the $\mathrm{E}_{\mathrm{a}}$ of new reactions was estimated using the correlation and the $\Delta \mathrm{G}$ of the new reactions. The frequency factor (A) was also examined considering the size, collision volume and the steric factor of molecule. The temperature exponential factor (n) was assumed to be zero in this study.

### First-principles calculation.
The Gibbs free energy difference $(\Delta \mathrm{G})$ was calculated using the software package $\mathrm{DMol}^{3}$ based on the density functional theory (DFT). First, geometry optimization of each molecule was performed within local density approximation (LDA) using Vosko-Wilk-Nusair (VWN). After that, the free energy was calculated within generalized gradient approximation (GGA) using Perdew Wang 91(PW91). Enthalpy (H), entropy (S) and heat capacity at constant pressure $(\mathrm{C}_{\mathrm{p}})$ as functions of temperature were also calculated using a vibrational analysis with $\mathrm{DMol}^{3}$.

### Pathway of New Reaction.
The gas phase reaction of $\mathrm{SiCl}_{4}-\mathrm{C}_{3} \mathrm{H}_{8}-\mathrm{H}_{2}$ system was calculated as new species and reactions in order to investigate the effect of chlorinated species on HTCVD. Thermodynamic calculation of $\mathrm{SiCl}_{4}-\mathrm{Ar}, \mathrm{C}_{3} \mathrm{H}_{8}-\mathrm{H}_{2}$ was shown, but $\mathrm{Si}-\mathrm{Cl}-\mathrm{C}-\mathrm{H}$ complex species were not considered [2]. On the other hand, $\mathrm{Si}-\mathrm{Cl}-\mathrm{C}-\mathrm{H}$ complex species were mentioned in the normal temperature CVD, but the species were not important due to low partial pressures [5]. We considered the pathway of producing $\mathrm{SiC}_{2}$ and $\mathrm{Si}_{2} \mathrm{C}$ from $\mathrm{SiCl}_{4}-\mathrm{C}_{3} \mathrm{H}_{8}-\mathrm{H}_{2}$ system because $\mathrm{SiC}_{2}$ and $\mathrm{Si}_{2} \mathrm{C}$ are important species for high temperature growth of SiC. Other possible pathways involving chlorinated species were also proposed based on the literatures [6].

### Thermo-fluid Analysis.
A thermo-fluid analysis was carried out in three steps as follows. First, the temperature distribution of the reactor was calculated by analyzing the electromagnetic field, heat transfer and fluid dynamics. Secondly, partial pressures of the species were evaluated by the gas phase reaction using the reaction rate constants. Finally, the growth rate was estimated by determining the sticking coefficients in the surface reaction by fitting them to experimental results. Commercially available software CFD-ACE+ was used under a two dimensional model. Main part of the simulation was the same of the Ref. [4]. The reaction rate constants and thermodynamic properties derived from the first-principles calculations were also used in the present study.

![](./images/811867722605395969_1.jpg)

Fig. 1. The activation energy $(\mathrm{E}_{\mathrm{a}})$ of $\mathrm{SiH}_{4}-\mathrm{C}_{3} \mathrm{H}_{8}-\mathrm{H}_{2}$ [3] as a function of the free energy differences $(\Delta \mathrm{G})$.

## Results and Discussion

Fig. 1 shows the activation energy ($E_a$) of $SiH_4$-$C_3H_8$-$H_2$ system [3] as a function of the free energy differences ($\Delta$G) derived from the first-principles calculations. $\Delta$G was calculated at the temperature of zero Kelvin (K). When the $\Delta$G was positive value, the $E_a$ correlated with $\Delta$G. In contrast, when the $\Delta$G was negative value, the $E_a$ did not correlate with $\Delta$G and the value was near zero. We consider the $E_a$ only in the case of positive $\Delta$G. The $E_a$ of new reactions were evaluated using the correlation with $\Delta$G.

We also examine the correlation of the frequency factor (A) with the size, collision volume and the steric factor of molecule. However, any correlation has not been found yet. We assumed that all the values of A were the constant value because those in Ref.[3] were concentrated in the range of $10^{12}$-$10^{14}$. The growth rates were calculated on the assumption that the A was constant in the range of $10^{11}$-$10^{15}$. As a result, the growth rate using the constant A was not much different from the previous result [4] in which the $E_a$ from literature [3] was used. The growth rate at $10^{14}$ was almost the same as the previous result. On the basis of these results, the gas phase reaction including new species and reactions was calculated using $E_a$ determined by $\Delta$G and the constant A of $10^{14}$.

The proposed pathways producing $SiC_2$ and $Si_2C$ from $SiCl_4$-$C_3H_8$-$H_2$ system are shown in Fig. 2. Thermodynamic calculation showed that $C_2H_4$, $C_2H_2$, $CH_4$ and $SiCl_2$ were the major species from $SiCl_4$-$C_3H_8$-$H_2$ system. We assumed Si-C-H-Cl complex species produced from these major species as shown in Fig. 2. The Si-C-H-Cl complex species could be converted into $SiC_2$, $Si_2C$ and HCl. The total number of reaction formula and species was 84 and 43 respectively, including other complexes such as Si-H, Si-H-Cl, C-H. Thermodynamic properties of new species were calculated with $DMol^3$. The $E_a$ of new reactions were evaluated using the correlation with $\Delta$G in Fig.1 as explained above.

Fig. 3. shows the partial pressures of main species in $SiH_4$-$C_3H_8$-$H_2$ system and $SiCl_4$-$C_3H_8$-$H_2$ system calculated with the gas phase reaction model at $2500^\circ$C using the thermo-fluid analysis. The reaction rate constants calculated by the above method were used. The partial pressures of Si, $SiC_2$, $Si_2C$ species in the $SiCl_4$ system decreased compared to those in the $SiH_4$ system and $C_2H_2$ species

![](./images/811867722605395969_2.jpg)

Fig. 2. The reaction processes of $SiC_2$ (a) and $Si_2C$ (b) from $SiCl_2$ and hydrocarbon.

increased. The partial pressures of $SiCl_2$, SiCl, Cl and HCl (not shown) appeared in the $SiCl_4$ system and the values were comparably large. The partial pressure of HCl was about 8 kPa. The reason that the Si species decreased in the $SiCl_4$ system was the formation of $SiCl_x$ species. $SiC_2$, $Si_2C$ species also decreased although the reaction processes in Fig. 2 were added to the gas phase reaction. It seems that the contribution of the processes in Fig. 2 to the formation of $SiC_2$, $Si_2C$ species is small. The decrease of $Si$, $SiC_2$, $Si_2C$ species suggests that the growth rate would decrease in the $SiCl_4$-$C_3H_8$-$H_2$ system because $Si$, $SiC_2$, $Si_2C$ species are the main sublimed species above $2000^\circ C$.

![](./images/811867722605395969_3.jpg)

Fig.3. Partial pressures of main species in $SiH_4$ system and $SiCl_4$ system calculated with the gas phase reaction model at $2500^\circ C$. Partial pressures of $H_2$, H, HCl are not shown here.

Moreover, HCl species, which could work as an etching gas, increased. The increase of the growth rate was reported in the CVD at $1600^\circ C$ using chlorinated species [7] because the formation of silicon droplets was suppressed. The effect of silicon droplets could be eliminated in our case because they are more likely to be vaporized at $2500^\circ C$. Our experimental result showed that the growth rate decreased in the $SiCl_4$-$C_3H_8$-$H_2$ system compared to the $SiH_4$-$C_3H_8$-$H_2$ system on the condition that the mole fractions of the source gases and temperature were the same in both systems. This would mean that the contribution of $SiCl_x$ and $C_2H_2$ species to the growth is small. In order to increase the growth rate, it might be necessary to lower the growth temperature.

A calculation of the growth rate including surface reactions is now under investigation in order to clarify the growth mechanism in the atmosphere of chlorinated species.

## Summary
We presented the HTCVD simulation that can deal with new source gases without experimental values of the reaction rates. The pathways producing $SiC_2$ and $Si_2C$ from $SiCl_4$-$C_3H_8$-$H_2$ system were proposed. The main sublimed species of $Si$, $SiC_2$, $Si_2C$ decreased in the $SiCl_4$-$C_3H_8$-$H_2$ system compared to the $SiH_4$-$C_3H_8$-$H_2$ system. This suggests that the growth rate would decrease in the atmosphere of chlorinated species.

## References
[1] A. Ellison, B. Magnusson, B. Sundqvist, G. Pozina, J.P. Bergman, E. Janzen and A. Vehanen: Mater. Sci. Forum Vol. 457-460 (2004), p. 9.

[2] S. Nigam, H. J. Chung, A. Y. Polyakov, M. A. Fanton, B. Weiland, D. W. Snyder and M. Skowronski: J. Crystal Growth Vol. 284 (2005), p.112.

[3] O. Danielsson, A. Henry and E. Janzen: J. Crystal Growth Vol. 243 (2002), p.170.

[4] Y. Kitou, E. Makino, K. Ikeda, M. Nagakubo and S. Onda: Mater. Sci. Forum Vol. 527-529 (2006), p. 107.

[5] A. Veneroni and M. Masi: Chem. Vap. Deposition Vol. 12 (2006), p. 562.

[6] G. Valente, C. Cavallotti, M. Masi and S. Carra: J. Crystal Growth Vol. 230 (2001), p.247.

[7] S. Leone, M. Mauceri, G. Pistone, G. Abbondanza, F. Portuese, G. Abagnale, G. L. Valente, D. Crippa, M. Barbera, R. Reitano, G. Foti and F. La Via: Mater. Sci. Forum Vol. 527-529 (2006), p. 179.

Silicon Carbide and Related Materials 2007
10.4028/www.scientific.net/MSF.600-603

Simulation Study for HTCVD of SiC Using First-Principles Calculation and Thermo-Fluid Analysis
10.4028/www.scientific.net/MSF.600-603.47

DOI References

[2] S. Nigam, H. J. Chung, A. Y. Polyakov, M. A. Fanton, B. Weiland, D. W. Snyder and M. kowronski: J. Crystal Growth Vol. 284 (2005), p.112.
doi:10.1016/j.jcrysgro.2005.06.027

[3] O. Danielsson, A. Henry and E. Janzen: J. Crystal Growth Vol. 243 (2002), p.170.
doi:10.1016/S0022-0248(02)01486-0

[4] Y. Kitou, E. Makino, K. Ikeda, M. Nagakubo and S. Onda: Mater. Sci. Forum Vol. 527-529 2006), p. 107.
doi:10.4028/www.scientific.net/MSF.527-529.107

[5] A. Veneroni and M. Masi: Chem. Vap. Deposition Vol. 12 (2006), p. 562.
doi:10.1002/cvde.200606468

[7] S. Leone, M. Mauceri, G. Pistone, G. Abbondanza, F. Portuese, G. Abagnale, G. L. Valente, D. rippa, M. Barbera, R. Reitano, G. Foti and F. La Via: Mater. Sci. Forum Vol. 527-529 (2006), p. 79.
doi:10.4028/www.scientific.net/MSF.527-529.179

[1] A. Ellison, B. Magnusson, B. Sundqvist, G. Pozina, J.P. Bergman, E. Janzen and A. Vehanen: Mater. Sci. Forum Vol. 457-460 (2004), p. 9.
doi:10.4028/www.scientific.net/MSF.457-460.9

[2] S. Nigam, H. J. Chung, A. Y. Polyakov, M. A. Fanton, B. Weiland, D. W. Snyder and M. Skowronski: J. Crystal Growth Vol. 284 (2005), p.112.
doi:10.1016/j.jcrysgro.2005.06.027

[4] Y. Kitou, E. Makino, K. Ikeda, M. Nagakubo and S. Onda: Mater. Sci. Forum Vol. 527-529 (2006), p. 107.
doi:10.4028/www.scientific.net/MSF.527-529.107

[7] S. Leone, M. Mauceri, G. Pistone, G. Abbondanza, F. Portuese, G. Abagnale, G. L. Valente, D. Crippa, M. Barbera, R. Reitano, G. Foti and F. La Via: Mater. Sci. Forum Vol. 527-529 (2006), p. 179.
doi:10.4028/www.scientific.net/MSF.527-529.179