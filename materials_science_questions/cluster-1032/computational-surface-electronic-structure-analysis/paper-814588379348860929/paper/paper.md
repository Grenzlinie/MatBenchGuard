PHYSICAL REVIEW B 92, 165112 (2015)

# Spin-dependent properties and images of MnO, FeO, CoO, and NiO(001) surfaces

A. Schrön and F. Bechstedt

Institut für Festkörpertheorie und -optik, Friedrich-Schiller-Universität Jena, Max-Wien-Platz 1, 07743 Jena, Germany
(Received 30 March 2015; published 12 October 2015)

We investigate the nonpolar, cleavage (001)$(2\times1)$ surfaces of antiferromagnetic late transition-metal oxides by means of the density functional theory for non-collinear spins and including the spin-orbit interaction. The effects of strong Coulomb interaction among the localized transition-metal $3d$ electrons are described by an on-site Hubbard $U$ added to the exchange-correlation functional in the local-density approximation. This approach guarantees finite energy gaps also for FeO and CoO, although they are still underestimated. Besides a change in the geometry due to rumpling and relaxation, we find that the size and orientation of the surface magnetic moments are also influenced by the surface. Electronic surface states appear in the fundamental gap close to the edges of the projected bulk bands. Only in the NiO case does an empty, well-separated band of $e_g$-derived surface states occur in the fundamental gap. As a consequence the scanning tunneling microscopy (STM) images exhibit almost the bulk $1\times1$ translational symmetry. For ferromagnetic tips strong spin contrasts are observed in spin-polarized STM. As a consequence of the bulk antiferromagnetic ordering, mainly chain structures become visible, independent of the tunneling into empty states or out from filled ones. Clear chemical trends with the occupation of the $t_{2g}$-minority-spin channel states along the row MnO $\rightarrow$ NiO are observed and discussed.

DOI: 10.1103/PhysRevB.92.165112
PACS number(s): 68.35.B−, 68.37.Ef, 73.20.At, 75.30.Et

## I. INTRODUCTION

The control over magnetic ordering down to a single atomic magnet, such as a single atomic spin on a surface, is of great importance for modern spintronic devices. The delicate interaction, e.g., the exchange coupling, of a spin-polarized surface atom and its neighbors influences the structural and electronic properties of a magnetic surface. The interplay among charge, spin, and orbital degrees of freedom in strongly correlated electron systems provides new opportunities to produce emergent quantum states such as charge-orbital ordering, multiferroelectricity, and unconventional superconductivity. One important ingredient is the knowledge of the spin structure of a certain material. It may be detected by spin- and surface-sensitive probing techniques.

The surface signature of a magnetic material depends on its spin density. It may be detectable within a spin-polarized scanning tunneling experiment [1–3]. Indeed, the interaction of such a surface with a magnetic tip may give rise to images different from those measured by conventional scanning tunneling microscopy (STM). Ferromagnetic tips may simultaneously resolve the topographic and magnetic surface structure of a conducting magnetic material. However, not only spin-polarized STM (SP-STM) provides unprecedented insight into collinear and noncollinear spin structures at surfaces. Direct access to spin imaging with atomic resolution on insulating magnetic surfaces is achieved by detecting the short-range magnetic exchange interaction within a magnetic exchange force microscopy (MExFM) using ferromagnetic tips [3–5]. The performance of MExFM studies can be well understood in the framework of $ab$ initio calculated spin-dependent atomic forces [6,7].

Prototypical examples for studying spin phenomena with atomic resolution are the (001) cleavage surfaces of transition-metal (TM) oxides MnO, FeO, CoO, and NiO. They are antiferromagnetically ordered below Néel temperatures of 116, 198, 291, and 525 K, respectively [8]. The $\text{TM}^{2+}$ ions in almost-rocksalt lattices carry local magnetic moments which vary with the occupation of the minority-spin $t_{2g}$ states in the localized TM $3d$ shell with 0 ($\text{Mn}^{2+}$), 1 ($\text{Fe}^{2+}$), 2 ($\text{Co}^{2+}$), and 3 ($\text{Ni}^{2+}$) electrons. Their antiferromagnetic (AF) ordering in the [111] direction is due to the alternate arrangement of ferromagnetic (111) planes of $\text{TM}^{2+}$ ions with opposite spin orientation. It is clearly visible at the (001) surface as demonstrated by MExFM studies of NiO [4,5]. The magnetic interaction between the different (111) planes is mediated by oxygen $\text{O}^{2-}$ ions by a superexchange mechanism [9].

Despite intense research, at least on the NiO(001) surface, and the simplicity of the atomic structure of bulk TM monoxides with only slightly distorted rocksalt geometries [10], many surface properties are less known. This is especially surprising in light of the important role of TM oxide surfaces in heterogeneous catalysis [11] and the water-splitting activity of CoO nanoparticles [12]. (i) Even the atomic geometry of the surfaces is under debate. Data of low-energy electron diffraction (LEED) and medium-energy ion scattering (MEIS) studies seem to give contradicting results [13–16]. Only the simultaneous occurrence of surface rumpling and interlayer relaxation is consistent [17]. Also, theoretical studies of MnO(001) resulted in opposite values [14,18], whereas qualitative agreement can be stated for NiO(001) [19–21]. (ii) The amount of reliable information about the electronic structure of TM oxide (TMO) surfaces is relatively limited. X-ray photoelectron spectroscopy (XPS) and electron-energy-loss spectroscopy (EELS) measurements have provided little experimental information about surface states. The same holds for emission and absorption spectra and angle-resolved photoemission spectroscopy (ARPES) data, which are available mainly for NiO. Only the surface barrier of NiO, its ionization energy, is known [22]. However, some more indirect information has been derived from STM studies of NiO(001) [23,24]. (iii) For any magnetic material the breaking of symmetry and reduced coordination at the surface may cause a deviation of the magnetic state at the surface compared to

1098-0121/2015/92(16)/165112(11)
165112-1
©2015 American Physical Society

the bulk termination. The effect on cleaved NiO(001) surfaces seems to be negligible [25,26]. The results of spatially resolved polarization-dependent x-ray absorption spectroscopy or x-ray magnetic linear dichroism are, however, difficult to interpret because of the domain structure of the surfaces.

The aim of the present paper is fourfold: (i) The interplay of magnetic ordering and relaxed atomic structure is inves- tigated, including the effect of spin-orbit interaction (SOI) and hence the noncollinearity of the $TM^{2+}$ spins. (ii) The surface influence on size and orientation of local magnetic moments is studied. (iii) The surface electronic structure is discussed versus the wave vector, layer contribution, and orbital character. The consequences for (SP-)STM images are demonstrated. (iv) Chemical trends are discussed, especially with respect to the partial filling of the $t_{2g}$ states in the minority-spin channel of a $TM^{2+}$ ion.

## II. THEORETICAL AND NUMERICAL METHODS

### A. Surface modeling

