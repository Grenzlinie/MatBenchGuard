# Tunable spin polarization and electronic structure of bottom-up synthesized $MoSi_2N_4$ materials

Rajibul Islam, $^{1, *}$ Barun Ghosh, $^{2, 3, *}$ Carmine Autieri, $^{1}$ Sugata Chowdhury, $^{4,5}$ Arun Bansil, $^{3}$ Amit Agarwal, $^{2}$ and Bahadur Singh $^{6, \dagger}$

$^{1}$International Research Centre MagTop, Institute of Physics,
Polish Academy of Sciences, Aleja Lotnikow 32/46, PL-02668 Warsaw, Poland
$^{2}$Department of Physics, Indian Institute of Technology, Kanpur 208016, India
$^{3}$Department of Physics, Northeastern University, Boston, Massachusetts 02115, USA
$^{4}$Department of Physics and Astronomy, Howard University, Washington, D.C. 20059, USA
$^{5}$IBM-HBCU Quantum Center, Howard University, Washington, D.C. 20059, USA
$^{6}$Department of Condensed Matter Physics and Materials Science,
Tata Institute of Fundamental Research, Mumbai 400005, India

Manipulation of spin-polarized electronic states of two-dimensional (2D) materials under ambient conditions is necessary for developing new quantum devices with small physical dimensions. Here, we explore spin-dependent electronic structures of ultra-thin films of recently introduced 2D synthetic materials $MSi_2Z_4$ (M = Mo or W and Z = N or As) using first-principles modeling. Stacking of $MSi_2Z_4$ monolayers is found to generate dynamically stable bilayer and bulk materials with thickness-dependent properties. When spin-orbit coupling (SOC) is included in the computations, $MSi_2N_4$ monolayers display indirect bandgaps and large spin-split states at the $K$ and $K'$ symmetry points at the corners of the Brillouin zone with nearly 100% spin polarization. The spins are locked in opposite directions along an out-of-the-plane direction at $K$ and $K'$, leading to spin-valley coupling effects. As expected, spin polarization is absent in the pristine bilayers due to the presence of inversion symmetry, but it can be induced via an external out-of-plane electric field much like the case of $Mo(W)S_2$ bilayers. A transition from an indirect to a direct bandgap can be driven by replacing N by As in $MSi_2$(N, As)$_4$ monolayers. Our study indicates that the $MSi_2Z_4$ materials can provide a viable alternative to the $MoS_2$ class of 2D materials for valleytronics and optoelectronics applications.

Introduction. Since the isolation of two-dimensional (2D) graphene from its parent graphite in 2004 [1–3], a variety of atomically thin materials have been exfoliated from bulk layered compounds with electronic states that encompass insulators to semiconductors to semimetals/metals. Prominent examples include hexagonal boron nitride [4], 2D transition-metal dichalcogenides (TMDs) [5–12], phosphorene [13, 14], and MXenes [15], among other materials [16]. These 2D materials offer exciting opportunities for exploring novel electronic, excitonic, correlated, and topological states under 2D charge confinement for spintronics, valleytronics, and optoelectronics applications and developing materials platforms for high-density devices with minimal physical dimensions. Stacking, twisting, and straining of such 2D layers to form moire superlattices and heterostructures brings unprecedented possibilities for tailoring properties [16–23]. A common approach for obtaining 2D materials is exfoliation from appropriate 3D layered materials using a top-to-bottom approach. Finding new 2D materials without parental analogs would provide a new paradigm for engineering states with diverse functionalities and offer new pathways for designing synthetic materials with desirable properties [16–23].

Among the methods of growing materials in a bottom-up approach is the use of a substrate with strong adatom adhesion. This method has shown success in synthesizing atomically thin films such as silicene [24], germanene [25], bismuthene [26], and borophene [27]. The stability and morphology of such materials are, however, strongly dependent on growth conditions due to the presence of dangling bonds of adatoms that either reorganize to generate complicated surface morphologies or get oxidized when exposed to air [28]. An alternate route proposed recently involves passivation of the high-energy surfaces of materials with elements that can generate synthetic layered 2D materials [29, 30]. By passivating non-layered molybdenum nitride with elemental silicon during chemical vapor deposition growth, large area (15 mm$\times$ 15 mm) layered 2D $MoSi_2N_4$ materials were synthesized. Importantly, $MoSi_2N_4$ shows remarkable properties such as stability under ambient conditions, a semiconducting behavior, and high mobility of $270/1200\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$, which is better than that of the widely used $MoS_2$ class of 2D materials [29–32]. $MoSi_2N_4$ and its derivative monolayers host gapped states in a pair of valleys located at the corners of the hexagonal Brillouin zone (BZ) [33–35]. Due to the breaking of the spatial inversion symmetry, the spin states in these monolayers become separated in energy and give rise to unique spin-valley couplings in the vicinity of the Fermi level and valley-contrasting Berry curvatures and orbital magnetic moments, which could potentially enable wide-ranging valleytronics and optoelectronics applications [36–42]. Despite the excellent

