# Thermal conductivity of $Bi_2Se_3$ from bulk to thin films: Theory and experiment

Lorenzo Paulatto
Sorbonne Université, CNRS, Institut de Minéralogie, de Physique des Matériaux et de Cosmochimie, IMPMC, UMR 7590, 4 place Jussieu, 75252 Paris Cedex 05, France

Danièle Fournier, Massimiliano Marangolo, Mahmoud Eddrief, Paola Atkinson, and Matteo Calandra
Sorbonne Université, CNRS, Institut des NanoSciences de Paris, INSP, UMR 7588, F-75005 Paris, France

![](./images/812638290623594496_1.jpg)
(Received 13 December 2019; revised manuscript received 22 March 2020; accepted 27 April 2020; published 19 May 2020)

We calculate the lattice-driven in-plane ($\kappa_\parallel$) and out-of-plane ($\kappa_\perp$) thermal conductivities of $Bi_2Se_3$ bulk, and of films of different thicknesses, using the Boltzmann equation with phonon scattering times obtained from anharmonic third order density functional perturbation theory. We compare our results for the lattice component of the thermal conductivity with published data for $\kappa_\parallel$ on bulk samples and with our room-temperature thermoreflectance measurements of $\kappa_\perp$ on films of thickness ($L$) ranging from 18 nm to 191 nm, where the lattice component has been extracted via the Wiedemann-Franz law. Ab initio theoretical calculations on bulk samples, including an effective model to account for finite sample thickness and defect scattering, compare favorably both for the bulk case (from literature) and thin films (new measurements). In the low-$T$ limit the theoretical in-plane lattice thermal conductivity of bulk $Bi_2Se_3$ agrees with previous measurements by assuming the occurrence of intercalated $Bi_2$ layer defects. The measured thermal conductivity monotonically decreases by reducing $L$; its value is $\kappa_\perp \approx 0.39 \pm 0.08$ W/m K for $L = 18$ nm and $\kappa_\perp = 0.68 \pm 0.14$ W/m K for $L = 191$ nm. We show that the decrease of room-temperature $\kappa_\perp$ in $Bi_2Se_3$ thin films as a function of sample thickness can be explained by the incoherent scattering of out-of-plane momentum phonons with the film surface. Our work outlines the crucial role of sample thinning in reducing the out-of-plane thermal conductivity.

DOI: 10.1103/PhysRevB.101.205419

## I. INTRODUCTION

While the thermoelectric properties of $Bi_2Te_3$ have been widely studied both for bulk and thin films [1], interest in the isostructural topological insulator $Bi_2Se_3$ mostly focused on its peculiar electronic structure and little is known on its thermal conductivity. The main reason is that its Seebeck coefficient is lower than that of $Bi_2Te_3$ and its thermal conductivity is somewhat higher, leading to a worse thermoelectric figure of merit $ZT$. Notwithstanding that, the situation could be different in $Bi_2Se_3$ thin films, where thermal conductivity could be reduced due to scattering with sample borders [2]. Little is known of the thermal conductivity in this case.

$Bi_2Se_3$, similarly to $Bi_2Te_3$, has a lamellar structure, consisting of sheets of covalently bonded Se-Bi-Se-Bi-Se atoms that are held together by weak interlayer van-der-Waals bonds. This highly anisotropic crystal structure is reflected in anisotropic thermal and electrical conductivity. Thermal conductivity of bulk $Bi_2Se_3$ has been measured by several authors. Navratil and coworkers [3,4] measured the thermoelectric properties and the in-plane thermal conductivity in bulk $Bi_2Se_3$ and extracted the lattice contribution to $\kappa_\parallel$ (lying in the plane of the $Bi_2Se_3$ layers, perpendicular to the [111] direction). They find values of the order of 1.33-1.63 W/m K at room temperature. Furthermore, the authors found a drop of $\kappa_\parallel$ at low temperatures which they attribute to the presence of charged Se vacancies.

There is a certain variance in experimental values of $\kappa$: In Ref. [5] and for $p$-doped samples, the in-plane conductivity was found to be of the order of 1.25 (W/m K), however the lattice contribution was not extracted. The room-temperature total lattice and electronic conductivity were also estimated in Ref. [6] and found to be 2.83 W/m K and 1.48 W/m K, respectively. More recently, the total in-plane thermal conductivity was estimated to be 3.5 W/m K [7].

In this work we present a detailed theoretical and experimental investigation of the thickness dependence of the out-of-plane thermal conductivity $\kappa_\perp$ for thin films grown by molecular beam epitaxy and having a thickness $L$ between 18 and 191 nm. We find that the out-of-plane thermal conductivity decreases monotonically with thickness. By using first-principles electronic structure calculations, we show that this is mostly due to the suppression of long-wavelength phonon propagating along the $c$ axis. Moreover, we show that the low temperature behavior of the lattice component of the thermal conductivity is mostly due to intercalated $Bi_2$ layers and not to Se vacancies, as suggested in previous works [3,4].

In Sec. II we present the experimental setup and techniques used to grow and measure the conductivity in thin films. In Sec. III we review and extend the theory of phonon-driven thermal transport in finite crystals. We report in Sec. IV A the computational details, in Sec. IV B the crystal geometry, and in Sec. IV C we compute the electronic contribution to thermal

*lorenzo.paulatto@sorbonne-universite.fr
---
2469-9950/2020/101(20)/205419(10)
205419-1
©2020 American Physical Society

conductivity via the Franz-Wiedemann law. In Sec. V we present our results on electronic structure (Sec. V A), phonon dispersion (Sec. V B), bulk thermal conductivity (Sec. V C), and thin films (Sec. V D).

## II. EXPERIMENT

### A. Thermal conductivity measurements

Thermal properties of thin films may be obtained at room temperature using modulated thermoreflectance microscopy [8,9]. In this setup the heat diffusion associated with a heat source created by an intensity modulated pump beam is measured at the sample surface using the variation in the coefficient of optical reflection, which is measured by a probe beam impinging the heated area. The pump beam is a 532 nm Cobolt laser focused on the sample through a ×50 (0.5 NA) objective microscope. The pump laser is intensity modulated in a frequency range 100 Hz–1 M Hz. Since the light penetration depth is around 10 nm a large amount of heat is released in the thin film.

