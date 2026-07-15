# Thermal conductivity in PbTe from first principles
A. H. Romero, $^{1,2}$ E. K. U. Gross, $^{2}$ M. J. Verstraete, $^{3}$ and Olle Hellman $^{4,5}$

$^{1}$ Department of Physics, West Virginia University, 207 White Hall, 26506, West Virginia, USA
$^{2}$ Max-Planck-Institute für Mikrostrukturphysik, Weinberg 2, D-06120 Halle, Germany
$^{3}$ Department of Physics and European Theoretical Spectroscopy Facility, Université de Liège, av du 6 août, 17, B-4000 Liège, Belgium
$^{4}$ Department of Applied Physics and Materials Science, California Institute of Technology, Pasadena, California 91125, USA
$^{5}$ Department of Physics, Chemistry and Biology (IFM), Linköping University, SE-581 83, Linköping, Sweden

(Received 20 April 2015; published 29 June 2015)

We investigate the harmonic and anharmonic contributions to the phonon spectrum of lead telluride and perform a complete characterization of how thermal properties of PbTe evolve as temperature increases. We analyze the thermal resistivity's variation with temperature and clarify misconceptions about existing experimental literature. The resistivity initially increases sublinearly because of phase space effects and ultra strong anharmonic renormalizations of specific bands. This effect is the strongest factor in the favorable thermoelectric properties of PbTe, and it explains its limitations at higher $T$. This quantitative prediction opens the prospect of phonon phase space engineering to tailor the lifetimes of crucial heat carrying phonons by considering different structure or nanostructure geometries. We analyze the available scattering volume between TO and LA phonons as a function of temperature and correlate its changes to features in the thermal conductivity.

DOI: 10.1103/PhysRevB.91.214310
PACS number(s): 31.15.E-, 61.48.-c, 71.20.Tx, 78.30.Na

Heat conversion by using thermoelectric power generation has received a huge amount of interest in the last few years: transforming a temperature gradient to a voltage difference promises to recover waste heat in thermal engines, transforming it into electrical energy. The thermoelectric efficiency of a material is captured by the figure of merit, $ZT = TS^2\sigma/\kappa$, where $T$ is the temperature, $S$ is the Seebeck coefficient, and $\sigma$ and $\kappa$ are the electrical and thermal conductivities. The search for good thermoelectrics is centered on finding materials with a high figure of merit, which implies large electric and small thermal conductivities. Since the 1990s, a sequence of new materials which offer new paradigms in this field and a large number of energy harvesting applications have been proposed [1-4].

Lead telluride is an industrial standard and a reference high performance thermoelectric, considered to be one of the materials to beat with alternative paradigms such as nanostructuring or nanoalloying. The properties of PbTe in its halite structure have been well documented, and it has been the basis of a large set of investigations, both in its pristine and alloyed configurations. The value of $ZT$ for the crystalline phase of PbTe is close to 1.4 [5]. Recent investigations have reported values above 1.5 which can be obtained by $n$ or $p$ doping, and the possibility of band gap engineering has been recently explored [2,5]. This value can be further increased by alloying or nanostructuring. For example, Hsu *et al.* recently reported a large figure of merit, close to 2.2 at 800 K, for nanostructured PbTe [6]. Alloying and nanostructuring minimizes the lattice thermal conductivity, and one must try to keep the electrical conductivity unaffected. A different approach to increasing the figure of merit is to enhance the electrical conductivity and $S$ by engineering the electronic band structure [7-9]. The use of PbTe as a starting material is the common factor in a long series of such improvements of $ZT$.

In order to understand the behavior of composite nanostructured or alloyed materials based on PbTe, it is important to be able to explain the thermoelectric properties of pristine PbTe, and, in particular, its low thermal conductivity between 450 and 800 K, which is the basis for its high efficiency at ambient conditions and makes it such a good starting point for nanostructuring and doping. For the crystalline system, the low thermal conductivity has been correlated to the presence of large anharmonic effects at the $\Gamma$ point and zone boundary, a large change in the Gruneissen parameters (in particular of a soft TO mode) and a very low speed of sound [5,10-17]. The electronic structure is intimately linked to the resonant bonding and vibrational properties, as shown by Lee *et al.* [18]. It is also important to note that recent champion thermoelectric materials, such as SnSe, are related to PbTe, and it is expected that they share the same strong anharmonicity [13]. An understanding of the anharmonic effects in PbTe will clarify many of the issues raised in other similar thermoelectrics.

