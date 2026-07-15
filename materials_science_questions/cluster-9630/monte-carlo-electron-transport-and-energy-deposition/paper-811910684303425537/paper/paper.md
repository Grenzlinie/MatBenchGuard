# 3D SIMULATIONS OF SECONDARY ELECTRON GENERATION AND TRANSPORT IN A DIAMOND AMPLIFIER FOR PHOTOCATHODES*

D. A. Dimitrov†, R. Busby, D. L. Bruhwiler, J. R. Cary, Tech-X Corp., Boulder, CO 80303, USA
I. Ben-Zvi, T. Rao, X. Chang, J. Smedley, Q. Wu, BNL, Upton, NY 11973, USA

## Abstract
The Relativistic Heavy Ion Collider (RHIC) contributes fundamental advances to nuclear physics by colliding a wide range of ions. A novel electron cooling section, which is a key component of the proposed luminosity upgrade for RHIC, requires the acceleration of high-charge electron bunches with low emittance and energy spread. A promising candidate for the electron source is the recently developed concept of a high quantum efficiency photoinjector with a diamond amplifier. We have started to implement algorithms, within the VORPAL particle-in-cell framework, for modeling of secondary electron and hole generation, and for charge transport in diamond. The algorithms include elastic and various inelastic scattering processes over a wide range of charge carrier energies. Initial results from the implemented capabilities will be presented and discussed.

## INTRODUCTION
To address the need for high average-current, high brightness electron beams in current and future accelerator-based systems (e.g. electron cooling of hadron accelerators, energy-recovery linac light sources, and ultra-high power free electron lasers), a new design for a photoinjector with a diamond amplifier was recently proposed [1] and is under active development [2, 3].

The new photoinjector concept has a number of important advantages [2] compared to existing metallic and semiconductor photocathodes. The idea of its operation is to first generate a primary electron beam using a conventional photocathode. These electrons are then accelerated to energies of the order of 5 to 10 keV by the time they reach a diamond window of the order of 10 to 30 $\mu$m thick. These primary electrons scatter in the diamond, generating a cascade of secondary electrons. The secondary electrons drift through the diamond under the acceleration of an external radio frequency (RF) field while also participating in scattering processes. The transported, large number of secondary electrons (compared to the number of primaries) are emitted at a negative electron affinity (NEA) surface of the diamond into the accelerating cavity of the electron gun.

In order to optimize the performance of this electron gun design, it is of considerable interest to understand the generation of secondaries and their transport in diamond samples with different characteristics (thickness, concentration and type of impurities, surface effects at both metal coated and NEA surfaces) and how a diamond amplifier couples to the overall operation of the complete photoinjector system. To address this problem, we have started to develop code, within the VORPAL [4] particle-in-cell (PIC) framework, for simulation of electron generation and charge transport in diamond. Here, we report on our on-going work to enable modeling capabilities for studying secondary electron generation and transport in diamond.

## MODELING OF SECONDARY ELECTRON GENERATION IN DIAMOND
The trajectory of an electron inside diamond can be simulated [5] using a Monte Carlo algorithm. The probability for a free electron with kinetic energy $E$ to travel a time $t$ inside the diamond without experiencing a collision is modeled by $\exp\left(-t/\tau_T\left(E\right)\right)$ where $\tau_T\left(E\right)$ is the total electron mean free time $1/\tau_T\left(E\right)=1/\tau_{el}\left(E\right)+1/\tau_{in}\left(E\right)$ and $\tau_{el}\left(E\right)$, $\tau_{in}\left(E\right)$ are the elastic, inelastic mean free times, respectively. We obtained the energy dependent mean free times from the total elastic and inelastic scattering cross sections given in Ref. [6]. The mean free times for the range of energies considered here are shown in Fig. 1. To simulate scattering processes, we implemented a Monte Carlo algorithm extended with the null collision method which is often used to simulate carrier transport [7]. Thus, our implementation is general and can directly be extended to handle additional scattering processes (e.g. inelastic processes involving phonons and impurities).

![](./images/811910684303425537_1.jpg)

Figure 1: The mean free times $\tau\left(E\right)$ (and the related mean free paths and scattering rates) can be calculated from the total scattering cross sections. The mean free times, shown here, indicate the characteristic time scales for these processes and the limitations they impose in Monte Carlo simulations.

---
*This work was supported by the US DoE under grants DE-FG02-06ER84509 (Tech-X) and DE-AC02-98CH10886 (BNL)
† dad@txcorp.com

05 Beam Dynamics and Electromagnetic Fields
D05 Code Developments and Simulation Techniques
1-4244-0917-9/07/$25.00 ©2007 IEEE

We implemented two models for elastic scattering. The first model considers the elastic scattering process to be isotropic (as in acoustic phonon scattering processes). The second model takes into account anisotropy making small angle scattering more probable relative to other angles. It is based on the Conwell-Weisskopf approach applicable to, e.g., ionized impurity scattering [7]. We are considering to implement a more accurate model, based on quantum mechanical formalism, in a future development. For the in-

