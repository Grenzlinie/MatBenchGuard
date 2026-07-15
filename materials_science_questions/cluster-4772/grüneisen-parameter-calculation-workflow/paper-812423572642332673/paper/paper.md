phys. stat. sol. (b) **235**, No. 2, 254–259 (2003) / DOI 10.1002/pssb.200301565

# Pressure dependent phonon properties
of cubic group III-nitrides

D. N. Talwar*

Department of Physics, Indiana University of Pennsylvania, Indiana, PA 15705-1087, USA

Received 5 August 2002, revised 20 August 2002, accepted 20 August 2002
Published online 4 February 2003

PACS 63.20.Dj, 65.40.Ba, 65.40.De, 78.30.Fs

By constructing rigid-ion models (RIMs) at ambient and high pressures we present a comprehensive study of lattice-dynamics and thermodynamical properties in cubic III-nitrides. Murnaghan's equation of state is adopted for relating the volume dependence to pressure. The force constants in the RIM scheme are opti- mized using non-linear least square fitting procedures with constrained parameters and weighting of the data on critical-point phonons, lattice and elastic constants. Theoretical results for the phonon dispersions, density of states, mode Grüneisen parameters, specific heat, and thermal expansion coefficients are com- pared and discussed with the existing experimental and *ab initio* data.

## 1. Introduction
The wide band gap nitrides of boron, aluminum, gallium, and indium are expected to yield materials for fabricating opto-electronic devices, capable of operating in the ultraviolet and blue regions as well as under high-power, high frequency, and high-temperature conditions [1–3]. Despite the rapid commercialization of nitride based devices, there is still much that is not well understood about these materials especially their fundamental properties viz., elastic, structural, electronic, vibrational and thermodynamic characteristics.

In this paper we report an extensive study of the pressure dependent phonon properties of cubic III- nitrides in terms of a rigid-ion-model. In Section 2, we outline a brief account of the *quasi-harmonic* lattice dynamical theory of thermal expansion. Computational details for obtaining the optimized pa- rameters (cf. Section 3.1) phonon dispersions (both at ambient and high pressures) (cf. Section 3.2), and thermo-dynamical (cf. Section 3.3) properties (viz., specific heats, mode Grüneisen parameters, thermal expansion coefficients, etc.) are reported. Comparison of the inter-atomic interactions in III-nitrides with III–V and other compounds has allowed us to attain useful insights about the relative strength of bond- bending and bond-stretching forces responsible for their distinct phonon-mode behavior and thermal properties. Theoretical results are compared and discussed in Section 3 with the existing *ab initio* [4], experimental [5–8], and predicted data [9] with concluding remarks presented in Section 4.

## 2. Theoretical considerations
Thermodynamical properties of solids occur in *anharmonic* models where the second-order coefficients in the potential energy are volume dependent. However, to a first approximation thermal expansion can be derived within the *quasi-harmonic* theory by treating the lattice vibrations as harmonic, but with assumed volume- and pressure-dependent frequencies [10]. In this approximation, the vibrational entropy $S_{\text{lat}}$ can be expressed as the sum of the contributions from

* Corresponding author: e-mail: talwar@iup.edu, Phone: +01 724 357 2190, Fax: +01 357 3804

© 2003 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim 0370-1972/03/23502-0254 $ 17.50+.50/0

$\omega_j(\boldsymbol{q})$ phonons

$$
S_{\text{lat}} = \sum S_j = \sum S\left(\frac{\hbar\omega_j(\boldsymbol{q})}{k_{\text{B}}T}\right). \tag{1}
$$

Here, $S(x)(\equiv k_{\text{B}}[\{x/\exp(x)-1)\}-\ln\{1-\exp(-x)\}])$ is the entropy function for a harmonic oscillator.
From Eq. (1), it follows that

$$
\left(\frac{\partial S_j}{\partial \ln V}\right)_T = \left(\frac{\text{d} \ln \omega_j(\boldsymbol{q})}{\text{d} \ln V}\right)\left(\frac{\partial S_j}{\partial \ln \omega_j(\boldsymbol{q})}\right)_T = -\left(\frac{\text{d} \ln \omega_j(\boldsymbol{q})}{\text{d} \ln V}\right)\left(\frac{\partial S_j}{\partial \ln T}\right)_V = \gamma_j(\boldsymbol{q}) C_j(\boldsymbol{q}), \tag{2}
$$

where the term

$$
\gamma_j(\boldsymbol{q}) = -\frac{\text{d} \ln \omega_j(\boldsymbol{q})}{\text{d} \ln V} = \frac{\text{d} \ln \omega_j(\boldsymbol{q})}{\text{d} P} \frac{\text{d} P}{\text{d} \ln V} = \frac{B}{\omega_j(\boldsymbol{q})}\left(\frac{\partial \omega_j(\boldsymbol{q})}{\partial P}\right) \tag{3}
$$

