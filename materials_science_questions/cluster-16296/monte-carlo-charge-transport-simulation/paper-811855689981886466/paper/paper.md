![](./images/811855689981886466_1.jpg)

Energy conservation in collision broadening over a sequence of scattering events in semiclassical Monte Carlo simulation

Z. Aksamija and U. Ravaioli

Citation: *Journal of Applied Physics* **105**, 083722 (2009); doi: 10.1063/1.3116544
View online: http://dx.doi.org/10.1063/1.3116544
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/105/8?ver=pdfcov
Published by the AIP Publishing

### Articles you may be interested in
[Monte Carlo calculations of electron transport in silicon and related effects for energies of 0.02–200 keV](http://)
J. Appl. Phys. **106**, 113703 (2009); 10.1063/1.3256195

[SelfConsistent Wigner Monte Carlo Simulations of Current in Emerging Nanodevices: Role of Tunneling and Scattering](http://)
AIP Conf. Proc. **893**, 1395 (2007); 10.1063/1.2730425

[Ensemble Monte Carlo Transport Simulations for Semiconducting Carbon NanoTubes](http://)
AIP Conf. Proc. **772**, 1049 (2005); 10.1063/1.1994472

[Analytic band Monte Carlo model for electron transport in Si including acoustic and optical phonon dispersion](http://)
J. Appl. Phys. **96**, 4998 (2004); 10.1063/1.1788838

[Improved algorithm for modeling collision broadening through a sequence of scattering events in semiclassical Monte Carlo](http://)
J. Appl. Phys. **87**, 303 (2000); 10.1063/1.371861

![](./images/811855689981886466_2.jpg)

# Energy conservation in collision broadening over a sequence of scattering events in semiclassical Monte Carlo simulation

Z. Aksamija${}^{\mathrm{a)}}$ and U. Ravaioli

Department of Electrical and Computer Engineering and Beckman Institute, University of Illinois,
Urbana, Illinois 61801 USA

(Received 8 December 2008; accepted 9 March 2009; published online 30 April 2009)

In this paper, we discuss energy conservation when collisional broadening is considered, and a Lorentzian lineshape assumed, in a Monte Carlo simulation of electron transport. We show that collisional broadening with a Lorentzian distribution does not lead to energy conservation on the average over many electron-phonon collision events. We compute the expected value of departure from energy conservation for a realistic silicon bandstructure, and compare it to results from full-band Monte Carlo simulation to show good agreement. Finally, we propose a corrected distribution approach, where the Lorentzian distribution is divided by the density-of-states curve to obtain a distribution which is able to conserve energy in the average over many electron-phonon collisions. © 2009 American Institute of Physics. [DOI: 10.1063/1.3116544]

## I. INTRODUCTION

Electron-phonon coupling is central to semiconductor transport simulation. It is usually treated in the Fermi’s golden rule formulation, but even at modest fields, such as those commonly present in modern semiconductor devices, finite state lifetime effects become important. $^{1}$ Such effects are treated formally by including self-energy in the scattering formulation. $^{2}$ In order to make the problem more tractable, especially for efficient Monte Carlo (MC) simulation of electron transport, various simplifying assumptions are made. The most common form is to assume a Lorentzian distribution in energy. This assumption is well justified by perturbation theory and is relatively simple to calculate and implement. In the limit of infinite state lifetime, it collapses to the energy-conserving delta function of the Fermi’s golden rule. On the other hand, when nonzero broadening is present, energy is no longer conserved exactly in each scattering event, and this has been noted to lead to accumulated broadening over many scattering events. $^{3}$ Past attempts to include collision broadening in semiclassical MC simulation of electron transport have noted that the broadening can be accumulated over many electron-phonon collisions during the simulation. $^{4}$ This accumulation of broadening adds spurious unphysical energy to the electron population. Such accumulation of energy can lead to nonphysical results and push the electron energy distribution into the hot electron regime. $^{1}$ One approach has been to remove the broadening from previous collision at each new collision so that at each instant only the broadening of one single collision event is felt by the electron. This removes the problem of accumulation of broadening but does not allow electrons to undergo an entire sequence of collision broadenings, which they need to do in order to fully simulate the quasiparticle nature of electrons in the presence of collision broadening. Our goal is to explore the reasons for this accumulation of energy and propose remedies, which can be implemented in standard semiclassical MC simulation tools in order to avoid accumulation of broadening and guarantee that energy conservation is achieved over many electron-phonon scattering events, thereby ensuring accuracy of the simulation.

Although the Lorentzian distribution does not strictly conserve energy, due to its symmetry and from physical principles, we do expect that in the average over many scattering events total energy is conserved. This is especially important to any kind of MC simulation of particles, where we have an ensemble of many thousands of particles, which are simulated for many thousands of time steps so that the overall number of scattering events occurring in the course of the simulation can be in the millions. Each such scattering event will not be energy conserving when broadening is considered and a Lorentzian lineshape is used.

## II. PROBLEM FORMULATION

We will focus on the dominant optical phonon scattering and approximate the optical phonon energy to be a constant $\omega_{o}$. Under this assumption, the Lorentzian distribution for the final energy after scattering takes the form of Eq. (1). The amount of broadening, represented by $\Gamma$, can be related by the optical theorem $^{5}$ to the total electron scattering rate $\mathbf{R}$, and the lifetime $\tau$, as in Eq. (2),

$$
P(E_{f})=\frac{1}{\pi} \frac{\Gamma}{\left(E_{f}-E_{i} \pm \omega_{o}\right)^{2}+\Gamma^{2}},\qquad(1)
$$

$$
\Gamma(E_{f})=\frac{\hbar}{2} R(E_{i}+\omega_{o})=\frac{\hbar}{2 \tau(E_{f})}.\qquad(2)
$$

Therefore, the value of final energy can be considered as a random variable, and a standard rejection technique can be employed to select the final energy according to the Lorentzian distribution. Under this view, we can also compute the expectation of the final energy for any initial energy level and verify if the expected value matches the optical phonon energy; in other words, we can compute how much the final

${}^{\text{a)}}$Electronic mail: aksamija@illinois.edu.

energy deviates from energy conservation in the average over many scatterings. This can be expressed in the standard form, as in Eq. (3). At first glance, it seems like the expectation will be energy conserving since the distribution is symmetric in energy, but due to the complex bandstructure in realistic materials, states are distributed uniformly in momentum space, but they are distributed nonuniformly in energy. Therefore we must convert the integral into an integral over momentum space Eq. (4), which is equivalent to an energy integral weighted by the density of states (DOS), as in Eq. (5),

$$
\left\langle E_{f}\right\rangle=\int d \vec{k} \frac{1}{\pi} \frac{\Gamma}{\left(E(\vec{k})-E_{i} \pm \omega_{o}\right)^{2}+\Gamma^{2}},
\tag{3}
$$

$$
\left\langle E_{f}\right\rangle=\frac{1}{\pi} \int \frac{E d E}{\left|\nabla_{\vec{k}} E(\vec{k})\right|} \frac{\Gamma}{\left(E(\vec{k})-E_{i} \pm \omega_{o}\right)^{2}+\Gamma^{2}},
\tag{4}
$$

$$
\left\langle E_{f}\right\rangle=\frac{1}{\pi} \int \frac{E g(E) \Gamma(E)}{\left(E-E_{i} \pm \omega_{o}\right)^{2}+\Gamma(E)^{2}} d E.
\tag{5}
$$

This formulation allows us to compute the difference between the expected value of the final energy and the energy conserving value, which is equal to initial plus phonon energy $\widetilde{E}_{f}=E_{i} \pm \omega_{o}$.

### III. CORRECTED DISTRIBUTION ALGORITHM FOR MC SIMULATION

The relevant parameters for our simulation, such as the DOS, can be computed numerically from realistic energy bandstructure for most semiconductors of interest. Full electron bandstructure of silicon is obtained from empirical pseudopotential calculations. $^{6}$ The DOS is then computed using the algorithm by Gilat and Raubenheimer, $^{7}$ which divides the first Brillouin zone into small cubes, and approximates the intersection of the energy conserving surface with each cube by a plane. The DOS is then computed by summing the contribution of each small cube. We use a grid of $40 \times 40$ $\times 40$ points in the irreducible wedge of the first Brillouin zone. The numerical result for silicon is shown in Fig. 1. The integration over energy can then be performed by numerical quadrature to plot the expected, or average, value of departure from energy conservation as a function of initial energy, shown in Fig. 2. The resulting plot can be compared to the gradient of the DOS in order to explain the effect of loss of energy conservation. The plots are very similar because a slope in the DOS will cause a net difference of the effect of broadening for different energies, causing the average departure from energy conservation to be nonzero. This is explained by the following: if the DOS is constant, then for each final state with energy in excess of energy conservation, there will be one that is below the energy conserving value by the same amount, and the two contributions will cancel. When there is some structure and slope to the DOS curve, the number of states will vary from energy level to level, and such cancellation of broadening will not occur. For an increasing DOS curve, the slope is positive causing a systematic preference for final energy levels that have more energy than what is dictated by energy conservation. This causes each scattering event to add additional energy to the particle that will not be subtracted away elsewhere.

![](./images/811855689981886466_3.jpg)

FIG. 1. Electronic DOS curve. The DOS counts the number of states near a given energy, therefore expressing the mapping from the three-dimensional momentum space into one-dimensional energy. It is computed numerically form the full electron bandstructure. The electron DOS has two sharp peaks where the bandstructure is flat and correspondingly the energy gradient small.

Another way to see this is to compare the contributions of two closely spaced energy levels. The level with the larger density of states will contribute more to the broadening, causing a net departure from energy conservation. In order to correct this problem, various solutions have been proposed, such as storing the amount of broadening at each scattering

![](./images/811855689981886466_4.jpg)

FIG. 2. Numerically computed expected value of departure from energy conservation, shown by solid line, and derivative of the DOS, dashed line. Values are in meV. Note that, especially at higher electron energies, several meV of energy can be accumulated at each scattering event. This can lead to large unphysical energies in the simulation because energy conservation is not upheld. The striking similarity of the curves demonstrates that the departure from energy conservation at each scattering is due to nonuniform spacing of energy levels and large slopes of the DOS curve, especially at higher energies.

![](./images/811855689981886466_5.jpg)

FIG. 3. Plot of corrected (solid line) and original (dashed line) Lorentzian broadening distribution. The corrected distribution is scaled by the DOS in order to offset the effect of nonuniform level spacing, or degeneracy, and produce a distribution that will conserve energy on the average over many scattering events.

event in the simulation, and subtracting away this broadening at the following scattering event. This was termed nonaccumulated broadening (NAB). $^{8}$ The approach was termed NAB due to its property that the broadening is not allowed to accumulate. But this property is exactly the issue with the NAB approach, as electrons are not allowed to undergo a whole sequence of broadening collisions and explore the quasiparticle states, but are instead only allowed to "feel" the impact of one single broadening at a time. This procedure successfully removes unphysical drift toward high energies, remedies the runaway broadening problem, and makes the MC simulation stable and accurate, but also prevents the full impact of quasiparticle states to be explored.

An alternative solution is to correct the Lorentzian distribution and divide it by the DOS curve, Fig. 3, in order to arrive at an energy distribution, which is energy conserving in the average over many particles/scattering events. The motivation is simply in the fact that it is not the Lorentzian distribution that causes the problem. The Lorentzian distribution is symmetric around the energy-conserving point so it would uphold energy conservation in the average over many scattering events were it not for the slope in the DOS curve of realistic semiconductor materials. In order to remove the effect of the DOS, we simply divide the Lorentzian distribution by the DOS curve and use this resulting distribution to select the broadened final states. This procedure ensures that the contribution from the DOS, the $g(E)$ in Eq. (5), cancels out and the results is exactly symmetric. Therefore, the integral (5) will be zero if we use a Lorentzian distribution divided by the DOS curve, as shown in Eq. (6). The $g(E)$ is assumed to be normalized. This idea can be termed a corrected distribution approach. Both of these techniques have been implemented into a full-band three-dimensional MC simulation, the details of which have been previously published. $^{9}$ The impact on the overall energy conservation has been tabulated throughout a MC simulation of a representative silicon device and explored. The results show a good agreement with the numerically computed results (5), as compared in Fig. 4,

$$
P(E_{f})=\frac{1}{\pi} \frac{1}{g(E_{f})} \frac{\Gamma}{\left(E_{f}-E_{i} \pm \omega_{o}\right)^{2}+\Gamma^{2}}. \tag{6}
$$

![](./images/811855689981886466_6.jpg)

FIG. 4. Plot of energy broadening extracted from a full-band MC simulation (solid line). The deviation from energy conservation follows the same trends as the numerically computed expected value of final energy (dashed line). This demonstrates that final energies in MC simulation including collisional broadening obey the expected trend and need to be corrected by the DOS.

We also note that as initial and final electron energies involved in a collision approach the band-gap, the corrected distribution becomes more skewed, Fig. 5. This makes energy conservation in the average over many collision events possible even at the lower values of energy where collisions are much less frequent. Therefore, dividing the Lorentzian distribution by the DOS ensures energy will be conserved on the average over all the scattering events in the simulation,

![](./images/811855689981886466_7.jpg)

FIG. 5. Plot of corrected (solid line) and original (dashed line) Lorentzian broadening distribution at lower energies near the band-gap. As the value of initial and final electron energies approaches the gap, the DOS approaches zero, so the corrected distribution becomes more and more skewed, thus ensuring that energy conservation is achieved on the average.

thereby preventing spurious accumulation of energy which leads to runaway broadening.

## ACKNOWLEDGMENTS
This work was supported by the Department of Energy Computational Science Graduate Fellowship Program of the Office of Science and National Nuclear Security Administration in the Department of Energy under Contract No. DE- FG02-97ER25308.

¹G. Ferrari, A. Asenov, M. Nedjalkov, and C. Jacoboni, J. Comput. Elec- tron. 5, 419 (2006).
²J. R. Barker, J. Phys. C 6, 2663 (1973).
³K. Kim, B. A. Mason, and K. Hess, Phys. Rev. B 36, 6547 (1987).
⁴L. Reggiani, P. Lugli, and A. P. Jauho, Phys. Rev. B 36, 6602 (1987).
⁵Y.-C. Chang, D. Z. Tang, J. Y. Tang, and K. Hess, Appl. Phys. Lett. 42, 76 (1983).
⁶M. L. Cohen and T. K. Bergstresser, Phys. Rev. 141, 789 (1966).
⁷G. Gilat and L. J. Raubenheimer, Phys. Rev. 144, 390 (1966).
⁸L. F. Register and K. Hess, J. Appl. Phys. 87, 303 (2000).
⁹A. Duncan and U. Ravaioli, IEEE Trans. Electron Devices 45, 867 (1998).