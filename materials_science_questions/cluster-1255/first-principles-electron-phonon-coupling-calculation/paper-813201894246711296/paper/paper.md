PHYSICAL REVIEW B 88, 054510 (2013)

# Nonempirical study of superconductivity in alkali-doped fullerides based on density functional theory for superconductors

Ryosuke Akashi¹ and Ryotaro Arita¹,²

¹Department of Applied Physics, The University of Tokyo, Hongo, Bunkyo-ku, Tokyo 113-8656, Japan
²JST-PRESTO, Kawaguchi, Saitama 332-0012, Japan

(Received 21 March 2013; revised manuscript received 8 August 2013; published 21 August 2013)

We apply the density functional theory for superconductors based on the local density approximation (LDA) to alkali-doped fullerides $A_3$C₆₀ with a face-centered-cubic structure. We evaluate the superconducting transition temperature ($T_\text{c}$) from first principles considering the energy dependence of electron-phonon coupling, the mass renormalization, and the retardation effect. The calculated $T_\text{c} = 7.5$, 9.0, and 15.7 K for $A = \text{K}$, $\text{Rb}$, $\text{Cs}$ are approximately 60% smaller than the experimentally observed values. Our results strongly suggest the necessity to go beyond the framework of the Migdal-Eliashberg theory based on the LDA.

DOI: 10.1103/PhysRevB.88.054510
PACS number(s): 74.20.Pq, 74.25.Kc, 74.70.Kn, 74.70.Wz

## I. INTRODUCTION

Doped fulleride superconductors $A_3$C₆₀ ($A = \text{alkali metal}$),¹,² which exhibit a maximum transition temperature ($T_\text{c}$) of 40 K, have provided a fertile playground for theoretical and experimental studies. The most significant feature of the fullerides is the narrow metallic bands formed by molecular orbitals, whose energy scale competes with the vibrational frequencies and electron-electron interactions. Moreover, recent experiments revealed that the $T_\text{c}$-volume ($V$) curve for this series shows a domelike dependence near the superconductor-Mott insulator transition.³⁻⁸ This dependence is, similarly to the celebrated superconducting dome in cuprates, reminiscent of a crossover from weak to strong correlation in this system.

Motivated by these properties, various theoretical studies have investigated unconventional pairing mechanisms.¹,⁹ On the other hand, there has also been a received idea that the superconductivity in this system is explained by the conventional phonon-mediated pairing mechanism. A full $s$-wave gap with spin-singlet pairing,¹⁰⁻¹² a C-isotope effect coefficient of $\gtrsim$0.20,¹³⁻¹⁵ and coherence peaks in the nuclear magnetic resonance and muon spin relaxation rates¹⁶,¹⁷ have been experimentally observed. In particular, in the $T_\text{c}$-$V$ plot, the regime where $T_\text{c}$ and $V$ positively correlate is seemingly consistent with the BCS theory; increasing $V$ results in smaller bandwidths, a larger density of states (DOS) at the Fermi level, and subsequently stronger electron-phonon coupling. Hence, the applicability of the phonon mechanism is still unsettled.

The Migdal-Eliashberg (ME) theory¹⁸ is a widely applicable theory of phonon-mediated superconductivity, where the self-energy with the lowest-order exchange contribution of the dressed phonons and the static screened Coulomb interaction is included. For various superconductors, it has been of central interest whether the ME theory based on the Kohn-Sham orbital calculated with the local density approximation¹⁹,²⁰ (KS-LDA) explains the experimental $T_\text{c}$.²¹⁻²³ Moreover, the recently developed density functional theory for superconductors (SCDFT) (Refs. 24 and 25) has provided us a way to calculate $T_\text{c}$ based on the ME theory nonempirically. The SCDFT treats the effects of the interactions such as the mass renormalization¹⁸ and the retardation effect,²⁶ taking the detail of the electronic structure. Since the $T_\text{c}$ calculation using the SCDFT has accurately reproduced experimentally observed $T_\text{c}$ in typical phonon-induced superconductors,²⁵,²⁷,²⁸ it allows us to directly judge the applicability of the ME theory to the fullerides. However, its application to molecular solids has not been reported due to its expensive computational cost. In this paper, we apply the SCDFT to fcc $A_3$C₆₀ having 63 atoms per unit cell [$A = \text{K}$ and $\text{Rb}$ under ambient pressure ($T_\text{c} = 19$ and 29 K), and $\text{Cs}$ under an optimum pressure of 7 kbar ($T_\text{c} = 35$ K)], focusing on the regime where $T_\text{c}$ and $V$ positively correlate. We calculate $T_\text{c}$ to see if the SCDFT reproduces the absolute values and the alkali-metal dependence of the experimentally observed $T_\text{c}$, with which we examine the applicability of the ME theory with the KS-LDA in the present system. The calculated $T_\text{c}$ suggests that we need to consider some factors missing in the framework of the ME theory based on the KS-LDA.

