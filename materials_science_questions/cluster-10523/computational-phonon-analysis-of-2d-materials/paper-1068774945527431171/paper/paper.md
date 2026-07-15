# Chiral Phonons in 2D Halide Perovskites

Mike Pols, $^{1, *}$ Geert Brocks, $^{1,2}$ Sofía Calero, $^{1}$ and Shuxia Tao $^{1, \dagger}$

$^{1}$ Materials Simulation & Modelling, Department of Applied Physics and Science Education,
Eindhoven University of Technology, 5600 MB, Eindhoven, The Netherlands

$^{2}$ Computational Chemical Physics, Faculty of Science and
Technology and MESA+ Institute for Nanotechnology,
University of Twente, 7500 AE, Enschede, The Netherlands

(Dated: November 27, 2024)


### Abstract

Phonons in chiral crystal structures can acquire a circular polarization, becoming chiral themselves. Chiral phonons carry a spin angular momentum, which is observable in heat currents, and, via coupling to the electron spin, in spin currents. Two-dimensional (2D) hybrid halide perovskites comprise a class of direct band gap semiconductors that can easily be forced into a chiral structure by incorporating chiral organic cations into the crystal. The degree of chirality can be tuned by modifying the organic cations. We reveal chiral phonons in such 2D perovskites, using on-the-fly machine-learning force fields based on density functional theory calculations. We find that particularly the low energy phonons, originating from the inorganic framework of the perovskites, are chiral. In the presence of a temperature gradient, a substantial angular momentum density can be induced, which is measurable in experiment.

Keywords: metal halide perovskites, density functional theory, machine-learning force fields, chirality, phonons, angular momentum, chiral phonons

## I. INTRODUCTION

Chiral molecules or crystals occur in two structures that are mirror images of one another. The two structures cannot be superimposed on each other through any rotation or translation, or otherwise be simply interconverted. Chiral materials, such as $\alpha$-SiO$_2$ ($\alpha$-quartz), display chiral optical properties, like optical rotation and circular dichroism (CD) [1, 2]. More recently, chirality induced properties of charge carriers, i.e. electrons and holes, have been highlighted in materials, for instance in chirality-induced spin selectivity (CISS) [3], fermions in graphene [4], Weyl semimetals [5], and topological insulators [6]. Chirality also emerges in bosons, as confirmed by the discovery and characterization of chiral phonons in two-dimensional (2D) transition metal dichalcogenides (TMDs) [7, 8], Moiré superlattices [9, 10] and three-dimensional (3D) materials like $\alpha$-HgS [11], $\alpha$-SiO$_2$ [12], and Te [13].

Chiral phonons have a nonzero angular momentum [7]. At thermal equilibrium the phonon occupancies are such that the total angular momentum averages to zero. However, in heat transport experiments out-of-equilibrium distributions of chiral phonons are created, which can carry an observable amount of angular momentum [14], analogous to the Edelstein effect for

* m.c.w.m.pols@tue.nl
† s.x.tao@tue.nl

electrical transport [15–17]. A nonzero phonon angular momentum can be measured as the crystal displays a recoil rotational motion, the Einstein-de Haas effect [18–20], or via the magnetic moment associated with the angular momentum [21]. Alternatively, by coupling the phonon angular momentum and electron spin [22], spin currents can be generated and detected [23], as in the spin Seebeck effect [24, 25].

Chiral effects in crystals are dictated by the crystal structure, and with a fixed structure such effects are typically not easily modified or manipulated. Hybrid organic-inorganic 2D halide perovskites form a class of materials whose properties can be tuned by substituting different ions. Chiral organic cations can be incorporated into the crystal structure, transferring structural chirality to the metal halide framework [26–28]. The nature and extent of this chirality can be tuned by modifying the cation [29, 30]. Besides the typical chiroptical properties, i.e. optical rotation and CD [31, 32], chiral 2D halide perovskites can also emit circularly polarized light [33, 34]. Moreover, in electron transport they give rise to spin-polarized currents without needing magnetism (CISS) [35, 36], and in phonon transport it is suggested they give rise to a spin Seebeck effect [25].

Halide perovskites present the potential to link chiral optical, electronic, and thermal properties, yet our fundamental understanding of them remains somewhat fragmentary. Phonons seem to be involved in many of these properties, but first-principles calculations of phonons in these compounds are challenging, because of the considerable number of atoms per unit cell. Recently, we have studied the temperature dependence of structural chirality in chiral 2D halide perovskites, through molecular dynamics simulations with machine-learning force fields (MLFFs) [28]. These force fields combine a low computational cost with the precision of first-principles calculations.

