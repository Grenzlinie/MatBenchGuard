# Exchange interactions at surfaces of Fe, Co, and Gd $^{*}$)

I. TUREK $^{**}$)

Institute of Physics of Materials, Acad. Sci. CR,
Žižkova 22, CZ-61662 Brno, Czech Republic

S. BLÜGEL $^{\dagger}$), G. BIHLMAYER

Institut für Festkörperforschung, Forschungszentrum Jülich, D-52425 Jülich, Germany

P. WEINBERGER

Center for Computational Materials Science, Technical University of Vienna,
Getreidemarkt 9/158, A-1060 Vienna, Austria

Received 24 September 2002

Magnetic exchange interactions at low-index surfaces of bcc iron, hcp cobalt, and hcp gadolinium are studied using *ab initio* electronic structure calculations. Interlayer exchange couplings derived from total-energy differences are enhanced at the surfaces over their bulk counterparts. This trend is in contrast to a surface reduction of on-site exchange parameters formulated within a classical Heisenberg model. A particular attention is paid to the sensitivity of exchange interactions at a Gd(0001) surface to relaxation of interlayer distances. The calculated results do not provide support for recently observed surface enhancement of the Curie temperature of the Gd metal.

PACS: 75.70.Rf

Key words: surface magnetism, exchange interactions, Curie temperature

## 1 Introduction

*Ab initio* theory of magnetic ground-state properties of transition-metal surfaces and thin films developed during the last decade [1] is based on the local spin-density approximation (LSDA) to the density-functional theory. However, a reliable description of finite-temperature properties as well as of systems containing rare-earth metals remains, in general, beyond the range of the standard LSDA.

The bulk hcp gadolinium with its (0001) surface represents a most interesting and puzzling system, as documented, e.g., by observed surface enhancement of its Curie temperature [2]. Theoretical explanation of the latter fact was provided in terms of an LSDA+U approach [3]. However, more recent works have thrown serious doubts on these conclusions, both on side of experiment [4] and theory [5].

Motivated by the above findings, we present here results of systematic first-principles investigations of exchange interactions at low-index surfaces of bcc Fe,

$^{*}$) Presented at the IX-th Symposium on Surface Physics, Třešť Castle, Czech Republic, September 2–6, 2002.
$^{**}$) Also at Department of Electronic Structures, Charles University in Prague, Czech Republic, and at Center for Computational Materials Science, Technical University of Vienna, Austria
$^{\dagger}$) Also at Fachbereich Physik, Universität Osnabrück, Germany

Czechoslovak Journal of Physics, Vol. 53 (2003), No. 1

hcp Co, and hcp Gd. Besides differences of total energies calculated for various spin configurations, we employed a framework of an effective classical Heisenberg Hamiltonian applied to itinerant magnets [6–8].

## 2 Formalism and computational details

The selfconsistent electronic structure calculations within the LSDA were per-formed using the all-electron scalar-relativistic tight-binding linear muffin-tin or-bital (TB-LMTO) method in the atomic-sphere approximation (ASA) [9]. The va-lence basis consisted of s-, p-, and d-type orbitals, whereas the 4f orbitals in the case of Gd were treated as part of atomic-like core with the majority (minority)4f level fully occupied (empty). In the case of surfaces, the selfconsistency region at the metal/vacuum interface comprised 7 atomic layers and 3 layers of empty spheres. The accuracy of the ASA was checked by the full potential linearized aug-mented plane-wave (FLAPW) method [10] as implemented in the FLEUR code which enabled to perform also LSDA+U calculations [5].

The effective Heisenberg Hamiltonian considered here has a form

$$
H_{\mathrm{eff}}=-\sum_{\mathbf{R} \mathbf{R}^{\prime}} J_{\mathbf{R} \mathbf{R}^{\prime}} \mathbf{e}_{\mathbf{R}} \cdot \mathbf{e}_{\mathbf{R}^{\prime}}, \tag{1}
$$

where the subscript $\mathbf{R}$ labels the lattice sites, the vectors $\mathbf{e}_{\mathbf{R}}$ are unit vectors point-ing in the direction of the individual local moments, and the pair exchange inter-actions $J_{\mathbf{R} \mathbf{R}^{\prime}}$ satisfy $J_{\mathbf{R} \mathbf{R}^{\prime}}=J_{\mathbf{R}^{\prime} \mathbf{R}}$ and $J_{\mathbf{R} \mathbf{R}}=0$. They were calculated using the magnetic force theorem [6, 7] applied within the TB-LMTO-ASA method for a collinear ground state [8]:

