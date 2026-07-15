
# Dissipation in graphene and nanotube resonators.

C. Seoánez and F. Guinea

Instituto de Ciencia de Materiales de Madrid, CSIC, Cantoblanco E28049 Madrid, Spain

A. H. Castro Neto

Department of Physics, Boston University, 590 Commonwealth Avenue, Boston, MA 02215, USA

Different damping mechanisms in graphene nanoresonators are studied: charges in the substrate, ohmic losses in the substrate and the graphene sheet, breaking and healing of surface bonds (Velcro effect), two level systems, attachment losses, and thermoelastic losses. We find that, for realistic structures and contrary to semiconductor resonators, dissipation is dominated by ohmic losses in the graphene layer and metallic gate. An extension of this study to carbon nanotube-based resonators is presented.

PACS numbers: 73.23.-b, 03.65.Yz, 62.25.+g, 85.85.+j

## I. INTRODUCTION.

Nano-electro-mechanical devices \( ^{1,2,3} \)  (NEMS) have attracted a great deal of attention, as they are a problem of fundamental interest, and also because of their potential applications.

Recently, NEMs made from graphene sheets have been studied \( ^{4} \) , following work on NEMs based on carbon nanotubes \( ^{5,6} \) . These devices show unique characteristics, as graphene sheet stacks have a high elastic modulus and very small total mass thanks to the low number of atomic planes (sometimes just even one) composing the bridge or cantilever, allowing for higher resonating frequencies than other materials of similar dimensions and increased potential sensitivity.

Graphene itself has attracted a great deal of attention \( ^{7} \) , because of its unique features. Graphene samples can be made one carbon layer thick, and doped by an external electric field. The lattice dynamics of these thin samples have not been studied in detail yet. Two dimensional systems have, in addition to acoustic modes, transverse flexural modes \( ^{8} \) , which are the ones explored in the experiments considered in this paper. The quadratic dispersion of these modes leads to a constant density of states at low energy. Experimental observations show that free standing graphene is not flat \( ^{9,10,11} \) , but corrugated. These ripples imply the existence of flexural deformations, and can lead to charge inhomogeneities in single layer graphene at low dopings \( ^{12,13} \) . Most graphene samples stand on  \( SiO_{2} \)  substrates \( ^{14} \) , and the interaction between the graphene layers and the substrate is not well known. The experiments discussed in this paper can provide information on this issue.

The potential sensitivity of a resonator-based detector may be in practice strongly reduced by dissipative processes affecting the vibrational mode used for detection, due to the associated widening of the resonance, which masks the frequency shifts used to determine the presence of external species adsorbed or close to the detector. Hence, it is of fundamental importance to gain knowledge about those damping mechanisms, to establish their relative importance and dependence on resonator parameters (dimensions, elastic constants, temperature, etc), which may help to optimize performances and determine where should efforts be put, not only to use them as detectors, but also as tools for the study of more fundamental questions like the quantum to classical crossover with increasing system sizes \( ^{2,15} \) .

In common resonating structures made of semiconductors the prevailing dissipative mechanism with decreasing size and temperature are surface-related losses: the presence of the imperfect surface, with its roughness, structural defects, impurities and dangling bonds, can be modeled by a distribution of effective two-level systems which couple to the vibrational eigenmodes of the device \( ^{16,17,18} \) . Many other processes contribute to a lower extent to the damping of vibrations in these devices. Some of them are common to all experimental setups, like attachment losses \( ^{19,20} \)  or thermoelastic damping \( ^{21,22,23} \) . Others depend on the actuation scheme: For example, in the magnetomotive actuation scheme \( ^{24} \) , a layer of metal is deposited on top of the vibrating semiconducting structure to control its motion with the Lorentz force actuating on the electron current that passes through the top layer in presence of an applied magnetic field. This metallic layer increases dissipation in two different ways: i) Increasing the local temperature due to electron-phonon interactions, thus "feeding" other mechanisms whose effect tends to grow with T, ii) Absorbing energy through the excitation of electron-hole pairs in the metallic layer due to the presence of fixed charges in the substrate supporting the oscillating structure, which create a potential on the electrons moving within the mobile structure that is time-dependent, as perceived by the latter.

This last mechanism has been ignored until now in the literature, perhaps due to the small amount of fixed charges in typical substrates like single-crystal Si or GaAs. But in the case of graphene or carbon-nanotube based resonators it must be considered, as it plays a much more significant role. This is due to the fact that graphene is conducting, and in some actuation setups, the control over the graphene layer's motion is through
 
![](./images/867771663767306279_1.jpg)

FIG. 1: (Color online) Sketch of the system considered in the text. v represents the Coulomb interaction between the charged graphene layer and the Si gate.

the establishment of a capacitive coupling between two charged layers, namely the oscillating graphene and a doped Si backgate. The number of carriers in both can be controlled by an external gate \( ^{14} \) . The coupling between the charges of both layers, apart from enabling the control of the resonator's motion, causes energy losses which will dominate at high temperatures. There will be also fixed charges in the supporting structure, mainly in the  \( SiO_{2} \)  layer located between the graphene and the doped Si backgate, absorbing energy too from the resonators motion. In this paper we give will give full account of these processes.

In the following, we start analyzing different dissipative processes which may be present in devices based on graphene. Our calculations should give reasonable order of magnitude estimates of the strengths of these mechanisms. In Sections II and III we model the absorption of mechanical energy due to the charge present in the oscillating graphene sheet, the  \( SiO_{2} \)  substrate and the Si backgate. In section IV we discuss the role as attenuation source played in these peculiar devices by the breaking and healing of bonds gluing the graphene sheet to the  \( SiO_{2} \)  substrate, a possibility also missing in current semiconducting resonators. Whereas for the latter prevail surface-related losses, we show in Section V that for graphene resonators this friction mechanism is highly suppressed thanks to their high degree of crystallinity. For completeness, we apply previous results of other works to estimate the effect of two more friction sources present in all setups, namely attachment losses and thermoelastic losses, in Section VI. Once these mechanisms have been studied, an extension of the results to carbon nanotube resonators is presented in Section VII.

To make numerical estimates we focus on the devices studied in \( ^{4} \) . The parameters which characterize the average oscillator studied there are given in Table \( [I] \) . A sketch of the system is shown in Fig. \( [1] \) .

## II. STATIC CHARGES AT THE AMORPHOUS  \( SiO_{2} \)  SUBSTRATE.

The graphene sheet can couple electrostatically to static charges. These charges give rise to a time depen-