* These authors contributed equally to this work
$\dagger$ bahadur.singh@tifr.res.in

stability of synthetic ${\rm MoSi_2N_4}$ monolayers under ambient conditions, it is not clear how their properties evolve in the multilayer and bulk of these bottom-up grown 2D van der Waals (vdW) materials.

Motivated by the new opportunities offered by a bottom-up approach, here we report layer-dependent stability and valleytronic properties of ${\rm MSi_2Z_4}$ (M = Mo or W, and Z = N or As) materials. Using density-functional-theory based first-principles modeling, we show that the ${\rm MoSi_2N_4}$ materials are dynamically stable up to the bulk limit. The monolayers are found to exhibit large spin-split states at the BZ corners $K$ and $K'$ with nearly 100% spin-polarization, similar to the ${\rm MoS_2}$ materials class. As expected, the spin-splitting is zero in the bilayer films as the inversion symmetry is restored. However, spin-splitting can be switched on and manipulated in the bilayers via an out-of-plane electric field. An indirect to direct bandgap transition in ${\rm MSi_2Z_4}$ is driven by the replacement of N by As. In addition to highlighting the unique thickness-dependent properties of ${\rm MSi_2Z_4}$, our study demonstrates the value of a bottom-up approach for synthesizing viable 3D bulk materials based on synthetic 2D vdW materials.

Methods. Electronic structure calculations were performed within the density functional theory (DFT) framework using the Vienna ab-initio simulation package (VASP) [43, 44]. The projector augmented wave (PAW) pseudopotentials were used with generalized-gradient approximation (GGA) [45] for treating exchange-correlation effects. A plane-wave cutoff of 500 eV was used in all calculations. Surface BZ integrations were performed using a $10\times10\times1$ Monkhorst-pack $k$-grid. Effects of spin-orbit coupling (SOC) were included self-consistently. The structural parameters were optimized until the residual forces on each atom became less than $10^{-4}$ eV/Å, and these optimized parameters were used in the calculations. An energy tolerance of $10^{-8}$ eV was used. The thin-film calculations were performed using a slab geometry with a vacuum layer of 20 Å to eliminate spurious interactions between the periodically repeated 2D layers. Phonon dispersion curves were obtained within the density functional perturbation theory (DFPT) framework using PHONOPY code [46] with a $4\times4\times1$ supercell. The robustness of our GGA-based results was assessed using the optPBE-vdW correlation functional [47–51] as well as the more advanced HSE hybrid-functional [52], see Supplemental Material (SM) [53] for details. PyProcar [54] and Pymatgen [55] packages were used for band structure illustrations.

Crystal structure and dynamical stability of ${\bf MoSi_2N_4}$.
Monolayer ${\rm MoSi_2N_4}$ crystallizes in the hexagonal lattice with space group $D_{3h}^1$ ($P\overline{6}m2$, No. 187). It involves strongly-bonded, seven-layer stacking in the order N-Si-N-Mo-N-Si-N that can be viewed as a sandwich involving an ${\rm MoN_2}$ layer and two Si-N bilayers [Fig. 1(a)-(e)]. This structure preserves trigonal $C_{3v}$ and $M_z(z\rightarrow-z)$ mirror-plane symmetries but breaks the inversion symmetry. The monolayers can be stacked in the -A-B-A- order to realize a 2H bilayer structure similar to that of ${\rm MoS_2}$. Unlike the monolayer, bilayer ${\rm MoSi_2N_4}$ realizes the higher-symmetry group $D_{6h}^4$ ($P6_3/mmc$, No. 194) [29, 56], restoring the spatial center of inversion, which is marked by the red dot in Fig. 1(b). The equilibrium interlayer distance ($d_0$) between the ${\rm Mo_1}$ and ${\rm Mo_2}$ sublayers in the bilayer is found to be 10.65 Å. Notably, the 2H-bilayer structure can be repeated to realize the bulk ${\rm MoSi_2N_4}$ materials like the transition metal dichalcogenides. The optimized structural parameters and Wyckoff positions for bulk ${\rm MSi_2Z_4}$ are listed in Table I.

