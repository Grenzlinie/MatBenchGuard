Journal Pre-proofs

Research articles

Permanent Magnet Design Assisted by Antiferromagnet-Ferromagnet Interface
Coupling: A Monte Carlo Study

Xudong Hang, Jian-Ping Wang

![](./images/812695967642943488_1.jpg)

PII:
S0304-8853(19)33719-9
DOI:
https://doi.org/10.1016/j.jmmm.2019.166360
Reference:
MAGMA 166360

To appear in:
Journal of Magnetism and Magnetic Materials

Received Date:
23 October 2019
Accepted Date:
26 December 2019

Please cite this article as: X. Hang, J-P. Wang, Permanent Magnet Design Assisted by Antiferromagnet-Ferromagnet
Interface Coupling: A Monte Carlo Study, Journal of Magnetism and Magnetic Materials (2020), doi: https://
doi.org/10.1016/j.jmmm.2019.166360

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover
page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will
undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing
this version to give early visibility of the article. Please note that, during the production process, errors may be
discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier B.V.

# Permanent Magnet Design Assisted by Antiferromagnet–Ferromagnet Interface Coupling: A Monte Carlo Study

Xudong Hang$^{\text{a}}$, Jian-Ping Wang$^{\text{b,a,*}}$

$^{\text{a}}$Department of Chemical Engineering and Materials Science, University of Minnesota, Minneapolis, MN 55455
$^{\text{b}}$Department of Electrical and Computer Engineering, University of Minnesota, Minneapolis, MN 55455

---

## Abstract

In the pursuit of rare-earth-free permanent magnets, materials with large saturation magnetization ($M_{\text{s}}$) stand out. However, large $M_{\text{s}}$ results in low anisotropy field, thus additional source of coercivity is needed to make useful magnets for a broad range of applications. In this paper, we investigate the use of interface coupling to an antiferromagnet (AFM) as a means to increase coercivity for permanent magnet design. Results on the effects of Néel temperature, AFM anisotropy, interface coupling strength, AFM volume ratio, as well as temperature dependence are obtained using Monte Carlo (MC) simulations. And before that, we clarify some practices in MC simulations of magnetic hysteresis. The origin of coercivity enhancement is investigated by examining the magnetization reversal process, which is found to agree with well-established theory of exchange bias. Finally, discussions and design suggestions are made on the AFM materials, the geometry, and experimental realization.

---

## 1. Introduction

Coercivity ($H_{\text{c}}$) enhancement is quite a universal observation in exchange bias (EB) systems, where a ferromagnet (FM) is exchange coupled to an antiferromagnet (AFM) at the interface [1, 2, 3, 4, 5]. Understanding of the origin of the coercivity has been achieved through extensive experimental [2, 6, 7, 8, 9] and theoretical [10, 11, 12, 13] studies. Application to the design of permanent magnet (PM) would be implied in this coercivity increase, if not for the fact that rare earth (RE) based PMs had satisfied all applications, and that introduction of AFM costs magnetization, which in many cases needs enhancement. However, the environmental costs of RE mining and processing, as well as RE supply risks have intrigued renewed interest in the search of RE-free PMs [14]. $\text{Fe}_{16}\text{N}_{2}$ is a promising candidate for RE-free PM due to its large saturation magnetization ($M_{\text{s}}$) [15, 16, 17]. But the anisotropy field ($H_{\text{K}}$) is low even with its decent magnetocrystalline anisotropy. Bulk magnets of $\text{Fe}_{16}\text{N}_{2}$ generally have a coercivity of 1200–2000 Oe [18, 19]. $\text{Fe}_{16}\text{N}_{2}$ nanoparticles were reported with a coercivity of 1000–3000 Oe [20, 21, 22]. A general design for $\text{Fe}_{16}\text{N}_{2}$ magnet projected different strategies with coercivity up to 3000–8000 Oe based on optimum microstructure and trade-off of saturation magnetization [23]. Additional coercivity is needed to make practical $\text{Fe}_{16}\text{N}_{2}$ magnets. So, this is an ideal case where coupling to AFM helps make better PM by trading "excessive" $M_{\text{s}}$ for more $H_{\text{c}}$, but it remains to be evaluated whether $H_{\text{c}}$ gain could potentially compensate for the loss of $M_{\text{s}}$ in terms of maximum energy product $(BH)_{\text{max}}$.

So far, this possibility of AFM–FM composite magnet has not been extensively explored. Only a few early experimental studies exist, and they are briefly summarized here. Sort *et al.* observed coercivity enhancement at room temperature in mechanically alloyed Co–NiO and Co–FeS powders after heat treatment [24]. Sort *et al.* achieved enhanced coercivity and $M_{\text{r}}/M_{\text{s}}$ (remnence/saturation) ratio at room temperature by ball milling hard magnetic material $\text{SmCo}_{5}$ with AFM NiO [25]. AFM–FM interface exchange coupling was confirmed to play an important role in this enhancement. The microstructure features

---

*Corresponding author*
Email address: jpwang@umn.edu (Jian-Ping Wang)

Preprint submitted to Elsevier
December 23, 2019

$SmCo_5$ particles embedded in an antiferromagnetic matrix, favoring large amount of interface. It was later confirmed that by adjusting the AFM-FM mixing ratio, increased $(BH)_{\text{max}}$ could also be achieved [26]. In a recent study Lottini *et al.* synthesized $\text{Co}_x\text{Fe}_{1-x}\text{O}$ (AFM)-$\text{Co}_x\text{Fe}_{3-x}\text{O}_4$ (ferrimagnetic) core-shell nanoparticles and observed greatly enhanced coercivity at 10 K due to interface exchange interaction [27]. Application to PM is ultimately limited by the ability of the AFM-FM composite to produce field, so caution is needed for balancing $M_s$ and $H_c$. A theoretical evaluation of designing PM with the help of AFM, including guidance of AFM material choice, is still lacking.

In this paper, we report results of Monte Carlo (MC) simulations of AFM-FM bilayers for PM applications. Though MC methods have been widely used to model hysteresis loops for anisotropic Heisenberg model [28] and exchange bias systems [29, 30, 31], some difficulties are not well addressed in the literature, and many practices such as $H_c$ determination and error estimation remain elusive. In Section 2 the method is examined. We then present results of coercivity dependence on AFM Néel temperature, anisotropy, volume fraction, interface coupling strength, and temperature in Section 3. The origin of coercivity enhancement is also studied through the magnetization reversal process.