<table><tr><td colspan="2">System properties</td></tr><tr><td>Dimensions</td><td>10  \( \cdot \)  10 \( ^{-9} \)  m</td></tr><tr><td>Thickness  \( t \)</td><td>10 \( ^{-6} \)  m</td></tr><tr><td>Width  \( w \)</td><td>10 \( ^{-6} \)  m</td></tr><tr><td>Length  \( L \)</td><td>10 \( ^{-6} \)  m</td></tr><tr><td>Height above substrate  \( d \)</td><td>300  \( \cdot \)  10 \( ^{-9} \)  m</td></tr><tr><td>Frequency  \( f_{0} \)</td><td>100 MHz</td></tr><tr><td>Amplitude  \( A \)</td><td>0.5 nm</td></tr><tr><td>Carrier density  \( \rho_{C} \)</td><td>10 \( ^{12} \)  cm \( ^{-2} \)</td></tr><tr><td colspan="2">Properties of graphite</td></tr><tr><td>Mass density  \( \rho_{M}^{C} \)</td><td>2200 kg/m \( ^{3} \)</td></tr><tr><td>Elastic constants</td><td></td></tr><tr><td>\( E \)</td><td>10 \( ^{12} \)  Pa</td></tr><tr><td>\( \nu \)</td><td>0.16</td></tr><tr><td>Debye temperature  \( \theta_{D} \)</td><td>\( \sim \)  570 K</td></tr><tr><td>Specific heat  \( C_{p} \)</td><td>700 J / Kg. K</td></tr><tr><td>Thermal conductivity  \( \kappa \)</td><td>390 W / m . K</td></tr></table>

TABLE I: Parameters used in the calculations presented in the main text, adapted to the systems studied in \( ^{4} \) . Bulk data taken from \( ^{25} \) .

dent potential acting on the electrons of the vibrating graphene. The energy is dissipated by creating electron-hole excitations in the graphene layer. Static charges have been proposed as a source of scattering by the carriers in the graphene \( ^{26,27} \) .

The time-dependent component of the unscreened potential induced by a charge separated by a distance d in the vertical direction from the graphene layer, acting on an electron at position  \( \vec{r} \)  in the graphene layer is given, approximately, by:

 \[ V(\vec{\mathbf{r}},t)\approx\frac{e^{2}d A e^{i\omega_{0}t}}{(|\vec{\mathbf{r}}|^{2}+d^{2})^{3/2}} \quad (1) \] 

