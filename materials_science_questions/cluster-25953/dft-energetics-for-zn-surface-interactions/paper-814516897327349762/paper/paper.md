PHYSICAL REVIEW B 93, 195435 (2016)

# Confinement effects in ultrathin ZnO polymorph films: Electronic and optical properties

Lorenzo Sponza, $^*$ Jacek Goniakowski, $^\dagger$ and Claudine Noguera

CNRS, UMR 7588, Institut des Nanosciences de Paris, F-75005 Paris, France
and Université Pierre et Marie Curie (Université Paris VI), Paris, France

(Received 15 March 2016; revised manuscript received 4 May 2016; published 25 May 2016)

Relying on generalized-gradient and hybrid first-principles simulations, this work provides a complete characterization of the electronic properties of ZnO ultrathin films, cut along the body-centered-tetragonal(010), cubane(100), hexagonal boron nitride(0001), zinc-blende(110), and wurtzite (10$\overline{1}$0) and (0001) orientations. The characteristics of the local densities of states are analyzed in terms of the reduction of the Madelung potential on undercoordinated atoms and surface states/resonances appearing at the top of the valence band and bottom of the conduction band. The gap width in the films is found to be larger than in the corresponding bulks, which is assigned to quantum confinement effects. The components of the high-frequency dielectric constant are determined and the absorption spectra of the films are computed. They display specific features just above the absorption threshold due to transitions from or to the surface resonances. This study provides a first understanding of finite-size effects on the electronic properties of ZnO thin films and a benchmark which is expected to foster experimental characterization of ultrathin films via spectroscopic techniques.

DOI: 10.1103/PhysRevB.93.195435

## I. INTRODUCTION

Zinc oxide is a wide-gap semiconductor [1] of technological importance, widely used for its semiconducting and optical properties. It can be grown under a wide variety of nanoparticle shapes and sizes or as thin films, with many potential applications in the fields of catalysis, gas sensors, photoelectric devices, or transparent electronics [2–4]. This richness of applications partly comes from the existence of many structural polymorphs, with rather close formation energies. While wurtzite (WUR) is its structural ground state under normal conditions, ZnO has also been prediceted to adopt zinc-blende (ZB), body-centred tetragonal (BCT), cubane (CUB), or hexagonal boron nitride (h-BN) structures, depending on the conditions of formation [5–9].

In these polymorphs, the zinc and oxygen atoms experience different environments, especially when some reduction of dimensionality takes place, which may strongly modify the electronic properties. Bulk gap widths and densities of states (DOS) have been scrutinized by first-principles simulations [10,11] and we have recently disentangled the effects of band narrowing and of electrostatics in the modifications of quasiparticle, absorption, and electron energy loss spectra [12].

Beyond bulk properties, the possibility of tuning electronic and optical properties through a reduction of dimensionality has fostered advances in the fabrication and structural characterization of ZnO nanostructures [13–19] and thin films on various substrates [20–30], with a range of techniques and under a variety of experimental conditions. In particular in ultrathin films, theoretical and experimental works indicate important variations of the atomic structure as a function of thickness [31–34]. However, to which extent the electronic properties are affected by these structural changes has not yet been investigated in detail.

In the present work, we focus on the electronic properties of ZnO thin films with four monolayer (4-ML) thickness, cut along the body-centered-tetragonal (BCT) (010), cubane (CUB) (100), hexagonal boron nitride (h-BN) (0001), zinc-blende (ZB) (110), and wurtzite (WUR) (01$\overline{1}$0) and (0001) orientations. We analyze the gap widths, the layer-projected density of states, and the optical properties. We are able to highlight the role of surface undercoordinated atoms in determining the largest modifications of these properties with respect to the corresponding bulk structures.

The structure of the paper is the following. After a description of the numerical approach (Sec. II), we stress the main structural characteristics which will be of importance for the understanding of the electronic properties (Sec. III). We then analyze the DOS characteristics, with special emphasis on electrostatic effects, and we discuss the gap widths (Sec. IV). Optical dielectric functions and absorption spectra are the subject of Sec. V, before the conclusion.

## II. METHOD

All ground-state calculations are performed within the framework of the density functional theory (DFT), using the projector augmented wave method [35,36], and a plane wave basis set, as implemented in VASP [37]. Valence electrons are $2s$ and $2p$ for oxygen and $3d$ and $4s$ for zinc. The Perdew, Burke, and Ernzerhof (PBE) generalized-gradient approximation [38] is systematically used for structural optimization, while electronic properties are computed with the range-separated hybrid HSE03 exchange-correlation functional [39]. The use of the HSE03 functional is meant to improve the PBE underestimation of the band gap in semiconductors and insulators and the excessive delocalization of $d$ electrons. It is especially useful for the simulation of compounds with full or empty $d$ shells, that are described less efficiently by the DFT+U approach.

Slabs of 4 ML [40] have been designed for each structure and orientation, with approximately $12$ Å of empty space to prevent spurious interactions between replicated slabs.

$^*$Present address: King's College of London, London, United Kingdom.
$^\dagger$Corresponding author: jacek@insp.jussieu.fr

2469-9950/2016/93(19)/195435(9)
195435-1
©2016 American Physical Society

Dipole correction is applied to slabs with two nonequivalent terminations. The energy cutoff is 500 eV and the k-point grids, centered at $\Gamma$, used to sample the Brillouin zone of the $(1\times1)$ surface cell, are $5\times7\times1$ for BCT(010), $4\times$ $4\times1$ for CUB(100), $8\times8\times1$ for h-BN(0001), $8\times6\times1$ for WUR($10\overline{1}0$), $8\times8\times1$ for ZB(110) and $6\times6\times1$ for WUR(0001). Cell optimization is stopped when all forces get lower than 0.01 eV/Å and in-plane components of the stress tensor are below $0.01$ eV/Å$^3$. This setting leads to converged values of the cell parameters within $0.01$ Å and of the total energies within 0.01 eV per formula unit. Only the ideal BCT structure ($a=b$) is considered.

Optical properties are computed within the linear response theory, in which the response to a perturbing field is described by the complex dielectric function $\epsilon(\mathbf{q},\omega)=$ $\epsilon_1(\mathbf{q},\omega)+i\epsilon_2(\mathbf{q},\omega)$ ($\omega$ the energy of the perturbation and $\mathbf{q}$ the exchanged momentum which tends to zero for interaction with light). In the random-phase approximation [41] (RPA), and under the assumption of an homogeneous medium (neglect of local fields NLFE), the dielectric function $\epsilon(\mathbf{q},\omega)=$ $1-4\pi\chi^0(\mathbf{q},\omega)/|\mathbf{q}|^2$ is expressed in terms of the macroscopic component of the independent particle polarizability $\chi^0(\mathbf{q},\omega)$, which we compute as the weighted sum over all transitions [42,43] from occupied to empty (HSE03) Kohn-Sham states, thus neglecting excitonic effects. Within such approximations, the absorption spectrum is given by $A(\omega)=$ $\lim_{\mathbf{q}\to0}\epsilon_2(\mathbf{q},\omega)$. Depending on the Cartesian direction along which the limit is taken, the spectra along the $x$, $y$, or $z$ direction are computed ($z$ perpendicular to the surface). The dielectric constant $\lim_{\mathbf{q}\to0}\epsilon_1(\mathbf{q},0)$ is computed via Kramers-Kronig relations from the imaginary part $\epsilon_2(\mathbf{q},\omega)$. The sum over all transitions has been cut at 30 eV and finer k-point grids (all centered in $\Gamma$) are used: $12\times9\times1$ for WUR($10\overline{1}0$), $9\times12\times1$ for BCT(010), $9\times9\times1$ for CUB(100), and $12\times12\times1$ for the remaining three structures.

