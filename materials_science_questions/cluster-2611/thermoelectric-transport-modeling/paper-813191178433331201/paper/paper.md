# Effect of Biaxial Strain on Electronic and Thermoelectric Properties of $\mathbf{Mg_2Si}$

HILAL BALOUT, $^{1}$ PASCAL BOULET, $^{1,3}$ and MARIE-CHRISTINE RECORD $^{2}$

1.—Madirel, UMR 7246, Aix-Marseille University and CNRS, FST St Jérôme, Av. Escadrille Normandie-Niemen, 13397 Marseille Cedex 20, France. 2.—IM2NP, UMR 7334, Aix-Marseille University and CNRS, FST St Jérôme, Av. Escadrille Normandie-Niemen, 13397 Marseille Cedex 20, France. 3.—e-mail: pascal.boulet@univ-amu.fr

The electronic and thermoelectric properties of biaxially strained magnesium silicide $\text{Mg}_2\text{Si}$ are analyzed by means of first-principle calculations and semiclassical Boltzmann theory. Electron and hole doping are examined for different doping concentrations and temperatures. Under strain the degeneracy of the electronic orbitals near the band edges is removed, the orbital bands are warped, and the energy gap closes up. These characteristics are rationalized in the light of the electron density transfers upon strain. The electrical conductivity increases with the biaxial strain, whereas neither the Seebeck coefficient nor the power factor (PF) follow this trend. Detailed analysis of the evolution of these thermoelectric properties is given in terms of the in-plane and cross-plane components. Interestingly, the maximum value of the PF is shifted towards lower temperatures when increasingly intensive strain is applied.

**Key words:** Magnesium silicide, thermoelectric properties, DFT calculations, strained structures

---

## INTRODUCTION

Research on thermoelectricity has attracted new interest in recent decades. By converting heat to electricity, thermoelectric devices enable recovery of waste thermal energy for low-power applications. Thermoelectric devices are typically composed of a plurality of thermoelectric couples connected electrically in series and thermally in parallel. A thermoelectric couple consists of a $p$-type and an $n$-type semiconducting material. Thus, thermoelectric devices have no moving parts, they are reliable and silent, and they do not produce greenhouse gases. $^{1}$

The performance of thermoelectric materials is quantified in terms of the dimensionless figure-of-merit parameter, $ZT$, defined as follows:

$$
ZT = \frac{S^2 \sigma}{\kappa_{\text{el}} + \kappa_{\text{ph}}} T, \tag{1}
$$

where $\sigma$ is the electrical conductivity, $S$ is the thermopower, $T$ is the temperature, and $\kappa_{\text{el}}$ and $\kappa_{\text{ph}}$ are the electronic and phononic contributions to the thermal conductivity, respectively. Equation 1 suggests that a key requirement for a good thermoelectric material is a high thermopower and electrical conductivity in the temperature range of interest along with a low thermal conductivity. High-performance thermoelectric materials are usually considered to have $ZT$ equal to or greater than one. $^{2}$

$\text{Mg}_2\text{X}$ (X = Si, Ge, Sn) alloys have been identified as promising advanced thermoelectric materials for use in the temperature range from 500 K to 800 K. $^{3,4}$ Compared with other thermoelectric materials operating in the same conversion temperature range, such as PbTe and $\text{CoSb}_3$, $\text{Mg}_2\text{X}$ are environmentally friendly materials, their constituent elements are nontoxic, and they are abundant in the Earth's crust. $^{5}$ With this type of materials, it may be possible to extend use of thermoelectricity to large-scale applications rather than being confined to technological niches as is currently the case. Hence, numerous papers have been published on these materials in recent years. $^{6-11}$

(Received June 7, 2013; accepted September 10, 2013;
published online October 23, 2013)

