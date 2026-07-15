# Identification of defects at the interface between 3C-SiC quantum dots and a $SiO_2$ embedding matrix

Márton Vörös¹, Adam Gali¹², Efthimios Kaxiras³, Thomas Frauenheim⁴, and Jan M. Knaup*³⁴

¹Department of Atomic Physics, Budapest University of Technology Economics, 1111 Budapest, Hungary
²Research Institute for Solid State Physics and Optics, Hungarian Academy of Sciences, P.O. Box 49, 1525 Budapest, Hungary
³Department of Physics, Harvard University, 17 Oxford St., Cambride, MA, 02138, USA
⁴Bremen Center for Computational Materials Science, University of Bremen, Am Fallturm 1, 28359 Bremen, Germany

Received 31 August 2011, revised 14 October 2011, accepted 14 October 2011
Published online 26 December 2011

Dedicated to Thomas Frauenheim on the occasion of his 60th birthday

Keywords defects, DFTB, interfaces, quantum dots, SiC

*Corresponding author: e-mail Jan.Knaup@bccms.uni-bremen.de, Phone: +1 (617) 495-7977, Fax: +1 (617) 495-3339

Due to the favorable band offsets, SiC nanoparticles embedded in silica form a very interesting quantum dot (QD) system. It is possible to produce such QDs in a simple oxidation–carbonization–reoxidation process on Si wafers. This could thus enable production of Si based LED integrated into Si logic devices. However, the luminescence of these QDs, is quenched. This is attributed to defect-mediated recombination of electron–hole pairs, most probably at the SiC/SiO₂ interface. We present tight-binding simulated annealing calculations, in order to construct models of SiC QDs in SiO₂, with the aim of obtaining an overview of the possible defects at the SiC/SiO₂ interface. We identify a number of recurring interface defects which can be attributed to C or Si rich conditions or general lattice mismatch relaxation. Similar to defects have been shown to be electrically active at the SiC/SiO₂ interface in MOS structures. We find evidence for strained Si–Si bonds, which can act as recombination centers in isolated SiC QDs. The defect classes identified in this work can serve as the basis for future, high precision simulations of their electronic structure.

![](./images/813343944107622401_1.jpg)

A 66-atom spherical SiC nanocrystal with a shell of SiO₂ including –OH termination (66-sph-1 cluster, only QM zone shown; cf. Fig. 2 for key).

© 2011 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

## 1 Introduction
A new experimental procedure allows to grow 3C-SiC nanocrystals of well-controlled size distribution embedded in a SiO₂ matrix on Si substrates [1, 2]. This method works by first growing a thermal oxide layer on the Si wafer in O atmosphere, then switching to annealing in CO atmosphere, which leads to the growth of SiC nanocrystals at the Si/SiO₂ interface. A final thermal oxidation step consumes the Si around the nanocrystals, while the much more stable SiC remains behind and is thus embedded in the oxide layer. The symmetrical band offsets of 3 eV at the conduction and valence band edges provide equally good electronic confinement for electrons as well as

holes and thus make SiC/SiO₂ a very interesting system to build quantum dots (QD). However, contrary to expectations, the luminescence predicted from the electronic confinement could not be observed [2]. Earlier theoretical studies on group IV QDs, made from Si [3–5] or Ge [5] based on *ab initio* simulations of supercells or clusters show, that in Si and Ge nanoparticles, the luminescence is quenched by interface defects, especially concerning the bonding situation of oxygen at the QD surface. Similar results are found for the surface of isolated SiC nanocrystals, where the presence of double bonded oxygen leads to dramatic red shift of the optical gap [6, 7]. It is expected, that the luminescence of the SiC QDs in SiO₂ is suppressed in a similar manner by defect-mediated, non-radiative recombination of electron-hole pairs. In this work we report on annealing simulations of different QD models embedded in an α-quartz matrix aimed at generating models of possible SiC/SiO₂ interface defects in the embedded QD system.

In this article we present the final results of our annealing study SiC QDs in SiO₂ matrix. Intermediate results have been presented at the ICFSI 2009 in Weimar [8]. In the following section, we will describe our simulation approach. In Section 3 we describe the models of our QDs before the annealing, in Section 4 we will report the results of our simulation and discuss which of the interface defects we find are potentially electrically active and thus probable centers for the observed quenching of QD luminescence.

