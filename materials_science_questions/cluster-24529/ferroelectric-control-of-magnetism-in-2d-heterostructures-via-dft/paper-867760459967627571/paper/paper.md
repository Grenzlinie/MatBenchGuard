# Spin-Torque Generation in Topological-Insulator-Based Heterostructures

Mark H. Fischer,¹ Abolhassan Vaezi,²,³ Aurelien Manchon,⁴ and Eun-Ah Kim³

¹ Department of Condensed Matter Physics, Weizmann Institute of Science, Rehovot 7610001, Israel
² Department of Physics, Stanford University, Stanford, California 94305, USA
³ Department of Physics, Cornell University, Ithaca, New York 14853, USA
⁴ King Abdullah University of Science and Technology (KAUST),
Physical Sciences and Engineering Division, Thuwal 23955-6900, Saudi Arabia

(Dated: November 21, 2021)

Heterostructures utilizing topological insulators exhibit a remarkable spin-torque efficiency. However, the exact origin of the strong torque, in particular whether it stems from the spin-momentum locking of the topological surface states or rather from spin-Hall physics of the topological-insulator bulk remains unclear. Here, we explore a mechanism of spin-torque generation purely based on the topological surface states. We consider topological-insulator-based bilayers involving ferromagnetic metal (TI/FM) and magnetically doped topological insulators (TI/mdTI), respectively. By ascribing the key theoretical differences between the two setups to location and number of active surface states, we describe both setups within the same framework of spin diffusion of the non-equilibrium spin density of the topological surface states. For the TI/FM bilayer, we find large spin-torque efficiencies of roughly equal magnitude for both in-plane and out-of-plane spin torques. For the TI/mdTI bilayer, we elucidate the dominance of the spin-transfer-like torque. However, we cannot explain the orders of magnitude enhancement reported. Nevertheless, our model gives an intuitive picture of spin-torque generation in topological-insulator-based bilayers and provides theoretical constraints on spin-torque generation due to topological surface states.

## I. INTRODUCTION

Harnessing the spin-momentum locking of the surface states of topological insulators holds great promise for spintronics applications. Indeed, recent experiments on TI/FM¹,² and TI/mdTI heterostructures³ observed a large spin-torque efficiency, the figure of merit for their application. The torque measured in these two sets of experiments, however, differs quite significantly. While the TI/FM experiments exhibit spin-transfer- and field-like torques of comparable magnitude, the TI/mdTI has predominantly spin-transfer-like torque, and thus resembles the spin-Hall setup of heavy metal (HM)/FM bilayers.⁴⁻⁶ Its efficiency, however, exceeds the HM/FM bilayers' by several orders of magnitude.

Devices consisting of topological insulators and ferromagnetic metals have so far mainly been the focus of theoretical studies in the context of magnetotransport, where the FM affects the transport properties of the topological surface states.⁷⁻⁹ Most theoretical investigations of torque generation using topological insulators, however, have focused on (ideal) TI/ferromagnetic insulator (FI) hybrid structures.¹⁰⁻¹³ There, a current through the topological surface state mainly results in a non-equilibrium spin density due to the surface states' helical spin structure (inverse spin-galvanic effect). Adding to the Oersted field, this acts as a magnetic field on the ferromagnetic moments.¹⁰,¹¹ This effect can clearly not account for either of the two setups.

In this work, we investigate TI/FM and TI/mdTI bilayers assuming that in both setups the spin torque originates in the spin-momentum locking of the topological surface states. After a short description of our approach based on spin diffusion into the ferromagnetic layer,¹ we discuss first the TI/FM bilayer with an in-plane magnetization, assuming a topological state at the interface, see Fig. 1(a). While it is not a priori clear that a TI next to a FM hosts a topological interface state, such a state is supported by density functional theory calculations.¹⁴ Then, we investigate the TI/mdTI structure. To describe this setup within the same scheme, we assume that both sides of the structure are 'metallic', i.e., have bulk states. Furthermore, we do not expect topological interface states

![](./images/867760459967627571_1.jpg)

FIG. 1. (Color online) The heterostructures we consider in this work: (a) TI / FM bilayer¹,² with a topological surface state at the inferace and (b) TI/ magnetically doped TI bilayer³ with surface states at the two opposite surfaces (indicated in red). The current in both cases runs in $x$ direction and the in-plane magnetization $\vec{M} = M\vec{m}$ is along the in-plane diagonal.