$$
J_{\mathbf{R} \mathbf{R}^{\prime}}=-\frac{1}{8 \pi \mathrm{i}} \int_{C} \operatorname{tr}_{L}\left[\Delta_{\mathbf{R}}(z) g_{\mathbf{R} \mathbf{R}^{\prime}}^{\uparrow}(z) \Delta_{\mathbf{R}^{\prime}}(z) g_{\mathbf{R}^{\prime} \mathbf{R}}^{\downarrow}(z)\right] \mathrm{d} z. \tag{2}
$$

In Eq. (2), the symbol $\operatorname{tr}_{L}$ denotes the trace over the angular momentum index $L=(\ell m)$ and energy integration is performed in the complex energy plane along a closed contour $C$ starting and ending at the Fermi energy. The quantities $g_{\mathbf{R} \mathbf{R}^{\prime}}^{\sigma}(z)$ ($\sigma$ being a spin index, $\sigma=\uparrow, \downarrow$) denote site-off-diagonal blocks of the so-called auxiliary Green-function matrices with elements $g_{\mathbf{R} L, \mathbf{R}^{\prime} L^{\prime}}^{\sigma}(z)$ while $\Delta_{\mathbf{R}}(z)=P_{\mathbf{R}}^{\uparrow}(z)-P_{\mathbf{R}}^{\downarrow}(z)$ are diagonal matrices related to the potential functions $P_{\mathbf{R} \ell}^{\sigma}(z)$ of the TB-LMTO-ASA method [9]. In addition to the pair exchange interactions $J_{\mathbf{R} \mathbf{R}^{\prime}}$, an on-site exchange parameter $J_{\mathbf{R}}^{0}$ defined by

$$
J_{\mathbf{R}}^{0}=\sum_{\mathbf{R}^{\prime}} J_{\mathbf{R} \mathbf{R}^{\prime}} \tag{3}
$$

can be introduced. It is related to the energy change due to an infinitesimal rotation of the $\mathbf{R}$-th local moment with respect to the bulk magnetization. The lattice summation in Eq. (3) can be done exactly by employing a sum rule [6]

Surfaces of Fe, Co, Gd

$$
\begin{aligned}
J_{\mathbf{R}}^{0}=\frac{1}{8 \pi \mathrm{i}} \int_{C} \operatorname{tr}_{L} & \left\{\Delta_{\mathbf{R}}(z)\left[g_{\mathbf{R R}}^{\uparrow}(z)-g_{\mathbf{R R}}^{\downarrow}(z)\right]\right. \\
& \left.+\Delta_{\mathbf{R}}(z) g_{\mathbf{R R}}^{\uparrow}(z) \Delta_{\mathbf{R}}(z) g_{\mathbf{R R}}^{\downarrow}(z)\right\} \mathrm{d} z,
\end{aligned}
\tag{4}
$$

which involves only the site-diagonal blocks of the Green-function matrices.

For bulk ferromagnets with all lattice sites equivalent ($J_{\mathbf{R}}^{0} \equiv J^{0}$), the Curie temperature in the mean-field approximation for the Hamiltonian (1) is given by

$$
k_{\mathrm{B}} T_{\mathrm{C}}^{\mathrm{MFA}}=\frac{2}{3} J^{0},
\tag{5}
$$

where $k_{\mathrm{B}}$ is the Boltzmann constant. For inhomogeneous systems like surfaces, a direct relation between the Curie temperature and the on-site exchange parameters $J_{\mathbf{R}}^{0}$ cannot be given. Hence, the latter quantities reflect merely the strength of the exchange interaction and its spatial variations. The same is true also for total-energy differences among selected magnetic configurations.

## 3 Results and discussion

### 3.1 Surfaces of bcc Fe and hcp Co

Table 1 summarizes total-energy differences calculated for bulk Fe and Co (with experimental lattice constants) and for their surfaces (with lattice sites coinciding with ideal truncated bulk positions). The $\Delta E^{\text {bulk }}$ is defined as energy separation (per bulk atom) between the bulk ferromagnetic (FM) ground state and an antiferromagnetic (AFM) bulk spin configuration with an AFM coupling between successive atomic layers parallel to a particular surface, while the $\Delta E^{\text {surf }}$ is energy difference (per surface atom) between the FM surface and a surface with an AFM coupling of the top layer to the semiinfinite FM bulk. The relation $\Delta E^{\text {bulk }}<\Delta E^{\text {surf }}$ proves a surface enhancement of effective interlayer exchange couplings for all three surfaces studied (Table 1).

Table 1. Energy difference between the AFM and FM states in the bulk Fe and Co and at their surfaces as calculated by the LMTO-ASA technique (see text for details).

