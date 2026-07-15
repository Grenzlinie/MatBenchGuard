# MONTE CARLO SIMULATION OF DISLOCATION-NUCLEATED ETCHING OF SILICON {111} SURFACES

DONALD L. WOODRASKA, JASON LACOSSE, AND JOHN A. JASZCZAK
Michigan Technological University, Department of Physics, 1400 Townsend Dr.,
Houghton, MI 49931-1295

## ABSTRACT

We investigate equilibrium properties and thermal etching of the {111} surfaces of silicon, both with and without perpendicular intersecting dislocations, using Monte Carlo computer simulation. A modified solid-on-solid (SOS) approach is employed which realizes the correct diamond-cubic (DC) crystal structure. Nearest-neighbor interactions are incorporated to model the bonding, while the effects of a dislocation are incorporated by the addition of an energy field modeled as a core region and an elastic strained region. Dislocations are seen to nucleate the etching process and result in the formation of etch pits. Etch rates and etch-pit morphologies are investigated as a function of the chemical potential driving force for etching, the temperature, and the energy parameters used to model the dislocation.

## INTRODUCTION

Tremendous scientific developments and technological applications have taken place over the last half-century related to crystal surfaces and crystal growth [1]. Nevertheless, the structure and dynamics of solid surfaces are still rich areas for research, particularly with the development of new crystal growth technologies and the increasing power of computational facilities to study them. Of particular practical interest for study are silicon and structurally related materials, which continue to be of great technological importance. The science of silicon crystal growth has allowed for a continual increase in both the size of single-crystal silicon wafers and the density of electronic components fabricated on them. Selective chemical and plasma etching techniques are currently used by the semiconductor industry to reveal the dislocation structure of crystals, as well as to orient and clean surfaces, and ultimately to fabricate patterns for devices [2]. Plasmas are also essential for low-temperature, thin-layer deposition of dielectric materials for insulation and encapsulation of circuits [3]. As device size decreases, however, more stringent controls of etch profile anisotropy and selectivity will require significantly increased control and understanding of plasma etching processes. Plasma-based materials processing technologies are increasingly important for characterizing crystal quality, fabrication of devices at new, smaller length scales, and possibly also in the development of three-dimensional device fabrication.

In this study we present preliminary results of Monte Carlo simulations of equilibrium properties and thermal etching of silicon {111} surfaces with intersecting dislocations. Several etch-pit morphologies associated with dislocations have been observed experimentally on {111} and {100} silicon surfaces by chemical etching, and there is evidence that the type of dislocation is one of the factors influencing observed morphologies. While some etch pits have flat bottoms, others have shapes of negative pyramids. Dislocations on silicon {111} surfaces have been revealed only recently by reactive ion plasma etching [4]. Etch pit morphologies on diamond surfaces are similar to those on silicon and have also been of interest for some time [5]. The aim of our studies is to identify, model and investigate the consequences of critical factors influencing etching processes at dislocations intersecting surfaces during wet chemical etching and plasma (fluorine-based and others) etching. First-principles and molecular dynamics [6] studies are proving useful for understanding local interactions of fluorine with the silicon surfaces; however, simulation size and time constraints render them impractical for use to study such processes as etching over relatively long time scales and on large surfaces with intersecting dislocations.

For several decades Monte Carlo (MC) computer simulations of model systems have been used to study a large variety of equilibrium and dynamical phenomena associated with crystal surfaces

Mat. Res. Soc. Symp. Proc. Vol. 389 © 1995 Materials Research Society

[7]. MC simulations have also been used to study growth on facets of perfect crystals [8], and facets with intersecting screw dislocations [9,10]. MC studies of crystal surface etching have not been carried out to the same extent as equilibrium and growth simulations. These studies have primarily considered the dissolution kinetics and morphology of perfect crystal faces [11], steps and edges [12]. Some studies of dissolution have also been done on surfaces intersecting screw dislocations [7], focusing on the geometrical effect of the resulting perpetual step and the resulting growth or etch spirals. Gilmer has performed MC simulations on a simple cubic crystal with a small columnar hole perpendicular to the surface that serves as a site for step nucleation during etching [13], but effects of elastic and core energies of dislocations on etching were not considered. Liu, Van der Eerden, and Bennema [14] have considered the effects of dislocation energies on the opening and closing of a hollow dislocation core (with the dislocation axis normal to the surface) using MC simulation of a (001) surface of a simple cubic crystal using the SOS approximation. Based on earlier work [15], an effective, cylindrical, strain-energy field was employed. In the presence of the dislocation strain-energy field, etch rates and the opening or closing the dislocation core were investigated under various chemical potential driving forces, temperatures, and strain-energy densities.