## 2. Model and Methods
### 2.1. The AFM-FM bilayer system

The bilayer system consists of anisotropic Heisenberg AFM and FM, both having body-centered cubic (bcc) lattice, coupled at the interface. The interface coordination is also bcc type. Periodic boundary conditions are applied in plane ($xy$), while there are two free surfaces at both ends, one in FM, the other in AFM. The Hamiltonian is as follows:

$$
\begin{aligned}
H= & -J_{\mathrm{FM}} \sum_{<i, j>\in \mathrm{FM}} \hat{\mathbf{S}}_{i} \cdot \hat{\mathbf{S}}_{j}-J_{\mathrm{AF}} \sum_{<i, j>\in \mathrm{AF}} \hat{\mathbf{S}}_{i} \cdot \hat{\mathbf{S}}_{j} \\
& -K_{\mathrm{FM}} \sum_{i \in \mathrm{FM}} S_{i, x}^{2}-K_{\mathrm{AF}} \sum_{i \in \mathrm{AF}} S_{i, x}^{2} \\
& -\mathbf{H} \cdot \sum_{i \in \mathrm{FM}, j \in \mathrm{AF}}\left(\mu_{\mathrm{FM}} \hat{\mathbf{S}}_{i}+\mu_{\mathrm{AF}} \hat{\mathbf{S}}_{j}\right) \\
& -J_{\mathrm{INT}} \sum_{\substack{<i \in \mathrm{FM}, \mathrm{int} \\
j \in \mathrm{AF}, \mathrm{int}>}} \hat{\mathbf{S}}_{i} \cdot \hat{\mathbf{S}}_{j},
\end{aligned}
$$

where the first two terms are exchange energy within FM and AFM, the next two terms are FM and AFM anisotropy, followed by the Zeeman energy, and the last term is interface coupling. $<\cdots>$ denotes summation over nearest neighbors. The spins are represented by unit vectors, so the exchange constants $J_{\mathrm{FM}}$ and $J_{\mathrm{AF}}$ (in eV) absorb the magnitude. The exchange constants of FM and AFM differ in sign. The anisotropy constant $K$ has unit eV (per spin) and can be converted to generally used units like $\mathrm{erg/cm^3}$ with knowledge of the crystal structure. The easy axis of both FM and AFM is set to the in-plane $x$-axis. $\mathbf{H}$ is the external field, and $\mu_{\mathrm{FM}}$ ($\mu_{\mathrm{AF}}$) is magnetic moment of one FM (AFM) spin in Bohr magneton. We restricted the field to be in the $x$ direction. For better comparison with experiment, the field is presented in unit Oe. $J_{\mathrm{INT}}$ is the strength of interface coupling, in unit of eV. We chose $J_{\mathrm{INT}}$ to be positive so that the interface coupling is FM type.

The system size is fixed to $20 \times 20$ spins in plane, and 20 layers of FM. The AFM thickness varies. We use $N_x \times N_y \times (N_{z,\mathrm{AF}}+N_{z,\mathrm{FM}})$ to denote a system size, where $N_x$ and $N_y$ are in-plane dimensions along $x$- and $y$-axis, $N_{z,\mathrm{AF}}$ and $N_{z,\mathrm{FM}}$ are number of layers in AFM and FM subsystems respectively. In all simulations, the properties of $\text{Fe}_{16}\text{N}_2$ are used as inputs, namely, $J_{\mathrm{FM}}=0.035$ eV, which corresponds to Curie temperature $T_{\mathrm{C}}=810$ K [16], $K_{\mathrm{FM}}=8 \times 10^{-5}$ eV and $\mu_{\mathrm{FM}}=2.5\ \mu_{\mathrm{B}}$. They combined correspond to $H_{\mathrm{K}}=11$ kOe, which lies in the range of experimental values [32, 33]. $\mu_{\mathrm{AF}}$ is set to $1.0\ \mu_{\mathrm{B}}$.

In a MC run, the system is initialized to a known ground state with all FM spins along field direction, and AFM consisting of alternating ferromagnetic layers in which the direction of the interface layer is determined by the sign of $J_{\mathrm{INT}}$. This is also the convergence state from a random initial spin configuration. The interface is uncompensated below magnetic order temperatures due to the choice of lattices. We use single spin flip (SSF) method and the trial step is a random movement of the spin vector within a cone of given size ("cone" algorithm) [28, 34], accepted according the Metropolis algorithm [35]. The error is estimated using the nonoverlapping batch means method [36], namely, the measurements are divided into $m$ nonoverlapping batches, and

$$
\frac{1}{m} \sum_{k=1}^{m}\left(\mu_{\mathrm{b}, k}-\mu\right)^{2},
$$

where $\mu_{\mathrm{b}, k}$, $k = 1,\cdots,m$ are batch means, and $\mu$ is the mean of all measurements, estimates the standard deviation. In a field scan, 20,000 measurements are averaged at each field step and the field is then increased (decreased) by 400 Oe. While one long MC run suffices to estimate mean values of quantities provided convergence, we average 20 field scans with different random number sequences to estimate $H_{\mathrm{c}}$ and exchange bias field $(H_{\mathrm{EB}})$ due to difficulties in determining switching field (Section 2.2). To evaluate the effect of AFM on coercivity, the bilayer system is compared to a homogeneous system where the AFM is replaced by FM, keeping the total system size as well as other parameters unchanged.

### 2.2. Monte Carlo coercivity
To simulate the hysteresis loop of an anisotropic Heisenberg model with MC methods, one difficulty is that in the metastable branches of a hysteresis loop, one is not evaluating the thermal expectations in the classical MC sense. Rather, the initial spin configuration and update mechanism are manipulated so that the system is forced to stay in one metastable state because the transition to the other (more) stable state does not happen within practical computer time for a large system [37]. Anisotropy is the energy barrier that prevents the transition from happening. If some other update mechanism is used, such as reflection of all spins with respect to the plane perpendicular to the easy axis, then the two (meta)stable states are averaged according to their relative energy and no hysteresis will be observed. On the other hand, hysteresis is a physical reality because of the long lifetime of metastability. Moreover, the "cone" method of proposing an update does agree with the spin precession picture in the high damping limit [34]. Some other local update mechanisms, such as a global rotation around the magnetization direction within a cone of small radius [28] also gives good grounding to the resulting hysteresis as it mimics the coherent rotation process. The coercive fields, as are important in any discussion of reversal mechanism of the Heisenberg model or exchange bias phenomena, need more explanation in MC simulations, because of its dependence on non-physical parameters like the field scan speed (FSS), the change in field divided by the number of Monte Carlo steps (MCSs) at each field step [28]. This artificial dependence is exactly due to the fact that the relevant quantities such as magnetization are measured before convergence and thus depend on the initial spin configuration. The lifetime of a metastable state varies with the applied demagnetizing field. Switching happens when more MCSs are taken at a field step than the metastability lifetime at that field. So the switching field depends on the FSS, and low FSS results in high coercivity, as demonstrated by Nehme et al. [28]. To make things worse, the metastability lifetime has a distribution of considerable width, so that the switching field also depends on the random number sequence. Examples of the distribution of metastability lifetime (defined when the magnetization along the field direction is zero) are shown in Fig. 1. At a small field the distribution is quite wide, while in a larger field it peaks sharply at a lower time.

