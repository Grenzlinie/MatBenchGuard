# ORDERED SURFACE PHASES OF Au ON Cu *

Stephen M. FOILES

Sandia National Laboratories, Livermore, CA 94550, USA

Received 18 May 1987; accepted for publication 1 July 1987

Calculations using the embedded atom method show that Au forms ordered surface layers on the low index faces of Cu which exist in equilibrium with a bulk containing dilute amounts of Au. These surfaces have a mixed Au-Cu surface plane rather than Au adatoms on a Cu surface. The (100) and (110) ordered surfaces contain 1/2 monolayer of Au arranged in c(2×2) structures, though the ordering on the (110) surface is poor in the direction normal to the close packed rows. The (111) surface has 1/3 monolayer of Au in a $(\sqrt{3} \times \sqrt{3}) R 30^{\circ}$ structure. The surface layers of all three faces are found to be rippled with the Au atoms 0.13 to 0.21 Å above the Cu atoms. The results for the (100) surface are in agreement with LEED results for the structure found for Au deposited on Cu.

## 1. Introduction

Experimental studies of the deposition of Au on the Cu(100) surface have shown the existence of a c(2×2) ordered structure after the deposition of 1/2 monolayer of Au [1-3]. Palmberg and Rhodin [1] proposed that this structure involved the incorporation of the Au into a mixed Cu-Au surface layer rather than an ordered overlayer of Au. The work of Graham [2] finds a similarity between the ion scattering from this surface and that of the $Cu_{3} Au$ surface suggesting that the mixed surface layer model is correct. Recent low energy electron diffraction (LEED) experiments by Wang et al. [3] have determined the structure formed by the deposition of 1/2 monolayer of Au on clean Cu(100) surfaces. The $I-V$ analysis of the LEED data shows that rather than an ordered overlayer of Au adatoms, the surface consists of a surface plane containing both Au and Cu with the Au atoms arranged in a c(2×2) pattern. The second atomic plane was found to contain solely Cu. (This structure of the surface layer is the same as for the (100) surface of the ordered $Cu_{3} Au$ alloy [4].) The surface layer was also found to be rippled with the Au atoms in the top layer positioned 0.1 Å higher than the Cu atoms. The separation of the

---
* This work was supported by the US Department of Energy, Office of Basic Energy Sciences, Division of Materials Science.

0039-6028/87/$03.50 © Elsevier Science Publishers B.V.
(North-Holland Physics Publishing Division)

first and second Cu layers was found to be expanded by $0.08\ \mathring{A}$ compared to the bulk spacing. These results are interesting because they indicate the existence of a stable ordered surface alloy.

In this paper, theoretical calculations using the embedded atom method [5] (EAM) are presented which support the results of the experimental studies of the (100) surface and determine the ordering on two other low index surfaces, the (111) and (110). This work was motivated by an earlier survey of the segregation to (100) surfaces of fcc metals using the EAM [6]. There it was found that Au impurities are bound to the surface layer of Cu by 0.4 eV. This suggests the possibility of forming a concentrated Cu-Au surface layer in equilibrium with dilute quantities of Au in bulk Cu.

The section 2 of this paper outlines the calculational approach. Next, the energetics of Au adatoms on the surface are compared with the energetics of incorporation of the Au into the surface layer to determine whether Au deposited on the surface will in fact incorporate into the surface layer. Finally, the simulation results for the equilibrium surface structure and composition of Cu-Au alloys in the limit of dilute Au concentrations are presented. (After modest annealing, the deposition experiment will effectively produce a dilute Au concentration in the region near the surface.) It is found that at room temperature for the three low index surfaces, (100), (110), and (111), ordered surface layers exist in equilibrium with bulk material containing less than about 0.01 atomic percent Au. In addition, the surfaces are rippled with the Au atoms displaced outward from the surface. The structure of the ordered layer for the (100) surface corresponds to the structure found experimentally. For the (110) surface, the outermost layer contains 1/2 monolayer of Au substitutionally arranged with a c(2 × 2) symmetry. For the (111) surface the surface contains 1/3 monolayer of Au substitutionally arranged with $(\sqrt{3} \times \sqrt{3}) \text{R}30^\circ$ symmetry.

