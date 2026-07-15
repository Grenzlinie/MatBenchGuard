# Material, size and environment dependence of plasmon-induced hot carriers in metallic nanoparticles

Stefano Dal Forno, $^{*, \dagger}$ Luigi Ranno, $^{\ddagger}$ and Johannes Lischner $^{*, \mathbb{I}}$

$^\dagger$Department of Physics, Imperial College London, London SW7 2AZ, United Kingdom.

$^\ddagger$Department of Materials, Imperial College London, London SW7 2AZ, United Kingdom.

$^\mathbb{I}$Department of Physics and Department of Materials, and the Thomas Young Centre for Theory and Simulation of Materials, Imperial College London, London SW7 2AZ, United Kingdom

E-mail: tenobaldi@gmail.com; j.lischner@imperial.ac.uk

## Abstract
Harnessing hot electrons and holes resulting from the decay of localized surface plasmons in nanomaterials has recently led to new devices for photovoltaics, photocatalysis and optoelectronics. Properties of hot carriers are highly tunable and in this work we investigate their dependence on the material, size and environment of spherical metallic nanoparticles. In particular, we carry out theoretical calculations of hot carrier generation rates and energy distributions for six different plasmonic materials (Na, K, Al, Cu, Ag and Au). The plasmon decay into hot electron-hole pairs is described via Fermi's Golden Rule using the quasistatic approximation for optical properties and a spherical well potential for the electronic structure. We present results for nanoparticles with diameters up to 40 nm, which are embedded in different dielectric media. We find that small nanoparticles with diameters of 16 nm or less in media with large dielectric

constants produce most hot carriers. Among the different materials, Na, K and Au generate most hot carriers. We also investigate hot-carrier induced water splitting and find that simple-metal nanoparticles are useful for initiating the hydrogen evolution reaction, while transition-metal nanoparticles produce dominantly holes for the oxygen evolution reaction.

Keywords

hot electrons, plasmon decay, nanoparticles, water splitting, nanophotonics

Energetic or "hot" electrons and holes produced by the decay of localized surface plasmons (LSP) in metallic nanostructures have recently generated much excitement. They can be harnessed in optoelectronic devices, such as photodetectors, or for solar energy conversion, i.e. in photocatalytic or photovoltaic devices. $^{1-8}$ For example, Mukherjee *et al.* observed that plasmon-induced hot electrons can trigger $\text{H}_2$ dissociation reactions on the surface of gold nanoparticles. $^{9}$ An important advantage of nanoplasmonic devices compared to traditional systems is their tunability: their optical and electronic properties depend sensitively on the nanoparticle size and shape, but also on the nanoparticle material and its environment. $^{10-15}$

To guide experimental progress and identify nano-devices with favorable hot-carrier prop- erties, a detailed theoretical understanding of the physico-chemical processes that govern hot-carrier generation is needed. However, developing such a theory is challenging because of the large size of experimentally relevant nanoparticles. Atomistic *ab initio* calculations are currently only feasible for metallic clusters and very small nanoparticles. $^{5,16,17}$ To model properties of experimentally relevant nanoparticles with radii of 10 nm or more, two different strategies have been employed. In many calculations, simplified models for the electronic structure of the nanoparticle are used, such as jellium models or non-interacting electron models. $^{18-21}$ For example, Manjavacas *et al.* employed a spherical well model to simulate hot-carrier generation in silver nanoparticles with diameters up to 25 nm. Such approaches are accurate for nanostructures made of simple metals (i.e. metals with conduction electrons
2

in s- or p-states), but are less reliable for transition-metal nanostructures where d-electrons can play an important role. $^{22,23}$

Another class of approaches is based on the assumption that the electronic structure of the nanomaterial is similar to the electronic structure of the bulk material, which can be obtained with *ab initio* approaches. These approaches are particularly useful for materials with shallow d-states, such as gold or copper. $^{22-25}$ However, a complete description of hot-carrier generation that captures both nanoparticle size effects and d-bands is still missing.

In this paper, we do not attempt to develop such a complete theory of hot-carrier gen- eration. Instead, we use a simplified description of the nanoparticle electronic structure to explore the dependence of hot-carrier properties on the nanoparticle material, size and environment. In particular, we carry out calculations for spherical nanoparticles with diam- eters up to 40 nm and investigate six different plasmonic metals: the simple-metals sodium (Na), potassium (K) and aluminium (Al) and the transition-metals gold (Au), silver (Ag) and copper (Cu). For some systems, such as simple-metal nanoparticles or transition-metal nanoparticles in an environment with a large dielectric constant, we expect that our simpli- fied electronic structure model gives accurate results. For transition-metal nanoparticles in an environment with weak screening, our calculations are less accurate because of the lack of d-states in the model, but should provide a useful *lower bound* on hot-carrier generation rates.

The paper is structured as follows: we first explain in detail our computational approach for calculating hot-carrier generation rates emphasizing the importance of an accurate de- scription of carrier lifetimes. We then present our results for the optical and hot-carrier properties of metallic nanoparticles, discuss consequences for hot-carrier induced solar water splitting and offer conclusions.

# Result and discussion

Description of the model. For a spherical nanoparticle of radius $R$ and volume $V = 4\pi R^3/3$, illuminated by light of frequency $\omega$, we use Fermi's golden rule to express the number of hot electrons with energy $E$ generated per unit time, volume and energy as

$$
N_{e}(E,\omega)=\frac{2}{V}\sum_{if}\Gamma_{if}(\omega)\delta(E-E_{f}), \tag{1}
$$

where the prefactor of 2 takes spin into account and $\Gamma_{if}$ is the probability rate of exciting an electron from state $\Psi_{i}$ to state $\Psi_{f}$ (with corresponding energies $E_{i}$ and $E_{f}$) given by

$$
\Gamma_{if}(\omega)=\frac{2\pi}{\hbar}\left|\langle\Psi_{f}|\Phi_{tot}(\omega)|\Psi_{i}\rangle\right|^{2}\rho_{if}. \tag{2}
$$

In this equation, $\Phi_{tot}$ denotes the total potential including both the external perturbation by the light field and the induced response of the nanoparticle, and $\rho_{if}$ describes the density of available states via $^{26}$

