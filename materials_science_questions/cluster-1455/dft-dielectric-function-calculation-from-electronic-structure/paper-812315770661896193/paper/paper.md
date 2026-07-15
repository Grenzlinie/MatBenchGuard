Invited Paper

# Mobility of Electrons and Holes in Semiconductors

G.D. Mahan

Department of Physics and Astronomy, The University of Tennessee, and
Solid State Division, Oak Ridge National Laboratory, and

B.A. Sanborn and P.B. Allen

Department of Physics, State University of New York at Stony Brook

## ABSTRACT

The mobility of electrons and holes is calculated in silicon as a function of temperature and the concentration of impurities. Calculations are done for both majority and minority carriers. Special care has been taken in the calculation of the contribution from impurity scattering. Both the dielectric function, and the local field corrections, have been calculated as a function of temperature and impurity concentration. The results agree with the data at low temperature, and at high doping at room temperature.

## 1. INTRODUCTION

Carrier mobility in doped semiconductors is limited primarily by scattering from ionized impurities and phonons$^{1-18}$. Here we present a calculation of mobility as a function of temperature and impurity concentration, and compare with experimental data. The scattering by phonons is generally well-understood, and we include the deformation potential scattering of acoustic and optical phonons.$^{1-2}$

The scattering of electrons and holes by ionized impurities is the most important limit on the mobility at high concentrations of doping$^{3-5}$. Here we have tried to improve the theoretical technology. The carriers scatter from the screened Coulomb potential of the impurity. A sophisticated model is taken for the screening from electron-electron interactions, which is calculated as a function of temperature and doping density. The scatterng is described by phase shifts which are calculated numerically. Our resulting mobilities should be an improvement over previous theories.

76 / SPIE Vol. 1679 Physics and Simulation of Optoelectronic Devices (1992)
0-8194-0840-9/92/$4.00

There have been many prior calculations of mobilities in semiconductors¹⁻¹³.
One landmark result was due to Rode¹⁻². He points out that in undoped semiconductors, theory does not agree with experiment unless one fiddles with the theoretical parameters. That is, one knows from independent ex- periments the values for the deformation potentials in silicon, and using those values gives the wrong mobility when compared with experiment. Theory and experiment continue to disagree for doped semiconductors. Past theories re- ported good agreement by adding various fudge factors, which are blamed on electron-electron interactions, etc. Here we leave out these fudge factors, and show results which do not always agree with experiment.

The degree of degeneracy of an electron gas may be characterized by the dimensionless temperature $\Theta = k_B T / E_F$, where $E_F$ is the Fermi degeneracy at zero temperature. In a multivalley semiconductor, such as silicon and germanium, the Fermi energy $E_F = \hbar^2(3\pi^2 n / n_{val})^{2/3} / 2m^*$ is smaller than it would be in a single valley at the same density. Multiple valleys push a semiconductor in the direction of nondegeneracy. Dandrea *et al.*¹⁹ found that $\Theta < 0.1$ defines the degenerate regime, while $\Theta > 10$ defines the nondegen- erate or classical regime. In between the electron gas is semidegenerate. In silicon at room temperature, $\Theta$ varies from 7.7 to 0.36 in the concentration range of $10^{18}$ to $10^{20}\ \text{cm}^{-3}$, putting doped silicon squarely in the region of semidegeneracy. This requires that all equations must be solved numerically.

## 2. THE BOLTZMANN EQUATION

The mobility is calculated by solving a transport equation for the motion of electrons and holes in an applied electric field. For the majority carriers, the distribution function $F(\vec{k})$ is assumed to be slightly disturbed from the equilibrium distribution $f(\vec{k}) = 1/(\exp[(\varepsilon(k) - \mu)/k_B T] + 1)$. The latter depends upon temperature $T$ and the chemical potential $\mu(T)$.

$$
F(\vec{k}) = f(\vec{k}) + e \vec{\mathcal{E}} \cdot \hat{k} g(k). \tag{1}
$$

Here $g(k)$ is the unknown change in the distribution function. It is found by solving the semiclassical Boltzmann's equation

