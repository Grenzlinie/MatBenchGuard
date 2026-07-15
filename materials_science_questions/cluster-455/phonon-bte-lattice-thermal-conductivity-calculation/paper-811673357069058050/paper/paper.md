# A Tight-Binding Hamiltonian for Band Structure and Carrier Transport in Graphene Nanoribbons

Daniel Finkenstadt¹, Gary Pennington², and Michael J Mehl¹

¹Code 6390, U.S. Naval Research Laboratory, 4555 Overlook Ave. SW, Washington, DC, 20375
²U.S. Army Research Laboratory, Adelphi, MD, 20783

## ABSTRACT

To understand nanoribbons of graphene, we developed an ab initio parametrized fit to Carbon and Hydrogen chemical data, out to arbitrary neighbor interactions, including relaxations. Our computed band structure confirms the well-known three-family behavior of armchair band gaps but also predicts a similar familial behavior for conductance in nanoribbon transistors. The Boltzmann carrier transport simulations from calculated phonon spectra show, over a range of temperatures, the familial conductance behavior. Both the peak field-effect mobility and the "on" conductance increase with ribbon width, the later being proportional to the width and inversely proportional to the lattice temperature. We will also discuss phonon-limited scattering of charge carriers in graphene.

## INTRODUCTION

Understanding and predicting carrier transport and scattering in graphite nanoribbons (GNRs) is important for potential nanoscale device applications, including use as ultra-small transistors and as bio/chemical sensors. Semiconducting GNRs , including armchair nanoribbons (ANRs) [1], are best suited for such applications since a gate potential may effectively turn the device current on and off by moving the Fermi level into and out of the carrier bands.

Previous transport studies have focused mainly on the ballistic transport regime. Here we focus on phonon-limited semi-classical transport, a regime that has been shown to describe many transport features in carbon nanotubes [2] but has received only limited attention in nanoribbons [3]. Semiclassical transport is applicable when the carrier mean free path between scattering events is much smaller than the ribbon length L. This transport regime is of interest since: 1) it allows for the incorporation of a relatively simple and highly predictive scattering theory, 2) many of the 'bulk' transport features obtained are also found in other regimes and 3) it gives the limits of the ballistic and phase coherent transport regimes. Phonon scattering will be considered since this mechanism is found to be significant in similar materials such as graphite and carbon nanotubes [2]. As both transport and associated scattering mechanisms depend strongly on the low-energy electronic structure of carriers, we find that important semi-classical transport properties also vary with the three ANR families.

Our approach will use a highly sophisticated tight-binding method, including arbitrary neighbor interactions, forces and relaxations, to describe the relaxed band-structure and phonon dispersions of ANRs, as a function of width. These data are then input into our transport model.

# THEORETICAL METHODS

We previously fit [1,4] tight-binding parameters for the C-H system to linearized augmented plane-wave results for diamond, graphite and simple cubic structures [5], as well as to the C2, H2, C6 and H6 dimers and rings computed via a Gaussian-based, all-electron density-functional theory. For C-H interactions, we fit methane, ethane and benzene. Subsequently, we have found that our parameters are stable for a variety of molecules and nanostructures: ethylene, cyclopropane, spiropentane, cubane, triangulanes and diamondoid nanorods. We have tested these systems with our parameters using two tight-binding codes: NRL-TB (static electronic structure) and TBMD (molecular dynamics and relaxations) [6,7]. In a previous work [1], we calculated the frozen-phonon dispersion for graphene; here, we test again the phonons of graphene, this time using the velocity autocorrelation method, as a way to obtain the vibrational spectra directly from molecular-dynamics data, including anharmonicity. In Figure 1, we show our calculated vibrational spectra for methane, compared to graphene and an ANR. We found in a previous work [8] that velocity autocorrelation gives a reasonable spectra, except for occasional pathological cases at high-symmetry points. For methane, our parameters fit closely with recent velocity-autocorrelation-calculated spectra using a different first-principles method [9]. While we continue to test other systems, we find that our parameters are very stable and seem to have a broad range of applicability to many C-H systems.

![](./images/811673357069058050_1.jpg)

Figure 1. Tight-binding calculated vibrational spectra, at T = 300K, for methane and graphene.

## Armchair nanoribbon carrier transport

To simulate ANR carrier transport, we solve the 1-d Boltzmann transport equation:

$$(\mathrm{eF} / \hbar) \partial_{\mathrm{k}} \mathrm{f}_{\mathrm{k}}=\Sigma_{\mathrm{q}}\left[\mathrm{f}_{\mathrm{k}+\mathrm{q}}\left(1-\mathrm{f}_{\mathrm{k}}\right) \mathrm{S}_{\mathrm{k}+\mathrm{q}, \mathrm{k}}-\mathrm{f}_{\mathrm{k}}\left(1-\mathrm{f}_{\mathrm{k}+\mathrm{q}}\right) \mathrm{S}_{\mathrm{k}, \mathrm{k}+\mathrm{q}}\right] \tag{1}$$

under near equilibrium conditions when the externally-applied axial field is small ($\mathrm{F} < \mathrm{k_B T/L}$ for ribbon-length L). The resulting non-equilibrium carrier distribution function $\mathrm{f_k}$ is then used to calculate the multicarrier ribbon conductance. Here the carrier-phonon scattering rate $\mathrm{S_{k,k+q}}$ is for axial momentum transfer $\mathrm{k} \rightarrow \mathrm{k + q}$ (wave vector takes on +/- values). Only the first electron subband is considered. Along with the scattering rate, $\mathrm{f_k}$ will be determined by the carrier charge density n. If the band structure is known, n is found from the Fermi level which is set by a transistor gate voltage. Using 1st order perturbation theory, equation 2 gives the scattering rate:

$$\mathrm{S_{k,k+q}} = \hbar \, \mathrm{D^2(q) \, DOS(k+q) \, [N_{ph}(E_{ph}) + 0.5 \pm 0.5] / (\pi \rho E_{ph} w)} \tag{2}$$

with $\mathrm{D = 16eV * q}$ the in-plane acoustic deformation potential of graphite, $\rho = 7.6 * 10^{-7} \, \mathrm{kg/m^2}$ for graphene, ribbon width is w, and $\mathrm{N_{ph}}$ is the Bose-Einstein phonon occupation, at a specified temperature T. The +/- is for emission/absorption. The carrier density of states (DOS) was calculated directly from our tight-binding approximated band structure, in Figure 2, with the ANR band gaps and Fermi velocity $\mathrm{v_F}$ calculated in [1]. Since we focus on long, thin ribbons, we consider only the low-energy $\mathrm{E_{ph}}$, contributing longitudinally polarized phonons for ideal graphene (up to the first peak below $750 \, \mathrm{cm^{-1}}$ in Figure 1).

Once $\mathrm{f_k}$ is found, the nanoribbon conductance is given, as shown in [2], by equation 3.

$$\mathrm{G = (e \, n / \hbar \, FL) \Sigma_k \, sgn(k) \, f_k \, DOS^{-1}(k) / \Sigma_k \, f_k} \tag{3}$$

The derivative with respect to density, $\mathrm{(L/e) \partial_n G}$, gives the field-effect mobility.

## RESULTS

The ANR exhibits hyperbolic bands that, in the limit of very wide ribbons, approach the ideal band structure in Figure 2, which is the band structure of an infinite sheet of graphene, folded multiple times back onto the $\Gamma \rightarrow \mathrm{K} \rightarrow \mathrm{M}$ line in k-space. As the width of the ribbon decreases, and the edges are relaxed, we find that a band gap opens, along with changes in the Fermi velocity $\mathrm{v_F}$, in inverse proportion to the ribbon width w. These gaps affect the inverse DOS in equation 3. Interestingly the variations in band gap occur in three families of ribbon widths, namely, the $3\mathrm{j}$ and $3\mathrm{j} \pm 1$ increments of ribbon width, measured as the number of dimer rows [10]. In our previous work [1], we verified this behavior, and we extended the familial grouping of band gap deviations also to the Fermi velocity, as well as to the conductance, which depends on band gap through the DOS. We repeat our calculations on conductance here, this time for only a few ribbon widths, to study the temperature-dependence of conductance, which in our preliminary results, behaves as a power law.

![](./images/811673357069058050_2.jpg)

Figure 2. Band-structure of graphene, folded multiple times onto $\Gamma \rightarrow \text{K} \rightarrow \text{M} \rightarrow \text{K} \rightarrow \Gamma$.

Transport simulations of an ANR transistor device are shown in Figure 3, where G is found to exhibit well-defined "on" and "off" states as n is varied. The on-state conductance is reached as n approaches the minimum value of $2/\text{h}v_{\text{F}}$ and increases with $v_{\text{F}}$ as a result of fast moving carriers and a smaller DOS for backscattering. The "on" conductance and the peak mobility are both found to increase roughly linearly as a function of ribbon width (dimer rows). The former result agrees with recent experimental measurements of the maximum conductance [11]. Expected trends are found when the transport properties of an ANR are compared: the 3j-1 and 3j families have the largest slope, and the 3j family has larger "on" conductance.