In the current work we apply these MLFFs to study the chiral properties of phonons in the 2D halide perovskite $MBA_2PbI_4$, and contrast it with similar achiral 2D halide perovskites. In particular, we calculate the spin angular momentum of the phonons as a function of their propagation direction. Mimicking heat transport experiments, we calculate the angular momentum generated by applying a temperature gradient. We find that around room temperature, only the phonons propagating in the lead iodide framework participate. An appreciable amount of angular momentum is generated if the temperature gradient is along the lead iodide planes, but not of it is perpendicular to those planes. In addition, there is considerable anisotropy within the planes.

## II. COMPUTATIONAL METHODS

To accurately model the vibrational properties of 2D halide perovskites, an accurate representation of the potential energy surface (PES) of the materials is required. Here we employ earlier trained machine-learning force fields (MLFFs) [28] to describe the PES of a range of 2D halide perovskites at the accuracy of density functional theory (DFT) calculations. The MLFFs were trained against energies, forces and stresses from DFT calculations with the SCAN exchange-correlation functional [37] in VASP [38-40]. During training the structures were sampled using an on-the-fly learning scheme from first-principles molecular dynamics simulations as described in Refs 41, 42. The full details of the training procedure, the training sets, and the validation of the MLFFs are shown in Supporting Note 1. The phonon modes were computed at the harmonic level using the MLFFs through the supercell approach as implemented in phonopy [43, 44]. The details of the phonon calculations and their sensitivity to the DFT computational settings can be found in Supporting Note 2.

## III. PHONON DISPERSION AND DENSITY OF STATES

To assess the character of the lattice vibrations in chiral $(S\text{-MBA})_2\text{PbI}_4$, we show its phonon density of states (DOS) in Figure 1. Analogous to three-dimensional (3D) perovskites [45, 46], we can identify three energy regions (Figure 1a); (i) a low energy region, 0 - 25 meV, (ii) a medium energy region, 25 - 210 meV, and (iii) a high energy region, 375 - 425 meV. Considering the contributions of the different atoms in the crystal lattice, the energy regions can be associated with the motion of different parts of the crystal lattice.

The low energy region (i), shown in Figure 1b, is primarily the result of vibrations in the inorganic framework $([\text{PbI}_4]^{2-})$, in particular in the lower half of that energy region. Some motion of the organic cations $(\text{MBA}^+)$ is mixed in, especially in the upper half of that energy region, due to coupling between the inorganic framework and the organic molecules [47]. The corresponding vibrations involve motions of the cations as a whole. Indeed, comparing the phonon DOS of different 2D perovskites (Supporting Note 3), we find that the contribution of the organic cations at low energies scales with their size and mass.

In contrast, the two higher energy regions are the result of vibrations within the organic cations. The medium energy region (ii) is associated with torsional or bending motion of molecular

fragments or, for example, $C-C$ and $C-N$ stretch vibrations. The high energy modes (iii) correspond to the stretch vibrations of $C-H$ and $N-H$ bonds in the organic cations.

![](./images/1068774945527431171_1.jpg)

FIG. 1. (a) Phonon density of states (DOS) of $(S-MBA)_2PbI_4$ with the (i) low energy, (ii) medium energy and (iii) high energy regions in red, yellow, and green colors, respectively. (b) A zoom-in of the low-energy region (0 - 25 meV). Gaussian broadenings of 2.0 meV and 0.1 meV were used in the full and detailed DOS, respectively.

In heat transport and electron-phonon coupling the low energy phonons are particularly relevant. The phonon dispersions in the low energy region of $(S-MBA)_2PbI_4$ (0 - 5 meV) are shown in Figure 2. We specifically focus on the dispersions in the in-plane $\Gamma-X$ and $\Gamma-Y$ as well as out-of-plane $\Gamma-Z$ directions of the inorganic layers within the 2D perovskite (Figure 2a-d). The absence of any imaginary modes in the phonon dispersion indicates that the $P2_12_12_1$ crystal structure of $(S-MBA)_2PbI_4$ observed in experiments [26], is a stable energy minimum.

Focusing on the acoustic phonons (Figure 2e-f), we find that in the in-plane directions ($\Gamma-X$ and $\Gamma-Y$), the three acoustic phonon branches are non-degenerate and have different group velocities. In contrast, we observe a near degeneracy between the two TA modes of the acoustic phonons in the out-of-plane direction ($\Gamma-Z$). Comparing the average group velocities of the acoustic phonons in the three directions ($\bar{v}^{\Gamma-X}=1861.3\,\text{m}\,\text{s}^{-1}$, $\bar{v}^{\Gamma-Y}=1796.3\,\text{m}\,\text{s}^{-1}$, and $\bar{v}^{\Gamma-Z}=1669.2\,\text{m}\,\text{s}^{-1}$), we find that they are actually quite similar, which indicates a surprisingly small anisotropy. We find a similarly low anisotropy in the phonon group velocities of $BA_2PbI_4$ and $PEA_2PbI_4$ in Supporting Note 4, which is in agreement with previous findings [48].

