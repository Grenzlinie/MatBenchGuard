# Theoretical and Experimental Demonstration of Electronic State of GeO₂

H. –C. Chang¹, S. –C. Lu², W. –C. Chang², T. –P. Chou², H. –S. Lan¹, C. –M. Lin¹, and C. W. Liu¹,²

¹Department of Electrical Engineering and Graduate Institute of Electronic Engineering,
National Taiwan University, Taipei, Taiwan
²Department of Electrical Engineering and Graduate Institute of Photonics and
Optoelectronics, National Taiwan University, Taipei, Taiwan

The transition levels of oxygen vacancy (Vo) in GeO₂ with different charge state are calculated by first principle method. The formation energy of GeO₂ indicates there is a (+2/0) fix charge state in bulk GeO₂. The (+1/0) transition level near Ge valence band maximum which shows positive charge trap of GeO₂. We demonstrate a Ge MOS capacitor with thermal oxidation. The hysteresis of CV shows a negative V<sub>fb</sub> shift which corresponds to the positive charge trap as theoretical calculation implies.

## Introduction

To approach high mobility channel metal-oxide-semiconductor field-effect transistors (MOSFETs), Ge has been regarded as a new channel material candidate. An important issue concerning Ge-MOSFETs is the electrical condition of the Ge/gate dielectric interface. Germanium oxide (GeO₂) is used as the potential passivation layer since the surface interface states densities are reduced effectively (1) by the methods of thermal oxidation (2). The electronic structure of Ge/GeO₂ interface models including a suboxide transition region did not reveal any defect level within the Ge band gap (3), suggesting that the suboxide itself should not be invoked as the cause of electrical degradation. In this work, we investigate the structure of GeO₂ with oxygen vacancy creation. The GeO₂ growth with furnace is also implemented.

## Models

First-principles calculations based on density functional theory were performed for the GeO₂. A α-phase quartz-like structure of GeO2 was chosen and the lattice parameters were rescaled prior to the structure relaxation to match the density of amorphous GeO₂ (3.6 g/cm³) (4). The structures were relaxed by using the CASTEP plane-wave pseudopotential total energy code (5). The fraction of Hartree–Fock exchange was set to be α=0.25 (PBE0) to provide good estimation for bandgap of GeO₂ (5.8 eV). The cut-off energy of the plane wave basis set was 550 eV and the k-points set was restricted to Γ point. We optimized atomistic structure for all atoms by PBE until the remaining force on each atom was below 0.01 eV/Å. To investigate the oxygen vacancy characteristic in the GeO₂ bulk, the oxygen was removed to create an oxygen vacancy. The deficiency of O will form Ge dangling bond (DB) in the 72-atom cell structure.

### Experiments

(100)-oriented p-type Ge wafers (Ga-doped with the resistivity of 0.2-0.5 Ω-cm) were used. The Ge wafers were cleaned by acetone with de-ionized water rinse to remove organic impurities, and then were dipped diluted 2% hydrofluoric acid in deionized water to remove Ge native oxides before the thermal oxidation. Subsequently, GeO₂ was formed by thermal oxidation at 500 °C. After GeO₂ formation, Al was used as the gate electrode with the area of 3×10⁻⁴ cm⁻² on the GeO₂ layer, and Al was evaporated on the Ge as back contact to form metal-oxide-semiconductor (MOS) capacitor for interface defect (Dᵢₜ) measurement.

![](./images/813371887106129920_1.jpg)

Fig. 1: GeO₂ with E' center is generated. The oxygen vacancy will form a three-fold oxygen after relaxation.

### Results and Discussions

The oxygen atom is removed from perfect cell structure as Fig.1 shows. To investigate different charge states with the defect structure, the charges are removed from the supercell system. Defect levels strongly impact the performance of semiconductor devices. In a MOS device, the Fermi level is located in the vicinity of the band gap of the semiconductor material, establishing the charge states of defects in the dielectric. There are levels involving transitions between different charge states of the same defect. Even if a defect does not have a charge-state transition level near the semiconductor band gap, its overall charge may still impact device performance, since the associated charge may induce carrier scattering and shift the threshold voltage of the device. The relaxation of the GeO₂ with oxygen vacancy after removing 2 electrons forms a three-fold coordinated oxygen and an unoccupied Ge dangling bond. The formation energy of the Ge dangling bond in different charge state is defined as