In the last decade, nanostructuring has proven to be a successful way to improve the figure of merit of thermoelectric materials. $^{1,8}$ In most cases, enhancements in $ZT$ result from reducing the lattice thermal conductivity. However, as shown by Koga et al., $^{12,13}$ $ZT$ can also be increased through enhancement of the power factor ($\text{PF} = S^2\sigma$). In nanostructured materials, mechanical strain plays an important role, and it is well known that electronic band-structure modifications appear in strained three-dimensional (3D) systems. $^{14,15}$ Therefore, the aim of the present work is to investigate the effect of biaxial strain, which may occur in layered $\text{Mg}_2\text{Si}$ heterostructures, on the electronic band structure and thermoelectric properties of bulk $\text{Mg}_2\text{Si}$. This investigation is conducted by density-functional theory (DFT) and Boltzmann transport theory calculations.

## THEORETICAL PROCEDURES

$\text{Mg}_2\text{Si}$ crystallizes in the cubic antifluorite structure; its lattice parameter is $a = 0.635$ nm. $^{16}$ In the primitive cell, the silicon atom occupies the $4a$ (0, 0, 0) site and the magnesium atoms occupy the $8c$ (0.25, 0.25, 0.25) sites. The $Fm-3m$ space group fixes the fractional coordinates of all atoms.

Our approach consists in two steps: (1) first-principles DFT$^{17,18}$ calculations performed using the plane-wave pseudopotential method as implemented in the Quantum-ESPRESSO package$^{19}$ and (2) calculations of transport properties performed using Boltzmann transport theory in the constant-scattering-time approximation as implemented in the BoltzTraP code.$^{20}$

The electron density of $\text{Mg}_2\text{Si}$ is self-consistently determined within the generalized gradient approximation using the Perdew–Burke–Ernzerhof exchange-correlation functional.$^{21}$ Ultrasoft pseudopotentials are used for all atoms.$^{22}$ Mg $2p^63s^2$ and Si $3s^23p^2$ orbitals are treated as valence orbitals. The cutoff energy that determines the quality of the plane-wave basis set was chosen as 410 eV based on the results of convergence tests. The $k$-point selection is based on the Monkhorst–Pack scheme. The $k$-point mesh used to sample the Brillouin zone is $20 \times 20 \times 20$ for the cell parameter determination and $80 \times 80 \times 80$ to obtain a more precise description of the electronic structure, which is a prerequisite for the subsequent calculations of transport properties. The lattice constant of $\text{Mg}_2\text{Si}$ was optimized until the total energy converged to at least $10^{-9}$ Ry, the forces borne by the atoms became smaller than $10^{-5}$ Ry/Bohr, and the strain on the lattice was smaller than 0.02 kbar (2 MPa).

In-plane biaxial strain was simulated by changing the $c/a$ ratio while keeping the cell volume constant. Throughout the paper, the biaxial strain is given in units of the relative change of the in-plane lattice constant as $\Delta a/a_0 = a/a_0 - 1$, where $a_0$ is the relaxed cell parameter. Hence, tensile and compressive strain correspond to $\Delta a/a_0 > 0$ and $\Delta a/a_0 < 0$, respectively.

## RESULTS AND DISCUSSION

### Electronic Band Structures

The electronic band structures calculated under different percentage strains from $-2\%$ to $+2\%$ are presented in Figs. 1 and 2. Since $a_0$ is found to be 0.6369 nm, the corresponding lattice parameter goes from 0.6242 nm to 0.6496 nm. The pressures resulting from these strains vary from 0 kbar to 0.4 kbar.

For strain-free $\text{Mg}_2\text{Si}$, the valence band presents a maximum at the $\Gamma$ point, consisting of a threefold-degenerate orbital, i.e., three equivalent valleys (Figs. 1e, 2a). When applying in-plane biaxial strain, these orbitals are energetically split into two groups, namely two degenerate in-plane valleys and one cross-plane one. This splitting can be explained by repulsion between valence electrons. Indeed, under in-plane tensile strain, the cross-plane interatomic bond distances are shortened and the Pauli repulsion interaction between electron pairs increases. As a consequence, an increase in energy of the cross-plane valence band is observed (Fig. 3). The calculated energy value at $2\%$ strain does not follow this trend. This is caused by an avoided band-crossing effect subsequent to the gap closure. By contrast, the in-plane interatomic bond distances are elongated. Therefore, the energy of the twofold-degenerate in-plane bands is decreased (Fig. 3). A similar effect for the in-plane compressive strain on the valence band is observed. Indeed, when compression occurs on $\text{Mg}_2\text{Si}$, the twofold-degenerate orbitals increase in energy as a result of the shortening of the in-plane interatomic bond distances and the energy of the cross-plane orbital decreases (Fig. 3).

