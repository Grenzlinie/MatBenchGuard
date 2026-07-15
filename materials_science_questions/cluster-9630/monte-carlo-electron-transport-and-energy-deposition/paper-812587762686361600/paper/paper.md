# Multiple coupled charge layers in electron beam induced charging phenomenon

Cite as: J. Appl. Phys. 128, 024902 (2020); https://doi.org/10.1063/5.0006488
Submitted: 03 March 2020 . Accepted: 22 June 2020 . Published Online: 14 July 2020

C. Li, H. M. Li, and Z. J. Ding

![](./images/812587762686361600_1.jpg) ![](./images/812587762686361600_2.jpg) ![](./images/812587762686361600_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

Thermoelectric transport control with metamaterial composites
Journal of Applied Physics 128, 025104 (2020); https://doi.org/10.1063/5.0004037

Super-Planckian radiative heat transfer between macroscale metallic surfaces due to near-field and thin-film effects
Journal of Applied Physics 128, 025305 (2020); https://doi.org/10.1063/5.0008259

Defect properties of solar cells with layers of GaP based dilute nitrides grown by molecular beam epitaxy
Journal of Applied Physics 128, 023105 (2020); https://doi.org/10.1063/1.5134681

![](./images/812587762686361600_4.jpg)

J. Appl. Phys. 128, 024902 (2020); https://doi.org/10.1063/5.0006488
128, 024902

© 2020 Author(s).

# Multiple coupled charge layers in electron beam induced charging phenomenon

Cite as: J. Appl. Phys. 128, 024902 (2020); doi: 10.1063/5.0006488
Submitted: 3 March 2020 · Accepted: 22 June 2020 ·
Published Online: 14 July 2020

![](./images/812587762686361600_5.jpg)

C. Li, $^{1}$ H. M. Li, $^{2,a)}$ and Z. J. Ding $^{1,a)}$

## AFFILIATIONS
$^{1}$ Hefei National Laboratory for Physical Sciences at Microscale and Department of Physics, University of Science and Technology of China, Hefei, Anhui 230026, People's Republic of China
$^{2}$ Super Computation Center, University of Science and Technology of China, Hefei, Anhui 230026, People's Republic of China

$^{a)}$Authors to whom correspondence should be addressed: hmli@ustc.edu.cn and zjding@ustc.edu.cn

## ABSTRACT
We report a discovery of the multiple coupled charge layer phenomenon in an insulating solid, $SiO_{2}$, when irradiated by an electron beam with the aid of a Monte Carlo method. In tracing the transporting electrons, their encountered elastic, inelastic, and phonon scatterings, in conjunction with the influence of the electric field, are incorporated to model their transport more accurately. In handling charging, we consider the trapping of holes and energy-exhausted electrons on their drift paths, with the use of the electric-field-dependent drift velocity and trapping cross section. The emission of secondary electrons is modified by considering their trapping on the emission paths. Besides, the trapped charges may become detrapped under the electric field, which is also taken into account. Totally, six (three coupled) alternating charge layers are formed, with each layer having a thickness of about $0.1\ \mu$m, being parallel to the sample surface and existing merely along the beam incidence axis. The first layer is positive and is formed by secondary electron emission, while the sixth layer is negative and is formed by the extensive trapping of primary electrons. The middle four layers are formed by charge drift, in which electrons and holes move to opposite directions. However, the layer number remains unchanged with the increasing primary energy, since the charging involved in the simulation is negative, in which the primary electrons of different energies would be decelerated to a similar landing energy of 2–3 keV.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0006488

## I. INTRODUCTION
Trapped charge distribution is an important issue since charge trapping is the origin of charging phenomenon, $^{1,2}$ which can change the image contrast in scanning electron microscopy (SEM). $^{3}$ Methods applicable to measuring trapped charge distribution, such as the mirror-deflection imaging in SEM $^{4}$ and the capacitance–voltage measurement, $^{5,6}$ can barely provide more information than the lateral location of the trapped charges and their total quantity. The exception is the acoustic and the thermal methods in that they allow the quantitative measurement of the trapped charge distribution along both lateral and depth directions, $^{7}$ but their spatial resolutions are currently in the micrometer order, $^{8–10}$ making them unable to reveal nanoscale features of the trapped charge distribution.

Physically, the primary electrons penetrating into the sample lose their kinetic energies continuously on their paths toward deeper regions to excite secondary electrons until negative charges are accumulated there when their energies are exhausted; on the other hand, positive charges left behind by secondary electron generation will appear in a shallower layered region due to the emission of secondary electrons. A simple phenomenological theory, the dynamic double layer model, $^{11}$ was proposed for the postulated charge distribution according to this physical picture.

In this paper, we report our discovery that the complexity involved in charging, i.e., the charge trapping and detrapping and the drift of holes and energy-exhausted electrons driven by the electric field, leads to the multiple layer distribution, which is rather more sophisticated than the postulated dynamic double layer distribution by the ideal theoretical model. The Monte Carlo method, the most suitable theoretical technique for investigating the electron–solid interactions, $^{12–17}$ is employed in this paper to calculate the trapped charge distribution by taking into account the comprehensive physical processes in charging phenomenon. $^{18,19}$


## II. ELECTRON TRANSPORT THEORY

Handling the electron transport in a solid sample should come first in simulating the charging phenomenon. In what follows, main points of the electron transport theory used in our Monte Carlo method, including elastic, inelastic and phonon scattering, resulting from electron-nucleus, electron-electron, and electron-lattice interactions, respectively, are recalled in brief. More details of the electron transport theory can be found in our previous work. $^{18,19}$

### A. Electron elastic scattering

The electron elastic scattering is described by the Mott cross section $^{20}$ calculated with the Thomas-Fermi-Dirac atomic potential, $^{21}$

$$
\frac{d \sigma_{\mathrm{e}}}{d \Omega}=|f(\theta)|^{2}+|g(\theta)|^{2}, \quad(1)
$$

where the scattering amplitudes,

$$
\begin{aligned}
& f(\theta)=\frac{1}{2 i k} \sum_{\ell=0}^{\infty}\left\{(\ell+1)\left(e^{2 i \delta_{\ell}^{+}}-1\right)+\ell\left(e^{2 i \delta_{\ell}^{-}}-1\right)\right\} P_{\ell}(\cos \theta), \\
& g(\theta)=\frac{1}{2 i k} \sum_{\ell=1}^{\infty}\left\{-e^{2 i \delta_{\ell}^{+}}+e^{2 i \delta_{\ell}^{-}}\right\} P_{\ell}^{1}(\cos \theta),
\end{aligned}
$$

are calculated by the partial-wave expansion method. $^{22}$ In Eq. (2), $P_{\ell}(\cos \theta)$ and $P_{\ell}^{1}(\cos \theta)$ are the Legendre and the first-order associated Legendre functions, respectively; $\delta_{\ell}^{+}$and $\delta_{\ell}^{-}$are the spin-up and spin-down phase shifts of the $\ell$ th partial wave, respectively.

### B. Electron inelastic scattering

The electron inelastic scattering is described by a dielectric functional approach, with the double differential scattering cross section given by

$$
\frac{d^{2} \lambda_{\text {in }}^{-1}}{d(\hbar \omega) d q}=\frac{1}{\pi a_{0} E} \operatorname{Im}\left\{\frac{-1}{\varepsilon(q, \omega)}\right\} \frac{1}{q}, \quad(3)
$$

where $\lambda_{\text {in }}$ is the electron inelastic mean free path (IMFP), $\hbar \omega$ is the energy loss, $\hbar q$ is the momentum transfer, $a_{0}$ is the Bohr radius, $E$ is the electron energy, and $\varepsilon(q, \omega)$ is the dielectric function of the sample. The energy loss function, $\operatorname{Im}\{-1 / \varepsilon(q, \omega)\}$, is modeled by Lorentz oscillators, $^{23}$

$$
\operatorname{Im}\left\{\frac{-1}{\varepsilon(q, \omega)}\right\}=\operatorname{Im}\left\{\frac{-1}{1+\sum_{j} \chi_{j}(q, \omega)}\right\}, \quad(4)
$$

where $\chi_{j}(q, \omega)$ is the complex electronic susceptibility of the $j$ th oscillator,

