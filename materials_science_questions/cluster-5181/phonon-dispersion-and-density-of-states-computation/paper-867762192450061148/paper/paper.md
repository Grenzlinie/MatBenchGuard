
# Vibrational frequencies of light impurities in silicon

J.M. Pruneda, \( ^{1} \)  S.K. Estreicher, \( ^{2} \)  J. Junquera, \( ^{3} \)  J. Ferrer, \( ^{4} \)  and P. Ordejón \( ^{5} \) 

 \( ^{1} \) Departamento de Física, Facultad de Ciencias,

Universidad de Oviedo, C./ Calvo Sotelo s/n, 33007 Oviedo, Spain \( ^{*} \) 

 \( ^{2} \) Department of Physics, Texas Tech University, Lubbock, TX 7940 9-1051, USA

 \( ^{3} \) Dep. de Física de la Materia Condensada C-III,

Universidad Autónoma, E-28049 Madrid, Spain

 \( ^{4} \) Departamento de Física, Facultad de Ciencias,

Universidad de Oviedo, C./ Calvo Sotelo s/n, 33007 Oviedo, Spain.

 \( ^{5} \) Institut de Ciència de Materials de Barcelona – CSIC,

Campus de la UAB, E-08193 Bellaterra, Spain

(Dated: October 29, 2018)

## Abstract

We have developed a formulation of density functional perturbation theory for the calculation of vibrational frequencies in molecules and solids, which uses numerical atomic orbitals as a basis set for the electronic states. The (harmonic) dynamical matrix is extracted directly from the first order change in the density matrix with respect to infinitesimal atomic displacements from the equilibrium configuration. We have applied this method to study the vibrational properties of a number of hydrogen-related complexes and light impurities in silicon. The diagonalization of the dynamical matrix provides the vibrational modes and frequencies, including the local vibrational modes (LVMs) associated with the defects. In addition to tests on simple molecules, results for interstitial hydrogen, hydrogen dimers, vacancy-hydrogen and self-interstitial-hydrogen complexes, the boron-hydrogen pair, substitutional C, and several O-related defects in c-Si are presented. The average error relative to experiment for the  \( \sim \)  60 predicted LVMs is about 2% with most highly harmonic modes being extremely close and the more anharmonic ones within 5-6% of the measured values.

PACS numbers: 63.20.Pw, 71.15.-m, 71.15.Mb, 71.55.Cn
 

## I. INTRODUCTION

The knowledge of the structures of impurities and defects is an essential prerequisite for understanding the electrical and optical changes that these complexes induce in semiconductors such as crystalline silicon \( ^{1,2} \) . The presence of light impurities such as H, B, C or O, results in the appearance of infra-red (IR) or Raman active local vibrational modes (LVMs) usually well isolated from the frequency range of the phonons of the host material. The observation of LVMs coupled with isotope substitutions and uniaxial stress measurements provide precious information about the type and number of impurity atoms involved and the symmetry of the defect. However, these data are rarely sufficient to identify unambiguously the defect. Since the early days of Stein \( ^{3} \) , a large number of vibrational modes have been identified through the interplay of experiment and theory.

The calculation of LVMs at the ab-initio level provides a critical link between theory and experiment. This is particularly true in the case of hydrogen, since it binds covalently in the immediate vicinity of many impurities and defects thus giving rise to a number of LVMs in the range  \( \sim \)  800 to  \( \sim \) 2200 cm \( ^{-1} \) . Other common impurities in Si which produce LVMs are B, C, O, but any element lighter than Si can in principle be observed by LVM spectroscopy.

The computation of systematically accurate vibrational frequencies is a challenge for first principles theory, given their sensitivity on details of bonding geometry and electronic structure. Typical accuracies in the calculated vibrational modes for light impurities in silicon in former works are within 3-10% of the experimental data, which means in some cases a deviation of over  \( 100 \, cm^{-1} \) .

Various approaches have been used to calculate LVMs, from semiempirical models \( ^{4} \) , to ab-initio Hartree-Fock \( ^{5} \)  and density functional theory \( ^{6,7,8} \) . In most cases, frequencies are calculated in the spirit of the frozen phonon approximation. One computes the total energy of the system in the equilibrium configuration (that in which the forces acting on the atoms are zero) and then for small displacements of selected atoms (either individually or in the direction of a normal mode, if this is known). The actual value of the atomic displacement (typically a few hundredths of an Å) and the response of the nearby atoms are parameters chosen by the user. One can either fit the energy vs. displacement to a polynomial and extract a specific vibrational mode \( ^{6,9} \) , or compute the dynamical matrix by finite differences \( ^{7} \) . When a few specific modes is all that is needed, only the movement of the atoms involved
 

in those modes is considered. In these methods, it is not possible to completely isolate the harmonic contributions from the anharmonic ones, since finite displacements always involve some anharmonic effects. For this reason, the frequencies obtained in this approach are sometimes referred to as quasi-harmonic \( ^{10} \) .

One can also calculate vibrational properties from constant-temperature molecular-dynamics simulations, for instance by extracting selected frequencies from the velocity-velocity autocorrelation function \( ^{11} \)  or by using more sofisticated spectral estimators, like the MUltiple SIgnal Classification (MUSIC) algorithm. \( ^{12,13} \)  This is computationally exhausting, since long molecular dynamics runs are required, but potentially very accurate. \( ^{13} \)  This also allows the calculation of frequencies as a function of temperature.

However, the calculation of vibrational frequencies does not necessarily require the actual displacement of the atoms, as in the methods described above. Linear response theory (in particular through the application of perturbation theory in density functional theory) has been thoroughly used in the past \( ^{14} \)  to compute the response of the system to infinitesimal atomic displacements, and from that, the vibrational frequencies in the harmonic approximation. This can be done with the only knowledge of the electronic solution in the equilibrium configuration. The advantage of this approach is that anharmonic effects are eliminated, and that no reference is needed to explicit finite atomic displacements. Besides, this approach allows to compute phonons with arbitrary q vector in crystalline systems, without having to consider a supercell commensurate with the periodicity of the phonon, as it is required in the frozen phonon and molecular dynamics approaches.

