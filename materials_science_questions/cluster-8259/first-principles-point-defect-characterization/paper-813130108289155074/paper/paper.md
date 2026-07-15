Author's Accepted Manuscript

Ga acceptor defects in $SnO_2$ revisited: A hybrid
functional study

Nirawith Palakawong, Yi-Yang Sun, Jiraroj T-
Thienprasert, Shengbai Zhang, Sukit Limpijumnong

![](./images/813130108289155074_1.jpg)

www.elsevier.com/locate/ceri

<table>
  <tr>
    <td>PII:</td>
    <td>S0272-8842(17)31056-8</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/10.1016/j.ceramint.2017.05.235</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>CERI15395</td>
  </tr>
</table>

To appear in: *Ceramics International*

Cite this article as: Nirawith Palakawong, Yi-Yang Sun, Jiraroj T-Thienprasert,
Shengbai Zhang and Sukit Limpijumnong, Ga acceptor defects in $SnO_2$ revisited:
A hybrid functional study, *Ceramics International*
http://dx.doi.org/10.1016/j.ceramint.2017.05.235

This is a PDF file of an unedited manuscript that has been accepted for
publication. As a service to our customers we are providing this early version of
the manuscript. The manuscript will undergo copyediting, typesetting, and a
review of the resulting galley proof before it is published in its final citable form.
Please note that during the production process errors may be discovered which
could affect the content, and all legal disclaimers that apply to the journal pertain.

# Ga acceptor defects in $SnO_2$ revisited: A hybrid functional study

Nirawith Palakawong$^{\text{a,b,c,*}}$, Yi-Yang Sun$^{\text{c}}$, Jiraroj T-Thienprasert$^{\text{b,d}}$, Shengbai Zhang$^{\text{c}}$,
and Sukit Limpijumnong$^{\text{a,b}}$

$^{\text{a}}$School of Physics and NANOTEC-SUT Center of Excellence on Advanced Functional Nanomaterials,
Suranaree University of Technology, Nakhon Ratchasima 30000, Thailand

$^{\text{b}}$Thailand Center of Excellence in Physics, Commission on Higher Education, Bangkok 10400, Thailand

$^{\text{c}}$Department of Physics, Applied Physics, and Astronomy, Rensselaer Polytechnic Institute, Troy, New
York 12180, USA

$^{\text{d}}$Department of Physics, Faculty of Science, Kasetsart University, Bangkok 10900, Thailand

## Abstract

$SnO_2$ is one of the most interesting oxide semiconductors due to its wide band
gap, good transparency, high thermal/chemical resistances, and low cost. As-grown
$SnO_2$ usually exhibits $n$-type conductivity with high carrier concentrations. Similar to
the case of $ZnO$, it is difficult to dope $SnO_2$ into $p$-type. Consequently, applications of
$SnO_2$ for optoelectronic as well as electronic devices are limited. In principle,
substitution of group-III elements, including Al, Ga, and In, for Sn atom in $SnO_2$ could
give a hole carrier resulting in a $p$-type conductivity. Based on the HSE functional
calculations [Phys. Rev. B **79**, 245206 (2009)], it has been reported that these dopants
are shallow acceptor defects. However, the calculations with PBE0 functional [J.
Mater. Chem. **22**, 25236 (2012)] showed that these dopants are deep acceptors. In this
work, Ga-doped $SnO_2$ are revisited by using HSE functional. We found that Ga$_{\text{Sn}}$ defect
is indeed a deep acceptor indicating that Ga$_{\text{Sn}}$ can serve only as a compensating acceptor

* Corresponding author; Tel.: +66 8 5140 5305; *E-mail:* nirawith@gmail.com (N. Palakawong).

defect in $SnO_2$. Hoping to make the acceptor level shallower, we further study the effect of (compressive) strain on the acceptor level associated with $Ga_{Sn}$ defect by alloying $SnO_2$ with Si atoms ($Si_xSn_{1-x}O_2$ alloy where $x \sim 0.17$). Our results showed that even with the application of strain, the acceptor level remains too deep to be useful.

Keywords: First-principles calculations; $SnO_2$; Impurities; Acceptor defects

### 1. Introduction