where A is the amplitude of the flexural mode, and  \( \omega_{0} \)  its frequency. The dissipation depends on the screening by the graphene layer \( ^{28} \) . A calculation of the damping is given in Appendix A. We find that, for a single graphene layer, a single charge gives a contribution to the inverse quality factor of:

 \[ Q^{-1}\approx\left\{\begin{array}{l l}\frac{1}{k_{\mathrm{F}}d}\frac{2\hbar}{M\omega_{0}d^{2}}&k_{\mathrm{F}}d\gg1\\ \frac{2\hbar\omega_{0}^{3}d^{2}}{M v_{\mathrm{F}}^{4}}&k_{\mathrm{F}}d\ll1\end{array}\right. \quad (2) \] 

where M is the mass of the oscillating sheet,  \( k_{F} = \pi \sqrt{\rho_{C}} \) , and  \( \rho_{C} \)  is the density of carriers in the graphene sheet. Typical values of this quantity are in the range  \( \rho_{C} \sim 10^{12} cm^{-2} \) , so that  \( k_{F} d \sim 10^{2} - 10^{3} \gg 1 \) . Eq.(2) can be generalized to a graphene sheet with N layers:

 \[ Q^{-1}\sim\frac{1}{\sqrt{N\rho}d}\frac{2\hbar}{M\omega_{0}d^{2}} \quad (3) \] 

The suppression with the number of layers is due to the increased screening in this system.

The total contribution to the inverse quality factor is obtained by multiplying eqs.(2) or (3) by the total number of charges  \( N_{ch} \) . An upper bound to the density of
 

local charges, deduced from some models for the electric conductivity of graphene \( ^{26,27} \) , is  \( \rho_{ch} \sim 10^{12} cm^{-2} \) . Using the parameters in Table \( ^{[1]} \) , we find  \( N_{ch} \sim 10^{4} \)  and  \( Q^{-1} \sim 10^{-11} \)  at low temperatures.

This mechanism leads to ohmic dissipation, as the energy is dissipated into electron-hole pairs in the metallic graphene layer. Hence, the temperature dependence of this mechanism is given by  \( Q^{-1}(T) \sim Q^{-1}(0) \times (kT/\hbar\omega_{0}) \) , and  \( Q^{-1} \sim 10^{-6} \)  at 300 K.

## III. OHMIC LOSSES AT THE GRAPHENE SHEET AND THE METALLIC GATE.

The electrons in the vibrating graphene layer induce a time dependent potential on the metallic gate which is sometimes part of the experimental setup. The energy is transferred to electron-hole pairs created at the gate or at the graphene layer. These processes contribute to the energy loss and decoherence of electrons in metallic conductors near gates \( ^{29,30} \) .

The coupling between charge fluctuations in the two metallic systems is due to long range electrostatic interactions. The corresponding hamiltonian is

 \[ \begin{aligned}H=\frac{1}{2}\Biggl\{&\int_{C}v_{scr}(z,\vec{\mathbf{r}},t)\rho^{C}(z,\vec{\textbf{r}},t)+\int_{G}v_{scr}(0,\vec{\textbf{r}}^{\prime},t)\rho^{G}(\vec{\textbf{r}}^{\ \prime})\Biggr\}\\&+\int_{C}\frac{1}{2\rho_{M} t w}\Pi^{2}+\frac{1}{2}\frac{E t^{3}w}{12}\Biggl[\Bigl(\frac{\partial^{2}\phi}{\partial x^{2}}\Bigr)^{2}+\Bigl(\frac{\partial^{2}\phi}{\partial y^{2}}\Bigr)^{2}\Biggr]\end{aligned} \quad (4) \] 

where the indices G and C stand for the gate and graphene layer, respectively.  \( \rho_{M} \)  is the mass density of the graphene sheet, and t, w, E its thickness, width and Young modulus, whereas  \( \phi(\vec{\mathbf{r}}, t) \)  represents the vibrating amplitude field of bending modes and  \( \Pi = \partial L / \partial \phi \)  is its conjugate momentum (L is the Lagrangian). The self-consistent screened potentials  \( v_{scr}(z, \vec{\mathbf{r}}, t) \) ,  \( v_{scr}(0, \vec{\mathbf{r}}, t) \)  are calculated as a function of the bare potentials  \( v_{0}(z, \vec{\mathbf{r}}, t) \) ,  \( v_{0}(0, \vec{\mathbf{r}}, t) \)  in Appendix B.

As in the case of eq.(1), the time-dependent part of the bare potentials couples the electronic degrees of freedom and the mechanical ones through the charge  \( \rho(\vec{\mathbf{r}}) \)  and amplitude of the vibrational mode,  \( A_{\vec{q}} \) , and would give rise to a term in the quantized hamiltonian of the form

 \[ H_{i n t}\propto\rho(\vec{\mathbf{r}})A_{\vec{\mathbf{q}}}\propto(b_{\vec{\mathbf{q}}}^{t}+b_{\vec{\mathbf{q}}})\sum_{\vec{\mathbf{k}},\vec{\mathbf{k}}^{\prime}}[c_{\vec{\mathbf{k}}+\vec{\mathbf{k}}^{\ prime}}^{t}c_{\vec{\mathbf{k}}^{\prime}}+\mathrm{h.c}] \quad (5) \] 

where  \( A_{\vec{q}} \)  and  \( \rho(\vec{\mathbf{r}}) \)  have been expressed in terms of creation and annihilation operators of phonons  \( (\vec{\mathbf{q}}, \omega_{\vec{\mathbf{q}}}) \)  and electrons of a 2D Fermi gas, respectively.

But a realistic model requires taking into account the screening of the potential associated to these charge fluctuations. In terms of the screened potentials, the induced broadening of the mode  \( (\vec{\mathbf{q}}, \omega_{\vec{\mathbf{q}}}) \)  of the graphene layer can be written, using Fermi's Golden Rule, as \( ^{29} \) 

 \[ \Gamma(\omega_{\vec{\mathbf{q}}})=\sum_{\alpha=G,C}\int d^{3}\vec{\mathbf{r}}\int d^{3}\mathbf{r}^{\prime}\Big\{{\mathrm{R e}}V_{\mathrm{s c r}}^{\alpha}(\vec{\mathbf{r}},\omega_{\vec{\mathbf{q}}})\times \] 

 \[ \times\mathrm{R e}V_{\mathrm{s c r}}^{\alpha}(\vec{\mathbf{r}}^{\prime},\omega_{\vec{\mathbf{q}}})\times\mathrm{I m}\chi^{\alpha}[\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega_{\vec{\mathbf{q}}}]\Big\} \quad (6) \] 

The static screening properties,  \( \lim_{\vec{\mathbf{q}}\to0}\operatorname{Re}\chi^{\alpha}(\vec{\mathbf{q}},0) \) , of the graphene layer and the gate are determined by their electronic compressibilities,  \( \nu^{C} \)  and  \( \nu^{G} \)  respectively. We will assume that the distance between the graphene and the gate is much larger than the electronic elastic mean free path in either material, so that their polarizability is well approximated by:

 \[ \chi^{\alpha}(\vec{\mathbf{q}},\omega)\approx\frac{\nu^{\alpha}D^{\alpha}|\vec{\mathbf{q}}|^{2}}{D^{\alpha}|\vec{{\mathbf{q}}}|^{2}+i\omega} \quad (7) \] 

where  \( D^{\alpha} = v_{F}^{G} l^{\alpha} \)  is the diffusion constant, and  \( l^{\alpha} \) , the elastic mean free path. The two dimensional conductivity is  \( g^{\alpha} = k_{F}^{\alpha} l^{\alpha} \) .

We assume the gate to be quasi two dimensional. This approximation is justified when the distance between the gate and the graphene layer is much larger than the width of the gate. In this situation, the broadening of the mode, eq.(6), can be expressed as

 \[ \Gamma(\omega_{\vec{\mathbf{q}}})\approx\int d^{2}\vec{\mathbf{k}}|v_{s c r}(d,\vec{\mathbf{k}},\omega_{\vec{\mathbf{q}}})|^{2}\mathrm{I m}\chi^{C}+|v_{\mathrm{s c r}}(0,\vec{\mathbf{k}},\omega_{\vec{\mathbf{q}}})|^{2}\mathrm{I m}\chi^{G} \quad (8) \] 

The screened potentials for a graphene layer oscillating in an eigenmode  \( (\vec{\mathbf{q}},\omega_{\vec{\mathbf{q}}}) \)  of amplitude  \( A_{\vec{q}} \) , have in a first approximation only one momentum component,  \( v_{scr}(\vec{\mathbf{k}},\omega_{\vec{\mathbf{q}}})=v_{scr}(\vec{\mathbf{q}},\omega_{\vec{\mathbf{q}}})\delta(\vec{\mathbf{k}}-\vec{\mathbf{q}}) \) , and these components are (see Appendix B)

 \[ \left\{\begin{array}{l}v_{s c r}(d,\vec{\mathbf{q}},\omega_{\vec{\mathbf{q}}})=\frac{q\left[\chi^{C}\left(e^{q d}+e^{-q d}\right)-2\chi^{C}e^{q d}\right]\rho_{C}A_{\vec{\mathbf{q}}}e^{-q d}}{2\chi^{C}\chi^{C}\left(1-e^{-2q d}\right)}\\ v_{s c r}(0,\vec{\mathbf{q}},\omega_{\vec{\mathbf{q}}})=\frac{|\vec{\mathbf{q}}|\left[-\nu^{C}\left(e^{2q d}+1\right)+2\nu^{G}\right]\rho_{0}A_{\vec{\mathbf{q}}}e^{-q d}}{2\nu^{C}\nu^{G}\left(1-e^{-2q d}\right)}\end{array}\right. \quad (9) \] 

where  \( q = |\vec{q}| \)  and  \( \rho_{C} \)  is the charge density in the graphene layer. The results for  \( \Gamma(\omega_{\vec{\mathbf{q}}}) \)  and  \( Q^{-1}(\omega_{\vec{\mathbf{q}}}) \)  can be formulated in terms of the total charge in the graphene layer,  \( Q_{C} = \int d^{2}\vec{r}\rho_{C} \approx L \times w \times \rho_{C} \) .

In the limit of short separation between the layers,  \( d \ll L \) , which is the situation present in current experimental setups, one has

 \[ \Gamma(\omega_{0})\approx\frac{\omega_{0}A^{2}Q_{C}^{2}}{4d^{2}}\Big(\frac{1}{\nu^{C}D^{C}}+\Big(\frac{\nu^{G}}{\nu^{C}}\Big)^{2}\frac{1}{\nu^{G}D^{G}}\Big) \quad (10) \] 

The limit  \( D|\vec{q}|^{2} \gg \omega \)  for the imaginary part of the susceptibility of a dirty metal,  \( \operatorname{Im}\chi(\vec{\mathbf{q}}, \omega) \approx \omega \nu / D |\vec{\mathbf{q}}|^{2} \) , has been used. The first term in the summation describes losses at the graphene sheet, and the second at the gate. The associated inverse quality factor, according to eq.(A6), is given by

 \[ Q^{-1}(\omega_{0})\approx\frac{\hbar Q_{C}^{2}}{2M\omega_{0}d^{2}}\Big(\frac{1}{\nu^{C}D^{C}}+\Big(\frac{\nu^{G}}{\nu^{C}}\Big)^{2}\frac{1}{\nu^{G}D^{G}}\Big) \quad (11) \]
 

To make numerical estimates, we use the parameters in Table \( [I] \) , with  \( \nu^{C}(E)=E/2\pi\hbar^{2}v_{F}^{2} \) ,  \( v_{F}\approx10^{6} \)  m/s for a single layer of graphene, and  \( \nu^{C}(E)=(N\gamma)/v_{\mathrm{F}}^{2} \)  for a stack of N layers \( ^{31} \) . Carriers in graphene stacks have large mobilities \( ^{14} \) , and we take  \( D^{C}\nu^{C}\approx10^{3} \) . Typical charge densities for the graphene layer are  \( \rho_{C}\sim10^{12}cm^{-2} \) , leading to a total charge  \( Q_{C}\sim10^{4} \) . For these parameters, the contribution of the graphene sheet is  \( Q^{-1}\sim10^{-8} \) . The relative contribution from the gate depends on the distance to the graphene sheet. For a Si layer with  \( D^{G}\nu^{G}\approx10^{3} \)  and at short distances, the contribution to the damping from the gate is of the same order as that of the graphene sheet.

Damping is associated to the creation of e-h pairs in a metal, which implies that this mechanism is ohmic. The inverse quality factor should increase linearly with temperature, leading to  \( Q^{-1} \sim 10^{-2} \)  at 300 K.

## IV. BREAKING AND HEALING OF SURFACE BONDS: VELCRO EFFECT.

In the fabrication process of the device, the graphene flake is deposited on the  \( SiO_{2} \)  substrate, and becomes linked to it through hydrogen bonds created by the silanol groups (SiOH) present at the substrate's surface. When the flake is set into motion, some of this bonds may repeatedly break and heal (the Velcro effect \( ^{32} \) ), causing dissipation of the energy stored in the vibration. Numerical estimates are difficult to make, but nevertheless two qualitative arguments showing that its role in the damping is probably negligible can be presented:

i) This mechanism is expected to be temperature independent, in contrast with the strong decrease of friction observed as temperature is lowered \( ^{4} \) .

ii) The elastic energy stored in a typical graphene oscillator of lateral dimensions  \( w \sim 1\mu m \)  is about 10eV, when the amplitude is  \( \sim 1nm \) . This means about  \( \sim 10^{-5}eV \)  per  \( nm^{2} \) . On the other hand, the energy per hydrogen bond is about  \( 10^{-1}eV \) , and typical radical densities at  \( SiO_{2} \)  surfaces are  \( 33 \sim 1nm^{-2} \) . Hence the elastic energy available on average for each hydrogen bond is much less than the energy stored in the bond. Only rare fluctuations, where a significant amount of energy is concentrated in a small area will be able to break bonds, and to induce energy dissipation. Note, however, that this argument ceases to be valid for very large amplitudes  \( \gtrsim 30nm \) . For higher amplitudes, this mechanism can induce significant losses.

