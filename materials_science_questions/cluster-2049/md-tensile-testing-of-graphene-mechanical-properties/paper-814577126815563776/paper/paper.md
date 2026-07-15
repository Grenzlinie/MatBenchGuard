RESEARCH ARTICLE

MATERIALS SCIENCE

# Mechanism of strength reduction along the graphenization pathway
Antonio Gamboa, $^{1,2,3}$ Baptiste Farbos, $^{1}$ Philippe Aurel, $^{2}$ Gérard L. Vignoles, $^{1}$ Jean-Marc Leyssale $^{1,4 *}$

2015 © The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).
10.1126/sciadv.1501009

Even though polycrystalline graphene has shown a surprisingly high tensile strength, the influence of inherent grain boundaries on such property remains unclear. We study the fracture properties of a series of polycrystalline graphene models of increasing thermodynamic stability, as obtained from a long molecular dynamics simulation at an elevated temperature. All of the models show the typical and well-documented brittle fracture behavior of polycrystalline graphene; however, a clear decrease in all fracture properties is observed with increasing annealing time. The remarkably high fracture properties obtained for the most disordered (less annealed) structures arise from the formation of many nonpropagating prefracture cracks, significantly retarding failure. The stability of these reversible cracks is due to the nonlocal character of load transfer after a bond rupture in very disordered systems. It results in an insufficient strain level on neighboring bonds to promote fracture propagation. Although polycrystallinity seems to be an unavoidable feature of chemically synthesized graphenes, these results suggest that targeting highly disordered states might be a convenient way to obtain improved mechanical properties.

## INTRODUCTION
The outstanding electronic, thermal, and mechanical properties of graphene have attracted considerable interest after its discovery by Novoselov *et al.* (1). Today, it is considered as a particularly promising building-block material for many nanotechnological applications such as transistors (2), nanomechanical resonators (3), or flexible electronics (4). Large-scale production of graphene is usually achieved through chemical vapor deposition (CVD) (5) or through reduction of graphene oxide (6, 7). An important drawback of these chemically derived graphenes is their polycrystalline nature, which can affect their properties (8). Grain boundaries (GBs) in CVD graphenes have been shown to mainly consist in serpent-like, often discontinuous, chains of pentagon-heptagon pairs (8–12). Other topological (point or extended) defects, as well as holes, have also been observed (11, 13) in CVD samples and in reduced graphene oxide at even higher concentrations (13).

Nanoindentation tests performed by Lee *et al.* (14) on polycrystalline samples with grain sizes in the range 1 to 100 μm did not exhibit any measurable property reduction with respect to pristine graphene (15). Similar experiments performed by Rasool *et al.* (8) on bicrystalline samples indicated a strength reduction of around 40 to 50% for low-angle GBs, in agreement with theoretical calculations on ideal tilt GBs (16, 17). Molecular dynamics (MD) simulations were also used to investigate the mechanics of more realistic polycrystalline graphene (PCG) models (18–21), constructed either from the growth of different randomly oriented graphene seeds (18, 21) or from the Voronoï tessellation of randomly oriented grains (20). Brittle fracture was observed in all of these studies, with crack nucleation occurring at bonds shared by a hexagon and a heptagon at GB ends or junctions. Young’s modulus increased with grain size, whereas the ultimate (or failure) strain decreased. Most recent investigations indicated an increase (inverse pseudo–Hall-Petch effect) in intrinsic strength with increasing grain size (20, 21), although earlier work on less disordered systems indicated the opposite (pseudo–Hall-Petch) effect (22). A detailed picture of the relationship between the structure (nature and spatial arrangement of grains and GBs) and the fracture properties and mechanisms is needed. Especially, the evolution of these properties along a thermodynamic path connecting highly disordered graphenes to their pristine counterpart remains unexplored.

In this work, we study the fracture properties of a highly disordered PCG model produced by a quench algorithm and their evolutions after exposure for increasing times at elevated temperatures, during which both the grain size and the nature and amount of GB evolve progressively toward pristine graphene. Our results show that fracture properties, including strain, stress, and energy, are significantly reduced along such a “graphenization” path. We then show that fracture in the most disordered (less annealed) models is delayed by the formation of many stable and reversible prefracture cracks (PFCs), with the latter being stabilized by the nonlocal character of load transfer after a bond rupture in highly disordered systems.

## RESULTS
Figure 1 shows our starting PCG model obtained from a long templated liquid-quench MD simulation. It is composed of disoriented hexagonal graphene domains connected by serpent-like high-angle GBs (Fig. 1B) in a highly disordered fashion. Some low-angle GBs (or subgrain boundaries) formed by distant, yet aligned, pentagon-heptagon pairs can also be observed (compare the low misorientation angle in Fig. 1C to the one in Fig. 1B). Other topological point defects include dislocation cores made of isolated pentagon-heptagon pairs (nonclosing Burger’s circuit in Fig. 1C), as well as lattice-preserving reconstructions of the divacancy (23–25) defect (Fig. 1D). Some planar amorphous domains at the junction of different GBs (Fig. 1E) are also observed. A few atoms (fewer than 0.1% of the total number) depart from the threefold $sp^2$ coordination. These defects, formed during the quench simulation, are mostly planar fourfold atoms, a well-known artifact from the reactive empirical bond order (REBO) family of interatomic potentials (26).

