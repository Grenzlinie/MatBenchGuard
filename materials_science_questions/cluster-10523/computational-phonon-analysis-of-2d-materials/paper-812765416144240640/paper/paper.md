# Structural and dynamical properties of Ge(001) in comparison with Si(001) and C(001)

W. Stigler and P. Pavone
Institut für Theoretische Physik, Universität Regensburg, D-93040 Regensburg, Germany

J. Fritsch
Department of Physics and Astronomy, Arizona State University, Tempe, Arizona 85287

(Received 27 April 1998)

We present the results of an *ab initio* calculation of the structural and dynamical properties of the (001) surfaces of Ge and Si. The computations have been performed within density-functional theory and density-functional perturbation theory. The calculated reconstruction parameters show an excellent agreement with previous theoretical investigations and experimental data. First, we have determined the phonon dispersion in the tilted dimer $p(2×1)$ reconstruction. The surface vibrations of Si(001) deviate from those of Ge(001) by characteristic shifts in the frequency of the phonon modes. This fact relates to chemical trends in the reconstruction behavior which are also discussed in comparison with the vibrational properties of the C(001) surface. Furthermore, complete dispersion curves of the surface modes of the $c(4×2)$ and $p(2×2)$ phases of Ge(001) and Si(001) were determined using local-coupling transfer, which is a method for modeling dynamical matrices of large-size superstructures. The phonon modes of the higher-order reconstructions show trends similar to those of the $p(2×1)$ reconstructions. Finally, the interpretation of experimental data from inelastic helium-atom scattering indicates a correlation of the surface dimers with local $c(4×2)$ or $p(2×2)$ symmetry at room temperature. [S0163-1829(98)04043-0]

## I. INTRODUCTION

Although the (001) surfaces of elementary semiconductors have attracted a great deal of interest in recent years, the description of their finite temperature behavior and dynamical properties is far from complete. The basic reconstruction mechanism of Ge(001), Si(001), and C(001) consists in the formation of dimers. Whereas diamond reconstructs into the symmetric $p(2×1)$ geometry, Ge and Si favor buckled dimers. It is generally accepted that the ground state in Ge(001) as well as in Si(001) is the $c(4×2)$ phase. However, the high-temperature structure of these surfaces is still under debate.

In scanning-tunneling microscopy (STM), low-energy electron diffraction (LEED), and ion-scattering experiments, $^{1-4}$ at least three different reconstructions are found for Ge(001), namely the ferromagnetic ordering in the $p(2×1)$ phase and the antiferromagnetic ordering in the higher-order reconstructions (HOR) $p(2×2)$ and $c(4×2)$. A top view of these reconstructions can be seen in Fig. 1. Culbertson *et al.* detected a LEED pattern in Ge(001) corresponding to the $c(4×2)$ phase at 100 K, while the $p(2×1)$ phase with smeared $c(4×2)$ spots was seen at $300$ K. $^{2}$ Whereas in some experiments (angle-resolved photoemission spectroscopy, LEED) a phase transition from the $c(4×2)$ to the $p(2×1)$ geometry is found to occur at $200$ K, $^{3}$ recent x-ray diffraction data indicate that the $c(4×2)$ phase is still dominant at 250 K, comprising approximately 60% of the surface. $^{5}$ The energy difference between the three geometries is indeed very small. In the calculations performed by Needels and co-workers, the antiferromagnetic ordering of the tilted dimers present in the HOR is found to be 0.06 eV per dimer lower in energy than the ferromagnetic ordering of the $p(2×1)$ geometry. $^{6}$

Far more experiments and theoretical investigations have been performed for the silicon surface. For an overview we refer to Refs. 7–10. Recent studies indicate a correlation of the dimers with a local antiferromagnetic ordering also at room temperature. In fact, the measured electronic dispersion curves seem to agree much better with the calculated band structure of the HOR than with those of the $p(2×1)$ phase. $^{8,11,12}$ The $c(4×2)$ and $p(2×2)$ reconstructions are about 0.05–0.07 eV per dimer more stable than the $p(2×1)$ structure. Shkrebtii and co-workers investigated Si(001) with *ab initio* molecular-dynamics runs at finite temperature. $^{10}$ They find the $p(2×1)$ structure not only to be energetically unfavorable but even to be unstable. They observed a spontaneous formation of the $c(4×2)$ and $p(2×2)$ geometries. Along a row the dimers tend to flip simultaneously so that the out-of-phase buckling of the HOR remains unchanged in the direction of the rows. A correlated flipping process of one single row induces a change of local $c(4$

![](./images/812765416144240640_1.jpg)

FIG. 1. Top view of the unit cells (left) and the irreducible parts of the surface Brillouin zones (right) of the $p(2×1)$, $p(2×2)$, and $c(4×2)$ reconstructions. The symmetry $\sigma_{x}$ [together with a nonprimitive translation for the $p(2×2)$ geometry], which only holds for the HOR, maps the two dimers of the respective unit cells onto each other.

$\times 2)$ to $p(2\times 2)$ symmetry and vice versa. Probably, it is the rapid alternation of phases and the small size of the domains with uniform symmetry which causes the overall $p(2\times 1)$ symmetry to be resolved in various experiments, e.g., in STM images where dimers seem to be symmetric at room temperature. $^{13}$

In this paper we report the results of ab initio calculations for the structural and vibrational properties of the Ge(001) and Si(001) surfaces performed using density-functional theory and density-functional perturbation theory (DFPT). To determine the surface phonon bands of the HOR of both surfaces, we employ a new technique of constructing the dynamical matrices by adaptation of the known coupling constants of another reconstruction. A first application of this method of local-coupling transfer (LCT) to the Ge(001) surface has been presented in a previous work. $^{14}$ Relevant information about the structure of Ge(001) at room temperature (RT) is obtained by comparing the calculated dispersion curves with the phonon spectra measured by inelastic He-atom scattering. $^{14}$ Clear evidence of antiferromagnetic ordering is found at room temperature also in Ge, supporting the picture of a dynamically disordered surface with local $c(4$ $\times 2)$ or $p(2\times 2)$ symmetries. Furthermore, while the dispersion curves of the bulk elementary semiconductors Si and Ge are similar if opportunely rescaled, characteristic shifts of the surface bands occur for the rescaled surface bands. This behavior is analyzed and related to chemical trends in the reconstruction behavior.

The paper is organized as follows. In Sec. II, we describe briefly the theoretical framework used to study the structural and dynamical properties of semiconductor surfaces. Results for the atomic surface geometry of the $p(2\times 1)$ and the higher-order reconstructions of Ge(001) and Si(001) are given in Sec. III. The phonon-dispersion curves for the $p(2$ $\times 1)$ phases of both surfaces obtained within DFPT are presented in Sec. IV. In the discussion of Sec. V, we focus on the differences in the dynamics of the two systems by investigating the details of the coupling constants of the atoms in the surface region. In Sec. VI a further comparison with the vibrational features of C(001) reveals the relation between the coupling strength of neighboring atoms in the surface region and the fundamental reconstruction behavior of the three elementary semiconductors. The application of LCT to Ge(001) and to Si(001) is described in Secs. VII and VIII, respectively. Finally, in Sec. IX we compare the phonon dispersion computed for the HOR of Si(001) and Ge(001) and give a conclusive interpretation of the helium-atom scattering data of Ref. 14.

## II. METHODS OF CALCULATION

We used the density-functional theory in the local-density approximation $^{16,17}$ to determine the electronic ground state. Specifically, the Kohn-Sham self-consistent equations $^{17}$ are solved for a given atomic configuration using the exchange-correlation potential in the parametrization of Perdew and Zunger. $^{18}$ The electron-ion interaction is described with the help of norm-conserving pseudopotentials. $^{19-21}$ The Kohn-Sham orbitals are expanded in plane waves up to 9 (8) Ry for the Ge (Si) surfaces. This choice for the kinetic-energy cutoff guarantees convergency for the computed bulk lattice constants and phonon frequencies within $4\%$ with respect to completely converged calculations. $^{6,19}$ Special points for bulk and surface calculations are generated according to the algorithm proposed by Froyen. $^{22}$ In order to restore translational invariance also perpendicular to the surface (z direction), we use a slab geometry with periodically repeated thin crystal films. For the $p(2\times 1)$ phase, each slab consists of ten atomic layers, while the number of layers is reduced to eight for the description of the HOR. Two neighboring crystal films are separated by a vacuum region corresponding to six interlayer distances. This choice ensures the decoupling of the surfaces of one slab and of neighboring films. $^{6,8}$