## II. METHOD

In the current SCDFT²⁴,²⁵ we solve the gap equation given by

$$
\Delta_{n\mathbf{k}}=-\mathcal{Z}_{n\mathbf{k}}\Delta_{n\mathbf{k}}-\frac{1}{2}\sum_{n'\mathbf{k}'}\mathcal{K}_{n\mathbf{k}n'\mathbf{k}'}\frac{\tanh[(\beta/2)E_{n'\mathbf{k}'}]}{E_{n'\mathbf{k}'}}\Delta_{n'\mathbf{k}'.}\quad(1)
$$

Here, $n$ and $\mathbf{k}$ denote the band index and crystal momentum, respectively, $\Delta$ is the gap function, and $\beta$ is the inverse temperature. The energy $E_{n\mathbf{k}}$ is defined as $E_{n\mathbf{k}} = \sqrt{\xi_{n\mathbf{k}}^2 + \Delta_{n\mathbf{k}}^2}$ and $\xi_{n\mathbf{k}} = \epsilon_{n\mathbf{k}} - \mu$ is the one-electron energy measured from the chemical potential $\mu$, where $\epsilon_{n\mathbf{k}}$ is obtained by solving the normal Kohn-Sham equation $\mathcal{H}_{\text{KS}}|\varphi_{n\mathbf{k}}\rangle = \epsilon_{n\mathbf{k}}|\varphi_{n\mathbf{k}}\rangle$ with $\mathcal{H}_{\text{KS}}$ and $|\varphi_{n\mathbf{k}}\rangle$ being the Kohn-Sham Hamiltonian and the Bloch state, respectively. The functions $\mathcal{Z}$ and $\mathcal{K}$ are the exchange-correlation kernels describing the effects of the interactions. The kernels describing the standard electron-phonon mechanism, $\mathcal{K} = \mathcal{K}^{\text{ph}} + \mathcal{K}^{\text{el}}$ and $\mathcal{Z} = \mathcal{Z}^{\text{ph}}$, have been proposed.²⁴,²⁵ Namely, the phonon contributions ($\mathcal{K}^{\text{ph}}$ and $\mathcal{Z}^{\text{ph}}$) were formulated referring to the ME theory, and the electron contribution ($\mathcal{K}^{\text{el}}$) corresponds to the screened static Coulomb interaction scattering the Cooper pairs.

Since the fulleride superconductors involve high-frequency phonons, the electron-phonon interaction has a strong dependence on both $\xi_{n\mathbf{k}}$ and $\xi_{n'\mathbf{k}'}$. In order to treat this effect, we

use the $n\boldsymbol{k}$-resolved form for $\mathcal{K}^{\text{ph}}$ and $\mathcal{Z}^{\text{ph}}$ defined by Eqs. (9) and (11) in Ref. 25, which require the electron-phonon matrix elements $g_{n\boldsymbol{k},n'\boldsymbol{k}'}^{\nu\mathfrak{q}}$ and the phonon frequencies $\omega_{\nu\mathfrak{q}}$ as inputs. For $\mathcal{K}^{\text{el}}$, on the other hand, we use the form given by Eq. (13) in Ref. 29, which is based on the static random-phase approximation (RPA) (Ref. 30) and properly treats the local-field effect due to the spatial dependence of the electron density.

## III. RESULT AND DISCUSSION

We calculated the band structure, phonon frequencies, electron-phonon and electron-electron interactions, and $T_{\text{c}}$ for fcc $A_3\text{C}_{60}$ with $A = \text{K}, \text{Rb}$ under ambient pressure and $\text{Cs}$ under an optimum pressure of 7 kbar. All of our calculations were performed within the local density approximation using *ab initio* plane-wave pseudopotential calculation codes QUANTUM ESPRESSO. $^{31,32}$ The pseudopotential for $\text{C}$ was generated in the configuration of $(2s)^{2.0}(2p)^{2.0}$, whereas those for $\text{K}$, $\text{Rb}$, and $\text{Cs}$ were generated in the ionized configurations of $(3p)^{6.0}(4s)^{0.0}(3d)^{0.0}$, $(4p)^{6.0}(5s)^{0.0}(4d)^{0.0}$, and $(5p)^{6.0}(6s)^{0.0}(5d)^{0.0}$ with the partial core correction. $^{33}$ The plane-wave energy cutoff was set to 50 Ry. The charge density was calculated with the $4 \times 4 \times 4$ $k$ points in the Monkhorst-Pack grid. Based on the density functional perturbation theory, $^{34}$ phonon dynamical matrices were calculated on the $2 \times 2 \times 2$ $q$ points from the Bloch states on the $4 \times 4 \times 4$ $k$ points using a Gaussian of width 0.025 Ry for the Fermi-surface integration, and the electron-phonon matrix elements were calculated on the $(4 \times 4 \times 4) \times (2 \times 2 \times 2)$ $k \times q$ points. Within the static RPA, the electron dielectric function $\varepsilon$ used for $\mathcal{K}^{\text{el}}$ was calculated on the $3 \times 3 \times 3$ $q$ points from the Bloch states on the $3 \times 3 \times 3$ $k$ points using the tetrahedron linear interpolation $^{35}$ with the Rath-Freeman treatment $^{36}$ considering 129 doubly occupied, three partially occupied, and 218 unoccupied bands. The SCDFT gap equation [Eq. (1)] was solved with the random sampling scheme given in Ref. 37, with which the sampling error in the calculated $T_{\text{c}}$ was approximately 3%: We considered 129 doubly occupied, three partially occupied, and 218 unoccupied bands, and the numbers of sampling $k$ points were 6000 for the $t_{1\text{u}}$ and 100 for the other bands. Particularly, we took care of the convergence of the calculated electronic DOS: On the basis of the fact that the convergence within an order of $0.1/(\text{eV spin})$ with the tetrahedron interpolation is achieved by $16 \times 16 \times 16$ $k$ points, we used the energy eigenvalues of the $t_{1\text{u}}$ states on a supplementary $15 \times 15 \times 15$ $k$ points for the calculation of the dielectric function, and generated the sampling points for solving the gap equation from the energy eigenvalues on $17 \times 17 \times 17$ $k$ points.