![](./images/867759412683473704_1.jpg)

FIG. 1. Atomic arrangement of (a) four and (b) two layers of ${\rm MoSi_2N_4}$ with AB stacking. The dashed box identifies the bulk unit cell of $2{\rm H-MoSi_2N_4}$. The red dot in the middle of the van der Waals gap in (b) marks the spatial center of inversion, which is absent in the monolayer. (c) Top view of monolayer ${\rm MoSi_2N_4}$. (d) Mo-N trigonal and (e) Si-N tetrahedral local coordination structures in ${\rm MoSi_2N_4}$ monolayers. The calculated phonon dispersion of (f) monolayer (1ML), (g) bilayer (2ML), and (h) bulk ${\rm MoSi_2N_4}$.

In order to showcase the stability of the monolayer and multilayer ${\rm MoSi_2N_4}$ films, we present the associated phonon dispersions in Figs. 1(f)-(h). The absence of imaginary phonon frequencies in the entire hexagonal BZ confirms the dynamical stability of these structures. Notably, the bulk phonon spectrum also lacks imaginary phonon frequencies. Our computations in which van der Waals interactions beyond the GGA are included yield similar results and affirm the robustness of our conclusions concerning the stability in all cases [53]. We thus infer that stable 3D bulk of ${\rm MoSi_2N_4}$ can be realized experimentally [57].

Spin-resolved electronic structure of monolayer ${\bf MoSi_2N_4}$.
The orbitally-resolved band structure of monolayer ${\rm MoSi_2N_4}$ without SOC is presented in Fig 2(a). An indirect band gap of 1.778 eV is obtained between the valence band maximum (VBM) and conduction band minimum (CBM), which are located at the

<table>
<caption>TABLE I. Calculated lattice parameters for 2H-bulk MoSi₂N₄, MoSi₂As₄, WSi₂N₄, and WSi₂As₄ using the GGA and optPBE-VDW density functionals. $a$ and $c$ are the hexagonal lattice constants and $u_{Si}$ , $u_{N/As}$, and $v_{N/As}$ are the internal parameter associated with Wyckoff positions $4e$ $(0,0,u_{Si})$, $4f$ $(\frac{1}{3},\frac{2}{3},u_{N/As})$, and $4e$ $(0,0,v_{N/As})$, respectively. The subscripts identify the atoms.</caption>
<tbody><tr><td></td><td></td><td>a (Å)</td><td>c (Å)</td><td>$u_{Si}$</td><td>$u_{N/As}$</td><td>$v_{N/As}$</td><td>$E_g$ (eV)</td></tr>
<tr><td rowspan="2">MoSi₂N₄</td><td>GGA</td><td>2.910</td><td>21.311</td><td>0.1095</td><td>0.1915</td><td>0.0859</td><td>1.655</td></tr>
<tr><td>vdW</td><td>2.932</td><td>20.772</td><td>0.1045</td><td>0.1889</td><td>0.0804</td><td>1.665</td></tr>
<tr><td rowspan="2">MoSi₂As₄</td><td>GGA</td><td>3.622</td><td>27.617</td><td>0.1106</td><td>0.1960</td><td>0.0703</td><td>0.508</td></tr>
<tr><td>vdW</td><td>3.681</td><td>27.408</td><td>0.1079</td><td>0.1950</td><td>0.0670</td><td>0.447</td></tr>
<tr><td rowspan="2">WSi₂N₄</td><td>GGA</td><td>2.914</td><td>21.439</td><td>0.1099</td><td>0.1914</td><td>0.0865</td><td>1.970</td></tr>
<tr><td>vdW</td><td>2.935</td><td>20.763</td><td>0.1043</td><td>0.1888</td><td>0.0805</td><td>1.985</td></tr>
<tr><td rowspan="2">WSi₂As₄</td><td>GGA</td><td>3.628</td><td>27.940</td><td>0.1121</td><td>0.1967</td><td>0.0723</td><td>0.207</td></tr>
<tr><td>vdW</td><td>3.685</td><td>27.397</td><td>0.1079</td><td>0.1952</td><td>0.0672</td><td>0.208</td></tr>
</tbody></table>

