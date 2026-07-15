# Phonon dispersion relation in rhodium: *Ab initio* calculations and neutron-scattering investigations

A. Eichler
Institut für Theoretische Physik and Center for Computational Materials Science, Technische Universität Wien, Wiedner Hauptstrasse 8-10, A-1040 Wien, Austria

K.-P. Bohnen and W. Reichardt
Forschungszentrum Karlsruhe, Institut für Nukleare Festkörperphysik, P.O. Box 3640, D-76021 Karlsruhe, Federal Republic of Germany

J. Hafner
Institut für Theoretische Physik and Center for Computational Materials Science, Technische Universität Wien, Wiedner Hauptstrasse 8-10, A-1040 Wien, Austria

(Received 15 May 1997)

The phonon dispersion relation in face-centered-cubic rhodium has been investigated by *ab initio* local-density functional (LDF) calculations and inelastic neutron-scattering measurements. The LDF calculations have been performed both using ultrasoft pseudopotentials and a plane-wave basis and norm-conserving pseudopotentials and a mixed basis set and include also all-electron calculations at a few high-symmetry points. Theory predicts the existence of Kohn anomalies that can be interpreted in terms of the calculated Fermi surfaces. The neutron-scattering experiments confirm that the *ab initio* calculations are accurate to within 3% (including the position and amplitude of the anomalies). [S0163-1829(98)00801-7]

## I. INTRODUCTION

Over the past 40 years phonon spectra of crystals have been determined by neutron-scattering experiments for a wide class of systems ranging from elements to multicomponent materials, from metals to semiconductors, insulators, and alloys. $^{1,2}$ A notable exception is the face-centered-cubic transition metal rhodium—despite its technological importance in many catalytic applications. Very recently, detailed experimental investigations of surface phonons for the Rh(111) surface have been presented, $^{3}$ but the phonon dispersion relation in the bulk remains unknown.

With the increasing computational power of modern workstations *ab initio* calculations of phonons have become possible. These investigations are all based on density functional theory, $^{4,5}$ differ, however, in the treatment of the tightly bound core electrons and/or in the basis set used for describing the wave functions. Since very accurate full-potential calculations [e.g., full-potential linearized augmented-plane wave (FLAPW)] are very time consuming, even with modern workstations, most of the studies have been restricted to selected phonon modes using the *frozen phonon* approach. $^{6}$ Calculations of the entire phonon spectrum have been carried out in the past mostly using generalized response theory. $^{7}$ Baroni and co-workers, as well as other groups used the formalism within a plane-wave basis and pseudopotentials. $^{8-10}$ Linearized-muffin-tin-orbital (LMTO) versions $^{11,12}$ and FLAPW versions $^{13}$ have also been developed. A very useful review of response theories in lattice dynamics and related fields (with many further references) has recently been presented by Gonze. $^{14}$

An alternative method is the direct calculation of interatomic or interplanar force constants using a supercell geometry. The size of the supercell is determined by the range of the interatomic interactions which can be quite substantial for systems showing phonon anomalies such as Nb or Mo, but also Pd and Pt. This method has been used in the past mostly for simple metals $^{15}$ and more recently for semiconductors and semimetals. $^{16}$ Calculations for transition and noble metals have been restricted to Cu, Ag, Pd, and Pt using norm-conserving pseudopotentials and a mixed basis description for dealing with strongly localized $d$ electrons. $^{17,18}$ For systems with $d$ electrons a convergence of the plane-wave expansion of the wave functions is difficult to achieve, even with present-day computer resources. In all these studies, however, the main emphasis has been on surface properties and thus the bulk results have only been used to assure that the theoretical description of the bulk was consistent with the measured phonon spectra and thus also with the atomic force constants that are needed for a full understanding of the lattice dynamics. New developments in the construction of pseudopotentials (*ultrasoft pseudopotentials* $^{19,20}$) and new algorithms for the self-consistent iterative diagonalization of the LDA Hamiltonian (conjugate gradient, residuum minimization, . . . $^{21,22}$) together with increasing computer power have made it possible to deal now also with transition metals in a pure plane-wave basis. This has the advantage that an accurate calculation of the forces is simple, which is a nontrivial task in the mixed basis description of the wave functions. $^{24-27}$ Since phonon modes are very sensitive to all kinds of approximations it is now possible to assess in detail the limits inherent in the theoretical approximations (LDA) as well as in the numerical treatments (full-potential–pseudopotential; norm-conserving-potential–ultrasoft potential; mixed-basis–plane-wave basis).


In this paper we attempt to answer some of these ques- tions. Our studies have concentrated on Rh since this is one of the few elemental systems for which so far no measured phonon spectra have been published. Similar to Pd and Pt²⁸·²⁹ we expect anomalies in the dispersion relation which constitute a severe test for any theoretical treatment. Further- more the surface properties of Rh are of great interest since Rh is an important catalyst for nitric oxide reduction and hydrotreating reactions. However, before studying the sur- face, bulk properties have to be known. This becomes very obvious in connection with recent He-scattering studies on Rh(111)³ where the authors could interpret their surface re- sults only by making ad hoc assumptions concerning the bulk properties. These assumptions, however, are in contrast to our theoretical predictions (preliminary results on bulk and surface phonons for Rh have been published in Ref. 30). Our calculations are supported by recent neutron-scattering experiments, results of which are included in this paper.

The organization of this paper is as follows. In Sec. II we present the results of inelastic neutron-scattering experiments on the phonon dispersion relation of Rh, together with force- constant models fitted to the measured phonons. In Sec. III we describe briefly the supercell approach for the calculation of interplanar force constants. The size of the supercells that have to be used as a consequence of the long-range nature of interatomic forces in metals in practice excludes the use of all-electron band-structure techniques and suggests a pseudopotential-based approach. For transition metals there are the alternatives to use either a norm-conserving pseudo- potential treated within a mixed-basis description or an ultra- soft pseudopotential and a pure plane-wave basis set. Section IV is devoted to a detailed comparison of the pseudopoten- tials and a confrontation of the pseudopotential results for lattice constants, bulk modulus, and the energy of high- symmetry frozen phonons with the results of all-electron [full-potential linearized augmented-plane wave (FLAPW)] calculations. Section V describes the dispersion relation cal- culated via the ab initio force-constant method and in Sec. VI a detailed analysis of the phonon anomalies in terms of Fermi-surface nesting and electron-phonon-coupling matrix elements is given. A discussion of the relevance of our re- sults will be presented in the last section.

## II. DETERMINATION OF THE PHONON DISPERSION CURVES BY INELASTIC NEUTRON SCATTERING

### A. Experimental

