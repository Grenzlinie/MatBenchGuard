**STRUCTURE OF MATTER
AND QUANTUM CHEMISTRY**

# Empirically Modified Potentials of Interaction
between Rare Gases for Matrix Isolation Problems

D. S. Bezrukov⁽ᵃ,ᵇ,∗⁾, N. N. Kleshchina⁽ᵇ⁾, I. S. Kalinina⁽ᵃ⁾, and A. A. Buchachenko⁽ᵃ,∗∗⁾

⁽ᵃ⁾ Skolkovo Institute of Science and Technology, Moscow, 121205 Russia
⁽ᵇ⁾ Department of Chemistry, Moscow State University, Moscow, 119991 Russia
∗ e-mail: d.bezrukov@skoltech.ru
∗∗ e-mail: a.buchachenko@skoltech.ru

Received November 9, 2018; revised November 9, 2018; accepted December 12, 2018

**Abstract**—Simple ways of modeling the gas-phase potentials of rare gas Ne, Ar, Kr, and Xe dimers are proposed to describe solid matrices and atomic and molecular systems isolated in them. The fitting parameters for Ne, Ar, Kr, and Xe, based on the reproduction of the lattice structural parameter and energy of atomization, were calculated. The resulting effective solid-state potentials of inert gas dimers were applied to the problem of modeling the sodium atom captured by argon matrix. The effect of solid-state modification on the geometries of stable trapping sites and on the shifts and shapes of the calculated electronic absorption spectrum of the Na@Ar system was investigated. It is shown that using the effective solid-state potentials can improve the agreement with experimental values.

**Keywords**: matrix isolation, pair potentials, absorption spectrum

DOI: 10.1134/S003602441908003X

## INTRODUCTION

Matrix isolation allows us to study the properties of atoms, molecules, clusters, and radicals that cannot be measured in the gas phase. Understanding the effect the environment has on the structure and properties of systems isolated in a matrix requires the use of theoretical approaches that correctly describe the matrix structure.

Even the simplest case when one atom is captured by an inert gas matrix (RG) is rather complicated for a theoretical description. First of all, the thermodynamic stability of the capture sites is determined by the balance of the matrix energy (i.e., the interaction between RG atoms) and the energy of interaction between the embedded atom and the surrounding RG atoms. To predict the structure of stable sites, we should consider both contributions correctly. The interaction between two similar RG atoms is usually stronger than with any other atom in the ground state [1]. Secondly, the simplest and most productive experimental approach to studying atoms in inert matrices is electron spectroscopy. The shifts and shapes of the excitation and emission bands of Me@Rg systems are determined by the difference between the many-body interaction energies of the system in ground and excited states. The main part of the interaction energy is associated with the matrix itself, so the spectral properties formally reflect the slight difference between two large quantities.

In a common practice, this problem is avoided by using pairwise potential approximation, i.e., by leaving only two-body contributions in the many-body potential energy expansion. For open-shell atoms in excited states, the diatomics-in-molecule (DIM) method is used as a natural extension of the pairwise potential approximation to the case of anisotropic atom-atom interaction [2]. Such a simple representation of the force field (FF), allows one to recast the potential energy into the sum of guest-host and host-host interactions. The spectroscopic properties of the matrix system are mostly determined by the first term, and more precisely, by its change upon electronic excitation. Nevertheless, the larger second term cannot be excluded from consideration, since it determines the configuration and vibrations of the guest atom.

The quality of modeling the spectra of embedded atoms depends directly on the accuracy of the force fields obtained using pair potentials usually borrowed from measurements or calculations for an isolated (gas-phase) pair of atoms. However, in relation to calculations of the excited state energy [3–5] the DIM model is usually considered the main source of inconsistency between calculations and experiments. To reach a final verdict it is necessary to carry out a more detail analysis of the other sources of error.

This work discusses simple options for correcting errors that arise from an insufficiently accurate matrix description. RG–RG interaction is usually simulated by the pair potentials proposed by Aziz et al. [6–9]. They are reconstructed from thermodynamic and transport data in the gas phase and considered accurate, as is confirmed by precision nonempirical calculations [10–12]. However, it is known that using these potentials for calculations of ideal rare gas crystals results in atomization energy overestimation and underestimation of the lattice parameter. Careful ab initio analysis [13] reveals the two main reasons for such errors: neglecting zero-point energy (especially for Ne) and neglecting three-particle interaction (especially for Xe). Many ways for constructing effective potentials describing ideal RG crystals with face-centered cubic (fcc) packaging have been proposed. Attempts to calculate and describe the contributions from the above effects [14–16] were made based on empirical approximations [17–20]. As far as we know, the role of these effects on matrix isolation was not considered in any these studies. Two ways of modification the initial gas-phase potentials are proposed in this work. They ensure agreement with experimental data on the lattice parameter and atomization energy, effectively considering the effect of many-particle corrections and zero-point energy. The potentials obtained for Ne, Ar, Kr, and Xe can be called effective (or empirical) solid-state potentials.

