# Prediction of Magnetic State of $\text{UO}_2$ within Hubbard-corrected Density-Functional Theory: A self-consistent approach

Mahmoud Payami*
School of Physics & Accelerators,
Nuclear Science and Technology Research Institute,
AEOI, P. O. Box 14395-836, Tehran, Iran

The magnetic state of $\text{UO}_2$ was determined experimentally to be anti-ferromagnetic. Starting from this experimental fact, researchers have calculated other properties within the Hubbard-corrected density-functional theory, DFT+U. Up to now, the Hubbard parameters for $\text{UO}_2$ were usually so chosen that the calculations give good results for some experimental data. Also, to our knowledge there exists no valid theoretical research report on the energetically stable magnetic state of this system. In present work, employing the new method which is based on density-functional perturbation theory, we have determined self-consistently the Hubbard parameters and ground-state energies for $\text{UO}_2$ crystal in both ferromagnetic and anti-ferromagnetic configurations, and the calculated results show that $\text{UO}_2$ crystal energetically favors an anti-ferromagnetic state with a small energy difference. In all the calculations the PBE-sol approximation was used for the exchange-correlation energy functional.

Keywords: Uranium dioxide; Ferromagnetism; Anti-ferromagnetism; Density-Functional Theory; Hubbard Model; Mott Insulator; DFT+U.

## I. INTRODUCTION

The popular local-density approximation (LDA) [1, 2] and generalized gradient approximation (GGA) [3] approximations for the exchange-correlation (XC) energy functional in the density-functional theory (DFT) [1, 4] suffer from self-interaction errors, which are significant in systems containing atoms with localized $d$ and $f$ orbitals, and by over-delocalization of their corresponding wave-functions lead to incorrect prediction of metallic behavior for Mott insulators. A simple and low-cost workaround is using the Hubbard-corrected DFT model to correct the correlation energy of localized orbitals in DFT energy-functional, DFT+U, in which only on-site corrections are added to the DFT energy functional [5]:

$$
E_{\text{DFT+U}} = E_{\text{DFT}}[n(\mathbf{r})] + E_{\text{Hub}}[n_{m}^{I\sigma}] - E_{\text{dc}}[n^{I\sigma}], \quad (1)
$$

where $n(\mathbf{r})$ is electron density, $n_{m}^{I\sigma}$ are orbital occupation numbers of atom at lattice site $\mathbf{R}_I$, and $n^{I\sigma} = \sum_m n_{m}^{I\sigma}$. The last term in right hand side of Eq. (1) is needed to avoid double counting of interactions contained in the first and second terms. The rotationally invariant form [6] of the correction is given by [5]:

