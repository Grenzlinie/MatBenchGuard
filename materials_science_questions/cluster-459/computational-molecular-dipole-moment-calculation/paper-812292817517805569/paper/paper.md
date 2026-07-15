# Charge Equilibration for Molecular Dynamics Simulations

Anthony K. Rappé† and William A. Goddard III*‡

BioDesign, Inc., Pasadena, California 91101, Department of Chemistry, Colorado State University, Fort Collins, Colorado 80523, and Materials Simulation Center, Beckman Institute (139-24),§ California Institute of Technology, Pasadena, California 91125 (Received: October 4, 1989)

We report here an approach for predicting charge distributions in molecules for use in molecular dynamics simulations. The input data are experimental atomic ionization potentials, electron affinities, and atomic radii. An atomic chemical potential is constructed by using these quantities plus shielded electrostatic interactions between all charges. Requiring equal chemical potentials leads to equilibrium charges that depend upon geometry. This charge equilibration (QEq) approach leads to charges in excellent agreement with experimental dipole moments and with the atomic charges obtained from the electrostatic potentials of accurate ab initio calculations. QEq can be used to predict charges for any polymer, ceramic, semiconductor, or biological system, allowing extension of molecular dynamics studies to broad classes of new systems. The charges depend upon environment and change during molecular dynamics calculations. We indicate how this approach can also be used to predict infrared intensities, dielectric constants, and other charge-related properties.

## I. Introduction

Knowledge of the charge distribution within molecules is essential for determining the electrostatic energies (including hydrogen bonding) in molecular mechanics and molecular dynamics calculations.1-4 Unfortunately, reliable charge distributions are known only for a few organic molecules.5,6 Thus, currently there is no effective approach to estimate the charges for inorganic systems (ceramics, zeolites, high-Tc superconductors), and current estimates of charges for polymers and large organic systems are quite uncertain. For biological molecules, the 20 standard amino acids and four standard bases have been assigned charges2-4 that are expected to be reasonably accurate; however, charges are not available for nonstandard amino acids, unusual bases, and various cofactors and substrates.

An additional serious problem is that current approaches1-4 to molecular mechanics and molecular dynamics use fixed charges that cannot readjust to match the electrostatic environment. Since the charges are not allowed to respond to the environment, the tradition is to incorporate a dielectric constant in the interaction potential, leading to additional uncertainties in the calculations.

We propose here a general scheme for predicting charges of large molecules based only on geometry and experimental atomic properties. The charge equilibration (QEq) approach allows the charges to respond to changes in the environment, including those in applied fields, and can be applied to any material (polymer, ceramic, semiconductor, biological, metallic).

In section II, we derive the basic equations for the charge equilibration approach. The scaling parameter λ relating atom size to crystal atomic radii is determined in section III by comparing theory and experiment for the alkali-metal halide diatomic molecules. In section IV, we discuss hydrogen atoms, which require an extension of the simple scheme of section II. Finally, in section V we apply the QEq method to a number of molecules and compare our results with experiment or ab initio theory.

The concepts involved in the QEq approach rest upon earlier ideas of Pauling, Mulliken, Margrave, Parr, Pearson, Mortier, and others. Section VI summarizes the relationship between QEq and some of these earlier ideas.

In section VII, we mention some possible extensions utilizing the ability of QEq to allow polarization of the charge distribution.

## II. Charge Equilibration

### A. Charge Dependence of Atomic Energy.
In order to estimate the equilibrium charges in a molecule, we first consider how the energy of an isolated atom changes as a function of charge. Using a neutral reference point, we can write the energy of atom A as7

$$
E_{\mathrm{A}}(Q)=E_{\mathrm{A} 0}+Q_{\mathrm{A}}\left(\frac{\partial E}{\partial Q}\right)_{\mathrm{A} 0}+1 / 2 Q_{\mathrm{A}}^{2}\left(\frac{\partial^{2} E}{\partial Q^{2}}\right)_{\mathrm{A} 0}+\ldots \quad(1)
$$

Including only terms through second order in (1) leads to

$$
\begin{gathered}
E_{\mathrm{A}}(+1)=E_{\mathrm{A} 0}+\left(\frac{\partial E}{\partial Q}\right)_{\mathrm{A} 0}+1 / 2\left(\frac{\partial^{2} E}{\partial Q^{2}}\right)_{\mathrm{A} 0} \\
E_{\mathrm{A}}(0)=E_{\mathrm{A} 0} \\
E_{\mathrm{A}}(-1)=E_{\mathrm{A} 0}-\left(\frac{\partial E}{\partial Q}\right)_{\mathrm{A} 0}+1 / 2\left(\frac{\partial^{2} E}{\partial Q^{2}}\right)_{\mathrm{A} 0}
\end{gathered}
$$

so that

$$
\left(\frac{\partial E}{\partial Q}\right)_{\mathrm{A} 0}=1 / 2(\mathrm{IP}+\mathrm{EA})=\chi_{\mathrm{A}}^{0}
$$

$$
\left(\frac{\partial^{2} E}{\partial Q^{2}}\right)_{\mathrm{A} 0}=\mathrm{IP}-\mathrm{EA}
$$

where IP and EA denote the ionization potential and electron affinity and $\chi_A$ is referred to as the electronegativity.

To understand the physical significance of the second-derivative quantity $\partial^2 E/\partial Q^2$, consider the simple case of a neutral atom with a singly occupied orbital, $\phi_A$, that is empty for the positive ion and doubly occupied for the negative ion. The difference between the IP and EA for this system is

$$
\mathrm{IP}-\mathrm{EA}=J_{\mathrm{AA}}^{0}
$$

where $J_{\mathrm{AA}}^{0}$ is the Coulomb repulsion between two electrons in the $\phi_A$ orbital (the self-Coulomb integral). We refer to this atomic repulsion quantity $J_{\mathrm{AA}}^{0}$ as the idempotential (self-Coulomb) for less awkward reference to it in later discussions. Of course, the

(1) Williams, D. E.; Cox, S. R. Acta Crystallogr., Sect. B 1984, 40, 404. Williams, D. E.; Houpt, D. J. Ibid. 1986, 42, 286. Williams, D. E.; Hsu, L. Y. Acta Crystallogr., Sect. A 1985, 41, 296. Cox, S. R.; Hsu, L. Y.; Williams, D. E. Ibid. 1981, 37, 293.

(2) Weiner, S. J.; Kollman, P. A.; Case, D. A.; Singh, U. C.; Ghio, C.; Alagona, G.; Profeta, S.; Weiner, P. J. Am. Chem. Soc. 1984, 106, 765-784. Weiner, S. J.; Kollman, P. A.; Nguyen, D. T.; Case, D. A. J. Comput. Chem. 1986, 7, 230-252.

(3) Brooks, R.; Bruccoleri, R. E.; Olafson, B. D.; States, D. J.; Swaminathan, S.; Karplus, M. J. Comput. Chem. 1983, 4, 187.

(4) Jorgensen, W. J.; Tirado-Rives, J. J. Am. Chem. Soc. 1988, 110, 1657.

(5) Cox, S. T.; Williams, D. R. J. Comput. Chem. Soc. 1961, 83, 304-323.

(6) Chirlian, L. E.; FrancI, M. M. J. Comput. Chem. 1987, 8, 894-905.

