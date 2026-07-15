
# Kondo effect of magnetic impurities on nanotubes

P. P. Baruselli \( ^{a,b} \) , A. Smogunov \( ^{b,c,d,e} \) , M. Fabrizio \( ^{a,c,f} \) , E. Tosatti \( ^{a,c,f) \) 

 \( ^{a} \) SISSA, Via Beirut 2/4, Trieste 34014, Italy

 \( ^{b} \)  CNR-IOM Democritos, Via Beirut 2/4, Trieste 34014, Italy

 \( ^{c} \) ICTP, Strada Costiera 11, Trieste 34014, Italy

 \( ^{d} \) Voronezh State University, University Square 1, Voronezh 394006, Russia

 \( ^{e} \) present address: CEA Saclay, France

 \( ^{f} \) INFM, Democritos Unità di Trieste, Via Beirut 2/4, Trieste 34014, Italy

## Abstract

The effect of magnetic impurities on the ballistic conductance of nanocontacts is, as suggested in recent work, amenable to ab initio study [1]. Our method proceeds via a conventional density functional calculation of spin and symmetry dependent electron scattering phase shifts, followed by the subsequent numerical renormalization group solution of Anderson models – whose ingredients and parameters are chosen so as to reproduce these phase shifts. We apply this method to investigate the Kondo zero bias anomalies that would be caused in the ballistic conductance of perfect metallic (4,4) and (8,8) single wall carbon nanotubes, ideally connected to leads at the two ends, by externally adsorbed Co and Fe adatoms. The different spin and electronic structure of these impurities are predicted to lead to a variety of Kondo temperatures, generally well below 10 K, and to interference between channels leading to Fano-like conductance minima at zero bias.

Keywords: Kondo effect, phase shifts, carbon nanotubes, magnetic impurities, zero-bias anomalies

## 1. Introduction

The zero-bias anomalies observed in STS conductance spectroscopy through adsorbed magnetic impurities and to some extent in metal break junctions have recently revived interest in the Kondo effect. Addressing these systems theoretically poses several problems. In the first place, and unlike quantum dots, ab initio electronic structure calculations such as density functional theory (DFT) are essential to establish a quantitatively meaningful starting point. Which among the impurity-related levels and resonances drive the spin polarization, what is their multiplicity, their hybridization, etc. are all questions that need an ab initio calculation. Next, this information must be translated into some manageable many body Hamiltonian, possibly without the loss of the brute quantitative information provided by DFT. Finally, the many body Hamiltonian(s) must be solved, to extract Kondo parameters and the predicted conductance features near zero bias, possibly with their behavior with parameters such as nanocontact geometry, temperature and external field, to be eventually compared with experiment. One approach in this direction was recently taken by our group [1]. Given a nanocontact between two leads, one identifies, with the help of symmetry, the impinging and outgoing channels that carry current across the impurity. From the matching symmetry selected local densities of states at the impurity, one identifies the important impurity orbitals with their different magnetic splittings and hybridizations. This leads to formulate multiorbital Anderson models, which contain a multiplicity of parameters to be adjusted. In our scheme the parameters are adjusted to yield, within the Hartree-Fock approximation, the same channel- and spin-dependent impurity scattering phase shifts as those that we calculate ab initio by DFT – whose input information is therefore put to maximal use. For the last step, solving the Anderson models, we employed a standard numerical renormalization group (NRG) scheme. While other groups have dealt with the overall Kondo problem in different ways [2, 3], we find our “DFT + NRG” route extremely instructive, and worth exploring in more complex situations than the simple Au-Ni-Au contact studied in Ref [1]. In the present application we consider a single wall carbon nanotube (SWNT) as our linear conducting system, and a single externally adsorbed transition metal atom, either Co or Fe, as the magnetic impurity. To begin with, the metallic nanotube has two conducting channels instead of only one as Au. The magnetic atoms in turn have in principle a richer multiplicity of magnetic levels than Ni. We wish to explore what this richness might bring.

## 2. Systems and symmetries