$\Gamma$ and $K/K'$ points, respectively. The energy difference, $\Delta_{\Gamma K}$, between the top of the valence bands at the $\Gamma$ and $K/K'$ points is 322 meV, and it can be tuned by strain to realize a direct band gap at the $K/K'$ point [33]. The Bloch wave functions at the VBM and CBM edges are composed of $d_{z^2}$ states of the Mo atoms. All states remain twofold spin degenerate without the SOC as seen in Fig. 2(a). When SOC is included, the top of the valence bands displays a large spin-splitting of 129 meV at $K$ due to the broken spatial inversion symmetry. [Since $K$ is not a time-reversal invariant momentum (TRIM) point, the spin-split states at $K$ are not twofold degenerate.] In contrast, the bands at the $\Gamma$ and $M$ points remain twofold spin degenerate as they are TRIM points [see Figs. 2(b) and (c)]. The indirect nature of the monolayer band gap, however, remains preserved with a value of 1.775 eV (2.342 eV) with GGA (HSE).

Our analysis reveals that the two spin-split states at $K$ have nearly 100% out-of-plane $(S_z)$ spin-polarization. This can be attributed to the presence of the horizontal mirror plane $M_z$ in monolayer MoSi₂N₄ that ensures that the $S_x$ and $S_y$ components of spin are zero. The spin-split states at $K$ and $K'$ are oppositely polarized since they form a Kramers pair obeying the time-reversal symmetry constraint $E(\vec{k},\uparrow)=E(-\vec{k},\downarrow)$. Figure 2(d) shows the evolution of the degree of spin-polarization of states at the top of the valence band as we go away from the $K$ point. Spin polarization decreases slightly to 99.9% for the change a momentum $\Delta k$ =0.553 Å⁻¹ (~38% of the $\Gamma-K$ distance), demonstrating its robustness. The spin texture of the state at the top of the valence band in the hexagonal BZ is shown schematically in Fig. 2(f). The preceding spin behavior is indicative of spin-valley locking in MoSi₂N₄ monolayers, which is similar to that observed previously in the TMDs [11].

We emphasize that the Zeeman-type out-of-plane spin polarization in the vicinity of $K$ points in the MoSi₂N₄ monolayer is tied to the crystal structure of the film, and therefore, it cannot be destroyed or manipulated with an out-of-plane electric field $E_z$. We have verified this property by calculating the spin-resolved band structure in the presence of an external electric field applied perpendicular to the monolayer. Figure 2(d) shows the results for $E_z = 0.03$ eV/Å. Both the spin-splitting and spin-polarization features are seen to be retained.

![](./images/867759412683473704_2.jpg)

FIG. 2.  Orbitally-resolved band structure of monolayer MoSi₂N₄ (a) without and (b) with spin-orbit coupling (SOC). Spin-resolved bands around $K$ along the $\Gamma-K$ direction for (c) $E_z = 0$ eV/Å and (d) $E_z = 0.03$ eV/Å with SOC. The color bar in (d) denotes the degree (in percent) of spin-polarization. (e) Spin-polarization decay profile of the states at the top of the valence band around the $K$ point. Large spin polarization (> 99.9%) persists over a wide momentum range along the $\Gamma-K$ direction. (f) Schematic representation of spin-valley locking in monolayer MoSi₂N₄. Red (blue) color represents spin pointing out of (into) the plane.

Tuning spin-structure of bilayer MoSi₂N₄ via an external electric field. Figure 3(a) shows the band structure of bilayer MoSi₂N₄. Similar to the monolayer case, the bilayer is an indirect bandgap semiconductor with the VBM and CBM edges located at the $\Gamma$ and $K/K'$ points, respectively. However, in contrast to the monolayer, the inversion symmetry is now restored and, as a result, all bands become twofold spin-degenerate. A small splitting at the $\Gamma$ point is driven by the interlayer interactions between the two MoSi₂N₄ layers, whereas the splitting at the $K/K'$ points is due to the SOC. The inversion symmetry of the bilayer, however, can be broken by an out-of-plane external electric field $E_z$, which

![](./images/867759412683473704_3.jpg)

FIG. 3. (a) Band structure of bilayer $MoSi_2N_4$ in the absence of external electric field ($E_z = 0$). (b) Same as (a) but for $E_z = 0.03$ eV/Å. Spin-splitting in the band structure is evident. (c) Evolution of the top four valence bands around the $K$ point with varying external electric field strength. Color scale gives the degree (in percent) of spin-polarization of the bands. Markings 1 and 2 identify the doublets associated with the first and second layers of the bilayer. (d) Degree of spin-splitting at the $K$ point as a function of $E_z$. Blue (red) markers show the intra- (inter)-layer $\Delta_{intra}$ ($\Delta_{inter}$) components of the spin-splitting. (e) A schematic of the electric-field effect on the bilayer band structure.