We construct slabs with symmetry-equivalent surfaces with $2\times1$ lateral unit cells consisting of nine atomic (001) layers. Tests of convergence of the surface energy indicate that this number of layers is sufficient. The upper part of the slab is illustrated in Fig. 1. The slab symmetry is obvious since in the case of (001) surfaces of rocksalt crystals an irreducible slab consists of four atomic layers with equal numbers of cations and anions [27]. Due to the antiferromagnetic ordering the $p(2\times1)$ unit cell is spanned by primitive basis vectors $\mathbf{a}_{1}=a_{0}(1,1,0)$ and $\mathbf{a}_{2}=\frac{a_{0}}{2}(-1,1,0)$, where $a_{0}$ is the bulk cubic lattice constant. Deviations from the rocksalt geometry due to the magnetic ordering [10] are omitted. Each lateral unit cell contains two TM atoms with opposite spins belonging to adjacent (111) cation sheets.

![](./images/814588379348860929_1.jpg)

FIG. 1. (Color online) Illustration of the upper part of the or- thorhombic slab with a $p(2\times1)$ lateral unit cell (black dashed rectangle). Small black and red (large blue and green) spheres refer to $TM^{2+}(O^{2-})$ ions. The spin-up and -down arrangements on the TM $3d$ shell and the antiferromagnetic ordering are indicated by black and red arrows, respectively.

The material slabs are separated by vacuum with a thickness of $10\ \mathring{A}$. Consequently, the superlattices of repeated slabs plus vacuum possess a vertical lattice constant of about $26$–$27\ \mathring{A}$. The Brillouin zone (BZ) of the resulting artificial orthorhombic crystal is sampled by a $\Gamma$-centered $8\times4\times1$ Monkhorst-Pack mesh [28] to compute electron and magnetization densities as well as total energies.

### B. Description of exchange and correlation

Total energies are computed by means of the density functional theory [29] within the local-density approximation (LDA) [30] using the parametrization of Perdew and Zunger [31]. Spin-orbit interaction is taken into account [32]. The LDA has been chosen since the generalized gradient approximation (GGA) for exchange and correlation (XC) [30] leads to a remarkable quenching of the orbital magnetization [33]. All DFT calculations are performed using the Vienna $Ab$ initio Simulation Package (VASP) [34]. The TM $3d$, TM $4s$, O $2s$, and O $2p$ states are included in the description. The one-particle wave functions are expanded into a basis set of plane waves up to a cutoff energy of 750 eV. The projector-augmented wave (PAW) method [35] is applied to construct the pseudopotentials and describe the wave functions in the core regions with an accuracy comparable to all-electron calculations. The absolute total energies are converged down to deviations smaller than $10$ meV/f.u. The resulting bulk lattice constants $a_{0}$ are listed in Table I.

The localization of the TM $3d$ orbitals requires a further im- provement of the XC description. TM compounds experience a strong on-site Coulomb repulsion between the $3d$ electrons due to the narrow $d$-band widths, which is not correctly described in a spin-polarized DFT-LDA or -GGA treatment. This error can be partly corrected within the DFT+$U$ method, in which the LDA or GGA XC functional is corrected by a Hubbard Hamiltonian for the Coulomb repulsion and exchange interaction. For the present calculations we use the DFT+$U$ method proposed by Dudarev *et al.* [36], in which only

TABLE I. Bulk properties of transition-metal oxides derived within the LDA+$U$+SOI treatment with $U=4$ eV: cubic lattice constant $a_{0}$, total magnetic moment $\mu$, easy spin axis $\mathbf{e}_{S}$, and indirect and direct fundamental gaps $E_{\text{g}}^{\text{ind}}$ and $E_{\text{g}}^{\text{dir}}$, respectively.

<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>MnO</th>
    <th>FeO</th>
    <th>CoO</th>
    <th>NiO</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$a_{0}$ ($\mathring{A}$)</td>
    <td>4.37</td>
    <td>4.24</td>
    <td>4.15</td>
    <td>4.07</td>
  </tr>
  <tr>
    <td>$\mu$ ($\mu_{\text{B}}$)</td>
    <td>4.53</td>
    <td>4.34</td>
    <td>3.69</td>
    <td>1.71</td>
  </tr>
  <tr>
    <td>$\mathbf{e}_{S}$</td>
    <td>(111) plane</td>
    <td>[111]</td>
    <td>$\approx[\overline{1}\overline{1}\ 1.5]$, [$\overline{1}$10]</td>
    <td>(111) plane</td>
  </tr>
  <tr>
    <td>$E_{\text{g}}^{\text{ind}}$ (eV)</td>
    <td>1.9</td>
    <td>2.0</td>
    <td>2.1</td>
    <td>2.2</td>
  </tr>
  <tr>
    <td>$E_{\text{g}}^{\text{dir}}$ (eV)</td>
    <td>2.6</td>
    <td>2.6</td>
    <td>2.3</td>
    <td>2.7</td>
  </tr>
</tbody>
</table>

an effective interaction parameter $U$ representing repulsion and exchange appears. Many different values between $U=0$ and $U=8$ eV have been used in the literature to improve structural, energetic, magnetic, and electronic properties of the bulk TM oxides. Here, the $U$ value is fixed to $U=4$ eV for MnO, FeO, CoO, and NiO. The inclusion of such a $U$ parameter of about 4 eV guarantees the correct energetic order of the sixfold bonding coordination (rocksalt structure) versus the fourfold ones (wurtzite and zinc-blende structures) for antiferromagnetic MnO [37]. There is also a tendency toward an improvement of other ground-state properties, including magnetic moments [37–40]. The latter quantities are rather insensitive to variations of the $U$ parameter by $\pm 1$ eV.

The $U=4$ eV value is smaller than the choice of about $U=6$ or 7 eV suggested in other surface calculations for MnO [41] or NiO [23,42]. Despite the excellent results for ground-state properties and fundamental energy gaps of bulk TM oxides, they are questionable for a correct description of the electronic structure. Rödl *et al.* [38,39] compared band structures obtained within the GW quasiparticle approach as well as the GGA+$U$ treatment. They found that the ordering of the O $2p$- and TM $3d$-derived valence bands becomes incorrect for large $U$ values. In order to widely fit the quasiparticle band structures, smaller $U$ values have been applied. The gap opening toward quasiparticle and experimental values has been reached by an additional scissors shift [43]. Such a missing shift is obvious from the direct ($E_{\text{g}}^{\text{dir}}$) and indirect ($E_{\text{g}}^{\text{ind}}$) band gaps listed in Table I. The indirect- and direct-gap values derived from the Kohn-Sham eigenvalues [30] within the LDA+$U$ ($U=4$ eV) framework are 1–2 eV too small compared with experimental and quasiparticle values. As a consequence the gaps in Table I are calculated without quasiparticle corrections.

There is still another problem related to the DFT+$U$ approach, particularly for FeO and CoO with fractionally occupied $t_{2g}$ shells in the minority-spin channel. The incorrect prediction of a metallic ground state for FeO and CoO [44] is sometimes considered the most striking example of the failure of the conventional band theory [45]. Indeed, only if large $U$ values and a spontaneous symmetry break are taken into account is an insulating ground state found [38]. Here, due to the SOI inclusion the symmetry break is reached by the splitting of the $t_{2g}$ levels. In the following, we therefore apply the LDA+$U$+SOI treatment with a noncollinear spin description to compute surface properties of MnO, FeO, CoO, and NiO, despite the gap underestimation.