$$
E_{\text{U}}[n_{mm'}^{I\sigma}] \equiv E_{\text{Hub}}{-E_{\text{dc}}} = \sum_{I,\sigma} \frac{U^I}{2} \text{Tr}[\mathbf{n}^{I\sigma}(\mathbf{1} - \mathbf{n}^{I\sigma})], \ (2)
$$

in which $\mathbf{n}^{I\sigma}$ is the atomic occupation matrix. This on-site correction, significantly improves the over-delocalization and lead to correct insulating properties.

The coefficients $U^I$ are called Hubbard on-site parameters, and for a known material, these $U^I$ values may be so adjusted that the calculations results well agrees with some experimental data [7]. However, in the case of designing new materials there is no experimental data to be used for parameters fitting and on the other hand, it is very important for the theory describing a material to be a parameter-free one. The first attempts in this way was using linear-response constrained-DFT (LR-cDFT) within super-cell method [5, 8] which was somewhat inconvenient and computationally demanding. Another scheme to estimate the parameters was named as constrained random-phase approximation (cRPA) [9] which was recently used by others [10] to estimate the U parameter for uranium dioxide. However, a new method based on density-functional perturbation theory (DFPT) was recently introduced which instead of using previous super-cells, focuses on the unit-cell, which is more convenient and relatively fast [11–13]. Using this new method, we have determined self-consistently the Hubbard parameters for $\text{UO}_2$ crystal in both ferromagnetic (FM) and anti-ferromagnetic (AFM) configurations of uranium atoms and showed that energetically $\text{UO}_2$ crystal favors an AFM magnetic state with a small energy difference, which is in agreement with experimental findings. In our recent work [14] we have demonstrated that choosing PBE-sol approximation [15] for the XC functional leads to excellent results from self-consistent DFT+U calculations, and therefore we have employed it in all computations throughout this work.

The organization of this paper is as follows: Section II is dedicated to the computational details; in Section III we present and discuss the calculated results; and finally section IV summarizes and concludes this research.

* mpayami@aeoi.org.ir

![](./images/1229402125872660481_1.jpg)

FIG. 1: $\text{UO}_2$ crystal structure as simple tetragonal with six atoms basis. Left and right figures schematically represent FM and AFM configurations, respectively. Large grey and small red balls represent uranium and oxygen atoms, respectively. The up-spin and down-spin atoms are shown with yellow and green colors, respectively.

## II. COMPUTATIONAL DETAILS

The crystal structure of uranium dioxide is described by a simple tetragonal lattice with a six-atoms basis, shown in Fig. 1. In FM configuration, all spins of U atoms have the same direction along $z$-axis, while to setup AFM structure for U atoms, we use the simple model in which the planes of U atoms alternate their spins along $z$ direction, i.e., we assume a 1-dimensional AFM.

The Hubbard on-site U parameters were calculated self-consistently using the HP code [13] included in the Quantum-ESPRESSO code package [16, 17] for both FM and AFM configurations of U atoms (shown in Fig. 1) in the context of PBE-sol [15] approximation to the XC. The calculations include results for both "atomic" and "ortho-atomic" types of projections onto Hubbard orbitals. The electronic structure calculations are based on the solution of the KS equations using the Quantum-ESPRESSO code package. For U and O atoms the scalar-relativistic ultra-soft pseudo-potentials (USPP) were used which were generated by the *atomic* code and generation inputs from the *pslibrary* [18], at https://github.com/dalcorso/pslibrary. The valence configurations $\text{U}(6s^2, 6p^6, 7s^2, 7p^0, 6d^1, 5f^3)$ and $\text{O}(2s^2, 2p^4)$ were adopted in the USPP generation. Kinetic energy cutoffs for the plane-wave expansions were chosen as 90 and 720 Ry for the wave-functions and densities, respectively. The smearing method of Marzari-Vanderbilt [19] for the occupations with a width of 0.01 Ry were used. For the Brillouin-zone integrations in geometry optimizations, a $8 \times 8 \times 6$ grid were used; All geometries were fully optimized for total residual pressures on unit cells to within 0.5 kbar, and residual forces on atoms to within $10^{-3}$ mRy/a.u. To self-consistent determination of the Hubbard parameters we have employed the HP code [13] following the flowchart shown in Fig. 2.

To start the self-consistent procedure for determining the Hubbard parameters according to Fig. 2, the convergent q-mesh of $4 \times 4 \times 3$ for linear response calculations was adopted and we gave initial values for $U_{in}$ in each of FM and AFM configurations; for the initial structure we chose simple tetragonal structure with appropriate lattice constants consistent with cubic structure of side $5.47\mathring{A}$. To avoid meta-stable states, we determined appropriate occupations of Hubbard orbitals $5f$ of uranium atoms [20, 21]. In this second step, we start the DFPT calculation and obtain new values for parameters named as $U_{out}$. In the third step, using the parameter $U_{out}$ we obtained in the second step, the geometry of the system is optimized taking care of meta-stable states. In each cycle the differences between input and output parameters were monitored to see if the self-consistency is reached within $\Delta$ value. For this system the self-consistency was reached within 6 to 8 cycles in the flowchart with $\Delta < 10^{-4}$.

![](./images/1229402125872660481_2.jpg)

FIG. 2: Flowchart of SCF determination of Hubbard parameters. In the first-step SCF and last-step structure-optimization, the meta-stable states were avoided [20, 21]

## III. RESULTS AND DISCUSSIONS

The calculations were performed at the level of DFT with on-site Hubbard corrections (DFT+U) for both

FM and AFM configurations, and the results showed that both FM and AFM magnetic states are insulators with different values for electronic band gaps. The self-consistent Hubbard parameters and geometric equilibrium lattice constants for FM and AFM states differ slightly; but their respective band gaps show relatively significant differences. The results are summarized in Table I.

As is seen from Table I, the AFM configuration with orthogonalized projections on Hubbard orbitals is the lowest energy state, and therefore the energetically stable state of $\mathrm{UO}_{2}$ is an AFM configuration. To our knowledge, this result is obtained for the first time. The lattice constants differ by $0.02\mathrm{\AA}$ and all are in excellent agreement with experiment. The band gaps for AFM are larger than corresponding values in FM configurations. It is important to note that the self-consistent Hubbard parameters are different for AFM and FM configurations which result from different responses of them to an external perturbation. Therefore, applying the same empirical value for AFM and FM states of a system and comparing the energies to decide the favored state is shown to be incorrect. As is seen, the band gap of AFM with orthogonalized projections gives the best agreement with experiment [22].

To compare the overall electronic states of FM and AFM configurations, we have plotted the electronic total density of states (DOS) and shown in Fig. 3. Inspecting the Fig. 3, one notices that the behaviors near the band edges are different for two magnetic states, and the value of band gap for FM is smaller than that of AFM.

## IV. CONCLUSIONS

In the study of strongly-correlated $\mathrm{UO}_{2}$ system, usually one takes an AFM configuration for the uranium atoms which is borrowed from experimental findings, and the best job afterwards is to calculate the Hubbard parameter U self-consistently, as done by present authors in earlier work. However, it is very much interesting to predict the magnetic state theoretically as well without resorting to experimental facts. This becomes vital in designing new novel materials. In present work, using DFPT, we have calculated self-consistently the Hubbard on-site parameters and thereof the total energies for the two AFM and FM states of $\mathrm{UO}_{2}$ crystal and have shown that the resulting parameters are different and AFM configuration is energetically favored by a small value of $0.01eV/(\text{formula unit})$.

## ACKNOWLEDGEMENT

This work is part of research program in School of Physics and Accelerators, NSTRI, AEOI.

## DATA AVAILABILITY

The raw or processed data required to reproduce these results can be shared with anybody interested upon sending an email to M. Payami.

[1] W. Kohn and L. J. Sham, "Self-consistent equations including exchange and correlation effects", *Phys. Rev.* **140**, A1133 (1965).

[2] J. P. Perdew and A. Zunger, "Self-interaction correction to density-functional approximations for many-electron systems", *Phys. Rev.* B **23**, 5048 (1981).

[3] J. P. Perdew, K. Burke, and M. Ernzerhof, "Generalized gradient approximation made simple", *Phys. Rev. Lett.* **77**, 3865 (1996); Erratum: *Phys. Rev. Lett.* **78**, 1396 (1997).

[4] P. Hohenberg and W. Kohn, "Inhomogeneous electron gas", *Phys. Rev.* **136**, B864 (1964).

[5] M. Cococcioni and S. de Gironcoli, "Linear response approach to the calculation of the effective interaction parameters in the LDA+ U method", *Phys. Rev.* B **71**, 035105 (2005).

[6] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, "Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+ U study", *Phys. Rev.* **B57**, 1505 (1998).

[7] M. Payami, "DFT+U study of UO2: Correct lattice parameter and electronic bandgap", arXiv:2302.13381 [cond-mat.str-el], https://doi.org/10.48550/arXiv.2302.13381.

[8] V. L. Campo Jr and M. Cococcioni, "Extended DFT+ U+ V method with on-site and inter-site electronic interactions", *J. Phys.: Condens. Matt.* **22**, 055602(2010).

[9] F. Aryasetiawan, K. Karlsson, O. Jepsen, and U. Schonberger, "Calculations of Hubbard U from first-principles", *Phys. Rev.* B **74**, 125106 (2006).

[10] S. L. Dudarev, P. Liu, D. A. Andersson, et. al., "Parametrization of LSDA+U for noncollinear magnetic configurations: Multipolar magnetism in UO2", *Phys. Rev. Materials* **3**, 083802 (2019).

[11] I. Timrov, N. Marzari, and M. Cococcioni, "Hubbard parameters from density-functional perturbation theory", *Phys. Rev.* B **98**, 085127 (2018).

TABLE I: Self-consistent Hubbard parameters $U_{sc}$ in eV; total energy with respect to the lowest one corresponding to ortho-atomic AFM, per formula unit $\Delta E$ in eV; total and absolute magnetizations per formula unit in Bohr-magneton; equilibrium lattice constants in $\mathring{A}$; and electronic band-gaps in eV for different cases studied. PBE-sol approximation was used for the XC, which turns out to be the best one.

<table>
  <thead>
    <tr>
      <th rowspan="2">U-proj</th>
      <th colspan="6">AFM</th>
      <th colspan="6">FM</th>
    </tr>
    <tr>
      <th>$U_{sc}$ ($eV$)</th>
      <th>$\Delta E$</th>
      <th>$M_{tot}$</th>
      <th>$M_{abs}$</th>
      <th>$a$ ($c$) ($\mathring{A}$)</th>
      <th>$E_g$ ($eV$)</th>
      <th>$U_{sc}$ ($eV$)</th>
      <th>$\Delta E$</th>
      <th>$M_{tot}$</th>
      <th>$M_{abs}$</th>
      <th>$a$ ($c$) ($\mathring{A}$)</th>
      <th>$E_g$ ($eV$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>o-atomic</td>
      <td>2.9787</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>2.150</td>
      <td>5.4540(5.4631)</td>
      <td>2.2281</td>
      <td>2.9936</td>
      <td>0.0103</td>
      <td>2.00</td>
      <td>2.175</td>
      <td>5.4541(5.4655)</td>
      <td>1.7102</td>
    </tr>
    <tr>
      <td>atomic</td>
      <td>2.0862</td>
      <td>0.0961</td>
      <td>0.00</td>
      <td>2.155</td>
      <td>5.4546(5.4766)</td>
      <td>1.3699</td>
      <td>2.1247</td>
      <td>0.1140</td>
      <td>2.00</td>
      <td>2.190</td>
      <td>5.4582(5.4770)</td>
      <td>0.9162</td>
    </tr>
  </tbody>
</table>

![](./images/1229402125872660481_3.jpg)

FIG. 3: Total electronic density of states (DOS) for AFM and FM configurations of $UO_2$ crystal. It is observed that in a given magnetic state of $UO_2$, the band gap is larger for orthogonalized projections. Moreover, the band gaps of AFM are larger than corresponding values for FM.

[12] I. Timrov, N. Marzari, and M. Cococcioni, "Self-consistent Hubbard parameters from density-functional perturbation theory in the ultrasoft and projector-augmented wave formulations", Phys. Rev. B 103, 045141 (2021).

[13] I. Timrov, N. Marzari, and M. Cococcioni, "HP–A code for the calculation of Hubbard parameters using density-functional perturbation theory", Comput. Phys. Commun. 279, 108455 (2022).

[14] M. Payami, S. Sheykhi, and M. R. Basaadat, "Self-consistent on-site and inter-site Hubbard parameters within DFT+U+V for UO2 using density-functional perturbation theory", arXiv:2306.06266v1 [cond-mat.mtrl-sci], https://doi.org/10.48550/arXiv.2306.06266 (2023).

[15] J. P. Perdew, et. al., "Restoring the density-gradient expansion for exchange in solids and surfaces", Phys. Rev. Lett. 100, 136406 (2008).

[16] P. Giannozzi, S. Baroni, N. Bonini, et. al., J. Phys.: Condensed Matt. 21, 395502 (2009).

[17] P. Giannozzi, O. Baseggio, P. Bonfà, et. al., J. Chem. Phys. 152, 154105 (2020).

[18] A. Dal Corso, "Pseudopotentials periodic table: From H to Pu", Comput. Mater. Sci. 95, 337 (2014).

[19] N. Marzari, et. al., "Thermal contraction and disordering of the Al (110) surface", Phys. Rev. Lett. 82, 3296 (1999).

[20] M. Payami, "Spin-symmetry broken ground-state of UO2 in DFT+U approach: the SMC method", Iranian J. Phys. Res. 22, 175 (2022), https://doi.org/10.47176/ijpr.22.3.81568; also arXiv:2108.12758v2 [cond-mat.mtrl-sci], https://doi.org/10.48550/arXiv.2108.12758 (2021).

[21] M. Payami, "Comparison of SMC and OMC results in determining the ground-state and metastable states solutions for UO2 in DFT+U

method", arXiv:2302.04231v1 [cond-mat.mtrl-sci,
https://doi.org/10.48550/arXiv.2302.04231 (2023).

[22] J. Schoenes, "Optical properties and electronic structure
of UO2", J. Appl. Phys. 49, 1463 (1978).