Surface temperature is then affected by heat diffusion carried by thermal waves [8,9]. The setup permits a spatial measurement of the surface temperature around the pump beam by a probe 488 nm Oxxius laser that is reflected on the heated surface. The variations of the reflectivity (amplitude and phase) are directly proportional to the modulated temperature variation through the refractive index variation and measured by a lock-in amplifier. To avoid artifacts due to variations in the optical quality of the surface, the probe beam is fixed on a small good quality area, while the pump beam is scanned around the probe beam. Finally, the amplitude and phase experimental data are fitted according to a standard Fourier diffusion law to extract the thermal parameters (thermal conductivity $k$ and/or thermal diffusivity $D$):

$$
D = k/d\ C, \tag{1}
$$

where $d$ is the sample density and $C$ its specific heat [10–15].

### B. Thin films growth

The growth of ${\text{Bi}}_{2}{\text{Se}}_{3}$ thin films was conducted by molecular beam epitaxy by following the procedure given in Ref. [16]. Flat (111)-B GaAs buffer surfaces were prepared in the III-V chamber and subsequently transferred to a second chamber where ${\text{Bi}}_{2}{\text{Se}}_{3}$ thin films were grown with thicknesses ranging from 18 nm up to 190 nm. The crystalline quality, epitaxial in-plane orientation, lattice parameter, crystalline structure of ${\text{Bi}}_{2}{\text{Se}}_{3}$ films were verified by reflection high-energy electron diffraction and x-ray diffraction. Surfaces are very flat ($\sim$5 nm rms roughness) and mirrorlike facilitating the reflectivity measurements.

## III. THEORY

### A. Scattering mechanisms in finite crystals

The behavior of lattice-driven thermal conductivity as a function of temperature has a typical shape which is mostly independent of the material: At high temperature it decreases as $1/T$, at lower temperature it has a maximum, then going towards zero temperature it decreases sharply to a finite value. The behavior of the lattice thermal conductivity at high temperature is determined by the anharmonic phonon-phonon interactions [17] with a contribution from defects. In the low temperature regime, named after Casimir who studied it in the 1930’s [18], thermal conductivity is not a bulk property but it depends on the sample finite size [18].

![](./images/812638290623594496_2.jpg)

FIG. 1. Possible scattering mechanisms in a slab-shaped crystal. (1) Normal momentum-conserving scattering (does not limit thermal transport). (2) Umklapp scattering. Absorption by: (3) point defects or isotopic disorder, or (4) rough “black” surface, with black-body emission to maintain thermal equilibrium. (5) Reflection by a rough “white” surface. (6) Reflection by a smooth surface. (7) Transmission through an intercalated surface.

Theoretical studies of the Casimir regime predate the possibility to study thermal conductivity by numerically integrating the phonon anharmonic properties [18–20]. The standard approach consists in modeling the sample boundaries as black bodies that absorb a fraction of the colliding phonons, reflect the rest, and emit phonons to maintain thermal equilibrium. These works use geometric calculations, valid in the linear regime where only the acoustic phonons are taken into account, to predict the low-temperature thermal conductivity, usually with a single free parameter: the surface reflectivity. Invariably they assume a simple geometry for the crystal, such as a long cylinder or a long square parallelepiped with a temperature gradient between its opposite faces; in a shorter cylinder with polished faces the model requires the inclusion of multiple internal reflections [20].

With the arrival of more powerful numerical techniques, it has become more effective to model the surface at the phonon level, as a scattering probability. The probability of scattering from the boundaries can be combined with the probability of scattering due to phonon-phonon interaction in accordance with Matthiessen’s rule [21]. This approach has been used in more recent literature [22] while keeping the assumptions of the long cylindrical geometry, not appropriate for application to thin films, where a temperature gradient can be applied orthogonally to the film lateral extension.

In Fig. 1 we have schematically depicted the possible scattering events responsible for limiting lattice-driven energy flow; we will briefly review them but for detailed discussion we redirect the reader to Ref. [23]. Mechanisms (1) and (2) are the intrinsic scattering processes: (1) is the “normal” (N) scattering, it conserves momentum and does not limit

thermal conductivity. N scattering is only important at very low temperature (a few K). (2) The umklapp (U) processes, that conserve crystal momentum modulus the addition of a reciprocal lattice vector, are the main limiting factor at high temperature and the prevalent intrinsic scattering mecha- nism. When studying thermal conductivity in the single-mode relaxation-time approximation (SMA), it is assumed that U scattering is dominant and that the scattered phonons are thermalized, i.e., that on average they are scattered toward the equilibrium thermal distribution. This approximation is very robust and works to within a few percent in a large range of temperatures and materials [24].

Diagram number (3) depicts the Rayleigh scattering with a point defect, which could be a vacancy [25], a substitutional defect, or isotopic disorder [21]. Finally, events (4), (5), (6), and (7) are possible interactions between a phonon and the sample boundary: (4) is adsorption and re-emission by the surface; (5) is inelastic reflection by a "white" surface. We remark that, as it has been shown in Ref. [20], events (4) and (5) are equivalent from a thermal-transport point of view, we will just use (4) from here on. Further on, (6) is elastic reflection, where the momentum component parallel to the surface is conserved but the orthogonal component is inverted. Reflections can limit thermal conductivity in the direction orthogonal to the surface. Finally, in (7) a phonon can cross the boundary without scattering; this is of course not possible if the sample is suspended in vacuum but can be the case if the sample is composed by multiple mismatched segments or if it contains stacking defects.

In order to describe the interface, we introduce three di- mensionless parameters: the absorption fraction $f_{a}$, the re flection fraction $f_{r}$, and the transmission $f_{t}$; these are the probabilities that a phonon will undergo process (4), (6), or (7), respectively, when it collides with the boundary. The condition $f_{a}+f_{r}+f_{t}=1$ holds. In general these parameters may depend on phonon energy and its incidence angle; they can be computed using molecular dynamics techniques [26]. A special limit case is a very rough surface for which $f_{a}=1$.

### B. Thermal transport in the single-mode approximation
In the single mode approximation (SMA) the thermal conductivity matrix is:
$$
\kappa_{\alpha \beta}=\frac{\hbar^{2}}{N_{0} \Omega k_{B} T^{2}} \sum_{j} v_{\alpha, j} v_{\beta, j} \omega_{j}^{2} n_{j}\left(n_{j}+1\right) \tau_{j} \quad (2)
$$
where $j$ is a composite index running over the phonon wave vectors $\mathbf{q}$ in reciprocal space and the phonon bands $v$; $N_{0}$ are the number of $\mathbf{q}$ points used to sample the Brillouin zone, $\Omega$ is the unit-cell volume, $k_{B}$ is the Boltzmann constant, and $T$ is temperature. Inside the sum, the composite index $j$ stands for the band index $v$ and the wave vector $\mathbf{q}$; then $\omega_{j}=\omega_{v}(\mathbf{q})$ is the phonon frequency, $v_{j}=\nabla_{\mathbf{q}} \omega_{v}(\mathbf{q})$ is the phonon group velocity, $\alpha$ and $\beta$ are cartesian directions, $(x, y, z) n_{j}=n(\omega_{v}(\mathbf{q}))$ is the Bose-Einstein distribution, and $\tau_{j}$ is the phonon relaxation time, or inverse full width at half maximum [27].

