# Computational Study on Surface Structure and Crystal Morphology of $\gamma$-Fe₂O₃: Toward Deterministic Synthesis of Nanocrystals

Roger C. Baetzold* and Hong Yang*

Department of Chemical Engineering, University of Rochester, Gavett Hall 206,
Rochester, New York 14627-0166

Received: June 23, 2003; In Final Form: October 20, 2003

This work is the first application of classical atomistic theory to a comprehensive treatment of $\gamma$-Fe₂O₃ surfaces. The surface energy and attachment energy of several low-index surfaces of $\gamma$-Fe₂O₃ have been calculated by the classical atomistic simulation methods. A mean-field approximation involving scaling the short-range potentials, charges, and force constants of the iron ions by a fraction corresponding to the partial occupation of octahedral iron sites in the spinel structure was employed. Reconstruction of the polar surfaces was required to remove the dipole perpendicular to the surface and to achieve structural stability. This was accomplished through the addition of vacancies. The two-dimensional periodic calculations were carried out with the MARVIN code. The (112) surface consisting of iron and oxygen ions had the smallest relaxed surface energy of 1.86 J/m², while several others including (001), (011), and (012) were within 0.1 J/m² of this value. The calculated surface energies of these planes were used in a Wulff plot to predict a polyhedral crystal habit for these crystals at thermodynamic equilibrium. The (111) surfaces terminated with iron ions had the smallest attachment energies, and an octahedral crystal with (001) facets is predicted for the growth morphology of $\gamma$-Fe₂O₃. Such surfaces possess iron ions in 3-fold coordination sites at 0.5 Å above the plane of oxygen ions, making them accessible to interact with adsorbed molecules. This information is relevant to understanding the growth of nanocrystals of $\gamma$-Fe₂O₃.

## Introduction

Synthesis of monodisperse nanometer-sized magnetic particles of metal alloys and metal oxides is an active research area because of their potential technological ramifications ranging from ultrahigh-density magnetic storage media,¹⁻⁵ to biological imaging, to carriers in biological molecule separations.⁶⁻¹⁰ Size, size distribution, shape, and dimensionality are important for the properties of these magnetic materials. Nanoparticles of various iron oxides (Fe₃O₄ and $\gamma$-Fe₂O₃ in particular) have been widely used in a range of biological applications.⁶,⁸,¹⁰⁻¹² We and others have recently been able to chemically synthesize highly monodisperse nanoparticles of iron oxides.¹³⁻¹⁹ We have further observed that the nanoparticles of cubic maghemite ($\gamma$-Fe₂O₃) can undergo morphological transformation from spherical into faceted shapes under moderate conditions.²⁰

In this paper, we present our computational study on surface structures and morphologies of $\gamma$-Fe₂O₃ crystals. By using classical atomistic calculations, we hope to determine theoretically the kinetic and thermodynamic stable surfaces and, in turn, derive the morphologies of this material under given conditions. The outcome of such studies could be very useful for designing synthetic conditions of $\gamma$-Fe₂O₃ nanoparticles.

Figure 1 shows the unit cell for $\gamma$-Fe₂O₃. The crystal structure of $\gamma$-Fe₂O₃ (cubic maghemite) is $Fd3m$ space group with cubic symmetry and a lattice constant of 8.35 Å.²¹ It has a spinel type structure, in which Fe³⁺ cations occupy the eight tetrahedral sites and additional 13¹/₃ Fe³⁺ cations occupy the 16 octahedral sites. All 32 oxygen sites are fully occupied. The classical atomistic simulation methods used in this paper for calculation of surface energy and attachment energy are based on the Born model and have been used to treat a variety of solid-state chemistry problems in ionic and covalent solids, such as transition metal compounds ranging from cuprate superconductors,²²,²³ binary oxides,²⁴ niobates,²⁵ and silver halide.²⁶ The basic potential model has also been applied to a variety of two-dimensional periodic solid surfaces which include spinels,²⁷,²⁸ ZnO,²⁹ ZnS,³⁰ FeS₂,³¹ and Al₂O₃.³² These methods have the characteristic of simplicity in concept, and yet they have proven to be valuable tools in conjunction with experiments. To the best of our knowledge, although the chemically related systems, such as Fe₃O₄³³ and $\alpha$-Fe₂O₃,³⁴,³⁵ and structurally similar spinel-type materials, including LiMn₂O₄/LiFe₅O₈,³⁶ MgAl₂O₄,²⁷ and ZnCr₂O₄,²⁸ have been treated with use of these methods, there has been no comprehensive study of $\gamma$-Fe₂O₃ with the classical

![](./images/812372348953952257_1.jpg)

**Figure 1.** The unit cell of $\gamma$-Fe₂O₃ showing the tetrahedral iron (in purple), octahedral iron (in green), and oxygen (in red) ions.

* Address correspondence to the authors at the following e-mail addresses: hongyang@che.rochester.edu (hy); baetzold@che.rochester.edu (rcb).

---

10.1021/jp035785k CCC: $25.00
© 2003 American Chemical Society
Published on Web 12/02/2003

atomistic simulation methods. The mean field approximation, which has been used previously for bulk crystal systems involving partial occupation of sites, and in the spinel solid solution system of $LiMn_{2}O_{4}$ and $LiF_{5}O_{8},^{36}$ is required in our present work because of the partial occupation of iron octahedral sites in $\gamma$-$Fe_{2}O_{3}$. The application of this approximation to solid surfaces has not been reported before.

### Method
#### Atomistic Simulations of Bulk $\gamma$-$Fe_{2}O_{3}$.
We use the atomistic simulation procedure to treat the crystal structure of $\gamma$-$Fe_{2}O_{3}$. The procedure is contained in the GULP (General Utilities Lattice Program) $^{37}$ for bulk crystals and the MARVIN program $^{38}$ for surface calculations. This approach is based upon the Born model and each ion contains its full formal charge. The polarizability of each ion is introduced through the shell model developed by Dick and Overhauser. $^{39}$ The charge is carried by a core of appropriate mass and a massless shell and the sum of the core and shell charges gives the total ion charge. The polarization energy is
$$E(d)=1/2kd^{2} \tag{1}$$
where $k$ is the spring constant for the particular ion and $d$ is the displacement of core and shell. The short-range interactions between ions are represented by Buckingham potentials
$$V(r)=A\exp(-r/\rho)-C/r^{6} \tag{2}$$
in which $r$ is the center-to-center distance between the shells of a pair of ions. The Buckingham potential between ions includes repulsive interactions between their charge clouds in the form of an exponential term containing $A$ and $\rho$ parameters, and an attractive van der Waals term containing $C$ as a parameter. The parameters are determined for empirical potentials by fitting to the structure, elastic, and dielectric properties of the crystal or calculated by ab initio methods.