<table>
<thead>
  <tr>
    <th>Metal</th>
    <th>Layers</th>
    <th>$\Delta E^{\text{bulk}}$<br>(mRy/atom)</th>
    <th>$\Delta E^{\text{surf}}$<br>(mRy/atom)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>bcc Fe</td>
    <td>(110)</td>
    <td>18.27</td>
    <td>22.28</td>
  </tr>
  <tr>
    <td></td>
    <td>(001)</td>
    <td>34.04</td>
    <td>46.47</td>
  </tr>
  <tr>
    <td>hcp Co</td>
    <td>(0001)</td>
    <td>18.32</td>
    <td>28.12</td>
  </tr>
</tbody>
</table>

The exchange interactions in the bulk transition metals and the corresponding Curie temperatures were studied in detail elsewhere [8]. Figure 1 presents layer-resolved local quantities at the surfaces: the magnetic moments and the on-site

![](./images/812411736672960512_1.jpg)

Fig. 1. Layer-resolved magnetic moments (left) and on-site exchange parameters $J_{\mathbf{R}}^{0}$ (right) at surfaces of bcc Fe and hcp Co. The layer numbering starts from the top surface layer, denoted by 0.

exchange parameters $J_{\mathbf{R}}^{0}$ (3). It is seen that the well-known surface enhancement of the moments is accompanied by a more complicated layer-dependence of the exchange parameters exhibiting a minimum in the top surface layer and a maximum in the first subsurface layer. A qualitative explanation follows from Eqs. (2) and (3) which show that $J_{\mathbf{R}}^{0}$ reflects the exchange splitting of the $\mathbf{R}$-th site as well as the splittings and number of its neighbors. Hence, the reduction of $J_{\mathbf{R}}^{0}$ in the top surface layer is due to the reduced coordination, whereas the maximum in the first subsurface position is due to the full (bulk-like) coordination of these sites and the enhanced surface local moments (Figure 1). Note that the layer-dependence of the on-site exchange parameters and its explanation are analogous to the case of hyperfine magnetic fields at the nuclei of iron atoms [9, 11].

### 3.2 Bulk hcp Gd

As shown recently [5], the LSDA combined with a 4f core treatment implemented within the FLAPW technique provides a surprisingly good description of the ground-state properties of hcp Gd, including especially the stabilization of the FM ground state with respect to an AFM spin structure with AFM coupling between neighboring close-packed (0001) atomic planes. Table 2 compares results obtained by the FLAPW method and the less accurate TB-LMTO-ASA technique. The agreement is quite satisfactory which is a necessary prerequisite for studies of the exchange interactions within the latter technique.

