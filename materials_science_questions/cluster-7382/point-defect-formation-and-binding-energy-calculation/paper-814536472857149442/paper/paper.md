Accepted Manuscript

First-principles study of interactions between substitutional solutes in bcc iron

O.I. Gorbatov, A. Hosseinzadeh Delandar, Yu N. Gornostyrev, A.V. Ruban, P.A. Korzhavyi

![](./images/814536472857149442_1.jpg)

PII:
S0022-3115(16)30127-1

DOI:
10.1016/j.jnucmat.2016.04.013

Reference:
NUMA 49661

To appear in:
*Journal of Nuclear Materials*

Received Date: 29 November 2015

Revised Date: 15 March 2016

Accepted Date: 7 April 2016

Please cite this article as: O.I. Gorbatov, A.H. Delandar, Y.N. Gornostyrev, A.V. Ruban, P.A. Korzhavyi, First-principles study of interactions between substitutional solutes in bcc iron, *Journal of Nuclear Materials* (2016), doi: 10.1016/j.jnucmat.2016.04.013.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

First-principles study of interactions between
substitutional solutes in bcc iron

O. I. Gorbatov$^{a,b,c}$, A. Hosseinzadeh Delandar$^{a}$, Yu. N. Gornostyrev$^{b,d}$,
A. V. Ruban$^{a,e}$, P. A. Korzhavyi$^{a,d}$

$^{a}$Department of Materials Science and Engineering, KTH Royal Institute of Technology,
SE-100 44 Stockholm, Sweden
$^{b}$Institute of Quantum Materials Science, Ekaterinburg 620107, Russia
$^{c}$Nosov Magnitogorsk State Technical University, Magnitogorsk 455000, Russia
$^{d}$Institute of Metal Physics, Ural Division RAS, Ekaterinburg 620219, Russia
$^{e}$Materials Center Leoben, 8700 Leoben, Austria

**Abstract**

Using density functional theory based calculations, employing the locally
self-consistent Green's function method and the projected augmented wave
method, we develop a database of solute-solute interactions in dilute alloys
of bcc Fe. Interactions within the first three coordination shells are computed
for the ferromagnetic state as well as for the paramagnetic (disordered local
moment) state of the iron matrix. The contribution of lattice relaxations to the
defect interaction energy is investigated in the ferromagnetic state. Implications
of the obtained results for modelling the phenomena of point defect clustering
and phase precipitation in bcc Fe-based alloys and steel are discussed.

Keywords: iron, substitutional defects, interactions, *ab initio* calculations

## 1. Introduction

Alloying is an important instrument of materials development which provides
an efficient way to control their structural state and properties [1]. Alloying ad-
ditions play a crucial role in iron-based alloys and steel exerting a significant
effect on their physical and chemical properties, phase stability and kinetics of
phase transformations. For example, in low carbon pipeline steels microalloy-
ing by Ti, Nb, and V provides not only dispersion strengthening, but also a
refinement of the grain structure (due to the suppression of recrystallization)
beneficial for the mechanical properties [2]. The additions of Ni, Mn, and Cr
(combined with alloying by Mo, Al, Ti, and Cu) are used to improve the strength
and plasticity of maraging steels for automotive applications [3, 4, 5]. However,
the precipitation can result in extra hardening and embrittlement in over-aged
alloys; this process is greatly accelerated under irradiation in reactor pressure
vessel steels [6].

Effective interactions of point defects are necessary input data for a sys-
tematic analysis of the structure, stability, and formation kinetics of various

Preprint submitted to *Journal of Nuclear Materials*
April 8, 2016

point defect arrangements that can then evolve into precipitates of metastable or stable phases in the alloy matrix. The knowledge of solute-solute as well as solute-vacancy interactions, which control the above mentioned processes in the bcc ($\alpha$-Fe) matrix, is therefore of practical value as it enables us to predict the microstructure evolution and the mechanical behavior of these alloys. Also, it enables assessments of radiation damage effects, offering new insight into the origin of temperature- and dose-dependent response of ferritic and ferritic- martensitic steels to irradiation, a problem of pivotal significance for nuclear energy applications [20, 21]. For example, the thermal stability of late bloom- ing phases in reactor pressure vessel steels is under discussion [7, 22, 23].

Unfortunately, the solute-solute interaction energies cannot be directly mea-
sured in an experiment. They can be evaluated, by means of thermodynamic models, from the phase diagrams or short-range order measurements [8]. The experimental data on the solute-solute interactions in iron are scarce [9, 10, 11,12, 13], and typically the data are not available simultaneously for the tempera-
ture ranges above and below the Curie temperature [14] in which the interactions are expected to be quite different [15].

The so-called CALculation of PHAse Diagrams (CALPHAD) method [16] of thermodynamic modeling, which is based on the empirical data and the laws of equilibrium thermodynamics, is widely used to predict phase equilibria in multicomponent systems. As has been shown, the CALPHAD method has certain limitations due to the requirement of a high degree of extrapolation in the metastable phase regions. Combining this method with ab initio calculations based on the electron (spin) density functional theory (DFT) [17, 18] allows one to overcome some limitations of the thermodynamic approach [19] and provides a reliable basis for developing new alloys.

Ab initio calculations allow for straightforward computations of the solute-
solute interactions in the fully ordered ferromagnetic state [24, 25], which are of interest for modeling the radiation damage in reactor pressure vessel steel [6, 26]. At the same time, technologically important temperatures for steel production are typically close to the Curie point $T_C$ where the magnetic structure is neither completely disordered nor fully ordered. As found in Refs. [14, 27], the solute-
solute interactions are very sensitive to the degree of magnetic order in Fe-based alloys. Hence, the state of magnetic order in the alloy may play a significant role in such processes as the decomposition [28, 29] and ordering [31, 32, 33] of the solid solution.

Ab initio calculated solute-solute and solute-vacancy interactions are avail-
able for most of the binary Fe-X alloys (see, for example, Refs. [27, 24, 28]). At the same time, there are few theoretical studies of ternary or multicomponent systems [29, 35, 36, 34, 37, 38, 39], in spite of their direct practical relevance. While in binary alloys of Fe with $3d$ elements only Cu and Zn solutes show a tendency to clustering, the addition of $s$-$p$ or $4d$ elements may result in the formation of a number of compounds including sulphide, phosphide, and inter-
metallic phases.

In this work, we use DFT-based methods to perform a systematic inves-
tigation of the interactions among the most important substitutional alloying

elements and impurities in steel. Namely, we consider Al, Si, P, S, Ti, V, Cr, Mn, Co, Ni, Cu, Zr, Nb, Mo, and W (in the order of increasing the atomic number) and also vacancies in bcc iron, as well as all pair combinations of these point defects.

## 2. Method of calculations

Pair interaction energies of point defects (substitutional solutes as well as vacancies) in bcc iron were obtained by means of *ab initio* calculations employing a supercell geometry. The list of solute elements, to be considered as substitutional impurities in Fe, included $3sp$ elements from Al to S, $3d$ elements from Ti to Cu, $4d$ elements Zr, Nb, and Mo, a $5d$ element W, and also vacancies. The individual point defects and their pair combinations were considered in a 128-site $(4 \times 4 \times 4)$ cubic supercell, with the two defects separated from each other by the distance of the $n$-th coordination shell radius, $n=1,2,3$. If multisite interactions are not important, as we assume here, the pair effective interactions $V_n$ for the $n$-th coordination shell (CS) can be determined in the dilute limit in the supercell total energy calculations as

$$
V_{n} \equiv V_{pq;n} = E_{pq;n} + E_{0} - E_{p} - E_{q}, \tag{1}
$$

where the $E$ terms on the right-hand side are the calculated total energies (all the supercells must be of the same size or their energies properly normalized). Subscript 0 denotes a supercell without defects, subscript $p$ and $q$ denote supercells containing single point defects $p$ and $q$, respectively, while subscript $pq;n$ denotes a supercell containing two defects $p$ and $q$ at a distance of $n$-th CS radius relative to each other.

The total energies were computed within the the generalized gradient approximation (GGA) [40] which correctly predicts the ferromagnetic bcc structure to be the ground state of iron and closely reproduces its equilibrium atomic volume [41]. The calculations employed two different electronic structure methods. First, similar to our previous studies of point defects in iron [14, 43], we used the locally self-consistent Green's function (LSGF) method [42] to compute the chemical and magnetic contributions to the point defect interactions on a rigid bcc lattice. The use of atomic sphere approximation does not allow for any local relaxation around the point defects in the LSGF method calculations. This approach can be justified for the impurity atoms having a small size misfit with the matrix, so that the relaxation effects can be neglected [43]. To evaluate the local relaxation contribution, we calculated the interactions in the ferromagnetic state by using the projector augmented wave (PAW) method [51] as implemented in the Vienna *ab-initio* simulation package (VASP) [52].

In the LSGF calculations, each atom of the supercell, together with three coordination shells around it, was considered self-consistently as a local interaction zone (LIZ) embedded in the effective medium of the LSGF method. Green's function calculations were carried out using the orbital quantum number cutoff