We propose a method, based on density functional perturbation theory (DFPT), to compute vibrational frequencies in the harmonic approximation. We use a basis set of numerical atomic orbitals to expand the electronic wavefunctions, which makes the method computationally very efficient, and allows us to calculate systems with a large number of atoms. We have applied it to make a systematic study of a number of defect centers in silicon, involving light impurities and their complexes with intrinsic defects (vacancies and self-interstitials). In most cases, the comparison of the calculated and measured vibrational frequencies is very favorable, improving on the results obtained by other approaches.

The outline of this paper is as follows. We first discuss the theoretical method and the model used to describe the defects. Then we compare the vibrational properties obtained for a variety of complexes with experimental data as well as other first-principles calculations.
 

in the literature. Finally, we discuss the results.

## II. METHODOLOGY

## A. Ground State Description

In this work, we use the fully self-consistent ab-initio code SIESTA \( ^{15,16} \) . The electronic energy is obtained from density-functional theory (DFT) \( ^{17,18} \)  within the local density approximation. The exchange-correlation potential is that of Ceperley-Alder \( ^{19} \)  as parameterized by Perdew and Zunger. \( ^{20} \)  Norm-conserving pseudopotentials \( ^{21} \)  in the Kleinman-Bylander form \( ^{22} \)  are used to remove the core electrons from the calculations.

The valence electron wavefunctions are described with numerical linear combinations of atomic orbitals (LCAO) of the Sankey type, \( ^{23} \)  but generalized to be arbitrarily complete with the inclusion of multiple-zeta orbitals and polarization states. \( ^{24} \)  These orbitals are numerical solutions of the free atom with the appropriate pseudopotential, and are strictly zero beyond some cutoff radius. This makes the calculation of the Kohn-Sham hamiltonian to scale linearly with the number of atoms, \( ^{15,16} \)  allowing calculations in very large systems with a modest computational cost.

In the present work, the basis sets include single-zeta (SZ), double-zeta (DZ), double-zeta plus polarization (DZP), and triple-zeta plus polarization (TZP). A DZP basis includes two sets of s and  \( p' \) s plus one set of  \( d' \) s on Si, O, C or B, two  \( s' \) s and one set of  \( p' \) s on H. The radial cutoff of the atomic orbitals was determined as described in Ref. 24, with an energy shift of 0.5 Ry, and a split-norm of 0.15 for all the species except H, for which the split-norm was 0.5. The charge density is projected on a real space grid with an equivalent cutoff of 90 to 150 Ry to calculate the exchange-correlation and Hartree potentials. The host crystal is represented by a periodic supercell of 64 host atoms, and the k-point sampling is reduced to the  \( \Gamma \)  point. This restriction appears to be quite sufficient for the calculation of vibrational spectra. Tests have been performed for selected defects in a 128 host atoms cell and the results are within a few wavenumbers of those obtained in the 64 host atoms cell.

In order to determine the equilibrium structure of the defects studied, we have relaxed all the atomic coordinates with a conjugate gradient algorithm, reaching a tolerance in the forces of  \( F_{max} < 0.01eV/\mathring{A} \) . The dynamical matrix for the whole cell is computed (see below)
 

from this ground state and its eigenfrequencies and eigenmodes obtained.

## B. Linear Response Theory

A new implementation of DFPT has been developed to compute the electronic response to infinitesimal atomic displacements. As is well known from the “2n + 1” theorem in quantum mechanics, \( ^{25} \)  the first-order change of the electronic wavefunction in a perturbative expansion allows the computation of the second-order change in the energies. This implies that only the properties of the unperturbed ground state are needed to obtain the linear response of the system. The extension of this theorem to DFT is that the knowledge of the first-order change in the electronic density determines variationally the second-order change in the energy. In this way, we obtain analytically the dynamical matrix from the gradient of the density relative to atomic displacement and, from it, the vibrational properties, without physically displacing any atom.

We describe briefly here the key points of our formulation. A complete report will be published elsewhere. \( ^{26} \)  The change in the electronic wavefunction is obtained by solving the first-order perturbation expansion of the Schrödinger equation (Sternheimer equation \( ^{27} \) )

 \[ \delta\hat{H}\psi_{0,i}+\hat{H}_{0}\delta\psi_{i}=\delta\epsilon_{i}\psi_{0,i}+\epsilon_{0,i}\delta\psi_{i} \quad (1) \] 

where  \( \psi_{0,i} \)  are the ground state electronic wavefunctions and  \( \delta\psi_{i} \)  the first order perturbation of  \( \psi_{i} \)  when an atom is displaced (if we consider atom  \( \alpha \) , this would be  \( \partial_{\alpha}\psi_{i} \) ). As we expand these wave functions in terms of atomic orbitals:

 \[ \psi_{0,i}(\mathbf{r})=\sum_{\mu}c_{i\mu}\phi_{\mu}(\mathbf{r}-\mathbf{R}_{\mu}) \quad (2) \] 

the derivatives can be directly written in terms of the derivatives of the atomic orbitals:

 \[ \partial_{\alpha}\psi_{i}(\mathbf{r})=\sum_{\mu}[\partial_{\alpha}c_{i\mu}\phi_{\mu}(\mathbf{r}-\mathbf{R}_{\mu})+c_{i\mu}\partial_{\alpha}\phi_{\mu}(\mathbf{r}-\mathbf{R}_{\mu})]. \quad (3) \] 

Only the orbitals  \( \phi_{\mu} \)  centered on atom  \( \alpha \)  appear in the last term which is equal to  \( -\nabla\phi_{\mu}(\mathbf{r}-\mathbf{R}_{\mu}) \) . The change in the coefficients,  \( \partial_{\alpha}c_{i\mu} \) , is obtained from equation 1.  \( \partial\psi_{i} \)  is then used to compute the perturbation in the electronic density

 \[ \partial_{\alpha}\rho(\mathbf{r})=\sum_{\mathbf{i}=1}^{\mathrm{o c c}}[\partial_{\alpha}\psi_{\mathbf{i}}^{*}\psi_{\mathbf{i}}+\psi_{\mathbf{i}}*\partial_{\alpha}\psi_{\mathbf{i}}]. \quad (4) \]
 