The limit of collinear spin densities requires that a common magnetization axis $\mathbf{e}_{\text{S}}=\mathbf{m}_{\text{S}}(\mathbf{x})/|\mathbf{m}_{\text{S}}(\mathbf{x})|$ exists for all space points $\mathbf{x}$, where $\mathbf{m}_{\text{S}}(\mathbf{x})$ is the spin-magnetization density. The integral over $\mathbf{m}_{\text{S}}(\mathbf{x})$ within a PAW sphere around a TM ion yields the spin-magnetic moment $\boxed{\mu}_{\text{S}}$ with magnitude $\mu_{\text{S}}$. Values for the total magnetic moment $\mu$ including the effect of the orbital magnetization are also listed in Table I together with the easy axis $\mathbf{e}_{\text{S}}$ or easy plane.

### C. Spin-polarized scanning tunneling microscopy

We assume that the TM oxide samples are doped, e.g., by lithium [24], to allow for electrical tunnel currents between metallic tip and back contact of the sample. Such a tunnel current $I(\mathbf{R}^{\text{t}})$ for a given position $\mathbf{R}^{\text{t}}$ of the tip apex atom is described within the Tersoff-Hamann approximation [46], which is based on the previous approach of Bardeen [47]. While the original Tersoff-Hamann treatment has been derived for non-spin-polarized systems, it can be generalized to a noncollinear spin-polarized surface (s) and a ferromagnetic tip (t) to [3]
$$
\begin{aligned}
I\left(\mathbf{R}^{\mathrm{t}}\right) \propto & \int d^{3} \mathbf{x} \int_{\varepsilon_{\mathrm{F}}}^{\varepsilon_{\mathrm{F}}+e U} d \varepsilon\left[n^{\mathrm{t}}\left(\mathbf{x}-\mathbf{R}^{\mathrm{t}}, \varepsilon_{\mathrm{F}}\right) n^{\mathrm{s}}(\mathbf{x}, \varepsilon)\right. \\
& \left.+\frac{1}{\mu_{\mathrm{B}}^{2}} \mathbf{m}_{\mathrm{S}}^{\mathrm{t}}\left(\mathbf{x}-\mathbf{R}^{\mathrm{t}}, \varepsilon_{\mathrm{F}}\right) \mathbf{m}_{\mathrm{S}}^{\mathrm{s}}(\mathbf{x}, \varepsilon)\right],
\end{aligned}
\tag{1}
$$
with the local density of states (LDOS)
$$
n^{\mathrm{t},\mathrm{s}}(\mathbf{x},\varepsilon)=\sum_{\substack{\mathbf{k},\nu\\s}}|\phi_{\mathbf{k}\nu}(\mathbf{x},s)|^{2}\delta(\varepsilon-\varepsilon_{\mathbf{k}\nu})
\tag{2}
$$
and the energy-resolved (spin) magnetization density
$$
\mathbf{m}_{\mathrm{S}}^{\mathrm{t},\mathrm{s}}(\mathbf{x},\varepsilon)=-\mu_{\mathrm{B}} \sum_{\substack{\mathbf{k},\nu\\s,s^{\prime}}} \phi_{\mathbf{k}\nu}^{*}(\mathbf{x},s) \boldsymbol{\sigma}_{ss^{\prime}} \phi_{\mathbf{k}\nu}(\mathbf{x},s^{\prime}) \delta(\varepsilon-\varepsilon_{\mathbf{k}\nu}). \quad (3)
$$

Here, $\varepsilon_{\text{F}}$ denotes the Fermi energy, $U$ is the applied tunnel bias, and $\boldsymbol{\sigma}_{ss^{\prime}}$ is the vector of the Pauli spin matrices. The Pauli spinors $\phi_{\mathbf{k}\nu}(\mathbf{x},s)$ and eigenvalues $\varepsilon_{\mathbf{k}\nu}$ are taken from the corresponding Kohn-Sham equations [30].

We assume further that electronic states of the tip are completely spin polarized at the Fermi energy with the magnetic axis parallel to the direction $\mathbf{e}^{\text{t}}=\mathbf{m}_{\text{S}}^{\text{t}}/|\mathbf{m}_{\text{S}}^{\text{t}}|$. It holds then $\mathbf{m}_{\text{S}}^{\text{t}}(\mathbf{x}-\mathbf{R}^{\text{t}},\varepsilon_{\text{F}})=\mu_{\text{B}}n^{\text{t}}(\mathbf{x}-\mathbf{R}^{\text{t}},\varepsilon_{\text{F}})\mathbf{e}^{\text{t}}$, and thus,
$$
\begin{aligned}
I(\mathbf{R}^{\mathrm{t}}) \propto & \int d^{3} \mathbf{x} n^{\mathrm{t}}\left(\mathbf{x}-\mathbf{R}^{\mathrm{t}}, \varepsilon_{\mathrm{F}}\right) \\
& \quad \times \int_{\varepsilon_{\mathrm{F}}}^{\varepsilon_{\mathrm{F}}+e U} d \varepsilon\left[n^{\mathrm{s}}(\mathbf{x}, \varepsilon)-\frac{1}{\mu_{\mathrm{B}}} \mathbf{e}^{\mathrm{t}} \mathbf{m}_{\mathrm{S}}^{\mathrm{s}}(\mathbf{x}, \varepsilon)\right].
\end{aligned}
\tag{4}
$$

Finally, the finite extent of the tunnel tip has to be taken into account. In practice, we assume that the local density of states of the tip apex $n^{\text{t}}(\mathbf{x}-\mathbf{R}^{\text{t}},\varepsilon_{\text{F}})$ can be described by a Gaussian shape [3,48,49].

## III. STRUCTURAL AND MAGNETIC PROPERTIES

### A. Rumpling and relaxation

The rumpling $R_{i}$ and relaxation $L_{i,i+1}$ of the layers $i=1$ and 2 forming the TMO(001)$(2 \times 1)$ surface of a transition-metal oxide with antiferromagnetic ordering AFII are determined after optimization of the atomic positions compared to the bulk ones. The results are summarized in Table II. For deeper layers the surface-induced atomic displacements are negligible. The calculated rumpling of the surface layer is small, of the order of $R_{1} \approx 1\%$–$2\%$, whereas the rumpling of the first subsurface layer, $R_{2} \lesssim -1\%$, shows the opposite sign. The opposite sign means that the $\text{O}^{2-}$ ions in the surface layer together with the underlying $\text{TM}^{2+}$ ions in the first subsurface layer are displaced toward the vacuum, whereas the $\text{TM}^{2+}$ ions in the surface layer together with the $\text{O}^{2-}$ ones in the first subsurface exhibit displacements in the opposite direction. On average, the surface layer is moved