$$
\rho_{if}(\omega)=\frac{\gamma_{if}}{\pi}\frac{1}{(\hbar\omega - [E_{f}-E_{i}])^{2}+\gamma_{if}^{2}}+\frac{\gamma_{if}}{\pi}\frac{1}{(\hbar\omega + [E_{f}-E_{i}])^{2}+\gamma_{if}^{2}}, \tag{3}
$$

where the first term captures resonant transitions, while the second term describes anti-resonant transitions. The relative importance of these two processes is controlled by the linewidth of the transition $\gamma_{if}$ which plays an important role for the distribution of hot carriers. $^{19}$ To calculate the distribution of hot holes $N_{h}(E,\omega)$, $E_{f}$ on the right hand side of Eq. 1 has to be replaced by $E_{i}$.

To calculate $\gamma_{if}$ we use Matthiessen's rule and partition the linewidth into contributions from electron-electron (el-el) and electron-phonon (el-ph) interactions in the initial and final states according to

$$
\gamma_{if}=\gamma_{el-el}^{i}+\gamma_{el-ph}^{i}+\gamma_{el-el}^{f}+\gamma_{el-ph}^{f}. \tag{4}
$$


The electron-phonon contributions to the linewidth are calculated with the Debye model²⁷,²⁸ according to

$$
\gamma_{el-ph}^{j}=\frac{2 \pi \lambda \hbar \omega_{D}}{3}, \tag{5}
$$

where $\omega_D$ denotes the Debye frequency corresponding to a Debye temperature $\Theta_D = \hbar\omega_D/k_B$ and $\lambda$ is the electron-phonon mass enhancment parameter.

For the electron-electron contributions to $\gamma_{if}$, Fermi liquid theory²⁹,³⁰ for a homogeneous electron gas of conduction electron density $\rho$ yields

$$
\gamma_{e l-e l}^{j}=\frac{m e^{4}\left(E_{j}-E_{F}\right)^{2}}{64 \pi^{3} \hbar^{2} \epsilon_{0}^{2} E_{s}^{3 / 2} E_{F}^{1 / 2}}\left(\frac{2 \sqrt{E_{s} E_{F}}}{4 E_{F}+E_{s}}+\arctan \sqrt{\frac{4 E_{F}}{E_{s}}}\right), \tag{6}
$$

with $m$, $e$, $\epsilon_0$ and $E_F = \frac{1}{2}(3\pi^2\rho)^{2/3}$ denoting the electron mass, the electron unit charge, the vacuum permittivity and the Fermi energy, respectively. Also, $E_S = \hbar^2 q_s^2/2m$ is the kinetic energy associated with the Thomas-Fermi screening vector $q_s^2 = \frac{e^2}{\epsilon_0}g(E_F)$, where $g(E_F)$ is the density of states at the Fermi level. Table 1 summarizes all parameters that were used in the calculation of $\gamma_{if}$.

Table 1: Conduction electron densities $\rho$ (in nm⁻³), work functions $\phi$ (in eV), Debye energies $k_B\Theta_D$ (in eV), electron-phonon coupling parameters $\lambda$ (dimensionless) and the resulting electron-phonon linewidths $\gamma_{el-ph}$ (in meV) of the selected metals.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Na</th>
      <th>K</th>
      <th>Al</th>
      <th>Cu</th>
      <th>Ag</th>
      <th>Au</th>
      <th>Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\rho$</td>
      <td>25.36</td>
      <td>13.18</td>
      <td>180.8</td>
      <td>84.53</td>
      <td>58.56</td>
      <td>59.01</td>
      <td>³¹</td>
    </tr>
    <tr>
      <td>$\phi$</td>
      <td>2.36</td>
      <td>2.29</td>
      <td>4.20 (100)</td>
      <td>5.10 (100)</td>
      <td>4.64 (100)</td>
      <td>5.47 (100)</td>
      <td>³¹</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>4.06 (110)</td>
      <td>4.48 (110)</td>
      <td>4.52 (110)</td>
      <td>5.37 (110)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>4.26 (111)</td>
      <td>4.94 (111)</td>
      <td>4.74 (111)</td>
      <td>5.31 (111)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>4.53 (112)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$k_B\Theta_D$</td>
      <td>0.013</td>
      <td>0.009</td>
      <td>0.034</td>
      <td>0.027</td>
      <td>0.019</td>
      <td>0.015</td>
      <td>³²</td>
    </tr>
    <tr>
      <td>$\lambda$</td>
      <td>0.18</td>
      <td>0.13</td>
      <td>0.45</td>
      <td>0.13</td>
      <td>0.12</td>
      <td>0.17</td>
      <td>³³</td>
    </tr>
    <tr>
      <td>$\gamma_{el-ph}$</td>
      <td>4.9</td>
      <td>2.3</td>
      <td>32.0</td>
      <td>7.4</td>
      <td>4.7</td>
      <td>5.2</td>
      <td></td>
    </tr>
  </tbody>
</table>

Figure 1 shows the calculated hot carrier lifetimes $\tau_{if} = \hbar/\gamma_{if}$ as a function of the hot carrier energies for the six selected metals. We observe lifetimes of up to several hundred

![](./images/867766725599298034_1.jpg)

Figure 1: Hot carrier lifetimes due to electron-phonon and electron-electron interactions for six different metals. The zero of energy is set to the Fermi level. The lifetimes span a time range between 1 and 300 femtoseconds.

femtoseconds for states near the Fermi level and less than 10 femtoseconds at carrier ener- gies higher than 2-3 eV. These values are in good agreement with previous theoretical and experimental pump-probe results. $^{11,22,27,34-36}$ Note that the discrepancy with two-photon photoemission experiments, which often report lifetimes in the picosecond range, $^{13,29,37,38}$ can be explained by transport effects. $^{39,40}$

The total potential in Eq. 2 is calculated within the quasi-static approximation $^{41}$ given by
$$
\Phi_{t o t}(\omega, \mathbf{r})=-E_{0} r \cos (\theta)+E_{0} \frac{\epsilon(\omega)-\epsilon_{m}}{\epsilon(\omega)+2 \epsilon_{m}} \begin{cases}r \cos (\theta), & r \leq R, \\ R^{3} \frac{\cos (\theta)}{r^{2}}, & r>R,\end{cases}
\tag{7}
$$
where the first term describes the perturbing light field and the second term captures the response of the nanoparticle. Also, $E_{0}$ is the strength of the external electric field which is set to ensure an illumination intensity of $1 \mathrm{~mW} / \mu \mathrm{m}^{2}$ and $\epsilon(\omega)$ and $\epsilon_{m}$ are the dielectric functions of the bulk material and the environment surrounding the nanoparticle, respectively. The bulk dielectric functions are calculated from experimental data for the refractive index $n(\omega)$