$l_{max}=3$. The low-lying $3s$ valence states of P and S, as well as the semi-core $3p$ states of Ti and V, $4p$ states of Zr and Nb, were included in the valence panel. For that purpose, the depth of the contour for complex energy integration was increased, whenever necessary, in order to encircle the semi-core states and the valence states altogether. A $29 \times 29 \times 29$ Monkhorst-Pack mesh of $k$-points was used for Brillouin zone integration. Vacancies were modeled using empty spheres containing no nuclear charge. Equal Wigner-Seitz radii were used for the atomic and empty spheres. The contributions of non-spherical charge density moments to the electrostatic potential and energy were taken into account via the multipole-corrected atomic sphere approximation(ASA+M) [44, 45].

The bcc-Fe matrix was considered in two different states of magnetic order, the case of a complete ferromagnetic (FM) order corresponding to $T=0$ and that of a complete magnetic disorder, a paramagnetic (PM) state corresponding to $T \gg T_{C}$, where $T_{C}$ is the Curie temperature. A comparison of these two limits enables us to predict how much (and in what direction) the solute-solute interactions may change as a result of magnetic disordering of the iron matrix. The magnetic disorder in the paramagnetic state was treated using the disordered local moment (DLM) model [46, 47] based on the coherent potential approximation (CPA) [48]. In the FM calculations, all the magnetic moments on the host (Fe) atoms were initially set to be equal in length and direction; the magnetic moments on the impurity atoms were initially set to zero. All the moments were then allowed to relax completely during the self-consistency iterations. In the DLM calculations, each lattice site of the host was considered to be occupied $50\%$ by Fe$\uparrow$ (iron spin up) and $50\%$ by Fe$\downarrow$(iron spin down) species. The magnetic moments on all the sites were given non-zero initial values and were then allowed to fully relax. A similar treatment was used for the impurity sites and even for the vacant sites. The effective alloy present at each lattice site of the supercell was treated within the CPA using an additional self-consistency loop.

In the PAW-VASP calculations, the same supercells (comprising 128 bcc lattice sites) were used as in the LSGF calculations. The plane wave basis was cut off at 350 eV. The Brillouin zone integrals were evaluated using a $4 \times 4 \times 4$ Monkhorst-Pack mesh of $k$-points. The defect interaction energies were computed at a fixed volume corresponding to the experimental room-temperature lattice parameter of pure iron, $a=0.286$ nm [49, 50]. Two series of PAW-VASP calculations were conducted: Every defect or defect pair was first considered on the undistorted bcc lattice, and then all the internal atomic coordinates for each supercell were relaxed (keeping fixed the volume and the shape of the supercell). The convergence criteria were $10^{-6}$ eV/atom for the total energy and $10^{-2}$ eV/nm for the forces.

The so obtained effective interaction can be split into the two distinct contributions

$$
V_{n}=V_{n}^{c h}+V_{n}^{s i}. \tag{2}
$$

Here $V_{n}^{c h}$ is associated with the interaction of substitutional species on sites of the ideal undistorted lattice and can be obtained using Eq. (1), $V_{n}^{s i}$ is the strain-

induced interaction, which is related to the local lattice deformation around defects and can be obtained as the difference of the relaxation energies around a pair of defects $p$ and $q$ located relative to each other at a distance of $n$-th CS, $\Delta E_{pq;n}$, and that for isolated impurities $p$ and $q$, $\Delta E_p$ and $\Delta E_q$, calculated using separate supercells:

$$
V_{n}^{\mathrm{si}}=\Delta E_{pq;n}-\Delta E_{p}-\Delta E_{q}. \tag{3}
$$

## 3. Results and discussion

### 3.1. Diagonal $X$-$X$ interactions

Table 1 shows the calculated effective interaction energies $V_n$ between two like solute atoms in FM bcc iron for the first three CSs ($n=1,2,3$) in comparison with the results of previous calculations. Hereafter, $X$-$X$ pair interactions are referred to as 'diagonal', as opposed to 'off-diagonal' $X$-$Y$ interactions considered in the next section. The interactions have been calculated by two methods: LSGF (without relaxation) and PAW-VASP (with and without relaxation of the atomic positions). A positive sign of the interaction energy corresponds to repulsion between the solutes; a negative sign indicates that formation of a solute-solute pair is energetically favorable. For impurities having $V_1>0$ (on the first CS), the alloy is stable with respect to decomposition by means of solute clustering, but the formation of short- or long-range ordered structures depends on the behavior of $V_n$ on more distant coordination shells. As can be seen from Table 1, the strongest interactions occur at the first and second nearest-neighbor distance; the magnitude of interaction energy decreases rapidly with the distance between defects. According to Ref. [24], the interactions beyond the third coordination shell are rather small; therefore, they are not considered in this study.

The interaction energies in the FM state obtained by the PAW-VASP method without local relaxations generally agree with the results obtained by LSGF method (see also Ref. [14]). The strongest effect of local relaxations is observed in the case of a S-S defect pair where the interaction energy changes sign due to the strain-induced contribution, thus resulting in an attraction between the S impurities instead of a strong repulsion. Another case of a large strain-induced contribution is observed in the Fe-P system, but the interaction energy does not change sign: the $V_1$ and $V_2$ interactions between two P impurities remain repulsive. In cases of Co, Ni, and Cu impurities in Fe the strain-induced interactions are found to be very weak. Typically, the strain-induced interaction on the second CS is less than that on the first shell, while the interaction on the third CS is even weaker (it does not exceed 0.01 eV for any of the considered solute pairs).

The interactions for the $3d$ solute elements in Fe change regularly as a function of the atomic number, and their amplitude becomes small for the elements neighboring iron [14]. Indeed, for Co and Ni, the interaction energies are close to zero, which indicates that the mutual position of two like impurities (Co or Ni) in the ferromagnetic bcc iron is inessential. Elements such as V, Cr, Co,

and Ni, whose electronic structure in the substitutional alloy differs only slightly from that of the Fe host [14], tend to stabilize the bcc phase of iron. Indeed, the phase diagrams of the Fe-Co, Fe-Ni and Fe-V systems exhibit wide regions of bcc-based solid solutions [53]. In contrast, the electronic structure of Ti sub-
stantially differs from that of the Fe host, so that the solubility of Ti in Fe islimited due to the formation of a topologically close-packed Laves phase $TiFe_{2}$ [53].

Our calculations for Ti, Nb, and Zr substitutional solutes in Fe show that the minimum interaction value $V_{n}$ is attained at the third CS, which favors the formation of intermetallic (Laves) phases in the respective binary alloys with a sufficient concentration of the solute component, although at small concen-
trations these elements do form solid solutions with iron [53]. The Al-Al and Si-Si interactions calculated in the FM state are in agreement with the results of previous calculations [32, 33]. The obtained strong repulsive interactions on the first two coordination shells and a weak attraction on the third shell are compatible with the $D_{3}$ type of short and long-range ordering reported for the Fe-Al and Fe-Si solid solutions [53].

Impurities of Cu and S in Fe hold a special place among the considered solute elements. The calculated values of Cu-Cu and S-S interactions for the first two coordination shells are negative. In the case of S, the atomic relaxation effects are very large. Without relaxation the PAW-VASP and LSGF calculations give, respectively, positive interaction values of 0.44 and 0.45 eV for the first CS. At the same time, the PAW-VASP calculations with local relaxation of atomicpositions yield an attractive interaction of -0.54 eV which is close to -0.50 eV reported in Ref. [57]. The strong strain-induced attraction for the S-S nearest-neighbor pair, as well as strong attractive interactions of S impurities with vacancies in Fe (see below), favor the precipitation of iron sulfide, which limits the solubility of sulfur in iron ferrite (the solubility is virtually zero at low temperatures). In contrast, the strain-induced interactions for Cu-Cu impurity pairs in bcc Fe are weak, the Cu clustering is mainly driven by the chemical contribution to the interactions. As noted in Ref. [14], the chemical contribution is related to the electronic structure of Fe-Cu alloys: the $3 d$ shell of $Cu$ is completely filled, so the formation of Cu-Fe bonds (at the expense of Cu-Cu and Fe-Fe bonds) is not accompanied by a decrease in energy. This factor is responsible for the decomposition of Fe-Cu solid solutions [28] and is the cause of a low solubility of copper in the ferromagnetic bcc iron. The formation of copper precipitates results in hardening and embrittlement of copper-bearing steel [6, 58]. At the same time, the clustering of S impurities with vacancies and other solutes in iron leads to the formation of sulfides (rich in Fe, Mn, and other elements) which are otherwise formed at temperatures exceeding 1000 K in $\gamma$ -Fe. These may also cause embrittlement of steel even when the sulphur content is extremely low.

**Table 1: Calculated effective interaction energies (eV) for pairs of like solutes in FM bcc Fe, in comparison with the results of previous calculations.
Negative interaction energies correspond to attraction between the solutes, positive ones correspond to repulsion.**