2 Methods We use the density functional based tight-binding (SCC-DFTB) method [9, 10] in a QM/MM embedding scheme [11–13] to simulate single SiC QDs embedded in 0.5–1 nm thick shells of explicitly QM simulated SiO₂. In this study, we employ the well-tested pbc-1-0 DFTB parametrization for the Si–O–C–H system [14].

We perform simulated annealing by Born–Oppenheimer molecular dynamics (MD), using the DFTB forces and energies. The ionic equations of motion are integrated with a time step of 1 fs. We employ an Adersen-type [15] thermostat to follow a temperature profile starting at 300 K, ramping up to 1500 K at a rate of 1.5 K/fs, then annealing at 1500 K for several ps before quenching. We apply a Fermi–Dirac broadening to the occupation of electronic states which follows the ionic target temperature.

<table>
<caption>Table 1 Properties of the quantum dot models: $N_{\text{SiC}}$, $N_{\text{SiO}_2}$: number of atoms in the SiO₂ and SiC parts, $r_{\text{QMZ}}$ radius of the QM zone, $N_{\text{mob}}$ number of mobile atoms.</caption>
<thead>
<tr>
<th>model</th>
<th>$N_{\text{SiC}}$</th>
<th>$N_{\text{SiO}_2}$</th>
<th>$r_{\text{QMZ}}$ (Å)</th>
<th>$N_{\text{mob}}$</th>
<th>notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>35-sph</td>
<td>35</td>
<td>570</td>
<td>12</td>
<td>211</td>
<td>spherical</td>
</tr>
<tr>
<td>51-tet</td>
<td>51</td>
<td>929</td>
<td>$\sim$15ª</td>
<td>656</td>
<td>tetrahedral, dissolved</td>
</tr>
<tr>
<td>64-cub</td>
<td>64</td>
<td>661</td>
<td>$\sim$13ª</td>
<td>544</td>
<td>cuboid</td>
</tr>
<tr>
<td>66-sph-1</td>
<td>66</td>
<td>530</td>
<td>13</td>
<td>213</td>
<td>spherical, C-rich surface</td>
</tr>
<tr>
<td>66-sph-2</td>
<td>66</td>
<td>534</td>
<td>13</td>
<td>214</td>
<td>spherical</td>
</tr>
<tr>
<td>66-sph-3</td>
<td>66</td>
<td>528</td>
<td>13</td>
<td>208</td>
<td>spherical</td>
</tr>
<tr>
<td>66-sph-4</td>
<td>66</td>
<td>789</td>
<td>14</td>
<td>291</td>
<td>spherical</td>
</tr>
<tr>
<td>66-sph-5</td>
<td>66</td>
<td>775</td>
<td>14</td>
<td>329</td>
<td>spherical</td>
</tr>
<tr>
<td>87-sph</td>
<td>87</td>
<td>772</td>
<td>14</td>
<td>345</td>
<td>spherical</td>
</tr>
<tr>
<td>66-sup</td>
<td>66</td>
<td>847</td>
<td>N/A</td>
<td>913</td>
<td>spherical, supercell, 66-sph-1 QD</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">ªQM zones are not spherically shaped.</td>
</tr>
</tfoot>
</table>

After an equilibration time of 3–5 ps, depending on the individual QD model, we exponentially quench the QD down to 0 K within 0.8 ps. Since this quench is very fast, we optimize the atomic postions of the quenched models using conjugate gradients until the maximum atomic force falls below $10^{-4}$ H/Bohr. A single MD trajectory is simulated for each structure listed in Table 1.

We identify potential electrically active defects by two means: first we analyze the bond network by an interatomic distance based bond search, regarding every deviation from ideal single-bonded neighbor count as a possible defect. Second, we calculate projected densities of states based on atomic orbital Mulliken populations. Since DFTB uses a minimal basis set, Mulliken analysis provides an accurate tool to analyze partial charges and atomic contributions to eigenstates.

3 Quantum dot models Table 1 lists the QD models used for is study. Initially, we base our models of the embedded QDs on approximately spherical SiC nanocrystals of 35, 66, and 87 atoms (in the following sph-37, shp-66, and shp-87, respectively) (in the 35-sph, 66-sph, and 87-sph, respectively) (cf. Fig. 1), similar to the structures used in Ref. [16] to enable comparison with the results on isolated

![](./images/813343944107622401_2.jpg)

Figure 1 (online color at: www.pss-b.com) Spherical quantum dot models with 35 (left), 66 (center), and 87 (right) atoms.