The SMA is accurate when Umklapp or dissipative scat- tering is dominant over "normal" and elastic scattering; wehave checked that this is always the case in $Bi_{2} Se_{3}$ above $1 ~K$ : Above this temperature the exact solution of the Boltzmann transport equation (BTE) [23] only increases $k$ by a couple percent. As the SMA equation is much cheaper to compute, easier to manipulate, and has a more straightforward interpre- tation, we will use it exclusively in the rest of the paper.

### C. Thermal transport in thin film crystals
In order to progress further we have to take into account the real geometry of our sample. In this paper we will consider two cases: (i) a thin film of $Bi_{2} Se_{3}$ of thickness $L$ along direction $z$ and virtually infinite in the other two directionswith two very rough opposing surfaces; (ii) bulk $Bi_{2} Se_{3}$  intercalated with partial planes of $Bi_{2}$ , which is a common kind of crystal defect [16,28], at an average distance $L$ .

In case (i) we consider a phonon emitted from a surface that moves toward the opposite surface with a $z$ component of its group velocity $v_{z}$ . After a time $L / v_{z}$ , the phonon will reach the other surface and be absorbed with probability $f_{a}$ , giving the first phonon scattering rate $\gamma_{a}^{(1)}$ and the relaxationtime $(\tau_{a}^{(0)})^{-1}=f_{a} \frac{v_{z}}{L}$ . If it is not absorbed (probability $f_{r}=$ 1 - fa), the phonon will be reflected back toward the initial surface with identical speed and it will undergo a second absorption/reflection process. The probability of a third re- flection is $f_{r}^{2}$ , for the $n$ th reflection is is $f_{r}^{(n-1)}$ . After summingthe geometric series, the total effective lifetime is:
$$
\left(\tau_{a}\right)^{-1}=2 \gamma_{a}=f_{a} \frac{v_{z}}{L} \sum_{i=1, n} f_{r}^{i-1}=\frac{v_{z}}{L}\left(\frac{f_{a}}{1-f_{r}}\right). \quad (3)
$$

For boundary scattering, $f_{a}=1-f_{r}$ conveniently cancels out giving $\tau_{a}=\frac{L}{v_{z}}$ , but we prefer to leave Eq. (3) in a general form to consider more general cases. Furthermore, if a phonon is reflected, its velocity component that is orthogonal to the surface will be inverted. We can account for this possibility in Eq. (2) renormalizing $v_{z}$ in the following way: A fraction $f_{r}$ of the phonons will change the sign of $v_{z}$ , a fraction of them will hit the opposite boundary, be reflected a second time and change sign again, and so on. The material is traversed in a "flying" time $\tau_{f}=L / v_{z}$ . During this time phonons arescattered at a rate $P_{x}=\tau / \tau_{f}$ , resetting the process, with $\tau$  being its total (intrinsic and extrinsic) relaxation time. Thiscan be expressed as:
$$
\tilde{v}_{z}=\sum_{i=0, \infty}\left(-\frac{\tau_{f}}{\tau} f_{r}\right)^{i} v_{z}=v_{z}\left(1+\frac{\tau}{\tau_{f}} f_{r}\right)^{-1}. \quad (4)
$$

Again, we do not replace $\tau_{f}$ with $1-\tau_{a}$ because we want to keep this equation as general as possible. In case (ii), a bulk material intercalated with planes, the reasoning is very similar, with the caveat that $1-f_{a}=f_{r}+f_{t}$ , although for an atom thin intercalated layer we can safely assume that $f_{r}$ is almost zero.

The final formula for $\kappa$ becomes:
$$
\kappa_{\alpha \beta}=\frac{\hbar^{2}}{N_{0} \Omega k_{B} T^{2}} \sum_{j} \tilde{v}_{\alpha, j} \tilde{v}_{\beta, j} \omega_{j}^{2} n_{j}\left(n_{j}+1\right) \tau_{j}^{t \alpha} \quad (5)
$$

with $\tilde{v}$ from Eq. (4), and $\tau$ comprises all the scattering terms, summed with the Matthiessen's rule:
$$
\tau^{t o t}=\left(\tau_{p h-p h}^{-1}+\tau_{a}^{-1}+\ldots\right)^{-1} \tag{6}
$$
where additional scattering terms like point-defect scattering can be added. In the case of $\mathrm{Bi}_{2} \mathrm{Se}_{3}$ we will see in Sec. $\mathrm{V} \mathrm{D}$ the impact that internally reflected phonon have on the conductivity. We also underline that while our samples are not freestanding in the experiment, we assume that, on the timescale of the measurements, the transmission of heat from $\mathrm{Bi}_{2} \mathrm{Se}_{3}$ to the GaAs substrate can be ignored.

## IV. TECHNICAL DETAILS OF FIRST-PRINCIPLES SIMULATIONS

### A. Computational method

All calculations have been performed using the QUANTUMESPRESSO suite of codes [29,30], and in particular PH [31] and D3Q [27] modules. D3Q efficiently computes three-body anharmonic force constants from density functional perturbation theory [32-34] and the " $2 n+1$ " theorem [35,36]. We also used the related THERMAL2 codes [23,27] to compute intrinsic phonon lifetime, scattering with isotopic defects [21] and border effects and to compute lattice-driven thermal conductivity in the single-mode relaxation time approximation (RTA) and by solving iteratively the full Peierls-Boltzmann [17] transport equation via a functional minimization [23].

We used the generalized gradient approximation with the PBE [37] parametrization. We employed norm-conserving pseudopotentials from the SG15-ONCV library [38-40], which include scalar-relativistic effects, and custom made pseudopotentials based on the SG15-ONCV pseudisation parameters, but including full-relativistic spin-orbit coupling (SOC). The PH code includes SOC effects [41], but the D3Q code does not, hence we always used scalar-relativistic pseudopotentials for the third order calculations.

We used a kinetic energy cutoff of 40 Ry for the plane wave basis set, and we integrated the electronic states of the Brillouin zone (BZ) using a regular Monkhorst-Pack grid of $8 \times 8 \times 8 k$ points, except when computing the effective charges and static dielectric constant via linear response, which only converged with a much finer grid of $32 \times 32 \times 32$ points.