### 2. Calculational method

The EAM is a technique for computing the energetics of an arbitrary arrangement of atoms in a metallic system. This technique has been described in detail elsewhere [5,6] and so will only be summarized here. The energy of the metal is assumed to have two contributions. First, an embedding energy associated with the interaction of each atom with the electron density provided by the remaining atoms of the metal. The second contribution is a pairwise interaction describing screened internuclear repulsion. In particular, the energy is assumed to be given by the expression

$$
E_{\mathrm{tot}} = \sum_{i} F_{i}(\rho_{i}) + \frac{1}{2} \sum_{ij,i \neq j} \phi_{ij}(R_{ij}). \tag{1}
$$

Here $\phi_{i j}(R_{i j})$ is the pairwise interaction between atoms $i$ and $j$ separated by the distance $R_{i j}$ and $F_{i}(\rho)$ is the embedding energy for placing atom $i$ into the local electron density $\rho$. The local electron density is computed from the superposition of atomic densities, i.e.

$$
\rho_{i}=\sum_{j \neq i} \rho_{j}^{\mathrm{a}}\left(R_{i j}\right). \tag{2}
$$

Here $\rho_{j}^{\mathrm{a}}(R)$ is the atomic electron density evaluated at a distance $R$ from the nucleus. The atomic electron densities are taken from Hartree-Fock calculations for free atoms. The embedding functions, $F_{i}(\rho)$, and the pairwise interactions, $\phi_{i j}(R)$, are determined empirically for the different elements by fitting to the lattice constant, sublimation energy, elastic constants, and vacancy formation energy of the pure elements and the heats of mixing of the binary alloys. The functions used here are from the set of functions for the fcc metals Cu, Ag, Au, Ni, Pd, and Pt that have been determined in ref. [6]. These functions have not been modified for this work so that the predictions below do not involve any adjustable parameters other than those used to fit the properties of the bulk materials.

Given the energies provided by the EAM, the equilibrium distribution of Cu and Au near a surface can be computed by Monte Carlo simulation techniques. The details of the procedure are the same as for earlier work on the surface segregation of Ni-Cu alloys [7] and Pd alloys with noble metals [8]. The simulations proceed by attempting various modifications of the system and accepting or rejecting that modification with a probability given by the relative statistical probabilities of the two configurations. (For the case where the total number of atoms of each element is constant, this ratio is just the Boltzman factor associated with the change in energy.) Two types of modifications are considered. First, spatial displacement of the atoms. This incorporates the strain and relaxation effects as well as the vibrational contributions to the free energy. Second, the chemical identity of each atom is allowed to change during the course of the simulation. (The simulations are performed with a fixed chemical potential difference between the two elements and a fixed total number of atoms.) This procedure yields rapid convergence of the simulation to the equilibrium composition profile since there is no need to diffuse the segregating species. The calculations consider a slab of atoms which is extended periodically in the directions parallel to the surface. The exact dimension of the computational cell depend on the surface exposed but the slabs are about $22 \AA$ thick and the periodicities in the plane of the surface range from 14.5 to $17.8 \AA$. Tests with larger cells found no significant differences in the results described below. All of the simulations presented here were performed for a temperature of 300 K.

### 3. Results

During the initial stages of the deposition of Au on a clean Cu(100) surface, Au atoms will be placed as adatoms on the Cu surface. One must then determine whether the Au will prefer to form a layer on top of the Cu surface, mix with the Cu in a region localized to the surface, or simply diffuse into the bulk. To address this question the energy of a Cu(100) surface with a single Au adatom was computed and compared to the energy for a Cu surface with a Cu adatom and a Au substitutional atom in the surface layer. This energy difference corresponds to a process where the deposited Au atom exchanges with a Cu atom in the surface. It is found that the incorporation of the Au adatom into the surface is energetically favored by 0.14 eV. Thus the energet- ics favor the initial incorporation of the deposited Au into the surface layer. The energetics of the Au atom in the surface layer compared to the bulk has been computed earlier using this technique and it was found that energy of a Au substitutional in the surface layer is 0.40 eV below that of the substitu- tional in the bulk and that the energy of the substitutional in the second atomic layer is 0.01 eV below its energy in the bulk. Therefore, the initial Au atoms will be energetically bound to the surface atomic layer in accord with the experimentally deduced structure.