$$
\chi_{j}(q, \omega)=\Omega_{j}^{2} \frac{f_{j}}{\omega_{j}^{2}(q)-\omega^{2}-i \omega \Gamma_{j}(q)}, \quad(5)
$$

where $\Omega_{j}=\sqrt{4 \pi n_{j} e^{2} / m}$ ( $m$ is the electron mass) is the plasma frequency; $f_{j}, \omega_{j}(q)$, and $\Gamma_{j}(q)$ are oscillator parameters, which can be obtained from the following dispersion relations:

$$
\hbar \omega_{j}(q)=\hbar \omega_{j}(0)+\alpha \hbar^{2} q^{2} / m, \quad(6)
$$

$$
\Gamma_{j}(q)=\Gamma_{j}(0)\left(1+\beta q^{2}\right), \quad(7)
$$

where $\alpha$ and $\beta$ are constants, depending on the material $(\alpha \approx 0$ and $\beta \approx 6 \AA^{2}$ for $\mathrm{SiO}_{2}$ ); $f_{j}, \omega_{j}(0)$, and $\Gamma_{j}(0)$ can be obtained by fitting the optical energy loss function, $\operatorname{Im}\{-1 / \varepsilon(0, \omega)\}$, to the experimental data. $^{24}$

For insulating materials, the influence of bandgap is taken into account by rewriting the energy loss function as $^{25}$

$$
\operatorname{Im}\left\{\frac{-1}{\varepsilon(q, \omega)}\right\}=\operatorname{Im}\left\{\frac{-1}{1+\sum_{j} \chi_{j}(q, \omega)}\right\} \theta\left(\hbar \omega-E_{\mathrm{g}}\right), \quad(8)
$$

where $E_{\mathrm{g}}=8.9 \mathrm{eV}$ for $\mathrm{SiO}_{2}$. In inelastic scattering, the energy loss of the transporting electrons $\hbar \omega$ will be transferred to the electrons in the sample, giving rise to the excitation of secondary electrons. The Heaviside step function on the right side of Eq. (8) requires $\hbar \omega$ to exceed $E_{\mathrm{g}}$, which is to guarantee that the electrons in the valence band of insulating materials can be excited to the conduction band, thus forming secondary electrons. It can also be inferred from Eq. (8) that the electron-electron interactions for transporting electrons with energy below $E_{\mathrm{g}}$ are absent, as validated by the vanishing values of the optical energy loss function (OELF) in this energy range for $\mathrm{SiO}_{2} \cdot{ }^{19}$ This reduced electron-electron interaction will increase the electron IMFP, which in conjunction with the small surface emission barrier (i.e., the electron affinity) makes the electron yield of insulating materials $^{26,27}$ much higher than that of semiconducting and conducting materials. $^{27-29}$

### C. Electron-phonon interaction

In fact, below $E_{\mathrm{g}}$ OELF of $\mathrm{SiO}_{2}$ still shows two sharp peaks but at very low energies, $\hbar \omega_{1}=0.063 \mathrm{eV}$ and $\hbar \omega_{2}=0.153 \mathrm{eV}$, corresponding to two longitudinal optical (LO) phonon modes. In principle, the electron-LO phonon interaction can be described by the Fröhlich time-dependent perturbation theory, ${ }^{30,31}$ and in $\mathrm{SiO}_{2}$, the frequencies of an electron of energy $E$ and effective mass $m^{*}$ to create and annihilate the LO phonon of energy $\hbar \omega, f^{+}$and $f^{-}$, are, respectively, given by $^{32}$

$$
f^{+}=(n+1) \frac{1}{\hbar^{2}} \sqrt{\frac{m^{*}}{2 E}} \frac{e^{2}}{4 \pi \varepsilon_{0}}\left(\frac{1}{\varepsilon_{\infty}}-\frac{1}{\varepsilon}\right) \hbar \omega \ln \frac{1+\sqrt{1-(\hbar \omega / E)}}{1-\sqrt{1-(\hbar \omega / E)}},
$$

$$
f^{-}=n \frac{1}{\hbar^{2}} \sqrt{\frac{m^{*}}{2 E}} \frac{e^{2}}{4 \pi \varepsilon_{0}}\left(\frac{1}{\varepsilon_{\infty}}-\frac{1}{\varepsilon}\right) \hbar \omega \ln \frac{1+\sqrt{1+(\hbar \omega / E)}}{-1+\sqrt{1+(\hbar \omega / E)}},
$$

where $\varepsilon$ and $\varepsilon_{\infty}$ are the static and optical dielectric constants ( $\varepsilon=3.9$ and $\varepsilon_{\infty}=2.25$ for $\mathrm{SiO}_{2}$ ). With Eqs. (9) and (10), both $f^{+}$ and $f^{-}$decrease continuously with increasing electron energy,

implying that LO phonons mainly dominate the energy loss for low-energy electrons, especially for those electrons with an energy below $E_g$ since their energy-loss channel by electron-electron interaction is shut down in Eq. (8). In the simulation, the interactions with those two LO-phonon modes mentioned above for the electrons with an energy below 30 eV have been taken into account with Eqs. (9) and (10). In addition to the energy loss, the interactions with LO phonons will result in the change in the electron transport direction, but the involved scattering angle is mostlyrather limited, as the forward scattering is dominant. $^{32}$

On the other hand, in $SiO_{2}$, there also exists acoustic phonons. Opposite to LO phonons, the influence of acoustic phonons is mainly concerned with the change in the electron transport direction, while the energy loss can be neglected due to the small energy of acoustic phonons. Thus, the electron-acoustic-phonon interactions are actually an elastic process. Furthermore, in $SiO_{2}$, the acoustic-phonon scattering frequency increases as the electron energy ranges from 0 eV to about the Brillouin-zone boundary, $^{33}$ but decreases as the electron energy ranges from 8 eV to $16 eV^{34}$ Thus, the electron-phonon interaction is dominated by LO phonons in a low electron energy range, e.g., below the Brillouin-zone boundary, but acoustic phonons come into play when the electron energy is between the Brillouin-zone boundary and tens of electrovolts. In addition, the change in the electron transport direction in interactions with acoustic phonons will naturally lead to the change in electron transport length and hence to the change in electron-LO phonon interactions. This is responsible for the slight broadening of the Si 2 p photoelectron peak emitted from a $SiO_{2}$ film grown on a Sisubstrate induced by photon illumination. $^{34}$

In contrast to the broadening of the photoelectron peak mentioned above, acoustic phonons could make the narrower secondary electron peak in the emitted electron energy spectrum. $^{35}$ In addition, the authors pointed out that taking acoustic phonons into account would not bring any change to the simulated electron yield under electron irradiation. $^{35}$ Furthermore, it is of interest to see that our simulated electron yield of $SiO_{2}$ under electron irradiation $^{19}$ agrees with experiments, even though acoustic phonons are neglected. Besides, by using the similar approach to handle the low- energy electron transport, the simulated electron yield of CsI under photon illumination using the Monte Carlo method $^{36}$ also approximately reproduced the experimental result.

On the other hand, the secondary electron emission (SEE) depth is very limited and is independent of primary energy. In our simulation of $SiO_{2}$, the emitted secondary electrons are mostly originated from a depth lower than 5 nm (not shown here). Note that this SEE depth is greater than that of conducting and semiconducting materials, which is mostly smaller than $1 nm.^{37}$ Nevertheless, in SiO,, this limited SEE depth in conjunction with the facts on the electron yield mentioned above implies that the influence of acoustic phonons on electron transport is not obvious; otherwise, the electron transport in the SEE region will be changed greatly, and this will lead to the disappearance of the agreement on the electron yield between experiments and the simulation, without taking acoustic phonons into account.

In addition, the inner-shell ionization and Auger electron generation have not been taken into account in our Monte Carlo algorithm. Obviously, the reliability of charging simulation is concerned with the accurate record of the total charge quantity accumulated in the sample and their spatial distribution, and the accuracy of the recorded values of these quantities could be improved by appropriately considering the inner-shell ionization and Auger electron generation. However, Auger electrons occupy only a very small proportion in all excited electrons in the sample, due to which the emitted electrons are mostly secondary electrons and backscattered electrons. Auger electrons only manifest themselves as a rather small signal peak in the energy spectrum of emitted electrons. Thus, neglecting Auger electrons is reasonable in the charging problem.

