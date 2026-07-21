![](./images/812448163737632769_1.jpg)

2 March 2001

Chemical Physics Letters 335 (2001) 517-523

# MD simulations of a doped ceria surface – very large surface ion motion

Micael Baudin $^{a}$, Mark Wojcik $^{a}$, Kersti Hermansson $^{a,*,}$, Anders E.C. Palmqvist $^{b}$, Mamoun Muhammed $^{c}$

$^{a}$ Department of Materials Chemistry, The Ångström Laboratory, Uppsala University, P.O. Box 538, S-751 21 Uppsala, Sweden
$^{b}$ Department of Applied Surface Chemistry, and Competence Centre for Catalysis-KCK, Chalmers University of Technology, S-41296 Göteborg, Sweden
$^{c}$ Department of Materials Chemistry, Royal Institute of Technology, KTH, S-100 44 Stockholm, Sweden

Received 13 July 2000; in final form 18 August 2000

## Abstract
Mean-square displacements (MSDs) and individual-ion square-displacements (ISDs) for the different constituents in Ca-doped $CeO_{2}(011)$ slabs at 300 K have been studied as a function of depth from the surface. Constant pressure-constant temperature MD simulations were used. The MSDs are 2–3 times larger at the surface than in the bulk, but ISDs as large as ca. 150 times the surface MSD value were observed during short-time periods for anions next to an anion vacancy at the surface. The chemical implications of this kind of motion are important, since transient structural distortions of this magnitude will lead to large electron re-distributions. © 2001 Elsevier Science B.V. All rights reserved.

## 1. Introduction
Many theoretical investigations of *bulk metal oxides* using lattice dynamics, molecular dynamics and quantum mechanics have been reported, but only a small number of MD simulations have been published for metal oxide systems with *surfaces* present (see, for e.g., [1–6]). The quoted investigations were concerned with the interaction of argon with the rigid MgO(001) surface [1], the structures and relative surface energies for different faces of $\alpha$-Al₂O₃ [2,3], the effect of temperature on the *struc-ture* of lamellar MgO [4] and NiO [5] systems and the relaxation of atoms at a $Cr_{2}O_{3}(0001)$ surface [6]. To the best of our knowledge, no theoretical data *on the motion and vibrations of individual surface ions* have been presented until recently, and neither do any experimental data exist (partly because of experimental obstacles). In a few recent papers [7–9], we have investigated the surface dynamics for low-index non-reconstructing surfaces of some pure binary oxides using MD simulations. We found that, for the most stable faces and those of intermediate stability (such as MgO(011) or $CeO_{2}(011)$), both cations and anions increase their MSDs compared to the bulk values by a factor which typically lies in the range from 1.1 to 2.0. It will be seen in the following that also in doped ceria the surface MSDs increase by modest amounts – but other effects emerge.

*Corresponding author. Fax: +46-18-513548.
E-mail address: kersti@kemi.uu.se (K. Hermansson).

0009-2614/01/$ - see front matter © 2001 Elsevier Science B.V. All rights reserved.
PII: S0009-2614(01)00002-1

![](./images/812448163737632769_2.jpg)
www.elsevier.nl/locate/cplett

The reason ceria has attracted our attention is because of its important role in several catalytic processes [10]. Ceria is used as one of the main components in three-way catalysts (TWCs) for automotive emission control [11-13]. A TWC is capable of performing simultaneously the re- duction of nitrogen oxides and the oxidation of carbon monoxide and hydrocarbons [14]. Ceria is mainly included for its high oxygen storage capacity (OSC) [15], and the OSC of ceria is believed to be related to the formation and an- nihilation of oxygen-ion vacancies. Several at- tempts to investigate this phenomenon, both experimentally and with theoretical modelling, have been described in the literature (see, e.g.,[15-19]) and suggest a close connection between the high OSC and the non-stoichiometry, e.g., doping of ceria. Palmqvist et al. [18] studied the ceria-catalysed $SO_{2}+2CO \to S+2CO_{2}$ reaction in a series of experiments with controlled defect concentrations of e.g., the Ca, Co, Mn, Nd or Pb divalent ions, and found a correlation be- tween catalytic performance and dopant. Also the OSC demonstrated such a correlation. The exact mechanisms behind both the OSC and the suggested catalytic activity of ceria remain ob- scure, and one primary reason is that not even the atomic-level surface structure is known. In the current study, we have used molecular dy- namics simulations to determine both the ionic structure and motion at a $Ca^{2+}$-doped $CeO_{2}(\begin{array}{lll}0 & 1 & 1\end{array})$ surface.