<table>
  <thead>
    <tr>
      <th>CS</th>
      <th></th>
      <th>Al</th>
      <th>Si</th>
      <th>P</th>
      <th>S</th>
      <th>Ti</th>
      <th>V</th>
      <th>Cr</th>
      <th>Mn</th>
      <th>Co</th>
      <th>Ni</th>
      <th>Cu</th>
      <th>Zr</th>
      <th>Nb</th>
      <th>Mo</th>
      <th>W</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>PAW-VASP (relaxed)</td>
      <td>0.13</td>
      <td>0.30</td>
      <td>0.12</td>
      <td>-0.54</td>
      <td>0.24</td>
      <td>0.26</td>
      <td>0.27</td>
      <td>0.13</td>
      <td>0.05</td>
      <td>0.08</td>
      <td>-0.22</td>
      <td>0.37</td>
      <td>0.38</td>
      <td>0.29</td>
      <td>0.36</td>
    </tr>
    <tr>
      <td></td>
      <td>PAW-VASP (unrelaxed)</td>
      <td>0.16</td>
      <td>0.42</td>
      <td>0.65</td>
      <td>0.44</td>
      <td>0.35</td>
      <td>0.32</td>
      <td>0.33</td>
      <td>0.14</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>-0.20</td>
      <td>0.70</td>
      <td>0.70</td>
      <td>0.41</td>
      <td>0.57</td>
    </tr>
    <tr>
      <td></td>
      <td>LSGF (unrelaxed), [14]</td>
      <td>0.15</td>
      <td>0.34</td>
      <td>0.57</td>
      <td>0.45</td>
      <td>0.44</td>
      <td>0.31</td>
      <td>0.24</td>
      <td>0.10</td>
      <td>0.05</td>
      <td>0.03</td>
      <td>-0.17</td>
      <td>0.82</td>
      <td>0.68</td>
      <td>0.34</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td></td>
      <td>[24, 56]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.24</td>
      <td>0.23</td>
      <td>0.24</td>
      <td>-0.08</td>
      <td>0.04</td>
      <td>-0.02</td>
      <td>-0.25</td>
      <td>0.33</td>
      <td>0.38</td>
      <td>0.28</td>
      <td>0.36</td>
    </tr>
    <tr>
      <td></td>
      <td>[25]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.35</td>
      <td>0.28</td>
      <td>0.21</td>
      <td>-0.07</td>
      <td>0.05</td>
      <td>-0.02</td>
      <td>-0.19</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[34]</td>
      <td></td>
      <td>0.31</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.28</td>
      <td></td>
      <td></td>
      <td>0.07</td>
      <td>-0.14</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[37]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.26</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[57]</td>
      <td>0.10</td>
      <td>0.30</td>
      <td>0.22</td>
      <td>-0.50</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[59]</td>
      <td>0.12</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[63]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.08</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>PAW-VASP (relaxed)</td>
      <td>0.13</td>
      <td>0.18</td>
      <td>0.07</td>
      <td>-0.23</td>
      <td>0.13</td>
      <td>0.15</td>
      <td>0.14</td>
      <td>0.14</td>
      <td>-0.01</td>
      <td>0.02</td>
      <td>-0.06</td>
      <td>0.13</td>
      <td>0.18</td>
      <td>0.16</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td></td>
      <td>PAW-VASP (unrelaxed)</td>
      <td>0.15</td>
      <td>0.24</td>
      <td>0.31</td>
      <td>0.11</td>
      <td>0.16</td>
      <td>0.14</td>
      <td>0.14</td>
      <td>0.14</td>
      <td>-0.01</td>
      <td>0.02</td>
      <td>-0.05</td>
      <td>0.37</td>
      <td>0.31</td>
      <td>0.22</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td></td>
      <td>LSGF (unrelaxed), [14]</td>
      <td>0.11</td>
      <td>0.11</td>
      <td>0.11</td>
      <td>-0.10</td>
      <td>0.11</td>
      <td>0.09</td>
      <td>0.11</td>
      <td>0.11</td>
      <td>-0.01</td>
      <td>-0.01</td>
      <td>-0.08</td>
      <td>0.36</td>
      <td>0.24</td>
      <td>0.20</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td></td>
      <td>[24, 56]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.13</td>
      <td>0.12</td>
      <td>0.12</td>
      <td>-0.04</td>
      <td>-0.01</td>
      <td>0.00</td>
      <td>-0.06</td>
      <td>0.15</td>
      <td>0.18</td>
      <td>0.16</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td></td>
      <td>[25]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.14</td>
      <td>0.12</td>
      <td>0.11</td>
      <td>-0.01</td>
      <td>-0.01</td>
      <td>0.00</td>
      <td>-0.05</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[34]</td>
      <td></td>
      <td>0.16</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.15</td>
      <td></td>
      <td></td>
      <td>0.02</td>
      <td>-0.03</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[37]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.03</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[57]</td>
      <td>0.12</td>
      <td>0.13</td>
      <td>0.03</td>
      <td>-0.24</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[59]</td>
      <td>0.12</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[63]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.08</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>PAW-VASP (relaxed)</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.09</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>0.00</td>
      <td>0.03</td>
      <td>-0.01</td>
      <td>-0.02</td>
      <td>0.00</td>
      <td>0.04</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td></td>
      <td>PAW-VASP (unrelaxed)</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.09</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.08</td>
      <td>0.00</td>
      <td>0.03</td>
      <td>-0.01</td>
      <td>-0.01</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td></td>
      <td>LSGF (unrelaxed), [14]</td>
      <td>-0.02</td>
      <td>-0.03</td>
      <td>-0.01</td>
      <td>0.04</td>
      <td>-0.02</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.03</td>
      <td>0.01</td>
      <td>-0.06</td>
      <td>-0.03</td>
      <td>0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td></td>
      <td>[24]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>-0.02</td>
      <td>-0.03</td>
      <td>0.00</td>
      <td>0.03</td>
      <td>0.03</td>
    </tr>
  </tbody>
</table>

The interactions calculated in this work generally agree with the previous results (see Table 1). Our analysis of the published data, as well of our own results, points out Mn as a special case among $3d$ solutes in Fe as the Mn-Mn interactions are extremely sensitive to the calculation details. This is related to an instability of the magnetic state of Mn atoms in bcc Fe matrix [14]. In turn, the magnitudes and directions of magnetic moments of Mn solutes and the magnetic moments on the neighboring Fe atoms are connected closely to the chemical interactions [14, 43] which are sensitive to any perturbation in the electronic subsystem [54].

In the case of Mn, there are two states having similar energies with the parallel and anti-parallel magnetic moment on Mn atom to the magnetic mo-
ment on the iron host [55]. We have chosen the magnetic configuration with the lowest energy to represent the energy of each atomic configuration. Although, in the majority of cases, the Mn atoms tend to orient their magnetic moment anti-parallel to that of the Fe host, in some cases, such as those of Mn-Mn and Mn-Si pairs bound as 2nd neighbors, the energies of anti-parallel magnetic con-
figurations are close to that in which the moment of the Mn atom(s) is oriented parallel to the magnetic moments of the host atoms. Let us note that this is the main reason for the scatter of calculated Mn-X interactions for the second CS as discussed in Ref. [37].

### 3.2. Off-diagonal $X-Y$ interactions

Among the "diagonal" X-X solute pairs considered in Sec. 3.1, only Cu-Cu and S-S pairs exhibit strong attractive interactions on the first two coordination shells. A more diverse behavior is exhibited by "off-diagonal" X-Y interactions of the considered solutes. The PAW-VASP calculated solute-solute and solute-
vacancy interactions in bcc Fe in the FM state are presented in the upper-
right part of Figure 1. The calculation details were the same as for the *relaxed* diagonal interactions presented in Table 1. The lower-left part of this Figure lists the corresponding strain-induced interactions defined by Eq. (3) and calculated as a difference between the relaxed and unrelaxed interactions.

For clarity, in Figure 1 we use grades of blue and red color to indicate the strength of attraction and repulsion, respectively, between the point defects. As can be seen from Figure 1, in most cases the interactions between the solutes are repulsive and thus do not promote solute clustering (although some of them may result in the formation of ordered phases in alloys with sufficiently high solute concentrations). Thus, the interactions of oversized $4d$ and $5d$ elements with other solutes in iron are found to be mostly repulsive. Also, for these elements one finds relatively strong strain-induced interactions. Similar to the case of diagonal X-X interactions, there are significant strain-induced contributions to the off-diagonal X-Y interactions for X, Y = P, S, Ti, V, Zr, Nb, and W elements. In other cases the strain-induced contribution is found to be small and, therefore, the interactions calculated without any relaxation can be considered as reliable.

The effect of Ni and Mn alloying on the copper clustering has been investi-
gated in several papers (see Ref. [29] and references therein). It is noteworthy that the interactions of Al and Si solutes with Cu impurities are very similar to