and the extinction index $\kappa(\omega)^{31}$ via the standard formulas

$$
\epsilon(\omega)=\epsilon_{1}(\omega)+i \epsilon_{2}(\omega), \tag{8}
$$

$$
\epsilon_{1}(\omega)=n(\omega)^{2}-\kappa(\omega)^{2}, \tag{9}
$$

$$
\epsilon_{2}(\omega)=2 n(\omega) \kappa(\omega), \tag{10}
$$

where $\epsilon_{1}(\omega)$ and $\epsilon_{2}(\omega)$ denote the real and imaginary parts of the dielectric function, respectively.

The final ingredients needed to evaluate Eqs. 1 and 2 are the single-particle wave functions $\Psi_{j}(\mathbf{r})$ and their energies $E_{j}$ of the spherical nanoparticle. These quantities are obtained by solving the Schrödinger equation for non-interacting electrons in a spherical well potential. For sufficiently large nanoparticles, it has been shown that the effect of electron-electron interactions on hot carrier generation rates is small. $^{19}$ For a given nanoparticle radius, the depth of the potential well is chosen such that the energy of the highest occupied state is equal to experimentally measured work function of the material under consideration (see Table 1). Note that the work function depends in general on the Miller indices of the surface. For simplicity, we worked with an averaged workfunction when more than one value was available corresponding to a polycrystalline sample. Additional details of our approach to solving the Schrödinger equation for the spherical well can be found in the Methods section. In our calculations, we replaced Delta-function in Eq. 1 by a Gaussian with a standard deviation $\sigma$ of 0.05 eV.

For a given photon energy $\hbar \omega$, integrating Eq. 1 over the hot electron (hole) energy yields the total number of hot electrons (holes) produced per unit time and volume according to

$$
N_{e(h)}(\omega)=\int_{-\infty}^{+\infty} N_{e(h)}(E, \omega) d E=\sum_{i f} \Gamma_{i f}(\omega), \tag{11}
$$


and the power absorbed by the hot carriers is given by

$$
P_{h c}(\omega)=\int_{-\infty}^{+\infty}\left(N_{e}(E, \omega)+N_{h}(E, \omega)\right)|E| d E=\sum_{i f} \Gamma_{i f}(\omega)\left(\left|E_{i}\right|+\left|E_{f}\right|\right), \tag{12}
$$

where all energies are measured with respect to the Fermi level. Similarly, following Man- javacas et al., we define a figure of merit (FoM) as the number of hot electrons above a certain energy $\delta E$ from the Fermi level according to

$$
N_{e}^{\delta E}(\omega)=\int_{\delta E}^{+\infty} N_{e}(E, \omega) d E=\sum_{\substack{i f \\ E_{f}>\delta E}} \Gamma_{i f}(\omega). \tag{13}
$$

The FoM of hot holes is obtained by performing the sum with the condition $E_{i}<-\delta E$.

Finally, the total number of hot carriers produced by a light source of spectral irradiance $S(\omega)=d I(\omega) / d \omega$, where $I(\omega)$ denotes the energy deposited by unit time and area, is given by

$$
N=\frac{1}{I_{0}} \int_{0}^{+\infty} N_{h c}(\omega) S(\omega) d \omega, \tag{14}
$$

where $N_{h c}(\omega)=N_{e}(\omega)+N_{h}(\omega)$ and $I_{0}=1 m W / \mu m^{2}$ is the intensity of the monochromatic light source used in Eq. 7.

We also study optical properties of spherical nanoparticles. If the nanoparticles radius is smaller than the wavelength of light, light absorption dominates over scattering processes. $^{41}$ Within the quasistatic approximation, the absorption cross section is given by

$$
C_{a b s}(\omega)=4 \pi \frac{\omega}{c} n_{m} R^{3} \Im\left(\frac{\epsilon(\omega)-\epsilon_{m}}{\epsilon(\omega)+2 \epsilon_{m}}\right), \tag{15}
$$

where $c$ is the speed of light and $n_{m}$ is the refractive index of the medium. The power absorbed by the nanoparticle in the quasistatic approximation is

$$
P_{q s}(\omega)=I_{0} C_{a b s}(\omega). \tag{16}
$$


As the radius of the nanoparticle becomes comparable to the wavelength of light, corrections to the quasi-static absorption cross section become important. In particular, Mie theory predicts a red shift of the plasmon energy as the radius increases. $^{10,12,41}$ The quasi-static approximation also fails for very small nanoparticles when the radius approaches the electron mean free path of the metal. $^{10}$

Optical properties. Figure 2 shows the quasi-static absorption cross section for spherical nanoparticles of the six selected plasmonic metals (Au, Ag, Cu, Al, K, Na) as a function of the photon energy and for different dielectric environments. In particular, we carried out calculations for $\epsilon_m = 1$ corresponding to a nanoparticle in vacuum, $\epsilon_m = 5$ corresponding roughly to a nanoparticle embedded in an organic material (for example, pentacene) and $\epsilon_m = 10$ corresponding to a nanoparticle embedded in a semiconductor, such as silicon or GaAs. All curves are offset for clarity and normalized such that the maximum absorption cross section is unity (as a consequence, the results are independent of the nanoparticle radius). The solar spectrum (standard direct plus circumsolar) $^{42}$ is also drawn as a shaded curve.

We observe a clear difference between simple metals (Al, K and Na) and transition metals (Au, Ag and Cu). The simple metals exhibit a Drude-like absorption spectrum with a single peak corresponding to the localized surface plasmon resonance. The high plasmon energy of Al results from its high conduction electron density. For larger environment dielectric constants, the plasmon peaks shift to lower energies as the additional screening of the surrounding medium reduces the energy required to polarize the nanoparticle. The shift is largest for Al, whose plasmon peak moves from 8.96 eV in vacuum to 3.40 eV for $\epsilon_m = 10$ and now overlaps with the solar spectrum. Table 2 summarizes the energies of the localized surface plasmon resonances of the selected metals in different environments.