We calculated the electron-phonon matrix elements $g_{n\boldsymbol{k},n'\boldsymbol{k}'}^{\nu\mathfrak{q}}$ only for the three partially occupied $t_{1\text{u}}$ bands. Also, we omitted the contribution from the lowest nine phonon branches, some of which show imaginary frequencies in the present accuracy. These nine branches are formed by the acoustic modes, librations, and independent vibrations of alkali-metal atoms in octahedral sites. $^{7}$

We determined the input structural parameters by energy optimization, ignoring the orientational disorder of the $\text{C}_{60}$ molecules. For $A = \text{K}$ and $\text{Rb}$, the lattice constants and atomic configurations were fully relaxed. For $A = \text{Cs}$ under a pressure of 7 kbar, we optimized the atomic configurations for different lattice constants and subsequently derived the corresponding lattice constant from the Murnaghan equation of state. $^{38}$ The calculated (experimental $^{7,39}$) lattice constants were 14.208 (14.240, room temperature), 14.404 (14.420, room temperature), and 14.740 (14.500, $T = 15$ K) $\text{\AA}$ for $A = \text{K}, \text{Rb}, \text{Cs}$ (7 kbar). The relaxed bond lengths of the pentagonal and hexagonal edges, which did not show significant alkali-metal and orientational dependence, were $\sim 1.43$ and $\sim 1.40$ $\text{\AA}$, respectively.

![](./images/813201894246711296_1.jpg)

FIG. 1. (Color online) DOS around the Fermi level. The inset is the view in a broader energy scale, where the characters of the bands are specified.

Let us move onto the calculated DOS of the partially occupied $t_{1\text{u}}$ bands in Fig. 1. The general trend is consistent with the previous calculation based on the generalized gradient approximation and the experimental lattice constants. $^{40}$ As anticipated previously, $^{3,4}$ replacing lighter alkali-metal elements with heavier ones (from $\text{K}$, $\text{Rb}$ to $\text{Cs}$) leads to slightly larger DOS at the Fermi level $N(0)$ (see Table I). More significantly, we also see that the bandwidth becomes narrower. The relation between these changes and the electron-phonon coupling is discussed later.

Table II summarizes our calculated frequencies of the $\Gamma$-point $H_{\text{g}}$-derived modes, which are distinguished as fivefold degenerate branches with strong electron-phonon coupling. The experimentally observed and preceding theoretical frequencies are also given for comparison. The agreement between our calculation and experiments is extremely good, which illustrates that our calculation properly describes the phonon properties of the present system. The alkali-metal

<table>
<caption>Table I. Calculated parameters representing the electronic structure and the electron-phonon and electron-electron interactions.</caption>
<thead>
  <tr>
    <th></th>
    <th>$\text{K}_3\text{C}_{60}$</th>
    <th>$\text{Rb}_3\text{C}_{60}$</th>
    <th>$\text{Cs}_3\text{C}_{60}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$N(0)$ [$/(\text{eV spin})$]</td>
    <td>8.352</td>
    <td>8.609</td>
    <td>9.328</td>
  </tr>
  <tr>
    <td>$\lambda_{N(0)}$</td>
    <td>0.562</td>
    <td>0.570</td>
    <td>0.603</td>
  </tr>
  <tr>
    <td>$\lambda_{N(\xi)}$</td>
    <td>0.489</td>
    <td>0.542</td>
    <td>0.652</td>
  </tr>
  <tr>
    <td>$\omega_{\text{ln},N(0)}$ (K)</td>
    <td>1071</td>
    <td>1054</td>
    <td>1052</td>
  </tr>
  <tr>
    <td>$\omega_{\text{ln},N(\xi)}$ (K)</td>
    <td>932</td>
    <td>944</td>
    <td>940</td>
  </tr>
  <tr>
    <td>$\mathcal{Z}$</td>
    <td>0.350</td>
    <td>0.367</td>
    <td>0.396</td>
  </tr>
  <tr>
    <td>$\mu$</td>
    <td>0.379</td>
    <td>0.370</td>
    <td>0.362</td>
  </tr>