lifts the spin-degeneracy at the non-TRIM $K/K'$ points, allowing the manipulation of spin-split states at the top of the valence bands.

Figure 3(b) shows the spin-resolved bilayer band structure for $E_z = 0.03$ eV/Å. The spin-split states are now seen to be resolved at the $K$ and $K'$ points with opposite spin-polarizations for the top bands. There are four spin-polarized valence bands near the Fermi level, two of which originate from the first layer whereas the other two come from the second layer of the bilayer. Evolution of these four bands with $E_z$ is shown in Fig. 3(c). To quantify the spin-splitting, we introduce the quantities $\Delta_{intra}$ and $\Delta_{inter}$. Here, $\Delta_{intra}$ is defined as the energy difference between first (second) layer spin-up and first (second) layer spin-down states, while $\Delta_{inter}$ is the energy difference between the first-layer spin-up and second-layer spin-down states. $\Delta_{intra}$ thus captures the effect of the SOC on spin-splitting, whereas $\Delta_{inter}$ codes the effect of the potential difference between the two layers caused by the external field. When $E_z = 0.01$ eV/Å, the spin-split doublet from the second layer lies at an energy that is slightly lower than that for the first-layer doublet, so that $\Delta_{inter}$ is smaller than $\Delta_{intra}$. The two topmost valence states are thus composed of states belonging to two different layers of the bilayer. When $E_z$ exceeds a critical value, $\Delta_{inter}$ becomes larger than $\Delta_{intra}$ and the two topmost valence states arise from the same layer. $\Delta_{intra}$ and $\Delta_{inter}$ are shown as a function of $E_z$ in Fig. 3(d). $\Delta_{inter}$ varies linearly with $E_z$ while $\Delta_{intra}$ shows negligible field dependence. A crossover between $\Delta_{intra}$ and $\Delta_{inter}$ is observed around $E_z = 0.012$ eV/Å. Notably, the spin polarization of the topmost valence states at the $K/K'$ points remains nearly 100% in the presence $E_z$.

We find that the applied electric field changes the splitting ($\Delta_{inter}$) between the states coming from different layers in the bilayer. In contrast, as we would expect, the effect of the field on the spin-splitting as well as the degree of spin-polarization of the states coming from the same layer is negligible. Sign of the spin-polarization of states at $K/K'$ points is electric-field-direction dependent. Evolution of the states at the $K$ point under positive and negative field directions is shown schematically in Fig 3(e). These results provide a clear pathway for manipulating the spin states in bilayer $MoSi_2N_4$. Electric-field-dependent evolution of the bilayer states for all the $MSi_2Z_4$ materials we investigated falls along the preceding lines. Notably, the values of the electric field required to manipulate the states here are much lower than in $MoS_2$ [11].

![](./images/867759412683473704_4.jpg)

FIG. 4. (a) Orbitally-resolved band structure of bulk $MoSi_2N_4$ in the bulk hexagonal Brillouin zone. (b) Bandgap and (c) average spin-polarization of the top layer as a function of the number of layers.

Layer-dependent states and spin polarization. We now turn to discuss the evolution of the bandgap and spin-polarization of multilayer $MoSi_2N_4$. Figure 4(a) shows the calculated bulk band structure using our optimized lattice parameters (Table I). It has an indirect bandgap of 1.655 eV (2.221 eV) within the GGA (HSE). The wave functions at the CBM edge at $K$ and the VBM edge at $\Gamma$

![](./images/867759412683473704_5.jpg)

FIG. 5. Calculated phonon spectrum of (a) monolayer (1ML), (b) bilayer (2ML), and (c) bulk $MoSi_2As_4$. Orbitally-decomposed band structure of (d) monolayer, (e) bilayer, and (f) bulk $MoSi_2As_4$.

consist of Mo $d_{z^2}$ states similar to the monolayer and bilayer cases. The bands along the $\Gamma - A$ direction remain weakly dispersive as a result of weak interlayer coupling. However, the SOC-split states can be seen at the $K$ and $H$ points. Evolution of the bandgap as a function of the layer thickness is shown in Fig. 4(b). The bandgap decreases slightly with increasing number of $MoSi_2N_4$ layers and converges to the bulk value for the eight-layer film. This insensitivity of the bandgap to layer thickness indicates that the weak van der Waal's coupling dominates the interlayer interactions in $MoSi_2N_4$.