(7) Iczkowsky, R. P.; Margrave, J. L. J. Am. Chem. Soc. 1981, 2, 3547.

(8) Parr, R. G.; Pearson, R. G. J. Am. Chem. Soc. 1983, 105, 1503-1509.

†BioDesign, Inc., and Colorado State University.

‡BioDesign, Inc., and California Institute of Technology.

§Contribution No. 8340.

0022-3654/91/2095-3358$02.50/0

© 1991 American Chemical Society

**Charge Equilibration for Molecular Dynamics Simulations**

**The Journal of Physical Chemistry, Vol. 95, No. 8, 1991 3359**

<table>
<caption>TABLE I: Atomic Parameters<sup>a</sup></caption>
<thead>
<tr>
<th>element</th>
<th>χ, eV</th>
<th>J, eV</th>
<th>R, Å</th>
<th>ζ, au</th>
</tr>
</thead>
<tbody>
<tr>
<td>Li</td>
<td>3.006</td>
<td>4.772</td>
<td>1.557</td>
<td>0.4174</td>
</tr>
<tr>
<td>C</td>
<td>5.343</td>
<td>10.126</td>
<td>0.759</td>
<td>0.8563</td>
</tr>
<tr>
<td>N</td>
<td>6.899</td>
<td>11.760</td>
<td>0.715</td>
<td>0.9089</td>
</tr>
<tr>
<td>O</td>
<td>8.741</td>
<td>13.364</td>
<td>0.669</td>
<td>0.9745</td>
</tr>
<tr>
<td>F</td>
<td>10.874</td>
<td>14.948</td>
<td>0.706</td>
<td>0.9206</td>
</tr>
<tr>
<td>Na</td>
<td>2.843</td>
<td>4.592</td>
<td>2.085</td>
<td>0.4364</td>
</tr>
<tr>
<td>Si</td>
<td>4.168</td>
<td>6.974</td>
<td>1.176</td>
<td>0.7737</td>
</tr>
<tr>
<td>P</td>
<td>5.463</td>
<td>8.000</td>
<td>1.102</td>
<td>0.8257</td>
</tr>
<tr>
<td>S</td>
<td>6.928</td>
<td>8.972</td>
<td>1.047</td>
<td>0.8690</td>
</tr>
<tr>
<td>Cl</td>
<td>8.564</td>
<td>9.892</td>
<td>0.994</td>
<td>0.9154</td>
</tr>
<tr>
<td>K</td>
<td>2.421</td>
<td>3.84</td>
<td>2.586</td>
<td>0.4524</td>
</tr>
<tr>
<td>Br</td>
<td>7.790</td>
<td>8.850</td>
<td>1.141</td>
<td>1.0253</td>
</tr>
<tr>
<td>Rb</td>
<td>2.331</td>
<td>3.692</td>
<td>2.770</td>
<td>0.5162</td>
</tr>
<tr>
<td>I</td>
<td>6.822</td>
<td>7.524</td>
<td>1.333</td>
<td>1.0726</td>
</tr>
<tr>
<td>Cs</td>
<td>2.183</td>
<td>3.422</td>
<td>2.984</td>
<td>0.5663</td>
</tr>
<tr>
<td>H</td>
<td>4.5280<sup>b</sup></td>
<td>13.8904<sup>b</sup></td>
<td>0.371</td>
<td>1.0698</td>
</tr>
</tbody>
</table>

<sup>a</sup>Reference 9. <sup>b</sup>Values for $Q_{\text{H}} = 0$; see eqs 20 and 21.

optimum shape of the orbital changes upon adding an additional electron, and an accurate description of the electron affinity requires configuration interaction so that the $J_{\text{AA}}^{0}$ derived from (4) may differ somewhat from the $J_{\text{AA}}^{0}$ calculated with a Hartree-Fock wave function.

Using (2) and (4) leads to

