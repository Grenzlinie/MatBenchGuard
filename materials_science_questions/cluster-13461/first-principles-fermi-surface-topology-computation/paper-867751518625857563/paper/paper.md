
# Topological Phases in Oxide Heterostructures with Light and Heavy Transition Metal Ions

Gregory A. Fiete \( ^{1, a)} \)  and Andreas Rüegg \( ^{2} \) 

 \( ^{1)} \) Department of Physics, The University of Texas at Austin, Austin, Texas 78712, USA
 \( ^{2)} \)  Theoretische Physik, ETH Zürich, CH-8093 Zürich, Switzerland

(Dated: 28 June 2018)

Using a combination of density functional theory, tight-binding models, and Hartree-Fock theory, we predict topological phases with and without time-reversal symmetry breaking in oxide heterostructures. We consider both heterostructures containing light transition metal ions, and those containing heavy transition metal ions. We find the (111) growth direction naturally leads to favorable conditions for topological phases in both perovskite structures and pyrochlore structures. For the case of light transition metal elements, Hartree-Fock theory predicts the spin-orbit coupling is effectively enhanced by on-site multiple-orbital interactions and may drive the system through a topological phase transition, while heavy elements with intrinsically large spin-orbit coupling require much weaker, or even vanishing electron interactions to bring about a topological phase.

## I. INTRODUCTION

Topological insulators (TI) have now been studied for nearly a decade and there are a number of excellent reviews available, from both an experimental and theoretical perspective. \( ^{1-4} \)  Aside from the important example of  \( SmB_{6} \) , \( ^{5-8} \)  all other experimental examples of topological insulators are weakly correlated. The most important reason for the weak correlation effects is that the bands of topological insulators near the Fermi energy are derived from s and p-type orbitals, which are rather extended. By contrast, the bands about the Fermi energy in  \( SmB_{6} \)  are predominantly derived from f-orbitals, which are more localized, and therefore lead to flatter bands and enhanced interaction effects. \( ^{9} \) 

One of the persistent challenges in experimental studies of TI is the problem of high bulk conductivity. \( ^{4} \)  While some progress has been made on this front over the past few years, it has largely been incremental, and for the most part has been focused on bismuth-based TI. An alternative route is to look for new classes of strongly insulating materials that might support topological insulator phases. If one is also interested in studying interaction effects that could possibly take one beyond the “band theory” description of topological insulators, materials with orbitals more localized than the s and p-orbitals are highly desirable. Transition metal oxides, which typically have bands derived from d-orbitals close to the Fermi energy, are excellent candidates: There are a large number of insulating oxides, and interaction effects are known to be important in many of them—the high temperature cuprate superconductors serving as an excellent example. \( ^{10,11} \)  Indeed, there have been a number of theoretical proposals for strongly correlated topological insulators in transition metal oxide systems. \( ^{12-20} \)  A recent review of the prospects for such exotic phases in the context of three dimensional iridium (and other heavy transition metals) oxides is given in Ref.[21].

In this article, we focus on topological phases in thin film (two-dimensional) oxide heterostructures that can be described within the band theory picture. There are three prime candidates: (1) The time-reversal invariant topological insulator characterized by a single  \( Z_{2} \)  invariant, (2) The time-reversal symmetry broken Chern insulator characterized by a quantized Chern number and quantized Hall conductance, and (3) The mirror symmetry protected (with respect to the center of the plane of the thin film \( ^{22} \) ) topological crystalline insulator characterized by a mirror Chern number. \( ^{23-26} \)  Combinations of these are possible as well for a “doubly topological” system, though clearly (1) and (2) are mutually exclusive. The Chern insulator differs from the quantum Hall insulator in that the former has time-reversal symmetry spontaneously broken by interactions (that is, a spontaneous magnetization of some sort), while the latter has time-reversal symmetry broken by the application of an external magnetic field. As a result, a Chern insulator requires interactions (because there is no spontaneous magnetism without electron-electron interactions), while a (integer) quantum Hall system does not. A topological crystalline insulator may possess time-reversal symmetry or have it broken by magnetic order; the only restriction is that any magnetic order present must respect the mirror symmetry. \( ^{24} \) 

In the remainder of this article, we will consider two transition metal oxide structures, the perovskite with formula  \( ABO_{3} \)  and the pyrochlore oxide  \( A_{2}B_{2}O_{7} \) , where A is typically a rare-earth element, B is a transition metal element, and O is oxygen. Two specific examples we study are  \( LaNiO_{3} \)  and  \( Y_{2}Ir_{2}O_{7} \) , which are both materials that have been grown and are well characterized in bulk form. Our new angle is to study the properties of thin films of these materials that are grown along the (111) crystalline axis. We find the physical properties of these films are
 

rather different from the bulk. Moreover, there does not appear to be an obvious way to infer the film properties from the bulk. As a result, these systems appear to be excellent candidates for exploring novel phenomena, such as topological phases, even when the bulk (non-thin film) materials possess strikingly different properties, such as a conducting behavior. We are thus presented with the exciting possibility of finding “new physics” in “old materials”.

## II. THIN FILM OXIDE HETEROSTRUCTURES

![](./images/867751518625857563_1.jpg)

