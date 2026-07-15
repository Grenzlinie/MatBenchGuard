# Quantum and classical size effects on thermoelectric transport in Si/Ge superlattices

W. L. Liu*, G. Chen*, J. L. Liu& and K. L. Wang&

*Mechanical and Aerospace Engineering Department
&Electrical Engineering Department
University of California at Los Angeles, CA 90095, USA
*Mechanical Engineering Department
Massachusetts Institute of Technology,
77 Massachusetts Avenue, Cambridge, MA 02139

## Abstract
Quantum size effect thermoelectric enhancement has been intensively investigated. However, the electronic transport along the in-plane direction is also affected by interface scattering that can be attributed to classical size effect. It has been observed that interface scattering sometimes greatly degrade low-dimensional thermoelectric enhancement. To have a complete understanding of the transport with both quantum and classical size effect, we conduct experimental investigation of in-plane thermoelectric properties on Si/Ge superlattices and theoretical characterization of those properties with electron Boltzmann transport model. In this paper, we will report the experimental result and comparison with the modeling.

**Keywords**: Thermoelectrics, Superlattices, Boltzmann Equation, Low-dimensionality

## Introduction
In recently years, lots of attention has been paid to low-dimensional thermoelectric enhancement. In 1993, Hicks and Dresselhaus¹ˢ² first quantitatively predicted the possibility to raise thermoelectric figure of merit, ZT, by order of magnitude through quantum size effect optimization. Following their work, various theoretical models have been developed³ˢ⁴ˢ⁵ and experimental investigations have been conducted for both in-plane and cross-plane ZT enhancement.⁶ˢ⁷ˢ⁸ Si/Ge superlattice is one of superlattice systems that have been intensively investigated for this purpose. Previous experimental investigation on Si/Ge superlattice showed improved ZT with reduced dimension as predicted by the two-dimensional transport model⁷. However, comparison of the model and measured data indicated that an extrinsic scattering term should be considered in the transport. The extrinsic scattering term, addressed by an extrinsic relaxation time obtained by data fitting,⁷, is attributed to the rough interface effect. In quantum effect two-dimensional transport model, electrons are assumed to be particles obeying two-dimensional dispersion and the interface scattering is assumed perfectly specular. Therefore, no resistive interface scattering mechanism is included. If the interface is rough, the diffuse scattering may cause the dispersion to deviate from two-dimensional since the phase coherence is destroyed and a randomly distributed velocity component perpendicular to the quantum well direction exists. For such a situation, the diffuse scattered electrons should be treat as three-dimensional particles and the back scattering of electron forms a resistive relaxation procedure that can be characterized by the Boltzmann transport equation with proper boundary condition. An effective quantum-classical size effect combined Boltzmann transport model for in-plane thermoelectric transport using Fuchs and Sondheimer's approach⁹ has been reported before.¹⁰ With single valley and infinite quantum well approximation, it demonstrated that, at the nanometer scale, both quantum size effect and classical size effect are important to transport properties. Since the band structure of superlattice is generally much complex than single valley infinite quantum well, more efforts are required to developed the model to make it applicable to calculate the transport properties of real superlattices. In this paper, we will present the theoretical calculation of transport properties of Si/Ge superlattices for which the multi-valley contribution and the strain effect are included. Also, we measured the thermoelectric properties of three Si/Ge superlattice samples at temperatures ranging from 80K to 300K. The measured data are compared with the modeling results and good agreement between experimental and theoretical values has been obtained. The combined model that includes both classical and quantum size effects provide a useful tool for further low-dimensional thermoelectric investigation.

## Theoretical model
The model is based on Fuchs and Sondheimer's approach for electrons transport in thin film metal, where electrons are treated as classical particles that partial diffuse and partial specularly scattered at the boundary with certain specularity $p_e$. To apply the method to semiconductor, the electrons cannot be treated as non-dispersion particles and proper dispersion should be introduced to characterize their movement. To account for both quantum and classical size effects, we introduced two-dimensional and three-dimensional dispersions to describe

---
0-7803-7683-8/02/$17.00 © 2002 IEEE
130
21st International Conference on Thermoelectronics (2002)