Figure 2 shows the calculated exchange interactions $J_{\mathbf{R}\mathbf{R}'}$ for experimental lattice constants of the hcp Gd structure. The pair interactions between the first nearest neighbors are positive and dominate clearly over the interactions of more

Surfaces of Fe, Co, Gd

Table 2. Ground-state properties of hcp Gd as calculated in a 4f core treatment and with an experimental value of the $c/a$ ratio for FM and AFM states: equilibrium lattice parameter (relative to the experimental value), bulk modulus, local magnetic moment, and the energy difference between the AFM and FM states.

<table>
  <thead>
    <tr>
      <th>Technique</th>
      <th>State</th>
      <th>$\Delta a/a$ (%)</th>
      <th>$B$ (Mbar)</th>
      <th>$M$ ($\mu_\text{B}$)</th>
      <th>$\Delta E$ (mRy/atom)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">LMTO-ASA</td>
      <td>FM</td>
      <td>$-1.3$</td>
      <td>0.46</td>
      <td>7.67</td>
      <td>–</td>
    </tr>
    <tr>
      <td>AFM</td>
      <td>$-1.5$</td>
      <td>0.45</td>
      <td>7.45</td>
      <td>2.92</td>
    </tr>
    <tr>
      <td rowspan="2">FLAPW</td>
      <td>FM</td>
      <td>$-1.4$</td>
      <td>0.50</td>
      <td>7.41</td>
      <td>–</td>
    </tr>
    <tr>
      <td>AFM</td>
      <td>$-1.7$</td>
      <td>0.49</td>
      <td>7.32</td>
      <td>4.12</td>
    </tr>
    <tr>
      <td>experiment</td>
      <td>FM</td>
      <td>0.0</td>
      <td>0.38</td>
      <td>7.63</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

distant pairs, which oscillate and tend rapidly to zero with increasing interatomic distance. This dependence is in full agreement with a Ruderman–Kittel–Kasuya–Yoshida (RKKY) asymptotic behavior [8].

Equation (5) yields $T_\text{C}^\text{MFA} = 334$ K, a value slightly above the experimental Curie temperature, $T_\text{C}^\text{exp} = 293$ K. It can be expected that more accurate methods of statistical physics will reduce the theoretical Curie temperature by 10 to 20% [8], i.e., shifting it even closer to experiment. This degree of quantitative agreement indicates that the present values of exchange interactions $J_{\mathbf{RR}'}$ are basically correct. Note that the role of the apparently small interactions beyond the first neighboring shell (Figure 2) is by no means negligible for reliable quantitative studies: their contribution to the real-space sum in (3) amounts to 25% of the total value of $J^0$. A similar remark refers also to the anisotropy of the first nearest-neighbor $J$’s: the pair interaction in the close-packed (0001) planes is about 20% smaller than that between these planes (Figure 2).

![](./images/812411736672960512_2.jpg)

Fig. 2. Pair exchange interactions $J_{\mathbf{RR}'}$ for ferromagnetic hcp Gd with experimental lattice constants $a$ and $c$ as a function of the interatomic distance $d = |\mathbf{R} - \mathbf{R}'|$. The crosses and squares refer to pairs of sites $\mathbf{R}$, $\mathbf{R}'$ lying in even (AA) and odd (AB) close-packed (0001) planes, respectively.

Czech. J. Phys. 53 (2003)

### 3.3 Gd(0001) surface

The total-energy differences between the FM and AFM configurations of hcp Gd, $\Delta E^{\text{bulk}}$ and $\Delta E^{\text{surf}}$ (cf. Subsection 3.1), are presented in Table 3 for different modifications of the LSDA and for different techniques, including the results of Ref. [3]. The Gd(0001) surface was treated in two structural models: with the lattice sites occupying the ideal truncated bulk positions (unrelaxed structure) and with a 3% contraction of the interalyer separation between the two topmost atomic layers (inward relaxation). The magnitude of the contraction was set according to LEED measurements [12] as well as to previous FLAPW calculations [5]. It can be seen that the effective interlayer interaction is enhanced at the surface, in qualitative agreement with the transition-metal surfaces (Subsection 3.1). However, the values of $\Delta E^{\text{bulk}}$ and $\Delta E^{\text{surf}}$ as well as their ratio depend appreciably on further details of the calculations. Note that $\Delta E^{\text{surf}}/\Delta E^{\text{bulk}} \approx 1.5$ for both ideal hcp(0001) surfaces (Co, Gd) calculated by the LMTO-ASA technique.

Table 3. Energy difference between the AFM and FM states in the bulk Gd and at its (0001) surface (see text for details). The bottom line corresponds to Ref. [3].

<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th rowspan="2">Technique</th>
      <th rowspan="2">$\Delta E^{\text{bulk}}$ (mRy/atom)</th>
      <th colspan="2">$\Delta E^{\text{surf}}$ (mRy/atom)</th>
    </tr>
    <tr>
      <th>ideal</th>
      <th>relaxed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">LSDA 4f core</td>
      <td>LMTO-ASA</td>
      <td>3.05</td>
      <td>4.46</td>
      <td>4.30</td>
    </tr>
    <tr>
      <td>FLAPW</td>
      <td>4.12</td>
      <td>7.35</td>
      <td>7.94</td>
    </tr>
    <tr>
      <td rowspan="2">LSDA+U</td>
      <td>FLAPW</td>
      <td>2.50</td>
      <td>6.54</td>
      <td>6.99</td>
    </tr>
    <tr>
      <td>FLAPW(*)</td>
      <td>4.63</td>
      <td>5.29</td>
      <td>9.93</td>
    </tr>
  </tbody>
</table>

The effect of surface relaxation on the $\Delta E^{\text{surf}}$ is rather weak in the present calculations, both the LMTO-ASA and the FLAPW ones, though in the case of Gd treated in the FLAPW/LSDA+U model another ambiguity enters through the choice of the muffin-tin radius [5]. On the other hand, a pronounced increase of $\Delta E^{\text{surf}}$ (by nearly a factor of two) due to the surface relaxation was reported in Ref. [3] (Table 3) and it was identified as an origin of the observed surface enhancement of the Curie temperature [2]. Note that according to the simple model employed in Ref. [3], all results of the present LMTO-ASA and FLAPW calculations would yield enhanced Curie temperatures at the surface (both ideal and relaxed), since the corresponding criterion ($\Delta E^{\text{surf}}/\Delta E^{\text{bulk}} > 4/3$) is satisfied in each case (Table 3). In analogy to the bulk case (Subsection 3.2), one can expect that the long-ranged exchange interactions will modify the resulting Curie temperatures considerably.

Figure 3 presents the calculated local magnetic moments and the on-site exchange parameters $J_{\mathbf{R}}^{0}$ at the ideal and relaxed Gd(0001) surfaces. The layer-resolved magnetic moments exhibit a small surface enhancement followed by Friedel-like oscillations around the bulk value. These oscillations can be resolved also in the

Surfaces of Fe, Co, Gd

![](./images/812411736672960512_3.jpg)

Fig. 3. Layer-resolved magnetic moments (left) and on-site exchange parameters $J_{\mathbf{R}}^{0}$ (right) at the (0001) surface of hcp Gd as calculated with the lattice sites in the ideal truncated bulk positions and with the top surface layer relaxed towards the bulk. The layer numbering starts from the top surface layer, denoted by 0.

layer-dependence of the parameters $J_{\mathbf{R}}^{0}$ which, however, starts with a reduced value in the top surface layer due to the reduced coordination, as discussed in Subsection 3.1. As a consequence, the maximum of the on-site exchange parameters is found in the second subsurface layer, in contrast to the transition-metal surfaces.

The surface relaxation does not change the investigated layer-dependences sub- stantially: it leads to a small reduction of the local moments and the on-site ex- change parameters in the first two top surface layers and a tiny enhancement in the second subsurface layer as compared to the ideal surface (Figure 3). The surface reduction of $J_{\mathbf{R}}^{0}$ agrees qualitatively with a small decrease of $\Delta E^{\text{surf}}$ due to the relaxation as found by the LMTO-ASA technique (Table 3).

## 4 Conclusions

We investigated the effect of low-index surfaces on exchange interactions in fer- romagnetic transition (Fe, Co) and rare-earth (Gd) metals. We found that effective exchange interactions between the atomic layers are enhanced at the surfaces as compared to the bulk, in clear contrast to a surface reduction of on-site exchange parameters obtained from a classical Heisenberg Hamiltonian. The latter property was explained in terms of a reduced coordination of surface atoms.

In the case of the Gd(0001) surface, we focused on the role of surface relaxation on the resulting exchange interactions. We found this effect rather weak, unable to produce a surface enhancement of the Curie temperature. However, an improved treatment of the effective Heisenberg Hamiltonian, which overcomes the mean-field

Czech. J. Phys. 53 (2003)

I. Turek et al.: Surfaces of Fe, Co, Gd

approximation and takes into account the pair exchange interactions beyond the first nearest neighbors, remains an important task for future studies.

The authors acknowledge financial support provided by the Grant Agency of the Czech Republic (202/00/0122, 106/02/0943), the Center for Computational Materials Science in Vienna (GZ 45.504), the Scientific and Technological Cooperation between Germany and the Czech Republic (TSR-013-98), and the RT Network 'Computational Magnetoelectron- ics' (HPRN-CT-2000-00143) of the European Commission.

### References

[1] M. Weinert and S. Blügel: in *Magnetic Multilayers* (Eds. L.H. Bennett and R.E. Watson). World Scientific, Singapore, 1994, p. 51.

[2] E.D. Tober et al.: Phys. Rev. Lett. **81** (1998) 2360.

[3] A.B. Shick, W.E. Pickett, and C.S. Fadley: Phys. Rev. B **61** (2000) R9213.

[4] C.S. Arnold and D.P. Pappas: Phys. Rev. Lett. **85** (2000) 5202.

[5] Ph. Kurz, G. Bihlmayer, and S. Blügel: J. Phys.: Condens. Matter **14** (2002) 6353.

[6] A.I. Liechtenstein, M.I. Katsnelson, V.P. Antropov, and V.A. Gubanov: J. Magn. Magn. Mater. **67** (1987) 65.

[7] V.P. Antropov, B.N. Harmon, and A.N. Smirnov: J. Magn. Magn. Mater. **200** (1999) 148.

[8] M. Pajda, J. Kudrnovský, I. Turek, V. Drchal, and P. Bruno: Phys. Rev. B **64** (2001) 174402.

[9] I. Turek, V. Drchal, J. Kudrnovský, M. Šob, and P. Weinberger: *Electronic Structure of Disordered Alloys, Surfaces and Interfaces*. Kluwer, Boston, 1997.

[10] E. Wimmer, H. Krakauer, M. Weinert, and A.J. Freeman: Phys. Rev. B **24** (1981) 864.

[11] S. Blügel: in *Magnetismus von Festkörpern und Grenzflächen*. Forschungszentrum Jülich, 1993 (in German).

[12] J. Giergiel et al.: Phys. Rev. B **51** (1995) 10201.