FIG. 1. (Color online.) (a) We consider oxide heterostructures grown along the (111) direction of the form  \( AB'O_{3}/ABO_{3}/AB'O_{3} \)  for the perovskite structure and  \( A_{2}B'_{2}O_{7}/A_{2}B_{2}O_{2}O_{4}/A_{2}B'_{2}O_{7} \)  for the pyrochlore structure. Both  \( AB'O_{3} \)  and  \( A_{2}B'_{2}O_{7} \)  are assumed to be non-magnetic, wide band gap (band) insulators. The shaded region consists of a (111) bilayer of the metallic  \( ABO_{3} \)  perovskite, such as  \( LaNiO_{3} \) , or in the case of pyrochlore structures, a bilayer or a trilayer of a material such as  \( Y_{2}Ir_{2}O_{7} \) . (b) Shown are the locations of the transition-metal ions (B) for the  \( ABO_{3} \)  structure. (c) The  \( ABO_{2} \)  bilayer system forms a “buckled honeycomb” lattice, which appears as a honeycomb lattice when projected to the plane perpendicular to (111). We assume that the relevant orbital degrees of freedom are the  \( e_{g} \)  orbitals of the transition-metal ions for  \( ABO_{3} \) . For  \( A_{2}B_{2}O_{7} \)  with heavy transition metal ions, the relevant orbitals come from the spin-orbit split  \( t_{2g} \)  manifold in the class of materials we study in this paper.

We are interested in a heterostructure similar to that shown in Fig.1, where the film is grown along the (111) direction. Most experimental studies of thin films in the perovskite systems  \( ABO_{3} \)  are grown along the (001) (or symmetry related) direction because aligning the growth direction along a cubic axis generally favors high quality films. On the other hand, growing along (111) effectively changes the crystal structure in a single layer thin film from a square lattice of transition metal ions for (001) to a triangular lattice of transition metal ions in (111), as shown in Fig.1. For a bilayer grown along (001), one will have two square lattices of transition metal ions stacked directly on top of each other, but for growth along (111) a second "shifted" triangular lattice will sit on top of the original one. The combination of the two shifted triangular lattices is a "buckled" honeycomb lattice. In this example, growing along the (111) direction allows one to effectively "engineer" the lattice of the thin film, with important implications for the band structure in the weak coupling limit and the magnetic order in the strong coupling limit.

Likewise, the (111) growth direction for the  \( A_{2}B_{2}O_{7} \)  pyrochlores leads to alternating planes of triangular and kagome lattices for the transition metal ions. [See Fig.5(a).] To the best of our knowledge, there have been no published experimental results on bilayer or trilayer films of  \( A_{2}B_{2}O_{7} \)  grown along (111), though there are a number of systems where (111) growth of  \( ABO_{3} \)  films has been demonstrated, \( ^{[27-29]} \)  and also of  \( AB_{2}O_{4} \)  spinels. \( ^{[30]} \)  Various theoretical proposals now exist for topological phases in (111) grown transition metal oxide films, \( ^{[31-44]} \)  and the list of candidate materials continues to grow. We believe it is likely that experiment will indeed find evidence of topological phases in this class of systems. Once a single example is found, experiments can be done to optimize material choices by “perturbing” around this material with different isovalent elements, substrates, etc, in order to achieve the maximum bulk gap. Our calculations suggest that the Chern insulator phase stands out as the mostly likely topological candidate for realistic conditions in thin film oxide heterostructures.

To be concrete, we will focus on the  \( LaNiO_{3} \)  perovskite \( ^{31-34} \)  and the  \( Y_{2}Ir_{2}O_{7} \)  pyrchlore iridate. \( ^{35,37} \)  (We note that an interesting theoretical study of Co-doped  \( LaNiO_{3} \)  (111) grown bilayers suggests that correlation-driven odd parity superconductivity may appear in this system. \( ^{45} \) ) First principles calculations show that the bands around the Fermi energy are predominantly of d-orbital character in both  \( LaNiO_{3} \)  and  \( Y_{2}Ir_{2}O_{7} \) . \( ^{33,34,46} \)  As a result, the spatial shape of the orbitals are highly asymmetric and can lead to interesting band features on the triangular, kagome, and honeycomb lattices that appear in the thin film structures of interest to us. In particular, a simple tight-binding model for the Ni d-orbitals leads to flat bands that touch dispersing bands quadratically \( ^{31} \)  (the flat touching feature persists with more realistic first principles band calculations \( ^{33,34} \) ), and also bands that cross in a Dirac point (see Fig.2). The stability of such band touching and crossing points with respect to interactions has been discussed recently in the literature in the context of interaction-generated topological phases. \( ^{31,32,47-51} \) 

The central idea is that certain types of interactions, such as an on-site multi-orbital \( ^{31,32} \)  interaction or different site density-density interaction in a single band \( ^{47-50} \)  model, can generate an effective spin-orbit term (at the Hartree-Fock level) that favors topological phases. This is one of the ideas we will explore in the remainder of this article in the context of real materials, though we will find that for heavier transition elements, such as iridium, “interaction generated spin-orbit coupling terms” are not needed to access topological phases. Thus, any doubts about the reliability of the Hatree-Fock predictions for enhanced spin-orbit effects can be circumvented by focusing on classes of materials with intrinsically large spin-orbit coupling.
 

## A. LaNiO_{3} bilayers

![](./images/867751518625857563_2.jpg)

![](./images/867751518625857563_3.jpg)