In this Letter, we show that a doped $(\begin{array}{lll}0 & 1 & 1\end{array})$ surface undergoes large time-dependent variations, which we suggest need to be taken into account in any mechanistic explanation of the OSC and the catalytic function of ceria surfaces. Today's com- mercial TWCs most often use undoped, and not doped, ceria in contact with an alumina support. However, we have found similar large-scale mo- tions for undoped ceria surfaces in contact with an alumina interface [20], i.e., the phenomenon re- ported here is not an isolated example, but appears to occur in several cases when the oxide surface structure has been distorted in some way. In the present Letter, we discuss the phenomenon as suchand report the results for a Ca-doped ceria $(\begin{array}{lll}0 & 1 & 1\end{array})$  surface.

## 2. Method

### 2.1. System geometries
The pure $CeO_{2}$ bulk lattice has the well-known fluorite structure, in which each $Ce^{4+}$ cation is surrounded by eight equivalent $O^{2-}$ ions forming the corners of a cube, and with each $O^{2-}$ ion co ordinated to four $Ce^{4+}$ . Our $Ca^{2+}$-doped slab sys tem used in the MD simulation was periodic in two dimensions, with the free surfaces perpendicular to the $(\begin{array}{lll}0 & 1 & 1\end{array})$ and $(\begin{array}{lll}0 & \overline{1} & \overline{1}\end{array})$-directions (Fig. 1). The new $x$ and $y$-directions are the crystallographic $(\begin{array}{lll}1 & 0 & 0\end{array})$  and $(01 \overline{1})$ -directions. The $Ca^{2+}$-doping of theCeO2(0 1 1) slab system was performed as follows: three calcium ions were introduced in every second plane and charge-balanced by removing one nearest-neighbour oxygen in the same plane, to preserve the zero net dipole moment perpendicular to the surface. This will lead to a doping degree of1/8, since for the undoped slab system, the MD- box consisted of 12 planes with 12 cerium ions in every plane, and for the $Ca^{2+}$ -doped system three calcium ions replaced an equal number of cerium ions in every second plane, giving 18 calcium ions altogether in the cell. The oxygen-vacancy con- centration was $6.25 \%$ (half the dopant concentra tion). This particular dopant concentration was chosen to match recent neutron diffraction [19] and catalytic [18] measurements, where the dopant concentration had to be kept low to ensure the formation of one single phase in the synthesis. The fact that dopant ions were introduced in every second plane of a slab which consisted of an even number of planes will lead to different surface dopant arrangements at the two faces. On one side, the dopant-oxygen vacancy pairs were located in the top-most layer, and on the other, they were located in the second top-most layer.

### 2.2. Ionic motion quantification
To study the ionic motion as a function of depth, the slabs were divided into 12 slices(essentially the 12 ionic planes that the slab con- sists of), $1.94 \AA$ thick, and distributed symmetri cally around the middle of the slab. The average atomic mean-square displacement (MSD) was then

![](./images/812448163737632769_3.jpg)
![](./images/812448163737632769_4.jpg)

Fig. 1. The starting geometry for the Ca-doped CeO₂(0 1 1) slab system. The black, white and large gray spheres are the Ce⁴⁺, O²⁻ and Ca²⁺ ions, respectively. The systems are periodic in the xy-plane. Left: yz-plane towards viewer. Right: xz-plane towards viewer.

calculated as $\langle (\mathbf{r}_i(t)-\overline{\mathbf{r}}_i)^2 \rangle$, where the average was taken over time and over all atoms $i$ within the specified slice $(z,z+\Delta z)$, where $\Delta z=1.94$ Å. An ion contributes to the average of a particular slice as long as it resides in this slice, and $\overline{\mathbf{r}}_i$ is the average position over the whole run. In addition to this method of measuring the ionic motion, we have studied the individual-ion squared-displacement (ISD), $\text{ISD}(t)=(\mathbf{r}_i(t)-\overline{\mathbf{r}}_i)^2$ of each ion in the outermost surface layers as a function of time.