This allows the computation of the dynamical matrix, by explicit derivation of the forces on all the atoms  \( \beta \)  in the system (the expressions of which can be found in Refs. 15 and 16 for our approach) with respect to the infinitesimal displacement of one of them ( \( \alpha \) ):

 \[ (M_{\alpha}M_{\beta})^{1/2}\mathbf{D}_{\alpha\beta}=\frac{\partial^{2}E}{\partial\mathbf{R}_{\alpha}\partial\mathbf{R}_{\beta}}=\partial_{\alpha}\mathbf{F}_{\beta} \quad (5) \] 

We remark that only terms up to first order in the electronic wavefunctions appear in the resulting formulas. Note that only the linear effects are obtained in this method, which is consistent with the harmonic approximation implicitly assumed in the diagonalization of the dynamical matrix. Thus, one expects to obtain high-quality frequencies for the vibrational modes that are harmonic, but the frequencies of modes involving large anharmonic contributions will be less accurate. Although phonons with arbitrary q vector can be obtained in the present approach, here we only calculate vibrations which are periodic with the simulation supercell (i.e.,  \( q = \Gamma \) ), since we are interested in LVMs.

## III. RESULTS

Tests of the method for free  \( SiH_{4} \) , CO,  \( CO_{2} \)  and  \( H_{2} \)  lead to very good agreement with experiment (see table I). Using an appropriate basis set reveals to be essential to reproduce accurate frequencies. In most of the cases a DZ set gives good values, but in some configurations a more complete basis is required. This is particularly true for bending modes. Oxygen likes to have polarization orbitals, and thus the frequencies are better when these are included. Note that the vibrational frequencies are more sensitive to the basis set size than the structural properties, such as bond lengths. In general, the largest improvements in the frequencies correspond to going from SZ to DZ, then DZ to DZP, but TZ basis produce only marginal improvements.

A number of defects containing light impurities in c-Si are now considered. These are H at a bond-center (BC) site, H dimers ( \( H_{2} \)  and  \( H_{2}^{*} \) ), the hydrogenated vacancy ( \( VH_{n}, n = 1, 2, 3, 4 \) ) and the saturated divacancy  \( V_{2}H_{6} \) , the self-interstitial-hydrogen  \( IH_{2} \)  complex, the  \( \{B, H\} \)  pair, substitutional C, interstitial O, and two charge states of the A-center (oxygen-vacancy complex). These embrace a range of Si-X bonding configurations, with X=H, C, O and B. In most cases, we have tried different basis sets in order to check, or improve the accuracy of our calculations when the chemical properties are particularly complex. We show
 

TABLE I: Calculated and measured \( ^{28} \)  frequencies for free SiH \( _{4} \) , CO, CO \( _{2} \)  and H \( _{2} \) , molecules with various basis sets.

<table><tr><td></td><td>SZ</td><td>SZP</td><td>DZ</td><td>DZP</td><td>TZ</td><td>TZP</td><td>Expt.</td></tr><tr><td colspan="8">SiH4</td></tr><tr><td>T2</td><td>2045</td><td>2064</td><td>2160</td><td>2153</td><td>2173</td><td>2159</td><td>2191</td></tr><tr><td>A1</td><td>1970</td><td>1974</td><td>2110</td><td>2116</td><td>2131</td><td>2125</td><td>2187</td></tr><tr><td>E</td><td>800</td><td>862</td><td>921</td><td>929</td><td>926</td><td>929</td><td>975</td></tr><tr><td>T2</td><td>701</td><td>772</td><td>806</td><td>818</td><td>817</td><td>821</td><td>914</td></tr><tr><td colspan="8">H2</td></tr><tr><td>A</td><td>3619</td><td>3670</td><td>4194</td><td>4185</td><td>4193</td><td>4191</td><td>4161</td></tr><tr><td colspan="8">CO</td></tr><tr><td>A</td><td>1681</td><td>1823</td><td>1885</td><td>2088</td><td>1945</td><td>2183</td><td>2170</td></tr><tr><td colspan="8">CO2</td></tr><tr><td>A1</td><td>2118</td><td>2355</td><td>2235</td><td>2277</td><td>2224</td><td>2394</td><td>2349</td></tr><tr><td>A2</td><td>1107</td><td>1216</td><td>1200</td><td>1241</td><td>1209</td><td>1331</td><td>1333</td></tr><tr><td>E</td><td>478</td><td>558</td><td>547</td><td>583</td><td>560</td><td>635</td><td>667</td></tr></table>

frequencies for the DZ and DZP basis sets. Although the diagonalization of the dynamical matrix gives all the ( \( \Gamma \)  point) modes in the cell, we present here only the stretching and some bending LVMs. We also obtain the eigenvectors which we use to determine the symmetry of the corresponding vibrational modes. Our results are compared with available experimental data, and with theoretical frequencies obtained by other authors using first-principle DFT.

## A.  \( H_{BC} \) ,  \( H_{2} \)  and  \( H_{2}^{*} \) 

At the BC site, \( ^{29} \)  hydrogen exists in the +1 and the 0 charge states. In the latter case, the odd electron does not participate in the bonding but resides in a non-bonding orbital primarily localized on the two Si atoms adjacent to the proton. Chemically, this is a 3-center, 2-electron bond, very much like the type of H bonding occurring in boron hydrides. The bond is somewhat compressed because optimal relaxation (no Si second nearest neighbors) would likely result in a longer Si-H-Si bond and a frequency lower than observed. This
 
![](./images/867762192450061148_1.jpg)

