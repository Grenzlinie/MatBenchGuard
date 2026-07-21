![](./images/813115774653693953_1.jpg)

Surface Science 465 (2000) 65-75

![](./images/813115774653693953_2.jpg)

# Structural and dynamical behavior of Al trimer on Al(111) surface

### C.M. Chang $^{a,*}$, C.M. Wei $^{b}$, S.P. Chen $^{c}$

$^{a}$ National Center for High-Performance Computing, Hsinchu, Taiwan 30043, Republic of China
$^{b}$ Institute of Physics, Academia Sinica, Nankang, Taipei, Taiwan 11529, Republic of China
$^{c}$ Theoretical Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA

Received 16 March 2000; accepted for publication 5 June 2000

## Abstract

Trimer is the smallest cluster that can have a one-dimensional or two-dimensional structure on surfaces, and it can diffuse and transform between these structures. Using first-principles density-functional theory (DFT) calculations, the structural and dynamical behaviors of Al trimer on Al(111) surface have been studied in detail. Al trimer on Al(111) surface has three different kinds of structure conformations (groups with similar configurations): close-packed (compact) triangular trimers, non-compact triangular trimers, and linear trimers. The close-packed triangular trimers are more stable than the non-compact triangular trimers and the linear trimers, while most of the non-compact triangular trimers are as stable as the linear trimers. For the dynamics of Al trimer on Al(111) surface, there are three different kinds of diffusion mechanisms: (1) concerted translations and rotation of compact triangular trimers (the highest energy barrier by DFT calculation, $E_{\text{d}}$=0.24 eV); (2) back-and-forth transformation between compact triangular trimers and linear trimers ($E_{\text{d}}$=0.21 eV); and (3) translation of linear trimers ($E_{\text{d}}$=0.28 eV). Among these different mechanisms with similar height of diffusion barriers, the concerted translations of the compact triangular trimers have the longest displacement of the center of mass in the least steps. Therefore, we expect the long-range diffusion of Al trimer on Al(111) surface is dominated by the concerted motion process of the compact triangular trimers. The concerted translations and concerted rotations of Al trimer on Al(111) surface have also been observed in the molecular dynamics simulations using the embedded atom method. © 2000 Elsevier Science B.V. All rights reserved.

**Keywords:** Aluminum; Density functional calculations; Molecular dynamics; Surface diffusion

---

## 1. Introduction

Knowledge of surface diffusion is essential for a detailed understanding of the mechanisms of many surface phenomena where the transport of atoms is involved. These phenomena include nucle-ation and growth of surface layer, heterogeneous catalysis, phase transitions, segregation and sin-tering, etc. [1]. In recent years, considerable pro-gress has been achieved in the study of surface diffusion and related phenomena, owing to signifi-cant improvements in experimental techniques [2,3]. Although a considerable amount of experi-mental information is now available for single-atom diffusion (for a collection of works for diffu-sion on metal surfaces, see Ref. [4], for example), relatively little is known about the details of cluster diffusion on surfaces. The diffusion of clusters on metal surfaces involves a sequence of steps that

* Corresponding author. Fax: +886-3-5773538.
E-mail address: c00jim00@nchc.gov.tw (C.M. Chang)

0039-6028/00/$ - see front matter © 2000 Elsevier Science B.V. All rights reserved.
PII: S0039-6028(00)00663-4

result in displacements of the center of mass and changes in the configurations of the cluster. A complete characterization of the diffusion process of the cluster, even for the case of dimers, is therefore much more complicated than that for single atoms. Due to the complicated nature of the diffusion process, the detailed migration mech- anisms of the clusters on metal surfaces have been solved for only a few cases [4–6].

fcc (111) surfaces possess two different adsorp- tion sites: the fcc site, which corresponds to a fcc stacking, and the hcp site, which corresponds to a hcp stacking (see Fig. 1). A cluster on fcc (111) surface can have different configurations according to the adsorption sites, the position of the center of mass, and the shape of the cluster. The cluster can diffuse on the surface and can be transformed back and forth among these different configura- tions, and this makes the diffusion behavior more complicated than the adatom diffusion. The trimer is the smallest cluster that can have a one-dimen- sional or a two-dimensional structure. On the fcc (111) surface, the only detailed experimental study of which we are aware for the diffusion behavior of clusters larger than dimers was done using thefield ion microscope (FIM) [2] for $Ir_{n}/Ir(111)$ [5,6]. For a theoretical study of trimer diffusion on fcc (111) surface, there exist two embedded atom method (EAM) [7,8] calculations for $Ir_{n}/Ir(111)$ [9] and $Ni_{n}/Ni(111)$ [10]. However, these calculations lack some of the configurations that trimers may have and ignore some of the possible diffusion paths, especially the transforma- tion between linear trimers and triangular trimers.