The phonon-phonon interaction was integrated using a very fine grid of $31 \times 31 \times 31 q$ points, when computing the linewidth along high-symmetry direction or the phonon spectral weight. A coarser grid of $19 \times 19 \times 19$ points was used when computing the thermal conductivity. The SMA thermal Boltzmann equation was itself integrated over a grid $19 \times 19 \times 19 q$ points. All the grids in this paragraph were shifted by a random amount in order to improve convergence avoiding symmetry-equivalent points. The finite size effects of section III C where included in the calculation of $\kappa$ using an in-house Octave [42] code available upon request.

### B. Simulated crystal structure

$\mathrm{Bi}_{2} \mathrm{Se}_{3}$ belongs to the tetradymite-type crystal with a rhombohedral structure (point group $R \overline{3} m$, Wyckoff number 166). In the rhombohedral unit cell there are three Se and two $\mathrm{Bi}$ atoms. One Se atom is at the (1a) site (0,0,0); the remaining $\mathrm{Se}$ and $\mathrm{Bi}$ atoms are at the twofold $(2 c)$ sites of coordinates $(u, u, u)$ and $(-u,-u,-u)$, with one free parameter for each species, which we indicate as $u_{\mathrm{Se}}$ and $u_{\mathrm{Bi}}$, respectively. Structural parameters obtained from experimental measurement and from $a b$ initio simulations are shown in Table I. Both the scalar relativistic and the fully relativistic PBE calculations give substantially expanded structures, both in $a$ and $c$, as is customary in this approximation. As the electronic band gap is quite sensitive to the geometry, we also calculated the band gap for the experimental volume. In all fully relativistic calculations the gap is substantially overestimated, in agreement with previous theoretical calculations.

$\mathrm{Bi}_{2} \mathrm{Se}_{3}$ thin films measured here had thicknesses between $18 \mathrm{~nm}$ and $191 \mathrm{~nm}$. The stack of $2 \mathrm{Bi}$ and $3 \mathrm{Se}$ atoms (one Q layer) is $0.984 \mathrm{~nm}$ thick, which means that even for the thinnest slab we have 18 or 19 Q layers.

### C. Electronic contribution to thermal conductivity

Commercially available bulk $\mathrm{Bi}_{2} \mathrm{Se}_{3}$ samples, and our epitaxial $\mathrm{Bi}_{2} \mathrm{Se}_{3}$ thin film samples, are always doped to a

TABLE I. Structural parameters of bulk $\mathrm{Bi}_{2} \mathrm{Se}_{3}$ : lattice parameters, $a, c$, unit cell volume $V$, lattice positions of Se and $\mathrm{Bi}, u_{\mathrm{Se}}, u_{\mathrm{Bi}}$, and the bulk band gap. Experimental data (Ref. [44]) is given and compared with the scalar relativistic (SR) and fully relativistic (SOC) calculations of this work where theoretically determined or experimentally determined lattice parameters were used as model input. Last row: results from literature DFT simulation.

|          | Structure          | $a$ (Å) | $c$ (Å) | $\mathrm{V}\left(\AA^{3}\right)$ | $u_{\mathrm{Se}}$ | $u_{\mathrm{Bi}}$ | gap (meV) |
|----------|--------------------|---------|---------|-----------------------------------|-------------------|-------------------|-----------|
|----------| Experimental:      | 4.138   | 28.64   | 422.8                             |                   |                   | $200 \pm 5$ |
| Approximation structure |        | $a$ (Å) | $c$ (Å) | $\mathrm{V}\left(\AA^{3}\right)$ | $u_{\mathrm{Se}}$ | $u_{\mathrm{Bi}}$ | gap (meV) |
|          | This paper:        |         |         |                                   |                   |                   |           |
| SR       | theoretical        | 4.198   | 30.12   | 459.6                             | 0.217             | 0.398             | 471       |
| SOC      | theoretical        | 4.211   | 29.76   | 457.0                             | 0.215             | 0.399             | 373       |
| SR       | experimental $^{\mathrm{a}}$ | 4.138 | 28.64 | 422.8                             | 0.211             | 0.400             | 183       |
| SOC      | experimental $^{\mathrm{a}}$ | 4.138 | 28.64 | 422.8                             | 0.209             | 0.401             | $333 / 444^{\mathrm{b}}$ |
|          | DFT simulations in literature: | | | | | | |
| SOC/VASP | experimental [43]  | 4.138   | 28.64   | 422.8                             |                   |                   | 320       |

$^{\mathrm{a}}$ Lattice parameters from Ref. [45] as in Ref. [43], also compatible with Ref. [46]
$^{\mathrm{b}}$ Indirect/direct gap.

205419-4

certain extent by the presence of vacancies and imperfect stoichiometry. For this reason, even if the perfect material is a small gap insulator, we expect to measure a certain amount of electron/hole driven thermal and electric transport. Although there is no simple way to isolate the electronic contribution to thermal transport ($k_e$), we can estimate it from electric conductivity. Mobility ($\mu$), doping, and electrical resistivity ($\rho_\parallel$) of most of the thin films have been measured by conventional Hall bar measurements performed in the plane perpendicular to the trigonal axis, $c$, of ${\rm Bi_2Se_3}$ thin films.

It turns out that, at 300 K our thin films are $n$ doped and present a metallic behavior with a carrier concentration between $1$--$2\times 10^{19}$ cm$^{-3}$, $\mu\sim300$--$400$ cm$^2$/V s, and $\rho_\parallel\sim$ 1--1.5 m$\Omega$ cm. A coarse evaluation of the electronic contribution to the in-plane thermal conductivity, $k_{e,\parallel}$, can be given by using the Wiedemann-Franz law $k_{e,\parallel}=LT/\rho_\parallel$, with $L$ ranging between 2 and $2.2\times 10^{-8}$ V$^2$ K$^{-2}$ [3]. Consequently, $k_{e,\parallel}$ at 300 K ranges between 0.4--0.7 W/m$\Omega$ K.

Concerning the out-of-plane resistivity term, $\rho_\perp$, a rough estimation can be given by $\rho_\perp\sim3.5\rho_\parallel$ since such a ratio is found in bulk ${\rm Bi_2Se_3}$ [47] leading to $k_{e,\perp}$ between 0.1--0.2 W/m K. It is worthwhile to underline that $\rho_\parallel$ measurements performed in very thin ${\rm Bi_2Se_3}$ samples (9 QL) give a slight lowering of the resistivity (0.7 m$^2$ cm), which may be caused by $k_{e,\perp}$ slightly increasing at very low thickness.