In the following we spotlight the fundamental reason for which PbTe has a large thermal resistivity, how its anharmonicity goes beyond the second order response in the interatomic force constants, and how the optical-acoustic branch crossing is removed with increasing temperature. The importance of full anharmonicities, to be able to describe neutron scattering data up to room temperature, has been underscored by Li *et al.* [13] using the same methods. Additionally Lee *et al.* [18] have pointed out that resonant bonding creates an anisotropy in the interatomic force constants, in particular along the (100) direction, which corresponds to the TO mode and is responsible for a large part of the anharmonicity. They have also correlated the phonon lifetimes with the available volume for three phonon scattering. We also observe these effects, now with infinite order anharmonic renormalization of frequencies (essential for PbTe), and we quantify the available phonon scattering volume.

We demonstrate here the strong dependence of the thermal resistivity with respect to volume, which converts to a dependence with respect to thermal expansion. For this quantity we also clarify differences with previously reported results, where good comparison was claimed, but with the wrong experimental data. Additionally, we also observe strong differences in the Grüneisen parameters obtained from the quasiharmonic approximation compared with fully anharmonic methods. This

is a difference that has been previously discussed in the references above: We show here that a fair comparison of these two methodologies, under the same conditions, exposes the pathologies of the full QHA self energy (its use is often restricted to the imaginary part).

There have been numerous theoretical studies on the lattice dynamics of PbTe. Recent papers have focused on demonstrating the sensitivity of the optical phonons to changes in volume [12] and temperature [13,14,19,20]. Experimentally, the phonon spectrum shows a strong dependence on temperature. The coupling between the acoustic and transverse optical modes is identified to strongly correlate with the thermal conductivity [19,20]. A clear theoretical explanation of the anomalous stiffening of the LO mode with increasing temperature was only given last year by Li et al. [13]. At the same time, there is a very strong anharmonicity between the ferroelectric transverse mode and the longitudinal acoustic mode, which was studied in part by Li et al. in a followup paper [21].

The anharmonic influence issue had already been raised, in particular in Refs. [10,12], and the large difference between predicted quasiharmonic approximation (QHA) results and experimental values was pointed out. Delaire et al. concluded that the anharmonicity comes mostly from higher order terms in the interatomic force constants, which affect the longitudinal acoustic phonons and the heat they carry. One of the most important features reported in PbTe in its B1 phase is the anharmonic behavior of the LA-TO coupling along the $\Gamma$-$X$ direction, and in particular the crossing occurring around 1/3 along that path. In Ref. [10] and then in Ref. [13], inelastic neutron scattering data has been reported, where the temperature effects are demonstrated to strongly affect the zone boundary by hardening the TO modes, such that the crossing between LA and TO is lifted as a function of temperature. In these same references the quasiharmonic then fully anharmonic band structures demonstrated the importance of the latter. Below we also use the TDEP method to analyze in detail the pathologies of the quasiharmonic approximation, the higher temperature phonons, and in particular the dramatic effect the renormalization has on the thermal resistivity. It is important to note that the method used to describe the anharmonic thermal behavior in this paper goes beyond the first few terms in the expansion of the interatomic force constants, and that it captures the complete anharmonic behavior to all orders.

At zero temperature, it is common practice to describe the system with a model Hamiltonian as a Taylor expansion of the full ion-electron system as a function of the ionic displacements:

$$
\begin{aligned}
H= & \sum_{i} \frac{\mathbf{p}_{i}^{2}}{2 m_{i}}+\frac{1}{2} \sum_{i j} \sum_{\alpha \beta} \Phi_{i j}^{\alpha \beta} u_{i}^{\alpha} u_{j}^{\beta} \\
& +\frac{1}{3!} \sum_{i j k} \Phi_{i j k}^{\alpha \beta \gamma} u_{i}^{\alpha} u_{j}^{\beta} u_{k}^{\gamma}+\frac{1}{4!} \sum_{i j k l} \Phi_{i j k l}^{\alpha \beta \gamma \delta} u_{i}^{\alpha} u_{j}^{\beta} u_{k}^{\gamma} u_{l}^{\delta}. \quad(1)
\end{aligned}
$$