<table><caption>TABLE II. Rumpling $R_i$ and interlayer relaxation $L_{i,i+1}$ for the first layers ($i=1,2$) closest to the surface compared with results of two different experimental methods, MEIS and LEED.</caption>
<tbody><tr><td></td><td></td><td>MnO</td><td>FeO</td><td>CoO</td><td>NiO</td></tr>
<tr><td>$R_1$ (%)</td><td>LDA+$U$</td><td>1.1</td><td>1.8</td><td>1.4</td><td>0.9</td></tr>
<tr><td></td><td>MEIS</td><td>$-3.6\pm0.7$ [14]</td><td></td><td></td><td>$-4.8\pm0.5$ [16]</td></tr>
<tr><td></td><td>LEED</td><td>$4.2\pm1.6$ [13]</td><td>$3.9\pm3.2$ [50]</td><td>$2.8\pm1.9$ [17]</td><td>$2.4\pm2.4$ [51]</td></tr>
<tr><td></td><td></td><td>$5.5\pm2.5$ [13]</td><td></td><td></td><td>0 to $-2$ [15]</td></tr>
<tr><td>$R_2$ (%)</td><td>LDA+$U$</td><td>$-0.4$</td><td>$-0.9$</td><td>$-0.8$</td><td>$-0.8$</td></tr>
<tr><td></td><td>MEIS</td><td>$-2.0\pm0.7$ [14]</td><td></td><td></td><td></td></tr>
<tr><td></td><td>LEED</td><td>$0.2\pm1.6$ [13]</td><td></td><td>0.0 [17]</td><td>$1.5\pm2.4$ [51]</td></tr>
<tr><td></td><td></td><td>$0.6\pm2.5$ [13]</td><td></td><td></td><td></td></tr>
<tr><td>$L_{1,2}$ (%)</td><td>LDA+$U$</td><td>$-0.8$</td><td>$-0.2$</td><td>$-0.3$</td><td>$-1.2$</td></tr>
<tr><td></td><td>MEIS</td><td>$0.1\pm0.7$ [14]</td><td></td><td></td><td>$-1.4\pm0.1$ [16]</td></tr>
<tr><td></td><td>LEED</td><td>$0.0\pm1.6$ [13]</td><td>$-2.4\pm4.6$ [50]</td><td>$5.7\pm1.9$ [17]</td><td>$-2$ to $-3$ [15]</td></tr>
<tr><td></td><td></td><td>$1.1\pm2.5$ [13]</td><td></td><td></td><td></td></tr>
<tr><td>$L_{2,3}$ (%)</td><td>LDA+$U$</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.0</td></tr>
<tr><td></td><td>MEIS</td><td>$-1.0\pm0.7$ [14]</td><td></td><td></td><td></td></tr>
<tr><td></td><td>LEED</td><td></td><td>$-3.2\pm4.8$ [50]</td><td>$2.3\pm1.9$ [17]</td><td></td></tr>
</tbody></table>

toward the subsurface one, resulting in a negative interlayer relaxation $L_{1,2}$. The corresponding effect $L_{2,3}$ on the next layers already vanishes. For MnO and NiO these results are in good agreement with other LDA+$U$ or GGA+$U$ calculations [18,19,41]. For FeO and CoO such studies are not available.

Measurements employing medium-energy ion scattering predict a negative rumpling of the surface layer for MnO and NiO, in contrast to the DFT+$U$ computations. In the case of MEIS studies of MnO [14] the sign of $R_2$ is in agreement with the theoretical prediction in Table II. The qualitative agreement of DFT+$U$ theory and LEED experiments is, in general, better. This is obvious for the $R_1$ results from measurements of all TMOs studied here [13,17,50,51]. In the case of the other quantities, $R_2$, $L_{1,2}$, and $L_{2,3}$, the deviations between theory and experiment are considerable. The reasons for the deviations between theory and experiment are still not clear. Some measurements [13,17,50,51] have been performed with thin or ultrathin TMO layers grown pseudomorphically on Ag(001) substrates. However, the quality of the bulk samples and of their cleavage may also be under discussion. Another problem is that the majority of studies have been conducted at room temperature, i.e., for the paramagnetic phase of MnO, FeO, and CoO instead of the antiferromagnetic one studied here.

### B. Energetic and magnetic properties

The surface energy $\gamma$ is minimized for the nine-layer slab including the surface-induced modifications of the orientation and magnitude of the magnetic moments. The results are summarized in Table III. The general chemical trend of the surface energies to increase along the series MnO, FeO, CoO, and NiO is not modified due to the XC functional used, the surface atomic relaxation, and the modification of the surface spins compared to previous collinear calculations for MnO and NiO [33]. Only the absolute values are slightly increased due to the use of the LDA XC functional.

The precise values of the surface magnetic moments influence the surface energetics only slightly. They are, however, difficult to derive and interpret due to the differences found for the bulk TMOs [10] (see Table I). For FeO with an important SOI a unique easy axis along [111] is obtained and also chosen as the starting point of the self-consistent surface calculations. However, in the case of bulk CoO the energetically most favorable orientation of the local magnetic moments along $[\overline{1}\overline{1}1.5]$ is threefold degenerate. At the surface this degeneracy is partially lifted. A nondegenerate $[\overline{1}\overline{1}1.5]$ orientation and a twofold-degenerate $[1.5\overline{1}\overline{1}]$ one result. In bulk CoO another orientation along $[\overline{1}10]$ is only $70\ \mu$eV/f.u. higher in energy. This axis is also threefold degenerate and splits into a nondegenerate $[\overline{1}10]$ orientation and a twofold-degenerate $[0\overline{1}1]$ orientation at the surface. Consequently, four nonequivalent magnetic orientations along $[\overline{1}\overline{1}1.5]$, $[1.5\overline{1}\overline{1}]$, $[\overline{1}10]$, and $[0\overline{1}1]$ have been considered as starting points for CoO(001) surface calculations. No significant magnetic anisotropy is obtained due to SOI for MnO and NiO. The inclusion of the Breit interaction leads to an easy (111) plane. Therefore, the nine orientations parallel to the [100], [110], $[\overline{1}10]$, [111], $[\overline{1}\overline{1}1]$, $[\overline{1}1\overline{1}]$, [101], $[0\overline{1}1]$, and [001] directions have been applied as starting points.

<table><caption>TABLE III. Surface energy $\gamma$ and directions of the local magnetic moments $\mathbf{e}_s^i$ in the surface layer $i=1$ and the first two subsurface layers $i=2,3$ and the change in the absolute value of the total magnetic moment of first-layer TM$^{2+}$ ions compared to the bulk value.</caption>
<tbody><tr><td></td><td>MnO</td><td>FeO</td><td>CoO</td><td>NiO</td></tr>
<tr><td>$\gamma$ (meV/Å$^2$)</td><td>59.4</td><td>65.3</td><td>71.3</td><td>80.4</td></tr>
<tr><td>$\mathbf{e}_s^1$</td><td></td><td>[1 1 2.5]</td><td>$[\overline{1}10]$</td><td>$[\overline{1}10]$</td></tr>
<tr><td>$\mathbf{e}_s^2$</td><td></td><td>[1 1 1.3]</td><td>$[\overline{1}10]$</td><td>$[\overline{1}10]$</td></tr>
<tr><td>$\mathbf{e}_s^3$</td><td></td><td>[1 1 1.3]</td><td>$[\overline{1}10]$</td><td>$[\overline{1}10]$</td></tr>
<tr><td>$\Delta\mu_1$ (units of $\mu_{\text{B}}$)</td><td>0.00</td><td>0.08</td><td>0.02</td><td>0.12</td></tr>
<tr><td></td><td></td><td></td><td>$-0.28$</td><td>0.02</td></tr>
</tbody></table>