We considered alternatively Co or Fe impurities on either (4,4) or (8,8) metallic SWNTs (see fig. 1). If z is the SWNT axis, its electronic states of can be classified according to parity with respect to xy plane reflection (e−o, even- odd) and xz plane reflection (s − a, symmetric and antisymmetric). DFT calculations (see section 3) predict that the externally adsorbed impurities should have minimum energy when at the hollow site (see fig. 2), that is above the center of a carbon hexagon. Assuming that geometry, the impurity electronic states can be classified according to the same parity numbers as those of clean
 

SWNTs. We are interested in particular in 3d and 4s impurity orbitals, whose parities are shown in tab. 1.

## 3. Ab initio electronic structure

We carried out standard density-functional theory (DFT) calculations, allowing for full relaxation of all atomic positions in a unit cell, which comprised 80 and 160 carbon atoms for the (4,4) and (8,8) tubes respectively plus one Co or Fe adsorbed impurity. Calculations used the standard plane-wave package Quantum-ESPRESSO [4] within the generalized gradient approximation (GGA) to exchange-correlation functionals in parametrization of Perdew, Burke and Ernzerhof. The plane wave cut-offs were 30 Ry and 300 Ry for the wave functions and for the charge density, respectively. Integration over the one-dimensional Brillouin zone was accomplished using 8 k-points and a smearing parameter of 10 mRy. When necessary to test the sensitivity of DFT results to correlation effects, we extended to “GGA+U” with a reasonably small Hubbard “U” [4]– but generally the straight DFT result was used.

We found that Co behaves as a  \( S = \frac{1}{2} \)  impurity on both (4,4) and (8,8) SWNTs, its  \( d_{xz} \)  orbital driving the spin polarization. The Co atom switches from the  \( 3d^{7}4s^{2} \)  configuration of the isolated atom to a slightly surprising low-spin  \( 3d^{9}4s^{0} \)  one when adsorbed on the nanotube. Fe behaves as a S = 1 impurity on the (8,8) tube, similarly switching from the high-spin  \( 3d^{6}4s^{2} \)  of the isolated atom to a low-spin  \( 3d^{8}4s^{0} \)  in the adsorbed state. Here the pair of orbitals  \( d_{xz} \)  and  \( d_{xy} \)  is magnetically polarized (see fig. 3 and tab. 2), a result in good agreement with previous calculations [5, 6]. Orbitals  \( d_{xy} \)  for Co and  \( d_{z^{2}} \)  for Fe are partly empty, and fall near the Fermi energy in straight DFT: but they promptly move below  \( E_{F} \)  when even a small U is switched on. We conclude that these orbitals are not going to be involved in Kondo behaviour and can be neglected to a first approximation in order to keep the many-body model simple. The behavior of Fe/(4,4) is complicated. The s orbital is partly filled, and  \( d_{z^{2}} \)  is magnetically polarized besides the  \( (d_{xz}, d_{xy}) \)  pair, so here Fe should behave as a  \( S = \frac{3}{2} \)  impurity.

As in previous work [1] we implemented DFT computation of the (spin-polarized) mean-field ballistic conductance and, more importantly, of the impurity-related spin- and channel-selected phase shifts suffered by the SWNT conduction electrons as a function of energy. An example is shown in fig. 4 for Co on the (4,4) SWNT.

## 4. Generalized Anderson model

The Kondo model is usually understood by means of a many-body Anderson Hamiltonian [7]. In our case we need to extend it in principle to the four SWNT conduction bands, each hybridized with some impurity orbital among the 3d and 4s, of same symmetry. These impurity orbitals in turn are mutually coupled by an intra-atomic ferromagnetic Hund exchange term,

 \[ H=\sum_{i=e,s,e a,o,s,o a}H_{i}^{A n d}+H_{H u n d} \quad (1) \] 

 \[ H_{H u n d}=J\sum_{i<j,j=1,4}\vec{\sigma}_{i}\cdot\vec{\sigma}_{j} \quad (2) \] 

 \[ \vec{\sigma}_{i}=\frac{1}{2}\sum_{\alpha\beta}d_{i\alpha}^{\dagger}\vec{s}_{\alpha\beta}d_{i\beta} \quad (3) \] 

 \[ H_{i}^{A n d}=\sum_{k}\epsilon_{i k}c_{i k}^{\dagger}c_{i k-t i}c_{i}^{\dagger}c_{i}+V_{i}(c_{i}^{\dagger}d_{i}+d_{i}c_{i}^{\dagger})+\epsilon_{i}d_{i}^{\dagger}d_{i}+U_{i}n_{i}^{\dagger}n_{i}^{\dagger}(4) \] 