## COMPUTATIONAL METHOD

In order to focus on statistical mechanical and kinetic behavior, and in order to simulate relatively large surfaces efficiently, we have developed a solid-on-solid (SOS) model for {111} surfaces of crystals with diamond cubic (DC) structure. While SOS models technically exclude voids and vacancies, such are included to a degree in our model. The DC structure is divided into columns of atoms, each with a specified height defining the surface. For a [111] DC surface, it is natural to divide the structure into three distinct types of columns, A, B, and C (Fig. 1). Each column can only terminate in certain "sheets", depending on the type of column and the type of sheet (a, b or c), where a sheet of atoms is separated from another by a layer of bonds parallel to <111> (Fig. 2). For example, should sheet n in Fig. 2 be composed of A and C type atoms, sheet n-1 would be composed of B and C types and sheet n+1 would be composed of A and B types. Depending on which sheet a column of atoms of a particular type terminates during any point of the simulation, one can determine the nature and direction of nearest-neighbor bonding. Periodic border conditions are used throughout to minimize finite-size effects.

![](./images/811669797287755777_1.jpg)

Fig. 1. Schematic of the silicon structure projected on (111). Each circle represents a solid-on-solid column of atoms at heights dictated by the diamond cubic structure, grouped according A, B, and C types.

Metropolis MC is implemented as follows [16,17]. A single MC step consists of selecting a surface site (in either a random or a staggered but sequential fashion), choosing at random to increase or decrease the surface height by one unit, and calculating the change in Hill energy, $\Delta \mathrm{H} \equiv \Delta \mathrm{E}_{\mathrm{b}}-\Delta \mu \Delta \mathrm{N}$, for the proposed move. $\Delta \mathrm{E}_{\mathrm{b}}$ is the change in broken-bond energy, and $\Delta \mathrm{N}= \pm 1$ is the change in column height. MC moves with $\Delta \mathrm{H} \leq 0$ were automatically accepted, while moves with $\Delta \mathrm{H}>0$ are accepted with probability $\exp (-\beta \Delta \mathrm{H})$, where $\beta \equiv 1 / \mathrm{k}_{\mathrm{B}} \mathrm{T}, \mathrm{k}_{\mathrm{B}}$ is the Boltzmann constant, and T is the temperature. Energy and temperature are scaled by the nearest-neighbor bond energy, J, which for silicon is 0.96 eV. We refer to the basic unit of time as a

![](./images/811669797287755777_2.jpg)

Monte Carlo sweep (MCS), which is one MC step per surface site.

The relevant dislocation types are the screw and mixed $60^\circ$ dislocations, each of the $1/2<110>\{111\}$ slip system. A dislocation along a $<111>$ direction has been incorporated into our model solely through an energy field associated with a perfect mixed $60^\circ$ dislocation. The additional energy per atom inside the dislocation core is parameterized based on atomistic simulations by Nandedkar and Narayan [18] using a Stillinger-Weber potential. The additional energy per atom outside the dislocation core varies inversely with the square of the distance of the atoms from the core radius. Because the dislocations lie in the $\{111\}$ glide planes, the dislocation lines are generally inclined with respect to the surface and etching results in etch pits of lower symmetry than one would expect for etch pits nucleated at dislocations perpendicular to the surface. While image forces acting on the dislocation lines due to the presence of the surface will tend to bend the dislocation lines at the surface, the dislocation lines are not expected to be perpendicular to the surface except at high temperatures. Simulations of dislocation lines inclined with respect to the surface will be undertaken in future studies, as will inclusion of steps resulting from screw components. Possible effects of surface reconstruction are also presently ignored.

## RESULTS AND DISCUSSION