Rhodium is one of the very few metallic elements for which no experimental phonon data exist in the literature. This is mainly due to the large absorption cross section for thermal neutrons of 145 barns at 2200 m/s which corre- sponds to a mean free path for absorption of 1 mm only. In order to reduce absorption losses in the various scattering configurations four differently oriented samples were cut from a commercial single crystal that had the (110) direction about 30° off the cylinder axis. Two of the samples in the shape of thin plates had the (001) axis vertical, the two oth- ers were optimized for 1-10 orientations. Measurements were performed at 297 K on the triple axis spectrometer 2T1 located at the Orphee reactor at Saclay. Doubly focussing PG002 crystals were used both for the monochromator and the analyzer in most cases. In some measurements a Cu(111) monochromator was used to improve the resolution. In a first experiment we had restricted our measurements to the (ξ00), (ξξ0), (ξξξ), and (1ξ0). directions. Analysis of the data by phenomenological models showed that the calculated phonon density of states depended much more sensitively on the number of allowed interactions than should be expected from differences in the reproduction of the phonon data in directions covered by the experiment. This clearly indicated that the experimental information was not sufficient to set up reliable lattice dynamical models. We found that the branches in the (1−ξ,ξ,ξ) direction should yield the most useful information to further pin the model parameters. For this reason additional measurements were carried out in this direction. The two upper branches can be measured in an 01-1 orientation of the sample. The lowest branch, how- ever, is polarized perpendicular to this plane and has a struc- ture factor identical to zero in this configuration. Our choice to measure this branch was to start from the 310 reciprocal lattice point in an 001 orientation of the sample and to run along the line (3−ξ,1+ξ,ξ) by continuously tilting the arcs of the goniometer of the sample.

![](./images/811807517670637569_1.jpg)

FIG. 1. Phonon frequencies of Rh at 297 K. Discrete symbols: neutron-scattering experiments. The lines are the result of a fit with a 24 parameter Born von Karman model.

### B. Results and analysis

The results of the experiment are depicted in Fig. 1. Un- certainties in the frequencies arising from the counting sta- tistics are smaller than 1%. Shifts in the low LO frequencies caused by a relaxed vertical collimation in the neutron beam have been corrected for by a computer program. Small sys- tematic errors may arise from the strong absorption in the sample and uncertainties in the calibration of the spectrom- eter. From a comparison of data obtained under different experimental configurations and reference scans on a Cu single crystal we estimate that uncertainties due to these ef- fects are well below 0.1 THz. Anomalous structures are ob- served in several branches in particular in the TA branches of the (ξξ0) direction, which reflect the topology of the Fermi surface. They will be analyzed in detail in Sec. VI. When trying to describe these features by force constant models interactions up to large distances have to be taken into ac- count which implies a large number of model parameters. We have carried out systematic studies using a variety of models in order to arrive at an optimum description of the experimental dispersion curves with a minimum of fitting

<table><caption>TABLE I. Force constants of a 24 parameter mixed TF/AS Born von Karman model in dyn/cm. The force constants for neighbors 6–9 are axially symmetric and are represented by two parameters $f_l$, $f_t$. The mean deviation between model and experiment is 0.031 THz.</caption>
<tbody><tr><th>NN</th><th colspan="5">Indices</th><th>ik</th><th colspan="4">Force constants ($\text{FI}_{ik}, f_l, f_t$)</th></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>xx</td><td>zz</td><td>xy</td><td>18431</td><td>−689</td><td>22462</td><td></td></tr>
<tr><td>2</td><td>2</td><td>0</td><td>0</td><td>xx</td><td>yy</td><td></td><td>6962</td><td>−2320</td><td></td><td></td></tr>
<tr><td>3</td><td>2</td><td>1</td><td>1</td><td>xx</td><td>yy</td><td>yz xz</td><td>3382</td><td>1408</td><td>510</td><td>1391</td></tr>
<tr><td>4</td><td>2</td><td>2</td><td>0</td><td>xx</td><td>zz</td><td>xy</td><td>496</td><td>−193</td><td>848</td><td></td></tr>
<tr><td>5</td><td>3</td><td>1</td><td>0</td><td>xx</td><td>yy</td><td>zz xy</td><td>240</td><td>453</td><td>−113</td><td>382</td></tr>
<tr><td>6</td><td>2</td><td>2</td><td>2</td><td>$f_l$</td><td>$f_t$</td><td></td><td>−1153</td><td>804</td><td></td><td></td></tr>
<tr><td>7</td><td>3</td><td>2</td><td>1</td><td>$f_l$</td><td>$f_t$</td><td></td><td>−750</td><td>−253</td><td></td><td></td></tr>
<tr><td>8</td><td>4</td><td>0</td><td>0</td><td>$f_l$</td><td>$f_t$</td><td></td><td>−696</td><td>411</td><td></td><td></td></tr>
<tr><td>9</td><td>3</td><td>3</td><td>0</td><td>$f_l$</td><td>$f_t$</td><td></td><td>1953</td><td>467</td><td></td><td></td></tr>
</tbody></table>

parameters. It turned out that the inclusion of interactions with atoms of the ninth nearest-neighbor (NN) shell (330) is crucial for a good reproduction of the anomalous structures in the branches of the 110 direction. Furthermore, it was found that the force constants of the ninth NN (330) and tenth NN (411) interactions are significantly different al- though the interatomic distances are identical. Indeed, the tenth NN force constants can be put to zero without sacrific- ing goodness of the fit. The dispersion curves in Fig. 1 were calculated with an ‘‘optimized’’ model using tensor forces (TF) up to the fifth NN and axially symmetric (AS) forces for interactions 6 to 9. The agreement between experiment and model fit is excellent. The choice of AS forces at large distances was guided by the intention to restrict the total number of fit parameters. A full TF model increases the number of parameters from 24 to 29 without significant im- provement of the fit. The parameters of the model are listed in Table I. The model was used to calculate the phonon density of states (PDOS) which is shown in Fig. 2. In spite of the complex force field the PDOS shows the typical shape of a fcc metal with dominant first NN interaction.

### III. Ab initio FORCE CONSTANT METHOD