![](./images/1068774945527431171_2.jpg)

FIG. 2. (a) Unit cell of $(S\text{-MBA})_2\text{PbI}_4$ with $P2_12_12_1$ space group. Hydrogen (H), carbon (C), nitrogen (N), iodine (I), and lead (Pb) are represented by white, gray, blue, purple, darkgray spheres, respectively. Brillouin zone of $(S\text{-MBA})_2\text{PbI}_4$, with paths along the (b) $b_1$-axis ($\Gamma$-$X$), (c) $b_2$-axis ($\Gamma$-$Y$), and (d) $b_3$-axis ($\Gamma$-$Z$), and special points X = $(\frac{1}{2}, 0, 0)$, Y = $(0, \frac{1}{2}, 0)$, and Z = $(0, 0, \frac{1}{2})$, with -X = $(-\frac{1}{2}, 0, 0)$ etc. (e) Phonon dispersion and (f) density of states of low energy region (0 - 5 meV). The DOS is broadened using a Gaussian smearing of 0.1 meV.

## IV. CHIRAL PHONON MODES

A phonon eigenmode with wave vector $\mathbf{q}$ and mode index $\sigma$ is described by a polarization vector $\mathbf{e}_{i,\mathbf{q},\sigma}$, with $i$ labeling the atoms in the unit cell. The polarization vectors are normalized over all atoms of the unit cell, so that $\sum_{i=1} \mathbf{e}_{i,\mathbf{q},\sigma}^{\dagger} \mathbf{e}_{i,\mathbf{q},\sigma} = 1$. The circular polarization of the phonon modes can be quantified by calculation the phonon spin as

$$
s_{\mathbf{q},\sigma}^{\alpha} = \sum_{i=1}^{N} \mathbf{e}_{i,\mathbf{q},\sigma}^{\dagger} S^{\alpha} \mathbf{e}_{i,\mathbf{q},\sigma}, \tag{1}
$$

where $S^{\alpha}$ ($\alpha = x, y, z$) are the spin-1 matrices on a Cartesian basis. The magnitude and sign of the circular polarization of an eigenmode determine the chirality or handedness of the phonon, with $0 < s_{\mathbf{q},\sigma}^{\alpha} \leq +1$ and $-1 \leq s_{\mathbf{q},\sigma}^{\alpha} < 0$ indicating a right- and left-handed phonon mode, respectively. Achiral phonon modes, with a linear polarization, such as longitudinal modes, have no circular polarization ($s_{\mathbf{q},\sigma}^{\alpha} = 0$).

The circular polarization can, in principle, be measured with respect to any arbitrary axis $\alpha$. However, some components will be zero for symmetry reasons. For instance, in the crystal

structure of $(S\text{-MBA})_2\text{PbI}_4$, space group $P2_12_12_1$, for phonons propagating in a direction along one of the crystal axes $\mathbf{q}=(q_x,0,0)$, $(0,q_y,0)$ or $(0,0,q_z)$, only the corresponding $x$-, $y$-, or $z$-component of $s_{\mathbf{q},\sigma}^{\alpha}$ is nonzero. In the current work we focus on those phonons propagating either in $x$-, $y$-, or $z$-directions. To calculate $s_{\mathbf{q},\sigma}^{\alpha}$ we follow the procedures outlined in earlier work [7, 13]. Additional details are provided in Supporting Note 5.

The dispersion of phonons in the low energy region of $(S\text{-MBA})_2\text{PbI}_4$, propagating along the $x$-, $y$-, and $z$-axis, as well as their respective chirality, is shown in Figure 3. Phonons propagating in the positive and negative direction along the different axes are shown in separate panels. Figure 3 demonstrates that in all directions chiral phonons can be found. One observes that phonons propagating in opposite directions, for instance, $\Gamma\!-\!X$ and $X\!-\!\Gamma$, see (Figure 3a), have an opposite circular polarization, i.e. $s_{\mathbf{q},\sigma}^{x}=-s_{-\mathbf{q},\sigma}^{x}$. This is a consequence of time-reversal symmetry [14], and is similar to the relation between spin-orbit split bands in an electronic band structure. Indeed, a similar coupling between the phonon propagation direction and its polarization has been observed in both Te and $\alpha\text{-SiO}_2$ [13].