### Equilibrium
One of the most fundamental equilibrium phenomena associated with faceted (planar at T=0) surfaces is the roughening transition. Above the roughening temperature, $T_R$, the energy for the formation of a step on a faceted surface vanishes, the faceted interface becomes microscopically rough and macroscopically curved on the equilibrium crystal shape [7,19]. The roughening transition influences both the correlation lengths in equilibrium and to a large extent much of the dynamics during growth or etching.

Calculation of the average interface width, surface specific heat, and height-difference correlation functions give a consistent indication that $T_R \approx 0.75$ for our SOS model of Si $\{111\}$. This $T_R$ is in satisfactorily agreement with that reported by Van Enckevort and Van der Eerden [20] for a non-SOS model of diamond $\{111\}$ surfaces. Variation of the step energy as a function of temperature is currently under investigation to more accurately determine $T_R$.

The surface specific heat, $C_V$, computed by the fluctuations in the surface energy [16], is a useful indicator of roughening transitions. For Si $\{111\}$ a pseudoroughening transition [16] is indicated in Fig. 3 by the peak in $C_V$ at $k_BT/J$=0.35, and is associated with fluctuations of the surface (Fig. 4) among layers within a periodic unit [the periodic unit in Si along $<111>$ contains

three energetically equivalent slices (see Fig. 2)].

![](./images/811669797287755777_3.jpg)

Fig. 3. Surface
specific heat, $C_V$, in
units of $k_B$ (per
atom), versus
temperature for a
surface of 2,700
surface sites. Each
data point represents
results of a 500,000
MCS simulation.

![](./images/811669797287755777_4.jpg)

Fig. 4. Spline-fit silicon (111) surfaces composed of 243 surface sites at
(a) $k_BT = 0.3$ J and (b) $k_BT = 0.4$ J, each after 400,000 MCS.

## Etching

Etching of Si {111} surfaces is simulated both with and without dislocations intersecting the surface. For surfaces without defects, etching takes place by activated nucleation of two-dimensional critical island-pits and subsequent layer etching at low T and $\Delta\mu$, analogous to growth behavior [7]. Nucleation, etching and coalescence of two-dimensional island-pits is shown on a surface in Fig. 5. Under such conditions below dynamical roughening the etch rates normal to the surface vary as $\exp(-\beta E_A)$, where the activation barrier, $E_A$,depends on the geometrical factors, the free energy of a step, and $\Delta\mu^{-1}$. When $\Delta\mu$ is sufficiently large such that $E_A \approx k_BT$, critical nuclei are formed thermally, the etch rate is proportional to $\Delta\mu$, and the surface is said to be dynamically rough [7,17].

In the presence of an intersecting dislocation, etching of the Si {111} surfaces is nucleated at the dislocation. Figure 6 shows a triangular-pyramid etch pit nucleated on a Si (111) surface at a dislocation along [111], after etching 50,000 MCS. Etch-pits nucleated without and with a dislocation are oriented as is most common experimentally: anti-parallel to the triangular {111} facets of an octahedral crystal shape [4,5]. Rates for etching normal to the surface, as a

![](./images/811669797287755777_5.jpg)

Fig. 5. Etched,
dislocation-free Si
(111) surface (spline
fit) composed of
11,907 surface sites
after 4600 MCS at
$\mathrm{k_BT}=0.03\mathrm{J}$ and
$\Delta\mu=-0.8\mathrm{J}$.

![](./images/811669797287755777_6.jpg)

Fig. 6. Etched Si
(111) surface (spline
fit) composed of
11,907 surface sites
with a perfect mixed
$60^\circ$ dislocation with
core radius $5\mathring{A}$ and
core energy $0.95\mathrm{eV/\mathring{A}}$
[18], after 50,000
MCS at $\mathrm{k_BT}=0.05\mathrm{J}$
and $\Delta\mu=-0.5\mathrm{J}$.

![](./images/811669797287755777_7.jpg)

Fig. 7. Rates of
etching normal to the
surface as a function
of chemical potential
driving force $\Delta\mu$ at
several temperatures
for an 11,907-site Si
(111) surface with a
dislocation as in
Fig. 6. Rates R are
in units of bond-
lengths ($d=2.35\mathring{A}$)
per Monte Carlo
sweep (MCS).