We outline here the method which has been used to cal- culate the phonon dispersion curves. All investigations are based on total-energy and force calculations within local- density-functional theory. $^{4,5}$ To simplify the task we elimi nate the tightly bound electrons by using the pseudopotential concept. $^{32}$ To obtain the phonon dispersion curves we need to know the interatomic force constants. In principle we can calculate the force constants using a supercell approach. The displacement of a single atom within the supercell induces forces on the surrounding atoms, which can be calculated using the Hellman-Feynman theorem. From the variation of the forces with the amplitude of the displacement the force constants can be calculated. Group theory can be used torestrict the number of atomic displacements to a minimum. $^{16}$  This technique works very well with supercells of modest size (64 atoms for semiconductors such as diamond), but already for the semimetal graphite the supercells must be extended to 144 atoms. $^{33}$ For metals the interatomic forces are notoriously long ranged. In this case it is easier to start by calculating the interplanar force constants describing the coupling between lattice planes perpendicular to the disper- sion direction. These force-constants can be calculated by setting up supercells elongated along the direction one is interested in and restricted to a $(1×1)$ geometry in the plane perpendicular to it. The long dimension of these cells is de- termined by the range of interaction. For rhodium we have used cells with up to 18 lattice planes to account for the long-range interactions. Starting from the equilibrium posi- tion and distorting the central lattice plane from the equilib- rium positions in three orthogonal directions, we calculated the forces acting on all other lattice planes in the unit cell. This allows immediately the calculation of the force-constant matrices coupling the layers. Knowledge of the force- constant matrices allows to set up the dynamical matrix. Ei- genvalues and eigenvectors are obtained via diagonalization. For the high symmetry directions eigenvectors are known and eigenvalues are given in terms of reciprocal lattice sums over the dynamical matrix multiplied by the eigenvectors.

From the long-wavelength limit of the phonon dispersion the elastic constants can be determined. However, this is a very delicate procedure since small errors in long-range cou- plings are strongly influencing the result. Alternatively the elastic constants can be calculated via static deformations of the primitive unit cell either as the second derivative of the total energy with respect to the deformation or from the stress/strain relations (the stress can also be calculated via the Hellman-Feynman theorem $^{20-22,33,34}$ ).

The procedure outlined above for calculating phonon branches and elastic constants has been carried out with a norm-conserving potential $^{27,35}$ in the mixed basis representa tion and with an ultrasoft pseudopotential $^{20}$ using a plane wave basis. Technical details concerning the calculationsbased on the mixed-basis approach are given in Ref. 36 while those for the approach based on the ultrasoft pseudo- potentials can be found in Refs. 21–23.

![](./images/811807517670637569_2.jpg)

FIG. 2. Phonon density of states of Rh calculated with the model described in the text.

### IV. COMPARISON OF NORM-CONSERVING AND ULTRASOFT PSEUDOPOTENTIALS

A norm-conserving pseudopotential to be used in mixed- basis calculations was constructed according to the prescrip- tion of Hamann et al., $^{37,38}$ as adapted by Elsässer et al. $^{35}$ for a mixed-basis set appropriate to transition metals. The calcu-

![](./images/811807517670637569_3.jpg)

FIG. 3. Real-space representation of the pseudopotentials: (P1) Norm-conserving pseudopotential, (P2) ultrasoft pseudopotential.

lation is based on the Hedin-Lundqvist $^{39}$ parametrization of the exchange-correlation functional in the scalar relativistic LDF Hamiltonian. All-electron eigenvalues and eigenfunctions have been calculated for an atomic $4d^{8.5}5s^{0.25}5p^{0.25}$ reference configuration, the logarithmic derivatives of the norm-conserving pseudo-orbitals and their energy derivatives calculated at the atomic eigenvalues of the reference configuration are fitted to the all-electron functions around a cutoff radius of $R_{c,d}$=0.74 a.u., $R_{c,s}$=1.64 a.u., $R_{c,p}$=1.82 a.u. equal to the experimental nearest-neighbor distance. The angular momentum-dependent ionic pseudopotentials P1 are shown in Fig. 3(a), the $s$ component of the pseudopotential is chosen as the local pseudopotential. Figure 4(a) shows the logarithmic derivatives of the pseudo-orbitals in comparison to the all-electron values. The mixed basis consists of plane waves (cutoff energy $E_{\text{cut}}$=10.5 Ry, corresponding to 60–70 plane waves per atom) plus five localized $d$ orbitals derived from the atomic $4d$ pseudo-orbitals by cutting off the tails beyond a cutoff radius $R_{\text{cut}}$=2.55 a.u. (see Elsässer et al. $^{35}$). The mixed basis leads to a generalized eigenvalue problem which is transformed to standard form by Cholesky-decomposition and then solved numerically by straightforward diagonalization.

The principle of ultrasoft pseudopotentials is based on Vanderbilts $^{19}$ observation that the requirement of norm conservation applied to the pseudo-orbitals imposes an upper limit to the cutoff radii where the pseudo-orbitals are matched to the all-electron wave functions. Small cutoff radii lead to high cutoff energies, Vanderbilt proposed to drop the norm-conserving requirement and, in order to achieve optimum transferability, to fit the logarithmic derivatives of the all-electron wave functions at more than one reference energy. The difference between the pseudoelectron and all-electron charges within $R_{c,l}$ is described in terms of a small number of localized augmentation functions. $^{19,20}$ Plane-wave convergence can be further improved by a proper construction of the pseudo-wave-functions. Kresse and Hafner $^{20}$ proposed to follow Rappe et al. $^{40}$ in expanding the pseudo-orbitals in terms of spherical Bessel functions, choosing the minimal set of three Bessel functions $j_{l}(q_{m}r)$, $m=1,3$ with the $q_{m}$'s determined such that the logarithmic derivatives join smoothly the logarithmic derivatives of the all-electron functions and that there are $(m-1)$ nodes for $r{<}R_{c,l}$ (see Ref. 20 for details). It is also advantageous to ‘‘pseudize’’ the augmentation functions in terms of ‘‘hard-core’’ norm-conserving pseudo-orbitals with a small augmentation radius $R_{\text{aug},l}$ (see again Ref. 20 for details). The starting point is again the scalar-relativistic LDF Hamiltonian with the exchange-correlation functional constructed by Ceperley and Alder as parametrized by Perdew and Zunger. $^{41}$ The atomic reference configuration was $4d^{8}5s^{1}$, i.e., the atomic ground-state configuration. The components of the pseudopotential are described by ultrasoft pseudopotentials with cutoff radii

![](./images/811807517670637569_4.jpg)