Here $\mathbf{p}$ indicates momentum and $\mathbf{u}_{i}$ the displacement of atom $i$. The indices $i j k l$ run over all atoms, and $\alpha \beta \gamma \delta$ over Cartesian components. The tensors $\Phi$ are the interatomic force constants of increasing order. From the second order expansion, the frequencies $\omega_{\mathbf{q} s}$ are obtained as a function of mode $s$ and wave vector $\mathbf{q}$. Through perturbation theory [22], one can include the phonon self energy $\Delta_{\mathbf{q} s}+i \Gamma_{\mathbf{q} s}$ where:

$$
\begin{aligned}
\Delta_{\mathbf{q} s}(\Omega)= & -\frac{18}{\hbar^{2}} \sum_{s^{\prime} s^{\prime \prime}} \iint_{\mathrm{BZ}} d \mathbf{q}^{\prime} d \mathbf{q}^{\prime \prime}\left|\Psi_{s s^{\prime} s^{\prime \prime}}^{\mathbf{q} \mathbf{q}^{\prime} \mathbf{q}^{\prime \prime}}\right|^{2} \\
& \times\left(\frac{n_{\mathbf{q}^{\prime} s^{\prime}}+n_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}+1}{\omega_{\mathbf{q}^{\prime} s^{\prime}}+\omega_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}+\Omega}+\frac{n_{\mathbf{q}^{\prime} s^{\prime}}+n_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}+1}{\omega_{\mathbf{q}^{\prime} s^{\prime}}+\omega_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}-\Omega}\right. \\
& \left.+\frac{n_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}-n_{\mathbf{q}^{\prime} s^{\prime}}}{\omega_{\mathbf{q}^{\prime} s^{\prime}}-\omega_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}+\Omega}+\frac{n_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}-n_{\mathbf{q}^{\prime} s^{\prime}}}{\omega_{\mathbf{q}^{\prime} s^{\prime}}-\omega_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}-\Omega}\right) \\
& +\frac{12}{\hbar} \sum_{s^{\prime}} \int_{\mathrm{BZ}} d \mathbf{q}^{\prime} \Psi_{s s s^{\prime} s^{\prime}}^{\mathbf{q} \overline{\mathbf{q}} \mathbf{q}^{\prime} \overline{\mathbf{q}}^{\prime}}\left(2 n_{\mathbf{q}^{\prime} s^{\prime}}+1\right) \\
\Gamma_{\mathbf{q} s}(\Omega)= & \sum_{s^{\prime} s^{\prime \prime}} \frac{\hbar \pi}{16} \iint_{\mathrm{BZ}} d \mathbf{q}^{\prime} d \mathbf{q}^{\prime \prime}\left|\Psi_{s s^{\prime} s^{\prime \prime}}^{\mathbf{q} \mathbf{q}^{\prime} \mathbf{q}^{\prime \prime}}\right|^{2} \\
& \times\left[\left(n_{\mathbf{q}^{\prime} s^{\prime}}+n_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}+1\right) \delta\left(\Omega-\omega_{\mathbf{q}^{\prime} s^{\prime}}-\omega_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}\right)\right. \\
& \left.+2\left(n_{\mathbf{q}^{\prime} s^{\prime}}-n_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}\right) \delta\left(\Omega-\omega_{\mathbf{q}^{\prime} s^{\prime}}+\omega_{\mathbf{q}^{\prime \prime} s^{\prime \prime}}\right)\right], \quad(3)
\end{aligned}
$$

![](./images/814616861244129281_1.jpg)

FIG. 1. (Color online) Phonon dispersion relation and Mode Grünesien parameters for $T=0$ K for a chosen path within the Brillouin zone.

![](./images/814616861244129281_2.jpg)

FIG. 2. (Color online) The energy of the TO(Γ) mode as a function of temperature. The harmonic line has no temperature dependence at all, the quasiharmonic has temperature dependence through the volume, the quasiharmonic+Δ is with the anharmonic shifts, which increases the disagreement. The experimental points are from Refs. [10] (circles) and [23] (triangles).