</tbody>
</table>

<table>
<caption>TABLE II. Experimentally observed and theoretically calculated $\Gamma$-point phonon frequencies (cm⁻¹). $H_{\text{g}}(1)$–$H_{\text{g}}(8)$ represent the modes related to the fivefold degenerate $H_{\text{g}}$ modes in the molecular limit (Refs. 1 and 2). The dashes denote the splitting induced by the crystal field.</caption>
<thead>
  <tr>
    <th rowspan="2"></th>
    <th colspan="2">Expt.</th>
    <th colspan="3">Present</th>
    <th colspan="2">Theory</th>
  </tr>
  <tr>
    <th>$\text{C}_{60}$⁠ᵃ</th>
    <th>$\text{K}_{3}\text{C}_{60}$⁠ᵇ</th>
    <th>$\text{K}_{3}\text{C}_{60}$</th>
    <th>$\text{Rb}_{3}\text{C}_{60}$</th>
    <th>$\text{Cs}_{3}\text{C}_{60}$</th>
    <th>$\text{K}_{3}\text{C}_{60}$⁠ᶜ</th>
    <th>$\text{K}_{3}\text{C}_{60}$⁠ᵈ</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$H_{\text{g}}(1)$</td>
    <td>273</td>
    <td>271</td>
    <td>262–271</td>
    <td>261–269</td>
    <td>261–270</td>
    <td>281</td>
    <td>252–258</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(2)$</td>
    <td>437</td>
    <td>431</td>
    <td>422–422</td>
    <td>420–422</td>
    <td>418–421</td>
    <td>454</td>
    <td>407–404</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(3)$</td>
    <td>710</td>
    <td>723</td>
    <td>685–689</td>
    <td>686–688</td>
    <td>687–689</td>
    <td>753</td>
    <td>658–663</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(4)$</td>
    <td>774</td>
    <td></td>
    <td>779–779</td>
    <td>779–780</td>
    <td>779–783</td>
    <td>785</td>
    <td>737–740</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(5)$</td>
    <td>1099</td>
    <td></td>
    <td>1111–1116</td>
    <td>1111–1116</td>
    <td>1113–1120</td>
    <td>1091</td>
    <td>1019–1023</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(6)$</td>
    <td>1250</td>
    <td></td>
    <td>1268–1274</td>
    <td>1268–1273</td>
    <td>1271–1275</td>
    <td>1290</td>
    <td>1137–1136</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(7)$</td>
    <td>1428</td>
    <td>1408</td>
    <td>1403–1408</td>
    <td>1402–1405</td>
    <td>1406–1407</td>
    <td>1387</td>
    <td>1349–1348</td>
  </tr>
  <tr>
    <td>$H_{\text{g}}(8)$</td>
    <td>1575</td>
    <td>1547</td>
    <td>1532–1537</td>
    <td>1532–1536</td>
    <td>1532–1538</td>
    <td>1462</td>
    <td>1532–1530</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="8">ᵃRaman scattering measurement, Ref. 41.</td>
  </tr>
  <tr>
    <td colspan="8">ᵇRaman scattering measurement, Ref. 42.</td>
  </tr>
  <tr>
    <td colspan="8">ᶜAb initio LDA full-potential calculation based on the linearized muffin-tin orbital method, Ref. 43.</td>
  </tr>
  <tr>
    <td colspan="8">ᵈAb initio LDA pseudopotential calculation based on the mixed basis method, Ref. 44.</td>
  </tr>
</tfoot>
</table>

dependence of the frequencies is small, which is due to the intramolecular property of the modes.