In contrast, the absorption spectra of the transition-metal nanoparticles exhibit a more complicated shape. For Ag, the spectrum has a strong plasmon peak at 3.50 eV followed by a broad shallow peak at higher energies (for $\epsilon_m = 1$). This additional feature results from

![](./images/867766725599298034_2.jpg)

Figure 2: Nanoparticle absorption cross section of six plasmonic metals in different environments. Solid, dashed and dash-dotted lines represent $\epsilon_m=1$, $\epsilon_m=5$ and $\epsilon_m=10$, respectively. All curves are normalized to their maximum value and are therefore independent of the nanoparticle radius. The shaded curve in the background is the direct plus circumsolar spectral irradiance $S(\omega)$.

transitions involving d-bands which – for Ag – sit about 4 eV below the Fermi level. For Au and Cu, the d-bands are much closer to the Fermi level (roughly 2.5 eV below it) resulting in a spectrum with a significantly reduced plasmon peak followed by a strong d-band structure.

Increasing the environment dielectric constant leads to dramatic changes in the absorption spectra of transition-metal nanoparticles. As the plasmon energy is reduced, the d-band features become less important and a Drude-like spectrum is recovered.

Table 2: Localized surface plasmon energies (in eV) of spherical nanoparticles in different dielectric environments calculated in the quasistatic approximation.

<table>
  <thead>
    <tr>
      <th>$\epsilon_m$</th>
      <th>Na</th>
      <th>K</th>
      <th>Al</th>
      <th>Cu</th>
      <th>Ag</th>
      <th>Au</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3.28</td>
      <td>2.29</td>
      <td>8.96</td>
      <td>2.15</td>
      <td>3.50</td>
      <td>2.40</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1.68</td>
      <td>1.19</td>
      <td>4.71</td>
      <td>2.00</td>
      <td>2.48</td>
      <td>2.00</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1.20</td>
      <td>0.87</td>
      <td>3.40</td>
      <td>1.69</td>
      <td>1.92</td>
      <td>1.62</td>
    </tr>
  </tbody>
</table>


We have compared the calculated absorption spectra with experimental measurements^{43-46} and found good agreement for the positions of the absorption peaks and also for the shifts induced by a dielectric environment.

Hot carrier energy distribution. Figure 3 shows the distribution of hot electrons and holes as a function of their energy for a Na nanoparticule with $R = 10$ nm. An environment dielectric constant of $\epsilon_m = 1$ was used and the photon energy was set to $\omega_{LSP} = 3.28$ eV, the energy of the localized surface plasmon. We find (see inset) that both hot electron and hole distributions are strongly peaked in the vicinity of the Fermi level $E_F$. At lower (higher) energies, the hole (electron) distribution has a complicated profile with many peaks and decays to zero for energies smaller (larger) than $E_F - \omega_{LSP}$ ($E_F + \omega_{LSP}$).

![](./images/867766725599298034_3.jpg)

Figure 3: Hot electron (red) and hole (blue) distributions for a sodium spherical nanoparticle of 10 nm radius. The photon energy is set to the energy of the localized surface plasmon. The dashed vertical line denotes the Fermi energy. The zero of energy is set to the vacuum level. The hot carrier distributions were rescaled such that the total energy of the hot carriers is equal to the energy absorbed by the nanoparticle.

This behaviour of the hot carrier distributions results from the competition between contributions to the density of final states (Eq. 3) from resonant and anti-resonant transitions. Anti-resonant transitions are strong when the transition energy is small and lifetimes are short (they vanish in the limit of infinite lifetimes) and thus give rise to the peaks near the Fermi level. Resonant transitions give significant contributions when lifetimes are long and the transition energy is equal to the photon energy. They give rise to electron and hole

distributions that look like shifted copies of each other.

Moreover, the energy-dependence of the carrier lifetimes results in a shift of the resonant peak towards the Fermi level. The magnitude of this shift increases for larger transition energies. This effect thus reduces the number of hot carriers. Promising systems for hot carrier generation should therefore feature weak electron-electron interactions (as those give rise to energy-dependent lifetimes) and low plasmon energies.

Another interesting feature in Fig. 3 is the peak in the hot electron distribution at $\sim 0.7$ eV. These electrons have energies above the vacuum level and can escape from the nanoparticle. Such plasmon-induced ionization processes are possible when the energy of the localized surface plasmon is larger than the work function of the material. The resulting hot electrons can be harvested without the need to extract them from the nanoparticle through transport processes that inevitably lead to hot carrier cooling. This mechanism could therefore be interesting for energy technology applications, such as solar cells or photoelectrochemical devices.

Figure 4 shows the distribution of hot electrons and holes as a function of the hot carrier energy for nanoparticles of different compositions and sizes. Again, an environment dielectric constant of $\epsilon_m = 1$ was used and the photon energy was set to the energy of the localized surface plasmon resonance (see Table 2).

We first discuss the size dependence of the hot carrier distributions. For very small nanoparticles (with radii of 4 nm or less), the distributions exihibit discrete peaks. The electronic structure of such nanoparticles is molecule-like with a discrete set of one-electron levels and the peaks in the hot carrier distribution result from transitions between such levels. For larger nanoparticles, the energy spacing between one-electron levels shrinks and the hot carrier distributions become quasi-continuous.

Considering the material dependence, we find that all six plasmonic metals exhibit hot carrier distributions with strong peaks near the Fermi energy. Those peaks are largest for Al, which has the highest plasmon energy and the shortest lifetime for carriers near $E_F$, see

![](./images/867766725599298034_4.jpg)

Figure 4: Hot electron (red) and hot hole (blue) distributions for spherical nanoparticles of different compositions and sizes. Photon energies are set to the energy of the localized surface plasmon. The dashed vertical line denotes the Fermi energy. The zero of energy is set to the vacuum level. The hot carrier distributions were rescaled such that the total energy of the hot carriers is equal to the energy absorbed by the nanoparticle.

Fig. 1. Interestingly, because of its high electron density, Al features the longest lifetimes for carriers far from the Fermi level which gives rise to the structure of fine sharp peaks in the hot carrier distributions. The localized surface plasmon energies of simple-metal nanoparticles (Na, K and Al) are similar to or larger than the their workfunctions and as a consequence the hot electron distributions in these materials have peaks near or above the vacuum level. In contrast, the energy of the localized surface plasmon in transition-metal nanoparticles (Au, Ag and Cu) is smaller than the workfunction and the resulting hot carrier distributions are relatively structureless and exhibit no peaks above the vacuum level.