![](./images/1068774945527431171_3.jpg)

FIG. 3. Dispersion of phonons in $(S\text{-MBA})_2\text{PbI}_4$ propagating along the (a) $x$-axis ($\text{-}X\!-\!\Gamma\!-\!X$), (b) $y$-axis ($\text{-}Y\!-\!\Gamma\!-\!Y$), and (c) $z$-axis ($\text{-}Z\!-\!\Gamma\!-\!Z$). Phonon branches are color-coded with the circular polarization of the phonon modes. Red, blue, and gray are used to represent right-handed ($s_{\mathbf{q},\sigma}^{\alpha}>0$), left-handed ($s_{\mathbf{q},\sigma}^{\alpha}<0$), and non-polarized ($s_{\mathbf{q},\sigma}^{\alpha}=0$) phonon modes.

By examining the chirality of the phonons across the whole spectrum, we find that the chiral phonon modes are primarily found in the low energy region of the phonon spectrum of $(S\text{-MBA})_2\text{PbI}_4$. In this region (0 - 25 meV), phonons can possess a substantial chirality ($|s_{\mathbf{q},\sigma}^{\alpha}|\geq\frac{1}{4}$), whereas that of higher energy phonons ($>25$ meV) is negligible, as shown in Figure S8 in

Supporting Note 5. Generally speaking, the phonon chirality appears to increase for phonons with wave vectors approaching the zone boundaries. In the $x$-direction (Figure 3a), the two lowest acoustic branches show appreciable chirality, as do several of the low energy optical branches. Chirality in the $y$-direction is predominantly observed in the optical modes near the zone boundary (Figure 3b). The two lowest acoustic modes in the $z$-direction seem to show appreciable chirality (Figure 3c), but this is slightly misleading, as they are almost degenerate, and their chirality sums up to zero.

As mentioned earlier, the low energy phonons are those phonons which heavily involve motions of the atoms within the inorganic framework. In previous work, we established that this inorganic framework has chiral structural distortions, resulting from the transfer of chirality from the organic cations to the inorganic framework [28]. In contrast, achiral 2D perovskites were found to lack such chiral distortions and chiral phonon modes. Indeed, for achiral 2D perovskites, i.e. (rac-MBA)$_2$PbI$_4$, BA$_2$PbI$_4$, or PEA$_2$PbI$_4$, we do not observe any circular polarization of the phonon modes, as shown in Supporting Note 5.

To support the evidence of the relation between structural chirality and phonon chirality, we have also compared the phonons in the two enantiomers of MBA$_2$PbI$_4$ in Supporting Note 6. Whereas the phonon dispersions are identical for the two enantiomers, we observe that phonons propagating in the same direction in each enantiomer have opposite polarization; for each phonon branch, a right-handed phonon in (S-MBA)$_2$PbI$_4$ becomes a left-handed phonon in (R-MBA)$_2$PbI$_4$, and vice versa. We propose that the chiral distortions within the inorganic framework [28], which can readily be tuned through compositional engineering [27, 49], play a crucial role in the emergence of circularly polarized phonons in 2D perovskites.

Figure 4 shows an example of the atomic motions of chiral phonons in (S-MBA)$_2$PbI$_4$. It illustrates the atomic motion of the lowest four phonon modes at the point $O=(\frac{2}{5},0,0)$ along the in-plane $\Gamma-X$ path. Modes 1, 2, and 4 are chiral, whereas mode 3 is achiral. The chiral modes exhibit an elliptical motion in the $yz$-plane, perpendicular to their propagation direction ($x$-direction). The achiral mode exhibits a linear oscillatory motion within this plane. Comparing the two lowest phonon modes, 1 and 2, we see that the semi-major axis of the elliptical motion for these two modes has a different orientation; mode 1 has it oriented along the $z$-axis, whereas it is parallel to the $y$-axis for mode 2. A similar analysis can be found in Supporting Note 6 for the phonons propagating along the $\Gamma-Y$ and $\Gamma-Z$ paths.

8

![](./images/1068774945527431171_4.jpg)

FIG. 4. (a) Phonon dispersion and (b) atomic motion in the selected phonon modes at $O = \left( \frac{2}{5}, 0, 0 \right)$ in (S-MBA)$_2$PbI$_4$. All mode numbers are colored to indicate the circular polarization, with red (right-handed), black (non-polarized), and blue (left-handed). The atoms follow the trajectories from red to yellow as time progresses.