In order to determine the ordering, if any, of the Au atoms in the surface layer, Monte Carlo simulations were performed for slabs exposing the (100), (110), and (111) surfaces at a temperature of 300 K. The chemical potentials for the calculations were chosen so that there is only dilute Au content in the bulk of the slab. (The relative composition of the bulk material and the surface will be discussed below.) In order to avoid prejudicing the simulation results by the initial distribution of Au atoms, the slab initially contains only Cu and the Au atoms are then created by the simulation. Figs. 1-3 show snapshots of randomly selected atomic configurations generated during the simulations for the (100), (111) and (110) surfaces respectively. For all three surfaces, the Au atoms are essentially confined to the surface atomic plane. For the (100) surface (see fig. 1) a clear c(2 × 2) arrangement of the atoms with a half monolayer of Au is seen. This agrees with the symmetry and coverage found in the experiments. For the (111) surface (see fig. 2), the ordered structure occurs with 1/3 of a monolayer of Au and a primitive $(\sqrt{3} \times \sqrt{3}) \text{R}30^{\circ}$ structure. (The particular configuration shown contains a defect, namely a Au site occupied by a Cu atom near the center of the figure.) The snapshot in fig. 3 of the (110) surface is from a simulation containing 4 times the surface area that was usually used. The majority of the surface shows a c(2 × 2) ordering of the Au atoms at a half monolayer. In this structure the close packed rows alternate between Cu and Au atoms and the rows are staggered with respect to each other. The fourth close packed row from the top is defected. A segment of this row maintains the alternation of Cu and Au along the row but this alternation

![](./images/811788769249198080_1.jpg)

Fig. 1. A snapshot of a randomly chosen configuration from the Monte Carlo simulation of the (100) surface of Cu containing dilute amounts of Au showing the c(2×2) ordered structure. The filled circles are Au atoms and the empty circles are Cu atoms. The simulations are for a temperature of 300 K and a bulk Au content of 0.1 atomic percent.

is out of registry with the other rows on the surface. This kind of defect is seen in several snapshots of this surface.

In order to quantify the ordering of these surfaces, in particular the (110)

![](./images/811788769249198080_2.jpg)

Fig. 2. As in fig. 1 except showing the $(\sqrt{3} \times \sqrt{3}) R 30^{\circ}$ arrangement of Au atoms on the (111) surface.

![](./images/811788769249198080_3.jpg)

Fig. 3. As in fig. 1 except showing the arrangement of Au on the (110) surface for a bulk composition of 0.01 at% Au.

surface, the two-dimensional structure factor of the Au atoms was computed.
The structure factor is defined here by the equation

$$
S(k)=\frac{1}{N}\left\langle\left|\sum_{i} \exp \left(\mathrm{i} \boldsymbol{k} \cdot \boldsymbol{R}_{i}\right)\right|^{2}\right\rangle,
\tag{3}
$$

where the sum is over the Au atoms, $\boldsymbol{k}$ is the wave vector in reciprocal space, $\boldsymbol{R}_{i}$ is the position of atom $i$, and the angular brackets denote an average over the configurations generated in the simulations. The structure factor was evaluated for $k_{z}=0$ where the $z$-direction is normal to the surface. While this quantity does not directly correspond to a specific measurement, the symmetry observed in this quantity will be the same as that seen in diffraction experiments. For the (100) and (111) surfaces, the structure factor shows extra peaks at the locations indicated by the symmetry of the observed structures and in agreement with the experimental results for the (100) surface. The structure factor computed for the (110) surface as a function of the wave vector in the plane of the surface is plotted in fig. 4. The large peaks in the data are the integral order beams of the surface. The four smaller peaks are due to the c(2 × 2) structure. Note that these peaks are narrow in the (110) direction but quite broad in the (001) direction. This behavior indicates that there is relatively good order along the close packed rows of the surface but that there is significant disorder between the chains. This corresponds nicely with the kind of defect seen in fig. 3.

![](./images/811788769249198080_4.jpg)