<table><tbody><tr><td></td><td colspan="21">Effective interactions</td></tr><tr><td></td><td></td><td>CS</td><td>Al</td><td>Si</td><td>P</td><td>S</td><td>Ti</td><td>V</td><td>Cr</td><td>Mn</td><td>Co</td><td>Ni</td><td>Cu</td><td>Zr</td><td>Nb</td><td>Mo</td><td>W</td><td>Vac</td></tr><tr><td rowspan="42">Strain-induced contribution</td><td rowspan="3">Al</td><td>1</td><td>0.17</td><td>0.11</td><td>-0.07</td><td>0.16</td><td>0.17</td><td>0.11</td><td>0.00</td><td>-0.01</td><td>-0.08</td><td>-0.15</td><td>0.21</td><td>0.23</td><td>0.19</td><td>0.26</td><td>-0.26</td></tr><tr><td>2</td><td>0.16</td><td>0.15</td><td>0.11</td><td>0.08</td><td>0.10</td><td>0.12</td><td>0.12</td><td>0.03</td><td>0.07</td><td>0.02</td><td>0.09</td><td>0.09</td><td>0.11</td><td>0.11</td><td>0.00</td></tr><tr><td>3</td><td>0.01</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.00</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.02</td><td>-0.03</td></tr><tr><td rowspan="3">Si</td><td>1</td><td>-0.07</td><td>0.24</td><td>-0.02</td><td>0.10</td><td>0.13</td><td>0.09</td><td>-0.02</td><td>0.02</td><td>-0.04</td><td>-0.12</td><td>0.11</td><td>0.16</td><td>0.15</td><td>0.24</td><td>-0.25</td></tr><tr><td>2</td><td>-0.01</td><td>0.14</td><td>0.06</td><td>0.03</td><td>0.08</td><td>0.13</td><td>0.12</td><td>0.06</td><td>0.11</td><td>0.01</td><td>0.05</td><td>0.08</td><td>0.12</td><td>0.14</td><td>-0.14</td></tr><tr><td>3</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.03</td><td>0.01</td><td>0.03</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.03</td><td>0.02</td><td>-0.04</td></tr><tr><td rowspan="3">P</td><td>1</td><td>-0.15</td><td>-0.27</td><td>-0.22</td><td>-0.04</td><td>0.05</td><td>0.03</td><td>-0.10</td><td>0.03</td><td>-0.05</td><td>-0.15</td><td>-0.14</td><td>0.01</td><td>0.06</td><td>0.16</td><td>-0.35</td></tr><tr><td>2</td><td>-0.04</td><td>-0.14</td><td></td><td>-0.08</td><td>0.00</td><td>0.07</td><td>0.14</td><td>0.08</td><td>0.06</td><td>0.07</td><td>-0.06</td><td>0.01</td><td>0.08</td><td>0.15</td><td>0.19</td><td>-0.28</td></tr><tr><td>3</td><td>-0.01</td><td>0.00</td><td></td><td>0.05</td><td>0.00</td><td>0.02</td><td>0.03</td><td>0.03</td><td>0.02</td><td>0.03</td><td>0.01</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.00</td></tr><tr><td rowspan="3">S</td><td>1</td><td>-0.29</td><td>-0.52</td><td>-0.79</td><td></td><td>-0.19</td><td>-0.03</td><td>-0.03</td><td>-0.16</td><td>0.02</td><td>-0.11</td><td>-0.28</td><td>-0.43</td><td>-0.16</td><td>-0.01</td><td>0.11</td><td>-0.53</td></tr><tr><td>2</td><td>-0.10</td><td>-0.23</td><td>-0.32</td><td></td><td>-0.03</td><td>0.09</td><td>0.14</td><td>0.03</td><td>0.01</td><td>-0.04</td><td>-0.16</td><td>-0.04</td><td>0.10</td><td>0.20</td><td>0.27</td><td>-0.39</td></tr><tr><td>3</td><td>0.01</td><td>0.00</td><td>0.00</td><td></td><td>-0.01</td><td>0.02</td><td>0.04</td><td>0.05</td><td>0.02</td><td>0.03</td><td>0.01</td><td>0.00</td><td>0.01</td><td>0.03</td><td>0.02</td><td>0.00</td></tr><tr><td rowspan="3">Ti</td><td>1</td><td>-0.11</td><td>-0.10</td><td>-0.08</td><td>-0.08</td><td></td><td>0.22</td><td>0.19</td><td>0.14</td><td>-0.01</td><td>-0.01</td><td>0.01</td><td>0.30</td><td>0.29</td><td>0.24</td><td>0.29</td><td>-0.21</td></tr><tr><td>2</td><td>-0.02</td><td>0.00</td><td>0.01</td><td>-0.03</td><td></td><td>0.13</td><td>0.12</td><td>0.09</td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.15</td><td>0.14</td><td>0.11</td><td>0.11</td><td>0.17</td></tr><tr><td>3</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.00</td><td></td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.00</td><td>0.01</td><td>0.01</td><td>0.00</td><td>-0.01</td></tr><tr><td rowspan="3">V</td><td>1</td><td>-0.10</td><td>-0.07</td><td>-0.04</td><td>-0.02</td><td>-0.08</td><td></td><td>0.25</td><td>0.22</td><td>0.06</td><td>0.10</td><td>0.07</td><td>0.28</td><td>0.29</td><td>0.27</td><td>0.30</td><td>-0.03</td></tr><tr><td>2</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.01</td><td></td><td>0.13</td><td>0.23</td><td>0.03</td><td>0.06</td><td>0.05</td><td>0.18</td><td>0.16</td><td>0.14</td><td>0.14</td><td>0.09</td></tr><tr><td>3</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td></td><td>0.03</td><td>0.04</td><td>0.01</td><td>0.03</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.02</td><td>0.01</td></tr><tr><td rowspan="3">Cr</td><td>1</td><td>-0.08</td><td>-0.05</td><td>-0.04</td><td>-0.04</td><td>-0.07</td><td>-0.07</td><td></td><td>0.20</td><td>0.10</td><td>0.14</td><td>0.04</td><td>0.23</td><td>0.28</td><td>0.27</td><td>0.30</td><td>-0.04</td></tr><tr><td>2</td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.01</td><td>0.00</td><td>-0.01</td><td></td><td>0.19</td><td>0.04</td><td>0.08</td><td>0.06</td><td>0.16</td><td>0.16</td><td>0.15</td><td>0.16</td><td>0.00</td></tr><tr><td>3</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>0.04</td><td>0.02</td><td>0.04</td><td>0.03</td><td>0.02</td><td>0.03</td><td>0.05</td><td>0.04</td><td>0.00</td></tr><tr><td rowspan="3">Mn</td><td>1</td><td>-0.04</td><td>-0.03</td><td>-0.04</td><td>-0.07</td><td>-0.04</td><td>-0.01</td><td>0.00</td><td></td><td>0.11</td><td>0.08</td><td>-0.09</td><td>0.15</td><td>0.22</td><td>0.20</td><td>0.22</td><td>-0.14</td></tr><tr><td>2</td><td>-0.01</td><td>-0.02</td><td>-0.05</td><td>-0.07</td><td>0.00</td><td>0.00</td><td>-0.01</td><td></td><td>0.05</td><td>0.10</td><td>0.03</td><td>0.09</td><td>0.25</td><td>0.22</td><td>0.22</td><td>-0.10</td></tr><tr><td>3</td><td>0.01</td><td>0.00</td><td>-0.01</td><td>-0.01</td><td>0.01</td><td>0.00</td><td>0.00</td><td></td><td>0.02</td><td>0.05</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.06</td><td>-0.03</td></tr><tr><td rowspan="3">Co</td><td>1</td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.02</td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.01</td><td></td><td>0.07</td><td>0.01</td><td>-0.03</td><td>0.03</td><td>0.08</td><td>0.08</td><td>0.04</td></tr><tr><td>2</td><td>0.00</td><td>0.00</td><td>0.00</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>-0.01</td><td>-0.01</td><td>0.03</td><td>0.05</td><td>0.06</td><td>0.07</td><td>-0.09</td></tr><tr><td>3</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.00</td></tr><tr><td rowspan="3">Ni</td><td>1</td><td>0.01</td><td>0.01</td><td>-0.02</td><td>-0.07</td><td>0.00</td><td>-0.01</td><td>-0.02</td><td>-0.01</td><td>0.00</td><td></td><td>-0.08</td><td>-0.05</td><td>0.06</td><td>0.14</td><td>0.15</td><td>-0.05</td></tr><tr><td>2</td><td>-0.01</td><td>-0.01</td><td>-0.04</td><td>-0.09</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>-0.02</td><td>0.00</td><td>0.05</td><td>0.09</td><td>0.12</td><td>-0.18</td></tr><tr><td>3</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>0.02</td><td>0.04</td><td>0.04</td><td>0.05</td><td>0.06</td><td>-0.03</td></tr><tr><td rowspan="3">Cu</td><td>1</td><td>0.02</td><td>0.00</td><td>-0.07</td><td>-0.17</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>-0.02</td><td>0.00</td><td>0.00</td><td></td><td>-0.06</td><td>0.05</td><td>0.09</td><td>0.13</td><td>-0.23</td></tr><tr><td>2</td><td>0.00</td><td>0.00</td><td>-0.04</td><td>-0.07</td><td>-0.02</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>-0.05</td><td>0.02</td><td>0.03</td><td>0.08</td><td>-0.21</td></tr><tr><td>3</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.03</td><td>-0.05</td></tr><tr><td rowspan="3">Zr</td><td>1</td><td>-0.22</td><td>-0.22</td><td>-0.25</td><td>-0.33</td><td>-0.19</td><td>-0.14</td><td>-0.11</td><td>-0.07</td><td>0.00</td><td>-0.01</td><td>-0.06</td><td></td><td>0.38</td><td>0.33</td><td>0.41</td><td>-0.65</td></tr><tr><td>2</td><td>-0.07</td><td>0.01</td><td>0.03</td><td>-0.01</td><td>-0.09</td><td>-0.02</td><td>0.00</td><td>0.00</td><td>0.01</td><td>-0.01</td><td>-0.06</td><td></td><td>0.17</td><td>0.17</td><td>0.18</td><td>0.08</td></tr><tr><td>3</td><td>0.02</td><td>0.01</td><td>-0.01</td><td>-0.02</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>-0.01</td><td>0.00</td><td></td><td>0.00</td><td>0.01</td><td>0.01</td><td>-0.07</td></tr><tr><td rowspan="3">Nb</td><td>1</td><td>-0.17</td><td>-0.14</td><td>-0.13</td><td>-0.17</td><td>-0.18</td><td>-0.13</td><td>-0.09</td><td>-0.02</td><td>0.01</td><td>0.01</td><td>-0.03</td><td>-0.34</td><td></td><td>0.34</td><td>0.39</td><td>-0.29</td></tr><tr><td>2</td><td>-0.05</td><td>0.00</td><td>0.02</td><td>-0.01</td><td>-0.06</td><td>-0.02</td><td>-0.01</td><td>0.02</td><td>0.01</td><td>-0.01</td><td>-0.03</td><td>-0.18</td><td></td><td>0.17</td><td>0.17</td><td>0.16</td></tr><tr><td>3</td><td>0.01</td><td>0.01</td><td>0.00</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td></td><td>0.03</td><td>0.03</td><td>-0.03</td></tr><tr><td rowspan="3">Mo</td><td>1</td><td>-0.13</td><td>-0.08</td><td>-0.06</td><td>-0.08</td><td>-0.13</td><td>-0.08</td><td>-0.04</td><td>-0.02</td><td>0.00</td><td>0.00</td><td>-0.02</td><td>-0.27</td><td>-0.23</td><td></td><td>0.33</td><td>-0.10</td></tr><tr><td>2</td><td>-0.02</td><td>0.00</td><td>0.01</td><td>-0.01</td><td>-0.04</td><td>-0.02</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>-0.01</td><td>-0.01</td><td>-0.10</td><td>-0.08</td><td></td><td>0.17</td><td>0.12</td></tr><tr><td>3</td><td>0.01</td><td>0.01</td><td>0.00</td><td>-0.01</td><td>0.00</td><td>-0.02</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.01</td><td>0.01</td><td></td><td>0.04</td><td>-0.01</td></tr><tr><td></td><td rowspan="3">W</td><td>1</td><td>-0.16</td><td>-0.10</td><td>-0.07</td><td>-0.09</td><td>-0.18</td><td>-0.11</td><td>-0.05</td><td>0.01</td><td>0.00</td><td>-0.01</td><td>-0.02</td><td>-0.35</td><td>-0.29</td><td>-0.16</td><td></td><td>0.06</td></tr><tr><td></td><td>2</td><td>-0.02</td><td>0.00</td><td>0.01</td><td>-0.01</td><td>-0.04</td><td>-0.02</td><td>-0.01</td><td>0.01</td><td>0.00</td><td>-0.01</td><td>-0.01</td><td>-0.11</td><td>-0.08</td><td>-0.05</td><td></td><td>0.16</td></tr><tr><td></td><td>3</td><td>0.01</td><td>0.01</td><td>0.01</td><td>-0.01</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td></td><td>0.00</td></tr><tr><td></td><td rowspan="3">Vac</td><td>1</td><td>0.03</td><td>0.02</td><td>0.04</td><td>0.08</td><td>-0.02</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.03</td><td>0.03</td><td>0.06</td><td>-0.10</td><td>-0.03</td><td>0.06</td><td>0.06</td><td></td></tr><tr><td></td><td>2</td><td>0.00</td><td>-0.03</td><td>-0.02</td><td>0.02</td><td>0.05</td><td>0.02</td><td>0.00</td><td>-0.01</td><td>-0.01</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.09</td><td>0.05</td><td>0.06</td><td></td></tr><tr><td></td><td>3</td><td>-0.03</td><td>-0.01</td><td>0.01</td><td>-0.01</td><td>-0.02</td><td>0.00</td><td>0.00</td><td>-0.01</td><td>0.00</td><td>-0.01</td><td>-0.03</td><td>-0.06</td><td>-0.03</td><td>-0.01</td><td>-0.01</td><td></td></tr></tbody></table>