FIG. 1: Calculated structure of  \( H_{2}^{*} \)  complex in silicon. Dark spheres are Si atoms, white spheres are H. The two perpendicular arrows represent the  \( H_{AB} \)  wag eigenmodes at  \( 842\ cm^{-1} \) . The twofold degenerate wagging mode for  \( H_{BC} \)  is found at  \( 560\ cm^{-1} \) .

suggests that as H moves along the trigonal axis, it tends to form something like Si...H-Si then Si-H-Si then Si-H...Si, a process which is highly anharmonic. The calculated frequency is in table II.

Raman \( ^{40} \)  and IR \( ^{33,41} \)  measurements of  \( H_{2} \)  in silicon reveal a considerable softening of the stretching mode with respect to the frequency of  \( H_{2} \)  in the gas phase. A number of calculations (for a review, see Ref. 39) found the molecule to be stable at the tetrahedral interstitial (T) site. The electron affinity of the Si atoms surrounding  \( H_{2} \)  is at least partly responsible for a small charge transfer from  \( H_{2} \)  to its Si neighbors, which results in a weakening of the H-H bond. Even though the H-H stretch mode is not expected to be fully harmonic, our calculated frequency is close to the experimental one (table II). Note that the errors relative to experiment in the  \( D_{2} \)  and HD frequencies are very different than the error in the  \( H_{2} \)  frequency. This is also a clear feature of these frequencies when they are calculated dynamically from the v-v autocorrelation function. \( ^{42} \) 

The trigonal  \( H_{2}^{*} \)  defect \( ^{8} \)  consists of one hydrogen atom close to the antibonding (AB) site, and the other near the BC site (see figure 1). The two H atoms are inequivalent. The Si- \( H_{AB} \)  bond length is slightly longer than the Si- \( H_{BC} \)  one (we obtain 1.580 and 1.510 Å,
 

respectively) which gives rise to different stretch frequencies for the two atoms:  \( 2135 \, cm^{-1} \)  for  \( H_{BC} \)  and  \( 1750 \, cm^{-1} \)  for  \( H_{AB} \) . We also obtain two degenerate waggind modes, associated with the  \( H_{BC} \)  atom, at  \( 560 \, cm^{-1} \) , and two waggind modes with 839 and  \( 843 \, cm^{-1} \) , related to  \( H_{AB} \) . The latter should be degenerate, but small inaccuracies in the atomic relaxations render them at slightly different frequencies.

TABLE II: Calculated and measured frequencies for  \( H_{BC} \)  (our calculation is spin polarized for  \( H_{DC}^{0} \)  and spin averaged for  \( H_{BC}^{+} \) ),  \( H_{2} \)  in the  \( \langle100\rangle \)  alignment, and  \( H_{2}^{*} = H_{BC}H_{AB} \) . A DZ basis was used for all these complexes. The errors relative to experimental values are in parenthesis. (a) is Ref. 30, (b) is Ref. 31, (c) is Ref. 32, (d) is Ref. 33, (e) is Ref. 34, (f) is Ref. 35, (g) is Ref. 36, (h) is Ref. 37, and (i) is Ref. 38. Were  \( H_{2} \)  a classical dumbbell, its wag modes would be at 731 and  \( 860 \, cm^{-1} \)  (see discussion in Ref. 39).

<table><tr><td></td><td>expt.</td><td>this work</td><td colspan="3">other authors</td></tr><tr><td></td><td></td><td></td><td colspan="3">HBC</td></tr><tr><td>HBC+</td><td>1998a</td><td>1891(−5%)</td><td>2203b(+10%)</td><td>2210c(+11%)</td><td></td></tr><tr><td>HBC0</td><td>-</td><td>1813</td><td>1768b</td><td>1945c</td><td></td></tr><tr><td></td><td></td><td></td><td colspan="3">H2 in Si</td></tr><tr><td>H2</td><td>3618d</td><td>3549(−2%)</td><td>3607c(+0%)</td><td>3396f(−6%)</td><td>3260i(−9%)</td></tr><tr><td>DH</td><td>3265d</td><td>3081(−6%)</td><td>3129e(−4%)</td><td></td><td></td></tr><tr><td>D2</td><td>2643d</td><td>2511(−5%)</td><td>2559e(−3%)</td><td></td><td></td></tr><tr><td></td><td>2062g</td><td>2135(+3%)</td><td>2164g(+5%)</td><td>2100h(+2%)</td><td>1945i(−5%)</td></tr><tr><td>H2*</td><td>1838g</td><td>1750(−5%)</td><td>1844g(+0%)</td><td>1500h(+18%)</td><td>1677i(−9%)</td></tr><tr><td></td><td>817g</td><td>843/839(+3%)</td><td>1002g(+22%)</td><td></td><td>711i(−13%)</td></tr></table>

## B. Hydrogen and native defects

A considerable number of IR and Raman lines are related to H–intrinsic defect complexes. It has been noted \( ^{43,44} \)  that vibrational modes above  \( 2000\ cm^{-1} \)  are mainly related to H in vacancies, while those lines below  \( 2000\ cm^{-1} \)  are predominant for the H-self-interstitial systems or H at AB sites. A large number of geometrical configurations may lead to very similar vibrational lines, making it difficult to identify these defects unambiguously. As noted
 

by other groups \( ^{2,45,46,47} \) , the stretching frequencies in  \( VH_{n} \)  (n = 1, 2, 3, 4) systems increases with n due to the repulsive H-H interaction. Thus, the highest IR line is that of  \( VH_{4} \) . The Si-H bonds point toward the center of the vacancy along the trigonal axes.

In our calculations (table III), VH has monoclinic symmetry, and the H oscillates parallel to the  \( \langle111\rangle \)  direction. In the orthorhombic  \( VH_{2} \) , the two equivalent H have stretching modes along the  \( \langle100\rangle \)  and  \( \langle001\rangle \)  directions. The frequencies for these modes are 2121 and  \( 2144\ cm^{-1} \)  respectively.  \( VH_{3} \)  has  \( C_{3v} \)  symmetry. The A singlet involves the movement of the three H atoms towards the vacancy, while in the twofold degenerate E mode one of the atoms moves in opposition.  \( VH_{4} \)  has  \( T_{d} \)  symmetry. In addition to the threefold degenerate  \( T_{2} \)  mode at 2205, we obtain an IR-inactive singlet  \( A_{1} \)  mode at 2265  \( cm^{-1} \) .

