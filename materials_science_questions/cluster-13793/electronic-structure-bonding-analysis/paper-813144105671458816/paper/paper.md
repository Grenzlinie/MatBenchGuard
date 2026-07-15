Materials Science in Semiconductor Processing 26 (2014) 79-86

![](./images/813144105671458816_1.jpg)

Contents lists available at ScienceDirect

# Materials Science in Semiconductor Processing

journal homepage: www.elsevier.com/locate/mssp

![](./images/813144105671458816_2.jpg)

# Electronic, optical and bonding properties of $MgYZ_2$
(Y=Si, Ge; Z=N, P) chalcopyrites from first principles

![](./images/813144105671458816_3.jpg)

Sibghat-ullah $^{a}$, G. Murtaza $^{b,*}$, R. Khenata $^{c}$, A.H. Reshak $^{d,e}$

$^{a}$ Department of Physics, Hazara University, Mansehra, Khyber-Pakhtunkhwa, Pakistan
$^{b}$ Materials Modeling Laboratory, Department of Physics, Islamia College University, Peshawar, Pakistan
$^{c}$ LPQ3M Laboratory, Institute of Science and Technology, University of Mascara, Algeria
$^{d}$ New Technologies - Research Center, University of West Bohemia, Univerzitni 8, 306 14 Pilsen, Czech Republic
$^{e}$ Center of Excellence Geopolymer and Green Technology, School of Material Engineering, University Malaysia Perlis, 01007 Kangar, Perlis, Malaysia

---

## ARTICLE INFO

**Keywords:**
Chalcopyrite semiconductors
DFT
Bandstructure
Optoelectronics

## ABSTRACT

The electronic and optical properties of $MgYZ_2$ (Y=Si, Ge; Z=N, P) compounds are carried out using first-principle calculations within the density functional theory. The calculations show close correspondence to the available experimental data compared to the previous theoretical calculations. Band gap decreases by changing the cations Y from Si to Ge as well as Z from N to P in $MgYZ_2$. The N/P p-states contribute majorly in the density of states. Bonding nature of the herein studied compounds is predicted from the electron density plots. Optical response of these compounds is noted from the complex refractive index, reflectivity and optical conductivity. The direct band gap and the high reflectivity of these compounds in the visible and ultraviolet regions of electromagnetic energy spectrum ensure their applications in optoelectronic and photonic domains.

© 2014 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

II-IV-$V_2$ chalcopyrite's semiconductors generally crystal- lize in tetragonal structure with space group $I\overline{4}2d(D_{2D}^{12})$. These compounds attracted considerable attention by offering remarkable and promising properties for photovoltaics due to their direct band gap, high optical absorption coefficient and interesting defects. Chalcopyrites are promising materials for spintronics, electronics and optoelectronics applications such as solar energy converters, infrared detectors, visible and invisible light emitting diodes, up convertors and optical parametric oscillators [1-8].