To treat the unit cell of $\gamma$-$Fe_{2}O_{3}$ we have to account for the noninteger number of $13^{1}/_{3}Fe^{3+}$ cations in octahedral sites. The cubic unit cell was therefore enlarged by a factor of 3 in one direction to have integer numbers of atoms in the repeating cell. The expanded cell has a composition of $Fe_{64}O_{96}$ in which the 8 vacancies of iron ions are randomly distributed among the 72 octahedral sites. Although we have tested such a model, the size of this cell is not large enough to avoid deviations from the tetragonal structure when the structure is relaxed. Much larger unit cells would be required to apply this approach, and in the present work we turned to the mean field approximation. $^{37}$ This approximation is not formally implemented in Marvin, so we adjusted the input parameters. In this approach, we scale the charge, the Buckingham potential parameter $A$, and the shell force constant of each octahedral iron cation by the fractional occupancy of octahedral sites which is $^5/_6$. This also involves using a full occupancy of each octahedral site. This description corresponds to an average charge of +2.5 on each iron in the fully occupied 16 octahedral sites. It should be noted that this is an average charge on the sites. The local environment in the presence of vacancies could differ to some extent from what is achieved with the mean field approximation. This factor has to be accounted for in a specific calculation where such vacancies are present.

The potential parameters that we employ are taken from the work of Islam and Catlow on $Fe_{3}O_{4}.^{33}$ We employ their parameters with the exception of the octahedral iron ion charge, force constant, and Buckingham potential with the oxygen ion modified as described above. This Buckingham $A$ parameter was further increased by 10% to give the experimental relaxed lattice constant of $8.35\ \text{\AA}$ for $\gamma$-$Fe_{2}O_{3}$. It is unknown how this modification would affect potential transferability to other iron oxide systems. The potential parameters used in this work are given in Table 1.

<table>
<caption>TABLE 1: Parameters Used To Study the Surface and Morphology of $\gamma$-$Fe_{2}O_{3}$</caption>
<tr>
<td colspan="4">Buckingham Potential: $V(r)=A\exp(-r/\rho)-C/r^{6}$</td>
</tr>
<tr>
<td>interaction</td>
<td>$A$ (eV)</td>
<td>$\rho$ (Å)</td>
<td>$C$ (eV·Å⁶)</td>
</tr>
<tr>
<td>Fe,o−O</td>
<td>1011.5</td>
<td>0.3299</td>
<td>0.0</td>
</tr>
<tr>
<td>Fe,t−O</td>
<td>976.6</td>
<td>0.3299</td>
<td>0.0</td>
</tr>
<tr>
<td>O−O</td>
<td>22764.3</td>
<td>0.1490</td>
<td>27.88</td>
</tr>
<tr>
<td colspan="4">Shell Model Parameters</td>
</tr>
<tr>
<td>ion</td>
<td colspan="2">shell charge $|e|$</td>
<td>$k$ (eV·Å⁻²)</td>
</tr>
<tr>
<td>Fe,o</td>
<td colspan="2">4.47</td>
<td>253.9</td>
</tr>
<tr>
<td>Fe,t</td>
<td colspan="2">4.97</td>
<td>304.7</td>
</tr>
<tr>
<td>O</td>
<td colspan="2">−2.207</td>
<td>27.29</td>
</tr>
</table>

#### Surface Structures of $\gamma$-$Fe_{2}O_{3}$.
The surface region in our calculation is composed of a finite number of two-dimensional infinite planes formed by cutting the crystal along a particular Miller index $(hkl)$ plane. In each plane, a two-dimensional cell represents every site in the plane with appropriate translation vectors. Several of these cells in successive planes comprise the basic repeat unit of $\gamma$-$Fe_{2}O_{3}$ that contains the composition of the bulk crystal unit cell of 8 iron ions at the tetrahedral site Fe,t; $13^{1}/_{3}$ iron ions at the octahedral site Fe,o and 32 O ions. The translation vectors and ion coordinates in each cell are calculated in the MARVIN program by using the relaxed crystal coordinates determined in the GULP calculation.

We considered the low index surfaces containing planes with the largest interplanar spacing, since these are the most important planes morphologically predicted by the Bravais−Friedel−Donnay−Harker theory. $^{40}$ We treated the (001), (011), (111), (012), (112), and (122) surfaces of $\gamma$-$Fe_{2}O_{3}$ in this work. We found that each of these surfaces is polar since each plane parallel to the surface is charged, as has been found for similar spinel surfaces. $^{27,28}$ For polar surfaces of this type, a dipole exists normal to the surface that causes the electrostatic energy to diverge. $^{41}$ The surface is thus unstable and must reconstruct to become stable through a mechanism, such as formation of vacancy defects, formation of facets, or adsorption of charged species.

Harding has recently discussed a general solution to the problem of polar interfaces and addressed some spinel-type surfaces. $^{42}$ A formula for surfaces was developed to provide a means to achieve stability through quenching the surface dipole. In this formulation, a set of planes with net zero charge per repeating unit was considered and a factor $\alpha$ was defined to specify the charge that must be transferred from the cell in the top plane to achieve the zero dipole. Consider an array of planes containing a two-dimensional cell in the top plane having charge $Q_{1}$ and underlying cells of charge $Q_{j}$ at distance $r_{j}$ normal from the top cell. If the charge of the cell in the top plane is changed to $\alpha Q_{1}$ and the corresponding charge $(1-\alpha)Q_{1}$ is added to a new layer at the bottom of the stack of repeating units, the $\alpha$ factor satisfies the following equation $^{42}$
$$\alpha=1+\sum(Q_{j}r_{j})/(Q_{1}a_{0}) \tag{3}$$
where $a_{0}$ is the thickness of the repeating unit. The summation in eq 3 runs over each layer in the repeating unit. This formula