The vibrational modes of  \( V_{2}H_{6} \)  are almost identical to those of  \( VH_{3} \) : The fully saturated divacancy behaves very much like two weakly coupled  \( VH_{3} \)  complexes. The  \( A_{2} \)  singlet at  \( 2176\ cm^{-1} \)  induces a dipole along the  \( \langle111\rangle \)  direction. In addition to this mode and the IR-active E doublet, we obtain two IR-inactive modes at  \( 2186\ cm^{-1} \)  and  \( 2134\ cm^{-1} $ .

The  \( HI_{2} \)  complex \( ^{50} \)  has two equivalent and weakly coupled hydrogen atoms, which yields two very similar stretching frequencies. Uniaxial stress measurements show that the two hydrogen atoms are equivalent. Our relaxed structure has almost  \( C_{2v} \)  symmetry, with the A mode higher than the B mode, confirming early results \( ^{50} \) . The deviation from perfect symmetry is due to the finite tolerance in the geometry optimization. This deviation is seen when comparing the IHD and IDH complexes: they should be identical but we find their frequencies to be off by  \( 2\ cm^{-1} \) . Note that we reproduce the correct ordering for the bending modes of  \( HI_{2} \)  at 737 and  \( 732\ cm^{-1} \)  (table IV).

## C. Oxygen, Carbon and Boron in Silicon

Oxygen is a well-known impurity which is especially important in Czochralski-grown Si, and a considerable amount of effort was focused in understanding its properties. \( ^{[51]} \)  We have computed the LVM frequencies for interstitial oxygen ( \( O_{i} \) ) and two charge states of the vacancy-oxygen complex (A-center). The results are in table V. Frequencies for  \( O_{i} \)  were computed with the oxygen placed at the BC site, where the probability of finding this delocalized atom is maximum, and the classical harmonic potential can better describe the local modes. The IR-active  \( A_{2u} \)  mode corresponds to the asymmetric-stretching mode,
 

while the  \( A_{1g} \)  is the symmetric one.  \( E_{u} \)  mode involves the movement of nearest silicon atoms with no participation of the oxygen \( ^{52} \) . Finally, TableVI shows the triply degenerate mode of substitutional carbon as well as the LVMs associated with the  \( \{B,H\} \)  complex. \( ^{2} \) 

## IV. CONCLUSIONS

We have presented a new development of DFPT, using localized atomic wavefunctions as a basis set, and applied it to the study of LVMs for light impurities in silicon. In contrast to other methods, the dynamical matrix is computed analytically without actually displacing any atom from its equilibrium position. The calculations are based on the ground state density matrix as computed with the SIESTA package.

Tests of the method for free molecules  \( \left(\mathrm{SiH}_{4}, \mathrm{H}_{2}, \mathrm{CO}, \mathrm{and} \mathrm{CO}_{2}\right) \)  show that this approach is highly accurate in situations where the anharmonic contributions are small. Note that the frequencies are obtained at T = 0K while experimental data are obtained at low, but non-zero, temperatures.

We have used a variety of basis set sizes to describe the electronic wavefunctions. In most cases, a DZ basis is quite sufficient to obtain accurate atomic structures and vibrational frequencies. Larger basis sets such as DZP improve the frequencies in situations that involve more complex chemical bondings. The defects included here are  \( H_{BC} \) ,  \( H_{2} \) ,  \( \mathrm{H}_{2}^{*} \) ,  \( VH_{n} \)  (with n=1,2,3,4),  \( V_{2}H_{6} \) ,  \( HI_{2} \) , the  \( \{B,H\} \)  pair, substitutional C, interstitial O and two charge states of the A center. These defects involve a wide range of bonding configurations.

The average error of the 60 calculated modes relative to experiment is about 2%. In situations where large anharmonic contributions are present, the accuracy of the method decreases somewhat  \( (5 - 6\%) \) . This occurs, for example, when H is close to a BC position. However, in most cases the calculated frequencies are in remarkable agreement (0 to 2%) with experimental data, implying that this perturbative approach is totally justified and that the ground state density matrix calculated with SIESTA is very reliable.

## V. ACKNOWLEDGMENTS

This work was supported by the spanish DGESIC (Project PB96-0080-C02). J.M.P. acknowledge F.P.I. Grant from the Spanish Ministry of Science and Technology. S.K.E.'s
 

research is supported in part by a grant from the R.A. Welch Foundation, a contract from the National Renewable Energy Laboratory, and a research award from the Humboldt Foundation. P.O. acknowledges support from Fundación Ramón Areces and Spain’s MCyT project BFM2000-1312-C02-01, as well as the use of computational resources from CESCA and CEPBA.

* Corresponding Author:pruneda@icmab.es

 \( ^{1} \)  S.J. Pearton, J.W. Corbett, and M. Stavola, “Hydrogen in Crystalline Semiconductors” (Springer-Verlag, New York, 1992).

 \( ^{2} \)  S.K. Estreicher, Mater. Sci. Eng. Rep. 14, 319 (1995).

 \( ^{3} \)  H.J. Stein, J. Electron. Mater. 1, 157 (1975).

 \( ^{4} \)  P. Deák, L.C. Snyder, and J.W. Corbett, Phys. Rev. B 37, 6887 (1988).

 \( ^{5} \)  K.G. Nakamura, K. Ishioka, M. Kitajima, and K. Murakami, Sol. St. Comm. 101, 735 (1997); K.G. Nakamura, K. Ishioka, M. Kitajima, E. Endou, M. Kubo and K. Miyamoto, J. Chem. Phys. 108, 3222 (1997).

 \( ^{6} \)  B. Tuttle and C.G. Van de Walle, Phys. Rev. B 59, 12884 (1999).

 \( ^{7} \)  R. Jones and P.R. Briddon, “The Identification of Defects in Semiconductors”, ed. M. Stavola, Semiconductors and Semimetals 51A (1998).

 \( ^{8} \)  K.J. Chang and D.J. Chadi, Phys. Rev. B 42, 7651 (1990).

 \( ^{9} \)  M. Saito, Y. Okamoto, A. Oshiyama, and T. Akiyama, Physica B 273-274, 196 (1999).

 \( ^{10} \)  R. Jones, J. Goss, C. Ewels, and S. Öberg, Phys. Rev. B 50, 8378 (1994).

 \( ^{11} \)  M.P. Allen and D.J. Tildesley, “Computer Simulation of Liquids” (Clarendon, Oxford 1987).

 \( ^{12} \)  S. Lawrence Marple, Jr., Digital Spectra Analysis with Applications (Prentice-Hall, Englewood Cliffs, NJ, 1987).

 \( ^{13} \)  J. Kohanoff, Comput. Mater. Sci 2, 221 (1994).

 \( ^{14} \)  S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001), and references therein.

 \( ^{15} \)  D. Sánchez-Portal, P. Ordejón, E. Artacho, and J.M. Soler, Int. J. Quant. Chem. 65, 453 (1997).

 \( ^{16} \)  J. M. Soler, E. Artacho, J. Gale, A. García, J. Junquera, P. Ordejón and D. Sánchez-Portal, J. Phys.: Cond. Matt (in press)
 

 \( ^{17} \)  P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964).

 \( ^{18} \)  W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).

 \( ^{19} \)  D.M. Ceperley and B.J. Alder, Phys. Rev. Lett. 45, 566 (1980).

 \( ^{20} \)  S. Perdew and A. Zunger, Phys. Rev. B 32, 5048 (1981).

 \( ^{21} \)  N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).

 \( ^{22} \)  L. Kleinman and D.M. Bylander, Phys. Rev. Lett. 48, 1425 (1982).

 \( ^{23} \)  O.F. Sankey and D.J. Niklevski, Phys. Rev. B 40, 3979 (1989); O.F. Sankey, D.J. Niklevski, D.A. Drabold, and J.D. Dow, Phys. Rev. B 41, 12750 (1990).

 \( ^{24} \)  E. Artacho, D. Sánchez-Portal, P. Ordejón, A. García, and J.M. Soler, Phys. Stat. Sol. (b) 215, 809 (1999).

 \( ^{25} \)  X. Gonze, Phys. Rev. A 52, 1096 (1995).

 \( ^{26} \)  J. M. Pruneda, J. Junquera and P. Ordejón, to be published.

 \( ^{27} \)  R.M. Sternheimer, Phys. Rev. 96, 951 (1954).

 \( ^{28} \)  T. Shimanouchi, “Molecular Vibrational Frequencies in NIST Chemistry WebBook”, NIST Standard Reference Database 69, Edited by P.J. Linstrom and W.G. Mallard, (2001).

 \( ^{29} \)  T.L. Estle, S.K. Estreicher, and D.S. Marynick, Hyp. Int. 32, 637 (1986); Phys. Rev. Lett 58, 1547 (1987).

 \( ^{30} \)  M. Budde, C.P. Cheney, G. Lüpke, N.H. Tolk, and L.C. Feldman, Phys. Rev. B 63, 195203 (2001).

 \( ^{31} \)  P.R. Briddon and R. Jones, Hyperfine Interactions 64, 593 (1990).

 \( ^{32} \)  C.G. Van de Walle, P.J.H. Denteneer, Y. Bar-Yam, and S.T. Pantelides, Phys. Rev. B 39, 10791 (1989).

 \( ^{33} \)  R.E. Pritchard, M.J. Ashwin, R.C. Newman, J.H. Tucker, E.C. Lightowlers, M.J. Binns, R. Falster, and S.A. McQuaid, Phys. Rev. B 56, 13118 (1997)

 \( ^{34} \)  B. Hourahine, R. Jones, S. Öberg, R.C. Newman, P.R. Briddon, and E. Roduner, Phys. Rev. B 57, 12666 (1998).

 \( ^{35} \)  C.G. Van de Walle, Phys. Rev. Lett. 80, 2177 (1998).

 \( ^{36} \)  J.D. Holbech, B. Bech Nielsen, R. Jones, P. Sitch, and S. Öberg, Phys. Rev. Lett. 71, 875 (1993).

 \( ^{37} \)  C.G. Van de Walle, Phys. Rev. B 49, 4579 (1994).

 \( ^{38} \)  Y-S Kim, Y-G Jin, J-W Jeong, and K.J. Chang, Semicond. Sci. Technol. 14, 1042 (1999).
 

 \( ^{39} \)  S.K. Estreicher, K. Wells, P.A. Fedders, and P. Ordejón, J. Phys. Cond. Matter 13, 6271 (2001).

 \( ^{40} \)  A.W.R. Leitch, V. Alex, and J. Weber, Phys. Rev. Lett. 81, 421 (1998)

 \( ^{41} \)  R.E. Pritchard, M.J. Ashwin, j.H. Tucker, and R.C. Newman, Phys. Rev. B 57, R15048 (1998).

 \( ^{42} \)  S.K. Estreicher, P.A. Fedders, and P. Ordejón, Physica B (in print).

 \( ^{43} \)  B.N. Mukashev, M.F. Tamendarov, and S.Zh. Tokmoldin, Mat. Sci. Forum 38-41, 1039 (1997).

 \( ^{44} \)  B. Bech Nielsen, L. Hoffmann, and M. Budde, Mater. Sci. Eng. B 36, 259 (1996)

 \( ^{45} \)  B. Bech Nielsen, L. Hoffman, M. Budde, R. Jones, J. Goss, and S. Öberg, Mater. Sci. Forum 196-201, 933 (1995).

 \( ^{46} \)  V.A. Singh, C. Weigel, J.W. Corbett, and L.M. Roth, Phys. Stat. Sol. B 81, 637 (1977).

 \( ^{47} \)  P. Deák, M. Heinrich, L.C. Snyder, and J.W. Corbett, Mater. Sci. Eng. B 4, 57 (1989); P. Deák, L.C. Snyder, M. Heinrich, C.R. Ortiz, and J.W. Corbett, Physica B 170, 253 (1991).

 \( ^{48} \)  E. V. Lavrov, J. Weber, L. Huang, and B. Bech Nielsen, Phys. Rev. B 64, 035204 (2001).

 \( ^{49} \)  B. Bech Nielsen (private communication).

 \( ^{50} \)  M. Budde, B. Bech Nielsen, P. Leary, J. Goss, R. Jones, P.R. Briddon, S. Öberg, and S.J. Breuer, Phys. Rev. B 57, 4397 (1998).

 \( ^{51} \)  See e.g. Early Stages of Oxygen Precipitation in Si, ed. R. Jones (Kluwer, The Netherlands, 1996).

 \( ^{52} \)  E. Artacho, A. Lizón-Nordström, and F. Ynduráin, Phys. Rev. B 51, 7862 (1995).

 \( ^{53} \)  H.J. Hrostowski and R.H. Kaiser, Phys. Rev. 101, 1264 (1956); T. Hallberg, L.I. Murin, J.L. Lindström, V.P. Markevich, J. Appl. Phys. 84, 2466 (1998).

 \( ^{54} \)  G.D. Watkins, and J.W. Corbett, Phys. Rev. 121, 1015 (1961); A.R. Bean, and R.C. Newman, Sol. St. Com. 9, 271 (1971).

 \( ^{55} \)  J. Coutinho, R. Jones, P.R. Briddon and S. Öberg, 2001 (to be published).

 \( ^{56} \)  M. Pesola, J. von Boehm, T. Mattila, and R.M. Nieminen, Phys. Rev. B 60, 11449 (1999).

 \( ^{57} \)  R.C. Newman and R.S. Smith, J. Phys. Chem. Sol. 30, 1943 (1969).

 \( ^{58} \)  P. Leary Ph.D. thesis, University of Exeter, 1997.

 \( ^{59} \)  M. Stavola, S.J. Pearton, J. Lopata, and W.C. Dautreumont-Smith, Phys. Rev. B 37, 8313 (1988).

 \( ^{60} \)  C.P. Herrero and M. Stutzmann, Phys. Rev. B 38, 12668 (1988).

 \( ^{61} \)  P.J.H. Denteneer, C.G. Van de Walle, and S.T. Pantelides, Phys. Rev. B 39, 10809 (1989).

 \( ^{62} \)  G.G. DeLeo and W.B. Fowler, Phys. Rev. Lett. 56, 402 (1986).
 