FIG. 4. Logarithmic derivatives of the pseudopotentials $P1$ and $P2$ (dashed lines) and of the all-electron potential (full lines). The symbols mark the reference energies.

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    $a$
   </th>
   <th>
    $B$
   </th>
   <th>
    $X_{long}$
   </th>
   <th>
    $X_{trans}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    $P1$
   </th>
   <td>
    3.81
   </td>
   <td>
    283.5
   </td>
   <td>
    7.15
   </td>
   <td>
    5.56
   </td>
  </tr>
  <tr>
   <th>
    $P2$
   </th>
   <td>
    3.77
   </td>
   <td>
    308.5
   </td>
   <td>
    7.25
   </td>
   <td>
    5.80
   </td>
  </tr>
  <tr>
   <th>
    FLAPW
   </th>
   <td>
    3.77
   </td>
   <td>
    305.9
   </td>
   <td>
    7.43
   </td>
   <td>
    5.78
   </td>
  </tr>
  <tr>
   <th>
    Exp.
   </th>
   <td>
    3.80
   </td>
   <td>
    268.6
   </td>
   <td>
    7.04
   </td>
   <td>
    5.56
   </td>
  </tr>
 </tbody>
</table>
TABLE II. Lattice constant $a$ (in Å), bulkmodulus $B$ (in GPa), and phonon frequencies at the $X$ point (in THz) calculated with the pseudopotentials ($P1$ and $P2$) and within a FLAPW calculation (Ref. 43). Experimental data are from Refs. 49 and 50, and this work.

$R_{c,d}$=$R_{c,p}$=2.65 a.u. and augmentation radii for the construction of the pseudized augmentation functions of $R_{{aug},d}$=2.15 a.u. and $R_{{aug},p}$=2.36 a.u. The $s$ component was described by a norm-conserving pseudopotential with two reference energies46 and $R_{c,s}$=2.36 a.u.

For the $s$ and $d$ components one reference energy is always the eigenvalue of the atomic reference configuration, the second energy is chosen such as to span the expected band width, for the $p$ component the reference energies are $E$=0 Ry and $E$= $- 0.2$ Ry (the precise choice of the reference energies has only a small influence on the pseudopotential). The all-electron potential truncated at $R_{loc}$=1.82 a.u. was chosen as the local part of the pseudopotential. The real-space form of this pseudopotential ($P2$) and the logarithmic derivatives calculated at a distance $R$=3 a.u. are again shown in Figs. 3(b) and 4(b).

The comparison of the logarithmic derivatives with the corresponding all-electron values shows both pseudopotentials to be of comparable transferability and accuracy—with slight advantages for the ultrasoft pseudopotential $P2$. For $P2$ we have included also the $f$ states in order to demonstrate that the potential is very accurate for excited states as well. The differences of the real-space form are mainly in the description of the $d$ components and of the local part, while the $s$ and $p$ components are rather similar. The $d$ component of the ultrasoft potential is much softer—this explains the better plane-wave convergence. Note also that the components of both pseudopotentials merge with the all-electron potential at approximately the same distance from the nucleus, although the cutoff radii are formally quite different. The reason is that in the ultrasoft pseudopotential scheme as set up by Kresse and Hafner,20 the wave functions are matched $at$ $R_{c,l}$, whereas in the norm-conserving scheme of Hamann $et$ $al$.37 $R_{c,l}$ is the characteristic distance of a cutoff function varying steeply $around$ $R_{c,l}$ so that wave functions and potentials match exactly only at considerably larger distances (see also the discussion in Kresse and Hafner42). A further important difference is in the choice of the local potential—remember that the local potential acts on all angular momentum components without separate nonlocal projectors (i.e., all components with $l$&gt;2). For the norm-conserving potential $P1$ the choice of the $s$-pseudopotential leads to a weak local potential, whereas for the ultrasoft pseudopotential $P2$ the local potential is the all-electron potential truncated at a radius $R_{loc}$=1.82 a.u. and this leads to a much more attractive electron-ion interaction for the higher angular momentum components.

In Table II we compare the predictions of the static lattice properties based on the two pseudopotentials and we confront them with the results of all-electron calculations performed using the full-potential linearized augmented plane-wave (FLAPW) method31,43 and the same exchange-correlation functional as used for the ultrasoft pseudopotential. This comparison also includes phonon frequencies at the $X$ point calculated using the frozen-phonon method and a doubled unit cell. The results of this comparison shows that there is an essentially perfect agreement of the results obtained with the ultrasoft pseudopotential, whereas agreement with experiment is slightly better with the norm-conserving pseudopotential. Similar agreement between ultrasoft pseudopotentials and FLAPW has already been documented for intermetallic compounds34 and has recently been shown to extend to the structural and magnetic phase diagram of the transition metals.44 We think that it is legitimate to say that FLAPW is at the moment the most accurate LDF-based all-electron technique for calculating total energies. Hence we can see that the ultrasoft pseudopotentials reproduce the LDF standard. The remaining discrepancy with experiment represents the characteristic LDF-overbinding error. For the lighter elements (including the $3d$ series) it is well documented that generalized gradient corrections (GGC) (see, e.g., Ref. 45) lead to an improved prediction of the cohesive properties, albeit with a certain tendency to over-correct the LDF error.34,44,46,47 For the heavier elements (starting with the $4d$ series) where the LDF error decreases this leads to a situation where the GGC error becomes larger than the LDF error.46,47 In the present case the GGC prediction for the lattice constant is $a$=3.85 Å (error $+ 1.3$%) and for the bulk modulus $B$=243 GPa (error $- 9.7$%). We conclude that for the heavy elements corrections to the GGC functionals are necessary before they can be considered as a genuine improvement over LDF theory. The norm-conserving pseudopotentials agree better with experiment (although they do not reach the LDF standard). The slight improvement in the prediction of the lattice constant leads to a more substantial improvement for the bulk modulus and zone boundary frequencies. We think that apart from a weak influence from the different exchange-correlation functional the difference is to be attributed mostly to the different description of the local potential. The choice made for potential $P2$ (truncated all-electron potential) describes the interaction of the ions with the higher angular momentum components of the electronic orbitals very well, whereas with potential $P1$ this attractive interaction is underestimated with the choice of the weak $s$-electron potential.

### V. PHONON DISPERSION FROM $ab$ $initio$ CALCULATIONS

Figure 5 shows the phonon dispersions along the main symmetry directions calculated with the two sets of potentials. The calculations have been performed for supercells stretching in the direction of the phonon wave vector. For the calculation using $P1$ cells with 18 layers have been used (for calculations with 9 layers see Ref. 48), whereas the computation with $P2$ has been performed with only 12 rhodium atoms per cell. This means that (even if the forces would have infinite range) for the calculation using the first setup the frequencies at nine equidistant $k$ points along each direc-

![](./images/811807517670637569_5.jpg)

FIG. 5. Dispersion relation for rhodium calculated with norm-conserving pseudopotential $P1$ (dashed line) and ultrasoft pseudopotential $P2$ (dashed line).

