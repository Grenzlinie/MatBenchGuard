Theoretical and experimental investigation of vacancy-based doping of monolayer MoS₂ on oxide

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2015 2D Mater. 2 045009

(http://iopscience.iop.org/2053-1583/2/4/045009)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 137.132.123.69
This content was downloaded on 28/11/2015 at 02:47

Please note that terms and conditions apply.

# 2D Materials

**PAPER**

## Theoretical and experimental investigation of vacancy-based doping of monolayer $\boldsymbol{\ce{MoS_2}}$ on oxide

Amithraj Valsaraj¹, Jiwon Chang², Amritesh Rai¹, Leonard F Register¹ and Sanjay K Banerjee¹

¹ Microelectronics Research Center and Department of Electrical and Computer Engineering, The University of Texas at Austin, Austin, TX-78758, USA
² SEMATECH, 257 Fuller Road #2200, Albany, NY-12203, USA

E-mail: amithrajv@utexas.edu

Keywords: density functional theory, modulation doping, atom projected density of states, transition metal dichalcogenides, high-$k$ dielectric

### Abstract

Monolayer (ML) transition metal dichalcogenides are novel, gapped two-dimensional materials with unique electrical and optical properties. Toward device applications, we consider $\ce{MoS_2}$ layers on dielectrics, in particular in this work, the effect of vacancies on the electronic structure. In density-functional based simulations, we consider the effects of near-interface O vacancies in the oxide slab, and Mo or S vacancies in the $\ce{MoS_2}$ layer. Band structures and atom-projected densities of states for each system and with differing oxide terminations were calculated, as well as those for the defect-free $\ce{MoS_2}$-dielectrics system and for isolated dielectric layers for reference. Among our results, we find that with O vacancies, both the Hf-terminated $\ce{HfO_2}$–$\ce{MoS_2}$ system, and the O-terminated and H-passivated $\ce{Al_2O_3}$–$\ce{MoS_2}$ systems appear metallic due to doping of the oxide slab followed by electron transfer into the $\ce{MoS_2}$, in manner analogous to modulation doping. The n-type doping of ML $\ce{MoS_2}$ by high-$k$ oxides with oxygen vacancies then is experimentally demonstrated by electrically and spectroscopically characterizing back-gated ML $\ce{MoS_2}$ field effect transistors encapsulated by oxygen deficient alumina and hafnia.

### Introduction

The unique electrical and optical properties of monolayer (ML) transition metal dichalcogenides (TMDs) [1, 2] have spurred intense research interest towards development of nanoelectronic devices utilizing these novel materials [3–10]. The atomically thin form of ML TMDs translates to excellent electrostatic gate control even at nanoscale channel length dimensions [11–13]. However, the two-dimensional (2D) nature of ML TMDs makes their properties susceptible to the surrounding environment, as evidenced by the mobility enhancement of ML $\ce{MoS_2}$ when placed on a high-$k$ dielectric such as hafnia ($\ce{HfO_2}$) [4]. This mobility improvement in 2D materials was attributed to the damping of Columbic impurity scattering by high-$k$ dielectrics [14]. Theoretical calculations of $\ce{HfO_2}$ interfaces have indicated that band offsets can be altered chemically by utilizing different interface terminations [15]. The conductive characteristics of $\ce{MoS_2}$ deposited on $\ce{SiO_2}$ have been shown to be dependent on the interface structure [16]. Controllable n-type doping of graphene transistors with extended air stability have been demonstrated by using self-encapsulated doping layers of titanium sub-oxide ($\ce{TiO_x}$) thin films [17]. These results puts into stark focus the need to consider the effect of surrounding materials and the interfaces with them on the characteristics of ML TMDs.

In an earlier preliminary study [18], we considered $\ce{MoS_2}$ on O- and Hf(Al)- terminated $\ce{HfO_2}$ ($\ce{Al_2O_3}$) via density functional theory (DFT). Those results suggest that O-terminated and H-passivated $\ce{HfO_2}$ and $\ce{Al_2O_3}$ exhibit potential as good substrates or gate insulators for ML $\ce{MoS_2}$, with a straddling gap (Type 1) band structure for the composite system devoid of any defect states within the band gap of the $\ce{MoS_2}$. However, ML $\ce{MoS_2}$ on Hf-terminated $\ce{HfO_2}$ shows a staggered gap alignment (Type 2), such that holes would be localized in the oxide rather than the $\ce{MoS_2}$ layer. But in the case of ML $\ce{MoS_2}$ on Al-terminated $\ce{Al_2O_3}$ slab, we found that there is a straddling gap (Type 1)

© 2015 IOP Publishing Ltd

alignment to again provide localization of holes to the $\mathrm{MoS}_{2}$ layer, although with some spill over into the nearby surface O states. We also considered O vacancies for $\mathrm{MoS}_{2}$ on O terminated slabs of $\mathrm{HfO}_{2}$ and $\mathrm{Al}_{2} \mathrm{O}_{3}$, observing significant doping in the latter. However, we did not include the van der Waal's interactions between the $\mathrm{MoS}_{2}$ and oxide as we do in this work, tease out doping mechanism, consider the remaining combinations of oxide terminations, consider vacancies in the $\mathrm{MoS}_{2}$, nor provide any experimental results.

In this work, we focus on the effects of O vacancies (O deficiency) in $\mathrm{MoS}_{2}$ on $\mathrm{HfO}_{2}$ and on $\mathrm{Al}_{2} \mathrm{O}_{3}$, and the effects of Mo and S vacancies in $\mathrm{MoS}_{2}$ on $\mathrm{HfO}_{2}$. We have used both DFT and experimental analysis. For the O deficient systems, two possible terminations for the $\mathrm{HfO}_{2}\left(\mathrm{Al}_{2} \mathrm{O}_{3}\right)$ slab are considered using DFT: an O-terminated $\mathrm{HfO}_{2}\left(\mathrm{Al}_{2} \mathrm{O}_{3}\right)$ slab with $\mathrm{H}$ passivation and an $\mathrm{Hf}(\mathrm{Al})$-terminated $\mathrm{HfO}_{2}\left(\mathrm{Al}_{2} \mathrm{O}_{3}\right)$. The naming of two possible terminations is indicative of the initial structures used as starting point in our atomistic relaxations. The effects of O-vacancies in the first few layers of oxide on the band structure of the $\mathrm{MoS}_{2-}$ oxide system were simulated, with results for vacancies in the topmost/ $\mathrm{MoS}_{2}$-adjacent $\mathrm{O}$ layer shown here. Among our findings, $\mathrm{O}$ vacancies can lead to modulation-like doping of the $\mathrm{MoS}_{2}$ from donor states in the oxide depending on the oxide terminations. Moreover, consistent with our theoretical results, electron doping of ML $\mathrm{MoS}_{2}$ via $\mathrm{O}$ deficiency in the high- $k$ oxides was experimentally demonstrated by electrically and spectroscopically characterizing back-gated ML $\mathrm{MoS}_{2}$ field effect transistors (FETs) encapsulated by $\mathrm{O}$ deficient alumina $\left(\mathrm{Al}_{2} \mathrm{O}_{x}\right)$ or $\mathrm{O}$ deficient hafnia $\left(\mathrm{HfO}_{x}\right)$.

## Methods
### Computational details
The DFT calculations were performed using the projector-augmented wave method with a plane-wave basis set as implemented in the Vienna $a b$ initio simulation package $[19,20]$. We chose a kinetic energy cutoff of $400 \mathrm{eV}$. The $k$-mesh grid of $7 \times 7 \times 1$ for the sampling of the first Brillouin zone (BZ) of the supercell was selected according to Monkhorst-Pack type meshes with the origin being at the $\Gamma$ point for all calculations except the band structure calculation. The local density approximation (LDA) [21] was employed primarily for the exchange-correlation potential as LDA has been shown to reproduce the apparent experimental band gap $\left(E_{\mathrm{g}}=1.8 \mathrm{eV}\right)[1]$ of ML $\mathrm{MoS}_{2}$ well $[22,23]$. The calculated lattice constant for the $\mathrm{MoS}_{2}$ layer after volume relaxation, $a=3.122 \AA$, is also a good match to the experimental value [24]. We have also re-checked some of the DFT results using the generalized gradient approximation (GGA) [25]. We note, however, that both the LDA and the GGA underestimate the band gap of at least the bulk $\mathrm{HfO}_{2}$ and $\mathrm{Al}_{2} \mathrm{O}_{3}$, which makes the prediction of band offsets from theoretical calculations unreliable. With approximately 150 atoms per supercell, use of presumably more accurate hybrid functionals or GW methods for atomistic relaxations was not practical. However, we have utilized hybrid functionals, namely HSE06 [26], to perform band structure calculations using the relaxed structures from our GGA simulations to further check our key conclusions. However, the primary objective of this theoretical work is to explore possible pathways to insulating and doping $\mathrm{MoS}_{2}$ MLs qualitatively toward device applications, ultimately for experimental follow-up for promising cases. Similarly, we did not include spin-orbit coupling here, which causes substantial spin splitting in the valence band, for similar reason. However, only conduction band doping is observed in our results, mitigating the impact of this latter approximation. Van der Waal's forces also were simulated due to the absence of covalent bonding between the TMD and the oxides [27]. In our computations, we have adopted the DFT-D2 scheme to model the non-local dispersive forces wherein a semi-empirical correction is added to the conventional Kohn-Sham DFT theory [28].

The two representative dielectrics, $\mathrm{HfO}_{2}$ and $\mathrm{Al}_{2} \mathrm{O}_{3}$, were chosen for high- $k$ value and minimal lattice mismatch, respectively. The $\mathrm{MoS}_{2}$ ML of principle interest, with its hexagonal lattice, was taken to be unstrained with its above-noted volume-relaxed lattice constant of $a=3.122 \AA$. For the dielectric oxide, the energetically stable crystalline phases of bulk $\mathrm{HfO}_{2}$ and $\mathrm{Al}_{2} \mathrm{O}_{3}$ at ambient conditions, namely, monoclinic $\mathrm{HfO}_{2}$ [29] and hexagonal $\mathrm{Al}_{2} \mathrm{O}_{3}$ [30], respectively, were utilized. Our simulations were performed by constructing a supercell of ML $\mathrm{MoS}_{2}$ on an approximately $2 \mathrm{~nm}$ thick oxide slab. For $\mathrm{HfO}_{2}$, atomic relaxation was performed within a rectangular supercell $(a=9.366 \AA, b=5.407 \AA)$ chosen to reduce the lattice mismatch between ML $\mathrm{MoS}_{2}$ and monoclinic $\mathrm{HfO}_{2}$. However, a roughly $6 \%$ strain remains along the in-plane directions in the $\mathrm{HfO}_{2}$ (figure 1(a)). For $\mathrm{Al}_{2} \mathrm{O}_{3}$, atomic relaxation was performed in a (rotated) hexagonal supercell $(a=8.260 \AA)$ with a strain of only about $0.2 \%$ (figure 1(b)). The systems were relaxed until the Hellmann-Feynman forces on the atoms were less than $0.02 \mathrm{eV} \AA^{-1}$. During relaxation, all the $\mathrm{MoS}_{2}$ ML atoms and the top half of the layers of the dielectric oxide were allowed to move in all three spatial dimensions. Oxygen vacancies were modeled by removing a single $\mathrm{O}$ atom from an $\mathrm{O}$-layer of the supercell. Since we have periodic supercells, the $\mathrm{O}$ vacancy is repeated in each instance of the supercell. The system is then allowed to relax again with the introduced O-vacancy. A similar procedure was followed in the modeling of Mo and S vacancies in the $\mathrm{MoS}_{2}-\mathrm{HfO}_{2}$ system. In the latter case, the $\mathrm{S}$ atom vacancy was introduced in the layer adjacent to the

![](./images/814578350226931716_1.jpg)

**Figure 1.** (a) Supercell of ML MoS₂ on an H-passivated, O-terminated HfO₂ slab of approximately 2 nm thickness with O-vacancy (side view). (b) Supercell of ML MoS₂ on an H-passivated, O-terminated Al₂O₃ slab of approximately 2 nm thickness with O-vacancy (side view). The monolayer of MoS₂ belongs to the space group P-6m2 (point group D₃h). (c) 3D schematic of a back-gated ML MoS₂ FET encapsulated by HfOₓ.

oxide surface. All simulations were performed at a temperature of 0 K.

## Experiment
ML MoS₂ was mechanically exfoliated from commercially available bulk MoS₂ crystals (SPI Supplies) onto a degenerately doped n-type Si-(100) substrate, which served as the back-gate, covered by a 90 nm thick thermal oxide. Upon exfoliation, the samples were annealed at 350 °C in high vacuum ($\sim 10^{-6}$ Torr) for 8 h to minimize tape residues and trapped adsorbates between the MoS₂ and the silicon dioxide substrate. A combination of optical microscopy, atomic force microscopy, Raman and photoluminescence measurements were used to identify atomically flat ML MoS₂ flakes of interest. Source and drain contacts were patterned using electron beam lithography followed by electron beam evaporation and solvent lift-off of an Ag/Au (20/30 nm) stack in the case of hafnia, or just Au (50 nm) in the case of alumina. Finally, devices were covered by $\sim 30$ nm of either alumina or hafnia deposited at 200 °C using atomic layer deposition (ALD) via the reaction of water with standard ALD precursors, namely trimethyl aluminum for alumina and tetrakis (dimethylamido) hafnium for hafnia (figure 1(c)). An in-depth look at the experimental details and device fabrication procedures can be found in the work by Rai *et al* [31, 32]. The stoichiometry of the as-deposited high-$k$ oxide was determined using x-ray photoelectron spectroscopy (XPS).

## Results and discussion
The band structure and atom-projected density of states (AP-DOS) have been calculated for the ML MoS₂-oxide system considering different possible terminations of the oxide at the interface in the presence of O vacancies in the oxide or Mo and S vacancies in the MoS₂. We compared (overlaid) the band structures for the MoS₂-oxide systems with vacancies to the ideal MoS₂-oxide results. In all cases, the highest occupied state of the system with vacancies serves as the zero energy reference in these 0 K simulations. However, the reference band structures absent vacancies are shifted up or down to provide a rough fit to the former in terms of band structure and the AP-DOS of the Mo and S atoms. (Otherwise, the zero energy reference for the latter would be the valence band edge.)

### ML MoS₂ on HfO₂ slab with O vacancy
When an O vacancy is introduced into the top layer of the O-terminated and H-passivated HfO₂ slab, in these 0 K simulations, an occupied defect state (band) is introduced within the band gap of ML MoS₂ (figure 2(a)), which is associated primarily with Hf atoms in the oxide. Analogous Hf-associated defect states also arise in an isolated O-terminated and H-passivated HfO₂ slab (figures 3(a) and (b)). In this latter case (and for analogous cases below) we simply removed the MoS₂ layer from the combined system, while otherwise holding the crystal structure fixed as a control. However, the close proximity of the occupied defect band to the conduction band (of the reference band structure) suggests that these states might be able to act as donors. As can be seen from the AP-DOS (figure 2(b)), the conduction band edge for MoS₂ is pinned at the Fermi level indicating n-type doping. However, the defect band formation due to the limited supercell size and associated very large $(1.97 \times 10^{14}\ \text{cm}^{-2})$ O-vacancy density in these simulations leaves the binding energy for lower defect densities uncertain. Alternatively, these interface states could function as relatively shallow charge traps, leading to degradation of device performance. Since a rectangular supercell was used in these simulations of MoS₂ on HfO₂, the corresponding BZ is smaller and the $K$ point of the primitive unit cell—where the ML

![](./images/814578350226931716_2.jpg)

Figure 2. (a) Band structure of ML MoS₂ on an H-passivated, O-terminated HfO₂ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ (black solid lines). The 0 eV reference corresponds to the highest occupied state in these 0 K simulations. The band structure of vacancy-free ML MoS₂–HfO₂ system (O-terminated) is superimposed for comparison (red dashed lines). However, this latter band structure, which otherwise would have its zero reference energy at the upper edge of the valence band, is shifted up or down to provide a reasonable fit to the former. (b) Atom-projected density of states for the ML MoS₂ and O-terminated HfO₂ system with an O-vacancy. Red arrows indicate the conduction and valence band edges. An occupied defect state (band) is introduced within the band gap of ML MoS₂.

![](./images/814578350226931716_3.jpg)

Figure 3. (a) Band structure of a freestanding H-passivated, O-terminated HfO₂ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ (black solid lines). The energy-shifted band structure of vacancy-free HfO₂ slab (O-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the O-terminated HfO₂ system with an O-vacancy. Defect states associated with Hf-atoms are observed.

MoS₂ band edges are located—folds into the $\Gamma$ point in the supercell's BZ.

In the case of Hf-terminated HfO₂–MoS₂ system with an O vacancy in the top layer of oxide, there is a straddling gap alignment (Type 1) as seen in the AP-DOS (figure 4(b)) for this large O-vacancy density, much as for O-terminated HfO₂. Moreover, there are now two partially occupied bands at the bottom of the conduction band (figure 4(a)), both of which are largely localized to the MoS₂ layer, resulting in a system that now appears metallic. Calculation of the band structure for a freestanding Hf-terminated HfO₂ slab with an O vacancy exhibits occupied conduction band states associated with the Hf atoms (figures 5(a) and (b)). In the combined HfO₂–MoS₂ system, these electrons are then transferred into the lower conduction-band-edge MoS₂ layer, in a modulation-doping-like process. In MoS₂, the DOS at the conduction and valence band edges are dominated by $d_{xz}$ and $d_{z^2}$ orbitals from the Mo atoms while in the HfO₂ the band edge states arise mainly from the contribution of Hf—d orbitals and O—p orbitals.

For the HfO₂–MoS₂ with O vacancy systems, we also repeated the simulations with the GGA approximation for comparison with the above LDA results. Figure 6(a) shows the band structure of ML MoS₂ on Hf-terminated HfO₂ with an O-vacancy, as obtained using both the GGA and the LDA approximations. The same nominal crystal structure was used, but a separate relaxation was performed for the LDA and

![](./images/814578350226931716_4.jpg)

Figure 4. (a) Band structure of ML MoS₂ on Hf-terminated HfO₂ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ (black solid lines). The energy-shifted band structure of vacancy free ML MoS₂–HfO₂ system with Hf-termination is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the ML MoS₂ and Hf-terminated HfO₂ system with an O-vacancy. A straddling gap band alignment is now observed along with two partially occupied bands at the conduction band edge both of which are largely localized to the MoS₂ layer, resulting in a system that now appears metallic.

![](./images/814578350226931716_5.jpg)

Figure 5. (a) Band structure of a freestanding Hf-terminated HfO₂ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ. The energy-shifted band structure of vacancy-free HfO₂ slab (Hf-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the Hf-terminated HfO₂ system with an O-vacancy. An occupied conduction band edge state associated with the Hf atoms is observed.

GGA calculations (the latter, however, starting with the former for computational efficiency). As can be seen, the results match closely, including the degree of degenerate doping. A similar comparison (not shown) was performed for MoS₂ on O-terminated HfO₂, again with good agreement between the results obtained with the GGA and with the LDA including the location of the occupied defect band just below the conduction band. Finally, in figure 6(b), we have used hybrid functionals, specifically HSE06, which provide a more accurate value for the band gap of bulk HfO₂ to simulate the band structure of ML MoS₂ on Hf-terminated HfO₂, to further check key results. The much larger computational demands required for hybrid method combined with the large supercell size constrained us to use a coarse $k$-point grid for evaluation of the band structure and precluded us from running any relaxations of the structure using the hybrid method. Instead, we reused the structure obtained from the GGA relaxations. As shown in figure 6(b), with the hybrid method, the conduction band edge is again pulled below the Fermi level as in our previous GGA and LDA results, indicating the n-type doping of ML MoS₂ modulated by dielectric oxide.

### ML MoS₂ on Al₂O₃ slab with O vacancy
For the O-terminated and H-passivated Al₂O₃–MoS₂ system, creation of an O vacancy in the top O-layer of Al₂O₃ produces only a modest effect on the

![](./images/814578350226931716_6.jpg)

Figure 6. (a) Band structure of ML MoS₂ on an Hf-terminated HfO₂ with an O vacancy obtained using the GGA (solid lines, black online). The band structure obtained using the LDA is overlaid on top for comparison (dashed lines, red online). Both results exhibit n-type doping, and essentially the same degree of degeneracy. (The zero energy reference remains the Fermi level in each case.) (b) Band structure of ML MoS₂ on an Hf-terminated HfO₂ with an O vacancy obtained using the HSE06. The conduction band edge is pulled below the Fermi level indicating n-type doping of MoS₂.

![](./images/814578350226931716_7.jpg)

Figure 7. (a) Band structure of ML MoS₂ on an H-passivated, O-terminated Al₂O₃ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ (black solid lines). The energy-shifted band structure of vacancy free ML MoS₂–Al₂O₃ system (O-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the ML MoS₂ and O-terminated Al₂O₃ system with an O-vacancy. A new partially filled band is introduced at the edge of the MoS₂ conduction band, which is largely localized to the MoS₂ layer, resulting in a system that now appears metallic.

conduction band edge states in comparison to the vacancy free reference system. However, the O-vacancy pulls the conduction band edge below the Fermi level, filling the lower MoS₂ conduction band states (figure 7(a)), which remain largely localized in space to the MoS₂ layer (figure 7(b)), resulting in a system that now appears metallic, much as for the Hf-terminated HfO₂–MoS₂ system with an O vacancy. Calculation of the band structure for an isolated O-terminated Al₂O₃ slab with an O vacancy exhibits occupied conduction band states associated with the O atoms (figures 8(a) and (b)). In the combined Al₂O₃–MoS₂ system, these electrons again are transferred into the lower conduction-band-edge MoS₂ layer, in a modulation-doping-like process.

For Al-terminated Al₂O₃–MoS₂ system, the system retains a straddling gap alignment after the introduction of an O vacancy in the oxide layer. However, an occupied state (band) deep in the band gap of the MoS₂ is produced (figure 9(a)), which is localized to the Al and O atoms in the oxide layer (figure 9(b)). Such defect states could serve as recombination centers or charge traps. In addition, however, a direct band gap is found at these doping concentrations, in contrast to the Al-terminated Al₂O₃–MoS₂ system without an O vacancy.

### Mo and S vacancies in MoS₂
We introduced a single Mo or S atom vacancy in the supercell of the MoS₂ on O-terminated and H-passivated HfO₂ system, with the S atom vacancy introduced in the layer adjacent to the oxide surface. The corresponding vacancy density is $1.97 \times 10^{14}\ \mathrm{cm}^{-2}$ in either case. The resultant band structure

![](./images/814578350226931716_8.jpg)

Figure 8. (a) Band structure of freestanding H-passivated, O-terminated $Al_2O_3$ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ. The energy-shifted band structure of vacancy-free $Al_2O_3$ slab (O-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the O-terminated $Al_2O_3$ system with an O-vacancy. An occupied conduction band edge state associated with the O atoms is observed.

![](./images/814578350226931716_9.jpg)

Figure 9. (a) Band structure of ML $MoS_2$ on Al-terminated $Al_2O_3$ slab with an O-vacancy in the top layer, plotted along the high symmetry directions of the BZ (black solid lines). The energy-shifted band structure of vacancy free ML $MoS_2$–$Al_2O_3$ system (Al-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the ML $MoS_2$ and Al-terminated $Al_2O_3$ system with an O-vacancy. An occupied state (band) deep in the band gap of the $MoS_2$ is produced, which is localized to the Al and O atoms in the oxide layer.

and AP-DOS are plotted in figures 10 and 11 for $MoS_2$–$HfO_2$ systems with Mo and S vacancies, respectively. In both cases, a straddling gap alignment is retained, but defect states are introduced into the band gap of the $MoS_2$ that are localized to the $MoS_2$ layer (figures 10(b) and 11(b)). With the Mo vacancy, several states are introduced within the nominal band gap, both occupied and empty, although at this vacancy concentration, the valence band edge is difficult to define (figure 10(a)). In the case of S vacancies in the $MoS_2$ ML, there are two unoccupied defect states (bands) introduced near mid gap, as well as significant distortion of the valence band edge structure at these vacancy concentrations (figure 11(a)).

### Experimental results

Electron doping of ML $MoS_2$ by O deficient high-$k$ oxides was experimentally demonstrated by electrically and spectroscopically characterizing back-gated ML $MoS_2$ FETs encapsulated by alumina ($Al_2O_x$) and hafnia ($HfO_x$). The DFT calculations would suggest that an O-deficient high-$k$ oxide encapsulating the $MoS_2$ ML would produce a combination of n-type modulation doping of the bands and occupied defect states within the gap in bulk materials, the latter contributing perhaps little to the doping but important when trying to pull the Fermi level below them. On exposure to air, the Hf (Al)-terminated $HfO_2$ ($Al_2O_3$) is unrealistic while the O-termination

![](./images/814578350226931716_10.jpg)

Figure 10. (a) Band structure of ML MoS₂ on an H-passivated, O-terminated HfO₂ slab with Mo-vacancy in the ML, plotted along the high symmetry directions of the BZ (black solid lines). The energy-shifted band structure of vacancy free ML MoS₂-HfO₂ system (O-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the ML MoS₂ and O-terminated HfO₂ system with Mo vacancy. Several states are introduced within the nominal band gap and significant distortion of the valence band edge structure is observed.

![](./images/814578350226931716_11.jpg)

Figure 11. (a) Band structure of ML MoS₂ on an H-passivated, O-terminated HfO₂ slab with S-vacancy in the ML, plotted along the high symmetry directions of the BZ (black solid lines). The energy-shifted band structure of vacancy free ML MoS₂-HfO₂ system (O-terminated) is superimposed for comparison (red dashed lines). (b) Atom-projected density of states for the ML MoS₂ and O-terminated HfO₂ system with S vacancy. Two unoccupied defect states (bands) are introduced near mid gap, and significant distortion of the valence band edge structure is observed.

provides a more accurate model for surface termina- tion in the oxide. However, in our experimental system (figure 1(c)), the high-$k$ oxide encloses the MoS₂ ML and MoS₂-oxide interface is not exposed to air allowing us to investigate both O-rich and O-deficient oxide interfaces.

Figure 12(a) shows the room temperature (RT) transfer characteristics of a back-gated ML MoS₂ FET before (blue) and after (red) encapsulation by ALD HfOₓ. The length ($L_{\text{CH}}$) and width ($W$) of the device are 900 nm and $2\ \mu\text{m}$, respectively, and the data was collected at a drain-source voltage ($V_{\text{DS}}$) of 50 mV. Before encapsulation, the device exhibits a threshold voltage ($V_{\text{th}}$) near $-15$ to $-20$ V. After encapsulation in ALD HfOₓ, there is a large negative shift in $V_{\text{th}}$ consistent with n-type doping, as well as pronounced stretch-out of the transfer characteristic as $V_{\text{BG}}$ is made more negative, consistent with near-band-edge defects in the band gap as predicted by the DFT for O-deficient HfOₓ. The n-type doping was further confirmed in Raman spectroscopy performed on the ML MoS₂ in the channel region of the same FET, figure 12(b), before (blue) and after (red) HfOₓ encapsulation. Before HfOₓ, the peak positions of the out-of-plane $A_{1\text{g}}$ and the in-plane $E_{2\text{g}}^{1}$ peaks are at $\sim402\ \text{cm}^{-1}$ and $\sim383\ \text{cm}^{-1}$, respectively, which is characteristic of ML MoS₂ [33]. After HfOₓ encapsulation, the $E_{2\text{g}}^{1}$ peak remains relatively unchanged, while the $A_{1\text{g}}$ peak shows a distinct broadening and a red shift in its peak position from $\sim402\ \text{cm}^{-1}$ to $\sim399\ \text{cm}^{-1}$. These changes in the $A_{1\text{g}}$ Raman peak upon HfOₓ encapsulation are indicative of the

![](./images/814578350226931716_12.jpg)

Figure 12. (a) Room temperature transfer characteristics of a back-gated ML MoS₂ FET before (blue) and after (red) ~30 nm ALD HfOₓ ($x \sim 1.56$) encapsulation, and (b) corresponding normalized Raman spectra of the ML MoS₂ FET channel before (blue) and after (red) ALD HfOₓ encapsulation. The shifted threshold voltage and $A_{1g}$ peak are consistent with n-type doping after encapsulation.

![](./images/814578350226931716_13.jpg)

Figure 13. (a) Room temperature transfer characteristics of a back-gated ML MoS₂ FET before (blue) and after (red) ~30 nm ALD HfOₓ ($x \sim 2.1$) encapsulation, and (b) corresponding normalized Raman spectra of the ML MoS₂ FET channel before (blue) and after (red) ALD HfOₓ encapsulation. There is no red shift or peak broadening of the $A_{1g}$ Raman mode implying negligible n-type doping of MoS₂.

increased electron concentration in the ML MoS₂ channel, and also have been observed in previous n-type doping studies of MoS₂ [34]. The Hf:O atomic ratio in the as-deposited HfOₓ was determined to be ~1:1.56 from XPS analysis, thereby establishing the correlation between oxygen deficiency and n-type doping of ML MoS₂ caused by HfOₓ.

The results for the control sample of O-rich HfOₓ on ML MoS₂ are shown in figure 13. The Hf:O ratio for the ALD deposited O-rich HfOₓ was determined to be ~1:2.1 from XPS measurements in exactly the same manner and using the same number of components that were used in peak fitting of the O-deficient HfOₓ. As can be clearly seen, there is negligible change in the Raman spectra of MoS₂ after O-rich HfOₓ deposition. There is no red shift or peak broadening of the $A_{1g}$ Raman mode implying negligible n-type doping of MoS₂. Moreover, from the transfer curve we can see that the device can be turned off within the same back-gate voltage sweep range after deposition of the O-rich HfOₓ. These results depict negligible doping of the ML MoS₂ after O-rich HfOₓ deposition, which contrast to the strong doping of the MoS₂ when an O-deficient HfOₓ was deposited.

Similar n-type doping results were obtained after encapsulating back-gated ML MoS₂ FETs with ALD Al₂Oₓ. Figures 14(a) and (b) show the RT transfer characteristics of a ML MoS₂ FET ($L_{CH}=500$ nm, $W=2.3$ μm, $V_{DS}=100$ mV, Au contacts) and the normalized Raman spectra of the ML MoS₂ channel, respectively, before (blue) and after (red) ALD Al₂Oₓ deposition. As in the case of HfOₓ, the negative $V_{th}$ shift (figure 14(a)) and the broadening and red shift of the $A_{1g}$ Raman peak (figure 14(b)) of ML MoS₂ after encapsulation in ALD Al₂Oₓ is indicative of n-type doping, again consistent with the DFT results with oxygen vacancies. The Al:O atomic ratio was determined to be ~2:1.55 from XPS analysis, thereby,

![](./images/814578350226931716_14.jpg)

confirming the inherent oxygen deficiency in the as-deposited high-$k$ oxide.

## Conclusion

In summary, DFT simulations suggest that occupied near-conduction-band-edge states that might function either as donors or shallow traps are introduced in the MoS₂-oxide system by O vacancies in the O-terminated and H-passivated HfO₂–MoS₂ system. More promising as a means of doping, with O vacancies, both the Hf-terminated HfO₂–MoS₂ system, and the O-terminated and H-passivated Al₂O₃–MoS₂ system appear metallic due to doping of the oxide slab followed by electron transfer into the MoS₂, in manner analogous to modulation doping. Consistent with these latter theoretical results, n-type doping of ML MoS₂ by high-$k$ oxides with oxygen vacancies was demonstrated experimentally by electrically and spectroscopically characterizing back-gated ML MoS₂ FETs encapsulated by alumina (Al₂Oₓ) and hafnia (HfOₓ). In contrast to the effects of vacancies in the oxides, in simulations, Mo and S vacancies in MoS₂ ML introduces multiple deep defect states in the band gap of MoS₂, as well as distorting the band edges.

## Acknowledgments

This work is supported by SEMATECH, the Nanoelectronics Research Initiative (NRI) through the Southwest Academy of Nanoelectronics (SWAN), and Intel. We thank the Texas Advanced Computing Center (TACC) for computational support.

## References

[1] Mak K F, Lee C, Hone J, Shan J and Heinz T F 2010 Atomically thin MoS₂: a new direct-gap semiconductor *Phys. Rev. Lett.* **105** 136805

[2] Splendiani A, Sun L, Zhang Y, Li T, Kim J, Chim C-Y, Galli G and Wang F 2010 Emerging photoluminescence in monolayer MoS₂ *Nano Lett.* **10** 1271–5

[3] Yoon Y, Ganapathi K and Salahuddin S 2011 How good can monolayer MoS₂ transistors be? *Nano Lett.* **11** 3768–73

[4] Radisavljevic B, Radenovic A, Brivio J, Giacometti V and Kis A 2011 Single-layer MoS₂ transistors *Nat. Nanotechnology* **6** 147–50

[5] Liu H and Ye P D 2012 Dual-gate MOSFET with atomic-layer-deposited as top-gate dielectric *IEEE Electron Device Lett.* **33** 546–8

[6] Bertolazzi S, Krasnozhon D and Kis A 2013 Nonvolatile memory cells based on MoS₂/graphene heterostructures *ACS Nano* **7** 3246–52

[7] Fontana M, Deppe T, Boyd A K, Rinzan M, Liu A Y, Paranjape M and Barbara P 2013 Electron–hole transport and photovoltaic effect in gated MoS₂ Schottky junctions *Sci. Rep.* **3** 1634

[8] Lopez-Sanchez O, Lembke D, Kayci M, Radenovic A and Kis A 2013 Ultrasensitive photodetectors based on monolayer MoS₂ *Nat. Nanotechnology* **8** 497–501

[9] Late D J *et al* 2013 Sensing behavior of atomically thin-layered MoS₂ transistors *ACS Nano* **7** 4879–91

[10] Chang J, Register L F and Banerjee S K 2013 Atomistic full-band simulations of monolayer MoS₂ transistors *Appl. Phys. Lett.* **103** 223509

[11] Wang Q H, Kalantar-Zadeh K, Kis A, Coleman J N and Strano M S 2012 Electronics and optoelectronics of two-dimensional transition metal dichalcogenides *Nat. Nanotechnology* **7** 4329–36

[12] Jariwala D, Sangwan V K, Lauhon L J, Marks T J and Hersam M C 2014 Emerging device applications for semiconducting two-dimensional transition metal dichalcogenides *ACS Nano* **8** 1102–20

[13] Liu H, Neal A T and Ye P D 2012 Channel length scaling of MoS₂ MOSFETs *ACS Nano* **6** 8563–9

[14] Jena D and Konar A 2007 Enhancement of carrier mobility in semiconductor nanostructures by dielectric engineering *Phys. Rev. Lett.* **98** 136805

[15] Peacock P W, Xiong K, Tse K and Robertson J 2006 Bonding and interface states of Si:HfO₂ and Si:ZrO₂ interfaces *Phys. Rev. B* **73** 075328

[16] Dolui K, Rungger I and Sanvito S 2013 Origin of the n-type and p-type conductivity of $MoS_2$ monolayers on a $SiO_2$ substrate Phys. Rev. B 87 165402

[17] Ho P-H, Yeh Y-C, Wang D-Y, Li S-S, Chen H-A, Chung Y-H, Lin C-C, Wang W-H and Chen C-W 2012 Self-encapsulated doping of n-type graphene transistors with extended air stability ACS Nano 6 6215-21

[18] Valsaraj A, Register L F, Banerjee S K and Chang J 2014 Density-functional-theory-based study of monolayer $MoS_2$ on oxide 2014 Int. Conf. on Simulation of Semiconductor Processes and Devices (SISPAD) pp 73-6

[19] Kresse G and Furthmüller J 1996 Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set Phys. Rev. B 54 11169-86

[20] Kresse G and Furthmüller J 1996 Efficiency of ab initio total energy calculations for metals and semiconductors using a plane-wave basis set Comput. Mater. Sci. 6 15-50

[21] Perdew J P and Wang Y 1992 Accurate and simple analytic representation of the electron-gas correlation energy Phys. Rev. B 45 13244-9

[22] Chang J, Register L F and Banerjee S K 2014 Ballistic performance comparison of monolayer transition metal dichalcogenide $MX_2$ (M = Mo, W; X = S, Se, Te) metal-oxide-semiconductor field effect transistors J. Appl. Phys. 115 084506

[23] Kang J, Liu W, Sarkar D, Jena D and Banerjee K 2014 Computational study of metal contacts to monolayer transition-metal dichalcogenide semiconductors Phys. Rev. X 4 031005

[24] Böker T, Severin R, Müller A, Janowitz C, Manzke R, Voß D, Krüger P, Mazur A and Pollmann J 2001 Band structure of $MoS_2$, $MoSe_2$, and $\alpha$-MoTe2: angle-resolved photoelectron spectroscopy and ab initio calculations Phys. Rev. B 64 235305

[25] Perdew J P, Burke K and Ernzerhof M 1996 Generalized gradient approximation made simple Phys. Rev. Lett. 77 3865-8

[26] Krukau A V, Vydrov O A, Izmaylov A F and Scuseria G E 2006 Influence of the exchange screening parameter on the performance of screened hybrid functionals J. Chem. Phys. 125 224106

[27] McDonnell S, Brennan B, Azcatl A, Lu N, Dong H, Buie C, Kim J, Hinkle C L, Kim M J and Wallace R M 2013 $HfO_2$ on $MoS_2$ by atomic layer deposition: adsorption mechanisms and thickness scalability ACS Nano 7 10354-61

[28] Grimme S, Antony J, Ehrlich S and Krieg H 2010 A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu J. Chem. Phys. 132 154104

[29] Kang J, Lee E-C and Chang K J 2003 First-principles study of the structural phase transformation of hafnia under pressure Phys. Rev. B 68 054106

[30] Mo S-D and Ching W Y 1998 Electronic and optical properties of $\theta$-$Al_2O_3$ and comparison to $\alpha$-$Al_2O_3$ Phys. Rev. B 57 15219-28

[31] Rai A et al 2015 Air stable doping and intrinsic mobility enhancement in monolayer molybdenum disulfide by amorphous titanium suboxide encapsulation Nano Lett. (doi:10.1021/acsnanolett.5b00314)

[32] Rai A, Valsaraj A, Movva H C P, Roy A, Tutuc E, Register L F and Banerjee S K 2015 Interfacial-oxygen-vacancy mediated doping of $MoS_2$ by high- $\kappa$ dielectrics 2015 73rd Annual Device Research Conf. (DRC) pp 189-90

[33] Li H, Zhang Q, Yap C C R, Tay B K, Edwin T H T, Olivier A and Baillargeat D 2012 From bulk to monolayer $MoS_2$: evolution of Raman scattering Adv. Funct. Mater. 22 1385-90

[34] Kiriya D, Tosun M, Zhao P, Kang J S and Javey A 2014 Air-stable surface charge transfer doping of $MoS_2$ by benzyl viologen J. Am. Chem. Soc. 136 7853-6