between the two TIs, but topological surface states on each side of the total structure,¹⁵ see Fig. 1(b). Note that while a current in the bulk may lead to additional contributions to the spin torque due to the spin Hall effect,⁴⁻⁶ we focus here entirely on the role of the topological surface states. Finally, we discuss our findings and propose ways to disentangle the various contributions to the spin torque.

## II. METHOD

The states at the surface of a topological insulator can exert a torque on an adjacent ferromagnet, which for in-plane magnetization is purely field-like.¹⁶ This field-like torque can intuitively be understood looking at the surface states described by the Dirac Hamiltonian

$$
\mathcal{H}_{\mathbf{k}}=v_{\mathrm{F}}(\hat{z} \times \vec{\sigma}) \cdot \mathbf{k}-\mu \tag{1}
$$

with $\vec{\sigma}$ the Pauli matrices acting in spin space and $\hat{z}$ is the unit vector in $z$ direction. Further, $\mu \neq 0$ is the chemical potential away from the charge neutrality point. The velocity operator $\vec{v}=\partial_{\mathbf{k}} \mathcal{H}_{\mathbf{k}}$ is directly proportional to the spin operator $\vec{S}=(\hbar / 2) \vec{\sigma}$ and reads

$$
\vec{v}=\frac{2}{\hbar} v_{\mathrm{F}}(\hat{z} \times \vec{S}). \tag{2}
$$

While the TI has a vanishing equilibrium spin expectation, a finite current density $j_{x}=e n\left\langle v_{x}\right\rangle_{\text {neq }}$ [Figs. 1(a) and (b)], where $e$ is the electron's charge and $n$ the electron density, yields a spin density

$$
\left\langle S_{y}\right\rangle_{\text {neq }}=-\frac{\hbar}{2 e v_{\mathrm{F}}} j_{x}. \tag{3}
$$

It is important to note that in a steady-state situation of a translationally invariant system,¹⁷ which is the situation we are interested in, there is no transfer of momentum between the topological surface state and the adjacent ferromagnet. Hence, there is also no net transfer of spin from the surface states to the ferromagnet as is the case in the situation of the spin Hall effect. However, the magnetic moments of the ferromagnetic layer couple to the surface-state spins through $\mathcal{H}_{e x}=-\Delta_{e x} \vec{m} \cdot \vec{S}$ with $\vec{m}$ the magnetization direction in the ferromagnet.¹⁰,¹¹ Thus, the spin polarization on the TI surface leads to a field-like torque of the form $\vec{T}=\Delta_{e x} \vec{m} \times\langle\vec{S}\rangle_{\text {neq }}$, which for an in-plane magnetization is out-of-plane. We show in the following how for an FM layer thicker than the diffusion length, spin diffusion leads to an additional in-plane torque (Slonczewski-like torque), in a way similar to the spin-current injection in HM/FM bilayers.⁴⁻⁶

Given the spin polarization at the TI surface, Eq. (3), as an input, we consider the diffusion of (itinerant) spins into the ferromagnetic metal and the torque they thereby exert. The diffusion (in $z$ direction) leads to a steady-state transverse spin density through¹⁸

$$
0=-\vec{\nabla} \cdot \vec{\mathcal{J}}_{i}-\frac{1}{\tau_{J}}(\vec{S} \times \vec{m})_{i}-\frac{1}{\tau_{\phi}}[\vec{m} \times(\vec{S} \times \vec{m})]_{i}-\frac{S_{i}}{\tau_{\text {sf }}}, \tag{4}
$$

where the spin current (for the $i$ th spin component) is given by

$$
\vec{\mathcal{J}}_{i}=-\mathcal{D} \vec{\nabla} S_{i} \tag{5}
$$

with $\mathcal{D}$ the diffusion coefficient. The second term in Eq. (4) describes the precession of the spins around the moments of the FM with $\tau_{J}$ the spin precession time. The third term captures the relaxation of the spin component perpendicular to $\vec{m}$ with $\tau_{\phi}$ the spin decoherence time, and the last term is the spin diffusion with time scale $\tau_{\text {sf }}$. In the following, we use $\lambda_{\text {sf }}=5 \mathrm{~nm}^{19}$ and values for $\lambda_{\mathrm{J}}$ and $\lambda_{\phi}$ of order $1 \mathrm{~nm}\left(\lambda_{i}^{2}=\mathcal{D} \tau_{i}\right)$.