tion are accurate in the sense of a frozen-phonon calculation, whereas for the second setup only six such points exist for each direction. For all other $k$ points the evaluation of the frequencies is in principle based on the assumption that the range of the forces caused by the distortion of one layer is limited only to lattice planes belonging to the same supercell. Nevertheless the agreement concerning the shape of the curves shows that already with the shorter cells the description of the dispersion relation is satisfying. Altogether the frequencies calculated with the ultrasoft pseudopotential are about $3\%$ higher than those derived from the norm-conserving potential $P1$, some phonon anomalies are more pronounced with $P1$ than with $P2$. The $3\%$ difference in the frequencies is just what we would expect on the basis of the differences in the lattice constants.

Figure 6 compares the frequencies calculated with $P2$ along all symmetry lines with the experimental values. The theoretical frequencies have been downscaled by $3\%$ to facilitate the comparison of details in the dispersion relation. This comparison demonstrates that all features of the phonon dispersion relation are adequately reproduced by the $ab$ initio calculations. The physical origin of the phonon anomalies observed along most of the symmetry directions will be discussed in more detail in the next section.

The $ab$ initio force constants can also be used to calculate the elastic constants via the method of long waves. That means that the slopes of the dispersion relation at $\Gamma$ are calculated according to
$$
\left.\frac{d \omega}{d \xi}\right|_{\xi=0}=2 \pi \sqrt{\frac{1}{m} \sum_{n=1}^{\infty} n^{2} \Phi_{n}},
\tag{1}
$$
where $\xi$ denotes the $q$-vector relative to the distance of the next reciprocal lattice point in that direction (i.e., $\xi=0.5$ at the zone boundary) and $\Phi_{n}$ is the $n$th interplanar force constant. From the calculated slopes the elastic constants can be evaluated easily. Alternatively, the elastic constants can be derived from the total energy differences calculated for the symmetric and homogeneously deformed unit cells (method of homogeneous deformations). Our results obtained with both potentials are compiled in Table III, the slopes of the dispersion relation at $\Gamma$ corresponding to the elastic constants from the homogeneous deformation method are given in Fig. 5. Whereas with potential $P2$ a reasonable consistency of both sets of elastic constants can be achieved (the discrepancy is $2.6\%$ for the bulk modulus and $7-8$ % for the shear constants), somewhat larger differences are found with the force constants derived with potential $P1$, although one would expect a better agreement for the larger cell. The reason for this discrepancy is the structure of Eq. (1). In the sum the force constants are weighted with the square of their distance, which means that the last accessible force constant for the larger cell ($P1$) has already a weight of 81, so already very small numerical errors in these force constants have a vast influence to the whole result.

![](./images/811807517670637569_6.jpg)

FIG. 6. Measured dispersion relation for rhodium (symbols). The full line indicates the calculated dispersion relation (pseudopotential $P2$) which has been scaled by $97\%$ for a better comparison.

TABLE III. Elastic constants for rhodium in GPa. The calculated results (with $P1$ and $P2$) have been obtained by homogeneous deformations of the unit cell $(A)$ and by a least square fit of the slopes of the dispersion relation in the high symmetry directions $(B)$, method of long waves, see text and Fig. 5.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th>Experiment $^{\mathrm{a}}$</th>
<th colspan="3">$P1$</th>
<th colspan="3">$P2$</th>
</tr>
<tr>
<th></th>
<th>$A$</th>
<th>$B$</th>
<th>$\Delta AB$ [%]</th>
<th>$A$</th>
<th>$B$</th>
<th>$\Delta AB$ [%]</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_{11}$</td>
<td>422.1</td>
<td>411.5</td>
<td>402.2</td>
<td>$-2.3$</td>
<td>481.8</td>
<td>477.0</td>
<td>$-1.0$</td>
</tr>
<tr>
<td>$C_{12}$</td>
<td>191.9</td>
<td>219.5</td>
<td>196.4</td>
<td>$-10.5$</td>
<td>221.9</td>
<td>236.5</td>
<td>$+6.6$</td>
</tr>
<tr>
<td>$C'$</td>
<td>115.1</td>
<td>146.0</td>
<td>102.9</td>
<td>$-29.5$</td>
<td>129.5</td>
<td>120.3</td>
<td>$-7.1$</td>
</tr>
<tr>
<td>$C_{44}$</td>
<td>194.0</td>
<td>163.0</td>
<td>162.2</td>
<td>$-0.5$</td>
<td>205.6</td>
<td>192.4</td>
<td>$-6.4$</td>
</tr>
<tr>
<td>B</td>
<td>268.6</td>
<td>283.5</td>
<td>265</td>
<td>$-6.5$</td>
<td>308.5</td>
<td>316.7</td>
<td>$+2.7$</td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$Ref. 49.

## VI. DISCUSSION OF THE ANOMALIES

In this section we will analyze the origin of the anomalies in the calculated (and measured) dispersion relation, in particular those in the transverse branches along the (110) direction following two different approaches. First we perform a purely geometrical analysis of the Fermi surface to find

possible nesting vectors for Kohn anomalies, following the method used by Miiller for investigating phonon anomalies in Pt (Ref. 29) and Pd.²⁸ The second approach includes in addition to a Fermi-surface analysis, a quantitative estimate of the strength of the electron-phonon coupling. For free-electron-like metals it has been shown⁵¹ that the interaction of the conduction electrons with the lattice vibrations changes abruptly when the sum of the phonon wave vector and a reciprocal lattice vector is just equal to $2\kappa_F$, i.e., if normal- or Umklapp-scattering processes occur between states on the Fermi sphere,

$$
|\mathbf{q}+\mathbf{G}|=|\mathbf{k}'-\mathbf{k}|_{|\mathbf{k}|=|\mathbf{k}'|=\kappa_F}=2\kappa_F. \tag{2}
$$

The physical origin of this effect is the discontinuous change in the occupation of the eigenstates at the Fermi level causing the well-known logarithmic singularity at $\mathbf{q}=2\kappa_F$ in the susceptibility of the electron gas.

In the phonon dispersion relation the effect leads to weak logarithmic singularities in $\partial\omega(\mathbf{q})/\partial\mathbf{q}$ known as Kohn anomalies. For simple metals the Kohn anomalies confirm the existence of an almost spherical Fermi surface, detailed studies have been reported, e.g., for Pb⁵² and Al.⁵³,⁵⁴ For transition metals and their compounds, the Fermi surfaces are far from spherical. However, in this case the Kohn anomalies can even be much more pronounced if the nesting condition

$$
\mathbf{q}+\mathbf{G}=\mathbf{k}'-\mathbf{k}, \tag{3}
$$