The variation in energy of the two highest valence orbitals can be rationalized in terms of charge density. Therefore, we plot in Fig. 4 the difference between the charge density in planes (011) and (110) of the structures strained at $\pm 2\%$ and that of the unstrained one. Red and blue colors represent loss and gain of electron density, respectively. During tensile strain, we observe in plane (110) (Fig. 4a) a loss of charge density between the Mg atoms and between the Si and Mg atoms. A loss of density is also observed in plane (011) (Fig. 4b) during compressive strain. These phenomena can be related to the increase in energy of the cross-plane and in-plane orbitals, respectively. The same type of discussion applies for the decrease in energy of the in-plane and cross-plane orbitals during tensile and compressive strain, respectively, which can be explained in terms of electron density gain in planes (011) and (110), respectively (Fig. 4c, d).

The conduction band of unstrained $\text{Mg}_2\text{Si}$ presents, at the $\Gamma$ point, two threefold-degenerate orbitals separated by 173 meV. Under biaxial strain, each orbital is split into a twofold-degenerate in-plane orbital and a nondegenerate cross-plane one. Figure 5 depicts the evolution in energy of the

![](./images/813191178433331201_1.jpg)

Fig. 1. Band structure of strain-free Mg₂Si and biaxially strained Mg₂Si: (a) 2% compressive strain, (b) 1.5% compressive strain, (c) 1% compressive strain, (d) 0.5% compressive strain, and (e) unstrained.

![](./images/813191178433331201_2.jpg)

Fig. 2. Band structure of strain-free Mg₂Si and biaxially strained Mg₂Si: (a) unstrained, (b) 0.5% tensile strain, (c) 1% tensile strain, (d) 1.5% tensile strain, and (e) 2% tensile strain.

![](./images/813191178433331201_3.jpg)

Fig. 3. Variation of the valence orbital energy with respect to biaxial strain.

conduction-band orbitals. In contrast to what occurs
in the valence band, when tensile strain is applied,
the energy of the cross-plane orbitals decreases and
that of the in-plane orbitals increases, whereas in the
case of compressive strain, the energy of the cross-
plane orbitals increases and that of the in-plane
orbitals decreases. Since these orbitals are unoccu-
pied, their evolution upon strain is solely caused by
their own crystal symmetry.

The evolution of the electronic bandgap is plotted in
Fig. 6. Whatever the type of strain, compressive or
tensile, the gap value decreases monotonically with
the amplitude of the strain. Tensile strain has a
greater impact on the gap evolution than compressive
strain. Indeed, the bandgap is nearly closed at 1.5%
tensile strain, whereas it is still open at 2% compres-
sive strain. The closure of the gap is due to both the
decrease in energy of the lowest conduction orbital and
the increase in energy of the highest valence one.
However, the variation of the latter orbital is faster,
and this is even more pronounced under tensile strain.
The latter difference might be explained by the
fact that, under tensile strain, the highest valence
orbital corresponds to the cross-plane one, which is
nondegenerate, whereas under compressive strain it
corresponds to the in-plane one, which is twofold-
degenerate.

## Thermoelectric Transport Properties

### Electrical Conductivity

The electrical conductivity calculated at 300 K and
900 K for unstrained Mg₂Si is plotted with respect to

![](./images/813191178433331201_4.jpg)