Figure 1: Effective pair interactions (upper right triangle) and strain-induced interactions (bottom left triangle) for selected solute atoms and vacancies on the first, second, and third coordination shells in the FM bcc Fe. The energies are in electronvolts (eV). Negative values correspond to attraction between the species (blue), positive ones correspond to repulsion (red).

those exhibited by Ni and Mn solutes. Therefore, Al and Si alloying may also promote the Cu precipitation in steel. Also, other $3sp$ elements such as P and S are calculated to have attractive interactions with $3d$ solute elements as Ni, Mn, and Cu. These interactions favor point defect clustering and formation of the respective phosphide and sulphide precipitates in steel.

An exceptional and interesting case is that of a Co impurity, which interacts very weakly with all other elements. The reason is that the electronic structure of a Co impurity is similar to that of the ferromagnetic Fe host [14]. At the same time, Co alloying strongly affects the magnetic properties of steel [60].

Comparison of the PAW-VASP calculated off-diagonal solute-solute interactions in the ferromagnetic $\alpha$-Fe with the results of recent first-principles calculations [24, 36, 34, 57] is made in Table 2. Our results are found to be in reasonable agreement with the previously reported interaction values. Most significant deviation occurs in some Mn-X cases discussed at the end of Sec. 3.1 and in Ref. [37].

### 3.3. Vacancy-solute interactions

Vacancy-solute interactions play a crucial role in diffusion-controlled processes such as ordering or decomposition, which occur in alloys under heat treatment or under irradiation [62, 64, 65, 66, 67]. Detailed knowledge of these interactions is important for predicting long-term behavior of nuclear materials (such as reactor steels and nuclear-waste containers) as well as for advancing our general understanding of kinetic processes in alloys.

The results of the present PAW-VASP calculations of vacancy-solute interactions (negative sign of the interaction energy corresponds to vacancy-solute binding) are presented in Figure 1 and compared with recent first-principles calculations in Table 3. The obtained values show good agreement with the corresponding results obtained in Refs. [24, 68, 43].

Vacancies are found to bind to most of the solutes in Fe (see Figure 1). The mechanism of the vacancy-solute binding is not associated with the relaxation of the lattice, but has a chemical nature. The fact that strain-induced contributions to the vacancy-solute interactions are generally very small (see Figure 1) is quite remarkable. It explains why the present PAW-VASP calculations, which take local relaxations into account, agree very well with the results of unrelaxed LSGF calculations of Ref. [43]. It follows that, in most cases, local relaxations around vacancy-solute pair are similar for different configurations and their effect on the interaction energy cancels out. Notable differences are observed for the vacancy interactions with oversized Zr, Nb, Mo, and W solutes at a distance of the first or second CS radius. These differences, as well as the differences between the present PAW-VASP calculations and similar calculations of Ref. [24], show sensitivity of the result to the calculation details such as supercell size, $k$-mesh, plane-wave basis cutoff, and the treatment of volume relaxation.

Table 2: Effective pair interaction energies between substitutional solutes in FM bcc Fe, obtained using locally-relaxed PAW-VASP calculations, compared with the results of previous calculations. Negative values correspond to attraction, and positive to repulsion, between the solutes.

<table>
  <thead>
    <tr>
      <th>CS</th>
      <th></th>
      <th>Si-P</th>
      <th>Si-Cr</th>
      <th>Si-Mn</th>
      <th>Si-Ni</th>
      <th>Si-Cu</th>
      <th>P-Mn</th>
      <th>P-Ni</th>
      <th>P-Cu</th>
      <th>Cr-Mn</th>
      <th>Mn-Ni</th>
      <th>Mn-Cu</th>
      <th>Ni-Cu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>PAW-VASP</td>
      <td>0.24</td>
      <td>0.09</td>
      <td>-0.02</td>
      <td>-0.04</td>
      <td>-0.12</td>
      <td>-0.10</td>
      <td>-0.05</td>
      <td>-0.15</td>
      <td>0.20</td>
      <td>0.08</td>
      <td>-0.09</td>
      <td>-0.08</td>
    </tr>
    <tr>
      <td></td>
      <td>[34]</td>
      <td></td>
      <td></td>
      <td>-0.01</td>
      <td>-0.03</td>
      <td>-0.05</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.06</td>
      <td>-0.04</td>
      <td>-0.04</td>
    </tr>
    <tr>
      <td></td>
      <td>[35, 36]</td>
      <td>0.32</td>
      <td></td>
      <td>0.03</td>
      <td>0.00</td>
      <td>-0.06</td>
      <td>-0.15</td>
      <td>-0.13</td>
      <td>-0.13</td>
      <td></td>
      <td>0.12</td>
      <td>-0.05</td>
      <td>-0.02</td>
    </tr>
    <tr>
      <td></td>
      <td>[37]</td>
      <td></td>
      <td>0.04</td>
      <td>-0.09</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.01</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>PAW-VASP</td>
      <td>0.14</td>
      <td>0.13</td>
      <td>0.12</td>
      <td>0.11</td>
      <td>0.01</td>
      <td>0.08</td>
      <td>0.07</td>
      <td>-0.06</td>
      <td>0.19</td>
      <td>0.10</td>
      <td>0.03</td>
      <td>-0.02</td>
    </tr>
    <tr>
      <td></td>
      <td>[34]</td>
      <td></td>
      <td></td>
      <td>0.33</td>
      <td>0.11</td>
      <td>0.05</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.11</td>
      <td>0.07</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td></td>
      <td>[35, 36]</td>
      <td>0.13</td>
      <td></td>
      <td>0.36</td>
      <td>0.12</td>
      <td>0.05</td>
      <td>0.05</td>
      <td>0.02</td>
      <td>-0.07</td>
      <td></td>
      <td>0.12</td>
      <td>-0.03</td>
      <td>-0.02</td>
    </tr>
    <tr>
      <td></td>
      <td>[37]</td>
      <td></td>
      <td>0.08</td>
      <td>0.04; 0.08</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.04</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Table 3: Vacancy-solute interactions (eV) in FM bcc Fe, obtained using locally-relaxed PAW-VASP calculations, in comparison with the results of previous calculations of Refs. [24, 34, 62, 63, 66, 68]. Negative values correspond to attraction between the species, positive ones correspond to repulsion.