Fig. 4. The structure factor, $S(k)$, as defined in eq. (3) computed for the (110) surface. The large peaks in the figure are the integral order positions and the smaller peaks are due to the approximate c(2×2) ordering of the Au atoms.

Another possibility for the structure of these surfaces is that the addition of Au could induce a reconstruction of the surface. Since the simulations preserve the total number of atoms in the surface, they are not likely to find reconstruc- tions, such as a missing row surface, that violate that constraint. For the (100) and (111) surface, no special attempt has been made to investigate the possibility of reconstruction. For the (110) surface, an obvious possible reconstruction is to the missing row surface geometry that is seen on the (110) surfaces of clean Ir, Pt and Au [9]. This surface is created by simply removing every other close-packed row on the (110) surface. In previous work applying the EAM to this reconstruction, the calculated energy of the missing row geometry was lower than that for the unreconstructed surface geometry for both Au and Pt in agreement with the experimental observation that these surface reconstruct [10]. In the present case, simulations have been performed

![](./images/811788769249198080_5.jpg)

Fig. 5. The relative composition of the surface layer and bulk of Cu-Au alloys computed at 300 K by Monte Carlo simulation for the three low index faces.

with the missing row surface geometry for a variety of bulk and so surface compositions. It is found that the Au atoms locate in both the first and second atomic planes with no apparent ordering. However, the energy of the missing row surfaces is computed to be greater than that for the unreconstructed surface indicating that the missing row reconstruction should not be observed in this case.

The calculations also determine the relative compositions of the surface layers and the bulk material corresponding to thermal equilibrium at room temperature. For the (110) surface the Au content of the second layer is comparable to that of the bulk while for both the (100) and (111) surfaces the second atomic layer is found to contain even less Au than the bulk. The relative compositions at 300 K of the outermost surface layer and the bulk are plotted in fig. 5. For the (100) surface, the surface layer reaches a composition close to a half monolayer at bulk compositions of about 0.01 atomic percent at room temperature. The composition of the surface then saturates at a half monolayer as the bulk composition increases further. This saturation of the surface layer is consistent with energy minimization results. The energy of a Au substitutional atom in the bulk is 0.09 eV less than the energy for placing that extra Au atom in a Cu site of the ordered surface. Thus the surface should not exceed $1/2$ monolayer composition since the energy is lowered (and the entropy is increased) by diffusing the extra Au atoms into the bulk. On the other hand, to exchange a Au atom in the ordered surface with a Cu atom in the bulk requires 0.32 eV. Thus, as Au is added to the system, the lowest

energy is obtained by placing Au atoms in the surface layer until it reaches 1/2 monolayer and then placing addition Au atoms in the bulk. This is consistent with the finite temperature results seen in the simulations.

The equilibrium between the surface and bulk compositions is similar for the (111) surface except that the surface composition saturates at 1/3 monolayer and a higher bulk concentration of Au (~ 0.1 at%) is required for this saturation. The (110) surface is qualitatively different in that the surface composition does not saturate though there is a slight flattening out of the surface composition versus bulk composition at a half monolayer. The fact that the surface composition of the (110) face does not saturate with increasing bulk composition suggests that the ordered surface will be harder to prepare in this case since at this temperature the surfaces are only ordered when the surface composition is close to that of the ideal ordered arrangement (i.e. 1/2 monolayer for the (110) surface). Thus there is only a small range of bulk compositions for which the (110) surface orders. On the other hand the onset of order with changing Au content might make an interesting study. The results presented in fig. 5 are for room temperature. At lower temperatures, one would expect that, if thermal equilibrium can be attained, the surface compositions of the (100) and (111) surfaces will saturate at lower bulk Au concentrations. For higher temperatures, a higher bulk concentration of Au would be required to produce the ordered surface layers.