Fig. 4. Variation of electron density between strain-free and 2% biaxially strained Mg₂Si: (a) tensile strain in the (110) plane, (b) compressive strain in the (011) plane, (c) tensile strain in the (011) plane, and (d) compressive strain in the (110) plane. Red color corresponds to electron density loss, and blue color corresponds to electron density gain (Color figure online).

![](./images/813191178433331201_5.jpg)

Fig. 5. Variation of the conduction orbital energy with respect to biaxial strain.

![](./images/813191178433331201_6.jpg)

Fig. 6. Evolution of the energy gap (in eV) with respect to the biaxial strain.

the carrier concentration in Fig. 7. As a consequence of the constant-relaxation-time approximation used in the BoltzTraP code, the electrical conductivity increases linearly with the carrier concentration. In the domain where carrier concentrations correspond to those of an intrinsic semiconductor, the electrical conductivity is higher at 900 K than at 300 K, as expected. In the heavily doped semiconducting regime, the curves at both 300 K and 900 K are superimposed.

For the strained structures, the xx and zz tensor elements of the electrical conductivity are depicted in Figs. 8a and 9a at 300 K for electron and hole doping of $10^{18}\ \mathrm{cm}^{-3}$, respectively, and Figs. 8d and 9d at 900 K for electron and hole doping of $1.2\times10^{20}\ \mathrm{cm}^{-3}$, respectively. The choice of these

![](./images/813191178433331201_7.jpg)

Fig. 7. Evolution of the Seebeck coefficient, electrical conductivity, and PF with respect to electron doping level.

![](./images/813191178433331201_8.jpg)

Fig. 8. xx and zz tensor elements of the electrical conductivity (a, d), Seebeck coefficient (b, e), and PF (c, f) with respect to biaxial strain at various temperatures and electron concentrations.

temperatures and doping concentrations follows
from the fact that the Seebeck coefficient $S$ exhibits
maxima for these values (Fig. 7). In the low-tem-
perature and electron-doping regimes (Fig. 8a), a
large enhancement of the electrical conductivity at
both high compressive and tensile strain is
observed. For $-2\%$ compressive and $+2\%$ tensile
strains, $\sigma_{xx}$ ($\sigma_{zz}$) is 10 times (10 times) and 60 times
(30 times) higher, respectively, than for the
unstrained structure. The curves for $\sigma_{xx}$ and $\sigma_{zz}$
follow each other tightly, except in the region of
high tensile strain (from and above $1.5\%$). The
trends are similar in the case of hole doping
(Fig. 9a). At high temperature and in the regime of
high electron or hole doping (Figs. 8d, 9d), the pic-
ture is radically different. Indeed, the electrical
conductivity is marginally improved (at most 2.25
times for $\sigma_{xx}$ for electron-doped $Mg_2Si$ under tensile

![](./images/813191178433331201_9.jpg)

Fig. 9. xx and zz tensor elements of the electrical conductivity (a, d), Seebeck coefficient (b, e), and PF (c, f) with respect to biaxial strain at various temperatures and hole concentrations.

![](./images/813191178433331201_10.jpg)

Fig. 10. Total electrical conductivity $\sigma$ versus strain at 300 K and 900 K for electron and hole doping of $10^{18}\ \text{cm}^{-3}$ and $1.2 \times 10^{20}\ \text{cm}^{-3}$.

strain) or even degraded in the case of $\sigma_{zz}$ for electron-doped $\text{Mg}_2\text{Si}$ under tensile strain.

The evolution of the total electrical conductivity $\sigma$ versus strain at 300 K and 900 K for electron and hole doping of $10^{18}\ \text{cm}^{-3}$ and $1.2 \times 10^{20}\ \text{cm}^{-3}$ is plotted in Fig. 10. Whatever the conditions, $\sigma$ increases with the strain. Whereas at 300 K the conductivity values are independent of the doping type (electrons or holes), at 900 K they are higher for electron doping.

![](./images/813191178433331201_11.jpg)

Fig. 11. Evolution of the Seebeck coefficient with respect to temperature for various electron and hole carrier concentrations.

