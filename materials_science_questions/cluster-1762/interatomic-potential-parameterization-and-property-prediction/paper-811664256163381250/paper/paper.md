# Core polarization in solids: Formulation and application to semiconductors

Eric L. Shirley
Optical Technology Division, National Institute of Standards and Technology, Gaithersburg, Maryland 20899

Xuejun Zhu and Steven G. Louie
Department of Physics, University of California, Berkeley, California 94720
and Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720

(Received 25 October 1996; revised manuscript received 4 March 1997)

Accurate treatment of exchange and correlation effects involving core and valence electrons can be surprisingly important in solid-state calculations, especially for solids having elements with shallow core electrons, such as Ga and Ge. A local-density-approximation treatment of core-valence interactions leads to errors of ~0.4 eV for key features in the band structures of Ge and GaAs, even when valence-valence interactions are treated in a first-principles, quasiparticle approach. We apply a core-polarization-potential treatment of core-valence interactions within the framework of such quasiparticle calculations. Final results have errors of ~0.1 eV in band-energy differences. [S0163-1829(97)07035-5]

## I. INTRODUCTION

Determining a material's quasiparticle (band) energies is often done in three steps. First, one solves the atomic structure of the constituent elements, thereby determining effective interactions between core and valence electrons. These interactions can be incorporated into pseudopotentials. $^{1,2}$ Second, one solves the solid's electronic structure self-consistently. This is often done within the local-density approximation (LDA), $^{3}$ which gives an accurate charge density and approximate band energies and one-electron wave functions. Third, quasiparticle energies are obtained by evaluating many-body corrections to LDA band energies, i.e., self-energy effects. $^{4-8}$ One replaces a LDA treatment of such effects with a proper, many-body treatment. So quasiparticle energies in solids reflect effects arising from atomic physics, band-structure effects, and exchange and dynamical electron correlation.

Tremendous simplification is achieved by treating core electrons differently from valence electrons. By ''partitioning'' electrons in this way, however, core-valence interactions are often treated at LDA or Hartree-Fock levels, even in quasiparticle treatments, $^{5-8}$ hampering ultimate accuracies attainable. This can be good enough, because core-valence many-body effects are so small, except in elements with shallow cores, including post-transition elements (e.g., Ga and Ge), alkalis, and alkaline earths.

Hybertsen and Louie $^{5}$ attributed underestimation of the zone-center, direct gap in Ge to relative overbinding of 4s states with respect to 4p states, because of the LDA treatment of core-valence interactions. Godby, Schlüter, and Sham $^{6}$ noted that results for the GaAs band gap were accurate partly because of cancellation of two errors: analogous overbinding effects in Ga and As, and neglect of relaxation of Ga(3d) core states. (The choice of pseudopotentials $^{9}$ in Ref. 6 may also have played a role: Quasiparticle calculations in Ref. 7, using different pseudopotentials, led to an underestimation of the gap.) Fahy, Wang, and Louie $^{10}$ argued that a successful prediction by correlated-wave-function quantum simulations of the structural properties of diamond, graphite, and silicon justifies using LDA-derived pseudopotentials a posteriori. References 11-13 also address such issues.

A different method for core-valence partitioning includes Hartree-Fock treatment of core-valence exchange, but treats core-valence correlation using the core-polarization-potential (CPP) approach. $^{14-18}$ The main motivation for that approach is the fact that valence electrons induce core polarization and feel the induced potential. A valence electron feels dipoles induced by itself and other valence electrons, and so the CPP introduces one- and two-electron terms in the valence Hamiltonian. Therefore, the CPP approach considers correlation between cores and one valence electron and correlation involving cores and several valence electrons. At long range, one-electron terms have the form $-\alpha/(2r^{4})$ as required by the Born-Heisenberg $^{19}$ result, where $\alpha$ is the core polarizability. At short range, these terms are truncated in a parametrized way to give correct binding energies for a single s, p, or d electron bound to the core in vapor phase. Effects beyond electron-core dipole interactions are approximately included by enforcing correct binding energies. Truncation reflects the finite core extent and eliminates divergences at the origin. Two-electron terms have an analogous form: they adhere to the classical result at long range, but are similarly truncated at short range.

Effects of core-valence correlation on valence states may be inferred from first-principles, many-body atomic calculations or from atomic spectra. Successful application of semiempirical CPP's is presented in Ref. 14, which also reviews prior work. Reference 16 applies a first-principles CPP treatment of core-valence correlation to atoms and $Na_{2}$. Reference 17 continues the same work, presents parameters sufficient to construct CPP's for most elements with $Z\leqslant40$, and cites further work.

This work, which was briefly reported previously, $^{20}$ finds quasiparticle energies in Si, Ge, GaAs, and AlAs, by combining the CPP approach and the Hybertsen-Louie approach to compute self-energies for band states. $^{5}$ This involves al-

gorithmic changes in the treatment of atomic many-body ef-
fects and quasiparticle self-energies. In the solid, CPP two-
electron terms modify dynamical screening by including core
polarization, and by coupling valence- and core-polarization
effects, these terms change the effective interaction between
valence electrons. Consequently, both the dielectric screen-
ing and electron self-energy are affected.

Core-valence interactions are one of several effects influ-
encing quasiparticle energies. Valid assessment of the CPP’s
efficacy requires accurate treatment of all others effects,
which are therefore discussed, below. The CPP approach and
its incorporation into quasiparticle calculations are described
next. Relevant computational details are provided, and we
present results found using the CPP approach to obtain qua-
siparticle energies. The CPP’s role in a more unified picture
of electron correlation is also discussed, facilitating a heuris-
tic model for core-polarization effects on electron self-
energies. A summary follows, and we also provide three
technical appendices.

## II. RELATED EFFECTS

### A. Quasiparticle vs density-functional calculations

Quasiparticle excitations, which involve electron addi-
tions and removals, are described by the one-electron
Green’s function⁴
$$
G(\mathbf{r}, \mathbf{r}^{\prime} ; E)=\sum_{n \mathbf{k}} \frac{\Psi_{n \mathbf{k}}(\mathbf{r}) \Psi_{n \mathbf{k}}^{*}\left(\mathbf{r}^{\prime}\right)}{E-\left(E_{n \mathbf{k}}^{\mathrm{qp}} \pm i \eta\right)},\qquad(1)
$$
written above for zero temperature. Indices $n$ and $\mathbf{k}$ denote
the band index and crystal momentum of a quasiparticle;
spin indices are suppressed. $E_{n \mathbf{k}}^{\mathrm{qp}}$ denotes (minus) the energy
to remove an electron from a filled, valence band for $E_{n \mathbf{k}}^{\mathrm{qp}}$
$<E_F$ (Fermi energy) or the energy to add an electron to an
empty, conduction band for $E_{n \mathbf{k}}^{\mathrm{qp}}>E_F$. A positive or negative
imaginary infinitesimal is added to $E_{n \mathbf{k}}^{\mathrm{qp}}$ in the respective
cases. $\Psi_{n \mathbf{k}}(\mathbf{r})$ is a quasiparticle orbital. Quasiparticle excita-
tions may be found by Dyson’s equation
$$
\begin{aligned}
& {\left[-\frac{1}{2} \nabla_{r}^{2}+V_{N}(\mathbf{r})+V_{H}(\mathbf{r})\right] \Psi_{n \mathbf{k}}(\mathbf{r})} \\
& \quad+\int d \mathbf{r}^{\prime} \Sigma\left(\mathbf{r}, \mathbf{r}^{\prime} ; E_{n \mathbf{k}}^{\mathrm{qp}}\right) \Psi_{n \mathbf{k}}\left(\mathbf{r}^{\prime}\right)=E_{n \mathbf{k}}^{\mathrm{qp}} \Psi_{n \mathbf{k}}(\mathbf{r}). \quad(2)
\end{aligned}
$$

Terms on the left include the kinetic energy, nuclear poten-
tial $V_N$, Hartree potential $V_H$, and nonlocal, energy-
dependent self-energy operator (describing exchange and
correlation). A successful approximation for self-energies in
semiconductors is the ‘‘$GW$ approximation’’
$$
\Sigma\left(\mathbf{r}, \mathbf{r}^{\prime} ; E\right) \approx+i \int \frac{d \omega}{2 \pi} e^{+i \eta \omega} G\left(\mathbf{r}, \mathbf{r}^{\prime} ; E+\omega\right) W\left(\mathbf{r}, \mathbf{r}^{\prime} ;-\omega\right).
\qquad(3)
$$

$W$ is the dynamically screened Coulomb interaction.⁴²¹ [Us-
ing pseudopotentials implies an approximate, yet adequate,
description of some one-electron terms in Eq. (2).]

If the local-density approximation (LDA) is used, the self-
energy is replaced by the Kohn-Sham exchange-correlation
potential $V_{\rm xc}(\mathbf{r})$. In semiconductors and insulators, LDA-
derived band gaps are either too small or closed because
of band overlaps. Quantifying this problem requires accurate
band-structure calculations, which need sufficient basis sets,
relativistic effects (including spin-orbit splittings), and core
relaxation [e.g., Ga ($3d$) states in GaAs ‘‘relax,’’ affecting
the band gap by about $-0.25$ eV (Ref. 22)]. Replacing
$V_{\rm xc}(\mathbf{r})$ with $\Sigma$ yields much more accurate band structures,
and band gaps, for insulating materials. To evaluate $\Sigma$, a
common approach⁵·⁶ (also taken here) is to first perform a
LDA or Hartree-Fock self-consistent-field calculation, from
which an approximate $G$ and $W$ are obtained. From these, $\Sigma$
is computed, while updating $G$ and/or $W$ as needed.

![](./images/811664256163381250_1.jpg)

FIG. 1. Errors in energies of one valence electron in the lowest,
$s$, $p$, and $d$ states bound to an atomic core, as given by several
approximations: Hartree-Fock (HF), LDA (Ref. 9), and the gener-
alized $GW$ approximation ($GW$) (Ref. 17). Errors denote differ-
ences from experimental numbers, given in Ref. 23. All calculations
are semirelativistic, and experimental data are properly spin-orbit
averaged. The energy is minus the removal energy. For instance,
the Hartree-Fock treatment does not bind electrons sufficiently
strongly.

### B. Core-valence interactions in Al, Si, Ga, Ge, and As

For free atoms, Shirley and Martin¹⁷ compare errors in
predicted binding energies of valence $s$, $p$, or $d$ electrons to
closed-shell, atomic cores (cf. Fig. 1), using LDA, Hartree-
Fock, and a ‘‘generalized $GW$’’ approximation. Errors in Al
and Si are small and are comparable for $3s$ and $3p$ electrons
for all approximations mentioned, and so quasiparticle re-
sults should not be biased when using any of the above treat-
ments of core-valence interactions. For post-transition ele-
ments, however, $4s$ and $4p$ states are strongly overbound in
the LDA, with $4s$ electrons the most overbound. This leads
to a negative bias for band energies, depending on the states’

<table>
<caption>TABLE I. Reference configurations and parameters for pseudopotential generation, and core-polarization-potential parameters. The length unit is the bohr radius, and the polarizability is in units of bohr³ or, equivalently, bohr² hartree⁻¹</caption>
<thead>
<tr>
<th>Element</th>
<th>Ref. config.</th>
<th>$s,p,d$ $r_c$</th>
<th>$\alpha$</th>
<th>$\lambda_l^{(l)}$'s for $l$=0,1,2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Al</td>
<td>$s^1p^{0.5}d^{0.5}$</td>
<td>1.3, 1.3, 1.3</td>
<td>0.2675</td>
<td>0.7129, 0.6969, 0.7207</td>
</tr>
<tr>
<td>Si</td>
<td>$s^1p^{1.5}d^{0.5}$</td>
<td>1.4, 1.4, 1.3</td>
<td>0.1650</td>
<td>0.6509, 0.6214, 0.6387</td>
</tr>
<tr>
<td>Ga</td>
<td>$s^1p^{0.3}d^{0.7}$</td>
<td>1.5, 1.5, 1.45</td>
<td>1.3147</td>
<td>0.9996, 1.0008, 1.1552</td>
</tr>
<tr>
<td>Ge</td>
<td>$s^1p^{1.5}d^{0.5}$</td>
<td>1.4, 1.4, 1.3</td>
<td>0.7772</td>
<td>0.8633, 0.8552, 0.8248</td>
</tr>
<tr>
<td>As</td>
<td>$s^1p^{2.5}d^{0.5}$</td>
<td>1.3, 1.3, 1.3</td>
<td>0.4833</td>
<td>0.7475, 0.7301, 0.6786</td>
</tr>
</tbody>
</table>