$^1$Laboratoire des Composites ThermoStructuraux, Université de Bordeaux, CNRS, Commissariat à l'énergie atomique et aux énergies alternatives, Herakles, Pessac 33600, France. $^2$Institut des Sciences Moléculaires, Université de Bordeaux, CNRS, Talence 33400, France. $^3$Centro de Investigaciones Químicas, Universidad Autónoma del Estado de Morelos, Cuernavaca, Mor 62209, Mexico. $^4$MultiScale Material Science for Energy and Environment, Massachusetts Institute of Technology–CNRS, Cambridge, MA 02139, USA.
*Corresponding author. E-mail: leyssale@mit.edu

Gamboa *et al.* Sci. Adv. 2015;1:e1501009  20 November 2015
1 of 8

![](./images/814577126815563776_1.jpg)

Fig. 1. PCG model obtained from liquid-quench MD simulation. (A) Full-size representation. (B to E) Enlargement on serpent-like GBs (B), subgrain boundaries (C), point defects (D), and amorphous domains (E). Black: bonds between two atoms that either are nonthreefold or belong to an NHR; white: other bonds; blue spheres: twofold atoms; red spheres: fourfold atoms; red lines in (B) and (C): some grain orientations; blue arrow in (C): a nonclosing Burger's circuit around a dislocation core.

Unlike most models produced so far (18-21, 27), which show compact grains with low polydispersity, our approach leads to more disordered arrangements of grains and GBs with a high variability of shapes and sizes.

The model presented in Fig. 1 seems, however, to be a good representation of a PCG in the high polycrystallinity limit [see Fig. 1 in Kurasch et al. (11) or Fig. 2 in Gómez-Navarro et al. (13)]. An advantage of the quench approach used in this work relates to the stability of the obtained GBs and point defects. Experimental observations of GBs (8-11) only revealed the presence of pentagons and heptagons. Other nonhexagonal rings (NHRs) such as tetragons, octagons, or nonagons, which are sometimes observed in graphene systems, are generally assumed to result from prolonged electron irradiation (28) or chemical treatment (oxidation/reduction) (13). The ratio

$$
f=\frac{n_{m<5}+n_{m>7}}{n_{5}+n_{7}}
$$

where $n_{i}$ is the number of $i$ member rings, can thus be considered as a reasonable indicator of the realism of the GBs present in the models (the lower the ratio is, the more realistic is the model). For the model of Fig. 1, $f=$ 0.01, which is around 20 times lower than for the models proposed by Kotakoski and Meyer (18) (f=0.22). Its average grain size is estimated to be in the range 3.3 to 4.2 nm (for the methodology of grain size determination, see Materials and Methods).

In Fig. 2, we show the evolution of the PCG model occurring during a 25-ns thermal annealing at 4000 K. A clear evolution toward the structure of graphene is observed with a significant decrease in potential energy (around 30 meV per atom) (Fig. 2D), concomitant with an increase in grain size (up to 5.1 to 8.3 nm) (Fig. 2E). Graphenization is induced by the transformation of pentagons and heptagons (Fig. 2G) into hexagons (Fig. 2F) through well-known Stone-Wales bond rotations. It results in the disappearance of the smallest grains (red ellipse in Fig. 2, A to C). The process is extremely quick in the initial 5 ns of annealing and then slows down. Obtained data for potential energy, grain size, and ring analysis seem to reach a plateau after 20 ns of simulation. The connectivity of NHRs is a relevant indicator of the structure of PCGs: NHRs are connected to two other NHRs in GBs—to one NHR at GB ends or at dislocation cores and to three or more NHRs at GB junctions or in the core of large disordered areas. The proportion of NHRs connected to two NHRs (Fig. 2H) gradually increases during thermal annealing from ≈58 to ≈65%, indicating an increase in the proportion of continuous GBs with respect to point defects and subgrain boundaries. During the initial 5 ns of annealing, the fractions of NHR having one and three or more first neighbors significantly increase and decrease, respectively, from a common coincidental initial value of 18%. This is consistent with the quick disappearance of large point defects and the rise of isolated pentagon-heptagon pairs observed in the models (compare Fig. 2, A and B, to Fig. 1). In the remaining heat treatment simulation, the fraction of NHRs having a unique NHR neighbor seems to slowly decrease from ≈34% after 5 ns of annealing to ≈25% after 25 ns. This is consistent with the early stages of the polygonization process: the migration of randomly located dislocation cores (blue rectangles in Fig. 2, A and B) toward well-defined, rather continuous, GBs (green rectangles in Fig. 2C).

We now describe the mechanical properties of the PCG model at different levels of the graphenization process. Typical stress-strain curves obtained from uniaxial tensile test simulations before and after 25 ns of annealing are compared to those of pristine graphene in Fig. 3A. All of the data presented here were obtained using the recently introduced screened environment-dependent (SED)-REBO potential (29). The latter has been specifically developed to overcome well-known cutoff artifacts in fracture simulations of carbon systems using REBO

![](./images/814577126815563776_2.jpg)