<table>
  <thead>
    <tr>
      <th>CS</th>
      <th></th>
      <th>Al</th>
      <th>Si</th>
      <th>P</th>
      <th>S</th>
      <th>Ti</th>
      <th>V</th>
      <th>Cr</th>
      <th>Mn</th>
      <th>Co</th>
      <th>Ni</th>
      <th>Cu</th>
      <th>Zr</th>
      <th>Nb</th>
      <th>Mo</th>
      <th>W</th>
      <th>Vac</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>PAW-VASP</td>
      <td>-0.26</td>
      <td>-0.25</td>
      <td>-0.35</td>
      <td>-0.53</td>
      <td>-0.21</td>
      <td>-0.03</td>
      <td>-0.04</td>
      <td>-0.14</td>
      <td>0.04</td>
      <td>-0.05</td>
      <td>-0.23</td>
      <td>-0.65</td>
      <td>-0.29</td>
      <td>-0.10</td>
      <td>-0.06</td>
      <td>-0.28</td>
    </tr>
    <tr>
      <td></td>
      <td>[24]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.24</td>
      <td>-0.06</td>
      <td>-0.06</td>
      <td>-0.21</td>
      <td>0.01</td>
      <td>-0.12</td>
      <td>-0.27</td>
      <td>-0.73</td>
      <td>-0.37</td>
      <td>-0.17</td>
      <td>-0.12</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[34]</td>
      <td></td>
      <td></td>
      <td>-0.24</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.12</td>
      <td></td>
      <td>-0.03</td>
      <td>-0.17</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.14</td>
    </tr>
    <tr>
      <td></td>
      <td>[43]</td>
      <td>-0.31</td>
      <td>-0.24</td>
      <td>-0.32</td>
      <td>-0.55</td>
      <td>-0.18</td>
      <td>-0.04</td>
      <td>-0.05</td>
      <td>-0.17</td>
      <td>-0.01</td>
      <td>-0.14</td>
      <td>-0.26</td>
      <td>-0.43</td>
      <td>-0.18</td>
      <td>-0.09</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[62]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.17</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[63]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[66]</td>
      <td></td>
      <td></td>
      <td>-0.30</td>
      <td>-0.38</td>
      <td></td>
      <td></td>
      <td>-0.05</td>
      <td>-0.17</td>
      <td></td>
      <td>-0.10</td>
      <td>-0.26</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[68]</td>
      <td></td>
      <td></td>
      <td>-0.29</td>
      <td>-0.36</td>
      <td>-0.22</td>
      <td>-0.04</td>
      <td>-0.05</td>
      <td>-0.16</td>
      <td></td>
      <td></td>
      <td>-0.24</td>
      <td></td>
      <td></td>
      <td>-0.33</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>PAW-VASP</td>
      <td>0.00</td>
      <td>-0.14</td>
      <td>-0.28</td>
      <td>-0.39</td>
      <td>0.17</td>
      <td>0.09</td>
      <td>-0.01</td>
      <td>-0.10</td>
      <td>-0.09</td>
      <td>-0.18</td>
      <td>-0.21</td>
      <td>0.08</td>
      <td>0.16</td>
      <td>0.12</td>
      <td>0.16</td>
      <td>-0.26</td>
    </tr>
    <tr>
      <td></td>
      <td>[24]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.17</td>
      <td>0.09</td>
      <td>-0.01</td>
      <td>-0.14</td>
      <td>-0.10</td>
      <td>-0.20</td>
      <td>-0.16</td>
      <td>0.07</td>
      <td>0.14</td>
      <td>0.11</td>
      <td>0.15</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[34]</td>
      <td></td>
      <td></td>
      <td>-0.14</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.07</td>
      <td></td>
      <td>-0.18</td>
      <td>-0.19</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.28</td>
    </tr>
    <tr>
      <td></td>
      <td>[43]</td>
      <td>-0.03</td>
      <td>-0.12</td>
      <td>-0.27</td>
      <td>-0.44</td>
      <td>0.11</td>
      <td>0.06</td>
      <td>-0.03</td>
      <td>-0.10</td>
      <td>-0.10</td>
      <td>-0.20</td>
      <td>-0.21</td>
      <td>0.08</td>
      <td>0.11</td>
      <td>0.05</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[62]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.18</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[63]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.09</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[66]</td>
      <td></td>
      <td></td>
      <td>-0.11</td>
      <td>-0.27</td>
      <td></td>
      <td></td>
      <td>-0.01</td>
      <td>-0.11</td>
      <td></td>
      <td>-0.20</td>
      <td>-0.17</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>[68]</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.10</td>
      <td>-0.19</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Strong vacancy-solute binding obtained for the 3sp solute elements deserves a special remark. Although the Mn-Si and Ni-Si solute pairs exhibit weak attraction at the first CS, due to the attractive interactions of these elements with vacancies (which are especially strong in the vacancy-Si case, see Sec. 3.3) these defect pairs can self-assemble into Mn-Ni-Si precipitates [61] in irradiated pressure vessel steel of light water reactors. Their precipitation may potentially cause hardening and embrittlement of the vessel at high neutron fluence [7, 23].

Other sp elements, such as P and S, are also found to attract to Mn, Ni, Cu, Zr, Nb, as well as to vacancies, and these interactions may result in the formation of phosphide or sulphide precipitates in steel.

We note that the vacancy-solute interactions reported in this paper have been obtained using the PBE exchange-correlation functional [40]. Another functional, so-called PBEsol [69], has been designed to take the large gradient of the electron density near the vacant site more accurately into account than the PBE. However, very similar point defect interactions were obtained in our test PAW-VASP calculations with PBE and PBEsol. For example, the maximum deviation of 0.03 eV was obtained for the vacancy-S interaction.

### 3.4. Effect of magnetic disordering

The impact of magnetic order on interactions has been investigated using LSGF calculations on a rigid lattice and in the low concentration limit. For this purpose two limiting cases, one corresponding to the fully ordered ferromagnetic state and the other to a completely disordered paramagnetic state, respectively, have been considered. The LSGF calculations of the interactions for the FM state were carried out at a fixed volume corresponding to the experimental low-temperature lattice parameter of pure iron ($a = 0.286$ nm [49, 50]), while the calculations for the paramagnetic (DLM) state were done at a high-temperature lattice parameter $a = 0.290$ nm [50].

In contrast to the PAW-VASP methodology employed in the calculations discussed in Sections 3.1-3.3, the LSGF method uses a shape approximation for the crystal potential and, therefore, cannot take into account the local lattice relaxations around point defects. One important advantage of the LSGF method is its efficiency in modeling the paramagnetic state by means of the disordered local moment approach [46, 47]. Alternative approaches based the PAW-VASP method and employing randomized magnetic structures have been developed [72, 73, 74, 75, 76], but are computationally very expensive. We note that, in spite of the differences between the methods, the solute-solute and vacancy-solute interactions calculated using PAW-VASP and LSGF methods in ferromagnetic iron are almost identical for the 3d elements and reasonably small for other point defects considered, as long as the relaxation effects are small, see Figures 1 and 2 and Tables 1 and 2. Sizeable differences are obtained for the interactions of 3p elements with 4d elements, as well as for the interactions of 3p elements with one another (it is noteworthy that the maximum difference often occurs on the second CS).

As Table 1 shows, the differences are mainly due to the unrelaxed supercell geometry used in the LSGF calculations (note that unrelaxed interactions

obtained using LSGF and PAW-VASP methods are very similar). In addition to the effect of local relaxations, the differences can be partly ascribed to the features of two methods used. For instance, the interactions calculated using LSGF are slightly more negative (or less positive) than the interactions calculated using PAW-VASP. This "over-binding" most probably originates from the same atomic sphere approximation that does not allow for atomic relaxations in LSGF calculations. We rely on the similarity of interactions calculated by the two methods for the unrelaxed supercell geometry and use LSGF method to investigate the effect of magnetism (separately from the relaxation effects that are obtained from PAW-VASP calculations and shown as the strain-induced contribution in Figure 1).