Over the past years the properties of $ABC_2$ type ternary chalcopyrites have been extensively studied. $MgYP_2$ (Si, Ge) compounds exist in chalcopyrite structure while $MgYN_2$ (Si, Ge) crystallizes in orthorhombic structure, however they can also synthesized in a chalcopyrite phase [1,9]. In spite of considerable work devoted to these materials their knowl- edge is still incomplete. Till now, no detailed study has appeared for $MgYZ_2$ (Y=Si, Ge; Z=N, P) chalcopyrite semi- conductors. Only few attempts were done for electronic and optical structures of $MgYZ_2$; Chiker et al. [1] investigated the electronic and optical properties of $MgSiP_2$ and $MgGeP_2$. The reported band structure profile was much less than the experimental measured values. Fang et al. [10] investigated the structural phase transition in $MgSiN_2$ compound by using the ultrasoft pseudo-potential method. In another report, Fang et al. [11] performed ab initio band structure calculation for $MgSiN_2$ and $Mg_3N_2$. They found that both compounds are direct band gap semiconductors. Basalaev and Demushin [12] studied the electronic structure and chemical bonding properties of $MgBX_2$ (B=Si, Ge, Sn; X=P,

---

* Corresponding author. Tel.: +92 321 6582416.
E-mail address: murtaza@icp.edu.pk (G. Murtaza).

http://dx.doi.org/10.1016/j.mssp.2014.03.053
1369-8001/© 2014 Elsevier Ltd. All rights reserved.

<table><thead><tr><th rowspan="2">Compound</th><th colspan="2">Latt. Cons.</th><th rowspan="2">u</th><th rowspan="2">$R_{MT}$</th><th rowspan="2">$R_{MT}$–$K_{max}$</th><th rowspan="2">l-max</th><th rowspan="2">K-points</th></tr><tr><th>$a$ (Å)</th><th>$c$ (Å)</th></tr></thead><tbody><tr><td>$MgSiN_{2}$</td><td>$4.44^{b}$</td><td>$8.702^{b}$</td><td>$0.31^{b}$</td><td>$Si=1.72, Mg=1.67, N=1.67$</td><td>7</td><td>10</td><td>99</td></tr><tr><td>$MgGeN_{2}$</td><td>$4.69^{c}$</td><td>$9.89^{c}$</td><td>$0.27^{c}$</td><td>$Ge=1.86, Mg=1.77, N=1.77$</td><td>7</td><td>10</td><td>99</td></tr><tr><td>$MgSiP_{2}$</td><td>$5.72^{a}$</td><td>$10.094^{a}$</td><td>$0.29^{a}$</td><td>$Si=2, Mg=2, P=2$</td><td>7</td><td>10</td><td>99</td></tr><tr><td>$MgGeP_{2}$</td><td>$5.652^{a}$</td><td>$10.115^{a}$</td><td>$0.30^{a}$</td><td>$Ge=2,Mg=2, P=1.92$</td><td>7</td><td>10</td><td>99</td></tr></tbody><tfoot><tr><td colspan="8">$^{a}$ Ref. [1].</td></tr><tr><td colspan="8">$^{b}$ Ref. [2].</td></tr><tr><td colspan="8">$^{c}$ Ref. [3].</td></tr></tfoot></table>

As, Sb) compounds with the chalcopyrite lattice as well as the study of $MgYN_{2}$ (Si, Ge) orthorhombic crystals, in which band structure of tetrahedral and orthorhombic crystals were discussed. Ouahrani [13] studied the thermodynamic and electronic properties of $MgSiP_{2}$. In the latter study, the author elucidates that $MgSiP_{2}$ undergoes a structural phase transition from chalcopyrite to the NaCl structure under pressure effects. Petukhov et al. [2] reported on the electronic structure of $MgSiN_{2}$ but give no detail for optical properties. Therefore, we think that it is timely to perform first-principles calculations on these properties, using the state of the art full-potential augmented plane wave plus local orbitals approach (FP-APW+lo) based on the density functional theory (DFT) [14,15].

The rest of the paper has been divided into three parts. In Section 2, we briefly describe the computational techniques used in this study. The most relevant results obtained for the electronic and optical properties for $MgYZ_{2}$ (Y=Si, Ge; Z=N, P) compounds are presented and discussed in Section 3. Finally, in Section 4 we summarize the main conclusions of our work.

## 2. Computational details

Present calculations were performed with the full potential linearized augmented plane wave plus local orbital (FP-LAPW+lo) method [16] based on DFT as implemented in wien2K package [17]. The exchange-correlation effects were calculated using the Engel-Vosko GGA (EV) scheme [18]. Different computational parameters, $R_{MT}$ $K_{max}$ (where $R_{MT}$ is the minimum muffin-tin radii and $K_{max}$ gives the magnitude of largest $K$ vector in the plane wave basis), $G_{max}$ (the potential and the charge density Fourier expansion parameter), $l$ (the valence wave functions inside the atomic muffin-tin-spheres expansion parameter) and $K$-points in the irreducible wedge of the first Brillouin zone (IBZ) that have been explored within the tetrahedron method [19] are given in Table 1. The self-consistency was achieved up to 0.001 Ry. The electronic and optical properties are calculated using the experimental lattice parameters given in Table 1.

## 3. Results and discussion

The $MgYZ_{2}$ (Y=Si, Ge; Z=N, P) compounds crystallize in chalcopyrite structure at normal growth conditions. The chalcopyrite structure of these compounds is shown in Fig. 1. As seen in the figure, the Mg atoms occupies (0, 0, 0) and (0, 1/2,1/4) sites, the Y cations occupy (0, 0, 1/2), (0, 1/2,3/4) sites, and Z atom occupies (u, 1/4, 1/8), (−u, 3/4,1/8), (3/4, u, 7/8), (1/4, −u,7/8) sites. This section describes the electronic and optical properties performed at the experimental lattice parameters.