is the mode Grüneisen parameter and $C_j(\boldsymbol{q}) \left(\equiv Nk_{\text{B}}x^2 \frac{\exp(x)}{[\exp(x)-1]^2}\right)$ is the contribution of a single harmonic oscillator $\omega_j(\boldsymbol{q})$ to the specific heat $C_V$

$$
C_V = \sum_j\left(\frac{\partial S_j}{\partial \ln T}\right)_V = \sum_j C_j(\boldsymbol{q}). \tag{4}
$$

From the Eqs. (3) and (4), one can define the average Grüneisen constant $\bar{\gamma}$ as

$$
\bar{\gamma} = \sum_j \gamma_j(\boldsymbol{q}) \, C_j(\boldsymbol{q}) \bigg/ \sum_j C_j(\boldsymbol{q}) = \frac{\Omega\alpha}{\chi_{\text{T}}C_V}, \tag{5}
$$

where $B$, $\Omega$, $P$, and $\alpha$ in Eqs. (3) and (5) are the isothermal bulk modulus, crystal volume, pressure, and thermal expansion coefficient, respectively. If the mode-Grüneisen parameters are known for all the phonon branches throughout the Brillouin zone, one can calculate the thermal expansion coefficient $\alpha(T)$ by using

$$
\alpha(T) = \frac{1}{\Omega}\int k_{\text{B}}x^2 \frac{\exp(x)}{[\exp(x)-1]^2}\left(\frac{\partial \omega}{\partial P}\right)g(\omega)d\omega. \tag{6}
$$

In Eq. (6), the term $g(\omega)$ is the density of phonon states. It has also become customary to convert the specific heat into a more slowly varying Debye temperature data $\theta_{\text{D}}(T)$.

## 3 Computational details
### 3.1 Optimization of the model parameters
Two sets of RIM force constants [10] one at ambient and the other at higher pressure are obtained for each compound in the cubic group III-nitride family by using novel optimization procedures. In estimating the $P \neq 0$ lattice constants, Murnaghan's equation of state is adopted in relating the volume dependence (see: Fig. 1) to pressure. Except for $\Gamma$ point, there exist no experimental data of the pressure dependent phonons at high critical points in III-nitrides. We used, however, the pressure variation relations between the lattice and elastic constants with phonons (see: Ref. [10]) to estimate approximate values of the frequencies at X and L points. In the optimization process of RIM parameters at ambient and high pressures, we followed the non linear least-square fitting procedures where the data on elastic constants are used as input and the values of phonons at critical points as constraints on the values of the parameters. To assess the significance of the two sets of force constants and to treat the phonon properties at any desired pressure a linear interpolation scheme was adopted.

![](./images/812423572642332673_1.jpg)

Fig. 1 Calculated variation of volume ratio as a function of pressure for the cubic BN, AlN, GaN, and InN based on Murnaghan's equation of state.

3.2 Phonons The results of RIM calculations for phonon dispersions along high symmetry directions together with the corresponding one-phonon density of states for zinc-blende AlN and GaN are displayed in Fig. 2 for ambient and high pressures. The values of critical point phonons at ambient pressure are found in good accord with the existing ab initio [4] and experimental [5-8] data (open and full circles, squares and triangles). Here, we summarize some of the salient features found in the phonon behaviors:

(i) For the InN → GaN → AlN → BN sequence where N atom is common, the zone center optical phonon modes increase with the decrease of the cation mass. Similarly the phonon gap between the opti-cal-acoustical bands decreases (from 220 (InN) → 200 (GaN) → 82 (AlN) → (?) 0 (BN)) with the in-crease in the anion to cation mass ratio.

(ii) In III-nitrides, the strength of elastic forces and the degree of mixture of ionic and covalent bond-ing are responsible for the LO-TO splitting at the zone center as well as for the distinct dispersive be-havior of the optical and acoustical phonons. As compared to BN (not shown here) and AlN where the LO phonons show pronounced dispersive behavior, in GaN and InN (not shown here) the dispersion of

![](./images/812423572642332673_2.jpg)

Fig. 2 RIM calculations of the phonon dispersions and one phonon density of states for cubic AlN and GaN. Full lines represent ambient and dotted lines represent 22.9 GPa (AlN) and 52.2 GPa (GaN).

![](./images/812423572642332673_3.jpg)

Fig. 3 Comparison of the calculated $C_{\mathrm{v}}(T)$ for GaN and AlN (line) with the experimental data [11-14].