## V. DISSIPATION DUE TO TWO-LEVEL SYSTEMS.

This is the typical mechanism for the damping of sound waves in insulating amorphous materials \( ^{34,35,36} \) . An atom or a few atoms can have two nearly degenerate configurations. A vibration modifies the energy difference between these situations. This mechanism leads to the damping of acoustic phonons in amorphous  \( SiO_{2}^{35} \) . It is also expected to dominate friction in many NEMs \( ^{24} \) . We expect the graphene sheet to show a high degree of crystallinity, and we will only consider two-level systems (TLSs) in the rest of the structure.

The TLSs can only dissipate energy if they are coupled to the vibrating graphene sheet. A possible mechanism is the existence of charge impurities associated to these defects (fluctuating charges), which are electrostatically coupled to the conducting electrons in the graphene.

We expect this mechanism to be less effective in the device considered here than in NEMs made of semiconducting materials, as now the TLSs reside in the  \( SiO_{2} \)  substrate, not in the vibrating structure. The coupling, arising from long range forces, will be in comparison accordingly suppressed, by a factor of order  \( (a/d)^{n} \) , where a is a length comparable to the interatomic separation, and n describes the decay of the coupling (n = 1 for the Coulomb potential between charged systems).

The temperature dependence of the contribution of TLSs to  \( Q^{-1} \)  is determined by the density of states of the modes coupled to the TLSs and the distribution of TLSs in terms of their parameters (tunneling amplitude  \( \Delta_{0}^{x} \)  and bias  \( \Delta_{9}^{z} \) ) \( ^{16} \) . The hamiltonian describing the coupling of the effective TLS's and the oscillating graphene sheet is given by \( ^{16} \) 

 \[ H=\epsilon\sigma_{x}+\frac{\Delta_{0}^{x}}{\epsilon}\sigma_{z}\sum_{\mathbf{k}}\lambda_{\mathbf{k}}(b_{\mathbf{k}}+b_{\mathbf{k}}^{\dagger})_{+}+\sum_{\mathbf{k}}\hbar\omega_{\mathbf{k}}(b_{\mathbf{k}}^{\dagger}b_{\mathbf{k}}+\mathrm{h.c.}) \quad (12) \] 

where  \( \epsilon=\sqrt{(\Delta_{0}^{x})^{2}+(\Delta_{0}^{z})^{2}} \) ,  \( \gamma \)  is the coupling constant, which will be strongly suppressed in these devices as compared to attenuation of acoustic waves in amorphous materials,  \( \gamma\sim1eV\times(a/d)^{n} \) ,  \( b_{k}^{\dagger} \)  represent the phonon creation operators associated to the different vibrational modes of a sheet, and  \( \sum_{\mathbf{k}}\lambda_{\mathbf{k}}(b_{\mathbf{k}}+b_{-\mathbf{k}}^{\dagger}) \)  represents the coupling to the strain tensor  \( u_{ik} \) . There are two types, compression modes (longitudinal waves) and bending modes. The damping is due to the initial transfer of energy from the vibrational mode studied by the experimentalists to the TLSs, which in a second step transfer this energy to the rest of the modes. The properties of the spin-boson model, eq.(12), are fully determined by the power-law s of the spectral function \( ^{37} \) ,  \( J(\omega)\equiv\sum_{k}|\gamma\lambda_{k}\Delta_{0}^{x}/\epsilon|^{2}\delta(\omega-\omega_{k})\sim\alpha\omega_{c}^{1-\sigma}s^{\omega} \) , where  \( \omega_{k} \)  is the frequency of mode k,  \( \alpha \)  is an adimensional constant and  \( \omega_{c} \)  is the upper cutoff of the phonon bath. For this system, compression modes give rise to a superohmic, s=2, bath, while the bending modes constitute an ohmic bath, s=1, and thus will prevail as a source of dissipation at low temperatures \( ^{37} \) . We will therefore restrict our analysis to the dissipation caused by the ohmic component of the vibrational spectrum.

Applying the method in \( ^{16} \)  to the 2D bending modes of the graphene sheet, one arrives at  \( J(\omega) = \alpha\omega \) , with

 \[ \alpha\approx4\Big(\gamma\frac{\Delta_{0}^{x}}{\epsilon}\Big)^{2}\frac{\rho_{M}^{1/2}(1+\nu)^{3/2}(1-\nu)^{1/2}}{\hbar t^{2}E^{3/2}\big(9+\frac{3\nu}{1-2\nu}\big)} \quad (13) \]
 

Here  \( \nu \)  is the Poisson ratio of graphene. Choosing fairly symmetrical TLSs,  \( \Delta_{\theta}^{x}/\epsilon \sim 1 \) , for the parameters in table I,  \( \alpha \sim 10^{-5} \times (a/d)^{2n} \) , very small. In ref. \( ^{35} \)  an expression is given for the inverse quality factor of a vibration damped by TLSs in amorphous insulators,

 \[ Q^{-1}(\omega,T)=\frac{P\gamma^{2}}{E k T}\int_{0}^{\epsilon_{m a x}}d\epsilon\int_{u_{m i n}}^{1}d u\frac{\omega}{u\sqrt{1-u^{2}}}C(\omega,T) \quad (14) \] 