degree of $4s$ character. States with strong $4s$ character can also be highly localized on atomic sites in semiconductors, $^{22}$ enhancing such a bias. Hybertsen and Louie$^5$ noted this effect on results for Ge when using LDA-derived pseudopotentials. Godby, Schlüter, and Sham$^6$ reported the same effect on results for GaAs.

Treating post-transition elements in Hartree-Fock and generalized $GW$ yields errors in binding energies opposite in sign to errors found in a LDA treatment. Generalized $GW$ errors are much smaller than those of LDA or Hartree-Fock treatments, but can still be $\sim 0.3$ eV, which is unacceptably large for semiconductor applications. Post-transition elements are difficult to treat because of their shallow cores. For high accuracy, one must either perform a more complete description of core-valence interactions or resort to some empiricism. With accurate experimental binding energies known for elements considered, $^{23}$ some empiricism is both efficacious and adequately reliable, permitting predictive capacity in solid-state work. (Analogous spectral data are not sufficiently accurate and complete for other post-transition elements, such as In, Sn, and Sb.) We therefore treat core-valence interactions using experimental atomic spectra and relativistic Hartree-Fock calculations, allowing separate evaluations of core-valence exchange and correlation effects. The CPP approach also requires linear, static dipole core polarizabilities, which are taken from Ref. 17 and found in Table I.

### C. Band structures of Si, Ge, GaAs, and AlAs

Band structures are affected by materials' ionicity, atomic shell structures, and core-valence and valence-valence interactions. Key band structure features are highly material dependent: the types (direct vs indirect) and sizes of fundamental band gaps, orderings and splittings of conduction-band valleys, or symmetries of atomic orbitals dominating various electron states. Consequently, an accurate description of core-valence interactions can help predict potential technological applications. Practical properties of semiconductors strongly affected by band structure include lifetimes and transport properties of hot carriers, and energies and strengths of optical absorption and emission features.

For band structures studies, Table II presents low-temperature experimental data, $^{24-27}$ LDA pseudopotential results (found with LDA-derived pseudopotentials), full-potential all-electron LDA results, $^{28-32}$ differences between the above two types of LDA results (mostly core-relaxation effects), pseudopotential-based quasiparticle results from Refs. 5 and 7, and the quasiparticle results corrected for pseudopotential errors (using numbers in Table II). Quasiparticle results for these materials are also found in Refs. 6, 33, and 34. All energies are referenced to valence-band maxima, where spin-orbit splitting effects have been included. *Numerical precision* of LDA calculations is percents of 1 eV, whereas numerical precision is $\sim 0.1$ eV in quasiparticle work. The LDA systematically underestimates band gaps by $0.5-2.0$ eV, and this discrepancy is reduced in quasiparticle results. *The most important many-body effects are, by far, those involving valence-valence interactions*.

Nonetheless, discrepancies between experiment and quasiparticle results are largest for Ge and GaAs, particularly with core-relaxation effects included. These discrepancies result from LDA treatment of core-valence interactions. Agreement with experiment is very good for Si. Agreement is nearly as good for AlAs, but $\Gamma_{8v} \to \Gamma_{6c}$ is underestimated. (We use the same notation as Ref. 24.) Apparently, the As core leads to important core-valence exchange and correlation effects, but not core-relaxation effects. In GaAs and Ge, besides there being core-relaxation effects, $\Gamma_{8v} \to \Gamma_{6c}$ transitions are too small, giving a small gap in GaAs and an incorrect prediction of a direct gap in Ge. However, indirect gaps in Ge are predicted accurately. The conduction-band, $X_{6c} \to L_{6c}$ intervalley splitting in GaAs is too large, and the $X_{6c} \to X_{7c}$ splitting is too small.

All of the above difficulties are explained by the LDA's overbinding effects in Ga, Ge, and As. The promotions $\Gamma_{8v} \to \Gamma_{6c}$ in AlAs and GaAs or $\Gamma_{8v} \to \Gamma_{7c}$ in Ge are essentially from $3p$ or $4p$ to $3s$ or $4s$ states, and band structures are correspondingly biased. At $L$ and $X$, one has states with mixed $s$ and $p$ character, as well as some $d$ character, with higher angular momenta emphasized more at $X$ than at $L$. In GaAs, the lowest conduction-band state at $X$ state is chiefly $\text{Ga}(4p)$ and $\text{As}(4s)$, whereas the second lowest is chiefly $\text{Ga}(4s)$ and $\text{As}(4p)$. (There is a symmetry reason for such combinations of $s$ and $p$ states.)

### D. Core relaxation

Core-relaxation effects are demonstrated in Table II. There are two types of effects, and both have been demonstrated in GaAs: $^{28}$ changes in core orbitals, affecting the crystal potential, and hybridization of core and valence atomic orbitals [e.g., Ga $(4p_z)$ with Ga $(3d_{xy})$]. Pseudopotential calculations neglect core-relaxation effects by definition, $^{35}$ while other pseudopotential errors are found to be small, based on results for Si and AlAs, where frozen-core errors are minimal. The GaAs band gap is reduced by $\sim 0.25$ eV because of core relaxation, as shown in Tables II

<table>
<caption>TABLE II. Band-energy differences in Si, Ge, GaAs, and AlAs, given in eV. Results from experiment, LDA pseudopotential (PP) and full-potential (FP) calculations, estimates of core-relaxation effects based on LDA calculations ($\Delta_{\text{cr}}$), and quasiparticle results (QP) without and with core-relaxation (cr) effects. Fundamental gaps are underlined and/or labeled $E_{g}$.</caption>
<tbody>
<tr>
<td>Quantity</td>
<td>Expt.a</td>
<td>LDA
PP</td>
<td>LDA
FP</td>
<td>$\Delta_{\text{cr}}$</td>
<td>QP
no
cr</td>
<td>QP
LDA
cr</td>
</tr>
<tr>
<td colspan="7"></td>
</tr>
<tr>
<td>Si</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow\Gamma_{6c}$</td>
<td>3.45</td>
<td>2.59</td>
<td>2.55</td>
<td>$-0.04$</td>
<td>3.35</td>
<td>3.31</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow X_{5c}$</td>
<td>1.32b</td>
<td>0.65</td>
<td>0.65</td>
<td>0.00</td>
<td>1.44</td>
<td>1.44</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow L_{6c}$</td>
<td>2.1,c2.40(15)d</td>
<td>1.47</td>
<td>1.43</td>
<td>$-0.04$</td>
<td>2.27</td>
<td>2.23</td>
</tr>
<tr>
<td>$L_{6c}\rightarrow X_{5c}$</td>
<td>$-0.78,-1.08(15)$</td>
<td>$-0.82$</td>
<td>$-0.78$</td>
<td>0.04</td>
<td>$-0.83$</td>
<td>$-0.79$</td>
</tr>
<tr>
<td>$E_{g}$</td>
<td>$\underline{1.17}$</td>
<td>$\underline{0.55}$</td>
<td>$\underline{0.52}$</td>
<td>$-0.03$</td>
<td>$\underline{1.29}$</td>
<td>$\underline{1.26}$</td>
</tr>
<tr>
<td>Ge</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow\Gamma_{7c}$</td>
<td>0.89</td>
<td>$-0.09$</td>
<td>$-0.26$</td>
<td>$-0.18$</td>
<td>0.71</td>
<td>0.53</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow X_{5c}$</td>
<td>1.10b</td>
<td>$\overline{0.50}$</td>
<td>$\overline{0.55}$</td>
<td>0.05</td>
<td>$\overline{1.23}$</td>
<td>$\overline{1.28}$</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow L_{6c}$</td>
<td>$\underline{0.744}$</td>
<td>0.01</td>
<td>$-0.05$</td>
<td>$-0.05$</td>
<td>0.75</td>
<td>0.70</td>
</tr>
<tr>
<td>$L_{6c}\rightarrow X_{5c}$</td>
<td>0.36</td>
<td>0.49</td>
<td>0.60</td>
<td>0.11</td>
<td>0.48</td>
<td>0.58</td>
</tr>
<tr>
<td>GaAs</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow\Gamma_{6c}$</td>
<td>$\underline{1.52}$</td>
<td>0.40</td>
<td>$\underline{0.13}$</td>
<td>$-0.27$</td>
<td>$\underline{1.29}$</td>
<td>$\underline{1.02}$</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow X_{6c}$</td>
<td>$\underline{2.01}$</td>
<td>$\overline{1.18}$</td>
<td>$\overline{1.21}$</td>
<td>0.02</td>
<td>$\overline{2.05}$</td>
<td>$\overline{2.07}$</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow L_{6c}$</td>
<td>1.84</td>
<td>0.83</td>
<td>0.70</td>
<td>$-0.13$</td>
<td>1.69</td>
<td>1.56</td>
</tr>
<tr>
<td>$L_{6c}\rightarrow X_{6c}$</td>
<td>0.17</td>
<td>0.35</td>
<td>0.51</td>
<td>0.15</td>
<td>0.37</td>
<td>0.52</td>
</tr>
<tr>
<td>$X_{6c}\rightarrow X_{7c}$</td>
<td>0.40</td>
<td>0.24</td>
<td>0.21</td>
<td>$-0.03$</td>
<td>0.29</td>
<td>0.26</td>
</tr>
<tr>
<td>AlAs</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow\Gamma_{6c}$</td>
<td>3.13</td>
<td>1.77</td>
<td>1.76</td>
<td>$-0.01$</td>
<td>2.75</td>
<td>2.74</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow X_{6c}$</td>
<td>$\underline{2.24}$</td>
<td>$\underline{1.20}$</td>
<td>$\underline{1.22}$</td>
<td>0.01</td>
<td>$\underline{2.08}$</td>
<td>$\underline{2.09}$</td>
</tr>
<tr>
<td>$\Gamma_{8v}\rightarrow L_{6c}$</td>
<td></td>
<td>$\overline{1.89}$</td>
<td>$\overline{1.91}$</td>
<td>0.01</td>
<td>$\overline{2.79}$</td>
<td>$\overline{2.80}$</td>
</tr>
<tr>
<td>$L_{6c}\rightarrow X_{6c}$</td>
<td></td>
<td>$-0.69$</td>
<td>$-0.69$</td>
<td>0.00</td>
<td>$-0.71$</td>
<td>$-0.71$</td>
</tr>
<tr>
<td>$X_{6c}\rightarrow X_{7c}$</td>
<td></td>
<td>0.86</td>
<td>0.87</td>
<td>0.01</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="7">aUnless noted, Ref. 24.</td>
</tr>
<tr>
<td colspan="7">bRef. 25.</td>
</tr>
<tr>
<td colspan="7">cRef. 26.</td>
</tr>
<tr>
<td colspan="7">dRef. 27.</td>
</tr>
</tbody>
</table>

and III. The LDA band gap for Ge is nearly zero in a semirelativistic pseudopotential calculation, if core-valence interactions are treated in the LDA, while an analogous fullpotential LDA result yields a 0.17-eV band overlap.

(Whereas Ge cores are deeper than Ga cores, there are two Ge cores per unit cell. So core-relaxation effects are about one-third as large for the Ge core as for Ga, and should be negligible for As.)

<table>
<caption>TABLE III. Band gap in GaAs, in eV, as found in pseudopotential and full-potential LDA results. Pseudopotential results include the nonlinear core correction.</caption>
<tbody>
<tr>
<td>Method</td>
<td>Result</td>
</tr>
<tr>
<td>FLAPW,a,b no $3d$-$4p$ hybridization</td>
<td>0.20</td>
</tr>
<tr>
<td>FLAPW,b with $3d$-$4p$ hybridization</td>
<td>0.12</td>
</tr>
<tr>
<td>FLAPWc</td>
<td>0.16</td>
</tr>
<tr>
<td>FLAPWd</td>
<td>0.13</td>
</tr>
<tr>
<td>Pseudopotential (this work)</td>
<td>0.40</td>
</tr>
<tr>
<td>LMTOe,f</td>
<td>0.25</td>
</tr>
<tr>
<td colspan="2">aFull potential linearized augmented plane wave.</td>
</tr>
<tr>
<td colspan="2">bRef. 28.</td>
</tr>
<tr>
<td colspan="2">cRef. 29.</td>
</tr>
<tr>
<td colspan="2">dRef. 31.</td>
</tr>
<tr>
<td colspan="2">eLinear muffin-tin orbital.</td>
</tr>
<tr>
<td colspan="2">fRef. 22.</td>
</tr>
</tbody>
</table>