The calculated solute-solute interaction energies on the first, second, and third coordination shells for the ferromagnetic (FM) and paramagnetic (DLM) states of the Fe matrix are shown in Figure 2. As can be seen from the Figure, the magnetic disordering of the iron matrix (accompanied by the difference in the lattice parameter between the high-temperature PM state and the low-temperature FM state of bcc Fe) produces strong effect on the solute-solute interactions. The transition from the ferromagnetic to the paramagnetic state is accompanied in almost all cases by a decrease in the absolute value of the interaction energy $|V_{n}|$; the most substantial change in $V_{n}$ is observed for V, Cr, Mn, and Cu [14]. For Cr-Cr solute pairs, the nearest-neighbor interaction $V_{1}$ changes sign, which was previously discussed in Ref. [27]. The interaction is repulsive in the ferromagnetic state and attractive in the paramagnetic state.

For the solutes whose diagonal interactions are strongly affected by magnetic disordering (see Figure 2a) one can expect the occurrence of a bending or a kink on the solubility line at its intersection with the concentration dependence of the Curie temperature $T_{C}$ on the corresponding binary phase diagram. Note that these features can be weakly manifested in the real phase diagrams because of both the measurement errors and the neglect (in our consideration) of the effects of short-range magnetic order, which are especially significant in $\alpha$-Fe at temperature $T \approx T_{C}$.

Among the elements considered above, S and Cu are the only solutes for which the diagonal X-X interactions are attractive $(V<0)$ in both the ferromagnetic and paramagnetic states. In agreement with Ref. [28] the calculations predict quite different value of Cu-Cu interactions for the FM and PM states of the iron matrix. As a result, the contribution of magnetism leads to a strong bending of the solubility line at the Curie temperature in the Fe-Cu system [77, 78, 79].

The V, Cr, Mn, Co, and Ni elements are well soluble in the bcc iron; therefore, the contribution from magnetism to the effective interactions manifests itself in the specific features of their phase diagrams at large concentrations of the alloying elements [77]. In particular, the contribution of magnetism is revealed in the change of the stability of the ordered phases in the Fe-Co [30, 31], Fe-Ni [80], and Fe-Cr [81, 82] systems due to the transition to the paramagnetic state.

Our calculations show (see Figure 2b) that off-diagonal X-Y type interac-

![](./images/814536472857149442_2.jpg)

Figure 2: Calculated effective interaction energies (eV) of point defects in the FM and PM (DLM) states for unrelaxed bcc Fe: diagonal X-X interactions (a) and off-diagonal X-Y interactions (b). Negative values correspond to attraction between the species (blue), positive ones correspond to repulsion (red).

tions typically become weaker and more short-ranged in the paramagnetic state as compared to the ferromagnetic state of the iron matrix. Thus, the calculated interactions of Mn with any other solute atom considered in this work are al-
most vanishing in the PM state. Very weak X-Y interactions are also exhibited by the Cr and Co with the other solutes in paramagnetic iron.

The calculated vacancy-solute interactions on the first coordination shell typically become more negative in the ferromagnetic ordered state of the $\alpha$-Fe matrix. Quantitatively large (exceeding 0.1 eV) effects of magnetic order are obtained for the elements that form strong chemical bonds with iron (all the considered $3p$ elements, from Al to S), for the elements that are practically insoluble in iron (Cu), and for $3d$ elements such as Cr and Mn that form sizeable magnetic moments in the iron matrix [43].

Interactions of vacancies with $3d$ impurities such as V, Cr, and Mn are found to exhibit a qualitative change upon the magnetic order-disorder transformation in the iron matrix. The vacancy-Mn binding energy in the ferromagnetic $\alpha$-Fe is calculated to be 0.16 eV, in agreement with the values obtained in previous studies (for review see Ref. [43]). At the same time, our calculations predict the vacancy-Mn binding energy to vanish in the paramagnetic DLM state. Simi-
larly, the calculations predict very weak interactions between a vacancy and a Co solute in the paramagnetic DLM state of $\alpha$-Fe. The calculated interactions of Co and Ni impurities with vacancies in ferromagnetic (FM) iron are attractive and exhibit a minimum at the 2nn (rather than at the 1nn) shell. This result is in agreement with the conclusion of an experimental study, Ref. [83], that vacancy-Co and vacancy-Ni pairs are bound beyond the 1nn shell.

## 4. Summary

Effective pair interactions between point defects (solute atoms, impurity atoms, and vacancies) in bcc Fe have been studied using electronic structure and total energy calculations for supercells containing different pairs of defects at a varied separation distance. A database of calculated X-X and X-Y pair interactions on the first three coordination shells in ferromagnetic and param-
agnetic states of the iron matrix has thus been obtained. The effect of atomic relaxations around the impurities has been singled out as the strain-induced contribution to the interaction energy.

The results show that the effective interactions in the bcc lattice of iron change in a regular manner depending on the atomic number of the element (number of valence $d$ and $s$ electrons). The electronic structure of the impurity is the key factor that determines the effective interactions and, therefore, their effect on the structural state and properties of steel. Very strong strain-induced interaction were found only between a $3sp$ impurity (P or S) and a group IV or V transition element. The solute-solute interactions and their dependence on the magnetic state of the matrix investigated in this work may be of practical interest, particularly, in connection with their role in the processes of solute clustering and precipitate formation in steel.

The present study leaves unanswered the question about the vibrational free energy contribution to the effective interactions. In Ref. [84] it was shown by calculation that the vibrational entropy gives a substantial contribution to the solubility limits for Sc in fcc Al. However, the calculations of Ref. [28] shown that the vibrational entropy contribution to Cu solubility in bcc Fe becomes inessential at temperatures close to the Curie temperature of Fe. The questions whether the effect of lattice vibrations on the effective interactions is large or not, and how to correctly take into account the anharmonicity and description of relaxations and phonons in the PM state call for further investigations.

## ACKNOWLEDGMENTS

This work has been supported by the Russian Science Foundation (grant 14-12-00673). A.H.D. acknowledges support by the Swedish Nuclear Fuel and Waste Management Company (SKB). The computations were partly performed on resources provided by the Swedish National Infrastructure for Computing (SNIC) at the National Supercomputer Center (NSC) in Linköping, Sweden.

## References

[1] W. C. Leslie and E. Hornbogen, Physical metallurgy of steels, in Physical Metallurgy, Ed. by R. W. Cahn and P. Haasen (North Holland, New York, 1983), Vol. 2, pp. 1555–1620.

[2] T. Gladman, The Physical Metallurgy of Microalloyed Steels, Maney, London, 1997.

[3] S. Floreen, in: R. K. Wilson (editor), Maraging steel: recent development and applications. Warrendale, PA: TMS AIME; 1988.

[4] V. K. Vasudevan, S. J. Kim, C. M. Wayman, Metall. Trans. A 21 (10) (1990) 2655–2668.

[5] S. J. Kim, C. M. Wayman, Mater. Sci. Eng. A 207 (1996) 22–29.

[6] G. R. Odette,G. E. Lucas, Radiat. Eff. Defect. S. 144 (1998) 189–231.

[7] G. R. Odette, R. K. Nanstad, JOM 61 (2009) 17–23.

[8] V. Pierron-Bohnes, E. Kentzinger, M. C. Cadeville, J. M. Sanchez, R. Caudron, F. Solal, R. Kozubski, Phys. Rev. B 51 (1995) 5760–5767.

[9] J. Chojcan, J. Alloys Compd. 264 (1998) 50–53.

[10] J. Chojcan, Hyperfine Interact. 156–157 (2004) 523–529.

[11] J. Chojcan. Phys. Status Solidi (b) 219 (2000) 375–381.

[12] J. Chicano, G. Roztocka G. Phys. Status Solidi (b) 204 (1997) 829–833.

[13] J. Chicano, J. Alloys Compd. 350 (2003) 62-67.

[14] O. I. Gorbatov, S. V. Okatov, Y. N. Gornostyrev, P. A. Korzhavyi, A. V. Ruban, Phys. Met. Metallogr. 114 (8) (2013) 642-653.

[15] V. Pierron-Bohnes, M. C. Cadeville, A. Finel, O. Schaerpf. J. Phys. I 1 (2) (1991) 247-260.

[16] H. L. Lukas, S. G. Fries, B. Sundman, Computational Thermodynamics, the CALPHAD Method, Cambridge University Press, Cambridge, 2007.

[17] P. Hohenberg, W. Kohn, Phys. Rev. 136 (1964) B864-B871.

[18] W. Kohn, L. J. Sham, Phys. Rev. 140 (1965) A1133-A1138.

[19] D. G. Pettifor, Acta Mater. 51 (2003) 5649-5673.

[20] S. L. Dudarev, Materials Research 43 (1) (2013) 35-61.

[21] C. Pareige, V. Kuksenko, P. Pareige, J. Nucl. Mater. 456 (2015) 471-476.

[22] G. Bonny, D. Terentyev, A. Bakaev, E. E. Zhurkin, M. Hou, D. Van Neck, L. Malerba, J. Nucl. Mater. 442 (1) (2013) 282-291.

[23] W. Xiong, H. Ke, R. Krishnamurthy, P. Wells, L. Barnard, G. R. Odette, D. Morgan, MRS Communications 4 (83) (2014) 101-105.