![](./images/811673357069058050_3.jpg)

Figure 3. Small-field approximated conductance of an armchair nanoribbon transistor showing variation among the three families: 3j (dimers = 12), 3j+1 (dimers = 10) and 3j-1 (dimers = 11).

For temperature-dependent conductance, we have three ANRs of varying width in Figure 3, showing a general trend towards higher conductance, with decreasing temperature, due to reduced phonon scattering. We find that the on conductance varies approximately as the inverse of the lattice temperature $\mathrm{G_{on}(T) = G_{on}(300K)*[300K/T]^\beta}$, where $\beta$ ~< 1.

## CONCLUSIONS

By developing a fully-general tight-binding Hamiltonian from first principles, we were able to study graphene with arbitrary neighbor-interactions and hydrogen-termination. Only for monolayer ribbons with width less than 5 nm do we find an appreciable band gap for engineering devices, such as those proposed by Obradovic [3]. Accordingly, we simulated monolayer nanoribbon transistors, in a phonon-scattering-limited regime.

Our results show that characteristic band structure variations among the armchair nanoribbon families also lead to variations in carrier transport, e.g. in transistors or in sensor applications that exploit the sensitive edge-bonding characteristics. This systematic trend also occurs over a range of temperatures from 200 – 400 K, with lower temperatures giving higher conductance. The on conductance is found to be approximately inversely proportional to the lattice temperature in the phonon-limited transport regime. Extensions of the three-family band-gap behavior [10,1] were found at all temperatures for carrier group velocity, conductance and

field-effect mobility. Interestingly two families of ribbons had large gaps but opposite deviations in ideal carrier group velocity with respect to the ribbon width. These deviations gave slow and fast switching characteristics, since a gate voltage can turn the nanoribbon transistor on (saturated) or off. Such devices could be exploited for nanoscale electronics and also for chemical-sensing based on the sensitivity of nanoribbons to edge states.

NOTICE: At the date this paper was written, URLs or links referenced herein were deemed to be useful supplementary material to this paper. Neither the author nor the Materials Research Society warrants or assumes liability for the content or availability of URLs referenced in this paper.

## ACKNOWLEDGMENTS

We acknowledge the support of the Office of Naval Research, DOD HPCMPO CHSSI, and the National Research Council. We also thank M. S. Fuhrer for fruitful discussions and C. Ashman at HPTI, for code support.

## REFERENCES

1. D. Finkenstadt, G. Pennington and M. J. Mehl, *Phys. Rev. B* **76**, 121405(R) (2007).
2. G. Pennington and N. Goldsman, *Phys. Rev. B* **68**, 045426 (2003); G. Pennington, N. Goldsman, A. Akturk and A. E. Wickenden, *Appl. Phys. Lett.* **90**, 062110 (2007).
3. B. Obradovic, R. Kotlyar, F. Heinz, P. Matagne, T. Rakshit, M. D. Giles, M. A. Stettler and D. E. Nikonov, *Appl. Phys. Lett.* **88**, 142102 (2006).
4. The parameters used in this paper are available from the authors, or at http://cst-www.nrl.navy.mil/bind/
5. D. A. Papaconstantopoulos, M. J. Mehl, S. C. Erwin and M. R. Pederson, in *Tight-Binding Approach to Computational Materials Science*, edited by P. Turchi, A. Gonis and L. Colombo, (Mater. Res. Soc. Proc. **491**, Pittsburgh, PA, 1998) p. 221.
6. R. E. Cohen, M. J. Mehl and D. A. Papaconstantopoulos, *Phys. Rev. B* **50**, 14694 (1994); M. J. Mehl and D. A. Papaconstantopoulos, *ibid.* **54**, 4519 (1996).
7. D. A. Papaconstantopoulos and M. J. Mehl, *J. Phys.: Condens. Matter* **15**, R413 (2003), and references therein.
8. D. Finkenstadt, N. Bernstein, J. L. Feldman, M. J. Mehl and D. A. Papaconstantopoulos, Phys. Rev. B 74, 184118 (2006).
9. J. A. Greathouse, R. T. Cygan and B. A. Simmons, *J. Phys. Chem. B* **110**, 6428 (2006).
10.Y.-W. Son, M. L. Cohen and S. G. Louie, *Nature* **444**, 347 (2006); *Phys. Rev. Lett.* **97**, 216803 (2006).
11.M. Y. Han, B. Ozyilmaz, Y. Zhang and P. Kim, *Phys. Rev. Lett.* **98**, 206805 (2007).