![](./images/814588379348860929_2.jpg)

FIG. 2. (Color online) (left) Minority spin density and orientation of spin-magnetization density for (a) FeO and (b) CoO(001)($2 \times$ 1) surfaces. The antiferromagnetic ordering is indicated by black and red lines and arrows. (right) Surface-induced rotation of total magnetic moments of TM$^{2+}$ ions relative to the easy axis of bulk (a) FeO and (b) CoO.

The results are summarized in Table III and Figs. 2 and 3. While for MnO and NiO the energetically most favorable orientations of the local magnetic moments are collinearly aligned in the entire slab, the same result is obtained for the [$\bar{1}$10] orientation in CoO. In order to quantify the non-collinearity with respect to a certain direction $\mathbf{e}_S$, we introduce the deviation angle $\Delta\alpha_{\mathbf{e}_S} = |\arccos(\mathbf{e}_S' \cdot \mathbf{e}_S/|\mathbf{e}_S||\mathbf{e}_S'|)|$, where $\mathbf{e}_S$ is the initial orientation of the magnetic moments and $\mathbf{e}_S'$ is the rotated one. Starting from the easy axis along [$\bar{1}\bar{1}1.5$] in CoO, the magnetic moments in the surface layer become noncollinear with respect to the inner layers. A rotation $\Delta\alpha_{[\bar{1}\bar{1}1.5]}$ of about $9^\circ$ toward the (001) plane is observed for the magnetic moments in the surface layer, whereas those in the inner layers are only slightly rotated toward the (001) plane by $0^\circ$-$2^\circ$ [see Fig. 2(b)]. The small rotation of the magnetic moments in the inner layers compared to the actual bulk easy axis can be attributed to the finite slab size and is a consequence of the interplay of three driving forces: (i) the rotation of the magnetic moments in the surface layer toward the (001) plane, (ii) the rotation of the magnetic moments in the inner layers toward the bulk easy axis, and (iii) the coupling of (i) and (ii) by the antiferromagnetic ordering, for which the energy is lowest if the magnetic moments between surface and inner layers are aligned parallel or antiparallel. Among the four starting orientations for CoO, the energetically most favorable solution (by $1\ \text{meV}/\mathring{\text{A}}^2$) is [$\bar{1}$10], in contrast to the finding for the bulk, where [$\bar{1}\bar{1}1.5$] is lowest in energy. The minor discrepancy from the bulk findings may be considered an artifact of the slab approach. Also, in the uppermost atomic layer of the FeO(001)($2 \times 1$) surface the magnetic moments become noncollinear with respect to their orientation in the inner layers. In contrast to CoO, however, the rotation of the magnetic moments at the FeO surface is toward the [001] direction, i.e., the surface normal as given in Table III and Fig. 2(a). The magnetic moments in the surface layer rotate away from the bulk easy axis by $\Delta\alpha_{[111]} \approx 25^\circ$, whereas those in the inner layers rotate by $4^\circ$-$8^\circ$. Thus, the noncollinearity is much stronger for the FeO surface than for CoO, and due to the coupling via the antiferromagnetic ordering, the rotation of the magnetic moments in the inner layers away from the bulk easy axis is also stronger compared to that of CoO. We remember that such a surface canting of Fe magnetic moments has also been observed for $\text{Fe}_3\text{O}_4$ nano-particles [52].

The surface influences not only the orientation of the magnetic moments for FeO, CoO, and NiO but also their absolute magnitude, as illustrated in Table III and Fig. 3. However, in terms of the absolute values (see Table I) the modifications in the first atomic layer of the surfaces remain small. Only for CoO and NiO may the modifications be

![](./images/814588379348860929_3.jpg)

FIG. 3. (Color online) Magnitude change of total magnetic moment of TM$^{2+}$ ions near the (001) surface of (a) FeO, (b) CoO, and (c) NiO. For CoO and NiO the calculations started from two different orientations.

measurable. Figure 3(b) shows that the resulting magnetic
moments differ less than $0.03\mu_{\mathrm{B}}$ from the bulk value if
the $[\overline{1}10]$ orientation is the starting point for the surface
relaxation. In contrast, for the $[\overline{1}\overline{1}1.5]$ starting point the total
magnetic moment of the $\mathrm{Co}^{2+}$ ions in the surface layer is
quenched by almost $0.3\mu_{\mathrm{B}}$. This quenching is almost solely
due to a quenching of the orbital contribution, which in
turn is a consequence of a redistribution of the minority-
spin density toward the vacuum. For this starting point, the
local magnetic spin moments become noncollinear [shown
in Fig. 2(b)]. This noncollinearity reduces the superexchange
that stabilizes the antiferromagnetic ordering and explains
why this starting point is less favorable for the nine-layer
slab than the $[\overline{1}10]$ orientation. In the $\mathrm{NiO}(001)(2 \times 1)$ case,
the magnetic moments are slightly increased by more than
$0.1\mu_{\mathrm{B}}$ for magnetic orientations aligned within the (001)
layer by SOI, e.g., the [110] orientation (see Table III). As
a consequence, the easy (001) plane is stabilized due to the
surface. Altogether, for NiO the surface-induced changes are
relatively small, so that the conclusion "that the magnetic
surface structure of a cleaved crystal is bulk-terminated" [25]
is reasonable.

## IV. ELECTRONIC PROPERTIES

### A. Surface bands and states

Surface electronic bands within the fundamental gap or the
pockets of the bulk conduction or valence bands are indicated
in Fig. 4 by comparison of slab bands with the projected
bulk band structure. Their identification is supported by a
comparison of the bulk DOS with that of the first atomic layer
of the slabs. Occupied surface bands in the fundamental gap
close to the top of the valence bands are hardly observable.
Only for NiO can such a surface band built mainly by $t_{2g}$
states of the minority-spin channel be identified in the entire
surface BZ. However, such bands appear in the pockets of the
projected band structure of MnO and FeO slightly below the
valence-band maximum (VBM). They are composed of TM $3d$
and O $2p$ states and appear between TM $3d$ $t_{2g}$- and $e_{g}$-derived
valence bands of the majority-spin channel (for MnO around
1.5 eV, for FeO around 2 eV below the VBM) or majority-spin
$e_{g}$-derived and minority-spin $t_{2g}$-derived valence bands (only
for FeO around 0.5 eV below the VBM).

In the MnO case [see Fig. 4(a)], empty surface bands related
to $t_{2g}$ states of the minority-spin channel appear in the center of

![](./images/814588379348860929_4.jpg)