### V. PHONON ANGULAR MOMENTUM

Having predicted the presence of chiral phonons in 2D halide perovskites, one needs a way to establish them experimentally. Figure 3 demonstrates that in every phonon branch $\sigma$ phonons moving in opposite directions, i.e. $\pm \mathbf{q}$, exhibit opposite chirality, such that $s_{\mathbf{q},\sigma}^{\alpha} = -s_{-\mathbf{q},\sigma}^{\alpha}$. In thermal equilibrium, their Bose-Einstein occupation numbers $f_0 \left( \omega_{\mathbf{q},\sigma} \right)$ are equal, since for every mode $\omega_{\mathbf{q},\sigma} = \omega_{-\mathbf{q},\sigma}$, which means their total chirality sums to zero.

However, the phonon distribution can be driven out-of-equilibrium by applying a temperature gradient along arbitrary directions, which generates a heat flux. This breaks the symmetry between occupations of the right- and left-moving modes, i.e. $f \left( \omega_{\mathbf{q},\sigma} \right) \neq f \left( \omega_{-\mathbf{q},\sigma} \right)$, and generates a phonon distribution with a nonzero net chirality. The effect is analogous to the Edelstein effect in electronic transport. As established earlier, phonon chirality is defined by a nonzero phonon spin (Eqn. 1). As the latter is a form of angular momentum, it is possible to measure it, either directly, using the Einstein-de Haas effect [50], or indirectly, via a coupling between phonons and magnetic moments, and the inverse spin-Hall effect [23].

To calculate the angular momentum, we follow the procedure as formulated by Hamada *et al.* [14]. Heat transport is described with the Boltzmann transport equation, where one assumes the temperature gradient to be small enough to permit linearization of the equation, and one considers a uniform relaxation time. Under these conditions, the components of the angular

momentum are given by

$$
J^{\mathrm{ph}, \alpha}=-\frac{\hbar \tau}{V} \sum_{\mathbf{q}, \sigma ; \beta=x, y, z} s_{\mathbf{q}, \sigma}^{\alpha} v_{\mathbf{q}, \sigma}^{\beta} \frac{\partial f_{0}\left(\omega_{\mathbf{q}, \sigma}\right)}{\partial T} \frac{\partial T}{\partial x^{\beta}} \equiv \sum_{\beta} \alpha^{\alpha \beta} \frac{\partial T}{\partial x^{\beta}},
\tag{2}
$$

where $J^{\mathrm{ph}, \alpha}$ $(\alpha=x, y, z)$ are the components of the total phonon angular momentum per unit volume, $\hbar$ is the reduced Planck constant, $\tau$ is the phonon relaxation time, $V$ the unit cell volume, $s_{\mathbf{q}, \sigma}^{\alpha}$ the phonon spin, $v_{\mathbf{q}, \sigma}^{\beta}$ $(\beta=x, y, z)$ the components of the phonon group velocity, and $f_{0}$ the Bose-Einstein distribution. The response tensor of the material is then defined by $\alpha^{\alpha \beta}$. It is a second rank tensor obeying the symmetry rules of the crystal structure, which in case of space group $P 2_{1} 2_{1} 2_{1}$ (point group $D_{2}$) gives off-diagonal elements of zero, $\alpha^{\alpha \beta}=0$ $(\alpha \neq \beta)$, and unequal diagonal elements, $\alpha^{x x} \neq \alpha^{y y} \neq \alpha^{z z}$ [14]. A more detailed discussion on the calculation of this quantity can be found in Supporting Note 7, as well as details on the convergence of the results.

Based upon the calculated spectrum of phonon modes in $(S\text{-MBA})_{2}\text{Pbl}_{4}$ and their chirality, we have calculated the induced angular momentum density according to Eqn. 2 as a function of temperature. The results are shown in Figure 5. Because of the symmetry of the structure, the induced angular momentum is parallel to the applied temperature gradient. In all directions, we observe that a gradient in the temperature results in the generation of a nonzero angular momentum. At low temperatures $(<150\,\text{K})$, the angular momentum shows a strong dependency on temperature, but for higher temperatures $(>150\,\text{K})$, it becomes independent of the temperature. This merely confirms that the low energy phonons in $(S\text{-MBA})_{2}\text{Pbl}_{4}$ cause the chiral effect, as for $k_{\mathrm{B}} T \gg \hbar \omega_{\mathbf{q}, \sigma}$, $f_{0}\left(\omega_{\mathbf{q}, \sigma}\right) \propto T$, so $J^{\mathrm{ph}, \alpha}$ should become independent of the temperature.