LO modes is shallower. The TO branches in BN and AlN show no or very little dispersion whereas up-ward dispersion is revealed for the TO phonons in GaN and InN. Our results exhibit a gradual develop-ment of the sharp density of states with distinct LO and TO phonons, as one moves along from BN $\rightarrow$ AlN $\rightarrow$ GaN $\rightarrow$ InN. Despite the differences in magnitude of the LO-TO splitting at $\Gamma$ point, related in part to the macroscopic electric fields accompanying polar modes, the phonon spectra of AlN exhibits similarities with both SiC and BP [10].

(iii) Similar to III-V compounds, our calculations show flatness of the TA branches over part of the Brillouin zone in GaN and InN. In AlN and BN, however, this feature disappears either partially or com-pletely. Consequently in GaN and InN, we see sharp and pronounced peaks in the TA region of the one-phonon density of states while broad bands appear in the corresponding region of AlN and BN.

3.3 Thermodynamical properties We calculated the mode Grüneisen parameters for III-nitrides along [001], [011], and [111] directions from the difference between $\omega_{j}(\boldsymbol{q})$'s at ambient and higher pres-sure by RIM using Eq. (3). For 3C-GaN, the results of $\gamma_{\mathrm{LO}(\Gamma)}$ and $\gamma_{\mathrm{TO}(\Gamma)}$ are found in good accord with the recent experimental [5-8] and ab initio [4] calculations.

It should be noted that the specific heat at constant pressure $C_{\mathrm{p}}(T)$ is measured experimentally and $C_{\mathrm{p}}-C_{\mathrm{v}}$ is only a small correction $(\leq 0.3 \%)$ compared to the experimental error involved. In Fig. 3, the comparison of the calculated values of $C_{\mathrm{v}}(T)$ for GaN and AlN with the experimental data [11-14] re-veals excellent agreement for the entire temperature range. The values of $C_{\mathrm{p}}(T)$ reported by Barin [15] for GaN are based on the approximation of Ref. [11] and show almost linear dependence with $T$ between 300-1700 K. In Fig. 4, we compared our results of $\alpha(T)$ for cubic AlN, and GaN over the extended

![](./images/812423572642332673_4.jpg)

Fig. 4 Comparison of the calculated thermal expansion coefficients for cubic AlN and GaN with the existing recommended data [9,16].

temperature range with the existing recommended data [9, 16]. Despite small negative mode Grüneisen parameters for the TA branches the calculated variations of $\alpha(T)$ in III-nitrides are seen much like that of $C_{v}(T)$, and unlike other III-V compounds [10] they do not exhibit negative values at lower $T$ values. In group III-nitrides the anomalous trends in the temperature variation of $\alpha(T)$ can be understood qualita tively in terms of the critical balance between the central and the non-central elastic forces associated with the stretching and bending of the bonds – determining the signs of Grüneisen parameter for the TA zone-edge phonons in tetrahedrally coordinated semiconductors. For the shear type TA(L) mode, the angular forces tend to make it stiffer under pressure, whereas the central elastic forces act in the opposite way. For instance, the signs of the mode Grüneisen parameters of the zone-boundary TA phonons and consequently the $\alpha(T)$ at low $T$ is positive for diamond, for which the angular forces are dominant, but negative for Si, Ge, and GaAs [10]. As compared to other zinc-blende semiconductors, the compensation between central and non-central forces in cubic III-nitrides is such that it exhibits much smaller mode softening, and hence the smaller pressure coefficients for the TA modes. All these effects are a conse- quence of the strong directional covalent bonding in the nitrides, which behave upon compression in a manner similar either to the carbon-based materials such as SiC or to solids involving at least one ele- ment iso-row to carbon such as B or N (viz., BP and III-nitrides) [10]. Although there are no experimen- tal data available for $\alpha(T)$ in cubic group III-nitrides, our results agree very well with the existing rec ommended values [9]. At low temperatures the negative values of $\alpha(T)$, if existed, would have been extremely small. Experimental results of $\alpha(T)$ using three-terminal capacitance dilatometers are very much needed both at low and high temperatures to check our theoretical predictions. We hope that the lattice dynamical calculations reported here should serve as a basis for the residual stress estimations in multilayer GaN/AlN, and GaN/InGaN devices [1–3] and for other theoretical studies.