The effect of this modification on calculations of the structure and spectra of matrix-isolated atoms was studied on the example of sodium in an argon matrix (Na@Ar). From the viewpoint of optical spectroscopy, this system is the most thoroughly studied one among systems of a metal atom matrix isolation. The absorption spectrum of Na $^2S \rightarrow ^2P$ transition has been considered in many studies. For Na in the gas phase, this transition is observed at 16956 and $16973\ \text{cm}^{-1}$ (Fraunhofer lines D₁ and D₂). Splitting occurs due to spin-orbit coupling in the $^2P$ state. If there was no spin-orbit coupling, the D line would be at $16968\ \text{cm}^{-1}$. Three bands with triplet structure and a full width at half maximum (FWHM) that exceeded $1000\ \text{cm}^{-1}$ are observed on the matrix absorption spectrum. So there are three different capture sites with high symmetry responsible for the Jahn–Teller triplet structure of the absorption bands. In all cases the signal center is shifted relative to the frequency of the gas-phase transition, and the shift magnitudes are 132 (the so-called red site), 1443 (the blue site), and $2583\ \text{cm}^{-1}$ (the violet site) [3].

Theoretical interpretations of the results described above differ. According to the modeling by Ryan et al. [3], all sites correspond to the capture of Na inside an Ar crystal lattice; i.e., red site corresponds to a hexavacancy (HV) formed by removing six RG atoms; blue site—to a tetravacancy (TV) obtained by removing four atoms; and violet one—to one atom of RG matrix being replaced (SS). Jacquet et al. [4] attributed the red site to Na atoms localized on the grain boundaries in a matrix which is far from an ideal crystal structure. Trapping site stability analysis carried out with molecular dynamics simulation of Na and Ar co-condensation onto a substrate [21] revealed the presence of only one TV site [3]. Different models of Na–Ar interaction were used in these works, but Ar–Ar interaction was described in the same way by Aziz gas-phase potential [7].

Following the Ryan et al., we analyzed the relative stability of different trapping sites and their absorption spectra in Na@Ar using the initial and effective potentials of solid-state Ar–Ar interaction. Attribution of the different trapping sites to the excitation spectrum bands by Ryan et al. were confirmed. It was shown that a more accurate description of the Ar matrix improves the agreement with the positions and shapes of the bands observed in the experiments. The effective solid-state potentials of inert gases may thus be recommended for research in the field of matrix isolation.

## CALCULATION DETAILS
### Potentials of Rare Gas Interaction

Along with more complex dependences [24–26] both Lennard-Jones and Morse potentials [17, 19, 22, 23] were used to construct the effective potentials of crystal RGs. In this paper, the following idea was proposed to obtain such potentials. The familiar and well-known gas-phase potential Aziz functions ($V_{\text{gas}}(R)$ for RG = Ne [6], Ar [7], Kr [8], and Xe [9], where $R$ is the internuclear distance) were modified using two transformations defined by two parameters. The first variant of modification was

$$
V_{\text{solid},1}(R) = \alpha_1 V_{\text{gas}}(\beta_1 + R), \tag{1}
$$

and the second was

$$
V_{\text{solid},2}(R) = \alpha_2 V_{\text{gas}}(\beta_2 + R). \tag{2}
$$

Parameters $\alpha$ and $\beta$ were chosen such that calculations of the ideal inert gas lattice reproduced the experimental values of lattice parameter $a$ and atomization energy. The energy of atomization was calculated as half the interaction energy between one atom and a spherical fragment of the fcc lattice for radii $r =$ 6, 8, and $10a$. The obtained values were extrapolated to the limit of an infinite crystal using next equation

$$
E_\infty \approx E(r) + C/r^3. \tag{3}
$$

Because of the long-range effects the equilibrium a value dependence on $\beta$ parameter is nonlinear. This parameter was first determined using an iterative procedure with $\alpha = 1.0$. Then $\alpha$ was calculated from the ratio of the experimental and calculated atomization energy values. The final results took the form of an exponent-spline-C6 function, as was described in [27].

### Na−Ar Coupling Sites