Tin dioxide ($\text{SnO}_2$), known as cassiterite in the mineral form, is one of the most interesting ceramics because of its wide band gap, good transparency, high thermal/chemical resistances, and low cost [1, 2]. Due to its large direct band gap of ~3.60 eV [3], $\text{SnO}_2$ has been widely applied in various applications, such as transparent conductive oxides (TCOs), solar cells, and solid state gas sensing materials [4-6]. The crystal structure of $\text{SnO}_2$ at room temperature is tetragonal rutile, in which the Sn and O atoms are six-fold and three-fold coordinated, respectively [7]. Usually, as-grown $\text{SnO}_2$ exhibits $n$-type conductivity with a high carrier concentration, which has been attributed to the intrinsic or extrinsic defects [8-11]. There are experimentally reports showing that the electrical conductivity strongly depends on the oxygen availability during the crystal growth process [9, 10]. Therefore, the origin of $n$-type conductivity in $\text{SnO}_2$ was assigned to intrinsic defects, especially the oxygen vacancies ($V_\text{O}$) [8, 9]. However, there is no direct evidence to support this assignment.

In order to make $\text{SnO}_2$ usable for a wide range of electronic devices, $\text{SnO}_2$ must be able to be doped into both $n$- and $p$-types. However, the inherent $n$-type conductivity in $\text{SnO}_2$ is an obstacle for making it into $p$-type semiconductor. In addition, an effective $p$-type dopant for $\text{SnO}_2$ has not been identified. In principle, substitution of group-III elements for Sn site could make it $p$-type and there are many literatures studying the feasibility of making $p$-type $\text{SnO}_2$ [12-14]. Singh *et al.* have used density functional theory (DFT) calculations with GGA+$U$ method to study $\text{SnO}_2$ doped with group-III elements [12]. They reported that $p$-type $\text{SnO}_2$ could be achieved by replacing Sn atom

with $Al(Al_{Sn})$, $Ga(Ga_{Sn})$, or $In(In_{Sn})$ atom. Further, Varley *et al.* have repeated Singh's calculations by using DFT calculations with more accurate hybrid functional proposed by Heyd-Scuseria-Ernzerhof (HSE) with a default Hartree-Fock mixing parameter of 25% [13]. Their results showed that $Al_{Sn}$, $Ga_{Sn}$, and $In_{Sn}$ defects in $SnO_2$ could act as a shallow acceptor in agreement with Singh's results. However, Scanlon and Watson have reinvestigated the possibility of making $p$-type $SnO_2$ by using the PBE0 hybrid functional [15] and revealed that these defects could not act as shallow accepters contradicting to previous results [14]. In addition, they found that $Ga_{Sn}$ defect is amphoteric with two defect transition levels $\varepsilon(+/0)=0.54$ eV and $\varepsilon(0/-)=1.05$ eV. This conflict is interesting and should be clarified. In this work, the $Ga_{Sn}$ defect in $SnO_2$ is revisited by using DFT calculations with HSE hybrid functional. We found that $Ga_{Sn}$ actually is a deep acceptor with defect transition level $\varepsilon(0/-)=0.79$ eV.

To find a way to enhance the acceptor concentration, i.e., making the acceptor level shallower, we studied the effects of crystal strain on the acceptor level. It has been illustrated that for the case of Na-doped ZnO, applying the compressive strain can make the acceptor level shallower [16]. To make it more practical, the compressive strain could be introduced by alloying the host material with an isovalent element that has the same crystal structure but with a smaller lattice constant [17]. Here, the compressive strain in $SnO_2$ is introduced by alloying $SnO_2$ with Si. Both $SiO_2$ and $SnO_2$ have rutile structure, but different lattice parameters, i.e., $a=4.18$ Å and $c=2.66$ Å for $SiO_2$ [18] and $a=4.74$ Å and $c=3.19$ Å for $SnO_2$ [19]. Our results show that applying compressive strain through alloying does not sufficiently shift the acceptor level to a usable value.

### 2. Computational details

