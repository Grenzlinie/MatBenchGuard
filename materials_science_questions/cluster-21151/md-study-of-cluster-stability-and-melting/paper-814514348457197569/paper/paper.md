# Molecular dynamics simulations of point defect production in cementite and $Cr_{23}C_6$ inclusions in $\alpha$-iron: Effects of recoil energy and temperature

K. O. E. Henriksson

Citation: *AIP Advances* **6**, 065010 (2016); doi: 10.1063/1.4954081

View online: http://dx.doi.org/10.1063/1.4954081

View Table of Contents: http://aip.scitation.org/toc/adv/6/6

Published by the American Institute of Physics

![](./images/814514348457197569_1.jpg)

AIP ADVANCES 6, 065010 (2016)
![](./images/814514348457197569_2.jpg)

# Molecular dynamics simulations of point defect production in cementite and $Cr_{23}C_6$ inclusions in $\alpha$-iron: Effects of recoil energy and temperature

K. O. E. Henriksson$^{a}$

Department of Physics, P.O. Box 43, FI-00014 University of Helsinki, Finland

(Received 8 March 2016; accepted 5 June 2016; published online 10 June 2016)

The number of point defects formed in spherical cementite and $Cr_{23}C_6$ inclusions embedded into ferrite ($\alpha$-iron) has been studied and compared against cascades in pure versions of these materials (only ferrite, $Fe_3C$, or $Cr_{23}C_6$ in a cell). Recoil energies between 100 eV and 3 keV and temperatures between 400 K and 1000 K were used. The overall tendency is that the number of point defects — such as antisites, vacancy and interstitials — increases with recoil energy and temperature. The radial distributions of defects indicate that the interface between inclusions and the host tend to amplify and restrict the defect formation to the inclusions themselves, when compared to cascades in pure ferrite and pure carbide cells. © 2016 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).
[http://dx.doi.org/10.1063/1.4954081]

## I. INTRODUCTION

Ferritic-martensitic (FM) stainless steels can be modelled as iron alloys with the principal alloying elements carbon and chromium. Specifically, if the iron is ferritic, i.e. is in the $\alpha$-phase, then the main pure carbides occurring are cementite ($Fe_3C$) and $Cr_{23}C_6$ (see e.g. Ref. 1). One important usage area for FM stainless steels is in the construction of nuclear applications, where the steels are subjected to e.g. neutron irradiation (see e.g. Refs. 2–5). Atoms can be kicked from their lattice sites by energetic neutrons, which leads to the formation of cascades. After the energy has been dissipated the local atomic environment generally exhibits a number of point defects, and possibly other extended defects. For a given atomic configuration and recoil energy the number of point defects may depend on the ambient temperature and other thermodynamic variables such as pressure.

The present literature on studies of cascades in iron containing carbides is very limited. Especially in the case of simulations the carbides studied have been based on W and Mo.$^{6}$ Many more studies have been carried out on the behavior of individual carbon atoms in iron, see e.g. Refs. 7–12. A recent study$^{13}$ using the same interatomic potential as in this work has been performed on carbides, but the focus was on the behavior of a passing dislocation.

In this study the effect of initial recoil energy and temperature on the defect production in model ferritic stainless steels containing carbides is investigated. Specifically, the material consists of ferrite ($\alpha$-iron) into which spherical carbides cementite ($Fe_3C$) and $Cr_{23}C_6$ have been embedded. For comparison, cascades have also been investigated in cells containing only pure versions of the materials, i.e. ferrite, $Fe_3C$ and $Cr_{23}C_6$ without any inclusions or other modifications.

## II. METHODS

### A. Cascade simulations

The cells of $Fe_3C$ and $Cr_{23}C_6$ were obtained from the density functional theory results presented in Ref. 14. Large cells of ferrite and the carbides $Fe_3C$ and $Cr_{23}C_6$— the latter ones with Cartesian

$^{a}$Electronic mail: krister.henriksson@helsinki.fi

2158-3226/2016/6(6)/065010/12
6, 065010-1
© Author(s) 2016.
![](./images/814514348457197569_3.jpg)

![](./images/814514348457197569_4.jpg)

FIG. 1. Number of antisites as a function of recoil energy for the pure carbides.

border lengths around 100 Å — were relaxed at 300 K and 0 GPa using the Berendsen thermostat and barostat. $^{15}$ For Fe the simulation cell was cubic, with an initial side length of $38a$, $a = 2.89$ Å being the lattice parameter.

In order to construct a ferrite cell containing an inclusion, the following procedure was followed. After relaxation of pure Fe a sphere of radius 20.5 Å was cut out to make room for an inclusion. The atom closest to the origin (0,0,0) — with position $\mathbf{r}_{0}^{\text{Fe}}$ — was selected and all atoms inside a sphere centered on this atom were removed. Spheres of radius 20 Å were extracted from the pure carbide cells, by first locating the atom closest to the origin (0,0,0) — the center of the carbide, with position $\mathbf{r}_{0}^{(c)}$ — and then extracting all atoms situated inside a sphere centered on this position. The carbide sphere was then combined with the Fe host containing the corresponding spherical cavity, such that the carbide center $\mathbf{r}_{0}^{(c)}$ coincided with the center $\mathbf{r}_{0}^{(\text{Fe})}$ of the cavity. This guarantees that the interface region is as uniform as possible in all directions. Each complete cell — Fe host with carbide inclusion — was carefully relaxed at 300 K and 0 GPa for 50 ps to prepare them for the cascade simulations.

The choice of the radial distance of about 20 Å for the inclusions is connected to the choice of recoil energies. The combinations used in this work provides results about cascades contained mostly inside the inclusions as well as cascades reaching somewhat outside them.

All molecular dynamics simulations were carried out using the code PARCAS. $^{16–19}$ The inter- atomic potential is of type Analytical Bond-Order Potential (ABOP) $^{20}$ and has previously been used for studies of C, Cr, and carbides in ferrite. $^{13,21–24}$

For the present work each cell — either of pure material or of ferrite with an inclusion — was heated from 300 K to a given temperature $T$ — 400 K, 600 K, 800 K, or 1000 K — and relaxed to 0 GPa for 50 ps using the Berendsen methods. At the end of this preparatory phase there were five

![](./images/814514348457197569_5.jpg)

FIG. 2. Number of antisites as a function of recoil energy for cells with inclusions.

![](./images/814514348457197569_6.jpg)

FIG. 3. Radial distribution of antisites for pure carbides. Left column: Pure Fe₃C. Right column: Pure Cr₂₃C₆.

different initial cells to be used for cascade simulations: (i) pure ferrite, (ii) pure Fe₃C, pure Cr₂₃C₆, (iv) ferrite with Fe₃C inclusion, and (v) ferrite with Cr₂₃C₆ inclusion.

For the recoil simulations the following steps were taken. All recoil positions were randomly chosen inside a sphere of radius $10\ \mathring{A}$ centered on the center of the carbides. The same recoil positions

![](./images/814514348457197569_7.jpg)

FIG. 4. Radial distribution of antisites for cells with inclusions. Left column: Fe₃C inclusion. Right column: Cr₂₃C₆ inclusion.

were used for all Cell types, recoil Energies, and Temperature events (CET). For all CETs a total of 50 cascades were simulated. With five cell types, five recoil energies $E$ (100, 300, 500, 1000 and 3000 eV), four temperatures $T$ (400, 600, 800, 1000 K), and 50 cascades per CET, a total of 5000 simulations were performed.

![](./images/814514348457197569_8.jpg)

FIG. 5. Number of vacancies (and interstitials) as a function of recoil energy for pure cells. Note that a smaller defect scale is used for pure Fe.

The cells used for cascade simulations were periodic. Berendsen temperature control was applied in 6 Å thick regions at the borders of the cell (about equal to two ferrite lattice parameters), with a target temperature of $T$. No pressure control was used. Each cascade event used a maximum simulation time of 50 ps. Before starting a recoil simulation, the cell was shifted in all Cartesian directions (periodic boundary conditions were enforced) so that the initial recoil position was at the very center of the simulation cell. The actual recoiling atom was the metal atom (Fe or Cr) closest to this position. Electronic stopping by Ziegler et al.,$^{25}$ obtained from the ZBL96 code developed in our laboratory,$^{26}$ was used on all atoms having an energy of 5 eV or more.

### B. Analysis methods
A Wigner-Seitz$^{27}$ (WS) cell analysis was used to find vacancies (empty WS cells) and interstitials (WS cells containing two or more atoms) in the relaxed samples. The degree of clustering of the defects was also analyzed. Two point defects were considered to be clustered if they were separated by a distance $r \leq r_c$. The chosen value was $r_c = 3.4$ Å, which is the maximum potential cutoff for all interactions between iron, chromium and carbon.

The fraction of defects of a certain type (vacancy or interstitial) which are located in a cluster of size $N$ or larger is calculated as
$$
f_c(N) = \left( \sum_{i=N}^{M} i \times N_c(i) \right) / N_d, \tag{1}
$$
where $M$ is the number of defects in the largest cluster, $N_c(i)$ is the number of clusters containing $i$ defects, and $N_d = \sum_{i=1}^{M} i \times N_c(i)$ is the total number of individual defects. If nothing else is specified, a value of $N = 2$ was used.

Defects were also analyzed for their distance to the carbide center. For each energy and temperature, the radial distances for defects in all cascade simulations were collected. The subsequent

![](./images/814514348457197569_9.jpg)

FIG. 6. Number of vacancies (and interstitials) as a function of recoil energy for cells with inclusions.

![](./images/814514348457197569_10.jpg)

FIG. 7. Radial distribution of vacancies for pure cells. Note that a smaller defect scale is used for pure Fe. Left column: Pure Fe. Middle column: Pure Fe₃C. Right column: Pure Cr₂₃C₆.

histograms display a yield density, defined as

$$
Y_{X}(r_{i}) = \frac{N_{X}(r_{i})}{N_{\text{rec}} \cdot V_{\text{shell}}(r_{i})}, \tag{2}
$$

where $X$ is the defect type, $r_{i}$ is the radial distance to the center of shell $i$, $N_{X}(r_{i})$ is the number of defects of type $X$ inside shell $i$, $N_{\text{rec}} = 50$ is the number of recoils (equals the number of cascades), and $V_{\text{shell}}(r_{i})$ is the volume of the spherical shell centered on radial distance $r_{i}$. In all cases a shell width of $5$ Å was used.

## III. RESULTS AND DISCUSSION

### A. Antisites

The number $N_{AS}$ of antisites formed in the cascades is shown in Fig. 1 for pure cells and Fig. 2 for cells with inclusions. $N_{AS}$ increases with energy for all temperatures and all cell types. For the

![](./images/814514348457197569_11.jpg)

FIG. 8. Radial distribution of vacancies for cells with inclusions. Left: Fe₃C inclusion. Right column: Cr₂₃C₆ inclusion.

higher energies the relative increase with energy is larger for the pure cells than for the cells with inclusions. In general the numbers are lower for the pure cells than for the cells with inclusions. In addition, the numbers are generally lower for Cr₂₃C₆ inclusions than the Fe₃C ones.

The radial distributions of antisites are shown in Fig. 3 for the pure cells and Fig. 4 for the cells with inclusions. In general the numbers are lower for the pure cells than for the cells with inclusions.

![](./images/814514348457197569_12.jpg)

FIG. 9. Radial distribution of interstitials for pure cells. Note that a smaller defect scale is used for pure Fe. Left column: Pure Fe. Middle column: Pure Fe₃C. Right column: Pure Cr₂₃C₆.

For the pure cells the distributions are relatively smooth. For the highest recoil energy of 3 keV the distribution is clearly visible out to at least $30\ \mathring{A}$ at all temperatures.

For the cells with inclusions there are very clear single peaks for all energies in the radial distribution at the two highest temperatures, with the peaks weakening or disappearing when the temperature and/or the recoil energy is lowered. However, for 1 and 3 keV there are always clear peaks close to $20\ \mathring{A}$, even at the lowest temperature. The peaks occur at a radial distance somewhat smaller than the initial radius of $20\ \mathring{A}$ of the embedded inclusion.

Comparing the pure cells and the cells with inclusions it seems that the ferrite host inhibits defect formation outside the inclusions, restricting the cascade and cascade damage to the inclusion itself. If it did not the distributions would be smoother, as in the case for the pure cells. The restriction is not perfect, as witnessed by non-zero antisite distributions outside a radial distance of $20\ \mathring{A}$ corresponding to the initial radius of the inclusions. The restriction effect was verified by visual inspection of the cascade simulations.

### B. Vacancies

The number $N_V$ of vacancies formed in the cascades is shown in Fig. 5 for pure cells and Fig. 6 for cells with inclusions. $N_V$ increases with energy for all temperatures and all cell types. For the higher

![](./images/814514348457197569_13.jpg)

FIG. 10. Radial distribution of interstitials for cells with inclusions. Left: Fe₃C inclusion. Right column: Cr₂₃C₆ inclusion.

energies the relative increase with energy is larger for the pure cells than for the cells with inclusions.
In general the numbers are lower for the pure cells than the cells with inclusions. In addition, the
numbers are generally lower for the Cr₂₃C₆ inclusion than the Fe₃C one. The number of interstitials
equals the number of vacancies and is hence not shown.

![](./images/814514348457197569_14.jpg)

FIG. 11. Clustering fractions of vacancies and interstitials as a function of recoil energy for pure cells. First row: Vacancies.
Second row: Interstitials. Left column: pure Fe. Middle column: pure Fe₃C. Right column: pure Cr₂₃C₆.

For pure Fe the number of vacancies is much smaller than for any of the cases with a carbide inclusion. The present result is consistent with previous simulation studies for pure Fe using mainly Embedded Atom Method (EAM) type potentials.²⁸⁻³⁰

The radial distributions of vacancies are shown in Fig. 7 for the pure cells, and in Fig. 8 for the cells with inclusions. For the pure cells the vacancy distributions are generally smoothly decreasing with radial distance, as for the antisites.

For the cells with a carbide inclusion the radial vacancy distributions first decreases out to about 5 Å, then increases out to about 15 Å, and then decreases again. The intermediate increase does not occur for all cases, but seems to be favored for high recoil energies at all temperatures, and for low recoil energies if the temperature is around 600 K or higher. A similar behavior occurs for antisites, but the initial decrease for small radial distances is very weak or missing.

## C. Interstitials

The radial distributions of interstitials are shown in Fig. 9 for the pure cells, and in Fig. 10 for the cells with inclusions. For pure Fe the interstitial distributions show peaks that are some distance from the core of the initial cascade, for all recoil energies when the temperature is 600 K and above. The distributions stretch further out than for vacancies, indicating that the interstitials are mainly located further out from the initial cascade core than the vacancies. For the pure carbides the interstitial distributions show no pronounced peaks.

For the cells with a carbide inclusion the radial interstitial distributions either decrease mono- tonically with radial distances, or first increase out to about 15 Å and then decrease. The qualitative radial behavior is closer to the antisites than the vacancies. The initial increase seen in the case of vacancies is now missing or much weaker than for the vacancies.

In other words, close to the center of the cascade there are more vacancies than interstitials — for all simulated cell types — which is consistent with the Brinkman picture of a cascade.³¹ For the cells with inclusions there is a pile-up of defects at a radial distance slightly lower than the initial radius of the inclusion. This effect is of course not seen for the pure cells where there is no interface. Visual inspection of cascades suggests this pile-up is simply due to the fact that the bulk of the cascade is restricted to the inclusion and its inner interface.

This effect may or may not be present in real steels with carbide inclusions, due to the fact that in this study the interface berween carbide and ferrite was not optimized in detail. A careful energy optimization of the interface, possibly using long-time Monte Carlo simulations, followed by cascade simulations, would perhaps yield different results.

![](./images/814514348457197569_15.jpg)

FIG. 12. Clustering fractions of vacancies and interstitials as a function of recoil energy for cells with inclusions. First row: Vacancies. Second row: Interstitials. Left column: Fe₃C inclusion. Right column: Cr₂₃C₆ inclusion.

## D. Clustering of vacancies and interstitials

The fractions of vacancies and interstitials in clusters are shown in Fig. 11 for the pure cells and in Fig. 12 for the cells with inclusions. For pure Fe the values are smaller than for all the other cells. There is an overall increase with recoil energy, but the maximum fraction never goes over 0.4 (40%). The present result is consistent with previous simulation studies of pure Fe.²⁸⁻³⁰

For pure carbide cells and the cells with inclusions the clustering fractions also increase with energy. In the latter cases the fraction reaches a plateau at the highest energies, where the fraction stabilizes at a value of 0.6 – 0.7.

For the cells with inclusions the clustering fraction increases faster with temperature for the lower recoil energies than for the higher ones, suggesting that the clustering at low energies is sensitive to temperature.

## IV. CONCLUSIONS

Molecular dynamics simulations of bulk cascades have been carried out for ferrite cells contain- ing Fe₃C and Cr₂₃C₆ inclusions, as well as cells consisting of pure ferrite, pure cementite (Fe₃C), pure Cr₂₃C₆, as a function of recoil energy and temperature. The number of point defects, such as antisites, vacancies, and interstitials, their clustering fraction, as well as radial distributions, have been calculated for all cell types. Comparisons have been made between the pure cells and those with inclusions. The overall tendency is that the number of defects as well as the clustering fraction in- creases with energy and temperature. Radial distributions indicate that the interface between carbide and host restricts the cascade damage to the inclusion, as verified by visual inspection of cascade simulations. Peaks in the distributions appear at radial distances slightly smaller than the initial radius of the carbide inclusions. Larger number of defects are formed, mainly inside the inclusions, than in cells containing only a pure version of the carbide.

## ACKNOWLEDGMENTS

The molecular dynamics calculations presented in this article have been carried out within the CSC's computating environment. CSC is the Finnish IT center for science and is owned by the Min- istry of Education. The research has been carried out with financial support from the Academy of Finland (contracts number 259249 and 264911).

1 H. J. Goldschmidth, *Interstitial alloys* (Butterworths, London, U.K., 1967).
2 G. R. Odette, M. J. Alinger, and B. D. Wirth, "Recent developments in irradiation-resistant steels," *Annual Rev. Mater. Sci.* 38, 471–503 (2008).
3 R. J. Kurtz, A. Alamo, E. Lucon, Q. Huang, S. Jitsukawa, A. Kimura, R. L. Klueh, G. R. Odette, C. Petersen, M. A. Sokolov, P. Spätig, and J. W. Rensman, "Recent progress toward development of reduced activation ferritic/martensitic steels for fusion structural applications," *J. Nucl. Mater.* 386-388, 411–417 (2009).
4 S. J. Zinkle and J. T. Busby, "Structural materials for fission and fusion energy," *Materials Today* 12, 12–19 (2009).
5 S. J. Zinkle and L. L. Snead, "Designing radiation resistance in materials for fusion energy," *Annual Review of Materials Research* 44, 241–267 (2014), DOI: 10.1146/annurev-matsci-070813-113627.
6 V. Rybin, Y. Trushin, F. Fedorov, and V. Kharlamov, "Special features of the effect of oversized impurities on the cascade development in alpha-iron alloys containing special carbides," *Tech. Phys. Lett.* 26, 876–878 (2000).
7 J.-W. Jang, B.-J. Lee, and J.-H. Hong, "Influence of Cu, Cr and C on the irradiation defect in Fe: A molecular dynamics simulation study," *J. Nucl. Mater.* 373, 28–38 (2008).
8 A. F. Calder, D. J. Bacon, A. V. Barashev, and Y. N. Osetsky, "Computer simulation of cascade damage in alpha-iron with carbon in solution," *J. Nucl. Mater.* 382, 91–95 (2008).
9 D. Terentyev, N. Anento, and A. Serra, "Interaction of dislocations with carbon-decorated dislocation loops in bcc Fe: an atomistic study," *J. Phys. Cond. Matter* 24 (2012), 10.1088/0953-8984/24/45/455402.
10 Y. Abe, T. Suzudo, S. Jitsukawa, T. Tsuru, and T. Tsukada, "EFFECTS OF CARBON IMPURITY ON MICROSTRUC- TURAL EVOLUTION IN IRRADIATED alpha-IRON," *Fusion Science Techn.* 62, 139–144 (2012).
11 N. Anento and A. Serra, "Carbon-vacancy complexes as traps for self-interstitial clusters in Fe-C alloys," *J. Nucl. Mater.* 440, 236–242 (2013).
12 V. Jansson and L. Malerba, "Simulation of the nanostructure evolution under irradiation in Fe-C alloys," *J. Nucl. Mater.* 443, 274–285 (2013).
13 F. Granberg, D. Terentyev, K. O. E. Henriksson, F. Djurabekova, and K. Nordlund, "Interaction of dislocations with carbides in BCC Fe studied by molecular dynamics," *Fusion Science and Technology* 66, 283–288 (2014), ICFRM-16 conference paper.
14 K. O. E. Henriksson, N. Sandberg, and J. Wallenius, "Carbides in stainless steels: Results from ab initio investigations," *Appl. Phys. Lett.* 93, 191912 (2008).
15 H. J. C. Berendsen, J. P. M. Postma, W. F. van Gunsteren, A. D. Nola, and J. R. Haak, "Molecular dynamics with coupling to an external bath," *J. Chem. Phys.* 81, 3684–3690 (1984).
16 PARCAS computer code, K. Nordlund. The main principles of the molecular dynamics algorithm are presented in Refs. 17 and 18. The adaptive time step and electronic stopping algorithms are the same as in Ref. 19.
17 K. Nordlund, M. Ghaly, R. S. Averback, M. Caturla, T. Diaz de la Rubia, and J. Tarus, "Defect production in collision cascades in elemental semiconductors and fcc metals," *Phys. Rev. B* 57, 7556–7570 (1998).
18 M. Ghaly, K. Nordlund, and R. S. Averback, "Molecular dynamics investigations of surface damage produced by kev self-bombardment of solids," *Phil. Mag. A* 79, 795 (1999).
19 K. Nordlund, "Molecular dynamics simulation of ion ranges in the 1 – 100 kev energy range," *Comput. Mater. Sci.* 3, 448 (1995).
20 K. O. E. Henriksson, C. Björkas, and K. Nordlund, "Atomistic simulations of stainless steels: a many-body potential for the Fe-Cr-C system," *J. Phys. Cond. Matter* 25, 445401 (2013).
21 K. O. E. Henriksson and K. Nordlund, "Mechanical and elastic changes in cementite Fe₃C subjected to cumulative 1 keV Fe recoils," *Nucl. Instr. Meth. Phys. Res. B* 338, 119–125 (2014).
22 J. Byggmästär, F. Granberg, A. Kuronen, K. Nordlund, and K. O. E. Henriksson, "Tensile testing of fe and fecr nanowires using molecular dynamics simulations," *J. Appl. Phys.* 117, 014313 (2015), http://dx.doi.org/10.1063/1.4905314.
23 K. O. E. Henriksson, "Cascades in model steels: the effect of cementite (Fe₃C) and Cr₂₃C₆ particles on short-term crystal damage," *Nucl. Instr. Meth. Phys. Res. B* 352, 36–38 (2015), http://dx.doi.org/10.1016/j.nimb.2014.11.112.
24 K. O. E. Henriksson and K. Nordlund, "Molecular dynamics simulations of cascades in strained carbide inclusions embedded in α-iron," *AIP Advances.* 5, 117152 (2015), http://dx.doi.org/10.1063/1.4936883.
25 J. F. Ziegler, J. P. Biersack, and U. Littmark, *The stopping and range of ions in matter* (Pergamon, New York, U.S.A., 1985).
26 K. Arstila and J. F. Ziegler, "zbl96," computer program (1996).
27 N. W. Ashcroft and N. D. Mermin, *Solid state physics* (Saunders College, Philadelphia, PA, USA, 1976).
28 R. Stoller, G. Odette, and B. Wirth, "Primary damage formation in bcc iron," *J. Nucl. Mater.* 251, 49–60 (1997), proceedings of the International Workshop on Defect Production, Accumulation and Materials Performance in an Irradiation Environ- ment.
29 D. Bacon, Y. Osetsky, R. Stoller, and R. Voskoboinikov, "{MD} description of damage production in displacement cascades in copper and α-iron," *J. Nucl. Mater.* 323, 152–162 (2003), proceedings of the Second {IEA} Fusion Materials Agreement Workshop on Modeling and Experimental Validation.
30 C. Bjrkas, K. Nordlund, L. Malerba, D. Terentyev, and P. Olsson, "Simulation of displacement cascades in fe90cr10 using a two band model potential," *J. Nucl. Mater.* 372, 312–317 (2008).
31 J. A. Brinkman, "On the nature of radiation damage in metals," *J. Appl. Phys.* 25, 961 (1954).