TABLE III: Calculated and measured frequencies for stretching modes in  \( VH_{n} \)  (n = 1, 2, 3, 4) and  \( V_{2}H_{6} \) . (a) is Ref. 44, (b) is Ref. 45, and (c) is Ref. 48. The error relative to experiment is in parenthesis. Our frequencies were obtained with a DZP basis. The measured values for the  \( VH_{2}D \) ,  \( VHD_{2} \)  and  \( VD_{3} \)  as published in Ref. 44 are now believed to belong to a divacancy complex \( ^{49} \)  and are therefore not listed here.

<table><tr><td colspan="2">expt.a</td><td>this work</td><td>Ref.b</td><td>Expt.a</td><td>this工作</td><td>Ref.b</td></tr><tr><td colspan="4">VH</td><td colspan="3">VH4</td></tr><tr><td>A&#x27;</td><td>2038</td><td>1971(-3%)</td><td>2248(+10%)</td><td>A1</td><td>2257c</td><td>2265(+0%)</td></tr><tr><td colspan="4">VD</td><td>T2</td><td>2222</td><td>2205(-1%)</td></tr><tr><td>A&#x27;</td><td>1507</td><td>1418(-6%)</td><td>1613(+7%)</td><td colspan="3">VH3D</td></tr><tr><td colspan="4">VH2</td><td>A1</td><td>2250</td><td>2251(+0%)</td></tr><tr><td>A1</td><td>2144</td><td>2163(+1%)</td><td>2316(+7%)</td><td>E</td><td>2224</td><td>2205(-1%)</td></tr><tr><td>B1</td><td>2121</td><td>2132(+1%)</td><td>2267(+7%)</td><td>A1</td><td>1620</td><td>1594(-2%)</td></tr><tr><td colspan="4">VHD</td><td colspan="3">VH2D2</td></tr><tr><td>A&#x27;</td><td>2134</td><td>2135(-0%)</td><td>2292(+7%)</td><td>A1</td><td>2244</td><td>2235(-0%)</td></tr><tr><td>A&#x27;</td><td>1555</td><td>1551(-0%)</td><td>1641(+5%)</td><td>B1</td><td>2225</td><td>2204(-1%)</td></tr><tr><td colspan="4">VD2</td><td>A1</td><td>1628</td><td>1603(-1%)</td></tr><tr><td>A1</td><td>1564</td><td>1552(-1%)</td><td>1658(+6%)</td><td>B2</td><td>1615</td><td>1585(-2%)</td></tr><tr><td>B1</td><td>1547</td><td>1532(-0%)</td><td>1625(+5%)</td><td colspan="3">VHD3</td></tr><tr><td colspan="4">VH3</td><td>A1</td><td>2236</td><td>2221(-1%)</td></tr><tr><td>A1</td><td>2185</td><td>2158(-1%)</td><td>2318(+6%)</td><td>A1</td><td>1636</td><td>1613(-1%)</td></tr><tr><td>E</td><td>2155</td><td>2100(-2%)</td><td>2256(+5%)</td><td>E</td><td>1616</td><td>1584(-2%)</td></tr><tr><td colspan="4">VH2D</td><td colspan="3">VD4</td></tr><tr><td>A&#x27;</td><td>2140</td><td>2298</td><td></td><td>A1</td><td>no-IR</td><td>1623</td></tr><tr><td>A&#x27;&#x27;</td><td>2101</td><td>2256</td><td></td><td>T2</td><td>1617</td><td>1584(-2%)</td></tr><tr><td>A&#x27;</td><td>1520</td><td>1632</td><td></td><td colspan="3">V2H6</td></tr><tr><td colspan="4">VHD2</td><td colspan="3">A1</td></tr><tr><td>A&#x27;</td><td>2121</td><td>2277</td><td></td><td>A1</td><td>2190c</td><td>2186(-0%)</td></tr><tr><td>A&#x27;</td><td>1534</td><td>1646</td><td></td><td>A2</td><td>2191</td><td>2176(-0%)</td></tr><tr><td>A&#x27;&#x27;</td><td>1509</td><td>1619</td><td></td><td>E</td><td>2166c</td><td>2143(-1%)</td></tr><tr><td colspan="4">VD3</td><td colspan="3">E</td></tr><tr><td>A1</td><td>1547</td><td>1661</td><td></td><td></td><td></td><td></td></tr><tr><td>E</td><td>1510</td><td>1619</td><td></td><td></td><td></td><td></td></tr></table>
 