## III. CORE-POLARIZATION-POTENTIAL FORMULATION

### A. Atomic theory

CPP treatments can be used within frozen-core all-electron or pseudopotential work, but this work is only the latter. For further details regarding the generation of normconserving (or shape-consistent) pseudopotentials, we refer to the standard references.1,2,36–39 The present CPP formulation is described in more detail in Ref. 17. Formally, the CPP only describes correlation. Exchange is treated exactly within the Hartree-Fock treatment. So the CPP modifies a Hartree-Fock treatment of core-valence interactions, and our CPP approach represents modification of Hartree-Fock pseudopotentials.

Core-valence correlation effects are expressed via oneand two-electron terms in the (valence) Hamiltonian. These operators act only on valence electrons. For an ion of type $I$ located at the origin, there is a one-electron term which is a nonlocal potential:

$$
\begin{aligned}
V_{e}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)= & -\frac{\alpha_{I}}{2 r^{2} r^{\prime 2}} \frac{\delta\left(r-r^{\prime}\right)}{r r^{\prime}} \\
& \times \sum_{l m} f\left(\frac{r}{\lambda_{I}^{(l)}}\right) f\left(\frac{r^{\prime}}{\lambda_{I}^{(l)}}\right) Y_{l m}(\hat{\mathbf{r}}) Y_{l m}^{*}\left(\hat{\mathbf{r}}^{\prime}\right). \quad(4)
\end{aligned}
$$

This has the same form as semilocal pseudopotentials. The $\alpha_{I}$ denotes a core polarizability, and we have used $f(x)$ $=\left[1-\exp \left(-x^{2}\right)\right]^{2}$. We have $f(x)=1$ at long range, yielding the Born-Heisenberg result, but we have $f(x)=0$ at short range, making $V_{e}$ behave well everywhere. For low angular momentum $l$, the $\lambda_{I}^{(l)}$'s are specified as follows: $\lambda_{I}^{(l)}$ is varied to achieve the correct removal energy for one valence electron with each $l$ bound to a core. For $l \geqslant 3$, we use $\lambda_{I}^{(2)}$. There is some arbitrariness regarding the form of $f$ functions. In Appendix A, where aspects of the $f$ functions are discussed further, we argue why such arbitrariness is not problematic here.

Besides $V_{e}$, the CPP has an analogous, two-electron term. For an ion of type $I$ located at the origin, one has the following interaction between two electrons at points $\mathbf{r}$ and $\mathbf{r}^{\prime}$. This interaction is a local potential, but depends on more than $\mathbf{r}$ $-\mathbf{r}^{\prime}$ :
$$
V_{e-e}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)=-\alpha_{I}\left(\frac{\mathbf{r} \cdot \mathbf{r}^{\prime}}{r^{3} r^{\prime 3}}\right) f\left(r / \Lambda_{I}\right) f\left(r^{\prime} / \Lambda_{I}\right). \quad(5)
$$

Because $V_{e}$ and $V_{e-e}$ describe electrons inducing and feeling the same core dipoles, it is reasonable to truncate $V_{e}$ and $V_{e-e}$ similarly at short range. Indeed, all $\lambda_{I}^{(l)}$'s are similar for $l$ $=0,1$, and 2 . It is not obvious how to specify $\Lambda_{I}$. We follow Ref. 17, which uses
$$
\Lambda_{I}=\frac{1}{2}\left(\lambda_{I}^{(0)}+\lambda_{I}^{(1)}\right). \quad(6)
$$

Effects of $V_{e-e}$ include cores' screening $l=1$ valencevalence exchange, and were included in results presented for eleven major-group elements in Ref. 17. When the ab initio $\lambda_{I}^{(l)}$'s gave accurate binding energies, such as in $\mathrm{B}, \mathrm{Al}$, and $\mathrm{Si}$, effects of $V_{e-e}$ were usually accurate to within $20 \%$ of the total effects. Results would have improved by enhancing the effects in some cases and reducing them in other cases. Such accuracy persists also for the present, semiempirical CPP's. Based on solid-state test of $V_{e-e}$ 's effects on quasiparticle self-energies, which we discuss later, we attribute to $V_{e-e}$ a 0.05-eV component of the uncertainty (to be added in quadrature with other components) of our theoretical values for interband transitions presented in Table II and emphasized throughout this work.

The nonlocal $V_{e}$ is not part of the local "Kohn-Sham" potential discussed in "exact" density-functional theory, ${ }^{40}$ which is valid only for the system of all electrons. However, addition of one valence electron to a core may be exactly described within the Green's function approach, which involves a nonlocal self-energy operator. Also, $V_{e-e}$ does not depend only on the difference between two valence electrons' coordinates, because the CPP describes creation of core excitations because of fluctuating valence charge densities, and such excitations can have nonzero momentum. The total crystal momentum, of valence electrons plus core excitations, is still conserved.

Because only valence electrons feel the CPP, core and valence orbitals will not automatically be orthogonal in allelectron calculations which use a CPP. However, we generate pseudopotentials within a Hartree-Fock context, even during the unscreening step. Only after unscreening are terms associated with $V_{e}$ added to the pseudopotential, implying that one should fit $\lambda_{I}^{(l)}$ 's within a pseudopotential framework. Because pseudopotentials are generated in near-neutral configurations, rather than with only one valence electron present, we obtain $\lambda_{I}^{(l)}$ 's as follows. We generate pseudopotentials in the same way as those used in the quasiparticle work, except with no valence electrons. Then, the $\lambda_{I}^{(l)}$ 's are adjusted to give these bare-core pseudopotentials (plus $V_{e}$ ) correct binding energies for one electron with $l$ $\leqslant 2$. The CPP therefore includes some vapor-phase, corerelaxation effects, in addition to correlation effects, which is desirable.

### B. Coordinating core and valence screening effects

It is straightforward to incorporate a CPP with the above form into quasiparticle calculations, via extension of the Hybertsen-Louie approach. $^{5} \Sigma$ depends on $G$ and $W$, and both $G$ and $W$ are affected by the CPP. Many effects are implicit, being caused by $V_{e}$. However, the form of $W$ is also modified. Without a CPP, the static $W$ is computed in the random-phase approximation (RPA) using the AdlerWiser method. $^{41}$ To obtain self-energies, $W$ is extended to finite frequency using a generalized plasmon-pole model. $^{5}$ Within the RPA, the microscopic dielectric matrix is given as
$$
\varepsilon=1-\nu\left(\chi_{C}^{0}+\chi_{V}^{0}\right). \quad(7)
$$

We shall often write matrix equations, such as the above one, with matrix indices suppressed. Here, $\varepsilon$ is the dielectric matrix, $\nu$ is the bare Coulomb interaction, and $\chi_{C}^{0}$ and $\chi_{V}^{0}$ are contributions of core and valence electrons to the irreducible polarizability, respectively. Normally, $\chi_{C}^{0}$ is neglected, but the CPP introduces it approximately. From Eq. (7), we find
$$
\begin{aligned}
\varepsilon^{-1}= & \left(\frac{1}{1-\nu \chi_{C}^{0}}\right)+\left(\frac{1}{1-\nu \chi_{C}^{0}}\right) \nu \chi_{V}^{0}\left(\frac{1}{1-\nu \chi_{C}^{0}}\right) \\
& +\left(\frac{1}{1-\nu \chi_{C}^{0}}\right) \nu \chi_{V}^{0}\left(\frac{1}{1-\nu \chi_{C}^{0}}\right) \nu \chi_{V}^{0}\left(\frac{1}{1-\nu \chi_{C}^{0}}\right)+\cdots
\end{aligned}
$$
or
$$
\varepsilon^{-1}=\left(\frac{1}{1-\nu \chi_{C}^{0}}\right)+\left(\frac{1}{1-\nu \chi_{C}^{0}}\right) \nu \chi_{V}\left(\frac{1}{1-\nu \chi_{C}^{0}}\right).
$$

The expression
$$
\varepsilon_{C}^{-1}=\left(1-\nu \chi_{C}^{0}\right)^{-1}
$$
describes cores' screening of the effective interaction between valence electrons. Core polarizabilities used include vertex corrections, and so are not evaluated strictly within the RPA regarding intracore interactions. This is not problematic, even though the evaluation of $W$ is based otherwise

on a RPA treatment of screening. Vertex corrections can be important when obtaining accurate core polarizabilities, hav- ing effects as large as $30\%,^{17}$ whereas, regarding interband transitions in the solids studied, $GW$ typically has $0.1-0.2$  eV agreement with experiment, provided that issues of core- valence interactions and core relaxation are resolved. (Reli- ance on experimental data for energies binding valence elec- trons to atomic cores is also outside of a RPA treatment.) For a monatomic system, the CPP modifies the effective, fundamental valence-valence interaction only through the operator $V_{e-e}$ . More work is needed to evaluate e for a polyatomic system because of intercore dipolar interactions. The $\chi_{V}$ in Eq. (9) is like the full, RPA valence density-response function, except that it is evaluated with the electron-electron interaction being
$$W_{C}=\varepsilon_{C}^{-1} \nu.\qquad(11)$$

$W_{C}$ is instantaneous and similar to $\nu$ , and Ref. 17 addresses such an adiabatic approximation.

### C. Evaluation of static $\varepsilon_{C}^{-1}$ and $\varepsilon^{-1}$
The matrix $\varepsilon_{C}^{-1}$ describes screening by the system of atomic cores of an external perturbation. Here external per- turbations are longitudinal electric fields associated with valence-electron density fluctuations. This matrix differs from
$$1+\nu \chi_{C}^{0}\qquad(12)$$
 because atomic cores feel the total effects of an external perturbation, including the potential because of induced core polarization. We first evaluate all effects of a core on itself(the results of which are contained in $V_{e-e}$ ) and then couple cores to each other. Defining the density response to a per- turbing potential for core $I$ as $\chi_{I}$ , the total response of a system of cores to an external perturbation, referred to as Xc, is
$$\chi_{C}=\sum_{I} \chi_{I}+\sum_{I} \chi_{I} \nu \sum_{J \neq I} \chi_{J}+\cdots.\qquad(13)$$

When coupling different cores, $\nu$ is well described in a point dipole picture, even though coupling core dipoles to valence electrons is influenced by the form of $V_{e-e}$ .
Let us denote, by $p_{I i}^{R}$ , the $i$ th Cartesian coordinate of the core dipole on atom $I$ in the unit-cell associated with lattice vector $R$ . At most $3 N$ independent $p_{I i}^{R}$ 's are required to de scribe the cores' response to a perturbation with crystal mo- mentum $q$ , where there are $N$ atoms per unit cell. We may derive $\varepsilon_{C}^{-1}(q)$ by considering such a perturbation. Define
$$p_{I i} \equiv p_{I i}^{\mathbf{R}=0}\qquad(14)$$
 and note the relation
$$p_{I i}^{\mathbf{R}}=e^{i \mathbf{q} \cdot \mathbf{R}} p_{I i}.\qquad(15)$$

A core dipole is given by the local electric field which thecore feels:
$$p_{I i}=\alpha_{I} E_{i}\left(\tau_{I}\right).\qquad(16)$$

E;( r) has contributions from the external perturbation and from other core dipoles. The sum of these contributions maybe written as follows:
$$E_{i}\left(\tau_{I}\right)=\sum_{G} \frac{\delta E_{i}\left(\tau_{I}\right)}{\delta \phi_{\mathrm{ext}}(\mathbf{G}+\mathbf{q})} \phi_{\mathrm{ext}}(\mathbf{G}+\mathbf{q})+\sum_{J j} \frac{\delta E_{i}\left(\tau_{J}\right)}{\delta p_{J j}} p_{J j}.$$

Based on Fourier analysis of $V_{e-e}$ , the contribution from the G+q Fourier component of the external potential is
$$\frac{\delta E_{i}\left(\tau_{I}\right)}{\delta \phi_{\mathrm{ext}}(\mathbf{G}+\mathbf{q})}=-i Q_{i} \Omega_{C}^{-1 / 2} J_{I}(Q) \exp \left(i \mathbf{Q} \cdot \tau_{I}\right). \quad(18)$$

We use the abbreviation $Q=G+q$ , the unit-cell volume is $\Omega_{C}$ , and we have introduced $J_{I}(Q)$ ,
$$J_{I}(Q)=\int_{0}^{\infty} d r \frac{\sin (Q r)}{Q r} \frac{\partial}{\partial r} f\left(\frac{r}{\Lambda_{I}}\right).\qquad(19)$$

 $J_{I}(Q)$ approaches one as $Q$ approaches zero. A given dipole affects the total potential felt by the valence electrons as described through the relation