which depends on the interatomic force constants to third and fourth order ($\Psi_{ss's''}^{qq'q''}$ and $\Psi_{ss's''s'''}^{qq'q''q'''}$) and describe the lifetime broadening and shifts of the phonon frequencies.

In Fig. 1 we show the phonon dispersion relations and mode Grüneisen parameters at 0 K for PbTe. The calculated Grüneisen parameters in PbTe are all positive except for the TA modes. When the temperature is increased, and the crystal expands, the optical modes should all soften in the quasiharmonic approximation, as reported in An et al. [12]. In Fig. 2 we show the energy of the TO modes at Γ as a function of temperature. In the harmonic approximation, they are naturally constant. In the quasiharmonic approximation, where $\Phi(T) = \Phi(V(T))$ and $V(T)$ is the volume as a function of temperature, the TO(Γ) mode softens rapidly, as indicated by the Grünesien parameters. If we add the anharmonic frequency shift, $\Delta_{qs}(\omega_{qs})$, the mode becomes unstable around 650 K. This is all contrary to experimental trends: the TO(Γ) mode should stiffen with temperature, not soften. At the Γ point several frequencies are seen in the neutron experiments, each corresponding to a peak in the scattering intensity. This is not reproduced at all in the QHA.

In case it was necessary, it is obvious by now that conventional quasiharmonic theory can not adequately describe PbTe at elevated temperature. Including the $T=0$ interatomic force constants up to fourth order does not help and even worsens the agreement, as seen in Fig. 2. The observed potential energy well for an atom in the crystal is "hardened out" as temperature increases, because it is now an average over the potential energy created by the fluctuating atoms close by, as is represented in Fig. 3. This behavior is not taken into account by the QHA, which leads to its failure, and is probably not accurately described using few anharmonic terms in the energy expansion. A clear difference can be observed in Fig. 4. While QHA predicts a fast growth of this factor with temperature, as can be observed for most of the $X$ and $\Gamma$ modes, this enhancement does not reproduce the observed experimental phonon hardening, and the TO mode evolution is qualitatively wrong. Our anharmonic calculations predict a slow decay of the Grünesien intensities as temperature increases, reproducing the saturation of all modes, in particular the TO in Fig. 2.

![](./images/814616861244129281_3.jpg)

FIG. 3. (Color online) Cartoon of the potential felt by a given atom using the two different approaches to describe the materials thermal behavior. Left: QHA—the potential at a given volume is fixed for all $T$. Right: TDEP—the ions see a different average potential energy surface depending on the temperature and the present anharmonicity.

As discussed, when the system is strongly anharmonic, a model Hamiltonian, at $T=0$, obtained up to second order is not sufficient, and the Born-Oppenheimer energy surface has a nontrivial temperature dependence. To incorporate this in a lattice dynamical model, we seek explicitly temperature-dependent force constants. We have performed extensive ab initio molecular dynamics (AIMD) to sample the potential energy surface. Using the temperature-dependent effective potential technique (TDEP), we extract the temperature-dependent interatomic force constants [24–26]. Since AIMD incorporates phonon-phonon and electron-phonon coupling implicitly to all orders, the effective force constants will contain that information. They represent the best possible fit of the potential energy surface, for the current volume and temperature, using a finite order of force constants.

We employ Born-Oppenheimer molecular dynamics in density functional theory (DFT) with the projector-augmented wave (PAW) method as implemented in the VASP code [27–30]. To converge the force constants fully, a $5\times5\times5$ supercell (250 atoms) is employed. For the BZ integration we use the $\Gamma$ point and run the simulations in the canonical ensemble, for a grid of temperatures and volumes. Temperature was controlled using a Nosé thermostat [31]. Exchange-correlation effects were treated using the AM05 functional [32,33], and we use a plane wave cutoff of 250 eV. The simulations run for about 30 ps after equilibration with a time step of 1 fs, ensuring proper ergodicity. A subset of uncorrelated samples was then chosen, and for each of the samples the electronic structure and total

![](./images/814616861244129281_4.jpg)

FIG. 4. (Color online) Mode Grünesien parameters as a function of temperature in the TDEP and quasiharmonic (QH) formalisms. The trends with increasing temperature are opposite, with the TDEP being the physically reasonable ones.