![](./images/813343944107622401_3.jpg)

Figure 2 (online color at: www.pss-b.com) Left: 64-atom "frayed"
3C-SiC cuboid, right: 51-atom 3C-SiC tetrahedral nanocrystal.

QD. The surface of the 66-sph-1 cluster was artificially
carbon enriched by replacing Si atoms with C, the 66-sph-2–5
clusters differ by random rotation and random displacement
by 1–2 Å with respect to the silica matrix. During the course
of the annealing simulations of these QDs, it turned out that
the reactivity of their surfaces was lower than expected, so
that the formation of a covalently linked interface was slow.
We therefore added two more nanocrystal models with
sharper edges and graver undercoordination of their surface
atoms: a 64-atom cuboid cutout of 3C-SiC (64-cub) in which
some surface atoms have been randomly shifted towards the
opposing surface and a 51-atom tetrahedral nanocrystal of
3C-SiC (51-tet) (cf. Fig. 2).

We model the surrounding silicon dioxide by α-quartz,
which is known to have quite similar properties to an
amorphous thermal oxide, keeping in mind that the oxide in
surroundings of the SiC nanocrystals can be expected to
amorphicize during the annealing simulations. We optimize
the atomic positions in a unit-cell model of α-quartz with
experimental cell vectors in a Γ-point calculation. We only
take the Γ-point into account here to ensure compatibility of
the atomic positions, partial charges, and charge transfer
coefficients to be used in a non-periodic embedding scheme.

For the embedded simulations, we use a $30 × 30 × 24$
unit cell $(\sim 15 × 15 × 12\ \text{nm}^3)$ 194,440-atom rhomboid of
SiO₂. The size of the outer SiO₂ part is chosen based on the
results of convergence analysis of surface reaction energies
on α-quartz surfaces using the same embedding scheme [13].
For the fully QM reference calculation we use a $5 × 5 × 4$
$(\sim 2.5 × 2.5 × 2,2\ \text{nm}^3)$ 900-atom supercell. We construct
the QM-zone models by superimposing the nanocrystal
geometry on the central $10 × 10 × 8$ quartz cell, removing
atoms from the quartz model in the shared volume by hand.
We remove atoms at the QD/matrix interface in such a
manner as to keep the SiO₂ stoichiometry of the silica part
and to keep the distances between outer SiC and inner SiO₂
atoms in the range of $\frac{1}{2} \cdots 1\frac{1}{2}$ bond lengths. The surrounding
QM zone is selected semi-automatically by choosing all Si
atoms from the SiO₂ part which fall within the desired QM
zone thickness plus their oxygen neighbors. Where this leads
to Si atoms protruding from an otherwise flat face of the
supercell, we shift these into the MM zone. After adding link
atoms and bond charge transfer compensation (BCTC)
neutralization [12, 13] of the QM- and inner MM-zones, this
inner zone is embedded into the outer part of the external
charge distribution. The title figure shows an example of a
QM-zone generated this way.

Since we do not apply force field parameters to the outer
charge distribution, we keep the positions of the link-atoms,
and first two layers of QM-zone border atoms fixed. The
procedure for generating the periodic supercell reference
model was analog, no atomic constraints are applied but we
keep the supercell vectors fixed during the whole simulation.

## 4 Results and discussion
### 4.1 Annealing
Figure 3 shows the roots of mean
square displacements (RMSD) of the SiC clusters and its
nearest neighbors during the MD simulations. It can be seen
that, with the exception of the 51-tet cluster, all structures
have reached equilibrium. Most simulations were equili-
brated within the first 3 ps of simulation time all were in
equilibrium after 5 ps. The different asymptotic RMSD
values correspond to different levels of overall structural
relaxation during the MD simulations. In stark contrast, the
tetrahedrally formed 51-atom SiC nanocrystal did not reach
equilibrium. The strong movements of the atoms led to long
convergence times in the QM calculations, so that the
comparatively short 3 ps simulation time that was reached
for this structure used the longest CPU time. Instead of
reaching a steady state, the RMSD curve shows a linear
increase in RMSD over time, which indicates a diffusive
behavior. This is consistent with the observation that the SiC
cluster dissolved over time. This shows that the choice of a
tetrahedral was somewhat overly successful in obtaining a
more reactive nanocrystal/matrix interface than the spherical
NCs. We therefore exclude the 51-atom tetrahedral QD from
our further analysis.

![](./images/813343944107622401_4.jpg)