![](./images/813115774653693953_3.jpg)

Fig. 1. Various Al trimer configurations on the Al(111) surface. (a) Compact triangular trimers. (b) Linear trimers. (c) Non-compact triangular trimers. Numbers under each panel are the total energies of the structures referred to the most stable configuration, FCC-H. The nomenclature is described in Section 3.1. The two non-compact triangular configurations, $2 ~F 1 H-90^{\circ}$ and $1 ~F 2 H-90^{\circ}$ , are not stable structures. The energies shown for these two structures are obtained by fixing one coordinate of the atoms marked by an asterisk; otherwise, the marked atoms would move back to form compact triangular trimers.

Recently, a first-principles calculation of Al dimer dynamics on Al(111) surface was reported [11], but there are no first-principles results for the structural and dynamical behavior of clusters with sizes larger than the dimer on a fcc (111) surface. Homoepitaxial trimer energetics on the Mg(0001) surface has been studied using the effective- medium theory by Tian et al. [12].

In this paper, we use the first-principles density- functional theory (DFT) [13,14] to calculate the structural and dynamical behavior of Al trimer on Al(111) surface. The structural stabilities, diffu- sion mechanisms and their corresponding activa- tion barriers are studied in detail. The trajectories of the diffusion processes are also simulated by molecular dynamics (MD) simulations using the embedded atom method. The paper is organized as follows. We give a brief description of the calculation method in Section 2. In Section 3, the results and discussions for the structural and dynamical behavior of Al trimer on Al(111) sur- face are presented in detail. Summaries and conclu- sions are given in Section 4.

## 2. Methods of calculations

### 2.1. First-principles density-functional theory calculation

The DFT calculations reported here were per- formed using the Vienna ab-initio simulation pack- age (VASP) [15-18] and its corresponding ultrasoft-pseudopotential [19]. The exchange-cor- relation functional is treated in the local-density approximation (LDA) [20,21] with Ceperley- Alder exchange potential ([22], as parametrized by Perdew and Zunger [23]). The wave functions are represented using a plane wave basis set with a kinetic energy cut-off of 9.5 Ry.

The supercell geometry used in this study is simu- lated by a repeating slab of six atomic layers with a vacuum region of $9.4\,\mathring{A}$. The Al trimer is added on one side of the surfaces. In the lateral directions, we use a hexagonal $(5\times5)$ surface unit cell, i.e. 25 atoms in each atomic layer. In the calculations, the trimer and the top three atomic layers are allowed to relax to their lowest energy positions. All the other atoms are kept at the bulk positions (LDA lattice constant, $a_0=3.98\,\mathring{A}$). For the k-point summations in the calculations, we took a $(2\times2)$ Monkhorst-Pack [24] k-point mesh in the surface Brillouin zone (SBZ). The geometry is optimized until the total energy is converged to $10^{-5}$ eV.

The sensitivity of the total energies on k-point summations, sizes of surface unit cell, slab and vacuum thickness, number of relaxed layers, etc., has been examined extensively. The results of the convergence test are summarized in Table 1. We can see from cases 1-3 that the $2\times2$ Monkhorst- Pack k-point mesh in the SBZ is enough for the k-point summation in this study. When the size of