where  \( u = \Delta_{r}/\epsilon \) ,  \( \epsilon_{max} \sim 5 \)  K, and  \( (u\sqrt{1-u^{2}})^{-1} \)  comes from the probability density of TLS's in an amorphous solid, like  \( \mathrm{SiO}_{2} \) .  \( Q^{-1}(\omega, T) \)  is a function of  \( C(\omega, T) \) , the Fourier transform of the correlation function  \( C(t, T) = \langle \sigma_{z}(t) \sigma_{z}(0) \rangle_{T} \) . For biased TLSs and  \( \alpha \ll 1 \)  an extensive analysis of  \( C(\omega, T) \)  is performed in \( ^{38} \) , where several expressions are provided in different limits. Using them, the estimate for  \( Q^{-1}(\omega, T) \)  follows:

 \[ \left\{\begin{array}{l}Q^{-1}(\omega,T)\approx\frac{P\gamma^{2}}{E k T}\left\{\frac{4\pi}{3}\alpha\epsilon_{m a x}+\frac{\pi^{2}}{3}\alpha^{2}k T\right\},\quad k T>\epsilon_{m a x}\\ Q^{-1}(\omega,T)\approx\frac{P\gamma^{2}\alpha}{E\hbar\omega}\frac{4\pi}{3}k T,\quad k T<\epsilon_{m a x}\end{array}\right. \quad (15) \] 

In the range of temperatures of current experiments (5K<T<300K), the dependence of dissipation with T is weak, and  \( Q^{-1} \sim 10^{-6} \times (a/d)^{4} \sim 10^{−22} \) . The main uncertainty of the calculation has been the use of the TLSs' distribution assumed for amorphous solids \( ^{39} \) , but due to the small value of  \( \alpha \)  a weak dissipation is expected also with a modified distribution. Thus the conclusion is that the relative importance of TLSs damping is much smaller for graphene than for other NEMs devices \( ^{2,3,40} \) .

## VI. OTHER FRICTION MECHANISMS

## A. Attachment losses.

The energy is transferred from the resonator mode to acoustic modes at the contacts and beyond \( ^{19,20} \) .

The main expressions needed are given in \( ^{20} \) . When  \( d \gg t \) , and d is much smaller than the wavelength of the radiated elastic waves in the  \( SiO_{2} \)  substrate, the contribution to the inverse quality factor is given by

 \[ Q^{-1}\approx\frac{w}{L}\Big(\frac{t}{d}\Big)^{2}\sqrt{\frac{\rho_{M}^{C}E^{C}(1-(\nu^{O})^{2})}{\rho_{M}^{O}E^{O}}} \quad (16) \] 

where the superscript O applies to the silicon oxide, and  \( \nu^{O} \)  stands for Poisson's ratio. The range of values of the quality factor varies from  \( Q^{-1} \approx 5 \cdot 10^{-6} \)  for a graphene monolayer, to  \( Q^{-1} \approx 5 \cdot 10^{-3} \)  for a stack with 30 layers and  \( t = 10nm \) . These quantities probably overestimate the attachment losses, as they do not include the impedance at the  \( SiO_{2} \) -graphene interface.

This damping process due to energy irradiated away from the resonator should not depend on temperature.

## B. Thermoelastic effects.

When the phonon mean free path of the acoustic phonons is shorter than the wavelength of the mode under study, the acoustic phonons can be considered a dissipative environment coupled to the mode by anharmonic terms in the ionic potential \( ^{21,22,23} \) . These anharmonic effects are described by the expansion coefficient,  \( \alpha \) , and the thermal conductivity,  \( \kappa \) . We follow the analysis in \( ^{41} \) . For a rectangular beam vibrating at a frequency  \( \omega \)  the inverse quality factor is

 \[ Q_{Z}^{-1}(T)=\frac{E\alpha^{2}T}{C_{p}}\frac{\omega\tau_{Z}}{1+(\omega\tau_{Z})^{2}} \quad (17) \] 

where E is the Young Modulus,  \( C_{p} \)  is the specific heat at a constant pressure, and  \( \tau_{Z} \)  is the thermal relaxation time associated with the mode, which in the case of a flexural vibration is given by  \( \tau_{Z} = t^{2} C_{p} / (\pi^{2} \kappa) \) . This estimate assumes that the graphene sheet is weakly deformed, and that the typical relaxation time is associated to the diffusion of phonons over distances comparable to the thickness of the sheet.

Although better approximations are available in the literature \( ^{22} \) , eq.(17) is enough for an estimate of the order of magnitude of  \( Q^{-1} \) . Using the parameters from table \( ^{[I]} \) , for  \( t = 10 \, nm \)  and  \( f \sim 100 \, MHz \) , we find that  \( \omega \tau_{Z} \ll 1 \) , and

 \[ Q_{Z}^{-1}(T=300\mathrm{K})\approx\frac{E\alpha^{2}T\omega t^{2}}{\pi^{2}\kappa}\sim5\cdot10^{-7} \quad (18) \] 

## VII. EXTENSION TO NANOTUBE OSCILLATORS.

The analysis presented here can be extended, in a straightforward way, to systems where the oscillating part is a nanotube.

We expect in these devices a larger impedance between the modes of the nanotube and those of the substrate, so that attachment losses will be suppressed with respect to the estimate presented here for graphene.

The damping mechanisms which require long range forces between the moving charges in the nanotube and degrees of freedom of the substrate (fluctuating and static charges) will not be significantly changed. A nanotube of length L at distance d from the substrate will interact with a substrate area of order  \( (L + d) \times d \) . A similar estimate for a graphene sheet of length L and width w gives an area  \( \sim (L + d) \times (w + d) \) . As  \( L \sim w \sim d \sim 1\mu m \) , the two areas are comparable.

On the other hand, ohmic losses induced in the nanotube will be reduced with respect to the two dimensional graphene sheet, as the number of carriers is lower in the nanotube.

Finally, we expect a longer phonon mean free path in the nanotube, which implies that thermoelastic effects will be reduced.
 

<table><tr><td></td><td>\( Q^{-1}(T = 300K) \)</td><td>Temperature dependence</td></tr><tr><td>Charges in the  \( \mathrm{SiO}_{2} \)</td><td>\( 10^{-7} - 10^{-6} \)</td><td>T</td></tr><tr><td>Charges in graphene sheet and metallic gate</td><td>\( 10^{-2} \)</td><td>T</td></tr><tr><td>Velcro effect</td><td>Absent</td><td>\( T^{0} \)</td></tr><tr><td>Two-level systems</td><td>\( 10^{-22} \)</td><td>A + BT</td></tr><tr><td>Attachment losses</td><td>\( 10^{-6} - 10^{-5} \)</td><td>T^{0}</td></tr><tr><td>Thermoelastic losses</td><td>\( 10^{-7} \)</td><td>T</td></tr></table>

TABLE II: Contribution of the mechanisms considered in the main text to the inverse quality factor  \( Q^{-1}(T) \)  of the systems studied in \( ^{4} \) .

## VIII. CONCLUSIONS.

We have considered six possible dissipation mechanisms which may lead to damping in a graphene mesoscopic oscillator. The main results are summarized in Table \( ^{[II]} \) . We expect that the calculations give the correct order of magnitude and dependence on external parameters.

We find that at high temperatures the leading damping mechanism is the ohmic losses in the metallic gate and the graphene sheet. This effect depends quadratically with the total charge at the graphene sheet, which can be controlled by the gate voltage.

At low temperatures attachment losses limit the quality of the vibration. If the resonator is strongly driven, a new damping mechanism may come into play, the Velcro effect, which may limit substantially the quality factor as compared with the slightly driven case. The high crystallinity of the resonators eliminates the main source of dissipation in semiconducting resonators, namely surface-related effective TLSs coupled to the local strain field.

These conclusions apply with only slight modifications to carbon nanotube-based resonators.

## IX. ACKNOWLEDGEMENTS.

F. G. acknowledges funding from MEC (Spain) through grant FIS2005-05478-C02-01 the European Union Contract 12881 (NEST), and CAM (Madrid), through program CITECNOMIK. A. H. C. N. was supported through NSF grant DMR-0343790. We acknowledge many useful discussions with A. M. Van Der Zande and J. Bunch.

## APPENDIX A: COUPLING TO FIXED CHARGES IN THE SiO₂ SUBSTRATE

The Fourier transform of the potential in eq.(1) is:

 \[ V(\vec{\mathbf{q}},\omega)=2\pi e^{2}A e^{-q d}\delta(\omega-\omega_{0}) \quad (A1) \] 

This potential is screened by the polarizability of the graphene layer \( ^{28} \) , so that  \( e^{2} \)  has to be replaced by :

 \[ e^{2}\rightarrow e^{*2}=\frac{e^{2}}{1+e^{2}/|\vec{\mathbf{q}}|\mathrm{Re}[\chi_{0}(|\vec{\mathbf{q}}|,\omega)]}\approx\frac{|\vec{\mathbf{q }}|}{Re[\chi_{0}(|\vec{\mathbf{q}}|,\omega)]} \quad (A2) \] 

where  \( \chi_{0} \)  is the susceptibility of the graphene layer. At low energy and momenta its value tends to the compressibility of the electrons in the layer:

 \[ \lim_{|\vec{\mathbf{q}}|\to0,\omega\to0}\mathrm{Re}[\chi_{0}(|\vec{\mathbf{q}}|,\omega)]=\left\{\begin{array}{ll}\frac{k_{\mathrm{F}}}{v_{\mathrm{F}}^{2}}&N=1\\ \frac{v_{\mathrm{F}}}{v_{\mathrm{F}}^{2}}&N\neq1\end{array}\right. \quad (A3) \] 

where N is the number of layers and  \( \gamma \)  is the interlayer hopping element. For a stack with N layers, we have used the model with one interlayer hopping element \( ^{31} \) , which gives rise to 2N low energy bands, most of which show a quadratic dispersion.

Using Fermi’s golden rule, we finally find for width of the graphene mode  \( (v(\vec{\mathbf{q}},\omega)=v(-\vec{\mathbf{q}},\mathbf{\omega})) \) :

 \[ \Gamma_{\mathrm{p h}}\approx\int d^{2}\vec{\mathbf{q}}|v(\vec{\mathbf{q}})|^{2}\mathrm{I m}\chi_{0}(\vec{\mathbf{q}},\omega_{0}) \quad (A4) \] 

where:

 \[ \mathrm{I m}\chi_{0}(\vec{\mathbf{q}},\omega_{0})\approx\left\{\begin{array}{l l}\frac{|\omega|k_{\mathrm{F}}}{v_{\mathrm{F}}^{2}|\vec{\mathbf{q}}|^{4}}&N=1\\ \frac{|\omega|\gamma^{2}N^{3/2}}{v_{\mathrm{F}}^{2}|\vec{\mathbf{q}}|\sqrt{\rho}}&N\neq1\end{array}\right. \quad (A5) \] 

where, for  \( N \neq 1 \) ,  \( \rho \)  is the total carrier density. This last expressions are valid for lengths bigger than the mean free path,  \( l \gg l_{mfp} \) .

The energy absorbed per cycle of oscillation and unit volume will be  \( \Delta E = (2\pi/\omega_{0})\hbar\omega_{0}\Gamma_{\mathrm{ph}}/twL = 2\pi\hbar\Gamma_{\mathrm{ph}}/twL \) , and the inverse quality factor  \( Q_{\mathrm{ph}}^{-1}(\omega_{0}) \)  will correspond to

 \[ Q_{\mathrm{p h}}^{-1}(\omega_{0})=\frac{1}{2\pi}\frac{\Delta E}{E_{0}}=\frac{\hbar\Gamma_{\mathrm{p h}}}{t w L}\frac{1}{\frac{1}{2}\rho\omega_{0}^{2}A^{2}}=\frac{2\hbar\Gamma_{\mathrm{p h}}}{M\omega_{0}^{2}A^{2}}, \quad (A6) \] 

where  \( E_{0} \)  is the elastic energy stored in the vibration, M is the total mass of the resonator, and A the amplitude of vibration. Substituting eqs.(A1,A2,A3,A5) in eq.(A4), and inserting (A4) in eq.(A6), one arrives at eqs.(2) and (3) for the dissipation due to a single charge in the substrate. The analysis presented here does not consider additional screening due to the presence of a metallic gate. In that case, one needs to add to the potential from a static charge, eq.(1) in the main text, a contribution from the image charge induced by the gate. This effect will reduce the coupling between the graphene layer and charges in the vicinity of the gate.

## APPENDIX B: SCREENING OF THE POTENTIALS AT THE GRAPHENE SHEET AND SI GATE

The equations for the selfconsistent potentials  \( v_{scr}(z,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega) \)  as a function of the bare potentials  \( v_{0}^{r}(z,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega) \)  are given by
 

 \[ \begin{align*}v_{scr}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega)&=v_{0}^{C}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega)+v_{0}^{G}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega)+\int_{C}d\vec{\mathbf{r}}_{1}\int_{C}d\tilde{\mathbf{r}}_{2}v_{\mathrm{Coul}}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}_{1},\omega)\chi^{C}(\vec{\mathbf{r}}_{{1}}-\vec{\mathbf{r}}_{2},\omega)v_{scr}(d,\vec{\mathbf{r}}_{{2}}-\vec{\mathbf{r}}^{\prime},\omega)+\\&+\int_{G}d\vec{\mathbf{r}}_{3}\int_{G}d\tilde{\mathbf{r}}_{4}v_{\mathrm{Coul}}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}_{3},\omega)\chi^{G}(\vec{\mathbf{r}}_{{3}}-\vec{\mathbf{r}}_{4},\omega)v_{scr}(0,\vec{\mathbf{r}}_{{4}}-\vec{\mathbf{r}}^{\prime},\omega)\\v_{scr}(0,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega)&=v_{0}^{G}(0,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega)+v_{0}^{C}(0,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega)+\int_{G}d\vec{\mathbf{r}}_{1}\int_{G}d\tilde{\mathbf{r}}_{2}v_{\mathrm{Coul}}(0,\vec{\mathbf{r}}-\vec{\mathbf{r}}_{1},\omega)\chi^{G}(\vec{\mathbf{r}}_{{1}}-\vec{\mathbf{r}}_{2},\omega)v_{scr}(0,\vec{\mathbf{r}}_{{2}}-\vec{\mathbf{r}}^{\prime},\omega)+\\&+\int_{C}d\tilde{\mathbf{r}}_{3}\int_{C}d\vec{\mathbf{r}}_{4}v_{\mathrm{Coul}}(0,\vec{\mathbf{r}}-\vec{\mathbf{r}}_{3},\omega)\chi^{C}(\vec{\mathbf{r}}_{{3}}-\vec{\mathbf{r}}_{4},\omega)v_{scr}(d,\vec{\mathbf{r}}_{{4}}-\vec{\mathbf{r}}^{\prime},\omega),\end{align*} \quad (B1) \] 