where  \( d_{i}^{\dagger} \)  creates an electron on the impurity orbital with symmetry i,  \( c_{ik}^{\dagger} \)  creates an electron in a k conduction state with symmetry i,  \( \vec{s} \)  are the Pauli matrices,  \( t_{i} \)  is a potential scattering term due to the charge density of the impurity,  \( V_{i} \)  is the coupling of the impurity orbital with the conduction electron states,  \( \epsilon_{i} \)  is the bare energy of the impurity orbital,  \( U_{i} \)  is the Hubbard repulsion on the orbital, J < 0 is a global Hund exchange parameter (favouring high spin for the isolated impurity), and the single particle energies of conduction electrons  \( \epsilon_{ik} \)  are such as to give a constant density of states, with exactly the same value as that of the clean SWNT (per spin direction) as computed by DFT:

 \[ \sum_{k}\delta(\epsilon-\epsilon_{i k})=\rho\simeq\frac{1}{12\mathrm{e V}},\quad i=e s,e o,a s,a o \quad (5) \] 

In practice, only conduction bands coupled to a magnetic orbital are retained in our NRG procedure (see section 6). This leaves us with a single band coupled to a single impurity level in the case of Co (once orbital  \( d_{xy} \)  is ignored), and with two bands, each coupled to one impurity level, in the case of Fe/(8,8) (once orbital  \( d_{z^{2}} \)  is ignored). The case of Fe/(4,4) is more involved and we will presently not deal with it.

## 5. Joining up DFT and many body

Hamiltonian eq. 1 is easily solved in the (unrestricted) Hartree-Fock approximation [7], breaking spin rotational symmetry. This leads to a phase shift in conduction electrons of symmetry  \( i (i = es, eo, as, ao) \)  at the Fermi energy

 \[ \delta_{i}^{\sigma}=\phi_{i}+\arctan\frac{\Gamma_{i}}{\epsilon_{i}^{\sigma}} \quad (6) \] 

where  \( \phi_{i} = \arctan \pi p_{ti} = 0 \)  is the phase shift caused by the impurity charge scattering. This is numerically found to be negligible, so we shall ignore it from now on. The peak of the impurity DOS is found to be at

 \[ \epsilon_{i}^{\sigma}=\epsilon_{i}+U_{i}\langle n_{i}^{-\sigma}\rangle-\sigma\frac{J}{2}(m_{l o t}-m_{i}) \quad (7) \] 

where

 \[ \langle n_{i}^{\sigma}\rangle=\frac{1}{\pi}\arctan\frac{\Gamma_{i}^{\sigma}}{\epsilon_{i}^{\sigma}} \quad (8) \] 

is the average occupation of up/down orbital

 \[ m_{i}=\langle n_{i}^{\uparrow}\rangle-\langle n_{i}^{\downarrow}\rangle \quad (9) \] 

is the magnetization of each orbital and

 \[ m_{l o t}=\sum_{i=1}^{n}m_{i} \quad (10) \]
 

is the total magnetization of the atom. As in [1], we choose to reproduce the same phase shifts at the Fermi energy for each symmetry, and the same peaks in the density of states of the impurity orbitals as those computed by DFT. This allows to uniquely fix  \( \epsilon_{i} \) ,  \( U_{i} \)  and  \( \Gamma_{i} \)  as long as just one magnetic orbital is considered in eq. 1 – that is the case of Co (i = os). When more than one orbital is involved, such as in Fe, (or in Co if orbital  \( d_{xy} \)  were to be taken into account) we need to fix J as well. We can extract J from the DFT calculated exchange splitting of filled orbitals, according to

 \[ \epsilon_{f}^{\uparrow}-\epsilon_{f}^{\downarrow}=\frac{1}{2}m_{tot} \quad (11) \] 