Figure 3 (online color at: www.pss-b.com) RMSDs of the core
atoms, defined as all atoms within a $2.5\ \text{Å}$ shell around the SiC
nanocrystal in the starting configurations. A vertical line indicates
the switch from heating to equilibration.

<table>
<caption>Table 2 Coordination error development.</caption>
<thead>
<tr>
<th>element</th>
<th>valence error</th>
<th colspan="2">atom counts</th>
<th rowspan="2">change</th>
</tr>
<tr>
<th></th>
<th></th>
<th>initial</th>
<th>final</th>
</tr>
</thead>
<tbody>
<tr>
<td>O</td>
<td>−1</td>
<td>114</td>
<td>78</td>
<td>−36</td>
</tr>
<tr>
<td></td>
<td>0</td>
<td>4461</td>
<td>4496</td>
<td>+35</td>
</tr>
<tr>
<td>C</td>
<td>+1</td>
<td>55</td>
<td>56</td>
<td>+1</td>
</tr>
<tr>
<td></td>
<td>−3</td>
<td>1</td>
<td>2</td>
<td>+1</td>
</tr>
<tr>
<td></td>
<td>−2</td>
<td>74</td>
<td>11</td>
<td>−63</td>
</tr>
<tr>
<td></td>
<td>−1</td>
<td>82</td>
<td>109</td>
<td>+27</td>
</tr>
<tr>
<td></td>
<td>0</td>
<td>149</td>
<td>184</td>
<td>+35</td>
</tr>
<tr>
<td>Si</td>
<td>−2</td>
<td>21</td>
<td>24</td>
<td>+3</td>
</tr>
<tr>
<td></td>
<td>−1</td>
<td>108</td>
<td>94</td>
<td>−14</td>
</tr>
<tr>
<td></td>
<td>0</td>
<td>2049</td>
<td>2132</td>
<td>+83</td>
</tr>
<tr>
<td></td>
<td>1</td>
<td>94</td>
<td>38</td>
<td>−56</td>
</tr>
<tr>
<td></td>
<td>+2</td>
<td>17</td>
<td>1</td>
<td>−16</td>
</tr>
</tbody>
</table>

Counts of atoms with the given differences from standard valence summed over all nanocrystals and simulation runs. Atomic valence is defined as the number of atoms within $1.2 \times (r_{\text{cov cent}} + r_{\text{cov neigh}})$ of the central atom with $r_{\text{cov}}$ the covalent radii of central and neighbor atom from Ref. [17].

The annealing procedure succeeded in significantly reducing the number of dangling bonds as well as over-coordinated atoms, as can be seen in Table 2. Note that the valence counts in the table are purely derived from interatomic distances and do not account for higher-order (i.e., double or triple) bonds. Some of the undercoordination indicated in the data must be attributed to this. Still, not all the undercoordination could be cured during the annealing simulations. This is partly caused by the limited annealing time, partly by structural mismatch and partly by the intrinsic constraints imposed by the model construction. The size constraint, imposed by the fixed supercell vectors in the periodic model and the fixed outer shells of silica in the QM/MM models do not allow full correction of overall density errors in the initial models, stemming from too large or small cavities for the nanocrystals.

To assess the influence of the annealing time on the healing of coordination defects, we analyze the evolution of a coordination parameter $\chi$ defined as

$$
\chi = \sum_{d=0}^{d_{\text{max}}} dN_d
$$

where $N_d$ is the number of atoms of a given coordination deviation $d$, which is defined as $n_{\text{bonds}} - n_{\text{valences}}$ for a given element. Figure 4 shows the coordination development for C and Si in the 64-cub nanocrystal during annealing, the behavior of the other nanocrystals is qualitatively the same. It can be seen that for both C and Si the number of undercoordinations remains approximately constant during the annealing time and exhibits a pronounced drop during the quenching phase at the end of the simulation, which is correlated to an increase in the number of normally coordinated atoms. Here, the bond-detection scheme employed leads to some distortion: in the high-temperature regime the all bonds undergo stretching mode vibrations. This leads to the artifact that a certain fraction of the bonds is stretched beyond the detection limits, leading to a shift from normal coordination to undercoordination. Taking this into account, the fact the no apparent increase in under-coordination occurs during the heating phase indicates that during this time some undercoordination defects (i.e., dangling bonds) must be healed. For the Si atoms, both effects approximately compensate each other, while for the C atoms, a visible dip of undercoordination shows that a quite significant number of C-dangling bonds was cured before the temperature artifact sets in. When examining the Si atoms (Fig. 4b), one can see a sharp drop of the overcoordination parameter during the heating phase and a further decrease during the first picosecond of the equilibration phase. Note that no apparent overcoordination is restored during the quenching, which proves that the decrease of overcoordination in the early part of the