![](./images/812695967642943488_2.jpg)

Figure 1: Lifetime (in MCS) of the metastable state on demagnetizing. The system starts from positive saturation and is let to relax in a negative field. System size: $20 \times 20 \times (10+20)$, $J_{\mathrm{AF}}=-0.03$ eV ($T_{\mathrm{N}}=725$ K), $J_{\mathrm{INT}}=0.01$ eV, $K_{\mathrm{AF}}=1 \times 10^{-4}$ eV, $T=300$ K.

As MC time doesn't have a physical meaning, it's difficult to choose a suitable FSS that gives experimentally correct coercivity. This choice is usually limited by computer time. To reconcile the dependence of coercivity on the random number sequence, 20 field scans using different seeds for random number generation are averaged, and an error estimation of coercivity is also obtained as the standard deviation, shown as error bar. A potentially better method of defining coercivity is to set a criterion on the metastability lifetime distribution, for example, a limit on the expectation value. However, this method is more complicated, and the criterion is still arbitrary. Since in this paper we are

![](./images/812695967642943488_3.jpg)

Figure 2: AFM-FM in equilibrium under different demag-
netizing fields. (a) The hysteresis loop. The blue and green
symbols represent the system starting from positive and neg-
ative saturation respectively. The two curves overlap and
there is no hysteresis. (b) Layer magnetization at −70 kOe;
the magnitude of the magnetization of each layer and its
projection to the field direction are both shown and la-
beled. Layers 0-19 are AFM, 20-39 FM. (c) The equilib-
rium spin configuration at −70 kOe; each arrow represents
one layer and has length close to unit. The top 4 AFM lay-
ers and every other FM layer are shown. The parameters
are: $J_{\text{AF}}=-0.03$ eV, $J_{\text{INT}}=0.01$ eV, $K_{\text{AF}}=0.01$ eV,
$T=30$ K.

concerned mainly with coercivity, we can avoid this
difficulty by comparing the coercivity of an AFM-
FM system and a homogeneous FM system of the
same size. By keeping all other parameters same,
the change in coercivity is caused solely by AFM.
The exact percentage change of $H_{c}$ cannot be ob-
tained in this way, as the coercivity is associated
with metastability lifetime, which is not fully quan-
tified.

### 2.3. Special case: hysteresis loop at equilibrium

Different from a single Heisenberg FM, the cou-
pled AFM-FM allows simulation of hysteresis loop
where each data point is taken at equilibrium. This
is the case of large $K_{\text{AF}}$ and large $J_{\text{INT}}$. The AFM
does not react to external field and remains aligned
to its easy axis, so that it provides a pinning bound-
ary condition for the FM. A stable partial domain
wall (DW) forms in the FM due to this boundary
condition. One such example is shown in Fig. 2 for
a system of size $20\times20\times(20+20)$. As can be seen
in Fig. 2(a), there is no hysteresis. Fig. 2(b) shows
the magnetization along field direction, and a par-
tial DW in FM can be observed. An interesting
observation is that the magnitude of magnetization
of each layer (normalized to the number of spins in a
layer) is close to one, i.e., all spins within one layer
are (nearly) aligned, so each layer can be treated
as a single spin vector, and the spin configuration
is shown in Fig. 2(c), from which one can see how
the partial DW is wound in the FM. This situation
is not of particular interest in the following discus-
sion, but it can be useful in the more general study
of exchange bias.

![](./images/812695967642943488_4.jpg)

Figure 3: Definition of angles in the two-spin model.

## 3. Results and discussion

### 3.1. Two-spin model

Before presenting results of the MC simulations,
the authors would like to show a simpler two-spin
model, where FM magnetization is represented by
a macro-spin, and so is one sublattice of the AFM.
For simplicity, we assume colinear AFM and FM
easy axis. The external field is applied at an angle $\alpha$
to the shared easy axis of the system. The definition
of the angles used to describe the system is shown
in Fig. 3. We set $\alpha$ to $10^{\circ}$ for the following results.

Total energy of the two-spin system is
$$
E=-2h\cos(\alpha-\theta)+\sin^{2}\theta+\hat{K}_{\text{AF}}\sin^{2}\phi-\hat{J}_{\text{INT}}\cos(\theta-\phi), \tag{3}
$$
where $E$ is scaled by $K_{\text{FM}}t_{\text{FM}}$, $t_{\text{FM}}$ ($t_{\text{AF}}$) is the
thickness of the FM (AFM) layer, $h=H/H_{\text{K}}$, $H_{\text{K}}$

![](./images/812695967642943488_5.jpg)

Figure 4: Example hysteresis loops from the calculations of two-spin model. $\hat{K}_{\mathrm{AF}}=1.0$.

being the anisotropy field, $\hat{K}_{\mathrm{AF}}=\frac{K_{\mathrm{AF}}}{K_{\mathrm{FM}}} \frac{t_{\mathrm{AF}}}{t_{\mathrm{FM}}}$ is the AFM anisotropy scaled to FM anisotropy, $\hat{J}_{\mathrm{INT}}=$ $\frac{J_{\mathrm{INT}}}{K_{\mathrm{FM}} t_{\mathrm{FM}} a^{2}}$ is normalized interface coupling strength, $a$ being (roughly) the lattice constant. Note that all quantities in eq. (3) are properly normalized and have unit 1.