Stable capture sites of Na@Ar system were identi-fied using the original technique described in [27, 28]. The modeled system consisted of a moving region whose atoms are free to move, and a surrounding region with fixed RG atoms modeling long-range order. This model corresponds to considering a matrix-isolated system as a point defect of an ideal crystal. The dimensions of the mobile and fixed regions were chosen so that the estimated energies did not change by more than $1-2\ \text{cm}^{-1}$ upon a subsequent increase in the size of the region. The moving part contained around 1000 atoms, while the fixed part contained around 8000. The energies of the systems with embedded Na atom and different numbers of removed rare gas atoms were found by minimizing the energy for a given set of pair potentials and then cor-rected for the atomization energy of corresponding number of removed RG atoms. The convex hulls approach was used to determine thermodynamic sta-bility, as in [29, 30]. Systems that are resistant to dis-proportionation processes correspond to thermody-namically stable capture sites. The considered options for force fields were

FF00: $V_{\text{gas}}$ for Ar−Ar and Na−Ar interactions;

FF10: $V_{\text{solid,1}}$ for Ar−Ar interaction and $V_{\text{gas}}$ for Na−Ar interaction;

FF11: $V_{\text{solid,1}}$ for Ar−Ar and Na−Ar interactions;

FF20: $V_{\text{solid,2}}$ for Ar−Ar interaction and $V_{\text{gas}}$ for Na−Ar interaction;

FF22: $V_{\text{solid,2}}$ for Ar−Ar and Na−Ar interactions.

Note that FF11 and FF22, modifications were applied to Na−Ar pair potentials with the same to Ar−Ar potential values of parameters $\alpha$ and $\beta$. This rather arbitrary correction was introduced in order to test the spectral characteristics. On the one hand, the identical transformation of all potentials should not greatly alter the results. On the other hand, empirical solid-state potentials effectively include correction to zero-point energy, the contribution from which should also be considered for the embedded atom.

### Electronic Spectra Simulation

The energy of excited states was calculated from Diatomics-in-Molecules [2] used for modeling simi-lar systems [3, 31]. A three-dimensional Hamiltonian matrix was parametrized by the energies of electronic terms $\text{B}^2\Sigma^+$ and $\text{A}^2\Pi$, which correspond to dissociation limit $\text{Na}(^2P) + \text{Ar}(^1S)$. As for the ground state, $V_{\Sigma}$ and $V_{\Pi}$ potentials were taken from [3] and used as the initial unperturbed forms.

It should be note that DIM for calculation the energy of a sodium atom in the P-state situated in a high-symmetry matrix environment can be reduced to a simpler approach. In groups of symmetry $T_{\text{d}}$ and $O_{\text{h}}$, a three-dimensional irreducible representation corre-sponds to the $P$ state, so a DIM Hamiltonian matrix consisting of three components of $P$ term is propor-tional to the identity matrix. The shift of the transition frequency due to interaction with the matrix can be calculated using the expression

$$
\Delta\omega = \Sigma_i N_i V_{\Delta}(R_i),\quad V_{\Delta}=V_0-V_{\text{GS}}, \tag{4}
$$

where $i$ is the index of the coordination polyhedron, $N_i$ is the number of atoms in the corresponding polyhe-dron, $R_i$ is the distance between the embedded atom and the polyhedron atoms, $V_0$ is the isotropic potential of the Na−Ar excited state, $V_0=(V_{\Sigma}+2V_{\Pi})/3$, and $V_{\text{GS}}$ is the potential of the Na−Ar ground state.

The shapes of the absorption bands were calculated in the semiclassical approximation via thermody-namic integration along the molecular dynamic tra-jectory (see, e.g., [3, 28, 31]). The trajectory was cal-culated at the classic temperature of 39 K correspond-ing to a real experimental temperature of 4 K [3, 32]. A Langevin thermostat with coupling constant $\gamma=$ 5 atomic units was used for our calculations. The equations of motion were integrated using the Verlet algorithm. The time step equal 0.25 fs was chosen such that the system energy remained the same for 10 ps. The equilibrium geometries of stable sites, obtained by analyzing thermodynamic stability, were thermostated for 50 ps. It should be note that the required tempera-ture was reached in 5 ps. The dynamic trajectory was observed for 5 ns. A model DIM Hamiltonian was obtained at each point of the trajectory, and the ener-gies of the vertical transitions were calculated.

## RESULTS AND DISCUSSION

### Effective Solid-State Potentials

The parameters calculated for the modifications of the RG−RG potentials are presented in Table 1. The experimental values of lattice parameter $a_{\text{exp}}$ and energy of atomization $E_{\text{exp}}$ (taken from [13]), com-pared to those calculated using initial gas-phase potentials $a_{\text{gas}}$ and $E_{\text{gas}}$ are also shown. Our results for the gas-phase potentials slightly differ from those pre-sented by Rościszewski et al. [13] (the energy of atom-ization is $\sim30\ \text{cm}^{-1}$ higher for all of the RGs, while the lattice parameters differ by less than $0.01\ \mathring{A}$). This discrepancy apparently results from our extrapolation to infinite crystal size (3).