### 2.3. The MD program

A constant-stress, constant-temperature molecular dynamics program has been written to treat systems periodic both in three and two dimensions, with dynamically variable lattice vectors (lengths and angle) [21]. The equations of motion for the box were handled by the Cleveland modification [22] of the Raman-Parrinello scheme [23,24], and the Nosé-Hoover formalism [25,26] was used for the constant temperature control. The Gear predictor-corrector algorithm was use to solve Newton's equations of motion, to the sixth order for the motion of the shells, and to the fifth order for remaining degrees of freedom. The Ewald summation technique for both two and three-dimensional periodic systems [27-29] has been implemented. All ions were allowed to move in the MD simulations.

### 2.4. Interatomic potentials

The interatomic potential parameters used in the present investigation are summarized as

follows. The ion–ion interaction consists of three parts: a short-range potential of the form $V(r)=Ae^{-r/\rho}-Cr^{-6}$, a long-range Coloumb potential, and the shell model [30], which gives the polarisation energy according to the formula $V(D)=kd^{2}$ (where $d$ is the displacement of the shell relative to the core). We have also assigned a fraction of the ion-mass to the shells [31]. The short-range parameters for the $Ce^{4+}$–$O^{2-}$ interaction originate from Butler et al. [32], while the shell-model parameters for $Ce^{4+}$ and $O^{2-}$ were derived by Sayle et al. [16]. The short-range parameters for the $Ca^{2+}$–$O^{2-}$ interaction and the shell-model parameter for $Ca^{2+}$ were taken from Lewis et al. [33], while the parameters for the $O^{2-}$–$O^{2-}$ interaction were given in an early work on $UO_{2}$ by Catlow et al. [34].

### 2.5. The simulation runs

MD simulations at room temperature and atmospheric pressure were performed for the $Ca^{2+}$-doped $CeO_{2}(011)$ slab system, and – for comparative purposes – for the undoped $CeO_{2}(011)$ slab system, and for the three-dimensional $CeO_{2}$ bulk crystals (pure and doped). All systems were equilibrated for 1.0 ps with temperature-scaling invoked every 50th step, followed by 7.5 ps equilibration without temperature-scaling. Trajectories were then collected for 8.0 ps. All simulation runs used a time-step of 0.20 fs. Such a short time-step was necessary to ensure the constancy of the Hamiltonian in this system where the ionic charges and interatomic forces are large.

### 3. Comparison with experiment

In this Letter, we report computational results for quantities and phenomena which are unfortunately not yet available from experiment. It is, therefore, particularly important to discuss any relevant, related experimental data that may be used as a test of the credibility of our results.

The quality of our model potentials with respect to bulk structure (undoped and Ca-doped) were discussed in [17], where a comparison of the computed radial distribution functions with the related $T(r)$ functions from pulsed neutron scattering data demonstrated excellent agreement between experiment and theory. In particular, the considerable differences between the $T(r)$ curves for undoped and doped ceria were reproduced by the simulations, which furthermore helped elucidate the structural reasons behind some of the fine details in the experimental curves.

We have not found in the literature any experimental data relating to ceria surface dynamics. However, Faber Jr. et al. [35] have reported crystallographic Debye–Waller factors from X-ray and neutron diffraction experiments [36] of bulk ceria; their values are 1.02(13) and 1.71(8) $\mathring{A}^{2}$ for Ce and O, respectively, at $900^{\circ}C$, corresponding to $\langle u^{2}\rangle$ values (i.e., MSD values) of 0.013(2) and 0.022(1) $\mathring{A}^{2}$. For bulk ceria we have performed simulations at several temperatures in the region 10–1500 K (using the same models as those employed in the slab simulations at 300 K). Our resulting MSDs at $900^{\circ}C$ are 0.009 $\mathring{A}^{2}$ for Ce and 0.017 $\mathring{A}^{2}$ for O, in reasonable agreement with experiment.

### 4. Surface dynamics