We used first-principles calculations based on density functional theory (DFT) within a plane-wave basis set as implemented in the VASP code [20-22]. The electron-ion interactions were described by the projector augmented wave (PAW) method [23]. The Sn $4d$ and Ga $3d$ states were treated as valence electrons. For the exchange-correlation energy, we used both generalized gradient approximation (GGA) parameterized by Perdew, Burke, and Ernzerhof (PBE) [15] and hybrid functional proposed by Heyd, Scuseria, and Ernzerhof (HSE) [24] with a mixing parameter of 0.32. The latter yields the calculated band gap of 3.61 eV in agreement with the experimental value of 3.60 eV [3]. The energy cutoff for expanding the plane wave basis set was set at 306 eV [21]. The spin polarization was treated for all cases with unpaired electrons. For bulk calculations, the $\Gamma$-centered grid scheme was used for $k$-space integration with a sampling mesh point of $3 \times 3 \times 5$. The calculated lattice parameters for $\text{SnO}_2$ obtained from both GGA-PBE and HSE are summarized in Table 1. They are in good agreement with the experimental values. For defect calculations, a supercell approach was employed using a supercell size of 72-atom, i.e., a $2 \times 2 \times 3$ repetition of the 6-atom primitive cell. All atoms in the supercell were allowed to relax until the residue force on each atom became less than 0.025 eV/Å. The chance of Ga substitution for Sn ($\text{Ga}_{\text{Sn}}$) could be determined from its formation energy, which is defined by [25]:

$$
E^{f}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q}\right)=E_{t o t}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q}\right)-E_{t o t}\left(\mathrm{SnO}_{2}\right)+\mu_{\mathrm{Sn}}-\mu_{\mathrm{Ga}}+q\left(E_{F}+E_{\mathrm{VBM}}\right), \tag{1}
$$

where $E_{tot}(\text{Ga}_{\text{Sn}}^q)$ is the calculated total energy of a supercell with Ga substitution for Sn in charge state $q$, $E_{tot}(\text{SnO}_2)$ is the calculated total energy of a perfect supercell, $\mu_{\text{Sn}}$

and $\mu_{\mathrm{Ga}}$ are the atomic chemical potentials described below, and $E_{F}$ is the Fermi energy referenced to the valence band maximum (VBM) of the perfect cell.

To grow $\mathrm{SnO}_{2}$ crystal under the thermodynamic equilibrium, it is required that $\mu_{\mathrm{SnO}_{2}}=\mu_{\mathrm{Sn}}+2 \mu_{\mathrm{O}}$, where $\mu_{\mathrm{SnO}_{2}}$ is the total energy of $\mathrm{SnO}_{2}$ per formula unit, $\mu_{\mathrm{Sn}}$ and $\mu_{\mathrm{O}}$ are the atomic chemical potentials for $\mathrm{Sn}$ and $\mathrm{O}$, respectively. To prevent the formation of the undesired phases, such as metallic $\alpha$-Sn and gaseous $\mathrm{O}_{2}$, the chemical potentials of $\mathrm{Sn}$ and $\mathrm{O}$ ( $\mu_{\mathrm{Sn}}$ and $\mu_{\mathrm{O}}$ ) are limited to the energy per formula unit of metallic $\alpha$-Sn and half of the energy of gaseous $\mathrm{O}_{2}$ molecule ( $\mu_{\mathrm{O}}=E_{t o t}\left(\mathrm{O}_{2}\right) / 2$ ), respectively. For the calculations of Ga defects, the chemical potential of Ga ( $\mu_{\mathrm{Ga}}$ ) is limited by $\beta-\mathrm{Ga}_{2} \mathrm{O}_{3}$ phase to prevent the formation of gallium oxide phase.

For the formation-energy calculations of charged defect by the supercell approach, there is a fictitious interaction arising from the neighboring cells due to periodic boundary conditions. This error can be reduced by applying a finite-size correction to the defect formation energy defined in Eq. (1). Here, we applied the finite-size correction scheme [26];

$$
E_{\text {correct }}^{f}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q}\right)=E^{f}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q}\right)+\frac{q^{2} a}{2 e L}, \quad (2)
$$