![](./images/811910684303425537_2.jpg)

Figure 2: The generation of secondary electrons in inelastic scattering processes involves excitation of an electron from the valence band to the conduction one creating electron-hole pairs.

elastic scattering, we implemented an algorithm based on the approach developed by Ziaja *et al.* [8]. In this algorithm, at each time step, given the energy $E$ of an existing electron that has been selected to participate in an inelastic scattering event, we choose first the energy $\omega$ that the electron will lose in the inelastic process (unless explicitly specified, we use atomic units $\hbar = m = e = 1$). We determine this energy by drawing a sample from the probability distribution for losing energy $\omega$ given the initial energy of the primary electron, $E$. The probability density function (pdf) $p\left(\omega \mid E\right)$ of this distribution can be calculated from the doubly differential inelastic cross section

$$
\frac{\partial^{2} \sigma_{i n}(q, \omega, E)}{\partial q \partial \omega}=\frac{1}{n \pi a_{0} E q} \operatorname{Im}\left(-\epsilon^{-1}(q, \omega)\right), \quad (1)
$$

where $E$ is the initial energy of the primary electron, $\omega$ is its energy loss in the inelastic scattering process, and $q$ is the magnitude of its momentum change. The momentum change has to satisfy $q_{-} \leq q \leq q_{+}$with $q_{\pm}=k\left(1 \pm \sqrt{1-(\omega / E)}\right)$, where $\epsilon(q, \omega)$ is the dielectric function for diamond and $\operatorname{Im}\left(-\epsilon^{-1}(q, \omega)\right)$ is the energy loss function (ELF). For the ELF, we used the data given by Ziaja *et al.* [8].

After an inelastic scattering process has been identified and the energy loss value $\omega$ for the primary electron has been drawn from the probability distribution with pdf $p\left(\omega \mid E\right)$, the code proceeds to draw a value for the magnitude of the momentum change $q$ of the primary. This value is sampled from the probability distribution with pdf $p\left(q \mid \omega, E\right)$ that is also calculated using the doubly differential inelastic cross section, Eq. (1). The pdfs are often calculated in the Ashley and/or TPP2 approximation models [8]. The simulations presented here are using the Ashley model. For the sampling from these conditional pdfs, we implemented a von Neumann rejection algorithm. To maintain conservation of momentum for independently chosen $E$ and $\omega$ values, the value of $q$ has to satisfy the inequalities $||\mathbf{p}_{e,s}^{i}|-|\mathbf{p}_{e,s}^{f}||<q<|\mathbf{p}_{e,s}^{i}|+|\mathbf{p}_{e,s}^{f}|$, where $\mathbf{p}_{e,s}^{i}$ is the initial and $\mathbf{p}_{e,s}^{f}$ the final momentum of the produced secondary electron. The electron-hole excitation process in diamond is shown in Fig. 2. This diagram also gives a short description of how the algorithm we implemented works: the initial energy $E_0$ of a valance electron is sampled, then the energy loss $\omega$ of the primary electron (or hole) is sampled and if $\hbar\omega>E_C-E_0$, a secondary electron with kinetic energy of $\hbar\omega-E_C+E_0$ and a hole with kinetic energy of $E_V-E_0$ are created; momenta and energies of all particles are updated to conserve total energy and momentum. In the current implementation, we consider two limiting cases for inelastic scattering processes [5]. The first case is with no transfer to the lattice allowed for energy loss $\omega<E_G$ and the second is when such loss is taken into account. In the current implementation, the initial energy of an electron in the valence band is sampled from the Fermi-Dirac distribution at $T=0$ K.

## SIMULATION RESULTS

To evaluate the implemented algorithms, we started with a previously studied simulation test case [8,5]. It consists of a single primary electron with energy $E=E'+E_C$, where for diamond $E_C\approx29$ eV (the valance band width is 23 eV and the gap is $E_G=5.46$ eV). The values of $E'$ were chosen from 250 eV to 1 keV.

For these parameters, the average energy sampled from the Fermi-Dirac distribution at $T=0$ K, is $3E_V/5\approx13.8$ eV. Thus, the average energy to create an electron-hole pair is $E_{e-h}=E_V+E_G-3E_V/5\approx14.66$ eV leading to an expected maximum number of secondary electrons produced $N_{e,s}^{max}=E'/E_{e-h}$.

The results for the average number of secondary electrons produced over time (from an average over 200 runs) with $E'=250$ eV for the primary electron are shown in Fig. 3. In this case, $N_{e,s}^{max}=17$. We are reaching a value close to this number after about 1000 fs but the plot in the figure is truncated to 100 fs to allow for easier comparison with the corresponding plot in [5]. The results for $N_{e,s}^{max}$ from a test primary electron with $E'=1$ keV from 200 runs are also shown in Fig. 3. The expected maximum number of secondaries in this case is $N_{e,s}^{max}=68$. Results from simulations of $N_{e,s}^{max}$ as a function of the initial energy of the primary test electron for $E'=250,500,750,1000$ eV are shown in Fig. 4.