![](./images/813343944107622401_5.jpg)

Figure 4 (online color at: www.pss-b.com) Time development of the absolute coordination parameters $|\chi|$ of the 64-cub nanocrystal during the annealing, partitioned into undercoordination ($\chi < 0$), normal coordination ($\chi = 0$), and overcoordination ($\chi > 0$).

![](./images/813343944107622401_6.jpg)

Figure 5 (online color at: www.pss-b.com) Time development of the absolute coordination parameters $|\chi|$ of the 66-sph1 nanocrystal during the annealing, partitioned into undercoordination ($\chi<0$), normal coordination ($\chi=0$), and overcoordination ($\chi>0$).

simulation was not purely a temperature artifact of the bond detection algorithm. During the equilibration phase between 2 and 5 ps, we observe some oscillation of the coordination parameter, but no longer-term movement of the average. This indicates that most of the defect healing takes place during the early part of the simulation. While this does not prove that shorter equilibration times might have been sufficient, we can conclude that our simulations cover the effects which can occur during accessible annealing times and under the given external constraints sufficiently well. A significant improvement on the temporal scale would require an extension of the simulation times by orders of magnitude, which is impractical with regard to the computational cost.

We compare the coordination evolutions of the embedded cluster simulation 66-sph1 (Fig. 5) with the periodic calculation 66-sup (Fig. 6), to see the behavioral differences between the two modeling approaches. The most striking difference we find is a much higher under- coordination of C atoms in the periodic simulation (Figs. 5a and 6a). This is not directly related to the periodicity, but rather an effect of a slightly larger cavity cut into the silica part of the periodic model. At the same time, the periodic model does not show any silicon dangling bonds at all. Comparing the time evolution of the carbon coordinations, we find that the coordination defects are healed to a much greater extent in the periodic supercell than in the embedded cluster model. However, at the end of the annealing process, the periodic model still shows a significantly greater carbon undercoordination that the embedded cluster model. Even though the reduction in carbon dangling bonds is higher in the supercell model, it must be kept in the mind that the total driving force for relaxation is also much larger due to the higher number of initial defects. We therefore conclude that

![](./images/813343944107622401_7.jpg)

Figure 6 (online color at: www.pss-b.com) Time development of the absolute coordination parameters $|\chi|$ of the 66-sup nanocrystal during the annealing, partitioned into undercoordination ($\chi<0$), normal coordination ($\chi=0$), and overcoordination ($\chi>0$).

the higher number of movable atoms in a supercell model does not dramatically increase the total relaxational freedom, as long as the MD is performed at constant volume.

### 4.2 Electronic structure
We know from experience at the $4\text{H-SiC/SiO}_2$ MOS interface [18–20] that the band alignment and detailed electronic structure of point defects in the silica/SiC system are delicate and their accurate description requires higher accuracy than DFTB allows. Even though the combination of minimal basis set and DFT self-interaction error leads to DFTB band gaps close to the experiment, the same cannot be assumed for localized states centered on point defects. We have shown that, given the right choice of functional, DFT is very suitable to describe this system. Based on this experience, DFT calculations using hybrid functionals could serve as the basis of future studies.

We do not aim at identifying the defects responsible for quenching the QD luminescence in this study. We will therefore forgo an in-depth analysis of the electronic structures of the models generated here, but briefly discuss the artifacts of the embedded cluster approach and their possible influence on the interface chemistry.

The main effect of using an embedded cluster model instead of a periodic supercell is the loss of translational symmetry. This does not affect the nanocrystal part of the examined system, but it may lead to some changes in the electronic structure of the matrix material. The comparison between the 66-sup and 66-sph1 models, in which the same SiC cluster is embedded in a periodic quartz structure and a non-periodic embedded cluster, respectively, allows to estimate these effects. Figure 7 shows density of states plots for the embedded cluster and supercells models. It can be seen that both the conduction and valence bands of the embedded cluster model are less structured and broadened with respect to the crystalline supercell model. This is consistent with a much stronger amorphization of the embedded cluster model, due to the strong mechanical constraints of the rigid supercell.

![](./images/813343944107622401_8.jpg)