![](./images/867760459967627571_2.jpg)

FIG. 2. (Color online) Spin accumulation in the ferromagnet ($d=8\mathrm{nm}$) as a function of distance $z$ from the TI/FM boundary, where the solid (dashed) line denotes $S_{\perp}$ ($S_{z}$). For these plots, we used a spin decoherence length of $\lambda_{\phi}=1\mathrm{nm}$ and the spin diffusion length of Permalloy $\lambda_{\text {sf }}=5 \mathrm{~nm}^{19}$. Green (red) curves correspond to a spin-precession length $\lambda_{\mathrm{J}}=1\mathrm{nm}$ ($\lambda_{\mathrm{J}}=0.5\mathrm{nm}$).

## III. TI/FM BILAYER

For the setup of Refs. 1 and 2, Fig. 1(a), we solve equations (4) and (5) requiring no spin current through the outer boundary of the FM, $\mathcal{J}(d)=0$, where $d$ is the thickness of the ferromagnetic layer. For the TI/FM interface, we assume that due to the exchange interaction, the itinerant spins of the FM right at the interface align with the spin density of the TI interface, i.e., $\vec{S}(0)=\gamma\langle\vec{S}\rangle_{\text {neq }}$ with $\gamma$ of order one.²⁰ With these boundary conditions, the spin distribution in $z$ direction is given by

$$
\hat{S}(z)=S_{\perp}(z)+i S_{z}(z)=S_{0} \frac{\cosh [\hat{k}(z-d)]}{\cosh (\hat{k} d)} \tag{6}
$$

with

$$
\hat{k}=\sqrt{\lambda_{\|}^{-2}-i \lambda_{J}^{-2}}, \tag{7}
$$

and $\lambda_{\|}^{-2}=\lambda_{\text {sf }}^{-2}+\lambda_{\phi}^{-2}$. $S_{\perp}(z)$ is the in-plane spin density and $S_{0}=|\vec{S}(0) \times \vec{m}|$ is the initial spin density ($z=0$),

![](./images/867760459967627571_3.jpg)

FIG. 3. (Color online) (a) Integrated torque as a function of the FM thickness $d$. We again set $\lambda_{\text{sf}}=5$nm, and the solid (dashed) lines denote the in-plane (out-of-plane) torque.

both perpendicular to $\vec{m}$. Figure 2 shows the in-plane spin density $S_{\perp}$ perpendicular to the magnetization (solid line) and $S_{z}$ along the $z$ axis (dashed line) for $d=8$nm. Note that this thickness $d\approx8$nm $\gg1/k'$ with $\hat{k}=k'+ik''$. Using Eq. (6), we can thus approximate
$$
\hat{S}(z)\approx S_{0}e^{-\hat{k}z}=S_{0}\cos k''ze^{-k'z}-iS_{0}\sin k''ze^{-k'z},\ (8)
$$
i.e., both components oscillate and decrease exponen- tially, see Figure 2.

Figure 3 shows the integrated torque as a function of the FM layer thickness $d$. Assuming the spin angular momentum to be a good quantum number, the torque is given by the spatial change of the spin current compen- sated by the spin relaxation,
$$
\hat{T}=\int_{0}^{d}dz\left[-\partial_{z}\hat{\mathcal{J}}(z)-\frac{1}{\tau_{\text{sf}}}\hat{S}(z)\right],\qquad(9)
$$
where we again use the short forms $\hat{T}=T_{\perp}+iT_{z}$ and $\hat{\mathcal{J}}=\mathcal{J}_{\perp}+i\mathcal{J}_{z}$. Given the spin distribution in $z$ direction of Eq. (6), we find
$$
\hat{T}=S_{0}\left(\frac{1}{\lambda_{\phi}^{2}}-\frac{i}{\lambda_{J}^{2}}\right)\frac{\mathcal{D}}{\hat{k}}\frac{\sinh(\hat{k}d)}{\cosh(\hat{k}d)}\qquad(10)
$$
$$
\rightarrow S_{0}\frac{\mathcal{D}}{\hat{k}}\left(\frac{1}{\lambda_{\phi}^{2}}-\frac{i}{\lambda_{J}^{2}}\right).\qquad(11)
$$