Figure 4(c) shows the evolution of spin-polarization of valence state as a function of the number of layers. Since the films with an even number of $MoSi_2N_4$ layers are inversion symmetric, these films display zero spin-polarization. Spin-polarization in films with an odd number of layers varies as $1/N$, where $N$ is the number of layers.

Band structure of $MSi_2Z_4$ materials. We now discuss the dynamical stabilities and band structures of other $MSi_2Z_4$ thin films. Figures 5(a)-(c) show the phonon spectra of monolayer, bilayer, and bulk $MoSi_2As_4$. No imaginary branches in the BZ are found, indicating stability of these films. Band structures of $MoSi_2As_4$ films and bulk are presented in Figs. 5(d)-(f). In contrast to $MoSi_2N_4$, the monolayer $MoSi_2As_4$ is a direct bandgap semiconductor with a bandgap of 0.508 eV (0.707 eV) within the GGA (HSE) at the $K/K'$ point. The bandgap is found to remain direct as the thickness increases from monolayer to bulk [58]. The interlayer coupling strength in $MoSi_2As_4$ is larger than in $MoSi_2N_4$, and the location of the direct bandgap changes from the $K$ to the $H$ point in going to the bulk limit [Fig. 5(f)]. $MoSi_2As_4$ monolayers also host nearly 100% spin-polarized states.

The phonon spectra and orbitally-resolved band structures of $WSi_2N_4$ and $WSi_2As_4$ are presented in the SM [53]. These systems are also stable up to the bulk limit and support highly spin-polarized states similar to the cases of $MoSi_2N_4$ and $MoSi_2As_4$. However, the W atoms with their stronger SOC yield increased spin-splittings at the $K/K'$ points in these materials.

Conclusion. Using first-principles modeling, we have carried out a systematic thickness-dependent investigation of the dynamical stabilities and electronic and spin-polarization properties of the $MSi_2Z_4$ (M = Mo or W and Z = N or As) compounds. These materials are found to be dynamically stable from the monolayer to the bulk limit, indicating that multilayer films and bulk of such bottom-up synthesized 2D vdW materials should be possible to realize experimentally. Our analysis reveals that the monolayers host two nearly 100% out-of-the-plane spin-polarized states at the $K$ points in the BZ with Zeeman-type spin splittings. The spin-polarization is reversed at the $K'$ points while the high degree of spin-polarization remains preserved. The spin-polarization of the states in the bilayers, which is zero due to the restoration of the inversion symmetry in the pristine bilayers, can be switched on and manipulated using an external electric field. $MoSi_2N_4$ and $WSi_2N_4$ exhibit a robust indirect bandgap from the monolayer to the bulk limit. In contrast, $MoSi_2As_4$ and $WSi_2As_4$ monolayers display a direct bandgap at the $K/K'$-point, which is preserved from the monolayer to the bulk. Our study provides insight into the bandgap, spin-polarization, and spin-valley locking of electronic states in $MSi_2Z_4$ materials class, and indicates that these materials could provide a viable materials platform as an alternative to the $MoS_2$ materials that are currently in common use for spintronics, valleytronics and optoelectronics applications.

## ACKNOWLEDGMENTS

We thank Tomasz Dietl for valuable discussions. The work is supported by the Foundation for Polish Science through the international research agendas program co-financed by the European union within the smart growth operational program. We acknowledge the access to the computing facilities of the Interdisciplinary Center of Modeling at the University of Warsaw, Grant Nos. G75-10, GB84-0 and GB84-7. R. I. and C. A. acknowledge support from Narodowe Centrum Nauki (NCN, National Science Centre, Poland) Project No.2020/37/N/ST3/02338. We acknowledge IIT Kanpur, Science Engineering and Research Board (SERB) and the Department of Science and Technology (DST) for financial support. The work at Northeastern University was supported by the Air Force Office of Scientific Research under award number FA9550-20-1-0322, and benefited from the computational resources of Northeastern University's Advanced Scientific Computation Center (ASCC) and the Discovery Cluster. The work at TIFR Mumbai is supported by the Department of Atomic Energy of the Government of India under project number 12-R&D-TFR-5.10-0100.

[1] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, *Science* **306**, 666 (2004).

[2] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. Grigorieva, S. Dubonos, Firsov, and AA, *Nature* **438**, 197 (2005).

[3] Y. Zhang, Y.-W. Tan, H. L. Stormer, and P. Kim, *Nature* **438**, 201 (2005).