The parameters of modification except $\beta_2$ change monotonically from Ne to Xe. Parameters $\alpha_1$ and $\beta_1$ tend to unity, indicating that the modified potential becomes closer to that of the gas phase upon an increase in the size of the rare gas atom. Parameter $\alpha_2$

<table><tbody><tr><td colspan="9">Table 1. Initial data and results from approximating variable parameters for modifying RG−RG potentials</td></tr><tr><td>RG</td><td>$E_{exp}$, cm$^{-1}$</td><td>$E_{gas}$, cm$^{-1}$</td><td>$a_{exp}$, Å</td><td>$a_{gas}$, Å</td><td>$\alpha_1$</td><td>$\beta_1$</td><td>$\alpha_2$</td><td>$\beta_2$, Å</td></tr><tr><td>Ne</td><td>165</td><td>234</td><td>4.464</td><td>4.275</td><td>0.7053</td><td>1.0432</td><td>0.7092</td><td>0.116</td></tr><tr><td>Ar</td><td>646</td><td>787</td><td>5.311</td><td>5.200</td><td>0.8208</td><td>1.0214</td><td>0.8293</td><td>0.074</td></tr><tr><td>Kr</td><td>936</td><td>1096</td><td>5.67</td><td>5.553</td><td>0.8565</td><td>1.0211</td><td>0.8602</td><td>0.080</td></tr><tr><td>Xe</td><td>1328</td><td>1524</td><td>6.132</td><td>6.049</td><td>0.8715</td><td>1.0138</td><td>0.8760</td><td>0.060</td></tr></tbody></table>

also tends to one in the Ne−Xe series, while the monotonic change in $\beta_2$ is interrupted for krypton, with which the parameter grows.

The relationship between the effective size of the atom and the proximity of the modified and gas-phase potentials can be easily traced by comparing the experimental and calculated data using gas-phase potentials. In case of neon, the difference between the lattice parameter values is slightly more than 4%; in the xenon matrix, it is no higher than 1.5%. A similar situation is observed for the atomization energies. For neon, the experimental and calculated values differ by 42%, while for xenon the data differ by 15%. The relative energy corrections in terms of percentage are around ten times higher than those for geometry.

### Capture Sites in Na@Ar

The energy dependences of the optimum Na@Ar structures on the number of distant Ar atoms $n$, calculated using different potentials, are shown in Fig. 1 in a relative scale, where the energy at $n = 1$ was taken for zero. The thermodynamically stable structure found in this case corresponded to substituting a single Na atom for an Ar atom (SS site, local symmetry $O_\text{h}$). Two other stable structures formed by removing four and six Ar atoms, respectively, correspond to the inclusion of Na in the regular tetrahedral tetravacancy TV ($T_\text{d}$ symmetry) and octahedral hexavacancy HV ($O_\text{h}$ symmetry). The qualitative shape of the dependence and the correspondence of the structures remained the same when the potentials of interaction were changed, but the quantitative effect of changing the gas-phase potentials of the Ar−Ar dimer on the effective solid-state potential was pronounced. In the latter case, the energy of structures with large numbers of distant Ar atoms decreased. No differences were observed in the results when using a modification of the first or second type. Modifying the Na−Ar potential resulted in a much less altered energy.

![](./images/812745923988815873_1.jpg)

Fig. 1. (Color online) Relative energies of the most stable Na@Ar structures corresponding to $n$ removed Ar atoms. Results from calculations with FF00 (the force field of gas-phase potentials), FF10 (FF20) (only the Ar−Ar potential was modified), and FF11 (FF22) (the Ar−Ar and Na−Ar potentials were modified) are shown. Numbers 1 and 2 denote modifications according to Eq. (1) and Eq. (2), respectively; $n$ is the number of Ar atoms.

The thermodynamically stable capture sites found here were entirely analogous to those postulated by Ryan et al. from geometrical considerations in [3] (where no thermodynamic stability analysis was performed).

The left side of Table 2 gives the distances between the Na and Ar atoms of the first three coordination polyhedra, each of which consists of $N_\text{i}$ atoms of Ar. Note that the third polyhedra of the TV and HV vacancies are split into two nonequivalent subshells, denoted as 3 and 3'. All variants of potential modification affect the distances to the second and third coordination polyhedra more strongly than to that of the nearest one. This dependence is observed for all sites and is most pronounced for TV.