### III. CHARGING SIMULATION MODELING
Electron transporting in a solid sample would slow down due to the occurrence of inelastic and LO-phonon scatterings. The trace of electron transport will be terminated when the kinetic energy of an electron is exhausted, that is, the energy becomes lower than a critical low value. Those energy-exhausted electrons together with the holes left by secondary electron generation will hereafter be referred to as deposited charges and can drift under an electric field. Note that those deposited charges are possible to be trapped on their drift paths by different kinds of trapping sites, thus forming a trapped charge distribution. Besides, the low- energy secondary electrons can also be trapped on their emission paths, and on the other hand, the trapped charges can be detrapped if the surrounding electric field is sufficiently intense. These aspects have been taken into account in our charging simulation modeling and more details about this section can be foundin our previous work. $^{18}$

The trapping sites in solids have mainly three kinds of origin, i.e., defects, impurities, and self-trapping sites. For $SiO_{2}$ , the defects that have been well characterized include the $E^{\prime}$ center, the peroxy radical and the non-bridging oxygen hole center (NBOHC). $^{38}$ The E' center is usually formed by trapping a hole at an oxygen vacancy $^{39}$ and this positively charged center can then trap electrons, while NBOHC is a hole trap. In addition to the ones mentioned above, several other kinds of defects can be induced by electron beam irradiation and those defects may transform between each other. $^{40}$ On the other hand, the doped elements in $SiO_{2}$ , e.g., Ge, Li, P, and B etc., are the impurities. In particular, the doped Ge substitutes Si; it has been theoretically shown by density functional theory calculations that an electron can be trapped at the doped Ge site and it increases the Ge-O bond length and the O-Ge-O bond angle by repelling the adjacent oxygens. $^{41}$ In contrast, the doped Li resides close to the Si site and an electron is trapped at the Si site, similarly increasing the Si-O bond length and the O-Si-O bond angle. In particular, the Coulombic interaction between the trapped electron and the doped Li improves the trapping stability of the electron at the Si site. $^{41}$ In addition to the impurities mentioned above, it has been experimentally found that electrons in $SiO_{2}$ can be trapped by the Na impurities. $^{42,43}$ Meanwhile, in pure $SiO_{2}$ , electrons and holes can also become self-trapped; electrons can be self trapped at the Si site, $^{41}$ while holes can be either self-trapped at a single bridging oxygen or delocalized over two equivalent bridgingoxygens of the same $SiO_{4}$ tetrahedron. $^{44}$

### A. Trapping of the drift charges

In the experimental study of electron drift in $SiO_2$, $^{45,46}$ a linear increase in the drift velocity, with the mobility being about $20\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$, when the electric field is increased from 0 to $0.7\ \text{MV cm}^{-1}$ has been observed, whereas beyond this range, the drift velocity becomes roughly saturated, with the saturated drift velocity being about $1.4\times 10^7\ \text{cm s}^{-1}$. Therefore, the electron drift velocity in the simulation is set as

$$
\mathbf{v}_{\mathrm{e}}= \begin{cases}-\mu_{\mathrm{e}} \mathbf{E}, & |\mathbf{E}|<0.7 \mathrm{MV} \mathrm{cm}^{-1}, \\ -v_{\mathrm{es}} \mathbf{E} /|\mathbf{E}|, & |\mathbf{E}| \geq 0.7 \mathrm{MV} \mathrm{cm}^{-1},\end{cases}
\tag{11}
$$

where $\mu_{\mathrm{e}}$ is the electron mobility of $\mathrm{SiO}_{2}$, $\mathbf{E}$ is the electric field vector, and $v_{\mathrm{es}}$ is the saturated electron drift velocity of $\mathrm{SiO}_{2}$; we set $\mu_{\mathrm{e}}=20\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ and $v_{\mathrm{es}}=1.4\times 10^7\ \text{cm s}^{-1}$. In contrast, the hole mobility of $\mathrm{SiO}_{2}$, $\mu_{\mathrm{h}}$, has been experimentally found to be almost independent of the electric field, and it is set in the simulation as the experimentally measured value of $\mu_{\mathrm{h}}=2\times 10^{-5}\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}^{46,47}$
The hole drift velocity is then given by

$$
\mathbf{v}_{\mathrm{h}}=\mu_{\mathrm{h}} \mathbf{E}.
\tag{12}
$$

To take the trapping of drift charges into account, a uniform distribution of the trapping sites in the sample is assumed, with the trap depth, $U$, modeled by a Gaussian function,

$$
f(U)=\frac{1}{\sqrt{2 \pi} \sigma_{\mathrm{t}}} \exp \left\{-\frac{\left(U-\mu_{\mathrm{t}}\right)^{2}}{2 \sigma_{\mathrm{t}}^{2}}\right\},
\tag{13}
$$

where $\mu_{\mathrm{t}}=1.5\ \text{eV}$ is the mean trap depth and $\sigma_{\mathrm{t}}=1.0\ \text{eV}$ is the standard deviation. It is also assumed $^{48}$ that the drift charges can only be trapped by either an empty trapping site or a trapping site occupied by an opposite charge.

The trapping capacity of the trapping sites is quantified by their trapping cross section. Experimentally, the trapping cross section of the drift electrons by the Coulomb attractive trapping sites is found to decrease when the applied electric field is increased, $^{49}$ due to electron heating and lowering of the trapping barrier; an analytical expression fitted from the experiment $^{49}$ is used to model the trapping cross section of the drift electrons by the hole-occupied trapping sites when the electric field exceeds $0.5\ \text{MV cm}^{-1}$,

$$
\sigma_{\mathrm{ch}}=\{18.92 \exp (-|\mathbf{E}| / 0.41)+0.037\} \times 10^{-13} \mathrm{~cm}^{2},
\tag{14}
$$

where $|\mathbf{E}|$ is in $\text{MV cm}^{-1}$; for $|\mathbf{E}|<0.5\ \text{MV cm}^{-1}$, $\sigma_{\text{eh}}=5\times 10^{-13}\ \text{cm}^2$.

However, the dependence of the trapping cross section of drift holes by the empty trapping sites on the electric field has been experimentally found to be weak, $^{50}$ so that it is set as $\sigma_{\mathrm{h} 0}=3\times 10^{-14}\ \text{cm}^2$. In addition, the trapping cross section of the drift electrons by the empty trapping sites and that of the drift holes by the electron-occupied trapping sites are set as $\sigma_{\mathrm{e} 0}=10^{-14}\ \text{cm}^2$ and $\sigma_{\mathrm{he}}=3\times 10^{-13}\ \text{cm}^2$, respectively.

On the other hand, the respective numbers of the empty, electron-occupied, and hole-occupied trapping sites are saved for all the subregions in the sample that are divided prior to the simulation. The total trapping cross section of a particular subregion for the drift electrons (holes) can be given by

$$
\begin{aligned}
& \sigma_{\mathrm{e}}=\sigma_{\mathrm{e} 0} n_{0}+\sigma_{\mathrm{eh}} n_{\mathrm{h}}, \\
& \sigma_{\mathrm{h}}=\sigma_{\mathrm{h} 0} n_{0}+\sigma_{\mathrm{he}} n_{\mathrm{e}},
\end{aligned}
\tag{15}
$$

where $n_{0}$ is the empty trapping site density and $n_{\mathrm{h}}$ ($n_{\mathrm{e}}$) the hole-occupied (electron-occupied) trapping site density. Then, the trapping step length for the drift electrons (holes) can be known,

$$
\begin{aligned}
& s_{\mathrm{e}}=-\ln R_{1} / \sigma_{\mathrm{e}}, \\
& s_{\mathrm{h}}=-\ln R_{1} / \sigma_{\mathrm{h}},
\end{aligned}
\tag{16}
$$

where $R_{1}$ is a random number. In this work, all random numbers are uniformly distributed in $(0,1)$.