[4] Y. Lin, T. V. Williams, and J. W. Connell, J. Phys. Chem. Lett. **1**, 277 (2010).

[5] K. F. Mak, C. Lee, J. Hone, J. Shan, and T. F. Heinz, Phys. Rev. Lett. **105**, 136805.

[6] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, *Nat. Nanotechnol.* **7**, 699 (2012).

[7] M. Chhowalla, H. S. Shin, G. Eda, L.-J. Li, K. P. Loh, and H. Zhang, *Nat. Chem.* **5**, 263 (2013).

[8] X. Huang, Z. Zeng, and H. Zhang, *Chem. Soc. Rev.* **42**, 1934 (2013).

[9] C. Tan and H. Zhang, *Chem. Soc. Rev.* **44**, 2713 (2015).

[10] H. Yuan, M. S. Bahramy, K. Morimoto, S. Wu, K. Nomura, B.-J. Yang, H. Shimotani, R. Suzuki, M. Toh, C. Kloc, X. Xu, R. Arita, N. Nagaosa, and Y. Iwasa, *Nat. Phys.* **9**, 563 (2013).

[11] T.-R. Chang, H. Lin, H.-T. Jeng, and A. Bansil, *Sci. Rep.* **4**, 6270 (2014).

[12] N. Morell, S. Tsepsic, A. Reserbat-Plantey, A. Cepellotti, M. Manca, I. Epstein, A. Isacsson, X. Marie, F. Mauri, and A. Bachtold, *Nano Lett.* **19**, 3143 (2019).

[13] L. Li, Y. Yu, G. J. Ye, Q. Ge, X. Ou, H. Wu, D. Feng, X. H. Chen, and Y. Zhang, *Nat. Nanotechnol.* **9**, 372 (2014).

[14] H. Liu, Y. Du, Y. Deng, and D. Y. Peide, *Chem. Soc. Rev.* **44**, 2732 (2015).

[15] M. Naguib, V. N. Mochalin, M. W. Barsoum, and Y. Gogotsi, *Adv. Mater.* **26**, 992 (2014).

[16] K. Novoselov, O. A. Mishchenko, O. A. Carvalho, and A. C. Neto, *Science* **353** (2016).

[17] K. S. Novoselov and A. H. C. Neto, *Phys. Scr.* **T146**, 014006 (2012).

[18] T. Heine, *Acc. Chem. Res.* **48**, 65 (2015).

[19] Y. Gong, J. Lin, X. Wang, G. Shi, S. Lei, Z. Lin, X. Zou, G. Ye, R. Vajtai, B. I. Yakobson, *et al.*, *Nat. Mater.* **13**, 1135 (2014).

[20] J. Wang, F. Ma, and M. Sun, *RSC Adv.* **7**, 16801 (2017).

[21] Y. Cao, V. Fatemi, S. Fang, K. Watanabe, T. Taniguchi, E. Kaxiras, and P. Jarillo-Herrero, *Nature* **556**, 43 (2018).

[22] C. Chen, B. Singh, H. Lin, and V. M. Pereira, *Phys. Rev. Lett.* **121**, 226602 (2018).

[23] A. Vargas, F. Liu, C. Lane, D. Rubin, I. Bilgin, Z. Hennighausen, M. DeCapua, A. Bansil, and S. Kar, *Sci. Adv.* **3**, e1601741 (2017).

[24] A. Fleurence, R. Friedlein, T. Ozaki, H. Kawai, Y. Wang, and Y. Yamada-Takamura, *Phys. Rev. Lett.* **108**, 245501 (2012).

[25] M. E. Dávila, L. Xian, S. Cahangirov, A. Rubio, and G. L. Lay, *New J. Phys.* **16**, 095002 (2014).

[26] L. Cheng, H. Liu, X. Tan, J. Zhang, J. Wei, H. Lv, J. Shi, and X. Tang, *J. Phys. Chem. C* **118**, 904 (2014).

[27] B. Feng, O. Sugino, R.-Y. Liu, J. Zhang, R. Yukawa, M. Kawamura, T. Iimori, H. Kim, Y. Hasegawa, H. Li, L. Chen, K. Wu, H. Kumigashira, F. Komori, T.-C. Chiang, S. Meng, and I. Matsuda, *Phys. Rev. Lett.* **118**, 096401 (2017).

[28] C. Grazianetti, D. Chiappe, E. Cinquanta, M. Fanciulli, and A. Molle, *J. Condens. Matter Phys.* **27**, 255005 (2015).

