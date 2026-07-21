This article was downloaded by: [UOV University of Oviedo]
On: 14 November 2014, At: 01:04
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811951289922486273_1.jpg)

Molecular Simulation

Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/gmos20

New software for finding transition states by probing accessible, or ergodic, regions

S. M. Woodley $^{a}$ & A. M. Walker $^{b}$

$^{a}$ DFRL, Department of Chemistry, University College London, London, UK
$^{b}$ Department of Earth Sciences, University of Cambridge, Cambridge, UK
Published online: 27 Jul 2010.

To cite this article: S. M. Woodley & A. M. Walker (2007) New software for finding transition states by probing accessible, or ergodic, regions, Molecular Simulation, 33:15, 1229-1231, DOI: 10.1080/08927020701714579

To link to this article: http://dx.doi.org/10.1080/08927020701714579

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# New software for finding transition states by probing accessible, or ergodic, regions

S. M. WOODLEY†* and A. M. WALKER‡

†DFRL, Department of Chemistry, University College London, London, UK
‡Department of Earth Sciences, University of Cambridge, Cambridge, UK

(Received August 2007; in final form September 2007)

An automated, iterative approach to finding the lowest energy, ionic diffusion paths through a periodic structure has been developed within our new code (written in FORTRAN 77 and named Bubble). The approach is quite general in that it can be applied to find, at a chosen temperature, the accessible (ergodic) regions of a hyper-surface, which is defined across a uniform grid [1]. We describe both our implementation within the Bubble code and its application to locating the approximate transition states for Mg interstitial diffusion in forsterite, which can then be refined using standard transition state searching [2].

Keywords: Ionic diffusion; Ergodic regions, Software; Transition states

An automated, iterative approach to finding the lowest energy, ionic diffusion paths through a periodic structure has been developed within our new code (written in FORTRAN 77 and named Bubble). The approach is quite general in that it can be applied to find, at a chosen temperature, the accessible (ergodic) regions of a hyper-surface, which is defined across a uniform grid [1]. We describe both our implementation within the Bubble code and its application to locating the approximate transition states for Mg interstitial diffusion in forsterite, which can then be refined using standard transition state searching [2].

In computational studies of diffusion within ionic crystals, it is necessary to be able to identify transition states, which are the least stable atomic configurations through which the system must evolve during an individual hopping event. Transition states, or saddle points, are represented by particular first-order turning points on a $(3N-3)$ dimensional energy hyper-surface, dimensions of which are the atomic coordinates. We initially require the approximate location and configuration of the relevant turning point, defined on a three-dimensional subspace where the diffusing atom is held fixed and the other atoms relaxed so as to minimise the lattice energy. For vacancy diffusion the approximate configuration of the transition state is known (broadly, an interstitial located somewhere between two lattice sites), but for interstitial diffusion the configuration of the transition state can be less obvious. Thus we evaluate a large area of the potential energy surface, as a function of the moving interstitial magnesium ion position. More precisely, the diffusing Mg(II) interstitial was fixed on a uniform grid covering the whole symmetry irreducible portion of the unit cell, whilst the ions in the extended neighbourhood were relaxed. Once this potential energy surface has been mapped, the problem becomes one of finding suitable approximate saddle points: the grid of energy points becomes the input data for our Bubble code to search.

A flow chart of the Bubble code is shown in figure 1. For ease of explanation consider an analogous problem on a two dimensional topography, discretised over a regular $n\times m$ grid, where height represents the energy. In our example the grid spans the $3\times3$ supercell of the crystal. The lowest point, or global minimum (GM), in the central unit cell is located by comparing all data. Next the code finds the lowest paths to the equivalent points in the adjacent unit cells; the highest point along such a path being the transition point. Imagine the effect of pouring water onto the GM of the central unit cell. As the basin containing the GM fills, water may spill out into higher basins. Eventually, one of the surrounding equivalent lowest basins will flood. The vector from the central GM to one of the

*Corresponding author. Email: uccasmw@ucl.ac.uk