the electrons at different scattering state. The specularly scattered electrons preserve phase and thus are quantized to form subband. This requires two-dimensional dispersion relationship to be applied to describe specularly scattered part. For diffuse scattered electrons, due to the existence of randomly distributed perpendicular velocity component, the three-dimensional dispersion relationship should be applied. The in-plane Boltzmann transport equation and its solution is given in detail in ref. 10. With the existence of barrier layer and multi-valleys, the transport matrix should be written as:

$$
\begin{aligned}
\ell^{(\alpha)}= & \frac{e^{2} \tau D_{1}}{D_{1}+D_{2}} \cdot \sum \int_{0}^{\zeta} d \eta \int_{0}^{\infty} v_{x}^{2} D O S(\varepsilon)\left(-\frac{\partial f_{0}}{\partial \varepsilon}\right)(\varepsilon-\zeta)^{\alpha} d \varepsilon \\
& \cdot \frac{1}{2} \int_{-1}^{1} g(\eta, \mu) d \mu \\
& (\alpha=0,1 \text { or } 2) \\
L^{11}= & \ell^{(0)} \\
L^{21}=T L^{12}= & -\frac{1}{e} \ell^{(1)} \\
L^{22}= & \frac{1}{e T^{2}} \ell^{(2)}
\end{aligned}
$$

where $e$ is electronic charge, $\tau$ is relaxation time, $D_{1}$ and $D_{2}$ are the thickness of quantum well layer and barrier layer respectively. The summation is over all the contributing carrier valleys and sub-bands. The notations of other symbols are the same as defined in ref. 10. The transport parameters, electrical conductivity $\sigma$, Seebeck coefficient $S$ and electron thermal conductivity $k_{e}$, can be expressed by the transport matrixes as:

$$
\begin{gathered}
\sigma=L^{(0)} \\
S=-\left(\frac{1}{e T}\right)\left(L^{(0)}\right)^{-1} L^{(1)} \\
k_{e}=\left(\frac{1}{e^{2} T}\right)\left(L^{(2)}-L^{(1)}\left(L^{(0)}\right)^{-1} L^{(1)}\right)
\end{gathered}
$$

In solving the energy integration, two-dimensional parabolic dispersion and the sub-band energy level for specularly scattered electrons is calculated by Kronig- Penny model. For the diffuse scattered electrons, three- dimensional parabolic dispersion of bulk Si is used. The effective mass components of Si can be found in many references $^{11,12}$ and the values used here are $m_{/ /}=0.916 m_{0}$ for longitudinal direction and $m_{\perp}=0.19 m_{0}$ for transverse direction. Band offset between Si layer and Ge layer is calculated with 'model solid theory'13 14, which gives the valence band offset between unstrained Si/Ge interface $\Delta E_{v}^{0}=0.68 eV$ and conduction band offset $\Delta E_{c}^{0}=0.22 eV$, where superscript ' 0 ' refers to unstrained state. For strained superlattice, average shift of conduction band extrema is:

$$
\Delta E_{c, A V}=\left(\Xi_{d}+\frac{1}{3} \Xi_{u}\right) \operatorname{Tr}(\tilde{\varepsilon})
$$

where $\tilde{\varepsilon}$ is the strain tensor, $\Xi_{d}$ is the dilation deformation potential and $\Xi_{u}$ is the uniaxial deformation potential. The Si/Ge superlattice semiconductor layers are biaxially strained in the plane of substrate by $\varepsilon_{/ /}$and uniaxially strained in the perpendicular direction by $\varepsilon_{\perp}$, which can be calculated by:

$$
\varepsilon_{/ /}=\frac{a_{s}}{a_{L}}-1
$$

$$
\varepsilon_{\perp}=\frac{-\varepsilon_{/ /}}{\sigma}
$$

where $a_{s}$ is the lattice constant of substrate, $a_{L}$ is the lattice constant of epilayer and $\sigma$ is Poisson's ratio. For the strained layer grown on (001) substrate,

$$
\sigma=\frac{c_{11}}{2 c_{12}}
$$

and