energies are recalculated using a $3 \times 3 \times 3$ $k$-point grid and a cutoff of 300 eV to obtain more accurate forces.

Recent experimental results [10,13] provide inelastic neutron scattering spectra for PbTe as a function of temperature. In Ref. [13] Li et al. also show TDEP calculations at 50 K and room temperature, which are fully compatible with our calculations at 300 K. Observe that in our figure we have used a different path along the Brillouin zone, to illustrate more clearly how the anharmonicity affects the LA/TO crossing. To compare with these experiments we convolve our data with the inelastic neutron scattering cross section [34]:

$$
\sigma_{\mathbf{q} s}(\Omega) \propto \frac{2 \omega_{\mathbf{q} s} \Gamma_{\mathbf{q} s}(\Omega)}{\left(\Omega^{2}-\omega_{\mathbf{q} s}^{2}-2 \omega_{\mathbf{q} s} \Delta_{\mathbf{q} s}(\Omega)\right)^{2}+4 \omega_{\mathbf{q} s}^{2} \Gamma_{\mathbf{q} s}^{2}(\Omega)}. \quad(4)
$$

Figure 5 shows the theoretical and experimental inelastic neutron scattering cross section. The Debye-Waller factor and the experimental transfer functions have been disregarded. For the calculations of the self energy, a $31 \times 31 \times 31$ $q$-point grid and a Gaussian smearing of 0.1 meV have been used for the numerical evaluation of $\Gamma$ and $\Delta$. The calculated and experimental spectra show remarkable agreement in absolute and relative shifts of the phonon frequencies. The TDEP accurately describes the double peak structure of the TO mode at $\Gamma$, as shown by Li et al. [13] at 300 K. Traces of this double peak remain at 600 K, which also agrees with the experimental picture. The energies of the two peaks as a function of temperature are shown with squares in Fig. 2, and they agree well with the experimental values.

A crossing of the experimental acoustic and optical branches in the $\Gamma$-$X$ direction is present at 300 K and disappears by 600 K. This is also reproduced by our calculations, and is central to the good thermal performance of PbTe, as will be shown below. For higher temperatures PbTe loses this topological advantage when the crossing is lifted. The quasiharmonic results do not reproduce any of these features, and at 600 K the self energy shifts have rendered the system completely unstable. Previous perturbation theoretical studies avoid this problem by disregarding either thermal expansion or $\Delta$ [19]. From the quantitative agreement with experimental data, we conclude that we have built an accurate lattice dynamical model for PbTe at finite temperature with a good description of thermal properties and temperature dependencies. We now apply it to the calculation of the lattice thermal resistivity $\rho$.

Experimental data for the thermal resistivity of PbTe has been measured in Refs. [35] and [36] at low and high temperature, respectively. In the literature, Ref. [37] is often referred to for the bulk lattice thermal conductivity of PbTe. This is not correct: The paper does not contain any values of lattice thermal conductivity. The data attributed to Ref. [37] is actually that contained in Ref. [35]. More importantly, close inspection of Ref. [35] shows that what is usually reported for the lattice thermal conductivity at high T is not a measurement but a linear extrapolation from values obtained between 50 and 280 K. The good agreement with experimental $\rho$ at high T in Refs. [19,20] is thus probably the result of the analytically linear behavior of $\rho$ in perturbation theory and the inappropriate

![](./images/814616861244129281_5.jpg)

FIG. 5. (Color online) PbTe Neutron scattering cross section. Notice the double peaks close to $\Gamma$ and the lifting of the optical branches above the acoustic captured within the TDEP method as compared to experiment. The quasiharmonic are included only for the reference.

linear extrapolation in Ref. [35]. The data of El Sharkawy [36] demonstrate the highly nonlinear behavior of $\rho(T)$.

We calculate the resistivity from the phonon Boltzmann equation for fixed volume, beyond the relaxation time approximation and including isotope scattering as described in Ref. [38]. The results are summarized in Fig. 7, using the TDEP and quasiharmonic treatments, together with experimental results and considering different volumes for the theoretical calculations.