The cation framework in ceria (both bulk and slab systems) is very rigid, and here we will only discuss the dynamics of the oxygen ions. In fact, for both the bulk and slab systems, the difference between the cation dynamics in the undoped and the doped systems is very small. Fig. 1 shows the starting geometry of the $Ca^{2+}$-doped $CeO_{2}(011)$ slab system. In Fig. 2, the slice-averaged atomic

![](./images/812448163737632769_5.jpg)

Fig. 2. Oxygen ion mean-square displacement (MSD) as a function of depth in the slab. Zero is in the middle of the slab.

MSDs throughout the whole slab at 300 K are shown, and compared with the $Ca^{2+}$-doped bulk value. It can be seen that the oxygen ions have an MSD (average of $x$, $y$ and $z$) about twice as high at the surface compared to the bulk. The average MSD for the oxygen ions in the middle of the slab is essentially the same as in the bulk.

The MSDs for the undoped ceria are smaller. In the middle of the slab, the magnitude of the oxygen MSD is about 85% of the doped ceria value ($0.0039$ $\AA^2$ compared to $0.0046$ $\AA^2$ for the doped system) and at the surface the MSD is about 2/3 of the value in the doped material.

We will now discuss the anisotropy of the bulk and surface oxygen motion. In the *undoped* bulk ceria structure, motion along the $y$- and $z$-directions is equivalent, while the MSD in the $x$-direction is somewhat different, due to structural anisotropy. The introduction of a surface breaks the symmetry and an increase in the dynamics can be observed in all three directions, but more importantly, it breaks the equivalence between the motion in the $y$- and $z$-directions. In the MD simulation the MSDs in the $x$- and $z$-directions increase to about $0.0065$ $\AA^2$, while the increase in the $y$-direction is more modest (and stops at $0.005$ $\AA^2$). In *doped* ceria we find a larger increase of the MSD in the $x$-direction to $\sim 0.011$ $\AA^2$ on both sides of the slab, and the MSD in the $z$-direction increases to $\sim 0.009$ $\AA^2$. The motion in the $y$ direction is seen to be much more dopant-dependent. On the side where the dopant ions and the oxygen vacancies reside in the top-most layer, the motion is suppressed (essentially towards the bulk value), and on the side where the dopant-oxygen vacancy pairs were initially located in the second top-most layer, the motion is enhanced to $\sim 0.0085$ $\AA^2$. The latter observation can be explained by the fact that oxygen ions from the topmost layer have migrated down to the layer underneath, thereby creating new oxygen vacancies in the topmost layer. These oxygen vacancies remain 'co-ordinated' to the Ca-ions in the second layer. As a result, oxygen vacancies become located in the topmost layer on both sides of the slab system, but on one side, these are co-ordinated to Ca ions in the same plane, and on the other side they are co-ordinated to Ca ions in the plane below. The different surface structures at the two faces, thus, have a profound effect on the dynamics in the $y$-direction, and results in the 'unsymmetrical' MSD pattern (with respect to the two slab sides) displayed in Fig. 2.

When the displacements are studied as a function of time, it becomes apparent that some surface-oxygen ions show a significant increase in displacement for short periods of time (Fig. 3). The magnitude of these ISDs generally lie in the region $0.01$-$0.1$ $\AA^2$, i.e., $2$-$15\times$ the MSD value for the surface slices (cf. Fig. 2), but as can be seen, some oxygen ions displace as much as 170 times the surface MSD value (e.g., at 3.6 ps). These large displacements last for $0.1$-$0.7$ ps.