FIG. 2. First principles band structure of the fully lattice relaxed  \( (\mathrm{LaAlO}_{3})_{10}/(\mathrm{LaNiO}_{3})_{2}/(\mathrm{ LaAlO}_{3})_{10} \)  system within (a) LDA and (b) GGA, which are essentially indistinguishable. Note the quadratic band touching at the  \( \Gamma \)  point as well as the linear crossings at K and  \( K' \) . \( ^{34} \)  For a spin unpolarized system the Fermi energy lies right at the quadratic band touching point, while for a fully polarized (ferromagnetic) system the Fermi energy lies right at the Dirac point. Our Hartree-Fock calculations suggest that for realistic interaction values, the system is very close to a fully spin-polarized state with a quantized Chern number—a quantum anomalous Hall state. \( ^{33,34} \)  See Fig.4(b).

The band structure obtained with the local density approximation (LDA) and the generalized gradient approximation (GGA) \( ^{34} \)  for the fully relaxed  \( LaNiO_{3} \)  (111) bilayer is shown in Fig. 2. The two are nearly indistinguishable. Rotations of the octahedral oxygen cages are known to be important for large classes of transition metal oxides, \( ^{52} \)  including  \( LaNiO_{3} \)  for which the adjacent oxygen cages counter-rotate about the (111) axis, as shown in Fig.3(a). To perform Hartree-Fock calculations with this band structure, we consider a tight-binding model based only on the nickel  \( e_{g} \)  orbitals that includes nearest-neighbor hopping via the oxygen p-orbitals and second-neighbor hopping via the oxygens p-orbitals. We find a good fit by including the small differences in the hopping to “outer” versus “inner” oxygen atoms. \( ^{33} \)  Assuming trigonal symmetry is preserved (a result consistent with our fully relaxed DFT results), we take the nearest-neighbor Slater-Koster parameters for hopping along the z-direction to be described by the matrix

 \[ \hat{t}_{z}=-\begin{pmatrix}{{{t}}}&{{{0}}} \\{{{0}}}&{{{t_{\delta}}}}\end{pmatrix} \quad (1) \] 

in the basis  \( (d_{z^{2}}, d_{x^{2}-y^{2}}) \) . Here t includes predominantly the hopping via the intermediate oxygen while  \( t_{\delta} \)  arises from the direct overlap and is small. We set  \( t_{\delta} = 0 \)  in the following. Assuming that the nearest-neighbor hopping in the x and y directions are equivalent to the hopping along the z direction, we obtain the corresponding matrices by a rotation of the  \( e_{g} \) -orbitals around (111) by  \( \pm 2\pi/3 \) . The matrix for the rotation

![](./images/867751518625857563_4.jpg)

(a)  \( \phi \)  about (111) (b) Title angle  \( \phi \) , with layer index

FIG. 3. (Color online.) (a) The pattern of the octahedral tilts/counter rotations present in the fully relaxed structure. (b) Layer resolved octahedral rotation angles for the  \( (\mathrm{LaNiO}_{3})_{2}/(\mathrm{LaAlO}_{3})_{10} \)  supercell obtained within the LDA approximation to DFT. As Fig. 2 shows, these rotations do not lift the quadratic band touching at the  \( \Gamma \)  point or the Dirac points at K,  \( K' \)  in the Brillouin zone because they preserve the trigonal point group symmetry. \( ^{34} \)  This, in turn, implies the predictions for interaction-driven topological phases in the  \( (\mathrm{LaNiO}_{3})_{2}/(\mathrm{LaAlO}_{3})_{N} \)  system remain qualitatively unchanged compared to the “ideal” lattice structure. \( ^{33} \) 

by  \( 2\pi/3 \)  is  \( \hat{R} = \begin{pmatrix} -1/2 & \sqrt{3}/2 \\ -\sqrt{3}/2 & -1/2 \end{pmatrix} \) . As a result, we find  \( \hat{t}_{x} = \hat{R}^{T} \hat{t}_{z} \hat{R} \) ,  \( \hat{t}_{y} = \hat{R}^{T} \hat{t}_{x} \hat{R} \) . The Slater-Koster parameters for second-neighbor hopping define the matrix \( ^{33} \) 

 \[ \hat{t}_{x y}=-\begin{pmatrix}{{{t^{\prime}/2}}}&{{{\sqrt{3}\Delta/2}}} \\{{{-\sqrt{3}\Delta/{2}}}}&{{{-3t^{\prime}/2}}}\end{pmatrix}. \quad (2) \] 

The off-diagonal entries proportional to  \( \Delta \)  are allowed in the bilayer system discussed here (as opposed to a perfect cubic system) because the two possible paths connecting second-neighbor transition-metal ions are not equivalent: they either involve “inner” or “outer” oxygens. \( ^{33} \)  Note that  \( \hat{t}_{xy} \)  is not symmetric if  \( \Delta \neq 0 \)  which means that there is an associated direction for the hopping. We use the convention that  \( \hat{t}_{xy} \)  denotes the hopping of an electron along a second neighbor bond which is reached by first following the y-axis and then the x-axis of the cube. By rotating the orbitals, we also obtain the second-neighbor hopping along the other directions:  \( \hat{t}_{yz} = \hat{R}^{T} \hat{t}_{xy} \hat{R} \) ,  \( \hat{t}_{zx} = \hat{R}^{T} \hat{t}_{yz} \hat{R} \) .

The generalized tight-binding model now takes the form

 \[ \begin{aligned}H_{0}&=\sum_{\boldsymbol{r}\in A}\sum_{s}\sum_{u=x y z}\left(\vec{d}_{s,\boldsymbol{r}}^{n}\hat{t}_{u}\vec{d}_{s,\mathbf{r}+\boldsymbol{e}_{u}}+\mathrm{h.c.}\right)\\&\quad+\sum_{\boldsymbol{r}\in A}\sum_{s}\sum_{u=x y z}\left(\vec{d}_{s,\boldsymbol{r}}^{n}\hat{t}_{u,u+1}\vec{d}_{s,\mathbf{r}+\boldsymbol{e}_{u}-\boldsymbol{e}_{u+1}}+\mathrm{h.c.}\right)\\\&\quad+\sum_{\boldsymbol{r}\in B}\sum_{s}\sum_{u=x y z}\left(\vec{d}_{s,\boldsymbol{r}}^{n}\hat{t}_{u,u+1}\vec{d}_{s,\mathbf{r}-\boldsymbol{e}_{u}+\boldsymbol{e}_{u+1}}+\mathrm{h.c.}\right),\end{aligned} \quad (3) \] 

where  \( \vec{d}_{s}=(d_{z^{2},s},d_{x^{2}-y^{2},s})^{T} \)  is a vector in orbital space,  \( s=\uparrow,\downarrow \)  is the spin and the notation  \( u+1 \)  refers to y if
 

<table><tr><td>fit</td><td>t [eV]</td><td>t&#x27; [eV]</td><td>\( \Delta \)  [eV]</td><td>E_{F} [eV]</td></tr><tr><td>unrelaxed (LDA)</td><td>0.598</td><td>0.062</td><td>-0.023</td><td>-0.693</td></tr><tr><td>fully relaxed (LDA)</td><td>0.541</td><td>0.045</td><td>-0.017</td><td>-0.641</td></tr><tr><td>fully relaxed (GGA)</td><td>0.508</td><td>0.046</td><td>-0.016</td><td>-0.593</td></tr></table>

TABLE I. Parameters obtained in tight-binding fits to the  \( e_{g} \)  DFT band structure of the unrelaxed and fully relaxed superlattice. There are very little changes between the unrelaxed and relaxed parameters, with  \( t^{\prime}/t \)  nearly invariant implying negligible change in the phase diagram shown in Fig.4.

u = x with a cyclic extension to the other elements.

Using the tight-binding model  \( H_{0} \)  with parameters t,  \( t' \) , and  \( \Delta \)  (with  \( t_{\delta} = 0 \) ), we fitted both the LDA and GGA band structures of the fully relaxed system near the Fermi level. The fitting parameters are listed in Table I and Fig. 4(a) shows the LDA together with the tight-binding band structure for the best fit. To study the multi-orbital interactions within Hartree-Fock theory, we use an on-site interaction of the form \( ^{10,53} \) 

 \[ \begin{aligned}H_{\mathrm{int}}=&\sum_{\boldsymbol{r}}\Big[U\sum_{\alpha}n_{\boldsymbol{r}\alpha\uparrow}n_{\boldsymbol{r}\boldsymbol{\alpha}\downarrow}+(U^{\prime}-J)\sum_{\alpha>\beta,s}n_{\boldsymbol{r}\alpha s}n_{\boldsymbol{r}\beta s}\\&+U^{\prime}\sum_{\alpha\neq\beta}n_{\boldsymbol{r}\alpha\uparrow}n_{\boldsymbol{r}\beta\downarrow}+J\sum_{\alpha\neq\beta}d_{\boldsymbol{r}\alpha\uparrow}^{\dagger}d_{\boldsymbol{r}\beta\uparrow}d_{\boldsymbol{r}\downarrow}^{\dagger}d_{\boldsymbol{r}\alpha\downarrow}\\&+I\sum_{\alpha\neq\beta}d_{\boldsymbol{r}\alpha\uparrow}^{\dagger}d_{\boldsymbol{r}\beta\uparrow}d_{\boldsymbol{r}\alpha\downarrow}^{\dagger}d_{\boldsymbol{r}\beta\downarrow}\Big].\end{aligned} \quad (4) \] 

We assume  \( U' = U - 2J \)  and I = J, which are valid in free space and believed to be approximately true in the solid state environment. The total multi-orbital Hubbard Hamiltonian for the  \( e_{g} \)  electrons is given by  \( H = H_{0} + H_{int} \) , where  \( H_{0} \)  is given in Eq. (3). The results \( ^{33,34} \)  are shown in Fig.4(b). Studying a model that explicitly includes oxygen p-orbitals (where charge-transfer physics may appear) leads to similar results. \( ^{33} \) 

## B.  \( Y_{2}Ir_{2}O_{7} \)  bilayers and trilayers

In order to study the (111) films of the pyrochlore in a set-up similar to that shown in Fig. 1(a), we consider a tight-binding model

 \[ H_{0}=\sum_{\langle i,j\rangle,\alpha,\beta}t_{i\alpha,j\beta}c_{i\alpha}^{\dagger}c_{j\beta}-\lambda\sum_{i}\mathbf{l}_{i}\cdot\mathbf{s}_{i}, \quad (5) \] 

where the d-orbital hopping takes the form \( ^{19,54} \) 

 \[ t_{i\alpha,j\beta}=t_{i\alpha,j\beta}^{in}+t_{i\alpha,j,\beta}^{dir}, \quad (6) \] 

which contains both an indirect and a direct hopping term between the d-orbitals. \( ^{12,13,55} \)  Here,  \( \lambda > 0 \)  is the intrinsic spin-orbit coupling in the system which acts within the  \( t_{2g} \)  manifold so  \( |I| = 1 \) , and  \( s_{i} \)  is the spin of the electron in a  \( t_{2g} \)  d-orbital on site i. \( ^{12,13,55} \)  In the 5d oxides, the strength of the spin-orbit coupling is estimated

![](./images/867751518625857563_5.jpg)

(a) LDA Tight Binding Fit

![](./images/867751518625857563_6.jpg)

(b) Hartree-Fock Phase Diagram

FIG. 4. (color online) (a) Fully relaxed LDA band structure and tight-binding (TB) fit. (b) Hartree-Fock phase diagram of the  \( LaNiO_{3} \)  bilayer. We estimate the experimental system has parameters  \( t^{\prime}/t \approx 0.1 \)  and  \( J/U \approx 0.0-1.0-2.0 \) , which is rather close to the quantum anomalous Hall (QAH) phase with ferromagnetic order. FO=ferro-orbital, AFM=antiferromagnetic, AFO=antiferro-orbital, FM=ferromagnetic, CDW=charge density wave.

![](./images/867751518625857563_7.jpg)

(a) Pyrochlore structure

![](./images/867751518625857563_8.jpg)

(b) Bilayer structure

FIG. 5. (Color online.) (a) Bulk pyrochlore lattice structure showing the alternation of kagome planes (green balls on lattice sites) and triangular lattice planes (grey balls on lattice sites) along the (111) direction. (b) A bilayer film viewed from the (111) direction.We focus on the bilayer and the triangular-kagome-triangular structure, which show the most promise for topological phases.

to be 0.2-0.7 eV and the hopping strength is on the order of 0.4-0.6 eV. \( ^{13,20} \)  The hopping amplitude in Eq. (6) contains a direct d-d hopping,  \( t_{i\alpha,j\beta}^{dir} \) , in addition to the indirect hopping via the oxygen orbitals. \( ^{19,54} \)  The direct hopping is parameterized by the strength of the  \( \sigma \) -bonds,  \( t_{s} \) , and the  \( \pi \) -bonds,  \( t_{p} \) . Following Refs. [19] and [54], we consider a set of representative ratios to explore a realistic parameter space: We set  \( t_{p} = -2t_{s}/3 \)  and consider the cases of  \( t_{s} = -t \)  and  \( t_{s}=t \) . Our preliminary GGA calculations for the thin-films suggest the band structure is most similar to that for  \( t_{s} = -t \) , though the further neighbor hopping is considerably more important for the 5d orbitals in  \( Y_{2}Ir_{2}O_{7} \)  than it is for the 3d orbitals in  \( LaNiO_{3} \) .

To carry out Hartree-Fock calculations for the  \( Y_{2}Ir_{2}O_{7} \)  films, we use the tight-binding model in Eq.(5) with  \( t_{s} = -t \)  supplemented by an on-site Hubbard term,  \( H_{U} = U \sum_{i} n_{i\uparrow} n_{i\downarrow} \) , and further restrict ourselves to the
 

 \( j = 1/2 \)  manifold. \( ^{35} \)  The results are shown in Fig. 6. Note the triangular-kagome-triangular (TKT) film supports a fairly wide region of a quantum anomalous Hall (Chern insulator=CI) state. We find that if one includes fluctuations beyond the Hartree-Fock approximation, this region moves to larger U values, close to what is reasonable for  \( Y_{2}Ir_{2}O_{7} \) . Therefore, we conclude that both the (111) grown  \( LaNiO_{3} \)  bilayer and the (111) grown  \( Y_{2}Ir_{2}O_{7} \)  TKT trilayer are candidates for a quantum anomalous Hall state. Moreover, we find that small changes to the kinetic terms in Eq.(3) can lead to a  \( Z_{2} \)  topological insulator in the (111) grown  \( Y_{2}Ir_{2}O_{7} \)  bilayer for small  \( U. \) ^{35}

![](./images/867751518625857563_9.jpg)

FIG. 6. (Color online.) Hartree-Fock phase diagrams for the single kagome layer (monolayer), bilayer, triangular-kagome-triangular (TKT), and kagome-triangular-kagome (KTK) systems. We have used  \( t_{s} = -t \)  and restricted ourselves to the j = 1/2 manifold. M=metallic, I=trivial insulator, TI=topological insulator, MC=magnetic conductor, MI=magnetic insulator, CI=Chern insulator (same as QAH).

## III. CONCLUSIONS

In conclusion, we have shown both the (111) grown  \( LaNiO_{3} \)  bilayer and the (111) grown  \( Y_{2}Ir_{2}O_{7} \)  TKT trilayer are candidates for a quantum anomalous Hall state, which will show a quantize Hall conductance. We also found that realistic changes to the kinetic terms of  \( Y_{2}Ir_{2}O_{7} \)  can also lead to a  \( Z_{2} \)  topological insulator in the (111) grown  \( Y_{2}Ir_{2}O_{7} \)  bilayer. The most natural way to detect these states is through transport measurements, as has been done for the few known  \( Z_{2} \)  TI \( ^{56,57} \)  and QAH systems. \( ^{58} \)  From the point-of-view of technology applications, there is clearly a need in the field for more systems known to possess these phases. The huge variety of transition metal oxides, combined with existing theoretical results, would seem to suggest it may only be a matter of time before a topological phase is discovered in a system similar to those we considered here.

## ACKNOWLEDGMENTS

We are grateful to our collaborators in this area, A.A. Demkov, X. Hu, P. J. Daudan, M. Kargarian, C. Mitra, and Z. Zhong. Our work was generously funded by ARO Grant No. W911NF-09-10527, NSF Grant No. DMR-0955778, and DARPA grant No. D13AP00052. The Texas Advanced Computing Center (TACC) at The University of Texas at Austin for provided the necessary computing resources. URL:http://www.tacc.utexas.edu.

 \( ^{1} \) J. E. Moore, “The birth of topological insulators,” Nature 464, 194–198 (2010).

 \( ^{2} \) M. Z. Hasan and C. L. Kane, “Colloquium: Topological insulators,” Rev. Mod. Phys. 82, 3045–3067 (2010).

 \( ^{3} \) X. L. Qi and S. C. Zhang, “Topological insulators and superconductors,” Rev. Mod. Phys. 83, 1057–1110 (2011).

 \( ^{4} \) Y. Ando, “Topological insulator materials,” J. Phys. Soc. Jpn. 82, 102001 (2013).

 \( ^{5} \) M. Dzero and V. Galitski, “A new exotic state in an old material: a tale of  \( SmB_{6} \) ,” JETP 117, 499–507 (Sep. 2013), ISSN 1063-7761, 1090-6509, http://link.springer.com/article/10.1134/S1063776113110083.

 \( ^{6} \) Maxim Dzero, Kai Sun, Victor Galitski, and Piers Coleman, “Topological kondo insulators,” Phys. Rev. Lett. 104, 106408 (Mar 2010), http://link.aps.org/doi/10.1103/PhysRevLett.104.106408.

 \( ^{7} \) M. Neupane, N. Alidoust, S-Y. Xu, T. Kondo, Y. Ishida, D. J. Kim, Chang Liu, I. Belopolski, Y. J. Jo, T-R. Chang, H-T. Jeng, T. Durakiewicz, L. Balicas, H. Lin, A. Bansil, S. Shin, Z. Fisk, and M. Z. Hasan, “Surface electronic structure of the topological kondo-insulator candidate correlated electron system smb6,” Nat. Comm. 4, 2991 (2013).

 \( ^{8} \) Xiaohang Zhang, N. P. Butch, P. Syers, S. Ziemak, Richard L. Greene, and Johnpierre Paglione, “Hybridization, inter-ion correlation, and surface states in the kondo insulator smb6,” Phys. Rev. X 3, 011011 (Feb 2013), http://link.aps.org/doi/10.1103/PhysRevX.3.011011.

 \( ^{9} \) Feng Lu, JianZhou Zhao, Hongming Weng, Zhong Fang, and Xi Dai, “Correlated topological insulators with mixed valence,” Phys. Rev. Lett. 110, 096401 (2013), http://link.aps.org/doi/10.1103/PhysRevLett.110.096401.

 \( ^{10} \) M. Imada, A. Fujimori, and Y. Tokura, “Metal-insulator transitions,” Rev. Mod. Phys. 70, 1039–1263 (1998).

 \( ^{11} \) P. A. Lee, N. Nagaosa, and X. G. Wen, “Doping a Mott insulator: Physics of high-temperature superconductivity,” Rev. Mod. Phys. 78, 17–85 (Jan 2006).

 \( ^{12} \) D. Pesin and L. Balents, “Mott physics and band topology in materials with strong spin-orbit coupling,” Nature Phys. 6, 376 (2010).

 \( ^{13} \) M. Kargarian, J. Wen, and G. A. Fiete, “Competing exotic topological insulator phases in transition-metal oxides on the pyrochlore lattice with distortion,” Phys. Rev. B 83, 165112 (2011).

 \( ^{14} \) M. Kargarian and G. A. Fiete, “Topological crystalline insulators in transition metal oxides,” Phys. Rev. Lett. 110, 156403 (2013).

 \( ^{15} \) W. Witczak-Krempa, T. P. Choy, and Y. B. Kim, “Gauge field fluctuations in three-dimensional topological Mott insulators,” Phys. Rev. B 82, 165122 (2010).

 \( ^{16} \) J. Maciejko and A. Rüegg, “Topological order in a correlated Chern insulator,” Phys. Rev. B 88, 241101 (Dec 2013), http://link.aps.org/doi/10.1103/PhysRevB.88.241101.

 \( ^{17} \) A. Rüegg and G. A. Fiete, “Topological order and semions in a strongly correlated quantum spin Hall insulator,” Phys. Rev. Lett. 108, 046401 (Jan 2012), http://link.aps.org/doi/10.1103/PhysRevLett.108.046401.

 \( ^{18} \) J. Maciejko, V. Chua, and G. A. Fiete, “Topological order in a correlated three-dimensional topological insulator,” Phys. Rev. Lett. 112, 016404 (Jan 2014), http://link.aps.org/doi/10.1103/PhysRevLett.112.016404.

 \( ^{19} \) Ara Go, William Witczak-Krempa, Gun Sang Jeon, Kwon Park, and Yong Baek Kim, “Correlation effects on 3d topological phases: From bulk to boundary,” Phys. Rev. Lett. 109, 066401 (2012).

 \( ^{20} \) Atsuo Shitade, Hosho Katsura, Jan Kuneš, Xiao-Liang Qi, Shou-Cheng Zhang, and Naoto Nagaosa, “Quantum spin hall effect in
 

a transition metal oxide na[sub 2]iro[sub 3],” Phys. Rev. Lett. 102, 256403 (2009).

 \( ^{21} \) W. Witczak-Krempa, G. Chen, Y. B. Kim, and L. Balents, “Correlated quantum phenomena in the strong spin-orbit regime,” Annu. Rev. Condens. Matter Phys. 5, 57–82 (2014), http://www.annualreviews.org/doi/abs/10.1146/annurev-conmatphys-020911-125138.

 \( ^{22} \) Junwei Liu, Timothy H. Hsieh, Peng Wei, Wenhui Duan, Jagadeesh Moodera, and Liang Fu, “Spin-filtered edge states with an electrically tunable gap in a two-dimensional topological crystalline insulator,” Nat. Mat. 13, 178183 (2014).

 \( ^{23} \) Jeffrey C. Y. Teo, Liang Fu, and C. L. Kane, “Surface states and topological invariants in three-dimensional topological insulators: Application to bi[subl 1 - x]sb[subl x],” Phys. Rev. B 78, 045426 (2008).

 \( ^{24} \) Timothy H. Hsieh, Hsin Lin, Junwei Liu, Wenhui Duan, Arun Bansil, and Liang Fu, “Topological crystalline insulators in the snte material class,” Nat. Commun. 3, 982 (2012).

 \( ^{25} \) Junwei Liu, Wenhui Duan, and Liang Fu, “Two types of surface states in topological crystalline insulators,” Phys. Rev. B 88, 241303 (Dec 2013), http://link.aps.org/doi/10.1103/PhysRevB.88.241303.

 \( ^{26} \) Timothy H. Hsieh, Junwei Liu, and Liang Fu, “Topological crystalline insulators and dirac octets in antiperovskites,” Phys. Rev. B 90, 081112 (Aug 2014), http://link.aps.org/doi/10.1103/PhysRevB.90.081112.

 \( ^{27} \) S. Middey, D. Meyers, M. Kareev, E. J. Moon, B. A. Gray, X. Liu, J. W. Freeland, and J. Chakhalian, “Epitaxial growth of (111)-oriented laalo \( _{3} \) /laniao \( _{3} \)  ultra-thin superlattices,” Appl. Phys. Lett. 101, 261602 (2012).

 \( ^{28} \) J. L. Blok, X. Wan, G. Koster, D. H. A. Blank, and G. Rijnders, “Epitaxial oxide growth on polar (111) surfaces,” Appl. Phys. Lett. 99, 151917 (2011).

 \( ^{29} \) S. Middey, D. Meyers, D. Doennig, M. Kareev, X. Liu, Y. Cao, P. J. Ryan, R. Pentcheva, J. W. Freeland, and J. Chakhalian, “Geometrically engineered mott phases in (111) oriented nickelate superlattices,” (2014), arXiv:1407.1570.

 \( ^{30} \) Xiaoran Liu, M. Kareev, Yanwei Cao, Jian Liu, S. Middey, D. Meyers, J. W. Freeland, and J. Chakhalian, “Electronic and magnetic properties of  \( (1\ 1\ 1) \) -oriented  \( cocr2o4 \)  epitaxial thin film,” (2014), arXiv:1406.0523.

 \( ^{31} \) A. Rüegg and G. A. Fiete, “Topological insulators from complex orbital order in transition-metal oxides heterostructures,” Phys. Rev. B 84, 201103 (2011).

 \( ^{32} \) K.-Y. Yang, W. Zhu, D. Xiao, S. Okamoto, Z. Wang, and Y. Ran, "Possible interaction-driven topological phases in (111) bilayers of  \( LaNiO_{3} \) ," Phys. Rev. B 84, 201104 (2011).

 \( ^{33} \) Andreas Rüegg, Chandrima Mitra, Alexander A. Demkov, and Gregory A. Fiete, “Electronic structure of  \( (\mathrm{laniao}_{3})_{2}/(\mathrm{laalo}_{3})_{N} \)  heterostructures grown along  \( [111] \) ,” Phys. Rev. B 85, 245131 (2012).

 \( ^{34} \) Andreas Rüegg, Chandrima Mitra, Alexander A. Demkov, and Gregory A. Fiete, “Lattice distortion effects on topological phases in  \( (\mathrm{laniao}_{3})_{2}/(\mathrm{laalo}_{3})_{N} \)  heterostructures grown along the  \( [111] \)  direction,” Phys. Rev. B 88, 115146 (Sep 2013), http://link.aps.org/doi/10.1103/PhysRevB.88.115146.

 \( ^{35} \) Xiang Hu, Andreas Rüegg, and Gregory A. Fiete, “Topological phases in layered pyrochlore oxide thin films along the [111] direction,” Phys. Rev. B 86, 235141 (2012).

 \( ^{36} \) Satoshi Okamoto, Wenguang Zhu, Yusuke Nomura, Ryotaro Arita, Di Xiao, and Naoto Nagaosa, “Correlation effects in (111) bilayers of perovskite transition-metal oxides,” Phys. Rev. B 89, 195121 (May 2014), http://link.aps.org/doi/10.1103/PhysRevB.89.195121.

 \( ^{37} \) Bohm-Jung Yang and Naoto Nagaosa, “Emergent topological phenomena in thin films of pyrochlore iridates,” Phys. Rev. Lett. 112, 246402 (Jun 2014), http://link.aps.org/doi/10.1103/PhysRevLett.112.246402.

 \( ^{38} \) Satoshi Okamoto, “Doped mott insulators in (111) bilayers of perovskite transition-metal oxides with a strong spin-orbit cou-

pling," Phys. Rev. Lett. 110, 066403 (Feb 2013).

 \( ^{39} \) Di Xiao, Wenguang Zhu, Ying Ran, Naoto Nagaosa, and Satoshi Okamoto, “Interface engineering of quantum hall effects in digital heterostructures of transition-metal oxides,” Nat. Comm. 2, 596 (2011).

 \( ^{40} \) David Doennig, Warren E. Pickett, and Rossitza Pentcheva, “Confinement-driven transitions between topological and mott phases in  \( (\mathrm{LaNiO}_{3})_{N}/(\mathrm{LaAl}^{\prime\prime}mathrm{rm}O_{3})_{M} \)  (111) superlattices,” Phys. Rev. B 89, 121110 (Mar 2014), http://link.aps.org/doi/10.1103/PhysRevB.89.121110.

 \( ^{41} \) J. L. Lado, V. Pardo, and D. Baldomir, “Ab initio study of z2 topological phases in perovskite (111) (srtio3)/(sriro3)2 and (ktao3)7/(kpto3)2 multilayers,” Phys. Rev. B 88, 155119 (Oct 2013), http://link.aps.org/doi/10.1103/PhysRevB.88.155119.

 \( ^{42} \) Qi-Feng Liang, Long-Hua Wu, and Xiao Hu, “Electrically tunable topological state in [111] perovskite materials with an antiferromagnetic exchange field,” New Journal of Physics 15, 063031 (2013).

 \( ^{43} \) Fa Wang and Ying Ran, “Nearly flat band with chern number c = 2 on the dice lattice,” Phys. Rev. B 84, 241103 (2011).

 \( ^{44} \) Yilin Wang, Zhijun Wang, Zhong Fang, and Xi Dai, “Interaction-induced quantum anomalous hall phase in (111) bilayer of  \( laco_{3} \) ,” (2014), arXiv:1409.6797.

 \( ^{45} \) Bing Ye, Andrej Mesaros, and Ying Ran, “Possible correlation-driven odd-parity superconductivity in  \( lan_{7/8}co_{1/8}o_{3} \)  (111) bilayers,” Phys. Rev. B 89, 201111 (May 2014), http://link.aps.org/doi/10.1103/PhysRevB.89.201111.

 \( ^{46} \) Xiangang Wan, Ari M. Turner, Ashvin Vishwanath, and Sergey Y. Savrasov, “Topological semimetal and fermi-arc surface states in the electronic structure of pyrochlore iridates,” Phys. Rev. B 83, 205101 (2011).

 \( ^{47} \) S. Raghu, X.-L. Qi, C. Honerkamp, and S.-C. Zhang, “Topological Mott insulators,” Phys. Rev. Lett. 100, 156401 (2008).

 \( ^{48} \) Y. Zhang, Y. Ran, and A. Vishwanath, “Topological insulators in three dimensions from spontaneous symmetry breaking,” Phys. Rev. B 79, 245331 (2009).

 \( ^{49} \) K. Sun, H. Yao, E. Fradkin, and S. A. Kivelson, “Topological insulators and nematic phases from spontaneous symmetry breaking in 2D Fermi systems with a quadratic band crossing,” Phys. Rev. Lett. 103, 046811 (2009).

 \( ^{50} \) J. Wen, A. Rüegg, C.-C. J. Wang, and G. A. Fiete, “Interaction-driven topological insulators on the kagome and the decorated honeycomb lattices,” Phys. Rev. B 82, 075125 (2010).

 \( ^{51} \) R. Yu, W. Zhang, H.-J. Zhang, S.-C. Zhang, X. Dai, and Z. Fang, "Quantized anomalous Hall effect in magnetic topological insulators," Science 329, 61-64 (2010).

 \( ^{52} \) S. Maekawa, T. Tohyama, S. E. Barnes, S. Ishihara, W. Koshibae, and G. Khaliullin, Physics of Transition Metal Oxides (Springer, Berlin, 2004).

 \( ^{53} \) T. Mizokawa and A. Fujimori, “Electronic structure and orbital ordering in perovskite-type 3 d transition-metal oxides studied by hartree-fock band-structure calculations,” Phys. Rev. B 54, 5368–5380 (Aug 1996).

 \( ^{54} \) William Witczak-Krempa and Yong Baek Kim, “Topological and magnetic phases of interacting electrons in the pyrochlore iridates,” Phys. Rev. B 85, 045124 (2012).

 \( ^{55} \) Bohm-Jung Yang and Yong Baek Kim, “Topological insulators and metal-insulator transition in the pyrochlore iridates,” Phys. Rev. B 82, 085111 (2010).

 \( ^{56} \) M. König, S. Wiedmann, C. Brune, A. Roth, H. Buhmann, L. Molenkamp, X.-L. Qi, and S.-C. Zhang, “Quantum spin hall insulator state in hgte quantum wells,” Science 318, 766 (2007).

 \( ^{57} \) Andreas Roth, Christoph Brüne, Hartmut Buhmann, Laurens W. Molenkamp, Joseph Maciejko, Xiao-Liang Qi, and Shou-Cheng Zhang, “Nonlocal transport in the quantum spin hall state,” Science 325, 294 (2009).

 \( ^{58} \) Cui-Zu Chang, Jinsong Zhang, Xiao Feng, Jie Shen, Zuocheng Zhang, Minghua Guo, Kang Li, Yunbo Ou, Pang Wei, Li-Li Wang, Zhong-Qing Ji, Yang Feng, Shuaihua, Xi Chen, Jinfeng
 

Jia, Xi Dai, Zhong Fang, Shou-Cheng Zhang, Ke He, Yayu Wang, Li Lu, Xu-Cun Ma, and Qi-Kun Xue, “Experimental observation

of the quantum anomalous hall effect in a magnetic topological insulator," Science 167, 167 (2013).
 