<table>
<caption>TABLE 2: Compositions of Planes in the Repeat Unit of $\gamma$-Fe₂O₃ for Different Surfaces</caption>
<thead>
<tr>
<th>surface</th>
<th>composition of planesª</th>
<th>no. of planesᵇ</th>
<th>av chargeᶜ</th>
</tr>
</thead>
<tbody>
<tr>
<td>001</td>
<td>2Fe,t</td>
<td>4</td>
<td>+6</td>
</tr>
<tr>
<td>001</td>
<td>4Fe,o; 8O</td>
<td>4</td>
<td>−6</td>
</tr>
<tr>
<td>011</td>
<td>4Fe,o; 4Fe,t; 8O</td>
<td>2</td>
<td>+6</td>
</tr>
<tr>
<td>011</td>
<td>4Fe,o;8O</td>
<td>2</td>
<td>−6</td>
</tr>
<tr>
<td>111</td>
<td>12Fe,o</td>
<td>1</td>
<td>+30</td>
</tr>
<tr>
<td>111</td>
<td>4Fe,o</td>
<td>1</td>
<td>+10</td>
</tr>
<tr>
<td>111</td>
<td>4Fe,t</td>
<td>1</td>
<td>+12</td>
</tr>
<tr>
<td>111</td>
<td>16O</td>
<td>1</td>
<td>−32</td>
</tr>
<tr>
<td>012</td>
<td>2Fe,t</td>
<td>4</td>
<td>+6</td>
</tr>
<tr>
<td>012</td>
<td>4Fe,o; 8O</td>
<td>4</td>
<td>−6</td>
</tr>
<tr>
<td>112</td>
<td>4Fe,o; 4Fe,t; 8O</td>
<td>2</td>
<td>+6</td>
</tr>
<tr>
<td>112</td>
<td>4Fe,o</td>
<td>2</td>
<td>−6</td>
</tr>
<tr>
<td>122</td>
<td>4Fe,o; 8O</td>
<td>4</td>
<td>−6</td>
</tr>
<tr>
<td>122</td>
<td>2Fe,t</td>
<td>4</td>
<td>+6</td>
</tr>
</tbody>
</table>

ª Number of ions per cell in a particular plane. ᵇ Number of planes in the repeating unit. ᶜ Average charge of the cell in the plane.

is applied to each surface of $\gamma$-Fe₂O₃ to obtain the final reconstructed and stable polar surfaces.

We have employed the MARVIN program³⁸ to study the surfaces of $\gamma$-Fe₂O₃. This is a static lattice simulation code for two-dimensional periodic systems of finite thickness. It employs the interatomic potentials described above where we have used the scaled parameters for iron ions at the octahedral sites, consistent with the mean field approximation. The entire surface unit is divided into two regions.²⁷⁻³² In region I, the ions are allowed to relax until there is zero force on each ion. In region II, which is attached to region I, the ions are fixed at the bulk positions determined in the GULP calculation. We varied the thicknesses of regions I and II to find region sizes such that the surface energy and structure become unchanged with further increases. We found that four repeat units in region I and six repeat units in region II gave converged results for (001), (011), and (111) surfaces. Five units in region I and nine units in region II were required for (012) and (112) surfaces; and six units in region I and twelve units in region II were used for (122) surfaces. This corresponds to an overall thickness of 83.5 Å in the case of (001) surfaces and somewhat less for the other surfaces. Equal numbers of ions were present in region I and region II for each termination of a given surface.

### Results

**Surface Reconstruction.** All of the surface planes comprising the low index surfaces of $\gamma$-Fe₂O₃ are polar. Table 2 shows the composition and sequence of alternating planes in the repeat unit. The number of these planes in the repeat unit is specified along with the average charge of the two-dimensional cell in each plane. It should be noted that either of the planes can terminate the crystal, and this increases the number of possible surfaces that need to be evaluated. All surfaces consist of a sequence of equally spaced alternating planes, except the (111) surfaces in which there is no alternate plane structure in the repeat unit. The planes can have a varying orientation related by symmetry as we scan through the repeating unit. For the oxygen plane in the (111) orientation, four ions are slightly out of plane with the other twelve, although our notation describes this as just one oxygen ion plane.

We applied Harding’s formula⁴² to each possible surface of $\gamma$-Fe₂O₃. The results are presented in Table 3. Most of the surfaces considered have an α factor of 0.5, since the charge alternates between equally spaced planes in the repeating unit. The exceptions are for the oxygen ion plane and the tetrahedral iron cation plane of the (111) surfaces. We next considered the

<table>
<caption>TABLE 3: Surfaces and Properties of $\gamma$-Fe₂O₃ª</caption>
<thead>
<tr>
<th>surface</th>
<th>compositionᵇ</th>
<th>α factor</th>
<th>ΔCᶜ</th>
<th>Δ compositionᵈ</th>
</tr>
</thead>
<tbody>
<tr>
<td>001</td>
<td>2Fe,t</td>
<td>0.5</td>
<td>−3</td>
<td>−Fe,t</td>
</tr>
<tr>
<td>001</td>
<td>4Fe,o; 8O</td>
<td>0.5</td>
<td>+3</td>
<td>−2Fe,o; −4O</td>
</tr>
<tr>
<td>011</td>
<td>4Fe,o; 4Fe,t; 8O</td>
<td>0.5</td>
<td>−3</td>
<td>−2Fe,o; −2Fe,t; −4O</td>
</tr>
<tr>
<td>011</td>
<td>4Fe,o; 8O</td>
<td>0.5</td>
<td>+3</td>
<td>−2Fe,o; −4O</td>
</tr>
<tr>
<td>111</td>
<td>12Fe,o</td>
<td>0.5</td>
<td>−15</td>
<td>−6Fe,o</td>
</tr>
<tr>
<td>111</td>
<td>4Fe,o</td>
<td>0.5</td>
<td>−5</td>
<td>−2Fe,o</td>
</tr>
<tr>
<td>111</td>
<td>4Fe,t</td>
<td>1.416664</td>
<td>+5</td>
<td>+2Fe,o</td>
</tr>
<tr>
<td>111</td>
<td>16O</td>
<td>0.531250</td>
<td>+15</td>
<td>−15Oᵉ</td>
</tr>
<tr>
<td>012</td>
<td>2Fe,t</td>
<td>0.5</td>
<td>−3</td>
<td>−Fe,t</td>
</tr>
<tr>
<td>012</td>
<td>4Fe,o; 8O</td>
<td>0.5</td>
<td>+3</td>
<td>−2Fe,o; −4O</td>
</tr>
<tr>
<td>112</td>
<td>4Fe,o; 4Fe,t; 8O</td>
<td>0.5</td>
<td>−3</td>
<td>−2Fe,o; −2Fe,t; −4O</td>
</tr>
<tr>
<td>112</td>
<td>4Fe,o; 8O</td>
<td>0.5</td>
<td>+3</td>
<td>−2Fe,o; −4O</td>
</tr>
<tr>
<td>122</td>
<td>2Fe,t</td>
<td>0.5</td>
<td>−3</td>
<td>−Fe,t</td>
</tr>
<tr>
<td>122</td>
<td>4Fe,o; 8O</td>
<td>0.5</td>
<td>+3</td>
<td>−2Fe,o; −4O</td>
</tr>
</tbody>
</table>

ª Fe,t is the iron ion occupying the tetrahedral site with +3 charge; Fe,o is the iron ion occupying the octahedral site with the average charge +2.5, corresponding to 5/6 occupancy by Fe³⁺. ᵇ Composition refers to numbers and the ions per cell before reconstruction. ᶜ ΔC is the charge added to the surface to quench the dipole, and −ΔC is the charge added to a new layer at the bottom of the stack of repeat units. ᵈ Δ composition is the change in surface composition needed to stabilize the surface. The ions removed (noted by a − sign) are added to a new layer at the bottom of repeating units. The ions added (noted by a + sign) are removed from the bottom of the stack of repeating units. ᵉ Cell area is doubled in each plane.