## V. RESULTS AND DISCUSSION

### A. Electronic structure

Before delving in the calculation of the vibrational properties, we have taken care to verify that the approximations used to deal with the $ab$ initio problem are valid. A few potential difficulties have to be accounted for: the first is that ${\rm Bi_2Se_3}$ is a small gap semiconductor, and special care is needed in order to prevent the gap from closing. The gap magnitude depends both on the kind of local- or semilocal-exchange and correlation kernels and on the lattice geometry used. In any case, the Kohn-Sham single particle gap is not guaranteed to be correct, as it is not a ground-state property. However, if its character is different from the experimental one it can indicate that the employed approximation is not appropriate. The optical gap has been measured experimentally as being direct and $200\pm5$ meV wide [44].

Another difficulty is treating the interlayer Van der Waals bond; the interlayer distances are usually overestimated by standard local density approaches. However it is possible to improve the agreement with experiment of vibrational frequencies using the experimental lattice parameters. For this reason, we have simulated the electronic structure using both the experimentally measured lattice parameter and the theoretically calculated values. In both cases we optimize the internal degrees of freedom to avoid unstable phonons.

In Fig. 2 we plot the electronic band structure, in a range of a few eV around the Fermi energy. We note that the band structure is very similar except for the case where relativistic effects are included in conjunction with the experimental lattice parameter [Fig. 2(b)]. When using the theoretical lattice parameter, (values give in Table I) the gap is of 471 meV in the scalar relativistic case and it decreases to 373 meV in the fully relativistic calculation. Conversely, if we use the experimental volume and optimize the internal coordinates, the gap is smaller for the scalar relativistic calculation 183 meV [Fig. 2(c)] while in the fully relativistic case the

Theoretical lattice parameter:

![](./images/812638290623594496_3.jpg)
![](./images/812638290623594496_4.jpg)
![](./images/812638290623594496_5.jpg)

(a) SR - 471 meV
(b) SOC - 373 meV
(c) Gap detail

Experimental lattice parameter:

![](./images/812638290623594496_6.jpg)
![](./images/812638290623594496_7.jpg)
![](./images/812638290623594496_8.jpg)

(d) SR - 183 meV
(e) SOC - 333 meV
(f) Gap detail

FIG. 2. Calculated electronic band structure of bulk ${\rm Bi_2Se_3}$. In the first row: using each method's respective calculated theoretical lattice parameter; second row: experimental lattice parameter. First column: scalar relativistic (SR), second column: fully relativistic (SOC), third column: comparison SR/SOC close to the Fermi energy.

![](./images/812638290623594496_9.jpg)

FIG. 3. Detail of the longitudinal-acoustic phonon dispersion along the [111] direction (parallel to the c axis) showing the effect of the lattice parameter. We plot four cases: at the experimental lattice parameter without SOC (black solid) and with SOC (blue dash) and at the relaxed theoretical lattice parameter without SOC (green dot) and with SOC (orange dash-dot).

indirect gap is at 333 meV and the direct gap at 444 meV [Fig. 2(d)].

### B. Phonon dispersion
The phonon dispersion does not change dramatically with the different choices of SOC treatment, however we do observe a global, relatively constant, rescaling of the frequencies which can be associated with the difference in the unit cell volume. When not including SOC, if the theoretical lattice parameter is used, the phonon dispersion exhibits negative frequencies. However, when using the experimental lattice parameters, which correspond to a 5% smaller unit cell volume, this instability is removed. Furthermore, if SOC is included, both theoretical and experimental lattice parameters yield stable phonons, as long as the internal degrees of freedom are properly relaxed. Because interplanes binding is mediated by Van der Waals forces, which usually leads to an overestimation of the bond length in the PBE approximation, we expect that the modes changing the interlayer distance will be too soft. For this reason, we show in Fig. 3 the phonon band that is more sensitive to a change in lattice parameter; it is the longitudinal acoustic (LA) mode along the [111] direction which, in the trigonal geometry, is orthogonal to the planes of Bi or Se.

We have compared the phonon frequencies at the $\Gamma$ point with available data from infrared and Raman spectroscopy, in order to establish which method gives a closer match to the phonon frequencies. These comparisons are summarized in Fig. 4 and Table II. We note that using the experimental lattice parameter gives a consistently better match for the Raman active modes than using the theoretical one, hence we will focus on the former. The SR calculations slightly underestimate the phonon frequencies, while with the inclusion of SOC the theoretical frequencies tend to overestimate the measured ones. SOC is more accurate for the highest optical bands but less so for the low-energy bands; as the latter are more important for thermal transport, due to the Bose-Einstein factor of Eq. (2), we expect that not including SOC may give a better match for the value of $\kappa$. We verified that our calculations at the theoretical lattice parameter agree with those of Ref. [48].

![](./images/812638290623594496_10.jpg)

FIG. 4. Experimental [16] Raman spectrum compared with theoretical calculations. The vertical lines indicate the theoretical harmonic phonon frequencies SR (orange) or with SOC (blue) at the experimental lattice parameter.

### I. Effective charges and LO-TO splitting
Even high-quality $Bi_2Se_3$ single crystals are doped by a relatively large amount $(10^{18}$–$10^{19}$ e/cm$^3)$ of lattice defects. Below we will see that this doping has no significant effect on the electronic structure nor on the geometry of the crystal, but it is sufficient to effectively screen long-range/small-wave-vector splitting of longitudinal and transverse optical modes (LO-TO splitting). In Fig. 5 we have plotted the phonon dispersion with and without the LO-TO splitting. We can see that a couple of modes are particularly affected. If we number the modes in order of increasing energy, these are the modes 8 and 9 where the atoms move in the plane perpendicular to [111] with Se ions going in the direction opposite to that of Bi ions. These modes are degenerate without LO-TO at an energy of 87 cm$^{-1}$, but the mode which is aligned with the $\mathbf{q}$ vector jumps to 130 cm$^{-1}$ when long-range effects are included. When coming from the [111] direction itself, along the $\Gamma$-$T$ line, the two modes remain degenerate, because the $\mathbf{q}$ wave vector is parallel to the polarization. In Fig. 6 we show the phonon dispersion used in the thermal transport calculations, with the lines enlarged proportionally to their intrinsic linewidth.

### C. Thermal transport in bulk
We have initially studied the phonon-driven thermal conductivity in the bulk phase as experimental data are available with good precision over a wide range of temperature. In particular we have taken as reference the data of Navratil and coworkers [3], where they estimate the fraction of lattice-driven and electron-driven transport.