At $300\,\text{K}$, the induced angular momentum is largest for a temperature gradient applied in the $x$-direction $(\alpha^{x x}=+9.6 \times 10^{-8} \times[\tau /(1\,\text{s})]\,\text{J}\,\text{s}\,\text{m}^{-2}\text{K}^{-1})$, with gradients applied in the $y$- and $z$-directions showing markedly lower responses and with an opposite sign $(\alpha^{y y}=-2.7 \times 10^{-8} \times[\tau /(1\,\text{s})]\,\text{J}\,\text{s}\,\text{m}^{-2}\text{K}^{-1}$ and $\alpha^{z z}=-1.1 \times 10^{-8} \times[\tau /(1\,\text{s})]\,\text{J}\,\text{s}\,\text{m}^{-2}\text{K}^{-1})$. In any case, the values are large enough to generate an angular momentum that can be observed in experiments [14], either converted to spin signals [23] or in a torque measurement [50].

Near the Brillouin zone (BZ) center at $\Gamma$ the three lowest energy branches are formed by the acoustic modes, but near the BZ edges these hybridize with the lowest energy optical modes, so the distinction between acoustic and optical modes is blurred there, see Figure 4. Nevertheless, it is instructive to decompose the response tensors into contributions from the three lowest energy phonons and the rest. We find that above $100\,\text{K}$ the contributions to $\alpha^{x x}$ almost completely

![](./images/1068774945527431171_5.jpg)

FIG. 5. (a) Illustration of the induced angular momentum from phonons $(J^{\text{ph}})$ in $(S\text{-MBA})_2\text{PbI}_4$ for a temperature gradient $(\Delta T)$ in the $x$-direction. The temperature dependence of the (b) $\alpha^{xx}$, (c) $\alpha^{yy}$, and (d) $\alpha^{zz}$ components of the response tensor given by solid lines. The contributions from the three lowest energy phonons and the other phonons are given by dashed and dotted lines, respectively.

come from the three lowest energy phonons (Figure 5b), with the higher energy optical phonons having essentially no effect. In contrast, for $\alpha^{yy}$ and $\alpha^{zz}$ (Figure 5c-d), the three lowest energy phonons and the optical phonons have similar contributions. These have opposite signs however, which explains the smaller values of $\alpha^{yy}$ and $\alpha^{zz}$ as compared to $\alpha^{xx}$, since they cancel out.

According to Eqn. 2 a phonon mode should have both a high chirality and high velocity to generate a substantial angular momentum. Therefore, it is not so surprising that the chiral acoustic modes provide a dominant contribution. As can be seen in Figure 3, these can be found along the $\Gamma-X$ path, but not along the $\Gamma-Y$ path, whereas along the $\Gamma-Z$ path, modes of opposite chirality are almost degenerate, canceling their contributions.

## VI. CONCLUSION

In summary, we investigate the vibrational properties of chiral 2D hybrid halide perovskites, using $\text{MBA}_2\text{PbI}_4$ as an example. Concerning chirality, the low energy vibrations (0 - 25 meV) are most important, which are vibrations of the inorganic framework, whereas the intermediate energy region (25 - 210 meV) and high energy region (375 - 425 meV), associated with vibrations within the organic cations, are much less important. Despite the very anisotropic structure of these 2D perovskites, with 2D metal halide layers alternating with layers of organic cations, the phonon group velocity is relatively isotropic.

Analyzing the chiral character of the phonons, we find that particularly the low energy phonons acquire chirality. The handedness of the chiral phonons couples with both the propagation

direction of the phonon and structural chirality of the crystal, in the sense that if either of the latter two is reversed, the handedness of the phonons is also reversed. As a consequence of these chiral phonons, chiral 2D perovskites can generate an observable angular momentum from a temperature gradient.

Having established the presence of circularly polarized phonons in 2D halide perovskites, we suggest that halide perovskites are an interesting class of materials to further investigate chiral phonons. The flexibility of the crystal composition allows for changes in the perovskite structure, through interchange of metal ions, halide ions, or the organic cations. In the first place, this allows us to more deeply understand the structure-property relationship between structural chirality and the circular polarization of phonons. Moreover, it allows for a tuning of the chiral phonons to envisioned applications.

## SUPPORTING INFORMATION

Supporting information will be made available on publication.

## ACKNOWLEDGMENTS

S.T. acknowledges funding from Vidi (project no. VI.Vidi.213.091) from the Dutch Research Council (NWO).

[1] X. Wang and Y. Yan, Phys. Rev. B **107**, 045201 (2023).