Obviously, Eqs. (11) and (12) determines the drift direction, along which the drift charge is trapped when it finishes one drift step, with the length determined from Eq. (16). Once the trapping occurs, a random number $R_{2}$ is needed to determine whether the charge is trapped by an empty trapping site or a trapping site occupied by the opposite charge. In particular, the drift electron (hole) is trapped by an empty trapping site if $R_{2}<\sigma_{\mathrm{e} 0} n_{0} / \sigma_{\mathrm{e}}$ ($R_{2}<\sigma_{\mathrm{h} 0} n_{0} / \sigma_{\mathrm{h}}$), in which one is subtracted from the number of empty trapping sites of the subregion in which trapping occurs and one is added to the number of electron-occupied (hole-occupied) trapping sites. Otherwise, the drift electron (hole) is trapped by a hole-occupied (electron-occupied) trapping site. In this latter case, the drift electron (hole) is recombined with a previously trapped hole (electron) and these two charges disappear from the simulation; then, the number of empty trapping sites increases by one, and the number of hole-occupied (electron-occupied) trapping site decreases by one.

### B. Trapping of the transporting secondary electrons

We also take into account the trapping of the secondary electrons transporting in the region beneath the sample surface down to a depth of $15\ \text{nm}$ and having energies below $3.5\ \text{eV}$, which is to model the SEE more accurately. Similar to the deposited electrons, those secondary electrons can be trapped by the empty or hole-occupied trapping sites, and the corresponding cross section is set as $\sigma_{\mathrm{e} 0}^{\star}$=$5\times 10^{-15}\ \text{cm}^2$ and $\sigma_{\mathrm{eh}}^{\star}$=$10^{-13}\ \text{cm}^2$, respectively.

Then, the total trapping cross section is given by

$$
\sigma_{\mathrm{e}}^{\star}=\sigma_{\mathrm{e} 0}^{\star} n_{0}+\sigma_{\mathrm{eh}}^{\star} n_{\mathrm{h}}.
\tag{17}
$$

And, the corresponding trapping step length is

$$
s_{\mathrm{e}}^{\star}=-\ln R_{3} / \sigma_{\mathrm{e}}^{\star},
\tag{18}
$$

where $R_{3}$ is a random number. Note that we begin to count the transport length for a secondary electron when its energy decreases to $3.5\ \text{eV}$, and its trapping occurs when the transport length exceeds the trapping step length. Also, by sampling a random number $R_{4}$, the secondary electron is trapped by an empty trapping site if $R_{4}<\sigma_{\mathrm{e} 0}^{\star} n_{0} / \sigma_{\mathrm{e}}^{\star}$, or otherwise by a hole-occupied trapping site. In addition, the number of empty, electron-occupied, and hole-

occupied trapping sites undergoes the same change as that in the trapping of a drift electron.

### C. Detrapping
The trap depth can be reduced in the electric field, with the reduction magnitude given by $^{51,52}$
$$
\Delta U=2 \sqrt{\frac{e^{3}|\mathbf{E}|}{4 \pi \varepsilon_{0} \varepsilon_{\mathrm{r}}}},
\tag{19}
$$
where $\varepsilon_{\mathrm{r}}$ is the relative dielectric constant of the sample. Obviously, the charges trapped by sites with depths shallower than $\Delta U$ would become detrapped. Furthermore, the detrapped charges are assumed to be uniformly distributed in the corresponding subregion and thereafter are treated as drift charges.

### D. Computation procedure
The procedure listed below is followed in simulating the charging phenomenon induced by primary electron irradiation.
(1) Consider the irradiation of $N$ primary electrons within a short time interval $\tau$ on a surface region of area $a$, corresponding to the current of $Ne/\tau$ and the current density of $Ne/\tau a$. The landing energy of primary electrons is added by $eV_{\mathrm{s}}$, where $e=1.6 \times 10^{-19} \mathrm{C}$ and $V_{\mathrm{s}}$ is the surface potential at the incidence site.
(i) Simulate the transport of these $N$ primary electrons and the cascaded secondary electrons until they escape from the sample surface, trapped by the trapping sites or become deposited in the sample when their energy decreases below the sample's affinity, $\chi(\chi=0.9 \mathrm{eV}$ for $\mathrm{SiO}_{2}$). The energy of the emitted electrons is added by $-eV_{\mathrm{s}}$ at the emission site, and all the emitted electrons are assumed to be detected.
(ii) When tracing the electron transport, save the positions of the deposited electrons and holes (their detailed generation time within $\tau$ is not counted). Note that the influence of the electric field on electron trajectory and energy is also taken into account in the same manner as in our previous work. $^{19}$
(2) With the total charge distribution, i.e., the sum of the deposited charges obtained in (1) and all the charges left by the previous irradiations, obtain the spatial potential distribution using the mono-image charge method. $^{19}$
The potential calculation is focused on the configuration of a semi-infinite sample which is covered above by a vacuum. Due to the long-range nature of the potential, only the potential in a limited space is calculated. This limited potential calculation space is taken as a cuboid, with its center being at the primary electron irradiation center on the sample surface and its upper surface being parallel to the sample surface. In order not to influence the charge drift, the cuboid should be big enough to accommodate all the charges; its length, width, and height are in the size of several micrometers or larger, depending on the primary energy. Furthermore, in practical calculations, the cuboid is divided into numerous non-uniform grids to numerically save the distributions of charge, potential, and electric field, and the size of a particular grid is gradually increased with its increasing distance to the primary electron irradiation center. With the knowledge of the charge quantity in each grid, the mono-image charge method $^{19}$ can then be applied, in which one image charge is required to be set in the space for the charge ensemble in each grid and the potential is calculated as the summation between the potential generated by the grid charge ensemble and that by the image charge. In particular, the position and charge quantity of the image charge can be determined by requiring the potential to satisfy the boundary condition on the sample surface, $\mathbf{e}_{\mathrm{n}} \cdot \mathbf{D}_{\mathrm{s}}=\mathbf{e}_{\mathrm{n}} \cdot \mathbf{D}_{\mathrm{v}}$, where $\mathbf{e}_{\mathrm{n}}$ is the unit surface normal vector, $\mathbf{D}_{\mathrm{s}}$ is the electric displacement vector in the sample and close to the sample surface, and $\mathbf{D}_{\mathrm{v}}$ is the electric displacement vector in vacuum and close to the sample surface. Note that in our previous work $^{18}$ the potential calculation was also done in this same manner and the calculated surface potential, determined from the shift of the secondary electron peak, agreed well with the experiment, suggesting the reliability of the potential calculation.
(3) Obtain the detrapping ratio of the trapped charges as $\int_{\Delta U^{\prime}}^{\Delta U} f(U) d U / \int_{\Delta U^{\prime}}^{U_{\max }} f(U) d U$, where $\Delta U$ and $\Delta U^{\prime}$ are calculated using Eq. (19) and are, respectively, the decrements in trap depth in the present and last time intervals. $U_{\max }$ is the trap depth maximum, which is set as $U_{\max }=3.5 \mathrm{eV}$.
(4) Simulate the drift of the charges. Here, the charges include those newly deposited in (1), those generated in the previous irradiations but have not been trapped and those have detrapped in (3). The drift time is counted for each of them, and if a charge is still drifting when the drift time reaches $\tau$, its position at $\tau$ will be saved as the start position for its next drift induced by the updated electric field in the subsequent time interval.
(5) Repeat (1)-(4) to calculate the irradiation in the next time interval until the total irradiation time reaches the requirement.

## IV. RESULTS AND DISCUSSION
The Monte Carlo method is then applied to study the charging of a semi-infinite $\mathrm{SiO}_{2}$ sample induced by the irradiation by a normally incident primary electron beam, with the focus placed on the trapped charge distribution. The current intensity and the diameter of the primary electron beam are taken as $0.1 \mathrm{nA}$ and $0.1$ $\mu \mathrm{m}$, respectively, and the trapping site's density as $2 \times 10^{9} \mathrm{~cm}^{-3}$. Figure 1 shows the trapped charge distributions obtained at six time instants for the primary beam of $5 \mathrm{keV}$, in which the density value of a particular region with volume $V$ is given by $\left(N_{\mathrm{h}}-N_{\mathrm{e}}\right) / V$, where $N_{\mathrm{h}}$ and $N_{\mathrm{e}}$ are, respectively, the trapped hole number and the trapped electron number there. These images sequenced in time clearly show the evolution of the trapped charge distribution with time until the steady state is reached in Fig. 1(f). The most remarkable and inconceivable feature in Fig. 1 is the appearance of the alternating positive and negative charge layers. All the charge layers are parallel to the sample surface, exist merely along the incidence axis of the primary electron beam and have the