function of $\Delta \mu$ (Fig. 7) are very similar to, though higher than, etch rates of dislocation-free surfaces. More detailed analyses of etch rates near the dislocation core are in progress to study the effects of the dislocation core radius and energy parameters on nucleation of steps at the core.

## CONCLUSIONS AND OUTLOOK
A modified SOS model for Si {111} surfaces, correctly accounting for the DC structure, promises to be an efficient simulation method for investigating equilibrium and dynamical properties of such sufaces. Equilibrium results are in satisfactory agreement with non-SOS models yet allow for substantially larger and longer simulations to be conducted. Dislocations intersecting the surface are shown to nucleate etching and produce pyramidal etch pits. Continuing studies are will quantify the surface roughness, roughening temperature, energy barriers for nucleation, etch rates both near and away from dislocations, dynamical roughening, and growth. Work is underway to include surface diffusion, incline the dislocation lines, include surface steps emanating from screw components, dynamically move the dislocation along the surface, and finally, to develop methods to simulate plasma etching of Si surfaces with dislocations.

## ACKNOWLEDGMENTS
The authors are grateful to E. M. Nadgorny and A. V. Pakhomov for helpful discussions about chemical and plasma-based etching, and for sharing their experimental results.

## REFERENCES
1. J. N. Sherwood, Faraday Discuss. **95**, 1 (1993).
2. R. B. Heimann. In, *Silicon Chemical Etching*. J. Grabmaier, editor. (Springer-Verlag, Berlin, 1982).
3. National Research Council, *Plasma Processing of Materials: Scientific Opportunities and Technological Challenges* (National Academy Press, Washington, 1991).
4. A. V. Pakhomov and E. M. Nadgorny, Bull. APS. **39(1)**, 930 (1994).
5. Y. L. Orlov, *The Mineralogy of the Diamond* (Wiley, New York, 1973) pp. 82-87.
6. P. C. Weakliem, C. J. Wu, and E. A. Carter, Phys. Rev. Lett. **69**, 200 (1992); L. E. Carter and E. A. Carter, Surf. Sci. **323**, 39 (1995).
7. For reviews, see: H. Müller-Krumbhaar, in *Monte Carlo Methods in Statistical Physics*, ed. K. Binder (Springer-Verlag, Berlin, 1986) p. 261; J. D. Weeks and G. H. Gilmer, Advances in Chemical Physics, **40**, 157 (1979); J. P. van der Eerden and P. Bennema, Prog. Crystal Growth Charact. **1**, 219 (1978).
8. G. H. Gilmer and P. Bennema, J. Crystal Growth **13/14**, 148 (1972).
9. G. H. Gilmer, J. Crystal Growth **35**, 15 (1976).
10. R. H. Swendsen, P. J. Kortman, D. P. Landau and H. Müller-Krumbhaar, J. Crystal Growth **35**, 73 (1976).
11. C. S. Kohli and M. B. Ives, J. Crystal Growth **16**, 123 (1972).
12. V. K. W. Cheng and B. A. W. Coller, J. Crystal Growth **84**, 436 (1987).
13. G. H. Gilmer, J. Crystal Growth **42**, 3 (1977).
14. G.-Z. Liu, J. P. van der Eerden, and P. Bennema, J. Crystal Growth **58**, 152 (1982) .
15. B. van der Hoek, J. P. van der Eerden, and P. Bennema, J. Crystal Growth **56**, 621 (1981).
16. J. A. Jaszczak, W. F. Saam and B. Yang, Phys. Rev. B **39**, 9289 (1989).
17. J. A. Jaszczak, W. F. Saam, and B. Yang, Phys. Rev. B **41**, 6864 (1990).
18. A. S. Nandedkar and J. Narayan, Phil. Mag. A. **61**, 873 (1990).
19. M. Wortis, in *Chemistry and Physics of Solid Surfaces* Vol. VII. R. Vanselow, editor. (Springer-Verlag, Berlin, 1988) p. 367.
20. W. J. P. Van Enckevort and J. P. Van der Eerden, J. Crystal Growth, **47**, 501 (1979).