where $E^{f}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q}\right)$ is the calculated formation energy obtained from Eq. (1). The last term on the right hand side is the Madelung energy, where $\alpha$ is the Madelung constant, $\varepsilon$ is the static dielectric constant of material, and $L$ is the linear dimension of the supercell (i.e., $L \sim \Omega^{1 / 3}$, where $\Omega$ is the supercell volume). We set $\alpha$ and $\varepsilon$ to 2.84 [27] and 12.33 [28], respectively. This gives the calculated Madelung energy for a single charge state $(q=-1$ and +1$)$ of $\mathrm{Ga}_{\mathrm{Sn}}$ defect in the 72-atom $\mathrm{SnO}_{2}$ supercell to be about $0.17 \mathrm{eV}$.

After applying the finite-size correction as mentioned above, we could determine the

defect transition level associated with the defect in two different charge states, i.e., $q_1$
and $q_2$. This level is actually defined as the Fermi-level position at which the formation
energies of the defect in the two charge states are equal, i.e.,

$$
\alpha(q_{1} / q_{2})=\frac{E_{correct}^{f}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q_{2}}\right)-E_{correct}^{f}\left(\mathrm{Ga}_{\mathrm{Sn}}^{q_{1}}\right)}{q_{2}-q_{1}}. \tag{3}
$$

To investigate the effect of compressive strain on the defect transition level
associated with $Ga_{Sn}$ defect in $SnO_{2}$, four $Sn$ atoms in a bulk 72-atom $SnO_{2}$ supercell
were replaced with $Si$ atoms to create $Si_{x}Sn_{1-x}O_{2}$ alloy with $x \sim 0.17$. While there are
many ways to replace four $Sn$ atoms with $Si$, in this work, four $Si$ atoms were
symmetrically substituted on the $Sn$'s sites, as depicted in Fig. 1(a). The cell volume of
the $Si_{x}Sn_{1-x}O_{2}$ alloy was fully optimized. Then, the $Ga_{Sn}$ defect in this alloy was
investigated in two different configurations, as illustrated in Figs. 1(b) and 1(c), where
we labeled them as the Ga *inside* and *outside* Si-clusters, respectively.

### 3. Results and discussion

The lattice parameters obtained from both GGA-PBE and HSE functionals are
tabulated in Table 1 in comparison with the experimental lattice parameters. It can be
clearly seen that the calculations with HSE functional give better results when
comparing with the experimental values. In addition, the calculated band gap and the
heat of formation obtained from HSE functional are 3.61 eV and $-$6.09 eV, respectively,
which are in good agreement with the experimental values of 3.60 eV [3] and $-$5.99 eV
[29]. However, the calculations with HSE functional take much more computational
resources compared to the calculations with GGA-PBE functional. Note that the
calculated band gap with GGA-PBE functional is only 1.27 eV, which is much lower

than the experimental value due to the well-known DFT problems. Moreover, the VBM and CBM positions obtained from GGA-PBE functional are known to be incorrect.
Therefore, the HSE functional will be used for further study.

To revisit the study of $p$-type conductivity in Ga-doped $SnO_2$, we reinvestigated a Ga substitution for Sn ($Ga_{Sn}$) in $SnO_2$. Because Ga has one less valence electron compared to Sn, $Ga_{Sn}$ is expected to be stable in a negative charge state ( $Ga_{Sn}^{-1}$ ) and/or neutral charge state ( $Ga_{Sn}^{0}$ ) depending on the electron Fermi energy. For $Ga_{Sn}^{-1}$, we found that Ga atom prefers to stay on the Sn site surrounded by six oxygen atoms similar to the geometry of Sn-O bonds in bulk $SnO_2$. This configuration is called on-center configuration. The six Ga-O bond lengths are 2% shorter than the Sn-O bond lengths in the bulk $SnO_2$. For $Ga_{Sn}^{0}$, we found that Ga in the on-center configuration is not the lowest-energy configuration. The formation energy can be lowered by breaking a Ga-O bond and shifting the Ga atom from the on-center site. The potential energy curve near the saddle point is illustrated in Fig. 2(a). The new configuration with five Ga-O bonds is called off-center configuration as illustrated in Fig. 2(b). The energy different between the on- and off-center configurations is 0.5 eV; indicating that $Ga_{Sn}^{0}$ clearly stables in the off-center configuration, or a small-polaron configuration.