The evolution of the electrical conductivity with respect to the constraints described above should, however, be considered with care since we considered the relaxation scattering time $\tau$ as constant. The fact that we could not find experimental data on the dependence of the electrical conductivity on

![](./images/813191178433331201_12.jpg)

Fig. 12. Total Seebeck coefficient versus strain at 300 K and 900 K for electron and hole doping of $10^{18}\ \text{cm}^{-3}$ and $1.2\times 10^{20}\ \text{cm}^{-3}$.

![](./images/813191178433331201_13.jpg)

Fig. 13. Total PF versus strain at 300 K and 900 K for electron and hole doping of $10^{18}\ \text{cm}^{-3}$ and $1.2\times 10^{20}\ \text{cm}^{-3}$.

strain for $\text{Mg}_2\text{Si}$ prevents us from estimating the evolution of $\tau$ with the constraints.

### Seebeck Coefficient

The absolute value of the Seebeck coefficient calculated for unstrained $\text{Mg}_2\text{Si}$ is plotted in Fig. 7 with respect to doping level at 300 K and 900 K, and in Fig. 11 with respect to temperature.

At a given temperature, in the doping range from $10^{17}\ \text{e/cm}^3$ to $1.2\times 10^{21}\ \text{e/cm}^3$, the curve of the Seebeck coefficient exhibits a maximum value ($400\ \mu\text{V/K}$ at 300 K and $10^{18}\ \text{e/cm}^3$, $225\ \mu\text{V/K}$ at 900 K and $1.2\times 10^{20}\ \text{e/cm}^3$). On either side of this maximum value, the Seebeck coefficient drops rapidly.

For low temperatures and low doping levels, the thermopower reaches values of about $-425\ \mu\text{V/K}$ for electron doping while for hole doping it is around $540\ \mu\text{V/K}$ (Fig. 11). These high values are a consequence of the position of the chemical potential, which is then located near the band edges. At fixed charge carrier concentration, when the temperature increases, the chemical potential is shifted towards the middle of the bandgap, and as a consequence the thermopower rapidly drops and levels off to a small, negative value ($-50\ \mu\text{V/K}$). Hence, in this temperature domain, the conduction is due to both electrons and holes (bipolar intrinsic regime).

For heavily doped $\text{Mg}_2\text{Si}$, the Seebeck coefficient grows linearly in absolute value with temperature up to about $150\ \mu\text{V/K}$ at 1200 K. This behavior is in good agreement with the Mott relation for thermoelectric power.²³

The calculated $S_{xx}$ and $S_{zz}$ tensor elements for strained $\text{Mg}_2\text{Si}$ are presented in Figs. 8b and 9b at 300 K for electron and hole doping of $10^{18}\ \text{cm}^{-3}$, respectively, and Figs. 8e and 9e at 900 K for electron and hole doping of $1.2\times 10^{20}\ \text{cm}^{-3}$, respectively. Note that the negative of the Seebeck coefficient is plotted in Fig. 8b, e.

![](./images/813191178433331201_14.jpg)

Fig. 14. Dependence of the PF on temperature at constant electron doping of $1.2\times 10^{20}\ \text{cm}^{-3}$.

Whatever the strain conditions applied or the carrier type and concentration, the Seebeck coefficient is lower than for strain-free $\text{Mg}_2\text{Si}$.

At low temperature and electron carrier concentration (Fig. 8b), the $S_{xx}$ thermopower decreases by about 20% and 17% for small (0.5%) tensile strain and small (-0.5%) compressive strain, respectively, while $S_{zz}$ decreases by about 30% and 10% for small tensile strain and small compressive strain, respectively. Under high strain ($\geq$1.5%), the absolute value of the Seebeck coefficient decreases by about 80%. This observation is valid for both tensile and compressive strains. However, in the case of tensile strain a change of sign of the $zz$ component is noticeable. Hence, high strain may induce a bipolar conduction regime in the material. In the case of low hole concentration (Fig. 9b), the description of the curves would be identical to above, except that $S_{xx}$ and $S_{zz}$ would be switched.