**Hot carrier power absorption.** Figure 5 compares the absorbed power calculated in the quasistatic approximation (Eq. 16) with the absorbed power computed from the hot carrier distributions (Eq. 12) for an $R = 6$ nm nanoparticle made of one of the six selected plasmonic materials in different dielectric media. The illumination intensity is set to $1\ \mathrm{mW/\mu m^2}$. In general, the two ways of calculating the absorbed power give different results. Two factors contribute to this discrepancy: i) the inability of the spherical well model to describe d-states and ii) finite carrier lifetimes that enable transitions which do not conserve energy (see Eq. 3). To distinguish these factors, we rescaled the hot carrier curves in Fig. 5 such that the height of their first peak is equal to the corresponding feature in the quasistatic curves.

For the simple metals (Na, K and Al), we find that the total power of the hot carriers $P_{hc}(\omega)$ follows closely the quasistatic absorption $P_{qs}(\omega)$ indicating that the spherical well model accurately describes the electronic structure of these systems. In contrast, there are clear differences between the two curves for transition-metal nanoparticles. For Ag, Au and Cu, $P_{hc}(\omega)$ has a peak at $\omega_{LSP}$ and decreases at higher photon energies, while $P_{qs}(\omega)$ goes through a minimum after the plasmon peak and then increases again. As discussed above, the increase in $P_{qs}(\omega)$ is caused by d-band transitions (recall that we are using experimentally measured bulk dielectric functions to calculate $P_{qs}$ which include d-band transitions as well as other contributions, such as phonon-assisted transitions). The spherical well model does

14

![](./images/867766725599298034_5.jpg)

Figure 5: Quasistatic absorbed power (solid lines) calculated using Eq. 16 and the hot carrier absorbed power (dots) calculated using Eq. 12 for an $R = 6$ nm nanoparticle. The hot carrier power has been rescaled to match the maximum value of the quasistatic curves.

not capture such transitions and the corresponding features in $P_{hc}(\omega)$ are missing.

Note, however, that an increase in the environment dielectric function reduces the relative importance of d-state features in $P_{qs}(\omega)$ for transition-metal nanoparticles and improves the agreement with $P_{hc}(\omega)$. We also observe that higher values of $\epsilon_m$ lead to higher absorption at $\omega_{LSP}$ (except for Al) indicating that there exists an optimal value for the medium dielectric constant which maximises hot carrier generation rates.

Hot carrier Figure of Merit. Figure 6 shows the FoM (Eq. 13) for nanoparticles of different sizes and compositions in various dielectric environments. We use the energy threshold $\delta E = 0.3\hbar\omega_{LSP}$, where $\omega_{LSP}$ denotes the energy of the localized surface plasmon (see Table 2).

We observe that the FoM of hot electrons (solid circles) is always larger than the FoM of hot holes (empty circles) (except in some cases for very small nanoparticles). This is due to the fact that electrons can be excited to arbitrarily high energies, while hole energies are restricted by the depth of the potential well. We also find that an increase in the environment dielectric constant $\epsilon_m$ results in an increase in the FoM. Specifically, the FoM of Al nanoparticles doubles as $\epsilon_m$ increases from 1 to 10, while the FoM of Na, K and Ag increases by a factor of 10. For Cu and Au, the FoM even increases by *two orders of magnitude* demonstrating the important role of environment screening for hot carrier properties. The increase in the FoM is caused by two factors: (i) increasing $\epsilon_m$ leads to enhanced absorption at the plasmon resonance (see Fig. 5) and (ii) increasing $\epsilon_m$ reduces the plasmon energy and thus increases the relative importance of resonant transitions.

Figure 6 also shows that in general the FoM decreases as the nanoparticle size is increased. For larger nanoparticles, a larger fraction of the excited carriers undergo anti-resonant tran- sitions and have energies closer to the Fermi level. Exceptions to this trend are the FoM of holes in Na, K and Au and the FoM for electrons in Ag for nanoparticles in environments with high dielectric constants. These systems exhibit a maximum in the FoM for radii in the range of 6-8 nms.


![](./images/867766725599298034_6.jpg)

Figure 6: Figure of Merit of hot electrons (solid circles) and hot holes (empty circles) as function of nanoparticle radius and environment dielectric constant. $\delta E$ in Eq. 13 was set to $0.3\hbar\omega_{LSP}$.

**Water splitting.** Plasmonic nanoparticles have been used as catalysts in the photoelectrochemical splitting of water into oxygen and hydrogen gas. $^{3-5}$ To identify promising candidate systems, we calculate the total number of hot electrons (holes) produced by sunlight (Eq. 14) with energies larger (less) than the hydrogen (oxygen) evolution energy $E_{HER} = -4.44$ eV ($E_{OER} = -5.67$ eV).$^{47}$ Fig. 7 shows our results for $R = 6$ nm nanoparticles in different dielectric environments (the radial dependence of water splitting properties can be found in the Supporting Information). We find that simple-metal nanoparticles (most notably, Na and K) are significantly more efficient at producing hot electrons for the hydrogen evolution reaction than transition-metal nanoparticles. This is because the Fermi levels of Na and K sit at a higher energy than in Au, Ag and Cu and therefore the number of hot electrons above the hydrogen evolution energy is larger. As $\epsilon_m$ increases, the total number of hot electrons increases and the difference between simple metals and transition metals becomes smaller.

In contrast, holes for the oxygen evolution reaction are much more efficiently produced in transition-metal nanoparticles, while the number of hot holes produced in Na and K is extremely small. Again, hot hole production rates are enhanced as $\epsilon_m$ increases. It is important to note that nanoparticles can undergo significant modifications in realistic environments. For example, alkali metals react with aqueous solutions to form dissolved hydroxide ions. Aluminium nanoparticles acquire a surface oxide layer which can act as a tunnel barrier for hot electrons or allow molecules to diffuse to the aluminium surface.$^{48}$

## Conclusions
We have studied properties of plasmon-induced hot electrons and holes in spherical nanoparticles and analyzed their dependence on the material, the nanoparticle size and its environment. Our theoretical calculations are based on Fermi's golden rule for the decay of the localized surface plasmon into electron-hole pairs via the Landau damping mechanism. Plasmon