![](./images/813144105671458816_4.jpg)

Fig. 1. Chalcopyrite structure of $MgYZ_{2}$.

The electronic properties of $MgYZ_{2}$ (Y=Si, Ge; Z=N, P) compounds in the chalcopyrite structure are studied via calculating the band structure and density of states. The calculated energy band structures along the high symmetry directions in the first Brillouin zone within the EV-GGA approximation are shown in Fig. 2. The zero energy is chosen to coincide with the top of valence band. From this figure it is clear that the overall band structure profile for both the valence band maximum (VBM) and conduction band minimum (CBM) are located at the ($\Gamma$) point, resulting a direct band gap ($\Gamma$-$\Gamma$) of 4.8 eV, 2.5 eV, 2.08 eV and 1.5 eV for $MgSiN_{2}$, $MgGeN_{2}$, $MgSiP_{2}$ and $MgGeP_{2}$, respectively. It is further seen that the replacement of Si by Ge reduces the band gap energy. This reduction is also observed by changing the anion Z from N to P. The reduction in the band gap by changing the anion and cation

![](./images/813144105671458816_5.jpg)

Fig. 2. Band structures of MgSiN₂, MgGeN₂, MgSiP₂ and MgGeP₂.

can be attributed to the increasing number of atomic numbers. Also the valence bandwid th of the MgSiN₂ and MgGeN₂ compounds is smaller than that of MgSiP₂ and MgGeP₂. The calculated values of the direct band gap for these compounds within GGA and EV-GGA are listed in Table 2 along with the experimental values and other theoretical calculations. It is seen that the GGA calculated band gaps are much lower than the experiment ones. The calculated band gaps with EV-GGA are in excellent agree- ment with the experimental measured data and show a significant improvement over the previously calculated results [1,3].

The contribution of different states in the band struc- ture can be elucidated from the density of states (DOS). Total and partial densities of states for MgYZ₂ are plotted in Fig. 3. The pattern of the DOS is almost similar in all compounds; however the bands are shifted towards Fermi

<table><caption>Table 2 Calculated bandgaps (in eV) along with experimental and other works.</caption>
<thead>
  <tr>
    <th>Compounds</th>
    <th colspan="2">This work</th>
    <th>Experimental</th>
    <th>Others</th>
  </tr>
  <tr>
    <th></th>
    <th>GGA</th>
    <th>EV</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>MgSiN₂</td>
    <td>4.8</td>
    <td>4.87</td>
    <td>–</td>
    <td>3.79ᵇ</td>
  </tr>
  <tr>
    <td>MgGeN₂</td>
    <td>2.5</td>
    <td>2.54</td>
    <td>–</td>
    <td>3.33ᵇ</td>
  </tr>
  <tr>
    <td>MgSiP₂</td>
    <td>2.08</td>
    <td>2.18</td>
    <td>2.2ᵃ, 2.3ᵃ</td>
    <td>1.71ᵃ, 1.15ᵃ, 2.12ᶜ</td>
  </tr>
  <tr>
    <td>MgGeP₂</td>
    <td>1.5</td>
    <td>1.6</td>
    <td>1.6ᵃ</td>
    <td>1.39ᵃ</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="5">ᵃ Ref. [1].</td>
  </tr>
  <tr>
    <td colspan="5">ᵇ Ref. [3].</td>
  </tr>
  <tr>
    <td colspan="5">ᶜ Ref. [13].</td>
  </tr>
</tfoot>
</table>

level in MgSiP₂ and MgGeP₂ compared to other com- pounds. The first band from the left is mainly occupied by the Z-s states. The next band below the Fermi level ($E_F$)

![](./images/813144105671458816_6.jpg)

Fig. 3. Total and partial density of states of MgYZ₂.

![](./images/813144105671458816_7.jpg)

Fig. 4. Electron charge density of MgYZ₂ in the (111) plane.

is the valence band (VB). The lower part of VB is mainly composed on p-states of anion Z. The upper part of the VB consists of Y and Z-p states. The bands above $E_F$, are the conduction band (CB). These bands are mainly composed of unoccupied Y and Z-p states.