We next show in Fig. 2 the $T_{\text{c}}$ calculated by the SCDFT with only the phonon contributions to the gap-equation kernels ($\mathcal{K}^{\text{ph}}$ and $\mathcal{Z}^{\text{ph}}$). The calculated $T_{\text{c}}$ (red solid square) is higher than the experimental $T_{\text{c}}$, which is because of the absence of the electron contribution. These values are consistent with the recent calculation based on the Eliashberg equation¹⁸ by Koretsune and Saito.⁴⁵ Interestingly, the experimentally observed alkali-metal dependence is reproduced. In order to examine the origin of this dependence, we calculated the electron-phonon coupling coefficient $\lambda_{N(0)} = \frac{2}{N(0)} \sum_{\mathbf{k}\mathbf{q}nn'v} \frac{|g_{n'\mathbf{k}+\mathbf{q},n\mathbf{k}}^{\nu\mathbf{q}}|^2}{\omega_{\nu\mathbf{q}}} \delta(\xi_{n\mathbf{k}})\delta(\xi_{n'\mathbf{k}+\mathbf{q}})$ and the characteristic frequency $\omega_{\text{ln},N(0)} = \exp\{\frac{2}{N(0)\lambda_{N(0)}} \sum_{\mathbf{k}\mathbf{q}nn'v} \frac{|g_{n'\mathbf{k}+\mathbf{q},n\mathbf{k}}^{\nu\mathbf{q}}|^2}{\omega_{\nu\mathbf{q}}} \delta(\xi_{n\mathbf{k}})\delta(\xi_{n'\mathbf{k}+\mathbf{q}}) \ln \omega_{\nu\mathbf{q}}\}$ using the set of sampling points. The calculated values are listed in Table I. By replacing lighter alkali-metal elements with heavier ones, $\lambda_{N(0)}$ is slightly enhanced due to the increase of $N(0)$. However, when we substitute $\lambda_{N(0)}$ and $\omega_{\text{ln},N(0)}$ into the McMillan-Allen-Dynes (MAD) formula,⁴⁶ $T_{\text{c}} = \frac{\omega_{\text{ln}}}{1.2} \exp[ -1.04(1+\lambda)/\lambda ]$ (with the Coulomb pseudopotential $\mu^*$ set to 0), the dependence of the resulting $T_{\text{c}}$ (blue open circle) is not as significant as that obtained from the SCDFT. Alternatively, we calculated $\lambda_{N(\xi)}$ and $\omega_{\text{ln},N(\xi)}$ defined by the following formulas:⁴⁷,⁴⁸

$$
\begin{aligned}
\lambda_{N(\xi)}= & \frac{2}{N(0)} \sum_{\substack{\mathbf{k q} \\ n n^{\prime} v}} \frac{\left|g_{n^{\prime} \mathbf{k}+\mathbf{q}, n \mathbf{k}}^{\nu \mathbf{q}}\right|^{2}}{\omega_{\nu \mathbf{q}}^{2}}\left[f_{\beta}\left(\xi_{n \mathbf{k}}\right)-f_{\beta}\left(\xi_{n^{\prime} \mathbf{k}}+\omega_{\nu \mathbf{q}}\right)\right] \\
& \times \delta\left(\xi_{n^{\prime} \mathbf{k}+\mathbf{q}}-\xi_{n \mathbf{k}}-\omega_{\nu \mathbf{q}}\right),
\end{aligned}
\tag{2}
$$

$$
\begin{aligned}
\omega_{\ln , N(\xi)}= & \exp \left\{\frac{2}{N(0) \lambda_{N(\xi)}} \sum_{\substack{\mathbf{k q} \\ n n^{\prime} v}} \frac{\left|g_{n^{\prime} \mathbf{k}+\mathbf{q}, n \mathbf{k}}^{\nu \mathbf{q}}\right|^{2}}{\omega_{\nu \mathbf{q}}^{2}}\left[f_{\beta}\left(\xi_{n \mathbf{k}}\right)\right.\right. \\
& \left.\left.-f_{\beta}\left(\xi_{n \mathbf{k}}+\omega_{\nu \mathbf{q}}\right)\right] \delta\left(\xi_{n^{\prime} \mathbf{k}+\mathbf{q}}-\xi_{n \mathbf{k}}-\omega_{\nu \mathbf{q}}\right) \ln \omega_{\nu \mathbf{q}}\right\},
\end{aligned}
\tag{3}
$$

where $f_{\beta}$ is the Fermi distribution function.⁴⁹ These formulas explicitly treat the energy conservation in electron-phonon scattering, and therefore include the effects of the electronic states within the phonon energy scale; since the scattering involves energy exchanges of order $\lesssim 0.2$ eV, electronic states within this energy range should contribute to the pair formation. As a result, the dependence of the calculated $\lambda_{N(\xi)}$ is more noticeable than that of $\lambda_{N(0)}$, and the corresponding $T_{\text{c}}$ derived from the MAD formula (blue solid circle) well reproduces the dependence of the $T_{\text{c}}$ calculated by the SCDFT and the experimentally observed $T_{\text{c}}$. The present analysis clarifies the significance of the electronic states within the finite energy range, not only at the Fermi level.

![](./images/813201894246711296_2.jpg)

FIG. 2. (Color online) Calculated $T_{\text{c}}$’s: Solid squares denote the values calculated using the SCDFT equation with only the phonon contribution ($\mathcal{K}^{\text{ph}}$ and $\mathcal{Z}^{\text{ph}}$), and open (solid) circles denote the values derived from the MAD formula (see text) using $\lambda_{N(0)}$ ($\lambda_{N(\xi)}$) and $\omega_{\text{ln},N(0)}$ ($\omega_{\text{ln},N(\xi)}$) in Table I. The triangles represent the experimentally observed values.