FIG. 4. (Color online) Electronic structure of (a) MnO, (b) FeO, (c) CoO, and (d) $\mathrm{NiO}(001)(2 \times 1)$ surface represented by the bands (blue
lines) of the nine-layer slab and the projected bulk band structure (gray shaded areas). The density of states (DOS) projected onto the surface
atoms (blue line) is compared with the bulk DOS (in arbitrary units). The plane-averaged electrostatic potentials are used for the energy
alignment. Red (green) dots at the $M$ point indicate strong contributions of $d_{3r^{2}-z^{2}}$ ($d_{x^{2}-y^{2}}$), i.e., $e_{g}$-states, whereas strong contributions of $t_{2g}$
are indicated with black dots.

the BZ but almost disappear near its boundary. In contrast to the $e_g$-derived surface bands (see below) the $t_{2g}$-derived ones are generally represented by linear combinations of the three basis functions $d_{xy}$, $d_{zx}$, and $d_{yz}$, whose contribution varies with the Bloch wave vector. Such $t_{2g}$ states, but in the entire BZ, lead to the lowest empty surface bands of FeO and CoO. For NiO all $t_{2g}$ states are occupied. As a consequence, the lowest-energy surface band just below the conduction-band minimum (CBM) of the bulk-projected bands is built by $e_g(d_{3r^2-z^2})$ states. It is not only visible in Fig. 4(d) but has also been derived in other LDA+$U$ calculations [42]. This band shifts down in energy from FeO via CoO to NiO, in agreement with the filling of the $t_{2g}$ minority-spin channel. Consequently, empty surface bands derived from $e_g(d_{x^2-y^2})$ states appear in the pockets of the projected conduction bands for FeO and CoO.

### B. Spin-polarized STM images

For an antiferromagnetic ordering the local spin polarization is not visible in the band structure or the DOS. The bulk bands are always twofold degenerate because of the symmetry between the TM$^{2+}$ ions with opposite spins. The investigation of antiferromagnetic surfaces requires experimental techniques which provide information at a length scale smaller than the magnetic unit cell to resolve the two spin sublattices. Such a method is scanning tunneling microscopy with a ferromagnetic tip [3]. Besides the electronic fingerprint of the surface the local spin polarization or magnetization may be detected. Indeed, according to (1) and (4) the tunnel current is determined not only by the LDOS $n^s({\bf r},\varepsilon)$ but also by the corresponding magnetic quantity ${\bf m}^s({\bf r},\varepsilon)$. Therefore, the influence of the latter contribution depends on the relative orientation between the tip magnetization and the local magnetization of the surface atoms.

For MnO, FeO, CoO, and NiO(001)$(2\times1)$ surfaces, resulting (SP-)STM images are depicted in Figs. 5–8, respectively. Results for both a nonmagnetic tip, i.e., vanishing spin contrast, and a fully spin-polarized tip aligned parallel to the easy axis of the surface magnetization, i.e., maximum spin contrast, are presented for positive and negative bias voltages. The energy intervals given in Figs. 5–8 refer to the CBM for the images of the empty states and the VBM for the images of the filled states. They do not refer to the true bias voltages. The position of the Fermi level of, e.g., a doped transition-metal oxide with a true quasiparticle gap (which is larger than the values in Table I) has to be added. The main message from the images of the four TMO(001)$(2\times1)$ surfaces is the appearance of a clear spin contrast between the TM$\uparrow$ and TM$\downarrow$ ions and, in some cases, also between the two inequivalent O ions in a unit cell. In general, if mainly TM $3d$ states are detected, well-pronounced chains along $[1\overline{1}0]$ are observed. Only if TM $4s$ states in the empty-state images of MnO(001)$(2\times1)$ (see Fig. 5) appear are the chains somewhat weakened because the TM $4s$ states of both spin channels are empty, and thus, no spin polarization is present. As a consequence, the filling of the $t_{2g}$ shell in the minority-spin channel along the row Mn$^{2+}$, Fe$^{2+}$, Co$^{2+}$, and Ni$^{2+}$ dominates the corrugation measured in the empty-state images for a given bias voltage of about $E_g/2=1$ eV. The trends in the filled-state images are more difficult to interpret. The valence-state images depend strongly on three competing contributions: (i) the successive filling of the minority-spin TM $3d$ $t_{2g}$ shell (as in the empty-state ones), (ii) the relative energy of the TM $3d$ $e_g$-derived bands in the majority-spin channel and the TM $3d$ $t_{2g}$-derived bands in the minority-spin channel, and (iii) the hybridization with O $2p$ states.

![](./images/814588379348860929_5.jpg)

FIG. 5. (Color online) Calculated (left) STM and (right) SP-STM images of the (001)$(2\times1)$ surface of antiferromagnetic MnO. In the right panels the tip magnetization is chosen parallel to the surface magnetic moments along the [111] direction. Black (red) spheres indicate TM$\uparrow$ (TM$\downarrow$) ions, and blue (green) spheres describe O$\uparrow$ (O$\downarrow$). The bias voltage for (top) empty-state and (bottom) filled-state images. They refer to the conduction-band minimum and valence-band maximum, respectively. The different colors indicate different corrugation heights (C.H.) of the surface.

In the STM image of MnO(001) in Fig. 5, the O$^{2+}$ ions appear as bright spots for an integration interval of $-0.8$ eV

![](./images/814588379348860929_6.jpg)

FIG. 6. (Color online) As in Fig. 5, but for FeO. The tip magnetization in the right panels is chosen parallel to the magnetic moments of the Fe surface atoms along [1 1 2.3].

below the VBM, whereas the $Mn^{2+}$ ions are only slightly visible. This situation is reversed if the integration interval is extended to $-1.6$ eV below the VBM, where the $Mn^{2+}$ ions dominate. This inversion of contrast is obtained because at the surface the Mn $3d_{3r^{2}-z^{2}}$-derived states are reduced by approximately 1 eV, which does not hold for the Mn $3d_{x^{2}-y^{2}}$- and O $2p$-derived ones. Therefore, mostly the O $2p_{z}$-derived states which extend toward the vacuum are visible if the smaller integration interval is used, while in the larger integration interval the Mn $3d_{3r^{2}-z^{2}}$-derived states dominate. The same trend is also observed in the SP-STM images. However, more important is the finding that spin contrast is observed not only between the $Mn^{2+}$ ions but also between the $O^{2-}$ ions, which themselves are nonmagnetic. The spin contrast between the

![](./images/814588379348860929_7.jpg)

FIG. 7. (Color online) As in Fig. 5, but for CoO. The tip magnetization in the right panels is chosen parallel to the magnetic moments of the Co surface atoms along $[1\overline{1}0]$. The inset shows experimental data [24] taken at a bias voltage of $+2.7$ V. The average corrugation in the measured images is 1 pm.

![](./images/814588379348860929_8.jpg)

FIG. 8. (Color online) As in Fig. 5, but for NiO. The tip magnetization is chosen parallel to $[1\overline{1}0]$. The insets depict experimental data [24] at the same bias voltage. The average corrugation in the measured images is 30 pm (15 pm) at $+1.1\ \text{V}$ ($-1.5\ \text{V}$).