The surface Brillouin zones (SBZ) and the unit cells in direct space are shown in Fig. 1, together with an illustration of the dimer buckling. The atomic equilibrium positions of the various reconstructions are found by shifting the ions along the Hellmann-Feynman forces. No constraint is imposed on the relaxation of the ions in all of the layers except for correct symmetry. The forces acting on the atoms are minimized to less than 0.1 mRy/a.u., which corresponds to a numerical uncertainty in the equilibrium positions of approximately $0.01$ Å.

The surface lattice dynamics is treated in the framework of first-order density-functional perturbation theory. $^{19,23}$ The dispersions of surface phonon modes of the $p(2\times 1)$ phases are determined by Fourier deconvolution of a set of dynamical matrices calculated on a fine grid of wave vectors in the irreducible wedge of the SBZ. The computation of the surface phonon bands of the HOR of Si and Ge will be described in full detail in Secs. VII and VIII.

## III. ATOMIC SURFACE STRUCTURE

In this section we present our results for the structural details of the $p(2\times 1)$, $c(4\times 2)$, and $p(2\times 2)$ phases of Ge(001). The geometry and total energy of the respective reconstructions in Si(001) have been reported earlier. $^{8}$ The lattice constant of the periodic slab configurations is fixed to the calculated value of $5.57$ Å obtained for the bulk lattice constant of Ge. This is in good agreement with the experimental value of $5.66$ Å.

The relaxation process for the $p(2\times 1)$ geometry was initiated by an opposite displacement in the surface plane of the two first-layer atoms per surface unit cell by $0.4$ Å from their ideal positions. Following the minimum force direction, the system then moved towards the lowest energy structure with symmetric reconstruction (SR). To obtain the energetically more stable tilted dimer configuration, we displaced one of the atoms $0.2$ Å out of the surface plane. The resulting asymmetric reconstruction (AR) turns out to be $0.19$ eV per dimer lower in energy than the SR. The total reconstruction energy is $1.41$ eV per dimer. The bond lengths in the whole slab change by less than $4\%$ as compared to the bulk value of $2.41$ Å. The dimer bond length is $2.39$ Å for the AR and $2.38$ Å for the SR. Considerable shifts of more than $0.4$ Å from the ideal positions only occur in the surface layer perpendicular to the dimer rows. Nonetheless, we observe the same deep penetration of the surface perturbation into the slab as found in Refs. 5 and 24. As can be seen in Fig. 2, we find displacements of more than $0.15$ Å normal to the surface in the first four layers. Since one crystal film comprises only 10

![](./images/812765416144240640_2.jpg)

FIG. 2. Equilibrium positions of the atoms in the first four layers of Ge(001) $p(2\times 1)$ in the tilted dimer configuration. The shifts from the ideal positions are indicated in $\mathring{\text{A}}$.

layers and both surfaces are allowed to relax, we cannot trace the geometric perturbation any further. In the remaining sections we will consider only the energetically favored asymmetric $p(2\times 1)$ configuration. The tilt angle of the dimers is found to be $17^\circ$. The relaxation parameters compare well with the results of the $ab$ initio calculations of Krüger $et$ $al.^{25}$ and Needels $et$ $al.^{26}$ as well as with the data from LEED (Ref. 2) and x-ray diffraction. $^{5,24}$

Similarly to Si(001), characteristic differences are seen in the comparison of the electronic band structure of the symmetrically reconstructed and the tilted-dimer Ge(001) surface. While the SR turns out to be metallic, the AR is semiconducting with a band gap of 0.23 eV. We obtain a band structure that is almost identical with the one found in the $ab$ initio calculation by Krüger and co-workers. $^{27}$ Some of the most prominent features such as the dangling-bond state corresponding to the up-shifted dimer atoms reproduce very well the dispersion curves measured by angle-resolved spectroscopy experiments. $^{28,29}$ Furthermore, there are only small differences in the dispersion curves of the (001) surfaces of Ge and Si. For more details we refer the reader to Refs. 8, 25, and 27.

To determine the relaxed positions of the HOR, the structure optimization is started from initial positions obtained by transferring the results from the tilted dimer $p(2\times 1)$ reconstruction according to the antiferromagnetic ordering of the dimers. Unlike in the $p(2\times 1)$ phase, where a relaxation of the subsurface layer atoms along the dimer rows is forbidden for symmetry reasons, they are displaced $0.12\ \mathring{\text{A}}$ in this direction in the HOR. The upper dimer atoms pull their nearest neighbors in the second layer closer to the dimer, while the lower first-layer atoms push their nearest neighbors of the second layer in the opposite direction. This lowers the total energy of the HOR by 0.08 eV per dimer relative to the asymmetric $p(2\times 1)$ configuration. The dimer bonds turn out to be $0.05\ \mathring{\text{A}}$ longer than in the $p(2\times 1)$ phase. The bonding lengths in the whole surface region differ by only $0.01\ \mathring{\text{A}}$ in the $p(2\times 2)$ and $c(4\times 2)$ phase.

### IV. PHONON DISPERSION OF THE $p(2\times 1)$ PHASES

The vibrational properties of the $p(2\times 1)$ configurations of Ge(001) and Si(001) are determined by calculating the dynamical matrices of fully relaxed ten-layer slabs on a uniform grid of 12 $\mathbf{q}$ points in the irreducible part of the SBZ, which corresponds to a (6,4) mesh. $^{30}$ By Fourier deconvolution on this grid, we obtain the real-space force constants up to a distance of two bulk lattice constants. Using these force constants, dynamical matrices can be obtained at arbitrary wave vectors of the SBZ. Similarly, in order to get the force constants of the bulk, we use a mesh of 19 $\mathbf{q}$ points in the fcc cell, generated according to the special-points scheme by Froyen with $\mathbf{f}_0=0.^{22}$

The force constants in the central region of the thin crystal films are essentially the same as the corresponding values of the bulk, which are, nevertheless, about 4% larger. This indicates the deep penetration of the surface perturbation into the bulk. The force constants in the surface region of the ten-layer slabs are significantly different from the bulk, due to the reconstruction and charge redistribution. Since macroscopic eigenmodes penetrate deeply into the bulk, we construct the dynamical matrices of crystal films comprising much more than only ten atomic layers. While the force constants in the surface region of the larger crystal films are assumed to be the same as the respective force constants of the small crystal films, the bulk force constants are used without modification for the inner region. The following calculations have been performed with a 26-layer slab. Inserting more than 16 bulk layers does not change the results significantly. Moreover, weakening of the bulk constants by 4% does not affect the phonon dispersion of the surface to a notable extent.

Empirical potentials designed for molecular-dynamics simulations lead to potential wells that are shallower and wider for Ge than for Si. $^{31}$ Our computations confirm this observation. In fact, multiplication of the Si force constants by a factor 0.937 yields bulk frequencies nearly identical to the bulk vibrations of Ge throughout the SBZ, if we additionally take into account the different masses. Therefore, it

![](./images/812765416144240640_3.jpg)

FIG. 3. Phonon dispersion of the $p(2\times 1)$ surfaces of Ge (thick lines) and Si (thin lines). Eigenmodes with dominant displacements in the first two layers are given by solid lines. The shaded area represents the surface projected band structure of the bulk. The Ge (Si) frequency scale is given at the left (right).

is possible to investigate the surface dynamics of Ge(001) and Si(001) by using the same energy scale for both materials. In the following text we use for Si rescaled coupling constants and replace its mass by the mass of Ge. In this way, the bulk phonon spectra of Ge and Si are essentially identical. Furthermore, distances in Si have been rescaled according to the ratio of the lattice constants $a_{0}(\text{Ge})/a_{0}(\text{Si})$.

In Fig. 3 we show the dispersion of the most prominent surface bands of both semiconductors. With the exception of the resonant feature $B_{1}$, which is only found in Ge near the lower rim of the bulk continuum along the $\overline{J}\overline{K}$ direction, both systems exhibit the same surface vibrational states. While the surface projected bulk band structure of Si is nearly indistinguishable from that of Ge, significant differences are seen in the dispersion only for some surface phonon bands.

Along the $\overline{\Gamma}\overline{J}$ direction all modes of the slab can be strictly separated into vibrations with pure sagittal polarization (SP) or shear horizontal (SH) polarization. While the SP modes are symmetric with respect to the mirror plane perpendicular to the dimer rows, SH modes are asymmetric. The lowest acoustic bands are the Rayleigh wave (SP), $A_{1}$ (SH), and $A_{2}$ (SP). Given the elastic constants, the velocity $v_{R}$ of the Rayleigh wave (RW) can be calculated with continuum theory. In Ge ($v_{R}=3065$ m/s) as well as in Si ($v_{R}$ $=5084$ m/s), the velocity of the RW is larger than the velocity of the lowest acoustic bulk wave ($v_{\text{SH}}=2750$ m/s, 4674 m/s),$^{32}$ which limits the surface projected bulk band structure. Hence, the RW is not pushed below the bulk continuum near the zone center in this direction of the dispersion. The three acoustic bands are therefore bulk resonant.