Fig. 2. Graphenization of the PCG model. (A to C) Snapshots of the system after thermal annealing at 4000 K for (A) 2.5 ns, (B) 5 ns, and (C) 25 ns. (D to I) Evolutions (with annealing time) of (D) potential energy per atom, (E) average grain size, (F) fractions of rings that are hexagons, (G) fractions of rings that are pentagons and heptagons, and (H and I) the connectivity (in terms of edge-sharing polygons) of NHRs: (H) fractions of NHRs having two NHR neighbors and (I) fractions of NHRs having one NHR neighbor and three or more NHR neighbors . The color code for (A) to (C) is the same as in Fig. 1.

potentials (30, 31). In SED-REBO formalism, first-neighbor interactions extend up to 0.33 nm (perfectly fitting the density functional theory isotropic expansion-compression curves of graphene and diamond), instead of 0.2 nm with conventional REBO potentials (either with a hard cutoff or smoothly switched from 0.17 nm).

The failure strengths of pristine graphene are 109 and 129 GPa for the AC and ZZ directions, respectively, which correspond to failure strains of 17 and 24%. Young's modulus, obtained in the linear part of the curves, has values of 875 GPa (AC direction) and 798 GPa (ZZ direction). The two PCG models show a brittle behavior, similar to the one observed for graphene. However, as reported in an earlier work (19), the linear elastic behavior is only obtained after a few percentages of deformation, during which defect-induced out-of-plane wrinkles get flattened. Both failure strength and strain are reduced by around 50% in the PCG models with respect to graphene. Young's modulus (around 800 GPa) remains close to that of pristine graphene. Another interesting observation from Fig. 3A is that both failure stress and strain seem to be reduced when going from quenched PCG models to graphenized PCG models.

In Fig. 3 (B to E), we show the evolutions of failure strain $(\varepsilon^{*})$, failure stress $(\sigma^{*})$, fracture energy $[E=\int_{0}^{\varepsilon^{*}} \sigma(\varepsilon) d \varepsilon]$, and Young's modulus $(Y)$ as a function of annealing time for tensile tests performed along the horizontal (x) and vertical (y) directions. Despite considerable fluctuations, significant reductions of $\varepsilon^{*}, \sigma^{*}$, and $E$ can be observed along the graphenization pathway, whereas stiffness $(Y)$ conversely increases (some abnormally high values of Y obtained for some models are discussed in fig. S1). One can more precisely see that all of these properties evolve rather slowly up to 15 ns of annealing, namely, when the largest structural changes occur. Then, quick changes in properties with annealing time are observed. Meanwhile, only minor structural rearrangements—mainly reordering of GBs, as monitored by the increase in the number of NHRs with two NHR neighbors—occur in the system.

While the increase in Y with annealing time was expected, the observed significant strength reduction (including decreases in failure stress, failure strain, and fracture energy) is rather counterintuitive, although some controversy regarding the existence, or not, of a pseudo-Hall-Petch effect in PCGs has been reported in the recent literature (20,22). In Fig. 4, we investigate the microscopic origin of such a strength reduction by closely looking at the fracture initiation process for two of the above-presented systems: a strong and a weak PCG model obtained after 5 and 25 ns of annealing, respectively.

Snapshots of the two systems in the very few steps preceding a dramatic fracture (corresponding to 11.15 and 7.90% strain for the systems annealed for 5 and 25 ns, respectively) are shown in Fig. 4 (A and B). In both cases, as in previous studies (16, 17, 19, 20, 22), fracture propagates from a broken $sp^{2}$ bond shared by a hexagon and a heptagon (this kind of bond having longer initial lengths than other configurations), either at a GB end (Fig. 4C) or at an isolated pentagon-heptagon pair

![](./images/814577126815563776_3.jpg)

Fig. 3. Tensile properties along the graphenization path. (A) Typical tensile curves for PCG before (blue) and after (red) 25 ns of thermal annealing at 4000 K [data for pristine graphene along the AC (yellow) and ZZ (green) directions are given for comparison]. (B to E) Evolutions (with annealing time) of (B) failure strain (ε*), (C) failure stress (σ*), (D) fracture energy (E), and (E) Young's modulus (Y). Blue circles: tensile tests along the horizontal (x) direction; red squares: tensile tests along the vertical (y) direction.

(Fig. 4D). Note that ≈0.1% of nonthreefold atoms are never involved in the fracture initiation process or in the early steps of its propagation. We thus conclude that these defects have very limited effect on the material's failure properties. Looking closely at Fig. 4A, we see that fracture does not propagate from the first broken bond. Instead, up to 19 bonds get broken at apparently randomly located defects (red arrows in Fig. 4A and blue curve in Fig. 4F) before the sheet actually fails. The first of these (single bond or few bonds) nanocracks (an opened dislocation core) occurs at a strain slightly below 8%, whereas fracture only takes place at around 11.3% strain (Fig. 4F). Most of these nanocracks also take place at bonds shared by hexagons and heptagons. We did not observe any clear correlation between the order at which these bonds fail and their initial elongations (fig. S2), although the first one to fail was also the one with the highest elongation. The initial length of the bonds is not the only criterion that can influence the order of their failures. Other criteria certainly include their orientations with respect to tension direction, local environments, and initial out-of-plane orientations.