where for example in the first equation  \( v_{0}^{C}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega) \)  represents the bare potential experienced by a point charge e in the graphene layer due to the presence of charges in that same layer, while  \( v_{0}^{G}(d,\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},\omega) \)  is the bare potential experienced by a point charge e in the graphene layer due to the presence of charges in the Si plane.  \( v_{Coul} \)  is the two-dimensional bare Coulomb potential. These equations simplify considerably in the  \( \vec{q} \)  space:

 \[ \left\{\begin{array}{l}v_{s c r}(d,\vec{\mathbf{q}},\omega)=v_{0}^{C}(d,\vec{\textbf{q}},\omega)e^{q d}+v_{0}^{G}(d,\vec{\textbf{q}},\omega)+v_{q}\chi^{C}(\vec{\textbf{q}},\boldsymbol{\omega})v_{s c r}(d,\vec{\textbf{q}},\omega)+v_{q}e^{-q d}\chi^{G}(\vec{\textbf{q}},\boldsymbol{\omega})v_{s c r}(0,\vec{\textbf{q}},\omega)\\ v_{s c r}({0},\vec{\textbf{q}},\omega)=v_{0}^{C}({0},\vec{\textbf{q}},\omega)+v_{0}^{G}({d},\vec{\textbf{q}},\omega)e^{q d}+v_{q}e^{-q d}\chi^{C}(\vec{\textbf{q}},\boldsymbol{\omega})v_{s c r}({d},\vec{\textbf{q}},\omega)+v_{q}\chi^{G}(\vec{\textbf{q}},\boldsymbol{\omega})v_{s c r}({0},\vec{\textbf{q}},\omega)\end{array}\right., \quad (B2) \] 

where  \( v_{q} = 2\pi e^{2}/|\vec{q}| \)  is the Fourier transform of the Coulomb potential in two dimensions, and where  \( v_{0}^{G}(0, \vec{\mathbf{q}}, \omega) \)  and  \( v_{0}^{G}(d, \vec{\mathbf{q}}, \omega) \)  have been expressed in terms of  \( v_{0}^{G}(d, \vec{\mathbf{q}}, \omega) \)  and  \( v_{0}^{C}(0, \vec{\mathbf{q}}, \omega) \) . Now we can calculate  \( v_{scr}(d, \vec{\mathbf{q}}, \omega) \)  and  \( v_{scr}(0, \vec{\mathbf{q}}, \omega) \)  in terms of the rest of the variables,

 \[ \left(\begin{array}{c}{v_{s c r}(d)}\\ {v_{s c r(0)}}\end{array}\right)=\left(\begin{array}{c c}{1-v_{q}\chi^{C}}&{-v_{q}e^{-q d}\chi^{G}}\\ {-v_{q}e^{-d q}\chi^{C}}&{1-v_{q}\chi^{G}}\end{array}\right)^{-1}\times\left(\begin{array}{c c}{e^{q d}}&{1}\\ {1}&{e^{q d}}\end{array}\right)\left(\begin{array}{c}{v_{0}^{C}(0)}\\ {v_{0}^{G}(d)}\end{array}\right) \quad (B3) \] 

The dependence on  \( \vec{q} \)  and  \( \omega \)  has been omitted for the sake of clarity. Now, if we are interested only in the long wavelength limit  \( v_{q}\chi^{C}, v_{q}\chi^{\bar{G}} \gg 1 \) , the last equation simplifies to

 \[ \left(\begin{array}{c}{v_{s c r}(d)}\\ {v_{s c r(0)}}\end{array}\right)=\frac{1}{v_{q}^{2}\chi^{C}\chi^{G}\left(1-e^{-2q d}\right)}\times\left(\begin{array}{c c}{v_{q}\left(\chi^{C}e^{-q d}-\chi^{G}e^{q d}\right)}&{v_{q}\left(-\chi^{G}+\chi^{C}\right)}\\ {v_{q}\left(-\chi^{C}+\chi^{G}\right)}&{v_{q}\left(\chi^{G}e^{-q d}-\chi^{C}e^{q d}\right)}\end{array}\right)\left(\begin{array}{c}{v_{0}^{C}(0)}\\ {v_{0}^{G}(d)}\end{array}\right) \quad (B4) \] 

 \[ a.\quad Values of v_{0}^{C}(0,\vec{\mathbf{q}},\omega)and v_{0}^{G}(d,\vec{\mathbf{q}}.\omega) \] 

Now we will calculate the parts of these terms which will give rise to a coupling to the vibration. When the graphene layer is set into motion with a bending mode of wavevector  \( \vec{q} \)  and amplitude  \( A_{\vec{q}} \) , the potential of a point charge e in the Si plane due to the charge in the graphene layer,  \( v_{0}^{C}(0,\vec{\mathbf{r}},t) \) , is
 

 \[ \begin{align*}v_{0}^{C}(0,\vec{\mathbf{r}},t)&=\frac{1}{2}\int_{C}d\vec{\mathbf{r}}^{\prime}v_{\mathrm{Coul}}(\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime},z^{\prime})\rho(\vec{\mathbf{r}}^{\ prime},z^{\prime},t)=\frac{1}{2}\int_{C}d\vec{\mathbf{r}}^{\prime}\frac{2\pi e^{2}\rho_{0}}{\sqrt{(\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime})^{2}+(d+A_{\vec{\mathbf{q}}}e^{i(\vec{\mathbf{q}}\vec{\mathbf{r}}^{\prime}-\omega_{\vec{\mathbf{q}}}t))^{2}}}\\&\approx\frac{1}{2}\int_{C}d\vec{\mathbf{r}}^{\prime}\frac{2\pi e^{2}\rho_{0}}{\sqrt{(\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime})^{2}+d^{2}}}+\frac{1}{2}\int_{C}d\vec{\mathbf{r}}^{\prime}\frac{2\pi e^{2}\rho_{0}A_{\vec{\mathbf{q}}}e^{i(\vec{\mathbf{q}}\vec{\mathbf{r}}^{\prime}-\omega_{\vec{\mathbf{q}}}t)d}}{\left((\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime})^{2}+d^{2}\right)^{3/2}}\approx f(\vec{\mathbf{r}})+\pi e^{2}\rho_{0}A_{\vec{\mathbf{q}}}e^{-dq}e^{i(\vec{\mathbf{q}}\vec{\mathbf{r}}^{\prime}-\omega_{\vec{\mathbf{q}}}t)}\end{align*} \quad (B5) \] 