[2] C. Multunas, A. Grieder, J. Xu, Y. Ping, and R. Sundararaman, Phys. Rev. Mater. **7**, 123801 (2023).

[3] K. Ray, S. P. Ananthavel, D. H. Waldeck, and R. Naaman, Science **283**, 814 (1999).

[4] M. I. Katsnelson, K. S. Novoselov, and A. K. Geim, Nat. Phys. **2**, 620 (2006).

[5] S.-Y. Xu, I. Belopolski, N. Alidoust, M. Neupane, G. Bian, C. Zhang, R. Sankar, G. Chang, Z. Yuan, C.-C. Lee, S.-M. Huang, H. Zheng, J. Ma, D. S. Sanchez, B. Wang, A. Bansil, F. Chou, P. P. Shibayev, H. Lin, S. Jia, and M. Z. Hasan, Science **349**, 613 (2015).

[6] D. Hsieh, Y. Xia, D. Qian, L. Wray, J. H. Dil, F. Meier, J. Osterwalder, L. Patthey, J. G. Checkelsky, N. P. Ong, A. V. Fedorov, H. Lin, A. Bansil, D. Grauer, Y. S. Hor, R. J. Cava, and M. Z. Hasan, Nature **460**, 1101 (2009).

[7] L. Zhang and Q. Niu, Phys. Rev. Lett. **115**, 115502 (2015).

[8] H. Zhu, J. Yi, M.-Y. Li, J. Xiao, L. Zhang, C.-W. Yang, R. A. Kaindl, L.-J. Li, Y. Wang, and X. Zhang, Science **359**, 579 (2018).

[9] N. Suri, C. Wang, Y. Zhang, and D. Xiao, Nano Lett. **21**, 10026 (2021).

[10] I. Maity, A. A. Mostofi, and J. Lischner, Phys. Rev. B **105**, L041408 (2022).

[11] K. Ishito, H. Mao, Y. Kousaka, Y. Togawa, S. Iwasaki, T. Zhang, S. Murakami, J.-i. Kishine, and T. Satoh, Nat. Phys. **19**, 35 (2023).

[12] H. Ueda, M. García-Fernández, S. Agrestini, C. P. Romao, J. van den Brink, N. A. Spaldin, K.-J. Zhou, and U. Staub, Nature **618**, 946 (2023).

[13] H. Chen, W. Wu, J. Zhu, Z. Yang, W. Gong, W. Gao, S. A. Yang, and L. Zhang, Nano Lett. **22**, 1688 (2022).

[14] M. Hamada, E. Minamitani, M. Hirayama, and S. Murakami, Phys. Rev. Lett. **121**, 175301 (2018).

[15] V. M. Edelstein, Solid State Commun. **73**, 233 (1990).

[16] J. C. R. Sánchez, L. Vila, G. Desfonds, S. Gambarelli, J. P. Attané, J. M. De Teresa, C. Magén, and A. Fert, Nat. Commun. **4**, 2944 (2013).

[17] T. Yoda, T. Yokoyama, and S. Murakami, Sci. Rep. **5**, 12024 (2015).

[18] A. Einstein and W. J. de Haas, Deut. Phys. Ges. **17**, 152 (1915).

[19] A. Einstein and W. J. de Haas, KNAW Proc. **18 I**, 696 (1915).

[20] L. Zhang and Q. Niu, Phys. Rev. Lett. **112**, 085503 (2014).

[21] D. M. Juraschek and N. A. Spaldin, Phys. Rev. Mater. **3**, 064405 (2019).

[22] D. M. Juraschek, P. Narang, and N. A. Spaldin, Phys. Rev. Res. **2**, 043035 (2020).

[23] K. Ohe, H. Shishido, M. Kato, S. Utsumi, H. Matsuura, and Y. Togawa, Phys. Rev. Lett. **132**, 056302 (2024).

[24] K. Uchida, S. Takahashi, K. Harii, J. Ieda, W. Koshibae, K. Ando, S. Maekawa, and E. Saitoh, Nature **455**, 778 (2008).

[25] K. Kim, E. Vetter, L. Yan, C. Yang, Z. Wang, R. Sun, Y. Yang, A. H. Comstock, X. Li, J. Zhou, L. Zhang, W. You, D. Sun, and J. Liu, Nat. Mater. **22**, 322 (2023).

[26] M. K. Jana, R. Song, H. Liu, D. R. Khanal, S. M. Janke, R. Zhao, C. Liu, Z. Valy Vardeny, V. Blum, and D. B. Mitzi, Nat. Commun. 11, 4699 (2020).