Nature of bonding among the cations and anions can be studied from the electronic charge density. The electronic charge density in the (111) plane for MgYZ₂ compounds is plotted in Fig. 4. The distribution of the electronic densities of cations Y and anions Z reveals that there is sharing of charge, hence the compounds are covalent in nature. This covalence is mainly due to the sp-hybridization of the anions and cations. It is further noticed that the covalent behavior increases among XZ as we replace the cations

from Si to Ge or N to P. A very small sharing of electron density among Mg and Z is also observed. So the bonding among MgZ is mostly ionic with small covalent character. Overall the bonding nature of $MgYZ_2$ compounds is mixed covalent and ionic.

Optical properties of materials provide useful information about their internal structures. Keeping this in mind we investigate the refractive index, reflectivity and optical conductivity of the herein studied compounds.

The complex refractive index $n(\omega)$ and extinction coefficient $k(\omega)$ are given by the following expressions:

$$
n(\omega)=\frac{1}{\sqrt{2}}\left[\left\{\varepsilon_{1}(\omega)^{2}+\varepsilon_{2}(\omega)^{2}\right\}^{1 / 2}+\varepsilon_{1}(\omega)\right]^{1 / 2} \tag{1}
$$

$$
k(\omega)=\frac{1}{\sqrt{2}}\left[\left\{\varepsilon_{1}(\omega)^{2}+\varepsilon_{2}(\omega)^{2}\right\}^{1 / 2}-\varepsilon_{1}(\omega)\right]^{1 / 2} \tag{2}
$$

The real and imaginary parts of dielectric function, $\varepsilon_{1}(\omega)$ and $\varepsilon_{2}(\omega)$, are calculated by the following relations [20]:

$$
\varepsilon_{2}(\omega)=\frac{8}{2 \pi \omega^{2}} \sum_{n \dot{n}} \int\left|P_{n \dot{n}}(k)\right|^{2} \frac{d S_{k}}{\nabla \omega_{n \dot{n}}(k)} \tag{3}
$$

$$
\varepsilon_{1}(\omega)=1+\frac{2}{\pi} P \int_{0}^{\infty} \frac{\dot{\omega} \varepsilon_{2}(\dot{\omega})}{\dot{\omega}^{2}-\omega^{2}} d \dot{\omega} \tag{4}
$$

where $P_{n \dot{n}}(k)$ is the dipole matrix element between initial and final states, $S_{k}$ is an energy surface with constant value, $\omega_{n \dot{n}}(k)$ is the energy difference between two states and $P$ denotes the principal part of the integral.

Real and imaginary parts of refractive index are further used in the following relation to evaluate normal incident reflectivity:

$$
R(\omega)=\left|\frac{\tilde{n}-1}{\tilde{n}+1}\right|=\frac{(n-1)^{2}+k^{2}}{(n+1)^{2}+k^{2}} \tag{5}
$$

Similarly frequency dependent optical conductivity $\sigma(\omega)$ are calculated by the following relation:

$$
\sigma(\omega)=2 W_{e v} \hbar \omega / \vec{E}_{0} \tag{6}
$$

where $W_{e v}$ is the transition probability per unit time.

Optical response of these compounds is studied using optical code of Ambrosch-Draxl and Sofo [21] as implemented in Wien2k [17]. Complex refractive index $(\tilde{n}(\omega)=n(\omega)+i k(\omega))$ describes the refraction as well as well absorption of the compounds. It consists of two parts; the real part, $n(\omega)$, is just the ordinary refractive index while another part, $k(\omega)$, is the extinction coefficient which describes the loss of photon energy when it propagate through the optical medium. As these compounds have tetragonal symmetry, two tenser components (parallel and perpendicular to the $c$-axis corresponding to the electric field) are required to completely describe the optical properties. The parallel and perpendicular components of refractive index ($n_{\|}$and$n_{\perp}$) and extinction

![](./images/813144105671458816_8.jpg)

Fig. 5. Refractive index as a function of energy for $MgYZ_2$ (Y=Si, Ge; Z=N, P).