Molecular Simulation
ISSN 0892-7022 print/ISSN 1029-0435 online © 2007 Taylor & Francis
http://www.tandf.co.uk/journals
DOI: 10.1080/08927020701714579

![](./images/811951289922486273_2.jpg)

Figure 1. Flow chart of the Bubble code: solid arrowheads of solid (broken) lines indicate direction of yes (no).

newly wet GM is the direction of diffusion. At this stage, one of the highest wet points is the transition state from one GM to the other. Adding more water will allow the transition states in the other directions to be found.

In our simulation, initially all grid points, apart from the lowest point in the central unit cell, are labelled as dry. Each time the water level is raised, the relative height of dry grid points that are nearest neighbours to wet grid points are checked; if below the water level then it is labelled as wet. Even for the smallest rise in water level, it is important to check the nearest neighbouring dry grid points to any newly wet points as flooding into neighbouring basins may occur. Moreover, grid points with a height that is higher than the previous water level and that have at least one neighbouring dry grid point with a height lower than the previous water level are labelled (coordinates stored) as possible key saddle points. Each time the water level is raised only the wet grid points that

![](./images/811951289922486273_3.jpg)

(a) The global minimum
(b) Just prior to reaching a tran-
sition state
(c) After reaching the transition
state

Figure 2. The growing bubble marks the accessible volume for hydrogen diffusion in forsterite crystal structure at a temperature (a) near 0K, (b) just below and (c) above the transition temperature.

define the current edge of the water pool need to be considered. To improve the efficiency of our code (CPU time requirements), the latter coordinates are stored in memory so that loops over all grid points are reduced to loops over the grid points at the water's edge. Note that the edge of the expanding pool of water marks the boundary of the most stable ergodic region, i.e. accessible area for the diffusing ion at a defined water depth, or temperature. (By pouring water onto a different local minimum, we can effectively investigate the shape/size of higher energy ergodic regions). In the actual case of diffusion in a crystal, the system is periodic in three directions and we thus simulate an expanding bubble on a 3D grid and the code loops over grid points that define the surface of this bubble (see figure 2).

The speed of the Bubble code depends upon both the number of grid points (which in turn depends on the required accuracy and system size) and the step size for the water level. Upon flooding into a basin containing one of the periodic images of the GM, the previous surface of the bubble can be reloaded and a smaller step taken so to reduce the number of candidate points. (Alternatively, although less efficient, as the code requires less than a minute on a typical desktop computer, successive runs of the code with ever decreasing step size could be performed). Once the approximate transition states are located, the second order transition state search can be implemented to allow for refinement of the transition structure with motion of the diffusing ion away from the grid points. In our example, a grid of $20 \times 40 \times 20$ points across the unit cell for forsterite (two neighbouring grid points $0.25$ Å apart) was sufficient. The Bubble code can also employ the appropriate space group symmetry, so reducing the 16,000 energy calculations to a more manageable 2000.

From experimental data [3], the mechanism of diffusion in forsterite is uncertain. Using Bubble, as well as finding the migration paths for diffusion, it was found that interstitial Mg diffusion has a higher activation barrier than O vacancy diffusion in all three crystallographic directions, (e.g. 3.13 compared to 0.72 eV in the [001] direction) so suggesting the mechanism is by vacancy diffusion [4].

### References

[1] J.C. Schön, H. Putz, M. Jansen. Studying the energy hypersurface of continuous system-The threshold algorithm. J. Phys.-Conden. Matt., 8, 143 (1996).
[2] A. Banerjee, N. Adams, J. Simons, R. Shepard. Search for stationary points on surfaces. J. Phys. Chem., 89, 52 (1985).
[3] S. Chakraborty. Rates and mechanisms of Fe-Mg interdiffusion in olivine at 980-1300°C. J. Geophys. Res., 120, 12317 (1997).
[4] A.M. Walker, S.M. Woodley, B. Slater, K. Wright. A computational study of magnesium point defects and diffusion in forsterite, Submitted.