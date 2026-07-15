PHYSICAL REVIEW B 89, 195112 (2014)

# Self-consistent hybrid functional for condensed systems

Jonathan H. Skone, $^{1}$ Marco Govoni, $^{2}$ and Giulia Galli $^{2, *}$

$^{1}$ Department of Chemistry, University of California, Davis, One Shields Ave., Davis, California 95616, USA
$^{2}$ Institute for Molecular Engineering, University of Chicago, 5801 South Ellis Avenue, Chicago, Illinois 60637, USA
(Received 15 March 2014; revised manuscript received 17 April 2014; published 9 May 2014)

A self-consistent scheme for determining the optimal fraction of exact exchange for full-range hybrid functionals is presented and applied to the calculation of band gaps and dielectric constants of solids. The exchange-correlation functional is defined in a similar manner to the PBE0 functional, but the mixing parameter is set equal to the inverse macroscopic dielectric function and it is determined self-consistently by computing the optimal dielectric screening. We found excellent agreement with experiments for the properties of a broad class of systems, with band gaps ranging between 0.7 and 21.7 eV and dielectric constants within 1.23 and 15.9. We propose that the eigenvalues and eigenfunctions obtained with the present self-consistent hybrid scheme may be excellent inputs for $G_{0}W_{0}$ calculations.

DOI: 10.1103/PhysRevB.89.195112
PACS number(s): 71.15.Mb, 31.15.E−, 77.22.−d

## I. INTRODUCTION

Density functional theory (DFT) [1] continues to be a widely used theoretical methodology to describe both condensed matter and molecular systems. Its success is owed to the reasonably good accuracy in predicting numerous properties of broad classes of materials and molecules at a relatively low computational cost. In the Kohn-Sham (KS) [2] formulation of DFT, the density-dependent potential, Eq. (1), is the sum of the Hartree $v_{H}$, the exchange-correlation $v_{xc}$, and the external potential of the nuclei $v_{ext}$:
$$
v_{\mathrm{KS}}(\mathbf{r})=v_{H}(\mathbf{r})+v_{\mathrm{xc}}(\mathbf{r})+v_{\mathrm{ext}}(\mathbf{r}). \tag{1}
$$