where in the second line an expansion for small  \( A_{q} \)  has been performed. The Fourier transform for  \( \omega \neq 0 \)  is

 \[ v_{0}^{C}(0,\vec{\mathbf{k}},\omega^{\prime})=\pi e^{2}\rho_{0}A_{\vec{\mathbf{q}}}e^{-d q}\delta(\vec{\mathbf{k}}-\vec{\mathbf{q}})\delta(\omega^{\prime}-\omega_{\vec{\mathbf{q}}})\quad,\quad|\vec{\mathbf{q}}|=1/L \quad (B6) \] 

Similarly, the potential of a point charge in the oscillating graphene sheet due to the charge in the Si plane  \( v_{0}^{G}(d) \) , is

 \[ v_{0}^{G}(d,\vec{\mathbf{r}},t)=\frac{1}{2}\int_{G}d\vec{\mathbf{r}}^{\prime}\frac{2\pi e^{2}\rho_{0}}{\sqrt{(\vec{\mathbf{r}}-\vec{\mathbf{r}}^{\prime})^{2}+(d+A_{\vec{\mathbf{q}}}e^{i(\vec{\mathbf{q}}\vec{\mathbf{r}}^{\prime}-\omega_{\vec{\mathbf{q}}}t))^{2}}}\approx f(\vec{\mathbf{r}})+\pi e^{2}\rho_{0}A_{\vec{\mathbf{q}}}e^{i(\vec{\mathbf{q}}\vec{\mathbf{r}}^{\prime}-\omega_{\vec{\mathbf{q}}}t)} \quad (B7) \] 

leading to the same expression as eq.(B6) but without the factor  \( e^{-qd} \) 

 \[ v_{0}^{G}(d,\vec{\mathbf{k}},\omega^{\prime})=v_{0}^{C}(0,\vec{\mathbf{k}},\omega^{\prime})e^{q d} \quad (B8) \] 

 \( ^{1} \)  A. N. Cleland, Foundations of Nanomechanics (Springer (Berlin), 2002).

 \( ^{2} \)  M. Blencowe, Phys. Rep. 395, 159 (2004).

 \( ^{3} \)  K. L. Ekinci and M. L. Roukes, Rev. Sci. Inst. 76, 061101 (2005).

 \( ^{4} \)  J. S. Bunch, A. M. van der Zande, S. S. Verbridge, I. W. Frank, D. M. Tanenbaum, J. M. Parpia, H. G. Craighead, and P. L. McEuen, Science 315, 490 (2007).

 \( ^{5} \)  V. Sazonova, Y. Yaish, H. Ustunel, D. Roundy, T. A. Arias, and P. L. McEuen, Nature 431, 284 (2004).

 \( ^{6} \)  V. Sazonova, Ph.D. thesis, Cornell University, Ithaca NY (2006).

 \( ^{7} \)  A. K. Geim and K. S. Novoselov, Nature Materials 6, 183 (2007).

 \( ^{8} \)  L. Wirtz and A. Rubio, Sol. State Comm. 131, 141 (2004).

 \( ^{9} \)  J. C. Meyer, A. K. Geim, M. I. Katsnelson, K. S. Novoselov, T. J. Booth, and S. Roth, Nature 446, 60 (2007).

 \( ^{10} \)  M. Ishigami, J. Chen, W. Cullen, M. Fuhrer, and E. Williams, Nano Lett. 7, 1643 (2007).

 \( ^{11} \)  E. Stolyarova, K. T. Rim, S. Ryu, J. Maultzsch, P. Kim, L. E. Brus, T. F. Heinz, M. S. Hybertsen, and G. W. Flynn, PNAS 104, 9209 (2007).

 \( ^{12} \)  J. Martin, N. Akerman, G. Ulbricht, T. Lohmann, J. H. Smet, K. von Klitzing, and A. Yacoby (2007), arXiv:0705.2180.

 \( ^{13} \)  S. Cho and M. S. Fuhrer (2007), arXiv:0705.3239.

 \( ^{14} \)  K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang,

Substituting (B6,B8) in eq.(B4), one obtains eq.(9).

Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Science 306, 666 (2004).

 \( ^{15} \)  G. Zolfagharkhani, A. Gaidarzhy, R. L. Badzey, and P. Mohanty, Phys. Rev. Lett. 94, 030402 (2005).

 \( ^{16} \)  C. Seoanez, F. Guinea, and A. H. Castro Neto, Europhys. Lett. 78, 60002 (2007).

 \( ^{17} \)  J. L. Yang, T. Ono, and M. Esashi, J. Microelectromech. Syst. 11, 775 (2002).

 \( ^{18} \)  M. Chu, R. E. Rudd, and M. P. Blencowe (2007), cond-mat/0705.0015.

 \( ^{19} \)  Y. Jimbo and K. Itao, J. Horological Inst. Jpn. 47, 1 (1968).

 \( ^{20} \)  D. M. Photiadis and J. A. Judge, Applied Physics Letters 85, 482 (2004).

 \( ^{21} \)  C. Zener, Phys. Rev. 53, 90 (1938).

 \( ^{22} \)  R. Lifshitz and M. Roukes, Phys. Rev. B 61, 5600 (2000).

 \( ^{23} \)  H. Üstunel, Ph.D. thesis, Cornell University, Ithaca NY (2006).

 \( ^{24} \)  P. Mohanty, D. A. Harrington, K. L. Ekinci, Y. T. Yang, M. J. Murphy, and M. L. Roukes, Phys. Rev. B 66, 085416 (2002).

 \( ^{25} \)  H. Pierson, Handbook of Carbon, Graphite, Diamond and Fullerenes - Properties, Processing and Applications (William Andrew Publishing/Noyes, New York, 1993).

 \( ^{26} \)  K. Nomura and A. MacDonald, Phys. Rev. Lett. 98, 076602 (2007).

 \( ^{27} \)  E. H. Hwang, S. Adam, and S. D. Sarma, Phys. Rev. Lett.
 

98, 186806 (2006).

 \( ^{28} \)  B. Wunsch, T. Stauber, F. Sols, and F. Guinea, New. Journ. Phys. 8, 318 (2006).

 \( ^{29} \)  F. Guinea, R. A. Jalabert, and F. Sols, Phys. Rev. B 70, 085310 (2004).

 \( ^{30} \)  F. Guinea, Phys. Rev. B 71, 045424 (2005).

 \( ^{31} \)  F. Guinea, A. H. Castro Neto, and N. M. R. Peres, Phys. Rev. B 73, 245426 (2006).

 \( ^{32} \)  A. M. Van Der Zande, private communication.

 \( ^{33} \)  Y. Dong, S. Pappu, and Z. Xu, Anal. Chem. 70, 4730 (1998).

 \( ^{34} \)  P. Anderson, B. Halperin, and C. Varma, Philos. Mag. 25, 1 (1972).

 \( ^{35} \)  P. Esquinazi, ed., Tunneling Systems in Amorphous and

Crystalline Solids (Springer (Berlin), 1998).

 \( ^{36} \)  P. Esquinazi, M. A. Ramos, and R. König, J. Low Temp. Phys. 135, 27 (2004).

 \( ^{37} \)  A. J. Leggett, S. Chakravarty, A. T. Dorsey, M. P. A. Fisher, A. Garg, and W. Zwerger, Rev. Mod. Phys. 59, 1 (1987).

 \( ^{38} \)  U. Weiss, Quantum Dissipative Systems (World Scientific (Singapore), 1999).

 \( ^{39} \)  W. A. Phillips, Rep. Prog. Phys. 50, 1657 (1987).

 \( ^{40} \)  A. N. Cleland and M. L. Roukes, J. Appl. Phys. 92, 2758 (2002).

 \( ^{41} \)  C. Zener, Elasticity and Anelasticity of Metals (The University of Chicago Press (Chicago), 1948).
 