## III. STRUCTURAL PROPERTIES

This section is devoted to a description of the main structural characteristics of the 4-ML films, with a special emphasis on those which will be of importance for understanding the electronic properties. For each polymorph, we have considered the film orientation which has the lowest energy, i.e., BCT(010), CUB(100), h-BN(0001), ZB(110), and WUR($10\overline{1}0$) [31,44]. We have also considered the WUR(0001) polar orientation, with a reconstructed $(2\times2)$ surface configuration in which one oxygen (respectively, zinc) atom on 4 is removed on the oxygen (respectively zinc) termination. This is the conventional method to reduce the buildup of a macroscopic dipole. The two-dimensional (2D) unit cells of these 4-ML films are sketched in Fig. 1. The surface unit cells display different symmetries: square for CUB(100); hexagonal in the case of h-BN(0001) and WUR(0001); and rectangular for BCT(010), WUR($10\overline{1}0$), and ZB(110). At the film surfaces, some atoms are undercoordinated. We label them $\text{U}_1$ and $\text{U}_2$ according to whether they are directly in contact with vacuum or immediately subsurface. Internal atoms are labeled I, as sketched in Fig. 1. In the h-BN(0001) films, $\text{U}_2$ atoms do not exist. In the case of WUR(0001), there are two types of subsurface atoms with different local environments: three atoms (labeled $\text{U}_3$ in the following) are adjacent to the surface vacancy while the fourth one (labeled $\text{U}_2$) is not.

![](./images/814516897327349762_1.jpg)

FIG. 1. Unit cells of 4-ML ZnO thin films. Zn and O atoms are represented by big (gray) and small (red) balls, respectively. For CUB(100) a sketch of the structure clarifies the convention for the sites and the layers.

Structural data, compared to reference bulk calculations [12], are reported in Table I, as well as the HSE03 film formation energy per surface area, defined as:

$$
E_{f}=\frac{E_{\mathrm{film}}-n E_{\mathrm{bulk}}^{\mathrm{WUR}}}{S}. \tag{1}
$$

In this expression, $n$ is the number of formula units in the thin-film cell, $E_{\mathrm{film}}$ is the total energy of the film per unit cell, $E_{\mathrm{bulk}}^{\mathrm{WUR}}$ is the total energy per formula unit of the bulk wurtzite structure, both calculated at the HSE03 level on top of the PBE structural ground state, and $S$ is the total surface of the film cell including upper and lower surfaces. Our results both on the structural parameters and the energetics compare well with similar $ab$ initio calculations found in the literature [31–34,45].

A feature shared by all films except h-BN(0001) is the expansion of the lateral lattice parameters with respect to bulk. This effect is caused by a flattening of the surface layers, evidenced by an increase in the average surface bond angle $\langle\alpha\rangle$. This is the so-called rotational relaxation mechanism, well known at the surface of semiconductors [46,47]. It induces a contraction of the structure in the perpendicular direction to preserve the atomic volumes. However, in the present case,