The exact exchange-correlation potential is not known and it is approximated in various manners. To date, in the condensed matter physics community, the most widely used exchange-correlation functionals have been the local density approximation (LDA) and semilocal generalized gradient approximation (GGA) [3]. Another popular approximation makes use of so-called hybrid functionals, defined by the sum of a local $v_{xc}$ and of a term proportional to the Hartree-Fock exact-exchange operator [4]. Within the generalized Kohn-Sham (GKS) formalism [5], the total nonlocal potential $v_{\mathrm{GKS}}(\mathbf{r},\mathbf{r}')$ is given by
$$
v_{\mathrm{GKS}}(\mathbf{r},\mathbf{r}')=v_{H}(\mathbf{r})+v_{\mathrm{xc}}(\mathbf{r},\mathbf{r}')+v_{\mathrm{ext}}(\mathbf{r}), \tag{2}
$$
where $v_{\mathrm{xc}}$ is now fully nonlocal and can be expressed as
$$
\begin{aligned}
v_{\mathrm{xc}}(\mathbf{r},\mathbf{r}')&=\beta v_{x}^{\mathrm{sr}-\mathrm{ex}}(\mathbf{r},\mathbf{r}';\omega)+\alpha v_{x}^{\mathrm{lr}-\mathrm{ex}}(\mathbf{r},\mathbf{r}';\omega) \\
&+(1-\beta)v_{x}^{\mathrm{sr}}(\mathbf{r};\omega)+(1-\alpha)v_{x}^{\mathrm{lr}}(\mathbf{r};\omega)+v_{c}(\mathbf{r}).
\end{aligned} \tag{3}
$$

In Eq. (3), $\alpha$ and $\beta$ are parameters that determine the amount of long-range and short-range exact exchange, respectively. The long-range nonlocal potential $v_{x}^{\mathrm{lr}-\mathrm{ex}}(\mathbf{r},\mathbf{r}';\omega)$ is defined as
$$
v_{x}^{\mathrm{lr}-\mathrm{ex}}(\mathbf{r},\mathbf{r}';\omega)=-\sum_{i=1}^{N_{\mathrm{occ}}}\phi_{i}(\mathbf{r})\phi_{i}^{*}(\mathbf{r}')\frac{\mathrm{erf}(\omega|\mathbf{r}-\mathbf{r}'|)}{|\mathbf{r}-\mathbf{r}'|}, \tag{4}
$$
where $\omega$ is a parameter (separation length) and $\phi_{i}$ are single-particle, occupied electronic orbitals. The short-range potential $v_{x}^{\mathrm{sr}-\mathrm{ex}}(\mathbf{r},\mathbf{r}';\omega)$ is defined in a similar manner, with the complementary error function replacing the error function in Eq. (4):
$$
v_{x}^{\mathrm{sr}-\mathrm{ex}}(\mathbf{r},\mathbf{r}';\omega)=-\sum_{i=1}^{N_{\mathrm{occ}}}\phi_{i}(\mathbf{r})\phi_{i}^{*}(\mathbf{r}')\frac{\mathrm{erfc}(\omega|\mathbf{r}-\mathbf{r}'|)}{|\mathbf{r}-\mathbf{r}'|}. \tag{5}
$$

The Coulomb potential is partitioned [6] as
$$
\frac{1}{|\mathbf{r}-\mathbf{r}'|}=\frac{\mathrm{erfc}(\omega|\mathbf{r}-\mathbf{r}'|)}{|\mathbf{r}-\mathbf{r}'|}+\frac{\mathrm{erf}(\omega|\mathbf{r}-\mathbf{r}'|)}{|\mathbf{r}-\mathbf{r}'|}. \tag{6}
$$

When $\alpha=\beta=0$, one recovers the KS equations with a local or semilocal exchange-correlation potential. If $\alpha=\beta=1$, one obtains the KS equations with exact-exchange potential. For short-range hybrid functionals $\alpha=0$, e.g., in HSE06 [7], where $\beta=0.25$ and $\omega=0.11$ bohr$^{-1}$, or in sX-LDA [8], where $\beta=1$ and the Thomas-Fermi screening factor is used instead of the error function. When $\alpha\neq0$ the range-separated hybrid functional is long ranged. Examples of long-range hybrid functionals include the empirical CAM-B3LYP functional [9], where $\alpha=0.65,\beta=0.19,\omega=0.33$ bohr$^{-1}$, as well as LC-$\omega$PBE [10], where $\alpha=1$, $\beta=0$, and $\omega=0.4$ bohr$^{-1}$. When $\alpha=\beta$, a full-range hybrid functional is obtained and $\alpha$ determines the fraction of exact exchange entering the definition of the potential:
$$
v_{\mathrm{xc}}(\mathbf{r},\mathbf{r}')=\alpha v_{x}^{\mathrm{ex}}(\mathbf{r},\mathbf{r}')+(1-\alpha)v_{x}(\mathbf{r})+v_{c}(\mathbf{r}), \tag{7}
$$
where $v_{x}^{\mathrm{ex}}(\mathbf{r},\mathbf{r}')$ corresponds to the sum of the exact-exchange terms of Eqs. (4) and (5), and similarly, $v_{x}(\mathbf{r})$ corresponds to the sum of the local exchange terms in Eq. (3).

An example of a full-range hybrid is PBE0 [11], where $\alpha=0.25$. Hybrid functionals have been regularly used to describe molecules [12], but their application to condensed matter systems has been slower to realize due to the substantial increase in computational cost, with respect to local functionals, when using, e.g., plane-wave basis sets. However, in the last decade, due in part to several methodological advances [13–15], hybrid functionals have been increasingly used to investigate a variety of periodic systems with plane-wave basis sets and have been shown to surmount some of

*Author to whom correspondence should be addressed: gagalli@uchicago.edu

1098-0121/2014/89(19)/195112(12)
195112-1
©2014 American Physical Society

the shortcomings of local and semilocal functionals [16]. The fraction of exact exchange included in the potential greatly affects the calculated electronic structure and related quantities such as the static dielectric constant, the energy gap, and equilibrium geometries. In most hybrid functionals used to date, the fraction of exact exchange is kept fixed.

Recently, several authors have suggested using $\alpha$ as an adjustable parameter to reproduce the experimental band gap of solids [17-21]. For nonmetallic, condensed systems the screening of the long-range tail of the Coulomb interaction is proportional to the inverse of the static dielectric constant $(\epsilon_{\infty}^{-1})$ and it is thus intuitive to relate the parameter $\alpha$ in Eq. (7) to $\epsilon_{\infty}^{-1}$. One may also justify such a relation by using many-body perturbation theory [22,23]. For example, in Hedin's equations [24], the exchange-correlation potential of Eq. (7) is replaced by the self-energy $\Sigma$, which is a nonlocal and energy-dependent operator. One of the most successful approximations to $\Sigma$ is the $GW$ approximation [25], which has been extensively used in the last three decades to improve upon the single-particle energies and wave functions obtained with local and semilocal DFT calculations [26-30]. Since the GKS potential is not energy dependent, one may only draw a comparison between Eq. (7) and Hedin's equation in the $GW$, static approximation, known as the static COulomb Hole plus Screened EXchange (COHSEX) [24]. The connection between hybrid functionals and the COHSEX approximation has been previously discussed [20,31,32], and we consider it here in further detail. Within the COHSEX approximation, the self-energy contains separable local and nonlocal potentials:
$$
\Sigma(\mathbf{r}, \mathbf{r}^{\prime}, \omega=0)=\Sigma_{\mathrm{COH}}(\mathbf{r}, \mathbf{r}^{\prime})+\Sigma_{\mathrm{SEX}}(\mathbf{r}, \mathbf{r}^{\prime}),\qquad(8)
$$
where the local $\Sigma_{\mathrm{COH}}$ represents the Coulomb-hole (COH) interaction and the nonlocal $\Sigma_{\mathrm{SEX}}$ is the statically screened exchange (SEX):
$$
\Sigma_{\mathrm{COH}}(\mathbf{r}, \mathbf{r}^{\prime})=-\frac{1}{2} \delta\left(\mathbf{r}-\mathbf{r}^{\prime}\right)\left[v(\mathbf{r}, \mathbf{r}^{\prime})-W(\mathbf{r}, \mathbf{r}^{\prime})\right],\qquad(9)
$$

$$
\Sigma_{\mathrm{SEX}}(\mathbf{r}, \mathbf{r}^{\prime})=-\sum_{i=1}^{\mathrm{N}_{\mathrm{occ}}} \phi_{i}(\mathbf{r}) \phi_{i}^{*}(\mathbf{r}^{\prime}) W(\mathbf{r}, \mathbf{r}^{\prime}).\qquad(10)
$$

In Eqs. (9) and (10), the screened Coulomb potential $W$ is given by
$$
W(\mathbf{r}, \mathbf{r}^{\prime})=\int d \mathbf{r}^{\prime \prime} \epsilon^{-1}(\mathbf{r}, \mathbf{r}^{\prime \prime}) v(\mathbf{r}^{\prime \prime}, \mathbf{r}^{\prime}),\qquad(11)
$$
where $\epsilon^{-1}$ is the dielectric response function and $v$ is the bare Coulomb potential. If we approximate the inverse microscopic dielectric function $\epsilon^{-1}$ by the inverse macroscopic dielectric constant $\epsilon_{\infty}^{-1}$, thereby neglecting the microscopic components of the dielectric screening, we obtain
$$
W(\mathbf{r}, \mathbf{r}^{\prime}) \approx \frac{1}{\epsilon_{\infty}} v(\mathbf{r}, \mathbf{r}^{\prime}).\qquad(12)
$$

Inserting Eq. (12) in Eqs. (9) and (10) yields the following expressions for COH and SEX:
$$
\Sigma_{\mathrm{COH}}(\mathbf{r}, \mathbf{r}^{\prime}) \approx-\left(1-\epsilon_{\infty}^{-1}\right) \frac{1}{2} \delta\left(\mathbf{r}-\mathbf{r}^{\prime}\right) v(\mathbf{r}, \mathbf{r}^{\prime}),\qquad(13)
$$

$$
\Sigma_{\mathrm{SEX}}(\mathbf{r}, \mathbf{r}^{\prime}) \approx-\epsilon_{\infty}^{-1} \sum_{i=1}^{\mathrm{N}_{\mathrm{occ}}} \phi_{i}(\mathbf{r}) \phi_{i}^{*}(\mathbf{r}^{\prime}) v(\mathbf{r}, \mathbf{r}^{\prime}).\qquad(14)
$$

We may now compare the exchange-correlation potential of Eq. (7) and the electron self-energy of Eq. (8) using the simplified expressions for COH and SEX given by Eqs. (13) and (14). If $\alpha=\epsilon_{\infty}^{-1}$ is chosen, the prefactors of the local and nonlocal exchange potentials in Eq. (7) are the same as those of the corresponding local and nonlocal self-energies in Eqs. (13) and (14), respectively. Hence through simplifications of the many-body self-energy, Eq. (8), we obtain $\alpha=1 / \epsilon_{\infty}$. We also note that the equivalence between Eq. (7) and Eqs. (13) and (14) holds exactly for the nonlocal terms where the exact exchange is present in both; the local operator arising from the COH part is expressed in Eq. (7) using a local/semilocal form. A similar proportionality between $\alpha$ and $\epsilon_{\infty}^{-1}$ was derived from many-body perturbation theory to study the polarizability of semiconductors in the framework of time-dependent DFT, where $\alpha$ was used to statically screen the long-range contribution to the exchange-correlation kernel in the polarizability, but without introducing a nonlocal potential in the Hamiltonian [33].

The use of the static electronic dielectric constant $(\epsilon_{\infty})$ to represent the effective screening of the exact-exchange potential in nonmetallic condensed systems has been previously suggested by several authors [31,34,35]. Marques *et al.* [31] evaluated $\epsilon_{\infty}$ at the semilocal Perdew-Burke-Ernzerhof (PBE) level of theory and set $\alpha=1 / \epsilon_{\infty}^{\mathrm{PBE}}$ using a full-range hybrid functional. Building upon previous work on range-separated hybrid functionals for molecules, Refaely-Abramson *et al.* [35] determined the static dielectric constant from the full dielectric response function in the random phase approximation (RPA). The results of both Refs. [31] and [35] showed a considerable improvement in computed electronic energy gaps over semilocal and hybrid functionals. Despite properly describing the correct long-range asymptotic limit, the accuracy of the prefactors used in Refs. [31] and [35] may be affected by the level of theory (PBE) or the approximations employed for the evaluation of the polarizability (RPA).

Using both a full-range and a short-range screened hybrid functional, Shimazaki and Asai [36,37] self-consistently evaluated $\alpha=\epsilon_{\infty}^{-1}$ by using a Penn model for the static dielectric constant.[38] Koller *et al.* [39] also reported a self-consistent short-range hybrid functional with the short-range mixing parameter dependent on the static dielectric constant. The latter was evaluated without including the density response to the perturbing external electric field (no local-field effects); an empirical fit was utilized to set the relation between $\alpha$ and $\epsilon_{\infty}$, resulting in considerable errors $(\sim 30 \%)$ in the computed macroscopic dielectric constants. The self-consistent hybrid implementations of Refs. [36] and [39] used approximate methods for the polarizability, which may have affected the overall accuracy of the procedure.

SELF-CONSISTENT HYBRID FUNCTIONAL FOR . . .

In this work we present a full-range, nonempirical hybrid functional where the mixing parameter $\alpha$ is determined self-consistently from the evaluation of the inverse static electronic dielectric constant $\epsilon_{\infty}^{-1}$. The latter is computed by including the full response of the electronic density to the perturbing external electric field, i.e., local-field effects are included, which are important to obtain accurate results. We computed the dielectric constants, electronic gaps, and several lattice constants of a broad class of solids and found results in considerably better agreement with experiments than those obtained with semilocal and the PBE0 hybrid functional.

The rest of the paper is organized as follows. Section II describes the methodology along with the computational details. Section III presents results obtained using a self-consistent (sc) hybrid. Section IV summarizes the present self-consistent hybrid scheme and concludes with future directions to explore.

## II. METHODS

### A. Self-consistent hybrid mixing scheme (sc-hybrid)

The self-consistent cycle used to determine the sc-hybrid functional proposed in this work is shown in Fig. 1. The self-consistency loop is started with an initial guess for $\alpha$, which is bound to range from 0 to 1; $\alpha$ determines the amount of exact exchange $v_{x}^{\text{ex}}(\mathbf{r},\mathbf{r}')$ included in the exchangecorrelation potential expression of Eq. (7). In this work we used the GGA exchange and correlation functional proposed by Perdew, Burke, and Ernzerhof (PBE) [40]; hence in Fig. 1 $v_{x}(\mathbf{r})$ denotes the PBE exchange functional. Once the hybrid exchange potential is defined, $\epsilon_{\infty}$ is computed self-consistently using the procedure outlined in Sec. II B and convergence is assessed by comparing $\epsilon_{\infty}$ evaluated in subsequent cycles.

As an initial guess for $\alpha$, we used both the value that reproduces the semilocal-only PBE limit ($\alpha=0$) and the value $\alpha=0.25$ corresponding to the global hybrid PBE0. Figure 2 illustrates how the self-consistent procedure of Fig. 1 leads to the same converged electronic dielectric constant, regardless of the initial value of $\alpha$, either PBE (sc-hybrid@PBE, blue dashed line and triangles) or PBE0 (sc-hybrid@PBE0, red solid line and circles). Generally only three to four iterations are required to reach convergence [41] with the only notable exceptions being the antiferromagnetic transition metal oxides CoO, MnO, and NiO, which respectively required five, five, and nine iterations to reach convergence.

![](./images/813141830911655938_1.jpg)

FIG. 1. (Color online) Diagram of the self-consistent hybrid scheme. The potential used in the solution of the generalized Kohn-Sham equation is defined in Eq. (7). $\epsilon_{\infty}$ is the static dielectric constant.

![](./images/813141830911655938_2.jpg)

FIG. 2. (Color online) Convergence of the value of the static dielectric constant $\varepsilon_{\infty}$ in the sc-hybrid scheme is shown for four prototypical semiconductors, Si, C, SiC, and Ge. The blue dashed line and triangles indicate the iterative procedure that starts with no inclusion of exact exchange: $\alpha=0$ (sc-hybrid@PBE); the red solid line and circles correspond to the iterative procedure started with a quarter of exact exchange $\alpha=0.25$ (sc-hybrid@PBE0). The blue and red arrows shown in the first panel indicate the PBE and PBE0 values of $\epsilon_{\infty}$. The solid black lines represent the value of the experimental macroscopic dielectric constant.

### B. Evaluation of the static dielectric constant

The static dielectric constant is the central quantity in the sc-hybrid scheme and its accurate computation is critical for the performance of our approach. It is therefore useful to briefly recall the techniques and the levels of approximation that are usually employed in evaluating $\epsilon_{\infty}$.

We consider the dielectric response of a system subject to a macroscopic electric field $\mathbf{E}_{\text{ext}}$, where the total potential acting on the system $v_{\text{tot}}$ includes both the perturbing macroscopic potential $v_{\text{macro}}=e\mathbf{r}\cdot\mathbf{E}_{\text{ext}}$, and the self-consistent generalized Kohn-Sham electronic potential $v_{\text{GKS}}$:
$$
v_{\text{tot}}=v_{\text{GKS}}+v_{\text{macro}}. \tag{15}
$$

The dielectric response to an external field may be computed using finite field methods, e.g., the Berry phase technique (known as the modern theory of polarization) [42,43], or firstorder perturbation theory, which is our method of choice in the present work. Within linear response, both density functional perturbation theory (DFPT) [44] and the coupled perturbed Kohn-Sham (CPKS) [45,46] equations [the coupled-perturbed Hartree-Fock method (CPHF) [47–49] extended to DFT] have been commonly employed to compute the macroscopic dielectric constants of solids. In this work we computed the dielectric constants using the CPKS method as implemented in CRYSTAL09 [50], where the perturbed KS orbitals are obtained

TABLE I. The electronic dielectric constant ($\epsilon_\infty$) determined using several levels of theory. The hybrid heading with $\alpha = 1/\epsilon_\infty^{\text{PBE}}$ refers to a hybrid calculation using $\alpha = 1/\epsilon_\infty$, where the dielectric constant was evaluated at the PBE level of theory. Similarly, the hybrid heading with $\alpha = 1/\epsilon_\infty^{\text{PBE0}}$ refers to a hybrid calculation where the dielectric constant was evaluated at the PBE0 level of theory. The sc-hybrid heading refers to hybrid calculations where the fraction of exact exchange is self-consistently determined from the dielectric constant. All local-field effects are included in the evaluation of the dielectric constant so that all $\epsilon_\infty$ hybrid function entries in the table are at the level of RPA + $f_{\text{sc--nl}}$. ME, MAE, MRE, and MARE are the mean, mean absolute, mean relative, and mean absolute relative error, respectively. The experimental geometry was used for each solid, with the structure or polytype indicated by the abbreviation in the second column: dC-diamond cubic; RS-rock salt cubic structure; ZB-zinc blende; M-monoclinic; Ru-rutile; WZ-wurtzite; Cr-corundum; XI-the XI proton ordered phase of ice; and cF-fcc, face-centered cubic. Note that CoO, NiO, and MnO are magnetic with AFM-II magnetic ordering.

<table>
<thead>
<tr>
<th></th>
<th></th>
<th>PBE</th>
<th>PBE0</th>
<th>hybrid</th>
<th>hybrid</th>
<th>sc-hybrid</th>
<th></th>
</tr>
<tr>
<th></th>
<th>Type</th>
<th>$\alpha = 0$</th>
<th>$\alpha = 0.25$</th>
<th>$\alpha = 1/\epsilon_\infty^{\text{PBE}}$</th>
<th>$\alpha = 1/\epsilon_\infty^{\text{PBE0}}$</th>
<th>$\alpha = 1/\text{sc-}\epsilon_\infty$</th>
<th>Exp.</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ge</td>
<td>(dC)</td>
<td>–</td>
<td>12.77</td>
<td>–</td>
<td>15.33</td>
<td>15.65</td>
<td>15.9 [66]</td>
</tr>
<tr>
<td>Si</td>
<td>(dC)</td>
<td>12.62</td>
<td>10.53</td>
<td>11.81</td>
<td>11.67</td>
<td>11.76</td>
<td>11.9 [67]</td>
</tr>
<tr>
<td>AlP</td>
<td>(ZB)</td>
<td>7.82</td>
<td>6.85</td>
<td>7.26</td>
<td>7.20</td>
<td>7.23</td>
<td>7.54 [67]</td>
</tr>
<tr>
<td>SiC</td>
<td>(ZB)</td>
<td>6.94</td>
<td>6.28</td>
<td>6.53</td>
<td>6.49</td>
<td>6.50</td>
<td>6.52 [67]</td>
</tr>
<tr>
<td>TiO₂</td>
<td>(Ru)</td>
<td>7.91</td>
<td>5.96</td>
<td>6.75</td>
<td>6.46</td>
<td>6.56</td>
<td>6.34 [68]</td>
</tr>
<tr>
<td>NiO</td>
<td>(RS)</td>
<td>16.98</td>
<td>4.74</td>
<td>9.20</td>
<td>5.12</td>
<td>5.49</td>
<td>5.76 [69]</td>
</tr>
<tr>
<td>C</td>
<td>(dC)</td>
<td>5.83</td>
<td>5.54</td>
<td>5.61</td>
<td>5.61</td>
<td>5.61</td>
<td>5.70 [67]</td>
</tr>
<tr>
<td>CoO</td>
<td>(RS)</td>
<td>–</td>
<td>4.52</td>
<td>–</td>
<td>4.73</td>
<td>4.92</td>
<td>5.35 [69]</td>
</tr>
<tr>
<td>GaN</td>
<td>(ZB)</td>
<td>5.78</td>
<td>5.00</td>
<td>5.19</td>
<td>5.12</td>
<td>5.14</td>
<td>5.30 [70]</td>
</tr>
<tr>
<td>ZnS</td>
<td>(ZB)</td>
<td>5.58</td>
<td>4.84</td>
<td>5.01</td>
<td>4.94</td>
<td>4.95</td>
<td>5.13 [67]</td>
</tr>
<tr>
<td>MnO</td>
<td>(RS)</td>
<td>7.62</td>
<td>4.32</td>
<td>5.11</td>
<td>4.41</td>
<td>4.45</td>
<td>4.95 [71]</td>
</tr>
<tr>
<td>WO₃</td>
<td>(M)</td>
<td>5.46</td>
<td>4.60</td>
<td>4.79</td>
<td>4.68</td>
<td>4.72</td>
<td>4.81 [72]</td>
</tr>
<tr>
<td>BN</td>
<td>(ZB)</td>
<td>4.59</td>
<td>4.37</td>
<td>4.40</td>
<td>4.39</td>
<td>4.40</td>
<td>4.50 [73]</td>
</tr>
<tr>
<td>HfO₂</td>
<td>(M)</td>
<td>4.54</td>
<td>3.97</td>
<td>4.03</td>
<td>3.97</td>
<td>3.97</td>
<td>4.41 [74]</td>
</tr>
<tr>
<td>AlN</td>
<td>(WZ)</td>
<td>4.54</td>
<td>4.15</td>
<td>4.18</td>
<td>4.16</td>
<td>4.16</td>
<td>4.18 [75]</td>
</tr>
<tr>
<td>ZnO</td>
<td>(WZ)</td>
<td>4.66</td>
<td>3.54</td>
<td>3.63</td>
<td>3.47</td>
<td>3.46</td>
<td>3.74 [76]</td>
</tr>
<tr>
<td>Al₂O₃</td>
<td>(Cr)</td>
<td>3.27</td>
<td>3.07</td>
<td>3.03</td>
<td>3.01</td>
<td>3.01</td>
<td>3.10 [77]</td>
</tr>
<tr>
<td>MgO</td>
<td>(RS)</td>
<td>3.12</td>
<td>2.89</td>
<td>2.83</td>
<td>2.81</td>
<td>2.81</td>
<td>2.96 [78]</td>
</tr>
<tr>
<td>LiCl</td>
<td>(RS)</td>
<td>2.96</td>
<td>2.82</td>
<td>2.78</td>
<td>2.77</td>
<td>2.77</td>
<td>2.70 [66]</td>
</tr>
<tr>
<td>NaCl</td>
<td>(RS)</td>
<td>2.49</td>
<td>2.37</td>
<td>2.31</td>
<td>2.30</td>
<td>2.29</td>
<td>2.40 [79]</td>
</tr>
<tr>
<td>LiF</td>
<td>(RS)</td>
<td>1.97</td>
<td>1.87</td>
<td>1.79</td>
<td>1.78</td>
<td>1.77</td>
<td>1.90 [66]</td>
</tr>
<tr>
<td>H₂O</td>
<td>(XI)</td>
<td>1.80</td>
<td>1.73</td>
<td>1.66</td>
<td>1.65</td>
<td>1.65</td>
<td>1.72 [80]</td>
</tr>
<tr>
<td>Ar</td>
<td>(cF)</td>
<td>1.74</td>
<td>1.70</td>
<td>1.66</td>
<td>1.66</td>
<td>1.66</td>
<td>1.66 [81]</td>
</tr>
<tr>
<td>Ne</td>
<td>(cF)</td>
<td>1.28</td>
<td>1.24</td>
<td>1.21</td>
<td>1.21</td>
<td>1.21</td>
<td>1.23 [82]</td>
</tr>
<tr>
<td>ME</td>
<td></td>
<td>0.96</td>
<td>–0.41</td>
<td>0.13</td>
<td>–0.20</td>
<td>–0.15</td>
<td>–</td>
</tr>
<tr>
<td>MAE</td>
<td></td>
<td>0.96</td>
<td>0.43</td>
<td>0.27</td>
<td>0.22</td>
<td>0.18</td>
<td>–</td>
</tr>
<tr>
<td>MRE (%)</td>
<td></td>
<td>18.5</td>
<td>–5.1</td>
<td>1.4</td>
<td>–3.8</td>
<td>–3.1</td>
<td>–</td>
</tr>
<tr>
<td>MARE (%)</td>
<td></td>
<td>18.5</td>
<td>6.2</td>
<td>5.6</td>
<td>4.5</td>
<td>4.0</td>
<td>–</td>
</tr>
</tbody>
</table>

using the potential of Eq. (15). The $v_{\text{GKS}}$ potential implicitly depends on the applied electric field through the perturbed charge density and orbitals. The perturbation of the equilibrium charge density caused by the presence of the external field is related to $v_{\text{macro}}$ by the reducible polarizability $\chi$:

$$
n_{\text{ind}}(\mathbf{r}) = \int \chi(\mathbf{r},\mathbf{r}')v_{\text{macro}}(\mathbf{r}')d\mathbf{r}'. \tag{16}
$$

$\chi$ is a nonlocal operator that describes the many-body polarization effects of the interacting electron gas. The polarizability $\chi$ may include retardation effects, giving rise to a frequency dependence of the dielectric tensor. Such dependence is not considered in the present work since we focus on the evaluation of the static dielectric screening. The static dielectric tensor $\epsilon_{ij}^{-1}$ can be expressed in terms of $\chi$ [51]:

$$
\epsilon_{ij}^{-1} = \delta_{ij} + \frac{4\pi e^2}{\Omega} \int d\mathbf{r} \int d\mathbf{r}' r_i \chi(\mathbf{r},\mathbf{r}') r_j', \tag{17}
$$

where $i,j$ denote Cartesian components and $\Omega$ is the volume of the cell. This result can be derived by relating the external electric field $\mathbf{E}_{\text{ext}}$ to the total electric field $\mathbf{E} = \mathbf{E}_{\text{ext}} - 4\pi \mathbf{P}$ and by computing the induced polarization field $\mathbf{P}$ by integrating the induced charge density

$$
\mathbf{P} = \frac{-e}{\Omega} \int n_{\text{ind}}(\mathbf{r})\mathbf{r}d\mathbf{r}. \tag{18}
$$

The approximations adopted in the computation of the static dielectric constant arise from the approximation chosen for $\chi$ in Eq. (17):

$$
\begin{aligned}
\chi & = \chi_0 + \chi_0 \frac{\delta v_{\text{GKS}}}{\delta n} \chi_0 + \chi_0 \frac{\delta v_{\text{GKS}}}{\delta n} \chi_0 \frac{\delta v_{\text{GKS}}}{\delta n} \chi_0 + \cdots \\
& = \chi_0 + \chi_0 \frac{\delta v_{\text{GKS}}}{\delta n} \chi, \tag{19}
\end{aligned}
$$

where $\chi_0$ is the irreducible polarizability [52]. The reducible and irreducible polarizabilities are also called interacting

TABLE II. The electronic dielectric constant evaluated using the sc-hybrid functional scheme is compared with results obtained from many-body perturbation theory. The scGW (e-h) calculations [84] used the HSE hybrid functional eigenvalues and orbitals as input, and the $G_0W_0$ (RPA) calculations [83] used the PBE functional eigenvalues and orbitals as input. The sc-hybrid (NLF) heading refers to a hybrid calculation where the uncoupled-perturbed Kohn-Sham equation is used, resulting in no inclusion of the local-field effects. The sc-hybrid (RPA $+f_{xc-nl}$) heading refers to a sc-hybrid calculation where the polarizability includes all local-field effects. ME, MAE, MRE, and MARE are the mean, mean absolute, mean relative, and mean absolute relative error, respectively. The experimental geometry was used for each solid, with the structure or polytype used indicated in Table I.

<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="2">sc-hybrid</th>
      <th rowspan="2">$G_0W_0$ [83] (RPA)</th>
      <th rowspan="2">scGW [84] (e-h)</th>
      <th rowspan="2">Exp.</th>
    </tr>
    <tr>
      <th>(NLF)</th>
      <th>(RPA $+f_{xc-nl}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ge</th>
      <td>15.05</td>
      <td>15.65</td>
      <td>–</td>
      <td>15.30</td>
      <td>15.9</td>
    </tr>
    <tr>
      <th>Si</th>
      <td>11.24</td>
      <td>11.76</td>
      <td>12.09</td>
      <td>11.40</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>AlP</th>
      <td>6.91</td>
      <td>7.23</td>
      <td>7.53</td>
      <td>7.11</td>
      <td>7.54</td>
    </tr>
    <tr>
      <th>SiC</th>
      <td>5.96</td>
      <td>6.50</td>
      <td>6.56</td>
      <td>6.48</td>
      <td>6.52</td>
    </tr>
    <tr>
      <th>C</th>
      <td>5.08</td>
      <td>5.61</td>
      <td>5.54</td>
      <td>5.59</td>
      <td>5.70</td>
    </tr>
    <tr>
      <th>GaN</th>
      <td>4.49</td>
      <td>5.14</td>
      <td>5.68</td>
      <td>5.35</td>
      <td>5.30</td>
    </tr>
    <tr>
      <th>ZnS</th>
      <td>4.54</td>
      <td>4.95</td>
      <td>5.62</td>
      <td>5.15</td>
      <td>5.13</td>
    </tr>
    <tr>
      <th>BN</th>
      <td>3.93</td>
      <td>4.40</td>
      <td>4.30</td>
      <td>4.43</td>
      <td>4.50</td>
    </tr>
    <tr>
      <th>ZnO</th>
      <td>2.89</td>
      <td>3.46</td>
      <td>5.12</td>
      <td>3.78</td>
      <td>3.74</td>
    </tr>
    <tr>
      <th>MgO</th>
      <td>2.42</td>
      <td>2.81</td>
      <td>2.99</td>
      <td>2.96</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>LiF</th>
      <td>–</td>
      <td>1.77</td>
      <td>1.96</td>
      <td>1.98</td>
      <td>1.90</td>
    </tr>
    <tr>
      <th>Ar</th>
      <td>1.60</td>
      <td>1.66</td>
      <td>1.66</td>
      <td>1.69</td>
      <td>1.66</td>
    </tr>
    <tr>
      <th>Ne</th>
      <td>1.17</td>
      <td>1.21</td>
      <td>1.25</td>
      <td>1.23</td>
      <td>1.23</td>
    </tr>
    <tr>
      <th>ME</th>
      <td>–0.57</td>
      <td>–0.14</td>
      <td>0.19</td>
      <td>–0.12</td>
      <td>–</td>
    </tr>
    <tr>
      <th>MAE</th>
      <td>0.57</td>
      <td>0.14</td>
      <td>0.25</td>
      <td>0.15</td>
      <td>–</td>
    </tr>
    <tr>
      <th>MRE (%)</th>
      <td>–10.7</td>
      <td>–3.0</td>
      <td>4.5</td>
      <td>–0.7</td>
      <td>–</td>
    </tr>
    <tr>
      <th>MARE (%)</th>
      <td>10.7</td>
      <td>3.0</td>
      <td>5.8</td>
      <td>2.0</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

and noninteracting density-density response functions, respectively [53]. The difference between $\chi$ and $\chi_0$ is given by so-called local-field effects [54,55], defined by the functional derivative $\frac{\delta v_{\text{GKS}}}{\delta n}$, which is the sum of the functional derivative of the Hartree and exchange-correlation potential with respect to the density:
$$
\frac{\delta v_{\mathrm{GKS}}}{\delta n}=\frac{\delta v_{H}}{\delta n}+\frac{\delta v_{\mathrm{xc}}}{\delta n},\qquad(20)
$$
where $\frac{\delta v_{\mathrm{xc}}}{\delta n} \equiv f_{\mathrm{xc}}$. If local fields are neglected (NLF, i.e., no local fields), $\frac{\delta v_{\mathrm{GKS}}}{\delta n}=0$ and the polarizability is equal to the irreducible polarizability
$$
\chi^{\mathrm{NLF}}=\chi_{0}.\qquad(21)
$$

$\chi_0$ can then be computed in the independent particle approximation (IPA), which assumes the electron-hole (e-h) interactions are negligible [56]. This approximation is formally equivalent to the one adopted for the calculation of $\epsilon_\infty$ by Koller *et al.* [39], who used the Fermi's golden rule to compute the frequency-dependent imaginary part of the dielectric screening, and the Kramers-Kronig relation to derive the static dielectric constant.

If only the Hartree term is included in Eq. (20) and the derivative of the exchange-correlation potential is set to zero ($f_{\mathrm{xc}}=0$), one obtains the RPA for the polarizability:
$$
\chi^{\mathrm{RPA}}=\left[1-\chi_{0} v\right]^{-1} \chi_{0}.\qquad(22)
$$

If both the Hartree and the exchange-correlation terms are included in Eq. (20), one obtains RPA $+f_{\mathrm{xc}}$ [57]. In linear response calculations of the dielectric screening with nonlocal operators in the KS potential, the functional derivative of $v_{\mathrm{xc}}$ with respect to the density is usually neglected; the resulting, approximate $f_{\mathrm{xc}}$ is denoted as $f_{\mathrm{xc}-l}$. If the functional derivative of the nonlocal operator is instead included, $f_{\mathrm{xc}}$ is denoted as $f_{\mathrm{xc-nl}}$. We note that when using local/semilocal functionals, the exchange-correlation potential entering $f_{\mathrm{xc}}$ depends explicitly on the density and its functional derivative may be readily evaluated; its inclusion in the calculation of the polarizability for some semiconductors and insulators was previously observed to be negligible [57]. However, nonlocal exchange-correlation potentials, e.g., derived from hybrid functionals, depend implicitly on the density through the KS orbitals and their functional derivative is not straightforward to compute. Within the CPKS method, this difficulty is overcome by calculating explicitly the perturbed orbitals and using them to evaluate the linear variation of the exact exchange with respect to the single-particle wave functions; hence, within the CPKS scheme, local-field effects are easily included [58].

The importance of including nonlocal contributions to $f_{\mathrm{xc}}$ in the calculation of band gaps of some semiconductors and insulators was pointed out by Paier *et al.* [57], following the suggestion of Bruneval *et al.* [59]; these authors derived $f_{\mathrm{xc}}$ from many-body perturbation theory and related it to the inclusion of e-h interactions in the many-body calculations of $\chi_0$, beyond the IPA.

Finally, we note that the CPKS scheme adopted here is efficient when used in conjunction with moderate size basis sets, e.g., the Gaussian basis sets we used with CRYSTAL09. However, this would be less practical when plane-wave basis

TABLE III. The calculated electronic dielectric tensor components for the optically anisotropic wurtzite phases of ZnO, AlN, and GaN are shown and compared with their respective experimental values.

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">ZnO</th>
      <th colspan="2">AlN</th>
      <th colspan="2">GaN</th>
    </tr>
    <tr>
      <th></th>
      <th>$\epsilon_\perp(\infty)$</th>
      <th>$\epsilon_\parallel(\infty)$</th>
      <th>$\epsilon_\perp(\infty)$</th>
      <th>$\epsilon_\parallel(\infty)$</th>
      <th>$\epsilon_\perp(\infty)$</th>
      <th>$\epsilon_\parallel(\infty)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PBE</th>
      <td>4.64</td>
      <td>4.68</td>
      <td>4.46</td>
      <td>4.69</td>
      <td>5.55</td>
      <td>5.72</td>
    </tr>
    <tr>
      <th>PBE0</th>
      <td>3.53</td>
      <td>3.57</td>
      <td>4.10</td>
      <td>4.27</td>
      <td>4.86</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>sc-hybrid</th>
      <td>3.45</td>
      <td>3.48</td>
      <td>4.10</td>
      <td>4.27</td>
      <td>4.99</td>
      <td>5.13</td>
    </tr>
    <tr>
      <th>Experiment [75,76]</th>
      <td>$3.70\pm0.01$</td>
      <td>$3.78\pm0.05$</td>
      <td>$4.13\pm0.02$</td>
      <td>$4.27\pm0.05$</td>
      <td>$5.18\pm0.02$</td>
      <td>$5.31\pm0.06$</td>
    </tr>
  </tbody>
</table>

TABLE IV. The Kohn-Sham (KS) energy gaps (eV) evaluated with the dielectric-dependent hybrid functionals are compared with the experimental electronic gaps for a wide range of materials. The experimental values correspond to either photoemission measurements or to optical measurements where the excitonic contributions were removed, with alumina the only exception (see text). The KS gaps were computed as the energy difference of the single-particle energies of the conduction band minimum and the valence band maximum. The solids are listed in the order of largest to smallest experimental $\epsilon_\infty$. The hybrid heading with $\alpha = 1/\epsilon_\infty^{\text{PBE}}$ refers to a hybrid calculation using a fixed $\alpha$ with the dielectric constant evaluated at the PBE level of theory. Similarly, the hybrid heading with $\alpha = 1/\epsilon_\infty^{\text{PBE0}}$ refers to a hybrid calculation with a fixed $\alpha$ and the dielectric constant evaluated at the PBE0 level of theory. The sc-hybrid heading refers to the hybrid calculation where the fraction of exact exchange is determined self-consistently from $\epsilon_\infty$. ME, MAE, MRE, and MARE are the mean, absolute, mean relative, and mean absolute relative error, respectively. The experimental geometry was used in all calculations, with the structure or polytype indicated in the second column: dC-diamond cubic; RS-rock salt cubic structure; ZB-zinc blende; M-monoclinic; Ru-rutile; WZ-wurtzite; Cr-corundum; XI-the XI proton ordered phase of ice; cF-fcc, face-centered cubic. Note that CoO, NiO, and MnO are magnetic with AFM-II magnetic ordering.

<table>
  <thead>
    <tr>
      <th></th>
      <th rowspan="2">Type</th>
      <th>PBE</th>
      <th>PBE0</th>
      <th>hybrid</th>
      <th>hybrid</th>
      <th>sc-hybrid</th>
      <th rowspan="2">Exp.</th>
    </tr>
    <tr>
      <th></th>
      <th>$\alpha = 0$</th>
      <th>$\alpha = 0.25$</th>
      <th>$\alpha = 1/\epsilon_\infty^{\text{PBE}}$</th>
      <th>$\alpha = 1/\epsilon_\infty^{\text{PBE0}}$</th>
      <th>$\alpha = 1/\text{sc-}\epsilon_\infty$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ge</td>
      <td>(dC)</td>
      <td>0.00</td>
      <td>1.53</td>
      <td>–</td>
      <td>0.77</td>
      <td>0.71</td>
      <td>0.74 [85]</td>
    </tr>
    <tr>
      <td>Si</td>
      <td>(dC)</td>
      <td>0.62</td>
      <td>1.75</td>
      <td>0.96</td>
      <td>1.03</td>
      <td>0.99</td>
      <td>1.17 [85]</td>
    </tr>
    <tr>
      <td>AlP</td>
      <td>(ZB)</td>
      <td>1.64</td>
      <td>2.98</td>
      <td>2.31</td>
      <td>2.41</td>
      <td>2.37</td>
      <td>2.51 [86]</td>
    </tr>
    <tr>
      <td>SiC</td>
      <td>(ZB)</td>
      <td>1.37</td>
      <td>2.91</td>
      <td>2.23</td>
      <td>2.33</td>
      <td>2.29</td>
      <td>2.39 [87]</td>
    </tr>
    <tr>
      <td>TiO₂</td>
      <td>(Ru)</td>
      <td>1.81</td>
      <td>3.92</td>
      <td>2.83</td>
      <td>3.18</td>
      <td>3.05</td>
      <td>3.3 [88]</td>
    </tr>
    <tr>
      <td>NiO</td>
      <td>(RS)</td>
      <td>0.97</td>
      <td>5.28</td>
      <td>2.00</td>
      <td>4.61</td>
      <td>4.11</td>
      <td>4.3 [89]</td>
    </tr>
    <tr>
      <td>C</td>
      <td>(dC)</td>
      <td>4.15</td>
      <td>5.95</td>
      <td>5.37</td>
      <td>5.44</td>
      <td>5.42</td>
      <td>5.48 [90]</td>
    </tr>
    <tr>
      <td>CoO</td>
      <td>(RS)</td>
      <td>0.00</td>
      <td>4.53</td>
      <td>–</td>
      <td>4.01</td>
      <td>3.62</td>
      <td>2.5 [91]</td>
    </tr>
    <tr>
      <td>GaN</td>
      <td>(ZB)</td>
      <td>1.88</td>
      <td>3.68</td>
      <td>3.10</td>
      <td>3.30</td>
      <td>3.26</td>
      <td>3.29 [92]</td>
    </tr>
    <tr>
      <td>ZnS</td>
      <td>(ZB)</td>
      <td>2.36</td>
      <td>4.18</td>
      <td>3.65</td>
      <td>3.85</td>
      <td>3.82</td>
      <td>3.91 [85]</td>
    </tr>
    <tr>
      <td>MnO</td>
      <td>(RS)</td>
      <td>1.12</td>
      <td>3.87</td>
      <td>2.55</td>
      <td>3.66</td>
      <td>3.60</td>
      <td>3.9 [93]</td>
    </tr>
    <tr>
      <td>WO₃</td>
      <td>(M)</td>
      <td>1.92</td>
      <td>3.79</td>
      <td>3.24</td>
      <td>3.50</td>
      <td>3.47</td>
      <td>3.38 [94]</td>
    </tr>
    <tr>
      <td>BN</td>
      <td>(ZB)</td>
      <td>4.49</td>
      <td>6.51</td>
      <td>6.24</td>
      <td>6.34</td>
      <td>6.33</td>
      <td>6.25 [95]ᵃ</td>
    </tr>
    <tr>
      <td>HfO₂</td>
      <td>(M)</td>
      <td>4.32</td>
      <td>6.65</td>
      <td>6.38</td>
      <td>6.68</td>
      <td>6.68</td>
      <td>5.84 [96]</td>
    </tr>
    <tr>
      <td>AlN</td>
      <td>(WZ)</td>
      <td>4.33</td>
      <td>6.31</td>
      <td>6.07</td>
      <td>6.24</td>
      <td>6.23</td>
      <td>6.28 [97]</td>
    </tr>
    <tr>
      <td>ZnO</td>
      <td>(WZ)</td>
      <td>1.07</td>
      <td>3.41</td>
      <td>3.06</td>
      <td>3.73</td>
      <td>3.78</td>
      <td>3.44 [98]</td>
    </tr>
    <tr>
      <td>Al₂O₃</td>
      <td>(Cr)</td>
      <td>6.31</td>
      <td>8.84</td>
      <td>9.42</td>
      <td>9.65</td>
      <td>9.71</td>
      <td>8.8 [99]</td>
    </tr>
    <tr>
      <td>MgO</td>
      <td>(RS)</td>
      <td>4.80</td>
      <td>7.25</td>
      <td>7.97</td>
      <td>8.24</td>
      <td>8.33</td>
      <td>7.83 [100]</td>
    </tr>
    <tr>
      <td>LiCl</td>
      <td>(RS)</td>
      <td>6.54</td>
      <td>8.66</td>
      <td>9.42</td>
      <td>9.57</td>
      <td>9.62</td>
      <td>9.4 [101]</td>
    </tr>
    <tr>
      <td>NaCl</td>
      <td>(RS)</td>
      <td>5.18</td>
      <td>7.26</td>
      <td>8.55</td>
      <td>8.73</td>
      <td>8.84</td>
      <td>8.6 [102]</td>
    </tr>
    <tr>
      <td>LiF</td>
      <td>(RS)</td>
      <td>9.21</td>
      <td>12.28</td>
      <td>15.48</td>
      <td>15.83</td>
      <td>16.15</td>
      <td>14.2 [103]</td>
    </tr>
    <tr>
      <td>H₂O</td>
      <td>(XI)</td>
      <td>5.57</td>
      <td>8.05</td>
      <td>11.19</td>
      <td>11.44</td>
      <td>11.71</td>
      <td>10.9 [104]</td>
    </tr>
    <tr>
      <td>Ar</td>
      <td>(cF)</td>
      <td>8.78</td>
      <td>11.20</td>
      <td>14.40</td>
      <td>14.54</td>
      <td>14.67</td>
      <td>14.2 [105]</td>
    </tr>
    <tr>
      <td>Ne</td>
      <td>(cF)</td>
      <td>11.65</td>
      <td>15.20</td>
      <td>23.32</td>
      <td>22.99</td>
      <td>23.67</td>
      <td>21.7 [105]</td>
    </tr>
    <tr>
      <td colspan="2">ME (eV)</td>
      <td>–2.7</td>
      <td>–0.3</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>0.3</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="2">MAE (eV)</td>
      <td>2.67</td>
      <td>1.08</td>
      <td>0.5</td>
      <td>0.4</td>
      <td>0.5</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="2">MRE (%)</td>
      <td>–46.9</td>
      <td>10.8</td>
      <td>–1.1</td>
      <td>4.9</td>
      <td>3.3</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="2">MARE (%)</td>
      <td>46.9</td>
      <td>21.1</td>
      <td>9.6</td>
      <td>7.4</td>
      <td>7.8</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

ᵃThe experimental value used here is the average of two reported values 6.1 and 6.4 eV.

sets are employed. Within a plane-wave pseudopotential approach with hybrid functionals, one may, for example, evaluate the dielectric constant by applying the modern theory of polarization and computing derivatives with respect to the applied field by finite differences. In this way all local-field effects are automatically included [42,43].

### C. Computational details

All hybrid functional calculations were carried out within an all-electron approach using the CRYSTAL09 [50] electronic structure package. We thus avoided possible inconsistencies generated by the use of pseudopotentials derived within PBE for hybrid functional calculations. We used Gaussian basis sets modified starting from Ahlrichs' def2-TZVPP molecular basis [60], with the only exception being the rare gases Ne and Ar basis sets, which were modified starting from the def2-QZVPD set [61]. The highly contracted core shells were not modified, while the valence shells were modified, when necessary, to avoid possible linear dependencies caused by the use of diffuse functions, which are utilized in the case of molecules to represent the tail of the wave functions in the vacuum region. In particular, we constrained the most diffuse exponents to be larger than or equal to $0.09$ bohr$^{-2}$. In most cases, we kept the size of the valence shell basis set to be the same as that of the uncontracted original def2 sets by augmenting the truncated basis sets accordingly. The Gaussian basis functions added to the original set were chosen so as to

TABLE V. The Kohn-Sham (KS) energy gaps (eV) evaluated in the present work (see Table IV) and quasiparticle gaps from Refs. [83] and [84] are compared with the measured electronic gaps for a subset of semiconductors and insulators. Both the scGW (RPA) and scGW (e-h) calculations used the HSE hybrid functional eigenvalues and orbitals as input, and the $G_0W_0$ (RPA) calculations used the PBE functional eigenvalues and orbitals as input. The sc-hybrid (NLF) heading refers to a hybrid calculation where the uncoupled-perturbed Kohn-Sham equation was used, thus neglecting all local-field effects. The sc-hybrid (RPA $+f_{\text{xc-nl}}$) heading refers to a sc-hybrid calculation where the polarizability includes all local-field effects. MRE and MARE stands for the mean relative and the mean absolute relative error, respectively. The experimental geometry was used for each solid, with the structure or polytype indicated in Table IV.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">sc-hybrid</th>
<th>$G_0W_0$ [83]</th>
<th>scGW [84]</th>
<th>scGW [84]</th>
<th rowspan="2">Exp.</th>
</tr>
<tr>
<th>(NLF)</th>
<th>(RPA $+f_{\text{xc-nl}}$)</th>
<th>(RPA)</th>
<th>(RPA)</th>
<th>(e-h)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ge</td>
<td>0.72</td>
<td>0.71</td>
<td>–</td>
<td>0.95</td>
<td>0.81</td>
<td>0.74</td>
</tr>
<tr>
<td>Si</td>
<td>1.00</td>
<td>0.99</td>
<td>1.12</td>
<td>1.41</td>
<td>1.24</td>
<td>1.17</td>
</tr>
<tr>
<td>AlP</td>
<td>2.42</td>
<td>2.37</td>
<td>2.44</td>
<td>2.90</td>
<td>2.57</td>
<td>2.51</td>
</tr>
<tr>
<td>SiC</td>
<td>2.38</td>
<td>2.29</td>
<td>2.27</td>
<td>2.88</td>
<td>2.53</td>
<td>2.39</td>
</tr>
<tr>
<td>GaN</td>
<td>3.47</td>
<td>3.26</td>
<td>2.80</td>
<td>3.82</td>
<td>3.27</td>
<td>3.29</td>
</tr>
<tr>
<td>ZnO</td>
<td>4.35</td>
<td>3.78</td>
<td>2.12</td>
<td>3.8</td>
<td>3.2</td>
<td>3.44</td>
</tr>
<tr>
<td>ZnS</td>
<td>3.96</td>
<td>3.82</td>
<td>3.29</td>
<td>4.15</td>
<td>3.60</td>
<td>3.91</td>
</tr>
<tr>
<td>C</td>
<td>5.55</td>
<td>5.42</td>
<td>5.50</td>
<td>6.18</td>
<td>5.79</td>
<td>5.48</td>
</tr>
<tr>
<td>BN</td>
<td>6.55</td>
<td>6.33</td>
<td>6.10</td>
<td>7.14</td>
<td>6.59</td>
<td>6.25 a</td>
</tr>
<tr>
<td>MgO</td>
<td>8.93</td>
<td>8.33</td>
<td>7.25</td>
<td>9.16</td>
<td>8.12</td>
<td>7.83</td>
</tr>
<tr>
<td>LiF</td>
<td>–</td>
<td>16.15</td>
<td>13.27</td>
<td>15.9</td>
<td>14.5</td>
<td>14.2</td>
</tr>
<tr>
<td>Ar</td>
<td>14.88</td>
<td>14.67</td>
<td>13.28</td>
<td>14.9</td>
<td>13.9</td>
<td>14.2</td>
</tr>
<tr>
<td>Ne</td>
<td>24.05</td>
<td>23.67</td>
<td>19.59</td>
<td>22.1</td>
<td>21.4</td>
<td>21.7</td>
</tr>
<tr>
<td>ME (eV)</td>
<td>0.45</td>
<td>0.36</td>
<td>–0.58</td>
<td>0.63</td>
<td>0.03</td>
<td>–</td>
</tr>
<tr>
<td>MAE (eV)</td>
<td>0.49</td>
<td>0.46</td>
<td>0.58</td>
<td>0.63</td>
<td>0.21</td>
<td>–</td>
</tr>
<tr>
<td>MRE (%)</td>
<td>4.0</td>
<td>0.8</td>
<td>–9.4</td>
<td>13.9</td>
<td>1.6</td>
<td>–</td>
</tr>
<tr>
<td>MARE (%)</td>
<td>7.5</td>
<td>5.9</td>
<td>9.5</td>
<td>13.9</td>
<td>4.6</td>
<td>–</td>
</tr>
</tbody>
</table>

$^{\text{a}}$Denotes that the experimental value used here is the average of two reported values, 6.1 and 6.4 eV.

generate a basis set as even tempered as possible. The orbital exponents of the augmented uncontracted valence shells were variationally optimized for all solids in the current study using the GGA functional PBE.

We note that a much denser $k$-point mesh is required for the convergence of the electronic dielectric constants than for the ground-state energies and electronic energy gaps (see Supplemental Material [62]). In all calculations carried out with the sc-hybrid scheme, we used the $k$-point mesh required to converge $\epsilon_\infty$.

We also carried out plane-wave calculations at the GGA level of theory using the QUANTUM-ESPRESSO plane-wave pseudopotential package [63] to compare with the results of CRYSTAL09. We employed both the projector-augmented wave function (PAW) pseudopotentials and norm-conserving pseudopotentials, which were either generated using the ATOM-PAW program [64] or obtained from the QUANTUM-ESPRESSO pseudopotential library [65]. For the transition metal atoms, unless otherwise noted, the $(n-1)s$ and $(n-1)p$ electrons, where $n$ is the highest principle quantum number, were always included in the valence. A comparison of planewave pseudopotential and localized Gaussian basis set results can be found in the Supplemental Material [62].

With the exception of the lattice optimizations, all calculations were performed at the experimental geometry and $T=0$ K.

TABLE VI. The valence bandwidths (VBW, eV) are shown for a subset of the solids. For a description of the dielectric-dependent exact-exchange mixing scheme hybrid functional column headings see text and Table IV.

<table>
<thead>
<tr>
<th></th>
<th>PBE</th>
<th>PBE0</th>
<th>hybrid</th>
<th>hybrid</th>
<th>sc-hybrid</th>
<th rowspan="2">Exp.</th>
</tr>
<tr>
<th></th>
<th>$\alpha=0$</th>
<th>$\alpha=0.25$</th>
<th>$\alpha=1/\epsilon_\infty^{\text{PBE}}$</th>
<th>$\alpha=1/\epsilon_\infty^{\text{PBE0}}$</th>
<th>$\alpha=1/\text{sc-}\epsilon_\infty$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si</td>
<td>11.9</td>
<td>13.4</td>
<td>12.4</td>
<td>12.5</td>
<td>12.4</td>
<td>12.5 [107]</td>
</tr>
<tr>
<td>C</td>
<td>13.4</td>
<td>23.6</td>
<td>23.0</td>
<td>23.0</td>
<td>23.0</td>
<td>23.0 [108]</td>
</tr>
<tr>
<td>Ge</td>
<td>–</td>
<td>14.0</td>
<td>–</td>
<td>13.0</td>
<td>12.9</td>
<td>12.9 [107]</td>
</tr>
<tr>
<td>SiC</td>
<td>15.4</td>
<td>17.0</td>
<td>16.3</td>
<td>16.4</td>
<td>16.4</td>
<td>16.9 [109]a</td>
</tr>
<tr>
<td>LiF</td>
<td>3.1</td>
<td>3.3</td>
<td>3.3</td>
<td>3.4</td>
<td>3.4</td>
<td>3.5 [110]</td>
</tr>
<tr>
<td>MgO</td>
<td>4.6</td>
<td>5.0</td>
<td>5.1</td>
<td>5.2</td>
<td>5.2</td>
<td>4.8 [111]</td>
</tr>
<tr>
<td>ZnO</td>
<td>6.1</td>
<td>7.0</td>
<td>6.7</td>
<td>7.0</td>
<td>7.2</td>
<td>9.0 [98]</td>
</tr>
<tr>
<td>TiO₂</td>
<td>5.7</td>
<td>6.4</td>
<td>6.1</td>
<td>6.2</td>
<td>6.1</td>
<td>~6.0 [88]</td>
</tr>
</tbody>
</table>

$^{\text{a}}$The value listed for SiC in the last column is the VBW obtained from $G_0W_0$ calculations using the plasmon-pole approximation and a model dielectric function (within IPA).

<table>
<caption>TABLE VII. The $d$-band position relative to the valence band maximum (eV) is shown for a subset of solids with $d$ electrons. The $G_0W_0$ and $GW_0$ results, as well as the experimental values, are taken from Ref. [83]. For a description of the dielectric-dependent exact-exchange mixing scheme hybrid functionals column headings see Table IV.</caption>
<tbody>
<tr>
<td>
</td>
<td>
PBE
</td>
<td>
PBE0
</td>
<td>
hybrid
</td>
<td>
hybrid
</td>
<td>
sc-hybrid
</td>
<td>
$G_0W_0$ [83]
</td>
<td>
$GW_0$ [83]
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$\alpha = 0$
</td>
<td>
$\alpha = 0.25$
</td>
<td>
$\alpha = 1/\epsilon_\infty^{\text{PBE}}$
</td>
<td>
$\alpha = 1/\epsilon_\infty^{\text{PBE0}}$
</td>
<td>
$\alpha = 1/\text{sc-}\epsilon_\infty$
</td>
<td>
RPA
</td>
<td>
RPA
</td>
<td>
Exp.
</td>
</tr>
<tr>
<td>
GaN
</td>
<td>
$-$13.8
</td>
<td>
$-$15.7
</td>
<td>
$-$16.0
</td>
<td>
$-$16.2
</td>
<td>
$-$16.6
</td>
<td>
$-$16.0
</td>
<td>
$-$16.9
</td>
<td>
$-$17.0
</td>
</tr>
<tr>
<td>
ZnO
</td>
<td>
$-$5.0
</td>
<td>
$-$6.0
</td>
<td>
$-$5.9
</td>
<td>
$-$6.2
</td>
<td>
$-$6.3
</td>
<td>
$-$6.2
</td>
<td>
$-$6.6
</td>
<td>
$-$7.5, $-$8.81
</td>
</tr>
<tr>
<td>
ZnS
</td>
<td>
$-$6.3
</td>
<td>
$-$7.8
</td>
<td>
$-$7.5
</td>
<td>
$-$7.5
</td>
<td>
$-$7.5
</td>
<td>
$-$7.0
</td>
<td>
$-$7.5
</td>
<td>
$-$9.03
</td>
</tr>
</tbody>
</table>

## III. RESULTS AND DISCUSSION

### A. Static electronic dielectric constant

The static electronic dielectric constant ($\epsilon_\infty$) of several crystalline materials was evaluated with PBE, PBE0, the fixed-$\alpha$ hybrid functionals ($\alpha = 1/\epsilon_\infty^{\text{PBE}}$ and $\alpha = 1/\epsilon_\infty^{\text{PBE0}}$), and the self-consistent version (sc-hybrid). In Table I results are shown for 24 solids, which cover a broad range of static dielectric constants (1.23–15.9) and band gaps (0.7–21.7 eV). In the case of noncubic systems, we report the average of the trace of the dielectric tensor. Results obtained with the semilocal PBE and the hybrid PBE0 functionals exhibit the poorest agreement with experiment, with the PBE error being at least twice as large as those of other hybrid functionals. The closest agreement with experiment is obtained with the sc-hybrid, although using $\alpha = 1/\epsilon_\infty^{\text{PBE}}$ or $\alpha = 1/\epsilon_\infty^{\text{PBE0}}$ also yields satisfactory results. We note that the absence of values for CoO and Ge in both the PBE and hybrid ($\alpha = 1/\epsilon_\infty^{\text{PBE}}$) columns is due to the fact that these systems turn out to be erroneously metallic when using semilocal functionals and thus $\epsilon_\infty^{\text{PBE}}$ cannot be evaluated.

We also compared the sc-hybrid results with those of many-body perturbation theory in the $GW$ approximation for a subset of solids for which previous $G_0W_0$ and self-consistent $GW$ results were reported [83,84] (see Table II). The $G_0W_0$ (RPA) calculations were carried out by evaluating the dielectric response in the random phase approximation, without updating the electronic wave functions. The sc$GW$ (e-h) calculations were carried out self-consistently, using a frequency-independent (static approximation) dielectric response with a vertex correction in $W$ that effectively includes the electron-hole interaction (e-h). The dielectric constants evaluated with sc-hybrid have similar errors as those obtained with the sc$GW$ (e-h) approach. The agreement between sc-hybrid and sc$GW$ (e-h) results suggests that the inclusion of nonlocal-field effects in the evaluation of $f_{\text{xc}}$ when computing $\epsilon_\infty$ may play a similar role as the inclusion of the vertex corrections in $W$, when carrying out $GW$ calculations. This interpretation is also supported by the comparison of sc-hybrid with $G_0W_0$(RPA) results, which show the poorest agreement with experiments. We recall that within RPA only the local-field effects coming from the Hartree potential are included. The sc-hybrid scheme with local-field effects neglected in $\chi$ [Eq. (21)] is shown in the column heading under sc-hybrid (NLF) in Table II. In the NLF case, the error is about three times as large as the case where local fields are included.

Overall, the agreement between sc-hybrid and sc$GW$ (e-h) results suggests that the static approximation captures most of the screening in the bulk materials considered here, and that including the dynamical frequency dependence in the dielectric response is not critical to obtain accurate static dielectric constants.

To further evaluate the accuracy of the static electronic dielectric constants obtained with the sc-hybrid functional, we compared the computed individual tensor components for the optically anisotropic wurtzite phases of GaN, AlN, and ZnO in Table III. The agreement with experimental results is very good for each of the individual tensor components.

<table>
<caption>TABLE VIII. The equilibrium lattice constant (Å) for a subset of solids compared with experiment. For a description of the dielectric-dependent exact exchange mixing scheme hybrid functionals column headings see Table IV. The first column corresponds to the lattice constant evaluated with plane-wave (PW) basis and PAW pseudopotentials. All other results were obtained with Gaussian basis sets (GTO). The $\alpha$ fixed sc-hybrid column indicates the value of $\alpha$ is kept fixed throughout the lattice optimization to the value of $\alpha$ determined self-consistently at the experimental geometry. The experimental lattice constants are from Ref. [112]. The (0 K) column corresponds to the experimental measured lattice constant extrapolated to 0 K. The ZPAE column is obtained by removing from the experimental (0 K) column the zero-point anharmonic expansion effects, determined from first principles. Our calculated results should be compared with the experimental (ZPAE) column, since in our calculations we do not include zero-point energy contributions.</caption>
<tbody>
<tr>
<td>
</td>
<td>
PBE PW
</td>
<td>
PBE GTO
</td>
<td>
PBE0
</td>
<td>
hybrid
</td>
<td>
hybrid
</td>
<td>
sc-hybrid
</td>
<td colspan="2">
Exp.
</td>
</tr>
<tr>
<td>
</td>
<td>
$\alpha = 0$
</td>
<td>
$\alpha = 0$
</td>
<td>
$\alpha = 0.25$
</td>
<td>
$\alpha = 1/\epsilon_\infty^{\text{PBE}}$
</td>
<td>
$\alpha = 1/\epsilon_\infty^{\text{PBE0}}$
</td>
<td>
$\alpha$ fixed
</td>
<td>
(0 K)
</td>
<td>
(ZPAE)
</td>
</tr>
<tr>
<td>
Si
</td>
<td>
5.47
</td>
<td>
5.47
</td>
<td>
5.44
</td>
<td>
5.46
</td>
<td>
5.46
</td>
<td>
5.46
</td>
<td>
5.43
</td>
<td>
5.42
</td>
</tr>
<tr>
<td>
C
</td>
<td>
3.57
</td>
<td>
3.57
</td>
<td>
3.55
</td>
<td>
3.55
</td>
<td>
3.55
</td>
<td>
3.55
</td>
<td>
3.57
</td>
<td>
3.54
</td>
</tr>
<tr>
<td>
SiC
</td>
<td>
4.38
</td>
<td>
4.38
</td>
<td>
4.35
</td>
<td>
4.37
</td>
<td>
4.36
</td>
<td>
4.36
</td>
<td>
4.36
</td>
<td>
4.34
</td>
</tr>
<tr>
<td>
MgO
</td>
<td>
4.26
</td>
<td>
4.26
</td>
<td>
4.21
</td>
<td>
4.20
</td>
<td>
4.19
</td>
<td>
4.19
</td>
<td>
4.21
</td>
<td>
4.19
</td>
</tr>
<tr>
<td>
LiCl
</td>
<td>
5.15
</td>
<td>
5.15
</td>
<td>
5.11
</td>
<td>
5.10
</td>
<td>
5.10
</td>
<td>
5.10
</td>
<td>
5.11
</td>
<td>
5.07
</td>
</tr>
<tr>
<td>
NaCl
</td>
<td>
5.69
</td>
<td>
5.68
</td>
<td>
5.63
</td>
<td>
5.61
</td>
<td>
5.61
</td>
<td>
5.61
</td>
<td>
5.60
</td>
<td>
5.57
</td>
</tr>
</tbody>
</table>

195112-8

### B. Electronic energy gaps and band structure

We now turn to the comparison of the Kohn-Sham gaps evaluated using the fixed dielectric-dependent hybrid functionals and the self-consistent dielectric-dependent functional (sc-hybrid) at the experimental geometries (Table IV). We also include in Table IV the results obtained with the GGA functional PBE and the fixed $\alpha = 0.25$ hybrid functional PBE0. In most cases, we found a considerable improvement over GGA with hybrid functionals, with the best results obtained for the dielectric-dependent hybrid functionals. The largest relative errors were found for the insulators alumina ($\mathrm{Al_2O_3}$) and hafnia ($\mathrm{HfO_2}$). This discrepancy with experiments may be due, at least in part, to the poor crystallinity of the samples used experimentally. The presence of "band tail states" was investigated for hafnia, and a corrected photoemission gap obtained by removing the band tails was reported (6.7 eV) [96], which is very similar to that computed with the sc-hybrid functional (6.8 eV). The alumina experimental gap reported in Table IV is an optical gap (excitonic contributions present). However, the exciton binding energy of alumina was estimated to be similar to that of excitons in MgO (0.06 eV) [106] and hence the optical and photoemission gaps are expected to differ at most by $\sim$0.1 eV.

Table V compares the electronic gaps evaluated with the present sc-hybrid scheme and with the $GW$ approximation. The $\text{sc}GW$ ($G_0W_0$) calculations used the HSE (PBE) hybrid functional eigenvalues and wave functions as input. The error of the sc-hybrid functional in predicting band gaps is similar to that introduced by the $\text{sc}GW$ method where e-h interactions are included in $W$.

We also computed the valence bandwidths for a subset of the solids listed in Tables I and IV; these are shown in Table VI. The results of the dielectric dependent hybrid functionals agree remarkably well with experiment, whereas the PBE and PBE0 functionals systematically underestimate and overestimate the bandwidths, respectively. There is an outlier, i.e., ZnO, for which none of the computed valence bandwidths agree with experiment. Both hybrid density functionals, as well as $GW$, incorrectly describe the localized occupied $d$ band, with a tendency to underbind (see Table VII). Though $\text{sc}GW$ results are not shown in Table VII, the authors of Ref. [84] reported that the $\text{sc}GW$ band positions are underbound by a similar magnitude as the $G_0W_0$ results.

### C. Lattice constants

We further used the dielectric-dependent hybrid functionals to perform structural optimizations of a subset of solids. In most cases, including exact exchange improves the agreement of the computed lattice constants with experiment for nonmetallic systems, as compared to the semilocal functional (PBE) results (see Table VIII). For the sc-hybrid functional, the total derivative of the energy $E(R,\alpha(R))$ with respect to the lattice constant $R$ is expressed as
$$
\frac{dE}{dR} = \left(\frac{\partial E}{\partial R}\right) + \left(\frac{\partial E}{\partial \alpha}\right)\frac{d\alpha}{dR}. \tag{23}
$$

When the second term on the right-hand side of Eq. (23) is much smaller than the first term, e.g., when $\alpha$ is almost constant as a function of $R$, close to the minimum, the total derivative of the energy can be approximated as
$$
\frac{dE}{dR} \cong \left(\frac{\partial E}{\partial R}\right). \tag{24}
$$

![](./images/813141830911655938_3.jpg)

FIG. 3. (Color online) Total energy of MgO as a function of the lattice constant (Å). The black dotted vertical line indicates the experimental value extrapolated to 0 K, where the zero-point anharmonic contribution has been removed. The colored arrows point to the minima of each surface. The PBE and PBE0 total energy curves were shifted by $-0.027$ and $-0.006$ hartrees, respectively, in order to fit on the same plot.

The sc-hybrid lattice constants shown in Table VIII and the sc-hybrid potential energy surface plotted for MgO in Fig. 3 were evaluated using Eq. (24). We note that the derivative in Eq. (24) is to be evaluated at constant $\alpha$ and its root is nearly insensitive to which $\alpha$ is chosen, whether the one determined self-consistently at the experimental equilibrium positions or a parameter $\alpha$ computed for a lattice constant close to the experimental equilibrium. This can be seen, for example, by comparing the results obtained with PBE0, hybrid, and sc-hybrid functionals and shown in Table VIII, which were obtained for different fixed values of $\alpha$ and yet yielded optimal lattice constants that differ by less than $0.02$ Å.

For most of the systems shown in Table VIII, Eq. (24) is a good approximation to the total derivative. However, in the case of NaCl and LiCl, the second term on the right-hand side of Eq. (23) is non-negligible and the roots of Eqs. (23) and (24) are different. In this case the root of Eq. (23) yields results in poor agreement with the experimental lattice constants [e.g., using Eq. (23) we obtain 5.96 Å for NaCl, and 5.35 Å for LiCl].

### IV. SUMMARY AND CONCLUSIONS

We presented a full-range hybrid functional for the calculation of the electronic properties of nonmetallic condensed systems which yielded results in excellent agreement with experiments for the band gaps and dielectric constants of a wide range of semiconductors and insulators. The exchange-correlation functional is defined in a way similar to the PBE0 functional, but the mixing parameter is set equal to the inverse macroscopic dielectric constant and it is determined self-consistently by computing the optimal dielectric screening. We

showed that convergence is usually achieved in 3–4 iterations, regardless of whether the initial value of the dielectric constant is computed at the PBE or PBE0 level of theory. In many cases, the results for $\alpha = 1/\epsilon_\infty^{\text{PBE0}}$ are of similar accuracy to the sc-hybrid results [113] which suggests that for certain systems self-consistency may be avoided, further reducing computational cost. The presence of $f_{\text{xc}}$ in the local fields was investigated in detail, with particular emphasis on the nonlocal exchange contribution $f_{x-\text{nl}}$, which yields an accurate description of the static dielectric constant, when included. Our results suggest that including the nonlocal contributions in $f_{\text{xc}}$ is an effective way of including long-range interaction effects in condensed phase systems, without resorting to expensive vertex corrections. The computed band gaps and dielectric constants are in general much improved with respect to those obtained with the PBE and PBE0 functionals, with errors with respect to experiments similar in magnitude to those of fully self-consistent $GW$ (e-h) calculations.

All results presented here were obtained within an all-electron scheme (except for W and Hf, for which we used effective-core pseudopotentials) and using first-order perturbation theory within the CPKS scheme to compute the dielectric constant. Work is in progress to implement finite field methods for the dielectric constant in plane-wave pseudopotential codes, which will allow for the use of the sc-hybrid scheme for liquids, in general disordered systems, and in *ab initio* molecular dynamics calculations. Though here we chose a full-range hybrid functional, our approach may be easily extended to range-separated hybrid functionals, where the static dielectric constant is used to define the mixing parameter of the long-range component. The computational cost of the sc-hybrid scheme is similar to that of hybrid calculations, making it a computationally cheaper alternative to $GW$ calculations. We note that a self-consistent dielectric screened hybrid functional provides a means to compute an effective statically screened Coulomb interaction $W$, and thus it offers a suitable starting point for $G_0W_0$ calculations.

## ACKNOWLEDGMENTS

We thank Michel Rérart and Roberto Orlando for helpful discussions pertaining to the CPKS implementation in CRYSTAL. We also wish to thank Ding Pan for helpful discussions and for providing the ice XI structure. This work was supported by the NSF Center for Chemical Innovation (Powering the Planet, Grant No. NSF-CHE-0802907) and by the Army Research Laboratory Collaborative Research Alliance in Multiscale Multidisciplinary Modeling of Electronic Materials (CRL-MSME, Grant No. W911NF-12-2-0023). All calculations were performed at the Navy DoD Supercomputing Resource Center of the Department of Defense High Performance Computing Modernization Program.

[1] P. Hohenberg, *Phys. Rev.* **136**, B864 (1964).
[2] W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).
[3] R. Dreizler and E. Gross, *Density Functional Theory* (Springer Verlag, Berlin, 1990).
[4] A. D. Becke, *J. Chem. Phys.* **98**, 1372 (1993).
[5] A. Seidl, A. Görling, P. Vogl, J. Majewski, and M. Levy, *Phys. Rev. B* **53**, 3764 (1996).
[6] Though we use, as an example, the error function to partition the Coulomb interaction into long and short range, other functions could be used such as the semiclassical Thomas-Fermi screening function.
[7] J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **124**, 219906 (2006).
[8] D. Bylander and L. Kleinman, *Phys. Rev. B* **41**, 7868 (1990).
[9] T. Yanai, D. P. Tew, and N. C. Handy, *Chem. Phys. Lett.* **393**, 51 (2004).
[10] E. Weintraub, T. M. Henderson, and G. E. Scuseria, *J. Chem. Theory Comput.* **5**, 754 (2009).
[11] C. Adamo and V. Barone, *J. Chem. Phys.* **110**, 6158 (1999).
[12] F. M. Bickelhaupt and E. J. Baerends, in *Reviews in Computational Chemistry* (John Wiley & Sons, Inc., New York, 2007), pp. 1–86.
[13] X. Wu, A. Selloni, and R. Car, *Phys. Rev. B* **79**, 085102 (2009).
[14] F. Gygi, *Phys. Rev. Lett.* **102**, 166406 (2009).
[15] F. Gygi and I. Duchemin, *J. Chem. Theory Comput.* **9**, 582 (2013).
[16] S. Kümmel and L. Kronik, *Rev. Mod. Phys.* **80**, 3 (2008).
[17] Z. D. Pozun and G. Henkelman, *J. Chem. Phys.* **134**, 224706 (2011).
[18] J. C. Conesa, J. Phys. Chem. C **116**, 18884 (2012).
[19] A. Alkauskas, P. Broqvist, F. Devynck, and A. Pasquarello, *Phys. Rev. Lett.* **101**, 106802 (2008).
[20] A. Alkauskas, P. Broqvist, and A. Pasquarello, *Phys. Status Solidi B* **248**, 775 (2011).
[21] P. Broqvist, A. Alkauskas, and A. Pasquarello, *Phys. Status Solidi A* **207**, 270 (2010).
[22] G. Strinati, *La Rivista del Nuovo Cimento* (1978-1999) **11**, 1 (1988).
[23] G. Onida, L. Reining, and A. Rubio, *Rev. Mod. Phys.* **74**, 601 (2002).
[24] L. Hedin, *Phys. Rev.* **139**, A796 (1965).
[25] M. S. Hybertsen and S. G. Louie, *Phys. Rev. Lett.* **55**, 1418 (1985).
[26] W. G. Aulbur, L. Jönsson, and J. W. Wilkins, *Solid State Phys.* **54**, 1 (2000).
[27] H.-V. Nguyen, T. A. Pham, D. Rocca, and G. Galli, *Phys. Rev. B* **85**, 081101 (2012).
[28] T. A. Pham, H.-V. Nguyen, D. Rocca, and G. Galli, *Phys. Rev. B* **87**, 155148 (2013).
[29] Y. Ping, D. Rocca, and G. Galli, *Phys. Rev. B* **87**, 165203 (2013).
[30] F. Bruneval and M. Gatti, in *Topics in Current Chemistry* (Springer, Berlin, 2014), pp. 1–37.

[31] M. A. L. Marques, J. Vidal, M. J. T. Oliveira, L. Reining, and S. Botti, Phys. Rev. B 83, 035119 (2011).

[32] J. E. Moussa, P. A. Schultz, and J. R. Chelikowsky, J. Chem. Phys. 136, 204117 (2012).

[33] S. Botti, F. Sottile, N. Vast, V. Olevano, L. Reining, H.-C. Weissker, A. Rubio, G. Onida, R. Del Sole, and R. W. Godby, Phys. Rev. B 69, 155112 (2004).

[34] T. Shimazaki and Y. Asai, Chem. Phys. Lett. 466, 91 (2008).

[35] S. Refaely-Abramson, S. Sharifzadeh, M. Jain, R. Baer, J. B. Neaton, and L. Kronik, Phys. Rev. B 88, 081204 (2013).

[36] T. Shimazaki and Y. Asai, J. Chem. Phys. 130, 164702 (2009).

[37] T. Shimazaki and Y. Asai, J. Chem. Phys. 132, 224105 (2010).

[38] In the Penn model [114] the static dielectric constant is approximated as $\epsilon_\infty \approx 1 + \left( \frac{\omega_p}{E_g} \right)^2$, where $\omega_p$ is the plasmon frequency and $E_g$ is the energy gap.

[39] D. Koller, P. Blaha, and F. Tran, J. Phys.: Condens. Matter 25, 435503 (2013).

[40] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[41] Convergence of the sc-hybrid scheme is achieved when $\epsilon_\infty <$ 0.01. In the present scheme $\epsilon_\infty$ is only evaluated at the end of each converged self-consistent field (SCF) calculation; in principle one could instead evaluate $\epsilon_\infty$ at each step of the SCF procedure in an attempt to reduce the overall number of SCF iterations, but this would be prohibitively expensive.

[42] R. King-Smith and D. Vanderbilt, Phys. Rev. B 47, 1651 (1993).

[43] R. Resta, Rev. Mod. Phys. 66, 899 (1994).

[44] S. Baroni, S. de Gironcoli, and A. Dal Corso, Rev. Mod. Phys. 73, 515 (2001).

[45] M. Rérat, R. Orlando, and R. Dovesi, J. Phys.: Conf. Ser. 117, 012016 (2008).

[46] B. G. Johnson and M. J. Frisch, Chem. Phys. Lett. 216, 133 (1993).

[47] J. A. Pople, R. Krishnan, H. B. Schlegel, and J. S. Binkley, Int. J. Quantum Chem. 16, 225 (1979).

[48] G. J. B. Hurst, M. Dupuis, and E. Clementi, J. Chem. Phys. 89, 385 (1988).

[49] R. Orlando, M. Ferrero, M. Rérat, B. Kirtman, and R. Dovesi, J. Chem. Phys. 131, 184105 (2009).

[50] R. Dovesi, R. Orlando, B. Civalleri, C. Roetti, V. R. Saunders, and C. M. Zicovich-Wilson, Zeitschrift für Kristallographie 220, 571 (2005).

[51] H. Ehrenreich, *The Optical Properties of Solids: Proceedings of the International School of Physics "Enrico Fermi"*, Varenna, edited by J. Tauc. (Academic Press, New York, 1966), p. 106.

[52] W. Hanke, Adv. Phys. 27, 287 (1978).

[53] A. L. Fetter and J. D. Walecka, *Quantum Theory of Many-Particle Systems* (Dover Publications, New York, 2003).

[54] S. L. Adler, Phys. Rev. 126, 413 (1962).

[55] N. Wiser, Phys. Rev. 129, 62 (1963).

[56] E. K. U. Gross, E. Runge, and O. Heinonen, *Many-Particle Theory* (Taylor & Francis, London, 1991).

[57] J. Paier, M. Marsman, and G. Kresse, Phys. Rev. B 78, 121201(R) (2008).

[58] The explicit calculation of the perturbed orbitals comes at the expense of evaluating unoccupied KS orbitals that enter the expression of the functional derivatives. Within DFPT applied to semilocal functionals, the calculations of empty orbitals is avoided by utilizing projection techniques [44].

[59] F. Bruneval, F. Sottile, V. Olevano, R. Del Sole, and L. Reining, Phys. Rev. Lett. 94, 186402 (2005).

[60] F. Weigend and R. Ahlrichs, Phys. Chem. Chem. Phys. 7, 3297 (2005).

[61] D. Rappoport and F. Furche, J. Chem. Phys. 133, 134105 (2010).

[62] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.89.195112 for additional information on the localized Gaussian basis sets used, the pseudopotentials used in plane-wave calculations, the $k$-point convergence for the polarizabilities, and a comparison of plane-wave and Gaussian basis set results.

[63] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos *et al.*, J. Phys.: Condens. Matter 21, 395502 (2009).

[64] A. R. Tackett, A. W. Holzwarth, and G. E. Matthews, Comput. Phys. Commun. 135, 329 (2001).

[65] http://www.quantum-espresso.org/pseudopotentials/.

[66] J. A. Van Vechten, Phys. Rev. 182, 891 (1969).

[67] P. Y. Yu and M. Cardona, *Fundamentals of Semiconductors* (Springer-Verlag, Berlin, 2001).

[68] J. R. DeVore, JOSA 41, 416 (1951).

[69] K. V. Rao and A. Smakula, J. Appl. Phys. 36, 2031 (1965).

[70] M. Giehler, M. Ramsteiner, O. Brandt, H. Yang, and K. H. Ploog, Appl. Phys. Lett. 67, 733 (1995).

[71] J. Plendl, L. Mansur, S. Mitra, and I. Chang, Solid State Commun. 7, 109 (1969).

[72] M. Hutchins, O. Abu-Alkhair, M. El-Nahass, and K. A. El- Hady, Mater. Chem. Phys. 98, 401 (2006).

[73] J. Chen, Z. H. Levine, and J. W. Wilkins, Appl. Phys. Lett. 66, 1129 (1995).

[74] M. Balog, M. Schieber, M. Michman, and S. Patai, Thin Solid Films 41, 247 (1977).

[75] S. Shokhovets, R. Goldhahn, G. Gobsch, S. Piekh, R. Lantier, A. Rizzi, V. Lebedev, and W. Richter, J. Appl. Phys. 94, 307 (2003).

[76] N. Ashkenov, B. N. Mbenkum, C. Bundesmann, V. Riede, M. Lorenz, D. Spemann, E. M. Kaidashev, A. Kasic, M. Schubert, M. Grundmann, G. Wagner, H. Neumann, V. Darakchieva, H. Arwin, and B. Monemar, J. Appl. Phys. 93, 126 (2003).

[77] R. H. French, H. Müllejans, and D. J. Jones, J. Am. Ceram. Soc. 81, 2549 (2005).

[78] D. R. Lide, *CRC Handbook of Chemistry and Physics*, 90th ed. (CRC Press/Taylor and Francis, Boca Raton, FL, 2010).

[79] M. Bass, C. DeCusatis, V. Enoch, J Lakshminarayanan, G. Li, C. MacDonald, V. Mahajan, and E. Van Stryland, *Handbook of Optics Volume IV: Optical Properties of Materials, Nonlinear Optics, Quantum Optics*, 3rd ed. (McGraw Hill Professional, New York, 2009).

[80] G. P. Johari and S. J. Jones, Proc. R. Soc. London A 349, 467 (1976).

[81] A. C. Sinnock and B. L. Smith, Phys. Rev. 181, 1297 (1969).

[82] W. Schulze and D. M. Kolb, J. Chem. Soc., Faraday Trans. 2 70, 1098 (1974).

[83] M. Shishkin and G. Kresse, Phys. Rev. B 75, 235102 (2007).

[84] M. Shishkin, M. Marsman, and G. Kresse, *Phys. Rev. Lett.* **99**, 246403 (2007).

[85] C. Kittel, *Introduction to Solid State Physics* (Wiley, New York, 2005).

[86] B. Monemar, *Phys. Rev. B* **8**, 5711 (1973).

[87] W. Choyke, D. Hamilton, and L. Patrick, *Phys. Rev.* **133**, A1163 (1964).

[88] Y. Tezuka, S. Shin, T. Ishii, T. Ejima, S. Suzuki, and S. Sato, *J. Phys. Soc. Jpn.* **63**, 347 (1994).

[89] G. A. Sawatzky and J. W. Allen, *Phys. Rev. Lett.* **53**, 2339 (1984).

[90] C. D. Clark, P. J. Dean, and P. V. Harris, *Proc. R. Soc. A* **277**, 312 (1964).

[91] J. van Elp, J. L. Wieland, H. Eskes, P. Kuiper, G. A. Sawatzky, F. M. F. de Groot, and T. S. Turner, *Phys. Rev. B* **44**, 6090 (1991).

[92] G. Ramírez-Flores, H. Navarro-Contreras, A. Lastras- Martínez, R. C. Powell, and J. E. Greene, *Phys. Rev. B* **50**, 8433 (1994).

[93] J. van Elp, R. H. Potze, H. Eskes, R. Berger, and G. A. Sawatzky, *Phys. Rev. B* **44**, 1530 (1991).

[94] J. Meyer, M. Kröger, S. Hamwi, F. Gnam, T. Riedl, W. Kowalsky, and A. Kahn, *Appl. Phys. Lett.* **96**, 193302 (2010).

[95] M. Levinshtein, S. L. Rumyantsev, and M. S. Shur, *Properties of Advanced Semiconductor Materials: GaN, AlN, InN, BN, SiC, and SiGe* (Wiley, New York, 2001).

[96] S. Sayan, T. Emge, E. Garfunkel, X. Zhao, L. Wielunski, R. A. Bartynski, D. Vanderbilt, J. S. Suehle, S. Suzer, and M. Banaszak-Holl, *J. Appl. Phys.* **96**, 7485 (2004).

[97] L. Roskovcová and J. Pastrňák, *Czech. J. Phys. B* **30**, 586 (1980).

[98] Ü. Özgür, Y. I. Alivov, C. Liu, A. Teke, M. A. Reshchikov, S. Doğan, V. Avrutin, S.-J. Cho, and H. Morkoç, *J. Appl. Phys.* **98**, 041301 (2005).

[99] M. E. Innocenzi, R. T. Swimm, M. Bass, R. H. French, A. B. Villaverde, and M. R. Kokta, *J. Appl. Phys.* **67**, 7542 (1990).

[100] R. Whited, C. J. Flaten, and W. Walker, *Solid State Commun.* **13**, 1903 (1973).

[101] G. Baldini and B. Bosacchi, *Phys. Status Solidi B* **38**, 325 (1970).

[102] S.-i. Nakai and T. Sagawa, *J. Phys. Soc. Jpn.* **26**, 1427 (1969).

[103] M. Piacentini, D. W. Lynch, and C. G. Olson, *Phys. Rev. B* **13**, 5530 (1976).

[104] K. Kobayashi, *J. Phys. Chem.* **87**, 4317 (1983).

[105] N. Schwentner, F. J. Himpsel, V. Saile, M. Skibowski, W. Steinmann, and E. E. Koch, *Phys. Rev. Lett.* **34**, 528 (1975).

[106] R. H. French, *J. Am. Ceram. Soc.* **73**, 477 (1990).

[107] S. D. Kevan, *Studies in Surface Science and Catalysis: Angle-Resolved Photoemission* (Elsevier, Amsterdam, 1992), Vol. 74.

[108] I. Jiménez, L. J. Terminello, D. G. J. Sutherland, J. A. Carlisle, E. L. Shirley, and F. J. Himpsel, *Phys. Rev. B* **56**, 7215 (1997).

[109] J. Furthmüller, G. Cappellini, H.-C. Weissker, and F. Bechstedt, *Phys. Rev. B* **66**, 045110 (2002).

[110] F. J. Himpsel, L. J. Terminello, D. A. Lapiano-Smith, E. A. Eklund, and J. J. Barton, *Phys. Rev. Lett.* **68**, 3611 (1992).

[111] L. Tjeng, A. Vos, and G. Sawatzky, *Surf. Sci.* **235**, 269 (1990).

[112] L. Schimka, J. Harl, and G. Kresse, *J. Chem. Phys.* **134**, 024116 (2011).

[113] Notable exceptions are CoO and NiO, for which the sc-hybrid and the $\alpha=1/\epsilon_\infty^{\text{PBE0}}$ hybrid were not as similar because the convergence in the sc-hybrid is not achieved until five and nine iterations, respectively, for CoO and NiO.

[114] D. R. Penn, *Phys. Rev.* **128**, 2093 (1962).