18

![](./images/867766725599298034_7.jpg)

Figure 7: Total number of hot electrons and holes produced after illuminating the nanopar- ticles with sunlight for different environment dielectric functions. Only electrons above the hydrogen evolution energy (HER) and holes below the oxygen evolution energy (OER) have been considered.

properties are described by the quasistatic approximation with experimental bulk dielectric functions and electronic energies and wavefunctions are determined by solving Schrödinger's equation for a spherical potential well. We find that hot carrier distributions depend sensi- tively on carrier lifetimes which we calculate by combining Debye theory for electron-phonon scattering with Fermi liquid theory for electron-electron scattering. An important limitation of the spherical well model is its inability to describe d-states. By comparing the calcu- lated total number of hot carriers with the nanoparticle absorption spectrum, we find that d-states play an important role in transition-metal nanoparticles in weak dielectric environ- ments. However, even for those systems our calculations provide a useful lower bound for hot carrier generation rates.

For all materials, the hot electron and hole distributions are peaked near the Fermi level because of strong anti-resonant transitions enabled by finite carrier lifetimes. Hot carriers are mostly produced by resonant transitions in materials with long carrier lifetimes and low plasmon energies embedded in environments with large dielectric constants. For simple-metal nanoparticles, plasmon-induced ionization is possible when the energy of the localized surface plasmon is larger than the material's workfunction. We model nanoparticles with diameters

up to 40 nm and find that small nanoparticles with diameters less than 16 nm exhibit the highest figure of merit. Among the different studied materials, most hot carriers are produced by Na, K and Au nanoparticles embedded in media with large dielectric constants. Finally, plasmon-induced water splitting was studied. We find that simple metals, in particular Na and K, efficiently generate electrons for the hydrogen evolution reaction while transition-metal nanoparticles produce holes for the oxygen evolution reaction. This suggests that either mixtures of simple-metal and transition-metal nanoparticles or bimetallic nanostructures, such as Janus or core-shell particles, should be used to achieve optimal performance in water splitting devices.

Future work should address the shortcomings of the theoretical approach, in particular the lack of d-states and the empirical description of plasmon properties. To capture d-states within a non-atomistic approach, it is possible to generalize effective mass models to multiple bands with non-parabolic dispersion relations. A parameter-free description of plasmon properties is possible through a direct calculation of the nanoparticle's polarizability within the random-phase approximation or time-dependent density-functional theory. $^{49,50}$

# Acknowledgement

The authors thank helpful discussions with Peter Nordlander, Ortwin Hess, Vincenzo Giannini and Ravishankar Sundararaman. S.D.F. and J.L. acknowledge support from EPRSC under Grant No. EP/N005244/1 and also from the Thomas Young Centre under Grant No. TYC-101. Via J.L.'s membership of the UK's HEC Materials Chemistry Consortium, which is funded by EPSRC (EP/L000202), this work used the ARCHER UK National Supercomputing Service.

### Methods

We model electrons in spherical metallic nanoparticles as free particles in a spherical potential well given by

$$
V(r)=
\begin{cases}
V_0, & r \leq R, \\
0, & r > R,
\end{cases}
\tag{17}
$$

where $r$ is the distance from the center of the nanoparticle, $V_0$ and $R$ denote the depth of the potential well and the radius of the nanoparticle, respectively. Exploiting spherical symmetry, we split the Schrödinger equation into an angular and a radial part. The solutions of the angular part are the spherical harmonics while the solutions of the radial part can be obtained numerically in terms of the spherical Bessel function of the first and second kind. Specifically, the radial Schrödinger equation is given by

$$
\left[ r^2 \frac{d^2}{dr^2} + 2r \frac{d}{dr} + \frac{2mr^2}{\hbar^2} (E - V(r)) - l(l+1) \right] \chi(r) = 0,
\tag{18}
$$

where $E$ is the energy of the electron state, $m$ is the mass of the electron and $l$ is the angular momentum quantum number. The radial solution $\chi(r)$ has to be continuous at the origin and at infinity, and its first derivative must be continuous at the surface of the nanoparticle.

Bound states have energies $V_0 < E < 0$ and the corresponding radial wavefunctions are of the form

$$
\chi(r) = A
\begin{cases}
j_l(k_1 r), & r \leq R, \\
j_l(k_2 r) + i y_l(k_2 r), & r > R,
\end{cases}
\tag{19}
$$

where $j_l$ and $y_l$ are the spherical Bessel function of the first and second kind, respectively, and $A$ is a normalisation constant. The wave vectors $k_1 = \sqrt{2m/\hbar^2 (E - V_0)}$ and $k_2 = \sqrt{2m/\hbar^2 E}$ depend on $E$ and must be chosen to guarantee continuity of the solutions and their first

derivatives at $r = R$. This condition leads to

$$
\frac{h_{l}(k_{2} R)}{h_{l}^{\prime}(k_{2} R)} \frac{j_{l}^{\prime}(k_{1} R)}{j_{l}(k_{1} R)}-\frac{k_{2}}{k_{1}}=0, \tag{20}
$$

where $h_{l}(r)$ is the spherical Hankel function of the first kind defined as $h_{l}(r)=j_{l}(r)+i y_{l}(r)$.
This equation can be easily solved numerically and the solutions are the energy eigenvalues $E_{nl}$.

Within this model, a spherical nanoparticle is characterized by two parameters: its radius $R$ and the well depth $V_{0}$, which is determined by the condition that the calculated Fermi energy of the nanoparticle should be equal to the experimentally measured work function of the bulk metal. Specifically, for a given valence electron density and nanoparticle radius, we calculate the number of electrons in the system, solve the Schrödinger equation with an initial starting guess for $V_{0}$ and determine the Fermi energy. We then vary $V_{0}$ until the calculated Fermi energy agrees with the measured work function.

Similarly, unbound states have energies $E>0$ and the corresponding radial wavefunctions are given by

$$
\chi(r)=A \begin{cases}j_{l}\left(k_{1} r\right), & r \leq R, \\ \alpha_{n l R} j_{l}\left(k_{2} r\right)+\beta_{n l R} y_{l}\left(k_{2} r\right), & r>R,\end{cases} \tag{21}
$$