As temperature increases, the thermal resistivity increases slower than linearly. This is strongly correlated with the position of the TO mode with respect to the acoustic branches: The nested scattering between the LA and TO branches was already pointed out by Ref. [19]. When the TO mode is lifted up with increasing temperature, the available scattering volume shrinks dramatically, and the acoustic phonons are allowed to carry heat unperturbed, and the resistivity is sublinear with T. This process is illustrated in Fig. 6, where at low temperature there are scattering channels available between the TO and LA. When the TO mode stiffens with temperature, these channels no longer satisfy momentum and energy conservation and the lifetimes of acoustic phonons increase.

At 100 K both methods start in decent agreement with experiment. As $T$ increases, however, the QHA results increase much faster, and the thermal expansion effect pushes the results away from the experimental curves. TDEP values are more reasonable and are smaller than experiment: additional possible scattering mechanisms (defects, grain boundaries) must add to the resistivity. In particular the sublinear behavior observed up to 600 K is reproduced correctly. At higher temperatures the expected linear behavior is restored, due to the high $T$ linear limit of the Bose Einstein distribution for each given frequency.

Additionally, 0 K perturbation theory becomes questionable in the case of PbTe: For a few modes, the linewidth and frequency can be comparable and $\Gamma_{\mathbf{q} s} \ll \omega_{\mathbf{q} s}$ definitely does not hold. What our results show is that the TDEP renormalized quantities do obey the relation $\Gamma_{\mathbf{q} s}(T) \ll \omega_{\mathbf{q} s}(T)$. Finally, the large Grüneisen parameters imply a strong volume dependence. In Fig. 7 we show the thermal resistivity for lattice parameters compressed and expanded by 1%, which leads to a factor 2 difference in resistivity. The intrinsic exchange-correlation error in current DFT functionals is certainly of this order of magnitude for the volume, and more accurate calculations will necessitate further improvements in the fundamentals of DFT.

Our results clearly demonstrate that a careful examination of the phonon response is crucial when dealing with systems as strongly anharmonic as PbTe. The TDEP method contains the anharmonic terms necessary to describe phonon frequencies at high $T$. We have noted that the crossing present in the phonon dispersion relation is lifted by the temperature renormalization

![](./images/814616861244129281_6.jpg)

FIG. 6. (Color online) The energy and momentum conserving surfaces for scattering between the TO mode and LA and TA phonons. As temperature increases and the TO mode stiffens, the available scattering volume for this channel of decay disappears, which is the origin of the kink in thermal resistivity. The isosurface represents the nesting factor for scattering between bands 2, 3, and 4, while conserving energy and momentum, integrated over $q'$ and $q''$.

of the interatomic force constants, with no need for additional perturbation theory. Quantitative prediction of the exception- ally low thermal resistivity is possible but still very challenging in this delicate system, where large anharmonicities determine the physical behavior. An important effect is also observed in the changes in the electronic structure as a function of temperature, Fig. 8, where we have taken the average of the electron band structure for 20 uncorrelated configurations. It is clear that, as the temperature changes, the electron potential surface also changes, and electron bands both shift and broaden. This can have a double effect, in bringing the valence band valleys closer to degeneracy (see maxima between $\Gamma$ and $X$ or $K$, and at $L$), which will affect the electronic part of $ZT$.

Many successful but heuristic attempts have been made to further reduce the low thermal conductivity of PbTe (by doping, alloying, and nanostructuring). We show here that a direct rational approach, based on first principles calculations, can now be taken. Exploiting the volume (and hence stress) dependence of the phonon frequencies, the phonon resistivity will be maximized by preserving the optical-acoustic cross- ings. The opposite effect—very different masses lead to a large phonon gap and impeded phonon scattering—was shown by Broido and co-workers, in BAs [39] among other compounds, and with anomalous pressure effects [40]. Many other high performance thermoelectrics present low-lying optical modes and could be manipulated in similar ways: using epitaxy to start from a lower lattice constant at ambient or uniaxial stress to create a preferred direction for the heat flow, as could certainly be done with SnSe [41,42], which is the bulk material with the highest reported figure of merit.

It is common to consider phonon band engineering, invoked in many nanostructuring or nanoalloying strategies, to reduce the speed of sound and break the group velocity of acoustic modes, e.g., using disorder or rattlers. Much less is quantified about the reduction of phonon lifetimes by manipulating the available phase space for decay, as we have demonstrated