$$
\frac{\partial f}{\partial k} = -\frac{g(k)}{\tau(k)} + \sum_{\vec{k}'} g(k') \hat{k} \cdot \hat{k}' \{ S(\vec{k}', \vec{k})[1 - f(k)] + S(\vec{k}, \vec{k}') f(k) \}, \tag{2}
$$

$$
\frac{1}{\tau(k)} = \sum_{\vec{k}'} \{ S(\vec{k}, \vec{k}')[1 - f(k')] + S(\vec{k}', \vec{k}) f(k') \} \tag{3}
$$


The functions $S(\vec{k}, \vec{k}')$ determine the rate of scattering according to Fermi's Golden Rule. We use standard expressions for the scattering by phonons $^{1-2}$. This includes acoustic and optical phonons, and intravalley and intervalley scattering. For carrier scattering by acoustical phonons, we assume the scattering is elastic. This assumes that $k = k'$, and that the relaxation approximation is valid for the electron scattering rate. However, for optical scattering, we retain the inelastic nature of the scattering. Then we solve (2) using Rode's iterative process. This method has the virtue that no assumptions nor approximations are made for $g(k)$: one just solves it on the computer.

### 3. IMPURITY SCATTERING

Impurity scattering is elastic and does not change the energy of the electron. The impurity is taken to be a point charge, and a screened interaction is obtained from modern theories of electron-electron interactions. These theories produce a screened electrostatic potential $V(r)$. The scattering of the electron from this potential is described by phase shifts $\delta_{\ell}(k)$, which determine the mobility. Both $V(r)$ and $\delta_{\ell}(k)$ are found by numerical solution. Similar calculations were reported earlier Saso and Kasuya $^{3}$.

For an impurity of charge $Z$, the screened potential in the Random-Phase Approximation (RPA) is
$$
V(r)=Z \int \frac{d^{3} q}{(2 \pi)^{3}} \frac{v_{q}}{\epsilon_{R P A}(q)} \exp (i \vec{q} \cdot \vec{r}), \tag{4}
$$

$$
\epsilon_{R P A}(q)=1-v_{q} \frac{m^{*} n_{v a l}}{\hbar^{2} \pi^{2}} \int_{0}^{\infty} k d k \frac{\partial f(k)}{\partial k} W\left(\frac{q}{2 k_{F}}\right), \tag{5}
$$

$$
W(x)=\frac{1}{2}+\frac{1}{4 x}\left(1-x^{2}\right) \log \left|\frac{x+1}{x-1}\right|, \tag{6}
$$

$$
v_{q}=4 \pi e^{2} / q \epsilon_{\infty}. \tag{7}
$$

Standard notation is used for the effective mass $m^{*}$ and high-frequency dielectric constant $\epsilon_{\infty}$. The energy bands were assumed to be isotropic.

The total charge in the screening cloud must cancel the impurity charge. This requirement is given by the Friedel sum rule, which at nonzero temperatures is expressed as an integral over the band energies
$$
Z=\frac{2 n_{v a l}}{\pi k_{B} T} \sum_{\ell}(2 \ell+1) \int_{0}^{\infty} d E \delta_{\ell}(E) f(E)[1-f(E)]. \tag{8}
$$


![](./images/812315770661896193_1.jpg)

Figure 1: Electron mobility in n-type silicon at 300K. Labels denote: TF is Thomas-Fermi potential with $q_s$ given by Thomas-Fermi value, F is Thomas Fermi potential with $q_s$ determined by Friedel sum rule, RPA is using screened potential and RPA dielectric function, STLS is screened potential using LFC dielectric function, ps is phase shift, and Born is second Born approximation.

We also calculated this value to check violations of the Friedel rule.

We also compared our result to other standard methods of computing the mobility from impurity scattering. One technique is to assume a Thomas-Fermi potential $V_{TF}(r) = Ze^2 \exp(-q_s r)/\epsilon_\infty r$. The screening constant $q_s$ can be given either by the Thomas-Fermi value$^{20}$, or else chosen to fit the Friedel Sum Rule (8). Another approximation is not to use phase shifts, but instead approximate $S(\vec{k},\vec{k}')$ by the second Born approximation. Using the Thomas-Fermi model in the second Born Approximation gives the Brooks-Herring formula for the transport lifetime

$$
\frac{1}{\tau_{i}^{B H}(k)}=\frac{2 \pi m^{*} Z^{2} e^{4}}{\hbar^{3} k^{3} \epsilon_{\infty}} N_{i}[\log (1+y)-\frac{y}{1+y}], \tag{9}
$$

$$
y=4 k^{2} / q_{s}^{2}. \tag{10}
$$

The density of impurities is $N_i$. Some numerical results are shown in fig.1 at 300 K and fig.2 for 77 K, and compared with the experimental data of Masetti et al.$^{17}$ and Yamanouchi et $al^{14}$ RPA results agree well with the data at 77 K. The label 'ps' denotes phase shift, while 'Born' denotes the second Born approximation. The label 'Fps' is the Thomas-Fermi model

![](./images/812315770661896193_2.jpg)

Figure 2: Electron mobility of n-type silicon at 77K. See fig.1 for labels.

where the Friedel sum rule is used to determine the screening length $q_s$.
These mobilities are higher, and in worse agreement when compared with experiment, than those "TFps' where the Thomas-Fermi approximation is used for $q_s$. However, none of the theories agree with experiment at 300 K in the range of low concentration.

Figure 3 shows the value of the Friedel sum rule (8). It should be unity for a consistent theory. However, the RPA results violate this rule badly at 77K, and less so at 300 K. The symbol LTFA applies to the case that the Thomas-Fermi screening wave vector is used for $q_s$. This case also violates the Friedel rule. Then one can vary $q_s$ to make the Friedel rule valid for each value of temperature and doping. However, fig.1 shows that this increases the mobility, and worsens the agreement betrweens theory and experiment.

Electron-electron interactions have been included in this calculation for their contribution to dielectric screening. However, they have not been in- cluded for their lifetime due to carrier-carrier scattering. Some prior calculations $^{7-8}$ concluded it was a small effect, while Fischetti $^{13}$ thought it was a big effect. We are in the process of including it in our calculations. The present results are preliminary, and the final results will include electron-electron interac- tions.

### 4.LOCAL FIELD CORRECTIONS

Better calculations of mobility are obtained with better impurity poten- tials $V(r)$. Improvements in this function can come from adding central cell

![](./images/812315770661896193_3.jpg)

Figure 3: Friedel sum rule vs. concentration. RPA potentials for the impurity are compared to the Thomas-Fermi approximation. The ratio $q_{TF}/\bar{k}$ is the screening length divide by the mean kinetic energy of the thermally excited electrons.

corrections, or else improving the dielectric function. Here we have tested the latter choice. Historically, the Thomas-Fermi and RPA are old theories. Nowadays most dielectric functions have local field factors $G(q)$ introduced by Hubbard$^{20}$. Then the proper screened potential for the electron scattering from an impurity, including vertex corrections$^{21}$ $\Gamma(q)=1/[1+v_qG(q)P(q)]$, has the form

$$
\frac{\epsilon_{LFC}(q)}{\Gamma(q)}=1-v_q[n_{val}-G(q)]\frac{m^*}{\hbar^2\pi^2}\int_0^\infty kdk\frac{\partial f(k)}{\partial k}W\left(\frac{q}{2k_F}\right). \tag{11}
$$

The local field correction was calculated at nonzero temperatures using the method of Singwi et al.$^{22-23}$, which solves a coupled set of equations which include the static structure factor $S(q)$

$$
G(q)=-\frac{1}{n}\int\frac{d^3q'}{(2\pi)^3}\frac{(-\vec{q}\cdot\vec{q}')}{q'^2}[S(\vec{q}+\vec{q}')-1], \tag{12}
$$

$$
S(q)=-\frac{1}{nv_q}\int\frac{d\omega}{\pi}\frac{1}{1-e^{-\beta\omega}}\Im\left[\frac{1}{\epsilon_{LFC}(q,\omega)}\right]. \tag{13}
$$

These numerical results for the mobility are also shown in fig.1 & 2. Local field effects cause a negligible difference from RPA, which has also been found in other calculations$^{21}$.


![](./images/812315770661896193_4.jpg)

Figure 4: Ratio of noninteracting to interacting compressibilities of the con- duction electrons in silicon as a function of concentration. The vertical lines show where $\Theta=1$. Note the negative values for $77K$.

## 5.COMPRESSIBILITY

The compressibility $K$ of an electron gas is defined as the derivative of the pressure with respect to the volume. It can also be defined as the long wave length limit of the dielectric function $^{20}$

$$
\lim _{q \rightarrow 0} \epsilon(q)=1+v_{q} n^{2} K. \tag{14}
$$

We can use our solutions for $G(q)$ to see what compressibility is predicted in doped silicon. It is usually compared to the noninteracting result $K_{free}=$ $3/(2nE_F)$. At room temperature we find that $K$ is positive, but it is negative at $77$ K for a wide range of impurity density. Usually this signals an instability in the electron gas. This result is shown in fig.4. We continue to investigate this interesting observation.

## 6. MINORITY CARRIERS

We are also calculating the mobility of minority carriers in silicons. So far we have included the contributions from scattering by phonons and im- purities. These results are shown in fig. 5.

It has been known from the work of McLean and Paige $^{24-25}$ that electron hole scattering is an important contribution to the mobility of minority car- riers. The majority carriers 'drag' the minority carriers. We are still working

![](./images/812315770661896193_5.jpg)

Figure 5: Calculated mobility of electrons as minority carriers in p-type silicon. Top curve is RPA, while lower curve is Thomas-Fermi. Both use the phase-shift method.

on this aspect of the calculation, and our results are incomplete without them.

### 7. ACKNOWLEDGEMENTS

GDM acknowledges research support from The University of Tennessee, and from the U.S. Departmernt of Energy through contract DE-AC05-84OR21400 administered by Martin Marietta Energy Systems Inc. Work at SUNYSB was supported in part by NSF grant DMR 9118414.

### 8. REFERENCES

1. D.L. Rode, Phys. Rev. B **2**, 1012-1024, 4036-4043 (1970)

2. D.L. Rode, in *Semiconductors and Semicmetals*, ed. R.K. Richardson and A.C. Beer (Academic Press, 1975 ) Vol. 10, Chap.1

3. T. Saso and T. Kasuya, J. Phys. Soc. Jpn. **48**, 1566-1575 (1980); **49**, 578-588 (1980)

4. J.R. Meyer and F.J. Bartoli, Phys. Rev. B **23**, 5413-5427 (1981)

5. H.S. Bennett, Solid State Elec. **26**, 1157-1166 (1983)

6. D.E. Burk and V. de la Torre, IEEE EDL-5, 231-233 (1984)

7. J.R. Meyer and F.J. Bartoli, Phys. Rev. B **36**, 5989-6000 (1987)

8. B.E. Sernelius, Phys. Rev. B **41**, 3060-3068 (1990)

9. W. Walukiewicz, Phys. Rev. B **41**, 10218-10220 (1990)

10. K.C. Kwong, N.Y. Du, J. Callaway and R.A. LaViolette, Phys. Rev. B **41**, 12666-12671 (1990)

11. M.E. Law, E. Solley, M. Liang and D.E. Burk, IEEE EDL-**12**, 401-403 (1991)

12. B.E. Sernelius and E. Söderström, J. Phys. CM **3**, 8425-8431 (1991)

13. M.V. Fischetti, Phys. Rev. B **44**, 5527-5534 (1991)

14. C. Yamanouchi, K. Mizuguchi and W. Sasaki, J. Phys. Soc. Jpn **22**, 859 (1967)

15. C. Jacoboni, C. Canali, G. Ottaviana, and A.A. Quaranta, Solid Stat Elec. **20**, 77-89 (1977)

16. Landolt Börnstein, New Series **17a** (Springer-Verlag, 1982)

17. G. Masetti, M. Severi, and S. Solmi, IEEE ED-**30**, 764 (1983)

18. J. del Alamo, S. Swirhum, and R.M. Swanson, Solid State Elec. **28**, 47054 (1985)

19. R.G. Dandrea, N.W. Ashcroft, and A.E. Carlsson, Phys. Rev. B **34**, 2097 (1986)

20. G.D. Mahan, *Many-Particle Physics*, Sec. Ed. (Plenum, 1990)

21. G.D. Mahan and B.E. Sernelius, Phys. Rev. Lett. **62**, 2718 (1989)

22. K.S. Singwi, M.P. Tosi, R.H. Land, and A. Sjölander, Phys. Rev. **176**, 589 (1968)

23. P. Vashishta and K.S. Singwi, Phys. Rev. B **6**, 875 (1972)

24. T.P. McLean and E.G.S. Paige, J. Phys. Chem. Solids. **16**, 220 (1960)

25. R.A. Höpfel, J. Shah, P.A. Wolff, and A.C. Gossard, Phys. Rev. Lett. **56**, 2736 (1986)