The situation is different for the system annealed for 25 ns (Fig. 4B). Although the first nanocrack occurs at almost the same strain level as for the system annealed for 5 ns (7.7%), it is quickly followed by a catastrophic fracture at around 8.4% strain, after only three to four nanocrack events (Fig. 4F). Thus, there is strong evidence that the possibility of having such nonpropagating PFCs in the most disordered graphenes can significantly enhance their mechanical properties. A clear indication of this is provided in Fig. 4G, where the evolutions of the average bond distances between atoms belonging to hexagons only (H-H) and/or defects (H-D/D-D) are plotted. As can be seen, the average bond lengths evolve almost equally with applied strain in the two systems up to fracture. The important difference is that fracture is significantly retarded in the most disordered system, leading to significantly larger average bond elongations when it eventually occurs. The change in slope observed between 8 and 11% strain for H-D bonds in the system annealed for 5 ns arises from the fact that 19 D-D bonds in this strain interval get broken, thus releasing some stress or strain on the neighboring H-D bonds.

The formation of PFCs observed in this work cannot be considered as a conventional plasticity effect because there is no defect mobility involved here and the fracture profiles remain entirely brittle. Furthermore, we have performed an unloading simulation during which the system of Fig. 4A was brought back to mechanical equilibrium by decreasing the applied strain at the same rate as in loading simulations. All but one of the PFCs disappeared during this simulation, reforming the broken bonds with relatively little hysteresis effect (fig. S3). PFC formation is thus a reversible pseudoelastic effect.

In Fig. 5A, we plot the evolution of the number of PFCs in tensile tests along x and y as a function of annealing time. A clear decreasing trend is observed, indicating that the probability of forming these stable nanocracks decreases with increasing degree of graphenization. Meanwhile, both the average strain $\varepsilon^{1}=0.073\pm0.007$ and the average stress $\sigma^{1}=43.41\pm6.14$ GPa at which the first nanocrack occurs do not show any particular evolutions with annealing time, even though large fluctuations are observed from one model to another (fig. S4). These data can be considered as hypothetical lower bounds of the fracture strain and stress in the limit of a perfectly brittle system in which the first broken bond immediately leads to fracture. Evolutions of the average fracture strain, stress, and energy with the number of PFCs are given in Fig. 5 (B, C, and D, respectively). Despite large error bars, the correlation between the material's resistance to fracture and the number of PFCs is evident. The possibility of forming stable PFCs allows extending the elasticity limit up to around 50% for both strain and stress, as shown in fig. S5.

![](./images/814577126815563776_4.jpg)

Fig. 4. Prefracture states of PCG annealed for 5 and 25 ns (from tensile tests along y). (A and B) Snapshots of the systems close to failure (A: 5 ns at $\varepsilon = 11.15\%$; B: 25 ns at $\varepsilon = 7.90\%$) exhibiting numerous nonpropagating nanocracks in (A), as indicated by red arrows. (C to E) Enlargements of the boxed areas in (A) and (B) color-coded according to bond distance (blue, <0.15 nm; cyan, 0.15 to 0.1533 nm; green, 0.1533 to 0.1567 nm; yellow, 0.1567 to 0.16 nm; brown, 0.16 to 0.1675 nm; orange, 0.1675 to 0.175 nm; red >0.175 nm). (F) Evolution (with strain) of the number of broken $sp^2$ bonds (nanocracks). (G) Evolution (with strain) of the average length of $sp^2$ bonds (H, atoms forming the bonds in a hexagonal environment; D, atoms forming the bonds in a defective environment). Fracture in the two systems will eventually propagate from the nanocracks shown in (C) and (D).

![](./images/814577126815563776_5.jpg)

Fig. 5. Effects of the number of PFCs on fracture properties. (A) Number of PFCs as a function of annealing time. (B to D) Evolutions (with the number of PFCs) of (B) fracture strain, (C) fracture stress, and (D) fracture energy.