TABLE IV: Calculated frequencies with a DZ basis set compared with experimental and other theoretical results for  \( HI_{2} \) . (a) is Ref. 50 and (b) is Ref. 45. The error relative to experiment is in parenthesis.

<table><tr><td colspan="2">expt.a this work</td><td>other authors</td><td>expt.a this work</td><td>Other authors</td></tr><tr><td colspan="3">IH2</td><td colspan="2">ID2</td></tr><tr><td>A</td><td>1989 2007(+1%)</td><td>2107b(+6%)</td><td>2145a(+8%)</td><td>1448 1440(-1%)</td></tr><tr><td>B</td><td>1986 2004(+1%)</td><td>2106b(+6%)</td><td>2143a(+8%)</td><td>1446 1438(-1%)</td></tr><tr><td>B</td><td>748 737(-1%)</td><td>(A) 775a(+3%)</td><td>609</td><td>590a</td></tr><tr><td>A</td><td>743 733(-1%)</td><td>(B) 768a(+3%)</td><td>601</td><td>583a</td></tr><tr><td>A</td><td>716</td><td>(B) 736a</td><td>566</td><td>564a</td></tr><tr><td>B</td><td>711</td><td>(A) 717a</td><td>562</td><td>555a</td></tr><tr><td colspan="5">IHD/IDH</td></tr><tr><td>expt.a</td><td colspan="2">this work</td><td colspan="2"><img src="imgs/img_in_image_box_1504_1634_1800_1704.jpg" ></td></tr><tr><td>1988</td><td colspan="2">2005/2007(+1%)</td><td>2106b(+6%)</td><td>2144a(+8%)</td></tr><tr><td>1447</td><td colspan="2">1440/1438(-1%)</td><td>1509b(+3%)</td><td>1540a(+6%)</td></tr><tr><td>746</td><td colspan="2">733/736(-2%)</td><td>771a(+3%)</td><td></td></tr><tr><td></td><td colspan="2">714/714</td><td>727a</td><td></td></tr></table>
 