4. Concluding remarks We have constructed rigid-ion models both at ambient and higher pressures to study the phonon and thermo-dynamical properties of cubic group III-nitrides. Our results for the complete phonon dispersion curves, density of states, mode Grüneisen parameters, specific heat, and thermal expansion coefficient are found in good agreement with the existing experimental and theoretical data. We found that the lattice dynamical description of $\alpha(T)$ in nitrides arises from the wave vector dependence of mode $\gamma$ and is related to their frequency spectrum. As the acoustic vibrations are dominant at low temperatures, the average Grüneisen constant or $\alpha(T)$ can become negative if the pressure or (volume) derivatives of the TA phonons are also negative (e.g., in Si and GaAs). In III-nitrides, although such lattice softening effects are not observed experimentally, our study suggest small negative mode gammas with weak $\gamma_{TA}$ values. The reason for the difference is that the directional partial covalent bond- ing in III-nitrides is much stronger than other zinc-blende type materials. It is worth mentioning that the TA modes depend on the electronic polarizability which is not included in the present RIM scheme. The negative values of $\alpha(T)$ at low $T$, if existed, would have been extremely small. Experimental re sults of $\alpha(T)$ using three-terminal capacitance dilatometers are needed to check our theoretical conjec tures.

Acknowledgements The author wishes to express his sincere thanks to Drs. David Look and D. C. Reynolds of the Wright State University, Dayton Ohio, and to Professor Robert Reeber of North Carolina State University, Ra- leigh for their continued interest and encouragement throughout the course of the present work. This research work was supported in part by the Cottrell Science Award # CC4600 (Research Corporation), and by the National Science Foundation Grant No. ECS-9906077.

### References

[1] S. Nakamura and G. Fasol, The Blue Laser Diode (Springer, Berlin, 1997).
[2] I. Akasaki, H. Amano, S. Sota, H. Sakai, T. Tanaka, and M. Koike, Jpn. J. Appl. Phys. 34, 1517 (1995).
[3] S. Nakamura, M. Senoh, S. Nagahama, N. Iwasa, T. Yamada, T. Matsushita, H. Kiyoku, and Y. Sugimoto, Jpn. J. Appl. Phys. 35, L74 (1996).

[4] K. Karch, F. Bechstedt, and T. Pletl, Phys. Rev. B 56, 3560 (1997);
K. Karch, F. Bechstedt, and T. Pletl, Phys. Rev. B 57, 7043 (1998);
K. Karch, F. Bechstedt, and T. Pletl, Phys. Rev. B 62, 4526 (2000);
K. Karch, F. Bechstedt, and T. Pletl, Phys. Rev. B 62, 8003 (2000).

[5] P. Perlin, C. Jauberthie-Carillon, J. P. Itie, A. San Miguel, I. Grzegory, and A. Polian, Phys. Rev. B 45, 83 (1992).
P. Perlin, T. Suski, J. W. Ager III, G. Conti, A. Polian, N. E. Christensen, I. Gorczyca, I. Grzegory, E. R. We- ber, and E. E. Haller, Phys. Rev. B 60, 1480 (1999).

[6] H. Siegle, A. R. Goñi, C. Thomsen, C. Ulrich, K. Syassen, B. Schöttker, D. J. As, and D. Schikora, in: Gallium Nitride and Related Materials II, edited by C. R. Abernathy, H. Amano, and J. C. Zopler, Mater. Res. Soc. Symp. Proc. 468 (Material Research Society, Pittsburgh, 1997), p. 225.

[7] A. R. Goñi, H. Siegle, K. Syassen, C. Thomsen, and J.-M. Wagner, Phys. Rev. B 64, 035205-1 (2001).

[8] Z. X. Liu, A. R. Goñi, K. Syassen, H. Siegle, C. Thomsen, B. Schöttker, D. J. As, and D. Schikora, J. Appl. Phys. 86, 929 (1999).

[9] G. A. Slack and S. F. Bartram, J. Appl. Phys. 46, 89 (1975).

[10] D. N. Talwar and J. C. Sherbondy, Appl. Phys. Lett. 67, 3301 (1995).
D. N. Talwar, G. Thaler, S. Zaranek, K. Peterson, S. Linger, D. Walker, and K. Holliday, Phys. Rev. B 55, 11293 (1997).

[11] Properties of Group III Nitrides, Electronic Materials Information Service (EMIS), edited by J. H. Edgar (IN- SPEC, London, 1994).

[12] R. Srinivas, D. Sulze, and H. Schwarz, J. Am. Chem. Soc. 112, 8334 (1990).

[13] R. D. Lafleur and J. M. Parnis, J. Phys. Chem. 96, 2429 (1992).

[14] C. H. Henrickson, D. Duffy, and D. P. Egman, Inorg. Chem. 7, 1047 (1968).

[15] I. Barin, Thermo Chemical Data of Pure Substances (VCH, Weinheim, 1995).

[16] R. R. Reeber and K. Wang, J. Mater. Res. 15, 40 (2000).