Since different d orbitals have slightly different splittings, we just took an average value as deduced from different orbitals. This yields  \( J \sim 1 \)  eV in Co and  \( J \sim \)  1.2 eV in Fe.

## 6. Results of NRG calculations

We solved the Anderson Hamiltonian by means of NRG [8, 9], which allows to compute all the needed static and dynamic quantities we need in an almost exact, albeit numerical, way. We extracted the conduction electrons phase shifts from the single particle energies at the zero energy fixed point, and the Kondo temperature from the impurity Green function at imaginary frequency:

 \[ G(i\epsilon)=\frac{1}{i\epsilon-\epsilon_{i}-\Sigma(i\epsilon)+i\Gamma_{i}}=\frac{1}{Z_{part}}\sum_{n}\frac{|\langle G S|d|n\rangle|^{2}}{i\epsilon-\epsilon_{n}} \quad (12) \] 

 \( (Z_{part} \)  is the partition function and GS the ground state). The Kondo temperature is given by

 \[ T_{K}=\frac{\pi w Z\Gamma}{4k_{b}} \quad (13) \] 

where w = 0.4128 is the Wilson coefficient and Z is the quasi-particle residue

 \[ Z^{-1}=1-\frac{\partial\Sigma(i\epsilon)}{\partial(i\epsilon)} \quad (14) \] 

Alternatively, an approximate formula [10], valid for one impurity coupled to one channel,

 \[ T_{K}\sim0.4107\sqrt{\frac{U_{i}\Gamma_{i}}{2}}e^{\pi\epsilon_{i}(\epsilon_{i}+U_{i})/2\Gamma_{i}U_{i}} \quad (15) \] 

could be used, with similar results.

The zero-bias conductance is given, in terms of the final phase shifts, by

 \[ g\equiv\frac{G}{G_{0}}=\cos^{2}(\delta_{e s}-\delta_{o s})+\cos^{2}(\delta e_{a}-\delta o_{a})\equiv g_{s}+g_{a} \quad (16) \] 

where  \( G_{0} \equiv \frac{2e^{2}}{h} \)  is the quantum of conductance. Note that in the clean tube  \( G = 2G_{0} \) . Phase shifts are only computed for Kondo channels, and are found to be always  \( \simeq \pi/2 \) . For the non-Kondo channels, they can be directly extracted from DFT. Since in DFT they are  \( \simeq 0 \) , they can be safely neglected. Summing up, both  \( \mathrm{Co}/(4,4) \)  and  \( \mathrm{Col}/(8,8) \)  should exhibit a (zero temperature and zero bias) conductance  \( G \sim G_{0} \) , whereas  \( \mathrm{Fe}/(8,8) \)  should have  \( G \sim 0 \) . These results remain valid so long as either temperature and/or bias remain well below  \( T_{K} \) . However, it turns out that Kondo temperatures  \( T_{k} \)  are quite low (see tab. 3), which might make this effect hard to observe in a real experiment. Interestingly, a much higher Kondo temperature of about 15 K has been quoted for  \( \mathrm{Co} \) /graphene[11]. While the reasons for this difference between graphene and nanotubes are presently being investigated, it should be noted that several factors differ, including symmetry, and heavy doping in real, deposited graphene.

Finally, we can qualitatively address the predicted bias-dependent lineshape of the Kondo conductance anomaly. Through the Keldysh technique for non-equilibrium Green functions it is possible to compute the finite-bias conductance [12], once the impurity Green function  \( G_{i}(\epsilon) \)  is calculated from NRG [13]:

 \[ g_{s,a}=1-\Gamma\overline{{S}}G_{i}(\epsilon) \quad (17) \] 

For simplicity, we have taken

 \[ G_{i}(\epsilon)=\frac{\Gamma_{k}/\Gamma}{\epsilon+i\Gamma_{k}} \quad (18) \] 