When taking into account the proper structural relaxation as explained above, the defect transition level $\varepsilon(0/-)$ associated with $Ga_{Sn}$ is ~0.79 eV above the VBM. In addition, the hole states localized on the oxygen atom nearby $Ga_{Sn}$ (see Fig. 2(b)) also reveal the deep characteristic. This means $Ga_{Sn}$ is indeed a deep acceptor which is in agreement with the result of Scanlon and Watson [14]. Based on our results, $Ga_{Sn}$ cannot be a source of $p$-type carriers in $SnO_2$.

Recently, it has been proposed that compressive strain could shift the deep acceptor levels to shallower values [16]. It was shown that by applying (hydrostatic) compressive strain to ZnO, the acceptor level of $Na_{Zn}$ became shallower and can be used to improve the $p$-type conductivity. For the case of Ga in $SnO_2$, the bond compression in the $-1$ charge state and the configuration distortion in the neutral charge state clearly suggest that the center around Ga prefers compressive strain. In addition, the structural distortion of the neutral charge state (from *on-center* to *off-center*) results in the energy lowering by 0.5 eV. This energy lowering is partially responsible for the very deep acceptor level. In principle, without this structural relaxation, the acceptor level can be 0.5 eV shallower. By analyzing the structure, application of the compressive strain into the $SnO_2$ host helps shifting the O neighbors closers to the Ga atom (reducing the strain for the $-1$ charge state) and at the same time might be sufficient to stop the neutral charge state from distorting to the *off-center* configuration (avoiding the structural distortion energy). Therefore, we tested to apply the compressive strain into $SnO_2$ by adding another element that crystalizes in the same crystal structure as the host, but with a smaller unit cell volume. We found that $SiO_2$ also has a tetragonal rutile structure with a smaller unit cell volume than that of $SnO_2$ as shown in Table 1. Therefore, we added Si into $SnO_2$ forming $Si_xSn_{1-x}O_2$ alloy by symmetrically replacing four Sn atoms in the $SnO_2$ supercell by four Si atoms as illustrated in Fig. 1(a) and re-optimized the cell volume of $Si_xSn_{1-x}O_2$ alloy. The alloy's volume is explicitly calculated using the GGA-PBE functional. We found that the volume of the alloy is 6.22% smaller than that of $SnO_2$ as shown in Table 2. After alloying, the tetragonal-$SnO_2$ has the supercell shape transformed into an almost perfect cubic-$Si_xSn_{1-x}O_2$. As shown in Table 1, the ratio between the unit cell volume of pure $SnO_2$ and pure $SiO_2$ obtained using the GGA-

PBE and HSE functional are almost exactly the same, i.e., ~1.55. We, therefore, assume the same compression ratio, i.e., ~6.22% compression from bulk $SnO_2$, for the HSE calculations of $Si_xSn_{1-x}O_2$ alloy.

To study the effects of compressive strain on the defect transition level associated with $Ga_{Sn}$, we substituted one Ga atom on Sn's site in $Si_xSn_{1-x}O_2$ alloy. To test different Sn sites in the alloy, two different configurations were studied; (1) $Ga_{Sn}$ *inside* Si-cluster ($Ga_{Sn}^{in}$) and (2) $Ga_{Sn}$ *outside* Si-cluster ($Ga_{Sn}^{out}$) as shown in Fig. 1(b) and 1(c), respectively. We found that the relaxations of the neutral $Ga_{Sn}$ remains the same as the non-strain case and the defect transition levels are still very deep. The levels associated with $Ga_{Sn}^{in}$ and $Ga_{Sn}^{out}$ are 0.87 eV and 0.71 eV above the VBM, respectively. This indicates that the strain effect is not sufficient to enhance the p-type carrier for Ga-doped $SnO_2$. Even the best case, the acceptor level is reduced by only ~0.1 eV.

Further, we investigated whether the change in the transition levels is mainly due to the effect of compressive strain or the effect of atomic Si. We directly compressed the cell volume of $SnO_2$ with the same ratio as mentioned before without alloying with Si and then replaced one Sn atom with Ga to create $Ga_{Sn}$ defect. We found that under the compression, the defect transition level is 0.69 eV above VBM. This is about 0.1 eV lower than the uncompressed case. The compressive strain helps to make the acceptor level shallower as expected. However, the effect is too small to be useful as the level remains too deep. The defect transition levels associated with $Ga_{Sn}$ defect in bulk $SnO_2$, $Si_xSn_{1-x}O_2$ alloy, and compressed bulk $SnO_2$ are shown in Fig. 3. Because the acceptor levels in all cases remain deep, we conclude that $Ga_{Sn}$ cannot be a source of hole carrier in $SnO_2$.