$\mathbf{k}',\mathbf{k}$ on the Fermi surface is satisfied not only for isolated points on the Fermi surface, but if the nesting vector $(\mathbf{q}+\mathbf{G})$ connects two parallel flat pieces of the Fermi surface. On this basis a detailed discussion of the origin of the strong anomalies in the phonon dispersion relations of Nb, Mo, NbC, etc., has been given by Weber et al.⁵⁶ It has also been shown that the less spectacular broad and shallow anomalies observed in the phonon spectra of Pt and Pd can be traced back to a number of nesting vectors clustering in a certain region of the Brillouin zone.²⁹,²⁸

Here we analyze the origin of the phonon anomalies marked in the dispersion relation in terms of Fermi-surface nesting. Figure 7 shows the intersection of the Fermi surfaces of the third to the sixth band with the (100) plane [constructed by mapping out the $E_n(\mathbf{k})$ surfaces on a 120 × 120 grid of $\mathbf{k}$ points as shown in Fig. 11 for the fifth band and plotting all points within 25 meV from the Fermi energy]. Our Fermi-surfaces are very similar to those described in detail by Andersen.⁵⁵ The dominant contribution to the density of states at the Fermi-level comes from flat parts of the bands around the $X$ point and along $\Gamma$-$K$. In our plots this is reflected by a broader linewidth in Fig. 7. Since the strength of the Kohn effect is proportional to the square of the electron-phonon matrix element summed over initial and final states, the scattering processes within those regions (band 5) will be by far the most important.

![](./images/811807517670637569_7.jpg)

FIG. 7. Cut through the Fermi surfaces of the third to the sixth bands along the (100) plane, calculated by mapping out the plane with 120×120 k points and marking those within an interval of 25 meV around the Fermi level.

Wave vectors $\mathbf{q}$ that satisfy the nesting condition [Eq. (3)] define the Kohn surface.²⁹,²⁸ The Kohn surfaces for intraband transitions of the fifth band within the (100) plane are shown in Fig. 8. Along the (110) direction there are in a small interval many intersections, exactly in the region where we found the anomalies in the transverse branches. In Fig. 9 some representative transitions corresponding to the Kohn anomalies in the (110) direction are sketched. All transitions but one are Umklapp processes and hence contribute to anomalies in the longitudinal as well as transverse branches.

In the second step of our analysis we estimated the influence of the electron phonon matrix elements, following an approach used by Weber.⁵⁶ Weber showed that the dominant contribution to the anomalies in Nb and Mo comes from a term (called $D_2$) describing second order corrections to the phonon eigenvalues due to first order displacements of an ion $\kappa$ in direction $\alpha$. $D_2$ is defined as

![](./images/811807517670637569_8.jpg)

FIG. 8. Cut through the Kohn surfaces along the (100) plane, see text.

![](./images/811807517670637569_9.jpg)

FIG. 9. Cut through the Fermi surface for the fifth band along the (100) plane. The arrows indicate nesting vectors corresponding to points at the (110) axes in the Kohn surface.

$$
D_{2}(\kappa \alpha, \kappa^{\prime} \beta | \mathbf{q})=-\sum_{\substack{\mathbf{k} \mu \mu^{\prime}, \mathbf{k}^{\prime}=\mathbf{k}+\mathbf{q}}} \frac{f_{\mathbf{k}^{\prime} \mu^{\prime}}-f_{\mathbf{k} \mu}}{\varepsilon_{\mathbf{k} \mu}-\varepsilon_{\mathbf{k}^{\prime} \mu^{\prime}}} g_{\mathbf{k} \mu, \mathbf{k}^{\prime} \mu^{\prime}}^{\kappa \alpha} g_{\mathbf{k}^{\prime} \mu^{\prime}, \mathbf{k} \mu}^{\kappa^{\prime} \beta}
\tag{4}
$$

with $f_{k \mu}$ being the occupancy of the electronic band $\mu$ at $k$ point $\mathbf{k}$ with the corresponding eigenvalue $\varepsilon_{\mathbf{k} \mu}$, and $g_{\mathbf{k} \mu, \mathbf{k}^{\prime} \mu^{\prime}}^{\kappa \alpha}$ the electron-phonon matrix element. Very similar analyses, but without considering the matrix elements have also been used by Sinha et al. $^{58}$ and Reese et al. $^{57}$ to explain the phonon anomalies for Yttrium and Thorium.

The sum in principle has to be carried out over all bands $\mu, \mu^{\prime}$ and all $k$ points $\mathbf{k}, \mathbf{k}^{\prime}$ that can be connected via the phonon wave vector $\mathbf{q}$. To simplify the calculation we restrict the summation to intraband transitions within the fifth band $(\mu=\mu^{\prime}=5)$ and only to $k$ points within the (100) plane. As a further simplification we use the approximation to the electron-phonon matrix-element proposed by Weber $^{56}$

$$
g_{\mathbf{k} \mu, \mathbf{k}^{\prime} \mu^{\prime}}^{\alpha} \propto\left(v_{\mathbf{k} \mu}^{\alpha}-v_{\mathbf{k}^{\prime} \mu^{\prime}}^{\alpha}\right),
\tag{5}
$$

where $v_{\mathbf{k} \mu}^{\alpha}$ is the electron velocity $\partial \varepsilon_{\mathbf{k} \mu} / \partial k_{\alpha}$. This approximation is exact in an energy band model with only $s$-like orbitals and nearest-neighbor transfer integrals. For $D_{2}$ this leads to

$$
-D_{2}^{\text {approx }}(\alpha | \mathbf{q})=c \sum_{\substack{\mathbf{k}, \mathbf{k}^{\prime}=\mathbf{k}+\mathbf{q}, \mu=5}} \frac{f_{\mathbf{k}}-f_{\mathbf{k}^{\prime}}}{\varepsilon_{\mathbf{k}}-\varepsilon_{\mathbf{k}^{\prime}}}\left(v_{\mathbf{k}}^{\alpha}-v_{\mathbf{k}^{\prime}}^{\alpha}\right)^{2}. \quad(6)
$$

In a qualitative way the approximation holds rather well, even for transition metals. In Fig. 10 we have plotted $-D_{2}^{\text {approx }}$ and $m \omega^{2}$ for the (110) and the $(1 \overline{1} 0)$ branches along the (110) direction. Because of the unknown proportionality factor in Eq. (5) we can use only arbitrary units for the representation of $-D_{2}^{\text {approx }}$. Nevertheless we see that maxima of $-D_{2}^{\text {approx }}$ coincide well with depressions in the dispersion relation.

