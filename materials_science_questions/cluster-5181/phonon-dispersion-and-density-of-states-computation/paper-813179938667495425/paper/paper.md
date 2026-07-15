![](./images/813179938667495425_1.jpg)

Atomistic force field for alumina fit to density functional theory

Joanne Sarsam, Michael W. Finnis, and Paul Tangney

Citation: *The Journal of Chemical Physics* **139**, 204704 (2013); doi: 10.1063/1.4832695
View online: http://dx.doi.org/10.1063/1.4832695
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/139/20?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
[A density functional theory study of structural, mechanical and electronic properties of crystalline phosphorus pentoxide](https://aip.scitation.org/doi/10.1063/1.3666017)
J. Chem. Phys. **135**, 234513 (2011); 10.1063/1.3666017

[High pressure, mechanical, and optical properties of ZrW₂O₈](https://aip.scitation.org/doi/10.1063/1.3544487)
J. Appl. Phys. **109**, 033510 (2011); 10.1063/1.3544487

[Quantum mechanics based force field for carbon (QMFF-Cx) validated to reproduce the mechanical and thermodynamics properties of graphite](https://aip.scitation.org/doi/10.1063/1.3456543)
J. Chem. Phys. **133**, 134114 (2010); 10.1063/1.3456543

[Density functional theory study of 3R- and 2H-CuAlO₂ under pressure](https://aip.scitation.org/doi/10.1063/1.3499659)
Appl. Phys. Lett. **97**, 141917 (2010); 10.1063/1.3499659

[Nonreactive molecular dynamics force field for crystalline hexahydro-1,3,5-trinitro-1,3,5 triazine](https://aip.scitation.org/doi/10.1063/1.2176621)
J. Chem. Phys. **124**, 104508 (2006); 10.1063/1.2176621

![](./images/813179938667495425_2.jpg)

# Atomistic force field for alumina fit to density functional theory

Joanne Sarsam,¹,² Michael W. Finnis,¹,²,³ and Paul Tangney¹,²,³,a)
¹Department of Materials, Imperial College London, London SW7 2AZ, United Kingdom
²Thomas Young Centre, Imperial College London, London SW7 2AZ, United Kingdom
³Department of Physics, Imperial College London, London SW7 2AZ, United Kingdom

(Received 17 July 2013; accepted 6 November 2013; published online 25 November 2013)

We present a force field for bulk alumina ($\text{Al}_2\text{O}_3$), which has been parametrized by fitting the energies, forces, and stresses of a large database of reference configurations to those calculated with density functional theory (DFT). We use a functional form that is simpler and computationally more efficient than some existing models of alumina parametrized by a similar technique. Nevertheless, we demonstrate an accuracy of our potential that is comparable to those existing models and to DFT. We present calculations of crystal structures and energies, elastic constants, phonon spectra, thermal expansion, and point defect formation energies. © 2013 AIP Publishing LLC.
[http://dx.doi.org/10.1063/1.4832695]

## I. INTRODUCTION

Alumina ($\text{Al}_2\text{O}_3$) is a material of great practical and theoretical importance. Its high hardness, strength, and melting point, combined with its low electrical conductivity and its resistance to corrosion and abrasion make it useful in a variety of applications. These include electronics and optics, as an industrial ceramic, as a catalyst, and catalyst support.¹ An exposed aluminium-containing alloy will oxidize to form a protective scale, and hence there is much industrial interest in the study of these alumina coatings. Alumina is also a major component of the Earth’s crust and mantle, and, as such, a good understanding of it is needed at extremes of temperature and pressure as well as at ambient conditions.

Alumina can exist in many crystalline polymorphs at ambient conditions²,³ and at high pressures the number is greater still.⁴,⁵ At low pressures, the crystal structures can be divided into two groups based on the structure of the oxygen sublattice: those whose oxygens are nearly in a hexagonal close packed (hcp) arrangement and those whose oxygens are close to a face centered cubic arrangement. Different polymorphs within each group differ in how the aluminium cations are arranged. The thermodynamically stable phase is corundum ($\alpha$-alumina), which has a 10 atom trigonal (rhombohedral) primitive cell of space group $R\overline{3}c$, consisting of a hcp oxygen sublattice with aluminium atoms occupying two-thirds of the octahedral interstices. The metastable structures are often referred to as transition aluminas because they are formed by heating the crystalline aluminium hydroxide minerals found in bauxite, which is aluminium’s principal ore. Heating causes dehydroxylation and, at sufficiently high temperatures ($\sim1100^\circ\text{C}$), corundum is formed. However, before $\alpha-\text{Al}_2\text{O}_3$ is formed, the alumina typically passes through a sequence of metastable phases as temperature is increased.²,³ In most cases, the final transformation in the sequence is either from $\theta-\text{Al}_2\text{O}_3$ or $\kappa-\text{Al}_2\text{O}_3$, which are almost certainly the lowest energy crystal structures among the transition aluminas. There is still debate about the precise structures of several of the transition aluminas, including $\gamma-\text{Al}_2\text{O}_3$, which is a member of the fcc oxygen sublattice group, and which is very important industrially as a heterogeneous catalyst.²,⁶⁻⁸

Atomistic simulations can contribute a great deal to our understanding of alumina in a range of contexts and physical conditions. However, the lynchpin of any atomistic simulation is the model used to describe bonding. Alumina has often been thought of as a predominantly ionic material; however, as with most oxides, many-body interactions are important.

Existing shell models⁹ incorrectly predict that the ground state of alumina has a C-type lanthanum oxide (bixbyite) structure, even though this phase has never been observed experimentally. It has been claimed that the corundum structure can only be stabilized with respect to bixbyite by including an induced-quadrupole term in the potential energy function.¹⁰

The current “gold standard” amongst alumina potentials are those of Jahn, Madden and Wilson.¹¹ Their potentials are fit to density functional theory (DFT) data, and account for breathing and dipolar and quadrupolar distortions of ions. However, their model contains a large number of extra degrees of freedom per ion which can have a significant impact on computational efficiency. Our aim is to create a faster, simpler potential that still captures enough of the essential physics of the system to be comparable in accuracy to the potentials of Jahn *et al.* Our primary interest is in the industrial applications of alumina, particularly corundum, and therefore our goal is to make a potential whose parameters are optimized for this phase at low pressures.

In this work, we present a force field for alumina that has been parametrized from *ab initio* calculations performed at high temperature. We demonstrate that we are able to get the correct ground state structure without the need for quadrupolar distortions. We test the accuracy of our potential by calculating equilibrium lattice parameters, thermal expansion, elastic constants, and phonons for the corundum phase and comparing them both to experimental data and to

a)E-mail: p.tangney@imperial.ac.uk

$\Gamma$ is minimized with respect to the set of parameters $\{\eta\}$ using Powell minimization. $^{20}$ The weights used were $w_f=1.0$, $w_s=0.5$, and $w_e=0.01$. We have found, for several materials, $^{12,13}$ that the final converged values of $\Delta F$, $\Delta S$, and $\Delta E$ are reasonably insensitive to these weights. However, particularly at the beginning of the parametrization process, it is important that $w_e$ is relatively small to reflect the fact that we only have one energy for every $3N$ force components.

The final parameter set is not unique because $\Gamma(\{\eta\})$ has many local minima. As we discuss in more detail in Sec. V, by fitting all parameters simultaneously we allow the different terms in the potential to compensate for one another. However, in practice we find that the electrostatic parameters, which are the only ones with a very clear physical interpretation, turn out to be almost the same if we repeat the Powell minimization using the same DFT data but starting from a different point in parameter space. For example, the charge and polarizability of the oxygen ion are always close to $-1.5$ a.u. and 6.5 a.u., respectively.

### B. Technical details
Our potential is fit to DFT data calculated on snapshot configurations from molecular dynamics (MD) simulations of a 120-atom supercell of $\alpha$-alumina, under periodic boundary conditions. Approximately forty snapshots are used in each iteration of the fitting procedure (i.e., each update of the parameter set), and four iterations were required to converge the fit to the $ab$ initio data. Altogether, around 60 000 DFT forces, stress components, and energies, were used for parameterization, and the fit reported in Sec. IV is to an additional $\sim$15 000 DFT numbers generated after the 4th update of the parameter set and which were not used in the fitting.

Our MD simulations were started with the perfect corundum crystal structure in a $2\times2\times1$ repetition of the conventional 30-atom hexagonal unit cell. $^{21}$ Positions and velocities were initially randomized and then temperature was stabilized at 2500 K (i.e., above the experimental melting temperature of $\sim$2300 K) using a Nosè-Hoover thermostat$^{22,23}$ and the pressure was stabilized at zero using a Parrinello-Rahman barostat. $^{22,23}$ After at least 10 ps, the thermostat and barostat were detached and MD was continued in the NVE ensemble. Snapshots separated in time by at least $1-2$ ps were extracted to generate the DFT dataset of forces, stresses, and energies. In the final iteration of the parameterization process, the density in the NVE simulation was $3.62\ \text{g}\ \text{cm}^{-3}$. The crystal had not melted but contained several defects and a high level of disorder. In all MD simulations reported in this article, the time step used was 30 a. u. (0.726 fs).

All our $ab$ initio calculations are performed using the Quantum Espresso package$^{19}$ which employs pseudopotentials and a plane-wave basis set. We use a plane wave energy cutoff for the wavefunctions of 80 Ry. In our 120 atom supercell calculations, we sample the Brillouin zone using the gamma point only, but in tests with a $2\times2\times2$ $k$-point grid the forces changed by less than $0.5\%$ which is more than an order of magnitude lower than our fit, $\Delta F$. To calculate forces on our snapshots, we treated exchange and correlation (XC) within the generalized gradient approximation (GGA) of Perdew, Burke, and Ernerhof. $^{24}$ We used Vanderbilt ultrasoft pseudopotentials$^{25}$ which were generated from all-electron calculations using the local density approximation (LDA). Using different XC functionals for atomic and bulk calculations does not introduce any further approximations beyond the pseudopotential approximation and the LDA and GGA but, of course, all quantities calculated with this mix of functionals will differ from a purely LDA calculation or a purely GGA calculaton. $^{26}$ From an empirical perspective, this can often be useful because LDA has a tendency to overbind materials while GGA tends to underbind them. Therefore, using one functional to generate the pseudopotential and another in the bulk usually gives structural parameters that are intermediate between the two. In what follows, DFT calculations that use LDA for the atomic calculation and GGA for the bulk will be referred to as "LDA/GGA" in our tabulated results. For comparison, we have also performed fully-LDA and GGA calculations of many of the quantities that we report.

## IV. RESULTS
Our converged fit to the DFT results is $\Delta F=0.092$, $\Delta S=0.027$, and $\Delta E=0.112$. The parameters of the force field are listed in Table I.

### A. Crystal structures
We have performed structural relaxations of $\alpha-\text{Al}_2\text{O}_3$, $\theta-\text{Al}_2\text{O}_3$, and $\kappa-\text{Al}_2\text{O}_3$ as well as the hypothetical bixbyite structure, which has been found to be comparable in energy to $\alpha-\text{Al}_2\text{O}_3$ in a number of theoretical studies, $^{8,10,11}$ but which has not been observed experimentally.

The $\theta-\text{Al}_2\text{O}_3$ crystal structure is based on fcc packing of oxygen ions. It has a monoclinic structure with space group C2/m and 20 atoms per unit cell. Half of the Al ions are octahedrally coordinated and half are tetrahedrally coordinated. Like $\alpha-\text{Al}_2\text{O}_3$, $\kappa-\text{Al}_2\text{O}_3$is based on a hcp packing of oxygen ions. However, whereas in $\alpha-\text{Al}_2\text{O}_3$the Al atoms are sixfold coordinated, in $\kappa-\text{Al}_2\text{O}_3$ a quarter of the Al ions are tetrahedrally coordinated and three quarters are octahedrally coordinated. $\kappa-\text{Al}_2\text{O}_3$ is orthorhombic with space group $\text{Pna2}_1$ and 40 atoms per unit cell. Bixbyite (space group Ia-3) can be visualized as a fluorite structure in which one quarter of the oxygen anions have been removed and all cations are fourfold coordinated. Materials adopting the bixbyite structure, such as lanthanum oxide, typically have larger cations.

<table>
<caption>TABLE I. Force-field parameters for our potential (in atomic units).</caption>
<thead>
<tr>
<th>Parameters</th>
<th>O-O</th>
<th>Al-O</th>
<th>Al-Al</th>
</tr>
</thead>
<tbody>
<tr>
<td>$D$</td>
<td>$8.4053\times10^{-5}$</td>
<td>$1.6529\times10^{-4}$</td>
<td>$7.0675\times10^{-3}$</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>12.8778</td>
<td>13.1889</td>
<td>16.8124</td>
</tr>
<tr>
<td>$r^0$</td>
<td>7.6048</td>
<td>5.9822</td>
<td>4.0855</td>
</tr>
<tr>
<td>$b$</td>
<td>0.0</td>
<td>2.0173</td>
<td>0.0</td>
</tr>
<tr>
<td>$c$</td>
<td>0.0</td>
<td>$-1.5141$</td>
<td>0.0</td>
</tr>
<tr>
<td>$\alpha$</td>
<td>6.4484</td>
<td></td>
<td>0.0</td>
</tr>
<tr>
<td>$q$</td>
<td>$-1.47026$</td>
<td></td>
<td>2.20539</td>
</tr>
</tbody>
</table>

TABLE IV. $\theta$-alumina structural parameters for our potentials as compared to $ab$ initio calculations and experimental$^{30}$ values. The positions of unique atoms in the cell are given in scaled coordinates.

|  | Expt. | LDA | GGA | LDA/GGA | Potential |
| --- | --- | --- | --- | --- | --- |
| $a$ (au) | 22.39 | 21.67 | 22.44 | 22.05 | 21.94 |
| $b$ (au) | 5.49 | 5.34 | 5.53 | 5.42 | 5.46 |
| $c$ (au) | 10.62 | 10.33 | 10.66 | 10.47 | 10.47 |
| $\beta$ (°) | 103.8 | 104.1 | 104.0 | 104.1 | 104.1 |
| $O(x, 0, z)$ | (0.161,0.098) | (0.159,0.107) | (0.160,0.108) | (0.158,0.107) | (0.161,0.109) |
| $O(x, 0, z)$ | (0.495,0.253) | (0.494,0.257) | (0.495,0.258) | (0.495,0.258) | (0.494,0.254) |
| $O(x, 0, z)$ | (0.827,0.427) | (0.827,0.431) | (0.826,0.432) | (0.826,0.430) | (0.827,0.433) |
| $Al(x, 0, z)$ | (0.917,0.207) | (0.910,0.205) | (0.910,0.205) | (0.911,0.205) | (0.910,0.204) |
| $Al(x, 0, z)$ | (0.660,0.316) | (0.658,0.315) | (0.658,0.316) | (0.658,0.316) | (0.658,0.316) |

![](./images/813179938667495425_3.jpg)

FIG. 1. Energy as a function of volume for corundum, bixbyite, theta, and kappa phases for our potential.

TABLE V. Energy differences between metastable phases and corundum. Results are given in eV per formula unit and compared to the experimental work of Ref. 31.

|  | Expt. | LDA/GGA | LDA | GGA | Potential |
| --- | --- | --- | --- | --- | --- |
| $\alpha -$ bixbyite | $\dots$ | $-0.200$ | $-0.234$ | $-0.082$ | $-0.352$ |
| $\alpha - \theta$ | $<-0.120$ | $-0.084$ | $-0.067$ | $-0.039$ | $-0.041$ |
| $\alpha - \kappa$ | $-0.160$ | $-0.006$ | $-0.090$ | $-0.084$ | $-0.028$ |

![](./images/813179938667495425_4.jpg)

FIG. 2. Volume compression of corundum for pressures up to 150 GPa. Our potentials are compared to the two potentials$^{11}$ and experimental data.$^{35–37}$

### E. Thermodynamic properties

The Fropho software package$^{40}$ is used to calculate thermodynamic properties from the results of phonon calculations, using the quasi-harmonic approximation. Free energy, entropy, and heat capacity are all calculated for both DFT and our potential for a $3 \times 3 \times 3$ cell (270 atoms), and are presented in Figure 5. Due to the computational expense of DFT, and to compare like with like, a relatively small simulation cell was used in both calculations. There is good agreement with DFT for all three quantities.

### F. Elastic constants

Like phonon frequencies, elastic constants are very sensitive to the parameters of the potential. We use the method outlined by Holm $et$ $al.^{28}$ to determine the six independent elastic constants of corundum from energy-strain data. Our results are compared to experiment and other theoretical work in Table VII and are in good agreement overall.

The same method is used to calculate elastic constants for the $\kappa$ phase of alumina. This phase has nine independent elastic constants. Elastic constants calculated for the $\kappa$ phase are given in Table VIII.

![](./images/813179938667495425_5.jpg)

FIG. 3. Thermal volume expansion of corundum relative to $V(T=300$ K). Our potential is compared to the two potentials from Ref. 11 and experimental data.$^{39}$

TABLE VI. Our theoretical values for the screened Born effective charge tensors $Z_{\alpha \beta}/\sqrt{\epsilon_{zz}^{\infty}}$ for the $Al_2O_3$ primitive cell. For Al, the tensor is the same for all atoms by symmetry; for O, the tensor is given for the atom at $(x_0, \frac{1}{2}+x_0, \frac{1}{4})$ in the primitive cell.

<table>
  <thead>
    <tr>
      <th colspan="7">(a) Potential</th>
      <th colspan="7">(b) DFT</th>
    </tr>
    <tr>
      <th></th>
      <td colspan="3">Al</td>
      <td colspan="3">O</td>
      <th></th>
      <td colspan="3">Al</td>
      <td colspan="3">O</td>
    </tr>
    <tr>
      <th></th>
      <td>x</td>
      <td>y</td>
      <td>z</td>
      <td>x</td>
      <td>y</td>
      <td>z</td>
      <th></th>
      <td>x</td>
      <td>y</td>
      <td>z</td>
      <td>x</td>
      <td>y</td>
      <td>z</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>x</th>
      <td>1.52</td>
      <td>0.00</td>
      <td>$-$0.02</td>
      <td>$-$1.10</td>
      <td>$-$0.03</td>
      <td>0.02</td>
      <th>x</th>
      <td>1.67</td>
      <td>0.01</td>
      <td>$-$0.020</td>
      <td>$-$1.21</td>
      <td>$-$0.04</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>y</th>
      <td>$-$0.02</td>
      <td>1.52</td>
      <td>0.00</td>
      <td>$-$0.03</td>
      <td>$-$1.10</td>
      <td>0.02</td>
      <th>y</th>
      <td>$-$0.02</td>
      <td>1.67</td>
      <td>0</td>
      <td>$-$0.04</td>
      <td>$-$1.21</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>z</th>
      <td>0.00</td>
      <td>$-$0.02</td>
      <td>1.52</td>
      <td>0.02</td>
      <td>0.02</td>
      <td>$-$0.85</td>
      <th>z</th>
      <td>0.01</td>
      <td>$-$0.02</td>
      <td>1.67</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>$-$0.91</td>
    </tr>
  </tbody>
</table>

### G. Defect formation energies

The study of defects in alumina has long been of interest, but a full understanding of the underlying mechanisms is still needed. $^{44}$ Hine *et al.* have calculated the formation energies of intrinsic defects in alumina using first principles methods with finite size corrections. $^{45,46}$ As classical molecular dynamics is able to access larger cell sizes than DFT, we use our potential to calculate defect formation energies using supercells of up to 12 000 atoms.

In the Zhang-Northrup formalism, $^{47}$ the formation energy $\Delta E_f$ of a defect, such as a vacancy or interstitial, is given by
$$
\Delta E_f = E^{\text{def}} - E^{\text{perf}} - \sum_i \Delta n_i \mu_i - \Delta n_e \mu_e, \tag{7}
$$
where $\mu_i$ is the chemical potential of atomic species $i$, $\mu_e$ is the chemical potential of an electron in the perfect crystal, and $\Delta n_e$ and $\Delta n_i$ are the net changes in the numbers of electrons and atoms of species $i$, respectively, required to create the defect. For the case of groups of defects that preserve both charge neutrality and stoichiometry such as a Frenkel pair, which comprises an interstitial and a vacancy (e.g., $V_{Al}^{3-} + Al_i^{3+}$, in Kröger-Vink notation), or a Schottky quintet of vacancies $(3V_O^{2+} + 2V_{Al}^{3-})$, the expression for the formation energy simplifies. It is no longer necessary to know the chemical potentials of the electrons or the atomic species. For example, the formation energy of an Al vacancy $(V_{Al}^{3-})$ is
$$
\Delta E_f\left[V_{Al}^{3-}\right] = E\left[V_{Al}^{3-}\right] - E^{\text{perf}} + \mu_{Al} - 3\mu_e, \tag{8}
$$
where $E[V_{Al}^{3-}]$ is the energy of a crystal containing a single triply charged Al vacancy and $E^{\text{perf}}$ is the energy of the perfect crystal. The formation energy of an Al interstitial $(Al_i^{3+})$ is
$$
\Delta E_f\left[Al_i^{3+}\right] = E\left[Al_i^{3+}\right] - E^{\text{perf}} - \mu_{Al} + 3\mu_e. \tag{9}
$$

At sufficiently low defect concentrations, the interstitial and the vacancy do not interact with one another and the formation energy of the pair simplifies to
$$
\begin{aligned}
\Delta E_f\left[V_{Al}^{3-} + Al_i^{3+}\right] &= \Delta E_f\left[V_{Al}^{3-}\right] + \Delta E_f\left[Al_i^{3+}\right] = E\left[V_{Al}^{3-}\right] \\
&\quad + E\left[Al_i^{3+}\right] - 2E^{\text{perf}}. \tag{10}
\end{aligned}
$$

To calculated this quantity with our potential, we construct a supercell containing $N$ $Al_2O_3$ units of the perfect crystal and use periodic boundary conditions. $E^{\text{perf}} = N\mu_{Al_2O_3} = N(2\mu_{Al} + 3\mu_O)$ is simply the potential energy of this

![](./images/813179938667495425_6.jpg)

FIG. 4. Phonon dispersion curves for corundum, calculated with our potential (black dots) and compared to DFT (blue triangles) and experiment (red crosses). $^{41}$

![](./images/813179938667495425_7.jpg)

FIG. 5. Thermodynamic properties of Al₂O₃ from lattice dynamics under
the quasi-harmonic approximation.

supercell. Neglecting finite size errors, which are discussed
below, $E_f[Al_i^{3+}]$ can be approximated by the energy of the
same supercell with an Al ion placed interstitially and the
atomic positions of all atoms in the cell relaxed. $E[V_{Al}^{3-}]$ can
be approximated by the energy calculated by taking one Al
ion out of the supercell of perfect crystal and relaxing the
atomic positions.

Expressions analogous to Eq. (10) for the energies of the
oxygen Frenkel pair and the Schottky quintet can be deduced
in a similar manner. They are

$$
\Delta E_{f}\left[V_{O}^{2+}+O_{i}^{2-}\right]=E\left[V_{O}^{2+}\right]+E\left[O_{i}^{2-}\right]-2 E^{\text {perf }}, \quad(11)
$$

$$
\begin{aligned}
\Delta E_{f}\left[3 V_{O}^{2+}+2 V_{A l}^{3-}\right] &=2 E\left[V_{A l}^{3-}\right]+3 E\left[V_{O}^{2+}\right] \\
&-\frac{(5 N-1)}{N} E^{\text {perf }}.
\end{aligned}\qquad(12)
$$

It is worth noting that, because the ions have partial charges
rather than formal integer charges, the defects in our calcula-
tions also have partial charges. This is reasonable if the partial

<table>
<caption>TABLE VII. Elastic constants of corundum as calculated for our potential and compared to both experimental results⁴³ and Wilson <i>et al.</i>'s AIM potentials.¹¹</caption>
  <thead>
    <tr>
      <th></th>
      <th>Expt.</th>
      <th>LDA</th>
      <th>GGA</th>
      <th>Potential</th>
      <th>AIM-LDA</th>
      <th>AIM-GGA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$c_{11}$</td>
      <td>497</td>
      <td>538</td>
      <td>452</td>
      <td>496</td>
      <td>508</td>
      <td>491</td>
    </tr>
    <tr>
      <td>$c_{33}$</td>
      <td>501</td>
      <td>525</td>
      <td>438</td>
      <td>478</td>
      <td>535</td>
      <td>479</td>
    </tr>
    <tr>
      <td>$c_{44}$</td>
      <td>147</td>
      <td>167</td>
      <td>134</td>
      <td>116</td>
      <td>148</td>
      <td>107</td>
    </tr>
    <tr>
      <td>$c_{12}$</td>
      <td>162</td>
      <td>180</td>
      <td>128</td>
      <td>212</td>
      <td>189</td>
      <td>218</td>
    </tr>
    <tr>
      <td>$c_{13}$</td>
      <td>116</td>
      <td>99</td>
      <td>95</td>
      <td>169</td>
      <td>125</td>
      <td>124</td>
    </tr>
    <tr>
      <td>$c_{14}$</td>
      <td>$-$22</td>
      <td>$-$9</td>
      <td>$-$7</td>
      <td>$-$26</td>
      <td>$-$30</td>
      <td>$-$30</td>
    </tr>
  </tbody>
</table>

charges can be interpreted as screened formal charges, as we
discuss in Sec. V B.

Although we can access large cell sizes with classical
molecular dynamics, the use of periodic boundary conditions
results in defect-defect interactions which must be accounted
for if we wish to calculate the energy of a single defect em-
bedded in an infinite supercell. The most commonly used fi-
nite size correction is that of Makov and Payne,⁴⁸ where the
energy of a cubic supercell of size $L$ is written as

$$
E(L)=E(L \rightarrow \infty)-\frac{q^{2} \alpha}{2 \epsilon L}-O\left(L^{-3}\right),\qquad(13)
$$

where $\epsilon$ is the relative dielectric constant of the medium,
$q$ is the monopole aperiodic charge and $\alpha$ is the Madelung
constant, which is a property of the shape of the supercell.
$-q^2\alpha/2L$ is known as the Madelung energy, and is defined as
the potential energy per unit cell of an infinite periodic lattice
of cells each containing a point charge $q$ and a uniform neu-
tralizing background. The Madelung energy can be calculated
using the Ewald method and used to find the Madelung poten-
tial $v_M = \alpha/L$. $E(L \rightarrow \infty)$ can be estimated as the $y$-intercept
of a linear fit to the graph of $E(L)$ against $v_M$ for different sizes
and shapes of cell.⁴⁵

With our potential, we have calculated defect formation
energies, $E_f$, using supercells with a variety of shapes and
sizes, including $4 \times 4 \times 4$, $5 \times 5 \times 5$, $6 \times 6 \times 6$, $7
\times 7 \times 7$, $8 \times 8 \times 8$, $9 \times 9 \times 9$, and $10 \times 10 \times 10$ repeti-
tions of the primitive 10-atom rhombohedral cell. In addition,
with both DFT and our potential, we have calculated $E_f$ using
$2 \times 2 \times 1$, $2 \times 2 \times 2$, $3 \times 3 \times 1$, $2 \times 2 \times 3$, $4 \times 4 \times 1$, and
$3 \times 3 \times 2$ repetitions of the conventional hexagonal 30-atom
cell. We calculated the Madelung potential for each cell and

<table>
<caption>TABLE VIII. Elastic constants of $\kappa$-alumina as calculated for our potentials and compared to the LDA calculations of Holm <i>et al.</i>²⁸</caption>
  <thead>
    <tr>
      <th></th>
      <th>Holm</th>
      <th>LDA</th>
      <th>GGA</th>
      <th>Potential</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$c_{11}$</td>
      <td>460</td>
      <td>515</td>
      <td>428</td>
      <td>392</td>
    </tr>
    <tr>
      <td>$c_{22}$</td>
      <td>410</td>
      <td>451</td>
      <td>373</td>
      <td>347</td>
    </tr>
    <tr>
      <td>$c_{33}$</td>
      <td>450</td>
      <td>467</td>
      <td>385</td>
      <td>362</td>
    </tr>
    <tr>
      <td>$c_{44}$</td>
      <td>120</td>
      <td>167</td>
      <td>136</td>
      <td>90</td>
    </tr>
    <tr>
      <td>$c_{55}$</td>
      <td>140</td>
      <td>147</td>
      <td>119</td>
      <td>74</td>
    </tr>
    <tr>
      <td>$c_{66}$</td>
      <td>160</td>
      <td>191</td>
      <td>154</td>
      <td>114</td>
    </tr>
    <tr>
      <td>$c_{12}$</td>
      <td>125</td>
      <td>140</td>
      <td>124</td>
      <td>148</td>
    </tr>
    <tr>
      <td>$c_{13}$</td>
      <td>95</td>
      <td>95</td>
      <td>86</td>
      <td>127</td>
    </tr>
    <tr>
      <td>$c_{23}$</td>
      <td>145</td>
      <td>119</td>
      <td>104</td>
      <td>187</td>
    </tr>
  </tbody>
</table>

The parameters of more flexible models, which can describe bonding beyond the traditional ionic/covalent/metallic limits, tend to be less transferable between materials because they characterize the material as a whole rather than its constituent atoms, pairs of atoms, triplets, etc.

In our approach, we use a physically motivated mathematical form for our potential, although it is simpler than the one used by Jahn *et al.* However, having adopted this form, we try to exploit its full flexibility. We do not care how it fits the DFT potential energy surface as long as it does so. Our primary goal is to approximate the potential energy surface rather than calculate properties of ions from which one can subsequently assemble the potential energy surface. We exploit the full flexibility of the form of our potential by fitting all parameters simultaneously and we achieve a closer fit to the DFT potential energy surface than if we had constrained the optimization of our parameters, as Jahn *et al.* have done to preserve transferability. We fit the potential energy surface rather closely with a model that has relatively few parameters and we do retain a degree of transferability, as can be seen from some of the tests presented here and in previous work. $^{12,13,15}$ We have chosen a useful middle ground between a more general and flexible model and a strict adherence to an ionic paradigm. The former may have provided greater accuracy if it was supplemented with terms to describe long range electrostatics, while the latter may have provided greater transferability.

It is important that the closeness of our fit, as quantified by $(\Delta F, \Delta S, \Delta E)$, is converged with respect to the number of configurations sampled in the region of configuration space on which we have focussed our parameterization (corundum near the melting point at low pressure). This assures us that we have an accurate representation of the energy surface in this region, but not necessarily beyond it.

### B. Partial charges vs formal charges

The contrast between our approach and the approach of Jahn *et al.* is nicely illustrated by how each assigns charges to ions. They assign formal (integer) charges to the ions ($-2$ a.u. for oxygen, $+3$ a.u. for aluminium) whereas we treat charges as parameters to be fitted. For the simple form of our potential we argue that, even for a strongly ionic material in which each ion carries a fixed integer charge on phonon time scales, one should not necessarily use these formal charges ($q_{\text{formal}}$) in the evaluation of the electrostatic energy. This is because pairwise models of interaction between ions neglect all mechanisms by which an ion's electrons respond to the ion's local environment. By modelling the interaction between all pairs of ions with the same function of interatomic distance one is, effectively, assuming that the electron densities of all ions, regardless of their environments, can be approximated with the same spherically symmetric function. We do not simply have a pairwise model but the only electronic response mechanism that we include in the mathematical form of our model is dipole polarizability. The polarizability of ions makes the pairwise interaction between any pair of ions dependent on the positions of all other ions. In real materials, and in the DFT calculations to which we fit our parameters, there are many other ways in which interactions differ from the limit of small inert ions that pair potentials represent. For example, the sizes of ions are finite and vary, their charge densities overlap, and they can be polarized to quadrupolar and higher order. All such electronic effects tend, on average, to reduce forces on ions with respect to the limit of small rigid ions. If these effects are not explicitly represented in the potential form, the screening of interactions should be reflected in the parameters of the pairwise potential. Effective pairwise interactions are weaker in a material with responsive electrons than in a material closer to the rigid ion limit.

Therefore, to acknowledge the limitations of the form of our potential, we include the ionic charges in the set of model parameters that are fit to DFT. The entire set of parameters is fit simultaneously and the parameterizer chooses the best compromise set it can find to minimize the cost function in Eq. (6). In practice, for this potential form, the best fit to DFT data is always achieved with charges that are substantially smaller than the formal charges (e.g. $-1.47$ a.u. for oxygen). If we fix charges to their formal values, as Jahn *et al.* have done, our best fit to the DFT forces is significantly worse.

We noted in Sec. IV D that we underestimate the frequencies of long wavelength longitudinal optical (LO) phonon frequencies. A reduction of ionic charges has the mathematical form of a homogeneous isotropic screening ($q = q_{\text{formal}}/\sqrt{\epsilon_{\text{eff}}}$) by an effective scalar high frequency permittivity, $\epsilon_{\text{eff}} > 1$. If all other parameters remained fixed, increasing the partial charges (reducing $\epsilon_{\text{eff}}$) is likely to increase the frequencies of long wavelength LO phonons by increasing the strength of the long-range electric fields that accompany them. However, this improvement of LO phonon frequencies would be at the expense of a worse description of other phonons.

Jahn *et al.* use formal ionic charges and although their model overestimates LO phonon frequencies, it is in closer agreement with experimental phonon dispersions than our model is. However, as noted above, in the form of their potential they explicitly include more response mechanisms, such as ion size variations and quadrupole polarization. Therefore, if they had fit the charges to DFT as we have done, one might expect the best fit to be achieved with partial charges closer to the formal ionic charges than in our model. It would be interesting to know what partial charges they would find, to what extent the fit to DFT would be improved, and whether the resulting potential would be more accurate and/or more or less transferable. On the face of it, one would presume that if they included partial charges as a degree of freedom, they would certainly find a better fit to DFT because fitting is always improved by including more parameters. However, that would only be a certainty for the DFT data to which they fitted and it might make the "predicted" comparison to other DFT data worse.

### VI. CONCLUSIONS

We have parametrized a dipole-polarizable atomistic force field for alumina by fitting to force, stress, and energy data from DFT calculations on the corundum phase.