In Fig. 7 we plot the experimental data of the in-plane thermal conductivity $\kappa_{\parallel}$ measured in Ref. [3], side by side with calculations from 2 K up to 400 K, in the RTA (we

205419-6

<table><caption>TABLE II. Phonons frequency at $\Gamma$, comparison of experimental data and calculations.</caption>
<tbody><tr><th rowspan="2">Symmetry</th><th colspan="4">IR active ($E \parallel c$)</th><th colspan="4">Raman active</th></tr>
<tr><td>$E_{u}$</td><td>$E_{u}$</td><td>$A_{2u}$</td><td>$A_{2u}$</td><td>$E_{g}$</td><td>$A_{1g}$</td><td>$E_{g}$</td><td>$A_{1g}$</td></tr>
<tr><td colspan="9">Experiments:</td></tr>
<tr><td>Ref. [49] (50 K)ª</td><td>61</td><td>134</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Ref. [49] (300 K)ª</td><td>65</td><td>129</td><td></td><td></td><td></td><td>72</td><td>131.5</td><td>174.5</td></tr>
<tr><td>Ref. [16]</td><td></td><td></td><td></td><td></td><td>39</td><td>74</td><td>135</td><td>177</td></tr>
<tr><td colspan="9">Simulations harmonic level:</td></tr>
<tr><td>SR theo.</td><td>76.2–123.8</td><td>129.7</td><td>143.4</td><td>161.2</td><td>38.3</td><td>61.8</td><td>130.5</td><td>171.5</td></tr>
<tr><td>SOC theo.</td><td>64.7–111.2</td><td>123.6</td><td>135.6</td><td>154.7</td><td>38.7</td><td>63.3</td><td>121.6</td><td>166.3</td></tr>
<tr><td>SR exp.ᵇ</td><td>87.8–129.8</td><td>134.2</td><td>145.2</td><td>166.4</td><td>45.6</td><td>75.6</td><td>139.7</td><td>180.1</td></tr>
<tr><td>SOC exp.ᵇ</td><td>78.0–123.0</td><td>128.5</td><td>138.0</td><td>162.3</td><td>40.2</td><td>73.6</td><td>132.2</td><td>173.6</td></tr>
<tr><td colspan="9">ªInfrared peak position are at 50 K and 300 K respectively.</td></tr>
<tr><td colspan="9">ᵇLattice parameters from Ref. [45].</td></tr>
</tbody></table>

checked that the exact inversion of the Boltzmann transport equation yields practically identical values). As it can be seen, the room temperature behavior of the lattice contribution to $\kappa_{\parallel}$ is in perfect agreement with our calculation of the intrinsic thermal conductivity. This agreement is possible thanks to the inclusion of lattice defects in the model, as explained in the rest of this section.

Below 20 K, $\kappa_{\parallel}$ is limited by extrinsic scattering processes such as the scattering with sample borders, with the isotopes or/and with lattice defects. As Navratil *et al.* used a large monocrystal, and isotopical effects are negligible in $Bi_2Se_3$ [50], only lattice defects can explain the low temperature behavior.

According to literature [28], two kind of defects are common in $Bi_2Se_3$ crystals: point-defect vacancies of Se and $Bi_2$ partial-layer intercalation. Each selenium vacancy contributes around two charges to the total doping, which means that at a doping concentration of around $10^{18}$–$10^{19}$ e/cm³ the fraction of missing Se atoms is of order 100–1000 ppm. We have simulated this defect concentration using an effective Rayleigh point-scattering model, assigning to each vacancy an effective mass as in Ref. [25]. We found that it is far too low to explain the low-temperature drop in thermal conductivity.

Even taking an unrealistically high point-defect concentration, such as 50 000 ppm (5%), the correct curve shape at low temperature is not reproduced. Finally, we remark that using a more accurate, i.e., *ab initio*, estimate of the defect cross section would be equivalent to a change in defect concentration but would not change the shape of the curve.

On the other hand, if we assume the presence of $Bi_2$ partial layers, we can include it in the simulation using Sparavigna-Casimir scattering theory, i.e., using an effective model that includes a scattering time which is proportional to the ratio between the phonon mean free path and the sample size. We tuned the average interdefect distance to fit the temperature of maximum $\kappa$, around 10 K. The theoretical position of the maximum is a better fitting parameter than its absolute value, as the latter is very difficult to converge at low temperature in simulations. Notwithstanding that, the calculation reproduces the absolute value quite well, which strengthens the validity of our assumption. In Fig. 8, the best agreement is found when the average distance between $Bi_2$ planes is fixed at 5 $\mu$m. Comparing this value to the size of the unit cell along $c$ gives a concentration of excess bismuth of around 100 ppm, and considering that each additional Bi atom provides

![](./images/812638290623594496_11.jpg)

FIG. 5. Phonon dispersion with (orange full line) and without (blue dash-dot line) long-range LO-TO splitting mediated by effective charges. These simulations use the experimental lattice parameters, PBE, SR.

![](./images/812638290623594496_12.jpg)

FIG. 6. Phonon dispersion, the width of the lines is proportional to their intrinsic linewidth; a different prefactor was used before and after the phonon gap to improve readability: 2 for the first six bands, 6 for the following nine bands.

![](./images/812638290623594496_13.jpg)

FIG. 7. In plane (i.e., orthogonal to $c$ axis) $\kappa$ measured by Navratil [3] (rounds) compared to simulations including the effect of Se vacancies (left) and $Bi_2$ layers intercalations (right) defects on $\kappa$; excess $Bi_2$ is expressed as average interplane distance and as ppm. The behavior at very low temperature (i.e., below 2 K) is not shown as it could suffer from the finite $k$-point mesh used in the calculations, due to the difficulty of converging the conductivity in the zero temperature limit.

three charges, this is compatible with the measured doping concentration.

We note that the effect of selenium vacancies and bismuth partial layer intercalation is qualitatively different: An increasing concentration of selenium vacancies causes a global reduction of $\kappa$; on the other hand increasing the frequency of bismuth partial layer intercalation moves the maximum of $\kappa$ toward higher temperatures, without changing its high-$T$ value. If we combine the two types of defects, we observe that selenium vacancies have virtually no effect until their concentration is greater than 100 ppm, after which scattering from vacancies lead to a considerable reduction in $\kappa$ at higher $T$. As a consequence, the best match remains a concentration of around 100 ppm bismuth partial layer intercalation with 100 ppm or less selenium vacancy. This is compatible with the high $n$-type concentration ($\simeq 10^{19}$ cm$^{-3}$) of the bulk material measured.