Beside the acoustic surface vibrations, we observe the following phonon modes in Ge(001). The main feature of the rocking mode $r$ ($\overline{\Gamma}$: 14.1 meV) is a periodic change of the dimer tilt angle. In the swinging mode $s$, which can only be identified along the $\overline{K}\overline{J}$ direction, the dimer atoms exhibit an in-phase displacement along the rows. The dimer stretch modes $ds_{1}$ ($\overline{K}$: 24.5 meV) and $ds_{2}$ ($\overline{K}$: 32.6 meV) are characterized by an oscillation of the dimer bond length. In the high-energy stretching mode $sb_{2}$ the bonds between the upper dimer atoms and the respective nearest neighbors in the subsurface layer are periodically varied with an energy at the $\overline{K}$ point of 26.3 meV, while in the mode ($sb$) the lower surface atoms perform a bond length oscillation with their nearest neighbors in the subsurface layer at an energy of 35.5 meV.

Although the coupling constants of Si have been rescaled to smaller values according to the bulk frequencies, all modes of Si(001) are higher in energy compared to Ge(001) except for the band $r$. In order to understand this observation, we examine the coupling parameters of the atoms in the surface region and their connection with the chemical details of the surface reconstruction.

## V. INFLUENCE OF STRETCH AND TRANSVERSE FORCE CONSTANTS ON THE PHONON DISPERSION

By means of density-functional calculations, Krüger *et al.* found clear chemical trends in the reconstruction behavior of the (001) surfaces of C, Si, and Ge.$^{25}$ Whereas diamond favors a $\sigma$-$\pi$ double bond between the dimer atoms in the symmetric configuration, yielding a bond length similar to the distance between the two carbon atoms in the $\text{C}_{2}\text{H}_{4}$ molecule, Ge reconstructs asymmetrically with a distance between the dimer atoms almost equal to the bond length in $\text{Ge}_{2}\text{H}_{6}$. For Si, the dimer bond length is in between the length of the double bond in $\text{Si}_{2}\text{H}_{4}$ and that of the single bond in $\text{Si}_{2}\text{H}_{6}$.