![](./images/812587762686361600_6.jpg)

FIG. 1. The distribution of the trapped charges in the semi-infinite SiO₂ under irradiation by a normal and continuous primary electron beam of 5 keV. The sample is bounded by z < 0, above which is vacuum. (a)–(f) show the distributions obtained at six time instants: (a) 2.02 ms; (b) 14.69 ms; (c) 24.48 ms; (d) 34.56 ms; (e) 44.93 ms; and (f) 57.02 ms.

thickness of about 0.1 $\mu$m. The separated charge layers are coupled positive and negative, and the layer with a smaller depth is formed earlier. Besides the positively charged surface layer, holes are mostly located in the inner region compared to the extensive trapping of electrons, since hole mobility$^{46,47}$ is about six orders of magnitude smaller than electron mobility$^{53}$ although the latter tends to decrease under the electric field.$^{45,46}$

To confirm that the formation of the alternating charge layers is not due to the particular combination of the values of the parameters, mobility and drift velocity, we have performed test simulations for the charge distributions induced by 5 keV electron beam irradiation with the different sets of mobility and drift velocity values (the test results are not shown here). In the first two tests, the hole mobility was increased by two and four orders of magnitude as compared to the value used in Fig. 1, while other parameters were unchanged. In these two tests, six similar alternating charge layers were formed but the thickness became smaller for each layer. In the third test, both the electron mobility and the saturated electron drift velocity were reduced by half, five alternating charge layers were also found in a reduced range. Since these two parameters are important for the simulation and any change of them will inevitably alter the simulation result, the layer thickness and the layer numbers. However, despite them, the nature of alternating charge layers does not change; it can be concluded that the formation of the alternating charge layers is independent of the particular set of mobility and drift velocity.

It is worth noting that the Monte Carlo method we used is actually a bulk model, in which the trapping sites playing as recombination centers are set in the sample. However, due to the surface states, formed by dangling bonds, surface contaminations, and surface defects etc. and located within the forbidden band, there also exists a certain distribution of recombination centers on the sample surface. The point is that the distribution of the surface recombination centers, both location and density, is rather uncertain and may vary over a large range by the surface condition that relates to many factors, such as sample composition, sample preparation, and experimental condition. Despite the involved uncertainties, surface recombination provides an extra channel for terminating charge motion and will shorten the charge life, especially for minority charges in semiconducting materials.

Here, we wish to elucidate that the influence of surface recombination on our simulation is rather limited due to two main reasons. First, in comparing with semiconducting materials, the charge motilities are much lower in insulating materials, making the charge drift in insulating materials more difficult. Second, in the charging condition induced by primary electron irradiation, the involved electric field is not uniform and has rather complicated directions, further increasing the difficulty for charges, especially the ones located deep inside, to reach the sample surface. In particular, the charging involved in Fig. 1 will be clarified to be negative in the following, such that more negative charges are contained in the sample than positive charges at any time instant. Since the first layer is positive, the total charge ensemble beneath the first layer is absolutely negative, leading the z-component of the electric field in the first layer region to point downwards (see Fig. 2).

Due to those two reasons, it can be expected that only the holes deposited very close to the sample surface with a limited amount and a portion of the electrons deposited in the first layer region have the opportunity to reach the sample surface and to be involved in surface recombination. On the other hand, in Fig. 1, the first charge layer remains positive during the entire course of primary electron irradiation. This first positive layer is believed to

![](./images/812587762686361600_7.jpg)

FIG. 2. The variation of the trapped charge distribution within a small time interval of $1\ \mu s$ starting from 34.56 ms. The electric field distribution within this time interval is also shown, with the field direction denoted by the arrow direction and the field strength by the arrow length. Symbols R1-R10 denote the different regions for the convenience of the discussion in the text.

be resulted from SEE, and holes dominate the charge accumulation in the SEE region. However, the thickness of the first layer is about $0.1\ \mu m$, much thicker than the SEE region (see Sec. II C). A reasonable interpretation for the thickness difference is the further drift of the holes, which extends their distribution range. In this regard, in the first layer region, holes are the majority charges and electrons are the minority charges, and hence, the amount of the electrons that can be involved in surface recombination is also limited.

In fact, the similar alternating charge layers have also been found in our previous work $^{19}$ for the trapped charge distribution of irregular nanoparticles, where the charge layers are approximately ring-shaped modulated by the particle geometry. In that simulation, the used primary energy is 1 keV and the special nanoparticle geometry enhances the SEE, such that the involved charging is positive. In principle, the mechanism for positive charging to become steady is to attract a portion of the emitted low-energy secondary electrons back to the sample surface by the electric field, leading the outmost layer to be negative. In this work, the simulation is focused on negative charging at higher primary energies, in which SEE suffers no impediment but instead is enhanced by negative surface potential, making the first layer positive. Furthermore, the previously obtained ring-shaped layer is thinner, due to the manner used there to handle charge trapping is relatively simple. In contrast, the charge trapping in this work is expected to be more accurate, with the use of the field-dependent drift velocity and trapping cross section.

It can be realized that our Monte Carlo method is based on tracing the motion of the charges step by step by regarding the charges as classical particles. In fact, there exists another approach in charging study, which is based on describing the related physical processes including primary electron incidence and transport, secondary electron generation and transport, SEE, charge trapping and detrapping, and charge recombination, as electric currents. $^{51,52}$ Flow of these currents should obey the continuity equation and would result in the change in the spatial charge distribution. However, this current-based approach applied only to the one-dimensional condition, e.g., the charging of a semi-infinite bulk due to the irradiation by a normally incident defocused primary electron beam. $^{51,52}$ Raftari et al. $^{54}$ developed a two-dimensional model, with the current-based approach, to study the charging of a semi-infinite bulk due to the irradiation by a normally incident primary electron beam. However, in this two-dimensional model, the detailed primary and secondary electron transport are not included. It is assumed that the charges generated in primary electron irradiation become thermalized within a small time interval after the incidence of the primary electrons, and an analytical formula is used to describe the thermalized charge distribution, which is actually the injected charge source. Once the thermalized charges are presented, they begin to transport due to drift and diffusion, which is handled in the cylindrical coordinate system. In Ref. 54, the simulation of the charging of a semi-infinite $SiO_2$ due to long time scale primary electron irradiation at 1 keV shows that the trapped electron distribution and the trapped hole distribution extend along lateral and depth directions as time goes on, and their density maxima are reached almost everywhere in the spatial distribution range. In the steady state of charging, the trapped electron distribution and the trapped hole distribution share quite similar distribution features, both spatial range and density. Thus, the potential generated by the trapped electrons approximately cancels that generated by the trapped holes, leading the charging there to be mainly induced by the non-trapped charges in the steady state. This is different from our result that in our simulation the potential is mainly generated by the trapped charges, since the non-trapped electron density and the non-trapped hole density are so low that they can be neglected. In our opinion, this difference is due to the different recombination manners. Specifically, the recombination in Ref. 54 occurs between the non-trapped electrons and the non-trapped holes, while the recombination in our simulation occurs between the non-trapped charges and the trapped charges (see Sec. III). Since the trapped electrons and the trapped holes are not involved in recombination in Ref. 54, their density maxima would be reached soon, and as time goes on, the ranges of the trapped charge distribution extend.

From here on, we begin to elucidate how the alternating charge layers in Fig. 1 are formed. Note that the charging effect manifested in SEM imaging, electron yield measurement and many other experiments, is usually related to the involved electric field. In the present simulation, the electric field not only distorts the trajectories of the transporting electrons but also drives the charges to drift along the electric field line. In this regard, the role of the electric field in the formation of the alternating charge layers is likely important.

It has to be noted that the trapped charge distribution at a particular time instant in Fig. 1 is formed due to the primary electron irradiation in a large time interval, i.e., from the very beginning to the considered time instant. If this large time interval is divided into numerous identical small time intervals, the considered trapped charge distribution is numerically equal to the integral of the trapped charge distribution variation over all the divided small time intervals. On the other hand, the electric field changes dynamically with the continuous primary electron irradiation. Nevertheless, within a small time interval, the electric field can be