### D. Thermal transport in thin films
Thermoreflectance measurements provide the total out-of-plane ($\kappa_\perp$) thermal conductivity which is the sum of the electronic and lattice contributions. As described in Sec. IV C, we estimate the lattice contribution after measuring the in-plane electronic conductivity in thin films and estimating the out-of-plane electronic conductivity from the measured conductance anisotropy of bulk $Bi_2Se_3$.

Transport measurements performed attest that our thin films are $n$ doped and present a metallic behavior with a carrier's concentration bracketed by $1$--$2 \times 10^{19}$ cm$^{-3}$, $\mu \sim$ 300--400 cm$^2$/V s, and $\rho_\parallel \sim 1$--$1.15$ m$\Omega$ cm at room temperature.

Thus a coarse evaluation of the electronic contribution to the in-plane conductivity $k_{el,\parallel}$ can be given using the Wiedmann-Franz law $k_{el,\parallel} = {\rm LT}/\rho_\parallel$ with L the Lorentz number, ranging between 2 and $2.2 \times 10^{-8}$ V$^2$ K$^{-2}$. Consequently $k_{el,\parallel}$ is bracketed between 0.4--0.7 W/m K.

In Table III we report the measured values for the total and lattice thermal conductivity, obtained by subtraction of the estimated electronic contribution. In Fig. 9, we compare the measured lattice thermal conductivity with the simulations. The agreement is within the experimental error bar. Including internal reflection effects (dashed line in the figure) does improve the agreement but is not sufficient to explain completely the discrepancy for the smallest slab. This may indicate that a simple Casimir model is not sufficient for such a thin sample; a more detailed description of the interaction of phonon with the surface, including $\mathbf{q}$ and $\omega$ dependence, could improve the agreement. Finally, the laser penetration depth in the sample (around 10 nm) could play a role for the

![](./images/812638290623594496_14.jpg)

FIG. 8. Our $b$ of the thermal conductivity with Ref. [3] is obtained assuming around 100 ppm of $Bi_2$ partial layers and 100 ppm of selenium vacancies.

<table>
<caption>TABLE III. Out-of-plane thermal conductivity of $Bi_2Se_3$, the experimental error bar can be evaluated to 20%.</caption>
<thead>
<tr>
<th rowspan="2">Thickness (nm)</th>
<th colspan="2">Thermal conductivity:</th>
</tr>
<tr>
<th>Total (measured) (W/m K)</th>
<th>Lattice (estimated) (W/m K)</th>
</tr>
</thead>
<tbody>
<tr>
<td>18</td>
<td>0.39</td>
<td>0.19</td>
</tr>
<tr>
<td>30</td>
<td>0.52</td>
<td>0.32</td>
</tr>
<tr>
<td>53</td>
<td>0.53</td>
<td>0.33</td>
</tr>
<tr>
<td>105</td>
<td>0.56</td>
<td>0.36</td>
</tr>
<tr>
<td>191</td>
<td>0.68</td>
<td>0.48</td>
</tr>
</tbody>
</table>


![](./images/812638290623594496_15.jpg)

FIG. 9. Thermal conductivity in thin films as a function of sample thickness $L$ at 300 K. Experimental data: lattice thermal conductivity, to be compared with $\kappa$ out-of-plane axis (dashed line). Blue thick line use our theory of Casimir scattering, while red lines use the method of cutting-off phonons of Ref. [51].

thinnest slabs, although there is no simple way to include it in the simulation.

We have also tested the approach of Ref. [51] (red lines of Fig. 9), which consists of cutting off completely the contribution of phonons that have mean free path $\tau v$ larger than the sample dimension. The behavior is relatively similar, but the predicted value of $\kappa$ is considerably larger for the smaller samples.

## VI. CONCLUSIONS

We calculate the phonon-component in-plane ($\kappa_{\parallel}$) and out-of-plane ($\kappa_{\perp}$) thermal conductivity of $Bi_2Se_3$ bulk and films with different thicknesses by using the Boltzmann equation with phonon scattering times obtained from anharmonic third order density functional perturbation theory. Our results agree with existing measurements on bulk samples [3,4] and with our room-temperature thermoreflectance measurements of $\kappa_{\perp}$ on films of thickness ranging from 18 nm to 191 nm.

The calculated thermal conductivity of bulk $Bi_2Se_3$ is in excellent agreement with the experimental data of Ref. [3] at all temperatures. While the high temperature limit (e.g., room temperature) is essentially determined by the intrinsic thermal conductivity, the low temperature regime, in the past attributed to Se vacancy, can be very well accounted for by assuming $\approx$100 ppm bismuth insertion and $\approx$100 ppm of Se vacancies. In contrast, Se vacancies alone do not explain the low-$T$ behavior of the conductivity.

In thin films, we find that the thermal conductivity measured at room temperature monotonically decreases with reducing film thickness $L$. We can attribute this reduction to incoherent scattering of out-of-plane momentum phonons with the film upper and lower surfaces. Our work outlines the crucial role of sample thinning in reducing the out-of-plane thermal conductivity.

## ACKNOWLEDGMENTS

M.C. acknowledges support from the European Graphene Flagship Core 2 Grant No. 785219. Computer facilities were provided by CINES, CCRT, and IDRIS (projects 907320 and 901202). M.M. and D.F. thank Haneen Sameer Abushammala and Heba Hamdan for assistance at the very beginning of thermoreflectance experiments.