We also found an important aspect of the mass-renormalization factor $\mathcal{Z} \equiv \mathcal{Z}_{n \mathbf{k}}^{\text{ph}}|_{\xi_{n \mathbf{k}} \to 0}$ given in Table I. In usual cases, $\mathcal{Z}$ is as large as $\lambda_{N(0)}$,²⁵ but our calculated $\mathcal{Z}$ is much smaller than $\lambda_{N(0)}$ or $\lambda_{N(\xi)}$. This is because the $t_{1\text{u}}$ bands are energetically isolated from other bands. The main contribution to the mass renormalization around the Fermi level generally comes from electron scattering to the states distributed within the several times of the Debye frequency. In the present case, however, the energy scale of the Debye frequency is as large as the bandwidth of the $t_{1\text{u}}$ bands, and there is no scattering

![](./images/813201894246711296_3.jpg)

FIG. 3. Calculated gap function for ${\rm Cs_3C_{60}}$ under a pressure of 7 kbar with $T=0.01$ K. The characters of the three bands are specified.

channel in the gapped region (see the inset of Fig. 1). This weak mass renormalization results in relatively higher $T_{\rm c}$ than expected from the conventional calculations. $^{18,46}$

Next let us move on to the results obtained with the electron contribution $(\mathcal{K}^{\rm el})$. The strength of $\mathcal{K}^{\rm el}$ is represented by its Fermi-surface average $\mu=\frac{1}{N(0)}\sum_{n{\bf k}n'{\bf k}'}\mathcal{K}_{n{\bf k}n'{\bf k}'}^{\rm el}\delta(\xi_{n{\bf k}})\delta(\xi_{n'{\bf k}'})$ (see Table I). We display in Fig. 3 the gap function in $T=0.01$ K for $A=$ Cs under a pressure of 7 kbar. The values of the gap function in the $t_{1{\rm u}}$ states are positive, whereas those in the highest doubly occupied $h_{\rm u}$ and the lowest unoccupied $t_{1{\rm g}}$ have a negative sign. Such a sign inversion of the gap function in the high-energy region represents the retardation effect in the SCDFT. $^{25}$ Here, the absolute values in the high-energy region are quite comparable to those in the low-energy region, which signifies the strong retardation effect compared with the previously reported conventional cases. $^{25,27,28}$ This is due to a large interband electron-electron Coulomb interaction. $^{1,2}$

Finally, we show the calculated $T_{\rm c}$ for $A=$ K, Rb, and Cs in Fig. 4 together with the experimentally observed $T_{\rm c}$. Thanks to the energy dependence of the electron-phonon coupling, the alkali-metal dependence of the experimentally observed $T_{\rm c}$ is well reproduced. In spite of the weak mass renormalization and the significant retardation effect, the absolute values are 7.5, 9.0, and 15.7 K, which are approximately $60\%$ lower than the experimentally observed $T_{\rm c}$ (19, 29, and 35 K). Such a huge discrepancy has not been observed in the previous SCDFT calculations. $^{25,27,28}$ In that sense, fullerides behave very differently from what is expected for usual conventional superconductors.

Here, we discuss how the theoretical $T_{\rm c}$ depends on the electron-electron and electron-phonon interactions. With $|g_{n{\bf k},n'{\bf k}'}^{v{\bf q}}|^2$ multiplied by 1.2 (0.8), we obtain $T_{\rm c}=17.5$ (1.5), 20.6 (2.3), and 31.7 (5.0) K for $A=$ K, Rb, and Cs, whereas we obtain $T_{\rm c}=5.8$ (9.6), 7.7 (11.3), and 14.7 (18.0) with $\mathcal{K}^{\rm el}$ multiplied by 1.2 (0.8). Concerning the $ab$ $initio$ calculation of the interactions, on the other hand, a recent paper reported that the electron-phonon interaction is enhanced by approximately $30\%$ by increasing the exchange contribution in the self-consistent calculation of the wave functions. $^{50}$ While a nonempirical $T_{\rm c}$ calculation with such a hybrid-type exchange-correlation functional has yet to be performed, it will be an interesting future subject.

![](./images/813201894246711296_4.jpg)

FIG. 4. (Color online) Calculated $T_{\rm c}$ by solving the SCDFT gap equation with the electron contribution $\mathcal{K}^{\rm el}$ compared with the experimentally observed values.

### IV. SUMMARY AND CONCLUSION

Using the SCDFT, we performed nonempirical calculations of $T_{\rm c}$ in fcc ${\rm A_3C_{60}}$ ($A=$ K, Rb, Cs). We focused on the energy dependence of electron-phonon coupling, the weak mass renormalization, and the strong retardation effect. Our calculated values of $T_{\rm c}$ were 7.5, 9.0, and 15.7 K for $A=$ K, Rb, and Cs (under a pressure of 7 kbar), which are approximately $60\%$ smaller than the experimentally observed values (19, 29, and 35 K). The present results indicate a necessity to go beyond the ME theory based on the KS-LDA even for the regime where $T_{\rm c}$ and $V$ positively correlate.

