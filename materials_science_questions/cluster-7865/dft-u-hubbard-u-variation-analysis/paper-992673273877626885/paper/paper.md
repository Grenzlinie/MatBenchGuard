# Quantum Modelling of Magnetism in Strongly Correlated Materials: Evaluating Constrained DFT and the Hubbard Model for Y114

Christian Tantardini^(a,b,c,\*), Darina Fazylbekova^c, Sergey V. Levchenko^d, Ivan S. Novikov^(d,e,f)

^a Institute of Physics Belgrade, University of Belgrade, Pregrevica 118, 11080 Belgrade, Serbia.,
^b Department of Materials Science and NanoEngineering, Rice University, Houston, Texas 77005, United States of America,
^c Institute of Solid State Chemistry and Mechanochemistry SB RAS, 630128, Novosibirsk, Russian Federation,
^d Skolkovo Institute of Science and Technology, Skolkovo Innovation Center, Bolshoy boulevard 30, Moscow, 121205, Russian Federation,
^e Moscow Institute of Physics and Technology, 9 Institutskiy per., Dolgoprudny, Moscow Region, 141701, Russian Federation,
^f Emanuel Institute of Biochemical Physics RAS, 4 Kosygin Street, Moscow, 119334, Russian Federation,

## Abstract

Transition-metal compounds represent a fascinating playground for exploring the intricate relationship between structural distortions, electronic properties, and magnetic behaviour, holding significant promise for technological advancements. Among these compounds, YBaCo₄O₇ (Y114) is attractive due to its manifestation of a ferrimagnetic component at low temperature intertwined with distortion effect due to the charge disproportionation on Co ions, exerting profound impact on its magnetic properties. In this perspective paper, we study the structural and magnetic intricacies of the Y114 crystal using a novel first-principles methodology. Traditionally, the investigation of such materials has relied heavily on computational modelling using density-functional theory (DFT) with the on-site Coulomb interaction correction $U$ (DFT+$U$) based on the Hubbard model (sometimes including Hund's exchange coupling parameter $J$, DFT+$U$+$J$) to unravel their complexities. Herein, we analysed the spurious effects of magnetic-moment delocalisation and spillover to non-magnetic ions in the lattice on electronic structure and magnetic properties of Y114. To overcome this problem we have applied constrained DFT (cDFT) based on the potential self-consistency approach, and comprehensively explore the Y114 crystal's characteristics in its ferrimagnetic order. We find that cDFT yields magnetic moments of Co ions much closer to the experimental values than Hubbard model with the parameters $U$ and $J$ fitted to reproduce experimental lattice constants. cDFT allows for an accurate prediction of magnetic properties using oxidation states of magnetic ions as well-defined parameters. Through this perspective, we not only enhance our understanding of the magnetic interactions in Y114 crystal, but also pave the way for future investigations into magnetic materials.

**Keywords:** strongly correlated material, constrained density functional theory, Hubbard model, magnetism

---

## 1. Introduction

Co-containing oxides often possess interesting magnetic properties. Among them, YBaCo₄O₇ (abbreviated as Y114) has recently attracted attention [1, 2, 3, 4, 5, 6, 7] due to its complex magnetic behaviour. For example, this structure demonstrates a spin–glass transition at around 66 K from a high-temperature paramagnetic state [1, 3, 4, 5, 6]. In such materials, charge disproportionation can occur, which can strongly influence their magnetic properties. Based on the formal oxidation state count, in Y114 three Co ions per primitive unit cell must adopt +2 oxidation state, and one Co ion adopts a +3 oxidation state. Such materials are known to exhibit dynamic distortion due to electronic fluctuations between the Co ions [1, 3, 4, 5, 6]. For this reason, a direct experimental observation of the expected differences in oxygen tetrahedral environments for each unique cobalt site to assign the correct oxidation state is currently not feasible [1, 3, 4, 5, 6]. The inability to refine the structure experimentally due to dynamic distortion can be effectively addressed through a computational approach, as previously demonstrated by Tantardini *et al.* [8] using Hubbard on-site correction $U$. However, describing magnetism with Hubbard-model-based corrections may not be sufficient due to the lack of experimental data needed to determine the parameters of the model, the Hubbard $U$ and Hund's coupling $J$, which describe the long-range interactions affecting local magnetic moments.

Here, we investigate the limitations of Hubbard model combined with spin-polarized DFT, incorporating both $U$ and $J$ parameters, using the simplest DFT functional known as the local spin density approximation (LSDA+$U$+$J$) in describing complex magnetic materials, and explain how these materials can be theoretically treated using constrained DFT (cDFT) with potential self-consistency, based on the same LSDA DFT functional. [9]. This approach differs from previously developed cDFT methods [10, 11, 12], because it imposes charge or magnetic moment hard constraints by finding such a potential that the corresponding self-consistent wavefunctions and electronic density satisfy the constraints exactly, rather than by using a penalty function directly for the deviation of the constrained

---

\*Correspond to christiantantardini@ymail.com

![](./images/992673273877626885_1.jpg)

Figure 1: Crystal structure of Y114 with $Co^{2+}$ and $Co^{3+}$ in their ferrimagnetic configuration.

quantity from the target. Specifically, a Lagrangian potential-based self-consistency constraint [9] will be applied to model cobalt ions in different oxidation states, $Co^{2+}$ and $Co^{3+}$, in Y114. Additionally, the same type of constraint is applied to the magnetic moments of other atoms in the lattice to prevent the spreading of magnetic moments to non-magnetic atoms, such as oxygen.

In summary, this study adopts an interdisciplinary approach, integrating experimental data obtained by inverse magnetic susceptibility measurements in X-ray powder diffraction at 2 K [6] and advanced computational techniques — specifically leveraging cDFT with a constrained atomic charge and magnetic moments — to unravel the intricate structural, electronic, and magnetic properties of magnetic oxides, emphasising the impact of the dynamic distortions due to the chemical disproportionation on magnetic order.

## 2. Theory

We aim to provide a comparison between Hubbard model and cDFT for describing strongly correlated materials [13]. In Kohn-Sham (KS) DFT the electronic structure of a material is obtained by solving a system of single-particle equations known as KS equations. The Hamiltonian in these equations includes the sum of kinetic energy and the external potential for a single electron. To these terms, the Hartree term, representing the Coulomb repulsion between all electrons (including the spurious self-interaction), and the exchange-correlation term, approximated in various forms in DFT (e.g., LSDA as considered here), are added. The KS states $\psi_{k,\nu}$ describe the single electron within a specific band $\nu$ at a specific $k$-point in the reciprocal space. These states are delocalized over the crystal.

In most cases, such a model can fully describe the properties of materials. However, in the case of strongly correlated materials such as transition-metal compounds, the self-interaction error and other exchange-correlation errors in approximate energy-functionals can lead to qualitatively incorrect description of localised valence $d$-orbitals, making it challenging to model oxidation states and magnetic interactions of transition-metal ions in crystals. The same problem occurs in lanthanides and actinides with the localised $f$-orbitals. Over the years, the on-site Coulomb interaction correction $U$ of Hubbard model [14, 15, 16] applied to DFT (DFT+$U$) practically addressed this issue by considering specific electronic interactions between atomic orbitals. The total energy in DFT+$U$ is formulated as follows:

$$
E^{\mathrm{DFT}+U}[\rho, n]=E^{\mathrm{DFT}}[\rho]+E^{U}[n]-E^{d c}[n]. \tag{1}
$$

Here, $\rho$ is the electron density of the system, $n$ is the density matrix for localised atomic orbitals on a specific atom $A$, and $E^{d c}[n]$ is a double-counting term removing the DFT energy contribution of the localized orbitals, which are now described by the Hubbard-like terms. In this framework, two alternative approaches to avoid double counting ($E^{d c}$) have been proposed: the fully localised limit (FLL) [17] and the around mean-field (AMF) [18]. The density matrix is generated by projecting KS states onto atomic orbitals with specific angular momentum $\ell$ and associated momentum projection $m$ of the atom $A$:

$$
n_{m m^{\prime}}^{A \sigma}=\sum_{k, \nu} f_{k \nu}^{\sigma}\left\langle\varphi_{m}^{A \sigma} \mid \psi_{k, \nu}\right\rangle\left\langle\psi_{k, \nu} \mid \varphi_{m^{\prime}}^{A \sigma}\right\rangle, \tag{2}
$$

where $f$ is the Fermi-Dirac distribution, $\sigma$ is the spin on the atom $A$, and $\varphi$ are the atomic orbitals described as product of radial functions and spherical harmonics centered on the atoms. If only diagonal terms of the local density matrix $n_{m m^{\prime}}^{A \sigma}$ are considered, the term $E^{U}[n]$ will lose its invariance under rotation. Therefore, the terms that come from the off-diagonal local density matrix should be also considered.

The energy term in the Hubbard model ($E^{U}[n]$) is given by:

$$
\begin{aligned}
E^{U}[n] &=\frac{1}{2} \sum_{A=1}^{M} \sum_{\{m\}, \sigma}\left\{\left\langle\varphi_{m}^{A}, \varphi_{m^{\prime \prime}}^{A}\left|V_{e e}\right| \varphi_{m^{\prime}}^{A}, \varphi_{m^{\prime \prime \prime}}^{A}\right\rangle n_{m m^{\prime}}^{\sigma} n_{m^{\prime \prime} m^{\prime \prime \prime}}^{-\sigma}\right. \\
&+\left(\left\langle\varphi_{m}^{A}, \varphi_{m^{\prime \prime}}^{A}\left|V_{e e}\right| \varphi_{m^{\prime}}^{A}, \varphi_{m^{\prime \prime \prime}}^{A}\right\rangle\right. \\
&\left.\left.-\left(\left\langle\varphi_{m}^{A}, \varphi_{m^{\prime \prime}}^{A}\left|V_{e e}\right| \varphi_{m^{\prime \prime \prime}}^{A}, \varphi_{m^{\prime}}^{A}\right\rangle\right)\right) n_{m m^{\prime}}^{\sigma} n_{m^{\prime \prime} m^{\prime \prime \prime}}^{\sigma}\right\}. \tag{3}
\end{aligned}
$$

Here, $V_{e e}$ is the screened electron-electron Coulomb repulsion. In the FLL formulation of $E^{d c}$ seen in the Eq. 1, the parameters $U$ and $J$, referred to as screened Coulomb and Hund's coupling parameters, enter as follows:

$$
E^{d c}[n]=\frac{1}{2} U N(N-1)-\frac{1}{2} J\left[N^{\uparrow}\left(N^{\uparrow}-1\right)+N^{\downarrow}\left(N^{\downarrow}-1\right)\right] \quad(4)
$$

where $N^\sigma = \sum_m n_{mm}^{A\sigma}$, and $N = \sum_{\sigma} N^\sigma$. In this formulation, which slightly differs from AMF, a constraint is applied to specific atomic orbitals of an atom. In practice, an energy constraint is applied to the Coulomb interaction between specific atomic orbitals of a chosen atom, preventing them from spreading over the entire structure. The DFT+$U$+$J$ method shares similarities with the Hartree-Fock (HF) method. It essentially replaces certain electronic interactions with a Hamiltonian reminiscent of HF Hamiltonian, similar to hybrid functionals, where part of the functional involves a Fock exchange operator acting on KS states. However, DFT+$U$+$J$ differs by utilising screened effective interactions and focusing only on a specific subset of states.

Within DFT+$U$+$J$ an assumption of orbital independence is made due to the localised nature of the orbitals the correction is applied to. Despite its formal resemblance to HF, DFT+$U$+$J$ operates on KS wave functions, lacking a direct physical interpretation beyond reproducing the charge density. In essence, DFT+$U$+$J$ bridges concepts from HF and hybrid functionals, incorporating screened interactions and orbital decoupling while selectively applying corrections to specific states in the system.

Moreover, $U$ and $J$ can be construed as parameters of the Hubbard model representing the weight of an additional penalty function integrated into the total energy. This augmentation introduces a biased solution to DFT. The values of these parameters are intricately linked to the atomic environment and concentration of specific atoms relative to the overall quantity of atoms within the given structure. Their determination necessitates the application of one of four distinct methodologies: (i) fitting, wherein various properties such as lattice parameters or magnetic moments are juxtaposed for different $U$ and $J$ values at varying concentrations of strongly correlated atom types, (ii) the linear response approach, colloquially known as the Cococcioni-Gironcoli method [19, 20, 21], (iii) the constrained random phase approximation (cRPA) [22], or (iv) pseudohybrid Hubbard density functional ACBN0 [23]. Regrettably, (ii)-(iv) are notably intricate and do not always yield results close to experiment, and (i) cannot be employed *a priori* without experimental values for comparative analysis. Furthermore, as we demonstrate below, LSDA+$U$+$J$ fails to describe the charge and magnetic moment distribution correctly in some cases.

The $U$ and $J$ parameters play pivotal role in determining the magnetic moments ($\mu$) of materials, particularly in systems characterised by strong electron-electron correlation and localised electronic states. These parameters influence magnetic moments through their effects on electronic configurations and spin alignments within the material's electronic structure.

### 1. Hubbard $U$ Parameter:
- The Hubbard $U$ parameter characterises the on-site Coulomb repulsion between electrons occupying the same atomic orbital. It is quantified by the Hubbard Hamiltonian term:
  $$
  \hat{H}_U = U \sum_i \hat{n}_{i\uparrow} \hat{n}_{i\downarrow}
  $$
  where $\hat{n}_{i\sigma}$ represents the number operator for electrons with spin $\sigma$ on site $i$.
- Increasing $U$ leads to a stronger repulsion between electrons on the same orbital, promoting electron localisation on different orbitals. This effect is captured by the Hubbard Hamiltonian.
- In magnetic materials, localised electrons tend to align their spins to minimise the Coulomb repulsion energy, contributing to the material's magnetic moment. Therefore, larger values of $U$ generally result in stronger electron localisation and larger magnetic moments.

### 2. Hund's Coupling Parameter $J$:
- Hund's coupling $J$ represents the exchange interaction between electrons with parallel spins on the same atomic site. It favours parallel spin configurations over anti parallel ones and is described by the Hamiltonian term:
  $$
  \hat{H}_J = -J \sum_i \left( \hat{S}_i^2 - \frac{\hat{n}_i(\hat{n}_i - 1)}{2} \right)
  $$
  where $\hat{S}_i$ is the total spin operator and $\hat{n}_i$ is the total electron number operator on site $i$.
- Increasing $J$ enhances the energy benefit of aligning spins, particularly in high-spin configurations with multiple unpaired electrons occupying orbitals with the same angular momentum (d- or f-orbitals), but different momentum projections $m$. This effect stabilises high-spin states and contributes to larger magnetic moments in magnetic materials.

### 3. Interaction between $U$ and $J$:
- $U$ and $J$ parameters often exhibit synergistic effects, where a larger $U$ can enhance the effectiveness of $J$ in stabilising high-spin states.
- However, there can also be competing effects between $U$ and $J$. For example, while larger values of $U$ generally lead to more localised electron states and larger magnetic moments, excessively large $U$ can hinder electron mobility and suppress magnetic ordering.

### 4. Material-Specific Considerations:
- The influence of $U$ and $J$ parameters on magnetic moments depends on the material's specific electronic structure, crystal symmetry, and other material parameters.
- Determination of $U$ and $J$ parameters tailored to the material of interest is essential for accurate predictions of magnetic properties. This can be achieved through empirical fitting or theoretical calculations based on electronic-structure methods, as discussed above.


The above mentioned drawbacks can be overcome through the advanced potential-based self-consistency constrained Density Functional Theory (cDFT) energy functional [24] denoted here as $E^{\text{cDFT}}$. This functional, designed to admit the same self-consistent solution as given by specific equations, is expressed as follows:

$$
E_{v_{\text{ext}},N_{\text{A}}}^{\text{cDFT}}[u] = E_{v_{\text{ext}}}^{\text{v}}[u] - R_{\text{A}}^{\text{v}}[u](W_{\text{AA}})^{-1}\left(\rho_{\text{A}}^{\text{v}}[u]-N_{\text{A}}\right) \quad (5)
$$

Here, $E_{v_{\text{ext}}}^{\text{v}}[u]$ is the DFT energy, $R_{\text{A}}^{\text{v}}[u]$ is the residual self-consistent potential, $W_{\text{AA}}$ is the integral of a weight function $w_{\text{A}}(\mathbf{r})$ (which is 1 inside the volume associated with fragment A, and 0 outside) squared, $u$ represents the screened potential, $v_{\text{ext}}$ the external potential depending on atomic positions and cell parameters, and $N_{\text{A}}$ is the number of electrons associated with a specific atomic fragment $A$. Notably, both $v_{\text{ext}}$ and $N_{\text{A}}$ are treated as external parameters in the calculation. The residual self-consistent potential is the integral of residual potential (i.e., the difference between the output and input screening potentials) times the weight function.

<table>
  <thead>
    <tr>
      <th>Atom</th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
      <th>LSDA+U+J / $\mu_B$</th>
      <th>cDFT / $\mu_B$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ba</td>
      <td>0.3333</td>
      <td>0.6667</td>
      <td>0.9816</td>
      <td>-0.0003</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>Ba</td>
      <td>0.6667</td>
      <td>0.3333</td>
      <td>0.4816</td>
      <td>-0.0003</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>0.3333</td>
      <td>0.6667</td>
      <td>0.3780</td>
      <td>0.0037</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>0.6667</td>
      <td>0.3333</td>
      <td>0.8780</td>
      <td>0.0037</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>Co2</td>
      <td>0.1692</td>
      <td>0.3385</td>
      <td>0.6908</td>
      <td>2.4181</td>
      <td>1.9974</td>
    </tr>
    <tr>
      <td>Co2</td>
      <td>0.6615</td>
      <td>0.8308</td>
      <td>0.6908</td>
      <td>2.4181</td>
      <td>1.9974</td>
    </tr>
    <tr>
      <td>Co2</td>
      <td>0.1692</td>
      <td>0.8308</td>
      <td>0.6908</td>
      <td>2.4181</td>
      <td>1.9974</td>
    </tr>
    <tr>
      <td>Co2</td>
      <td>0.8308</td>
      <td>0.6615</td>
      <td>0.1908</td>
      <td>2.4181</td>
      <td>1.9974</td>
    </tr>
    <tr>
      <td>Co2</td>
      <td>0.3385</td>
      <td>0.1692</td>
      <td>0.1908</td>
      <td>2.4181</td>
      <td>1.9974</td>
    </tr>
    <tr>
      <td>Co2</td>
      <td>0.8308</td>
      <td>0.1692</td>
      <td>0.1908</td>
      <td>2.4181</td>
      <td>1.9974</td>
    </tr>
    <tr>
      <td>Co1</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.4423</td>
      <td>-2.5309</td>
      <td>-3.3055</td>
    </tr>
    <tr>
      <td>Co1</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.9423</td>
      <td>-2.5309</td>
      <td>-3.3055</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.0091</td>
      <td>0.5045</td>
      <td>0.7642</td>
      <td>0.0269</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.4955</td>
      <td>0.5045</td>
      <td>0.7642</td>
      <td>0.0269</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.4955</td>
      <td>0.9909</td>
      <td>0.7642</td>
      <td>0.0269</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.9909</td>
      <td>0.4955</td>
      <td>0.2642</td>
      <td>0.0269</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.5045</td>
      <td>0.4955</td>
      <td>0.2642</td>
      <td>0.0269</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.5045</td>
      <td>0.0091</td>
      <td>0.2642</td>
      <td>0.0269</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.1634</td>
      <td>0.3267</td>
      <td>0.5033</td>
      <td>-0.1161</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.6733</td>
      <td>0.8366</td>
      <td>0.5033</td>
      <td>-0.1161</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.1634</td>
      <td>0.8366</td>
      <td>0.5033</td>
      <td>-0.1161</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.8366</td>
      <td>0.6733</td>
      <td>0.0033</td>
      <td>-0.1161</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.3267</td>
      <td>0.1634</td>
      <td>0.0033</td>
      <td>-0.1161</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.8366</td>
      <td>0.1634</td>
      <td>0.0033</td>
      <td>-0.1161</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2571</td>
      <td>-0.0658</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td>O</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.7571</td>
      <td>-0.0658</td>
      <td>0.0000</td>
    </tr>
  </tbody>
</table>

Table 1: Atomic fractional coordinates for the ferrimagnetic Y114 structure optimised with LSDA+U+J (lattice parameters: $a = b = 6.274715382$ Å; $c = 10.234961467$ Å; $\alpha = \beta = 90$; $\gamma = 120$). Magnetic moments calculated with LSDA+U+J and constrained DFT (cDFT). The relaxed atomic positions, primitive vectors, and magnetic moments are all within $10^{-4}$ of the expected values based on crystal symmetry.

The functional $E_{v_{\text{ext}},N_{\text{A}}}^{\text{cDFT}}[u]$ is stationary at the self-consistent potential $v^{*}$, leading to the following self-consistency relation:

$$
E_{v_{\text{ext}},N_{\text{A}}}^{\text{SC}} = E_{v_{\text{ext}},N_{\text{A}}}^{\text{cDFT}}[v^{*}] \quad (6)
$$

Moreover, the functional stationary behaviour is expressed as:

$$
E_{v_{\text{ext}},N_{\text{A}}}^{\text{cDFT}}[u] = E_{v_{\text{ext}},N_{\text{A}}}^{\text{cDFT}}[v^{*}] + O((u - v^{*})^2) \quad (7)
$$

The gradient of this functional with respect to the screened potential $u$ is given by:

$$
\begin{aligned}
\frac{\delta E_{v_{\text{ext}},N_{\text{A}}}^{\text{cDFT}}[u]}{\delta u(\mathbf{r})} &= \int \chi_{0}(\mathbf{r},\mathbf{r}') R^{+\text{v}}[u, \Lambda_{\text{A}}[u]](\mathbf{r}')d\mathbf{r}' \\
&+ \left(\int \epsilon_{e}(\mathbf{r},\mathbf{r}')w_{\text{A}}(\mathbf{r}')d\mathbf{r}'\right)(W_{\text{AA}})^{-1}(\rho_{\text{A}}^{\text{v}}[u]-N_{\text{A}})
\end{aligned}
\quad (8)
$$

Here, $\Lambda_{\text{A}}[u]$ is defined as:

$$
\Lambda_{\text{A}}[u] \triangleq -R_{\text{A}}^{\text{v}}[u](W_{\text{AA}})^{-1}, \quad (9)
$$

$\epsilon_{e}(\mathbf{r},\mathbf{r}')$ is the electron dielectric response function, and $\chi_{0}(\mathbf{r},\mathbf{r}')$ is the independent-particle susceptibility. The formulation introduces a residual for cDFT, denoted as $R^{\text{cDFT}}$, defined as:

$$
\begin{aligned}
R^{\text{cDFT}}[u](\mathbf{r}') &= R^{\text{v}}[u](\mathbf{r}') + \Lambda w_{\text{A}}(\mathbf{r}') \\
&+ c\,w_{\text{A}}(\mathbf{r}')(\rho_{\text{A}}[u]-N_{\text{A}})
\end{aligned}
\quad (10)
$$

where $c$ is a constant, whose value is formally arbitrary, but for practical purposes should be of order one, as it defines the balance between the convergence inside the space spanned by $w_{\text{A}}$ and the convergence inside the space perpendicular to it. The cDFT residual vanishes when both $R^{\text{v}}$ and $\rho_{\text{A}}^{\text{v}}[u]-N_{\text{A}}$ vanish, indicating self-consistency.

The formulation allows for easy computation of derivatives and forces within the cDFT framework, using the $2n+1$ theorem of perturbation theory. Notably, derivatives with respect to number of electrons $(N_{\text{A}})$ yield quantities such as the chemical potential of fragment $A$ $(\chi_{A})$.

The advantages of cDFT for describing magnetic moments are the following:

1.  **Targeted Studies:** cDFT allows one to perform targeted studies by imposing specific constraints on the electronic density, such as fixing the magnetic moments of certain atoms or regions within a material. This capability is particularly useful for investigating phenomena like magnetic phase transitions, spin-crossover materials, or the effects of magnetic doping on electronic properties.

2.  **Understanding Magnetism at the Atomic Level:** With cDFT, it is possible to explore the atomic-scale origins of magnetism in materials. By controlling the magnetic moments of individual atoms or groups of atoms, one can dissect the contributions of different electronic orbitals and chemical environments to the overall magnetic behaviour. This level of detail is crucial for understanding the microscopic mechanisms driving magnetic phenomena.

![](./images/992673273877626885_2.jpg)

Figure 2: Crystal Structure of the optimised ferrimagnetic Y114. Legend: Co within the tetrahedron, azure; Ba, green; Y, grey; O, red.

3. Consistent Description of Magnetic Interactions Between Localized Magnetic Moments: Magnetic interactions play a fundamental role in determining the properties of magnetic materials. The advantage of the hard constraint in cDFT is the full self-consistency of the electronic states fulfilling the constraint. Thus, interaction between the magnetic moments localised according to the constraint is described consistently with interactions that cause the localisation.

4. Prediction of Magnetic Properties: By solving the electronic structure problem self-consistently within the constraints imposed by cDFT, one can obtain accurate predictions of various magnetic properties, such as magnetic moments, magnetic susceptibilities, and magnetic exchange interactions. These predictions can be compared with experimental measurements, providing valuable insights into the underlying physics of magnetism in materials.

5. Exploration of Complex Magnetic Systems: cDFT can be applied to explore the magnetic properties of complex systems, including magnetic nanoparticles, magnetic thin films, and magnetic heterostructures. These systems often exhibit intricate magnetic behaviours arising from size effects, interface effects, or proximity-induced magnetism. cDFT enables one to unravel these complexities and understand how they influence the overall magnetic behaviour of the system.

6. Design of New Magnetic Materials: By leveraging the predictive capabilities of cDFT, one can accelerate the discovery and design of new magnetic materials with tailored magnetic properties. By systematically exploring the parameter space of different magnetic configurations, compositions, and structures, cDFT-guided computational screening can identify promising candidates for experimental synthesis and characterisation.

As a test example for cDFT theoretical framework, we investigate atomic and electronic structure, and magnetic interactions in Y114. Our choice of Y114 as a test case is strategic for several reasons. Firstly, its complex crystal structure and rich electronic properties make it an ideal candidate for exploring the interplay between electronic correlations, lattice distortions, and magnetic interactions. Additionally, the compound exhibits metallic behaviour with the drop of conductivity with increasing of temperature [25] and antiferromagnetic component at low temperature [1, 26, 6]. By utilising DFT+$U+J$ and cDFT methods, we aim to capture the subtle interplay between electron-electron interactions and structural distortions that underlie the magnetism in Y114. These methods allow us to incorporate the effects of strong electron correlation and spin-orbit coupling, providing a more accurate description of the material's electronic structure compared to conventional DFT approximations.

Through comparative analysis of our theoretical predictions with experimental observations, we validate and refine our theoretical framework. In the future we expect to extend our investigation to other magnetic materials.

In essence, our study of the magnetism in Y114 serves is a stepping stone towards a more comprehensive theoretical understanding of complex materials, with implications for diverse fields ranging from condensed matter physics to materials science and beyond.

3. Computational Details

We have performed spin-polarised collinear magnetic calculations along z-axis considering opposite initial spin magnetic moments orientation for $\text{Co}^{2+}$ respect to $\text{Co}^{3+}$. The atomic positions and lattice parameters of the hexagonal crystal structure of Y114 (Materials Project number: mp-19151) are fully relaxed without spin-orbit coupling. This optimisation was executed in the plane-waves basis (PW) framework, employing the Hubbard model applied to LSDA DFT functional (LSDA+$U+J$) [27, 14, 15, 16]. We have fitted the $U$ and $J$ parameters by comparing the computed lattice constants with those from neutron diffraction experiment on Y114 [1]. The final deviations from experimental values of lattice constants $a$ and $c$ were -0.27% and 0.34%, respectively, obtained with $U = 8$ eV for $\text{Co}^{2+}$, $U = 6$ eV for $\text{Co}^{3+}$, and $J = 0.1$ eV for both $\text{Co}^{2+}$ and $\text{Co}^{3+}$ with slightly different tetrahedral coordination. Potential-based self-consistency cDFT [9] with the LSDA functional without spin-orbit coupling was used to self-consistently optimise the magnetic moments for the ferrimagnetic structure, previously optimised with Hubbard model (see Fig. 1), constraining the charge of cobalt atoms to +3 and +2 for corresponding coordinations, and magnetic moments of Y, Ba, and O to zero. The radii of 2 Bohr (the span of the weight functions $w_{\text{A}}(\mathbf{r})$) were chosen to calculate the spherical integrals around atoms. The weight function goes smoothly from 1 to 0 in the region from 1.8 to 2.0 Bohr. This type of partitioning is specific for optimised norm-conserving Vanderbilt pseudopotentials (ONCVPs), which were taken from PseudoDojo project [28, 29] pseudo-dojo.org. The PW kinetic energy cut-off was set at 50 Ha, with a 6×6×3 $\Gamma$-centered $k$-point grid. Convergence was reached when forces fell below $5 \cdot 10^{-5}$ Ha/Bohr. For the geometry optimisation with LSDA+$U+J$ we used Quantum Espresso v.7.2 [30, 31], while cDFT calculations were executed utilising the ABINIT code [32, 33, 34].

![](./images/992673273877626885_3.jpg)

Figure 3: Total and Co 3d-projected density of states (pDOS) calculated with LSDA+$U$+$J$ (a) and cDFT (b).

## 4. Results and Discussion

We fully relaxed the hexagonal structure of Y114 with the ferrimagnetic order, adjusting both atomic positions and lattice constants, characterised by space group $P6_3mc$. Several optimisations were conducted using the LSDA+$U$+$J$ approach, applying different values of $U$ and $J$ on a grid to the $3d$-electrons of Co ions. This iterative process aimed to determine the optimal $U$ and $J$ values that align the computed lattice constants with the experimental values obtained via neutron diffraction at 10 K, as reported in the literature [1], see the Computational Details section.

The Y114 crystal with the ferrimagnetic order exhibits two slightly different environments for $Co^{2+}$ to $Co^{3+}$ as seen in Fig. 2. This was not possible to observe in some experiments due to the electron delocalisation between cobalt sites, inducing fluctuations in the Co oxidation states from $Co^{2+}$ to $Co^{3+}$ and vice versa[1, 6, 35, 26].

<table>
  <thead>
    <tr>
      <th>Bond</th>
      <th>exp. [1]</th>
      <th>GGA+$U$ [8] (no magnetic)</th>
      <th>LSDA+$U$+$J$ (ferrimagnetic)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Co1-O1</td>
      <td>2.0339</td>
      <td>1.9344</td>
      <td>1.8955</td>
    </tr>
    <tr>
      <td>Co1-O2</td>
      <td>1.9239</td>
      <td>1.8983</td>
      <td>1.8824</td>
    </tr>
    <tr>
      <td>Co1-O3</td>
      <td>1.9239</td>
      <td>1.8983</td>
      <td>1.8818</td>
    </tr>
    <tr>
      <td>Co1-O4</td>
      <td>1.9239</td>
      <td>1.8983</td>
      <td>1.8818</td>
    </tr>
    <tr>
      <td>Co2-O2</td>
      <td>1.8875</td>
      <td>1.8752</td>
      <td>1.92581</td>
    </tr>
    <tr>
      <td>Co2-O5</td>
      <td>1.9057</td>
      <td>1.9325</td>
      <td>1.92581</td>
    </tr>
    <tr>
      <td>Co2-O6</td>
      <td>1.9057</td>
      <td>1.9325</td>
      <td>1.92581</td>
    </tr>
    <tr>
      <td>Co2-O7</td>
      <td>1.9368</td>
      <td>-</td>
      <td>1.96010</td>
    </tr>
  </tbody>
</table>

Table 2: Bond lengths in Å for Y114 structure shown in the Fig. 2 obtained from experiment [1], GGA+$U$ non-magnetic state calculations [8], and ferrimagnetic LSDA+$U$+$J$ calculations performed in this work.

The coordination of $Co^{3+}$ (see Fig. 2) is characterised by a distorted tetrahedral geometry in the experimental structure [1]. In this structure, the apical bond (Co1-O1) is the longest one between Co and O (see Table 2), while the bonds with the other three basal oxygen atoms have nearly identical lengths (see Co1-O2, Co1-O3, and Co1-O4 in Table 2). In both the non-magnetic structure studied by Tantardini *et al.* [8] and the ferrimagnetic structure investigated here, a distorted tetrahedron associated with $Co^{3+}$ is observed (see Table 3). In these computed structures, the longest bond remains the apical one. However, in the ferrimagnetic structure, the two basal oxygen atoms that form bridges between $Co^{3+}$ and Ba (see Co1-O3 and Co1-O4 in Table 2) have similar bond length, and they slightly differ from the one for the third basal oxygen atom, which forms a bridge between $Co^{3+}$ and Y (see Co1-O2 in Table 2).

<table>
  <thead>
    <tr>
      <th>Bond Angle</th>
      <th>exp. [1]</th>
      <th>GGA+$U$ [8] (no magnetic)</th>
      <th>LSDA+$U$+$J$ (ferrimagnetic)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O1-Co1-O2</td>
      <td>108.5881</td>
      <td>117.6609</td>
      <td>109.3700</td>
    </tr>
    <tr>
      <td>O1-Co1-O3</td>
      <td>108.5881</td>
      <td>100.1790</td>
      <td>109.3755</td>
    </tr>
    <tr>
      <td>O1-Co1-O4</td>
      <td>108.5881</td>
      <td>100.1791</td>
      <td>109.3755</td>
    </tr>
    <tr>
      <td>O2-Co1-O3</td>
      <td>110.3398</td>
      <td>117.6609</td>
      <td>109.5612</td>
    </tr>
    <tr>
      <td>O2-Co1-O4</td>
      <td>110.3398</td>
      <td>117.6609</td>
      <td>109.5612</td>
    </tr>
    <tr>
      <td>O3-Co1-O4</td>
      <td>110.3398</td>
      <td>100.1790</td>
      <td>109.5833</td>
    </tr>
    <tr>
      <td>O2-Co2-O5</td>
      <td>112.9615</td>
      <td>-</td>
      <td>113.9086</td>
    </tr>
    <tr>
      <td>O2-Co2-O6</td>
      <td>112.9615</td>
      <td>-</td>
      <td>113.9086</td>
    </tr>
    <tr>
      <td>O2-Co2-O7</td>
      <td>107.0432</td>
      <td>-</td>
      <td>108.3735</td>
    </tr>
    <tr>
      <td>O5-Co2-O6</td>
      <td>103.2645</td>
      <td>-</td>
      <td>104.8207</td>
    </tr>
    <tr>
      <td>O5-Co2-O7</td>
      <td>110.3193</td>
      <td>-</td>
      <td>107.7532</td>
    </tr>
    <tr>
      <td>O6-Co2-O7</td>
      <td>110.3193</td>
      <td>-</td>
      <td>107.7533</td>
    </tr>
  </tbody>
</table>

Table 3: Bond angles in degrees for experimental Y114 structure shown in the Fig. 2 [1], GGA+$U$ non-magnetic structure from the previous work by Tantardini *et al.* [8], and the ferrimagnetic LSDA+$U$+$J$ structure calculated in this work.

The O-coordination of $Co^{2+}$ (see Fig. 2) is a distorted tetrahedron in both the experimental and ferrimagnetic structures, but it is triangular in the non-magnetic structure, as shown by Tantardini *et al.* [8] (see Table 2 and Table 3). In the experimental structure, the apical distance between $Co^{2+}$ and the oxygen that bridges Y and $Co^{3+}$ is the shortest (see Co2-O5 in Ta-

ble 2). However, in the ferrimagnetic structure obtained here using LSDA+U+J, this distance is identical to that between $\text{Co}^{2+}$ and the oxygen atoms bridging the other $\text{Co}^{2+}$ ions in the Kagome lattice (see Co2-O6 and Co2-O7 in Table 2). Fur- thermore, in both the experimental and calculated ferrimagnetic structures, the longest bond is between $\text{Co}^{2+}$ and the oxygen that bridges to $\text{Co}^{3+}$. This distance is increased to $2.19\ \text{\AA}$ by the triangular distortion of $\text{Co}^{2+}$ in the non-magnetic structure obtained by Tantardini *et al.* [8].

In summary, our study successfully describes the different atomic sites within the material. Cobalt atoms are arranged such that $\text{Co}^{3+}$ sites are positioned between the triangles formed by $\text{Co}^{2+}$ sites, characteristic of the Kagome lattice structure [36, 37, 38].

The ferrimagnetic properties of the structure (see Table 1) are due to distinct magnetic moments for the two types of Co sites. The cobalt (Co) atom has an atomic number of 27 and a valence electronic configuration of $4s^23d^7$. In a tetrahedral coordina- tion, the Co ion has three $3d$ orbitals that do not participate in chemical bonding. These orbitals are divided into two differ- ent groups based on symmetry: the $t_2$ group, consisting of the $d_{xy}$, $d_{yz}$, and $d_{xz}$ orbitals, which are higher in energy compared to the $e$ group, consisting of the $d_{x^2-y^2}$ and $d_{z^2}$ orbitals [39]. Thus, for $\text{Co}^{2+}$, the valence electronic configuration changes to $4s^03d^7$, which can only exist in one possible configuration with 3 unpaired spin magnetic moments (i.e., $3\ \mu_B$). In con- trast, for $\text{Co}^{3+}$, the valence electronic configuration changes to $4s^03d^6$, which can adopt two configurations: a high-spin statewith 4 unpaired electrons (i.e., $4\ \mu_B$) or a low-spin state with 2 unpaired electrons (i.e., $2\ \mu_B$). The LSDA+U+J magnetic mo- ments are $2.41\ \mu_B$ for $\text{Co}^{2+}$ and $-2.53\ \mu_B$ for $\text{Co}^{3+}$. The devia- tion between LSDA+U+J magnetic moments and the expected values can be explained by a spillover of magnetic moment to other atoms in the crystal (e.g., oxygen), by Co ions adopting lower-spin states, by interaction between Co ions, or by a com- bination of these factors. We find a rather small magnetisation of the order of $0.1\ \mu_B$ on the oxygen atoms, which cannot ex- plain the deviation. The experimental values of magnetic mo- ments, deduced from inverse magnetic susceptibility measure-ment in X-ray powder diffraction at $2\ \text{K}$ [6], are $-3.49(8)\ \mu_B$ for $\text{Co}^{3+}$ and $2.19(4)\ \mu_B$ for $\text{Co}^{2+}$. Interestingly, the experimen- tal magnetic moment of $\text{Co}^{2+}$ is even further from the expected high-spin moment $3\ \mu_B$ than the LSDA+U+J, and falls between the high-spin and low-spin value $(1\ \mu_B)$ for the free $\text{Co}^{2+}$ ion. As discussed in the literature on quantum chemical topology of spin-density distributions [40, 41], this can be explained by the interaction between Co ions in the lattice.

To address the discrepancies in magnetic moments derived from LSDA+U+J and experiments, we employed cDFT [9] imposing a constraint on charge of the cobalt atoms. Based on the previous works [8, 1, 6, 35, 26], three of the four Co atoms per formula unit were assigned the oxidation state of +2, and the remaining Co atom was constrained to the oxidation state of +3. Furthermore, oxygen barium, and yttrium are ex- pected to be non-magnetic, and therefore their magnetic mo- ments were constrained to be zero. It is noteworthy that cDFT is parameterised directly to account for local effects attributable to the different oxidation states of cobalt atoms, while the $U$ and $J$ parameters in traditional LSDA+U+J are chosen based on other criteria, and are forced to be the same for magnetic ions in different oxidation states. This results in delocaliza- tion of the $d$-electrons and incorrect magnetic moments. cDFTyields the magnetic moments of $-3.30\ \mu_B$ for $\text{Co}^{3+}$ and $2.00\ \mu_B$ for $\text{Co}^{2+}$, which are much closer to the experimental values [6] than LSDA+U+J (see Table 1). Thus, cDFT correctly repro- duces the interaction (via chemical bonding) between Co ions, resulting in the apparent reduction of local spin moment on Co ions, particularly on $\text{Co}^{2+}$ with $(d^7)$ configuration.

These differences between LSDA+U+J and cDFT are fur- ther investigated by examining the projected density of states (pDOS), as illustrated in Figure 3. We find drastic differences between the two methods. In contrast to LSDA+U+J, which exhibits spin-majority states with predominant O $2p$ character at and near the Fermi energy (as depicted in Fig. 3a), cDFT pDOS in general exhibits sharper peaks, indicating state local- isation, and the states around the Fermi level are spin-minority states with predominant $\text{Co}^{2+}$ $3d$ character (Fig. 3b). The smaller contribution of O $2p$ states around the Fermi level in the case of cDFT can be attributed to the constraint steering the magnetic moments on non-magnetic ions in the crystal to zero. Thus, cDFT provides a unique and, according to the experimen- tal results, more accurate representation of electronic structure and orbital occupation within Y114.

## 5. Conclusions

In this study, we have demonstrated how potential-based self- consistent cDFT can be used to improve description of mag- netic interactions in complex magnetic compounds, using Y114 as a prototypical example. While Hubbard model, with the pa- rameters $U$ and $J$ fitted to reproduce experimental lattice con- stants, correctly predicts charge disproportionation leading toslightly different tetrahedral O-coordination of $\text{Co}^{2+}$ and $\text{Co}^{3+}$ ions, and ferrimagnetic order, it fails to correctly describe mag- netic moments of the Co ions. By imposing potential-based self-consistent charge constraints on the Co ions, and con- straining the magnetic moments of non-magnetic ions (Y, Ba, and O) to be zero in the cDFT framework, we obtain mag- netic moments of Co ions much closer to experimental values. Thus, potential-based self-consistent cDFT allows for accurate prediction of magnetic properties using the much more intu- itive parameter choice (charges around the magnetic ions) than choice of $U$ and $J$ in Hubbard model.

The cDFT results confirm the value of magnetic moment of $\text{Co}^{2+}$ ions close to $2\ \mu_B$, which is exactly between high-spin and low-spin states of an isolated $\text{Co}^{2+}$ ion. This is explained by a strong interaction (bonding) between Co ions in the lattice. This bonding can also explain the dynamic redistribution of the +2/+3 charge in the Co lattice and the resulting oxygen tetrahe- dra distortion, rendering it difficult to detect in experiments.

## 6. Acknowledgments

The research was carried out within the state assignment to ISSCM SB RAS (project No. 121032500059-4). I.S.N. was supported by Russian Science Foundation (grant number 22-73-10206, https://rscf.ru/project/22-73-10206/). Authors would like to thank Prof. Dr. A.G. Kvashnin for useful discussion.

## 7. Data Availability

Data are available upon reasonable request to the corresponding author.

## References

[1] M. Valldor, M. Andersson, The structure of the new compound ybaco4o7 with a magnetic feature, Solid State Sciences 4 (7) (2002) 923-931.

[2] M. Valldor, Syntheses and structures of compounds with ybaco4o7-type structure, Solid State Sciences 6 (3) (2004) 251-266. doi:https://doi.org/10.1016/j.solidstatesciences.2004.01.004. URL https://www.sciencedirect.com/science/article/pii/S1293255804000172

[3] A. Maignan, V. Caignaert, D. Pelloquin, S. Hébert, V. Pralong, J. Hejtmanek, D. Khomskii, Spin, charge, and lattice coupling in triangular and kagomé sublattices of co o 4 tetrahedra: Yb ba co 4 o 7+ $\delta$ ($\delta$= 0, 1), Physical Review B 74 (16) (2006) 165110.

[4] V. Caignaert, A. Maignan, V. Pralong, S. Hébert, D. Pelloquin, A cobaltite with a room temperature electrical and magnetic transition: Ybaco4o7, Solid state sciences 8 (10) (2006) 1160-1163.

[5] N. Podberezskaya, A. Smolentsev, L. Kozeeva, M. Y. Kameneva, A. Lavrov, Yttrium barium heptaoxocobaltite ybaco 4 o 7+ $\delta$: Refinement of the structure and determination of the composition, Crystallography Reports 58 (2013) 682-686.

[6] L. Chapon, P. Radaelli, H. Zheng, J. Mitchell, Competing magnetic interactions in the extended kagomé system y ba co 4 o 7, Physical Review B 74 (17) (2006) 172401.

[7] R. Nithya, T. G. Kumary, T. R. Ravindran, Absence of phase transitions in an oxygen stoichiometric cobaltite, YBaCo4O7, AIP Advances 3 (2) (2013) 022115. arXiv:https://pubs.aip.org/aip/adv/article-pdf/doi/10.1063/1.4792597/13060911/022115\_1\_online.pdf, doi:10.1063/1.4792597. URL https://doi.org/10.1063/1.4792597

[8] C. Tantardini, E. Benassi, Crystal structure resolution of an insulator due to the cooperative jahn-teller effect through bader's theory: the challenging case of cobaltite oxide y114, Dalton Transactions 47 (15) (2018) 5483-5491.

[9] X. Gonze, B. Seddon, J. A. Elliott, C. Tantardini, A. V. Shapeev, Constrained density functional theory: A potential-based self-consistency approach, Journal of Chemical Theory and Computation 18 (10) (2022) 6099-6110.

[10] B. Kaduk, T. Kowalczyk, T. Van Voorhis, Constrained density functional theory, Chemical reviews 112 (1) (2012) 321-370.

[11] D. D. O'Regan, G. Teobaldi, Optimization of constrained density functional theory, Physical Review B 94 (3) (2016) 035159.

[12] Q. Wu, T. Van Voorhis, Constrained density functional theory and its application in long-range electron transfer, Journal of Chemical Theory and Computation 2 (3) (2006) 765-774.

[13] B. Himmetoglu, A. Floris, S. de Gironcoli, M. Cococcioni, Hubbard-corrected dft energy functionals: The lda+u description of correlated systems, International Journal of Quantum Chemistry 114 (1) (2014) 14-49.

[14] V. I. Anisimov, J. Zaanen, O. K. Andersen, Band theory and mott insulators: Hubbard u instead of stoner i, Physical Review B 44 (3) (1991) 943.

[15] V. Anisimov, O. Gunnarsson, Density-functional calculation of effective coulomb interactions in metals, Physical Review B 43 (10) (1991) 7570.

[16] V. I. Anisimov, I. V. Solovyev, M. A. Korotin, M. T. Czyżyk, G. A. Sawatzky, Density-functional theory and nio photoemission spectra, Phys. Rev. B 48 (1993) 16929-16934. doi:10.1103/PhysRevB.48.16929. URL https://link.aps.org/doi/10.1103/PhysRevB.48.16929

[17] A. I. Liechtenstein, V. I. Anisimov, J. Zaanen, Density-functional theory and strong interactions: Orbital ordering in mott-hubbard insulators, Phys. Rev. B 52 (8) (1995) R5467-R5470. doi:10.1103/physrevb.52.r5467. URL https://doi.org/10.1103/physrevb.52.r5467

[18] M. T. Czyżyk, G. A. Sawatzky, Local-density functional and on-site correlations: The electronic structure of la2cuo4 and lacuo3, Phys. Rev. B 49 (20) (1994) 14211-14228. doi:10.1103/physrevb.49.14211. URL https://doi.org/10.1103/physrevb.49.14211

[19] M. Cococcioni, S. De Gironcoli, Linear response approach to the calculation of the effective interaction parameters in the lda+ u method, Physical Review B 71 (3) (2005) 035105.

[20] I. Timrov, N. Marzari, M. Cococcioni, Hp – a code for the calculation of hubbard parameters using density-functional perturbation theory, Computer Physics Communications 279 (2022) 108455.

[21] I. Timrov, N. Marzari, M. Cococcioni, Self-consistent hubbard parameters from density-functional perturbation theory in the ultrasoft and projector-augmented wave formulations, Phys. Rev. B 103 (2021) 045141. doi:10.1103/PhysRevB.103.045141. URL https://link.aps.org/doi/10.1103/PhysRevB.103.045141

[22] B. Amadon, T. Applencourt, F. Bruneval, Screened coulomb interaction calculations: Crpa implementation and applications to dynamical screening and self-consistency in uranium dioxide and cerium, Phys. Rev. B 89 (12) (2014) 125110. doi:10.1103/physrevb.89.125110. URL https://doi.org/10.1103/physrevb.89.125110

[23] L. A. Agapito, S. Curtarolo, M. Buongiorno Nardelli, Reformulation of DFT $+u$ as a pseudohybrid hubbard density functional for accelerated materials discovery, Phys. Rev. X 5 (2015) 011006. doi:10.1103/PhysRevX.5.011006. URL https://link.aps.org/doi/10.1103/PhysRevX.5.011006

[24] X. Gonze, B. Seddon, J. A. Elliott, C. Tantardini, A. V. Shapeev, Constrained density functional theory: A potential-based self-consistency approach, Journal of Chemical Theory and Computation 18 (10) (2022) 6099-6110.

[25] E. Tsipis, D. Khalyavin, S. Shiryaev, K. Redkina, P. Nunez, Electrical and magnetic properties of ybaco4o7+ $\delta$, Materials chemistry and physics 92 (1) (2005) 33-38.

[26] A. Huq, J. Mitchell, H. Zheng, L. Chapon, P. Radaelli, K. Knight, P. Stephens, Structural and magnetic properties of the kagomé antiferromagnet ybaco4o7, Journal of Solid State Chemistry 179 (4) (2006) 1136-1145.

[27] J. P. Perdew, Y. Wang, Accurate and simple analytic representation of the electron-gas correlation energy, Phys. Rev. B 45 (23) (1992) 13244-13249. doi:10.1103/physrevb.45.13244. URL http://dx.doi.org/10.1103/physrevb.45.13244

[28] M. van Setten, M. Giantomassi, E. Bousquet, M. Verstraete, D. Hamann, X. Gonze, G.-M. Rignanese, The pseudodojo: Training and grading a 85 element optimized norm-conserving pseudopotential table, Computer Physics Communications 226 (2018) 39-54. doi:https://doi.org/10.1016/j.cpc.2018.01.012. URL https://www.sciencedirect.com/science/article/pii/S0010465518300250

[29] D. R. Hamann, Optimized norm-conserving vanderbilt pseudopotentials, Phys. Rev. B 88 (2013) 085117.

[30] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Braccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, R. M. Wentzcovitch, Quantum espresso: a modular and open-source software project for quantum simulations of materials, Journal of Physics: Condensed Matter 21 (39) (2009) 395502.

[31] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna,

I. Carnimeo, A. D. Corso, S. de Gironcoli, P. Delugas, R. A. DiSta-
sio, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Ger-
stmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj,
E. Küçükbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L.
Nguyen, H.-V. Nguyen, A. O. de-la Roza, L. Paulatto, S. Poncé, D. Rocca,
R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Tim-
rov, T. Thonhauser, P. Umari, N. Vast, X. Wu, S. Baroni, Advanced
capabilities for materials modelling with quantum espresso, Journal of
Physics: Condensed Matter 29 (46) (2017) 465901.

[32] X. Gonze, F. Jollet, F. A. Araujo, D. Adams, B. Amadon, T. Applen-
court, C. Audouze, J.-M. Beuken, J. Bieder, A. Bokhanchuk, E. Bousquet,
F. Bruneval, D. Caliste, M. Côté, F. Dahm, F. D. Pieve, M. Delaveau,
M. D. Gennaro, B. Dorado, C. Espejo, G. Geneste, L. Genovese,
A. Gerossier, M. Giantomassi, Y. Gillet, D. Hamann, L. He, G. Jomard,
J. L. Janssen, S. L. Roux, A. Levitt, A. Lherbier, F. Liu, I. Lukačević,
A. Martin, C. Martins, M. Oliveira, S. Poncé, Y. Pouillon, T. Rangel,
G.-M. Rignanese, A. Romero, B. Rousseau, O. Rubel, A. Shukri,
M. Stankovski, M. Torrent, M. V. Setten, B. V. Troeye, M. Verstraete,
D. Waroquiers, J. Wiktor, B. Xue, A. Zhou, J. Zwanziger, Recent develop-
ments in the abinit software package, Computer Physics Communications
205 (2016) 106–131.

[33] X. Gonze, B. Amadon, G. Antonius, F. Arnardi, L. Baguet, J.-M. Beuken,
J. Bieder, F. Bottin, J. Bouchet, E. Bousquet, N. Brouwer, F. Bruneval,
G. Brunin, T. Cavignac, J.-B. Charraud, W. Chen, M. Côté, S. Cottenier,
J. Denier, G. Geneste, P. Ghosez, M. Giantomassi, Y. Gillet, O. Gingras,
D. R. Hamann, G. Hautier, X. He, N. Helbig, N. Holzwarth, Y. Jia, F. Jol-
let, W. Lafargue-Dit-Hauret, K. Lejaeghere, M. A. L. Marques, A. Mar-
tin, C. Martins, H. P. C. Miranda, F. Naccarato, K. Persson, G. Petretto,
V. Planes, Y. Pouillon, S. Prokhorenko, F. Ricci, G.-M. Rignanese, A. H.
Romero, M. M. Schmitt, M. Torrent, M. J. van Setten, B. Van Troeye,
M. J. Verstraete, G. Zérah, J. W. Zwanziger, The abinit project: Impact,
environment and recent developments., Computer Physics Communica-
tions 248 (2020) 107042.

[34] A. H. Romero, D. C. Allan, B. Amadon, G. Antonius, T. Applencourt,
L. Baguet, J. Bieder, F. Bottin, J. Bouchet, E. Bousquet, F. Bruneval,
G. Brunin, D. Caliste, M. Côté, J. Denier, C. Dreyer, P. Ghosez, M. Gi-
antomassi, Y. Gillet, O. Gingras, D. R. Hamann, G. Hautier, F. Jollet,
G. Jomard, A. Martin, H. P. C. Miranda, F. Naccarato, G. Petretto, N. A.
Pike, V. Planes, S. Prokhorenko, T. Rangel, F. Ricci, G.-M. Rignanese,
M. Royo, M. Stengel, M. Torrent, M. J. van Setten, B. V. Troeye, M. J.
Verstraete, J. Wiktor, J. W. Zwanziger, X. Gonze, Abinit: Overview, and
focus on selected capabilities, J. Chem. Phys. 152 (2020) 124102.

[35] M. Soda, Y. Yasui, T. Moyoshi, M. Sato, N. Igawa, K. Kakurai, Magnetic
structure of ybaco4o7 with kagome and triangular lattices, Journal of the
Physical Society of Japan 75 (5) (2006) 054707.

[36] N. J. Ghimire, I. I. Mazin, Topology and correlations on the kagome
lattice, Nature Materials 19 (2) (2020) 137–138. doi:10.1038/
s41563-019-0589-8.
URL https://doi.org/10.1038/s41563-019-0589-8

[37] I. Syôzi, Statistics of Kagomé Lattice, Progress of Theoretical
Physics 6 (3) (1951) 306–308. arXiv:https://academic.
oup.com/ptp/article-pdf/6/3/306/5239621/6-3-306.pdf,
doi:10.1143/ptp/6.3.306.
URL https://doi.org/10.1143/ptp/6.3.306

[38] M. L. Kiesel, R. Thomale, Sublattice interference in the kagome hubbard
model, Physical Review B—Condensed Matter and Materials Physics
86 (12) (2012) 121105.

[39] Y. Jean, Molecular orbitals of transition metal complexes, OUP Oxford,
2005.

[40] G. Bruno, G. Macetti, L. Lo Presti, C. Gatti, Spin density topology,
Molecules 25 (15) (2020) 3537.

[41] G. Macetti, L. Lo Presti, C. Gatti, Spin density accuracy and distribution
in azido cu (ii) complexes: A source function analysis, Journal of compu-
tational chemistry 39 (10) (2018) 587–603.