necessary change in charge of the surface plane to quench the dipole and achieve stability. This change in charge leads to a corresponding composition change of the surface cell. We could accomplish this change by creating integer numbers of surface vacancies per single cell for all cases except the oxygen (111) surface. For this surface we doubled the area of the cell in each plane to accommodate the required integer number of oxygen ion vacancies. In the case of the other (111) surface containing 4Fe,t and with α other than 0.5, we added two octahedral iron cations that each possesses +2.5 charges in this mean field approximation onto the top plane to stabilize the surface. These changes involve several vacancies and lead to many possible arrangements of the vacancies on the surface, which we examined in our calculations.

**Energy of Reconstructed Surfaces.** The surface energy corresponding to the energy difference of surface ions and bulk ions per unit area is calculated directly in the Marvin program.³⁸ It is defined according to the following equation

$$
\gamma=(E_{\mathrm{t}}-E_{\mathrm{b}}-nE_{\mathrm{cr}})/S \tag{4}
$$

where $\gamma$, $E_{\mathrm{cr}}$, $E_{\mathrm{t}}$, and $E_{\mathrm{b}}$ are surface energy, crystal energy, total energy of the surface simulation cell in Marvin for a given Miller index surface of area $S$ with $n$ unit cells, and the boundary energy that describes the interaction between the ions in regions I and II, respectively.³⁸ The quantity determined in our calculation is an internal energy and not a free energy, and no entropy term is considered, as is common in this type of calculation.²⁷⁻³² Since crystal habit is determined by the relative energies of different surfaces, we would not expect entropy effects to alter this ordering. A surface with low surface energy is more stable than that with high surface energy, thus the surface with the lowest energy represents the predicted result at equilibrium.

We computed the surface energies for all the reconstructed surfaces. As indicated in the previous section, there are several arrangements of vacancies that satisfy the requirement of quenching the surface dipole. For some surfaces such as those containing only two Fe³⁺ as in (001), (012), or (122), the sites

![](./images/812372348953952257_2.jpg)

Figure 2. The unrelaxed (001) surface of $\gamma$-Fe₂O₃ showing the unique sites for octahedral irons (in green) and oxygen ions (in red). The numbers next to the sites are used to identify the ions of interest.

<table>
<caption>TABLE 4: Calculated Surface Energies for Different Initial Vacancy Configurations of the (001) Surface Containing Fe₄O₈ᵃ</caption>
<thead>
<tr>
<th>Fe vacancies</th>
<th>O vacancies</th>
<th>unrelaxed $\gamma$ (J/m²)</th>
<th>relaxed $\gamma$ (J/m²)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1,2</td>
<td>3,4,5,6</td>
<td>17.58</td>
<td>1.99</td>
</tr>
<tr>
<td>1,2</td>
<td>1,2,4,6</td>
<td>7.07</td>
<td>1.97</td>
</tr>
<tr>
<td>1,2</td>
<td>1,2,5,6</td>
<td>8.29</td>
<td>2.08</td>
</tr>
<tr>
<td>1,2</td>
<td>1,2,3,4</td>
<td>6.01</td>
<td>2.79</td>
</tr>
<tr>
<td>1,2</td>
<td>5,6,7,8</td>
<td>17.58</td>
<td>2.05</td>
</tr>
<tr>
<td>1,2</td>
<td>2,3,6,7</td>
<td>8.06</td>
<td>2.49</td>
</tr>
<tr>
<td>1,3</td>
<td>1,2,3,4</td>
<td>9.80</td>
<td>4.34</td>
</tr>
<tr>
<td>1,3</td>
<td>1,2,5,6</td>
<td>6.29</td>
<td>2.04</td>
</tr>
<tr>
<td>1,3</td>
<td>1,2,7,8</td>
<td>9.80</td>
<td>2.03</td>
</tr>
<tr>
<td>1,3</td>
<td>2,4,6,8</td>
<td>8.15</td>
<td>2.10</td>
</tr>
<tr>
<td>1,3</td>
<td>2,3,6,7</td>
<td>6.07</td>
<td>2.03</td>
</tr>
<tr>
<td>2,4</td>
<td>3,4,5,6</td>
<td>10.32</td>
<td>3.42</td>
</tr>
<tr>
<td>2,4</td>
<td>1,2,7,8</td>
<td>9.80</td>
<td>4.61</td>
</tr>
<tr>
<td>2,3</td>
<td>3,4,5,6</td>
<td>6.01</td>
<td>2.48</td>
</tr>
<tr>
<td>2,3</td>
<td>2,3,4,5</td>
<td>5.86</td>
<td>2.12</td>
</tr>
<tr>
<td>2,3</td>
<td>1,2,3,4</td>
<td>6.01</td>
<td>2.48</td>
</tr>
<tr>
<td>2,3</td>
<td>1,2,5,6</td>
<td>8.29</td>
<td>4.46</td>
</tr>
<tr>
<td>2,3</td>
<td>1,3,5,7</td>
<td>10.15</td>
<td>2.25</td>
</tr>
<tr>
<td>2,3</td>
<td>1,4,5,8</td>
<td>8.06</td>
<td>2.25</td>
</tr>
<tr>
<td>1,4</td>
<td>1,4,5,8</td>
<td>8.06</td>
<td>2.25</td>
</tr>
<tr>
<td>1,4</td>
<td>1,3,5,7</td>
<td>10.15</td>
<td>2.25</td>
</tr>
<tr>
<td>1,4</td>
<td>1,2,7,8</td>
<td>6.01</td>
<td>2.48</td>
</tr>
</tbody>
</table>

ᵃ See Figure 2 for numbering convention.

are symmetrical and only one of the geometries needs to be considered. There are many initial geometrical arrangements of vacancies that could provide a stable surface, Table 3. Our approach to evaluate these surfaces was to select a range of high and low symmetry examples with the vacancies either clustered or separated. This treatment required 25−30 different arrangements to be calculated. We illustrate this procedure for a few different starting vacancy arrangements for the (001) surface terminated with Fe₄O₈. Figure 2 shows the unique ion positions in the cell at the surface and their corresponding numerical assignments. Table 4 lists the calculated surface energies for different reconstructions of the (001) surface planes, using the assignments presented in Figure 2. The data show that there is a large decrease in surface energy upon relaxation. The most stable surfaces upon relaxation do not necessarily have the lowest surface energy in the unrelaxed state. The most stable surface had iron ion vacancies on adjacent sites and oxygen ion vacancies nearby.