The right side of Table 2 presents the contributions from coordination polyhedra to the matrix shift of the $^2S \rightarrow {}^2P$ spectrum according to Eq. (4), which can be applied to the stable highly symmetric structures. As expected, the atoms of the first polyhedron make the largest contributions to the shifts. When modifying the Ar−Ar potentials, these contributions grow from ~40 to ~300 cm$^{-1}$, depending on the capture site.

The results for gas-phase potentials are in qualitative agreement with similar calculations for the structures of stable Mn [27] and Yb capture sites [28] in argon, krypton, and xenon matrices.

### Absorption Spectra

The energies of the vertical $^2S \rightarrow {}^2P$ transition are presented in Table 3. The center of the SS substitution

<table><caption>Table 2. Geometry parameters of stable Na@Ar capture sites and contributions to the spectral shift</caption>
<thead>
  <tr>
    <th rowspan="2">Polyhed-<br>ron $i$</th>
    <th rowspan="2">$N_i$</th>
    <th colspan="5">Distance $R_i$ (Å)</th>
    <th colspan="5">Contribution to shift, $N_iV_\Delta(R_i)$, cm<sup>–1</sup></th>
  </tr>
  <tr>
    <th>FF00</th>
    <th>FF10</th>
    <th>FF11</th>
    <th>FF20</th>
    <th>FF22</th>
    <th>FF00</th>
    <th>FF10</th>
    <th>FF11</th>
    <th>FF20</th>
    <th>FF22</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="13">SS, substitutional site</td>
  </tr>
  <tr>
    <td>1</td>
    <td>12</td>
    <td>3.837</td>
    <td>3.928</td>
    <td>3.920</td>
    <td>3.926</td>
    <td>3.920</td>
    <td>594</td>
    <td>776</td>
    <td>488</td>
    <td>773</td>
    <td>510</td>
  </tr>
  <tr>
    <td>2</td>
    <td>6</td>
    <td>5.201</td>
    <td>5.309</td>
    <td>5.312</td>
    <td>5.308</td>
    <td>5.311</td>
    <td>169</td>
    <td>133</td>
    <td>139</td>
    <td>134</td>
    <td>130</td>
  </tr>
  <tr>
    <td>3</td>
    <td>24</td>
    <td>6.410</td>
    <td>6.549</td>
    <td>6.547</td>
    <td>6.549</td>
    <td>6.548</td>
    <td>−170</td>
    <td>−190</td>
    <td>−139</td>
    <td>−190</td>
    <td>−149</td>
  </tr>
  <tr>
    <td colspan="13">TV, tetravacancy</td>
  </tr>
  <tr>
    <td>1</td>
    <td>12</td>
    <td>4.339</td>
    <td>4.428</td>
    <td>4.432</td>
    <td>4.428</td>
    <td>4.431</td>
    <td>967</td>
    <td>930</td>
    <td>793</td>
    <td>930</td>
    <td>797</td>
  </tr>
  <tr>
    <td>2</td>
    <td>12</td>
    <td>5.637</td>
    <td>5.753</td>
    <td>5.756</td>
    <td>5.754</td>
    <td>5.756</td>
    <td>95</td>
    <td>50</td>
    <td>78</td>
    <td>49</td>
    <td>64</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
    <td>6.760</td>
    <td>6.901</td>
    <td>6.904</td>
    <td>6.901</td>
    <td>6.903</td>
    <td>−34</td>
    <td>−35</td>
    <td>−29</td>
    <td>−35</td>
    <td>−29</td>
  </tr>
  <tr>
    <td>3'</td>
    <td>12</td>
    <td>6.769</td>
    <td>6.911</td>
    <td>6.913</td>
    <td>6.910</td>
    <td>6.912</td>
    <td>−104</td>
    <td>−107</td>
    <td>−85</td>
    <td>−104</td>
    <td>−88</td>
  </tr>
  <tr>
    <td colspan="13">HV, hexavacancy</td>
  </tr>
  <tr>
    <td>1</td>
    <td>8</td>
    <td>4.459</td>
    <td>4.543</td>
    <td>4.552</td>
    <td>4.546</td>
    <td>4.552</td>
    <td>607</td>
    <td>572</td>
    <td>499</td>
    <td>570</td>
    <td>498</td>
  </tr>
  <tr>
    <td>2</td>
    <td>24</td>
    <td>5.796</td>
    <td>5.916</td>
    <td>5.918</td>
    <td>5.916</td>
    <td>5.918</td>
    <td>70</td>
    <td>−1</td>
    <td>59</td>
    <td>−1</td>
    <td>33</td>
  </tr>
  <tr>
    <td>3</td>
    <td>24</td>
    <td>7.786</td>
    <td>7.948</td>
    <td>7.951</td>
    <td>7.948</td>
    <td>7.950</td>
    <td>−180</td>
    <td>−167</td>
    <td>−147</td>
    <td>−167</td>
    <td>−144</td>
  </tr>
  <tr>
    <td>3'</td>
    <td>6</td>
    <td>7.811</td>
    <td>7.977</td>
    <td>7.977</td>
    <td>7.976</td>
    <td>7.977</td>
    <td>−44</td>
    <td>−41</td>
    <td>−37</td>
    <td>−44</td>
    <td>−24</td>
  </tr>