regarded as static by taking it as the zero order of its real dynamic value. Based on these two aspects, elucidating the relation between the trapped charge distribution at a particular time instant and the dynamic electric field can be transformed to elucidating the relation between the trapped charge distribution variation and the static electric field within a small time interval.

Following this spirit, we present in Fig. 2 the variation of the trapped charge distribution within a small time interval in conjunc- tion with the involved electric field. The selected time interval starts from $t_{1}=34.560$ ms and ends at $t_{2}=34.561$ ms, with the time interval being $1 \mu s$ . Furthermore, the variation of the trapped charge distribution $\Delta \rho_{t}$ is given by $\Delta \rho_{t}(r)=\rho_{t}(r, t_{2})-\rho_{t}(r, t_{1})$ , where $\rho_{t}$ is the trapped charge density and $r$ is the position vector of a point in the sample. In particular, in Fig. 2, the positive values(positive variations) represent net hole accumulation or net electron loss, while the negative values (negative variations) represent net electron accumulation or net hole loss. The point is that the varia- tion, positive or negative, depends strongly on the electric field direction that positive variation occurs in a particular region if the surrounding electric fields point inwards, say in regions R5, R7, R9, and R10, and negative variation occurs if they point outwards, say in regions R2 and R8.

Naturally, the variation of the trapped charge distribution is directly due to the continuous beam irradiation, which is the princi- pal power to propel the evolution of the trapped charge distribution by depositing positive and negative charges in the sample. This alsoholds for the variation within a limited time interval. Figure 3(a) shows the distribution of the electrons deposited within the same time interval as that of Fig. 2, where the presence of the lateral elec- tron density stripes is very unusual. As shown in Fig. 3(b), the dis- tribution of the holes deposited within the same time interval is quite similar to Fig. 3(a) on the intensity, spatial range, and stripe. For comparison, we present in Fig. 4 the distributions of the charges deposited within the same time interval as that of Fig. 2 without taking charging into account, where the distributions are smooth without any stripes. This enables the stripes in Fig. 3 to be accounted for by the electric-field-induced electron trajectory distor- tion. Furthermore, in Fig. 5, we present the distributions of the charges deposited within an earlier $1 \mu$ s time interval, starting from3.513 ms and ending at 3.514 ms. It can be seen that Fig. 5 is quite similar to Fig. 3, but its distribution range exceeds that in Fig. 3. However, the distribution range of Fig. 5 is exceeded by that in Fig. 4. That is to say, the involved charging results in the continuous compression of charge deposition range with the increasing time. It can be inferred, however, from this fact that the involved charging is negative, in which the incident primary electrons are decelerated by the negative surface potential. To see this intuitively, we present in Fig. 6 the evolution of the surface potential and the maximum dep- osition depth of electrons with time at the primary energy of 5 keV. In Fig. 6, the involved charging can be confirmed to be negative by the negative surface potential, and depending on the deceleration degree, which is proportional to the absolute surface potential, the maximum deposition depth of electrons decreases from the initial $\sim 0.5 \mu m$ (charging free case) to the saturated $\sim 0.22 \mu m$ .

After the charges become deposited, they will drift along the electric field line until they are trapped or recombined. An impor- tant physical quantity that needs to be noted is the drift length, $s_{d}=-\ln R_{S} / \sigma$ , where $R_{S}$ is the random number and $\sigma$ is the total trapping cross section. The drift length represents the distance from the position where the charge is deposited to the position where it is trapped or recombined, and is dynamically related not only to the trapped charge distribution but also to the electric field. $^{18}$ Despite the difference between the drift length of electrons and that of holes, their magnitude is mostly lower than $0.1 \mu m$ in this simulation, as shown by the counted drift length for charges deposited in a particular region in Fig. 7. Based on the short drift lengths shown in Fig. 7, it can be inferred that the deposited charges in Fig. 3 could barely drift to regions R7-R10 and hence the density variations there have another origin. This origin is believed to be the charge detrapping. Figures 8(a) and 8(b) show, respec- tively, the distributions of electrons and holes detrapped from the trapping sites within the same time interval as Fig. 2. Clearly, the detrapped charges in Figs. 8(a) and 8(b) are distributed much more extensively than the deposited charges in Fig. 3. In particular, R8 suffers an obvious negative variation of the trapped charge density in Fig. 2, which can be accounted for by hole detrapping, since in Fig. 8(b) R8 has an appreciable intensity. Therefore, although the deposited charge densities in Figs. 3(a) and 3(b) are much higher

![](./images/812587762686361600_8.jpg)

FIG. 3. The distribution of the charges deposited within the same time interval as in Fig. 2: (a) deposited electrons; (b) deposited holes.

![](./images/812587762686361600_9.jpg)

FIG. 4. The distribution of the charges deposited within the same time interval as in Fig. 2 without taking charging into account: (a) deposited electrons; (b) deposited holes.

![](./images/812587762686361600_10.jpg)

FIG. 5. The distribution of the charges deposited within the time interval (from 3.513 ms to 3.514 ms): (a) deposited electrons; (b) deposited holes.

![](./images/812587762686361600_11.jpg)

FIG. 6. The evolution of the surface potential (solid square) and the maximum deposition depth of electrons (solid circle) as a function of the beam irradiation time at the primary energy of 5 keV.

![](./images/812587762686361600_12.jpg)

FIG. 7. The distribution of the drift length of electrons (solid square) and holes (solid circle) deposited within the same time interval as in Fig. 2 and within the spatial range of $-0.12\ \mu\text{m} < x < 0.12\ \mu\text{m}$, $-0.12\ \mu\text{m} < y < 0.12\ \mu\text{m}$, and $-0.22\ \mu\text{m} < z < -0.12\ \mu\text{m}$.

![](./images/812587762686361600_13.jpg)

FIG. 8. The distribution of the charges detrapped from the trapping sites within the same time interval as in Fig. 2. (a) detrapped electrons; (b) detrapped holes.

than the detrapped ones in Figs. 8(a) and 8(b), it is the detrapped charges that mainly contribute to the variation of the trapped charge density in deep regions.

So far, the two kinds of charge origins, i.e., charge deposition and charge detrapping, have been clarified; it is now suitable to elu- cidate the relation between the trapped charge distribution varia- tion in Fig. 2 and the involved electric field. Essentially, the charges in Figs. 3 and 8 form a mixture of electrons and holes, and they will drift under the electric field demonstrated in Fig. 2. For R1-R3, the electric field component therein, which is parallel to the sample surface and pointing to either $-x$ or $+x$ axis, pushes holes forwards to R1 and R3 and pulls electrons backwards to R2, thus contribut- ing to the negative variation of the trapped charge density in R2. The negative variation in R2 is also related to R5, as holes in R2 are pushed downwards to R5 and electrons in R5 are pulled upwards to R2 by the $z$-component of the electric field. However, such charge flows between R1 and R4 and between R3 and R6 are quite limited, since the $z$-component of the electric field is rather weak at their boundaries. Different from R1-R3 and R5, where the charges either deposited or detrapped contribute to the variations, those in R4, R6, R7-R10 are mainly contributed by the detrapped charges. The charge flow also occurs between R4 and R7 and between R6 and R9. R8 mainly suffers hole detrapping and the electric field therein pushes the holes outwards to the surrounding regions, such that a negative variation of the trapped charge density occurs there. Near the outmost edges of regions R7, R9 and R10, a weak electron detrapping occurs, as shown in Fig. 8(a), and their drift outwards to farther regions results in the extension of the trapped charge dis- tribution in Fig. 1. Note that the densities of both the deposited charges and the detrapped charges are much stronger than the vari- ation of trapped charge density in Fig. 2, implying these charges are mostly recombined.