![](./images/812372348953952257_3.jpg)

Figure 3. Two-dimensional unit cells of (001) surfaces terminated with (a) unrelaxed and (b) relaxed iron ions and with (c) unrelaxed and relaxed (d) iron−oxygen ions.

<table>
<caption>TABLE 5: Calculated Surface Energies for $\gamma$-Fe₂O₃</caption>
<thead>
<tr>
<th rowspan="2">surface</th>
<th>reconstructed surface</th>
<th colspan="2">surface energy $\gamma$ (J/m²)</th>
</tr>
<tr>
<th>composition</th>
<th>unrelaxed</th>
<th>relaxed</th>
</tr>
</thead>
<tbody>
<tr>
<td>001</td>
<td>Fe,t</td>
<td>5.19</td>
<td>1.98</td>
</tr>
<tr>
<td>001</td>
<td>2Fe,o; 4O</td>
<td>7.07</td>
<td>1.97</td>
</tr>
<tr>
<td>011</td>
<td>2Fe,o; 2Fe,t; 4O</td>
<td>6.22</td>
<td>2.03</td>
</tr>
<tr>
<td>011</td>
<td>2Fe,o; 4O</td>
<td>6.41</td>
<td>1.97</td>
</tr>
<tr>
<td>111</td>
<td>6Fe,o</td>
<td>9.51</td>
<td>2.16</td>
</tr>
<tr>
<td>111</td>
<td>2Fe,o</td>
<td>6.45</td>
<td>2.56</td>
</tr>
<tr>
<td>111</td>
<td>4Fe,t; 2Fe,o</td>
<td>8.88</td>
<td>2.69</td>
</tr>
<tr>
<td>111</td>
<td>8.5O</td>
<td>12.24</td>
<td>2.01</td>
</tr>
<tr>
<td>012</td>
<td>Fe,t</td>
<td>5.60</td>
<td>2.12</td>
</tr>
<tr>
<td>012</td>
<td>2Fe,o; 4O</td>
<td>5.34</td>
<td>1.89</td>
</tr>
<tr>
<td>112</td>
<td>2Fe,o; 2Fe,t; 4O</td>
<td>8.92</td>
<td>1.92</td>
</tr>
<tr>
<td>112</td>
<td>2Fe,o; 4O</td>
<td>7.15</td>
<td>1.86</td>
</tr>
<tr>
<td>122</td>
<td>Fe,t</td>
<td>10.41</td>
<td>2.65</td>
</tr>
<tr>
<td>122</td>
<td>2Fe,o; 4O</td>
<td>10.11</td>
<td>2.23</td>
</tr>
</tbody>
</table>

Table 5 gives the most stable surface energies determined from all the initial arrangements of vacancies considered. For the (001), (011), and (112) surfaces, the two possible surface terminations give almost the same surface energy, which indicates their structural similarities. The most stable surface is (112) containing Fe₂O₄ in the reconstructed surface cell, but several other surfaces including (001), (011), and (012) are very close in stability and also have a surface energy less than 2 J/m². We examined the positions of ions in several of these surfaces. Figure 3 shows plots of the ion positions for two possible terminations of the (001) surface before and after the ions are relaxed. The surface terminated with just iron ions shows that upon relaxation the top plane contains oxygen and iron ions, so that a rather similar structure is obtained for the two terminations. Figure 4 shows the positions of ions near the top surface plane for (112), (012), and (011) surfaces of lowest surface energy. There are oxygen and iron ions in the top plane of these relaxed surfaces that all have a rather similar surface energy. A common feature of these surfaces is the broadening of the iron−oxygen plane compared to the unrelaxed surfaces

![](./images/812372348953952257_4.jpg)

Figure 4. Top views of the relaxed and reconstructed (a) (112), (b) (012), and (c, d) (011) surfaces. The (112) and (012) surfaces are terminated with $Fe_4O_8$, while the (011) surface can be terminated with either (c) $Fe_4O_8$ or (d) $Fe_8O_8$. These surfaces have the smallest surface energies.

due to the complex geometry of the surface. This relaxed plane contains ions distributed over a distance of $\sim 1$ Å. The iron ions are highly coordinated in this surface region.

We also examined some unsymmetrical reconstructed surfaces that are possible on the (011) and (112) planes containing eight iron and eight oxygen ions. For both of these surfaces a net +3 charge was removed to quench the dipole (according to the data in Table 3). This treatment could be accomplished by removing atoms from the top plane in the surface in one of the following three fashions: (1) one Fe,t; (2) three Fe,t and three O; and (3) one Fe,t, four Fe,o, and five O. The calculated surface energies were larger than those for the symmetrical reconstructions considered in Tables 3 and 5, which suggests that these unsymmetrical reconstructions are less stable.

The equilibrium crystal morphology may be deduced from the relaxed surface energies by construction of the Wulff plot. $^{43}$ In this approach, the faces with smallest surface energies have proportionally the greatest area. Figure 5 shows a complex morphology for $\gamma$-$Fe_2O_3$ based on the surfaces energies of these surfaces. The equilibrium habit of these nanocrystals would take a polyhedral shape with multiple facets including (001), (012), (011) and (112) labeled in multiples of these planes.

Growth Morphology. The crystal habit of nanocrystals may not only be determined by equilibrium considerations under particular experimental conditions; the rate of growth can also affect the crystal habit. In the latter case the slowest growing surface determines the crystal habit. Hartman and co-workers have developed a means to compare the relative growth rates of different surfaces. $^{44,45}$ The method has been tested and applied for surfaces of $Al_2O_3$ and $ZrSiO_4$. $^{38}$ This theory was developed for flat surface planes that are expected to grow in a layer-by-layer mechanism. It is assumed that the energy of binding a growth unit to the existing surface will be the factor that controls the rate of growth and external factors such as solvent are not considered in this theory. The attachment energy $(E_{att})$ is defined as the energy released per molecule when a growth slice with thickness of $d_{hkl}$ is attached to a crystal surface of Miller index $hkl$, where thickness $d_{hkl}$ is equal to $a/(h^2 + k^2 + l^2)^{1/2}$ and $a$ is the lattice constant of a cubic-phase material. Thus, the morphologically most important face in a growing crystal would be the one with the smallest growth rate or attachment energy. This correlation was demonstrated by several calculations in conjunction with experimental observations. $^{40,46}$ The $d_{hkl}$ values in the repeat units containing a screw axis or glide plane were reduced by a factor that reflects the number of planes equivalent by symmetry.

![](./images/812372348953952257_5.jpg)

Figure 5. Wulff plot for $\gamma$-$Fe_2O_3$ showing the equilibrium morphology based on the relaxed surface energies.