<table>
<caption>Table 1<br>Convergence test of the total energy difference ($E_{\text{diff}}$) with respect to the vacuum space ($D_{\text{vac}}$), number of relaxed layers ($N_{\text{rl}}$), number of atomic layers ($N_{\text{l}}$), surface cell size, and k-point mesh in the SBZ$^{\text{a}}$</caption>
<thead>
<tr>
<th>Case</th>
<th>$D_{\text{vac}}$ ($\mathring{A}$)</th>
<th>$N_{\text{rl}}$</th>
<th>$N_{\text{l}}$</th>
<th>Surface cell</th>
<th>k-point mesh</th>
<th colspan="3">$E_{\text{diff}}$ (eV)</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>HCP-T</th>
<th>HCP-L</th>
<th>3LB</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>11.7</td>
<td>2</td>
<td>5</td>
<td>$5\times5$</td>
<td>$1\times1$</td>
<td>0.03</td>
<td>0.19</td>
<td>0.30</td>
</tr>
<tr>
<td>2</td>
<td>11.7</td>
<td>2</td>
<td>5</td>
<td>$5\times5$</td>
<td>$2\times2$</td>
<td>0.12</td>
<td>0.24</td>
<td>0.38</td>
</tr>
<tr>
<td>3</td>
<td>11.7</td>
<td>2</td>
<td>5</td>
<td>$5\times5$</td>
<td>$3\times3$</td>
<td>0.09</td>
<td>0.24</td>
<td>0.37</td>
</tr>
<tr>
<td>4</td>
<td>11.7</td>
<td>2</td>
<td>5</td>
<td>$6\times6$</td>
<td>$2\times2$</td>
<td>0.10</td>
<td>0.24</td>
<td>0.40</td>
</tr>
<tr>
<td>5</td>
<td>11.7</td>
<td>3</td>
<td>5</td>
<td>$5\times5$</td>
<td>$2\times2$</td>
<td>0.11</td>
<td>0.24</td>
<td>0.36</td>
</tr>
<tr>
<td>6</td>
<td><b>9.4</b></td>
<td><b>3</b></td>
<td><b>6</b></td>
<td><b>$5\times5$</b></td>
<td><b>$2\times2$</b></td>
<td><b>0.07</b></td>
<td><b>0.15</b></td>
<td><b>0.29</b></td>
</tr>
<tr>
<td>7</td>
<td>7.1</td>
<td>4</td>
<td>7</td>
<td>$5\times5$</td>
<td>$2\times2$</td>
<td>0.09</td>
<td>0.15</td>
<td>0.30</td>
</tr>
<tr>
<td>8</td>
<td>20.9</td>
<td>4</td>
<td>6</td>
<td>$5\times5$</td>
<td>$2\times2$</td>
<td>0.08</td>
<td>0.15</td>
<td>0.28</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9">$^{\text{a}}$ The total energy difference is referred to the most stable structure, FCC-H. Structural configurations can be found in the text and figures, except the 3LB structure, which is the intermediate state for the intercell translation of linear trimer. The parameter set used in this study is in the sixth case with bold numbers shown in bold.</td>
</tr>
</tfoot>
</table>

the surface unit cell increases from a $(5 \times 5)$ to a $(6 \times 6)$ surface unit cell, the change of the total energy difference is less than 0.03 eV (see cases 2 and 4 in Table 1). For the convergence of slab thickness (see cases 5–7 in Table 1), increasing the number of atomic layers from six to seven results in changes of total energy difference by less than 0.02 eV. Increasing the vacuum thickness from 9.4 to $20.9 \mathring{A}$ and relaxing one more layer (from three to four layers) changes the total energy difference by less than 0.01 eV (see cases 6 and 8 in Table 1). For the present study, we use the bold parameter set in case 6 of Table 1, and the total energy differences are accurate to 0.03 eV.

### 2.2. Molecular dynamics simulations by the embedded atom method

The Al EAM potential used in this study is in the Voter–Chen form [25], and the parameters can be found in Refs. [25–27]. We use a slab with 11 layers, each layer consisting of 36 atoms, in the EAM-MD calculations. Periodic boundary conditions are applied in the $x$ and $y$ directions with free surfaces in the $z$ direction. The whole system is allowed to relax to the equilibrium structure before the MD run.

The procedures of the MD simulations are as follows. At first, the initial velocity components are assigned from a Maxwellian distribution appropriate to the desired temperature (ranging from 200 to 350 K in this study; the melting temperature of Al is 933.5 K). The dynamic processes of atoms in the system are determined by the numerical solution of the classical equation of motion, which can be integrated using the ‘velocity’ form of the Verlet algorithm [28]. Then, a 5 ps canonical equilibration run is made to ensure the system is equilibrated at the desired temperature. Afterwards, the system is left undisturbed in a 95 ps microcanonical simulation. The time step used in the MD simulation is chosen to be 1 fs, which is sufficiently small to simulate the diffusional processes, since the vibration period in metals is about 1 ps.

## 3. Results and discussions