[27] J. Son, S. Ma, Y.-K. Jung, J. Tan, G. Jang, H. Lee, C. U. Lee, J. Lee, S. Moon, W. Jeong, A. Walsh, and J. Moon, Nat. Commun. 14, 3124 (2023).

[28] M. Pols, G. Brocks, S. Calero, and S. Tao, J. Phys. Chem. Lett. 15, 8057 (2024).

[29] C. Zhou, Y. Chu, L. Ma, Y. Zhong, C. Wang, Y. Liu, H. Zhang, B. Wang, X. Feng, X. Yu, X. Zhang, Y. Sun, X. Li, and G. Zhao, Phys. Chem. Chem. Phys. 22, 17299 (2020).

[30] J.-T. Lin, D.-G. Chen, L.-S. Yang, T.-C. Lin, Y.-H. Liu, Y.-C. Chao, P.-T. Chou, and C.-W. Chiu, Angew. Chem. Int. Ed. 60, 21434 (2021).

[31] J. Ahn, E. Lee, J. Tan, W. Yang, B. Kim, and J. Moon, Mater. Horiz. 4, 851 (2017).

[32] S. Apergi, G. Brocks, and S. Tao, J. Phys. Chem. Lett. 14, 11565 (2023).

[33] G. Long, C. Jiang, R. Sabatini, Z. Yang, M. Wei, L. N. Quan, Q. Liang, A. Rasmita, M. Askerka, G. Walters, X. Gong, J. Xing, X. Wen, R. Quintero-Bermudez, H. Yuan, G. Xing, X. R. Wang, D. Song, O. Voznyy, M. Zhang, S. Hoogland, W. Gao, Q. Xiong, and E. H. Sargent, Nat. Photonics 12, 528 (2018).

[34] Z.-G. Yu, J. Phys. Chem. Lett. 11, 8638 (2020).

[35] H. Lu, J. Wang, C. Xiao, X. Pan, X. Chen, R. Brunecky, J. J. Berry, K. Zhu, M. C. Beard, and Z. V. Vardeny, Sci. Adv. 5, eaay0571 (2019).

[36] Y.-H. Kim, Y. Zhai, H. Lu, X. Pan, C. Xiao, E. A. Gaulding, S. P. Harvey, J. J. Berry, Z. V. Vardeny, J. M. Luther, and M. C. Beard, Science 371, 1129 (2021).

[37] J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. 115, 036402 (2015).

[38] G. Kresse and J. Hafner, Phys. Rev. B 49, 14251 (1994).

[39] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

[40] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[41] R. Jinnouchi, F. Karsai, and G. Kresse, Phys. Rev. B 100, 014105 (2019).

[42] R. Jinnouchi, J. Lahnsteiner, F. Karsai, G. Kresse, and M. Bokdam, Phys. Rev. Lett. 122, 225701 (2019).

[43] A. Togo, J. Phys. Soc. Jpn. 92, 012001 (2023).

[44] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, J. Phys. Condens. Matter 35, 353001 (2023).

[45] C. Quarti, G. Grancini, E. Mosconi, P. Bruno, J. M. Ball, M. M. Lee, H. J. Snaith, A. Petrozza, and F. De Angelis, J. Phys. Chem. Lett. 5, 279 (2014).

[46] F. Brivio, J. M. Frost, J. M. Skelton, A. J. Jackson, O. J. Weber, M. T. Weller, A. R. Goñi, A. M. A. Leguy, P. R. F. Barnes, and A. Walsh, Phys. Rev. B 92, 144308 (2015).

[47] R.-I. Biega, M. Bokdam, K. Herrmann, J. Mohanraj, D. Skrybeck, M. Thelakkat, M. Retsch, and L. Leppert, J. Phys. Chem. C 127, 9183 (2023).

[48] C. Li, H. Ma, T. Li, J. Dai, M. A. J. Rasel, A. Mattoni, A. Alatas, M. G. Thomas, Z. W. Rouse, A. Shragai, S. P. Baker, B. J. Ramshaw, J. P. Feser, D. B. Mitzi, and Z. Tian, Nano Lett. 21, 3708 (2021).

[49] H. Lu, C. Xiao, R. Song, T. Li, A. E. Maughan, A. Levin, R. Brunecky, J. J. Berry, D. B. Mitzi, V. Blum, and M. C. Beard, J. Am. Chem. Soc. 142, 13030 (2020).

[50] H. Zhang, N. Peshcherenko, F. Yang, T. Z. Ward, P. Raghuvanshi, L. Lindsay, C. Felser, Y. Zhang, J.-Q. Yan, and H. Miao, Observation of Phonon Angular Momentum (2024), 2409.13462.