![](./images/814616861244129281_7.jpg)

FIG. 7. (Color online) Thermal resistivity of PbTe versus temper- ature. The red lines are QHA results with $T=0$ force constants and volumes corresponding to the experimental thermal expansion. The green lines are calculated using temperature-dependent force con- stants, with volumes following the experimental thermal expansion.

![](./images/814616861244129281_8.jpg)

FIG. 8. (Color online) Electronic band structure average over a molecular dynamics trajectory.

happens in PbTe, confirming the work of Shiga *et al.* [19]. The presence of anharmonicity is intimately linked to the mass of the atoms and overall softness of the phonon modes, which are important features of most successful thermoelectrics.

Summarizing, we describe the relevance of high orders of the interatomic force constants in the proper description of the thermoelectric properties of PbTe. This result should guide future work on alloy-based thermoelectrics as well as other high temperature applications. The dependence should also affect similar compounds, where strong anharmonicities have been reported, and can not be accounted for by normal perturbation theories.

A.H.R. acknowledges the support of the Marie Curie Actions from the European Union in the international in- coming fellowships (Grant No. PIIFR-GA-2011-911070) and the Donors of the American Chemical Society Petroleum Research Fund for partial support of this research under contract 54075-ND10. This material is also based upon work supported by the National Science Foundation under Grant No. 1434897. M.J.V. acknowledges an Action de Recherches Concertées (ARC) grant (TheMoTherm # 10/15-03) from the Communauté Française de Belgique, and computer time from CECI, SEGI, and PRACE-2IP and 3IP (EU FP7 Grant Nos. RI-283493 and RI-312763) on Huygens, Hector, and Archer. Support from the Swedish Research Council (VR) program 637-2013-7296 is gratefully acknowledged. Supercomputer resources were provided by the Swedish National Infrastruc- ture for Computing (SNIC).

[1] M. Zebarjadi, K. Esfarjani, M. S. Dresselhaus, Z. Ren, and G. Chen, *Energy Environ. Sci.* **5**, 5147 (2012).

[2] A. D. LaLonde, Y. Pei, H. Wang, and G. Jeffrey Snyder, *Mater. Today* **14**, 526 (2011).

[3] A. J. Minnich, M. S. Dresselhaus, Z. F. Ren, and G. Chen, *Energy Environ. Sci.* **2**, 466 (2009).

[4] M. S. Dresselhaus, G. Chen, Z. Ren, G. Dresselhaus, A. Henry, and J. P. Fleurial, *JOM* **61**, 86 (2009).

[5] A. D. LaLonde, Y. Pei, and G. J. Snyder, *Energy Environ. Sci.* **4**, 2090 (2011).

[6] K. F. Hsu, S. Loo, F. Guo, W. Chen, J. S. Dyck, C. Uher, T. Hogan, E. K. Polychroniadis, and M. G. Kanatzidis, *Science* (New York, NY) **303**, 818 (2004).

[7] C. M. Jaworski, M. D. Nielsen, H. Wang, S. N. Girard, W. Cai, W. D. Porter, M. G. Kanatzidis, and J. P. Heremans, *Phys. Rev. B* **87**, 045203 (2013).

[8] Y. Pei, H. Wang, and G. J. Snyder, *Advanced materials* (Deerfield Beach, FL) **24**, 6125 (2012).

[9] Q. Zhang, F. Cao, W. Liu, K. Lukas, B. Yu, S. Chen, C. Opeil, D. A. Broido, G. Chen, and Z. Ren, *J. Am. Chem. Soc.* **134**, 10031 (2012).

[10] O. Delaire, J. Ma, K. Marty, A. May, M. McGuire, M.-H. Du, D. Singh, A. Podlesnyak, G. Ehlers, M. Lumsden, and B. Sales, *Nat. Mater.* **10**, 614 (2011).

[11] D. J. Singh, *Sci. Adv. Mater.* **3**, 561 (2011).

[12] J. An, A. Subedi, and D. J. Singh, *Solid State Commun.* **148**, 417 (2008).

[13] C. W. Li, O. Hellman, J. Ma, A. F. May, H. B. Cao, X. Chen, A. D. Christianson, G. Ehlers, D. J. Singh, B. C. Sales, and O. Delaire, *Phys. Rev. Lett.* **112**, 175501 (2014).

[14] C.-L. Chen, H. Wang, Y.-Y. Chen, T. Day, and G. J. Snyder, *J. Mater. Chem.* **A** **2**, 11171 (2014).

[15] J. Al-Otaibi and G. P. Srivastava, *J. Appl. Phys.* **116**, 043702 (2014).

[16] T. Shiga, T. Murakami, T. Hori, O. Delaire, and J. Shiomi, *Appl. Phys. Express* **7**, 041801 (2014).

[17] Y. Chen, X. Ai, and C.A. Marianetti, *Phys. Rev. Lett.* **113**, 105501 (2014).

[18] S. Lee, K. Esfarjani, T. Luo, J. Zhou, Z. Tian, and G. Chen, *Nat. Commun.* **5**, 3525 (2014).

[19] T. Shiga, J. Shiomi, J. Ma, O. Delaire, T. Radzynski, A. Lusakowski, K. Esfarjani, *Phys. Rev. B* **85**, 155203 (2012).

[20] Z. Tian, J. Garg, K. Esfarjani, T. Shiga, J. Shiomi, and G. Chen, *Phys. Rev. B* **85**, 184303 (2012).

[21] C. W. Li, J. Ma, H. B. Cao, A. F. May, D. L. Abernathy, G. Ehlers, C. Hoffmann, X. Wang, T. Hong, A. Huq, O. Gourdon, and O. Delaire, *Phys. Rev. B* **90**, 214303 (2014).

[22] D. C. Wallace, *Thermodynamics of Crystals*, Dover Books on Physics (Dover Publications Inc., Mineola, NY, 1998).

[23] W. Cochran, R. A. Cowley, G. Dolling, and M. M. Elcombe, *Proc. R. Soc. London, Ser. A* **293**, 433 (1966).

[24] O. Hellman, I. A. Abrikosov, and S. I. Simak, *Phys. Rev. B* **84**, 180301 (2011).

[25] O. Hellman, P. Stenereg, I. A. Abrikosov, and S. I. Simak, *Phys. Rev. B* **87**, 104111 (2013).

[26] O. Hellman and I. A. Abrikosov, *Phys. Rev. B* **88**, 144301 (2013).

[27] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[28] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

[29] G. Kresse and J. Hafner, *Phys. Rev. B* **48**, 13115 (1993).

[30] G. Kresse, *Comput. Mater. Sci.* **6**, 15 (1996).

[31] S. Nosé, *Mol. Phys.* **52**, 255 (1984).

[32] R. Armiento and A. E. Mattsson, *Phys. Rev. B* **72**, 085108 (2005).

[33] A. E. Mattsson and R. Armiento, *Phys. Rev. B* **79**, 155101 (2009).

[34] R. A. Cowley, *Rep. Prog. Phys.* **31**, 123 (1968).

[35] E. D. Devyatkova and I. A. Smirnov, *Sov. Phys. Solid State,* USSR **4**, 2507 (1962).

[36] A. A. El-Sharkawy, A. M. Abou El-Azm, M. I. Kenawy, A. S. Hillal, and H. M. Abu-Basha, *Int. J. Thermophys.* **4**, 261 (1983).

[37] V. I. Fedorov and V. I. Machuev, *Sov. Phys. Solid State,* USSR **11**, 1116 (1969).

[38] D. A. Broido, M. Malorny, G. Birner, N. Mingo, and D. A. Stewart, *Appl. Phys. Lett.* **91**, 231922 (2007).

[39] D. A. Broido, L. Lindsay, and T. L. Reinecke, *Phys. Rev. B* **88**, 214303 (2013).

[40] L. Lindsay, D. A. Broido, J. Carrete, N. Mingo, and T. L. Reinecke, *Phys. Rev. B* **91**, 121202 (2015).

[41] L.-D. Zhao, S.-H. Lo, Y. Zhang, H. Sun, G. Tan, C. Uher, C. Wolverton, V. P. Dravid, and M. G. Kanatzidis, *Nature* (London) **508**, 373 (2014).

[42] J. Carrete, N. Mingo, and S. Curtarolo, *Appl. Phys. Lett.* **105**, 101907 (2014).