$$
\tilde{\varepsilon}=\left(\begin{array}{lll}
\varepsilon_{x x} & \varepsilon_{x y} & \varepsilon_{x z} \\
\varepsilon_{y x} & \varepsilon_{y y} & \varepsilon_{y z} \\
\varepsilon_{z x} & \varepsilon_{z y} & \varepsilon_{z z}
\end{array}\right)=\left(\begin{array}{ccc}
\varepsilon_{/ /} & 0 & 0 \\
0 & \varepsilon_{/ /} & 0 \\
0 & 0 & \varepsilon_{\perp}
\end{array}\right)
$$

where $c_{11}$ and $c_{12}$ is compliance constants. Band splitting among $\Delta$ valleys are therefore given by:

$$
\Delta E_{c}^{001}=\frac{2}{3} \Xi_{u}^{\Delta}\left(\varepsilon_{\perp}-\varepsilon_{/ /}\right)
$$

$$
\Delta E_{c}^{100,010}=-\frac{1}{3} \Xi_{u}^{\Delta}\left(\varepsilon_{\perp}-\varepsilon_{/ /}\right)
$$

and no split happens among $L$ valleys. Parameters, such as deformation potentials, lattice constants and compliance constants used in calculation are given in Table 1.

<table><tbody><tr><td colspan="3">Table 1 Constants used in band shift calculation</td></tr><tr><td></td><td>Si</td><td>Ge</td></tr><tr><td>Deformation potential (eV) ¹⁴</td><td></td><td></td></tr><tr><td>$E_{c}^{Δ}$</td><td>4.18</td><td>2.55</td></tr><tr><td>$E_{c}^{L}$</td><td>-0.66</td><td>-1.54</td></tr><tr><td>$Ξ_{u}^{Δ}$</td><td>9.16</td><td>9.42</td></tr><tr><td>$Ξ_{u}^{L}$</td><td>16.14</td><td>15.13</td></tr><tr><td>Lattice Constant (Å) ¹¹</td><td></td><td></td></tr><tr><td>$a_{L}$</td><td>5.4309</td><td>5.6461</td></tr><tr><td colspan="3">Substrate lattice constant (Vegard's law):</td></tr><tr><td colspan="3">$a_{s,Si(xGe)-x}=xa_{L,Si}+(1-x)a_{L,Ge}$</td></tr><tr><td>Compliance constants ($10^{12}$ dynes/cm²) ¹³</td><td></td><td></td></tr><tr><td>$c_{11}$</td><td>1.675</td><td>1.315</td></tr><tr><td>$c_{12}$</td><td>0.650</td><td>0.494</td></tr></tbody></table>

In constant relaxation time Boltzmann transport model, mobility is an averaged value that account for the major scattering mechanisms in bulk material. In our calculation, we take the mobility at 300K is $100cm^{2}/Vs$ for the doping level of about $10^{19}\sim 10^{20}cm^{-315,16}$ and ignore the mobility change at different doping levels. This simplification does not affect the model significantly since the optimum ZT are always be found at degenerate region where the carrier

concentration is around $10^{19} \mathrm{cm}^{-3}$. To investigate transport properties at different temperature, we applied two temperature dependent mobility relationships. Mobility of bulk Si is mainly determined by lattice scattering and impurity scattering. The lattice mobility in Bardeen-Shockley form $^{17}$ is:

$$
\mu_{L}=\frac{(8 \pi)^{0.5} \hbar^{4} c_{11}}{3 \varepsilon_{l n}^{2}\left(m_{n}^{*}\right)^{0.5}\left(k_{B} T\right)^{1.5}} \quad(15)
$$

where $\varepsilon_{l n}$ is the shift of edge of conduction band. The temperature variation of $\varepsilon_{l n}, m_{n}^{*}$ and $c_{11}$ can be neglected and the lattice mobility varies with temperature following the $T^{-1.5}$ law. The ionized impurity mobility, in Brook-Herring form, is:

$$
\begin{gathered}
\mu_{I}=\frac{2^{3.5}}{\pi^{1.5}} \frac{\chi^{2}\left(\kappa_{B} T\right)^{2.5}}{\left(m_{n}^{*}\right)^{0.5} e^{3} N_{I}} \frac{1}{\ln (1+b)-b /(1+b)}, \\
b=\frac{6}{\pi} \frac{\chi m_{n}^{*}\left(\kappa_{B} T\right)^{2}}{n \hbar^{2} e^{2}}
\end{gathered}
$$

where $\chi$ is Si dielectric constant, $N_{I}$ is the ionized impurity density. The combined mobility can be expressed as:

$$
\mu=\mu_{L} \int_{0}^{\infty} \frac{x^{3} \exp (-x)}{6 \mu_{L} / \mu_{I}+x^{2}} d x, \quad x=\frac{\varepsilon}{\kappa_{B} T}
$$

When $\mu_{L} \gg \mu_{I}$, the mobility-temperature $(\mu \sim T)$ relationship follows the $T^{-1.5}$ law, which is typical for non-degenerate semiconductors. However, experimental investigation by Morin and Maita $^{18}$ showed that as the impurity density increase, the mobility becomes small and less temperature dependent. Its temperature dependence can be described as $\mu \propto T^{-m}$ where $m$ decrease from 1.5 to 0 as impurity density increase. In the degenerate region, mobility dependence on temperature is rather weak and and approach $\mu=$ const. In our modeling, we applied two $\mu \sim T$ relationships for two extreme cases, $\mu=C T^{-1.5}$ for lattice scattering dominated case and $\mu=$ const. for lattice scattering and ionized impurity scattering jointly dominated (degenerate region) case. We expected that the degenerate region relationship to be more reasonable.

### Experiment
Three Si/Ge superlattice samples with different bi-layer thickness and doping levels have been grown and experimentally investigated. The samples were grown by solid source molecular-beam-epitaxy (MBE) technology on (100) oriented silicon-on-insulator (SOI) substrate. The superlattice layer is grown after 200nm alloy buffer layer graded to $\mathrm{Si}_{0.2} \mathrm{Ge}_{0.8}$ to provide lattice mismatch accommodation. To facilitate the measurement, a sample that has only the buffer layer was grown and measured for subtraction purpose. $^{19}$ The superlattice layer was homogeneously doped with Sb to $\sim 10^{19} \mathrm{~cm}^{-3}$. However, due to the structural difference, the open-and-close time of individual shutters in MBE chamber are different during different sample growth. This results in some variation of doping levels among the 3 samples. The structures of the 3 samples and their doping levels estimated from calibration are listed in Table 2.

<table>
<caption>Table 2 Si/Ge superlattice sample structures</caption>
<thead>
<tr>
<th>Sample</th>
<th>Periods</th>
<th>Si</th>
<th>Ge</th>
<th>Doping</th>
</tr>
</thead>
<tbody>
<tr>
<td>JL254</td>
<td>91</td>
<td>88Å</td>
<td>22 Å</td>
<td>$0.8×10^{19}\mathrm{cm}^{-3}$</td>
</tr>
<tr>
<td>JL255</td>
<td>133</td>
<td>60 Å</td>
<td>15 Å</td>
<td>$1.0×10^{19}\mathrm{cm}^{-3}$</td>
</tr>
<tr>
<td>JL256</td>
<td>250</td>
<td>32 Å</td>
<td>8 Å</td>
<td>$1.2×10^{19}\mathrm{cm}^{-3}$</td>
</tr>
</tbody>
</table>

To get the ZT value, we measured all three parameters: thermal conductivity, Seebeck coefficient and electrical conductivity along the in-plane direction. The in-plane thermoelectric measurement and data process method are given in ref. 19. The anisotropic thermal conductivity is measured by 2-wire $3 \omega$ method and the Seebeck coefficient and electrical conductivity is measured by the 4-point method.

![](./images/812381959677280257_1.jpg)

Figure 1. Powerfactor modeling with electron specularity $p_{e}=1.0$ and $p_{e}=0.7$ for the 3 Si/Ge superlattice structures, compared with measured power factor data at 300K.

![](./images/812381959677280257_2.jpg)

Figure 2. Experimental Seebeck coefficient of 3 Si/Ge superlattice compared theoretical results. (The dots represents)

experimental data and the lines are modeling results)