At high temperature and high electron doping (Fig. 8e), like in the previous case, the thermopower of strained $\text{Mg}_2\text{Si}$ is smaller than that of strain-free

material. However, we do not observe that the See- beck coefficient eventually changes sign under high strain. Moreover, the evolution of the Seebeck coef- ficient with respect to strain is different depending on whether the conduction is due to electrons or holes (Fig. 9e). In particular, the anisotropy between $S_{xx}$ and $S_{zz}$ is larger for hole than for electron conduction, especially for high strain, where it is roughly double.

The evolution of the total Seebeck coefficient ver- sus strain at 300 K and 900 K for electron and hole doping of $10^{18} cm^{-3}$ and $1.2 × 10^{20} cm^{-3}$ is given in Fig. 12. One can observe that, in the strained struc- tures, the Seebeck coefficient is always lower than in the unstrained material. This could be due to the sharpening of the orbitals at the $\Gamma$ point when strain is applied (Figs. 1,2). In effect, when electronic bands become steeper, the density of states decreases as well as the Seebeck coefficient.

## Power Factor

The power factor, $PF = S^{2}\sigma$, is a function of tem- perature and doping level. For strain-free $Mg_{2}Si$, the dependence of the PF on carrier concentration at given temperatures (300 K and 900 K) is depicted in Fig. 7. For both temperatures, the maximum PF is observed at around $10^{21} e/cm^{3}$. The location of this peak is dictated by the electrical conductivity. The PF maximum at 900 K is seven times higher than that at 300 K. This behavior is related to the ratio between S at 300 K and S at 900 K, which amounts to about 2.5.

The dependence of $PF_{xx}$ and $PF_{zz}$ on the strain is depicted in Figs. 8c and 9c for electron and hole doping, respectively, at 300 K and $10^{18} cm^{-3}$, and Figs. 8f and 9f for electron and hole doping, respectively, at 900 K and $1.2 × 10^{20} cm^{-3}$.

For low electron and hole carrier concentrations, application of strain results in a decrease of the PF compared with the unstrained situation, except for $PF_{xx}$ at $1.5\%$ tensile strain, for which the best compromise is found between a moderately small value of $S_{xx}$ and a moderately large value of $\sigma_{xx}$. In this case, the improvement of the PF is about $15\%$.

For high temperature and high carrier concen- tration, $PF_{zz}$ is systematically improved under compressive strain for electron conduction, and for tensile strain smaller than $1\%$ for hole conduction. The largest improvement is obtained at $-1\%$ com- pressive strain and amounts to about $11\%$. In all other cases, both $PF_{xx}$ and $PF_{zz}$ are degraded.

The total PF, which is presented in Fig. 13 as a function of strain at 300 K and 900 K for electron and hole doping of $10^{18} cm^{-3}$ and $1.2 × 10^{20} cm^{-3}$, is systematically degraded under strain. The dependence of the PF on temperature at constant electron doping of $1.2 × 10^{20} cm^{-3}$ is depicted in Fig. 14. It is worth mentioning that, under com- pressive and tensile strain, the location of the PF maximum is systematically shifted towards lower temperature as the strain increases. This evolution is also observed at constant hole doping of $1.2 × 10^{20} cm^{-3}$.

## CONCLUSIONS

This paper presents results of DFT calculations coupled with Boltzmann transport theory to inves- tigate the thermoelectric properties of $Mg_{2}Si$ under biaxial strain. From DFT the electronic band structures are calculated. Their evolution under strain is determined and shows removal of the orbital degeneracy, band warping, and energy gap closure. Among the calculated electronic transport properties, only the electrical conductivity increases upon strain. Orbital sharpening is observed at the edge of the valence band, inducing a decrease of the thermopower and hence of the PF. Increasing the intensity of the strain of $Mg_{2}Si$ produces a shift of the PF maximum towards lower temperature. This result could be attractive for substitution of thermoelectric materials containing hazardous or rare elements for the working temperature range from 500 K to 600 K.