<table>
<caption>TABLE I. Structural and energetic properties of ZnO 4-ML thin films: surface unit cell parameters (in-plane $a$,$b$), film thickness $h$, surface layer average angle $\langle\alpha\rangle=(\alpha_1+\alpha_2)/2$, as shown in Fig. 1, dangling bond angle $\theta$ (see text), and formation energy $E_f$ per surface area. Structural quantities are compared to corresponding bulk values [12] (in parenthesis).</caption>
<tbody>
<tr>
<td colspan="2">WUR(10$\overline{1}$0): Rectangular 2D unit cell</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>$3.32\ (+1.2\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$b$ (Å)</td>
<td>$5.34\ (+0.8\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$h$ (Å)</td>
<td>$9.39\ (-1.0\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\langle\alpha\rangle$ $(^\circ)$</td>
<td>$112.7\ (+3.7\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\theta$ $(^\circ)$</td>
<td>$10$</td>
</tr>
<tr>
<td>$E_f$ (eV/Å$^2$)</td>
<td>$0.058$</td>
</tr>
<tr>
<td colspan="2">BCT(010): Rectangular 2D unit cell</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>$5.70\ (+1.4\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$b$ (Å)</td>
<td>$3.31\ (+0.9\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$h$ (Å)</td>
<td>$8.69\ (-5.4\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\langle\alpha\rangle$ $(^\circ)$</td>
<td>$117.9\ (+4.3\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\theta$ $(^\circ)$</td>
<td>$6$</td>
</tr>
<tr>
<td>$E_f$ (eV/Å$^2$)</td>
<td>$0.049$</td>
</tr>
<tr>
<td colspan="2">ZB(110): Rectangular 2D unit cell</td>
</tr>
<tr>
<td>$a$ (Å)</td>
<td>$3.31\ (+1.2\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$b$ (Å)</td>
<td>$4.60\ (-0.4\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$h$ (Å)</td>
<td>$11.41\ (-0.3\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\langle\alpha\rangle$ $(^\circ)$</td>
<td>$111.8\ (+2.1\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\theta$ $(^\circ)$</td>
<td>$28$</td>
</tr>
<tr>
<td>$E_f$ (eV/Å$^2$)</td>
<td>$0.067$</td>
</tr>
<tr>
<td colspan="2">CUB(100): Square 2D unit cell</td>
</tr>
<tr>
<td>$a=b$ (Å)</td>
<td>$6.34\ (+1.0\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$h$ (Å)</td>
<td>$10.05\ (-4.3\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\langle\alpha\rangle$ $(^\circ)$</td>
<td>$129.8\ (+3.6\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\theta$ $(^\circ)$</td>
<td>$12$</td>
</tr>
<tr>
<td>$E_f$ (eV/Å$^2$)</td>
<td>$0.078$</td>
</tr>
<tr>
<td colspan="2">h-BN(0001): Hexagonal 2D unit cell</td>
</tr>
<tr>
<td>$a=b$ (Å)</td>
<td>$3.39\ (-2.6\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$h$ (Å)</td>
<td>$7.11\ (+4.8\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\theta$ $(^\circ)$</td>
<td>$0$</td>
</tr>
<tr>
<td>$E_f$ (eV/Å$^2$)</td>
<td>$0.049$</td>
</tr>
<tr>
<td colspan="2">WUR(0001): Hexagonal 2D unit cell</td>
</tr>
<tr>
<td>$a=b$ (Å)</td>
<td>$6.62\ (+0.9\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$h$ (Å)</td>
<td>$8.11\ (-5.5\%$ wrt bulk$)$</td>
</tr>
<tr>
<td>$\theta$ $(^\circ)$</td>
<td>$0$</td>
</tr>
<tr>
<td>$E_f$ (eV/Å$^2$)</td>
<td>$0.086$</td>
</tr>
</tbody>
</table>

it does not preclude some simultaneous bond contraction. In the h-BN(0001) film, since the layers are already flat, surface bond breaking only induces a contraction of the in-plane parameters, which leads to an expansion in the perpendicular direction.

More detailed analysis (Table III in Sec. IV) shows that, in all structures, undercoordinated atoms $\text{U}_1$ or $\text{U}_3$ have lost one first neighbor and between three and five second neighbors, while atoms $\text{U}_2$ have a complete first coordination shell and a second coordination shell reduced by one to three units. The average Zn-O bond lengths around $\text{U}_1$ and $\text{U}_3$ atoms are reduced by approximately $0.1$ Å (see Table I in the Supplemental Material [48]). In all cases, I atoms have complete first and second coordination shells, and the bond relaxation around them is quasineligible on average.

Finally, in Table I, we give the angle $\theta$ between the $ab$ plane and the plane which contains the three first neighbors of $\text{U}_1$ atoms. This angle measures the projection of the dangling bond located on $\text{U}_1$ atoms on the $z$ axis perpendicular to the surface, and thus characterizes the mixing of $p_z$ with $p_{x,}p_y$ orbitals in the surface dangling bonds.

### IV. ELECTRONIC STRUCTURE

In this section, we discuss the electronic characteristics, obtained by using the hybrid HSE03 exchange-correlation functional on top of the PBE structural ground state of the films. The relevant characteristics include the main DOS structures in the valence (VB) and conduction (CB) bands, and the gap width. We relate their modifications with respect to their respective bulks to changes in the local environment of the surface atoms.

#### A. Characteristics of the local densities of states

Figure 2 displays the local densities of states (LDOS) of the six films, projected on internal layers (I atoms), surface atoms of type $\text{U}_1$, and subsurface atoms of type $\text{U}_2$ or $\text{U}_3$.

The overall DOS shape is similar for all polymorphs. At the very bottom of the VB, two peaks with nearly O $2s$ and Zn $3d$ character, respectively, are found, lower in energy than the oxygen band, formed by the $\text{O}_1$ peak ($\sim -5$ eV) due to Zn $4s$-O $2p$ bonding states, and the $\text{O}_2$ region (from Fermi level to about $-4$ eV), associated to Zn $3d$-O $2p$ antibonding states and O-O hybridization. In the conduction band, beyond the extended onset region, three zones can be identified: The $S$ zone, mainly formed by O $2p$ - Zn $4s$ antibonding states; the $P_1$ zone, formed by states with mixed Zn $p$ and Zn $s$ character; and the $P_2$ zone at higher energy, with predominant Zn $p$ orbital component. The average positions of the most noticeable structures are reported in Table II, together with a comparison of gap widths $E_g$ between the bulks and the films.

There is a close resemblance between the LDOS shapes that are found on the internal I atoms and those in the bulk, displayed in our previous work [12]. The tiny differences, in particular the splitting of the Zn $d$ state due to the crystal field which is somewhat blurred in some films, result from the long-range electrostatic and/or covalent interactions existing in ZnO, which are partly cut in the films.

As far as LDOS on surface atoms $\text{U}_1$, $\text{U}_2$, or $\text{U}_3$ are concerned, it is difficult to find systematic characteristics of the $S$, $P_1$, or $P_2$ peaks in the CB, likely because of the delocalized nature of the orbitals involved, except in the two WUR films for which the $S$ and $P_2$ peaks of the $\text{U}_1$ and $\text{U}_2$ LDOS are shifted towards higher energies. Close to the VB and CB band edges, there is a clear enhancement of the surface LDOS on undercoordinated atoms, but, considering the orbital overlap between surface and subsurface atoms and the small width of the films, it is difficult to discriminate between actual surface states and surface resonances. In the CB, for all polymorphs, surface resonances mainly localized on $\text{U}_1$ and $\text{U}_2$ atoms are present from approximately 2 to 4 eV above the CB minimum. The CB minimum itself involves orbitals on all atoms of

![](./images/814516897327349762_2.jpg)

FIG. 2. Local densities of states in ZnO 4-ML films on I, $U_1$, $U_2$, and $U_3$ [in the case of WUR(0001)] atoms, represented as solid black, dashed blue, dotted red, and dashed-dotted green lines, respectively.

the films, except in the WUR(0001) film, where there is a well-defined surface state on $U_3$ atoms.

In the VB, surface resonances with strong $U_1$ and $U_2$ oxygen $p_z$ character and, to a lesser extent, I oxygen orbitals are present in all polymorphs in an energy range from 0.2 to $\approx 1$ eV below the top of the VB. At the extreme top of the VB true surface states with $U_1/U_3$ and $U_2$ oxygen $p_x$ and $p_y$ character are present, with a degree of hybridization with $p_z$ orbitals which increases in the series: h-BN(0001), WUR(0001), BCT(010), WUR(10$\overline{1}$0), CUB(100), and ZB(110) (see Fig. 1 in the Supplemental Material [48]). As expected, the evolution of the degree of hybridization follows the variations of the angle $\theta$ between the $U_1$ dangling bond orientation and the direction $z$ perpendicular to the surface which increases in the series (Table I). The relationship among these VB LDOS characteristics, the absorption spectra, and the optical dielectric function will be discussed in Sec. V.

More remarkable are the differences between internal and surface LDOS involving localized O $2s$ and Zn $3d$ orbitals in the valence band. Figure 2 evidences a systematic shift towards higher energies (blue-shift) for the former and towards lower energies (red-shift) for the latter on the $U_1$ or $U_3$ atoms, while the opposite is true on $U_2$ atoms. These shifts are given in Table III and are related to the modifications of the electrostatic potential on undercoordinated atoms, to be discussed below.

### B. Electrostatic effects

LDOS characteristics, especially as far as localized states are concerned, may be understood by considering the electrostatic potentials [49] $V_O$ and $V_{Zn}$ acting on the various oxygen and zinc atoms of the films. They include long-range contributions, but their variations among nonequivalent atoms are mainly related to local environments (i.e., to the variations $\delta N_1$ and $\delta N_2$ of the numbers of first and second neighbors). Table III records the differences $\delta V_O$ and $\delta V_{Zn}$ of electrostatic potentials between undercoordinated surface atoms and fully coordinated internal atoms.

On $U_1/U_3$ atoms, the negative sign of $\delta V_O$ and the positive sign of $\delta V_{Zn}$ indicate a decrease (in absolute value) of the electrostatic potential, as expected from the loss of one first neighbor. The effect is modulated by longer-range interactions and by the length of the broken bond. For example, in the h-BN film, which has a quasilayered structure, the bonds which are broken at the surface are very long and do not induce strong modifications of electrostatic potential. Consequently, the latter is mostly determined by the in-plane arrangement, which does not change from plane to plane. In WUR(10$\overline{1}$0) and (0001), BCT(010), ZB(110), and CUB(100) films, $\delta V_O$ and $\delta V_{Zn}$ are quite noticeable. WUR(0001) film displays the largest potential variations, which we will discuss separately. Conversely, as far as $U_2$ atoms are concerned, the signs of $\delta V_O$ and $\delta V_{Zn}$ are opposite to those on $U_1$ and $U_3$, consistently, with

TABLE II. Mean positions of the main LDOS structures on the internal I layers (see text) with respect to the Fermi level (in eV); bulk and film gap widths $E_g$ and their difference $\delta E_g = E_g$(film)-$E_g$(bulk) (in eV). Note that for h-BN the bulk gap value recorded here is the minimal gap; the direct one is equal to 2.42 eV.

<table>
<thead>
<tr>
<th></th>
<th>O $2s$</th>
<th>Zn $3d$</th>
<th>$O_1$</th>
<th>$O_2$</th>
<th>$S$</th>
<th>$P_1$</th>
<th>$P_2$</th>
<th>$E_g$(bulk)</th>
<th>$E_g$(film)</th>
<th>$\delta E_g$</th>
</tr>
</thead>
<tbody>
<tr>
<td>WUR(10$\overline{1}$0)</td>
<td>$-18.83$</td>
<td>$-6.36$</td>
<td>$-4.14$</td>
<td>$-1.86$</td>
<td>$9.8$</td>
<td>$12.5$</td>
<td>$14.9$</td>
<td>$2.20$</td>
<td>$2.25$</td>
<td>$+0.05$</td>
</tr>
<tr>
<td>BCT(010)</td>
<td>$-18.81$</td>
<td>$-6.30$</td>
<td>$-3.94$</td>
<td>$-1.72$</td>
<td>$9.6$</td>
<td>$11.1$</td>
<td>$15.0$</td>
<td>$2.20$</td>
<td>$2.37$</td>
<td>$+0.17$</td>
</tr>
<tr>
<td>ZB(110)</td>
<td>$-18.70$</td>
<td>$-6.19$</td>
<td>$-4.21$</td>
<td>$-1.83$</td>
<td>$10.3$</td>
<td>$12.0$</td>
<td>$14.8$</td>
<td>$2.09$</td>
<td>$2.31$</td>
<td>$+0.22$</td>
</tr>
<tr>
<td>CUB(100)</td>
<td>$-18.56$</td>
<td>$-6.18$</td>
<td>$-3.64$</td>
<td>$-1.48$</td>
<td>$9.7$</td>
<td>$11.7$</td>
<td>$15.8$</td>
<td>$2.68$</td>
<td>$2.71$</td>
<td>$+0.03$</td>
</tr>
<tr>
<td>h-BN(0001)</td>
<td>$-18.72$</td>
<td>$-6.15$</td>
<td>$-3.92$</td>
<td>$-1.67$</td>
<td>$9.9$</td>
<td>$12.3$</td>
<td>$15.2$</td>
<td>$2.31$</td>
<td>$2.66$</td>
<td>$+0.35$</td>
</tr>
<tr>
<td>WUR(0001)</td>
<td>$-19.21$</td>
<td>$-6.63$</td>
<td>$-4.61$</td>
<td>$-2.35$</td>
<td>$9.4$</td>
<td>$11.8$</td>
<td>$13.9$</td>
<td>$2.20$</td>
<td>$1.62$</td>
<td>$-0.58$</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE III. Shifts of the average peak positions (in eV), variations of electrostatic potentials $\delta V_{\text{O}}$ and $\delta V_{\text{Zn}}$ on oxygen and Zn atoms (in V), and of coordination numbers $N_1$ and $N_2$ on under-coordinated $\text{U}_1$, $\text{U}_2$, and $\text{U}_3$ atoms, with respect to internal atoms I.</caption>
<thead>
<tr>
<th>
</th>
<th>
O $2s$
</th>
<th>
Zn $3d$
</th>
<th>
O $2p$
</th>
<th>
$\delta V_{\text{O}}$
</th>
<th>
$\delta V_{\text{Zn}}$
</th>
<th>
$\delta N_1$
</th>
<th>
$\delta N_2$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
WUR(10$\overline{1}$0):
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\text{U}_1$-I
</td>
<td>
+0.64
</td>
<td>
$-$0.37
</td>
<td>
+0.53
</td>
<td>
$-$0.76
</td>
<td>
+0.47
</td>
<td>
$-$1
</td>
<td>
$-$4
</td>
</tr>
<tr>
<td>
$\text{U}_2$-I
</td>
<td>
$-$0.33
</td>
<td>
+0.42
</td>
<td>
$-$0.09
</td>
<td>
+0.37
</td>
<td>
$-$0.54
</td>
<td>
0
</td>
<td>
$-$2
</td>
</tr>
<tr>
<td>
BCT(010):
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\text{U}_1$-I
</td>
<td>
+0.55
</td>
<td>
$-$0.27
</td>
<td>
+0.43
</td>
<td>
$-$0.60
</td>
<td>
+0.36
</td>
<td>
$-$1
</td>
<td>
$-$3
</td>
</tr>
<tr>
<td>
$\text{U}_2$-I
</td>
<td>
$-$0.11
</td>
<td>
+0.33
</td>
<td>
$-$0.01
</td>
<td>
+0.19
</td>
<td>
$-$0.39
</td>
<td>
0
</td>
<td>
$-$2
</td>
</tr>
<tr>
<td>
ZB(110):
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\text{U}_1$-I
</td>
<td>
+0.43
</td>
<td>
$-$0.20
</td>
<td>
+0.42
</td>
<td>
$-$0.51
</td>
<td>
+0.25
</td>
<td>
$-$1
</td>
<td>
$-$5
</td>
</tr>
<tr>
<td>
$\text{U}_2$-I
</td>
<td>
$-$0.09
</td>
<td>
+0.07
</td>
<td>
$-$0.01
</td>
<td>
+0.08
</td>
<td>
$-$0.10
</td>
<td>
0
</td>
<td>
$-$1
</td>
</tr>
<tr>
<td>
CUB(100):
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\text{U}_1$-I
</td>
<td>
+0.42
</td>
<td>
$-$0.15
</td>
<td>
+0.38
</td>
<td>
$-$0.45
</td>
<td>
+0.20
</td>
<td>
$-$1
</td>
<td>
$-$3
</td>
</tr>
<tr>
<td>
$\text{U}_2$-I
</td>
<td>
$-$0.08
</td>
<td>
+0.15
</td>
<td>
+0.01
</td>
<td>
+0.09
</td>
<td>
$-$0.17
</td>
<td>
0
</td>
<td>
$-$1
</td>
</tr>
<tr>
<td>
h-BN(0001):
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\text{U}_1$-I
</td>
<td>
+0.37
</td>
<td>
$-$0.02
</td>
<td>
+0.18
</td>
<td>
$-$0.18
</td>
<td>
+0.10
</td>
<td>
$-$1
</td>
<td>
$-$3
</td>
</tr>
<tr>
<td>
WUR(0001):
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$\text{U}_1$-I
</td>
<td>
0.35
</td>
<td>
$-$0.05
</td>
<td>
+0.41
</td>
<td>
$-$0.40
</td>
<td>
+0.08
</td>
<td>
$-$1
</td>
<td>
$-$5
</td>
</tr>
<tr>
<td>
$\text{U}_3$-I
</td>
<td>
+0.78
</td>
<td>
$-$0.63
</td>
<td>
+0.66
</td>
<td>
$-$0.92
</td>
<td>
+0.75
</td>
<td>
$-$1
</td>
<td>
$-$3
</td>
</tr>
<tr>
<td>
$\text{U}_2$-I
</td>
<td>
$-$0.18
</td>
<td>
+0.41
</td>
<td>
$-$0.10
</td>
<td>
+0.23
</td>
<td>
$-$0.58
</td>
<td>
0
</td>
<td>
$-$3
</td>
</tr>
</tbody>
</table>

no loss of first neighbors (of opposite charge) and a decrease in the number of second neighbors (of same charge).

Within a Hartree or Hartree-Fock approximation, the diagonal matrix elements of the Hamiltonian/Fock operator on an atomic orbital basis set have a contribution $-V_i$ due to the electrostatic potential [50,51]. Applied to ZnO films, the decrease of $|\delta V|$ on $\text{U}_1$ and $\text{U}_3$ atoms thus pushes their O $2s$ levels towards higher energies and their Zn $3d$ levels towards lower energies. Conversely, the increase of $|\delta V|$ on $\text{U}_2$ atoms pushes their O $2s$ levels and their Zn $3d$ levels in the opposite direction. Figure 3 shows that the correlation is quantitatively obeyed for all undercoordinated atoms.

The reduction of electrostatic potential on $\text{U}_1$/$\text{U}_3$ atoms is also responsible for the presence of strong surface states/resonances in the top part of the VB and the bottom part of the CB. However, the hybridized character of these states makes the correlation between their positions and the reduction of electrostatic potential less quantitative than for the more localized O $2s$ and Zn $3d$ states, and the precise surface geometry also plays a role. At the very bottom of the CB where the states are more diffuse, no actual surface state exists, only resonances with a substantial admixing with I atom orbitals, despite the values of $\delta V_{\text{O}}$ and $\delta V_{\text{Zn}}$. More localized DOS structures corresponding to surface resonances may be found from approximately 2 to 4 eV above the CB minimum (Fig. 2).

![](./images/814516897327349762_3.jpg)

FIG. 3. Linear correlation between the positions with respect to I of the Zn $3d$ and O $2s$ LDOS peaks localized on atoms $\text{U}_1$,$\text{U}_2$, and $\text{U}_3$ and the electrostatic potential differences $\delta V_{\text{O}}$ or $\delta V_{\text{Zn}}$ for all polymorph films (see text).

At the very top of the VB, in WUR(10$\overline{1}$0), WUR(0001), BCT(010), and CUB(100) films, $\delta V_{\text{O}}$ and $\delta V_{\text{Zn}}$ are sufficiently large to produce surface states and surface resonances. Highest in energy are weak oxygen-oxygen antibonding states mainly involving $p_x$ and $p_y$ orbitals within the surface layer, while a few tenths of eV below are surface resonances of oxygen $p_z$ dangling bond character. In ZB(110) films, little oxygen-oxygen bonding exists within the surface layer, so the states at the very top of the VB have a resonance, not a surface state, character. As well recognized at the surface of ZB semiconductors, the buckling of the surface dimers which pushes oxygens outwards and tends to transform the $sp_3$ bonding into $sp_2$ hybridization pushes back the dangling bond surface state into the VB. In the h-BN(0001) film, with all layers being nearly identical from an electronic point of view due to the extremely weak interlayer coupling (reflected in the weak $\delta V_{\text{O}}$ and $\delta V_{\text{Zn}}$ values), VB states display a mixed character between $\text{U}_1$ and I orbitals. Finally, the largest electrostatic potential variations are found at the surface of WUR(0001) on $\text{U}_3$ atoms. They induce the presence of surface states with $p_x$,$p_y$ character, not only at the top of the VB but also at the bottom of the CB.

As shown in Table III, in WUR(0001), there is a surprisingly large difference in $\delta V_{\text{O}}$ and $\delta V_{\text{Zn}}$ values between $\text{U}_1$ and $\text{U}_3$ atoms, while their local environments present the same reduction of first neighbors and a not-so-different reduction

of second neighbors. Remembering that atoms $U_1$ and $U_3$ are of same chemical nature and are located at opposite film terminations, we assign the difference to a residual electrostatic dipole, due to an incomplete compensation of polarity. Indeed, at the WUR(0001) semi-infinite polar surface, it is usually considered that the removal of one-fourth of surface ions does heal polarity because the ratio of successive interlayer distances $R_1/(R_1+R_2)$ is close to $1/4$. However, this statement neglects the fact that the $R_1/(R_1+R_2)$ ratio is not exactly equal to $1/4$. It also neglects the polarization of electronic origin, which exists in the non-centro-symmetric wurtzite structure. Moreover, in the 4-ML film, finite-size effects have to be taken into account, which modify the criterion of polarity compensation [52,53]. This interpretation is further confirmed by an analogous simulation of a 4-ML ZB(111) film. Since along the ZB(111) polar orientation $R_1/(R_1+R_2)=1/4$ and since there is no spontaneous po- larization in the ZB centrosymmetric structure, the removal of one-fourth of surface ions exactly heals polarity at its semi-infinite (111) surface. In ZB(111) thin films, thus only finite-size effects may produce a residual dipole. We indeed find that the difference in $\delta V_O$ and $\delta V_{Zn}$ values between $U_1$ and $U_3$ atoms is strongly reduced compared to that in WUR(0001) ($-0.02$ V and $+0.17$ V on oxygen and zinc atoms, respectively, to be compared to $-0.52$ V and $+0.67$ V).

### C. Band gaps

As shown in Table II, the direct gaps at $\Gamma$ of the films are systematically larger than their bulk counterparts, except in the WUR(0001) film. Several effects affect the gap widths [54].

The first one is a gap enlargement due to the decrease of surface band widths as the local environment of atoms becomes less dense. This mechanism has been invoked to explain gap differences between ZnO bulk polymorphs [10,12]. However, for a given polymorph, it cannot explain gap differences between films and bulk. Indeed, surface atoms have fewer second neighbors than internal atoms, leading to a narrowing of the O $2p$-O $2p$ band width at the top of the valence band and of the Zn $4s$-Zn $4s$ band width at the bottom of the conduction band. A gap enlargement thus can take place in the LDOS of surface atoms but not in the LDOS of internal atoms which have more or less the same local environment as in the bulk. The surface effect thus does not modify the minimal gap of the whole film, which is fixed by the LDOS of internal atoms.

A second effect is a gap reduction due to the decrease of the electrostatic potential on surface atoms, as discussed above. Surface states present at the top of VB or bottom of CB induce a gap reduction. We have previously seen that the effect is especially strong in the WUR(0001) film but also exists, although to a lesser extent, in WUR($10\overline{1}0$), BCT(010), and CUB(100) films. However, Table II shows that, in all cases except WUR(0001), this electrostatic-driven gap reduction is not dominant. The gaps in the films are larger than in the bulks, which requires larger gaps in the LDOS of I atoms than in the bulks. We have checked that the structural distortions which occur in the central layers with respect to the bulk structure (increase of lateral lattice parameter and layer flattening) yield negligible gap variations (one order of magnitude lower than those found). We thus suggest that the gap increase that we find may be due to quantum confinement, i.e., the quantification of states propagating perpendicular to the film surfaces. This effect is known to induce an opening of the gap in semiconductor nanocrystallites and thin films [55–57]. Since it asymptotically decreases as objects become bigger, it is expected to be particularly strong in 4-ML ultrathin films and to likely prevail over the gap narrowing due to electrostatic effects, except when the latter is exceptionally strong as in WUR(0001).

## V. OPTICAL PROPERTIES

On the basis of the electronic structure characteristics discussed in the preceding section, we now analyze the optical properties of the ZnO films, first focusing on the optical dielectric constant and then on the absorption spectra.

### A. Optical dielectric function

The values of the high-frequency bulk dielectric constant $\epsilon_\infty$, i.e., the values of the dielectric constant in the limit of infinite phonon and zero electronic frequencies, are gathered in Table IV for the various ZnO polymorphs. In anisotropic bulks (WUR, BCT, and h-BN), the ordinary (OC) and extraordinary (EC) components are given, associated to a momentum transfer parallel and perpendicular to the $ab$ plane, respectively.

In bulk WUR, the values found are in agreement with previous theoretical estimations at the same level of the- ory [58–60], and close to the experimental value of 3.7 [61], a typical value for a semiconductor of mixed ionic and covalent character. Among the polymorphs, the variations of $\epsilon_\infty$ qualitatively correlate with the mean valence electronic density $n$, as expected from simple models of screening [50] $\epsilon_\infty \approx 1+4\pi ne^2/(mE_g^2)$.

The evaluation of the high-frequency dielectric constants $\epsilon_\infty$ of the films is less straightforward. In a first step, the dielectric constant $\epsilon_{\rm sc}(D)$ of the simulated supercell, which includes the film (of thickness $\tilde{h}$) and a large vacuum thickness $L$, is calculated for several values of $D=L+\tilde{h}$ and shown to depend on $D$ according to the following law:

$$
\epsilon_{\rm sc}(D) = \frac{\tilde{h}*\epsilon_\infty+(D-\tilde{h})*\epsilon_{\rm vac}}{D} \tag{2}
$$

TABLE IV. High-frequency dielectric function, in the bulk (left part of the table) and in the films (right part), with reference to the mean electronic density $n$ in the bulk (in $\mathring{\rm A}^{-3}$). OC and EC denote the ordinary and extraordinary components, respectively. In the films, $x$ and $y$ refer to directions parallel to the surface, while $z$ is perpendicular to it.

<table>
  <thead>
    <tr>
      <th></th>
      <th>OC</th>
      <th>EC</th>
      <th>$n$</th>
      <th></th>
      <th>$x$</th>
      <th>$y$</th>
      <th>$z$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WUR</td>
      <td>3.50</td>
      <td>3.54</td>
      <td>1.54</td>
      <td>$(10\overline{1}0)$</td>
      <td>4.04</td>
      <td>4.12</td>
      <td>3.72</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>(0001)</td>
      <td>4.22</td>
      <td>4.22</td>
      <td>3.97</td>
    </tr>
    <tr>
      <td>BCT</td>
      <td>3.35</td>
      <td>3.44</td>
      <td>1.47</td>
      <td>(010)</td>
      <td>4.09</td>
      <td>4.09</td>
      <td>3.69</td>
    </tr>
    <tr>
      <td>ZB</td>
      <td>3.59</td>
      <td>3.59</td>
      <td>1.54</td>
      <td>(110)</td>
      <td>3.96</td>
      <td>3.88</td>
      <td>3.72</td>
    </tr>
    <tr>
      <td>CUB</td>
      <td>2.92</td>
      <td>2.92</td>
      <td>1.23</td>
      <td>(100)</td>
      <td>3.46</td>
      <td>3.46</td>
      <td>3.19</td>
    </tr>
    <tr>
      <td>h-BN</td>
      <td>3.58</td>
      <td>3.68</td>
      <td>1.60</td>
      <td>(0001)</td>
      <td>4.53</td>
      <td>4.53</td>
      <td>4.09</td>
    </tr>
  </tbody>
</table>

in which $\epsilon_{\text{vac}} = 1$ is the vacuum dielectric constant. This law, which is an extrapolation of the expression derived in Ref. [62] for the dielectric screening in two-dimensional insulators, assumes that the electronic polarizability of a complex medium can be estimated from an average of the polarizabilities of its various parts weighted by their respective volumes. From the constant value of $D * [\epsilon_{\text{sc}}(D) - 1]$ that we find while varying $D$, the products $\tilde{h} * (\epsilon_{\infty} - 1)$ can be obtained for each of the three components associated to momentum transfers along $x$, $y$, and $z$.

It is not easy to derive truly reliable values for $\epsilon_{\infty}$, due to the uncertainty on the extension $\tilde{h}$ of the electronic clouds relevant for screening effects in the various thin films. The values written in Table IV, obtained under the assumption that $\tilde{h}$ is equal to the geometric distance $h$ between the outermost planes, must thus be considered as upper bounds to the true values, since $h$ likely underestimates $\tilde{h}$. At variance, the prediction of the anisotropy between the various components is not expected to suffer much from this uncertainty, since the variations of the effective values of $\tilde{h}$ between the three components may only yield second-order corrections. The anisotropy between the $x$ and $y$ components is nonexistent [WUR(0001), CUB(100), h-BN(0001)] or extremely weak [WUR(10$\overline{1}$0), BCT(010) [63], ZB(110)], while the $z$ component is systematically smaller than the $x$ and $y$ ones. The overall anisotropy is thus larger in thin films than in the bulks.

### B. Absorption spectra
The absorption spectra (frequency dependence of the imaginary part of the dielectric function in the limit of vanishing momentum transfer) of the six ZnO thin films are displayed in Fig. 4, together with their bulk reference. As for the high-frequency dielectric constant, the anisotropy of the films is reflected in an increase of nonequivalent contributions in the absorption spectra.

Beyond the onset region to be discussed below, the film absorption spectra present many similarities with their corresponding bulks. The main absorption peaks, labeled A, B, and the shoulder C correspond to transitions from the upper part of the VB (from 0 to $\approx 3$ eV below the VB maximum), to the lower part of the CB (from 0 to $\approx 4$ eV above the CB minimum), to the $\text{S/P}_1$ region, and to the $\text{P}_2$ region, respectively, with reference to the LDOS structures (Fig. 2). Transitions from the Zn $3d$ states have a small weight and their contributions to this part of the spectrum is negligible. At variance, the small X structure located around $\omega = 20$ eV in both OC and EC is due to transitions from these localized Zn $3d$ states to the $\text{P}_2$ region. Due to the differences in local environments of the I, $\text{U}_1$,$\text{U}_2$, and $\text{U}_3$ atoms and the LDOS structure shifts which result, the absorption peaks in the films are generally broadened with respect to their bulk counterparts.

The main differences between the bulk and film absorption spectra occur in the vicinity of the absorption threshold, as seen in Fig. 5, which displays an enlarged view of this spectral region. First, the threshold energy is slightly shifted with respect to the bulk due to the gap variations (cf. Table II). In most polymorphs, this shift is very small and hardly visible at the scale of the figure. Only in WUR(0001) can it be well observed, due to the larger reduction of Madelung potential on surface atoms.

![](./images/814516897327349762_4.jpg)

FIG. 4. Optical absorption spectra of ZnO 4-ML thin films and bulks. For the bulks, dashed-dotted black and dotted red lines denote the ordinary and extraordinary spectra. In the films, solid black, dotted blue, and dashed red lines are for the $\mathbf{q} \parallel x$,$\mathbf{q} \parallel y$,$\mathbf{q} \parallel z$ spectra, respectively. CUB(100) and $h$-BN(0001) are isotropic on the $xy$ plane, so only the $\mathbf{q} \parallel x$ component is reported. Dotted vertical lines arbitrarily aligned with structures of WUR(10$\overline{1}$0), highlight A, B, C, and X regions of the spectra. All spectra have been convoluted with a 0.5-eV-wide Gaussian function.

Specific structures are observed in the $\omega$ range approximately 0–3 eV above threshold, which involve transitions between surface states/resonances in close vicinity to the VB maximum and CB minimum. Starting from the threshold, the first peaks which appear are in the $x$ and $y$ components of the spectra, consistently with the mostly $p_x$ and $p_y$ orbital character of the surface states at the top of the valence band. In the WUR(0001) absorption spectrum, a well-defined prepeak exists due to a transition between the surface states at the top of the VB and the bottom of the CB.

The threshold and first peaks in the $z$ absorption spectra occur at slightly higher energies than in the $x$ and $y$ spectra. Except in WUR(0001) in which electrostatic effects play a prominent role, this energy difference $\Delta$ inversely correlates

![](./images/814516897327349762_5.jpg)

FIG. 5. Optical absorption spectra of ZnO 4-ML thin films close to threshold. Spectra have been convoluted with a 0.1-eV-wide Gaussian function. The red and black arrows mark the absorption threshold in the films and their respective bulks, respectively.

with the degree of hybridization of the $p_{z}$ orbitals with the $p_{x}$ and $p_{y}$ ones, discussed in Sec. IV A. It decreases in the series h-BN(0001), BCT(010), WUR(10$\overline{1}$0), CUB(100), ZB(110), which is consistent with the decrease of anisotropy of the optical dielectric constant displayed in Table IV.

The above discussion of threshold specific structures and anisotropy should be considered as only a preliminary attempt to characterize the film absorption spectra at low energy, before applying a more involved Bethe-Salpeter approach. Indeed, the present RPA+NLFE method neglects excitonic effects which are known to red-shift the absorption threshold and induce a redistribution of spectral weight at low energy, as shown, e.g., in Ref. [60] in the case of bulk ZnO. Nevertheless, while it likely predicts incorrect peak intensities and positions, the existence of transitions involving localized surface states and of absorption anisotropies consistent with the dangling bond orientation and the optical dielectric constant anisotropy (as shown in Table V) should remain qualitatively valid.

<table>
<caption>Table V. Correlation between the degree of hybridization of $p_{z}$ and $p_{x},p_{y}$ orbitals at the top of VB (measured by the dangling bond angle $\theta$), the energy difference $\Delta$ between the $z$ and $x,y$ first absorption peaks, and the anisotropy of the optical dielectric constant $\epsilon_{\infty}^{x,y}/\epsilon_{\infty}^{z}$.</caption>
<thead>
  <tr>
    <th> </th>
    <th>$\theta$ ($^\circ$)</th>
    <th>$\Delta$ (eV)</th>
    <th>$\epsilon_{\infty}^{x,y}/\epsilon_{\infty}^{z}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>h-BN(0001)</td>
    <td>0</td>
    <td>$-0.6$</td>
    <td>1.107</td>
  </tr>
  <tr>
    <td>BCT(010)</td>
    <td>6</td>
    <td>$-0.6$</td>
    <td>1.108</td>
  </tr>
  <tr>
    <td>WUR(10$\overline{1}$0)</td>
    <td>10</td>
    <td>$-0.4$</td>
    <td>1.107; 1.086</td>
  </tr>
  <tr>
    <td>CUB(100)</td>
    <td>12</td>
    <td>$-0.4$</td>
    <td>1.085</td>
  </tr>
  <tr>
    <td>ZB(110)</td>
    <td>28</td>
    <td>$-0.2$</td>
    <td>1.064; 1.043</td>
  </tr>
</tbody>
</table>

## VI. CONCLUSION

The present work, which relies on gradient-corrected and hybrid first-principles simulations, provides a complete characterization of the electronic properties of ZnO thin films with 4-ML thickness, cut along the BCT(010), CUB(100), h-BN(0001), ZB(110), WUR(10$\overline{1}$0), and (0001) orientations.

The modifications of the local densities of states have been described and analyzed in terms of the reduction of the Madelung potential on undercoordinated atoms and surface states/resonances appearing at the top of the VB and bottom of the CB. The gap width in the films is found to be larger than in the corresponding bulk, which is assigned to quantum confinement effects.

The components of the high-frequency dielectric constant have been determined. They are larger than their bulk counterparts and display a larger anisotropy. Finally, the absorption spectra of the films have been computed. They display specific features in an energy range just above threshold due to transitions from or to surface states/resonances.

This study provides a first understanding of finite-size effects on the electronic properties of ZnO thin films. Analysis of their thickness dependence is currently under progress in our group.

## ACKNOWLEDGMENT

We gratefully acknowledge generous allocations of computing time at at GENCI- [TGCC/CINES/IDRIS] under Project No. 100170.

[1] R. A. Powell, W. E. Spicer, and J. C. McMenamin, Phys. Rev. B 6, 3056 (1972).

[2] Ü. Özgür, Ya. I. Alivov, C. Liu, A. Teke, M. A. Reshchikov, S. Doğan, V. Avrutin, S.-J. Cho, and M. Morkoç, J. Appl. Phys. 98, 041301 (2005).

[3] C. Klingshirn, Phys. Status Solidi B 244, 3027 (2007).

[4] C. Klingshirn, J. Fallert, H. Zhou, J. Sartor, C. Thiele, F. Maier-Flaig, D. Schneider, and H. Kalt, Phys. Status Solidi B 247, 1424 (2010).

[5] A. Schleife, F. Fuchs, J. Furthmüller, and F. Bechstedt, Phys. Rev. B **73**, 245212 (2006).

[6] J. Carrasco, F. Illas, and S. T. Bromley, *Phys. Rev. Lett.* **99**, 235502 (2007).

[7] J. Wang, A. J. Kulkarni, K. Sarasamak, S. Limpijumnong, F. J. Ke, and M. Zhou, *Phys. Rev. B* **76**, 172103 (2007).

[8] C. R. A. Catlow, S. A. French, A. A. Sokol, A. A. Al-Sunaidi, and S. M. Woodley, *J. Comput. Chem.* **29**, 2234 (2008).

[9] S. Zhang, Y. Zhang, S. Huang, P. Wang, and H. Tian, *Chem. Phys. Lett.* **557**, 102 (2013).

[10] I. Demiroglu, S. Tosoni, F. Illas, and S. T. Bromley, *Nanoscale* **6**, 1181 (2014).

[11] D. Zagorac, J. C. Schön, J. Zagorac, and M. Jansen, *Phys. Rev. B* **89**, 075201 (2014).

[12] L. Sponza, J. Goniakowski, and C. Noguera, *Phys. Rev. B* **91**, 075126 (2015).

[13] Zhong Lin Wang, *J. Phys.: Condens. Matter* **16**, R829 (2004).

[14] J. Shen, H. Zhuang, D. Wang, C. Xue, and H. Liu, *Cryst. Growth Des.* **9**, 2187 (2009).

[15] M. Bitenc, G. Drazić, and Z. Crnjak-Orel, *Cryst. Growth Des.* **10**, 830 (2010).

[16] S. Xu and Z. L. Wang, *Nano Res.* **4**, 1013 (2011).

[17] H. Zhuang, J. Li, J. Wang, P. Xu, and N. An, *Mater. Charact.* **62**, 593 (2011).

[18] J. Li, H. Zhuang, J. Wang, and P. Xu, *Mater. Lett.* **65**, 1659 (2011).

[19] X. Han, X. Zhou, Y. Jiang, and Z. Xie, *J. Mater. Chem.* **22**, 10924 (2012).

[20] Y. F. Chen, H. J. Ko, S. K. Hong, and T. Yao, *Appl. Phys. Lett.* **76**, 559 (2000).

[21] S. K. Hong, T. Hanada, H. J. Ko, Y. F. Chen, T. Yao, D. Imai, K. Araki, M. Shinohara, K. Saitoh, and M. Terauchi, *Phys. Rev. B* **65**, 115331 (2002).

[22] T. P. Smith, W. J. Mecouch, P. Q. Miraglia, A. M. Roskowski, P. J. Hartlieb, and R. F. Davis, *J. Cryst. Growth* **257**, 255 (2003).

[23] T. Koyama and S. F. Chichibu, *J. Appl. Phys.* **95**, 7856 (2004).

[24] Q. Y. Xu, Y. Wang, X. L. Du, Q. K. Xue, and Z. Zhang, *Appl. Phys. Lett.* **84**, 2067 (2004).

[25] Y. Wang, X. L. Du, Z. X. Mei, Z. Q. Zeng, M. J. Ying, H. T. Yuan, J. F. Jia, Q. K. Xue, and Z. Zhang, *Appl. Phys. Lett.* **87**, 051901 (2005).

[26] C. Tusche, H. L. Meyerheim, and J. Kirschner, *Phys. Rev. Lett.* **99**, 026102 (2007).

[27] G. Weirum, G. Barcaro, A. Fortunelli, F. Weber, R. Schennach, S. Surnev, and F. P. Netzer, *J. Phys. Chem. C* **114**, 15432 (2010).

[28] D. Kato, T. Matsui, and J. Yuhara, *Surf. Sci.* **604**, 1283 (2010).

[29] M. S. Xue, W. Li, F. J. Wang, J. S. Lu, and J. P. Yao, *J. Alloys Compd.* **502**, 127 (2010).

[30] R. Schennach, F. Weber, M. Piffl, G. Weirum, and S. Surnev, *Surf. Eng.* **28**, 87 (2012).

[31] F. Claeyssens, C. L. Freeman, N. L. Allan, Y. Sun, M. N. R. Ashfold, and J. H. Harding, *J. Mater. Chem.* **15**, 139 (2005).

[32] C. L. Freeman, F. Claeyssens, N. L. Allan, and J. H. Harding, *Phys. Rev. Lett.* **96**, 066102 (2006).

[33] Benjamin J. Morgan, *Phys. Rev. B* **80**, 174105 (2009).

[34] I. Demiroglu and S. T. Bromley, *Phys. Rev. Lett.* **110**, 245501 (2013).

[35] P. E. Blochl, *Phys. Rev. B* **50**, 17953 (1994).

[36] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[37] G. Kresse and J. Furthmüller, *Comput. Mat. Sci.* **6**, 15 (1996).

[38] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996); **78**, 1396 (1997).

[39] V. I. Anisimov, F. Aryasetiawan, and A. I. Lichtenstein, *J. Phys.: Condens. Matter* **9**, 767 (1997).

[40] As in Ref. [34], a single monolayer (1 ML) is defined as the minimal thickness for which all atoms are connected. It corresponds to a bilayer in Refs. [31,32,33].

[41] G. Onida, L. Reining, and A. Rubio, *Rev. Mod. Phys.* **74**, 601 (2002).

[42] S. L. Adler, *Phys. Rev.* **126**, 413 (1962).

[43] N. Wiser, *Phys. Rev.* **129**, 62 (1963).

[44] B. Meyer and D. Marx, *Phys. Rev. B* **67**, 035403 (2003).

[45] J. Goniakowski, C. Noguera, and L. Giordano, *Phys. Rev. Lett.* **98**, 205701 (2007).

[46] D. J. Chadi, *J. Vac. Sci. Technol.* **15**, 631 (1978).

[47] D. J. Chadi, *Phys. Rev. B* **19**, 2074 (1979).

[48] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.93.195435, for more information on first neighbor Zn-O distances (Table I) and LDOS at the top of the VB (Fig. 1).

[49] Average electrostatic potentials are evaluated by locating a test charge with norm unity at each ion core, as implemented in VASP [37].

[50] C. Noguera, *Physics and Chemistry at Oxide Surfaces* (Cambridge University press, Cambridge, 1996).

[51] C. Noguera, *Surf. Rev. Letters* **08**, 121 (2001).

[52] C. Noguera and J. Goniakowski, *J. Phys.: Condens. Matter* **20**, 264003 (2008).

[53] C. Noguera and J. Goniakowski, *Chem. Rev.* **113**, 4073 (2013).

[54] J. Goniakowski and C. Noguera, *C. R. Physics* **17**, 471 (2016).

[55] L. E. Brus, *J. Chem. Phys.* **79**, 5566 (1983).

[56] A. D. Yoffe, *Adv. Phys.* **42**, 173 (1993).

[57] Al. L. Efros and M. Rosen, *Phys. Rev. B* **58**, 7120 (1998).

[58] J. Wróbel, K. J. Kurzydlowski, K. Hummer, G. Kresse, and J. Piechota, *Phys. Rev. B* **80**, 155124 (2009).

[59] A. Schleife, C. Rödl, F. Fuchs, J. Furthmüller, and F. Bechstedt, *Phys. Rev. B* **80**, 035112 (2009).

[60] P. Gori, M. Rakel, C. Cobet, W. Richter, N. Esser, A. Hoffmann, R. Del Sole, A. Cricenti, and O. Pulci, *Phys. Rev. B* **81**, 125207 (2010).

[61] *Handbook of Condensed Matter and Materials Data*, edited by W. Martienssen and H. Warlimont (Springer-Verlag, Berlin, 2005).

[62] P. Cudazzo, I. V. Tokatly, and A. Rubio, *Phys. Rev. B* **84**, 085406 (2011).

[63] The anisotropy $\epsilon_\infty^x - \epsilon_\infty^y$ in the BCT(010) film is less than 0.01 and thus not visible in Table IV.