Thus, it becomes clear that the charge drift, in which electrons and holes move to opposite directions, induces the specific varia- tion of the trapped charge distribution in Fig. 2. Again, since the trapped charge distribution at any time instant in Fig. 1 can be numerically seen as the integral of numerous such variations in Fig. 2, the charge drift is also crucial for the formation of the trapped charge distribution. From this point, an interpretation for the formation of the alternating charge layers can be given. At first, the first layer is positive and is formed by SEE, whereas its thick- ness is broadened by hole's drift. The sixth layer is negative and is formed by the trapping of the primary electrons. In fact, these twolayers are the foundation of the dynamic double layer model. $^{11}$  Furthermore, for the region beneath but adjacent to the first layer, the electric field therein is expected to be more determined by the first layer than others, leading its direction to point approximately downwards (see Fig. 2). This electric field allows the electrons to be attracted upwards and holes to be pushed downwards, giving rise to the formation of a negative layer, i.e., the second layer, there. Similarly, the second layer attracts the holes in regions beneath and adjacent to it upwards and pushes the electrons therein downwards, giving rise to the formation of the third layer, which is positive. Naturally, the formation of the rest two layers, i.e., the fourth layer and the fifth layer, can be understood in the same manner.

Furthermore, with this interpretation, the layer thickness can be naturally related to the charge drift length. For the middle four layers, as detailed above, they are due mainly to the opposite drift of electrons and holes, allowing their thickness to be determined approximately as the summation of the electron drift length and the hole drift length. Say, in Fig. 7, the counted charges are taken from a particular region approximately located in the second layer and their drift-length summation can be taken as $0.1\ \mu m$, corre- sponding approximately to the thickness of the second layer. Note that the drift length distributions in Fig. 7 should be time depen- dent due to the dynamic nature of the trapped charge distribution. However, from Figs. 1(b)-1(f), the trapped charge distribution does not change greatly and this stage occupies a majority time ratio in the entire primary electron irradiation. Thus, it can be expected that the charge drift length in any particular region remains approximately unchanged in most of the time during primary electron irradiation. In turn, the thickness of the second layer and other layers in Fig. 1 also remains approximately unchanged in most of the time. On the other hand, in Fig. 7, the overall electron drift length exceeds that of holes, since the second layer has been mostly occupied by trapped electrons when counting the drift lengths of the charges deposited there. However, the con- dition is expected to become the opposite that the overall hole drift

![](./images/812587762686361600_14.jpg)

FIG. 9. The distribution of the trapped charges in the semi-infinite SiO₂ under irradiation by a normal and continuous primary electron beam of 10 keV. (a)-(f) show the distributions obtained at six time instants: (a) 25.92 ms; (b) 55.29 ms; (c) 81.21 ms; (d) 112.32 ms; (e) 155.51 ms; and (f) 211.10 ms. Other conditions are the same as in Fig. 1.

length exceeds that of electrons or the drift-length summation is dominated by holes for the regions that have been mostly occupied by trapped holes (see Sec. III). This applies to the first, third and fifth layers. Due to the similar trapping cross sections used in han- dling the trapping of electrons and holes and the similar trapped charge density in different layers in Fig. 1, the hole drift lengths in those three positive layers and the electron drift length in the fourth layer would be similar to the electron drift length in Fig. 7, thus the layer thickness is similar to each other among the upper five layers. However, the sixth layer is more extensive, since it is formed due mainly to the trapping of the extensively distributed primary electrons.

![](./images/812587762686361600_15.jpg)

FIG. 10. The distribution of the trapped charges in the semi-infinite SiO₂ under irradiation by a normal and continuous primary electron beam of 15 keV. (a)-(f) show the distributions obtained at six time instants: (a) 144.00 ms; (b) 230.40 ms; (c) 288.00 ms; (d) 345.60 ms; (e) 518.40 ms; and (f) 633.60 ms. Other conditions are the same as in Fig. 1.

On the other hand, the formation of the charge layers outside the deposition region would be due mainly to the drift of the detrapped charges. This enables the later appearance of the deeper charge layers to be understood. For example, growing of the positive layer located around $z=-0.5\ \mu\text{m}$ (the fifth layer) in Fig. 1(c) with charge detrapping requires the electric field to be sufficiently intense and the sample has to undergo the continuous beam irradiation for a certain period of time to make the condition satisfied. In addition, in contrast to the simple electric field near the beam incidence axis, pointing roughly along the $z$ axis, the electric field in the lateral regions far away from the beam incidence axis has more complicate directions, leading to the more complicated charge drift there and thus to the failure of the formation of the alternating charge layers.

In addition, we have also performed the simulation with the increased primary electron energies of 10 keV and 15 keV. Figures 9 and 10 show the evolutions of the trapped charge distribution in these two cases, respectively, in which Figs. 9(f) and 10(f) correspond to the steady state of charging. In comparing with Fig. 1, the trapped charge distribution in Figs. 9 and 10 has similar features, and it is of interest to see that in steady states Figs. 9(f) and 10(f) also show totally six alternating positive and negative (or three coupled) charge layers with the similar distribution range. This is considered in principle to be related to the deceleration of primary electrons in negative charging. In particular, the magnitude of the deceleration is proportional to that of the steady surface potential $|V_{\text{s}}(+\infty)|$, and the landing energy of the primary electrons on the sample surface is $E_{1}=E_{\text{p}}-e|V_{\text{s}}(+\infty)|$. It is worth mentioning that in negative charging $E_{1}$ is almost independent of $E_{\text{p}}$ because as has been validated both theoretically $^{18}$ and experimentally, $^{55}$ $|V_{\text{s}}(+\infty)|$ is approximately proportional to $E_{\text{p}}$. Furthermore, $E_{1}$ ranges 1-3 keV for most of insulating materials. $^{26,55}$
Figure 11 shows the evolutions of the surface potential in the 10 keV and 15 keV cases as a function of time. It can be found that the surface potential saturates at about $-7.6$ kV in the 10 keV case and at about $-11.8$ kV in the 15 keV case, resulting in the corresponding landing energy of 2.4 keV and 3.2 keV, respectively. Meanwhile, in the 5 keV case, the landing energy would be 2.5 keV (see Fig. 6). Thus, the similar landing energies among these cases result in the same number of charge layers and similar distribution ranges.

Since negative charging is usually encountered at relatively high primary energies, the involved trapped charge distribution could occupy in the sample a space with an appreciable size, as shown by the micrometer-order depth in Figs. 1, 9, and 10. This brings great difficulty for completely eliminating negative charging by using the low-energy flooding technique with a certain kind of positively charged particle or the laser-illumination technique with the laser energy below $E_{\text{g}}$, since they can barely recombine or release the charges trapped deeply. Although difficult, this work is still expected to be helpful for developing new strategies to eliminate negative charging more effectively by providing the necessary knowledge about how the trapped charges in the sample are distributed in the nanometer scale. Note that the gridding size for the charge distribution in the charge-layer region is very fine, $\sim$10 nm in depth dimension. When the size is coarsened to $\sim$200 nm, the second and the third layers will be averaged with the charge density being about zero, and so do the fourth and the fifth layers. In this coarse averaging, only the first and the sixth layers are left and our simulation result would be reduced to the simple dynamic double layer model; however, the surface potential will be still existed and contributed by the first and the sixth layers as well as the charges in the other region not counted as charge layers. Thus, this work provides a possible way to improve the dynamic double layer model by introducing more layers beneath the sample surface, with the intension of enabling this model to better explain the charging problems induced by electron irradiation.

![](./images/812587762686361600_16.jpg)

FIG. 11. The evolution of the surface potential of the semi-infinite SiO₂ at primary beam energy of 10 keV (solid square) and 15 keV (solid circle) as a function of the beam irradiation time.

## V. CONCLUSION

Multiple coupled charge layers have been found for the trapped charge distribution in the charging phenomenon of SiO₂ induced by electron beam irradiation. The involved charge layers are merely distributed along the incidence axis of the primary electron beam and each of them is parallel to the sample surface, and the shallower layers tend to be formed at a faster rate than the deeper ones. Essentially, the charge drift under the electric field, in which electrons and holes move to opposite directions, is crucial for forming such trapped charge distributions. As for the deeper layers, their later formation is closely related to charge detrapping, which requires the sample to be irradiated for a period of time to make the electric field sufficiently intense. Furthermore, due to the deceleration of primary electrons in negative charging, the number of the charge layers does not increase when the primary electron energy is increased. Considering the fact that the experimental measurement of the nanoscale trapped charge distribution is quite hard, this work by taking into account of comprehensive physical processes is expected to advance the understanding of mechanism behind the charging phenomenon in insulating materials.