TABLE V: Calculated and measured LVMs for interstitial O ( \( O_{i} \) ) and two charge states of the A-center ( \( VO^{0} \)  and  \( VO^{-} \) ). (a) is Ref. 53 for  \( O_{i} \)  and Ref. 54 for  \( VO^{(0/-)} \) , (b) is Ref. 55, and (c) is Ref. 56. For  \( VO^{(0/-)} \)  a DZP basis was used for O and its Si nearest-neighbors, and a DZ basis for the other Si atoms. For  \( O_{i} \) , a DZP basis was used for all the atoms in the cell.

<table><tr><td></td><td colspan="3">expt.a this work</td><td>Calcb</td><td>Calc c</td></tr><tr><td rowspan="4">O_{i}</td><td rowspan="2">A_{2u}</td><td colspan="2">D_{3d}</td><td>D_{3d}</td><td>C_{2}</td></tr><tr><td>1136</td><td>1131(-0%)</td><td>1184(+4%)</td><td>1108(-2%)</td></tr><tr><td>A_{1g}</td><td>618</td><td>607(-2%)</td><td>619(+0%)</td><td>621(+0%)</td></tr><tr><td>E_{u}</td><td>518</td><td>538(+4%)</td><td>519(+0%)</td><td>518(+0%)</td></tr><tr><td rowspan="2">VO^{0}</td><td>B_{1}</td><td>836</td><td>861(+3%)</td><td>839^{a}(+0%)</td><td>843(+1%)</td></tr><tr><td>A_{1}</td><td>534</td><td>546(+2%)</td><td>548^{a}(+3%)</td><td>540(+1%)</td></tr><tr><td rowspan="2">VO^{-}</td><td>B_{1}</td><td>885</td><td>897(+1%)</td><td>872^{a}(-1%)</td><td>850(-4%)</td></tr><tr><td>A_{1}</td><td>545</td><td>558(+2%)</td><td>532^{a}(-2%)</td><td>539(-1%)</td></tr></table>

TABLE VI: Calculated and measured frequencies for substitutional C and the {B,H} pair in Si. (a) is Ref. 57, (b) is Ref. 58, (c) is Ref. 59, (d) is Ref. 61, (e) is Ref. 62, and (f) is Ref. 60. A DZP basis was used for C and its Si nearest-neighbors, and DZ for the other atoms. For the {B,H} pair, a DZ basis was used for all the atoms.

<table><tr><td></td><td colspan="3">expt. this work other authors</td></tr><tr><td rowspan="2">C_{s}</td><td>T_{d}</td><td>607^{a}</td><td>631(+4%)</td></tr><tr><td>A</td><td>1903^{c}</td><td>1958(+3%)</td></tr><tr><td>\{B,H\}</td><td></td><td></td><td>1880^{e}(-1%)</td></tr><tr><td></td><td>E</td><td>652</td><td>695(+6%)</td></tr></table>
 