$$\frac{\delta \phi_{\text {ind }}(\mathbf{G}+\mathbf{q})}{\delta p_{I i}}=-i Q_{i}\left(\frac{4 \pi}{Q^{2}}\right) \Omega_{C}^{-1 / 2} J_{I}(Q) \exp \left(-i \mathbf{Q} \cdot \tau_{I}\right) \text {. }$$

Let us make the abbreviation,
$$\Theta_{I i}(\mathbf{Q})=\sqrt{\frac{4 \pi}{\Omega_{C}}}\left(\frac{Q_{i}}{Q}\right) J_{I}(Q) \exp \left(-i \mathbf{Q} \cdot \tau_{I}\right). \quad(21)$$

Regarding the contributions of core dipoles, one knows
$$\begin{aligned}
\frac{\delta E_{i}\left(\tau_{I}\right)}{\delta p_{J j}}= & \sum_{\mathbf{R}}\left(1-\delta_{\mathbf{R}, 0} \delta_{I J}\right)\left(-\frac{\partial}{\partial \tau_{I i}}\right) \\
& \times\left(\frac{\partial}{\partial \tau_{J j}}\right) \frac{1}{\left|\mathbf{R}+\tau_{J}-\tau_{I}\right|} \exp (i \mathbf{q} \cdot \mathbf{R}). \quad(22)
\end{aligned}$$

This omits intracore interactions, which are incorporated into the $\alpha_{I}$ 's. The above sum can be found using Ewald-Kornfeld techniques, $^{42}$ as described in Appendix B.
The infinite summation in Eq. (15) may now be carried out through a matrix inversion, by first defining
$$M_{I i, J j}=\frac{\delta E_{i}\left(\tau_{I}\right)}{\delta p_{J j}},\qquad(23)$$

$$K_{I i, J j}=\alpha_{I}^{-1} \delta_{I i, J j}-M_{I i, J j},\qquad(24)$$
 to obtain
$$\begin{aligned}
\left(\varepsilon_{C}^{-1}\right)_{\mathbf{G}, \mathbf{G}^{\prime}}(\mathbf{q})= & \frac{Q^{\prime}}{Q}\left[\delta_{\mathbf{G}, \mathbf{G}^{\prime}}-\sum_{I i} \sum_{J j} \Theta_{I i}(\mathbf{Q})\right. \\
& \left.\times\left(K^{-1}\right)_{I i, J j}\left[\Theta_{J j}\left(\mathbf{Q}^{\prime}\right)\right]^{*}\right].
\end{aligned}\qquad(25)$$

Except within the space spanned by the $\Theta$ vectors, the (Her mitean) matrix in brackets is the identity matrix. Thus the matrix in brackets is trivially diagonalized and inverted, which is useful. The only difficulties with such transforma-

tions are that the difference between $\varepsilon_{C}^{-1}$ and the identity matrix fluctuates wildly in the neighborhood of $\mathbf{q}=0$, be- cause of the long-ranged Coulomb potential, and that $K$ can be poorly conditioned for numerical inversion. Manipulation of the formulas for $\varepsilon^{-1}$ yields

$$
\varepsilon=\varepsilon_{C}-\nu \chi_{V}^{0}, \quad(26)
$$

so that $\varepsilon$ and $\varepsilon^{-1}$ may otherwise be constructed in the usual manner, with care taken near $\mathbf{q}=0$.

### D. Modified plasmon-pole model

$V_{e-e}$ also changes forms of the Kramers-Kronig relations and the generalized, longitudinal $f$-sum rule. Both sum rules are used in the generalized plasmon-pole model to extend $\varepsilon^{-1}$ to finite frequency. Whereas changes follow because of the replacement, $\nu \rightarrow W_{C}$, the two-electron operator describ- ing $W_{C}$ is frequency-independent and commutes with the electron-density operator, and so analogs of the sum rules for $\chi_{V}$ are unaffected, yielding

$$
\begin{aligned}
\int_{0}^{\infty} \frac{d \omega}{\omega} \varepsilon_{2, G, G^{\prime}}^{-1}(\mathbf{q}, \omega)= & +\frac{\pi}{2}\left[\varepsilon_{1, \mathbf{G}, \mathbf{G}^{\prime}}^{-1}(\mathbf{q}, \omega=0)\right. \\
& \left.-\left[W_{C} \nu^{-1}\right]_{\mathbf{G}, \mathbf{G}^{\prime}}(\mathbf{q})\right], \quad(27)
\end{aligned}
$$

$$
\begin{aligned}
\int_{0}^{\infty} d \omega \omega \varepsilon_{2, \mathbf{G}, \mathbf{G}^{\prime}}^{-1}(\mathbf{q}, \omega)= & -\frac{\pi}{2} \omega_{p}^{2} \sum_{K, K^{\prime}} \\
& \times \frac{\rho\left(\mathbf{K}-\mathbf{K}^{\prime}\right)}{\rho(0)} \frac{(\mathbf{K}+\mathbf{q}) \cdot\left(\mathbf{K}^{\prime}+\mathbf{q}\right)}{|\mathbf{K}+\mathbf{q}|^{2}} \\
& \times\left[W_{C} \nu^{-1}\right]_{\mathbf{G}, \mathbf{K}}(\mathbf{q}) \\
& \times\left[W_{C} \nu^{-1}\right]_{\mathbf{K}^{\prime}, \mathbf{G}^{\prime}}(\mathbf{q}). \quad(28)
\end{aligned}
$$

This manner of writing the sum rules is helpful when iden- tifying algorithmic changes, because of core polarization, necessary for computing self-energies. In real space, $\varepsilon_{1}^{-1}$ and $\varepsilon_{2}^{-1}$ are the real and imaginary parts of $\varepsilon^{-1}$, while their Fourier transforms are generally complex. We refer to Ref. 7 for further details on the generalized plasmon-pole model.

### E. Evaluation of self-energies

$\Sigma$ can be separated into an exchange term $(\Sigma_{\mathrm{x}})$, dynami cal exchange term $(\Sigma_{\mathrm{dx}})$, and Coulomb-hole term $(\Sigma_{\mathrm{coh}})$, with $\Sigma_{\mathrm{x}}+\Sigma_{\mathrm{dx}}$ often called the screened-exchange term $(\Sigma_{\text {sex }})$. We now have

$$
\begin{aligned}
\left\langle\psi_{n \mathbf{k}}\left|\Sigma_{\mathbf{x}}\right| \psi_{n \mathbf{k}}\right\rangle= & -\sum_{n_{1}}^{\text {occ }} \sum_{\mathbf{q}, \mathbf{G}, \mathbf{G}^{\prime}}\left[W_{C} \nu^{-1}\right]_{\mathbf{G}, \mathbf{G}^{\prime}}(\mathbf{q}) \nu\left(\mathbf{q}+\mathbf{G}^{\prime}\right) \\
& \times\left\langle\psi_{n \mathbf{k}}\left|e^{j(\mathbf{q}+\mathbf{G}) \cdot \mathbf{r}}\right| \psi_{n_{1}, \mathbf{k}-\mathbf{q}}\right\rangle \\
& \times\left\langle\psi_{n_{1}, \mathbf{k}-\mathbf{q}}\left|e^{-j\left(\mathbf{q}+\mathbf{G}^{\prime}\right) \cdot \mathbf{r}^{\prime}}\right| \psi_{n \mathbf{k}}\right\rangle. \quad(29)
\end{aligned}
$$

Expressions for $\Sigma_{\mathrm{dx}}$ and $\Sigma_{\text {coh }}$ are the same as in Ref. 7, which describes them further, but sum rules for the general- ized plasmon-pole model differ as discussed above. We fol- low the convention $\nu(\mathbf{Q})=4 \pi /\left(\Omega Q^{2}\right)$, where $\Omega$ is crystal volume, but the unit-cell volume is $\Omega_{C}$. Modifications re- quired because of the CPP are straightforward, except for sampling $W(\mathbf{q}, \omega)$ near $\mathbf{q}=0$, which is discussed in Appen$\operatorname{dix} \mathrm{C}$.

## IV. RESULTS

### A. Numerical details

Whether in the LDA or Hartree-Fock treatment, we gen- erated Hamann-Schlüter-Chiang $^{1}$ pseudopotentials with Vanderbilt's cutoff functions. $^{2}$ The radially nonlocal Fock exchange is not amenable to this procedure, and was re- placed by an equivalent, orbital-dependent radially local po- tential. This accomplishes exact Hartree-Fock results and preserves benefits of norm conservation. Table I provides pseudopotential and CPP parameters. Several tests have proved band-energy differences to be insensitive to details of pseudopotential generation, so that core-relaxation effects are the chief difficulty with using pseudopotentials in this work. We worked within a semirelativistic (i.e., properly $j$-weighted, spin-orbit-averaged) framework, and spin-orbit splittings were included $a$ posteriori in the band structure. We used semilocal pseudopotentials, using $l=2$ channels as local.

In the solid state, we used 16- and 64-Ry cutoffs for wave functions and crystal potentials, respectively. Band-energy differences were converged to $-0.01 \mathrm{eV}$. Self-consistent LDA calculations used 10 special points $^{43}$ and the Ceperley Alder functional. $^{44,45}$ Quasiparticle results used 22 special points (or 28 special points when computing the Lindhard polarizability). Calculations were also done using a 10- special-point mesh to test convergence with respect to Brillouin-zone sampling. Band-energy differences changed by $\leqslant 0.1 \mathrm{eV}$, indicating convergence at a much better level. We estimate numerical precision of the results, with all as- pects of the calculation considered, to be $\sim 0.1 \mathrm{eV}$.

The $\varepsilon^{-1}$ matrix was expanded for $|\mathbf{G}+\mathbf{q}|$ up to 3.1 bohr $^{-1}$. The Ewald-Kornfeld sum used in the evaluation of $\varepsilon_{C}^{-1}$ was done using $R_{\max }=20$ bohrs for the real-space sum, 300 reciprocal-lattice vectors for the reciprocal-space sum, and $\eta=0.2$. These cutoff parameters greatly exceeded the necessary values to realize the Clausius-Mossotti relation (see Appendix B) to about ten figures.

$G W$ calculations were iterated to achieve self-consistency of quasiparticle energies, but LDA orbitals were retained, having proved adequate in previous work. $^{5,7}$ (Effects of the replacement, $\nu \rightarrow W_{C}$, on $\Sigma$ are no larger than differences between $V_{\mathrm{xc}}$ and $\Sigma$ and have even smaller effects on band- energy differences.) We implemented only rigid-shift cor- rections to energy spectra for valence and conduction bands. Remaining self-consistency effects would be small. Core- relaxation effects were included $a$ posteriori, being estimated as the differences between full-potential and pseudopotential LDA results in Table II. LDA pseudopotentials were gen- erated as specified in Table I, but with a LDA treatment of core-valence interactions, including the nonlinear core correction. $^{35,46}$

### B. Quasiparticle energies

Table IV includes CPP-based quasiparticle results for $\mathrm{Si}$, Ge, GaAs, and AlAs, experimental band energies, LDA re-