We calculated the attachment energy for the surfaces of $\gamma$-$Fe_2O_3$ containing several different arrangements of vacancies. These surfaces are therefore not flat and growth units that fit onto the top of an existing reconstructed surface needed to be created. These growth units contain a plane at the surface with structure complementary to that of the surface under study. Figure 6 shows an illustration of the concept on attaching a growth layer to the reconstructed surfaces. One side of the attaching slice must fit onto the top of the existing reconstructed surface, while the other side should have the same structure as the top plane in the restructured surfaces. Our procedure was to compute the energy of the unrelaxed growth unit, which is called the slice energy. The slice energy $(E_{sl})$ was subtracted from the crystal energy to give the attachment energy following eq 5: $^{45}$

$$
E_{\text{att}} = E_{\text{cr}} - E_{\text{sl}} \tag{5}
$$

Alternatively, the unrelaxed attachment energy could be calculated directly from the interaction energy between ions in the unrelaxed slice in region I and the unrelaxed ions in region II. The relaxed attachment energy was calculated analogously, except that ions in the relaxed growth slice interact with ions in region II that occupy relaxed positions determined in a prior calculation. All the surfaces except (111) contain symmetry elements in the planes of the repeat unit. We, thus, have evaluated the attachment energy for the planes of (004), (022), (048), and (224) instead of (001), (011), (012), and (112), respectively.

![](./images/812372348953952257_6.jpg)

Figure 6. An illustration showing how a slice is constructed to calculate the attachment energies to the reconstructed surfaces.

<table>
<caption>TABLE 6: Calculated Attachment Energies per Molecule of $\gamma$-Fe₂O₃ at Various Surfaces</caption>
<thead>
<tr>
<th>reconstructed surface</th>
<th>surface composition</th>
<th colspan="2">$E_{att}$ (eV)</th>
</tr>
<tr>
<th></th>
<th></th>
<th>unrelaxed</th>
<th>relaxed</th>
</tr>
</thead>
<tbody>
<tr>
<td>004</td>
<td>Fe,t</td>
<td>17.4</td>
<td>12.6</td>
</tr>
<tr>
<td>004</td>
<td>2Fe,o; 4O</td>
<td>15.8</td>
<td>15.3</td>
</tr>
<tr>
<td>022</td>
<td>2Fe,o; 2Fe,t; 4O</td>
<td>17.0</td>
<td>14.9</td>
</tr>
<tr>
<td>022</td>
<td>2Fe,o; 4O</td>
<td>12.5</td>
<td>12.5</td>
</tr>
<tr>
<td>111</td>
<td>2Fe,o</td>
<td>9.0</td>
<td>8.4</td>
</tr>
<tr>
<td>111</td>
<td>6Fe,o</td>
<td>13.2</td>
<td>13.4</td>
</tr>
<tr>
<td>111</td>
<td>8.5O</td>
<td>10.6</td>
<td>10.0</td>
</tr>
<tr>
<td>048</td>
<td>2Fe,o; 4O</td>
<td>31.6</td>
<td>42.4</td>
</tr>
<tr>
<td>048</td>
<td>Fe,t</td>
<td>34.4</td>
<td>49.1</td>
</tr>
<tr>
<td>224</td>
<td>2Fe,o; 4O</td>
<td>38.0</td>
<td>38.6</td>
</tr>
<tr>
<td>224</td>
<td>2Fe,t; 2Fe,o; 4O</td>
<td>41.7</td>
<td>41.3</td>
</tr>
</tbody>
</table>

Experimentally, it has been observed from vapor-phase reactions that (001), (011), and (111) surfaces of $\gamma$-Fe₂O₃ are dominant in the final products and no other planes in synthetic or natural materials have been reported.²¹ We thus selected several low-index surface planes for morphological study. High index surfaces were not considered because they are morphologically less significant than low index surfaces according to the Bravais−Friedel−Donnay−Harker theory.⁴⁰ Table 6 presents the calculated lowest attachment energies for the selected low Miller index surfaces of $\gamma$-Fe₂O₃. We note that the relaxed attachment energy is not necessarily smaller than the unrelaxed attachment energy. The trend of both unrelaxed and relaxed attachment energy is that the (111) surface has the smallest values followed by the (022) and (004) surfaces. The (048) and (224) surfaces have the largest attachment energies among all those examined. The (111) surfaces would be the most important when growth rates determine the crystal habit. Under kinetically favored conditions, an octahedral shape is expected for the growth morphology of $\gamma$-Fe₂O₃. Figure 7 shows the Wulff plot based on the calculated data. A highly faceted shape with predominant (111) faces and (004) faces at the vertexes is predicted. Figure 8 shows the stable relaxed (111) surfaces viewed in two different directions. The iron-terminated surfaces containing 6Fe,o or 2Fe,o have the smallest attachment energies. They consist of iron ions in 3-fold sites at ∼0.5 Å above the plane of oxygen ions with bond distances ranging between 1.84 and 1.92 Å. The 2Fe,o surface is shown in top and side views in Figure 8, panels a and b, respectively. In the case of the reconstructed (111) surface with 6Fe,o shown in side view in Figure 8c, the iron ions are located in complete and partial rows. In both of these surfaces, the iron ions are exposed rather than embedded in the surface layer, which makes them potentially the most reactive with adsorbed molecules. In the case of oxygen-terminated (111) surfaces, the oxygen ions extend slightly above the iron ions shown in Figure 8d.

![](./images/812372348953952257_7.jpg)

Figure 7. Wulff plot for $\gamma$-Fe₂O₃ showing the growth morphology based on the relaxed attachment energies.

It is interesting to further evaluate the composition and structure of the next plane that grows on top of the (111) surfaces which have the smallest attachment energies. In the case of 4Fe,o surface, a 4Fe,t plane forms, followed by a plane of 16 oxygen ions. It can be conjectured that this iron plane could reduce the Coulomb attractions between the 4Fe,o plane and the oxygen plane, which leads to the low attachment energies.

### Discussion
In our treatment, the mean field approximation is applied to account for the partial occupancy of iron octahedral sites. This method makes it possible to calculate the surface energy and attachment energy for surfaces of $\gamma$-Fe₂O₃. We employed an analysis that attributes the formation of nanoparticles of different crystal habit to the bonding nature of the solid itself. For growth under equilibrium conditions, the crystal habit with lowest free energy is expected to form. Under this formation mechanism, the crystals formed have surfaces of the lowest surface free energy, which we approximate as the lowest surface energy in these calculations. We predict from the relaxed surface energies and the corresponding Wulff plot that the (012) and (112) surface planes of $\gamma$-Fe₂O₃ would predominate with contributions from (011) planes. Such $\gamma$-Fe₂O₃ crystals would have polyhedral structures.