[24] P. Olsson, T. P. C. Klaver, C. Domain, Phys. Rev. B 81 (2010) 054102-1 - 054102-12.

[25] C. Liu, M. Asato, N. Fujima, T. Moshing, Materials Transactions, 54 (2013) 1667-1672.

[26] C. S. Becquart, C. Domain, Curr. Opin. Solid State Mater. Sci. 16 (3) (2012) 115-125.

[27] A. V. Ruban, P. A. Korzhavyi, B. Johansson, Phys. Rev. B 77 (2008) 094436-1-094436-5.

[28] O. I. Gorbatov, I. K. Razumov, Yu. N. Gornostyrev, V. I. Razumovskiy, P. A. Korzhavyi, A. V. Ruban, Phys. Rev. B 88 (2013) 174113.

[29] O. I. Gorbatov, Yu. N. Gornostyrev, P. A. Korzhavyi, A. V. Ruban, Scr. Mater. 102 (2015) 11-14.

[30] M. Sluiter and Y. Kawazoe, Science reports of the Research Institutes, Tohoku University. Ser. A 40 (1995) 301-306.

[31] M. Rahaman, A. V. Ruban, A. Mookerjee, B. Johansson, Phys. Rev. B 83 (2011) 054202.

[32] O. I. Gorbatov, Yu. N. Gornostyrev, A. R. Kuznetsov, A. V. Ruban, Solid State Phenom. 172-174 (2011) 618-623.

[33] O. I. Gorbatov, A. R. Kuznetsov, Yu. N. Gornostyrev, A. V. Ruban, N. V. Ershov, V. A. Lukshina, Yu. P. Chernenkov, V. I. Fedorov, J. Exper. Theor. Phys. 112 (2011) 848–859.

[34] E. Vincent, C. S. Becquart, C. Domain, J. Nucl. Mater. 351 (2006) 88–99.

[35] R. Ngayam-Happy, C. S. Becquart, C. Domain, J. Nucl. Mater. 440 (2013) 143–152.

[36] E. Vincent, C. S. Becquart, C. Domain, J. Nucl. Mater. 382 (2008) 154–159.

[37] A. Bakaev, D. Terentyev, X. He, D. Van Neck, J. Nucl. Mater. 455 (1) (2014) 5–9.

[38] A. Bakaev, D. Terentyev, G. Bonny, T. P. C. Klaver, P. Olsson, D. Van Neck, J. Nucl. Mater. 444 (2014) 237–246.

[39] A. Bakaev, D. Terentyev, X. He, E. E. Zhurkin, D. Van Neck, J. Nucl. Mater. 451 (1) (2014) 82–87.

[40] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865–3868.

[41] A. V. Ruban, I. A. Abrikosov, Rep. Progr. Phys. 71 (2008) 046501.

[42] I. A. Abrikosov, S. I. Simak, B. Johansson, A. V. Ruban, H. L. Skriver, Phys. Rev. B 56 (1997) 9319–9334.

[43] O. I. Gorbatov, P. A. Korzhavyi, A. V. Ruban, B. Johansson, Yu. N. Gornostyrev, J. Nucl. Mater. 419 (2011) 248–255.

[44] H. L. Skriver, N. M. Rosengaard, Phys. Rev. B. 43 (1991) 9538–9549.

[45] P. A. Korzhavyi, I. A. Abrikosov, B. Johansson, A. V. Ruban, H. L. Skriver, Phys. Rev. B. 59 (1999) 11693–11703.

[46] A. J. Pindor, J. Staunton, G. M. Stocks, H. Winter, J. Phys. F: Metal Phys. 13 (1983) 979–989.

[47] B. L. Gyorffy, A. J. Pindor, J. B. Staunton, G. M. Stocks, H. Winter, J. Phys. F: Metal Phys. 15 (1985) 1337–1386.

[48] P. Soven, Phys. Rev. 156 (1967) 809–813.

[49] Z. S. Basinski, W. Hume Rothery, A. L. Sutton, Proc. R. Soc. Lond. A 229 (1955) 459–467.

[50] I. Seki, K. Nagata, ISIJ Int. 45 (2005) 1789–1794.

[51] P. E. Blöchl, Phys. Rev. B 50 (1994) 17953.

[52] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758.

[53] O. Kubaschewski, Iron-Binary Phase Diagrams, Springer Verlag, Berlin,
1982.

[54] G. Rahman, I. G. Kim, H. K. D. H. Bhadeshia, A. J. Freeman, Phys. Rev.
B. 81 (2010) 184423.

[55] V. I. Anisimov, V. P. Antropov, A. I. Liechtenstein, V. A. Gubanov, A. V.
Postnikov, Phys. Rev. B. 37 (1988) 5598.

[56] P. Olsson, C. Domain, J. Wallenius, Phys. Rev. B 75 (2007) 014110.

[57] Y. W. You, X. S. Kong, X. B. Wu, W. Liu, C. S. Liu, Q. F. Fang, Z. Wang,
(2014). J. Nucl. Mater. 455 (1) (2014) 68–72.

[58] D. J. Bacon, Yu. N. Osetsky, J. Nucl. Mater. 329–333 (2004) 1233–1237.

[59] H. Amara, C. C. Fu, F. Soisson, P. Maugis. Phys. Rev. B 81 (2010) 174101.

[60] V. V. Serikov, N. M. Kleinerman, A. V. Vershinin, N. V. Mushnikov, A. V.
Protasov, L. A. Stashkova, O. I. Gorbatov, A. V. Ruban, Yu. N. Gornos-
tyrev, J. Alloys Compd. 614 (2014) 297–304.

[61] P. D. Styman, J. M. Hyde, D. Parfitt, K. Wilford, M. G. Burke, C. A.
English, P. Efsing, J. Nucl. Mater. 459 (2015) 127–134.

[62] F. Soisson, C.-C. Fu, Phys. Rev. B 76 (2007) 214102-1–214102-12.

[63] Y. Zhang, P. C. Millett, M. R. Tonks, X. M. Bai, S. B. Biner, Comput.
Mater. Sci. 101 (2015) 181–188.

[64] S. Huang, D. L. Worthington, M. Asta, V. Ozolins, G. Ghosh, P. K. Liaw,
Acta Mater. 58 (2010) 1982–1993.

[65] S. Choudhury, L. Barnard, J. D. Tucker, T. R. Allen, B. D. Wirth, M.
Asta, D. Morgan, J. Nucl. Mater. 411 (2011) 1–14.

[66] L. Messina, M. Nastar, T. Garnier, C. Domain, P. Olsson. Phys. Rev. B 90
(2014) 104203.

[67] K. Yu. Khromov, F. Soisson, A. Yu. Stroev, V. G. Vaks, J. Exper. Theor.
Phys. 112 (3) (2011) 414–440.

[68] T. Ohnuma, N. Soneda, M. Iwasawa, Acta Mater. 57 (2009) 5947–5955.

[69] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria,
L. A. Constantin, X. Zhou, K. Burke, J. P. Perdew et al., Phys. Rev. Lett.
100 (2008) 136406.

[70] F. R. de Boer, R. Boom, W. C. M. Mattens, A. R. Miedema, A. K. Niessen,
in Cohesion in Metals: Transition Metal Alloys, Vol. 1, edited by F. R. de
Boer and D. G. Pettifor, North-Holland, Amsterdam, 1988.

[71] J. Friedel, in The Physics of Metals, edited by J. M. Ziman, Cambridge University Press, Cambridge, 1969.

[72] F. Körmann, A. Dick, B. Grabowski, T. Hickel, and J. Neugebauer, Phys. Rev. B 85 (2012) 125104.

[73] A. V. Ruban and V. I. Razumovskiy, Phys. Rev. B 85 (2012) 174407.

[74] A. V. Ruban, V. I. Razumovskiy, and F. Körmann, Phys. Rev. B 89 (2014) 179901.

[75] N. Sandberg, Z. Chang, L. Messina, P. Olsson, and P. Korzhavyi, Phys. Rev. B 92 (2015) 184102.

[76] I. A. Abrikosov, A. V. Ponomareva, P. Steneteg, S.A. Barannikova, and B. Alling, Current Opinion in Solid State and Materials Science 20 (2016) 85-106.

[77] A. P. Miodownik, Bull. Alloy Phase Diagrams 2 (1982) 406-412.

[78] G. Salje, M. Feller Knipmeier, J. Appl. Phys. 48 (1977) 1833-1839.

[79] T. Nishizawa, M. Hasebe, and M. Ko, Acta. Metall. 27 (1979) 817-828.

[80] M. Ekholm, H. Zapolsky, A. V. Ruban, I. A. Abrikosov, Phys. Rev. Lett. 105 (2010) 167208.

[81] P. A. Korzhavyi, B. Sundman, M. Selleby, B. Johansson, Mater. Res. Soc. Symp. Proc. 842 (2005) 517-522.

[82] A. V. Ruban, V. I. Razumovskiy, Phys. Rev. B. 86 (2013) 174111.

[83] A. Möslang, E. Albert, E. Recknagel, A. Weidinger, P. Moser, Hyperfine Interact. 15 (16) (1983) 409-412.

[84] V. Ozolins, M. Asta. Phys. Rev. Lett. 86 (2001) 448.