</tbody>
</table>

$R_i$ is the distance between the Na atom and $N_i$ atoms of the equivalent Ar atoms of the $i$th coordination polyhedron (one of the three nearest to the embedded Na atom) for the SS, TV, and HV sites. $N_iV_\Delta(R_i)$ is the contribution to the spectral shift from all atoms of the $i$th polyhedron, according to Eq. (4).

<table><caption>Table 3. Shifts of the absorption band centers in the Na@Ar system with respect to the gas-phase $^2S \to {}^2P$ transition of the Na atom, according to results from modeling, cm<sup>–1</sup></caption>
<thead>
  <tr>
    <th>Site</th>
    <th>FF00</th>
    <th>FF10</th>
    <th>FF11</th>
    <th>FF20</th>
    <th>FF22</th>
    <th>[33]</th>
    <th>[3]</th>
    <th>[4]</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>SS</td>
    <td>64</td>
    <td>548</td>
    <td>82</td>
    <td>570</td>
    <td>79</td>
    <td>800</td>
    <td>~2600</td>
    <td>~2400</td>
  </tr>
  <tr>
    <td>TV</td>
    <td>382</td>
    <td>348</td>
    <td>304</td>
    <td>347</td>
    <td>299</td>
    <td>680</td>
    <td>~900</td>
    <td>~1500</td>
  </tr>
  <tr>
    <td>HV</td>
    <td>87</td>
    <td>39</td>
    <td>71</td>
    <td>38</td>
    <td>73</td>
    <td>465</td>
    <td>~200</td>
    <td>—</td>
  </tr>
</tbody>
</table>

site band shifts most strongly to the blue region, by $484\ \text{cm}^{-1}$ for FF10 and $506\ \text{cm}^{-1}$ for FF20. The shifts of the TV and HV sites are $-34$ and $-48\ \text{cm}^{-1}$, respectively. Unlike the SS site, modification here results in a shift to the red region. Modifying the Ar–Ar potential thus alters the order of the absorption bands of different capture sites observed in the total spectrum. In the unmodified FF00 force field, the band of the SS site was the closest to the gas-phase frequency, while it now becomes the one most distant. Modifying the Na–Ar potential returns the shifts of SS and HV to values close to those calculated for the FF00 field, but the center of the band is in the first case shifted slightly to the blue region; in the second, to the red region. The TV vacancy differs from the others, since modifying the Na–Ar potential results in an even greater blue shift of the band, which is similar in magnitude to the shift caused by modifying the Ar–Ar potentials.

Table 3 also presents the results from earlier calculations of the considered system (estimated from the figures). Our results for FF00 coincide fully with the data of Ryan et al. [3], since the force fields are identical. The calculations from [33] yield the same order of the bands of the three sites. A multi-particle force field, constructed with the effective core potential, was used in [4]. These authors did not consider the HV site, suggesting an alternative model for localizing atoms at grain boundaries. According to their calculations for the two postulated geometries, the magnitudes of the shift are $-130$ and $-280\ \text{cm}^{-1}$. Finally, in the same work, Ryan et al. [3] performed calculations with an artificial modification of the Na–Ar pair potential in the $\text{B}^2\Sigma^+$ state. The sequence of the bands coincided with our data for the effective solid-state potentials.

### Absorption Band Shapes

Figure 2 shows absorption spectra calculated using different force fields. All profiles have a triplet structure, due to the vibronic Jahn–Teller splitting of the triply degenerate excited state of an atom in a high-symmetry field. A similar structure was obtained both in experiment [3] and in earlier calculations [4, 33].

![](./images/812745923988815873_2.jpg)

Fig. 2. (Color online) Absorption bands of the stable capture sites of the Na@Ar system. Presented are the results from calcula- tions with potentials FF00 (the force field of gas-phase potentials), FF10 (FF20) (only the Ar–Ar potential was modified), and FF11 (FF22) (the Ar–Ar and Na–Ar potentials were modified). Numbers 1 and 2 denote modifications according to Eqs. (1) and (2), respectively.