### ACKNOWLEDGMENTS

The authors thank Takashi Koretsune and Susumu Saito for fruitful discussions. This work was supported by Funding Program for World-Leading Innovative R&D on Science and Technology (FIRST program) on "Quantum Science on Strong Correlation," JST-PRESTO, Grants-in-Aid for Scientific Research (23340095), and the Next Generation Super Computing Project and Nanoscience Program from MEXT, Japan.

$^{1}$O. Gunnarsson, *Alkali-Doped Fullerides: Narrow-Band Solids with Unusual Properties* (World Scientific, Singapore, 2004).

$^{2}$O. Gunnarsson, Rev. Mod. Phys. **69**, 575 (1997).

$^{3}$K. Tanigaki, T. W. Ebbesen, S. Saito, J. Mizuki, J. S. Tsai, Y. Kubo, and S. Kuroshima, *Nature* (London) **352**, 222 (1991).

$^{4}$R. M. Fleming, A. P. Ramirez, M. J. Rosseinsky, D. W. Murphy, R. C. Haddon, S. M. Zahurak, and A. V. Makhija, *Nature* (London) **352**, 787 (1991).

$^{5}$A. Y. Ganin, Y. Takabayashi, Y. Z. Khimyak, S. Margadonna, A. Tamai, M. J. Rosseinsky, and K. Prassides, *Nat. Mater.* **7**, 367 (2008).


$^{6}$Y. Takabayashi, A. Y. Ganin, P. Jeglič, D. Arčon, T. Takano, Y. Iwasa, Y. Ohishi, M. Takata, N. Takeshita, K. Prassides, and M. J. Rosseinsky, *Science* **323**, 1585 (2009).

$^{7}$A. Y. Ganin, Y. Takabayashi, P. Jeglič, D. Arčon, A. Potočnik, P. J. Baker, Y. Ohishi, M. T. McDonald, M. D. Tzirakis, A. McLennan, G. R. Darling, M. Takata, M. J. Rosseinsky, and K. Prassides, *Nature (London)* **466**, 221 (2010).

$^{8}$Y. Ihara, H. Alloul, P. Wzietek, D. Pontiroli, M. Mazzani, and M. Riccò, *Phys. Rev. Lett.* **104**, 256402 (2010); *Europhys. Lett.* **94**, 37007 (2011).

$^{9}$M. Capone, M. Fabrizio, C. Castellani, and E. Tosatti, *Rev. Mod. Phys.* **81**, 943 (2009).

$^{10}$Z. Zhang, C. C. Chen, S. P. Kelty, H. Dai, and C. M. Lieber, *Nature (London)* **353**, 333 (1991).

$^{11}$R. Tycko, G. Dabbagh, M. J. Rosseinsky, D. W. Murphy, A. P. Ramirez, and R. M. Fleming, *Phys. Rev. Lett.* **68**, 1912 (1992).

$^{12}$L. Degiorgi, G. Briceno, M. S. Fuhrer, A. Zetti, and P. Wachter, *Nature (London)* **369**, 541 (1994).

$^{13}$T. W. Ebbesen, J. S. Tsai, K. Tanigaki, J. Tabuchi, Y. Shimakawa, Y. Kubo, I. Hirosawa, and J. Mizuki, *Nature (London)* **355**, 620 (1992).

$^{14}$C. C. Chen and C. M. Lieber, *Science* **259**, 655 (1993).

$^{15}$M. S. Fuhrer, K. Cherrey, A. Zettl, M. L. Cohen, and V. H. Crespi, *Phys. Rev. Lett.* **83**, 404 (1999).

$^{16}$V. A. Stenger, C. H. Pennington, D. R. Buffinger, and R. P. Ziebarth, *Phys. Rev. Lett.* **74**, 1649 (1995).

$^{17}$R. F. Kiefl, W. A. MacFarlane, K. H. Chow, S. Dunsiger, T. L. Duty, T. M. S. Johnston, J. W. Schneider, J. Sonier, L. Brard, R. M. Strongin, J. E. Fischer, and A. B. Smith III, *Phys. Rev. Lett.* **70**, 3987 (1993).

$^{18}$A. B. Migdal, *Sov. Phys. JETP* **7**, 996 (1958); G. M. Eliashberg, *ibid.* **11**, 696 (1960); D. J. Scalapino, in *Superconductivity*, edited by R. D. Parks (Dekker, New York, 1969), Vol. 1; J. R. Schrieffer, *Theory of Superconductivity* (Westview, Boulder, CO, 1971).

$^{19}$D. M. Ceperley and B. J. Alder, *Phys. Rev. Lett.* **45**, 566 (1980).

$^{20}$J. P. Perdew and A. Zunger, *Phys. Rev. B* **23**, 5048 (1981).

$^{21}$S. Y. Savrasov and D. Y. Savrasov, *Phys. Rev. B* **54**, 16487 (1996).