<table><caption>TABLE IV. Band-energy differences in Si, Ge, GaAs, and AlAs, in eV. Results for experiment, LDA full-potential FP calculations, and quasiparticle results with a LDA treatment of core-valence interactions and the present results. All results include core-relaxation effects. Fundamental gaps are underlined.</caption>
<tbody><tr><th>Quantity</th><th>Expt.a</th><th>LDA</th><th>Quasiparticle,<br>core-valence<br>interactions<br>treated in LDA</th><th>Quasiparticle,<br>this work</th></tr>
<tr><td>Si</td><td></td><td></td><td></td><td></td></tr>
<tr><td>$\Gamma_{8v}\rightarrow\Gamma_{6c}$</td><td>3.45</td><td>2.55</td><td>3.31</td><td>3.28</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow X_{5c}$</td><td>$1.32^{\text{b}}$</td><td>0.65</td><td>1.44</td><td>1.31</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow L_{6c}$</td><td>$2.1,^{\text{c}}$2.40(15)d</td><td>1.43</td><td>2.23</td><td>2.11</td></tr>
<tr><td>$L_{6c}\rightarrow X_{5c}$</td><td>$-0.78,-1.08(15)$</td><td>$-0.78$</td><td>$-0.79$</td><td>$-0.80$</td></tr>
<tr><td>$E_{g}$</td><td>$\underline{1.17}$</td><td>$\underline{0.52}$</td><td>$\underline{1.26}$</td><td>$\underline{1.13}$</td></tr>
<tr><td>Ge</td><td></td><td></td><td></td><td></td></tr>
<tr><td>$\Gamma_{8v}\rightarrow\Gamma_{7c}$</td><td>0.89</td><td>$-0.26$</td><td>0.53</td><td>0.85</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow X_{5c}$</td><td>$1.10^{\text{b}}$</td><td>$\underline{0.55}$</td><td>$\underline{1.28}$</td><td>1.09</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow L_{6c}$</td><td>$\underline{0.744}$</td><td>$-0.05$</td><td>0.70</td><td>$\underline{0.73}$</td></tr>
<tr><td>$L_{6c}\rightarrow X_{5c}$</td><td>0.36</td><td>0.60</td><td>0.58</td><td>0.36</td></tr>
<tr><td>GaAs</td><td></td><td></td><td></td><td></td></tr>
<tr><td>$\Gamma_{8v}\rightarrow\Gamma_{6c}$</td><td>$\underline{1.52}$</td><td>$\underline{0.13}$</td><td>$\underline{1.02}$</td><td>$\underline{1.42}$</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow X_{6c}$</td><td>$\underline{2.01}$</td><td>$\underline{1.21}$</td><td>$\underline{2.07}$</td><td>$\underline{1.95}$</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow L_{6c}$</td><td>1.84</td><td>0.70</td><td>1.56</td><td>1.75</td></tr>
<tr><td>$L_{6c}\rightarrow X_{6c}$</td><td>0.17</td><td>0.51</td><td>0.52</td><td>0.20</td></tr>
<tr><td>$X_{6c}\rightarrow X_{7c}$</td><td>0.40</td><td>0.21</td><td>0.26</td><td>0.33</td></tr>
<tr><td>AlAs</td><td></td><td></td><td></td><td></td></tr>
<tr><td>$\Gamma_{8v}\rightarrow\Gamma_{6c}$</td><td>3.13</td><td>1.76</td><td>2.74</td><td>2.93</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow X_{6c}$</td><td>$\underline{2.24}$</td><td>$\underline{1.22}$</td><td>$\underline{2.09}$</td><td>$\underline{2.03}$</td></tr>
<tr><td>$\Gamma_{8v}\rightarrow L_{6c}$</td><td></td><td>$\underline{1.91}$</td><td>$\underline{2.80}$</td><td>$\underline{2.91}$</td></tr>
<tr><td>$L_{6c}\rightarrow X_{6c}$</td><td></td><td>$-0.69$</td><td>$-0.71$</td><td>$-0.88$</td></tr>
<tr><td>$X_{6c}\rightarrow X_{7c}$</td><td></td><td>0.87</td><td></td><td>1.07</td></tr>
<tr><td colspan="5">aUnless noted, Ref. 24.</td></tr>
<tr><td colspan="5">bRef. 25.</td></tr>
<tr><td colspan="5">cRef. 26.</td></tr>
<tr><td colspan="5">dRef. 27.</td></tr>
</tbody></table>

sults, and quasiparticle results reflecting a LDA treatment of core-valence interactions. All theoretical results include core-relaxation effects. Excepting minor revisions, results were briefly reported previously.²⁰ Present results include small corrections for AlAs, because of a previous error in constructing the Al CPP. Core-relaxation effects are now in- cluded for Si. Core-relaxation effects have changed by per- cents of 1 eV because of choices of full-potential work cited, and some notational errors are corrected. Below, we empha- size effects of treatment LDA or CPP of core-valence in- teractions.

There are minor effects in Si, and both treatments yield accurate quasiparticle results. Note that, when computing the $s^{2}p^{2}(^{3}P)\rightarrow sp^{3}(^{5}S)$ promotion in atomic Si using CPP- enhanced, valence-only configuration-interaction, $V_{e-e}$ facili tates effective screening by the core of valence-valence ex- change, improving agreement with experiment by $\sim 0.2$ eV.¹⁷ Thus this work tests some but not all important aspects of core-valence interactions.

In Ge, the present results substantially improve $\Gamma_{8v}\rightarrow\Gamma_{6c}$ and $\Gamma_{8v}\rightarrow X_{5c}$. Only CPP-based results predict a conduction-band minimum at L, giving the correct ordering for closely spaced conduction-band valleys. Regarding $\Gamma_{8v}\rightarrow X_{5c}$, the experimental value cited in Ref. 5 1.3 eV is derived from direct and inverse photoelectron spectroscopy. A more reliable value for $\Gamma_{8v}\rightarrow X_{5c}$ may be inferred from the behavior of the $\Delta$-line minimum in Si-Ge alloys.²⁵ This minimum, known for up to 85% Ge, may be extrapolated to pure Ge. Then, one must extrapolate to X, giving an energy 0.15 eV higher than the $\Delta$ minimum, with an uncertainty of percents of 1 eV. This final number agrees very well with empirical pseudopotential results,⁴⁷ which generally are very reliable.

In GaAs, the present approach improves $\Gamma_{8v}\rightarrow\Gamma_{6c}$, $X_{6c}\rightarrow X_{7c}$, and $L_{6c}\rightarrow X_{6c}$ transitions considerably, while re- maining numbers are comparable in accuracy to those found using a LDA treatment of core-valence interactions. We dis- cussed earlier the atomic origin of the difficulties with the above three transitions. The $\Gamma_{8v}\rightarrow\Gamma_{7c},\Gamma_{8c}$ transition is also affected by core-relaxation effects, though not as much as is the $\Gamma_{8v}\rightarrow\Gamma_{6c}$ transition.

In AlAs, $\Gamma_{8v}\rightarrow\Gamma_{6c}$ is improved, with other transitions being nearly as accurate. A dependence of quasiparticle re- sults for AlAs on the treatment of core-valence interactions occurs for analogous reasons as in GaAs, but on a smaller scale. We discount the experimental value for the

conduction-band valley at $L$, as it was only obtained from
extrapolations based on data for $\mathrm{Al}_{x} \mathrm{Ga}_{1-x} \mathrm{As}$ alloys. $^{48}$

## V. DISCUSSION

There is a 10% increase in computational requirements when core-polarization effects are incorporated into quasi-particle codes. About 75% of the computational resources are devoted to evaluating the valence, Lindhard polarizabil-ity. There is about a 50% enhancement of computation time for the rest of the calculations. Calculations in this work required about 150 h total on an IBM RS 6000/550, $^{49}$ but results for the coarse Brillouin-zone meshes required only about 24 h total. So quasiparticle calculations are very prac-tical for semiconductors and can be done with reasonable computational resources. Since completion of these results, we have optimized the codes substantially by accelerating convolutions using fast-Fourier-transform techniques.

The CPP scheme has so far been motivated primarily in terms of many-body core-valence interactions in isolated at-oms. Here, we also consider aspects of the CPP scheme in a solid-state context, and we present a model to estimate the CPP's effects on the self-energy, which we test in GaAs.

As a crude approximation, the matrix $(W_{C} \nu^{-1}-1)$ acts like a scalar,
$$-x \equiv-\frac{4 \pi}{\Omega_{C}} \sum_{J} \alpha_{J},\qquad(30)$$
where $J$ runs over atoms in a unit cell. The "expansion co-efficient'' for effects at higher order in the polarizabilities is roughly
$$y \equiv \frac{4 \pi}{\varepsilon \Omega_{C}} \sum_{J} \alpha_{J}.\qquad(31)$$

Division by $\varepsilon$ in $y$ occurs because intercore, dipole-dipole interactions are screened, an effect obfuscated by first con-structing $\varepsilon_{C}$ and then incorporating it into $\varepsilon$. Respective val ues of $x$ and $y$ are about 0.07 and 0.007 in GaAs, the mate rial with the greatest core polarizability in this work, and so effects beyond first order in $\alpha$'s are small.

Consider now the self-energy operator for a valence elec-tron, approximated by
$$\Sigma=+i G W.\qquad(32)$$

In this terse notation, and neglecting effects beyond $G W$, we have
$$G=G_{C}+G_{V}+G_{U} \equiv G_{C}+G^{\prime},$$

$$W=W_{C}+W_{C} \chi_{V} W_{C} \equiv \nu+W^{\prime}+W_{C} \chi_{V} W_{C}.\qquad(33)$$

$G_{C}, G_{V}$, and $G_{U}$ sum over core, occupied valence, and empty states, respectively, giving
$$\begin{aligned}
G W= & G_{C} \nu+G_{C} W^{\prime}+G^{\prime} \nu+G^{\prime} W^{\prime}+G^{\prime} W_{C} \chi_{V} W_{C} \\
& +G_{C} W_{C} \chi_{V} W_{C}.
\end{aligned}\qquad(34)$$

Denoting the six terms on the right-hand side as "term 1'' through "term 6,'' one may consider how well each term is included in the CPP approach.

Term 1 is included in a Hartree-Fock treatment of core-valence interactions. Term 2 is included as part of the effects of $V_{e}$. Term 3 is included as part of $\Sigma_{x}$. If there were only one valence electron in a system, term 4 would constitute the remainder of the effects of $V_{e}$. For more than one valence electron, some of the parts of term 4 enter only via $V_{e-e}$, as demonstrated by the approximate relation
$$\begin{aligned}
G^{\prime}\left(\mathbf{r}, \mathbf{r}^{\prime} ; E\right) \approx & G^{\prime}\left(\mathbf{r}, \mathbf{r}^{\prime} ; E\right)_{\text {no valence states occupied }} \\
& +2 \pi i \sum_{V=\text { valence states }} \Psi_{V}(\mathbf{r}) \Psi_{V}^{*}\left(\mathbf{r}^{\prime}\right) \delta\left(E-\varepsilon_{V}\right). \\
& (35)
\end{aligned}$$

Comparing this result with $V_{e-e}$ 's effects on $\Sigma_{x}$, we see that the remainder of term 4 is included correctly through $\Sigma_{x}$. Including term 5 corresponds directly to including $\Sigma_{dx}$ and $\Sigma_{coh}$. Term 6 is not included. It describes valence electrons' screening of core-valence exchange, in analogy to screening effects occurring in $\Sigma_{sex }$. Term 6 was absent in CPP enhanced, valence-only configuration-interaction calcula-tions for atomic Al, and errors in results were much smaller than the total effects of $V_{e-e}$ : typically $\sim 0.02 eV$ in inter level spacings, suggesting similar band-energy-difference er-rors. Furthermore, term 6 should provide similar contribu-tions to conduction- and valence-band energies. Phillips $^{50}$ noted that term 6 may be large in systems with shallow cores, e.g., noble metals.

The largest effects of the CPP on band energies are be-cause of $V_{e}$ and must not be confused with comparable ef fects of how one treats core-valence exchange (LDA vs Hartree-Fock). Approximately, $V_{e-e}$ leads to scaling of $\Sigma_{x}$, $\Sigma_{dx}$, and $\Sigma_{coh}$ each by a factor of $1-x$. [Still, the sum of all effects of the CPP (including $V_{e}$ ) lowers total energies of physical systems.] Because we have
$$W_{C} \approx[1-x] \nu,\qquad(36)$$
scaling of $\Sigma_{x}$ is most clear, whereas $\Sigma_{dx}$ and $\Sigma_{coh}$ are af fected by the replacement
$$\nu\left[\chi_{V}^{0} \frac{1}{1-\nu \chi_{V}^{0}}\right] \nu \rightarrow W_{C}\left[\chi_{V}^{0} \frac{1}{1-W_{C} \chi_{V}^{0}}\right] W_{C}.\qquad(37)$$

Important parts of the denominators are their second terms, because $\Sigma_{dx}$ and $\Sigma_{coh}$ weight the low-frequency $\varepsilon^{-1}$, for which the second terms are large, most heavily, suggesting that $\Sigma_{dx}$ and $\Sigma_{coh}$ would scale as the factor $(1-x)$. More explicitly, $\Sigma_{dx}$ and $\Sigma_{coh}$ emphasize the $\omega^{-1}$ moment of the imaginary part of expression (37), while the $\omega$ moment of the imaginary part of the bracketed quantity is unaffected by such a replacement. The pole frequency for a single-pole model is multiplied by a factor of $(1-x)^{1 / 2}$, a well-known result. Hence the associated pole strength changes by a factor of $(1-x)^{-1 / 2}$, and so the $\omega^{-1}$ moment of expression (37) changes by a factor of $(1-x)^{2}(1-x)^{-1}=(1-x)$. To dem onstrate this scaling, in Table V we present effects of includ-ing or omitting $V_{e-e}$ on $\Sigma_{x}, \Sigma_{dx}$ , and $\Sigma_{coh}$ in GaAs.