The band widths of the same capture site are virtually independent of the modification of the Ar–Ar poten- tial. Modifying the Na–Ar potential results in a certain narrowing of the band at the TV site, due to the shoul- der in the high-frequency region. The positions of the centers of the bands—the central component of the triplet—virtually coincide with the energies of the ver- tical transitions discussed above.

Experimentally observed centers of absorption bands of the so-called red, blue, and violet Na@Ar sites are shifted to the blue region by 132, 1443, and $2583\ \text{cm}^{-1}$, relative to the gas-phase signal. As can be seen from Table 3, none of the calculations agree with the experimental values to any degree of accuracy. However, there is no doubt about the identification of the blue and red sites with the TV and SS structures, respectively. Our data allows to attribute the band with a shift of $132\ \text{cm}^{-1}$ (the red site) to the HV site. This assignment is consistent with the interpretation of Ryan et al. [3], but contradicts the assumptions of [4].

According to our calculations, the HV site in the Na@Ar system is thermodynamically stable. Although its relative energy is notably higher than that of the SS and TV sites, it should be remembered that the relative energies of the minima on the convex hull are not in any way connected with the population of a particular site. In closed systems, the population is largely deter- mined by the total concentration of atoms and the conditions of preparing the matrix. This is indirectly confirmed by the results from modeling the deposition process, which in the considered system do not pro- vide the main SS site [3], due apparently to unfavor- able kinetics under the conditions of steric hindrances. The results from the experiment in [3] indicate that the population of the red site in the sputtered samples is quite large, but with prolonged irradiation of the matrices, there is a redistribution of the population in favor of the violet site. This behavior is characteristic of stable sites that do not have the lowest energy [28].

Localizing Na atoms at intergrain boundaries should result in spreading of the spectrum, due to the variety of possible geometries, and probably to the fail- ure of the triplet structure. The two possible options considered in [4] for localization actually correspond to triplets displaced relative to one another. In addi- tion, defect sites are likely to be energetically more advantageous than lattice since, since Ar–Ar interac- tion is stronger than Na–Ar interaction. The activa- tion of Na mobility upon irradiation of the matrix should result in ejection of the guest on the surfaces of the grains, and thus to an increase (rather than a decrease) in the intensity of its spectral band.

To describe the Na@Ar system, Ryan et al. [3] used the DIM model, parametrized by the most accurate Na–Ar potentials available from the gas-phase mea- surements and nonempirical calculations taken as a basis in this work. However, we failed in reproducing the experimental values of the shifts of the bands of different sites. Reasonable agreement was reached only after artificial modification of the potential of the excited state. The data of this work show that a more accurate description of the matrix using the effective solid-state potentials also leads to improved agreement with the experimental data, but to a lesser extent from a quantitative point of view. The model proposed by Jacquet et al. [4] yields closer positions of the SS and TV sites for the experimental findings. Note that although it is not as good in reproducing the two-par- ticle component of the potential, it does contain mul- tiparticle interactions. During modeling, it includes the expansion of the matrix because of oscillations, i.e., those factors that were effectively allowed for when building solid-state pair potentials.

It should be noted that the influence of the modi- fied potentials of the matrix grows as the characteristic

![](./images/812745923988815873_3.jpg)

Fig. 3. (Color online) Dependences of $V_{\Delta}$ (4) on distance Na–Ar, obtained using gas-phase and modified potentials.

size of the site shrinks from HV to TV and then to SS. The error in the shift of the band calculated using gas-phase potentials with respect to the experimental error increases in the same sequence, with notable improvement in the results from the modification. However, changing only the characteristics of the matrix for the system in question does not allow us to obtain band shifts close to those measured for compact SS and TV sites. Figure 3 shows change $V_{\Delta}$ in Na–Ar potential difference (4) as the internuclear distance. According to Eq. (4), a shift of $2500\ \text{cm}^{-1}$ can yield 33 Ar atoms localized at a distance of 4–4.5 Å from the Na atom. This situation is not realistic for a matrix with a minimum equilibrium distance between neighbors of around 3.7 Å. The Na–Ar interaction potentials in excited states should probably be refined (especially B²Σ⁺ [3]), or the many-particle contributions to the energy of interaction should be considered explicitly.

## CONCLUSIONS

Simple empirical versions of modifying gas-phase potentials for the interaction of inert gases were proposed that allow us to describe the structure and energy of their crystals. Using the electronic spectrum of the Na@Ar system as an example, it was shown that using these effective solid-state potentials qualitatively improves the results of spectral simulation.