A kinetically dominated growth is also possible in this crystallization process. In this case, the attachment energy is important. The theory developed by Hartman and colleagues attributes the rate of growth on flat surfaces as being proportional to the energy released when binding a new growth unit to the crystal surface.⁴⁴,⁴⁵ This concept is analogous to linear free energy relationships often invoked to explain kinetic effects. Our calculations indicate that (111) surfaces containing iron ions

![](./images/812372348953952257_8.jpg)

Figure 8. The relaxed reconstructed (111) surfaces with initial surface composition containing (a, b) 2Fe,o viewed from the (a) top and (b) side, (c) 6Fe,o, and (d) 8.5O viewed from the side. These surfaces have the smallest attachment energies.

would be the slowest growing surfaces, which would result in primarily an octahedral crystal habit of $\gamma$-Fe₂O₃.

Crystallization theory at the level we have discussed does not take certain factors into consideration. One factor is the degree of supersaturation in solution. Other factors that could influence the growth include temperature, solvent, molecule binding to the crystal surface, diffusion rates, and density of active growth sites. There does not seem to be a comprehensive theory that takes all of these factors into account, although Liu and Bennema⁴⁷,⁴⁸ have made significant progress in this direction. We are currently working on incorporating these factors in further analysis of $\gamma$-Fe₂O₃ nanoparticle formation under various experimental conditions.

A point of interest is the interaction of molecules with the (111) surfaces terminated with ions of iron. These surfaces contain iron cations coordinated to only three oxygen anions. These iron ions are sterically unhindered, which should promote interactions between these iron cations and adsorbing molecules. This structure property is unlike those of the other surfaces where the iron ions are almost fully coordinated and imbedded in a plane of oxygen ions. Thus, appropriate anionic molecules might be expected to have attractive Coulomb interactions with these iron ions and adsorb on these (111) surfaces.

The (001) surface of $\gamma$-Fe₂O₃ has been prepared experimentally by a molecular beam epitaxy method on (001) surfaces of MgO.²¹ A reconstructed surface was observed⁴⁹ in contrast to earlier experiments under different conditions where no reconstruction was observed.⁵⁰ A proposed surface model that explained the LEED patterns involved removing every other Fe³⁺ ion on the (001) surface terminated by Fe³⁺. This is the reconstruction we considered in the present work. Alternatively, the reconstruction we considered at the Fe₄O₈ terminated surface would also be consistent with the experimental data.

Cubic maghemite is usually formed by the transformation from another iron oxide and almost always adopts the habit of its precursors.²¹ Rods or cubes have been observed and morphologies with predominantly (011) planes have been reported. Nanocrystals of $\gamma$-Fe₂O₃ have been prepared from the vapor-phase reaction of ferric chloride in an oxygen−hydrogen flame.⁵¹ Crystals of $\gamma$-Fe₂O₃ with diameter below 40 nm exhibit only (001) and (111) faces. When the particle size is larger than 40 nm, the (011) planes are also observed. Compared to our calculations, none of the planes predicted by the equilibrium morphology are observed and so we can rule out an equilibrium process. The predicted growth morphology is consistent with this experimental result for the nanocrystals. Our calculations for (011) planes have slightly larger attachment energies and do not explain their formation in the larger crystals. This size-dependent shape evolution could be indicative that the computational approach developed can have practical implications and ramifications in design and synthesis of nanocrystals with designed morphologies, such as cubes, rods, other faceted shapes, and spheres.

## Conclusions

A comprehensive study of $\gamma$-Fe₂O₃ surfaces was carried out with use of the classical atomistic simulation method. The mean field theory was employed to account for the partial occupancy of octahedral iron sites in the spinel structure. The low-index surfaces of $\gamma$-Fe₂O₃ were all polar and unstable unless reconstructed. We introduced surface vacancies and a corresponding plane at the bottom of the stack of repeat units to quench the dipole perpendicular to the surface. We carried out these two-dimensional periodic calculations with the MARVIN program using bulk coordinates for the relaxed crystal from the GULP code. The surface energy was used to evaluate the equilibrium morphology. The most stable surface of $\gamma$-Fe₂O₃ contains the (112) surface plane with the lowest surface energy of 1.86 J/m², but several others including (001), (011), and (012) have values within 0.1 J/m². A polyhedral crystal habit is predicted for the equilibrium morphology of $\gamma$-Fe₂O₃. The attachment energy is used to determine the growth morphology. In this case, the smallest attachment energy was found for (111) surfaces terminated with iron ions and the attachment energy increased in the following order: (111) < (022) < (004) < (224) < (048). An octahedral crystal habit was predicted for the growth morphology of $\gamma$-Fe₂O₃ with (004) planes at the vertexes. In this growth morphology, the (111) surface of $\gamma$-Fe₂O₃ is terminated with iron cations and should be reactive. The iron ions are not clearly exposed on other surfaces, which may lead to different surface adsorption behavior. The morphology prediction in this work is based upon theoretical calculations that treat the crystal itself, and does not consider its environment. We will include various factors such as the effects of solvent

in our future work. Our simulations on growth morphology agree well with those observed nanocrystals (<40 nm) experimentally, which suggests that the computational approach we have developed is directly relevant to the designs of nanometer-sized dots, wires, and other faceted particles.

Acknowledgment. This work is supported by the University of Rochester and National Computational System Alliance (NCSA) under grant no. DMR030021N. We are grateful to Prof. Julian Gale of Imperial College, London for helpful advice and the GULP computer code and Dr. Ben Slater of the Royal Institution of Great Britain for providing a copy of the MARVIN computer program. We are grateful to Dr. Sean Fleming of Curtin University of Technology for the GDIS computer program used in drawing the surface structures and crystal morphologies. We thank Mr. Xiaowei Teng for the help in the illustration. This work made use of the IBM P690 supercomputers at the University of Illinois (UIUC) supported by NCSA.

## References and Notes