$\text{Mn}^{2+}$ ions is easily explained. If the magnetic moments of the $\text{Mn}^{2+}$ ions and the tip are parallel, tunneling is allowed, whereas tunneling is forbidden if the magnetic moments are antiparallel. In order to explain the spin contrast between the $\text{O}^{2-}$ ions, the superexchange mechanism must be considered. It leads to an asymmetry in the spin-resolved LDOS in the vicinity of the $\text{O}^{2-}$ ions at the surface [15], even though the total magnetization vanishes. If the magnetic moment of the $\text{Mn}^{2+}$ ion below an $\text{O}^{2-}$ ion is parallel to the magnetic moment of the tip, the tunneling current becomes large above the respective $\text{O}^{2-}$ ion, and it appears as a bright spot. The opposite holds if the magnetic moments of the tip and the $\text{Mn}^{2+}$ ion below the $\text{O}^{2-}$ ion is aligned antiparallel.

For the $\text{FeO}(001)$ surface, the $\text{Fe}^{2+}$ ions are clearly visible in the STM images of the filled states in Fig. 6. Also in the SP-STM images a strong spin contrast is observed if an integration interval of $-1\ \text{eV}$ below the VBM is used. In contrast to MnO, it is not the $\text{Fe}^{2+}$ ions with magnetic moments parallel to the magnetic moment of the tip that appear as bright spots in the SP-STM image but the ones aligned antiparallel to the magnetic moment of the tip. The uppermost valence bands in FeO are almost completely derived from minority-spin Fe $3d\ t_{2g}$ states. Therefore, only if the magnetic moments of the tip and the $\text{Fe}^{2+}$ ion in the surface are antiparallel can tunneling from the minority-spin $t_{2g}$ state into the tip occur. If the integration interval is increased to $-2\ \text{eV}$ below the VBM, contributions from the O $2p$ and the majority-spin Fe $3d\ e_{g}$ states are also taken into account. Consequently, the $\text{O}^{2-}$ ions also appear in the STM image, and the spin contrast between the $\text{Fe}^{2+}$ ions is reduced in the SP-STM image.

In the STM images of the filled states at the $\text{CoO}(001)$ surface plotted in Fig. 7, the $\text{Co}^{2+}$ ions as well as $\text{O}^{2-}$ ions appear with similar strength for an integration interval of $-1\ \text{eV}$ below the VBM. If the integration interval is increased to $-2\ \text{eV}$ below the VBM, the $\text{Co}^{2+}$ ions dominate the corresponding STM image, and the $\text{O}^{2-}$ ions are less clearly visible. Above the $\text{Co}^{2+}$ ions, tunneling occurs mostly from the minority-spin $t_{2g}$ states in the smaller integration interval. For the larger integration interval tunneling from the majority-spin $e_{g}$ states, especially the $d_{3r^{2}-z^{2}}$ state, also becomes important. Consequently, in the SP-STM image obtained for integration down to $-1\ \text{eV}$ below the VBM, the $\text{Co}^{2+}$ ions with magnetic moments aligned antiparallel to the magnetic moment of the tip are clearly visible as bright spots, whereas the $\text{Co}^{2+}$ ions with parallel orientation are not visible at all. In the SP-STM image obtained for the larger integration interval down to $-2\ \text{eV}$ below the VBM, on the other hand, the spin contrast between the parallel and antiparallel aligned $\text{Co}^{2+}$ ions is significantly reduced due to the tunneling from the majority-spin $d_{3r^{2}-z^{2}}$ states. CoO is, besides NiO, the only TMO for which STM experiments have been performed, to our knowledge. The agreement of the measured empty-state STM image obtained by Castell *et al.* [24] with the STM images calculated for two integration intervals of $+1$ and $+3\ \text{eV}$ above the CBM is excellent. We emphasize again that the bias voltage of $2.7\ \text{V}$ used by Castell *et al.* cannot be related directly to the integration interval used for the calculation of our (SP-)STM images. However, because the lowest conduction bands are almost completely derived from $\text{TM}^{2+}$ states, the actual integration interval plays only a minor role.

The STM image in Fig. 8 obtained for the occupied states at the $\text{NiO}(001)$ surface in an integration interval of $-0.75\ \text{eV}$ below the VBM is very similar to the one obtained for the $\text{MnO}(001)$ surface and an integration interval of $-0.8\ \text{eV}$ below the VBM in Fig. 5. The $\text{O}^{2-}$ ions appear as bright spots in the STM image as well as the SP-STM image. However, while the $\text{Mn}^{2+}$ ions show a very strong spin contrast in the corresponding SP-STM image, the $\text{Ni}^{2+}$ ions show almost no spin contrast. For NiO the uppermost valence bands are mostly determined by majority-spin $e_{g}$ states as well as minority-spin $t_{2g}$ states. Both contributions are of approximately the same magnitude in the integration interval of $-0.75\ \text{eV}$ below the VBM. If the integration interval is increased to $-1.5\ \text{eV}$

below the VBM, the $Ni^{2+}$ ions with magnetic moments aligned antiparallel to the tip magnetization become visible in the SP-STM image due to stronger tunneling from the minority-spin $t_{2g}$ states. Therefore, the spin contrast between the $Ni^{2+}$ ions is also increased. Comparing the STM images of the lowest conduction bands measured by Dudarev *et al.* [23] with the corresponding images in Fig. 8, we again obtain excellent qualitative agreement.

## V. SUMMARY AND CONCLUSIONS

In this paper we have studied the structural, energetic, electronic, and magnetic properties of the TMO(001) surfaces (TM = Mn, Fe, Co, Ni) in a DFT framework using an LDA+$U$ XC functional, applying the repeated slab approach, and including SOI. The structural modifications of the bulk geometry due to the surface and the antiferromagnetic ordering are small. This makes a comparison with experimental data difficult. While the LEED results are almost in qualitative agreement with the calculations, a clear contradiction to the atomic displacements measured in MEIS has to be stated. Not only the structural changes but also the surface influence on the magnitude of the magnetic moments are small. Nevertheless, a weak tendency for their rotation away from the bulk easy axis toward the surface normal (FeO) or the surface plane (CoO) is found.

Well-pronounced surface states are hardly visible in the fundamental gap of a TMO. Occupied bands related to surface states mainly appear in pockets close to the bulk valence-band maximum. Empty surface-state bands are more pronounced near the conduction-band minima. The most significant surface band is predicted for NiO(001)$(2\times1)$. A well-separated $e_g(d_{3r^2-z^2})$ band appears in the upper part of the fundamental gap. As a consequence, the empty-state as well as filled-state STM images computed for a non-spin-polarized tip clearly exhibit a nearly bulk terminated $1\times1$ surface geometry with the highest corrugations for the TM ions but with an increasing visibility of the oxygen ions along the row MnO, FeO, CoO, and NiO, at least in the filled-state images. The trends can be explained with a successive filling of the TM $3d$ $t_{2g}$ shell in the minority-spin channel. For a ferromagnetic tip we predict well-pronounced [1$\overline{1}$0] chains showing each second atom in the surface unit cell, i.e., a well-pronounced spin contrast. The increasing importance of the oxygen states along the TMO row even suggests a possible observation of zigzag chains in the filled-state images of CoO and NiO.