If $G W$ were adequate to treat systems with highly local ized atomic states, less empiricism should have been re-quired when treating core-valence interactions. However, this may not apply in other circumstances, because we have

<table>
<caption>TABLE V. Change in (parts of) self-energy, in eV, for band states in GaAs because of $V_{e-e}$, including changes in $\Sigma_{\text{x}}$, $\Sigma_{\text{dx}}$, and $\Sigma_{\text{coh}}$, and $\Sigma$=$\Sigma_{\text{x}}$+$\Sigma_{\text{dx}}$+$\Sigma_{\text{coh}}$, taken from calculations and from the simple estimate discussed in the text. The latter case is in parentheses. States are specified by crystal momentum and band index, written in small Roman numerals.</caption>
<thead>
<tr>
<th>State</th>
<th>Change in $\Sigma_{\text{x}}$</th>
<th>Change in $\Sigma_{\text{dx}}$</th>
<th>Change in $\Sigma_{\text{coh}}$</th>
<th>Change in $\Sigma$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Gamma_{\text{i}}$</td>
<td>1.49 (1.29)</td>
<td>$-1.26\left(-0.96\right)$</td>
<td>0.66 (0.52)</td>
<td>0.88 (0.85)</td>
</tr>
<tr>
<td>$\Gamma_{\text{ii}}$$\cdots$$\Gamma_{\text{iv}}$</td>
<td>1.00 (0.95)</td>
<td>$-0.92\left(-0.66\right)$</td>
<td>0.81 (0.59)</td>
<td>0.90 (0.89)</td>
</tr>
<tr>
<td>$\Gamma_{\text{v}}$</td>
<td>0.32 (0.46)</td>
<td>$-0.37\left(-0.34\right)$</td>
<td>0.99 (0.62)</td>
<td>0.94 (0.73)</td>
</tr>
<tr>
<td>$\Gamma_{\text{vi}}$$\cdots$$\Gamma_{\text{viii}}$</td>
<td>0.43 (0.36)</td>
<td>$-0.36\left(-0.26\right)$</td>
<td>0.69 (0.56)</td>
<td>0.76 (0.67)</td>
</tr>
<tr>
<td>$L_{\text{i}}$</td>
<td>1.45 (1.28)</td>
<td>$-1.23\left(-0.94\right)$</td>
<td>0.69 (0.55)</td>
<td>0.92 (0.89)</td>
</tr>
<tr>
<td>$L_{\text{ii}}$</td>
<td>1.07 (1.02)</td>
<td>$-0.93\left(-0.72\right)$</td>
<td>0.64 (0.50)</td>
<td>0.78 (0.80)</td>
</tr>
<tr>
<td>$L_{\text{iii}}$$\cdots$$L_{\text{iv}}$</td>
<td>1.00 (0.95)</td>
<td>$-0.82\left(-0.66\right)$</td>
<td>0.69 (0.57)</td>
<td>0.87 (0.86)</td>
</tr>
<tr>
<td>$L_{\text{v}}$</td>
<td>0.34 (0.41)</td>
<td>$-0.42\left(-0.29\right)$</td>
<td>0.87 (0.57)</td>
<td>0.79 (0.68)</td>
</tr>
<tr>
<td>$L_{\text{vi}}$$\cdots$$L_{\text{vii}}$</td>
<td>0.35 (0.33)</td>
<td>$-0.27\left(-0.25\right)$</td>
<td>0.59 (0.57)</td>
<td>0.68 (0.65)</td>
</tr>
<tr>
<td>$L_{\text{viii}}$</td>
<td>0.13 (0.17)</td>
<td>$-0.27\left(-0.12\right)$</td>
<td>0.67 (0.51)</td>
<td>0.54 (0.55)</td>
</tr>
<tr>
<td>$X_{\text{i}}$</td>
<td>1.43 (1.28)</td>
<td>$-1.19\left(-0.93\right)$</td>
<td>0.70 (0.56)</td>
<td>0.94 (0.92)</td>
</tr>
<tr>
<td>$X_{\text{ii}}$</td>
<td>1.14 (1.04)</td>
<td>$-0.97\left(-0.73\right)$</td>
<td>0.68 (0.51)</td>
<td>0.84 (0.81)</td>
</tr>
<tr>
<td>$X_{\text{iii}}$$\cdots$$X_{\text{iv}}$</td>
<td>0.98 (0.95)</td>
<td>$-0.80\left(-0.66\right)$</td>
<td>0.63 (0.54)</td>
<td>0.81 (0.83)</td>
</tr>
<tr>
<td>$X_{\text{v}}$</td>
<td>0.31 (0.32)</td>
<td>$-0.30\left(-0.22\right)$</td>
<td>0.59 (0.50)</td>
<td>0.60 (0.60)</td>
</tr>
<tr>
<td>$X_{\text{vi}}$</td>
<td>0.30 (0.36)</td>
<td>$-0.33\left(-0.25\right)$</td>
<td>0.67 (0.53)</td>
<td>0.64 (0.64)</td>
</tr>
<tr>
<td>$X_{\text{vii}}$$\cdots$$X_{\text{viii}}$</td>
<td>0.35 (0.28)</td>
<td>$-0.31\left(-0.25\right)$</td>
<td>0.82 (0.69)</td>
<td>0.86 (0.72)</td>
</tr>
</tbody>
</table>

sought accuracies in band-energy differences which were percents of the self-energies. The minimal empiricism used here facilitated a high degree of control in the description of core-valence interactions, potentially improving predictive capacity for other solid-state applications.

## VI. SUMMARY
We present a core-polarization-potential (CPP) approach to treat core-valence interactions in solids. The approach differs from mean-field treatments of core-valence interactions, because it deals more explicitly with dynamical effects involving fluctuating core dipoles interacting with the electric fields of fluctuating valence charge densities. By employing data from vapor-phase atomic spectra, we have obtained greater control when describing core-valence interactions than is afforded by the local-density approximation (LDA) or Hartree-Fock treatment. This improved results for theoretical quasiparticle band energies, achieving agreement with experiment of $\sim 0.1$ eV in Si, Ge, GaAs, and AlAs. This accuracy is not found if core-valence interactions are treated in the LDA, and use of atomic spectra does not hamper transferability or predictive capacity of the approach when treating solids.

It is straightforward to include core-polarization effects within a quasiparticle code. Additional required computational resources are minimal. Core-valence many-body effects are appreciable in many materials, particularly ones containing elements with shallow cores, e.g., post-transition elements. Beyond dispute, however, the most important many-body effects in solids still result from interactions within the system of valence electrons.

Analyzing the problem of electron correlations in the total system of core and valence electrons shows that most, though not all, many-body interactions involving core and valence electrons are incorporated in the present approach. Whereas it has worked well in systems studied, applicability should break down in systems with even shallower ‘‘core’’ states, e.g., II-VI compounds. Zakharov *et al.*$^{51}$ found that pseudopotential-based $GW$ calculations for these systems gave good results, also using noble-metal-cation cores. However, Ref. 51 omitted core-relaxation effects and treated core-valence interactions at a LDA level, thereby exploiting a cancellation of errors in these two effects. Rohlfing *et al.*$^{33}$

<table>
<caption>TABLE VI. Errors, in hartrees, in excited-state energies for one valence electron bound to an otherwise bare core. A positive error indicates underestimation of the binding energy. Errors are given for Hartree-Fock (HF) results, all-electron (ae), core-polarization-potential results using two forms for the $f$ functions, and pseudopotential (pp), core-polarization-potential results using the same two forms. Further details are provided in Appendix A.</caption>
<thead>
<tr>
<th>State</th>
<th>HF error</th>
<th>$\Delta_{l}$ (ae),<br>MFM</th>
<th>$\Delta_{l}$ (ae),<br>JMD</th>
<th>$\Delta_{l}^{\prime}$ (pp),<br>MFM</th>
<th>$\Delta_{l}^{\prime}$ (pp),<br>JMD</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ga($5s$)</td>
<td>0.0099</td>
<td>0.0006</td>
<td>$-0.0005$</td>
<td>$-0.0007$</td>
<td>$-0.0030$</td>
</tr>
<tr>
<td>Ga($5p$)</td>
<td>0.0078</td>
<td>0.0003</td>
<td>$-0.0004$</td>
<td>$-0.0001$</td>
<td>$-0.0010$</td>
</tr>
<tr>
<td>Ge($5s$)</td>
<td>0.0115</td>
<td>0.0010</td>
<td>$-0.0001$</td>
<td>$-0.0009$</td>
<td>$-0.0038$</td>
</tr>
<tr>
<td>Ge($5p$)</td>
<td>0.0094</td>
<td>0.0006</td>
<td>$-0.0001$</td>
<td>$-0.0001$</td>
<td>$-0.0013$</td>
</tr>
</tbody>
</table>

have treated such systems by using a much deeper core- valence partition. Their results were also of good quality. It is not yet fully established, however, how the $GW$ approxi mation may break down for systems with more localized and strongly correlated atomlike electron states.

## ACKNOWLEDGMENTS
We are indebted to R. J. Needs for suggesting reexamina- tion of the band structure of GaAs. We also benefited from discussions with E. Artacho, M. Cardona, M. L. Cohen, C. Elsässer, R. W. Godby, M. S. Hybertsen, M. Schlüter, and A. Zunger. We thank D. J. Singh for providing semirelativistic all-electron LDA band energies for Ge. This work was sup- ported by National Science Foundation Grant. No. DMR-9520554 and by the Director, Office of Energy Research, Office of Basic Energy Sciences, Materials Sciences Divi- sion of the U.S. Department of Energy under contract No. DE-AC03-76SF00098. E.L.S. was supported in part by the Miller Institute for Basic Research in Science. CRAY com- puter time was provided by the National Science Foundation at the San Diego Supercomputer Center. E.L.S. acknowl- edges collaboration with R. M. Martin on much of the back- ground work on core-valence partitioning, done in the De- partment of Physics at the University of Illinois at Urbana- Champaign under U.S. Department of Energy Contract No. DE-FG02-91ER45439, and supported in part by the John and Fannie Hertz Foundation. Part of this work was also con- ducted under the auspices of the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sci- ence, by the Lawrence Livermore National Laboratory under Contract No. W-7405-ENG-48.

## APPENDIX A
There is an infinite variety of choices for the $f$ functions in Eq. (4), and we have chosen only one. Müller, Flesch, and Meyer $^{14}$ discuss four possible choices, one of which requires other core polarizabilities besides linear, static dipole. Jeung, Malrieu, and Daudey $^{15}$ also discuss a particular shape for the $f$ functions, $r^{2}/(r^{2}+d^{2})$ , where $d$ is an adjustable parameter. We have chosen the same $f$ function as Müller et al., who made their choice in part because of the accuracy of higher- lying states in the elements studied. For element $I$ and angu lar momentum $l$ , the $f$ function depends on the ratio $r/\lambda_{l}^{(I)}$ or $r/d$ . A parameter $\lambda_{l}^{(I)}$ or $d$ is set so that this relation holds:
$$\left\langle\phi_{\nu l}\left|V_{e}\right| \phi_{\nu l}\right\rangle+\varepsilon_{\nu l}\left.\right|_{\mathrm{HF}}+R_{l}=0.\qquad(A1)$$

Here $|\phi_{\nu l}\rangle$ denotes the lowest valence state with a given $l$ , when there is one electron bound to a core. $R_{l}$ is the experi mental electron removal energy for state $|\phi_{\nu l}\rangle$ . Equation(A1) only considers first-order effects of $V_{e}$ , which consti tute about $97 \%$ of its effect.
Because of freedom in choice of $f$ functions, Eq. (A1) does not uniquely specify the description of core-valence correlation, implying uncertainty in results obtained. This motivates further justification of choice of the $f$ function and estimation of uncertainties because of the arbitrariness in that choice. The four cited $f$ functions depending only on $\alpha$ pro duce appreciably different results in tests for Ge: The three forms suggested by Müller et al. yield band-energy differ- ences consistent to within $\sim 0.01 eV$ , but the form in Jeung et al. yields quite different results, the greatest discrepancy being a zone-center gap smaller by 0.08 eV.
Above results might typify the worst-case scenario for uncertainty because of the choice of $f$ functions. However, uncertainty can be reduced by considering the quantity
$$\Delta_{l}=\left\langle\phi_{(\nu+1) l}\left|V_{e}\right| \phi_{(\nu+1) l}\right\rangle+\varepsilon_{(\nu+1) l}\left.\right|_{\mathrm{HF}}+S_{l}. \quad(\mathrm{A} 2)$$