In order to analyze the coupling strength as a function of the bond length, we investigate in detail the force constants of Si(001) $p(2\times 1)$ and Ge(001) $p(2\times 1)$ between nearest neighbors residing at the equilibrium positions $\mathbf{R}_{\kappa}$ and $\mathbf{R}_{\kappa'}$. The modulus of the force acting on the atom $\kappa$ has a maximum if the atom $\kappa'$ is displaced along the vector $\mathbf{R}_{\kappa\kappa'}^{\text{n.n.}}$ $=\mathbf{R}_{\kappa}-\mathbf{R}_{\kappa'}$. As expected, the direction along which the force has a maximum coincides with the direction of the covalent bonds. Only small deviations from the ‘‘ideal’’ direction defined by the bond direction of less than $6^{\circ}$ are seen for the atomic displacements and the resulting extremal forces.

Consequently, if the atom $\kappa'$ is shifted by the vector $\mathbf{u}_{\kappa'}$ in an arbitrary direction with constant $|\mathbf{u}_{\kappa'}|$, the projection $\mathbf{u}_{\kappa'}\cdot\mathbf{F}_{\kappa}$ of the force $\mathbf{F}_{\kappa}$ acting on the atom at the position $\mathbf{R}_{\kappa}$ will have a maximum for $\mathbf{u}_{\kappa'}\parallel\mathbf{R}_{\kappa\kappa'}$. Therefore, the directions of the atomic shifts $\mathbf{u}_{\kappa'}$ which lead to extremal projections can be determined by calculating the extrema of $\mathbf{u}_{\kappa'}$ $\cdot\mathbf{F}_{\kappa}=\sum_{i,j}u_{\kappa i}K_{ij}^{\text{n.n.}}(\kappa,\kappa')u_{\kappa'j}$ with the boundary condition that $|\mathbf{u}_{\kappa'}|$ is constant:

$$
\frac{\delta}{\delta u_{\kappa'l}}\left[\sum_{i,j}u_{\kappa i}K_{ij}^{\text{n.n.}}(\kappa,\kappa')u_{\kappa'j}-\lambda\sum_{i,j}\delta_{i,j}u_{\kappa'j}\right]=0. \quad (1)
$$

The indices $i$ and $j$ refer to the Cartesian coordinates. The $(3\times 3)$ matrix $\mathbf{K}_{ij}^{\text{n.n.}}(\kappa,\kappa')$ is the respective part of the force-constant matrix of the entire crystal film. The solutions of

Eq. (1) are the eigenvectors of the symmetric matrix $\frac{1}{2}[\mathbf{K}_{ij}^{\text{n.n.}}(\kappa,\kappa')+\mathbf{K}_{ji}^{\text{n.n.}}(\kappa,\kappa')]$. The eigenvalues have the interpretation of extremal force constants. In this way, we obtain one bond-stretch force constant $\Phi_S$ and two transverse force constants $\Phi_{T_1}$ and $\Phi_{T_2}$. The corresponding eigenvectors $\mathbf{V}_{T_1}$ and $\mathbf{V}_{T_2}$ have to be orthogonal to $\mathbf{V}_S$ and to one another. For symmetry reasons, these constants are associated with displacements $\mathbf{u}_{\kappa'}$ along $(\Phi_S)$ and perpendicular $(\Phi_{T_1},\Phi_{T_2})$ to the bonding direction in the bulk. Furthermore, the two transverse force constants are identical.

For the surface system, the bonding directions coincide with the eigenvectors associated to the $\Phi_S$ constants up to $6^\circ$ in the entire slab. Therefore, the vectors $\mathbf{V}_{T_1}$ and $\mathbf{V}_{T_2}$ are almost perpendicular to the bonding direction. The values $\Phi_{T_1}$ and $\Phi_{T_2}$ are found to be almost identical. Furthermore, the $(3\times 3)$ matrices $\mathbf{K}^{\text{n.n.}}(\kappa,\kappa')$ between nearest neighbors in the slabs are almost symmetric, so that the $\Phi$'s and the $\mathbf{V}$'s can also be obtained from the diagonalization of $\mathbf{K}^{\text{n.n.}}(\kappa,\kappa')$. The stretch force constants $\Phi_S$ are dominant by a factor 5 to 8 over all of the other elements of the force-constant matrix of the slabs, on-site coupling excluded. The latter can be obtained using translational invariance of the system. The magnitude of the force constants between second nearest neighbors, e.g., is less than 10% of the largest nearest-neighbor coupling. Hence the interaction between nearest neighbors plays the most important role not only for structural and electronic but also for the vibrational properties. The $\Phi_S$ values depend almost linearly on the bond lengths. This fact is also confirmed by extracting the stretch force constants from the coupling parameters of the $c(4\times 2)$ phase in Si(001) as described in Sec. VIII. The graph obtained in this way is the same for Ge and Si after rescaling the quantities of Si as explained in the preceding section.

The rescaled bond lengths in the surface region of Si(001) are smaller compared to the respective interatomic distances in Ge(001). Because of that, the corresponding stretch force constants are larger and all the Si surface bands involving significant bond-length oscillations are shifted to higher frequencies. Especially the dimer bond and the back bonds of the upper dimer atoms are stronger in Si(001) by about 21% and 10%, respectively. This leads to the different vibrational behavior of the two systems. To demonstrate this, we have replaced these stretch force constants in Ge by those of Si (including the rescaling), while the rest of the force-constant matrix remained unchanged. This was achieved by simply exchanging the mentioned eigenvalues of the corresponding diagonalized $(3\times 3)$ matrices $\mathbf{K}(\kappa,\kappa')$ and then transforming back to Cartesian coordinates. We did not adjust the bonding directions since they differ by less than $5^\circ$ throughout the slabs of the two systems. The resulting change in phonon dispersion of Ge(001) consists in a shift of the bands $sb$, $sb_2$, $ds_1$, $ds_2$, and $s$ to higher frequencies. As a result, the bands $sb$, $sb_2$, and $ds_1$ are in almost perfect agreement with the respective phonon bands of Si(001). The bulk resonant mode $B_1$ is pushed in parts into the bulk continuum, where it cannot be detected anymore. The three acoustic modes, however, are hardly influenced since these eigenmodes are characterized by a collective in-phase motion of surface atoms. Finally, almost negligible changes are found for the rocking mode since it is strongly bulk resonant and is characterized by a periodic variation of the dimer tilt angle. To alter the frequency of the rocking mode, the transverse force constants would also have to be adapted.

## VI. COMPARISON WITH C(001)

In order to extract general trends for the dynamical properties of group-IV tetrahedral semiconductor surfaces, we present in this section a comparison of our results for Si and Ge with the calculation of C(001) performed by Alfonso and co-workers.¹⁵ They determined the vibrational properties of C(001) within frozen-phonon calculations using the Harris total-energy functional. Since C(001) reconstructs symmetrically in the $p(2\times 1)$ phase, a one-to-one correspondence between the vibrational surface features of C(001) and Si(001) or Ge(001) cannot be established. For example, the modes $sb$ and $sb_2$, which are related to bond-length oscillations between one of the surface atoms and the respective nearest neighbors in the subsurface layer, do not appear in C(001) because of the mirror symmetry with respect to the plane perpendicular to the direction of the dimers. The corresponding feature on the C(001) surface is a medium-energetic bouncing mode characterized by an in-phase motion of the two dimer atoms in and out of the surface plane.

To compare the remaining surface modes, we need to find a common energy scale for diamond and Ge. To this aim, the simplest procedure which includes both masses and coupling-constant effects consists in scaling the diamond frequencies to give identical optical bulk frequencies at the $\bar{\Gamma}$ point [multiplication by $\omega_{\text{Ge}}(\Gamma)/\omega_{\text{C}}(\Gamma)$]. In contrast with Si and Ge, where simply rescaling the phonon energies yields nearly identical bulk band structures, the rescaled dispersion curves of diamond and Ge exhibit small differences for the bulk. The maximum of the optical frequencies in diamond is, e.g., slightly higher than $\omega_{\text{C}}(\Gamma)$ whereas the two values coincide in Ge and Si.¹⁹,³⁶ Nonetheless, the proposed way of rescaling the phonon energies of C(001) is sufficient for our purposes since only rough estimates need to be drawn for the following discussion.

Except for the mentioned bouncing mode that is not found in Ge and Si, Alfonso *et al.* detect a rocking mode in the rescaled energy range of 17 to 35 meV, a swinging mode at 29–36 meV, and a dimer stretch mode at approximately 42 meV. These bands are all placed substantially above the Si and especially the Ge bands. Another high-frequency feature is a twisting mode reported for C(001) at the rescaled energy range of 36 to 38 meV, which is characterized by an opposing movement of the dimer atoms in the direction of the rows. Modes with similar displacement pattern are found in Si and Ge in the wide energy range of 19 to 32 meV, due to a strong coupling with subsurface layer vibrations.

The frequency of the dimer stretch mode $\omega_{\text{C}}(ds)$ in C(001) is well above the bulk continuum. Furthermore, $\omega_{\text{C}}(ds)$ resides in the middle between the singly bonded C—C stretching frequency of ethane (28.5 meV) and the double-bonded C$\xlongequal{}$C stretching frequency in ethene (46.5 meV). Although the bond length of the dimer atoms in C(001) basically coincides with the C$\xlongequal{}$C distance in ethene, the stretching frequency is considerably lower at the surface, indicating a coupling with subsurface layer vibrations.

The results for C(001) are consistent with our findings for

the relation between the coupling strength of adjacent surface atoms and the chemical details of the reconstruction. The primary relaxation mechanism after cutting an elemental semiconductor along a (001) plane is to saturate the remaining dangling bonds of the surface atoms. Since the $2p$ atomic orbitals are more localized than the $2s$ orbitals in diamond, $p$-like states are able to accumulate charge in the bonding region very efficiently, leading to a strong tendency of $\pi$-bond formation. This mechanism is suppressed in Si and especially in Ge since the $p$ valence bonds being orthogonal to the $p$ orbitals in the core region are more extended than the $s$ valence states. Consequently, Ge and Si favor the tilted-dimer configuration, with the surface atoms forming a single $\sigma$ bond in Ge and a $\sigma$ bond with a small $\pi$-bond admixture in Si.

These observations were already reported by Krüger *et al.* in Ref. 9 and used to explain the different type of reconstruction. Our results indicate that the tendency of Si and especially of C to form stronger bonds than Ge is not restricted to the dimer atoms but manifests itself in the whole surface region. For example, all the rescaled bond lengths in Si(001) turn out to be smaller than the corresponding interatomic distances in Ge(001). Furthermore, stronger bonds enforce the dynamical coupling between adjacent atoms. Consequently, all the surface phonons involving bond-length oscillations are energetically higher in Si and especially in C than in Ge.

## VII. PHONON DISPERSION OF THE HOR OF Ge(001)
Whereas we used DFPT for the determination of the vibrational features of the $p(2\times 1)$ geometry in Ge(001), the direct *ab initio* calculation of the surface phonons of HOR is not computationally feasible, because of the large number of atoms in the slab unit cell. Instead, we propose an approach for extracting information about the dynamical properties of the HOR from the knowledge of the force constants of the $p(2\times 1)$ phase. This method, which has been published in a previous Letter, $^{14}$ is mainly based on considerations on the structure and symmetry.

The coupling constants of the $p(2\times 1)$ geometry have been analyzed in Sec. V. As stated there, a rapid decrease of the magnitude of the coupling constants with increasing interatomic distances is observed. The nearest-neighbor interaction dominates the vibrational properties of the elemental semiconductors. Therefore, reasonable results can be obtained by adapting mainly the nearest-neighbor force constants to the different structures. In the following, we describe the adaptation procedure in terms of the eigenvalues and eigenvectors of $\mathbf{K}^{\text{n.n.}}$.

The nearest-neighbor force-constant matrices of the HOR are obtained by transferring the $\Phi$'s and the $\mathbf{V}$'s from the $p(2\times 1)$ geometry to the HOR. Major changes occur for the dimer pairs $D_{1}$ and $D_{2}$, which are schematically represented in Fig. 4. The known eigenvectors $\mathbf{V}_{S}$ and $\mathbf{V}_{T}$ of the dimer $D_{1}$ in the $p(2\times 1)$ phase are first rotated about an axis along $V_{T_{2}}$ (direction of the dimer row) by $1^{\circ}$ to yield the eigenvectors of $D_{1}$ in the HOR. This procedure is consistent with the difference in the value of the tilt angle between the two reconstructions. For obtaining the force constants of the dimer $D_{2}$, we perform a subsequent reflection according to the $\sigma_{x}$ ![](./images/812765416144240640_4.jpg)

FIG. 4. Graphic representation of two subsequent dimers along the dimer row for the $p(2\times 1)$ (left) and $c(4\times 2)$ or $p(2\times 2)$ (right) phases. We also display for each dimer the eigenvectors of the force constant matrix $K_{ij}$ between the two dimer atoms. The symmetry $\sigma_{x}$ maps the dimer $D_{1}$ of the HOR onto the dimer $D_{2}$. symmetry; $\mathbf{V}_{T_{2}}$ remains unchanged by this reflection. The eigenvalues $\Phi_{S}$ are then adapted for both dimers according to the slightly changed dimer bond length in the HOR as compared to the $p(2\times 1)$ phase, using the graph established between bond lengths and magnitude of the stretch force constants in Sec. V. As mentioned there, the $\Phi_{T}$ values need not be altered. The procedure is the same for all the other bonds between neighboring atoms.

The coupling constants between atoms at a greater distance can be adapted to the antiferromagnetic ordering by imposing the $\sigma_{x}$ symmetry of the HOR onto the corresponding real-space force constants of the $p(2\times 1)$ geometry. Force constants which are forbidden by symmetry in the basic reconstruction cannot be obtained with this procedure. However, these constants have a small magnitude and, therefore, have only a small effect on the phonon dispersion. The on-site $\mathbf{K}$ matrices are determined by imposing the translational invariance of the slab. Finally, the force-constant matrix is slightly modified to assure also the rotational invariance of the surface system. This can be achieved with the help of a Monte Carlo algorithm. We vary the values of the symmetric force-constant matrix with the constraint of correct space symmetry and minimize the deviations from the acoustic sum rule and from the rotational invariance as well as the magnitude of the variations.

We estimate the error of each value in the force-constant matrix $\Delta K_{ij}^{\text{max}}(\mathbf{R},\mathbf{R}')$ between atoms at the positions $\mathbf{R}$ and $\mathbf{R}'$ to be not more than 5% of the biggest on-site coupling, which corresponds in magnitude to a typical second-nearest-neighbor coupling constant. Since the phonon eigenvectors $\mathbf{v}_{\lambda}$ obey in short notation the equation
$$
K\mathbf{v}_{\lambda}=\omega_{\lambda}^{2}\mathbf{v}_{\lambda},
$$
we can approximate the error $\Delta \omega_{\lambda}^{2}$ by means of first-order perturbation theory
$$
\Delta \omega_{\lambda}^{2}=\langle\mathbf{v}_{\lambda}|\Delta K|\mathbf{v}_{\lambda}\rangle,
$$
which yields the error in the frequencies
$$
\Delta \omega_{\lambda}=\frac{1}{2\omega_{\lambda}}\langle\mathbf{v}_{\lambda}|\Delta K|\mathbf{v}_{\lambda}\rangle. \tag{2}
$$

We assume the values of $\Delta K_{ij}(\mathbf{R},\mathbf{R}')$ to be statistically independent, unless they are identical, which can be the case for, e.g., symmetry reasons. If we additionally assume the value of $\Delta K_{ij}(\mathbf{R},\mathbf{R}')$ for a given set of parameters

![](./images/812765416144240640_5.jpg)

FIG. 5. Measured dispersion of surface vibrational states (crosses) in comparison with the calculated surface phonon bands (thick lines) for the $p(2\times 1)$ reconstruction along the $\overline{\Gamma M}$ direction. Different gray scales reflect the magnitude of the calculated scattering intensities.

$\{i,j,\mathbf{R},\mathbf{R}'\}$ to be with equal probability between $-\Delta K_{ij}^{\text{max}}(\mathbf{R},\mathbf{R}')$ and $+\Delta K_{ij}^{\text{max}}(\mathbf{R},\mathbf{R}')$, we can compute the standard deviation of $\Delta\omega_{\lambda}$.

Equation (2) shows that high-frequency modes can be computed very accurately. Phonon frequencies that correspond mainly to an in-phase vibration of the surface atoms are rather insensitive to variations in the local structure, and can also be approximated very well if the acoustic sum rule holds. For low-energetic nonacoustic modes, however, the error may become quite large. Our error analysis predicts an uncertainty for the phonon frequencies of Ge(001) of less than 1 meV, except for the $t$ mode, which will be described in Sec. IX.

The reliability of our method has been tested for Si(001) where the dynamical matrix at the $\overline{J}$ point of the $c(4\times 2)$ geometry has been calculated with DFPT. $^{8}$ This matrix compares very well with the one determined by transferring the force constants of the $p(2\times 1)$ phase of Si(001). The deviations are consistent with our error analysis.

The full dispersion of Ge(001) is presented together with the results for Si(001) in Sec. IX. At the end of this section we discuss the calculated surface phonon bands of the HOR and the $p(2\times 1)$ phase in the lower part of the frequency spectrum. Important information about the vibrational states in Ge(001) can be obtained by comparing these modes with the results recently obtained by inelastic helium-atom scattering. $^{14}$ For Si(001), no such data are available. At room temperature (RT), the Ge(001) surface exhibits monatomic steps, so that two different types of domains, with dimer rows in the $[1\overline{1}0]$ and $[110]$ direction, respectively, are probed at the same time. We restrict our discussion to the time-of-flight spectra recorded at RT along the $[100]$ direction, which is the only one common to the two domains.

To compare our results with the measured data, we have calculated the differential reflection coefficient of inelastic He-atom scattering according to Eq. 6.37 of Ref. 33, which has been successfully applied earlier. $^{34,35}$ The contribution to the scattering cross section is dominated by the displacements of the surface atoms along the surface normal, thermally weighted by the Bose-Einstein factor.

In Fig. 5, the calculated low-energy surface phonon bands and scattering intensities of the Ge(001) $p(2\times 1)$ phase are shown together with the measured dispersion along the $[100]$ direction. The experimental data forming the flat branch at 7 meV are related to a strong feature prominent in the time-of-flight spectra. This flat feature, which is also resolved in the $[110]$ direction, is not reproduced by our calculations in any direction. This clearly shows that the $p(2\times 1)$ phase cannot describe conclusively the phonon dispersion of Ge(001) at RT. Therefore, important contributions to the phonon spectra have to come from HOR.

![](./images/812765416144240640_6.jpg)

FIG. 6. Theoretical (thick lines) and measured surface bands (crosses) in the $[100]$ direction in the energy range accessible to inelastic He-atom scattering displayed for the HOR. The $x$ scale of the figures is referred to the $\overline{M}$ point of the basic $(1\times 1)$ surface geometry which corresponds to the $\overline{\Gamma}$ $(\overline{J})$ point in the $p(2\times 2)$ $[c(4\times 2)]$ structure. We display all the calculated surface vibrations which are mainly localized in the upper two layers. In the sketched window we observe six to eight bulk resonant bands with diffuse displacement patterns. Therefore, we refrain from continuing the calculated dispersion curves within these areas. The error bars are approximately the same for all the data points and are indicated only for some representative points. The uncertainty in the calculated frequencies within the LCT approach is less than 1 meV. A further band, not displayed in this viewgraph, is the rocking mode $r$ at 13 to 14.5 meV which produces weak peaks in the scattering intensities, in agreement between experiment and theory.

In Figs. 6 and 7 we display the calculated surface bands and scattering intensities for the HOR of Ge(001) in comparison with the features seen in the time-of-flight spectra. Pronounced surface phonons obtained by means of the LCT approach in the lower part of the dispersion along the $[1\overline{1}0]$ direction are the Rayleigh wave (RW), the acoustic $A_{1}$ and $A_{2}$ features with displacements of the upper-layer atoms mainly along $(A_{1})$ and perpendicular $(A_{2})$ to the dimer rows, and the previously mentioned $t$ band, associated with a twist-

![](./images/812765416144240640_7.jpg)

FIG. 7. Two recorded time-of-flight spectra along the $[100]$ direction. The incident angle is $28.5^{\circ}$ (a) and $23.5^{\circ}$ (b). The inelastic phonon peaks correspond to the $\text{RW}_{f}$ band (1), the $\text{RW}_{f,2}$ mode near the $\overline{\Gamma}$ point (2), the acoustic branch (RW) near the $\overline{M}$ point (3), the features inside the sketched window of Fig. 6 (4), the 5 meV mode near the $\overline{M}$ point (5), and the RW band near the $\overline{\Gamma}$ point (6).

ing motion of the dimer atoms in the surface plane. The bands $A_{2f}$, $\mathrm{RW}_{f}$, and $\mathrm{RW}_{f,2}$ are related to the folding of surface bands of the $p(2\times 1)$ phase according to the geometry of the HOR. The major contributions to the calculated scattering cross section arise from the RW band near the zone center and the flat $\mathrm{RW}_{f}$ branch near 7 meV almost throughout the entire SBZ of the HOR. It is important to note that all measured surface modes represented by crosses in Fig. 6 are in good agreement with the calculated intensities and phonon branches, which is also the case for the [110] and $[1\overline{1}0]$ directions not displayed here. The RW mode near the zone center is not pushed below the bulk continuum in Ge (as in Si), which results in a mixing with bulk states. This can account for the scatter of the experimental data below 3 meV.

Especially the 7 meV feature which is completely missing in the calculated spectrum of the $p(2\times 1)$ geometry is prominent assuming HOR for Ge(001). Hence, the $p(2$ $\times 1)$ geometry cannot describe the surface reconstruction of Ge(001) at RT. The much better agreement seen in Fig. 6 clearly reveals fingerprints of the $c(4\times 2)$ or $p(2\times 2)$ phase prevalent in the measured phonon dispersion. The phonon modes calculated for the $c(4\times 2)$ phase include the weak 5 meV feature experimentally resolved near the $\overline{M}$ point, but not the lower band. The $p(2\times 2)$ geometry reproduces the acoustic branch (RW) near the $\overline{M}$ point, but not the branch at 5 meV.

We interpret those observations in the following way: (i) both structures occur on Ge(001) at RT; (ii) neighboring dimers are likely to flip simultaneously as observed in the molecular-dynamics simulation by Shkrebtii *et al.* for $\text{Si}(001);^{10}$ (iii) since this mechanism induces a change of local $c(4\times 2)$ to $p(2\times 2)$ symmetry and vice versa, we get contributions to the scattering intensities from both reconstructions; (iv) simultaneous flipping of the dimers along a row requires a significant correlation which manifests itself also in the energy difference between the HOR and the $p(2\times 1)$ phase of 0.08 eV per dimer.

### VIII. APPLICATION OF LCT TO Si(001)
For the application of LCT to Si(001) we can use additional information since the dynamical matrix at the $\overline{J}$ point of the $c(4\times 2)$ geometry has been computed also by means of DFPT. This enables us to calculate the phonons of the HOR with higher precision.

First we consider the force-constant matrix of Si(001) $c(4\times 2)$. Neglecting masses, the dynamical matrix at some $\mathbf{q}$ point is given by
$$
D_{ij}(\kappa,\kappa'|\mathbf{q})=\sum_{l_{1},l_{2}}K_{ij}(\kappa^{0,0},\kappa'^{l_{1},l_{2}})e^{i\mathbf{q}\cdot\mathbf{R}_{l_{1},l_{2}}}.
$$

In this section, $\kappa,\kappa'$ and $l_{1},l_{2}$ are indices for the atoms and surface unit cells, respectively. Considering the rapid decay of the interatomic coupling for large distances, any pair $\kappa,\kappa'$ of atoms can be classified according to one of the following two cases.

In the first case, the dynamical matrix $D_{ij}(\kappa,\kappa'|\mathbf{q})$ essentially has contributions from one coupling constant $K_{i,j}(\kappa^{0,0},\kappa'^{\hat{l}_{1},\hat{l}_{2}})$ only. In Fig. 8 we have illustrated as an example the force constants between one of the upper dimer atoms $1^{0,0}$ and the corresponding lower dimer atom $3^{l_{1},l_{2}}$ in different unit cells. We can neglect all contributions except the nearest-neighbor coupling $K_{ij}(1^{0,0},3^{0,0})$ and set $K_{ij}(\kappa^{0,0},\kappa'^{l_{1},l_{2}})$ to
$$
\begin{aligned}
D_{ij}(\kappa,\kappa'|\mathbf{q})e^{-i\mathbf{q}\cdot\mathbf{R}_{l_{1},l_{2}}},&&\{l_{1},l_{2}\}=\{\hat{l}_{1},\hat{l}_{2}\},\\
0,&&\{l_{1},l_{2}\}\neq\{\hat{l}_{1},\hat{l}_{2}\}.
\end{aligned}
$$

![](./images/812765416144240640_8.jpg)

FIG. 8. Top view of the Si(001) $c(4\times 2)$ reconstruction. The atomic index $\kappa$ and the two-dimensional lattice vector $\mathbf{R}_{l_{1},l_{2}}$ of some assorted atoms in the notation $\kappa^{l_{1},l_{2}}$ are indicated.

In the second case, there are two contributions $K_{ij}(\kappa^{0,0},\kappa'^{\hat{l}_{1}^{1},\hat{l}_{2}^{1}})$ and $K_{ij}(\kappa^{0,0},\kappa'^{\hat{l}_{1}^{2},\hat{l}_{2}^{2}})$ to be taken into account for the determination of the dynamical matrix. As depicted in Fig. 8, the matrix $D_{ij}(1,2|\mathbf{q})$, e.g., has major contributions from the coupling between the upper dimer atom $1^{0,0}$ and the lower atom 2 of the two neighboring dimers along a row. These two $(3\times 3)$ force-constant matrices, however, are not independent of one another for symmetry reasons (reflection about a plane through the central dimer). In fact, for $\mathbf{q}$ equal to the $\overline{J}$ point of the $c(4\times 2)$ geometry, these two force constants add up to
$$
\begin{aligned}
&K_{ij}(\kappa^{0,0},\kappa'^{\hat{l}_{1}^{1},\hat{l}_{2}^{1}})e^{i\mathbf{q}\cdot\mathbf{R}_{\hat{l}_{1}^{1},\hat{l}_{2}^{1}}}+K_{ij}(\kappa^{0,0},\kappa'^{\hat{l}_{1}^{2},\hat{l}_{2}^{2}})e^{i\mathbf{q}\cdot\mathbf{R}_{\hat{l}_{1}^{2},\hat{l}_{2}^{2}}}\\
&\quad=2e^{i\mathbf{q}\cdot\mathbf{R}_{\hat{l}_{1}^{1},\hat{l}_{2}^{1}}}\begin{pmatrix}
a_{11}&0&a_{13}\\
0&a_{22}&0\\
a_{31}&0&a_{33}
\end{pmatrix}
\end{aligned}
$$
since the two phases are equal at the $\overline{J}$ point and
$$
K_{ij}(\kappa^{0,0},\kappa'^{\hat{l}_{1}^{1},\hat{l}_{2}^{1}})=\begin{pmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{pmatrix},
$$
$$
K_{ij}(\kappa^{0,0},\kappa'^{\hat{l}_{1}^{2},\hat{l}_{2}^{2}})=\begin{pmatrix}
a_{11}&-a_{12}&a_{13}\\
-a_{21}&a_{22}&-a_{23}\\
a_{31}&-a_{32}&a_{33}
\end{pmatrix}.
$$

Consequently we obtain the elements $a_{11}$, $a_{22}$, $a_{33}$, $a_{13}$, and $a_{31}$ of the two considered force-constant matrices through the investigation of the dynamical matrix. Unfortunately, the elements $a_{12}$, $a_{21}$, $a_{23}$, and $a_{32}$ are not accessible

![](./images/812765416144240640_9.jpg)

FIG. 9. Side view of the HOR atomic geometry. The area marked row 1 indicates a unit cell as used in our computations. The unit cell is chosen to incorporate the atoms displayed in the figure and two more per layer behind those. The atomic index of the atom behind the atom $\kappa$ is $\kappa+1$. As an example, the index 1 corresponds to an upper dimer atom. The lower first-layer atom of the neighboring dimer along the row has index 2.

in this way. From the bulk and the $p(2 \times 1)$ geometry, however, we know that the diagonal elements $a_{11}, a_{22}, a_{33}$ of the coupling between second-nearest neighbors are dominant in magnitude. Hence, a transfer of the elements $a_{12}, a_{21}$, $a_{23}$, and $a_{32}$ from the $p(2 \times 1)$ phase to the $c(4 \times 2)$ geometry will produce little error. Therefore, we can determine the force constants between any pair of atoms in the whole slab with a maximal error on the order of a typical third-nearest-neighbor coupling. In contrast to that, the uncertainties in the described procedure for Ge correspond to typical second-nearest-neighbor coupling constants since data only from the $p(2 \times 1)$ structure were used for the local-coupling transfer. Furthermore, if we recalculate the dynamical matrix at the $\bar{J}$ point of $Si(001) c(4 \times 2)$, we reproduce exactly the matrix determined by DFPT. Especially flat surface bands are therefore reproduced very accurately by our approach.

The force-constant matrix of the $p(2 \times 2)$ phase of Ge(001) was calculated by transferring the coupling constants of the $p(2 \times 1)$ phase. This yielded a good approximation since the local structural characteristics, namely tilted dimers, are present on both surfaces. Since the force constants of $Si(001) c(4 \times 2)$ are known more precisely, we can go one step further for Si and transfer the coupling constants from $c(4 \times 2)$ to $p(2 \times 2)$. This yields very accurate results since both surfaces exhibit the same structure along a whole dimer row.

In fact, the differences in the atomic positions of equivalent atoms of the HOR in the area marked row 1 in Fig. 9 are negligible. Hence the bonding lengths and bonding directions within a dimer row are identical. This in turn means, according to the general ideas of the LCT approach, that the coupling between atoms within one dimer row can directly be transferred from the $c(4 \times 2)$ to the $p(2 \times 2)$ reconstruction. There is no need to further manipulate the force constants like in the case of Ge.

Differences only arise when we consider the coupling between atoms at different dimer rows. By means of symmetry, however, the remaining unknown terms can be easily determined. Consider, for example, the coupling of atom 11 in Fig. 9 to the closest upper-layer atom of the neighboring dimer row marked atom $a$. The respective force constant corresponds to the coupling of atom 11 to a lower dimer atom in the $c(4 \times 2)$ phase, but to a higher dimer atom in the $p(2 \times 2)$ geometry. Since the symmetry operation $\sigma_{x}$ maps the upper dimer atom 4 of the central dimer row onto $a$ in the $p(2 \times 2)$ reconstruction and 12 onto 11, the force constant between the atoms 12 and 4 can be transferred to the coupling between 11 and $a$.

As in this example, all important coupling parameters can be related to a coupling constant between atoms within row 1. Since these parameters are approximately the same for both structures, the force-constant matrix of the $p(2 \times 2)$ reconstruction is obtained very easily from that of the $c(4 \times 2)$ phase, just by considering the symmetry of the respective structure. Furthermore, variations of the force constants between atoms at greater distances that cannot be obtained in the above-mentioned way have only a very small effect on the dispersion of the surface bands. We estimate an error in all the phonon frequencies of the HOR of Si(001) of no more than 0.6 meV in the Si frequency scale.

![](./images/812765416144240640_10.jpg)

FIG. 10. Phonon dispersion of $c(4 \times 2)$ surfaces of Ge and Si along the $\bar{J} \bar{\Gamma}$ ([110]), $\bar{\Gamma} \bar{J}^{\prime}$ ([1 $\overline{1} 0]$), and $\bar{M} \bar{\Gamma}$ ([100]) directions according to Fig. 1. In the $c(4 \times 2)$ geometry the $\bar{M}$ and $\bar{J}^{\prime}$ points correspond to the $\bar{J}$ point. Only eigenmodes with significant displacements of the first-layer atoms are plotted. At the $\bar{J}$ point we denote in parentheses the polarization (SP, SH) of the first-layer atoms, as well as the $\pm$ classification of the displacement vectors of neighboring dimers along a row as described in the text. Surface bands that are weakly localized because of a strong coupling to subsurface layer vibrations are marked with a superscript $w$. The shaded areas represent the surface projected band structure of the bulk. Since the Si frequencies given in the text have been rescaled, we denote at the right the Ge as well as the Si frequency scale. In the windows sketched at low frequencies we observe six to eight bulk resonant bands with diffuse displacement patterns. There are several bulk resonant bands in the area marked $r$ that correspond to a rocking motion of the dimer atoms.

## IX. COMPARISON OF THE PHONONS OF THE HOR OF Ge(001) AND Si(001)

In Figs. 10 and 11 we display the phonon dispersion of the HOR of Ge(001) and Si(001) along the [110], [1$\overline{1}$0], and [100] directions. For the interpretation of experimental data, it is important to note that scattering experiments may probe the [110] and [1$\overline{1}$0] directions simultaneously, if monatomic

![](./images/812765416144240640_11.jpg)

FIG. 11. Phonon dispersion of the $p(2 \times 2)$ surfaces of Ge and Si along the $\overline{J} \overline{\Gamma}$ ([110]), $\overline{J} \overline{J'}$ ([1$\overline{1}$0]), and $\overline{\Gamma} \overline{M}$ ([100]) directions according to Fig. 1. In the $p(2 \times 2)$ geometry the $\overline{M}$ and $\overline{J'}$ points correspond to the $\overline{\Gamma}$ point.

steps are present on the surfaces at room temperature. The [100] direction, however, is equivalent in all terraces. Be- cause of the large size of the unit cells, there is a wealth of surface features to be observed in every reconstruction.

Along the $\overline{\Gamma} \overline{J}$ direction, all modes can be classified as even or odd modes with respect to the reflection about a plane perpendicular to the rows. The symmetry plane con- tains a surface dimer. In even (odd) modes the dimer atoms vibrate in the sagittal plane (along the row). Unlike in the $p(2 \times 1)$ phase, the motion of the second-layer atoms is not restricted to SP or SH polarization through symmetry. Con- sequently, we observe more complicated displacement pat- terns in the HOR. Furthermore, the displacement patterns of neighboring dimers along a row are correlated because of the $\sigma_{x}$ symmetry. At the high-symmetry points $\overline{\Gamma}$, $\overline{J}$, $\overline{J'}$, and $\overline{M}$ of the Brillouin zones, the reflected displacement vector of one dimer is either in-phase $(+)$ or out-of-phase $(-)$ with the vector of the neighboring dimer.

Because of the lack of symmetry in the $\overline{\Gamma} \overline{M}$ direction, the displacement patterns of the respective eigenvectors are rather complicated. In addition, most features are strongly bulk resonant. Since there is the possibility to classify each mode along $\overline{\Gamma} \overline{J}$ according to SH or SP polarization, we dis cuss the observed surface bands in this direction.

Pronounced surface phonons in the low-energy spectrum have already been presented in Sec. VII. In the following, the frequencies of Si have been rescaled. In the energy range of 12.7-15.2 meV in Ge and Si we find several bulk resonant modes corresponding to a rocking motion of the surface dimers, with an oscillation of the dimer tilt angle. At ener- gies greater than 19 meV, a lot of surface states can be found with an increasing variation of the bond lengths between adjacent atoms.

There are two possible displacement patterns for the SH modes, namely an in-phase and an out-of-phase movement of the two atoms of one dimer. This corresponds to a swing- ing $(s)$ or a twisting motion $(t)$ of the first-layer atoms. We can identify five to eight mostly bulk resonant SH modes between 20 (20.4) meV and 33.5 (35) meV in Ge (Si). Among the SP modes in the medium-energy range of the dispersion, we identify several $d_{r s}$ modes with a displace ment pattern that is somewhat in between a pure rocking motion and a bond stretch vibration of the dimer atoms. The corresponding energy range is 19.5 (20.7)-25.5 (26.2) meV in Ge (Si). At higher frequencies the bond-length oscillation is dominating. Consequently, we find three to four dimer stretch modes $(d s)$ with energies between 27 (28.1) and 35(35) meV in Ge (Si).

Finally, two high-frequency modes can be found in parts of the dispersion of all the considered systems, namely a $t$ mode at 35.8 (36.3) to 36.1 (36.7) meV and a $d s$ band slightly below the $t$ feature. These two bands correspond to the $s b$ mode of the $p(2 \times 1)$ phase. The $t$ mode as an example is related to the folding of the $s b$ mode at the $\overline{J'}$ $(\overline{\Gamma})$ point of the $p(2 \times 1)$ phase onto the $\overline{J}$ point of the $c(4$  $\times 2)(p(2 \times 2))$ geometry.

The latter two modes as well as the low-energetic $t$ band in the acoustic region of the phonon dispersion at the $\overline{J}$ point have been described in great detail in Ref. 8. In the molecular-dynamics simulations performed by Shkrebtii et al. for Si(001), dimer flipping events have been shown to be coupled to large twisting amplitudes of the dimers in the[100] direction. Hence, the low energy of the $t$ mode espe cially in Si(001) indicates that important contributions to dimer flipping processes arise from the thermal excitation of these surface phonons. A corresponding low-energetic fea- ture in the $p(2 \times 1)$ geometry cannot be found since the dis placement of the second-layer atoms is constrained by sym- metry to the direction of the dimer rows. This is not the case for the HOR. There, the subsurface-layer atoms can move in such a way that bond lengths can be kept nearly constant, enabling the remarkably low energy of this nonacoustic fea-ture. Considering the similarities of the Ge(001) and Si(001) surfaces, it seems likely that the calculated frequency of the $t$ band in Ge(001) is too high. As already mentioned, the $t$ band was the only surface band that could not be predicted with an uncertainty of less than 1 meV by our error analysis.In contrast, the $t$ band in $Si(001) c(4 \times 2)$ and $Si(001) p(2$ ×2) is obtained very accurately because the coupling con- stants could have been determined with higher precision by our LCT approach for Si(001).

## X. SUMMARY

In this paper we have presented the results from ab initio calculations for the structural and vibrational properties of Ge(001) and Si(001). The calculations have been performed within density-functional theory and density-functional per- turbation theory using a geometry of periodically repeated thin crystal films and describing the electron-ion interaction by norm-conserving nonlocal pseudopotentials.

Similarly to Si(001), the asymmetric configuration of the $p(2 \times 1)$ reconstruction of $Ge(001)$ turns out to be $0.19 eV$ per dimer lower in energy than the symmetric one. A further reduction of the energy by 0.08 eV is found for the HOR. The bond lengths of the relaxed structures do not differ from the bulk value by more than 4% throughout the crystal films.

The tilt angles are between $17^\circ$ and $18^\circ$ for the three tilted dimer configurations of Ge. Whereas the interatomic distances in the HOR are nearly identical, the bond lengths of the dimers are shortened by $0.05$ Å as compared to the $p(2$ $\times 1)$ geometry. The relaxation parameters compare well with other theoretical studies and experimental data.

We have calculated the phonon dispersion of Ge(001) $p(2\times 1)$ and compared our results with Si(001). The most significant surface bands are present in both Ge and Si. Whereas the dispersion of bulk Ge and bulk Si are nearly the same up to a scaling factor, characteristic shifts occur for the surface modes, reflecting chemical trends in reconstruction behavior. Ge avoids double bonding to a larger extent than Si. Hence the bond lengths in Si are shorter than in Ge in the surface region, distances being already rescaled to the respective lattice constants. Smaller bond lengths yield stronger force constants in Si. Consequently, all the modes except for the three acoustic surface bands RW, $A_1$, and $A_2$ and the rocking mode $r$ are more energetic. This trend could be generalized by including the case of C(001), which reconstructs in the symmetric configuration. Diamond exhibits a strong tendency of $\pi$-bond formation, which results in even stronger bonds between nearest neighbors. This in turn leads to particularly high frequencies of surface vibrations which involve bond-length oscillations.

The magnitude of the coupling constants decreases rapidly with increasing interatomic distances. Hence the interaction between nearest neighbors plays the most important role not only for structural and electronic but also for the vibrational properties. This fact led us to the development of the LCT approach, which involves the following general features.

(i) Applicability: We can compute the phonon dispersion of large-size superstructures in the whole SBZ, provided the force-constant matrix of a similar system (basic system) is known.

(ii) Common subunits: Properties of subunits which are characteristic for the two systems are extracted by a detailed analysis of the force-constant matrix of the basic reconstruction. The coupling constants $K_{ij}(\mathbf{R},\mathbf{R}')$ are then transferred to the supercell according to equivalent local bonding environments such as the tilted dimers or equivalent dimer rows (by symmetry adaptation, if necessary). Furthermore, the coupling constants are adapted to the occurrence of small changes in the bond lengths and the symmetry of the supercell under investigation.

(iii) Advantages of LCT: The major advantage of this model is the possibility to describe large-size supercells inaccessible to computationally demanding theories such as DFPT. A detailed error analysis is obtained through a thorough inspection of the basic force-constant matrix.

The coupling constants of the HOR of Ge(001) have been calculated by transferring the coupling constants of the $p(2$ $\times 1)$ phase. For the HOR of Si(001), some of the force constants had to be transferred from the $p(2\times 1)$ phase, while the most important coupling parameters were adapted from the dynamical matrix computed within DFPT for the $c(4$ $\times 2)$ reconstruction at the $\bar{J}$ point. The transfer from the $c(4\times 2)$ to the $p(2\times 2)$ phase yields very accurate results since the two surfaces of the HOR exhibit the same structure along a whole dimer row.

Due to the large size of the unit cells, we observe a wealth of surface states including rocking, twisting, swinging, and stretching motions of surface atoms in each considered reconstruction. The phonon-dispersion curves of the HOR of Ge(001) and Si(001) are similar, the bands of Si being in general more energetic, just as in the $p(2\times 1)$ reconstruction.

The phonon dispersion of Ge(001) has been compared to the measured data from inelastic He-atom scattering. Whereas poor agreement is observed for the $p(2\times 1)$ structure, the calculated surface bands of the HOR reproduce very well the experimentally resolved surface features as well as the scattering intensities. Analogous to the results from recent molecular-dynamics studies and photoemission experiments for Si(001), we conclude that the HOR are present at room temperature also in Ge(001), indicating a short-range correlation between adjacent dimers. We get contributions to the scattering intensities from both reconstructions. Consequently, thermally induced correlated flipping processes do not change the antiferromagnetic ordering of the tilted dimers along a row at a local scale. This correlation also manifests itself in the energy difference between the HOR and the $p(2\times 1)$ phase of 0.08 eV per dimer.

So far we have investigated only nonpolar covalently bonded systems with the LCT approach. An extension to polar materials could be undertaken by separation of the coupling constants into short-range and long-range contributions. The latter arise from the effective charges of the atoms, which could be transferred from the basic structure to equivalent atoms of the supercell.

## ACKNOWLEDGMENTS

We are indebted to G. Brusdeylins and J. P. Toennies for their He-atom scattering data. We would like to thank S. Baroni and P. Giannozzi for providing numerical support and D. Strauch, A. Mayer, and B. Doak for helpful discussions. This work has been performed on the CRAY-YMP supercomputers of the HLRZ of the KFA in Jülich under Contract No. K2710000 and of the Leibniz Rechenzentrum in Munich.

$^{1}$J. A. Kubby, J. E. Griffith, R. S. Becker, and J. S. Vickers, Phys. Rev. B $\textbf{36}$, 6079 (1987).

$^{2}$R. J. Culbertson, Y. Kuk, and L. C. Feldman, Surf. Sci. $\textbf{167}$, 127 (1986).

$^{3}$S. D. Kevan, Phys. Rev. B $\textbf{32}$, 2344 (1985).

$^{4}$W. R. Lambert, P. L. Trevor, M. J. Cardillo, A. Sakai, and D. R. Hamann, Phys. Rev. B $\textbf{35}$, 8055 (1987).

$^{5}$S. Ferrer, X. Torrelles, V. H. Etgens, H. A. van der Vegt, and P. Fajardo, Phys. Rev. Lett. $\textbf{75}$, 1771 (1995).

$^{6}$M. Needels, M. C. Payne, and J. D. Joannopoulos, Phys. Rev. B $\textbf{38}$, 5543 (1988).

$^{7}$J. Fritsch and U. Schröder, Phys. Rep. (to be published).

$^{8}$J. Fritsch and P. Pavone, Surf. Sci. **344**, 159 (1995).

$^{9}$P. Krüger and J. Pollmann, Phys. Rev. B **47**, 1898 (1993).

$^{10}$A. I. Shkrebtii, R. Di Felice, C. M. Bertoni, and R. Del Sole, Phys. Rev. B **51**, 11 201 (1995).

$^{11}$J. E. Northrup, Phys. Rev. B **47**, 10 032 (1993).

$^{12}$Z. Zhu, N. Shima, and M. Tsukada, Phys. Rev. B **40**, 11 868 (1989).

$^{13}$R. A. Wolkow, Phys. Rev. Lett. **68**, 2636 (1992).

$^{14}$W. Stigler, P. Pavone, U. Schröder, J. Fritsch, G. Brusdeylins, T. Wach, and J. P. Toennies, Phys. Rev. Lett. **79**, 1090 (1997).

$^{15}$D. R. Alfonso, D. A. Drabold, and S. E. Ulloa, Phys. Rev. B **51**, 1989 (1995).

$^{16}$P. Hohenberg and W. Kohn, Phys. Rev. **136**, B864 (1964).

$^{17}$W. Kohn and L. J. Sham, Phys. Rev. **140**, A1133 (1965).

$^{18}$J. P. Perdew and A. Zunger, Phys. Rev. B **23**, 5048 (1981).

$^{19}$P. Giannozzi, S. de Gironcoli, P. Pavone, and S. Baroni, Phys. Rev. B **43**, 7231 (1991).

$^{20}$N. Troullier and J. L. Martins, Phys. Rev. B **43**, 1993 (1991).

$^{21}$K. Karch, Ph.D. thesis, University of Regensburg, Germany (unpublished).

$^{22}$S. Froyen, Phys. Rev. B **39**, 3168 (1989).

$^{23}$S. Baroni, P. Giannozzi, and A. Testa, Phys. Rev. Lett. **58**, 1861 (1987).

$^{24}$R. Rossmann, H. L. Meyerheim, V. Jahns, J. Wever, W. Moritz, D. Wolf, D. Dornisch, and H. Schulz, Surf. Sci. **279**, 199 (1992).

$^{25}$P. Krüger and J. Pollmann, Phys. Rev. Lett. **74**, 1155 (1995).

$^{26}$M. Needels, M. C. Payne, and J. D. Joannopoulos, Phys. Rev. Lett. **58**, 1765 (1987).

$^{27}$P. Krüger, A. Mazur, J. Pollmann, and G. Wolfgarten, Phys. Rev. Lett. **57**, 1468 (1986).

$^{28}$L. Kipp, R. Manzke, and M. Skibowski, Surf. Sci. **269/270**, 854 (1992).

$^{29}$E. Landemark, R. I. G. Uhrberg, P. Krüger, and J. Pollmann, Surf. Sci. Lett. **236**, L359 (1990).

$^{30}$An $(M,N)$ mesh defines a set of points $\mathbf{q}_{m,n}=(m/M)\mathbf{G}_{1}+(n/N)\mathbf{G}_{2}$ with $0\leqslant m\leqslant M-1$ and $0\leqslant n\leqslant N-1$. The vectors $\mathbf{G}_{1}$ and $\mathbf{G}_{2}$ ($|\mathbf{G}_{1}|\geqslant|\mathbf{G}_{2}|$) are the primitive translations of the SBZ.

$^{31}$P. C. Weakliem and E. A. Carter, J. Chem. Phys. **96**, 3240 (1992).

$^{32}$*Semiconductors: Physics of Group IV and III-V Compounds*, edited by O. Madelung, Landolt-Börnstein, New Series, Group III, Vol. 17a (Springer-Verlag, Berlin, 1982); *Semiconductors: Intrinsic Properties of Group IV Elements and III-V, II-VI, and I-VII Compounds*, edited by O. Madelung, Landolt-Börnstein, New Series, Group III, Vol. 22a (Springer-Verlag, Berlin 1987).

$^{33}$W. Kress and F. W. de Wette, *Surface Phonons* (Springer-Verlag, Berlin, 1991).

$^{34}$J. Fritsch, P. Pavone, and U. Schröder, Phys. Rev. Lett. **71**, 4194 (1993).

$^{35}$R. Honke, P. Pavone, and U. Schröder (unpublished).

$^{36}$P. Pavone, K. Karch, O. Schütt, W. Windl, D. Strauch, P. Giannozzi, and S. Baroni, Phys. Rev. B **48**, 3156 (1993).