$$
E^{f}\left(V_{0}^{q}\right)=E_{t o t}\left(V_{0}^{q}\right)-E_{t o t}\left(G e O_{2}\right)+\mu_{0}+q\left(E_{f}-E_{v}\right) \tag{1}
$$

, where $E_{tot}(V_0^q)$ is the total energy of the supercell containing the vacancy, and $E_{tot}(GeO_2)$ is the total energy of $GeO_2$ perfect crystal in the same supercell. $q$ denote charge state (0, +1, +2) in this model. $\mu_0$ is half of the chemical potential of $O_2$ molecule. In Fig. 2, we show the formation energy for each charge state as a function of Fermi-level position. This figure gives us information on the defects that may introduce fix charge in MOS devices. If The oxygen vacancy has transition level far away from the semiconductor band edges, it will occur in fixed highly charged states. From Fig. 2, it shows the (2+/0) transition level well above conduction-band minimum (CBM) of Ge. The $GeO_2$ is aligned with Ge by VBO=3.6~4.5 eV (6-9) with different process conditions and models. The Ge DBs will be always above Fermi level and thus positively charged.

![](./images/813371887106129920_2.jpg)

Fig. 2: Formation energy of different charge state (0, +1, +2).

Charge-state switching levels are important for determining the properties of defects in MOS-dielectrics, since carrier-defect transfer processes happen on much shorter time scales than atomic relaxation (10). The charge-state switching levels were obtained by fixing the atomic configuration, and then either adding or removing an electron to determine the switching level. With fixed $q$=0 atomic cell structure, and define the switching level as:

$$
(q / q')=\frac{E_{tot}\left(V^{q}\right)-E_{tot}\left(V^{q'}\right)}{q'-q}-E_{v} \tag{2}
$$

$E_{tot}\left(V^{q}\right)$ is the the total energy of the defect cell in charge state $q$, and $E_v$ is the valence band maximum extracted from neutral defect cell. The level determined by considering the defect in the final charge state ($q$=+1) but calculated in the same atomic cell structure

as in the initial charge state ($q$=0) is 3.31eV. The defect level of three-fold Ge is located near the Ge VBM, which could be a trap center for hole.

The $C$-$V$ measurement is carried out using an HP 4284A impedance analyzer. Fig. 3 shows the $C$-$V$ characteristics under different bias conditions of same $GeO_2$ MOSCAP. We can obtain the oxide growth rate of the p-Ge wafer from the equivalent oxide thickness. The growth rate become slower with increasing oxide thickness due to the limitation of oxygen diffusion. To extract the Qit, we plot the flat band voltage versus the equivalent oxide thickness in Fig. 3. The result of n-type Ge is also shown in the figure. And since we only consider the variation between the flat band voltages of each sample, The flat band voltage shift can be derived to:

$$
\Delta V_{F B}=\left(\frac{\Delta Q_{e f f}+\Delta Q_{i t}\left(\psi_{S}=0\right)}{\varepsilon_{G e}}\right) \times t_{O X} \tag{3}
$$

Where $\varepsilon_{Ge}$ is the dielectric constant of Ge substrate and $t_{ox}$ refer to the $GeO_2$ layer thickness. Based on our previous calculations, the $D_{it}$ value is about $1.8×10^{11}\ \text{cm}^{-2}\text{eV}^{-1}$ at flat the band voltage, and the variations between the $D_{it}$ values of different samples are very small. With respect to CNL, the value of $Q_{it}$ is calculated to be around $1×10^{10}\ \text{cm}^{-2}$. Moreover, the fitting line in Fig. 3 is almost straight for both n- and p-type Ge, indicating the $\Delta Q_{eff}+ \Delta Q_{it}$ is almost the same with different oxide thickness. $Q_{it}$ is small compare to the total amount of charge, and the effective positive fixed charges density is $1.2×10^{12}\ \text{cm}^{-2}$ for p-Ge and $8.5×10^{11}\ \text{cm}^{-2}$ for n-Ge, respectively.

![](./images/813371887106129920_3.jpg)

Fig. 3: The $V_{FB}$ of GeO2/Ge sample of different oxide thickness. (■) is p-type Ge and (●) is n-type Ge.

Hysteresis phenomena are influenced by numerous parameters, namely, bias, time, and temperature (11). The trapping occurs mostly in the bulk of oxide rather than only at the interface. Considering the model with bulk traps, two mechanisms for hole trap filling

can be possible: a filling by channel-to-defect tunneling or by the capture of $GeO_2$ valence band holes. A small relaxation of the charge-state level may occur after channel carrier tunneling into defect (12). Once charged, the defect may change its structure to modify the energy of carrier. Our result shows a lift of energy level when the defect is positive charge and relaxed, which may trap the hole when negative bias.

With one hour furnace oxidation, the measured CET is 10.6 nm. The $V_{fb}$ shift for forward bias and backward bias is 490 mV. It can also be seen from the hysteresis that the more holes trapped with the larger negative bias. The reverse bias direction shows no positive $V_{fb}$ shift, indicating there is no electron trap level in the furnace $GeO_2$ oxide. Moreover, with increasing $GeO_2$ thickness, the hysteresis (100 mV) and the dispersion percentage (1.5%) can both reduce. It benefits from the better electrical quality of $GeO_2$ layer with longer thermal oxidation time.

![](./images/813371887106129920_4.jpg)

Fig. 4: $C$-$V$ characteristics of the $GeO_2$ MOS capacitors with different extent of Vg sweep at 100 kHz

## Conclusion

In summary, the first principle calculation of $GeO_2$ bulk oxide is performed with oxygen vacancy. The (+2/0) level shows there is a positive fix charge well above Ge conduction band maximum. The positive (+1/0) trap level is located 3.31eV above the $GeO_2$ valence band maximum. The $GeO_2$ MOS capacitors with thermal oxidation shows negative $V_{fb}$ shift which indicate the positive charge trap as the simulation imply.

## Acknowledgments

This work is supported by the National Science Council, Taiwan, R.O.C. under contract nos. 97-2221-E-002-229-MY3 and 97-2221-E-002-232-MY3. The support of 5 years 50 billion program of National Taiwan University is highly appreciated.

### References

1.  C. H. Lee, T. Nishimura, N. Saido, K. Nagashio, K. Kita and A. Toriumi, *Intl. Electron Devices Meeting (IEDM)*, p. 457 (2009)

2.  H. Matsubara, T. Sasada, M. Takenaka, and S. Takagi, *Appl. Phys. Lett.*, **93**, 032104 (2008).

3.  M. Houssa, G. Pourtois, M. Caymax, M. Meuris, and M.M. Heyns, *Appl. Phys. Lett.*, **92**, 242101, (2008).

4.  A. C. Wright, G. Etherington, J. A. E. Desa, R. N. Sinclair, G. A. N. Connell, and J. C. Mikkelsen, Jr., *J. Non-Cryst. Solids*, **49**, 63 (1982).

5.  S. J. Clark, M. D. Segall, C. J. Pickard, P. J. Hasnip, M. J. Probert, K. Refson, and M. C. Payne, *Z. Kristallogr.***220**, 567 (2005).

6.  E. Martinez, O. Renault, L. Fourdrinier, L. Clavelier, C. Le Royer, C. Licitra, T. Veyron, J. M. Hartmann, V. Loup, L. Vandroux, M. J. Guittet, and N. Barret, *Appl. Phys. Lett.*, **90**, 053508 (2007).

7.  A. Ohta, H. Nakagawa, H. Murakami, S. Higashi, S. Miyazaki, *e-J. Surf. Sci. Nanotech.*, **4**, 174 (2006).

8.  M. Perego, G. Scarel, M. Fanciulli, I.L. Fedushkin, A.A. Skatova, *Appl. Phys. Lett.*, **90**, 162115 (2007).

9.  M. Yang, R.Q. Wu, Q. Chen, W.S. Deng, Y.P. Feng, J.W. Chai, J.S. Pan, S.J. Wang, *Appl. Phys. Lett.*, **94**, 142903 (2009).

10. J.R. Weber, a Janotti, and C.G. Van de Walle, *Journal of Applied Physics*, **109**, 033715 (2011).

11. G. Ribes, J. Mitard, M. Denais, S. Bruyere, F. Monsieur, C. Parthasarathy, E. Vincent, and G. Ghibaudo, *IEEE Transactions on Device and Materials Reliability*, **5**, pp. 5-19, (2005).

12. P. Blöchl and J. Stathis, *Physical Review Letters*, **83**, pp. 372-375 (1999).