Figure 7 (online color at: www.pss-b.com) Comparison of the densities of states (DOS) between embedded cluster (emb.) and supercell (per.) models. DOS curves use independent y-axis scales to compensate for different atom counts and resulting absolute DOS values. The curves emb. term. and emb. nc show the projected densities of states in the embedded cluster model on the terminating OH groups and the SiC nanocrystal, respectively.

In a similar manner, the presence of terminating OH groups at the outer surface of the embedded $\text{SiO}_2/\text{SiC}$ cluster leads to artifacts in the electronic energy spectrum of the model. As can be seen in Fig. 7, the hydroxyl groups cause a significant peak of occupied states just under the Fermi energy. At elevated temperatures during the annealing process these donor states could lead to the stabilization of negatively charged defects at the cluster interface. However, this effect will be reduced during the quenching process and should not influence the subsequent geometry optimization.

### 4.3 Interface point defects
The $\text{SiC/SiO}_2$ interfaces generated in this study often show complexes of point defects. As these complexes appear in great variation, we concentrate on the point defects which form the building blocks of these complexes. In the following we discuss the recurring types of defects at the $\text{SiC/SiO}_2$ interface we found in our simulations.

### 4.4 C-dimers
Under carbon rich surface conditions as modeled in the 66-sph1 and 66-sup nanocrystals, we observe the formation of $\text{sp}^3$ hybridized C–C dimers, in part with dangling bonds. Some deviation of the C coordination geometries from the tetrahedral configuration are attributed to local strain. These defects are very similar to $(\text{C}_\text{i})_2$ defects found at the $\text{SiC/SiO}_2$ MOS interface in earlier studies [18]. These defects have been shown to act as hole traps at the interface and account for a part of the observed correlation between excess carbon and the density of interface traps in thermally grown SiC MOS structures. Similar defects in $\text{SiO}_2$ act as electron traps close to the 4H-SiC conduction band edge [19].

On the surface of isolated SiC nanoparticles, a $2\times1$ like C reconstruction of the surface leads to similar $\text{sp}^3$ bonded carbon dimers which lead to gap states with oscillator strength usually smaller than that for the band edge [16, 21].

### 4.5 Si–Si bonds
Si–Si bonds appear at the interface where surface Si atoms of matrix and nanocrystal are close to each other (cf. Fig. 8). It is not clear whether these bonds are stabilized by the QD matrix interface or of they are an artifact of O deficiency incurred in the model construction phase. It is, however known from bulk $\alpha$-quartz [19] as well as SiC nanocrystals in vacuum [16, 21] that Si–Si are electrically active in the vicinity of the bulk 4H-SiC band edges. If Si–Si bonds on the surface of isolated QDs are elongated, the corresponding localized states move towards midgap. Therefore Si–Si bonds, originating from interstitial Si atoms

![](./images/813343944107622401_9.jpg)

Figure 8 (online color at: www.pss-b.com) Si–C–C ring connected to a threefold coordinated O, found in the 66-sup quantum dot.

as well as reconstruction directly at the interface must be be considered as possible recombination centers.

### 4.6 4-member rings
Rings of four atoms appear in a number of variations, all of which contain either one or two Si atoms and at most two O atoms. The formation of such rings requires the deformation of the normal $sp^3$ bonding tetrahedra of the involved group IV atoms, which results in strain. Therefore, a four-member ring cannot be an absolute minimum energy configuration. However, external constraints may change this. Two driving forces lead to the formation of these strained rings: higher than optimal (local) density of atoms and the presence of dangling bonds. While the former will have some impact in the observed system, the presence of large numbers of dangling bonds rather indicates too low than too high density. The saturation of such dangling bonds plays a bigger role here. A strained bond will always be energetically favorable to an unsaturated valence. With this in mind, the formation of small, strained rings must be regarded as a form of inner surface reconstruction.

### 4.7 Threefold coordinated O
Threefold coordinated, $sp^2$ hybridized O atoms appear in all examined models. Since they can only exist, if the O gives off one electron, they must be correlated to acceptor defects. Of the 51 O-$sp^2$ observed in total, 35 are found within the third neighbor shell of Si or C atoms having at least one dangling bond. These dangling bonds could act as acceptors for the excess electrons, yet no correlation between the temporal developments of the dangling bond and O-$sp^2$ counts could be found. It is also notable, that the total number of threefold coordinated O atoms has not dropped significantly during the annealing and relaxation, while the number of Si and C dangling bonds was strongly reduced (cf. Table 2).