## Results and comparison
Figure 1 shows the plot of calculated powerfactor vs. carrier concentration for three Si/Ge superlattice structures at 300K. For each sample, two theoretical curves are presented which represent the result considering total quantum size effect ($p_e$=1.0) and quantum-classical combined size effect ($p_e$=0.7). The measured powerfactor data of the 3 samples are also shown in the figure as circle, square and diamond points for JL256, JL255 and JL254 respectively. For every specific structure, the difference between the $p_e$=1.0 and $p_e$=0.7 curves can be regarded as the degradation of the powerfactor by classical size effect. The figure clearly shows that as the period reduces, the "gap" between the two curves increases so that the classical size effect on the power factor degradation increases. The figure also shows that the measured data of the 3 samples lies in the region where both quantum and classical size effect are important.

Figure 2 shows the modeled Seebeck coefficient from 80K to 300K compared with the experimental data. Seebeck coefficient is independent of $\mu \sim T$ relationship, as given by eqn. 6. In the modeling, the electron specularity $p_e$ is taken as 0.7. It can be seen that, at most temperature points, the modeled Seebeck coefficients are quite close to the experimental data and the temperature dependent trend of Seebeck coefficient is reasonably captured by the model.

![](./images/812381959677280257_3.jpg)

Figure 3. Experimental electrical conductivity compared with theoretical results for samples (a) JL245 (b) JL255 and (c) JL256 (The dots represents experimental data and the lines are modeling results. For the theoretical modeling, two $\mu \sim T$ relationships are used, as discussed in the text. )