For the limit in the last line, we used $d\rightarrow\infty$. As expected from the fast decay of the spin density in Figure 2, the torque is 'deposited' within only a few nanometers. The total torque exerted on the ferromagnet as a function of the thickness $d$ thus stays constant with layer thickness.

For the geometry described in Fig. 1(a), the spin po- larization perpendicular to the magnetization of the FM is $\sqrt{2}/2$ of the total polarization $\langle S_{y}\rangle_{\text{neq}}$, and we find for the thick-FM limit $(d\gg1/k')$
$$
\hat{T}=-\frac{\hbar}{2}\frac{\mathcal{D}}{\hat{k}}\left(\frac{1}{\lambda_{\phi}^{2}}-\frac{i}{\lambda_{J}^{2}}\right)\frac{\sqrt{2}}{2}\frac{j_{x}}{ev_{\text{F}}}.\qquad(12)
$$

![](./images/867760459967627571_4.jpg)

FIG. 4. The two torque components as a function of the TI thickness $d_{1}$ for $\vec{S}_{1}=-\vec{S}_{2}$ for $\lambda_{\text{J}}=\lambda_{\phi}=1$nm (in the mdTI) and $\lambda_{\text{sf}}=5$nm (on both sides) and $d_{2}=6$nm. The solid (dashed) line denotes the in-plane (out-of-plane) torque. (b) shows the two components for fixed $d_{1}=3$nm [gray bar in (a)] as a function of the ratio $|\vec{S}_{1}|/|\vec{S}_{2}|$ for $|\vec{S}_{1}|+|\vec{S}_{2}|$ fixed.

In analogy to the spin-Hall angle $\theta_{\text{SH}}=(2eJ_{\text{S}})/(\hbar J_{C})$, which describes the spin-Hall current per charge current, we define the spin-torque efficiency
$$
\hat{\theta}=\frac{\hat{T}}{j_{x}}\frac{2e}{\hbar}=-\frac{\sqrt{2}}{2}\frac{\mathcal{D}}{v_{\text{F}}\hat{k}}\left(\frac{1}{\lambda_{\phi}^{2}}-\frac{i}{\lambda_{J}^{2}}\right).\qquad(13)
$$

For $\lambda_{\text{J}}\sim\lambda_{\phi}\ll\lambda_{\text{sf}}$, the out-of-plane and in-plane spin- torque efficiencies are of comparable magnitude. Using $\lambda_{\text{J}}=\lambda_{\phi}=1$nm, $\lambda_{\text{sf}}=5$nm, $v_{\text{F}}=5\times10^{5}$ms$^{-1}$, and a typical diffusion coefficient $\mathcal{D}=1-10$cm$^{2}$s$^{-1}$, we find for the in-plane and out-of-plane-torque efficiency $|\theta_{\perp}|=0.15-1.5$ and $|\theta_{z}|=0.065-0.65$.

### IV. TI/mdTI BILAYER

We apply the same scheme now to investigate the setup of Ref. 3, Fig. 1(b), namely a bilayer of a TI (thickness $d_{1}$) and a Cr-doped TI (thickness $d_{2}$). At sufficiently low temperature, the doped TI exhibits ferromagnetism due to the magnetic moments introduced by Cr dop- ing. $^{21}$ Within our approach, the key difference between the TI/mdTI bilayer setup and the TI/FM setup is then the spatial location of the topological surface states. As- suming no topological distinction between TI and mdTI, we do not anticipate a topological state at the inter- face. Instead, we expect two surface states, one on each naked surface [see Figure 1(b)]. These two surfaces carry the current $\vec{j}_{1}$ and $\vec{j}_{2}$ with associated spin-polarization

$\vec{S}_{1}$ and $\vec{S}_{2}$. Now the boundary conditions for the spin-diffusion equation (4) as stated for the TI/FM bilayer has to change. First, the spin density on the two sides are $\vec{S}(0)=\vec{S}_{1}$ and $\vec{S}(d_{1}+d_{2})=\vec{S}_{2}$. In addition, we require that the spin density and the spin current match at the interface, i.e. at $z=d_{1}$.

Figure 4(a) shows the integrated torque of a 6nm thick mdTI as a function of $d_{1}$ for $j_{1}=j_{2}$ and thus $\vec{S}_{1}=-\vec{S}_{2}$, where we use again $\lambda_{J}=\lambda_{\phi}=1$nm (in the mdTI) and $\lambda_{sf}=5$nm. For $d_{1}=0$, i.e., no TI next to the mdTI, the contributions from the two surface states exactly cancel and upon increasing $d_{1}$ the torque grows monotonically with the field-like torque always smaller than the transfer-like torque. The two currents will in general not be identical, and Fig. 4(b) shows the two torques for $d_{1}=3$nm and $d_{2}=6$nm, the dimensions of the experimental setup, for different ratios of $|\vec{S}_{1}|/|\vec{S}_{2}|$. As long as $|\vec{S}_{1}|\approx|\vec{S}_{2}|$, the spin-transfer-like torque dominates, in accordance with the experimental results of Ref. 3.

## V. DISCUSSION AND CONCLUSIONS

In this work, we analyzed the spin-torque generation in TI-based heterostructures arising from the spin-momentum locking of the topological surface states. Considering itinerant spins that diffuse in the ferromagnetic side (either FM or mdTI), we find both an out-of-plane (field-like) and an in-plane (Slonczewski-like) torque. For realistic parameters, a spin-torque efficiency of the order of $|\theta|\approx0.1-1$ should be expected. This agrees with the reported values in Refs. 1 and 2 and is comparable to or larger than the largest value of spin-torque efficiency observed in HM/FM structures to date. $^{4-6,22}$ However, we do not find as large a spin-torque efficiency as reported in Ref. 3 within our approach.

Within our model, both components of the torque stem from the combination of the inverse spin-galvanic effect of the TI surface and spin diffusion into the FM. The two torque components not only differ in their direction, but also in their behavior under $\vec{M}\mapsto-\vec{M}$: While the field-like torque changes sign, the Slonczewski-like torque does not. This can help distinguish in-plane torque arising from out-of-plane spin polarization $^{23}$ from Slonczewski-like torque. For 'metallic' TIs, an additional spin-transfer-like torque arises from the bulk spin Hall effect. As transport is dominated by the surface states for thin TIs, $^{24}$ we still expect the two components of the torque to be of comparable magnitude. In the case of the TI/mdTI heterostructure, the fact that the transfer-like torque is more than an order of magnitude larger than the field-like torque, however, hints at a dominant contribution from the bulk.

In closing we comment on limits of the applicability of our approach to extremely thin FM layers. As the total spin torque stays constant independent of FM layer thickness for $d\gtrsim2$nm, thin FM layers are preferable for device applications. However, our calculation treating the FM layer in $z$ direction to be in the diffusive regime relies on a FM layer that is thicker than its mean free path. For a device with an FM layer thinner than the diffusion length, the device should be modeled using a semiclassical Boltzmann approach or through quantum tunneling of spins. $^{9,25-27}$ Our simple model can already guide ferromagnetic resonance measurements, which do not require such thin FM layers, and help distinguish the various contributions to the spin-torque in TI based heterostructures.

## ACKNOWLEDGMENTS

The authors are grateful to Alex Mellnik and Dan Ralph for helpful discussions. MHF and E-AK acknowledge support from NSF grant no. DMR-0955822 and from NSF grant no. DMR-1120296 to the Cornell Center for Materials Research. MHF further acknowledges the Swiss Society of Friends of the Weizmann Institute of Science. AM was supported by the King Abdullah University of Science and Technology (KAUST).

---

$^{1}$ A. R. Mellnik, J. S. Lee, A. Richardella, J. L. Grab, P. J. Mintun, M. H. Fischer, A. Vaezi, A. Manchon, E. A. Kim, N. Samarth, and D. C. Ralph, Nature $\mathbf{511}$, 449 (2014).
$^{2}$ Y. Wang, P. Deorani, K. Banerjee, N. Koirala, M. Brahlek, S. Oh, and H. Yang, Phys. Rev. Lett. $\mathbf{114}$, 257202 (2015).
$^{3}$ Y. Fan, P. Upadhyaya, X. Kou, M. Lang, S. Takei, Z. Wang, J. Tang, L. He, L.-T. Chang, M. Montazeri, G. Yu, W. Jiang, T. Nie, R. N. Schwartz, Y. Tserkovnyak, and K. L. Wang, Nat Mater $\mathbf{13}$, 699 (2014).
$^{4}$ L. Liu, T. Moriyama, D. C. Ralph, and R. A. Buhrman, Phys. Rev. Lett. $\mathbf{106}$, 036601 (2011).
$^{5}$ L. Liu, C.-F. Pai, Y. Li, H. W. Tseng, D. C. Ralph, and R. A. Buhrman, Science $\mathbf{336}$, 555 (2012).
$^{6}$ C.-F. Pai, L. Liu, Y. Li, H. W. Tseng, D. C. Ralph, and R. A. Buhrman, Applied Physics Letters $\mathbf{101}$, 122404 (2012).
$^{7}$ A. A. Burkov and D. G. Hawthorn, Phys. Rev. Lett. $\mathbf{105}$, 066802 (2010).
$^{8}$ P. Schwab, R. Raimondi, and C. Gorini, EPL (Europhysics Letters) $\mathbf{93}$, 67004 (2011).
$^{9}$ T. Yokoyama and Y. Tserkovnyak, Phys. Rev. B $\mathbf{89}$, 035408 (2014).
$^{10}$ I. Garate and M. Franz, Phys. Rev. Lett. $\mathbf{104}$, 146802 (2010).
$^{11}$ T. Yokoyama, J. Zang, and N. Nagaosa, Phys. Rev. B $\mathbf{81}$, 241410 (2010).
$^{12}$ Y. Tserkovnyak and D. Loss, Phys. Rev. Lett. $\mathbf{108}$, 187201 (2012).
$^{13}$ Y. Tserkovnyak, D. A. Pesin, and D. Loss, Phys. Rev. B $\mathbf{91}$, 041121 (2015).

14 Hsu et al., unpublished.

15 Y.-T. Hsu, M. H. Fischer, T. L. Hughes, K. Park, and E.-A. Kim, Phys. Rev. B 89, 205438 (2014).

16 P. Birame Ndiaye, C. A. Akosa, M. H. Fischer, A. Vaezi, E. Kim, and A. Manchon, arXiv:1509.06929.

17 See F. Mahfouzi, B. K. Nikolić, and N. Kioussis, arXiv:1506.01303 for effects of scattering on FM bound- aries

18 A. Manchon, R. Matsumoto, H. Jaffres, and J. Grollier, Phys. Rev. B 86, 060404 (2012).

19 J. Bass and W. P. P. Jr, Journal of Physics: Condensed Matter 19, 183201 (2007).

20 We will set in the following $\gamma=1$. Note that this choice of the boundary condition for the diffusion equation is cru- cial. For a spin-Hall situation, the torque is due to a spin current injected into the FM, and thus the correct bound- ary condition is a non-zero spin-current at the interface, i.e. $\mathcal{J}(0) \neq 0$. For realistic parameters, i.e., $\lambda_{\mathrm{sf}} \gg \lambda_{\phi}, \lambda_{\mathrm{J}}$, this results in a torque almost completely in-plane.

21 P. P. J. Haazen, J.-B. Laloë, T. J. Nummy, H. J. M. Swagten, P. Jarillo-Herrero, D. Heiman, and J. S. Mood- era, Applied Physics Letters 100, 082404 (2012).

22 I. M. Miron, K. Garello, G. Gaudin, P.-J. Zermatten, M. V. Costache, S. Auffret, S. Bandiera, B. Rodmacq, A. Schuhl, and P. Gambardella, Nature 476, 189 (2011).

23 C. M. Wang and X. L. Lei, Phys. Rev. B 89, 045415 (2014).

24 N. Bansal, Y. S. Kim, M. Brahlek, E. Edrey, and S. Oh, Phys. Rev. Lett. 109, 116804 (2012).

25 J. Xiao, A. Zangwill, and M. D. Stiles, The European Physical Journal B 59, 415 (2007).

26 P. M. Haney, H.-W. Lee, K.-J. Lee, A. Manchon, and M. D. Stiles, Phys. Rev. B 87, 174411 (2013).

27 W. Chen, M. Sigrist, J. Sinova, and D. Manske, Phys. Rev. Lett. 115, 217203 (2015).