Therefore, a direct correlation between $sp^2$ coordinated O and Si or C dangling bonds is unlikely.

Eighteen O-$sp^2$ are part of 4-member rings, often in the form Si–O-$sp^2$–Si double bridges (some of these are also counted in the 35 atoms close to dangling bonds). The O-$sp^2$ double bridges should not be confused with Si–O–Si double bridges in which both O atoms are normally coordinated and which are the lowest energy configuration of negatively charged O interstitials in $\alpha$-quartz [19]. More generally, threefold coordinated oxygen atoms are connected to oxygen deficiency in $SiO_2$, often appearing in the presence of Si interstitials [19].

### 4.8 Si–C–C rings
The Si–C–C three-membered ring structure shown in Fig. 8 can be regarded as a C–$C_i$ split interstitial defect, where an interstitial carbon shares the lattice site of a regular C atom. At the surface of the embedded QD this common defect assumes a different structure than in bulk SiC, where both C atoms are $sp^2$ hybridized and each exhibit a dangling p-orbital. Here both C atoms are $sp^3$ hybridized, one dangling bond is saturated by bonding to a surface Si atom which had a dangling bond from the cutting of the spherical nanocrystal. The second dangling bond is healed by creating a complex with an O atom from a neighboring Si–O–Si bridge, leading to a threefold coordinated O atom.

### 4.9 Overcoordinated Si
A relatively large number of Si atoms are five- or even sixfold coordinated in the starting geometries. These are artifacts of the embedding procedure where the cavities walls lie comparatively close to the nanocrystal. As can be seen in Table 2, all but one octahedrally coordinated Si atoms are annealed out, as are just under 2/3 of the single overcoordination occurrences. This is consistent with the expectation that any non-$sp^3$ configuration is unfavorable for Si. It is, however, known that fivefold coordinated Si atoms can appear in silica under Si-rich conditions [19].

### 4.10 Dangling bonds
As has already been discussed, a causal relation between the presence of Si or C dangling bonds and overcoordinated O is unlikely, since it is not supported by any correlation in the time evolutions of their abundances. The main cause of the dangling bonds in our systems is of geometric nature. The unreconstructed surfaces of the nanocrystal and cavity naturally show a high density of dangling bonds. Some of these are seemingly healed in the initial structures by the proximity of surface atoms of the respective other part, but the formation of a bond is not in all cases favorable. In the natural system, deviations in the cavity size from the ideal will be compensated for by medium range density adjustment of the oxide part. The freedom for this is limited in our simulations due to the rigid outer shells in the embedded clusters and the fixed supercell of the periodic calculation. Therefore, we expect that we find a somewhat higher density of dangling bonds than natural.

It should also be noted, that in some simulations dangling bonds appeared by breaking of Si–O bonds at the rim of the rigid outer layer. This indicates two possible problems with the simulations. First, a the initial distribution of electrons could be faulty, leading to electrons being drawn from bonding or put into antibonding states. Second, too large cavities might lead to heavy tensile strain throughout the oxide, which can be relieved through this bond-breaking in the outer oxide layer.

## 5 Summary and outlook
The results presented in the preceding section can be categorized into three classes: C excess related, O deficiency related and lattice mismatch related. From the experimental setup, none of these categories can be ruled out directly. A lattice mismatch between the SiC and silica parts of the system exists and dangling bonds resulting from it cannot be ruled out. The oxidation of SiC is known to produce C excess at the SiC/$\text{SiO}_2$ interface [18, 22, 23] through transient C interstitials. The same mechanism is likely to also produce some C interstitials during the oxidation–carbonization–reoxidation process. Similarly, O deficiency or Si excess, which we regard to be equivalent in their consequences, is also quite possible.

Even though fully optimized, realistic models of silica-embedded SiC nanoparticles, could not be obtained by DFTB MD simulation within a practicable simulation runtime, we were able to identify and classify abundant point defects at this particular $\text{SiC/SiO}_2$ interface. The present results will enable the construction of simplified models of the involved $\text{SiC/SiO}_2$ interfaces containing isolated variants of the identified defects as well as small complexes of thereof. These models will then be examined using state of the art high accuracy methods, especially screened hybrid exchange DFT, to identify specific spectroscopic signatures of these defects. Further studies in this direction are in progress. These simulations are expected to produce specific spectroscopic signatures which can be correlated to experimental results. The high-precision electronic structure data will also allow the determination which defects mediate non-radiative recombination of excitons in the QD system and thus quench the luminescence.