coefficient ($k_{\parallel}$ and $k_{\perp}$) as a function of energy are plotted in Fig. 5 for $MgYZ_2$ ($Y=$Si, Ge; $Z=$N, P). From Fig. 5, it can be seen that $n_{\parallel}(0)$ and $n_{\perp}(0)$ at zero frequency show the static refractive index. They increase beyond the zero frequency limits and reached to their maximum values. Beyond the maximum value they start to decrease and with few oscillations they go beyond unity. In this region ($n<1$) the phase velocity of the photons increases to universal constant $C$. However the group velocity is always less than $C$; therefore the relativity relations are not effected [20]. It is further seen that the peaks in the spectra shifted towards lower energy by changing the cations from Si to Ge. The variation is in accordance to the decrease in the bandgaps. The calculated values of zero frequency refractive index ($n_{\parallel}(0)$ and$n_{\perp}(0)$), their maximum values ($Max.n_{\parallel}(\omega)$ and $Max.n_{\perp}(\omega)$), birefringence ($\Delta n(0)$) and anisotropy among the parallel and perpendicular parts of the refractive index are given in Table 3.

It is further noted that the birefringence $\Delta n(0)$ is maximum in $MgSiP_2$ compared to other compounds.

Extinction coefficient $k(\omega)$ shows the absorption of materials. The absorption is due to the interband transition of the electrons from the valence band to the unoccupied states of conduction band. It is observed from the absorption spectra that the absorption edge of $MgSiN_2$, $MgGeN_2$, $MgSiP_2$ and $MgGeP_2$ are located at 5.19 (5.00), 2.73 (2.78), 2.34(2.47) and 2.10 (2.15) for $k_{\parallel}$ and $(k_{\perp})$, respectively. These are in accordance with the variation of the bandgap which decreases by changing the cation Y as well as Z from top to bottom of the periodic table. The absorption edge corresponds to the transition of the electrons from the top of the valence band to the bottom of the conduction band at the $\Gamma$ point. Beyond the critical points, the absorption increases and becomes maximum at some particular energy, and then it decreases with small oscillations. The

<table>
<caption>Table 3 Calculated zero frequency refractive index, $n(0)$, maximum refractive index, $n(\omega)$, and anisotropy range.</caption>
<thead>
<tr>
<th>Compounds</th>
<th>$n_{\parallel}(0)$</th>
<th>$n_{\perp}(0)$</th>
<th>$\Delta n(0)$</th>
<th>Max.$n_{\parallel}$</th>
<th>Max.$n_{\perp}$</th>
<th>Anisotropy range</th>
</tr>
</thead>
<tbody>
<tr>
<td>$MgSiN_2$</td>
<td>1.90</td>
<td>1.9013</td>
<td>0.0013</td>
<td>2.7224</td>
<td>2.7326</td>
<td>6.45–19.5</td>
</tr>
<tr>
<td>$MgGeN_2$</td>
<td>2.16</td>
<td>2.18</td>
<td>0.02</td>
<td>2.733</td>
<td>2.8745</td>
<td>4.27–19.0</td>
</tr>
<tr>
<td>$MgSiP_2$</td>
<td>2.826</td>
<td>2.952</td>
<td>0.126</td>
<td>3.8023</td>
<td>4.1936</td>
<td>2.92–10.26</td>
</tr>
<tr>
<td>$MgGeP_2$</td>
<td>3.065</td>
<td>3.030</td>
<td>−0.035</td>
<td>4.0714</td>
<td>4.103</td>
<td>2.15–12.7</td>
</tr>
</tbody>
</table>

![](./images/813144105671458816_9.jpg)

Fig. 6. Reflectivity as a function of energy for $MgYZ_2$ ($Y=$Si, Ge; $Z=$N, P).

compounds $MgSiN_2$, $MgGeN_2$, $MgSiP_2$ and $MgGeP_2$ show high absorption in the range 7.55-18.80 eV, 3.84-12.38 eV, 3.79-11.75 eV, and 2.53-9.73 eV, respectively. However large anisotropy is seen in this energy range while the parallel and perpendicular parts are isotropic in the lower and upper energy range. It is further noted that the absorption shifts towards lower energy by changing the cations from Si to Ge for $MgSiN_2$, $MgGeN_2$ and $MgSiP_2$, $MgGeP_2$. Similar trend is also observed by changing the anion N to P.