$^{22}$H. J. Choi, D. Roundy, H. Sun, M. L. Cohen, and S. G. Louie, *Nature (London)* **418**, 758 (2002); *Phys. Rev. B* **66**, 020513(R) (2002).

$^{23}$L. Boeri, O. V. Dolgov, and A. A. Golubov, *Phys. Rev. Lett.* **101**, 026403 (2008).

$^{24}$M. Lüders, M. A. L. Marques, N. N. Lathiotakis, A. Floris, G. Profeta, L. Fast, A. Continenza, S. Massidda, and E. K. U. Gross, *Phys. Rev. B* **72**, 024545 (2005).

$^{25}$M. A. L. Marques, M. Lüders, N. N. Lathiotakis, G. Profeta, A. Floris, L. Fast, A. Continenza, E. K. U. Gross, and S. Massidda, *Phys. Rev. B* **72**, 024546 (2005).

$^{26}$P. Morel and P. W. Anderson, *Phys. Rev.* **125**, 1263 (1962); N. N. Bogoliubov, V. V. Tolmachev, and D. V. Shirkov, *A New Method in the Theory of Superconductivity* (Consultants Bureau, New York, 1959).

$^{27}$A. Floris, G. Profeta, N. N. Lathiotakis, M. Lüders, M. A. L. Marques, C. Franchini, E. K. U. Gross, A. Continenza, and S. Massidda, *Phys. Rev. Lett.* **94**, 037004 (2005).

$^{28}$A. Sanna, G. Profeta, A. Floris, A. Marini, E. K. U. Gross, and S. Massidda, *Phys. Rev. B* **75**, 020511(R) (2007).

$^{29}$S. Massidda, F. Bernardini, C. Bersier, A. Continenza, P. Cudazzo, A. Floris, H. Glawe, M. Monni, S. Pittalis, G. Profeta, A. Sanna, S. Sharma, and E. K. U. Gross, *Supercond. Sci. Technol.* **22**, 034006 (2009).

$^{30}$M. S. Hybertsen and S. G. Louie, *Phys. Rev. B* **35**, 5585 (1987); **35**, 5602 (1987).

$^{31}$P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. Fabris, G. Fratesi, S. de Gironcoli, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, *J. Phys.: Condens. Matter* **21**, 395502 (2009); http://www.quantum-espresso.org/.

$^{32}$N. Troullier and J. L. Martins, *Phys. Rev. B* **43**, 1993 (1991).

$^{33}$S. G. Louie, S. Froyen, and M. L. Cohen, *Phys. Rev. B* **26**, 1738 (1982).

$^{34}$S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, *Rev. Mod. Phys.* **73**, 515 (2001).

$^{35}$G. Lehmann and M. Taut, *Phys. Status Solidi* **54**, 469 (1972).

$^{36}$J. Rath and A. J. Freeman, *Phys. Rev. B* **11**, 2109 (1975).

$^{37}$R. Akashi, K. Nakamura, R. Arita, and M. Imada, *Phys. Rev. B* **86**, 054513 (2012).

$^{38}$F. D. Murnaghan, *Proc. Natl. Acad. Sci. U.S.A.* **30**, 244 (1944).

$^{39}$O. Zhou and D. E. Cox, *J. Phys. Chem. Solids* **53**, 1373 (1992).

$^{40}$Y. Nomura, K. Nakamura, and R. Arita, *Phys. Rev. B* **85**, 155452 (2012).

$^{41}$D. S. Bethune, G. Meijer, W. C. Tang, H. J. Rosen, W. G. Golden, H. Seki, C. A. Brown, and M. S. de Vries, *Chem. Phys. Lett.* **179**, 181 (1991).

$^{42}$P. Zhou, K. A. Wang, A. M. Rao, P. C. Eklund, G. Dresselhaus, and M. S. Dresselhaus, *Phys. Rev. B* **45**, 10838 (1992).

$^{43}$V. P. Antropov, O. Gunnarsson, and A. I. Liechtenstein, *Phys. Rev. B* **48**, 7651 (1993).

$^{44}$K. P. Bohnen, R. Heid, K. M. Ho, and C. T. Chan, *Phys. Rev. B* **51**, 5805 (1995).

$^{45}$T. Koretsune and S. Saito (private communication).

$^{46}$P. B. Allen and R. C. Dynes, *Phys. Rev. B* **12**, 905 (1975).

$^{47}$P. B. Allen, *Phys. Rev. B* **6**, 2577 (1972).

$^{48}$M. Casula, M. Calandra, G. Profeta, and F. Mauri, *Phys. Rev. Lett.* **107**, 137006 (2011).

$^{49}$The temperature entering the Fermi distribution function was fixed to 10 K.

$^{50}$J. Laflamme Janssen, M. Côté, S. G. Louie, and M. L. Cohen, *Phys. Rev. B* **81**, 073106 (2010).