The system starts from the equilibrium state in a large positive external field, in which $\mathbf{M}_{\mathrm{FM}}$ is nearly aligned with $\mathbf{H}$. The field is then decremented, at each step a new equilibrium configuration is found by a gradient descent method in the $(\theta, \phi)$ space, starting from the equilibrium configuration of the last step. When the field becomes negative, the system goes into a metastable state. Switching only happens when the local energy minimum that the system was in disappears. After equilibrating the system in the negative maximum field, the field is swept in the opposite direction to complete a hysteresis loop.

Example hysteresis loops of the two-spin system with normalized AFM anisotropy $\hat{K}_{\mathrm{AF}}=1$ are shown in Fig. 4. It is seen that at a weak interface coupling $\hat{J}_{\mathrm{INT}}=0.5$, the system exhibits loop shift, while at a stronger interface coupling $\hat{J}_{\mathrm{INT}}=2$, the system exhibits loop widening.

We calculated coercivity of the two-spin system under different values of $\hat{K}_{\mathrm{AF}}$ and $\hat{J}_{\mathrm{INT}}$ and the results are shown as a colormap in Fig. 5. Note that the $\hat{J}_{\mathrm{INT}}$ range corresponds to an actual interface coupling strength of 1 meV to 30 meV, given $K_{\mathrm{FM}}=1.0 \times 10^{7} \mathrm{erg} / \mathrm{cm}^{3}, t_{\mathrm{FM}}=20 \mathrm{~nm}$, and $a=2$ $\AA$. There is a clear phase boundary described by $\hat{J}_{\mathrm{INT}}=\hat{K}_{\mathrm{AF}}$ in Fig. 5 that separates the cases of loop shift (exchange bias) and loop widening (enhanced coercivity). Two line profiles are also shown in Fig. 5, both having a discontinuous transition from one phase to the other.

![](./images/812695967642943488_6.jpg)

Figure 5: Colormap of the coercivity (in unit of $H_{\mathrm{K}}$) dependence on $\hat{K}_{\mathrm{AF}}$ and $\hat{J}_{\mathrm{INT}}$ of the two-spin model. The coercivity of the FM is denoted as "no AF". Two line profiles, labeled on the colormap, are shown alongside it. The green lines in the line profiles indicate FM coercivity.

While this two-spin model nicely illustrates the key idea of the current study-the search of the balance between $M_{\mathrm{s}}$ and $H_{\mathrm{c}}$, between $K_{\mathrm{AF}}$ and $J_{\mathrm{INT}}$ for permanent magnet applications, it has several limitations. First, the effective exchange strength of both FM and AFM is infinite, which is not physical. Also due to this, the anisotropy and interface coupling strength lack a natural scale and thus not easily related to real materials. Second, magnetization switching only occurs when a local energy minimum disappears, corresponding to zero temperature. It cannot be easily generalized to finite temperature situations. Third, this model explicitly assumes coherent rotation as the mechanism for magnetization switching, which is known to overestimate coercivity. The MC simulation addresses these issues and is presented below.

### 3.2. Magnetization reversal process

We first studied the magnetization reversal process in $20 \times 20 \times(20+20)$ systems. The increase in coercivity that will be shown later can be clearly understood with the knowledge of reversal mechanism. The case of enhanced coercivity (loop shift) is realized in small (large) $K_{\mathrm{AF}}$ and large (small) $J_{\mathrm{INT}}$. Fig. 6(a) shows the case of enhanced $H_{\mathrm{c}}$, where it is seen that AFM switches, following FM.

In Fig. 6(b) AFM is stable. Due to the small system size, the reversal process in both cases is coherent rotation, as characterized by the (almost) conserva- tion of the magnitude of FM magnetization in this process (Figs. 6(a) and (b)). We can thus represent the FM with a single vector of its magnetization (normalized to number of spins), with length close to unit. The same is true for the interface layer of AFM. In this notation, the path of the reversal is shown in Figs. 6(c) and (d) for enhanced coercivity and loop shift respectively. In Fig. 6(c), the magne- tization of the AFM interface layer closely follows the reversal path of FM, while in Fig. 6(d) it is seen that the magnetization of the interface layer of AFM stays in a narrow region around its initial vector position and never deviates too much in the course of FM switching. Note that any path from $(1,0,0)$ to $(-1,0,0)$ is equally likely, the particu lar one shown being a result of the random number sequence chosen. Fig. 6 shows results at 30 K. The essence is same at 300 K but a higher temperature comes with more noise. A single FM system is also studied and switches by coherent rotation at both30 K and 300 K, as a result of small system size.

### 3.3. Effect of AFM anisotropy, Néel temperature, and interface coupling strength

We now present results on the effects of $K_{AF}$ , $T_{N}$ , and $J_{INT}$ on the coercivity of the AFM-FM systems at 300 K. The system size is chosen to be $20 ×20 \times(10+20)$ , i.e., AFM takes up a third of total volume. The dependence of $H_{c}$ on $K_{AF}$ at various values of $J_{AF}$ and $J_{INT}$ is shown in Fig. 7. One observation is that the coercivity increases nearly linearly with $K_{AF}$ , provided that the condition for enhanced coercivity is satisfied. If not, as in the case of $J_{AF}=-0.03 eV, K_{AF}=0.5 meV$ , and $J_{INT}=1 meV,^{1}$ then a collapse of $H_{c}$ is observed. A loop shift takes over from loop widening. In Figs. 7(a) and (b), the thick solid horizontal line indicates $H_{c}$ value for a homogeneous FM system of size 20 × 20 × 30. The dashed lines indicate its uncertainty. The fact that coercivity is above this reference in most of the parameter space we ex- plored shows that it is not merely a size effect and that AFM plays a role in coercivity enhancement.

![](./images/812695967642943488_7.jpg)

Figure 6: Magnetization reversal process. (a) and (b) show the cases of enhanced $H_{c}$ and loop shift respectively. (c) and(d) show the path of magnetization vectors corresponding to(a) and (b) respectively. In (c) the AFM switches together with FM, while in (d) the AFM is stable. In (a) and (c) theparameters are: $J_{AF}=-0.03 eV, J_{INT}=0.03 eV, K_{AF}=$  $1 ×10^{-4} eV, H=-30 kOe$ . In (b) and (d): $J_{AF}=-0.03 eV$ , JINT = 0.001 eV, KAF = 5 x 10-4 eV, H = -28 kOe. T = 30 K for both cases.