Frequency dependent reflectivity $R(\omega)$ of the compounds is calculated and depicted in Fig. 6 for $MgYZ_2$ (Y=Si, Ge; Z=N, P) along parallel $R_{||}(\omega)$ and perpendicular $R_{\perp}(\omega)$ to the $c$-axis. The reflectivity spectra of these compounds start from the zero frequency which is the static part of the reflectivity. Beyond the zero frequency limit it increases and with some oscillations and becomes maximum and then decreases and vanishes at high energy.

The zero frequency limits and its maximum values are given in Table 4 along with the energy range in which it is maximum and highly anisotropic. In view of the table it is clear that the zero frequency limit of $R_{||}(\omega)$ and $R_{\perp}(\omega)$ increases by changing the cation Si to Ge as well as anion N to P. The compounds $MgSiP_2$ and $MgGeP_2$ show reflectivity over 50%, therefore these compounds can be effectively used for the shielding of high frequency ultraviolet radiations.

Optical conductivity parameter provides the conductivity of electrons under the photon field. The optical conductivity of $MgYZ_2$ (Y=Si, Ge; Z=N, P) along parallel $(\sigma_{||}(\omega))$ and perpendicular $(\sigma_{\perp}(\omega))$ to the $c$-axis is shown in Fig. 7. The conduction starts at a particular energy (critical point). The critical points are mentioned in Table 5. The critical points are in close agreement to the band gap calculated from the band structure. Beyond the critical points the conductivity increases and become

<table>
<caption>Table 4<br>Calculated zero frequency reflectivity, $R(0)$, maximum reflectivity, Max. $R$, maximum reflectivity range and anisotropy range.</caption>
<thead>
<tr>
<th>Compounds</th>
<th>$R_{||}(0)(\%)$</th>
<th>$R_{\perp}(0)(\%)$</th>
<th>Max.$R_{||}(\%)$</th>
<th>Max.$R_{\perp}(\%)$</th>
<th>Max. $R$ range</th>
<th>Anisotropy range</th>
</tr>
</thead>
<tbody>
<tr>
<td>$MgSiN_2$</td>
<td>9.71</td>
<td>9.65</td>
<td>31.23</td>
<td>35.06</td>
<td>6.80-21.12</td>
<td>7.46-24.9</td>
</tr>
<tr>
<td>$MgGeN_2$</td>
<td>13.61</td>
<td>13.77</td>
<td>33.86</td>
<td>35.00</td>
<td>3.99-18.94</td>
<td>4.20-22.63</td>
</tr>
<tr>
<td>$MgSiP_2$</td>
<td>22.78</td>
<td>24.40</td>
<td>59.41</td>
<td>57.73</td>
<td>3.05-16.95</td>
<td>3.11-16.83</td>
</tr>
<tr>
<td>$MgGeP_2$</td>
<td>25.81</td>
<td>25.38</td>
<td>58.32</td>
<td>50.57</td>
<td>2.33-16.83</td>
<td>2.09-15.98</td>
</tr>
</tbody>
</table>

![](./images/813144105671458816_10.jpg)

Fig. 7. Conductivity as a function of energy for $MgYZ_2$ (Y=Si, Ge; Z=N, P).

<table><caption>Table 5
Calculated critical point (in eV), maximum conductivity, Max . $\sigma(\omega)$, (in $\Omega^{-1} \mathrm{~cm}^{-1}$) and anisotropy range (in eV).</caption>
<tbody>
<tr>
<td>Compounds</td>
<td>Critical point</td>
<td>Max.$\sigma_{||}(\omega)$</td>
<td>Max.$\sigma_{\perp}(\omega)$</td>
<td>Anisotropy range</td>
</tr>
<tr>
<td>$\mathrm{MgSiN}_{2}$</td>
<td>4.71</td>
<td>6529.22</td>
<td>7393.16</td>
<td>7.50-22.83</td>
</tr>
<tr>
<td>$\mathrm{MgGeN}_{2}$</td>
<td>2.55</td>
<td>5396.37</td>
<td>5132.68</td>
<td>2.60-20.84</td>
</tr>
<tr>
<td>$\mathrm{MgSiP}_{2}$</td>
<td>2.20</td>
<td>9833.25</td>
<td>10905.2</td>
<td>3.70-11.13</td>
</tr>
<tr>
<td>$\mathrm{MgGeP}_{2}$</td>
<td>1.92</td>
<td>11042.3</td>
<td>8441.14</td>
<td>2.34-13.20</td>
</tr>
</tbody>
</table>