(1) Moser, A.; Rettner, C. T.; Best, M. E.; Fullerton, E. E.; Weller, D.; Parker, M.; Doerner, M. F. *IEEE Trans. Magn.* **2000**, *36*, 2137.
(2) Weller, D.; Doerner, M. F. *Annu. Rev. Mater. Sci.* **2000**, *30*, 611.
(3) Sun, S. H.; Murray, C. B.; Weller, D.; Folks, L.; Moser, A. *Science* **2000**, *287*, 1989.
(4) Sellmyer, D. J.; Luo, C. P.; Yan, M. L.; Liu, Y. *IEEE Trans. Magn.* **2001**, *37*, 1286.
(5) Teng, X.; Yang, H. *J. Am. Chem. Soc.* **2003**, *125*, released ASAP Nov 1, 2003.
(6) Hafeli, U.; Schutt, W.; Teller, J.; Zborowski, M. *Scientific and Clinical Applications of Magnetic Carriers*; Plenum Press: New York, 1998.
(7) Safarik, I.; Safarikova, M. *Monatsh. Chem.* **2002**, *133*, 737.
(8) Pouliquen, D.; Chouly, C. Magnetic microcarriers for medical applications. In *Microspheres, Microcapsules and Liposomes: Preparation and Chemical Applications*; Arshady, R., Ed.; Citus Books: London, UK, 1999; Vol. 2; p 373.
(9) Bulte, J. W. M.; Douglas, T.; Witwer, B.; Zhang, S. C.; Strable, E.; Lewis, B. K.; Zywicke, H.; Miller, B.; van Gelderen, P.; Moskowitz, B. M.; Duncan, I. D.; Frank, J. A. *Nat. Biotechnol.* **2001**, *19*, 1141.
(10) Perez, J. M.; Josephson, L.; O'Loughlin, T.; Hogemann, D.; Weissleder, R. *Nat. Biotechnol.* **2002**, *20*, 816.
(11) Perez, J. M.; O'Loughin, T.; Simeone, F. J.; Weissleder, R.; Josephson, L. *J. Am. Chem. Soc.* **2002**, *124*, 2856.
(12) Zhao, M.; Josephson, L.; Tang, Y.; Weissleder, R. *Angew. Chem., Int. Ed.* **2003**, *42*, 1375.
(13) Kreibig, U.; Bonnemann, H.; Hormes, J. Nanostructured metal clusters and colloids. In *Handbook of Surfaces and Interfaces of Materials: Nanostructured Materials, Micelles, and Colloids*; Nalwa, H. S., Ed.; Academic Press: San Diego, CA, 2001; Vol. 3, p 1.
(14) Hyeon, T. *Chem. Commun.* **2003**, *927*.
(15) Rockenberger, J.; Scher, E. C.; Alivisatos, A. P. *J. Am. Chem. Soc.* **1999**, *121*, 11595.

(16) Sun, S. H.; Zeng, H. *J. Am. Chem. Soc.* **2002**, *124*, 8204.
(17) Fried, T.; Shemer, G.; Markovich, G. *Adv. Mater.* **2001**, *13*, 1158.
(18) Kotov, N. A. *MRS Bull.* **2001**, *26*, 992.
(19) Guo, Q.; Rahman, S.; Teng, X.; Yang, H. *J. Am. Chem. Soc.* **2003**, *125*, 630.
(20) Wang, Y.; Teng, X.; Wang, J.-S.; Yang, H. *Nano Lett.* **2003**, *3*, 789.
(21) Cornell, R. M.; Schwertmann, U. *The Iron Oxides: Structure, Properties, Reactions, Occurrence and Uses*; VCH: Weinheim, Germany, 1996.
(22) Zhang, X.; Catlow, C. R. A. *Phys. Rev. B* **1992**, *46*, 457.
(23) Baetzold, R. C. *Phys. Rev. B* **1988**, *38*, 11304.
(24) Bush, T. S.; Gale, J. D.; Catlow, C. R. A.; Battle, P. D. *J. Mater. Chem.* **1994**, *4*, 831.
(25) Baetzold, R. C. *Phys. Rev. B* **1993**, *48*, 5789.
(26) Catlow, C. R. A.; Corish, J.; Harding, J. H.; Jacobs, P. W. M. *Philos. Mag. A* **1987**, *55*, 481.
(27) Davies, M. J.; Parker, S. C.; Watson, G. W. *J. Mater. Chem.* **1994**, *4*, 813.
(28) Binks, D. J.; Grimes, R. W.; Rohl, A. L.; Gay, D. H. *J. Mater. Sci.* **1996**, *31*, 1151.
(29) Whitmore, L.; Sokol, A. A.; Catlow, C. R. A. *Surf. Sci.* **2002**, *498*, 135.
(30) Hamad, S.; Cristol, S.; Callow, C. R. A. *J. Phys. Chem. B* **2002**, *106*, 11002.
(31) de Leeuw, N. H.; Parker, S. C.; Sithole, H. M.; Ngoepe, P. E. J. *Phys. Chem. B* **2000**, *104*, 7969.
(32) Nygren, M. A.; Gay, D. H.; Catlow, C. R. A. *Surf. Sci.* **1997**, *380*, 113.
(33) Islam, M. S.; Catlow, C. R. A. *J. Solid State Chem.* **1988**, *77*, 180.
(34) Mackrodt, W. C.; Davey, R. J.; Black, S. N.; Docherty, R. *J. Cryst. Growth* **1987**, *80*, 441.
(35) Jones, F.; Rohl, A. L.; Farrow, J. B.; van Bronswijk, W. *PCCP Phys. Chem. Chem. Phys.* **2000**, *2*, 3209.
(36) Woodley, S. M.; Catlow, C. R. A.; Piszora, P.; Stempin, K.; Wolska, E. *J. Solid State Chem.* **2000**, *153*, 310.
(37) Gale, J. D. *J. Chem. Soc., Faraday Trans.* **1997**, *93*, 629.
(38) Gay, D. H.; Rohl, A. L. *J. Chem. Soc., Faraday Trans.* **1995**, *91*, 925.
(39) Dick, B. G.; Overhauser, A. W. *Phys. Rev.* **1958**, *112*, 90.
(40) Docherty, R.; Clydesdale, G.; Roberts, K. J.; Bennema, P. *J. Phys. D: Appl. Phys.* **1991**, *24*, 89.
(41) Tasker, P. W. *Philos. Mag. A-* **1979**, *39*, 119.
(42) Harding, J. H. *Surf. Sci.* **1999**, *422*, 87.
(43) Dowty, E. *Am. Miner.* **1980**, *65*, 465.
(44) Hartman, P.; Perdok, W. G. *Acta Crystallogr.* **1955**, *8*, 49.
(45) Hartman, P.; Bennema, P. *J. Cryst. Growth* **1980**, *49*, 145.
(46) Berkovitch-Yellin, Z. *J. Am. Chem. Soc.* **1985**, *107*, 8239.
(47) Liu, X. Y.; Boek, E. S.; Briels, W. J.; Bennema, P. *Nature* **1995**, *374*, 342.
(48) Liu, X. Y.; Bennema, P. *J. Cryst. Growth* **1996**, *166*, 112.
(49) Voogt, F. C.; Fujii, T.; Smulders, P. J. M.; Niesen, L.; James, M. A.; Hibma, T. *Phys. Rev. B* **1999**, *60*, 11193.
(50) Gao, Y.; Chambers, S. A. *J. Cryst. Growth* **1997**, *174*, 446.
(51) Batis-Landoulsi, H.; Vergnon, P. *J. Mater. Sci.* **1983**, *18*, 3399.