[1] S. Heinze, M. Bode, A. Kubetzka, O. Pietzsch, X. Nie, S. Blugel, and R. Wiesendanger, *Science* **288**, 1805 (2000).
[2] M. Bode, Rep. Prog. Phys. **66**, 523 (2003).
[3] R. Wiesendanger, Rev. Mod. Phys. **81**, 1495 (2009).
[4] U. Kaiser, A. Schwarz, and R. Wiesendanger, *Nature* (London) **446**, 522 (2007).
[5] F. Pielmeier and F. J. Giessibl, *Phys. Rev. Lett.* **110**, 266101 (2013).
[6] M. Granovskij, A. Schrön, and F. Bechstedt, *Phys. Rev. B* **88**, 184416 (2013).
[7] M. Granovskij, A. Schrön, and F. Bechstedt, *New J. Phys.* **16**, 023020 (2014).
[8] C. Kittel, *Introduction to Solid State Physics*, 8th ed. (Wiley, New York, 2005).
[9] P. W. Anderson, *Solid State Phys.* **14**, 99 (1963).
[10] A. Schrön, C. Rödl, and F. Bechstedt, *Phys. Rev. B* **86**, 115134 (2012).
[11] C. Noguera, *Physics and Chemistry at Oxide Surfaces* (Cambridge University Press, Cambridge, 1996).
[12] L. Liao, Q. Zhang, Z. Su, Z. Zhao, Y. Wang, Y. Li, X. Lu, D. Wei, G. Feng, Q. Yu, X. Cai, J. Zhao, Z. Ren, H. Fang, F. Robles-Hernandez, S. Baldelli, and J. Bao, *Nat. Nanotechnol.* **9**, 69 (2014).
[13] E. A. Soares, R. Paniago, V. E. de Carvalho, E. L. Lopes, G. J. P. Abreu, and H.-D. Pfannes, *Phys. Rev. B* **73**, 035419 (2006).
[14] T. Okazawa and Y. Kido, *Surf. Sci.* **556**, 101 (2004).
[15] M. R. Welton-Cook and M. Prutton, *J. Phys. C* **13**, 3993 (1980).
[16] T. Okazawa, Y. Yagi, and Y. Kido, *Phys. Rev. B* **67**, 195406 (2003).
[17] K.-M. Schindler, J. Wang, A. Chassé, H. Neddermeyer, and W. Widdra, *Surf. Sci.* **603**, 2658 (2009).
[18] H. Momida and T. Oguchi, *J. Phys. Soc. Jpn.* **72**, 588 (2003).
[19] O. Bengone, M. Alouani, P. Blöchl, and J. Hugel, *Phys. Rev. B* **62**, 16392 (2000).
[20] N. Yu, W.-B. Zhang, N. Wang, Y.-F. Wang, and B.-Y. Tang, *J. Phys. Chem. C* **112**, 452 (2008).
[21] D. Ködderitzsch, W. Hergert, W. M. Temmerman, Z. Szotek, A. Ernst, and H. Winter, *Phys. Rev. B* **66**, 064434 (2002).
[22] J. Szuber, *J. Electron Spectrosc. Relat. Phenom.* **34**, 337 (1984).
[23] S. L. Dudarev, A. I. Liechtenstein, M. R. Castell, G. A. D. Briggs, and A. P. Sutton, *Phys. Rev. B* **56**, 4900 (1997).
[24] M. R. Castell, S. L. Dudarev, G. A. D. Briggs, and A. P. Sutton, *Phys. Rev. B* **59**, 7342 (1999).
[25] F. U. Hillebrecht, H. Ohldag, N. B. Weber, C. Bethke, U. Mick, M. Weiss, and J. Bahrdt, *Phys. Rev. Lett.* **86**, 3419 (2001).
[26] S. Mandal, K. S. R. Menon, F. Maccherozzi, and R. Belkhou, *Europhys. Lett.* **95**, 27006 (2011).
[27] F. Bechstedt, *Principles of Surface Physics* (Springer, Berlin, 2003).
[28] H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**, 5188 (1976).
[29] P. Hohenberg and W. Kohn, *Phys. Rev.* **136**, B864 (1964).
[30] W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).
[31] J. P. Perdew and A. Zunger, *Phys. Rev. B* **23**, 5048 (1981).
[32] D. Hobbs, G. Kresse, and J. Hafner, *Phys. Rev. B* **62**, 11556 (2000).
[33] A. Schrön and F. Bechstedt, *J. Phys.: Condens. Matter* **25**, 486002 (2013).
[34] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).
[35] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).
[36] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, *Phys. Rev. B* **57**, 1505 (1998).
[37] A. Schrön, C. Rödl, and F. Bechstedt, *Phys. Rev. B* **82**, 165109 (2010).

[38] C. Rödl, F. Fuchs, J. Furthmüller, and F. Bechstedt, *Phys. Rev. B* **77**, 184408 (2008).

[39] C. Rödl, F. Fuchs, J. Furthmüller, and F. Bechstedt, *Phys. Rev. B* **79**, 235114 (2009).

[40] M. Krause and F. Bechstedt, *J. Supercond. Novel Magn.* **26**, 1963 (2013).

[41] V. Bayer, C. Franchini, and R. Podloucky, *Phys. Rev. B* **75**, 035404 (2007).

[42] A. Rohrbach, J. Hafner, and G. Kresse, *Phys. Rev. B* **69**, 075413 (2004).

[43] F. Bechstedt, in *Many-Body Approach to Electronic Excitations: Concepts and Applications*, edited by M. Cardona, K. von Klitzing, R. Merlin, and H.-J. Queisser, Springer Series in Solid-State Sciences Vol. 181 (Springer, Heidelberg, 2015).

[44] K. Terakura, A. R. Williams, T. Oguchi, and J. Kübler, *Phys. Rev. Lett.* **52**, 1830 (1984).

[45] P. Fulde, in *Electron Correlations in Molecules and Solids*, 3rd ed., edited by M. Cardona, P. Fulde, K. von Klitzing, R. Medin, H.-J. Queisser, and H. Stormer, Springer Series in Solid-State Sciences Vol. 100 (Springer, Berlin, 1995).

[46] J. Tersoff and D. R. Hamann, *Phys. Rev. B* **31**, 805 (1985).

[47] J. Bardeen, *Phys. Rev. Lett.* **6**, 57 (1961).

[48] S. Sauer, F. Fuchs, F. Bechstedt, C. Blumenstein, and J. Schäfer, *Phys. Rev. B* **81**, 075412 (2010).

[49] E. J. Snyder, E. A. Eklund, and R. S. Williams, *Surf. Sci.* **239**, L487 (1990).

[50] E. Lopes, G. Abreu, R. Paniago, E. Soares, V. de Carvalho, and H.-D. Pfannes, *Surf. Sci.* **601**, 1239 (2007).

[51] M. Caffio, B. Cortigiani, G. Rovida, A. Atrei, C. Giovanardi, A. di Bona, and S. Valeri, *Surf. Sci.* **531**, 368 (2003).

[52] K. L. Krycka, J. A. Borchers, R. A. Booth, Y. Ijiri, K. Hasz, J. J. Rhyne, and S. Majetich, *Phys. Rev. Lett.* **113**, 147203 (2014).