Acknowledgements J.M.K. is grateful for a research scholarship from the German Research Association, DFG. M.V. acknowledges the support from GE Lighting Hungary. The bilateral support from MTA-DFG No. 436 is greatly appreciated. Part of the calculations for this work were performed on Harvard FAS computing facilities. Use of computing facilities at the Bremen Center for Computational Materials Science is greatly appreciated.
Atomic structure representations were prepared using VMD [24].
For all DFTB calculations the $\text{DFTB}^+$ code [25] was used.

## References
[1] Z. Makkai, B. Pécz, I. Bársony, G. Vida, A. Pongrácz, K. V. Josepovits, and P. Deák, Appl. Phys. Lett. **86**, 253109 (2005).
[2] A. Pongrácz, G. Battistig, C. Dicsö, K. Josepovits, and P. Deák, Mater. Sci. Eng. C **27**, 1444 (2007).
[3] M. Nishida, Phys. Rev. B **69**(16), 165324 (2004).
[4] I. Vasiliev, J. R. Chelikowsky, and R. M. Martin, Phys. Rev. B **65**(12), 121302 (2002).
[5] H. C. Weissker, J. Furthmüller, and F. Bechstedt, Phys. Rev. B **65**(15), 155327 (2002).
[6] M. Vörös, P. Deák, T. Frauenheim, and A. Gali, Mater. Sci. Forum **679/680**, 520–523 (2011).
[7] M. Vörös, P. Deák, T. Frauenheim, and A. Gali, J. Chem. Phys. **133**(6), 064705 (2010).
[8] J. M. Knaup, M. Vörös, P. Déak, A. Gali, T. Frauenheim, and E. Kaxiras, Phys. Status Solidi C **7**(2), 407 (2009).
[9] B. Aradi, B. Hourahine, and T. Frauenheim, J. Phys. Chem. A **111**, 5678 (2007).
[10] T. Frauenheim, G. Seifert, M. Elstner, Z. Hajnal, G. Jungnickel, D. Porezag, S. Suhai, and R. Scholz, Phys. Status Solidi B **217**, 41 (2000).
[11] Q. Cui, M. Elstner, E. Kaxiras, T. Frauenheim, and M. Karplus, J. Phys. Chem. B **105**, 569 (2001).
[12] J. M. Knaup, Computational Studies of Hybrid Interface Formation, Ph.D. thesis, University Paderborn, Nov. 2008.
[13] J. M. Knaup, P. Tölle, C. Köhler, and T. Frauenheim, Eur. Phys. J. Spec. Topics **177**, 59 (2009).
[14] C. Köhler, Z. Hajnal, P. Deák, T. Frauenheim, and S. Suhai, Phys. Rev. B **64**(8), 085333 (2001).
[15] H. C. Andersen, J. Chem. Phys. **72**(4), 2384–2393 (1980).
[16] M. Vörös, P. Deák, T. Frauenheim, and A. Gali, Appl. Phys. Lett. **96**, 051909 (2010).
[17] P. Pyykkö and M. Atsumi, Chem. – Eur. J. **15**, 186–197 (2009).
[18] J. M. Knaup, P. Deák, T. Frauenheim, A. Gali, Z. Hajnal, and W. J. Choyke, Phys. Rev. B **71**, 235321 (2005).
[19] J. M. Knaup, P. Deák, T. Frauenheim, A. Gali, Z. Hajnal, and W. J. Choyke, Phys. Rev. B **72**, 115323 (2005).
[20] P. Deák, A. Gali, J. Knaup, Z. Hajnal, T. Frauenheim, P. Ordejón, and W. J. Choyke, Phys. B **340–342**, 1069 (2003).
[21] M. Vörös, P. Deák, T. Frauenheim, and A. Gali, Mater. Sci. Forum **679/680**, 516–519 (2011).
[22] B. Hornetz, H. J. Michel, and J. Halbritter, J. Mater. Res. **9**, 3088 (1994).
[23] K. Chang, N. Nuhfer, L. Porter, and Q. Wahab, Appl. Phys. Lett. **77**, 2186 (2000).
[24] W. Humphrey, A. Dalke, and K. Schulten, J. Mol. Graphics **14**, 33–38 (1996).
[25] $\text{DFTB}^+$. www.dftb-plus.info.