Pronounced maxima in $-D_{2}^{\text {approx }}$ appear at phonon wave vectors linking flat parallel pieces of the Fermi surfaces that have large velocities of opposite sign in the direction of the polarization vector $\alpha$ and parallel velocities and minor dispersion in the directions orthogonal to it. When we look at the graphical representation of the Fermi surface of the fifth band in the (100) plane (Fig. 11, compare Fig. 10 for the location of the nesting vectors.) we find that the sections determined by the geometrical analysis of the Kohn curves fulfill exactly these criteria.

![](./images/811807517670637569_10.jpg)

FIG. 10. The upper curves show the phonon dispersion relation $(m \omega^{2})$ for a transverse $[(1 \overline{1} 0)$ (a) and the longitudinal (110) (b)] branch in $N / m^{2}$ , the lower ones $-D_{2}^{approx }$ for the same polarizations arbitrarily scaled, see text.

### VII. SUMMARY AND CONCLUSION

In this paper we have presented detailed experimental and theoretical studies of the lattice dynamics of face-centered-

![](./images/811807517670637569_11.jpg)

FIG. 11. Potential energy surface of the fifth band over the (100) plane. The bright stripe indicates the Fermi level.

cubic rhodium. Our inelastic neutron-scattering measure- ments demonstrate the existence of anomalous structures in several branches of the phonon dispersion relation [in par- ticular in the TA branches of the $(\xi \xi 0)$ direction] which reflect the topology of the Fermi surface.

In a first step, the measured dispersion relation has been analyzed using empirical force-constant models. We find that tensor forces up to the fifth nearest neighbors and axially symmetric forces for the interaction with the sixth to ninth neighbor shells are necessary to achieve a perfect fit with the measured phonon frequencies. This demonstrates the long- range character of the interatomic forces in transition metals.

Detailed $a b$ initio calculations of the phonon frequencies have been performed using the direct method, i.e., deriving the force constants from the forces induced by static atomic displacements in a supercell. However, due to the long-range nature of the interatomic interactions in an fcc metal a $4 \times 4 \times 4$ supercell containing 256 atoms would be required. The alternative is to derive sets of interplanar force constants from $1 \times 1 \times n$ supercells elongated in the direction of the phonon wave vector. Still such calculations require ex- tremely efficient tools for total energy calculations. At present the highest computational efficiency is certainly of- fered by pseudopotential codes. Because even today the ac- curacy of pseudopotential techniques applied to transition metals is not entirely undisputed, we performed a detailed comparative study based on conventional norm-conserving pseudopotentials and a mixed basis set and on ultrasoft pseudopoentials and a pure plane-wave basis on the other hand. For comparison static lattice properties and $X$-point phonons have also been computed using the full-potential linearized augmented-plane wave (FLAPW) method. The re- sults may be briefly summarized as follows: All-electron and ultrasoft pseudopotentials produce virtually identical results, the difference between theory and experiment is $\approx 0.7 \%$ in the lattice constant and $\approx 3 \%$ in the phonon frequencies. The norm-conserving pseudopotential leads to slightly better agreement with experiment $(\approx 0.2 \%$ in the lattice constant, $\lesssim 1 \%$ in the phonon frequencies), but is slightly off the "ex act" LDA result provided by the FLAPW calculations. A detailed analysis shows that-apart from a small difference coming from slightly different exchange-correlation functionals-the observed difference has to be attributed to a different choice of the local component of the pseudopoten- tial.

The excellent agreement between theory and experiment includes also the quantitative description of the phonon anomalies. A detailed analysis of the Fermi and Kohn sur- faces establishes a one-to-one correlation between the posi- tions of the observed and calculated phonon anomalies and nesting vectors connecting flat pieces of the Fermi surface. A quantitative analysis of the strength of the anomalies has been performed along the lines proposed by Weber, $^{56}$ i.e., calculating the dominant contribution to the dynamical ma- trix in second-order perturbation theory and approximating the electron-phonon matrix element in terms of the differ- ence in the electron velocities on the regions of the Fermi surface connected by the phonon wave vectors. This analysis shows that-as proposed by Weber-dominant phonon anomalies appear at wave vectors linking flat regions on the Fermi-surface with large and opposite electron velocities in the direction of the phonon polarization vector and only weak dispersion in the perpendicular directions.

In summary our work shows that pseudopotential tech- niques may now be used to predict the lattice dynamics of transition metals with very high accuracy and to provide a detailed understanding of the origin of phonon anomalies and their relation to details of the electronic structure. On a more technical level we find that different types of pseudo- potentials can do the job-with very careful chosen pseudo- potentials even $100 \%$ agreement with the most accurate all electron calculations can be achieved. A certain advantage of the ultrasoft pseudopotentials and the plane-wave basis is that the iterative techniques for the ground-state calculation show better scaling properties and hence can be extended to even more complex systems.

## ACKNOWLEDGMENTS

We thank Dr. Walter Wolf for performing the FLAPW calculations. The Karlsruhe-Wien cooperation was supported by the Human Capital and Mobility Network " $A b$ initio(from electron structure) calculation of complex processes in solids'' (EU Contract No. ERBCHRXCT930369), supported in Austria by the Austrian Science Foundation under Project No. P10015-PHYS.

$^{1}$ H. Bilz and W. Kress, Phonon Dispersion Relations in Insulators(Springer, Berlin, 1979).

$^{2}$ Zahlenwerte und Funktionen aus Naturwissenschaft und Technik, Landolt-Börnstein, New Series III, Vol. 13a (Springer, Berlin,1981).

$^{3}$ Ch. Wöll and G. Witte, Surf. Sci. 323, 228 (1995).

$^{4}$ P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964); W. Kohn and L. J. Sham, ibid. 140, A1133 (1965); W. Kohn, in Highlights of Condensed Matter Theory, edited by M. P. Tosi, M. Fumi, and F. Bassani (North-Holland, Amsterdam, 1985).

$^{5}$ R. O. Jones and O. Gunnarsson, Rev. Mod. Phys. 61, 689 (1989).

$^{6}$ K. Kunc, in Electronic Structure, Dynamics, and Quantum Struc tural Properties of Condensed Matter, edited by J. T. Devreese and P. van Camp (Plenum, New York, 1985).

$^{7}$ S. Baroni, P. Giannozzi, and A. Testa, Phys. Rev. Lett. 58, 1861(1987); R. D. King-Smith and R. J. Needs, J. Phys.: Condens. Matter 2, 3431 (1990).

$^{8}$ P. Giannozzi, S. de Gironcoli, P. Pavone, and S. Baroni, Phys. Rev. B 43, 7231 (1991).

$^{9}$ P. Pavone, K. Karch, O. Schütt, W. Windl, D. Strauch, P. Gian nozzi, and S. Baroni, Phys. Rev. B 48, 3156 (1993).