We have calculated the total energies for different structural configurations and the energy barriers of various possible diffusion paths, including translations, rotations, and transformations of Al trimer on Al(111) surface. These results are discussed in the following subsections. We present the DFT results for the structural stabilities of Al trimers on Al(111) surface in Section 3.1. The diffusional paths and their corresponding migration energies for $\text{Al}_3/\text{Al}(111)$ obtained by DFT calculations are presented in Section 3.2. In Section 3.3, we show the trajectories of the diffusional processes obtained by molecular dynamics simulations with the embedded atom method.

### 3.1. Structural stabilities

Trimers on the fcc (111) surface can have a linear form or a triangular form. The configurations for trimers are much more complicated than the configurations for adatoms and dimers. Therefore, we group the trimer configurations into three different kinds of conformations (see Fig. 1 and Table 2). The first is the close-packed (compact) triangular trimer. There are four compact triangular configurations that can be identified as FCC-H, HCP-H, FCC-T, and HCP-T, as shown in Fig. 1a. The nomenclature used here is based on: (1) the trimer atoms sitting at fcc sites (FCC) or hcp sites (HCP) and (2) the center of mass of the trimer being on a hollow site (H) or a top site (T). We find that the most stable configuration for a close-packed Al triangular trimer is the FCC-H configuration. This configuration is lower in energy by 0.01, 0.05, and 0.07 eV than the HCP-H, FCC-T, and HCP-T configurations, respectively. The second is the linear trimer, which may have fcc linear (FCC-L) configuration and hcp linear (HCP-L) configuration, as can be seen in Fig. 1b. We find that the Al linear trimers are much more energetically unfavorable than the close-packed Al triangular trimers. The FCC-H compact trimer is more stable than the fcc linear (FCC-L) trimer and the hcp linear (HCP-L) trimer by 0.17 and 0.15 eV, respectively. These results are consistent with the experimental results for $\text{Ir}_n/\text{Ir}(111)$ [5], which show that the triangular trimers are found more frequently than linear trimers, and the compact triangular trimer, FCC-H, is the most stable configuration.

<table>
<caption>Table 2<br>Structural conformations, configurations and energies of an Al trimer on an Al(111) surface¹</caption>
<thead>
<tr>
<th colspan="2">Compact triangular trimer</th>
<th colspan="2">Linear trimer</th>
<th colspan="2">Non-compact triangular trimer</th>
</tr>
<tr>
<th>Configuration</th>
<th>Energy</th>
<th>Configuration</th>
<th>Energy (eV)</th>
<th>Configuration</th>
<th>Energy</th>
</tr>
</thead>
<tbody>
<tr>
<td>FCC-H</td>
<td>0.00</td>
<td>HCP-L</td>
<td>0.15</td>
<td>1F2H-120°</td>
<td>0.12</td>
</tr>
<tr>
<td>HCP-H</td>
<td>0.01</td>
<td>FCC-L</td>
<td>0.17</td>
<td>2F1H-150°</td>
<td>0.15</td>
</tr>
<tr>
<td>FCC-T</td>
<td>0.05</td>
<td></td>
<td></td>
<td>1F2H-150°</td>
<td>0.15</td>
</tr>
<tr>
<td>HCP-T</td>
<td>0.07</td>
<td></td>
<td></td>
<td>3H-120°</td>
<td>0.16</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2F1H-120°</td>
<td>0.16</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3F-120°</td>
<td>0.16</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>2F1H-90°</td>
<td>0.22</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>1F2H-90°</td>
<td>0.23</td>
</tr>
</tbody>
</table>

¹ The structural energies are referred to the most stable structure, FCC-H.

The third possibility is the non-compact triangular trimers. There are eight non-compact triangular trimer configurations lying between the compact triangular trimers and linear trimers, as shown in Fig. 1c. The meanings of the nomenclature, $nFmH$-$k^\circ$, for the non-compact triangular trimer are as follows: (1) $n$ denotes the number of trimer atoms sitting at fcc (F) sites, and $m$ denotes the remaining atom(s) sitting at hcp (H) sites ($n+m=3$); (2) $k^\circ$ denotes the obtuse angle of the non-compact triangular trimer. For example, the 2F1H-120° configuration means that there are two of the trimer atoms sitting at fcc sites and the remaining one sitting at hcp site, and the obtuse angle is about 120°. We find that most of these non-compact triangular trimers, except the two configurations of 1F2H-90° and 2F1H-90°, are as stable as the linear ones (see Fig. 1 and Table 2). The 1F2H-90° and 2F1H-90° configurations are not stable structures for $\text{Al}_3/\text{Al}(111)$. The energies shown in Fig. 1 and Table 2 for 1F2H-90° and 2F1H-90° trimers are obtained by fixing one coordinate of the atoms marked by an asterisk, as shown in Fig. 1c; otherwise, the marked atoms would move back to form compact triangular trimers. From Fig. 1c, we can see that the most stable configuration among these non-compact triangular Al trimers is the 1F2H-120° configuration, which is lower in energy by 0.03 and 0.05 eV than the HCP-L and FCC-L linear trimers, respectively. This result is not surprising because in the 1F2H-120° structure, the central atom (at fcc site) and the two end atoms (at hcp sites) have formed two ‘mixed FCC-HCP dimers’, which are more stable than the unmixed FCC-FCC and HCP-HCP dimers [11].