From Fig. 7(a) it can be seen that once the interface coupling is stronger than some threshold, which can be as low as 5 meV, it stops mattering too much in determining $H_{c}$ . For example, increasing $J_{INT}$ from5 meV to 20 meV only results in a small increase in coercivity. This is because as a good approxi- mation, $J_{INT}$ only determines whether or not AFM will contribute to coercivity, while if it happens, the amount of extra coercivity contributed by AFM is determined by its anisotropy. When $J_{INT}$ is weak(compared to $K_{AF}$ ), AFM will not switch with FM, in which case we expect a loop shift (exchange bias). If $J_{INT}$ is strong, FM swithing will result in AFM switching, in which case a loop widening (enhanced Hc) is expected. Experimentally, the interface cou- pling strength is difficult to control and likely to have a distribution, the fact that we only need to make it above a threshold without needing to fine- tune it to a precise value is beneficial to experimen- tal design. Fig. 7(b) shows the $H_{c}-K_{AF}$ curves at different $J_{AF}(T_{N})$ , with fixed $J_{INT}=10 meV$ . Itis seen that $T_{N}$ plays an important role. High $T_{N}$ 

\footnotetext{ $^{1}$ The numerical value of $K_{AF}$ depends on the anisotropy and crystal structure of AFM. To give some concrete idea, suppose the AFM has the crystal structure of MgO, i.e., rock salt structure with lattice constant $a=4.2 \AA$ , and a uniaxial anisotropy constant of $1.0 ×10^{7} erg / cm^{3}$ , then the value of $K_{AF}$ is $1.2 ×10^{-4} eV$ . Fig. 7 explored the reasonable range of $K_{AF}$ .}

![](./images/812695967642943488_8.jpg)

Figure 7: Dependence of coercivity on AFM anisotropy at various $J_{\text{AF}}$ and $J_{\text{INT}}$ values, for a $20×20×(10+20)$ system. In (a), $J_{\text{AF}}$ is fixed to $-30$ meV, while in (b) $J_{\text{INT}}$ is fixed to 10 meV. In both (a) and (b), the thick horizontal line indicates the coercivity of a reference FM system of size $20×$ $20×30$, with uncertainty indicated by dash lines.

helps increase $H_{\text{c}}$, but generally it should be below $T_{\text{C}}$ of the FM. We thus restricted $T_{\text{N}}$ to be lower than $T_{\text{C}}$. The conversion between $J_{\text{AF}}$ and $T_{\text{N}}$ is listed in Table 1. For $T_{\text{N}}$ below 300 K, there is no longer long-range order in AFM, and the random motion of AFM spins destabilizes FM through the interface so that the coercivity of AFM–FM system under this condition is smaller than a homogeneous FM system of the same size.

Limited by computer time, we used a small system size that does not allow a full DW, the reversal of AFM–FM is through coherent rotation, as illustrated in Section 3.2. The increase in $H_{\text{c}}$ can be understood as follows: AFM doesn't respond to the external field, so it provides some boundary condition at the interface that "locks" the FM spins, making it harder for the FM to switch.

Table 1: Conversion between $J_{\text{AF}}$ and $T_{\text{N}}$ of AFM. The AF size is $20×20×10$.