## ACKNOWLEDGEMENTS

Part of the computations were performed at the Mésocentre d'Aix-Marseille Université (Project Number 13b020). This work was also granted access to the HPC resources of Centre Informatique National de l'Enseignement Supérieur (CINES), Montpellier, France under allocation C2013086881 made by Grand Equipement National de Calcul Intensif (GENCI). The authors are grateful to the EADS foundation for funding Hilal Balout's PhD thesis.

## REFERENCES

1. P. Boulet and M.C. Record, *Int. J. Nanotechnol.* 9, 368 (2012).
2. R.Z. Zhang, C.L. Wang, J.C. Li, W.B. Su, J.L. Zhang, M.L. Zhao, J. Liu, Y.F. Zhang, and L.M. Mei, *Solid State Sci.* 12, 1168 (2010).
3. R.G. Morris, R.D. Redin, and G.C. Danielson, *Phys. Rev.* 109, 1909 (1958).
4. M. Akasaka, T. Iida, A. Matsumoto, K. Yamanaka, Y. Takanashi, T. Imai, and N. Hamada, *J. Appl. Phys.* 104, 013703 (2008).
5. M. Baleva, G. Zlateva, A. Atanassov, M. Abrashev, and E. Goranova, *Phys. Rev. B* 72, 115330 (2005).
6. W. Liu, X. Tang, and J. Sharp, *J. Phys. Appl. Phys.* 43, 085406 (2010).
7. V.K. Zaitsev, M.I. Fedorov, E.A. Gurieva, I.S. Eremin, P.P. Konstantinov, A.Y. Samuni, and M.V. Vedernikov, *Phys. Rev. B* 74, 045207 (2006).
8. Q. Zhang, J. He, T.J. Zhu, S.N. Zhang, X.B. Zhao, and T.M. Tritt, *Appl. Phys. Lett.* 93, 102109 (2008).
9. W. Xi-Na, W. Yong, Z. Jin, Z. Tian-Chong, M. Zeng-Xia, G. Yang, X. Qi-Kun, D. Xiao-Long, Z. Xia-Na, H. Xiao-Dong, and Z. Ze, *Chin. Phys. B* 18, 3079 (2009).
10. J. Tani and H. Kido, *Intermetallics* 16, 418 (2008).
11. B. Yu, D. Chen, Q. Tang, C. Wang, and D. Shi, *J. Phys. Chem. Solids* 71, 758 (2010).
12. T. Koga, T.C. Harman, S.B. Cronin, and M.S. Dresselhaus, *Phys. Rev. B* 60, 14286 (1999).
13. T. Koga, X. Sun, S.B. Cronin, and M.S. Dresselhaus, *Appl. Phys. Lett.* 75, 2438 (1999).

14. N.F. Hinsche, I. Mertig, and P. Zahn, *J. Phys.: Condens. Matter* 23, 295502 (2011).

15. M.O. Baykan, S.E. Thompson, and T. Nishida, *J. Appl. Phys.* 108, 093716 (2010).

16. P. Villars, and K. Cenzual, *Pearson Crystal's data—Crystal Structure Database for inorganic compound* (Materials Park, OH: ASM International, 2010/2011).

17. P. Hohenberg and W. Kohn, *Phys. Rev.* 136, B864 (1964).

18. W. Kohn and L.J. Sham, *Phys. Rev.* 140, A1133 (1965).

19. P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A.P. Seitsonen, A. Smogunov, P. Umari, and R.M. Wentzcovitch, *J. Phys.: Condens. Matter.* 21, 2009 (395502).

20. G.K.H. Madsen, K. Schwarz, P. Blaha, and D.J. Singh, *Phys. Rev. B* 68, 125212 (2003).

21. J.P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* 77, 3865 (1996).

22. D. Vanderbilt, *Phys. Rev. B* 41, 7892 (1990).

23. N.F. Mott and E.A. Davis, *Electronic Processes in Non-crystalline Materials* (Oxford: Clarendon, 1971), p. 47.