It is important to point out that these very large ISDs do not occur in the undoped material: the maximum found during 8 ps simulation of a pure ceria slab is only $0.20$ $\AA^2$ (i.e., about the same as the small peak at 3.0 ps in Fig. 3. In the doped bulk material, the largest ISD is $0.20$ $\AA^2$. Both the OSC (see Section 1) and the catalytic functionality are probably mainly concerned with the immediate surface layer, and in the following we will limit our discussion to the surface dynamics.

The peak-shaped form of the ISDs in Fig. 3 show that the large displacements do not originate from migrations. The mechanism can be further illuminated by scrutinizing the Ce-O distance during the large displacements. The Ce-O1 bond in Fig. 3, for example, is elongated from its equilibrium value of $2.3$ $\AA$ to more than $3.8$ $\AA$ during the displacement. The O1 ion temporarily dis-

![](./images/812448163737632769_6.jpg)

Fig. 3. The individual-ion squared displacements (ISD) (averaged for $x$, $y$ and $z$) for four selected surface-oxygen ions, all coordinating the same surface-cerium ion (there are 24 surface-cations in total). They all lie in roughly the same $xy$-plane.

places towards the empty space given by a vacancy nearby, leading to a very much less bound oxygen ion. Fig. 4 illustrates the displacement.

Even though the magnitude of the ISD for a surface oxygen is related to its coordination, this does not entirely explain the phenomenon ob- served. At its equilibrium position during the simulation, the O1 ion has a coordination number of 3. The bridge oxygens ((B) in Fig. 4), on the other hand, have a coordination number of 2 only, but despite this, do not exhibit any large instan- taneous displacements. The overall preference to displace is a complex consequence of the number and strengths of the Ce-O bonds and the existence of fairly empty space nearby.

![](./images/812448163737632769_7.jpg)

Fig. 4. Snapshot of the individual surface structure at 300 K after 3.6 ps. The upper figure is a topview, and the lower is a sideview (cf. the ordered structure in Fig. 1). The displacement of one selected oxygen ion (O1) is indicated by the arrow in the upper figure. The arrow points from the ion's equilibrium po- sition towards its maximum displacement. The bridging oxygen ions (denoted 'B' in the figure) are discussed in the text.

The displacements illustrated in Fig. 3 are not exotic events. One-sixth of the topmost surface oxygens are structurally very similar to O1, and also perform similarly large excursions.

## 5. Chemical implications

We have found that $Ca^{2+}$-doped $CeO_{2}(011)$ surfaces contain oxygen species which exhibit very large displacements from their equilibrium posi- tions. The large amplitudes are connected to structurally short-lived (0.5-1.0 ps) distortions from the average structure, and arise from the more 'porous' structure that doping with, for ex- ample, $Ca^{2+}$-ions gives. Here, we have focussed on describing the dynamics occurring, which is an important topic per se, since virtually no such data - experimental or theoretical exist - in the litera- ture. However, the implications of this motion are greater. We believe that such ionic displacements, involving large cation-anion elongations, will lead to charge redistributions and the creation of local electric fields, and have a profound impact on many adsorbate-substrate interactions and disso- ciation processes.

In this connection, it should also be of interest to discuss the time scales involved. Let us consider an atom or molecule adsorbed on the oxide surface, and more specifically, adsorbed at the type of sur- face defect we have described in this Letter, namely, an anion vacancy and its structurally dis- torted arrangement of neighbouring oxygen ions. An estimate of the average residence time of the adsorbate on the surface is given by $\tau=\tau_{0} \exp [\Delta H_{ads}/(RT)]$, where $\tau_{0}$ is correlated with the surface atom vibration period and $\Delta H_{ads}$ has a positive sign for stabilizing energies [37]. $\tau_{0}$ is typ ically of the order of 0.1 ps (see Fig. 3). Let us as- sume that the adsorbate is bound to the surface via chemisorption of a rather modest strength with a $\Delta H_{ads}$ value of, say, 30 kJ/mol. At 300 K, $\tau$ becomes ca. 18000 ps (and ca. 18 ps at 700 K, which is close to the functional temperature in car catalysts). The large-amplitude motions we have observed in our model calculations occur approximately every 5 ps (based on more data, not shown here), and an adsorbate molecule is therefore likely to experience

such a dynamic event during its interaction with the surface. In conclusion, if our model calculations of $Ca^{2+}$-doped ceria reflect reality, then large-amplitude oxygen motion at defect surface sites takes place, and it takes place often enough to affect the adsorbate-substrate interaction and the doped material's catalytic activity.

## Acknowledgements

The Swedish Natural Science Research Council (NFR) and Ångpanneföreningens Forskningss-tiftelse (ÅF) are gratefully acknowledged for financial support.

## References

[1] A. Alavi, I.R. McDonald, Mol. Phys. 69 (1990) 703.
[2] S. Blonski, S.H. Garofalini, Surf. Sci. 295 (1993) 263.
[3] L.J. Alvarez, L.E. Leon, J.F. Sanz, M.J. Capitan, J.A. Odriozola, Phys. Rev. B 50 (1994) 2561.
[4] R. Ferneyhough, D. Fincham, G.D. Price, M.J. Gillan, Modelling Simul. Mater. Sci. Eng. 2 (1994) 1101.
[5] P.M. Oliver, G.W. Watson, S.C. Parker, Phys. Rev. B 52 (1995) 5223.
[6] F. Rohr, M. Baumer, H.-J. Freund, J.A. Mejias, V. Staemmler, S. Muller, L. Hammer, K. Heinz, Surf. Sci. 372 (1997) L291.
[7] M. Baudin, M.C. Wojcik, K. Hermansson, Phys. Chem. Chem. Phys. (2001) submitted.
[8] M. Baudin, M.C. Wojcik, K. Hermansson, Surf. Sci. (2000) in press.
[9] M. Baudin, K. Hermansson, Surf. Sci. (2000) (submitted).
[10] A. Tscöpe, J.Y. Ying, in: G.C. Hadjipanayis, R.W. Siegel (Eds.), Nanophase Materials: Synthesis-Properties-Applications, Kluwer, London, 1994, p. 781.
[11] Nippon Shoukai Ltd., Eur. Pat. 507590a, 1993.

[12] N.E.Chemcat K.K., Jpn. Pat. 4284847, 1993.
[13] Kyatara Kogyo K.K., Jpn. Pat. 4180835, 1993.
[14] J. Barbier, D. Duprez, Appl. Catal. B Env. 4 (1994) 105 (and references therein).
[15] Y.F. Yu Yao, J. Catal. 87 (1984) 152.
[16] T.X.T. Sayle, S.C. Parker, C.R.A. Catlow, J. Phys. Chem. 98 (1994) 13625.
[17] J. Soria, A. Martinez-Arias, J. Conesa, J. Chem. Soc. Faraday Trans. 91 (1995) 1669.
[18] A.E.C. Palmqvist, M.F.M. Zwinkels, Y. Zang, S.G. Järås, M. Muhammed, Nanostructured Materials 8 (1997) 801.
[19] S. Carolis, J.L. Pascual, L.G.M. Pettersson, M. Baudin, M. Wojcik, K. Hermansson, A.E.C. Palmqvist, M. Muhammed, J. Phys. Chem. B 103 (1999) 7627.
[20] M. Baudin, M.C. Wojcik, K. Hermansson, Thin Solid Films (2000) accepted.
[21] M. Baudin, M. Wojcik, K. Hermansson, Surf. Sci. 375 (1997) 374.
[22] C.L. Cleveland, J. Chem. Phys. 89 (1988) 4987.
[23] M. Parrinello, A. Raman, Phys. Rev. Lett. 45 (1980) 1196.
[24] M. Parrinello, A. Raman, J. Appl. Phys. 52 (1981) 7182.
[25] S. Nosé, J. Chem. Phys. 81 (1984) 511.
[26] W.G. Hoover, Phys. Rev. A 31 (1985) 1695.
[27] P.P. Ewald, Ann. Phys. 64 (1921) 253.
[28] D.E. Parry, Surf. Sci. 49 (1975) 433 (Erratum, Surf. Sci. 54 (1976) 195).
[29] D.M. Heyes, M. Barber, J.H.R. Clarke, J. Chem. Soc. Faraday Trans. II 10 (1977) 1485.
[30] B.G. Dick, A.W. Overhauser, Phys. Rev. 112 (1958) 90.
[31] P.J. Mitchell, D. Fincham, J. Phys. Condens. Matter 5 (1993) 1031.
[32] V. Butler, C.R.A. Catlow, B.E.F. Fender, J.H. Harding, Solid State Ionics 8 (1983) 109.
[33] G.V. Lewis, C.R.A. Catlow, J. Phys. C: Solid State Phys. 18 (1985) 1149.
[34] C.R.A. Catlow, Proc. R. Soc. A 333 (1977) 533.
[35] J. Faber Jr., M.A. Seitz, M.H. Mueller, J. Phys. Chem. Solids 37 (1976) 909.
[36] J. Faber Jr., M.A. Seitz, M.H. Mueller, J. Phys. Chem. Solids 37 (1976) 903.
[37] F.C. Tompkins, Chemisorption of Gases on Metals, Academic Press, New York, 1978.