### 3.2. Diffusion mechanisms

Because of the various structures that Al trimers can have on Al(111) surface, the diffusion behaviors are complicated, so we group them into three different kinds of mechanisms (see Table 3). The first is the diffusion of compact triangular trimers. For close-packed triangular trimer diffusions, there are three kinds of diffusion paths, according to their initial and final states of the triangular trimer (see Fig. 2). For $\text{Al}_3/\text{Al}(111)$, the diffusion between FCC-H and HCP-T configurations has an energy barrier of 0.24 eV and translates the trimer by a distance of $(\sqrt{6}/6)a_0$. The energy barrier for diffusion between FCC-T and HCP-H configurations, which also translates the trimer by a distance of $(\sqrt{6}/6)a_0$, is 0.22 eV. Both of these two concerted translations can result in a long-range diffusion by repeating the same process. For the rotational process (without any net displacement) from FCC-T to HCP-T configurations, the energy barrier is 0.02 eV (with respect to the FCC-T configuration), and the barrier for the reverse process is 0.00 eV. For this low barrier of the rotational processes, one would expect the compact trimer (with the center of mass on top of a surface atom) to rotate freely, even at very low temperatures.

In calculating these diffusion processes, we

<table>
<caption>Table 3: Diffusion processes, paths, energy barriers ($E_{\text{d}}$), and displacement of the center of the mass ($d_{\text{cmass}}$) for the Al trimer on Al(111) surfaces<sup>a</sup></caption>
<thead>
<tr>
<th>Diffusion process</th>
<th>Diffusion path</th>
<th>$E_{\text{d}}$</th>
<th>$d_{\text{cmass}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><i>Compact triangular trimer diffusion</i></td>
</tr>
<tr>
<td>Concerted intercell</td>
<td>FCC-H$\leftrightarrow$HCP-T</td>
<td>0.24</td>
<td>$\sqrt{6}/6a_{0}$</td>
</tr>
<tr>
<td>Translation</td>
<td>FCC-T$\leftrightarrow$HCP-H</td>
<td>0.22</td>
<td>$\sqrt{6}/6a_{0}$</td>
</tr>
<tr>
<td>Intracell rotation</td>
<td>FCC-T$\leftrightarrow$HCP-T</td>
<td>0.07</td>
<td>Local</td>
</tr>
<tr>
<td colspan="4"><i>Transformation between triangular and linear trimers</i></td>
</tr>
<tr>
<td>Atom-by-atom</td>
<td>FCC-H$\leftrightarrow$1F2H-120°$\leftrightarrow$FCC-L 2F1H-120°$\leftrightarrow$HCP-H</td>
<td>0.21</td>
<td>$\sqrt{6}/6a_{0}$</td>
</tr>
<tr>
<td>Intercell transformation</td>
<td>FCC-H$\leftrightarrow$1F2H-120°$\leftrightarrow$HCP-L 2F1H-120°$\leftrightarrow$HCP-H</td>
<td>0.21</td>
<td>$\sqrt{6}/6a_{0}$</td>
</tr>
<tr>
<td colspan="4"><i>Linear trimer diffusion</i></td>
</tr>
<tr>
<td>Intercell translation</td>
<td>FCC-L$\leftrightarrow$HCP-L</td>
<td>0.28</td>
<td>$\sqrt{6}/6a_{0}$</td>
</tr>
<tr>
<td>Intracell translation</td>
<td>FCC-L$\leftrightarrow$HCP-L</td>
<td>0.25</td>
<td>Local</td>
</tr>
<tr>
<td>Atom-by-atom</td>
<td>FCC-L$\leftrightarrow$2F1H-120°$\leftrightarrow$HCP-L</td>
<td>0.19</td>
<td>Local</td>
</tr>
<tr>
<td>Intracell transformation</td>
<td>FCC-L$\leftrightarrow$1F2H-120°$\leftrightarrow$HCP-L</td>
<td>0.19</td>
<td>Local</td>
</tr>
</tbody>
</table>

<sup>a</sup> Energy is in electron-volts, and $a_{0}$ is the lattice constant.

![](./images/813115774653693953_4.jpg)

Fig. 2. Structural configurations, diffusion paths and the corresponding energy barrier profile for the concerted motions of close-packed Al triangular trimers on Al(111) surface. Translations of the compact trimer (FCC-T$\leftrightarrow$HCP-H; FCC-H$\leftrightarrow$HCP-T) are accomplished by concerted motion of three trimer atoms. Rotation between FCC-T and HCP-T states is also accomplished by concerted motions. Numbers under each panel are the total energies of the structures referred to the most stable configuration, FCC-H. Arrows indicate the diffusion paths, and the numbers near the arrows are the total energies (also referred to the FCC-H configuration) of the transition state with the moving atom(s) at the bridge site(s). The energy unit is in electron-volts.

move the trimer atoms along the diffusion paths and fix only one coordinate of a trimer atom. After relaxation, all the trimer atoms still bind together, thus indicating that the concerted motion of trimer atoms accomplishes the compact triangular trimer diffusion.

The second mechanism is the back-and-forth transformation between the close-packed triangular trimer and the linear trimer. There are many possible diffusion paths with similar diffusion barriers for the transformation mechanism. Among all these possible diffusion paths, two of the short-

![](./images/813115774653693953_5.jpg)

Fig. 3. Two shortest diffusion paths and their corresponding energy barrier profiles for the transformation between the compact Al triangular trimers (FCC-H, HCP-H) and the Al linear trimers (FCC-L, HCP-L) on Al(111) surface. The meanings of the numbers are the same as those in Fig. 2.

est paths are shown in Fig. 3. These two paths of (a) FCC-H↔1F2H-120°↔FCC-L↔2F1H-120°↔HCP-H and (b) FCC-H↔1F2H-120°↔HCP-L↔2F1H-120°↔HCP-H have the same diffusion barrier of 0.21 eV, and result in displacement of the center of mass by a distance of $(\sqrt{6}/6)a_{0}$ and the rotation of the trimer by $60^{\circ}$. However, two of the close-packed triangular trimer configurations, FCC-T and HCP-T, cannot be reached by this back-and-forth transformation mechanism. The translation and rotation of the compact trimer between FCC-H and HCP-H can also result from the concerted motions, as shown in Fig. 2. In the concerted motion process (FCC-H↔HCP-T↔FCC-T↔HCP-H), which needs one step less than the steps of the transformation processes mentioned above, the trimer is rotated by $60^{\circ}$, and the center of mass is displaced by a distance of $(\sqrt{6}/3)a_{0}$, which is twice as long as the distance $((\sqrt{6}/6)a_{0})$ displaced by the transformation mechanism.

The third mechanism is the diffusion of linear trimers. There are two concerted translational paths with the same displacement of $(\sqrt{6}/6)a_{0}$ (see Fig. 4 and Table 3) for the diffusion of linear trimers. The first is a translation at an angle of $\pm 30^{\circ}$ with respect to the linear trimer axis and results in a long-range (intercell) diffusion if the process is repeated alternately. The other is a local movement (intracell diffusion), in the direction perpendicular to the linear trimer, which can only move back and forth between the fcc and the hcp sites. The energy barriers are 0.28 eV for the long-range diffusion and 0.25 eV for the local movement. The local movement of the linear trimer can also be accomplished by individual atomic jumps of the trimer atoms. The shortest paths for the atom-by-atom local movements, FCC-L↔1F2H-120°↔HCP-L and HCP-L↔2F1H-120°↔FCC-L (see Fig. 4 and Table 3) have the same energy barrier of 0.19 eV, which is lower than the energy barrier for the concerted local movement.

![](./images/813115774653693953_6.jpg)

Fig. 4. Diffusion paths and their corresponding energy barrier profile for the intercell and intracell diffusions of Al linear trimers on Al(111) surface. The meanings of the numbers are the same as those in Fig. 2.

Hence, the local diffusion of the linear trimer should be accomplished by jumps of individual atoms.

Any one of the three different mechanisms discussed above can achieve a long-range diffusion of the trimer (see Table 3). For a displacement of the center of mass by a distance of $(\sqrt{6}/6)a_{0}$, the concerted translation of compact triangular trimer needs only one step with an energy barrier of 0.22 or 0.24 eV. The back-and-forth transformation between triangular and linear trimers, with an energy barrier of 0.21 eV, needs four steps to achieve this displacement. Although the intercell translation of the linear trimer also has a displacement of $(\sqrt{6}/6)a_{0}$ in one step, it needs a slightly higher migration energy of 0.28 eV. Therefore, we expect the long-range diffusion of Al trimer on Al(111) surface to be dominated by the concerted motion process of the compact triangular trimers, which has the largest displacement in the least number of steps and a relatively low diffusion barrier.

### 3.3. Molecular dynamics simulations

To further test the findings of the static DFT calculations, we also performed molecular dynamics simulations with the embedded atom method to determine the diffusion trajectories for Al trimer on Al(111) surface. Consistent with the static DFT calculations, the MD trajectories show that the translation of the compact Al triangular trimer is accomplished by the concerted motions (FCC-H$\leftrightarrow$HCP-T in Fig. 5a and FCC-T$\leftrightarrow$HCP-H in Fig. 5b) that the three trimer atoms moved together. During the four 100 ps simulations at $T$=200, 250, 300, and 350 K, no individual atomic jumps are observed. The rotational process between the FCC-T and HCP-T (Fig. 2) configurations are also observed in the MD simulations (see Fig. 6). In these MD simulations, the rotational process has many more events than the translation process. This is also consistent with the DFT results that the rotational process has a much lower diffusion barrier than the translation process¹. However, there are too few events to obtain a good statistical estimate of the diffusion energies and prefactors from the present

---
¹ In fact, we observed the rotational mechanism in the EAM-MD simulation first and found that it occurred more frequently than the translation mechanism. Then, we used the first-principle DFT to calculate the rotational energy barrier, and found that the rotational energy barrier was much lower than the translational energy barrier.

![](./images/813115774653693953_7.jpg)

Fig. 5. Snapshots of the trajectories for concerted translations of $Al_3$/Al(111) by EAM-MD simulations at 300 K. (a) from FCC-H to HCP-T; (b) from FCC-T to HCP-H.

![](./images/813115774653693953_8.jpg)

Fig. 6. Snapshots of the trajectories for concerted rotations of $Al_3$/Al(111) by EAM-MD simulations at 300 K: (a) from FCC-T to HCP-T; (b) from HCP-T to FCC-T.

EAM-MD simulations. Further detailed studies are needed to extract these quantities.

## 4. Summaries and conclusions

The trimer is the smallest cluster that can have a one-dimensional or a two-dimensional structure on surfaces, and it can diffuse and transform between these structures. The relatively stability of the different structures and the diffusion dynamics may affect the island morphology during crystal or thin-film growth. In this paper, we have studied the structures and dynamics for Al trimer on Al(111) surface in detail by first-principles density-functional theory calculations. Among the various trimer configurations, we find that the fcc compact triangular trimers with the center of mass above hollow sites are the most stable configurations (FCC-H). All the compact triangular trimers are more stable than the non-compact triangular trimers and the linear trimers, while most of the non-compact triangular trimers are as stable as the linear trimers.

The diffusional dynamics for Al trimer on Al(111) surface can be split into three different mechanisms. The first mechanism is the concerted motions, translation as well as rotation, of the compact triangular trimer. Either of the concerted translations, FCC-H$\leftrightarrow$HCP-T or FCC-T$\leftrightarrow$HCP-H, can result in a long-range diffusion by repeating the process. With the addition of the concerted rotational process, FCC-T$\leftrightarrow$HCP-T, the compact triangular trimer can diffuse to all the compact triangular trimer configurations over the whole surface. The second mechanism is the transformations between the compact triangular trimers and the linear trimers by individual atomic jumps. This transformation mechanism can also result in a long-range diffusion by repeating the process. The third mechanism is the intracell and intercell translation of linear trimers. Both the intercell and intracell diffusions of the Al linear trimer by concerted motions have higher energy barriers than the other two mechanisms mentioned above. The intracell diffusion of the linear trimer can also result from jumps of individual atoms with a lower barrier than the concerted one, but it can not achieve a long-range diffusion.

For the movement of the center of mass by a distance of $(\sqrt{6}/6)a_0$, the back-and-forth transformation between the triangular and linear trimers with an energy barrier of 0.21 eV needs four steps to accomplish the displacement, while the concerted translation of a compact triangular trimer needs only one step, with an energy barrier of 0.22 or 0.24 eV, to achieve the same displacement. Although the intercell translation of the linear trimer also displaces the center of mass by a distance of $(\sqrt{6}/6)a_0$ in one step, it needs a slightly higher diffusion energy barrier of 0.28 eV. Therefore, we expect the long-range diffusion of Al trimer on Al(111) surface to be dominated by the concerted motion of the compact triangular trimers, which has the longest displacement in the least steps with a relatively low energy barrier. These concerted motions, translations and rotations have also been observed in the EAM-MD simulations.

## Acknowledgements

We thank J. Hafner for providing us with the VASP code. C.M.C. and C.M.W. are supported by the National Science Council, Republic of China under the grants NSC 88-2112-M-001-025. S.P.C. is supported by the US Department of Energy.

## References

[1] A. Zangwill, Physics at Surfaces, Cambridge University Press, Cambridge, 1988.
[2] T.T. Tsong, in: Atom-probe Field Ion Microscopy, Cambridge University Press, Cambridge, 1990, pp. 202-265.
[3] M.C. Tringides (Ed.), Surface Diffusion: Atomistic and Collective Processes, Plenum Press, New York, 1997.
[4] G.L. Kellogg, Surf. Sci. Rep. 21 (1994) 1.
[5] S.C. Wang, G. Ehrlich, Surf. Sci. 239 (1990) 301.
[6] C.L. Chen, T.T. Tsong, Phys. Rev. B 41 (1990) 12403.
[7] M.S. Daw, M.I. Baskes, Phys. Rev. Lett. 50 (1983) 1285.
[8] M.S. Daw, M.I. Baskes, Phys. Rev. B 29 (1984) 6443.
[9] C.M. Chang, C.M. Wei, S.P. Chen, Phys. Rev. B 54 (1996) 17083.
[10] C.L. Liu, J.B. Adams, Surf. Sci. 268 (1992) 73.
[11] A. Bogicevic, P. Hyldgaard, G. Wahnström, B. Lundqvist, Phys. Rev. Lett. 81 (1998) 172.

[12] Z.J. Tian, U. Yxklinten, B.I. Lundqvist, K.W. Jacobsen, Surf. Sci. 258 (1991) 427.

[13] P. Hohenberg, W. Kohn, Phys. Rev. B 136 (1964) 864.

[14] W. Kohn, L.J. Sham, Phys. Rev. A 140 (1965) 1133.

[15] G. Kress, J. Hafner, Phys. Rev. B 47 (1993) 558.

[16] G. Kress, J. Hafner, Phys. Rev. B 49 (1994) 14251.

[17] G. Kress, J. Furthmüller, Comput. Mater. Sci. 6 (1996) 15.

[18] G. Kress, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.

[19] G. Kress, J. Hafner, J. Phys.: Condens. Mater. 6 (1994) 8245.

[20] S. Lundqvist, N.H. March (Eds.), The Theory of the Inhomogeneous Electron Gas, Plenum, New York, 1983.

[21] W.E. Pickett, Comput. Phys. Rep. 9 (1989) 115.

[22] D.M. Ceperley, B.J. Alder, Phys. Rev. Lett. 45 (1980) 566.

[23] J.P. Perdew, A. Zunger, Phys. Rev. B 23 (1981) 5048.

[24] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.

[25] A.F. Voter, S.P. Chen, Characterization of Defects in Materials, R.W. Siegel, R. Sinclair, J.R. Weertman (Eds.), MRS Symposia Proceedings Vol. 82, Materials Research Society, Pittsburgh, PA, 1987, p. 175.

[26] S.P. Chen, A.F. Voter, D.J. Srolvitz, J. Mater. Res. 5 (1990) 955.

[27] S.P. Chen, A.F. Voter, R.C. Albers, A.M. Boring, P.J. Hay, Phys. Rev. Lett. 57 (1986) 1308.

[28] W.C. Swope, H.C. Andersen, P.H. Berens, K.R. Wilson, J. Chem. Phys. 76 (1982) 637.