## ACKNOWLEDGMENTS

This work was supported by the National Key Research and Development Project (No. 2019YFF0216404) and Education Ministry through the "111" Project 2.0 (No. BP0719016). We thank supercomputing center of USTC for the support of parallel computing.

## DATA AVAILABILITY

The data that support the findings of this study are available within the article.

## REFERENCES

$^{1}$J. Cazaux, *X-ray Spectrom.* **25**, 265 (1996).
$^{2}$J. Cazaux, *Microsc. Microanal.* **10**, 670 (2004).
$^{3}$J. Cazaux, *Ultramicroscopy* **108**, 1645 (2008).
$^{4}$B. Vallayer, G. Blaise, and D. Treheux, *Rev. Sci. Instrum.* **70**, 3102 (1999).
$^{5}$Y. Nissan-Cohen, J. Shappir, and D. Frohman-Bentchkowsky, *Appl. Phys. Lett.* **44**, 417 (1984).
$^{6}$J. W. Hong, S. M. Shin, C. J. Kang, Y. Kuk, Z. G. Khim, and S.-I. Park, *Appl. Phys. Lett.* **75**, 1760 (1999).
$^{7}$A. Imburgia, R. Miceli, E. R. Sanseverino, P. Romano, and F. Viola, *IEEE Trans. Dielectr. Electr. Insul.* **23**, 3126 (2016).
$^{8}$C. Perrin, V. Griseri, C. Inguimbert, and C. Laurent, *J. Phys. D Appl. Phys.* **41**, 205417 (2008).
$^{9}$V. Griseri, C. Perrin, and C. Laurent, *J. Electrostat.* **67**, 400 (2009).
$^{10}$G. Chen, Z. Xu, and L. W. Zhang, *Meas. Sci. Technol.* **18**, 1453 (2007).
$^{11}$A. Melchinger and S. Hofmann, *J. Appl. Phys.* **78**, 6224 (1995).
$^{12}$Z. J. Ding and R. Shimizu, *Surf. Sci.* **197**, 539 (1988).
$^{13}$R. Shimizu and Z. J. Ding, *Rep. Prog. Phys.* **55**, 487 (1992).
$^{14}$Z. J. Ding and R. Shimizu, *Scanning* **18**, 92 (1996).
$^{15}$Z. J. Ding, H. M. Li, X. D. Tang, and R. Shimizu, *Appl. Phys. A* **78**, 585 (2004).
$^{16}$S. F. Mao, Y. G. Li, R. G. Zeng, and Z. J. Ding, *J. Appl. Phys.* **104**, 114907 (2008).
$^{17}$C. Li, S. F. Mao, and Z. J. Ding, *J. Appl. Phys.* **125**, 024902 (2019).
$^{18}$C. Li, B. Da, and Z. J. Ding, *Appl. Surf. Sci.* **504**, 144138 (2020).
$^{19}$C. Li, S. F. Mao, Y. B. Zou, Y. G. Li, P. Zhang, H. M. Li, and Z. J. Ding, *J. Phys. D Appl. Phys.* **51**, 165301 (2018).
$^{20}$N. F. Mott, *Proc. R. Soc. Lond. Ser. A* **124**, 425 (1929).
$^{21}$R. A. Bonham and T. G. Strand, *J. Chem. Phys.* **39**, 2200 (1963).
$^{22}$Y. Yamazaki, Ph.D. thesis (Osaka University, 1977).
$^{23}$J.-C. Kuhr and H.-J. Fitting, *J. Electron Spectrosc. Relat. Phenom.* **105**, 257 (1999).

$^{24}$Y. Sun, H. Xu, B. Da, S. F. Mao, and Z. J. Ding, *Chin. J. Chem. Phys.* **29**, 663 (2016).
$^{25}$D. Tahir, H. L. Kwon, H. C. Shin, S. K. Oh, H. J. Kang, S. Heo, J. G. Chung, J. C. Lee, and S. Tougaard, *J. Phys. D Appl. Phys.* **43**, 255301 (2010).
$^{26}$J. Cazaux, *Nucl. Instrum. Methods Phys. Res. B* **244**, 307 (2006).
$^{27}$H. Seiler, *J. Appl. Phys.* **54**, R1 (1983).
$^{28}$Y. Lin and D. C. Joy, *Surf. Interface Anal.* **37**, 895 (2005).
$^{29}$C. G. Walker, M. M. El-Gomati, A. M. Assa'd, and M. Zadrazil, *Scanning* **30**, 365 (2008).
$^{30}$H. Fröhlich, *Proc. R. Soc. Lond. A* **160**, 230 (1937).
$^{31}$H. Fröhlich, *Adv. Phys.* **3**, 325 (1954).
$^{32}$H.-J. Fitting and J.-U. Friemann, *Phys. Status Solidi A* **69**, 349 (1982).
$^{33}$M. V. Fischetti, *Phys. Rev. Lett.* **53**, 1755 (1984).
$^{34}$E. Cartier and F. R. McFeely, *Phys. Rev. B* **44**, 10689 (1991).
$^{35}$J. P. Ganachaud, C. Attard, and R. Renoud, *Phys. Status Solidi B* **199**, 175 (1997).
$^{36}$A. Akkerman, A. Gibrekhterman, A. Breskin, and R. Chechik, *J. Appl. Phys.* **72**, 5429 (1992).
$^{37}$Y. B. Zou, S. F. Mao, B. Da, and Z. J. Ding, *J. Appl. Phys.* **120**, 235102 (2016).
$^{38}$J. P. Vigouroux, J. P. Duraud, A. L. Moel, C. L. Gressus, and D. L. Griscom, *J. Appl. Phys.* **57**, 5139 (1985).
$^{39}$D. L. Griscom, *Phys. Res. Int.* **2013**, 1 (2013).
$^{40}$H. J. Fitting, A. N. Trukhin, T. Barfels, B. Schmidt, and A. V. Czarnowski, *Radiat. Eff. Defect Solids* **157**, 575 (2002).
$^{41}$A.-M. El-Sayed, M. B. Watkins, V. V. Afanas'ev, and A. L. Shluger, *Phys. Rev. B* **89**, 125201 (2014).
$^{42}$D. J. DiMaria, F. J. Feigl, and S. R. Butler, *Appl. Phys. Lett.* **24**, 459 (1974).
$^{43}$D. J. DiMaria, F. J. Feigl, and S. R. Butler, *Phys. Rev. B* **11**, 5023 (1975).
$^{44}$D. L. Griscom, *J. Non Cryst. Solids* **352**, 2601 (2006).
$^{45}$R. C. Hughes, *Phys. Rev. Lett.* **35**, 449 (1975).
$^{46}$R. C. Hughes, *Solid State Electr.* **21**, 251 (1978).
$^{47}$R. C. Hughes, *Phys. Rev. B* **15**, 2012 (1977).
$^{48}$K. Ohya, K. Inai, H. Kuwada, T. Hayashi, and M. Saito, *Surf. Coat. Technol.* **202**, 5310 (2008).
$^{49}$T. H. Ning, *J. Appl. Phys.* **47**, 3203 (1976).
$^{50}$J. J. Tzou, J. Y. C. Sun, and C. T. Sah, *Appl. Phys. Lett.* **43**, 861 (1983).
$^{51}$M. Touzin, D. Goeuriot, C. Guerret-Piécourt, D. Juvé, D. Tréheux, and H. J. Fitting, *J. Appl. Phys.* **99**, 114110 (2006).
$^{52}$H. J. Fitting, N. Cornet, M. Touzin, D. Goeuriot, C. Guerret-Piécourt, and D. Tréheux, *J. Eur. Ceram. Soc.* **27**, 3977 (2007).
$^{53}$R. C. Hughes, *Phys. Rev. Lett.* **30**, 1333 (1973).
$^{54}$B. Raftari, N. V. Budko, and C. Vuik, *J. Appl. Phys.* **118**, 204101 (2015).
$^{55}$E. I. Rau, S. Fakhfakh, M. V. Andrianov, E. N. Evstafeva, O. Jbara, S. Rondot, and D. Mouze, *Nucl. Instrum. Methods Phys. Res. B* **266**, 719 (2008).