Figure 3(a), (b) and (c) are the modeled electrical conductivity vs. temperature compared with the experimental data for samples JL254, JL255 and JL256 respectively. The two lines are the theoretical modeling results using relationships $\mu = CT^{-1.5}$ and $\mu = const$ and the points are the experimental data. It is not surprising to see that the $\mu = CT^{-1.5}$ curve goes far away from the experimental data at low temperature and the $\mu = const$ curve is reasonably close to the experimental data at all temperature points. A better fitting can be obtained by using relationship$\mu = CT^{-n}$ , where $n$ is a number smaller than 1.0 that account for weak temperature dependence.

![](./images/812381959677280257_4.jpg)

Figure 4. Theoretical and experimental ZT values of the 3 samples (The theoretical phonon thermal conductivity is obtained using Chen's model with phonon specularity $p$=0.6 for JL256, $p$=0.5 for JL255 and $p$=0.45 for JL254).

In the low-dimensional system, thermoelectric enhancement benefits from two aspects: the powerfactor increase and the thermal conductivity reduction. A comprehensive investigation of the ZT enhancement of the superlattice requires that both the electronic and phonon transport to be characterized. For phonon transport in superlattice, Chen$^{20,21}$ present a model that emphasizes that the phonon interface scattering, rather than the group velocity reduction, is the main mechanism that makes the in-plane thermal conductivity much smaller than bulk value. The model is effective in both in-plane and cross-plane directions and is supported by the experimental data of anisotropic thermal conductivity measurement.$^{22}$ Using Chen's model, we can make a theoretical calculation of the phonon thermal conductivity for the three samples. In the calculation, the phonon scattering specularity $p_{ph}$ for each sample is the obtained from best experimental data fitting. The fitted specularity values are $p_{ph}$=0.6 for JL256, $p_{ph}$=0.5 for JL255 and $p_{ph}$=0.45 for JL254. A comprehensive theoretical modeling of thermoelectric figure-of-merit, ZT, can be obtained from the equation: $ZT = S^{2}\sigma T/k_{e}+k_{ph}$ , where the electronic thermal conductivity is given by eqn.7 and the $\mu = const$ relationship is applied for mobility temperature relationship. Figure 4 shows the modeled ZT


vs. temperature variation compared with the measured ZT data from the sample. Both experimental data and theoretical modeling demonstrated increased ZT with decreased period. However, it should be noticed that classical size effect are included in both phonon and electron transport in the modeling. For the phonon transport, the interface scattering causes in-plane thermal conductivity reduction and makes ZT increase. However, for the electron transport, less interface scattering is preferred since it may degrade the quantum enhancement effect. With the two scattering effects into consideration, the ideal structure for in-plane thermoelectric transport should have the interface property that can be totally specular for electron scattering and totally diffuse for phonon scattering. From the point of view of the competition of quantum and classical effects, superlattice structure with small interface diffusion and large band offset is good for low-dimensional enhancement. This is a factor that is determined by material property and growth technology and should be considered together with other factors such as carrier pocket degeneracy and confinement direction etc. in thermoelectric optimization.

## Conclusion

In this paper, we presented a theoretical model of classical size effect on in-plane thermoelectric transport. Electron Boltzmann transport equation is employed to establish a quantum-classical size effect combined model for electron transport along the in-plane direction in superlattices. The model is applied to calculate the transport properties of Si/Ge superlattice structures and compared with experimental data. Good agreement between modeling and experimental data indicates that interface scattering effect causes the degradation of thermoelectric properties of the Si/Ge superlattices. The classical size effect might possibly exist in other low- dimensional material systems and the model presented in this paper can be used as an effective tool for theoretical characterization. The combination of electron transport and phonon transport models shows that for the superlattice ZT enhancement, the interface scattering effects on both electron transport and phonon transport should be considered concurrently.

## Acknowledgement

This work is supported by ONR MURI on thermoelectrics (N00014-97-1-0516).

## References

1. L.D. Hicks and M. S. Dresselhaus, *Phys. Rev. B*, 47, 12727 (1993).
2. L.D. Hicks and M. S. Dresselhaus, *Phys. Rev. B*, 47, 16631 (1993).
3. J. O. Sofo and G. D. Mahan, *Appl. Phys. Lett.*, 65, 2690 (1994).
4. D. A. Broido and T. L. Reinecke, *Phys. Rev. B*, 51, 13797 (1995)
5. T. Koga, X. sun, S. B. Cronin, and M. S. Dresselhaus, *Appl. Phys. Lett.*, 75, 2438 (1999).
6. T.C. Harman, D.L. Spears, D.R. Calawa, S.H. Groves, and M.P. Walsh, *Proceedings ICT'97*, 416 (1997).

7. T. Koga, S.B. Cronin, M.S. Dresselhaus, J.L. Liu, and K.L Wang, *Appl. Phys. Lett.*, 77, 1490 (2000).
8. R. Venkatasubramanian, T. Colpitts, B. O'Quinn, S. Liu, N. ElMasry, and M. Lamvik, *Appl. Phys. Lett.* 75, 1104 (1999).
9. C. R. Tellier and A. J. Tosser, *Size Effects in Thin Films*, Elsevier Scientific, New York (1982).
10. W. L. Liu and G. Chen, *Proceedings of MRS 2001 Fall meeting*, Symposium G: Thermoelectric Materials 2001-- Research and Applications, G8.28 (2001).
11. N. W. Ashcroft and N. D. Mermin, *Solid State Physics*, Saunders College Publishing, Philadelphia (1976).
12. J. Singh, *Physics of Semiconductors and Their Heterostructures*, McGraw-Hill, (1993).
13. C. G. Van de Walle, *Phys. Rev. B.*, 39, 1871 (1989)
14. E. Kasper ed., Properties of Strained and Relaxed Silicon Geremanium, EMIS Datareviews Series No. 12 (1995)
15. C. Jacoboni, C. Canali, G. Ottaviani, and A. A. Quaranta, *Solid State Electron.* 20, 77 (1977)
16. S. S. Li and W. R. Thurber, *Solid State Electron.* 20, 609 (1977)
17. P. P. Debye and E. M. Conwell, *Phys. Rev.*, 93, 693 (1954)
18. F. J. Morin and J. P. Maita, *Phys. Rev.*, 96, 28 (1954)
19. W.L .Liu, T. Borca-Tasciuc, J. L. Liu, T. Koga, K. L. Wang, M. S. Dresselhaus, G. Chen, *Proceedings ICT'01*, 340 (2001).
20. G. Chen, *J. Heat Trans.*, 119, 220 (1997).
21. G. Chen, *Phys. Rev. B*, 57, 14958 (1998).
22. W.L .Liu, T. Borca-Tasciuc, G. Chen, J. L. Liu, and K. L. Wang, *J. of Nanoscience and Nanotechnology*, 1, 39 (2001).

---

134
21st International Conference on Thermoelectronics (2002)