$^{10}$ C. Bungaro, S. de Gironcoli, and S. Baroni, Phys. Rev. Lett. 77,2491 (1996).

$^{11}$ S. Y. Savrasov, Phys. Rev. Lett. 69, 2819 (1992); S. Y. Savrasov, D. Y. Savrasov, and O. K. Andersen, ibid. 72, 372 (1994).

$^{12}$ S. Y. Savrasov, Phys. Rev. B 54, 16470 (1996); S. Y. Savrasov and D. Y. Savrasov, ibid. 54, 16487 (1996).

¹³R. Yu and H. Krakauer, Phys. Rev. B **49**, 4467 (1994); Phys. Rev. Lett. **74**, 4067 (1995).

¹⁴X. Gonze, Phys. Rev. B **55**, 10 337 (1996); X. Gonze and Ch. Lee, *ibid.* **55**, 10 355 (1996).

¹⁵W. Frank, C. Elsässer, and M. Fähnle, Phys. Rev. Lett. **74**, 1791 (1995).

¹⁶G. Kresse, J. Furthmüller, and J. Hafner, Europhys. Lett. **32**, 729 (1995).

¹⁷K. M. Ho and K. P. Bohnen, Europhys. Lett. **4**, 435 (1987).

¹⁸K.-M. Ho, C. L. Fu, and B. N. Harmon, Phys. Rev. B **29**, 1575 (1984).

¹⁹D. Vanderbilt, Phys. Rev. B **41**, 7892 (1990).

²⁰G. Kresse, thesis, Technische Universität Wien, 1993; G. Kresse and J. Hafner, J. Phys.: Condens. Matter **6**, 8245 (1994).

²¹G. Kresse and J. Hafner, Phys. Rev. B **47**, RC558 (1993); **48**, 13 115 (1994); **49**, 14 251 (1994).

²²G. Kresse and J. Furthmüller, Comput. Mater. Sci. **6**, 15 (1996).

²³G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11 169 (1996).

²⁴P. Pulay, Mol. Phys. **17**, 197 (1969).

²⁵K. M. Ho, C. L. Fu, and B. N. Harmon, Phys. Rev. B **28**, 6687 (1983).

²⁶S. Goedecker and K. Maschke, Phys. Rev. B **45**, 1597 (1992).

²⁷K. M. Ho, C. Elsässer, C. T. Chan, and M. Fähnle, J. Phys.: Condens. Matter **4**, 5189 (1992).

²⁸A. P. Miiller, Can. J. Phys. **53**, 2491 (1975).

²⁹D. H. Dutton, B. N. Brockhouse, and A. P. Miiller, Can. J. Phys. **50**, 2915 (1972).

³⁰K.-P. Bohnen, A. Eichler, and J. Hafner, Surf. Sci. **368**, 222 (1996).

³¹E. Wimmer, H. Krakauer, M. Weinert, and A. J. Freeman, Phys. Rev. B **24**, 864 (1981); H. J. F. Jansen and A. J. Freeman, *ibid.* **30**, 561 (1984).

³²D. J. Singh, *Planewaves, Pseudopotentials and the LAPW Method* (Kluwer Academic, Boston, 1994).

³³G. Kresse, J. Furthmüller, and J. Hafner (unpublished).

³⁴R. Stadler, W. Wolf, R. Podloucky, G. Kresse, J. Furthmüller, and J. Hafner, Phys. Rev. B **54**, 1729 (1996).

³⁵C. Elsässer, N. Takeuchi, K. M. Ho, C. T. Chan, P. Braun, and M. Fähnle, J. Phys.: Condens. Matter **2**, 4371 (1990).

³⁶K. P. Bohnen and K. M. Ho, Surf. Sci. Rep. **19**, 99 (1993).

³⁷D. R. Hamann, M. Schlüter, and C. Chiang, Phys. Rev. Lett. **43**, 1494 (1979).

³⁸G. B. Bachelet and M. Schlüter, Phys. Rev. B **25**, 2103 (1982).

³⁹L. Hedin and B. I. Lundqvist, J. Phys. C **4**, 2064 (1971).

⁴⁰A. M. Rappe, K. M. Rabe, E. Kaxiras, and J. D. Joannopoulos, Phys. Rev. B **41**, 1227 (1990).

⁴¹J. P. Perdew and A. Zunger, Phys. Rev. B **23**, 5048 (1981).

⁴²G. Kresse, J. Hafner, and R. J. Needs, J. Phys.: Condens. Matter **4**, 7451 (1992).

⁴³W. Wolf (private communication).

⁴⁴E. Moroni, G. Kresse, J. Hafner, and J. Furthmüller, Phys. Rev. B **56**, 15 629 (1997).

⁴⁵J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B **46**, 6671 (1992).

⁴⁶G. Kresse, J. Furthmüller, and J. Hafner, Phys. Rev. B **50**, 13 181 (1994).

⁴⁷K. Seifert, J. Hafner, J. Furthmüller, and G. Kresse, J. Phys.: Condens. Matter **7**, 3683 (1995).

⁴⁸G. Nolte, Diploma thesis, University Karlsruhe, 1995.

⁴⁹E. Walker, J. Ashkenazi, and M. Dacorogna, Phys. Rev. B **24**, 2254 (1981).

⁵⁰P. Villars and L. D. Calvert, *Pearson's Handbook of Crystallographic Data for Intermetallic Phases* (American Society for Metals, Metals Park, Ohio, 1985).

⁵¹W. Kohn, Phys. Rev. Lett. **2**, 393 (1959).

⁵²B. N. Brockhouse, T. Arase, G. Caglioti, K. R. Rao, and A. D. B. Woods, Phys. Rev. **128**, 1099 (1962).

⁵³R. Stedmann and G. Nilsson, Phys. Rev. **145**, 492 (1966).

⁵⁴J. Hafner and P. Schmuck, Phys. Rev. B **9**, 4138 (1974).

⁵⁵O. K. Andersen, Phys. Rev. B **2**, 883 (1970).

⁵⁶W. Weber, in *Superconductivity of d- and f-Band Metals*, edited by H. Suhl and M. B. Maple (Academic, New York, 1980); C. M. Varma and W. Weber, Phys. Rev. Lett. **39**, 1094 (1977).

⁵⁷R. A. Reese, S. K. Sinha, and D. T. Peterson, Phys. Rev. B **8**, 1332 (1973).

⁵⁸S. K. Sinha, T. O. Brun, L. D. Muhlestein, and J. Sakurai, Phys. Rev. B **1**, 2430 (1970).