where $\alpha$ and $\beta$ are chosen to guarantee continuity of the solutions and its first derivative at $r = R$ and $A$ is a normalization constant. To discretize the continuous spectrum of unbound states, we impose hard wall boundary conditions at a radius $R_{H W} \gg R$.

# Supporting Information Available

The following files are available free of charge. Radial dependence plots of water splitting hot carriers.


# References

1. Clavero, C. Plasmon-induced hot-electron generation at nanoparticle/metal-oxide interfaces for photovoltaic and photocatalytic devices. *Nat Photon* **2014**, *8*, 95-103.

2. Linic, S.; Christopher, P.; Ingram, D. B. Plasmonic-metal nanostructures for efficient conversion of solar to chemical energy. *Nature materials* **2011**, *10*, 911-921.

3. Szuromi, P. Plasmonic Water Splitting. *Science* **2013**, *339*, 1125-1125.

4. Fujishima, A.; Honda, K. Electrochemical Photolysis of Water at a Semiconductor Electrode. *Nature* **1972**, *238*, 37-38.

5. Yan, L.; Wang, F.; Meng, S. Quantum Mode Selectivity of Plasmon-Induced Water Splitting on Gold Nanoparticles. *ACS Nano* **2016**, *10*, 5452-5458.

6. Thomann, I.; Pinaud, B. A.; Chen, Z.; Clemens, B. M.; Jaramillo, T. F.; Brongersma, M. L. Plasmon enhanced solar-to-fuel energy conversion. *Nano letters* **2011**, *11*, 3440-3446.

7. Zhang, X.; Chen, Y. L.; Liu, R.-S.; Tsai, D. P. Plasmonic photocatalysis. *Reports on Progress in Physics* **2013**, *76*, 046401.

8. Awazu, K.; Fujimaki, M.; Rockstuhl, C.; Tominaga, J.; Murakami, H.; Ohki, Y.; Yoshida, N.; Watanabe, T. A plasmonic photocatalyst consisting of silver nanoparticles embedded in titanium dioxide. *Journal of the American Chemical Society* **2008**, *130*, 1676-1680.

9. Mukherjee, S.; Libisch, F.; Large, N.; Neumann, O.; Brown, L. V.; Cheng, J.; Las-siter, J. B.; Carter, E. A.; Nordlander, P.; Halas, N. J. Hot Electrons Do the Impossible: Plasmon-Induced Dissociation of H2 on Au. *Nano Letters* **2013**, *13*, 240-247.

10. Scholl, J. A.; Koh, A. L.; Dionne, J. A. Quantum plasmon resonances of individual metallic nanoparticles. *Nature* **2012**, *483*, 421-427.

23

11. Brongersma, M. L.; Halas, N. J.; Nordlander, P. Plasmon-induced hot carrier science and technology. *Nat Nano* **2015**, *10*, 25-34.

12. Derkachova, A.; Kolwas, K.; Demchenko, I. Dielectric Function for Gold in Plasmonics Applications: Size Dependence of Plasmon Resonance Frequencies and Damping Rates for Nanospheres. *Plasmonics* **2016**, *11*, 941-951.

13. Govorov, A. O.; Zhang, H.; Demir, H. V.; Gun'ko, Y. K. Photogeneration of hot plas- monic electrons with metal nanocrystals: Quantum description and potential applica- tions. *Nano Today* **2014**, *9*, 85 - 101.

14. Zhang, X.; Wu, X.; Centeno, A.; Ryan, M. P.; Alford, N. M.; Riley, D. J.; Xie, F. Signif- icant Broadband Photocurrent Enhancement by Au-CZTS Core-Shell Nanostructured Photocathodes. *Sci Rep* **2016**, *6*, 23364.

15. Genç, A.; Patarroyo, J.; Sancho-Paramon, J.; Arenal, R.; Duchamp, M.; Gonza- lez, E. E.; Henrard, L.; Bastús, N. G.; Dunin-Borkowski, R. E.; Puntes, V. F. *et al.* Tuning the Plasmonic Response up: Hollow Cuboid Metal Nanostructures. *ACS Pho- tonics* **2016**, *3*, 770-779.

16. Prineha, N.; Ravishankar, S.; Harry, A. A. Plasmonic hot carrier dynamics in solid-state and chemical systems for energy conversion. *Nanophotonics* **2016**, *5*, 96, 1.

17. Ma, J.; Wang, Z.; Wang, L.-W. Interplay between plasmon and single-particle excitations in a metal nanocluster. *Nature Communications* **2015**, *6*, 10107.

18. Ekardt, W. Dynamical Polarizability of Small Metal Particles: Self-Consistent Spherical Jellium Background Model. *Phys. Rev. Lett.* **1984**, *52*, 1925-1928.

19. Manjavacas, A.; Liu, J. G.; Kulkarni, V.; Nordlander, P. Plasmon-Induced Hot Carriers in Metallic Nanoparticles. *ACS Nano* **2014**, *8*, 7630-7638.

24

20. Kumarasinghe, C. S.; Premaratne, M.; Bao, Q.; Agrawal, G. P. Theoretical analysis of hot electron dynamics in nanorods. *Sci Rep* **2015**, *5*, 12140.

21. Long, R.; Prezhdo, O. V. Instantaneous Generation of Charge-Separated State on TiO2 Surface Sensitized with Plasmonic Nanoparticles. *Journal of the American Chemical Society* **2014**, *136*, 4343-4354.

22. Bernardi, M.; Mustafa, J.; Neaton, J. B.; Louie, S. G. Theory and computation of hot carriers generated by surface plasmon polaritons in noble metals. *Nature Communica- tions* **2015**, *6*, 7044.

23. Brown, A. M.; Sundararaman, R.; Narang, P.; Goddard, W. A.; Atwater, H. A. Ab initio phonon coupling and optical response of hot electrons in plasmonic metals. *Phys. Rev. B* **2016**, *94*, 075120.

24. Brown, A. M.; Sundararaman, R.; Narang, P.; Goddard, W. A.; Atwater, H. A. Non- radiative Plasmon Decay and Hot Carrier Dynamics: Effects of Phonons, Surfaces, and Geometry. *ACS Nano* **2016**, *10*, 957-966.