where

 \[ k_{b}T_{K}=\frac{w\pi}{4}\Gamma_{K}=0.342\Gamma_{k} \quad (19) \] 

This gives rise to a Fano lineshape [14]

 \[ g_{s,a}=\frac{(q+v)^{2}}{(q^{2}+1)(v^{2}+1)},\qquad v\equiv\epsilon/\Gamma_{k} \quad (20) \] 

with q = 0, so for each band  \( (s - a) \)  the lineshape is predicted to be a symmetric antilorentzian, with a width proportional to the Kondo temperature. Small sources of asymmetry will arise from a) the potential scattering  \( t_{i} \)  which we ignored in Eq. 4; b) from the interference with orbitals belonging to the same band a or s, but with different symmetry  \( e/o \) ; and c) from particle-hole asymmetries in eq. 18. However, we estimate that the asymmetry parameter q should generally remain below 0.1. In  \( \mathrm{Co}/(4,4) \)  and  \( \mathrm{Col}/(8,8) \) , only  \( g_{s} \)  contributes to the lineshape,  \( g_{a} \)  being almost one – and moreover independent from energy on the Kondo energy scale. In  \( \mathrm{Fe}/(8,8) \) , both  \( g_{s} \)  and  \( g_{a} \)  have an antilorentzian shape, although with very different widths. The total lineshape is just their sum (see fig. 5).

## 7. Conclusions

We implemented our recently devised DFT+NRG scheme [1] to calculate the Kondo effect caused by Co and Fe adsorbed impurities on the conductance of (4,4) and (8,8) nanotubes. On the methodological side, the present calculation represents a good pedagogical illustration of our technique. For the systems chosen, the predicted anomalies are symmetric antilorentzian dips, reducing total zero bias conductance to zero for Fe, and by a factor 1/2 for Co. While there are no data to compare with,
 

<table><tr><td></td><td>s</td><td>a</td></tr><tr><td>e</td><td>\( d_{z^{2}}, d_{x^{2}-y^{2}}, s \)</td><td>\( d_{xy} \)</td></tr><tr><td>o</td><td>\( d_{xz} \)</td><td>\( d_{yz} \)</td></tr></table>

Table 1: Symmetries of d and s orbitals with respect to the xy plane (even e - odd o) and the xz plane (symmetric s - antisymmetric a).

<table><tr><td>Impurity</td><td>Magnetic Orbital</td><td>Symmetry</td><td>Spin</td></tr><tr><td rowspan="2">Co</td><td>\( d_{xz} \)</td><td>os</td><td>\( \frac{1}{2} \)</td></tr><tr><td>\( (d_{xy}) \)</td><td>ea</td><td>0</td></tr><tr><td rowspan="3">Fe</td><td>\( d_{xz} \)</td><td>os</td><td>\( \frac{1}{2} \)</td></tr><tr><td>\( d_{xy} \)</td><td>ea</td><td>\( \frac{1}{2} \)</td></tr><tr><td>\( (d_{z^{2}}, s) \)</td><td>es</td><td>0</td></tr></table>

Table 2: Magnetic orbitals as found from DFT calculations, their symmetry, and spin theory (S = 1/2 for each magnetic orbital). Orbitals in parentheses are not Kondo orbitals, so do not contribute to the total spin of the impurity and are ignored in the many-body model, but still participates in transport.

this prediction should in principle be amenable to experimental check. However, we note that our calculated Kondo temperatures are very small, which might constitute and experimental challenge.

This work was sponsored under PRIN/COFIN, and also under FANAS/AFRI. We are indebted to A. Ferretti, P. Lucignano, R. Mazzarello, and L. De Leo for early collaboration and discussions.

## References

[1] P. Lucignano, R. Mazzarello, A. Smogunov, M. Fabrizio, and E. Tosatti, Nature Materials 8, 563 (2009).

[2] M. Reyes Calvo, J. Fernández-Rossier, J. J. Palacios, D. Jacob, D. Natelson, and C. Untiedt, Nature 458, 1150 (2009).