[29] Y.-L. Hong, Z. Liu, L. Wang, T. Zhou, W. Ma, C. Xu, S. Feng, L. Chen, M.-L. Chen, D.-M. Sun, *et al.*, *Science* **369**, 670 (2020).

[30] K. S. Novoselov, *Natl. Sci. Rev.* **7**, 1842 (2020).

[31] S. Bertolazzi, J. Brivio, and A. Kis, *ACS nano* **5**, 9703 (2011).

[32] Y. Cai, G. Zhang, and Y.-W. Zhang, *J. Am. Chem. Soc.* **136**, 6269 (2014).

[33] S. Li, W. Wu, X. Feng, S. Guan, W. Feng, Y. Yao, and S. A. Yang, *Phys. Rev. B* **102**, 235435 (2020).

[34] H. Ai, D. Liu, J. Geng, S. Wang, K. H. Lo, and H. Pan, *Phys. Chem. Chem. Phys.* **23**, 3144 (2021).

[35] C. Yang, Z. Song, X. Sun, and J. Lu, *Phys. Rev. B* **103**, 035308 (2021).

[36] O. Gunawan, Y. P. Shkolnikov, K. Vakili, T. Gokmen, E. P. De Poortere, and M. Shayegan, *Phys. Rev. Lett.* **97**, 186404 (2006).

[37] D. Xiao, W. Yao, and Q. Niu, *Phys. Rev. Lett.* **99**, 236809 (2007).

[38] D. Gunlycke and C. T. White, *Phys. Rev. Lett.* **106**, 136806 (2011).

[39] D. Xiao, G.-B. Liu, W. Feng, X. Xu, and W. Yao, *Phys. Rev. Lett.* **108**, 196802 (2012).

[40] T. Cai, S. A. Yang, X. Li, F. Zhang, J. Shi, W. Yao, and Q. Niu, *Phys. Rev. B* **88**, 115140 (2013).

[41] X. Xu, W. Yao, D. Xiao, and T. F. Heinz, *Nat. Phys.* **10**, 343 (2014).

[42] C. Autieri, A. Bouhon, and B. Sanyal, *Philos. Mag.* **97**, 3381 (2017).

[43] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

[44] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[45] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[46] A. Togo and I. Tanaka, *Scr. Mater.* **108**, 1 (2015).

[47] J. c. v. Klimeš, D. R. Bowler, and A. Michaelides, *Phys. Rev. B* **83**, 195131 (2011).

[48] J. Klimeš, D. R. Bowler, and A. Michaelides, *J. Phys.: Cond. Matt.* **22**, 022201 (2009).

[49] I. Mosyagin, D. Gambino, D. G. Sangiovanni, I. A. Abrikosov, and N. M. Caffrey, *Phys. Rev. B* **98**, 174103 (2018).

[50] F. Conte, D. Ninno, and G. Cantele, *Phys. Rev. Research* **2**, 033001 (2020).

[51] D. Chakraborty, K. Berland, and T. Thonhauser, *Journal of Chemical Theory and Computation* **16**, 5893 (2020).

[52] J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **118**, 8207 (2003).

[53] *See Supplemental Material at "URL will be inserted here" for exchange-correlation functional dependent properties of MSi₂Z₄, layer dependent stability and band structure of WSi₂Z₄, and adhesion energy of all the studied materials.*

[54] U. Herath, P. Tavadze, X. He, E. Bousquet, S. Singh, F. Munoz, and A. H. Romero, *Comput. Phys. Commun.*

251, 107080 (2020).

[55] S. P. Ong, W. D. Richards, A. Jain, G. Hautier, M. Kocher, S. Cholia, D. Gunter, V. L. Chevrier, K. A. Persson, and G. Ceder, Comput. Mater. Sci. 68, 314 (2013).

[56] H. Zhong, W. Xiong, P. Lv, J. Yu, and S. Yuan, Phys. Rev. B 103, 085124 (2021).

[57] Notably, the thickness-dependent stability of 2D $MoSi_2Z_4$ materials indicates that multilayers and bulk of these materials should be possible to realize experi- mentally. Our results here should be contrasted with the thickness-dependent stability studies in the literature on various 2D materials synthesized using a top-to-bottom approach from a stable bulk. It is not clear a priori that stability in top-to-bottom synthesis ensures a similar sta- bility in the bottom-up synthesis.

[58] The calculated HSE band structure with the opti- mized geometry obtained using the GGA and optPBE- vdW functional remains direct from monolayer to bulk $MoSi_2As_4$.