25. Sundararaman, R.; Narang, P.; Jermyn, A. S.; Goddard III, W. A.; Atwater, H. A. The- oretical predictions for hot-carrier generation from surface plasmon decay. *Nat Commun* **2014**, *5*.

26. Cohen-Tannoudji, C.; Diu, B.; Laloë, F. *Quantum mechanics*; Quantum Mechanics; John Wiley & Sons: Paris, 1977; pp 1344-1356.

27. Sklyadneva, I. Y.; Chulkov, E. V.; Schöne, W.-D.; Silkin, V. M.; Keyling, R.; Echenique, P. M. Role of electron-phonon interactions versus electron-electron inter- actions in the broadening mechanism of the electron and hole linewidths in bulk Be. *Phys. Rev. B* **2005**, *71*, 174302.

28. Hofmann, P.; Sklyadneva, I. Y.; Rienks, E. D. L.; Chulkov, E. V. Electron-phonon coupling at surfaces and interfaces. *New Journal of Physics* **2009**, *11*, 125005.

29. Vallée, F. Ultrafast spectroscopy of metals. *Comptes Rendus de l'Académie des Sciences - Series IV - Physics* **2001**, *2*, 1469 – 1482.

30. Ogawa, S.; Nagano, H.; Petek, H. Hot-electron dynamics at Cu(100), Cu(110), and Cu(111) surfaces: Comparison of experiment with Fermi-liquid theory. *Phys. Rev. B* **1997**, *55*, 10869–10877.

31. Haynes, W. M. *Handbook of Chemistry and Physics, 96th Edition (Internet Version 2016)*; CRC Press/Taylor and Francis: Boca Raton, FL, 2015-2016.

32. Ashcroft, N.; Mermin, N. *Solid State Physics*; Saunders College: Philadelphia, 1976; p 461.

33. Grimvall, G. The Electron-Phonon Interaction in Normal Metals. *Physica Scripta* **1976**, *14*, 63.

34. Echenique, P.; Pitarke, J.; Chulkov, E.; Rubio, A. Theory of inelastic lifetimes of low-energy electrons in metals. *Chemical Physics* **2000**, *251*, 1 – 35.

35. Voisin, C.; Christofilos, D.; Del Fatti, N.; Vallée, F.; Prével, B.; Cottancin, E.; Lermé, J.; Pellarin, M.; Broyer, M. Size-Dependent Electron-Electron Interactions in Metal Nanoparticles. *Phys. Rev. Lett.* **2000**, *85*, 2200–2203.

36. Arbouet, A.; Voisin, C.; Christofilos, D.; Langot, P.; Fatti, N. D.; Vallée, F.; Lermé, J.; Celep, G.; Cottancin, E.; Gaudry, M. *et al.* Electron-Phonon Scattering in Metal Clus- ters. *Phys. Rev. Lett.* **2003**, *90*, 177401.

37. Klein-Wiele, J.-H.; Simon, P.; Rubahn, H.-G. Size-Dependent Plasmon Lifetimes and Electron-Phonon Coupling Time Constants for Surface Bound Na Clusters. *Phys. Rev. Lett.* **1998**, *80*, 45–48.

38. Del Fatti, N.; Voisin, C.; Achermann, M.; Tzortzakis, S.; Christofilos, D.; Vallée, F. Nonequilibrium electron dynamics in noble metals. *Phys. Rev. B* **2000**, *61*, 16956–16966.

39. Aeschlimann, M.; Bauer, M.; Pawlik, S.; Knorren, R.; Bouzerar, G.; Bennemann, K. Transport and dynamics of optically excited electrons in metals. *Applied Physics A* **2000**, *71*, 485–491.

40. Knoesel, E.; Hotzel, A.; Wolf, M. Ultrafast dynamics of hot electrons and holes in copper: Excitation, energy relaxation, and transport effects. *Phys. Rev. B* **1998**, *57*, 12812–12824.

41. Maier, S. A. *Plasmonics: Fundamentals and Applications*; Springer: New York, 2007.

42. Standard Tables for Reference Solar Spectral Irradiances: Direct Normal and Hemi-spherical on $37^\circ$ Tilted Surface. 2012; https://doi.org/10.1520/G0173-03R12.

43. Tcherniak, A.; Ha, J. W.; Dominguez-Medina, S.; Slaughter, L. S.; Link, S. Probing a Century Old Prediction One Plasmonic Particle at a Time. *Nano Letters* **2010**, *10*, 1398–1404.

44. Duval Malinsky, M.; Kelly, K. L.; Schatz, G. C.; Van Duyne, R. P. Nanosphere Lithog-raphy: Effect of Substrate on the Localized Surface Plasmon Resonance Spectrum of Silver Nanoparticles. *The Journal of Physical Chemistry B* **2001**, *105*, 2343–2350.

45. Ekinci, Y.; Solak, H. H.; Löffler, J. F. Plasmon resonances of aluminum nanoparticles and nanorods. *Journal of Applied Physics* **2008**, *104*, 083107.

46. Kolobkova, E.; Nikonorov, N. Metal sodium nanoparticles in fluorophosphate glasses. *Journal of Alloys and Compounds* **2015**, *637*, 545 – 551.

47. Sergio, T. The absolute electrode potential: an explanatory note (Recommendations 1986). *Pure and Applied Chemistry* **1986**, *58*, 955.

48. Zhou, L.; Zhang, C.; McClain, M. J.; Manjavacas, A.; Krauter, C. M.; Tian, S.; Berg, F.; Everitt, H. O.; Carter, E. A.; Nordlander, P. *et al.* Aluminum nanocrystals as a plasmonic photocatalyst for hydrogen dissociation. *Nano letters* **2016**, *16*, 1478-1484.

49. Bonafe, F. P.; Aradi, B.; Guan, M.; Douglas-Gallardo, O. A.; Lian, C.; Meng, S.; Frauen-heim, T.; Sanchez, C. G. Plasmon-driven sub-picosecond breathing of metal nanoparti-cles. *Nanoscale* **2017**, *9*, 12391-12397.

50. Douglas-Gallardo, O. A.; Berdakin, M.; Sánchez, C. G. Atomistic Insights into Chemi-cal Interface Damping of Surface Plasmon Excitations in Silver Nanoclusters. *The Jour-nal of Physical Chemistry C* **2016**, *120*, 24389-24399.

Graphical TOC Entry

![](./images/867766725599298034_8.jpg)