### 4. Conclusion

We performed first-principles calculations with GGA-PBE and HSE functionals to study Ga in $SnO_2$ with and without compressive strain. We found that Ga acts as a deep acceptor in $SnO_2$ with the ionization energy of ~0.8 eV. We further tested the compressive strain effect on the acceptor level. We found that by applying the strain of ~6% either by direct compression or alloying with smaller cations (Si), the acceptor level can be lowered but by only about 0.1 eV and the acceptor level still too deep to be useful. Therefore, we conclude that Ga could not be the source of hole carriers in $SnO_2$.

### Conflict of Interest

We declare that we do not have any commercial or associative interest that represents a conflict of interest in connection with the work submitted.

### Acknowledgments

This work was partially supported by NANOTEC, NSTDA (Thailand) through its Center of Excellence Network program. N.P. is supported by the Thailand Research Fund through the Royal Golden Jubilee Ph.D. Program (Grant No. PHD/0180/2552) and the Thailand Center of Excellence in Physics (ThEP Center), Commission on Higher Education, Bangkok, Thailand. J.T. is supported by the Kasetsart University Research and Development Institute (KURDI). The supercomputer time was provided

by the Center for Computational Innovations (CCI) at Rensselaer Polytechnic Institute,
New York, USA.

References

[1] Z.M. Jarzebski, J.P. Marton, Physical properties of $SnO_2$ materials: II. Electrical properties, Journal of The Electrochemical Society, 123 (1976) 299C-310C.

[2] Z.M. Jarzebski, J.P. Morton, Physical properties of $SnO_2$ materials: III. Optical properties, Journal of The Electrochemical Society, 123 (1976) 333C-346C.

[3] K. Reimann, M. Steube, Experimental determination of the electronic band structure of $SnO_2$, Solid State Communications, 105 (1998) 649-652.

[4] M. Batzill, U. Diebold, The surface and materials science of tin oxide, Progress in Surface Science, 79 (2005) 47-154.

[5] H.M. Yates, P. Evans, D.W. Sheel, S. Nicolay, L. Ding, C. Ballif, The development of high performance $SnO_2$:F as TCOs for thin film silicon solar cells, Surface and Coatings Technology, 213 (2012) 167-174.

[6] G.N. Advani, A.G. Jordan, Thin films of $SnO_2$ as solid state gas sensors, Journal of Electronic Materials, 9 (1980) 29-49.

[7] S. Das, V. Jayaraman, $SnO_2$: A comprehensive review on structures and gas sensors, Progress in Materials Science, 66 (2014) 112-255.

[8] C.G. Fonstad, R.H. Rediker, Electrical properties of high- quality stannic oxide crystals, Journal of Applied Physics, 42 (1971) 2911-2918.

[9] S. Samson, C.G. Fonstad, Defect structure and electronic donor levels in stannic oxide crystals, Journal of Applied Physics, 44 (1973) 4618-4621.

[10] N. Masahiro, S. Shigeo, Properties of oxidized $SnO_2$ single crystals, Japanese Journal of Applied Physics, 10 (1971) 727.

[11] B. Stjerna, C.G. Granqvist, A. Seidel, L. Häggström, Characterization of rf- sputtered $SnO_x$ thin films by electron microscopy, Hall- effect measurement, and Mössbauer spectrometry, Journal of Applied Physics, 68 (1990) 6241-6245.

[12] A.K. Singh, A. Janotti, M. Scheffler, C.G. Van de Walle, Sources of electrical conductivity in $SnO_2$, Physical Review Letters, 101 (2008) 055502.

[13] J.B. Varley, A. Janotti, A.K. Singh, C.G. Van de Walle, Hydrogen interactions with acceptor impurities in $SnO_2$: First-principles calculations, Physical Review B, 79 (2009) 245206.