In addition to the compositional order of the surface, the calculations also give information about the detailed atomic positions at the surface. Previous calculations showed that the EAM correctly predicts the inward contraction of the surface layer of the clean metal surfaces [6]. In addition, the surface geometry of the $\mathrm{Ni}_{3} \mathrm{Al}$ surfaces have been computed and it was found that the surface planes are rippled with the Al atoms above the Ni atoms [11]. For all three of the surfaces studied here, the calculations again show a rippled surface with the Au atoms sitting somewhat above the Cu atoms in the surface plane. For the (100) surface, the separation of the second and third atomic planes is within $0.005 \AA$ of the bulk spacing. The spacing from the second atomic layer to the Cu atoms in the surface is $0.02 \AA$ less than the bulk interplanar spacing and the spacing to the Au atoms is $0.16 \AA$ greater than the interplanar spacing. This gives a rippling of $0.18 \AA$ in the surface layer. The second atomic plane has no rippling. Wang et al. [3] find in their LEED analysis that the spacing from the second plane to the Cu atoms in the surface is expanded by $0.08 \AA$ from the bulk spacing and that the spacing from the second plane to the Au atoms is expanded by $0.18 \AA$ from the bulk spacing. This gives a rippling of $0.1 \AA$ in the surface plane. The theory and LEED analysis agree on the position of the Au atoms with respect to the bulk but the calculations place the Cu atoms in the surface plane $0.1 \AA$ closer to the bulk. The calculations for the (111) surface show a rippling of $0.21 \AA$ in the surface layer. The spacing to the Cu atoms in the surface layer is contracted by $0.03 \AA$

while the spacing to the Au atoms is expanded by $0.18\ \mathring{A}$. For the (110) surface, the rippling is calculated to be somewhat smaller. The spacing between the second and third layer Cu atoms is found to be contracted by 0.01 $\mathring{A}$ compared to the bulk spacing of $1.28\ \mathring{A}$. The spacing between the top layer Au and the second layer is expanded by $0.09\ \mathring{A}$ and the spacing to the top level Cu is contracted by $0.04\ \mathring{A}$ to give a rippling of $0.13\ \mathring{A}$.

## 4. Summary

These calculations have shown that the deposition of Au onto the (100) surface of Cu should result in the incorporation of the Au atoms into the surface atomic layer with the Au atoms arranged in a c(2×2) pattern. In addition, the surface should be rippled with the Au atoms residing above the Cu atoms. These results are in agreement with recent LEED experiments. Also, the ordering of Au deposited on the (111) and (110) has been predicted. More generally, the calculations show that compositionally *ordered* surface layers of Au and Cu exist in thermal equilibrium with a compositionally *disordered* bulk Cu containing dilute amounts of Au. In addition, the results show that the EAM is a useful tool for investigating such novel surface behavior since only information about the bulk properties of the materials is required to determine the surface structure and ordering.

## References

[1] P.W. Palmberg and T.N. Rhodin, J. Chem. Phys. 49 (1968) 134.
[2] G.W. Graham, Surface Sci. 184 (1987) 137.
[3] Z.Q. Wang, Y.S. Li, C.K.C. Lok, J. Quinn, F. Jona and P.M. Marcus, Solid State Commun. 62 (1987) 181.
[4] V.S. Sundaram, R.S. Alben and W.D. Robertson, Surface Sci. 46 (1974) 653;
    H.C. Potter and J.M. Blakeley, J. Vacuum Sci. Technol. 12 (1975) 635;
    T.M. Buck, G.H. Wheatley and L. Marchut, Phys. Rev. Letters 51 (1983) 43;
    E.G. McRae and R.A. Malic, Surface Sci. 148 (1984) 551;
    D. Sondericker, F. Jona and P.M. Marcus, to be published.
[5] M.S. Daw and M.I. Daskes, Phys. Rev. Letters 50 (1983) 1285; Phys. Rev. B29 (1984) 6443.
[6] S.M. Foiles, M.I. Baskes and M.S. Daw, Phys. Rev. B33 (1986) 7983.
[7] S.M. Foiles, Phys. Rev. B32 (1985) 7685.
[8] S.M. Foiles, Proc. Materials Research Society Meeting, Symp. J, Boston, 1986, J. Vac. Sci. Technol., in press.
[9] C.M. Chan and M.A. Van Hove, Surface Sci. 171 (1986) 226, and references therein.
[10] M.S. Daw, Surface Sci. 166 (1986) L161;
    S.M. Foiles, Surface Sci., to be published.
[11] S.M. Foiles and M.S. Daw, J. Mater. Res. 2 (1987) 5.