$$
E_{\text{A}}(Q) = E_{\text{A}0} + \chi_{\text{A}}^{0}Q_{\text{A}} + {1/2}J_{\text{AA}}^{0}Q_{\text{A}}^{2} \tag{1'}
$$

where the $\chi_{\text{A}}^{0}$ and $J_{\text{AA}}^{0}$ can be derived directly from atomic data. However, the atomic IP and EA must be corrected for exchange interactions present in atoms but absent in molecules.⁹ (The atomic states contain unpaired spins, whereas the molecules for which we will use $\chi_{\text{A}}$ and $J_{\text{A}}$ generally have all spins paired.) This leads⁹ to the generalized Mulliken-Pauling electronegativities and idempotentials in Table I.

The idempotential is roughly proportional to the inverse size of the atom, and indeed, one can define a characteristic atomic size $R_{\text{A}}^{0}$ by

$$
J_{\text{AA}}^{0} = 14.4/R_{\text{A}}^{0} \quad \text{or} \quad R_{\text{A}}^{0} = 14.4/J_{\text{AA}}^{0}
$$

where the conversion factor 14.4 allows $R_{\text{A}}^{0}$ to be in angstroms and $J_{\text{AA}}^{0}$ to be in electronvolts. This equation leads to $R_{\text{H}}^{0} = 0.84$ Å, $R_{\text{C}}^{0} = 1.42$ Å, $R_{\text{N}}^{0} = 1.22$ Å, $R_{\text{O}}^{0} = 1.08$ Å, $R_{\text{Si}}^{0} = 2.06$ Å, $R_{\text{S}}^{0} = 1.60$ Å, and $R_{\text{Li}}^{0} = 3.01$ Å. Comparing with bond distances of diatomics $R_{\text{HH}}^{0} = 0.74$ Å, $R_{\text{CC}}^{0} = 1.23$ Å, $R_{\text{NN}}^{0} = 1.10$ Å, $R_{\text{OO}}^{0} = 1.21$ Å, $R_{\text{SiSi}}^{0} = 2.20$ Å, $R_{\text{SS}}^{0} = 1.63$ Å, and $R_{\text{LiLi}}^{0} = 3.08$ Å, we see that this characteristic atomic distance corresponds roughly with the homopolar bond distance.

Use of a quadratic relation such as (1') is expected to be valid only in a restricted region. In particular, the $\chi$ and $J$ are clearly invalid outside the range corresponding to emptying or filling the valence shell of electrons. Thus we restrict the ranges to

$$
-7 < Q_{\text{Li}} < +1 \quad -4 < Q_{\text{C}} < +4 \quad -2 < Q_{\text{O}} < +6 \tag{5}
$$

etc. and take $E_{\text{A}}(Q) = \infty$ outside these ranges.

**B. Electrostatic Balance.** In order to calculate the optimum charge distribution, we need to evaluate the interatomic electrostatic energy, $\sum_{\text{A}<\text{B}}Q_{\text{A}}Q_{\text{B}}J_{\text{AB}}$, where $J_{\text{AB}}$ is the Coulomb interaction between unit charges on centers A and B ($J_{\text{AB}}$ depends on $R_{\text{AB}}$, the distance between A and B). This leads to a total electrostatic energy of

$$
E(Q_{1}\dots Q_{N}) = \sum_{\text{A}}(E_{\text{A}0} + \chi_{\text{A}}^{0}Q_{\text{A}} + {1/2}Q_{\text{A}}^{2}J_{\text{AA}}^{0}) + \sum_{\text{A}<\text{B}}Q_{\text{A}}Q_{\text{B}}J_{\text{AB}} \tag{6}
$$

which we rewrite as

$$
E_{\text{Q}}(Q_{1}\dots Q_{N}) = \sum_{\text{A}}(E_{\text{A}0} + \chi_{\text{A}}^{0}Q_{\text{A}}) + {1/2}\sum_{\text{A,B}}Q_{\text{A}}Q_{\text{B}}J_{\text{AB}} \tag{6'}
$$

(suggesting that $J_{\text{AA}}(R) \to J_{\text{AA}}^{0}$ as $R \to 0$).

Taking the derivative of $E$ with respect to $Q_{\text{A}}$ leads to an atomic-scale chemical potential of the form

$$
\chi_{\text{A}}(Q_{1}\dots Q_{N}) = \frac{\partial E}{\partial Q_{\text{A}}} = \chi_{\text{A}}^{0} + \sum_{\text{B}}J_{\text{AB}}Q_{\text{B}} \tag{7}
$$

or

$$
\chi_{\text{A}}(Q_{1}\dots Q_{N}) = \chi_{\text{A}}^{0} + J_{\text{AA}}^{0}Q_{\text{A}} + \sum_{\text{B} \neq \text{A}}J_{\text{AB}}Q_{\text{B}} \tag{7'}
$$

where $\chi_{\text{A}}$ is a function of the charges on all the atoms. For equilibrium, we require that the atomic chemical potentials be equal, leading to $N - 1$ conditions

$$
\chi_{1} = \chi_{2} = \dots = \chi_{N} \tag{8}
$$

Adding the condition on total charge

$$
Q_{\text{tot}} = \sum_{i=1}^{N}Q_{i} \tag{9}
$$

leads to a total of $N$ simultaneous equations for the equilibrium self-consistent charges that are solved once for a given structure. These QEq equations can be written as

$$
\text{CD} = -\text{D} \tag{10}
$$

where
$$
D_{1}=-Q_{\text{tot}}
$$
$$
D_{i} = \chi_{i}^{0} - \chi_{1}^{0} \quad \text{for } i \geq 2 \tag{11}
$$
and
$$
C_{1i} = Q_{i}
$$
$$
C_{ij} = J_{ij} - J_{1j} \quad \text{for } i \geq 2 \tag{12}
$$

The inequalities in (5) are implemented in our programs as follows. We first solve (10)-(12) for the charges and check the inequalities in (5). If any atom is outside its range, we fix its charge at the boundary. Defining $D$ for the nonfixed atoms as
$$
D_{i} = \chi_{i}^{\text{OF}} - \chi_{1}^{\text{OF}} \quad \text{for } i \neq 1
$$
$$
D_{1} = -(Q_{\text{tot}} - \sum_{\text{B fixed}} Q_{B})
$$
where
$$
\chi_{\text{A}}^{\text{OF}} = \chi_{\text{A}}^{0} + \sum_{\text{B fixed}} J_{\text{AB}}Q_{\text{B}} \tag{13}
$$
we solve the reduced set of equations. We find that this procedure works reliably for all cases considered.

**C. Shielding Corrections.** In order to solve the QEq equations (10), we must first specify the form for the Coulomb potential $J_{\text{AB}}$ between unit charges on centers A and B separated by a distance $R$. For large separations

$$
J_{\text{AB}}(R) = 14.4/R \tag{14}
$$

(where 14.4 converts units so that $R$ is in angstroms and $J$ is in electronvolts). However, for distances where the charge distributions on centers A and B overlap, the simple Coulomb law (14) is no longer valid. Indeed, as $R \to 0$, (14) leads to
$$
J_{\text{AB}}(R) \to \infty
$$
whereas it should lead to a finite value related to $J_{\text{AA}}$ and $J_{\text{BB}}$, as illustrated in Figure 1. This overlap or shielding correction to (14) will be quite large for bonded atoms.

There are a number of ways of evaluating the shielding of the two charge distributions. We have chosen to express the shielding as the Coulomb integral between atomic densities. We could obtain the atomic densities from accurate (spherically averaged) Hartree-Fock (HF) or local-density calculations on atoms. However, in the current implementation of QEq, we describe the atomic density in terms of a single Slater orbital. For an atom whose outer valence orbital is $ns$, $np$, or $nd$, we construct a normalized $ns$ Slater orbital of the form

$$
\phi_{ns}^{\text{slat}} = N_{n}r^{n-1}e^{-\zeta r} \tag{15}
$$

(9) Rappé, A. K.; Goddard, W. A., III. Generalized Mulliken-Pauling Electronegativities. I. Main Group Elements (Groups 1, 13-17). *J. Phys. Chem.*, submitted for publication.

<table><caption>TABLE II: Charge Equilibration Results</caption>
<thead>
<tr>
<th>metal halide</th>
<th>$Q_{exp}^{a}$</th>
<th>$Q_{QEq}^{b}$</th>
<th>$Q_{\lambda=0.5}$</th>
<th>$\epsilon = 14$</th>
<th>$\epsilon = 1$</th>
<th>$\epsilon = 2$</th>
<th>$\epsilon = 0$</th>
</tr>
</thead>
<tbody>
<tr>
<td>NaCl</td>
<td>0.792</td>
<td>0.766</td>
<td>0.776</td>
<td>0.420</td>
<td>2.504</td>
<td>0.682</td>
<td>0.395</td>
</tr>
<tr>
<td>NaBr</td>
<td>0.757</td>
<td>0.745</td>
<td>0.756</td>
<td>0.391</td>
<td>2.561</td>
<td>0.644</td>
<td>0.368</td>
</tr>
<tr>
<td>NaI</td>
<td>0.708</td>
<td>0.709</td>
<td>0.720</td>
<td>0.350</td>
<td>2.663</td>
<td>0.585</td>
<td>0.328</td>
</tr>
<tr>
<td>KCl</td>
<td>0.800</td>
<td>0.775</td>
<td>0.784</td>
<td>0.473</td>
<td>2.095</td>
<td>0.737</td>
<td>0.447</td>
</tr>
<tr>
<td>KBr</td>
<td>0.783</td>
<td>0.768</td>
<td>0.777</td>
<td>0.448</td>
<td>2.165</td>
<td>0.708</td>
<td>0.423</td>
</tr>
<tr>
<td>KI</td>
<td>0.740</td>
<td>0.754</td>
<td>0.764</td>
<td>0.411</td>
<td>2.299</td>
<td>0.663</td>
<td>0.387</td>
</tr>
<tr>
<td>RbCl</td>
<td>0.784</td>
<td>0.763</td>
<td>0.771</td>
<td>0.484</td>
<td>1.918</td>
<td>0.741</td>
<td>0.459</td>
</tr>
<tr>
<td>RbBr</td>
<td>0.768</td>
<td>0.757</td>
<td>0.766</td>
<td>0.460</td>
<td>1.977</td>
<td>0.713</td>
<td>0.435</td>
</tr>
<tr>
<td>RbI</td>
<td>0.753</td>
<td>0.747</td>
<td>0.757</td>
<td>0.424</td>
<td>2.088</td>
<td>0.672</td>
<td>0.400</td>
</tr>
<tr>
<td>CsCl</td>
<td>0.743</td>
<td>0.769</td>
<td>0.777</td>
<td>0.505</td>
<td>1.874</td>
<td>0.763</td>
<td>0.479</td>
</tr>
<tr>
<td>CsBr</td>
<td>0.734</td>
<td>0.767</td>
<td>0.776</td>
<td>0.482</td>
<td>1.935</td>
<td>0.739</td>
<td>0.457</td>
</tr>
<tr>
<td>CsI</td>
<td>0.735</td>
<td>0.763</td>
<td>0.773</td>
<td>0.449</td>
<td>2.054</td>
<td>0.703</td>
<td>0.424</td>
</tr>
<tr>
<td>LiF</td>
<td>0.837</td>
<td>0.791</td>
<td>0.803</td>
<td>0.427</td>
<td>6.033</td>
<td>0.748</td>
<td>0.399</td>
</tr>
<tr>
<td>LiCl</td>
<td>0.731</td>
<td>0.939</td>
<td>0.958</td>
<td>0.406</td>
<td>13.513</td>
<td>0.737</td>
<td>0.379</td>
</tr>
<tr>
<td>LiBr</td>
<td>0.694</td>
<td>0.902</td>
<td>0.921</td>
<td>0.377</td>
<td>13.563</td>
<td>0.685</td>
<td>0.351</td>
</tr>
<tr>
<td>LiI</td>
<td>0.647</td>
<td>0.841</td>
<td>0.860</td>
<td>0.333</td>
<td>14.936</td>
<td>0.608</td>
<td>0.310</td>
</tr>
<tr>
<td>NaF</td>
<td>0.879</td>
<td>0.665</td>
<td>0.671</td>
<td>0.434</td>
<td>1.751</td>
<td>0.666</td>
<td>0.411</td>
</tr>
<tr>
<td>KF</td>
<td>0.821</td>
<td>0.662</td>
<td>0.667</td>
<td>0.473</td>
<td>1.530</td>
<td>0.695</td>
<td>0.450</td>
</tr>
<tr>
<td>RbF</td>
<td>0.781</td>
<td>0.653</td>
<td>0.657</td>
<td>0.481</td>
<td>1.435</td>
<td>0.695</td>
<td>0.458</td>
</tr>
<tr>
<td>CsF</td>
<td>0.697</td>
<td>0.655</td>
<td>0.660</td>
<td>0.496</td>
<td>1.427</td>
<td>0.711</td>
<td>0.473</td>
</tr>
</tbody>
</table>

$^{a}$Reference 25. $^{b}$From eq 17 with $\lambda_{opt} = 0.4913$.

![](./images/812292817517805569_1.jpg)

Figure 1. Shielded potentials for 1s-7s Slater orbitals. Here $\zeta_{A}$ was taken from eq 17 with $R_{A} = 0.759a_{0}$ (carbon). Also included is the unshielded Coulomb potential, 14.4/R.

where $N_{n}$ is the normalization constant. From (15), the average size of the atom is

$$
R_{\mathrm{A}} \equiv\langle r\rangle=(2 n+1) /\left(2 \zeta_{\mathrm{A}}\right) \quad(16)
$$

Consequently, we choose the valence orbital exponent $\zeta_{A}$ for atom A by the relation

$$
\zeta_{\mathrm{A}}=\lambda(2 n+1) /\left(2 R_{\mathrm{A}}\right) \quad(17)
$$

where $R_{A}$ is the covalent radius in atomic units $(a_{0}=0.52917$ Å) for atom A, which we select from experimental crystal structure data (see Table I). An adjustable parameter $\lambda$ is included in (17) to account for the difference between an average atom size as given by (16) and the crystal covalent radius $R_{A}$. We require that the same $\lambda$ be used for all atom of the periodic table and in section III determine I by comparing the predicted and experimental dipole moments of the alkali-metal halide diatomics. The diatomic Coulomb integral $J_{AB}$ involving these Slater functions is evaluated exactly for $\zeta_{A}$ and $\zeta_{B}$ at the various distances.

### III. Alkali-Metal Halides

In order to determine the scaling factor $\lambda$ that adjusts atomic radii to Coulomb shielding distance, we considered the 12 alka- li-metal halide molecules MX, where M = Na, K, Rb, or Cs and X = Cl, Br, or I. For these systems, (8) and (9) reduce to

$$
\begin{gathered}
Q_{\mathrm{X}}=-Q_{\mathrm{M}} \\
Q_{\mathrm{M}}=\frac{\chi_{\mathrm{X}}^{0}-\chi_{\mathrm{M}}^{0}}{J_{\mathrm{MM}}+J_{\mathrm{XX}}-2 J_{\mathrm{MX}}}
\end{gathered}
$$

We require that the calculated $Q_{M}$ lead to the experimental dipole moment $^{10}$

$$
\mu_{\mathrm{MX}}=(1 / 4.80324) Q_{\mathrm{M}} R_{\mathrm{MX}} \quad(19)
$$

where $R_{MX}$ is the experimental bond distance (the constant4.80324 allows $Q$ to be in electron units, $R$ in angstroms, and $\mu$ in debyes). The only variable here is the scaling parameter $\lambda$. The best value of $\lambda$ is 0.4913, which leads to an average error of0.0018 e (see Table II). Rounding off to $\lambda=1 / 2$ leads also to an average error of 0.0018 e, and hence (17) becomes

$$
\zeta_{\mathrm{A}}=(2 n+1) /\left(4 R_{\mathrm{A}}\right) \quad\left(17^{\prime}\right)
$$

(with $R_{A}$ in units of $a_{0}$).

We did not use $M=Li$ and $X=F$ in the fits because the errors were larger for these first-row elements. However, the results for these eight cases are also listed in Table II. Including these cases, the average error increases to 0.15 e.

### IV. Hydrogen

The Mulliken-like definition $^{11}$ for electronegativity leads for hydrogen to $\chi_{H}^{M}=1 /_{2}(IP+EA)=7.17 eV$ , which is not consistent with the Pauling $^{12}$ or other $^{13}$ empirical values for electronegativities. With $\chi_{H}^{M}$ , the hydrogen is more electronegative than C $(\chi_{C}^{emp}=5.34)$ or $N(\chi_{N}^{emp}=6.90)$ , whereas the Pauling scale(based on chemical experience) has hydrogen much more elec- tropositive than $C(\chi_{H}^{P}=2.1$ , while $\chi_{C}^{P}=2.5)$ and slightly more electronegative than boron $(\chi_{B}^{P}=2.0)$ . As discussed in ref 9, the problem with $\chi_{H}^{M}$ is that the effective EA for H is much smaller than the atomic value because the $H$ orbital involved in a bond cannot expand to the value achieved in a free $H^{-}$ ion. Consequently, we redefine $\chi_{H}^{0}$ and $J_{HH}^{0}$ for hydrogen, allowing $EA_{H}$ to be a variable.

From an examination of the charges on $H$ in the molecules $LiH$ , $CH_{4}, NH_{3}, H_{2} O$ , and $HF$ , we find that an accurate description of $Q_{H}$ is obtained if the effective charge parameter $\zeta_{H}$ is allowed to be charge-dependent:

$$
\zeta_{\mathrm{H}}\left(Q_{\mathrm{H}}\right)=\zeta_{\mathrm{H}}^{0}+Q_{\mathrm{H}} \quad(20)
$$

Here $\zeta_{H}^{0}=1.0698$ is based on (17) where $R_{H}=0.371$ Å. The idempotential $J_{HH}$ becomes charge-dependent:

$$
J_{\mathrm{HH}}\left(Q_{\mathrm{H}}\right)=\left(1+Q_{\mathrm{H}} / \zeta_{\mathrm{H}}^{0}\right) J_{\mathrm{HH}}^{0} \quad(21)
$$

(10) Huber, K.; Herzberg, G. K. Constants of Diatomic Molecules; Van Nostrand-Reinhold Co.: New York, 1979.
(11) Mulliken, R. S. J. Chem. Phys. 1935, 3, 573.
(12) Pauling, L. Nature of the Chemical Bond, 3rd ed.; Cornell University Press: Ithaca, NY, 1960.
(13) Sanderson, S. T. Chemical Bonds and Bond Energy; Academic Press: New York, 1976.

![](./images/812292817517805569_2.jpg)

![](./images/812292817517805569_3.jpg)

Figure 2. (a) Predicted charges for Ala-His-Ala. The N and O termini are charged as appropriate for a peptide. Comparisons with charges from AMBER² are given in parentheses. (b) Same as (a) except that His is protonated.

<table>
  <thead>
    <tr>
      <th colspan="5">TABLE III: Charges on Hydrogenⁿ</th>
    </tr>
    <tr>
      <th>compd</th>
      <th>exptl</th>
      <th>QEqᵇ</th>
      <th>HFᶜ</th>
      <th>QEq^HFᵈ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HF</td>
      <td>0.415ʲ</td>
      <td>0.462</td>
      <td>0.462</td>
      <td>0.457</td>
    </tr>
    <tr>
      <td>H₂O</td>
      <td>0.325ᵉ</td>
      <td>0.353</td>
      <td>0.398</td>
      <td>0.346</td>
    </tr>
    <tr>
      <td>NH₃</td>
      <td>0.267ᵉ</td>
      <td>0.243</td>
      <td>0.338</td>
      <td>0.233</td>
    </tr>
    <tr>
      <td>CH₄</td>
      <td>0.150ʰ</td>
      <td>0.149</td>
      <td>0.124</td>
      <td>0.124</td>
    </tr>
    <tr>
      <td>LiH</td>
      <td>-0.768ʲ</td>
      <td>-0.767</td>
      <td>-0.682ᵉ</td>
      <td>-0.679</td>
    </tr>
  </tbody>
</table>

ⁿ From eq 23 for $\chi_H(Q)$ and eq 7 for other atoms. ᵇ Fitted to experimental charges; $\chi_H^0 = 4.5280$, $J_H^0 = 13.8904$. ᶜ Reference 6. ᵈ Fitted to HF charges; $\chi_H^0 = 4.7174$, $J_H^0 = 13.4725. ^e$Closlowski, J. Phys. Rev. Lett. 1989, 62, 1469. ʲ Reference 25. ˢ Reference 26. ʰ Reference 27.

To determine the parameters $\chi_{HH}^0$ and $J_{HH}^0$, we considered the five cases in Table III and compared with experiment (where the experimental charges are based on the lowest moments) or accurate theory. A least-squares fit leads to

$$
\chi_{\mathrm{H}}^{0}=4.5280 \mathrm{eV} \quad J_{\mathrm{HH}}^{0}(0)=13.8904 \mathrm{eV} \tag{22}
$$

and a good fit to the experimentally derived charges (see Table III, first two columns). Thus

$$
E_{\mathrm{H}}+E_{\mathrm{H} 0}+\chi_{\mathrm{H}}^{0} Q_{\mathrm{H}}+1 /{ }_{2} J_{\mathrm{HH}}^{0} Q_{\mathrm{H}}^{2}\left(1+Q_{\mathrm{H}} / 1.0698\right) \tag{23}
$$

Instead of determining the parameters in (20) with experimentally derived charges, we could use the charges calculated from electrostatic potentials of HF wave functions. This might be more appropriate for comparing with charges from HF calculations. This leads to

$$
\chi_{\mathrm{H}}^{0}=4.7174 \mathrm{eV} \quad J_{\mathrm{HH}}^{0}=13.4725 \mathrm{eV} \tag{24}
$$

and other results as in the last column of Table III.

Equations 20 and 21 are well-behaved in the range of $Q_{\mathrm{H}}$

$$
-1.0<Q_{\mathrm{H}}<+1.0 \tag{5'}
$$

corresponding to (5). (They would lead to unphysical results for sufficiently negative values of $Q_{\mathrm{H}}$.)

In solving (using (21), we use (20) with an estimated $Q_{\mathrm{H}}$ and iterate until all $Q_{\mathrm{H}}$'s are self-consistent. This converges rapidly for all cases tried (six to ten iterations for an initial guess of zero for all cases discussed).

### V. Results

To test the utility of the charge equilibration approach, calculations were carried out on a representative set of molecules for which ab initio partial charges or experimentally derived charges are available.⁵·⁶ The calculations were carried out at the experimental geometries,¹⁴⁻¹⁶ using the electronegativities, idempotentials, and atomic radii in Table I. The results are presented in Table IV, where we show both the values using hydrogen parameters (eq 21) based on experimental moments (denoted QEq) and the values based on HF charges (denoted QEq^HF). The theoretical partial charges for ab initio HF calculations were obtained from fitting electrostatic potentials. Experimental charges are based on fitting to the lowest electrostatic moment from experiment.

When we compare the various theoretical and experimental charges, it is clear that there is no real standard for accuracy. Thus, for $\mathrm{H}_{2} \mathrm{CO}$, HF leads to $Q_{\mathrm{C}}=0.58$, MP2 (second-order Møller-Plesset theory) leads to $Q_{\mathrm{C}}=0.19$, and QEq leads to $Q_{\mathrm{C}}$ = 0.21. Similarly, for $\mathrm{H}_{2} \mathrm{O}$, HF leads to $Q_{\mathrm{H}}=0.40$, MP2 leads to $Q_{\mathrm{H}}=0.47$, experiment leads to $Q_{\mathrm{H}}=0.33$, and QEq leads to $Q_{\mathrm{H}}=0.36$. Nevertheless, we believe that the QEq charges are in reasonable agreement with both experiment and ab initio theory.

Figure 2 shows the charges for a typical peptide (histidine) in the neutral and protonated states. For these calculations, we used the tripeptide Ala-His-Ala in the extended configuration with the amino terminus protonated and the carboxy terminus in the carboxylate form (-COO⁻). For protonated His (Figure 2b), the net charge from QEq is distributed over the molecule, as would be expected for a vacuum. When these molecules are solvated with water, we would expect more localized charges. For comparison, we also show the charges on His from the AMBER com-

![](./images/812292817517805569_4.jpg)

Figure 3. Predicted charges for an adenosine (deoxy) nucleotide. Charges from AMBER² are given in parentheses.

(14) All polyatomic geometries are from ref 15 or 16. Diatomic geometries are from ref 10.

(15) Harmony, M. D.; et al. J. Phys. Chem. Ref. Data 1979, 8, 619.

(16) Callomon, J. H.; Hirota, E.; Kuchitsu, K.; Lafferty, W. J.; Maki, A. G.; Pote, C. S. Landolt-Börnstein, New Series; Springer-Verlag: New York, 1978; Vol. 7.

(17) Gasteiger, J.; Marsili, M. Tetrahedron 1980, 36, 3219-3288.

(18) Del Re, G. J. Chem. Soc. 1958, 4031. Del Re, G.; Pullman, B.; Yonezawa, T. Biochim. Biophys. Acta 1963, 75, 153.

(19) Mortier, W. J.; Van Genechten, K.; Gasteiger, J. J. Am. Chem. Soc. 1985, 107, 829-835. Mortier, W. J.; Ghosh, S. K.; Shankar, S. Ibid. 1986, 108, 4315-4320.

(20) In this fit we weighted CH₄ as 5, LiH as 0.2, and the others as 1.

(21) Dosen-Micovic, L.; Jerimic, D.; Allinger, N. L. J. Am. Chem. Soc. 1983, 105, 1716-1722, 1723-1733.

![](./images/812292817517805569_5.jpg)

![](./images/812292817517805569_6.jpg)

![](./images/812292817517805569_7.jpg)

![](./images/812292817517805569_8.jpg)

Figure 4. Predicted charges for (top to bottom) polyethylene, poly(vi- nylidene difluoride), poly(tetrafluoroethylene), and poly(oxymethylene).

![](./images/812292817517805569_9.jpg)

![](./images/812292817517805569_10.jpg)

Figure 5. Predicted charges for (a) Nylon 66 and (b) PEEK. For each case, an additional unit was included on each end (to eliminate end effects).

puter program (in parentheses). $^{2}$

Figure 3 shows the QEq charges for a typical nucleotide (adenosine) from DNA. This is compared with the charges from AMBER (in parentheses). $^{2}$

In Figure 4, we give the charges for the repeat units for (a) polyethylene, (b) poly(vinylidene difluoride), (c) poly(tetra- fluoroethylene), and (d) orthorhombic poly(oxymethylene), while Figure 5 has those for (a) Nylon 66 and (b) PEEK (poly(eth- er-ether-ketone)) (poly(oxy-1,4-phenyleneoxy-1,4-phenylene- carbonyl-1,4-phenylene)). In all cases, we used the extended configuration with three such units for which only the charges of the middle fragment are shown. There is no standard of comparison for these systems; however, the charges are in rea- sonable agreement with analogous parts of Figures 2 and 3.

In Figure 6, we show charges for $NaCl,(NaCl)_{2}$ , and $(NaCl)_{4}$ , where $R_{NaCl}=2.84 \AA$ and the bond angles are $90^{\circ}$ as in an NaCl crystal. The charges show a reasonable trend.

## VI. Comparison with Other Methods

The idea that the Mulliken electronegativity, $\chi=1 / 2(IP+EA)$ , is equal to the chemical potential $\mu=-\partial E / \partial Q$ was suggested by Iczkowsky and Margrave. $^{7}$ The relation between electronegativity and quantum-mechanical wave functions was established by Parr et al., $^{22}$ who showed that $\mu=\partial E(\rho) / \delta \rho$ , where $E(\rho)$ is the density functional for the energy.

![](./images/812292817517805569_11.jpg)

Figure 6. Clusters of sodium chloride, all with $R=2.84 \AA$ and bond angles of $90^{\circ}$ .

The charge expansion of the total energy (1) was suggested by Iczkowsky and Margrave. $^{7}$

It was Parr and Pearson $^{8}$ who identified the physical significance of the second-order coefficient IP - EA as an atomic hardness

$$\eta_{\mathrm{A}}^{0}=1 / 2(\mathrm{IP}-\mathrm{EA})=1 / 2 J_{\mathrm{AA}}^{0}$$

We agree with them that the quantity IP - EA is an important chemical quantity. However, the identification with hardness in acids and bases is less obvious. Consequently, we refer $^{9}$ to this atomic Coulomb repulsion quantity $J_{AA}^{0}=IP-EA=2 \pi_{A}^{0}$ as the idempotential (self-Coulomb interaction) for less awkward ref- erence in discussions.

Popular approaches for estimating charges in molecules have been the partial equalization of orbital electronegativities (PEOE) of Gasteiger $^{17}$ and the Del Re $^{18}$ scheme. These methods depend upon the topology (bond connections) but not on geometry. From Table IV, we see that these schemes generally lead to the proper sign but underestimate the $Q_{H}$ of alkanes by a factor of 3-6.

A simplification of QEq theory would be to replace the Coulomb interaction $J_{AB}(R)$ by a shielded Coulombic term

$$J_{\mathrm{AB}}(R)=14.4 /\left(\epsilon R_{\mathrm{AB}}\right)\qquad(25)$$

We show in Table III the effect of using this approximation (using(21) with the fit of $\chi_{H}$ and $J_{HH}$ in experiment). Using $\epsilon=1.0$  often leads to net charges opposite those expected from electro- negativities and hence to very unreasonable charge distributions. Using dielectric constants around $\epsilon=2.0$ leads to the best self consistent charges. For $\epsilon=14$ , we obtain values that are generally the right sign but a factor of 2-3 small. The results are very sensitive to geometry and to $\epsilon$ , resulting often in singular points in the variation of $Q$ with $R$ . Thus, we cannot recommend the simple Coulomb potential with dielectric constant approximation(25).

Mortier et al. $^{19}$ derived equations analogous to (10)-(12) from density functional theory and suggested that these equations lead to reasonable charges if the standard atomic electronegativities are modified for the molecular environment. The major difference from QEq is that Mortier used the unshielded Coulomb potential(25) with $\epsilon=14.4$ . Mortier's electronegativity equalization method $^{6}$ (EEM) starts with the Sanderson $^{13}$ values for electro negativities (which are not in electronvolts) and the Parr-Pearson values $^{8}$ values of the Mulliken hardnesses (in electronvolts) and modifies them so that the predicted charges best fit the Mulliken charges from STO-3G calculations on small molecules. Using the Mortier-modified Sanderson electronegativities $(\chi_{H}=3.832$ , $\chi_{C}=4.053, \chi_{N}=5.002, \chi_{O}=5.565)$ and Parr-Pearson hardnesses $(\eta_{H}=6.836, \eta_{C}=5.617, \eta_{N}=6.8158, \eta_{O}=6.777$ , where $\eta=$  $1 / 2 J$ ) with $\epsilon=14.4$ leads to the EEM results in Table III. The correct sign is generally obtained, but the magnitudes are low by factors of 3-6. Mortier has applied this approach to the predictionof charges for a number of ceramic crystals. $^{23}$

Allinger and co-workers $^{21}$ have developed the induced dipole moment and energy (IDME) method for treating electrostatic effects in molecules in terms of bond dipole moments and induced bond dipole moments. This approach is geometry-dependent but

(22) Parr, R. G.; Donelly, R. A.; Levy, M.; Palke, W. E. J. Chem. Phys.1978, 68, 3801.
(23) Uytterhoeven, L.; Mortier, W. J.; Geerling, P. J. Phys. Chem. Solids1989, 50, 479.

<table>
<thead>
<tr><th colspan="15">TABLE IV: Charge Equilibration Results</th></tr>
<tr><th>compd</th><th>atom</th><th>QEq</th><th>QEqHF</th><th>exptl</th><th>HF</th><th>MP2</th><th>PEOE</th><th>Del Re</th><th>IDME</th><th>EEM</th><th>$\epsilon = 14^{b}$</th><th>$\epsilon = 1^{b}$</th><th>$\epsilon = 2^{b}$</th></tr>
</thead>
<tbody>
<tr><td>HF</td><td>H</td><td>0.46</td><td>0.46</td><td>$0.41^{c}$</td><td>0.46</td><td>...</td><td>0.27</td><td></td><td></td><td></td><td>0.22</td><td>−1.00</td><td>0.36</td></tr>
<tr><td>H₂O</td><td>H</td><td>0.35</td><td>0.35</td><td>$0.33^{d}$</td><td>0.40</td><td>0.47</td><td>0.21</td><td>0.33</td><td>0.36</td><td>0.05</td><td>0.11</td><td>−1.00</td><td>0.23</td></tr>
<tr><td>NH₃</td><td>H</td><td>0.24</td><td>0.23</td><td>$0.27^{d}$</td><td>0.34</td><td>...</td><td>0.11</td><td>0.24</td><td></td><td>0.02</td><td>0.05</td><td>−0.11</td><td>0.13</td></tr>
<tr><td>CH₄</td><td>H</td><td>0.15</td><td>0.13</td><td>$0.14^{e}$</td><td>0.12</td><td>...</td><td>0.02</td><td>0.04</td><td>0.07</td><td>0.00</td><td>0.01</td><td>−0.02</td><td>0.05</td></tr>
<tr><td>C₂H₆</td><td>H</td><td>0.16</td><td>0.13</td><td>$0.17^{f}$</td><td>...</td><td>0.23</td><td>0.02</td><td>0.04</td><td>0.07</td><td>0.01</td><td>0.02</td><td>−0.05</td><td>0.04</td></tr>
<tr><td>C₂H₂</td><td>H</td><td>0.13</td><td>0.11</td><td></td><td>0.29</td><td>...</td><td>0.12</td><td>0.03</td><td></td><td>0.01</td><td>0.03</td><td>...</td><td>0.06</td></tr>
<tr><td>C₂H₄</td><td>H</td><td>0.15</td><td>0.13</td><td></td><td>0.17</td><td>0.22</td><td>0.05</td><td>0.03</td><td></td><td>0.01</td><td>0.02</td><td>−0.08</td><td>0.05</td></tr>
<tr><td>C₆H₆</td><td>H</td><td>0.10</td><td>0.09</td><td></td><td>...</td><td>...</td><td>0.06</td><td>0.03</td><td></td><td>0.01</td><td>0.03</td><td>0.04</td><td>0.05</td></tr>
<tr><td>CO₂</td><td>O</td><td>−0.45</td><td>−0.45</td><td>$-0.33^{f}$</td><td>−0.45</td><td>...</td><td>−0.19</td><td>−0.14</td><td></td><td>−0.05</td><td>−0.11</td><td>−0.15</td><td>−0.29</td></tr>
<tr><td>H₂CO</td><td>O</td><td>−0.43</td><td>−0.44</td><td></td><td>−0.50</td><td>−0.45</td><td>−0.31</td><td>−0.14</td><td>−0.41</td><td>−0.10</td><td>−0.22</td><td>−0.34</td><td>−0.31</td></tr>
<tr><td rowspan="4">H₃COH</td><td>C</td><td>0.19</td><td>0.24</td><td></td><td>0.58</td><td>0.19</td><td>0.11</td><td>0.05</td><td>0.36</td><td>0.03</td><td>0.05</td><td>−0.11</td><td>0.14</td></tr>
<tr><td>H</td><td>0.12</td><td>0.10</td><td></td><td>−0.04</td><td>0.13</td><td>0.10</td><td>0.04</td><td>0.21</td><td>0.04</td><td>0.08</td><td>0.22</td><td>0.09</td></tr>
<tr><td>H(O)</td><td>0.36</td><td>0.34</td><td></td><td>0.39</td><td>...</td><td>0.21</td><td>0.30</td><td>0.36</td><td>0.03</td><td>0.07</td><td>−0.51</td><td>0.20</td></tr>
<tr><td>O</td><td>−0.66</td><td>−0.66</td><td></td><td>−0.63</td><td>...</td><td>−0.40</td><td>−0.45</td><td>−0.58</td><td>−0.11</td><td>−0.26</td><td>0.22</td><td>−0.42</td></tr>
<tr><td rowspan="4">H₂NC(O)H</td><td>C</td><td>−0.15</td><td>−0.09</td><td></td><td>0.21</td><td>...</td><td>0.63</td><td>−0.01</td><td>0.23</td><td>0.01</td><td>0.01</td><td>0.24</td><td>0.00</td></tr>
<tr><td>H₈</td><td>0.14</td><td>0.12</td><td></td><td>−0.01</td><td>...</td><td>0.05</td><td>0.06</td><td>−0.03</td><td>0.02</td><td>0.06</td><td>0.06</td><td>0.07</td></tr>
<tr><td>Hᵢ</td><td>0.18</td><td>0.16</td><td></td><td>0.04</td><td>...</td><td>0.05</td><td>0.06</td><td>0.00</td><td>0.02</td><td>0.06</td><td>−0.06</td><td>0.08</td></tr>
<tr><td>O</td><td>−0.42</td><td>−0.43</td><td></td><td>−0.57</td><td>−0.28</td><td>−0.13</td><td>−0.09</td><td></td><td>−0.22</td><td>−0.24</td><td>−0.33</td><td></td></tr>
<tr><td rowspan="5">HOC(O)H</td><td>C</td><td>0.39</td><td>0.42</td><td></td><td>0.66</td><td>0.48</td><td>0.20</td><td>0.17</td><td></td><td>0.03</td><td>0.06</td><td>−0.20</td><td>0.27</td></tr>
<tr><td>N</td><td>−0.63</td><td>−0.61</td><td></td><td>−0.92</td><td>−0.89</td><td>−0.37</td><td>−0.52</td><td></td><td>−0.05</td><td>−0.10</td><td>0.30</td><td>−0.35</td></tr>
<tr><td>Hc</td><td>0.29</td><td>0.28</td><td></td><td>0.42</td><td>0.42</td><td>0.16</td><td>0.22</td><td></td><td>0.04</td><td>0.09</td><td>0.04</td><td>0.19</td></tr>
<tr><td>Hᵢ</td><td>0.23</td><td>0.22</td><td></td><td>0.40</td><td>0.41</td><td>0.16</td><td>0.22</td><td></td><td>0.04</td><td>0.09</td><td>−0.21</td><td>0.17</td></tr>
<tr><td>O</td><td>−0.44</td><td>−0.44</td><td></td><td>−0.60</td><td>...</td><td>−0.26</td><td>−0.12</td><td></td><td>−0.08</td><td>−0.18</td><td>...</td><td>−0.31</td></tr>
<tr><td rowspan="5">H₃CCN</td><td>C</td><td>0.56</td><td>0.58</td><td></td><td>0.78</td><td>...</td><td>0.29</td><td>0.22</td><td></td><td>0.05</td><td>0.12</td><td>...</td><td>0.35</td></tr>
<tr><td>H(C)</td><td>0.16</td><td>0.14</td><td></td><td>0.03</td><td>...</td><td>0.15</td><td>0.05</td><td></td><td>0.05</td><td>0.12</td><td>...</td><td>0.10</td></tr>
<tr><td>O</td><td>−0.65</td><td>−0.65</td><td></td><td>−0.67</td><td>...</td><td>−0.48</td><td>−0.45</td><td></td><td>−0.08</td><td>−0.19</td><td>...</td><td>−0.40</td></tr>
<tr><td>H(O)</td><td>0.38</td><td>0.37</td><td></td><td>0.46</td><td>...</td><td>0.30</td><td>0.30</td><td></td><td>0.06</td><td>0.13</td><td>...</td><td>0.25</td></tr>
<tr><td>N</td><td>−0.24</td><td>−0.25</td><td></td><td>−0.43</td><td>...</td><td>−0.20</td><td>−0.07</td><td></td><td>−0.07</td><td>−0.14</td><td>0.15</td><td>−0.21</td></tr>
<tr><td rowspan="4">H₂C═C═O</td><td>C</td><td>0.22</td><td>0.22</td><td></td><td>0.43</td><td>...</td><td>0.06</td><td>0.08</td><td></td><td>0.01</td><td>0.00</td><td>−0.36</td><td>0.13</td></tr>
<tr><td>C</td><td>−0.37</td><td>−0.31</td><td></td><td>−0.39</td><td>...</td><td>0.02</td><td>−0.12</td><td></td><td>0.00</td><td>−0.01</td><td>0.06</td><td>−0.16</td></tr>
<tr><td>H</td><td>0.13</td><td>0.11</td><td></td><td>0.13</td><td>...</td><td>0.04</td><td>0.04</td><td></td><td>0.02</td><td>0.05</td><td>0.05</td><td>0.08</td></tr>
<tr><td>O</td><td>−0.45</td><td>−0.45</td><td></td><td>−0.41</td><td>...</td><td>−0.23</td><td>−0.15</td><td></td><td>−0.10</td><td>−0.23</td><td>...</td><td>−0.34</td></tr>
<tr><td rowspan="3">SiH₄</td><td>C</td><td>0.42</td><td>0.42</td><td></td><td>0.77</td><td>...</td><td>0.12</td><td>0.14</td><td></td><td>0.02</td><td>0.05</td><td>...</td><td>0.26</td></tr>
<tr><td>C</td><td>−0.23</td><td>−0.19</td><td></td><td>−1.08</td><td>...</td><td>−0.01</td><td>−0.06</td><td></td><td>0.02</td><td>0.03</td><td>...</td><td>−0.13</td></tr>
<tr><td>H</td><td>0.13</td><td>0.11</td><td></td><td>0.36</td><td>...</td><td>0.07</td><td>0.03</td><td></td><td>0.03</td><td>0.07</td><td>...</td><td>0.11</td></tr>
<tr><td>PH₃</td><td>H</td><td>0.08</td><td>0.07</td><td></td><td>0.06</td><td>...</td><td>0.01</td><td>0.04</td><td></td><td>...</td><td>0.02</td><td>−0.07</td><td>0.06</td></tr>
<tr><td rowspan="2">ClH</td><td>H</td><td>0.19</td><td>0.18</td><td></td><td>0.15</td><td>...</td><td>0.10</td><td>0.04</td><td></td><td>...</td><td>0.08</td><td>−1.00</td><td>0.15</td></tr>
<tr><td>H</td><td>0.32</td><td>0.31</td><td>0.25</td><td>...</td><td>...</td><td>0.15</td><td>...</td><td></td><td>...</td><td>0.16</td><td>−1.00</td><td>0.26</td></tr>
</tbody>
</table>

$^{a}$Carpenter, J. E.; McGrath, M. P.; Hehre, W. H. J. Am. Chem. Soc. 1989, 111, 6154. $^{b}$From eq 25. $^{c}$Reference 25. $^{d}$Reference 26. $^{e}$Reference 27. $^{f}$Buckingham, A. D.; Disch, R. L.; Dunmur, D. A. J. Am. Chem. Soc. 1968, 90, 3104.

assumes that electrostatic interactions can be built upon a molecular connectivity framework. Thus the extension to salts is not apparent. Partial charges reported by Allinger and co-workers are provided in Table IV in the column labeled IDME. The charges calculated by this approach appear to underestimate charge transfer from hydrogen by a factor of 2 (e.g., 0.07 on H in CH₄ and C₂H₆ compared with 0.15 and 0.17 for experimentally derived charges).

### VII. Properties

In addition to calculating electrostatic energies and multipole moments, the self-consistent charges can be used to evaluate the other properties such as infrared or Raman intensities. For example, if we express the $\alpha$ component of the dipole moment as
$$
\mu_{\alpha}=\sum_{i} Q_{i} R_{i \alpha} \tag{26}
$$
then the dipole derivative can be written as
$$
\frac{\partial \mu_{\alpha}}{\partial R_{j \beta}}=Q_{j} \delta_{\alpha \beta}+\sum_{i} \frac{\partial Q_{i}}{\partial R_{j \beta}} \tag{27}
$$
Using (10)
$$
\sum_{k} A_{i k} Q_{k}=-B_{i}
$$
we can write
$$
\sum_{k} \frac{\partial A_{i k}}{\partial R_{j \beta}} Q_{k}+\sum_{k} \mathrm{~A}_{i k} \frac{\partial Q_{k}}{\partial R_{j \beta}}=0 \tag{28}
$$
where (for $i \neq 1$)
$$
\frac{\partial A_{i k}}{\partial R_{j \beta}}=\frac{\partial J_{i k}}{\partial R_{j \beta}}-\frac{\partial J_{1 k}}{\partial R_{j \beta}} \tag{29}
$$
Equation 28 is solved to obtain the $\partial Q_{k} / \partial R_{j \beta}$ that are substituted into (27), which is transformed to normal modes to yield the dipole intensity of each mode. Similar formulas can be derived for Raman intensities and other charge-related quantities.

For crystals, this approach could be used to predict dielectric constants and changes of polarization with temperature (pyroelectricity) and stress (piezoelectricity).

### VIII. Summary

The charge distributions from charge equilibration (QEq) lead to good agreement with experiment. The QEq approach uses only readily available experimental data (atomic IP and EA, atomic radius) and thus can be applied to any combination of atoms. (The relevant $\chi$ and $J$ values have been tabulated for all elements through Lw.⁹,²⁴) The results for simple examples of typical organic, inorganic, biological, and polymer systems seem reasonable, and we believe that this approach will prove valuable in simulating biological, polymer, and inorganic materials.

Acknowledgment. These studies were initiated while A.K.R. was on sabbatical at BioDesign, and we thank the BioDesign staff for useful discussions. We also thank BioDesign for the use of BIOGRAF in carrying out these calculations. Partial funding for this research (W.A.G.) was provided by a grant from the Air Force Office of Scientific Research (No. AFOSR-88-0051).

(24) Rappé, A. K.; Goddard, W. A., III. Generalized Mulliken-Pauling Electronegativities. II. J. Phys. Chem., submitted for publication.
(25) Lovas, F. J.; Tiemann, E. J. Phys. Chem. Ref. Data 1974, 3, 609.
(26) Hellwege, K.-H., Hellwege, A. M., Eds. Molecular Constants; Landolt-Börnstein, New Series, Group II, Vol. 14; Springer-Verlag: New York, 1982.
(27) Amos, R. D. Mol. Phys. 1979, 38, 33. Based on CI calculations at $R_{\mathrm{CH}}=1.102 \AA$ and $\Omega_{x y z}=6.17 \times 10^{-50} \mathrm{~cm}^{2}$.