[3] T. A. Costi, L. Bergqvist, A. Weichselbaum, J. von Delft, T. Micklitz, A. Rosch, P. Mavropoulos, P. H. Dederichs, F. Mallet, L. Saminadayar, and C. Bäuerle, Phys. Rev. Lett. 102, 056802 (2009).

[4] www.quantum-espresso.org

[5] E. Durgun, S. Dag, V. M. K. Bagci, O, Gülseren, T. Yildirim, and S. Ciraci, Phys. Rev. B 67, 201401 (2003).

[6] Y. Yagi, T. M. Briere, M. H. F. Sluiter, V. Kumar, A. A. Farajian, and Y. Kawazoe, Phys. Rev. B 69, 075414 (2004)

[7] P. W. Anderson, Phys. Rev. 124, 41 (1961).

[8] K. G. Wilson, Rev. Mod. Phys. 47, 773 (1975).

[9] R. Bulla, T. A. Costi, and T. Pruschke, Rev. Mod. Phys. 80, 395 (2008).

[10] A. Hewson, The Kondo problem to heavy fermions, Cambridge Univ. Press (1993).

[11] T. O. Wehling, A. V. Balatsky, M. I. Katsnelson, A. I. Lichtenstein, and A. Rosch, Phys. Rev. Lett. 81, 115427 (2010).

[12] Y. Meir and N. S. Wingreen, Phys. Rev. Lett. 68, 2512 (1992).

[13] T. A. Costi, A. C. Hewson, and V. Zlatic, J. Phys.: Condens. Matter 6, 2519 (1994).

[14] U. Fano, Phys. Rev. 124, 1866 (1961).

<table><tr><td>Imp.</td><td>SWNT</td><td>Orb.</td><td>\( \epsilon_{d} \) (eV)</td><td>U(eV)</td><td>\( \Gamma \) (eV)</td><td>\( T_{K} \) (K)</td></tr><tr><td rowspan="2">Co</td><td>(4,4)</td><td>\( d_{xz} \)</td><td>-1.62</td><td>2.17</td><td>0.082</td><td>\( \sim \)  1</td></tr><tr><td>(8,8)</td><td>\( d_{xz} \)</td><td>-1.83</td><td>2.11</td><td>0.054</td><td>\( \sim \)  1</td></tr><tr><td rowspan="2">Fe</td><td rowspan="2">
(8,8)
</td><td>\( d_{xz} \)</td><td>-1.24</td><td>2.01</td><td>0.060</td><td>\( \sim \)  10 \( ^{-4} \)</td></tr><tr><td>\( d_{xy} \)</td><td>-1.38</td><td>2.13</td><td>0.043</td><td>\( \sim \)  10 \( ^{-3} \)</td></tr></table>

Table 3: Recapitulative table of important quantities of our Anderson models. Kondo temperature is so low in Fe due to the reduced broadening  \( \Gamma \)  and to the Hund coupling J that couples the two impurity orbitals.

![](./images/867772228014441131_1.jpg)

Figure 1: A schematic view of clean (4,4) and (8,8) SWNTs with their symmetries.
 
![](./images/867772228014441131_2.jpg)

Figure 2: A schematic view of (4,4) and (8,8) SWNTs with an impurity adsorbed in the hollow position.

![](./images/867772228014441131_3.jpg)

![](./images/867772228014441131_4.jpg)

Figure 3: Projected density of states of impurity 3d and 4s orbitals. Above: Co on (4,4) SWNT; below: Fe on (8,8) SWNT.
 
![](./images/867772228014441131_5.jpg)

![](./images/867772228014441131_6.jpg)

Figure 4: Above: conductance as a function of energy of conduction electrons for Co on (4,4) SWNT, for each symmetry s - a and spin direction u - d (up-down); below: phase shift of conduction electrons for different symmetries s - a, e - o and spin directions u - d.

![](./images/867772228014441131_7.jpg)

![](./images/867772228014441131_8.jpg)

Figure 5: Predicted zero-bias anomaly for Co impurity on both (4,4) and (8,8) SWNTs (above) and for Fe on (8,8) SwNT (below) ( \( g \equiv G/G_{0} \) ,  \( G_{0} = 2e^{2}/h \) ).
 