maximum at a particular energy beyond this it again decreases and vanishes at high energy where electrons not respond to the very high frequency radiations. The maximum conductivity and the anisotropy ranges are given in Table 5. It is noted that the conductivity of $\mathrm{MgGeZ}_{2}$ compounds is larger than that of $\mathrm{MgSiZ}_{2}$.

### 4. Conclusions

We applied the highly accurate FP-LAPW+lo method within the EV-GGA to predict the physical properties of $\mathrm{MgYZ}_{2}$ (Y=Si, Ge; Z=N, P) compounds. The conclusions are that the compounds have wide and direct bandgaps. The P-states of N and P have high density of states in these compounds. All the compounds have a mixed covalent and ionic bonding nature. The birefringence is predicted to be higher for $\mathrm{MgSiP}_{2}$ compound. Reflectivity in these compounds is found to be high in the visible and ultraviolet regions of energy spectrum. Based on their direct bandgaps and unique optical properties these materials are very useful for the applications in photonics, optoelectronics and optics.

### Acknowledgments

Author (R. Kh.) acknowledges the financial support by the Deanship of Scientific Research at King Saud University for funding the work through the Research Group Project NO RPG-VPP-088. For the author A.H. Reshak the result was developed within the CENTEM project, reg. no. CZ.1.05/2.1.00/03.0088, co-funded by the ERDF as part of the Ministry of Education, Youth and Sports OP RDI program.

### References

[1] F. Chiker, Z. Kebbab, R. Miloua, N. Benramdane, Solid State Commun. 151 (2011) 1568-1573.
[2] A.G. Petukhov, W.R.L. Lambrecht, B. Segall, Phys. Rev. B 49 (1994) 4549.
[3] L.C. Tang, Y.C. Chang, J.Y. Huang, C.S. Chang, Proc. SPIE 7056 (2008) 705605.
[4] J.L. Shay, J.H Wernick, Ternary Chalcopyrite Semiconductors" Growth, Electronics Properties and ApplicationsPergamon, Oxford, 1975.
[5] M.V. Schilfgaarde, T.J. Coutts, N. Newman, T. Peshek, Appl. Phys. Lett. (2010)143503-3.
[6] G.S. Solomon, J.B. Posthill, M.L. Timmons, Appl. Phys. Lett. 55 (1989) 1531-1533.
[7] A. Rockett, R.W. Birkmire, J. Appl. Phys. 70 (1991) 81.
[8] S. Choi, G.B. Cha, S.C. Hong, S. Chao, Y. Kim, J.B. Kettrson, S.Y Jeong, G.C. Yi, Solid State Commun. 122 (2002) 165-167.
[9] J.E. Vannostrand, J.D. Albrecht, R. Cortez, K.D. Leedy, B. Johnson, M.J. O'Keede, J. Electron. Mater. 34 (2005) 1349.
[10] C.M. Fang, H.T. Hintzen, G. Dewith, Appl. Phys. A 78 (2004) 717-719.
[11] C.M. Fang, R.A. de Groot, R.J. Bruls, H.T. Hintzen, G. de With, J. Phys.: Condens. Matter 11 (1999) 4833-4842.
[12] Y.M. Basalaev, P.V. Demushin, J. Struct. Chem. 51 (2010) 1191-1194.
[13] T. Ouahrani, Eur. Phys. J. B 86 (2013) 369.
[14] P. Hohenberg, W. Kohn, Phys. Rev. B 136 (1964) 864.
[15] W. Kohn, L.J. Sham, Phys. Rev. A 140 (1965) 1133.
[16] E. Sjostedt, L. Nordstrom, D.J. Singh, Solid State Commun. 114 (2000) 15.
[17] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz, WIEN2K, An Augmented Plane Wave +Local Orbitals Program for Calculating Crystal PropertiesTechnische Universitat, Wien, Austria, ISBN 3-9501031-1-2, 2001.
[18] E. Engel, S.H. Vosko, Phys. Rev. B 47 (1993) 13164.
[19] P.E. Blochl, O. Jepsen, O.K. Anderson, Phys. Rev. B 49 (1994) 16223.
[20] M. Fox, Optical Properties of Solids, Oxford University Press, Oxford, UK, 2001.
[21] C. Ambrosch-Draxl, J. Sofo, Comput. Phys. Commun. 175 (2006) 1.