We performed two additional series of tensile simulations on the systems annealed for 5 and 25 ns (still along y) to check the dependence of our findings on the used strain rate and interatomic potential. In the first series, the tests were repeated at a five-times-slower strain rate (namely, $2 \times 10^8\ \text{s}^{-1}$ instead of $10^9\ \text{s}^{-1}$). In the second series, we used the second-generation REBO (instead of SED-REBO) potential, with a hard cutoff set at 0.2 nm, as in most simulation work published so far (12, 16–20, 22, 27). As shown in table S1, all fracture properties obtained with the slower strain rate (including $\varepsilon^*$, $\sigma^*$, number of PFCs, $\varepsilon^1$, and $\sigma^1$ are within the error bars of those obtained at the higher strain rate, indicating that strain rate effects are very limited. However, properties obtained with the REBO potential and the hard cutoff (table S1) show a 30 to 50% reduction with respect to those obtained with the more accurate SED-REBO potential. The formation of PFCs in the latter simulations is considerably reduced and so are their effects on the fracture properties.

Having evidenced the correlation between the number of PFCs and the fracture properties, we now try to understand why single-bond cracks seem to have a high probability of inducing fracture in the most ordered—not in the most disordered—graphene sheets. In Fig. 6, we look at fracture initiation in the two systems described in Fig. 4. We start with the

![](./images/814577126815563776_6.jpg)

resilient system corresponding to 5 ns of annealing (Fig. 6A). A PFC first forms at the bond between red atoms (Fig. 6C) at a strain of around 0.089 when the latter has an average length of around 0.177 nm; this exactly corresponds to the average distance at which PFCs are formed (0.175 ± 0.005 nm as averaged over the 19 PFCs obtained in this system). This PFC immediately induces some strain (load transfer) on a neighboring bond (blue atoms) whose length increases from 0.156 to ≈0.166 nm (part of the load is also transferred to the bond between pink atoms, but to a lesser extent). Then, all vertically aligned bonds undergo a con- stant progressive elongation with applied strain. At around 11.15% strain, the bond between blue atoms reaches a length of ≈0.175 nm (averaging over fluctuations) and eventually fails (Fig. 6D). Again, this promotes an increase in bond lengths on the neighboring bonds (mainly between pink and green atoms), which eventually fail after an addi- tional 0.25% tension during which their lengths get close to the bond rupture threshold. The rupture of these bonds immediately leads to the breakdown of the bond between orange atoms, even though the bond length (0.16 nm) is relatively far from the threshold, and initiates the catastrophic fracture of the sheet. Overall, ≈2.5% extra strain was applied between the appearance of the PFC (Fig. 6C) and the failure of the sheet (Fig. 6, E and F). A qualitatively similar behavior is observed for the system presented in Fig. 6B: (i) formation of a PFC at the bond of red atoms (Fig. 6G); (ii) delayed rupture of the bonds of neighboring blue atoms (Fig. 6H) then green atoms (Fig. 6I); and (iii) immediate rupture of the bond of pink atoms followed by the catastrophic fracture (Fig. 6J). However, a major difference from the case of Fig. 6A is that, here, all steps of the process take place within a narrow strain interval of only ≈0.6%, which is too short to allow for the formation of many PFCs. The reason for this is that, unlike in the resilient system, we can see in Fig. 6B that every time a bond breaks, a neighboring bond is almost immediately elongated to the rupture threshold.

## DISCUSSION
Using MD simulations and the SED-REBO potential, we have studied the fracture properties of a PCG model prepared by a liquid-quench method and their evolutions along a 25-ns thermal annealing simula- tion at an elevated temperature. We have shown that, counterintuitive- ly, all fracture properties reduce while the model progressively evolves toward graphene. An explanation for the high resilience of the less annealed models is the formation of numerous reversible PFCs. The reversible PFCs, acting as mechanical fuses, significantly retard fracture or, in other words, increase the limit of elasticity (fig. S5). Our results also suggest that graphenization strengthens the local character of load transfer after a bond rupture, progressively suppressing the formation of stable cracks and hence reducing the overall strength of the system. Although the usual goal of the synthesis of graphene and other two- dimensional covalent materials is increase in grain size, the present work suggests that working on GBs, and especially promoting disorder, might be an additional direction to look at to improve mechanical strength.

## MATERIALS AND METHODS
### Preparation of the models
Atomistic models of PCG were prepared as follows. First, an initial configuration was generated by random insertions of 10,032 atoms (with

a nonoverlap condition) in a periodic orthorhombic box of roughly 16 nm $(x) \times 16$ nm $(y) \times 20$ nm $(z)$, corresponding to a perfect graphene sheet on the $xy$ plane. This system was quickly equilibrated in the liquid phase by MD simulations at 8000 K with the second-generation REBO potential (30) and then quenched to room temperature with a nonuniform temperature ramp having its minimum rate (0.5 K/ps) around the melting point of carbon (32). During the quench, an external potential

$$
V_{\text{ext}}(\mathrm{eV})=\cos \left(\frac{2 \pi}{0.335} z-\pi\right)+1 \text { for }|z|<\frac{0.335}{2} \mathrm{~nm}
$$

ensured that the system regrouped into a unique planar PCG sheet centered on $z=0$. This structure was then simulated for 25 ns at 4000 K, and configurations were stored and quickly cooled to room temperature every 2.5 ns. During annealing, up to 31 atoms evaporated from the sheet. They were removed from the system before property calculations. The 11 resulting structures (10 annealed and 1 raw) were then relaxed at room temperature and zero pressure for 750 ps with the SED-REBO potential (29).

## Structural analysis
Standard structural analysis methods were used to determine coordination and ring statistics. The main difficulty here was providing some estimates of the average size of hexagonal graphene domains. Two methods were used for that aim. In the first approach, we started by computing the average distance $d$ between hexagonal atoms and their closest defect atom. The relationship $D=6.1 d-0.14$ (determined on ideal graphene flakes, assuming that edge atoms act as defects) allows the determination of the average diameter $D$ of circular graphene domains contained in the model. This method, sharing the philosophy of the one proposed by Gelb and Gubbins (33) to determine pore size distributions, provides a lower bound for the average grain size. The second method is based on a circular core shell model, where graphene grains of diameter $D$ constitute the core and the shell of thickness $l$ is a GB shared by two grains (34). In such a system, the surface fraction of hexagonal graphene reads

$$
\phi_{\mathrm{G}}=\frac{D^{2}}{D^{2}+2 I D+2 l^{2}}
$$

Assuming that $l$ is given by the average diameter of a ring, we end up with $l=0.253$ nm. An estimation of the average hexagonal grain size $D$ in PCGs can thus be obtained from the fraction of hexagonal rings, equal to $\phi_{\mathrm{G}}$, if we assume that, on average, hexagonal rings and NHRs have the same area [this should hold because the ratio of (smaller) pentagons to (larger) heptagons is always close to unity]. This approach considers monodisperse circular rings, two assumptions maximizing the grain size for a given $\phi_{\mathrm{G}}$. For this reason, the obtained grain sizes are considered to constitute upper bounds. However, the presence of discontinuities in GBs has the opposite effect (that is, they tend to underestimate the apparent grain size). Nevertheless, Farbos et al. (34) showed that the grain sizes obtained with this second approach are very close to the coherence length $L_{\mathrm{a}}$ derived from diffraction calculations.

## Fracture simulations
Fracture properties were obtained from uniaxial tensile test simulations performed using MD simulations and the SED-REBO potential (29). A deformation was applied to one dimension ($x$ or $y$) at a constant engineering strain rate of $1 \mathrm{~ns}^{-1}$. Poisson effects in the other plane direction were accounted for by fixing the corresponding stress element to zero, using a Berendsen barostat operated with a coupling parameter of $10^{4} \mathrm{GPa}^{-1} \cdot \mathrm{fs}^{-1}$ and a Berendsen thermostat operated at a temperature of 300 K with a 50-fs time constant (35). Equations of motion were integrated with the velocity-Verlet scheme using a 0.5-fs time step. The average properties and standard deviations (error bars) reported in Results were obtained from five simulations with different sets of initial velocities, all corresponding to a Maxwell-Boltzmann distribution of 300 K. Two separate sets of data were presented for tensions along $x$ and $y$; because of the finite size of the polycrystalline models, the properties were not expected to be entirely isotropic. Stress-strain curves were then analyzed after the conversion of engineering strain into true strain to determine elastic and fracture properties. Obtaining these properties was essentially trivial. The only subtlety here was related to the determination of Young's modulus $(Y)$ because of well-known nonlinearity at low strains due to both out-of-plane ripples at mechanical equilibrium (19) and the interatomic potential used (36). In this work, $Y$ was determined by fitting the stress-strain curves in the 3% strain interval showing the highest slope. In some cases, we observed that this linear domain takes place at large strains (up to 5 to 8%, as shown in fig. S1). This can lead to relatively large errors because at such high strains, the definition of true strain becomes significantly dependent on the definition of the origin of strain, which is a particularly sensitive issue in rippled graphene systems. Finally, the interlayer spacing of graphite (0.335 nm) was used as graphene thickness to express stress in pressure units and fracture energy as volumetric energy. Although some controversies regarding this assumption exist, recent work based on the analysis of electron density in graphene and graphite (37) confirms that it is a reasonable estimate.

## SUPPLEMENTARY MATERIALS
Supplementary material for this article is available at http://advances.sciencemag.org/cgi/content/full/1/10/e1501009/DC1
Fig. S1. Determination of Young's modulus.
Fig. S2. Effects of initial bond length on the appearance of PFCs.
Fig. S3. Reversibility of PFCs.
Fig. S4. Formation of the first PFC.
Fig. S5. Individual fracture stress versus fracture strain plots.
Table S1. Effects of strain rate and interatomic potential on fracture properties.

## REFERENCES AND NOTES
1. K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, A. A. Firsov, Electric field effect in atomically thin carbon films. Science 306, 666-669 (2004).
2. F. Xia, D. B. Farmer, Y.-M. Lin, P. Avouris, Graphene field-effect transistors with high on/off current ratio and large transport band gap at room temperature. Nano Lett. 10, 715-718 (2010).
3. J. S. Bunch, A. M. van der Zande, S. S. Verbridge, I. W. Frank, D. M. Tanenbaum, J. M. Parpia, H. G. Craighead, P. L. McEuen, Electromechanical resonators from graphene sheets. Science 315, 490-493 (2007).
4. G. Eda, G. Fanchini, M. Chhowalla, Large-area ultrathin films of reduced graphene oxide as a transparent and flexible electronic material. Nat. Nanotechnol. 3, 270-274 (2008).
5. X. Li, W. Cai, J. An, S. Kim, J. Nah, D. Yang, R. Piner, A. Velamakanni, I. Jung, E. Tutuc, S. K. Banerjee, L. Colombo, R. S. Ruoff, Large-area synthesis of high-quality and uniform graphene films on copper foils. Science 324, 1312-1314 (2009).
6. S. Stankovich, D. A. Dikin, G. H. B. Dommett, K. M. Kohlhaas, E. J. Zimney, E. A. Stach, R. D. Piner, S. T. Nguyen, R. S. Ruoff, Graphene-based composite materials. Nature 442, 282-286 (2006).
7. S. Park, R. S. Ruoff, Chemical methods for the production of graphenes. Nat. Nanotechnol. 4, 217-224 (2009).
8. H. I. Rasool, C. Ophus, W. S. Klug, A. Zettl, J. K. Gimzewski, Measurement of the intrinsic strength of crystalline and polycrystalline graphene. Nat. Commun. 4, 2811 (2013).

9. P. Y. Huang, C. S. Ruiz-Vargas, A. M. van der Zande, W. S. Whitney, M. P. Levendorf, J. W. Kevek, S. Garg, J. S. Alden, C. J. Hustedt, Y. Zhu, J. Park, P. L. McEuen, D. A. Muller, Grains and grain boundaries in single-layer graphene atomic patchwork quilts. *Nature* **469**, 389-392 (2011).

10. K. Kim, Z. Lee, W. Regan, C. Kisielowski, M. F. Crommie, A. Zettl, Grain boundary mapping in polycrystalline graphene. *ACS Nano* **5**, 2142-2146 (2011).

11. S. Kurasch, J. Kotakoski, O. Lehtinen, V. Skákalová, J. Smet, C. E. Krill III, A. V. Krasheninnikov, U. Kaiser, Atom-by-atom observation of grain boundary migration in graphene. *Nano Lett.* **12**, 3168-3173 (2012).

12. H. I. Rasool, C. Ophus, Z. Zhang, M. F. Crommie, B. I. Yakobson, A. Zettl, Conserved atomic bonding sequences and strain organization of graphene grain boundaries. *Nano Lett.* **14**, 7057-7063 (2014).

13. C. Gómez-Navarro, J. C. Meyer, R. S. Sundaram, A. Chuvilin, S. Kurasch, M. Burghard, K. Kern, U. Kaiser, Atomic structure of reduced graphene oxide. *Nano Lett.* **10**, 1144-1148 (2010).

14. G.-H. Lee, R. C. Cooper, S. J. An, S. Lee, A. van der Zande, N. Petrone, A. G. Hammerberg, C. Lee, B. Crawford, W. Oliver, J. W. Kysar, J. Hone, High-strength chemical-vapor-deposited graphene and grain boundaries. *Science* **340**, 1073-1076 (2013).

15. C. Lee, X. Wei, J. W. Kysar, J. Hone, Measurement of the elastic properties and intrinsic strength of monolayer graphene. *Science* **321**, 385-388 (2008).

16. R. Grantab, V. B. Shenoy, R. S. Ruoff, Anomalous strength characteristics of tilt grain boundaries in graphene. *Science* **330**, 946-948 (2010).

17. Y. Wei, J. Wu, H. Yin, X. Shi, R. Yang, M. Dresselhaus, The nature of strength enhancement and weakening by pentagon-heptagon defects in graphene. *Nat. Mater.* **11**, 759-763 (2012).

18. J. Kotakoski, J. C. Meyer, Mechanical properties of polycrystalline graphene based on a realistic atomistic model. *Phys. Rev. B* **85**, 195447 (2012).

19. T. Zhang, X. Li, S. Kadkhodaei, H. Gao, Flaw insensitive fracture in nanocrystalline graphene. *Nano Lett.* **12**, 4605-4610 (2012).

20. Z. D. Sha, S. S. Quek, Q. X. Pei, Z. S. Liu, T. J. Wang, V. B. Shenoy, Y. W. Zhang, Inverse pseudo Hall-Petch relation in polycrystalline graphene. *Sci. Rep.* **4**, 5991 (2014).

21. B. Mortazavi, G. Cuniberti, Atomistic modeling of mechanical properties of polycrystalline graphene. *Nanotechnology* **25**, 215704 (2014).

22. Z. Song, V. L. Artyukhov, B. I. Yakobson, Z. Xu, Pseudo Hall-Petch strength reduction in polycrystalline graphene. *Nano Lett.* **13**, 1829-1833 (2013).

23. O. Cretu, A. V. Krasheninnikov, J. A. Rodríguez-Manzo, L. Sun, R. M. Nieminen, F. Banhart, Migration and localization of metal atoms on strained graphene. *Phys. Rev. Lett.* **105**, 196102 (2010).

24. F. Banhart, J. Kotakoski, A. V. Krasheninnikov, Structural defects in graphene. *ACS Nano* **5**, 26-41 (2011).

25. J.-M. Leyssale, G. L. Vignoles, A large-scale molecular dynamics study of the divacancy defect in graphene. *J. Phys. Chem. C* **118**, 8200-8216 (2014).

26. J. Kotakoski, A. V. Krasheninnikov, K. Nordlund, Energetics, structure, and long-range interaction of vacancy-type defects in carbon nanotubes. *Phys. Rev. B* **74**, 245420 (2006).

27. Z. D. Sha, Q. X. Pei, Z. S. Liu, V. B. Shenoy, Y. W. Zhang, Is the failure of large-area polycrystalline graphene notch sensitive or insensitive? *Carbon* **72**, 200-206 (2014).

28. A. W. Robertson, C. S. Allen, Y. A. Wu, K. He, J. Olivier, J. Neethling, A. I. Kirkland, J. H. Warner, Spatial control of defect creation in graphene at the nanoscale. *Nat. Commun.* **3**, 1144 (2012).

29. R. Perriot, X. Gu, Y. Lin, V. V. Zhakhovsky, I. I. Oleynik, Screened environment-dependent reactive empirical bond-order potential for atomistic simulations of carbon materials. *Phys. Rev. B* **88**, 064101 (2013).

30. D. W. Brenner, O. A. Shenderova, J. A. Harrison, S. J. Stuart, B. Ni, S. B. Sinnott, A second-generation reactive empirical bond order (REBO) potential energy expression for hydrocarbons. *J. Phys. Condens. Matter* **14**, 783-802 (2002).

31. S. J. Stuart, A. B. Tutein, J. A. Harrison, A reactive potential for hydrocarbons with intermolecular interactions. *J. Chem. Phys.* **112**, 6472-6486 (2000).

32. B. Farbos, P. Weisbecker, H. E. Fischer, J.-P. Da Costa, M. Lalanne, G. Chollon, C. Germain, G. L. Vignoles, J.-M. Leyssale, Nanoscale structure and texture of highly anisotropic pyrocarbons revisited with transmission electron microscopy, image processing, neutron diffraction and atomistic modeling. *Carbon* **80**, 472-489 (2014).

33. L. D. Gelb, K. E. Gubbins, Pore size distributions in porous glasses: A computer simulation study. *Langmuir* **15**, 305-308 (1999).

34. B. Farbos, J.-P. Da Costa, G. L. Vignoles, J.-M. Leyssale, Nanoscale elasticity of highly anisotropic pyrocarbons. *Carbon* **94**, 285-294 (2015).

35. H. J. C. Berendsen, J. P. M. Postma, W. F. van Gunsteren, A. DiNola, J. R. Haak, Molecular dynamics with coupling to an external bath. *J. Chem. Phys.* **81**, 3684-3690 (1984).

36. A. Gamboa, G. L. Vignoles, J.-M. Leyssale, On the prediction of graphene's elastic properties with reactive empirical bond order potentials. *Carbon* **89**, 176-187 (2015).

37. P. Wagner, V. V. Ivanovskaya, M. J. Rayson, P. R. Briddon, C. P. Ewels, Mechanical properties of nanosheets and nanotubes investigated using a new geometry independent volume definition. *J. Phys. Condens. Matter* **25**, 155302 (2013).

**Acknowledgments:** J.-M.L. acknowledges B. Coasne for fruitful discussions. **Funding:** This work was supported by Agence Nationale de la Recherche through the PyroMaN project (contract ANR-2010-BLAN-929) and by Institut Carnot "Materials and Systems Institute of Bordeaux." J.-M.L.'s stay at the Massachusetts Institute of Technology was supported by the French ICoME2 LabEx (grant ANR-11-LABX-0053). Part of the simulations was achieved using the computer facilities at Mésocentre de Calcul Intensif Aquitain. **Author contributions:** J.-M.L. and G.L.V. designed the study. A.G., B.F., P.A., and J.-M.L. developed and optimized the simulation codes. A.G., B.F., and J.-M.L. performed the simulations. A.G., B.F., G.L.V., and J.-M.L. analyzed the results. J.-M.L. wrote the paper. **Competing interests:** The authors declare that they have no competing interests. **Data and materials availability:** All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors, J.-M.L.

Submitted 29 July 2015
Accepted 16 October 2015
Published 20 November 2015
10.1126/sciadv.1501009

**Citation:** A. Gamboa, B. Farbos, P. Aurel, G. L. Vignoles, J.-M. Leyssale, Mechanism of strength reduction along the graphenization pathway. *Sci. Adv.* **1**, e1501009 (2015).

![](./images/814577126815563776_7.jpg)

# Mechanism of strength reduction along the graphenization pathway
Antonio Gamboa, Baptiste Farbos, Philippe Aurel, Gérard L.
Vignoles and Jean-Marc Leyssale (November 20, 2015)
Sci Adv 2015, 1:.
doi: 10.1126/sciadv.1501009

This article is publisher under a Creative Commons license. The specific license under which this article is published is noted on the first page.

For articles published under CC BY licenses, you may freely distribute, adapt, or reuse the article, including for commercial purposes, provided you give proper attribution.

For articles published under CC BY-NC licenses, you may distribute, adapt, or reuse the article for non-commerical purposes. Commercial use requires prior permission from the American Association for the Advancement of Science (AAAS). You may request permission by clicking here.

The following resources related to this article are available online at
http://advances.sciencemag.org. (This information is current as of November 1, 2016):

Updated information and services, including high-resolution figures, can be found in the online version of this article at:
http://advances.sciencemag.org/content/1/10/e1501009.full

Supporting Online Material can be found at:
http://advances.sciencemag.org/content/suppl/2015/11/17/1.10.e1501009.DC1

This article cites 37 articles, 6 of which you can access for free at:
http://advances.sciencemag.org/content/1/10/e1501009#BIBL

---

Science Advances (ISSN 2375-2548) publishes new articles weekly. The journal is published by the American Association for the Advancement of Science (AAAS), 1200 New York Avenue NW, Washington, DC 20005. Copyright is held by the Authors unless stated otherwise. AAAS is the exclusive licensee. The title Science Advances is a registered trademark of AAAS