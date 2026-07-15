# Lead and selenite adsorption at water–goethite interfaces from first principles

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2017 J. Phys.: Condens. Matter 29 365101

(http://iopscience.iop.org/0953-8984/29/36/365101)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 132.174.250.220
This content was downloaded on 03/09/2017 at 11:35

Please note that [terms and conditions apply]().

You may also be interested in:

[Predicting the acidity constant of a goethite hydroxyl group from first principles]()
Kevin Leung and Louise J Criscenti

[The electric double layer at a rutile TiO2 water interface modelled using density functional theory based molecular dynamics simulation]()
J Cheng and M Sprik

[Hematite(001)-liquid water interface from hybrid density functional-based molecular dynamics]()
Guido Falk von Rudorff, Rasmus Jakobsen, Kevin M Rosso et al.

[Applications of large-scale density functional theory in biology]()
Daniel J Cole and Nicholas D M Hine

[Challenges in modelling nanoparticles for drug delivery]()
Amanda S Barnard

[Polarity of oxide surfaces and nanostructures]()
Jacek Goniakowski, Fabio Finocchi and Claudine Noguera

[Going clean: structure and dynamics of peptides in the gas phase and paths to solvation]()
Carsten Baldauf and Mariana Rossi

[The amorphous silica–liquid water interface studied by ab initio molecular dynamics (AIMD): local organization in global disorder]()
Álvaro Cimas, Frederik Tielens, Marialore Sulpizi et al.

# Lead and selenite adsorption at water–goethite interfaces from first principles

Kevin Leung¹ and Louise J Criscenti

Sandia National Laboratories, MS 1415, & 0754, Albuquerque, NM 87185 United States of America

E-mail: kleung@sandia.gov

Received 25 April 2017, revised 16 June 2017
Accepted for publication 7 July 2017
Published 4 August 2017

![](./images/813120490167074817_1.jpg)

## Abstract
The complexation of toxic and/or radioactive ions on to mineral surfaces is an important topic in geochemistry. We apply periodic-boundary-conditions density functional theory (DFT) molecular dynamics simulations to examine the coordination of Pb(II), $SeO_3^{2-}$, and their contact ion pairs to goethite (1 0 1) and (2 1 0) surfaces. The multitude of Pb(II) adsorption sites and possibility of Pb(II)-induced FeOH deprotonation make this a complex problem. At surface sites where Pb(II) is coordinated to three FeO and/or FeOH groups, and with judicious choices of FeOH surface group protonation states, the predicted Fe–Pb distances are in good agreement with EXAFS measurements. Trajectories where Pb(II) is in part coordinated to only two surface Fe–O groups exhibit larger fluctuations in Pb–O distances. Pb(II)/$SeO_3^{2-}$ contact ion pairs are at least metastable on goethite (2 1 0) surfaces if the $SeO_3^{2-}$ has a monodentate Se–O–Fe bond. Our DFT-based molecular dynamics calculations are a prerequisite for calculations of finite temperature equilibrium binding constants of Pb(II) and Pb(II)/$SeO_3^{2-}$ ion pairs to goethite adsorption sites.

Keywords: density functional theory molecular dynamics, water-material interface, ion Adsorption, deprotonation

(Some figures may appear in colour only in the online journal)

## 1. Introduction

The complexation of transition metal ions and oxyanions, and their contact ion pairs, to iron oxyhydroxides (FeOOH) has broad implications for the retention and reactions of toxic and/or radioactive species in the environment. At FeOOH-water interfaces, the adsorption of Pb(II) and $SeO_3^{2-}$, two ions which are the focus of this study, have been examined through extended x-ray absorption fine structure (EXAFS) measurements [1–4] and bulk adsorption (‘titration’) measurements [5, 6]. In this work we apply electronic structure techniques to predict the adsorption properties of $Pb^{2+}$ and the $Pb^{2+}$/$SeO_3^{2-}$ contact ion pair at different binding sites on the (1 0 1) and (2 1 0) surface facets of goethite ($\alpha$-FeOOH, the most prominent form of FeOOH). Here the unit cell and surface designation refer to the *Pnma* space group.

Our work expands on previous modeling studies on goethite surfaces. Surface complexation models (SCM), which do not explicitly include interatomic interactions, have been used to fit the bulk adsorption data for a single adsorbed cation, often incorporating EXAFS results to narrow the list of potential surface complexes to be considered in the SCM [6–22]. Molecular simulation studies, using classical force fields that do not explicitly apply electronic structure methods, have also been applied to predict ion adsorption in single solute systems [23–27]. Fewer studies have attempted to model more complex systems involving multiple oxyanions [7, 28–30], oxycations [30], or a combination of both [2, 3, 31–33].

Electronic structure methods, like density functional theory (DFT), have increasingly been applied to model the coordination of transition and heavy metal ions and oxyanions to mineral surfaces. Thus both static cluster- and slab-based DFT calculations have been applied to obtain improved understanding of which surface sites are involved in ion adsorption [34–44, 45]. One driving force for using DFT is that it is challenging to derive

¹ Author to whom any correspondence should be addressed.

accurate molecular force fields for heavy metal ions and oxyanions. Furthermore, at oxide-water interfaces, the protonation states of surface OH groups can change as external conditions (such as pH) vary. The adsorption of cations or anions can also cause deprotonation or protonation because of the induced change in the electrostatic environment. The protonation states in turn affect the tendency of cations and anions to bind to such surface sites. DFT-based *ab initio* molecular dynamics (AIMD) simulations have been amply demonstrated to predict reliable acidity constant ($\text{p}K_a$) values of OH groups on multiple material surfaces [46–59]. $\text{p}K_a$ controls the tendency of surface FeOH groups to become protonated or deprotonated. Therefore concerted ion complexation and protonation state changes should be accurately captured using AIMD, provided sufficiently long simulation times and the effects of varying initial modeling conditions are carefully analyzed.

In this work, we apply DFT and AIMD methods to build on insights from the charge-distribution multi-site complexation (CD-MUSIC) model applied by Mangold [5] to describe single-solute and Pb(II)-$\text{SeO}_3^{2-}$ pairwise adsorption to goethite. This model, and the MUSIC model, will be briefly described in the Methods section. We evaluate the Pb–Fe distances and other structural signatures of Pb(II) surface complexes proposed therein, and briefly discuss the bidentate adsorption of $\text{SeO}_3^{2-}$ on goethite surfaces. Previous CD-MUSIC research [2, 3, 5, 6] has identified various edge-shared, corner-shared, and mixed Pb(II) binding sites on the (101) and (210) surfaces (figure 1), which are re-examined in this work. The (101) and (210) are among the most prominent facets exposed on goethite crystals. In the past researchers have used 90% (101) and 10% (210) facets to fit models [5]. While in recent years the (100) facet has been shown to be significant, the binding sites on (101) and (100) have been suggested to be structurally similar (see [5], page 50). This explains our focus on the (101) and (210) facets.

The CD-MUSIC predictions correspond to EXAFS experimental Fe–Pb distances of approximately 3.37 and $3.90\ \text{\AA}$ [2–4]. The Fe–Pb distances do not strongly depend on solution pH, but the $3.90\ \text{\AA}$ signature vanishes above $\text{pH}=6$ [2–4]. However, EXAFS is performed on a mixture of surfaces. Partly due to this, fitting surface complexation models to bulk adsorption edge data can be a non-unique exercise. Our atomic length-scale modeling on specific surfaces avoids this uncertainty. AIMD also includes the effects of water configurations and their fluctuations on ion adsorption. The Pb–O bond lengths are found to exhibit more fluctuations along the trajectories at some Pb(II)-binding sites than others, revealing qualitative information about the relative stability of Pb(II) at these sites. Elucidation of this real-time fluctuation and relaxation behavior is a prerequisite to future free energy calculations of ion adsorption. Adsorption free energies ultimately govern the equilibrium binding constants of ions at mineral-water interfaces [60].

## 2. Computational methods

We focus on periodically replicated simulation cells with slab geometries for goethite. The alternative is to use cluster models. As will be discussed in section 3.1, cluster models are found to yield long Fe(III)–O linkages and structural instabilities when several $\text{H}_2\text{O}$ molecules are used to terminate the edges. Slab models of FeOOH are structurally stable, but the configuration space for ion adsorption increases significantly. Furthermore, in the case of Pb(II), the predicted Pb–Fe distances, which are key markers measured in EXAFS studies, can depend on whether explicit $\text{H}_2\text{O}$ molecules are present or not, whether they are minimized at $T=0\ \text{K}$ or allowed to fluctuate in liquid-state configurations at finite temperature (see below).

DFT geometry optimization calculations and finite temperature AIMD simulations apply the Perdew–Burke–Ernezhof (PBE) functional [61], the projector-augmented wave-based Vienna atomic simulation package (VASP) [62, 63, 82], a 400 eV energy cutoff, and $\Gamma$-point sampling of the Brillouin zone. The DFT + U formalism [64, 65] with Hubbard $U$ and $J$ parameters of 4.0 eV and 1.0 eV, is applied to the $3d$ orbitals of Fe atoms, similar to AIMD simulations used previously to compute $\text{p}K_a$ [59]. DFT + U reduces the self-interaction error associated with applying the semi-local PBE functional to strongly localized $3d$ orbitals. The Fe pseudopotential used does not include pseudovalent $3p$ electrons. Since the PBE functional tends to slightly overestimate bond lengths and lattice constants, we do not focus on Pb–O and Fe–O distances obtained in EXAFS measurements. Instead we use non-bonded Pb–Fe distance as the main distance of merit.

As discussed in our previous work [59], the optimized goethite crystal unit cell size is $10.04\times3.04\times4.65\ \text{\AA}^3$. The starting surface structural motifs are guided by CD-MUSIC [5, 6] and previous molecular models [66, 67]. The periodically replicated AIMD simulation cell with (101) surface termination is constructed such that the goethite slab has a $\text{Fe}_{32}\text{O}_{72}\text{H}_{48}$ stoichiometry and an overall dimension of $11.06\times12.18\times25\ \text{\AA}^3$. Antiferromagnetic (AFM) ordering, with up/down spins residing on alternating Fe sheets along the (100) direction, is imposed. The total net spin polarization of the system is set to zero. Variations on the energies of solids as a function of AFM ordering are generally on the order of meV’s per formula unit. Classical force field-based grand canonical Monte Carlo (GCMC) simulations [68] are first applied to determine the average number of water molecules filling the gap between FeOOH (101) surfaces in the simulation cell, thus ‘pre-equilibrating’ the initial water content and configurations for AIMD simulations [59]. The SPC/E water model [69] and the ClayFF force field for FeOOH [70] are used for these purposes, with the FeOOH atoms frozen in DFT-optimized positions. $76\ \text{H}_2\text{O}$ molecules exist in the space between the goethite surfaces after GCMC simulations.

The (210) facet simulation cell has dimensions $13.89\times11.71\times27.31\ \text{\AA}^3$, and a $\text{Fe}_{48}\text{O}_{120}\text{H}_{96}$ stoichiometry not including water molecules. AFM ordering is also imposed. The amount of water present in the simulation cell (85–89 $\text{H}_2\text{O}$ molecules), and the initial aqueous configurations used in AIMD calculations, are determined in a way similar to the (101) simulation cells.

The bare goethite surface slabs, when optimized in vacuum, are initially charge-neutral and exhibit zero dipole moments in the direction perpendicular to the surfaces. After adding

![](./images/813120490167074817_2.jpg)
![](./images/813120490167074817_3.jpg)

(a)
(b)

Figure 1. Top views of $Pb^{2+}$ binding sites on the (a) (1 0 1) and (b) 210 goethite surfaces. O atoms are depicted as red spheres and Fe octahedra are grey. In (a), green, blue, and yellow Pb-sites represent edge-shared (with Pb coordinated to 2 surface O), corner-plus-edge-shared (3 surface O), and the 'trench' (3 surface O) site, respectively. In (b), the blue, pink, orange, and white Pb-sites are face-shared (3 surface O), edge-shared (2 surface O), edge-plus-corner-shared (3 surface O), and corner-shared (2 surface O), respectively. The Pb-O coordinations are also color coded: yellow, green, and blue denote face-, edge-, and at least partial corner-sharing characters. Protons are omitted in this illustration.

an adsorbed $Pb^{2+}$, $2\ H^{+}$ are removed from surface FeOH groups on the same surface to ensure electroneutrality. Our AIMD trajectories therefore reflect pH-of-zero-charge conditions. The exceptions to charge neutrality will be highlighted. In general, the energies of periodically replicated simulation cells with net charges should be corrected to account for image-image interactions. Such corrections are non-trivial for systems with interfaces. Furthermore, overall charge-neutral systems should better represent geochemical reality. For these reasons, we have focused on charge-nuetral simulation cells.

For $SeO_{3}^{2-}$ adsorption, the dianion replaces two surface $OH^{-}$ groups, and no charge compensation method is needed. The simulation cell with a $Pb^{2+}/SeO_{3}^{2-}$ contact ion pair is also charge neutral without changing protonation states. The special starting configurations needed for this ion pair will be discussed in section 3.5.

Starting from each final GCMC molecular configuration (i.e. after adding liquid water), an AIMD trajectory is generated for 10.0-20.0ps using the tritium mass for all protons, a 0.5 fs time step, and a $10^{-6}$ eV energy convergence criterion at each Born-Oppenheimer dynamics time step. The trajectories are thermostatted at $T=400$ K. The elevated temperature is needed to represent liquid water properties when the PBE functional is applied and quantum nuclear effects are neglected, which is the case herein [71]. With these settings, the drift in total energy is less than $1\ K\ ps^{-1}$.

Computational details associated with the trajectories are listed in table 1. Most of the calculations omit dispersion corrections. This enables comparison with our previous work which uses an identical computational protocol [59]. Adding the dispersion correction is known to improve AIMD predictions of liquid water structure ($g(r)$) at finite temperature [71]. But it has yet to be demonstrated that this gives universally superior predictions at water/oxide interfaces. As a spot-check, one version of this correction [72] is applied in one AIMD trajectory.

Although we do not apply the MUSIC and CD-MUSIC models in this work, they are extensively referenced for comparison purposes. Here we briefly describe these methods.

The Multi-Site Complexation (MUSIC) model adapts a bond valence model to oxide surfaces [73]. For metal (hydr) oxides, the charge of a cation in the solid is compensated by the charge of the surrounding oxygens and vice versa. The charge is distributed over the surrounding ligands, which can be expressed per bond, leading to the concept of bond valence $v$ introduced by Pauling [74]. This concept was later modified such that the actual bond valence ($s$), based on differences in metal-oxygen distances ($R$), is given by:

$$
s=\mathrm{e}^{(R-R_{o})/b}.
$$

Here $R_{o}$ is an element-specific distance and $b$ a constant [75]. The value of $R_{o}$ has been obtained by analysis of the bond valence structure of many crystals, such that the sum of the actual bond valences $\sum_{j}s_{j}$ around an oxygen based on the known distances $R$, is equal to the valence $v$ of the oxygen. The MUSIC model (1996) uses this model for bulk crystals as the basis for developing a model for oxide surface p$K_{a}$'s. The protonation affinity of an oxygen is determined from the undersaturation of the oxygen valence which is determined based on the coordination to metal cations, the $s$ associated with each bond, and the number of donating and accepting H bonds.

The charge distribution (CD) model [76] was developed to expand the MUSIC model to consider inner-sphere ion adsorption. It was noted that for oxyanions, inner sphere complexes are partially incorporated into the surface by a ligand

<table><caption>Table 1. Computational details of the trajectories and the two or three smallest average Fe–Pb distances; three are given if a third Fe–Pb distances is less than about 5 Å . For trajectories C and G, the distances represent averages over the last 8ps and 12.3 ps, respectively, because of large changes in Pb(II)-adsorption configurations in the early part of the trajectories. Other averages omit the first $\sim$1 ps of each trajectory. B–C represent the same initial Pb(II) adsorption geometry, with different water configurations.</caption>
<thead>
  <tr>
    <th>Trajectory</th>
    <th>Duration</th>
    <th>Surface</th>
    <th>$D_{\text{Fe-Pb}}$ (Å)</th>
    <th>Figure</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>A</td>
    <td>9.5</td>
    <td>(1 0 1)</td>
    <td>NA</td>
    <td>figure 4(a)</td>
  </tr>
  <tr>
    <td>B</td>
    <td>11.5</td>
    <td>(1 0 1)</td>
    <td>3.35, 3.39, 4.31</td>
    <td>Figure 4(b)</td>
  </tr>
  <tr>
    <td>C</td>
    <td>16.8</td>
    <td>(1 0 1)</td>
    <td>3.48, 3.54, 5.02</td>
    <td>Figures 4(c) and (d)</td>
  </tr>
  <tr>
    <td>D</td>
    <td>10.8</td>
    <td>(2 1 0)</td>
    <td>3.51, 3.59</td>
    <td>Figures 6(a) and (b)</td>
  </tr>
  <tr>
    <td>E</td>
    <td>10.8</td>
    <td>(2 1 0)</td>
    <td>3.34, 4.22</td>
    <td>Figures 6(c) and (d)</td>
  </tr>
  <tr>
    <td>F</td>
    <td>10.7</td>
    <td>(2 1 0)</td>
    <td>3.45, 3.75</td>
    <td>Figures 6(e) and (f)</td>
  </tr>
  <tr>
    <td>G</td>
    <td>13.6</td>
    <td>(2 1 0)</td>
    <td>3.37, 3.85</td>
    <td>Figures 6(g) and (h)</td>
  </tr>
  <tr>
    <td>H</td>
    <td>6.5</td>
    <td>(2 1 0)</td>
    <td>3.51, 3.96</td>
    <td>NA</td>
  </tr>
  <tr>
    <td>I</td>
    <td>11.1</td>
    <td>(2 1 0)</td>
    <td>NA</td>
    <td>figure 8(a) and (b)</td>
  </tr>
  <tr>
    <td>J</td>
    <td>11.8</td>
    <td>(2 1 0)</td>
    <td>NA</td>
    <td>figures 8(c) and (d)</td>
  </tr>
</tbody>
</table>

exchange reaction while the other part is located in the Stern layer. The CD-MUSIC model does not treat surface com- plexes as point charges, but rather considers them to have a spatial distribution of charge at the interface.

## 3. Results

### 3.1. Static DFT calculations and $SeO_{3}^{2-}$ adsorption

Figure 2 depicts static (i.e. $T=0$ K, geometry optimization) calculations. First, figure 2(a) represents an attempt to use cluster-based DFT calculations. The model has 3 Fe(III) cen- ters, 13 O, and 17 H atoms to yield a charge-neutral cluster with 6-coordinated Fe ions. Fe(III) tend to exhibit robust cluster structures when they are bonded to $OH^{-}$ [7]. However, in order to achieve charge neutrality, four of the thirteen OH groups have to be further protonated to become $H_{2}O$ mol- ecules. Fe(III) ions are only weakly coordinated to some of these $H_{2}O$, yielding elongated Fe–O bonds (figure 2(a)). The average $Fe-O(H_{2}O)$ distance is $2.11$ Å compared to the average $Fe-O(OH^{-})$ bond length of $2.03$ Å in figure 2(a). Hence the added $H^{+}$ to form $H_{2}O$ destabilizes the cluster. Furthermore, this cluster appears too small to accommodate the adsorption of both Pb(II) and $SeO_{3}^{2-}$. This leads us to apply slab models in the rest of this manuscript.

Figure 2(b) depicts three unit cells of the optimized, pris- tine (2 1 0) surface. The surface structure is in agreement with that of [66]. In this static picture, there are 2 types of $Fe_{2}OH$ groups, in agreement with the MUSIC model [6]. Here $Fe_{n}OH$ means that the O is bonded to $n$-Fe ions. Two of the four $Fe_{2}OH$ groups in each surface cell accepts a hydrogen bond and two do not; all four donate hydrogen bonds. The two $Fe_{1}OH$ groups accept hydrogen bonds; the pK$_{a}$ of these $Fe_{1}OH$ groups are clearly different from the adsorbed $H_{2}O$ associated with $Fe_{1}OH_{2}$ groups. MUSIC model pK$_{a}$ predictions for these FeOH groups are sensitive to whether ‘structural hydrogen bond bridges’ are present. In general, the MUSIC pK$_{a}$ for the (2 1 0) surface are difficult to reconcile with AIMD simula- tions because, as will be discussed, some of the adsorbed $H_{2}O$ molecules can dissociate from the surface in the trajectories, and other adsorbed $H_{2}O$ may reorient to flip the identity of hydrogen bond donors and acceptors.

For a minimal comparison of the possible deprotonation sites at $T=0$ K, we have removed a $H^{+}$ from both types of $Fe_{2}OH$ in vacuum, leaving net negatively charged slabs in the simulation cells. As might be expected, deprotonating a $Fe_{2}OH$ group in which the O atom is a hydrogen bond acceptor is more energetically favorable than deprotonating a $Fe_{2}OH$ group which is only a hydrogen bond donor. The energy dif- ference is 0.40 eV. Only the trend is meaningful; the precise energy difference needs to be corrected for the slab-like sim- ulation cell with a net charge, and currently the methods to make such corrections are arguably under development.

Figure 2(c) depicts the pristine goethite (1 0 1) surface. There are five types of FeOH groups on this surface. According to the MUSIC model, one of these five types, marked ‘$Fe_{3}O$,’ is deprotonated under ambient conditions [6]. In the figure, ‘$O_{I}H$’ and ‘$O_{II}H$’ are respectively, an OH group that is origi- nally a OH in the bulk FeOOH framework, and a O anion on the surface terminated by adding a $H^{+}$. We will henceforth omit the ‘I’ and ‘II’ subscripts on the O anions. All surface Fe(III) ions are coordinated to either $OH^{-}$ or $O^{2-}$; there are no $Fe(III)OH_{2}$ terminations, unlike the (2 1 0) surface, or the (1 0 0) surface examined in [77].

We only briefly consider $SeO_{3}^{2-}$ adsorption in this work using static, $T=0$ K DFT calculations. Figure 2(d) depicts a $SeO_{3}^{2-}$ inserted on to the goethite (1 0 1) surface, replacing two $OH^{-}$ groups and retaining simulation cell charge neu- trality. This mode of adsorption has been suggested in the literature and has been computationally demonstrated for other oxyanions such as $CO_{3}^{2-}$, $SO_{4}^{2-}$, and $AsO_{4}^{-}$ [36, 37, 41, 78, 79]. The two Se–Fe distances in the optimized geometry are 3.34 and $3.36$ Å . The average is in good agreement with EXAFS data ($3.38$ Å ) [1] and DFT calculations based on a cluster with two Fe(III) ions [7]. Since the $SeO_{3}^{2-}$ is strongly bonded to the surface, with two of its O atoms inserted into the FeOOH framework, neither thermal fluctuations nor the aqueous environment is expected to alter the predictions. Hence we have not applied finite temperature AIMD simula- tions in this case.

![](./images/813120490167074817_4.jpg)

![](./images/813120490167074817_5.jpg)

![](./images/813120490167074817_6.jpg)

![](./images/813120490167074817_7.jpg)

Figure 2. (a) FeOOH cluster with $Pb^{2+}$ and $SeO_3^{2-}$; (b) top view of goethite (210) surface; (c) side view of a goethite (101) surface supercell, showing the 5 types of FeOH or FeO environments; the 'trench' position is located where $Fe_3O$ groups are already deprotonated in accordance with the MUSIC model [6]; (d) side view of goethite (101) surface with $SeO_3^{2-}$ inserted, replacing $2\ OH^-$. Grey, red, white, ice blue, and yellow represent Fe, O, H, Pb, and Se, respectively. In panel (a) and (b), $H_2O$ oxygen atoms are shown in blue, and a few representative hydrogen bonds are depicted as blue dashes. In (c) and (d), O-H bonds are depicted as hollow sticks.

### 3.2. Pb(II) surface Complexation on goethite (101): $T=0\ K$ models

Geometry optimization at $T=0\ K$ is less conclusive for Pb(II) adsorption than for $SeO_3^{2-}$ insertion. For example, figure 3(a) depicts an optimized geometry for Pb(II) in the 'trench' site on the (101) surface (yellow site in the illustration of figure 1(a)). This Pb(II) is coordinated to the $Fe_3O$ group already deprotonated on pristine (101) surfaces under ambient conditions (figure 2(c)), and to two $Fe_2O$ groups newly deprotonated to accommodate the positive charge of the Pb(II) cation. When liquid water is added and an AIMD simulation is conducted at finite temperature (initial configuration shown in figure 4(a)), this Pb(II) detaches from the surface within picoseconds and becomes solvated by water molecules. This is illustrated in the figure 4(b) snapshot, where the Pb(II) ion is already 2.98 and 3.46 Å from the closest O-atoms on the surface after 7.1 ps. In contrast, the average of the three Pb-O distances in figure 3(a) is 2.27 Å . Thus $T=0\ K$ structures do not always give even qualitative accurate predictions at liquid-material interfaces.

We next examine Pb(II) adsorption sites suggested by CD-MUSIC model analysis. One model suggests purely edge-shared or corner-plus-edge-shared configurations, where the corner is a $Fe_1OH$ group; the Pb is also coordinated to a $Fe_3O$ group [5]. These correspond to the green and blue sites in figure 1(a), respectively. Geometry optimization calculations applied to these initial configurations in the absence of water molecules always yield Pb(II) coordinated to 3 surface OH groups (blue site), making $Pb^{2+}$ shared among 2 corners and 2 edges (figures 3(b)-(d)). It will be shown that Pb(II) at this site is at least metastable in the presence of liquid water (figures 4(c)-(f)), in the sense that Pb(II) does not desorb over the duration of the trajectory.

The proton configuration strongly affects Pb(II) adsorption. The protonation states of FeOH depends on their $pK_a$. MUSIC model $pK_a$ for the FeOH groups are estimated in the absence of the cation [6]; coordination of the highly charged divalent $Pb^{2+}$ to FeOH groups may strongly modify their $pK_a$. The configuration shown in figure 3(b), with $Pb^{2+}$ coordinated to a deprotonated $Fe_3O$ on goethite (101) surface, is the

![](./images/813120490167074817_8.jpg)

Figure 3. Optimized geometries of a single Pb(II) adsorbed on to the goethite (1 0 1) surface in the absence of water. (a) $Pb^{2+}$ at the trench' site, coordinated to a $Fe_{3}O$ and two deprotonated $Fe_{2}O$ groups. (b)-(d) $Pb^{2+}$ adsorption at a site on goethite (1 0 1) surface which has a mixture of corner- and edge-sharing character. (b) Deprotonation at the $Fe_{3}OH$ site; (c) deprotonation at the $Fe_{1}OH$ site; (d) no deprotonation. Panels (b)-(d) are displaced in the lateral direction relative to (a) (and figure 2(c)) for easy visualization.

most stable, followed by $Pb^{2+}$ coordinated to a deprotonated $Fe_{1}O$ (figure 3(c)) which is 0.463 eV less favorable. When all three coordinating FeOH groups are protonated, the energy is the least favorable (+1.211 eV compared to figure 3(b)). We caution that, to preserve charge neutrality in the calculations, one or two protons in the FeOOH interior are removed in these static calculations, only. Therefore the predicted energy changes in such $T=0$ K calculations are not as definitive as AIMD simulations (figure 4 below) with explicit liquid $H_{2}O$ present and no deprotonation of interior OH groups.

The two closest Fe-Pb distances in figure 3(b) are both $3.27$ Å, in best agreement with EXAFS measurements (3.35 Å) among the figure 3 panels. In figure 3c, the distances are 3.33 and 3.46 Å. One of them agrees with the $3.35$ Å EXAFS value but the other is not reported in experiments. In figure 3(d), they are 3.50 and 3.52 Å at substantial variance with measured values. Adding explicit $H_{2}O$ molecules in these $T=0$ K optimization calculations do not substantially improve the agreement. Furthermore, due to the multitude of $H_{2}O$ hydrogen-bonding sites on dry FeOOH surfaces, optimizing the geometry with explicit $H_{2}O$ present at $T=0$ K would require a substantial exploration of the configuration space. Instead we conduct AIMD simulations to deal with the effect of water, so that interfacial liquid water configurations are spontaneously sampled at finite temperature.

### 3.3. AIMD simulations of Pb(II) on goethite (1 0 1)

Given the predictions of the $T=0$ K DFT calculations above, and the cost of AIMD simulations, we focus on AIMD simulations of the 3-coordinated Pb(II) adsorption site (blue site in figure 1(a)) on the (1 0 1) surface. As will be discussed, the introduction of liquid water leads to significant motion of the Pb(II) cation, including a 2-coordinated configuration in part of one trajectory.

Trajectory B starts with the protonation configuration of figure 3(b), which is found to be optimal in $T=0$ K calculations. Figures 4(c) and (d) depict the initial and final configurations for Pb(II) adsorption, which are similar except for orientation changes in some FeOH groups. The $Fe_{3}O$ group coordinated to $Pb^{2+}$ remains deprotonated throughout the trajectory. The two closest Pb-Fe distances relax to and fluctuate

![](./images/813120490167074817_9.jpg)

Figure 4. (a) and (b) Initial and final configurations depicting $Pb^{2+}$ desorption from the figure 3(a) surface site, when liquid water is added (Trajectory A). (c) and (d) Initial and final configurations depicting $Pb^{2+}$ adsorption at a site on goethite (1 0 1) surface which has a mixture of corner- and edge-sharing characters, when liquid water is added to figure 3(b) (Trajectory B). (e) and (f) Initial and final configurations of Trajectory C; they are similar to (c) and (d), but with a different initial water configuration where the deprotonated $Fe_3OH$ group almost shares a proton with a $H_2O$. $H_2O$ molecules are depicted as wire-frames, except for the $H_2O$ molecule coordinated to Pb in panel (e); it has diffused away in panel (f).

around an average of 3.37 Å (figure 5(a)), in good agreement with EXAFS measurements. The agreement is better than when no water is present (figure 3(b)). The next shortest Fe–Pb distance is 4.31 Å . This $Pb^{2+}$ binding site does not yield the 3.90 Å Fe–Pb distance observed in EXAFS [2–4]. Therefore at least one other Pb-binding site must be present at low pH to explain the experimental 3.90 Å distance. The mean distances between Pb(II) and the two $Fe_1OH$ oxygens are both 2.38 Å , somewhat larger than the EXAFS value of 2.27 Å . As expected, DFT/PBE slightly overestimates Pb–O bond lengths. The Pb(II)–O distance for the $Fe_3O$ group averages to 2.39 Å . The inset to figure 5(a) shows that the fluctuations in Pb–O distances are small after the first picosecond. $Pb–O_{water}$ coordination distances are longer [80]; the two closest Pb(II)–$O_{water}$ distances are 3.00 and 2.86 Å . This represents our most stable binding site simulation on the (1 0 1) surface.

![](./images/813120490167074817_10.jpg)

Figure 5. (a) and (b) The two smallest $Pb^{2+}-Fe$ distances as a function of time in Trajectories B and C, respectively. The inset in panel (a) depicts Pb-O distances for trajectory B. (c) Protonation states of the FeOH groups initially coordinated to $Pb^{2+}$ in trajectory C; 1 and 0 refer to protonated and deprotonated states. (d) Pb-O distances for Trajectory C. Green, blue, and yellow refer to the $Fe_{3}O(H)$ and the two $Fe_{1}OH$ groups coordinated to $Pb^{2+}$, respectively.

Trajectory C illustrates the effect of varying the initial configurations. It starts with a protonation configuration identical to that of Trajectory B, but with a different initial $H_{2}O$ configuration (figure 4(e)). Operationally, the starting configuration is obtained by running different number of GCMC steps from that in Trajectory B. Here, after GCMC pre-equilibration, a $H_{2}O$ molecule has formed a hydrogen bond with the $Fe_{3}O$ group coordinated to $Pb^{2+}$. For a time, this $H_{2}O$ reversibly transfers a $H^{+}$ to that $Fe_{3}O$ group, protonating it (figure 5(c)). As a result, the $Pb^{2+}$ coordinates to the O-site of that $H_{2}O$ rather than the O-site of the now protonated $Fe_{3}OH$ group. This drastically weakens its electrostatic interaction with the goethite surface, and indeed the average Pb-Fe distance is larger in this initial part of the trajectory. At the 7.0 ps point, the $H_{2}O$ molecule intervening between the Pb(II) and the $Fe_{3}O$ group diffuses away, and the Pb-Fe distances start to exhibit significant fluctuations (figure 5(b)). The distance between Pb and the O atom in the $Fe_{3}O$ group also vacillates between ionic bonding ($\sim$2.5 Å ) and no bonding (>3 Å , figure 5(d)). Figure 4(f) shows the final configuration, with $Pb^{2+}$ coordinated to the same three FeOH and FeO groups as Trajectory B (figure 4(d)), with the same $Fe_{3}O$ group deprotonated, but the fluctuations have not ended at that point. This trajectory embodies both 2- and 3-coordinated Pb(II). The large fluctuations suggest that a binding configuration with a strong 2-coordinated Pb(II) character is not stable, and the Pb(II) is unlikely to persist there for long. Given the large oscillations unique to this trajectory, the average bond lengths are likely meaningless and cannot be compared to EXAFS distances.

Since part of the trajectory evidently has a $Fe_{3}OH$ group next to the adsorbed Pb(II), we do not need to examine another trajectory with an initially protonated $Fe_{3}OH$ group. This $Fe_{3}OH$ is ultimately deprotonated, just like at the end of Trajectory B. According to the MUSIC model, this $Fe_{3}OH$ group should retain its proton in the absence of a cation [32]. We conclude that the proximity of the Pb(II) has induced $Fe_{3}OH$ deprotonation. In other words, concerted Pb(II) adsorption and $Fe_{3}OH$ deprotonation is observed. This trajectory underscores the importance of testing multiple initial configurations in AIMD simulations of these complex oxide surfaces.

In summary, the (101) surface, with a deprotonated $Fe_{3}OH$ group and two protonated $Fe_{1}O$ groups coordinated to the Pb, is consistent with the shortest Pb-Fe distance measured in EXAFS experiments. We do not observe spontaneous deprotonation of the two $Fe_{1}OH$ groups coordinated to the $Pb^{2+}$.

### 3.4. Pb(II) surface complexation on goethite (210)

Next we address the (210) surface. As discussed above, its surface structure comes from previous modeling work [66]. It exhibits $Fe_{1}OH$ and $Fe_{1}OH_{2}$ surface groups as well as two types of $Fe_{2}OH$. CD-MUSIC models predict several binding sites, including a 2-coordinated Pb bridging complex (pink in figure 1(b)) [5], and a 3-coordinated Pb complex both edge-shared and corner-shared (orange in figure 1(b)) [6]².

First we consider structures optimized at $T=0$ K. Two $H_{2}O$ molecules are added to surfaces with an adsorbed Pb(II), and two protons removed to maintain charge neutrality in the simulation cell. Adding the $H_{2}O$ molecules allows the two-coordinated Pb(II) to be either corner-shared (white site in figure 1(b), starting configuration of Trajectory D, below) or edge-shared (pink site in figure 1(b), starting configuration of Trajectories E-G, with different protonation states). The Pb-Fe distances are 3.85 Å in the former case and 2.9. 3.0, and 3.1 Å in the latter. They are in poor agreement with the EXAFS shortest Fe-Pb separation, and we have not depicted these $T=0$ K results in figures or analyzed them in more detail. Furthermore, during AIMD simulations, $\sim$50% of the $H_{2}O$ initially coordinated to a single Fe(III) on the surface (the $Fe_{1}OH_{2}$ groups mentioned above) are found to detach from the surface at least temporarily, so that Fe(III) coordination environments in ultrahigh vacuum and in liquid water-immersed conditions cannot be unambiguously compared. See also [43]. The (100) surface exhibits similar weak Fe(III)-water bonds [77]. (Recall that there is no $H_{2}O$ coordinated to Fe(III) on the (101) surface.) Instead we use GCMC to add water to these $T=0$ K structures and conduct AIMD simulations. The Fe-Pb distances obtained in AIMD simulations become significantly different than those obtained in $T=0$ K optimization calculations.

First we consider corner-sharing (white site in figure 1(b); Trajectory D). This configuration has been proposed in CD-MUSIC models for Cd(II) adsorbed on the (210) surface

²Note that figure 1 in [5], section 4, is said to describe a 3-coordinated Pb site identical to that in [7] but in fact refers to a different binding site.

![](./images/813120490167074817_11.jpg)

Figure 6. Representative Pb(II) binding configurations on the (2 1 0) surface. (a)–(h) correspond to the starting- (or near starting-) and end-points of trajectories D–G, respectively. Some Fe(III) octahedra may appear truncated at the end of the trajectories because the H₂O bonded to them may have temporarily diffused away.

[6]. The Pb(II) is initially corner-shared between two $Fe_1OH$ groups, one of which is deprotonated. During AIMD equilibration, the deprotonated $Fe_1O$ group immediately acquires a proton from other FeOH groups (figure 6(a)). The Pb(II) coordination is evidently not sufficient to shift the $pK_a$ of the $Fe_1OH$ group on this surface sufficiently to deprotonate it. Along minor parts of this Trajectory D, Pb(II) becomes coordinated to a $Fe_2OH$ on the surface, temporarily distancing itself from one of the $Fe_1OH$ and becoming edge-shared. This behavior is reflected in the fluctuating Pb-O distances (figure 7(e)). The final configuration has the Pb remaining corner-shared, with the $Fe_2OH$ oxygen 2.6 Å away (figure 6(b)). The average Pb-O distances are 2.26, 2.44, and 2.49 Å for the two $Fe_1OH$ groups and the $Fe_2OH$, respectively. All these FeOH groups remain protonated after the first few hundreds of femtoseconds. The two shortest Fe-Pb distances average to 3.51 and 3.60 Å (figure 7(a)). They are significantly larger than the EXAFS value of 3.38 Å. As in Trajectory C on the (1 0 1) surface, trajectories with a partial 2-coordinated Pb character exhibit large coordination shell fluctuations (figure 7(e)). We argue that these complexes are unlikely to persist in the long term, or represent the binding sites revealed by EXAFS.

In Trajectory E, a Pb(II) is initially edge-shared and coordinated to two FeOH groups: a $Fe_1OH$ and a deprotonated $Fe_2O$ group (figure 6(c); akin to the pink site in figure 1(b)). After 4 ps, the $Fe_2O$ group gains a proton from a nearby $Fe_2O$ on the surface, to which the Pb(II) becomes now coordinated. The final configuration of this trajectory is shown in figure 6(d). The $Pb^{2+}$ has become ‘face-shared’ among three surface OH/ $O^-$ groups (blue site in figure 1(b)). The shortest Fe-Pb distance fluctuates around 3.34 Å (figure 7(c)), in good agreement with the EXAFS value and is similar to Trajectory B for the (1 0 1) surface. It appears that, as long as Pb is coordinated to a deprotonated $Fe_2O$ or $Fe_3O$ group and two other FeOH groups, the shortest Fe-Pb distance fluctuates around this EXAFS value. The next shortest Fe-Pb distance is 4.22 Å, again in accord with Trajectory B. Therefore the Pb(II) adsorption geometry depends less on facet ((1 0 1) versus (2 1 0)) than the local structure of the binding sites. Whether the free energies associated with Pb(II) adsorption strongly depend on facets will be examined in future AIMD potential-of-mean-force calculations. The fluctuations in the Pb(II)-O($Fe_2O$) distance (figure 7(f)) remain substantial in this trajectory.

Figure 6(e) (Trajectory F) depicts the Pb(II) initially edge-shared and coordinated to a $Fe_2O$ and a $Fe_1O$. This is similar to figure 6(c) except that both of the Fe-O groups coordinated to Pb(II) are initially deprotonated. As the simulation proceeds, both groups acquire a proton from elsewhere on the surface (figure 6(d)). One $H_2O$ molecule is bound to the Pb(II) over the entire trajectory to compensate for the Pb(II) being coordinated to only two surface FeO groups. Figure 7(g) shows that there are large fluctuations in Pb-O distances, as we have observed on other trajectories with predominantly 2-coordinated Pb(II). The final configuration (figure 6(f)) resembles the initial 2-coordinated, Pb(II) adsorption site in figure 6(e) except for the change in protonation states. The two shortest Fe-Pb distances average to 3.45 and 3.75 Å. The shorter of these distances is somewhat larger than the EXAFS value.

![](./images/813120490167074817_12.jpg)

Figure 7. (a)–(d) The two smallest Fe–$Pb^{2+}$ distances as a function of time in Trajectories D–G. Only the first 11 ps of Trajectory G is shown. (e) and (f) The corresponding O–$Pb^{2+}$ distances. Green refers to O atom from the $Fe_2OH$ group while yellow and blue are for $Fe_1OH$ groups; in panel (g), only, the green line refers to a Pb–$O_{water}$ distance because Pb is only coordinated to two FeO groups on the surface in this Trajectory F.

Figure 6(g) (Trajectory G) depicts the initial configuration of a Pb(II) edge-shared at a different location, between a deprotonated $Fe_1OH$ and a deprotonated $Fe_2OH$ group. The first $Fe_1OH$ group becomes immediately protonated, as observed in other trajectories on the (2 1 0) surface. The $Pb^{2+}$ jumps from this edge-shared site to a different corner-plus-edge-shared site, away from the initially coordinated $Fe_1OH$ group towards another $Fe_1OH_2$ group. It remains bound to the initially deprotonated $Fe_2O$. The final configuration is depicted in figure 6(h). It corresponds to the orange site in figure 1(b) and agrees with a CD-MUSIC predicted site [6]. We discard the initial 1.4 ps associated with the large, early Pb(II) displacement. Using statistics over the remainder of the trajectory, the smallest Fe-Pb distances average to 3.37 Å and 3.85 Å. Among all trajectories examined, this trajectory yields the best overall agreement with both the smallest and the second smallest Pb-Fe distances of 3.38 Å and 3.9 Å reported in EXAFS measurements. Perhaps just as importantly, all the key Fe-Pb and O-Pb distances exhibit qualitatively small fluctuations than the previous trajectories after the initial equilibration period (figures 7(d) and (h)). The only other trajectory with qualitatively similar small fluctuations is B, also with 3-coordinated Pb(II), on the (1 0 1) surface (figure 5(a)).

To test the effect of van der Waal’s forces, we have extended Trajectory D while turning on Grimme’s DFT-D2 correction [72]. This new trajectory, ‘H,’ yields the same final protonation state as D (without the dispersion correction). The mean nearest Fe-Pb distances (3.51 and 3.96 Å ) are slightly larger, likely because this trajectory does not contain a small segment where Pb(II) is bound to any deprotonated FeOH, which is the case for D. The fraction of water molecules bound to surface Fe(III) ions also remains the same as the case without

![](./images/813120490167074817_13.jpg)
![](./images/813120490167074817_14.jpg)

![](./images/813120490167074817_15.jpg)
![](./images/813120490167074817_16.jpg)

Figure 8. $Pb^{2+}$-$SeO_3^{2-}$ contact ion pair complexation on goethite (2 1 0) surfaces. (a) and (b) Initial and final configurations of the ion pair with a $SeO_3H^-$ initially replacing a $H_2O$ on the surface. One of the $SeO_3H^-$ O atoms is directly coordinated to a Fe ion (Trajectory I). (c) and (d) Initial and final configurations when the $SeO_3H^-$ is initially only hydrogen-bonded to the surface (Trajectory J). The ion pair desorbs in this second case.

dispersion corrections. We conclude that dispersion corrections do not strongly affect these AIMD results.

Comparing Trajectories G, B and E, Pb(II) coordination to a deprotonated $Fe_2OH$ or $Fe_3OH$ group is found to yield good agreement with the shortest EXAFS Pb–Fe distance. Comparing Trajectory G and F, edge-plus-corner 3-coordinated Pb(II) is found to yield a second shortest Fe–Pb distance in better agreement with EXAFS data (3.90 Å) than 2-coordinated edge-shared sites. Comparing the same two trajectories, a deprotonated $Fe_2OH$ group coordinated to Pb(II) again yields a superior shortest Pb–Fe distance. Note that the $Fe_2OH$ group starts out deprotonated but acquires a proton during Trajectory F; in contrast, this group is deprotonated throughout Trajectory G. Therefore longer runs appear needed to assess $Fe_2OH$ protonation states. Varying the initial conditions, or using deprotonation constraints [58, 59], are needed to model concerted Pb(II) adsorption and $Fe_2OH$ deprotonation. In contrast, protonation is fast for $Fe_1OH$ groups.

Regarding changes in Pb(II) coordination, the trajectory starting with corner-shared Pb(II) remains corner-shared. Of the three trajectories with edge-shared 2-coordinated Pb(II), two become 3-coordinated face- or edge-plus-corner shared and only one remains 2-coordinated. This suggests that 2-coordinated Pb(II) sites are less stable in terms of free energy. The 3-coordinated edge-plus-corner-shared Pb-binding site on the (2 1 0) surface consistent with CD-MUSIC predictions [2, 3, 6] (orange site in figure 1(b)) yields the best overall agreement with Pb–Fe distances reported in EXAFS experiments. This site also exhibits the least fluctuation in Pb–O distances among trajectories on the (2 1 0) surface, suggesting that it should be the most stable adsorption site. We stress that, within $\sim$15 ps AIMD trajectories, the Pb(II) cation does not always spontaneously sample the available adsorption configuration space. Even initially edge-shared Pb(II) coordinated to the same $Fe_1OH$ and $Fe_2OH$ groups can yield qualitatively different adsorption and fluctuation behavior within this time frame if the initial water configuration differs.

### 3.5. $Pb^{2+}$-$SeO_3^{2-}$ contact ion pairs

Finally, we perform preliminary studies of $Pb^{2+}$-$SeO_3^{2-}$ contact ion pairing adsorption on the goethite (2 1 0) surface. The experimental data on ion pairing, e.g. [4], have not specified the facet dependence. Due to the cost of these simulations, we

have opted to perform a qualitative study of one surface and defer more systematic studies to the future.

Figure 8(a) depicts one initial configuration of this adsorbed ion pair. The Pb(II) is initially edge-shared. The $SeO_3H^-$ is in fact initially protonated to facilitate convergence of the DFT Kohn–Sham wavefunctions. The difficulty in convergence is likely due to the significant charge separation in the contact-ion pair. The charges involved may not be suf- ficiently well-solvated in the configuration initialized using classical force fields (see the Method section). After less than 0.5 ps, the proton on the selenite anion migrates to the goe- thite surface, and we obtain the expected $Pb^{2+}$-$SeO_3^{2-}$ contact ion pair. To the best of our knowledge, the experimental data suggests unprotonated selenite anions in contact ion pairs ([5] table 4.4). Hence it is reasonable that the $Pb^{2+}$/$SeO_3^{2-}$ contact ion pair is obtained in the AIMD simulations even when we start with $SeO_3H^-$. The initial protonation states should not strongly affect the final configurations because the trajectory involves a direct proton exchange between $SeO_3H^-$ and the FeO group hydrogen-bonded to the anion through the proton being transferred. The changes are therefore strongly local- ized and do not directly involve the adsorption of the Pb(II) ion, which appears much more sensitive to initial conditions.

The $SeO_3^{2-}$ is initially coordinated to one surface Fe ion, replacing the surface $H_2O$ to which that Fe is formerly bound. This is distinct from the $SeO_3^{2-}$ adsorption configuration in figure 2(d), where the anion replaces two surface $OH^-$ groups. Over the entire 11 ps trajectory, the $Pb^{2+}$-$SeO_3^{2-}$ contact- ion-pair remains tethered to the surface in this way (figure 8(b)). This is consistent with the 'type A' $Pb^{2+}$/$SO_4^{2-}$ contact ion pair adsorption on goethite surfaces reported in the literature [4, 81].

Figure 8(c) depicts the initial configuration of another adsorbed ion pair. The $SeO_3H^-$ is initially hydrogen bonded to a $H_2O$ and a FeOH group on the surface. It does not replace a Fe-bound $H_2O$ on the surface, as is the case with figure 8(a). This mode of complexation has been discussed for $Pb(II)/SO_4^{2-}$ ([3, 4, 81]) and $Pb(II)CO_3^{2-}$ ([2]) adsorption on FeOOH surfaces. Within a few picoseconds, the $SeO_3^{2-}$ desorbs from the surface (figure 8(d)). The initially edge- shared Pb(II) has also detached itself from the surface, with the closest Pb(II)–O(FeOOH) surface being 3.40 Å at the end of the trajectory. This suggests that, for the ion pair to stay adsorbed to the goethite surface, there should be one (or more) direct oxyanion ionic-bond with a surface Fe ion. Our AIMD simulations therefore dispute the 'type B' or 'type C' contact ion pair adsorption configuration defined in [4, 81], where the oxyanion is not chemically bonded to the goethite surface.

## 4. Conclusions

We have applied *ab initio* molecular dynamics (AIMD) techniques to model $Pb^{2+}$ and $Pb^{2+}$/$SeO_3^{2-}$ contact ion pair adsorption on overall charge-neutral goethite/water inter- faces. In particular, we examine multiple Pb(II)-binding sites and vary the initial water configurations and goethite surface protonation states using AIMD simulations of periodically replicated, charge-neutral simulation cells. With judicious choice of surface FeOH group protonation states, the AIMD predictions are in broad agreement with EXAFS data, and are consistent with certain CD-MUSIC predicted sites on the (1 0 1) and (2 1 0) surfaces where Pb(II) is coordinated to three surface FeO groups [2–6]. Our AIMD simulations examine FeOH group protonation state changes, Pb–O bond length fluctuations, and concerted Pb(II)/proton dynamics. They constitute a foundational study for future AIMD potential-of- mean-force simulations of Pb(II) and $Pb(II)/SeO_3^{2-}$ adsorp- tion free energy calculations at different binding sites on goethite/water interfaces. Ultimately, the equilibrium adsorp- tion constants, critical to first-principles modeling of ion par- titioning on mineral surfaces, are related to the free energy of adsorption.

For an isolated $Pb^{2+}$ on goethite (1 0 1) and (2 1 0) sur- faces, the deprotonation of at least one FeOH group coordi- nated to 3-coordinated $Pb^{2+}$ appears necessary to reproduce the shortest Fe–Pb distance (~3.38 Å ) reported in EXAFS data, regardless of whether the $Pb^{2+}$ is face-shared on one Fe-octahedron or edge-and-corner-shared on two Fe-octahedra. Not coincidentally, such deprotonated FeOH groups should yield stronger electrostatic interactions, and therefore should provide more energetically favorable Pb(II) binding sites. To reproduce the second shortest Fe–Pb distance of 3.85 Å reported by EXAFS, $Pb^{2+}$ corner-shared between a $Fe_1OH$ and a deprotonated $Fe_2OH$ group on the (2 1 0) surface is the best candidate. At pH above 6.0, this second-shortest Fe–Pb signature is known to disappear, suggesting this par- ticular site is no longer available for Pb(II) coordination [2–4]. This behavior can be be investigated in future AIMD studies by varying the solution pH. In general, Pb(II) initially coordi- nated only to two FeOH surface groups either exhibits large configurational fluctuations and Fe–Pb distances, or becomes coordinated to a third FeOH surface group during at least part of the trajectory. Therefore our simulations dispute the pos- sibility of the purely two-coordinated Pb(II) surface sites sug- gested in some CD-MUSIC model studies and assignments based on EXAFS experiments [2–5].

Regarding $Pb^{2+}$/$SeO_3^{2-}$ contact ion pair adsorption on goethite (2 1 0) surfaces, our AIMD simulations show that if the $SeO_3^{2-}$ anion is only hydrogen-bonded to the goethite surface, it desorbs in a picosecond time scale. If the $SeO_3^{2-}$ anion inserts itself on to the FeOOH surface via a monoden- tate Se–O–Fe bridge, the contact ion pair remains stable on the (2 1 0) surface—at least for the duration of a 11.8 ps AIMD trajectory.

AIMD permits some spontaneous $H^+$ configuration rear- rangement within 15–20 ps trajectory lengths. On both sur- faces, $Fe_1OH$ groups coordinated to $Pb^{2+}$ either remain protonated in AIMD trajectories, or acquire a proton if they start out without one. The proximity of the highly charged $Pb^{2+}$ does not shift the $pK_a$ of these $Fe_1OH$ group to suffi- ciently low values to affect their protonation states. In con- trast, the $Fe_3OH$ on the (1 0 1) surface and $Fe_2OH$ groups on the (2 1 0) facet become deprotonated in the presence of $Pb^{2+}$.

However, the deprotonation dynamics takes place on the order of 10ps. In these cases, the dynamics are strongly influenced by local water configurations. These findings suggest that concerted $\text{H}^{+}$ and Pb(II) motion on goethite surfaces is important. Such concerted motion is an important mechanism for future AIMD deprotonation free energy calculations to explore.

## Acknowledgment
We thank Lynn Katz at University of Texas at Austin, and Jeremiah Mangold at Clemson University, for useful discussions on initial conditions used in simulations. Sandia National Laboratories is a multimission laboratory managed and operated by National Technology and Engineering Solutions of Sandia, a wholly owned subsidiary of Honeywell International, Inc, for the US Department of Energy's National Nuclear Security Administration under contract DE-NA0003525. LJC and KL acknowledge support from the US DOE Office of Basic Energy Sciences, Division of Chemical Sciences, Geosciences, and Biosciences.

## References
[1] Hayes K F, Roe A L, Brown G E, Hodgson K O, Leckie J O and Parks G A 1987 *Science* **238** 783

[2] Ostergren J D, Trainor T P, Bargar J R, Brown G E and Parks G A 2000 *J. Colloid Interface Sci.* **225** 466

[3] Ostergren J D, Trainor T P, Bargar J R, Parks G A and Persson P 2000 *J. Colloid Interface Sci.* **225** 483

[4] Elzinga E J, Peak D and Sparks D L 2001 *Geochim. Cosmochim. Acta* **65** 2219

[5] Mangold J E 2013 *Predicting Ion Adsorption onto the Iron Hydroxide Goethite in Single and Multi-Solute Systems* (Austin, TX: University of Texas Press) (Dissertation)

[6] Venema P, Hiemstra T and van Riemsdijk W H 1996 *J. Colloid Interface Sci.* **183** 515

[7] Hiemstra T, Rietra R P J J and Van Riemsdijk W H 2007 *Croatica Chem. Acta* **80** 313

[8] Rietra R P J J, Hiemstra T and van Riemsdijk W H 1999 *J. Colloid Interface Sci.* **218** 511–21

[9] Criscenti L J and Sverjensky D A 1999 *Am. J. Sci.* **299** 828

[10] Hiemstra T Van Riemsdijk W H 2000 *J. Colloid Interface Sci.* **225** 94

[11] Criscenti L J and Sverjensky D A 2002 *J. Colloid Interface Sci.* **253** 329

[12] Hiemstra T, Rahnemaie R and Van Riemsdijk W H 2004 *J. Colloid Interface Sci.* **278** 282

[13] Ponthieu M, Juillot F, Hiemstra T, van Riemsdijk W H and Benedetti M F 2006 *Geochim. Cosmochim. Acta* **70** 2679

[14] Sverjensky D A 2006 *Geochim. Cosmochim. Acta* **70** 2427

[15] Sverjensky D A and Fukushi K 2006 *Environ. Sci. Technol.* **40** 263

[16] Sverjensky D A and Fukushi K 2006 *Geochim. Cosmochim. Acta* **70** 2778

[17] Fukushi K and Sverjensky D A 2007 *Geochim. Cosmochim. Acta* **71** 3717

[18] Fukushi K and Sverjensky D A 2007 *Geochim. Cosmochim. Acta* **71** 1

[19] Salazar-Camacho C and Villalobos M 2010 *Geochim. Cosmochim. Acta* **74** 2257

[20] Villalobos M and Leckie J O 2001 *J. Colloid. Interface Sci.* **235** 15

[21] Barrow N J and Cox V C 1992 *J. Soil Sci.* **43** 295

[22] Piasecki W and Sverjensky D A 2008 *Geochim. Cosmochim. Acta* **72** 3964

[23] von Rudorff G F, Jakobsen R, Rosso K M and Blumberger J 2016 *J. Phys.: Condens. Matter* **28** 394001

[24] Alexandrov V and Rosso K M 2013 *J. Phys. Chem. C* **117** 22880

[25] Gu X, Evans L J and Barabash S J 2010 *Geochim. Cosmochim. Acta* **74** 5718

[26] Churakov S V and Kosakowski G 2010 *Phil. Mag. A* **90** 2459

[27] Larrucea J, Lid S and Cierach L J 2014 *Comput. Mater. Sci* **92** 343

[28] Villalobos M and Pérez-Gallegos A 2008 *J. Colloid Interface Sci.* **326** 307

[29] Hiemstra T and Van Riemsdijk W H 1999 *J. Colloid Interface Sci.* **210** 182

[30] Stadler M and Schindler P W 1993 *Clays. Clay Miner.* **41** 288

[31] Stachowicz M, Hiemstra T and Van Riemsdijk W H 2008 *J. Colloid Interface Sci.* **320** 400

[32] Venema P, Hiemstra T, Weidler P G and van Riemsdijk W H 1998 *J. Colloid Interface Sci.* **198** 282

[33] Hiemstra T, Van Riemsdijk W H, Rossberg A and Ulrich K U 2009 *Geochim. Cosmochim. Acta* **73** 4437

[34] Paul K W, Borda M J, Kubicki J D and Sparks D L 2005 *Langmuir* **21** 11071

[35] Paul K W, Kubicki J D and Sparks D L 2006 *Environ. Sci. Tech.* **40** 7717

[36] Paul K W, Kubicki J D and Sparks D L 2007 *Euro. J. Soil Sci.* **58** 978

[37] Kubicki J D, Kwon K D, Paul K W and Sparks D L 2007 *Euro. J. Soil Sci.* **58** 932

[38] Kubicki J D, Paul K W and Sparks D L 2008 *Geochem. Trans.* **9** 4

[39] Mason S E, Trainor T P and Chaka A M 2011 *J. Phys. Chem. C* **115** 4008

[40] Mason S E, Trainor T P and Goffinet C J 2012 *Comput. Theor. Chem.* **987** 103

[41] Acelas N Y, Mejia S M, Mondragón F and Flórez E 2013 *Comput. Theor. Chem.* **1005** 16

[42] Zubieta C E, Fortunato L F, Belelli P G and Ferullo R M 2014 *Appl. Surf. Sci.* **314** 558

[43] Alexandrov V and Rosso K M 2015 *Phys. Chem. Chem. Phys.* **17** 14518

[44] Russell B, Payne M and Ciacchi L C 2009 *Phys. Rev. B* **79** 165101

[45] Wang J, Xia S and Yu L 2015 *Appl. Surf. Sci.* **339** 28

[46] Liu X, Cheng J, Sprik M and Wang R 2013 *Geochim. Cosmochim. Acta* **120** 487

[47] Liu X, Cheng J and Sprik M Wang R 2014 *Geochim. Cosmochim. Acta* **140** 410

[48] Liu X, Cheng J, Sprik M and Wang R 2015 *Geochim. Cosmochim. Acta* **168** 293

[49] Liu X, Meijer E J, Lu X and Wang R 2012 *Clays. Clay Miner.* **60** 341

[50] Pfeiffer-Laplaud M, Gaigeot M-P and Sulpizi M 2016 *J. Phys. Chem. Lett.* **7** 3220

[51] Pfeiffer-Laplaud M and Gaigeot M-P 2016 *J. Phys. Chem. C* **120** 14034

[52] Pfeiffer-Laplaud M and Gaigeot M-P 2016 *J. Phys. Chem. C* **120** 4866

[53] Pfeiffer-Laplaud M, Costa D, Tielens F, Gaigeot M-P and Sulpizi M 2015 *J. Phys. Chem. C* **119** 27354

[54] Costanzo F, Della Valle R G, Sulpizi M and Sprik M 2011 *J. Chem. Phys.* **134** 244508

[55] Sulpizi M and Sprik M 2008 *Phys. Chem. Chem. Phys.* **10** 5238

[56] Sulpizi M and Sprik M 2010 *J. Phys. Condens. Mat.* **22** 284116

[57] Cheng J, Sulpizi M and Sprik M 2009 *J. Chem. Phys.* **131** 154504

[58] Leung K, Nielsen I M B and Criscenti L J 2009 *J. Am. Chem. Soc.* **131** 18358

[59] Leung K and Criscenti L J 2012 *J. Phys.: Condens. Matter* **24** 124015

[60] Zhang C, Liu X, Lu X, Meijer E J, Wang K, He M and Wang R 2016 *Clay and Clay Mater.* **64** 337

[61] Perdew J P, Burke K and Ernzerhof K M 1996 *Phys. Rev. Lett.* **77** 3865

[62] Kresse G and Joubert D 1999 *Phys. Rev. B* **59** 1758

[63] Kresse G and Furthmüller J 1996 *Phys. Rev. B* **54** 11169

[64] Anisimov V I, Zaanen J and Andersen O K 1991 *Phys. Rev. B* **44** 943

[65] Liechtenstein A I, Anisimov V I and Zaanen J 1995 *Phys. Rev. B* **52** 5467

[66] Rustad J R, Felmy A R and Hay B P 1996 *Geochim. Cosmochim. Acta* **60** 1563

[67] Boily J-F 2012 *J. Phys. Chem. C* **116** 4714

[68] Martin M G and Thompson A P 2004 *Fluid Phase Equil.* **217** 105

[69] Berendsen H J C, Grigera J R and Straatsma T P 1987 *J. Phys. Chem.* **91** 6269

[70] Cygan R T, Liang J J and Kalinichev A G 2004 *J. Phys. Chem. B* **108** 1255

[71] Zhang C, Wu J, Galli G and Gygi F 2011 *J. Chem. Theor. Comput.* **7** 3054

[72] Grimme S 2006 *J. Comput. Chem.* **27** 1787

[73] Hiemstra T, Venema P and van Riemsdijk W K 1996 *J. Colloid Interface Sci.* **184** 680

[74] Pauling L 1929 *J. Am. Chem. Soc.* **51** 1010

[75] Brown I D and Altermatt K K 1976 *Acta Cryst. B* **32** 1957

[76] Hiemstra T and van Riemsdijk W K 1996 *J. Colloid Interface Sci.* **179** 488

[77] Chen Y, Bylaska E J and Weare J H 2017 *Geochem. Trans.* **18** 3

[78] Zhu M, Northrup P, Shi C, Billinge S J L, Sparks D L and Waychunas G A 2014 *Environ. Sci. Tech. Lett.* **1** 97

[79] Otte K, Schmahl W W and Pentcheva R 2013 *J. Phys. Chem. C* **117** 15571

[80] Bargar J R, Brown G E and Parks G A 1997 *Geochim. Cosmochim. Acta* **61** 2617

[81] Zhang G Y and Peak D 2007 *Geochim. Cosmochim. Acta* **71** 2158

[82] Paier J, Marsman M and Kresse G 2007 *J. Chem. Phys.* **127** 024103