[1] K. Behnia, *Fundamentals of Thermoelectricity*, 1st ed. (OUP Oxford, New York, London, 2015).
[2] M. Dresselhaus, G. Chen, M. Tang, R. Yang, H. Lee, D. Wang, Z. Ren, J.-P. Fleurial, and P. Gogna, *Adv. Mater.* **19**, 1043 (2007).
[3] J. Navrátil, J. Horák, T. Plecháček, S. Kamba, P. Lošťák, J. Dyck, W. Chen, and C. Uher, *J. Solid State Chem.* **177**, 1704 (2004).
[4] J. Navrátil, T. Plecháček, J. Hork, S. Karamazov, P. Lošťák, J. Dyck, W. Chen, and C. Uher, *J. Solid State Chem.* **160**, 474 (2001).
[5] Y. S. Hor, A. Richardella, P. Roushan, Y. Xia, J. G. Checkelsky, A. Yazdani, M. Z. Hasan, N. P. Ong, and R. J. Cava, *Phys. Rev. B* **79**, 195208 (2009).
[6] C. Uhrer and D. Morelli, *Thermal Conductivity 25/Thermal Expansion 13* (Technomic Publishing, Boca Raton, Florida, 1999).
[7] D. Fournier, M. Marangolo, M. Eddrief, N. N. Kolesnikov, and C. Fretigny, *J. Phys.: Condens. Matter* **30**, 115701 (2018).
[8] A. Rosencwaig, J. Opsal, W. L. Smith, and D. L. Willenborg, *Appl. Phys. Lett.* **46**, 1013 (1985).
[9] L. Pottier, *Appl. Phys. Lett.* **64**, 1618 (1994).
[10] L. Fabbri, D. Fournier, L. Pottier, and L. Esposito, *J. Mater. Sci.* **31**, 5429 (1996).
[11] B. Li, L. Pottier, J. Roger, D. Fournier, K. Watari, and K. Hirao, *J. Eur. Ceram. Soc.* **19**, 1631 (1999).
[12] K. Plamann, D. Fournier, B. C. Forget, and A. Boccara, *Diam. Relat. Mater.* **5**, 699 (1996).
[13] B. Li, J. P. Roger, L. Pottier, and D. Fournier, *J. Appl. Phys.* **86**, 5314 (1999).
[14] C. Pélissonnier-Grosjean, D. Fournier, and A. Thorel, *J. Phys. IV (France)* **09**, 201 (1999).
[15] C. Frétigny, J.-Y. Duquesne, D. Fournier, and F. Xu, *J. Appl. Phys.* **111**, 084313 (2012).
[16] M. Eddrief, P. Atkinson, V. Etgens, and B. Jusserand, *Nanotechnology* **25**, 245701 (2014).
[17] R. S. Peierls, *Quantum Theory of Solids* (Oxford University Press, Oxford, UK, 1955).
[18] H. Casimir, *Physica* **5**, 495 (1938).
[19] R. Berman, F. E. Simon, and J. S. Ziman, *Proc. R. Soc. London A* **220**, 171 (1953).
[20] R. Berman, E. L. Foster, and J. S. Ziman, *Proc. R. Soc. London A* **231**, 130 (1955).

[21] M. Omini and A. Sparavigna, *Physica B: Condensed Matter* **212**, 101 (1995).

[22] A. Sparavigna, *Phys. Rev. B* **65**, 064305 (2002).

[23] G. Fugallo, M. Lazzeri, L. Paulatto, and F. Mauri, *Phys. Rev. B* **88**, 045430 (2013).

[24] G. Fugallo, A. Cepellotti, L. Paulatto, M. Lazzeri, N. Marzari, and F. Mauri, *Nano Lett.* **14**, 6109 (2014).

[25] C. A. Ratsifaritana and P. G. Klemens, *Int. J. Thermophys.* **8**, 737 (1987).

[26] A. Alkurdi, S. Pailhès, and S. Merabia, *Appl. Phys. Lett.* **111**, 093101 (2017).

[27] L. Paulatto, F. Mauri, and M. Lazzeri, *Phys. Rev. B* **87**, 214303 (2013).

[28] F.-T. Huang, M.-W. Chu, H. H. Kung, W. L. Lee, R. Sankar, S.-C. Liou, K. K. Wu, Y. K. Kuo, and F. C. Chou, *Phys. Rev. B* **86**, 081104(R) (2012).

[29] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. De Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. Seitsonen, A. Smogunov, P. Umari, and R. Wentzcovitch, *J. Phys.: Condens. Matter* **21**, 395502 (2009).

[30] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carnimeo, A. D. Corso, S. de Gironcoli, P. Delugas, R. A. D. J. A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. O. de-la Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N. Vast, X. Wu, and S. Baroni, *J. Phys.: Condens. Matter* **29**, 465901 (2017).

[31] A. Dal Corso, S. Baroni, R. Resta, and S. de Gironcoli, *Phys. Rev. B* **47**, 3588 (1993).

[32] C. S. Baroni, P. Giannozzi, and A. Testa, *Phys. Rev. Lett.* **58**, 1861 (1987).

[33] P. Giannozzi, S. de Gironcoli, P. Pavone, and S. Baroni, *Phys. Rev. B* **43**, 7231 (1991).

[34] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, *Rev. Mod. Phys.* **73**, 515 (2001).

[35] X. Gonze and J.-P. Vigneron, *Phys. Rev. B* **39**, 13120 (1989).

[36] A. Debernardi and S. Baroni, *Solid State Commun.* **91**, 813 (1994).

[37] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[38] D. R. Hamann, *Phys. Rev. B* **88**, 085117 (2013).

[39] M. Schlipf and F. Gygi, *Comput. Phys. Commun.* **196**, 36 (2015).

[40] P. Scherpelz, M. Govoni, I. Hamada, and G. Galli, *J. Chem. Theory Comput.* **12**, 3523 (2016).

[41] A. Dal Corso, *Phys. Rev. B* **76**, 054308 (2007).

[42] J. W. Eaton, D. Bateman, S. Hauberg, and R. Wehbring, *GNU Octave Version 5.1.0 Manual: A High-Level Interactive Language for Numerical Computations* (2019), https://www.gnu. org/software/octave/doc/v5.2.0/.

[43] J.-M. Zhang, W. Zhu, Y. Zhang, D. Xiao, and Y. Yao, *Phys. Rev. Lett.* **109**, 266405 (2012).

[44] G. Martinez, B. A. Piot, M. Hakl, M. Potemski, Y. S. Hor, A. Materna, S. G. Strzelecka, A. Hruban, O. Caha, J. Novák, A. Dubroka, Č. Drašar, and M. Orlita, *Sci. Rep.* **7**, 6891 (2017).

[45] R. Wyckoff, *Crystal Structures*, Crystal Structures Vol. 1 (Inter-science Publishers, Hoboken, New Jersey, 1963).

[46] X. Chen, H. D. Zhou, A. Kiswandhi, I. Miotkowski, Y. P. Chen, P. A. Sharma, A. L. Lima Sharma, M. A. Hekmaty, D. Smirnov, and Z. Jiang, *Appl. Phys. Lett.* **99**, 261912 (2011).

[47] M. Stordeur, K. K. Ketavong, A. Priemuth, H. Sobotta, and V. Riede, *Phys. Status Solidi B* **169**, 505 (1992).

[48] W. Cheng and S.-F. Ren, *Phys. Rev. B* **83**, 094301 (2011).

[49] W. Richter and C. R. Becker, *Phys. Status Solidi B* **84**, 619 (1977).

[50] The relative mass variance of selenium isotopes is only 0.046%, while bismuth has only one stable isotope.

[51] O. Hellman and D. A. Broido, *Phys. Rev. B* **90**, 134309 (2014).

205419-10