[14] D.O. Scanlon, G.W. Watson, On the possibility of p-type $SnO_2$, Journal of Materials Chemistry, 22 (2012) 25236-25245.

[15] J.P. Perdew, M. Ernzerhof, K. Burke, Rationale for mixing exact exchange with density functional approximations, The Journal of Chemical Physics, 105 (1996) 9982-9985.

[16] Y.Y. Sun, T.A. Abtew, P. Zhang, S.B. Zhang, Anisotropic polaron localization and spontaneous symmetry breaking: Comparison of cation-site acceptors in GaN and ZnO, Physical Review B, 90 (2014) 165301.

[17] Y.R. Ryu, T.S. Lee, J.A. Lubguban, A.B. Corman, H.W. White, J.H. Leem, M.S. Han, Y.S. Park, C.J. Youn, W.J. Kim, Wide-band gap oxide alloy: BeZnO, Applied Physics Letters, 88 (2006) 052103.

[18] W.H. Baur, A.A. Khan, Rutile-type compounds. IV. $SiO_2$, $GeO_2$ and a comparison with other rutile-type structures, Acta Crystallographica Section B, 27 (1971) 2133-2139.

[19] W. Baur, Über die verfeinerung der kristallstrukturbestimmung einiger vertreter des rutiltyps: TiO₂, SnO₂, GeO₂ und MgF₂, Acta Crystallographica, 9 (1956) 515-520.

[20] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented- wave method, Physical Review B, 59 (1999) 1758-1775.

[21] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Computational Materials Science, 6 (1996) 15-50.

[22] G. Kresse, J. Hafner, Norm-conserving and ultrasoft pseudopotentials for first-row and transition elements, Journal of Physics: Condensed Matter, 6 (1994) 8245.

[23] P.E. Blöchl, Projector augmented-wave method, Physical Review B, 50 (1994) 17953-17979.

[24] J. Heyd, G.E. Scuseria, M. Ernzerhof, Hybrid functionals based on a screened Coulomb potential, The Journal of Chemical Physics, 118 (2003) 8207-8215.

[25] A. Janotti, C.G. Van de Walle, Native point defects in ZnO, Physical Review B, 76 (2007) 165202.

[26] G. Makov, M.C. Payne, Periodic boundary conditions in ab initio calculations, Physical Review B, 51 (1995) 4014-4022.

[27] M. Leslie, N.J. Gillan, The energy and elastic dipole tensor of defects in ionic crystals calculated by the supercell method, Journal of Physics C: Solid State Physics, 18 (1985) 973.

[28] K.F. Young, H.P.R. Frederikse, Compilation of the static dielectric constant of inorganic solids, Journal of Physical and Chemical Reference Data, 2 (1973) 313-410.

[29] E.G. Lavut, B.I. Timofeyev, V.M. Yuldasheva, E.A. Lavut, G.L. Galchenko,

Enthalpies of formation of tin (IV) and tin (II) oxides from combustion calorimetry, The

Journal of Chemical Thermodynamics, 13 (1981) 635-646.

Table 1. The calculated lattice parameters ($a$ and $c$), internal parameter ($u$), and cell volume ($\Omega$) of $SnO_2$ and $SiO_2$ in the tetragonal rutile structure by using the GGA-PBE and HSE functionals accompanied with the corresponding experimental values.

<table>
  <thead>
    <tr>
      <th rowspan="3"></th>
      <th colspan="4">GGA-PBE</th>
      <th colspan="4">HSE</th>
      <th colspan="4">Exp.</th>
    </tr>
    <tr>
      <th>$a$</th>
      <th>$c$</th>
      <th>$u$</th>
      <th>$\Omega$</th>
      <th>$a$</th>
      <th>$c$</th>
      <th>$u$</th>
      <th>$\Omega$</th>
      <th>$a$</th>
      <th>$c$</th>
      <th>$u$</th>
      <th>$\Omega$</th>
    </tr>
    <tr>
      <th>(Å)</th>
      <th>(Å)</th>
      <th></th>
      <th>(Å³)</th>
      <th>(Å)</th>
      <th>(Å)</th>
      <th></th>
      <th>(Å³)</th>
      <th>(Å)</th>
      <th>(Å)</th>
      <th></th>
      <th>(Å³)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$SnO_2$</td>
      <td>4.77</td>
      <td>3.22</td>
      <td>0.306</td>
      <td>73.21</td>
      <td>4.74</td>
      <td>3.18</td>
      <td>0.306</td>
      <td>71.55</td>
      <td>4.74</td>
      <td>3.19</td>
      <td>0.307</td>
      <td>71.47ᵃ</td>
    </tr>
    <tr>
      <td>$SiO_2$</td>
      <td>4.19</td>
      <td>2.68</td>
      <td>0.306</td>
      <td>47.12</td>
      <td>4.16</td>
      <td>2.66</td>
      <td>0.306</td>
      <td>46.12</td>
      <td>4.18</td>
      <td>2.66</td>
      <td>0.306</td>
      <td>46.54ᵇ</td>
    </tr>
  </tbody>