Overall, our simulation results are in qualitative to fair agreement with previous simulation results on electron scattering in diamond [8,5,6] particularly taking into account that we are not comparing these results under the same conditions. The results we present here are for the Ashley model with the band structure taken into account as

![](./images/811910684303425537_3.jpg)

Figure 3: The dependence of the number of generated secondary electrons for the two limiting cases (with loss to the lattice and with no loss allowed) is simulated for two initial energies of a primary electron: $E = 250 + E_C$ eV, lower two curves, and $E = 1000+E_C$ eV, upper two curves. The number of secondaries for the limiting case with no loss to the lattice is close to the number reported by Ziaja et al. [5] at $t = 100$ fs (14 vs 10). We observe a larger number of secondaries at 100 fs for the model with loss to the lattice compared to the value they reported (10 vs 6). However, they did not include the generation of secondaries due to created holes while we include this effect.

![](./images/811910684303425537_4.jpg)

Figure 4: The maximum average number of secondary electrons produced for four different initial energies (above $E_C$) of the primary electron for the two limiting cases with no loss to the lattice (circles) and with such energy loss (squares) in inelastic collisions. These numbers are consistent with what is expected for each of the cases.

in Ref. [5, 6], at $T = 0$ K, and the holes allowed to scatter and to also generate electron-hole pairs.

However, the results in Ref. [5], the main ones we compare with here, are based on simulations that did not include the scattering of holes and their contribution to the generation of electron-hole pairs. They are also at $T > 0$ K. Both of these effects lead to smaller average number of secondary generated electrons in their simulations. The results in Ref. [8], did not take into account the band structure. They treated diamond in the free-electron approximation. The results in Ref. [6] are from simulations with models that allowed holes to scatter and to generate secondaries but did not include values for the the average number of electrons from the Ashley model; only results from TPP2 based models were reported. We will add the TPP2 model and the non-zero temperature effect in Phase II. This will allow us to better verify the implemented models against published results. We also analyzed the secondary electron energies and the particle spatial distributions (these results are not included here due to space limitations) at three different times after the primary electron enters the diamond. Our results show similar behavior and are close to the previously reported values of these quantities [5].

## SUMMARY

We have implemented Monte Carlo models, within the VORPAL PIC code, for simulation of secondary electron generation and elastic scattering in diamond. The first simulation results from the code are in fair agreement with previously published simulation studies even though the comparison was not done under the same conditions due to differences in the implemented approaches. More importantly, these results indicate that a gain of the order of up to two orders of magnitude is possible for primary electrons with several keV of energies. In future developments, the code will be extended with models for electron-phonon and charge impurity scattering, electron-hole recombination, and temperature effects. Once these are implemented, the simulations will be compared to experimentally measured quantities such as drift velocity and yield of transmitted electrons.

## REFERENCES

[1] I. Ben-Zvi, X. Chang, P. D. Johnson, J. Kewisch, and T. Rao. Secondary emission enhanced photoinjector. C-AD Accelerator Physics Report C-A/AP/149, Brookhaven National Lab, 2004.

[2] T. Rao, Ilan Ben-Zvi, A. Burrill, X. Chang, S. Hulbert, P. D. Johnson, and J. Kewisch. Diamond amplifier for photocathodes. In V. Yakimenko, editor, *Advanced Accelerator Concepts: Eleventh Workshop*. American Physical Society, 2004.

[3] X. Chang, I. Ben-Zvi, A. Burrill, S. Hulbert, P. D. Johnson, J. Kewisch, T. Rao, J. Smedley, Z. Segalov, and Y. Zhao. Measurement of the secondary emission yield of a thin diamond window in transmission mode. In C. Horak, editor, *2005 Particle Accelerator Conference*. IEEE, number 2251-3, 2005.

[4] C. Nieter and J. R. Cary. VORPAL: a versatile plasma simulation code. *J. Comput. Phys.*, 196:448–473, 2004.

[5] B. Ziaja, A. Szöke, D. van der Spoel, and J. Hajdu. Space-time evolution of electron cascades in diamond. *Phys. Rev. B*, 66:024116–1/9, 2002.

[6] B. Ziaja, R. A. London, and J. Hajdu. Unified model of secondary electron cascades in diamond. *J. Appl. Phys.*, 97:064905–1/9, 2005.

[7] M. Lundstrom. *Fundamentals of Carrier Transport*. Cambridge University Press, second edition, 2000.

[8] B. Ziaja, D. van der Spoel, A. Szöke, and J. Hajdu. Auger-electron cascades in diamond and amorphous carbon. *Phys. Rev. B*, 64(214104-1/8), 2001.