In analogy to Eq. (A1), this applies to the second-lowest valence state with a given $l$ . $S_{l}$ is the corresponding re moval energy. Generally, $\Delta_{l}$ is not zero, because $V_{e}$ is fitted by considering the state $|\phi_{\nu l}\rangle$ , whereas $|\phi_{(\nu+1) l}\rangle$ has a dif ferent shape in the core region. $\Delta_{l}$ can be larger in pseudo potential work than all-electron work, because of the flexibil- ity in shapes of pseudovalence wave functions, which results from a lack of need for orthogonality to core orbitals and is motivated by Wentzel-Kramers-Brillouin $^{52}$ arguments.
In pseudopotential results, one must distinguish pseudo- potential errors (given by differences in values obtained for  (v+1)Z|HF in Hartree-Fock all-electron vs Hartree-Fock pseudopotential calculations) and errors involved in model- ing core-valence correlation. The former errors involve an energy dependence of the pseudopotential scattering proper-ties; the latter involve an energy dependence of effects of $V_{e}$  on scattering properties (cf. Ref. 53). For pseudopotential-based work, we suggest estimating errors associated with $V_{e}$  alone using the mixed expression
$$\begin{aligned}
\Delta_{l}^{\prime}= & \left\langle\phi_{(\nu+1) l}\left|V_{e}\right| \phi_{(\nu+1) l}\right\rangle\left.\right|_{\text {pseudopotential }} \\
& +\left.\varepsilon_{(\nu+1) l}\right|_{\mathrm{HF}, \text { all electron }}+S_{l}.
\end{aligned}\qquad(A3)$$

In Table VI, results are given for $l=0$ and $l=1$ states in atomic Ga and Ge. Less important $5 d$ states lie above core shake-up thresholds, and so describing them is more compli- cated. Our choice of $f$ function is labeled "MFM," and that from Jeung et al., "JMD."" Salient results are in the last two columns and justify our choice of $f$ functions because of small $\Delta_{l}^{\prime}$ 's for states $\{|\phi_{(\nu+1) l}\rangle\}$ . Remaining arbitrariness in f functions should affect the band-energy differences by a percent of 1 eV, and correcting such arbitrariness would likely increase zone-center gaps in Ge and GaAs.

## APPENDIX B
Our Ewald-Kornfeld sums, unconventional because of crystal momentum q, also include both direct- and reciprocal-space sums. $^{54}$ Having $q$ modifies direct-space sums by introducing phase factors, and reciprocal-space sums involve different discrete vectors Q's instead of G's, the former being the latter plus q. We have
$$\begin{aligned}
\int_{C} d^{3} r e^{-i \mathbf{Q} \cdot \mathbf{r}} \sum_{\mathbf{R}} e^{i \mathbf{q} \cdot \mathbf{R}} F(\mathbf{r}-\mathbf{R})= & \int_{C} d^{3} r \sum_{\mathbf{R}} e^{-i \mathbf{Q} \cdot(\mathbf{r}-\mathbf{R})} \\
& \times F(\mathbf{r}-\mathbf{R}) \\
= & \int d^{3} r e^{-i \mathbf{Q} \cdot \mathbf{r}} F(\mathbf{r}). \\
& \text { (B1) }
\end{aligned}$$

The first two integrations run over a unit cell, and the last integral runs over all space. $F$ decays rapidly at long range. The $\mathbf{R}$'s are real-space lattice vectors, and we exploited equality of $e^{i \mathbf{q} \cdot \mathbf{R}}$ and $e^{i \mathbf{Q} \cdot \mathbf{R}}$. Using Ewald-Kornfeld sums, we find

$$
\begin{aligned}
K_{I i, J j}= & \frac{\delta_{I i, J j}}{\alpha_{I}}-\left[\sum_{\mathbf{R}}\left(1-\delta_{\mathbf{R}, 0} \delta_{I J}\right) e^{i \mathbf{q} \cdot \mathbf{R}}\left[\frac{\partial^{2}}{\partial \Delta_{i} \partial \Delta_{j}}\right.\right. \\
& \left.\left.\times \frac{\operatorname{erfc}(\sqrt{\eta}|\Delta|)}{|\Delta|}\right]\right|_{\Delta=\mathbf{R}+\tau_{J}-\tau_{I}}+\frac{4 \pi \delta_{I i, J j}}{3}\left(\frac{\eta}{\pi}\right)^{3 / 2} \\
& \left.-\sum_{\mathbf{Q}} \frac{4 \pi}{\Omega_{C}}\left(\frac{Q_{i} Q_{j}}{Q^{2}}\right) e^{-Q^{2} / 4 \eta-i \mathbf{Q} \cdot\left(\tau_{J}-\tau_{I}\right)}\right]. \quad \text { (B2) }
\end{aligned}
$$

Everything above is independent of crystal symmetry, but when atoms have tetrahedral or cubic site symmetry, the Clausius-Mossotti formula result holds for $\mathbf{q} \rightarrow 0$, which is shown as follows. We may write the above result in shorthand as

$$
K=\alpha^{-1}-M=(1-M \alpha) \alpha^{-1} \quad \text { (B3) }
$$

or

$$
K^{-1}=\alpha(1-M \alpha)^{-1} . \quad \text { (B4) }
$$

We also have

$$
\frac{1}{\varepsilon_{C M}}=1-\frac{4 \pi}{\Omega_{C}} \sum_{I i} \sum_{J j} \frac{q_{i} q_{j}}{q^{2}} K_{I i, J j}^{-1} .
$$

where the scalar $\varepsilon_{C M}$ is the macroscopic, longitudinal $\varepsilon_{C}$. Let us think of $(1-M \alpha)^{-1}$ as a $3 N \times 3 N$ matrix, for $N$ atoms per unit cell, acting on a vector $\mathbf{h}$, where $h_{I i}=q_{i} / q$. This gives

$$
\frac{1}{\varepsilon_{\mathrm{CM}}}=1-\frac{4 \pi}{\Omega_{C}} \sum_{I i} h_{I i}^{*}\left[\alpha(1-M \alpha)^{-1} \mathbf{h}\right]_{I i} . \quad \text { (B6) }
$$

The real-space sum in $M$ vanishes as $\eta$ grows large, and $M$ does not depend on $\eta$, and so choosing very large $\eta$ yields

$$
\begin{aligned}
(M \alpha \mathbf{h})_{I i}= & +\frac{4 \pi}{3}\left(\frac{\eta}{\pi}\right)^{3 / 2} \alpha_{I} \frac{q_{i}}{q}-\sum_{j} \frac{q_{j}}{q} \\
& \times \sum_{\mathbf{Q}} \sum_{J} \frac{4 \pi}{\Omega_{C}} \frac{Q_{i} Q_{j}}{Q^{2}} \alpha_{J} e^{-Q^{2} / 4 \eta-i \mathbf{Q} \cdot\left(\tau_{J}-\tau_{I}\right)} .
\end{aligned}
$$

For appropriate symmetry, sums over $\mathbf{Q}$ and $J$ simplify at small $\mathbf{q}$. The phased Gaussian factor, summed over $J$'s for each site type, is a Fourier component of a sum of Gaussians at such sites. Such components have at least tetrahedral symmetry in reciprocal space, rendering the sum unaffected by this substitution before summation: For all $\mathbf{Q} \neq \mathbf{q}$, replace

$$
\frac{Q_{i} Q_{j}}{Q^{2}} \rightarrow \frac{1}{3} \delta_{i j} . \quad \text { (B8) }
$$

We may therefore write

$$
\begin{aligned}
(M \alpha \mathbf{h})_{I i}= & +\frac{4 \pi}{3}\left(\frac{\eta}{\pi}\right)^{3 / 2} \alpha_{I} \frac{q_{i}}{q}-\frac{q_{i}}{q} \sum_{J} \frac{4 \pi}{\Omega_{C}} \alpha_{J} \\
& -\frac{q_{i}}{q} \sum_{\mathbf{Q} \neq \mathbf{q}} \sum_{J} \frac{4 \pi}{3 \Omega_{C}} \alpha_{J} e^{-Q^{2} / 4 \eta-i \mathbf{Q} \cdot\left(\tau_{J}-\tau_{I}\right)} .
\end{aligned}
$$

This may be written equivalently as

$$
\begin{aligned}
(M \alpha \mathbf{h})_{I i}= & -\frac{2}{3} \frac{q_{i}}{q} \sum_{J} \frac{4 \pi}{\Omega_{C}} \alpha_{J}+\frac{4 \pi}{3}\left(\frac{\eta}{\pi}\right)^{3 / 2} \alpha_{I} \frac{q_{i}}{q} \\
& -\frac{q_{i}}{q} \sum_{\mathbf{Q}} \sum_{J} \frac{4 \pi}{3 \Omega_{C}} \alpha_{J} e^{-Q^{2} / 4 \eta-i \mathbf{Q} \cdot\left(\tau_{J}-\tau_{I}\right)} .
\end{aligned}
$$

The second and third terms cancel, and so $\mathbf{h}$ is an eigenvector of $M \alpha$, with eigenvalue

$$
-\frac{2}{3} \frac{4 \pi}{\Omega_{C}} \sum_{J} \alpha_{J} . \quad \text { (B11) }
$$

Applying this result to Eq. (B6) yields the Clausius-Mossotti result.

## APPENDIX C

For evaluating $\Sigma$, zone integration near the zone center is discussed for cases without CPP's in Refs. 5 and 6. Here changes are needed, because $W_{C}$ differs from $\nu$. For $\Sigma_{\mathrm{x}}$, one needs $\left(W_{C} \nu^{-1}\right)_{\mathbf{G}, \mathbf{G}^{\prime}}$ for $\mathbf{q} \rightarrow 0$. Because $K$ and the $\Theta$ functions depend on the $\mathbf{q}$'s direction, angular averaging is needed, and 18 spherical integration points suffice. ${ }^{55}$ Denoting the angular average of quantity $A$ by $\langle A\rangle_{\Omega}$, for $\mathbf{q} \rightarrow 0$, $\mathbf{G} \neq 0, \mathbf{G}^{\prime} \neq 0$, we have

$$
\begin{aligned}
\left\langle\left(W_{C} \nu^{-1}\right)_{\mathbf{G}, \mathbf{G}^{\prime}}\right\rangle_{\Omega}= & \delta_{\mathbf{G}, \mathbf{G}^{\prime}}-\frac{G^{\prime}}{G} \sum_{I i} \sum_{J j} \Theta_{I i}(G) \\
& \times\left\langle K_{I i, J j}^{-1}\right\rangle_{\Omega} \Theta_{J j}^{*}\left(G^{\prime}\right),
\end{aligned}
$$

whereas, for $\mathbf{q} \rightarrow 0, \mathbf{G}=0, \mathbf{G}^{\prime}=0$, we have

$$
\left\langle\left(W_{C} \nu^{-1}\right)_{\mathbf{G}, \mathbf{G}^{\prime}}\right\rangle_{\Omega}=1-\sum_{I i} \sum_{J j} \frac{4 \pi}{\Omega_{C}}\left\langle\frac{q_{i} q_{j}}{q^{2}} K_{I i, J j}^{-1}\right\rangle_{\Omega} .
$$

Symmetry ensures self-cancellation for other matrix elements of $\left(W_{C} \nu^{-1}\right)_{\mathbf{G}, \mathbf{G}^{\prime}}$.

Regarding $\Sigma_{\mathrm{dx}}$ and $\Sigma_{\mathrm{coh}}$, we have only evaluated the angular averages of the $\omega^{-1}$ and $\omega$ moments of the matrix elements of $\varepsilon_{2}^{-1}$, neglecting further, complicated effects of covariance of the moments. This approximation is validated by convergence of results with respect to zone sampling. Equations (C1) and (C2) describe frequency-independent parts of $\varepsilon^{-1}$, which are subtracted from $\varepsilon^{-1}$ to obtain the $\omega^{-1}$ moment, and so angular averaging of $\varepsilon_{C}^{-1}$ facilitates averaging of this moment. (As in Ref. 5, the total $\varepsilon^{-1}$ is explicitly angle averaged.)