Our results confirm the attribution of three experimentally recorded spectral bands (red, blue, and violet) to three thermodynamically stable crystalline capture sites: hexavacancies, tetravacancies, and substitutions, respectively [3]. For this system, however, the discrepancy between calculations and experiments cannot be eliminated only by clarifying the description of the matrix itself.

## ACKNOWLEDGMENTS

The authors thank G.K. Ozerov (PhD in physics and mathematics) for his helpful comments on our results. This work was supported by the Russian Science Foundation, grant no. 17-13-01466. The shapes of the electronic absorption spectra were calculated using the supercomputer resources of Moscow State University’s Scientific Research Center.

## REFERENCES

1. C. Crépin-Gilbert and A. Tramer, Int. Rev. Phys. Chem. 18, 485 (1999).
2. J. Tully, in *Semiempirical Methods of Electronic Structure Calculation*, Ed. by G. Segal (Springer, New York, 1977), p. 173.
3. M. Ryan, M. Collier, C. Crépin, et al., J. Phys. Chem. A 114, 3011 (2010).
4. E. Jacquet, D. Zanuttini, B. Gervais, et al., J. Chem. Phys. 135, 174503 (2011).
5. B. M. Davis, B. Gervais, and J. G. McCaffrey, J. Chem. Phys. 148, 124308 (2018).
6. R. A. Aziz and M. J. Slaman, Chem. Phys. 130, 187 (1989).
7. R. A. Aziz, J. Chem. Phys. 99, 4518 (1993).
8. A. K. Dham, A. R. Allnatt, W. J. Meath, and R. A. Aziz, Mol. Phys. 67, 1291 (1989).
9. A. K. Dham, W. J. Meath, R. A. Aziz, et al., Chem. Phys. 142, 173 (1990).
10. K. Patkowski and K. Szalewicz, J. Chem. Phys. 133, 094304 (2010).
11. P. Slavíček, R. Kalus, P. Paška, et al., J. Chem. Phys. 119, 2102 (2003).
12. R. Hellmann, B. Jäger, and E. Bich, J. Chem. Phys. 147, 034304 (2017).
13. K. Rościszewski, B. Paulus, P. Fulde, and H. Stoll, Phys. Rev. B 62, 5482 (2000).
14. P. Schwerdtfeger, B. Assadollahzadeh, and A. Hermann, Phys. Rev. B 82, 205111 (2010).
15. C. L. Tian, F. S. Liu, L. C. Cai, et al., J. Chem. Phys. 143, 174506 (2015).
16. M. Abbaspour and Z. Borzouie, Fluid Phase Equilib. 379, 167 (2014).
17. J. S. Brown, Proc. Phys. Soc. London 89, 987 (1966).
18. M. Ross, J. Chem. Phys. 73, 4445 (1980).
19. N. P. Gupta, Solid State Commun. 63, 921 (1987).
20. Y. Choi, T. Ree, and F. H. Ree, Phys. Rev. B 48, 2988 (1993).
21. C. Crepin, B. Bouvier, V. Brenner, et al., Chem. Phys. 272, 243 (2001).
22. I. J. Zucker, J. Chem. Phys. 25, 915 (1956).
23. C. Malinowska-Adamska, P. Sloma, and J. Tomaszewski, Phys. Status Solidi B 200, 451 (1997).
24. J. A. Barker and M. V. Bobetic, J. Chem. Phys. 79, 6306 (1983).

25. P. Schwerdtfeger, N. Gaston, R. P. Krawczyk, et al., Phys. Rev. B **73**, 064112 (2006).

26. N. D. Drummond and R. J. Needs, Phys. Rev. B **73**, 024107 (2006).

27. N. N. Kleshchina, K. A. Korchagina, D. S. Bezrukov, and A. A. Buchachenko, J. Phys. Chem. A **121**, 2429 (2017).

28. L.-G. Tao, N. N. Kleshchina, R. Lambo, et al., J. Chem. Phys. **143**, 174306 (2015).

29. Q. Zhu, A. R. Oganov, and P. B. Allen, Phys. Rev. B **87**, 195317 (2013).

30. A. Frost, J. Am. Chem. Soc. **73**, 2680 (1951).

31. J. P. Visticot, J. M. Mestdagh, A. Lallement, et al., J. Chem. Phys. **100**, 158 (1994).

32. J. P. Bergsma, P. H. Berens, E. J. Heller, et al., J. Chem. Phys. **88**, 612 (1984).

33. J. A. Boatz and M. E. Fajardo, J. Chem. Phys. **101**, 3472 (1994).

Translated by V. Avdeeva

RUSSIAN JOURNAL OF PHYSICAL CHEMISTRY A Vol. 93 No. 8 2019