</table>

ᵃReference [19]

ᵇReference [18]

**Table 2.** The calculated parameters of 72-atom SnO₂ with and without alloying with Si atom. $L_x$, $L_y$, and $L_z$ are the expanded cell dimensions in relative to the primitive cell parameters, where $L_x = L_y = 2a$ and $L_z = 3c$. The parameters for the alloy are explicitly calculated only for the GGA-PBE case. For HSE calculations, the compression ratio obtained from the GGA-PBE case (−6.22%) is used to calculate the alloy parameters relative to bulk SnO₂ (the cell shape of the alloy is approximated to be a cube, i.e., $L_x = L_y = L_z = \Omega^{1/3}$).

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">GGA-PBE</th>
      <th colspan="2">HSE</th>
    </tr>
    <tr>
      <th></th>
      <th>SnO₂</th>
      <th>SiₓSn₁₋ₓO₂</th>
      <th>SnO₂</th>
      <th>SiₓSn₁₋ₓO₂</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$L_x = L_y$ (Å)</td>
      <td>9.54</td>
      <td>9.37(44)</td>
      <td>9.48</td>
      <td>9.30</td>
    </tr>
    <tr>
      <td>$L_z$ (Å)</td>
      <td>9.65</td>
      <td>9.37(49)</td>
      <td>9.55</td>
      <td>9.30</td>
    </tr>
    <tr>
      <td>$\Omega$ (Å³)</td>
      <td>878.51</td>
      <td>823.86</td>
      <td>858.62</td>
      <td>805.20</td>
    </tr>
    <tr>
      <td>$\Delta\Omega$ (%)</td>
      <td colspan="2">−6.22</td>
      <td colspan="2">−6.22</td>
    </tr>
  </tbody>
</table>

![](./images/813130108289155074_2.jpg)

Fig. 1. Schematic illustration of the structures for $Si_xSn_{1-x}O_2$ alloy (a), $Ga_{Sn}$ in $Si_xSn_{1-x}O_2$ alloy at inside (b) and outside (c) Si-cluster configurations. The red, green, blue, and yellow balls represent Sn, O, Si, and Ga atoms, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/813130108289155074_3.jpg)

Fig. 2. (a) The total energy ($\Delta E$) of $\text{Ga}_{\text{Sn}}^0$ in bulk $\text{SnO}_2$ as a function of the Ga's displacement ($d$) near the saddle point. The total energy of the $\text{Ga}_{\text{Sn}}^0$ at the on-center configuration ($d = 0.00$ Å) is set to be zero and the vertical dashed line marks the mirror symmetry point. (b) Ga atom is moved along the Ga-O bond, as indicated by the blue arrow, until one Ga-O bond appears broken and the total energy is reduced by 0.5 eV. The localized hole states on the oxygen atom nearby $\text{Ga}_{\text{Sn}}$ are depicted as a gray colour. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/813130108289155074_4.jpg)

Fig. 3. Defect transition levels $\varepsilon(0/-)$ associated with $Ga_{Sn}$ in four configurations, i.e.,
(a) bulk $SnO_{2}$, (b) $Si_{x}Sn_{1-x}O_{2}$ alloy with inside configuration, (c) $Si_{x}Sn_{1-x}O_{2}$ with
outside configuration, and (d) $6.22\%$ compressed bulk $SnO_{2}$. In the plot, the valence
band maximum for each configuration is set to be zero.