For the $\omega$ moment of $\varepsilon_{2}^{-1}$, one needs to average changes because of core polarization, i.e., modifications of the effective $\Omega^{2}$ matrix,

$$
\begin{aligned}
& \left(W_{C} \nu^{-1}-1\right) \Omega^{2}+\Omega^{2}\left(W_{C} \nu^{-1}-1\right) \\
& +\left(W_{C} \nu^{-1}-1\right) \Omega^{2}\left(W_{C} \nu^{-1}-1\right),
\end{aligned}
\tag{C3}
$$

written in shorthand. The $\Omega^{2}$ matrix is from Ref. 5,
$$
\Omega_{\mathbf{G}, \mathbf{G}^{\prime}}^{2}(\mathbf{q})=\frac{\mathbf{Q} \cdot \mathbf{Q}^{\prime}}{Q^{2}} \frac{\rho\left(\mathbf{Q}-\mathbf{Q}^{\prime}\right)}{\rho(0)} \omega_{p}^{2},
\tag{C4}
$$
$\omega_{p}$ being the classical valence plasma frequency. Even for $N=2$ atoms per unit cell, evaluating the third term is difficult, and so we neglect it, yielding only a $\sim 2$-meV error in band-energy differences for our coarse meshes, and a smaller error for our fine meshes.

The first two terms are related by symmetry, and so we give angle-averaged results for
$$
\sum_{\mathbf{K}}\left(W_{C} \nu^{-1}-1\right)_{\mathbf{G}, \mathbf{K}} \Omega_{\mathbf{K}, \mathbf{G}^{\prime}}^{2}.
\tag{C5}
$$

Deriving these only requires applying knowledge about $\varepsilon_{C}^{-1}$ for $\mathbf{q} \rightarrow 0$ from any direction. One needs results only for matrix elements of $\varepsilon^{-1}$ with $\mathbf{G}=0, \mathbf{G}^{\prime}=0$, when one has

$$
\begin{aligned}
- & \sum_{\mathbf{K} \neq 0} \sum_{I i} \sum_{J j} \sum_{k}\left(\frac{4 \pi}{\Omega_{C}}\right)^{1 / 2} \Theta_{J j}^{*}(\mathbf{K}) \frac{K_{k}}{K}\left\langle\frac{q_{i} q_{k}}{q^{2}} K_{I i, J j}^{-1}\right\rangle_{\Omega} \\
& \times \frac{\rho(\mathbf{K})}{\rho(0)} \omega_{p}^{2}-\frac{4 \pi}{\Omega_{C}} \sum_{I i} \sum_{J j}\left\langle\frac{q_{i} q_{j}}{q^{2}} K_{I i, J j}^{-1}\right\rangle_{\Omega} \omega_{p}^{2},
\end{aligned}
\tag{C6}
$$

or with $\mathbf{G} \neq 0, \mathbf{G}^{\prime} \neq 0$, when one has

$$
\begin{aligned}
- & \frac{G^{\prime}}{G} \sum_{\mathbf{K} \neq 0} \sum_{I i} \sum_{J j} \sum \Theta_{I i}(\mathbf{G}) \Theta_{J j}^{*}(\mathbf{K}) \\
\times & \left\langle K_{I i, J j}^{-1}\right\rangle_{\Omega}\left(\frac{\mathbf{K} \cdot \mathbf{G}^{\prime}}{K G^{\prime}}\right) \frac{\rho\left(\mathbf{K}-\mathbf{G}^{\prime}\right)}{\rho(0)} \omega_{p}^{2} \\
- & \frac{G^{\prime}}{G} \sum_{I i} \sum_{J j} \sum_{k} \Theta_{I i}(\mathbf{G}) \\
\times & \left(\frac{4 \pi}{\Omega_{C}}\right)^{1 / 2}\left\langle\frac{q_{i} q_{k}}{q^{2}} K_{I i, J j}^{-1}\right\rangle_{\Omega} \frac{G_{k}^{\prime}}{G^{\prime}} \frac{\rho\left(-\mathbf{G}^{\prime}\right)}{\rho(0)} \omega_{p}^{2}.
\end{aligned}
\tag{C7}
$$

$^{1}$D. R. Hamann, M. Schlüter, and C. Chiang, Phys. Rev. Lett. 43, 1494 (1979).
$^{2}$D. Vanderbilt, Phys. Rev. B 32, 8412 (1985).
$^{3}$P. C. Hohenberg and W. L. Kohn, Phys. Rev. 136, B864 (1964); W. L. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).
$^{4}$L. Hedin and S. Lundqvist, in *Solid State Physics*, edited by H. Ehrenreich, F. Seitz, and D. Turnbull (Academic, New York, 1969), Vol. 23, p. 1.
$^{5}$M. S. Hybertsen and S. G. Louie, Phys. Rev. Lett. 56, 1418 (1985); M. S. Hybertsen and S. G. Louie, Phys. Rev. B 34, 5390 (1986).
$^{6}$R. W. Godby, M. Schlüter, and L. J. Sham, Phys. Rev. Lett. 56, 2415 (1986); R. W. Godby, M. Schlüter, and L. J. Sham, Phys. Rev. B 37, 10 159 (1988).
$^{7}$S. B. Zhang, D. Tománek, M. L. Cohen, S. G. Louie, and M. S. Hybertsen, Phys. Rev. B 40, 3162 (1989).
$^{8}$X. Zhu and S. G. Louie, Phys. Rev. B 43, 14 142 (1991).
$^{9}$G. B. Bachelet, D. R. Hamann, and M. Schlüter, Phys. Rev. B 26, 4199 (1982).
$^{10}$S. Fahy, X. W. Wang, and S. G. Louie, Phys. Rev. Lett. 61, 1631 (1989); Phys. Rev. B 42, 3503 (1990).
$^{11}$E. L. Shirley, R. M. Martin, G. B. Bachelet, and D. M. Ceperley, Phys. Rev. B 42, 5057 (1990).
$^{12}$L. Mitáš, E. L. Shirley, and D. M. Ceperley, J. Chem. Phys. 95, 3467 (1991).
$^{13}$X. P. Li, D. M. Ceperley, and R. M. Martin, Phys. Rev. B 44, 10 929 (1991).
$^{14}$W. Müller, J. Flesch, and W. Meyer, J. Chem. Phys. 80, 3297 (1984).
$^{15}$G. H. Jeung, J. P. Malrieu, and J. P. Daudey, J. Chem. Phys. 77, 3571 (1982).
$^{16}$E. L. Shirley, L. Mitáš, and R. M. Martin, Phys. Rev. B 44, 3395 (1991).
$^{17}$E. L. Shirley and R. M. Martin, Phys. Rev. B 47, 15 404 (1993); 47, 15 413 (1993).
$^{18}$E. L. Shirley, Ph.D. thesis, University of Illinois at UrbanaChampaign, 1991.
$^{19}$M. Born and W. Heisenberg, Z. Phys. 23, 388 (1924).
$^{20}$E. L. Shirley, X. Zhu, and S. G. Louie, Phys. Rev. Lett. 69, 2955 (1992).
$^{21}$J. J. Quinn and R. A. Ferrell, Phys. Rev. 112, 812 (1958); L. Hedin, ibid. 139, A796 (1965).
$^{22}$G. B. Bachelet and N. E. Christensen, Phys. Rev. B 31, 879 (1985).
$^{23}$For aluminum and silicon, S. Bashkin and J. O. Stoner, Jr., *Atomic Energy Levels and Grotian Diagrams* (North-Holland, New York, 1975 and 1978), Vols. I and II; for arsenic, A. N. Ryabtsev, J. F. Wyart, and Th. A. M. van Kleef, Phys. Scr. 30, 407 (1984).
$^{24}$*Crystal and Solid State Physics*, Vol. 17A of *Landolt-Börnstein, Numerical Data and Functional Relationships in Science and Technology*, edited by O. Madelung (Springer, Berlin, 1984).
$^{25}$Extrapolated using band calculations plus finite temperature corrections from known $\Delta$-line minimum in Si-Ge alloys: R. Braunstein, A. R. Moore, and F. Herman, Phys. Rev. 109, 695 (1958).
$^{26}$R. Hulthen and N. G. Nilsson, Solid State Commun. 18, 1341 (1976).
$^{27}$D. Straub, L. Ley, and F. J. Himpsel, Phys. Rev. Lett. 54, 142 (1985).
$^{28}$B. I. Min, S. Massidda, and A. J. Freeman, Phys. Rev. B 38, 1970 (1988).
$^{29}$H. Krakauer, S.-H. Wei, B. M. Klein, and C. S. Wang, Bull. Am. Phys. Soc. 29, 391 (1984).
$^{30}$N. Hamada, M. Hwang, and A. J. Freeman, Phys. Rev. B 41, 3620 (1990).
$^{31}$S.-H. Wei and A. Zunger, Phys. Rev. B 39, 3279 (1989).
$^{32}$D. J. Singh (private communication).

$^{33}$M. Rohlfing, P. Krüger, and J. Pollman, Phys. Rev. B $\mathbf{48}$, 17 791 (1993).

$^{34}$F. Bechstedt, R. Delsole, G. Cappelini, and L. Reining, Solid State Commun. $\mathbf{84}$, 765 (1992); J. Q. Wang, Z. Q. Gu, and M. F. Li, Phys. Rev. B $\mathbf{44}$, 8707 (1991); J. Q. Wang, Z. Q. Gu, B. S. Wang, and M. F. Li, Commun. Theor. Phys. $\mathbf{15}$, 169 (1991).

$^{35}$H. S. Greenside and M. Schlüter, Phys. Rev. B $\mathbf{28}$, 535 (1983).

$^{36}$G. P. Kerker, J. Phys. C $\mathbf{13}$, L189 (1980).

$^{37}$A. M. Rappe, K. M. Rabe, E. Kaxiras, and J. D. Joannopoulos, Phys. Rev. B $\mathbf{41}$, 1227 (1990).

$^{38}$N. Troullier and J. L. Martins, Phys. Rev. B $\mathbf{43}$, 1993 (1991); Solid State Commun. $\mathbf{74}$, 613 (1990).

$^{39}$M. Krauss and W. J. Stevens, Annu. Rev. Phys. Chem. $\mathbf{35}$, 357 (1984).

$^{40}$See, for instance, L. J. Sham, Phys. Rev. B $\mathbf{32}$, 3876 (1985), and references therein.

$^{41}$S. L. Adler, Phys. Rev. $\mathbf{126}$, 413 (1962); N. Wiser, ibid. $\mathbf{129}$, 62 (1963).

$^{42}$P. P. Ewald, Ann. Phys. (Leipzig) $\mathbf{64}$, 253 (1921).

$^{43}$D. J. Chadi and M. L. Cohen, Phys. Rev. B $\mathbf{8}$, 5747 (1973); H. J. Monkhorst and J. D. Pack, ibid. $\mathbf{13}$, 5188 (1976).

$^{44}$D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. $\mathbf{45}$, 566 (1980).

$^{45}$J. Perdew and A. Zunger, Phys. Rev. B $\mathbf{23}$, 5048 (1981).

$^{46}$S. G. Louie, S. F. Froyen, and M. L. Cohen, Phys. Rev. B $\mathbf{26}$, 1738 (1982).

$^{47}$M. L. Cohen and J. R. Chelikowsky, *Electronic Structure and Optical Properties of Semiconductors* (Springer, New York, 1988).

$^{48}$These results are tabulated in Ref. 24.

$^{49}$Certain commercial equipment, instruments, or materials are identified in this paper to foster understanding. Such identification does not imply recommendation or endorsement by the National Institute of Standards and Technology, nor does it imply that the materials or equipment identified are necessarily the best available for the purpose.

$^{50}$J. C. Phillips, Phys. Rev. $\mathbf{123}$, 420 (1961).

$^{51}$O. Zakharov, A. Rubio, X. Blase, M. L. Cohen, and S. G. Louie, Phys. Rev. B $\mathbf{50}$, 10 780 (1994).

$^{52}$H. A. Kramers, Z. Phys. $\mathbf{39}$, 828 (1926).

$^{53}$E. L. Shirley, D. C. Allan, R. M. Martin, and J. D. Joannopoulos, Phys. Rev. B $\mathbf{40}$, 3652 (1989).

$^{54}$C. Kittel, *Introduction to Solid State Physics*, 6th ed. (Wiley, New York, 1986).

$^{55}$*Handbook of Mathematical Functions*, edited by M. Abramowitz and I. A. Stegun (Dover, New York, 1965).