<table>
  <thead>
    <tr>
      <th>$J_{\text{AF}}$ (meV)</th>
      <th>$T_{\text{N}}$ (K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$-30$</td>
      <td>$725$</td>
    </tr>
    <tr>
      <td>$-20$</td>
      <td>$460$</td>
    </tr>
    <tr>
      <td>$-15$</td>
      <td>$355$</td>
    </tr>
    <tr>
      <td>$-10$</td>
      <td>$235$</td>
    </tr>
  </tbody>
</table>

![](./images/812695967642943488_9.jpg)

Figure 8: Coercivity dependence on AFM size. In-plane dimension is $20×20$, and FM size is fixed to 20 layers. For each data point, a corresponding reference system, that of a homogeneous FM with the same size as the AFM—FM bilayer is also shown. It is seen that the reference system shows little coercivity variance with size, indicating negligible finite size effect.

### 3.4. Effect of AFM volume fraction

The effect of AFM size is summarized in Fig. 8. The following parameters are used: $J_{\text{AF}} = -0.03$ eV, $K_{\text{AF}} = 1×10^{-4}$ eV, $J_{\text{INT}} = 0.01$ eV. The in-plane size is fixed to $20×20$, and FM fixed to 20 layers, while the number of AF layers varies from 1 to 24. For each size, the coercivity of a corresponding reference FM system (whose size is equal to the corresponding AFM-FM complsite) is also shown. The coercivity of the reference systems shows little dependence on size. As the AFM size increases, a larger portion of the AFM–FM system doesn't react to external field, making switching harder and a higher $H_{\text{c}}$ is expected. As a rough estimation, when the AFM size equals FM, the coercivity doubles. This is not quantitatively accurate though. The AFM volume fraction is an important parameter that determines the balance between $H_{\text{c}}$ and $M_{\text{s}}$, however, this simple MC approach is not capable of fully quantifying it.

### 3.5. Temperature dependence

In an AFM–FM composite magnet, because $T_{\text{N}}$ of AFM is lower than $T_{\text{C}}$ of FM, performance degradation might be expected at high temperature. We

![](./images/812695967642943488_10.jpg)

Figure 9: Coercivity dependence on temperature. The AFM-FM size is $20\times20\times(10+20)$, and FM reference size is $20\times20\times30$. The parameters are: $J_{\text{AF}}=-0.03$ eV, $J_{\text{INT}}=0.01$ eV, $K_{\text{AF}}=2\times10^{-4}$ eV.

performed MC estimation of coercivity at a temperature range of 275 to 475 K. The result is shown in Fig. 9, from which one can see that AFM-FM doesn't underperform FM. The percentage $H_c$ decrease at 475 K as compared to 300 K for FM is 36%, while for AFM-FM it is 37%. This indicates that proper choice of AFM material ($T_{\text{N}}=725$ K in Fig. 9) can ensure good high temperature performance of the AFM-FM composite magnet.

### 3.6. Discussion: magnetization reversal by DW motion
Due to the small system size, magnetization reversal is through coherent rotation, as illustrated in Fig. 6. We briefly discuss in this section the case in which the reversal is dominated by DW motion. To allow for a full domain wall in this case of moderate FM anisotropy, the system needs to have a size of hundreds of atomic layers, which is computationally expensive. However, we can generalize the results of coherent rotation to DW motion by examining the partial DW as presented in Fig. 2. For illustrative purposes, Fig. 2 shows the case of unrealistically large AFM anisotropy, in which case every point on the hysteresis loop is at true equilibrium and thus there is no hysteresis. Imagine for a realistic AFM anisotropy, a DW nucleates at the top surface of FM and propagates towards the AFM-FM interface. If the interface coupling strength is strong enough to overcome $K_{\text{AF}}$, then AFM will be switched by the FM. The mechanism is exactly same as the one we discussed extensively above. If this happens, AFM will contribute extra coercivity. However, due to lack of any magnetic frustration in this simple lattice model, FM cannot effectively limit DW motion and would have a low intrinsic coercivity. Also, at a much larger system size, the $J_{\text{INT}}$ threshold for loop widening to occur cannot be easily generalized without actually performing the calculations.

If the DW is perpendicular to the interface, it is still possible to switch the AFM by forming and propagating a DW in AFM, alongside the DW in FM. But the situation is slightly different in that in addition to having to overcome the energy barrier from AFM anisotropy, $J_{\text{INT}}$ in attenuated by the AFM DW energy. So, a stronger interface coupling is necessary to achieve enhanced coercivity. Without actual calculations on systems with larger lateral size, we cannot quantify the requirements of $J_{\text{INT}}$ though.

### 3.7. Discussion: geometry and materials
This work only studies the bilayer structure, which is a one-dimensional case. Some previous works have studied the FM-AFM core-shell particles (three-dimensional, 3D) [31, 38]. A two-dimensional system, the cylindrical core-shell particle is less studied. Higher dimension comes with larger interface to volume ratio, but AFM shell with the same thickness occupies more volume, which is disadvantageous for the purpose of PM applications. The inverted AFM-core-FM-shell geometry similar to previous experimental study [27] might have its advantage. A possible experimental realization of the AFM-FM bilayer structure would be nitriding a thin Fe foil (500 nm) on one side and oxidizing it on the other. Diffusion and ion implantation are good ways of achieving the desired AFM-FM structure. The AFM materials should have an intermediate $T_{\text{N}}$ to ensure both high temperature performance and direction setting by field cooling. AFM anisotropy should be considered together with interface coupling strength. Within the range that sees enhanced coercivity instead of loop shift, the larger $K_{\text{AF}}$ the better. From the optimization point of view, it pays off to start from AFM materials with the largest anisotropy. Oxides and nitrides of Cr, Mn, Fe, Co, Ni, ... are natural candidates. FeO and CoO have large anisotropy [39] but low Néel temperature ($T_{\text{N}}$ of FeO and CoO are 200 K and 290 K respectively [3]). MnN [40] and NiO have good $T_{\text{N}}$ but low anisotropy. However,

experiment showed that NiO can increase coerciv-
ity of Co and $SmCo_5$ considerably [24, 25]. IrMn
has high anisotropy [41], but is heavy and expen-
sive. It remains a challenge to find suitable AFM
materials for PM applications. A ferrimagnet might
be considered to replace AFM since it gives some
magnetization. But it remains to be seen whether
the coercivity enhancement is as good because fer-
rimagnet more or less reacts to external field.

## 4. Conclusions
In summary, we performed MC simulations on
AFM-FM EB bilayers under external demagnetiz-
ing field. The switching (coercive) field is related
to the lifetime of the metastable state, whose distri-
bution was sampled. A larger coercive field in the
MC sense is understood as having longer metasta-
bility lifetime. No simple relation between the co-
ercivity and metastability lifetime can be obtained
though. This method was applied to the design
of PMs using AFM–FM coupling. Results on the
effects of AFM $T_N$, anisotropy, volume fraction, in-
terface coupling strength, and temperature depen-
dence were presented. We showed that coupling to
AFM is promising to make useful PMs out of high-
magnetization FM materials by increasing coerciv-
ity. The choice of AFM materials, geometry, and
possible experiments were briefly discussed. We be-
lieve more experimental efforts should be devoted
to exploring this possibility of developing AFM-FM
composite PMs.

## Acknowledgments
The authors are grateful to the helpful discus-
sions with Kexin Feng, Jinming Liu, Dr. Bin Ma,
and Dr. Delin Zhang. This work is partially
supported by Niron Magnetics, Inc. The authors
acknowledge the **Minnesota Supercomputing Insti-
tute (MSI)** at the University of Minnesota for pro-
viding resources that contributed to the research
results reported within this paper.

## References
[1] W. H. Meiklejohn, C. P. Bean, New magnetic
anisotropy, Phys. Rev. 105 (1957) 904–913 (Feb 1957).
doi:10.1103/PhysRev.105.904.
URL https://link.aps.org/doi/10.1103/PhysRev.
105.904

[2] R. Jungblut, R. Coehoorn, M. T. Johnson, J. aan de
Stegge, A. Reinders, Orientational dependence of
the exchange biasing in molecular-beam-epitaxy-grown
$Ni_{80}Fe_{20}/Fe_{50}Mn_{50}$ bilayers (invited), J. Appl. Phys.
75 (10) (1994) 6659–6664 (1994). doi:10.1063/1.
356888.
URL https://doi.org/10.1063/1.356888

[3] J. Nogués, I. K. Schuller, Exchange bias, J. Magn.
Magn. Mater. 192 (2) (1999) 203 – 232 (1999).
doi:10.1016/S0304-8853(98)00266-2.
URL http://www.sciencedirect.com/science/
article/pii/S0304885398002662

[4] R. L. Stamps, Mechanisms for exchange bias, J. Phys.
D 33 (23) (2000) R247 (2000).
URL https://iopscience.iop.org/article/10.1088/
0022-3727/33/23/201

[5] J. Nogués, J. Sort, V. Langlais, V. Skumryev,
S. Suriñach, J. S. Muñoz, M. D. Baró, Exchange bias
in nanostructures, Phys. Rep. 422 (3) (2005) 65 – 117
(2005). doi:10.1016/j.physrep.2005.08.004.
URL http://www.sciencedirect.com/science/
article/pii/S0370157305003303

[6] C.-H. Lai, H. Matsuyama, R. L. White, T. C. Anthony,
Anisotropic exchange for NiFe films grown on epitaxial
NiO, IEEE Trans. Magn. 31 (6) (1995) 2609–2611 (Nov
1995). doi:10.1109/20.490068.

[7] C.-L. Lin, J. M. Sivertsen, J. H. Judy, Magnetic prop-
erties of NiFe films exchange-coupled with NiO, IEEE
Trans. Magn. 31 (6) (1995) 4091–4093 (Nov 1995).
doi:10.1109/20.489871.

[8] C. Lai, H. Matsuyama, R. L. White, T. C. Anthony,
G. G. Bush, Exploration of magnetization reversal and
coercivity of epitaxial NiO {111}/NiFe films, J. Appl.
Phys. 79 (8) (1996) 6389–6391 (1996). doi:10.1063/1.
362007.
URL https://aip.scitation.org/doi/abs/10.1063/
1.362007

[9] C. Leighton, J. Nogués, B. J. Jönsson-Åkerman, I. K.
Schuller, Coercivity enhancement in exchange biased
systems driven by interfacial magnetic frustration,
Phys. Rev. Lett. 84 (2000) 3466–3469 (Apr 2000).
doi:10.1103/PhysRevLett.84.3466.
URL https://link.aps.org/doi/10.1103/
PhysRevLett.84.3466

[10] E. Fulcomer, S. H. Charap, Thermal fluctuation af-
tereffect model for some systems with ferromagnetic-
antiferromagnetic coupling, J. Appl. Phys. 43 (10)
(1972) 4190–4199 (1972). doi:10.1063/1.1660894.
URL https://doi.org/10.1063/1.1660894

[11] D. Mauri, H. C. Siegmann, P. S. Bagus, E. Kay, Simple
model for thin ferromagnetic films exchange coupled to
an antiferromagnetic substrate, J. Appl. Phys. 62 (7)
(1987) 3047–3049 (1987). doi:10.1063/1.339367.
URL https://doi.org/10.1063/1.339367

[12] T. C. Schulthess, W. H. Butler, Consequences
of spin-flop coupling in exchange biased films,
Phys. Rev. Lett. 81 (1998) 4516–4519 (Nov 1998).
doi:10.1103/PhysRevLett.81.4516.
URL https://link.aps.org/doi/10.1103/
PhysRevLett.81.4516

[13] M. D. Stiles, R. D. McMichael, Coercivity in exchange-
bias bilayers, Phys. Rev. B 63 (2001) 064405 (Jan 2001).
doi:10.1103/PhysRevB.63.064405.
URL https://link.aps.org/doi/10.1103/PhysRevB.
63.064405

[14] J. Cui, M. Kramer, L. Zhou, F. Liu, A. Gabay, G. Hadjipanayis, B. Balasubramanian, D. Sellmyer, Current progress and future challenges in rare-earth-free permanent magnets, Acta Mater. 158 (2018) 118 - 137 (2018). doi:10.1016/j.actamat.2018.07.049.
URL http://www.sciencedirect.com/science/article/pii/S1359645418305858

[15] T. K. Kim, M. Takahashi, New magnetic material having ultrahigh magnetic moment, Appl. Phys. Lett. 20 (12) (1972) 492-494 (1972). doi:10.1063/1.1654030.
URL https://doi.org/10.1063/1.1654030

[16] Y. Sugita, K. Mitsuoka, M. Komuro, H. Hoshiya, Y. Ko- zono, M. Hanazono, Giant magnetic moment and other magnetic properties of epitaxially grown $Fe_{16}N_{2}$ single crystal films (invited), J. Appl. Phys. 70 (10) (1991) 5977-5982 (1991). doi:10.1063/1.350067.
URL https://doi.org/10.1063/1.350067

[17] J. P. Wang, N. Ji, X. Liu, Y. Xu, C. Sanchez-Hanke, Y. Wu, F. M. F. de Groot, L. F. Allard, E. Lara- Curzio, Fabrication of $Fe_{16}N_{2}$ films by sputtering process and experimental investigation of origin of giant saturation magnetization in $Fe_{16}N_{2}$, IEEE Trans. Magn. 48 (5) (2012) 1710-1717 (May 2012). doi:10.1109/TMAG.2011.2017156.

[18] Y. Jiang, M. A. Mehedi, E. Fu, Y. Wang, L. F. Al- lard, J.-P. Wang, Synthesis of $Fe_{16}N_{2}$ compound free standing foils with 20 MGOe magnetic energy product by nitrogen ion-implantation, Sci. Rep. 6 (2016) 25436 EP -, article (May 2016).
URL http://dx.doi.org/10.1038/srep25436

[19] Y. Jiang, V. Dabade, L. F. Allard, E. Lara-Curzio,R. James, J.-P. Wang, Synthesis of $\alpha''$-Fe₁₆N₂ compound anisotropic magnet by the strained-wire method, Phys. Rev. Applied 6 (2016) 024013 (Aug 2016). doi:10.1103/PhysRevApplied.6.024013.
URL https://link.aps.org/doi/10.1103/PhysRevApplied.6.024013

[20] T. Ogi, A. B. Dani Nandiyanto, Y. Kisakibaru, T. Iwaki, K. Nakamura, K. Okuyama, Facile synthesis of single-phase spherical $\alpha''$-Fe₁₆N₂/Al₂O₃ core-shell nanoparticles via a gas-phase method, J. Appl. Phys. 113 (16) (2013) 164301 (2013). doi:10.1063/1.4798959.
URL https://doi.org/10.1063/1.4798959

[21] C. W. Kartikowati, A. Suhendi, R. Zulhijah, T. Ogi, T. Iwaki, K. Okuyama, Effect of magnetic field strength on the alignment of $\alpha''$-Fe₁₆N₂ nanoparticle films, Nanoscale 8 (2016) 2648-2655 (2016). doi:10.1039/C5NR07859H.
URL http://dx.doi.org/10.1039/C5NR07859H

[22] I. Dirba, C. Schwöbel, L. Diop, M. Duerrschnabel, L. Molina-Luna, K. Hofmann, P. Komissinskiy, H.-J. Kleebe, O. Gutfleisch, Synthesis, morphology, thermal stability and magnetic properties of $\alpha''$-Fe₁₆N₂ nanoparticles obtained by hydrogen reduction of $\gamma$-Fe₂O₃ and subsequent nitrogenation, Acta Mater. 123 (2017) 214 - 222 (2017). doi:10.1016/j.actamat.2016.10.061.
URL http://www.sciencedirect.com/science/article/pii/S1359645416308291

[23] J.-P. Wang, $Fe_{16}N_{2}$-from a 40-year mystery of magnetic materials to one of promises for rare-earth-free magnets (invited talk), in: Intermag, 2018 (2018).

[24] J. Sort, J. Nogués, X. Amils, S. Suriñach, J. S. Muñoz, M. D. Baró, Room-temperature coercivity enhancement in mechanically alloyed antiferromagnetic-ferromagnetic powders, Appl. Phys. Lett. 75 (20) (1999) 3177-3179 (1999). doi:10.1063/1.125269.
URL https://doi.org/10.1063/1.125269

[25] J. Sort, J. Nogués, S. Suriñach, J. S. Muñoz, M. D. Baró, E. Chappel, F. Dupont, G. Chouteau, Coercivity and squareness enhancement in ball-milled hard magnetic-antiferromagnetic composites, Appl. Phys. Lett. 79 (8) (2001) 1142-1144 (2001). doi:10.1063/1.1392308.
URL https://doi.org/10.1063/1.1392308

[26] J. Sort, S. Suriñach, J. S. Muñoz, M. D. Baró, J. Nogués, G. Chouteau, V. Skumryev, G. C. Hadjipanayis, Improving the energy product of hard magnetic materials, Phys. Rev. B 65 (2002) 174420 (May 2002). doi:10.1103/PhysRevB.65.174420.
URL https://link.aps.org/doi/10.1103/PhysRevB.65.174420

[27] E. Lottini, A. López-Ortega, G. Bertoni, S. Turner, M. Meledina, G. Van Tendeloo, C. de Julián Fernández, C. Sangregorio, Strongly exchange coupled core-shell nanoparticles with high magnetic anisotropy: A strategy toward rare-earth-free permanent magnets, Chem. Mater. 28 (12) (2016) 4214-4222 (2016). doi:10.1021/acs.chemmater.6b00623.
URL https://doi.org/10.1021/acs.chemmater.6b00623

[28] Z. Nehme, Y. Labaye, R. Sayed Hassan, N. Yaacoub, J. M. Greneche, Modeling of hysteresis loops by Monte Carlo simulation, AIP Adv. 5 (12) (2015) 127124 (2015). doi:10.1063/1.4938549.
URL https://doi.org/10.1063/1.4938549

[29] U. Nowak, K. D. Usadel, J. Keller, P. Miltényi, B. Beschoten, G. Güntherodt, Domain state model for exchange bias. I. theory, Phys. Rev. B 66 (2002) 014430 (Jul 2002). doi:10.1103/PhysRevB.66.014430.
URL https://link.aps.org/doi/10.1103/PhysRevB.66.014430

[30] D. Lederman, R. Ramírez, M. Kiwi, Monte Carlo simulations of exchange bias of ferromagnetic thin films on FeF₂(110), Phys. Rev. B 70 (2004) 184422 (Nov 2004). doi:10.1103/PhysRevB.70.184422.
URL https://link.aps.org/doi/10.1103/PhysRevB.70.184422

[31] E. Eftaxias, K. N. Trohidou, Numerical study of the exchange bias effects in magnetic nanoparticles with core/shell morphology, Phys. Rev. B 71 (2005) 134406 (Apr 2005). doi:10.1103/PhysRevB.71.134406.
URL https://link.aps.org/doi/10.1103/PhysRevB.71.134406

[32] X. Hang, X. Zhang, B. Ma, V. Lauter, J.-P. Wang, Epitaxial $Fe_{16}N_{2}$ thin film on nonmagnetic seed layer, Appl. Phys. Lett. 112 (19) (2018) 192402 (2018). doi:10.1063/1.5028396.
URL https://doi.org/10.1063/1.5028396

[33] X. Li, M. Yang, M. Jamali, F. Shi, S. Kang, Y. Jiang, X. Zhang, H. Li, S. Okatov, S. Faleev, A. Kalitsov, G. Yu, P. M. Voyles, O. N. Mryasov, J.-P. Wang, Heavy-metal-free, low-damping, and non-interface perpendicular fe16n2 thin film and magnetoresistance device, physica status solidi (RRL) - Rapid Research Letters 13 (7) (2019) 1900089 (2019). arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1002/pssr.201900089,

doi:10.1002/pssr.201900089.
URL https://onlinelibrary.wiley.com/doi/abs/10.1002/pssr.201900089

[34] U. Nowak, R. W. Chantrell, E. C. Kennedy, Monte carlo simulation with time step quantification in terms of langevin dynamics, Phys. Rev. Lett. 84 (2000) 163-166 (Jan 2000). doi:10.1103/PhysRevLett.84.163.
URL https://link.aps.org/doi/10.1103/PhysRevLett.84.163

[35] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, E. Teller, Equation of state calculations by fast computing machines, J. Chem. Phys. 21 (6) (1953) 1087-1092 (1953). doi:10.1063/1.1699114.
URL https://doi.org/10.1063/1.1699114

[36] C. J. Geyer, Introduction to Markov Chain Monte Carlo, 2011 (2011).

[37] K. Binder, D. W. Heermann, Monte Carlo Simu- lation in Statistical Physics An Introduction, 5th Edition, Springer, 2010 (2010). doi:10.1007/978-3-642-03163-2.

[38] K. Trohidou, M. Vasilakaki, L. D. Bianco, D. Fio- rani, A. Testa, Exchange bias in a magnetic or- dered/disordered nanoparticle system: A Monte Carlosimulation study, J. Magn. Magn. Mater. 316 (2) (2007) e82 - e85, proceedings of the Joint European Magnetic Symposia (2007). doi:10.1016/j.jmmm.2007.02.035.
URL http://www.sciencedirect.com/science/article/pii/S0304885307001321

[39] A. Schrön, C. Rödl, F. Bechstedt, Crystalline and mag- netic anisotropy of the $3d$-transition metal monoxides MnO, FeO, CoO, and NiO, Phys. Rev. B 86 (2012)115134 (Sep 2012). doi:10.1103/PhysRevB.86.115134.
URL https://link.aps.org/doi/10.1103/PhysRevB.86.115134

[40] M. Meinert, B. Büker, D. Graulich, M. Dunz, Large exchange bias in polycrystalline MnN/CoFe bilayers at room temperature, Phys. Rev. B 92 (2015) 144408 (Oct2015). doi:10.1103/PhysRevB.92.144408.
URL https://link.aps.org/doi/10.1103/PhysRevB.92.144408

[41] G. Vallejo-Fernandez, L. E. Fernandez-Outon, K. O'Grady, Measurement of the anisotropy con- stant of antiferromagnets in metallic polycrystallineexchange biased systems, Appl. Phys. Lett. 91 (21)(2007) 212503 (2007). doi:10.1063/1.2817230.
URL https://doi.org/10.1063/1.2817230