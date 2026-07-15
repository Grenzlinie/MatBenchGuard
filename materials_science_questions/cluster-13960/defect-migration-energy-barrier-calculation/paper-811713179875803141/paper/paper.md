# Modified analytical interatomic potential for a W-H system with defects

Xiao-Chun Li $^{a}$, Xiaolin Shu $^{a}$, Yi-Nan Liu $^{a}$, F. Gao $^{b}$, Guang-Hong Lu $^{a,*}$

$^{a}$ Department of Physics, Beijing University of Aeronautics and Astronautics, Beijing 100191, China
$^{b}$ Pacific Northwest National Laboratory, Richland, WA 99352, USA

---

## ARTICLE INFO
Article history:
Received 11 June 2010
Accepted 19 October 2010

## ABSTRACT
We construct modified W-H and W-W analytical bond-order potentials for a W-H system. In combination with Brenner's H-H potential, we demonstrate that such potentials can reproduce energetics and structural properties of W and W-H systems, including defect formation energies, surface energies and diffusion barriers as well as melting point determined from first-principles or experiments. The present potentials can be employed for modelling the behaviour of H in W containing defects such as vacancies and surfaces.

© 2010 Elsevier B.V. All rights reserved.

---

## 1. Introduction
The fusion energy is being developed internationally via the International Thermonuclear Experimental Reactor (ITER) Project [1], which aims to demonstrate the extended burn of deuterium-tritium (D-T) plasma in a fusion reaction [2]. However, it is well known that the mechanical property of plasma facing materials (PFMs) under the D-T plasma irradiation is one of the most important issues for the ITER project and even the future fusion reactors. The damaged types for the PFMs in the fusion reaction include displacement damage caused by high energy neutrons and surface damage caused by He and H from the plasma such as blistering, erosion, and sputtering.

High-Z materials are potential candidates for the PFMs, among which W and its alloys have been considered to be the most promising materials for future Tokamak [2]. The advantage of W is its high melting temperature, high thermal conductivity and low sputtering erosion [3]. However, as a PFM, W will be subject to high flux bombardments of H isotope ions, and radiation damage, leading to microstructural changes, and significant effects on its intrinsic mechanical properties and structural strength. H can result in the formation of H bubbles, which can produce surface roughening and blistering. This remains a key obstacle in the development of W as a PFM, and thus requires further investigation. In addition to the experiment [4-7], computation has been severing as an essential tool to understand the H behaviour in W [8-12]. Recently first-principles method has been employed to investigate the microscopic vacancy trapping mechanism for H bubble formation in W [11]. First-principles can provide detailed electronic and bonding information of H in W, but it is difficult to fully understand the temperature effects and to simulate larger systems. Molecular dynamics (MD) have become a key tool for modelling material processes based on an atomic level description. Due to these characteristics, MD has recently been employed to model the H bubbles formation in W and the H bombardment on the W-C surface [9,13]. Despite these studies, the MD simulations of the interaction between H and defects in W are still rare due to lack of interatomic potential.

The reliability of the MD simulation greatly depends on the accuracy of the interatomic potential used in the simulations. Hence, great efforts have been made in developing proper potentials. Recently, a W-C-H analytical bond-order potential has been constructed by Juslin et al. (BOP-Juslin) [14]. In the BOP-Juslin, the W-W potential is extended to include second nearest neighbor interaction, which provides a good description of the coordination dependence of structure parameters. In addition, cohesive energies, thermal properties, point defects and surface properties have been reasonably described. However, the defect formation energies in W calculated from the BOP-Juslin are generally smaller than those from the experiments or first-principles. For example, the vacancy formation energy is 1.68 eV, largely deviating from the experimental value of $3.7\pm0.2$ eV [15] and the value of 3.11 [16] and 3.56 eV [17] determined from the first-principles. Also, the calculated formation energy of a self-interstitial is 8.31 eV, smaller than 9.548 [17] and 9.82 eV [16] from the first-principles. Also, the observed energetically favorable self-interstitial configuration is the [1 1 0] dumbbell, different from the [1 1 1] dumbbell calculated by the first-principles [16,17]. It is obvious that the BOP-Juslin is not suitable to study the properties of defects and defect clusters in W. On the other hand, the W-H potential in the BOP-Juslin correctly describes the solubility of H in the bcc W and reproduces the cohesive energies and structures of small $WH_n$ molecules. However, the cutoff distance of this W-H potential is too short, which is only $2.35$ Å, less than the first neighbour distance of a perfect W. This implies that a substitutional H will not interact

---

* Corresponding author.
E-mail address: lgh@buaa.edu.cn (G.-H. Lu).

0022-3115/$ - see front matter © 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.jnucmat.2010.10.020

with its first nearest neighbour W atoms, leading to very high H formation energy. Thus, the binding properties of H to vacancy is unphysical [18]. To correctly model the properties of H atoms and defects, and to simulate defect generation in W-H systems, it is urgently required to construct new potentials.

In this paper, we construct a new analytical BOP that is suitable for modelling the properties of defects and defect clusters in W-H systems. Such potentials behave well for reproducing various properties of W and W-H systems such as defect formation energies, structural properties, diffusion barriers, and melting point. The paper is organized as follows. In Section 2 the potential formalism is firstly provided, while the fitting methodology and the potential parameters for the W-W and W-H interactions are described in the Section 3. The structural properties of W-H systems and energetics of defects calculated from the new developed potentials are compared with other theoretical calculations and experiments in Section 4, which provides a way to validate the present potentials. Finally, the results are summarized in Section 5.

### 2. Potential formalism
The analytical BOP has been applied to a number of systems, such as compound semiconductors Ga-N [19], Ga-As [20], Si-C [21,22], the metal-carbon systems of Pt-C [23], W-C-H [14], Be-C-H [24], hydrocarbons [25] and pure metals such as Fe [26]. The total energy of a system is written as a sum over individual bond energies by

$$
E=\sum_{i>j} f^{c}\left(r_{i j}\right)\left[V^{R}\left(r_{i j}\right)-\frac{b_{i j}+b_{j i}}{2} V^{A}\left(r_{i j}\right)\right]. \tag{1}
$$

The pair-like attractive and repulsive energies are given in a Morse-like form described by

$$
V^{R}\left(r_{i j}\right)=\frac{D_{0}}{S-1} \exp \left[-\beta \sqrt{2 S}\left(r_{i j}-r_{0}\right)\right], \tag{2}
$$

$$
V^{A}\left(r_{i j}\right)=\frac{S D_{0}}{S-1} \exp \left[-\beta \sqrt{2 / S}\left(r_{i j}-r_{0}\right)\right], \tag{3}
$$

where $D_0$ is the dimer bond energy, $r_0$ is the dimer bond distance, and $S$ and $\beta$ are adjustable parameters.

The interaction is restricted to the second nearest neighbors by a cutoff function, which is given by

$$
f^{c}(r)=\left\{\begin{aligned}
1, & & r \leqslant R-D \\
\frac{1}{2}-\frac{1}{2} \sin \left(\frac{\pi}{2}(r-R) / D\right), & & |R-r| \leqslant D, \\
0, & & r \geqslant R+D
\end{aligned}\right. \tag{4}
$$

where $D$ and $R$ are adjustable parameters, and $R+D$ is the cutoff radius. The bond-order parameter, including three-body contributions and angularity, is described by

$$
b_{i j}=\left(1+\chi_{i j}\right)^{-1 / 2}, \tag{5}
$$

$$
\chi_{i j}=\sum_{k(\neq i, j)} f^{c}\left(r_{i k}\right) g\left(\theta_{i j k}\right) \exp \left[\alpha_{i j k}\left(r_{i j}-r_{i k}\right)\right], \tag{6}
$$

where $\alpha_{i j k}$ are adjustable parameters, and the summarize is over the third atom $k$. The angular function, $g(\theta)$, is given by

$$
g(\theta)=\gamma\left(1+\frac{c^{2}}{d^{2}}-\frac{c^{2}}{d^{2}+(h+\cos \theta)^{2}}\right), \tag{7}
$$

where $\gamma, c, d$, and $h$ are adjustable parameters.

In simulations with high-energy collisions, the atoms will be much closer so that the above potential will not be effective. In such case, the repulsive part of the potential can be expressed by the following form.

$$
V_{\text {mod }}^{R}(r)=V^{P P}(r)[1-F(r)]+V^{R}(r) F(r), \tag{8}
$$

where $V^{PP}$ can be the Ziegler-Biersack-Littmark universal repulsive potential [27] or a repulsive pair potential for a dimer determined by a first-principles method [28]. $F(r)$ is the Fermi function expressed by

$$
F(r)=\frac{1}{1+\exp \left[-b_{f}\left(r-r_{f}\right)\right]}, \tag{9}
$$

where the constants $b_f$ and $r_f$ are chosen such that the potential is effectively unmodified at the equilibrium and longer bonding distances, but also gives smooth fit to the repulsive potential. The detailed formalism of the analytical BOP can be found elsewhere [19-24].

### 3. Fitting methodology
As the potential formalism has been determined, an extensive fitting database is necessary for constructing potentials. The properties of a W equilibrium structure can be easily obtained through available experimental data and first-principles calculations, including cohesive energies, lattice constants, elastic constants, bulk modulus and defect formation energies. There are also some experimental and first-principles data for W-H, but we mainly consider the defect properties of H in the bulk W, such as the formation energies of a substitutional or interstitial H defects in a bcc W.

In order to achieve a potential with high quality, here we use a lattice relaxation fitting approach [22] and least square method to fit the W-W and W-H potentials. The objective function, $U$, is defined as

$$
U=\sum_{i} w_{i}\left[f_{i}\left(\lambda^{n}\right)-F_{i}\right]^{2}, \tag{10}
$$

which determines if the fitted each individual set of parameters can be accepted. The calculated property $f_i$ depends on the potential parameters $\lambda^{n}$. The smaller the value of $U$, the closer $f_i(\lambda^{n})$ is to the reference value $F_i$. The weight of each data item $i$ in the fitting process, denoted as $w_i$, determines how well the fitting can reproduce the corresponding property. We first construct a fitting database including lattice constants, elastic constants, formation energies of defects, and set the reference values of fitting properties $(F_i)$ in W and W-H systems. The fitting code first produces a set of parameters $\lambda^{n}$, which can be used to calculate the fitting properties $f_i(\lambda^{n})$. Here a conjugate gradient algorithm implemented in the MD code LAMMPS [29,30] has been employed to relax the lattice and obtain the formation energies of defects and structure properties, with a $4\times4\times4$ simulation box containing 128 W atoms. The objective function is determined as soon as all the fitting properties are calculated. This process is repeated until the selection criteria have been satisfied. Such parameters will be further confirmed by testing the fitting properties as well as other properties that are not included the fitting database. All the test were performed with a larger $10\times10\times10$ simulation box.

This lattice relaxation fitting approach is very useful to obtain the potential parameters to reproduce accurate defect formation energies. Although computational time greatly increases, this is quite necessary for fitting an accurate potential of all the systems. The parameters derived for the W-W and W-H interactions are given in Table 1, in which the parameters for the H-H interaction from Brenner [25] are also provided.

**Table 1**
Potential parameters for W–W and W–H interactions in the present work, along with the those for H–H interaction given by Brenner [25]. Here $\alpha_{ijk}=0$ except $\alpha_{WHW}=0.451823$ and $\alpha_{HHH}=4.0$.

| Parameter          | W–W          | W–H          | H–H (Brenner) |
|--------------------|--------------|--------------|---------------|
| $D_0$ (eV)         | 2.87454      | 3.035928     | 4.7509        |
| $r_0$ (nm)         | 0.238631     | 0.176306     | 0.074144      |
| $\beta$ ($\text{nm}^{-1}$) | 13.3682    | 13.54368     | 19.436        |
| $S$                | 1.25348      | 1.031565     | 2.3432        |
| $\gamma$           | $8.3879\times10^{-4}$ | $8.595\times10^{-3}$ | 12.33 |
| $c$                | 0.850284     | 0.146902     | 0.0           |
| $d$                | 0.144317     | 0.393100     | 1.0           |
| $h$                | $-$0.36846   | 0.558936     | 1.0           |
| $R$ (nm)           | 0.4131580    | 0.2568113    | 0.140         |
| $D$ (nm)           | 0.0930180    | 0.0133729    | 0.030         |
| *Fermi function*   |              |              |               |
| $r_f$ (nm)         | 0.13         | 0.05         | 0.035         |
| $b_f$ ($\text{nm}^{-1}$) | 120      | 70           | 150           |

---

**Table 2**
Properties of the dimer, the bcc structure, and other bulk phases of W determined from the present BOP, in comparison with those from the experiment, first-principles, and other potentials including the BOP-Juslin, FS, and MEAM potential. Here, $E_c$, $E_f$, and $E_m$ are cohesive energy (eV/atom), formation energy (eV), and migration energy (eV), respectively. $\Delta E$ is the energy difference of the sc, fcc and diamond W structures with respect to a bcc one (eV/atom). $d\langle ijk\rangle$ represents the $\langle ijk\rangle$ dumbbell interstitial configuration. Other symbols are as follows. $r_0$, the dimer bond distance (nm); $a$, the lattice constant (nm); $B$, bulk modulus (GPa); $c_{ij}$, the elastic constant (GPa); $T_m$, melting points (K); *SIA*, self-interstitial atom; *vac*, vacancy; *1NN*, first-nearest-neighbor; *2NN*, second nearest neighbor; *tet*, tetrahedral interstitial; *oct*, octahedral interstitial. The asterisk denotes the properties used in the potential fitting.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Present BOP</th>
      <th>Experimental</th>
      <th>First-principles</th>
      <th>FSª</th>
      <th>MEAMᵇ</th>
      <th>BOP-Juslinᶜ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">Body-centered cubic (bcc)</td>
    </tr>
    <tr>
      <td>$E_c$</td>
      <td>−8.906*</td>
      <td>−8.90ᵈ</td>
      <td>−7.406ᶜ</td>
      <td>−8.90ᵃ</td>
      <td>−8.66</td>
      <td>−8.89</td>
    </tr>
    <tr>
      <td>$a$</td>
      <td>0.3165*</td>
      <td>0.3165ᵉ</td>
      <td>0.318ᶠ</td>
      <td>0.31652ᵃ</td>
      <td>0.3164</td>
      <td>0.3165</td>
    </tr>
    <tr>
      <td>$B$</td>
      <td>307</td>
      <td>308–314ᵍ</td>
      <td>320ʰ, 305ᶠ</td>
      <td>310ᵃ</td>
      <td>314</td>
      <td>308</td>
    </tr>
    <tr>
      <td>$c_{11}$</td>
      <td>515*</td>
      <td>501–521ᵍ</td>
      <td>522ʰ</td>
      <td>522ᵃ</td>
      <td>533</td>
      <td>542</td>
    </tr>
    <tr>
      <td>$c_{12}$</td>
      <td>203*</td>
      <td>199–207ᵍ</td>
      <td>204ʰ</td>
      <td>204ᵃ</td>
      <td>205</td>
      <td>191</td>
    </tr>
    <tr>
      <td>$c_{44}$</td>
      <td>162*</td>
      <td>151–160ᵍ</td>
      <td>149ʰ</td>
      <td>161ᵃ</td>
      <td>163</td>
      <td>162</td>
    </tr>
    <tr>
      <td>$E_f^{vac}$</td>
      <td>3.52*</td>
      <td>3.7 ± 0.2ⁱ</td>
      <td>3.11ʲ, 3.56ᶠ</td>
      <td>3.63ᵏ</td>
      <td>3.95</td>
      <td>1.68</td>
    </tr>
    <tr>
      <td>$E_m^{vac}$</td>
      <td>1.81*</td>
      <td>1.8 ± 0.1ⁱ</td>
      <td>1.66ʲ, 1.78ᶠ</td>
      <td>1.44ᵏ</td>
      <td>1.61</td>
      <td>1.77ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{2vac}(1NN)$</td>
      <td>6.42</td>
      <td></td>
      <td>6.71ˡ</td>
      <td>6.83ᵏ</td>
      <td></td>
      <td>3.00ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{2vac}(2NN)$</td>
      <td>6.89</td>
      <td></td>
      <td>6.93ˡ</td>
      <td>6.86ᵏ</td>
      <td></td>
      <td>3.28ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{SIA}d&lt;100&gt;$</td>
      <td>12.01</td>
      <td></td>
      <td>11.49ᶠ, 11.74ʲ</td>
      <td>8.65ᵏ</td>
      <td></td>
      <td>8.93ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{SIA}d&lt;110&gt;$</td>
      <td>9.53</td>
      <td></td>
      <td>9.84ᶠ, 10.10ʲ</td>
      <td>8.44ᵏ</td>
      <td>8.98</td>
      <td>8.77ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{SIA}d&lt;111&gt;$</td>
      <td>9.33*</td>
      <td>9.06 ± 0.63ᵐ</td>
      <td>9.548ᶠ, 9.82ʲ</td>
      <td>7.81ᵏ</td>
      <td></td>
      <td>9.62ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{SIA}tet$</td>
      <td>10.75</td>
      <td></td>
      <td>11.05ᶠ, 11.99ʲ</td>
      <td>8.82ᵏ</td>
      <td></td>
      <td>8.60ᵏ</td>
    </tr>
    <tr>
      <td>$E_f^{SIA}oct$</td>
      <td>12.05</td>
      <td></td>
      <td>11.68ᶠ, 11.64ʲ</td>
      <td>8.86ᵏ</td>
      <td></td>
      <td>9.92ᵏ</td>
    </tr>
    <tr>
      <td>$T_m$</td>
      <td>4550</td>
      <td>3695ᵉ</td>
      <td></td>
      <td></td>
      <td>4600</td>
      <td>2750</td>
    </tr>
    <tr>
      <td colspan="7">Dimer</td>
    </tr>
    <tr>
      <td>$E_c$</td>
      <td>−1.44*</td>
      <td>−2.5 ± 2.5ⁿ</td>
      <td>−2.05ᶜ</td>
      <td>−3.10ᶜ</td>
      <td></td>
      <td>−2.71</td>
    </tr>
    <tr>
      <td>$r_0$</td>
      <td>0.239*</td>
      <td>0.22ⁿ</td>
      <td>0.195ᶜ</td>
      <td>0.252ᶜ</td>
      <td></td>
      <td>0.234</td>
    </tr>
    <tr>
      <td colspan="7">Face-centered cubic (fcc)</td>
    </tr>
    <tr>
      <td>$a$</td>
      <td>0.4002</td>
      <td></td>
      <td>0.4084ᶜ, 0.3960ʰ</td>
      <td>0.3927ᶜ</td>
      <td>0.4013</td>
      <td>0.4005</td>
    </tr>
    <tr>
      <td>$\Delta E$</td>
      <td>0.209</td>
      <td>0.200ᵒ</td>
      <td>0.463ᶜ, 0.369ʰ</td>
      <td>0.145ᶜ</td>
      <td>0.263</td>
      <td>0.346</td>
    </tr>
    <tr>
      <td colspan="7">Simple cubic (sc)</td>
    </tr>
    <tr>
      <td>$a$</td>
      <td>0.2602</td>
      <td></td>
      <td>0.2663ᶜ</td>
      <td>0.2689ᶜ</td>
      <td>0.2628</td>
      <td>0.2671</td>
    </tr>
    <tr>
      <td>$\Delta E$</td>
      <td>2.592</td>
      <td></td>
      <td>1.217ᶜ</td>
      <td>1.501ᶜ</td>
      <td>2.61</td>
      <td>1.614</td>
    </tr>
    <tr>
      <td colspan="7">Diamond</td>
    </tr>
    <tr>
      <td>$a$</td>
      <td>0.5924</td>
      <td></td>
      <td>0.5868ᶜ</td>
      <td>0.5868ᶜ</td>
      <td>0.5659</td>
      <td>0.5940</td>
    </tr>
    <tr>
      <td>$\Delta E$</td>
      <td>4.558</td>
      <td></td>
      <td>2.328ᶜ</td>
      <td>3.109ᶜ</td>
      <td>3.70</td>
      <td>3.109</td>
    </tr>
  </tbody>
</table>

ª Ref. [31].
ᵇ Ref. [32].
ᶜ Ref. [14].
ᵈ Ref. [33].
ᵉ Ref. [34].
ᶠ Ref. [17].
ᵍ Ref. [35].
ʰ Ref. [36].
ⁱ Ref. [15].
ʲ Ref. [16].
ᵏ Present work.
ˡ Ref. [37].
ᵐ Ref. [38].
ⁿ Ref. [39].
ᵒ Ref. [40].

---

## 4. Results

### 4.1. W–W

We consider dimer properties, cohesive energy, lattice constant, vacancy formation energy, self-interstitial atom formation energy and elastic constants of a ground-state W bcc structure in the fitting database, as determined from the experimental and first-principles results. These properties calculated from the present BOP are shown in **Table 2**, together with data from the experiments and first-principles. The properties of the fcc, sc and diamond structures of W are also calculated and are given in **Table 2** for comparison. The related data from Finnis–Sinclair (FS) [31] potential and modified embedded atom method (MEAM) [32] are also presented.

The cohesive energy of bcc W calculated from the present BOP agrees well with those from the experiments as well as other

analytical potentials. Both the bulk modulus and the elastic constants are consistent with those from experiments. The observed energetically favorable self-interstitial configuration is the [1 1 1] dumbbell, agree with the first-principles calculation. While from BOP-Juslin the [1 1 0] dumbbell is shown to be more stable. The formation energies obtained from the present BOP agree well with the values from both the first-principles calculations and experiment. On the other hand, the properties of the dimer (cohesive energy and dimer distance) and different phases (lattice constants and cohesive energies) based on the present BOP agree reasonably with the first-principles or experimental data, similar to the BOP-Juslin.

In contrast to the BOP-Juslin, the present BOP well reproduces the vacancy formation energy of W. This is because, in the fitting process, we pay especial attention to the vacancy formation energy, giving it a high weight among all the fitting parameters. As shown in Table 2, the vacancy formation energy is calculated to be 3.52 eV, which agrees well with those from both the first-principles calculations (3.11 and 3.56 eV) [16,17] and the experiment $(3.7\pm 0.2$ eV) [15]. Also, the monovacancy migration energy barrier and divacancy formation energies agree with those from the first-principles calculations. However, the BOP-Juslin leads to much lower formation energy for both vacancy and divacancy. The present potential can thus be considered to be reasonable in describing the properties of vacancy-related properties of a bcc W.

We further test the present BOP by calculating the melting point and the surface properties of W, which is important to obtain the vacancy-related defect properties. In order to determine the melting point of W at ambient pressure, we perform the MD simulations of a solid-liquid interface with a $16\times 8\times 8$ simulation box containing 2048 W atoms. Temperature and pressure were controlled using the Berendsen thermostat and barostat [41]. The left part of the constructed solid-liquid interface is fixed, while the right part is relaxed at 6000 K, followed by cooling down and quenching the system to 0 K. So-formed initial state is then relaxed to different temperatures, and equilibrated for up to 2 ns. The melting process is showed in Fig. 1. This leads to an estimate of the melting point of $4550\pm 50$ K, 860 K higher than experimental value (3690 K) [34]. However, the melting point from the BOP-Juslin is $2750\pm 50$ K [14], 940 K lower than the experimental value. For reference, the melting point from MEAM is 4600 K [32], 910 K higher than experimental value. However, the present BOP can basically reproduce the W melting point, similar to other analytical potentials, including BOP-Juslin.

<table>
<caption>Table 3
Surface energy $\gamma$ ($\text{J/m}^2$) and layer spacing variation $\Delta_{ij}^{(hkl)}$ (with respect to that of bulk, %) obtained from the present BOP, along with those from the experiments, first-principles, and the BOP-Juslin surface energy for (1 0 0) surface for comparison.</caption>
<thead>
<tr>
<th>
</th>
<th>
Present BOP
</th>
<th>
Experimental
</th>
<th>
First-principles
</th>
<th>
BOP-Juslin$^{\text{a}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$\gamma^{(1\ 0\ 0)}$
</td>
<td>
3.157
</td>
<td>
$2.990^{\text{b}}$
</td>
<td>
$4.635^{\text{d}}$
</td>
<td>
1.446
</td>
</tr>
<tr>
<td>
$\gamma^{(1\ 1\ 0)}$
</td>
<td>
2.319
</td>
<td>
$3.220^{\text{c}}$
</td>
<td>
$4.005^{\text{d}}$
</td>
<td>
0.931
</td>
</tr>
<tr>
<td>
$\gamma^{(2\ 1\ 1)}$
</td>
<td>
2.872
</td>
<td>
</td>
<td>
$4.177^{\text{d}}$
</td>
<td>
1.270
</td>
</tr>
<tr>
<td>
$\Delta_{12}^{(100)}$
</td>
<td>
$-5.0$
</td>
<td>
${-4}\sim{-8}^{\text{c}}$
</td>
<td>
${-6}\pm 0.5^{\text{e}}$
</td>
<td>
$-8.4$
</td>
</tr>
<tr>
<td>
$\Delta_{23}^{(100)}$
</td>
<td>
$-2.6$
</td>
<td>
${+0.5}\pm 0.5^{\text{c}}$
</td>
<td>
$0.5\pm 0.5^{\text{e}}$
</td>
<td>
$-0.9$
</td>
</tr>
<tr>
<td>
$\Delta_{12}^{(110)}$
</td>
<td>
$-6.3$
</td>
<td>
${-2.7}\pm 0.5^{\text{f}}$
</td>
<td>
$-3.6^{\text{g}}$
</td>
<td>
$-3.9$
</td>
</tr>
<tr>
<td>
$\Delta_{23}^{(110)}$
</td>
<td>
$-0.32$
</td>
<td>
$0.0\pm 0.3^{\text{f}}$
</td>
<td>
$+0.2^{\text{g}}$
</td>
<td>
$+0.1$
</td>
</tr>
<tr>
<td>
$\Delta_{12}^{(211)}$
</td>
<td>
$-18.1$
</td>
<td>
${-12.4}^{\text{h}},{-9.3}^{\text{i}}$
</td>
<td>
</td>
<td>
$-12.0$
</td>
</tr>
</tbody>
</table>

<p>$^{\text{a}}$ Ref. [14].<br>
$^{\text{b}}$ Ref. [42].<br>
$^{\text{c}}$ Ref. [43].<br>
$^{\text{d}}$ Ref. [44].<br>
$^{\text{e}}$ Ref. [45].<br>
$^{\text{f}}$ Ref. [46].<br>
$^{\text{g}}$ Ref. [47].<br>
$^{\text{h}}$ Ref. [48].<br>
$^{\text{i}}$ Ref. [49].</p>

<table>
<caption>Table 4
Formation energies (eV) of single H atom in the TIS, OIS and SS in a bcc W, in comparison with those from first-principles and the BOP-Juslin. The asterisk denotes the properties used in the potential fitting.</caption>
<thead>
<tr>
<th>
Configuration
</th>
<th>
Present BOP
</th>
<th>
First-principles$^{\text{a}}$
</th>
<th>
BOP-Juslin$^{\text{b}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
TIS
</td>
<td>
$0.86^{\ast}$
</td>
<td>
0.88
</td>
<td>
$-5.0$
</td>
</tr>
<tr>
<td>
OIS
</td>
<td>
$1.18^{\ast}$
</td>
<td>
1.26
</td>
<td>
$-4.8$
</td>
</tr>
<tr>
<td>
SS
</td>
<td>
$4.04^{\ast}$
</td>
<td>
4.08
</td>
<td>
4.06
</td>
</tr>
</tbody>
</table>

<p>$^{\text{a}}$ Ref. [10,11].<br>
$^{\text{b}}$ Ref. [14].</p>

Surface properties are also quite important to test an interatomic potential. Particularly, as a PFM in a nuclear fusion Tokamak, the H/He plasma irradiation starts from the W surface, making the surface properties extremely essential. We thus calculate the surface properties, including the surface energies and

![](./images/811713179875803141_1.jpg)

Fig. 1. Melting progress of W. (a) Initial state of solid-liquid interface, (b) relaxed the initial state to 4500 K for 0.5 ns, (c) relaxed the initial state to 4500 K for 2.0 ns, (d) relaxed the initial state to 4600 K for 0.5 ns, and (e) relaxed the initial state to 4600 K for 2.0 ns.

structures of the (1 0 0), (1 1 0), and (2 1 1) surfaces of a bcc W. The surface energy is determined by

$$
E_{S}=\frac{E_{T}-N \times E_{c}}{2 A}, \tag{11}
$$

where $E_{T}$ is the relaxed energy of a modelling system with two free surfaces, $N$ is the number of atoms, $E_{c}$ is the cohesive energy, and $A$ is the surface area. The results are showed in Table 3.

The surface energies of the (1 0 0), (1 1 0) and (2 1 1) surfaces determined from the present BOP are $3.157 \mathrm{~J} / \mathrm{m}^{2}, 2.319 \mathrm{~J} / \mathrm{m}^{2}$, and $2.872 \mathrm{~J} / \mathrm{m}^{2}$, respectively, lower than $4.635 \mathrm{~J} / \mathrm{m}^{2}, 4.005 \mathrm{~J} / \mathrm{m}^{2}$, and $4.177 \mathrm{~J} / \mathrm{m}^{2}$ calculated from the first-principles. However, both calculations predict the same order of relative stability of these surfaces. Among these surfaces, the (1 1 0) surface has lowest surface energy and thus is the most stable, while the (1 0 0) surface is less stable than (1 1 0), but more stable than (2 1 1). On the other hand, the average surface formation energy determined from the experiment is $2.990 \mathrm{~J} / \mathrm{m}^{2}$ [42] and $3.220 \mathrm{~J} / \mathrm{m}^{2}$ [43].The surface energies of the (1 0 0), (1 1 0) and (2 1 1) surfaces calculated from the BOP-Juslin are $1.446 \mathrm{~J} / \mathrm{m}^{2}, 0.931 \mathrm{~J} / \mathrm{m}^{2}$ and $1.270 \mathrm{~J} / \mathrm{m}^{2}$, respectively, which are much lower, but it also predicts the same relative stability. In addition, the first-principles calculation gives larger surface energies as compared with the experiment. For the layer spacing, both the present BOP and the BOP-Juslin predict the similar trend, but both with larger deviation for the spacing of $\Delta_{23}^{(100)}$ in comparison with the experiment.

### 4.2. W-H

As described in the Introduction, the W-H cutoff distance of the BOP-Juslin is too short to describe the correct behaviour of H at a vacancy. Employing such short W-H cutoff distance gives rise to a large deviation of H formation energies from first-principles. As shown in Table 4, the formation energies of H at the tetrahedral interstitial site (TIS), the octahedral interstitial site (OIS), and the substitutional site (SS) determined by the first-principles are 0.88 eV, 1.26 eV, and 4.08 eV [10,11], respectively. However, the BOP-Juslin gives -5.00 eV, -4.80 eV, and 4.06 eV, respectively. Both refer to half of the chemical potential of $\mathrm{H}_{2}$. In order to make the W-H potential correctly describe H-vacancy interaction, we set the potential parameters R and D large enough to ensure the correct description for the W-H interactions, particularly for the substitutional case. The fitting database for the W-H interaction is quite different from that of the BOP-Juslin. In the present BOP, we mainly consider the defect properties of H in bulk W, including the formation energies of single H atom at the TIS, OIS, and SS. Furthermore, the properties of W-H molecules have been also taken into account.

In Table 4 we show the formation energies obtained from the present BOP. The formation energies of H at the TIS, the OIS, and the SS are 0.86 eV, 1.18 eV, and 4.08 eV, respectively. These energies are in good agreement with those from the first-principles calculations [10,11]. The formation energies determined from the BOP-Juslin for the TIS and the OIS cases largely deviate from those from the first-principles. Further, the occupancy preference of H is also consistent with that from the first-principles, and the present BOP gives the most stable configuration for H at a vacancy. It is to be at an off-vacancy-center position, and the distance between H and vacancy center is 0.100 nm, in consistent with 0.128 nm from the first-principles calculations [11], while the BOP-Juslin gives a much lower value of 0.063 nm.

Four types of W-H molecules that have been observed by experiments are fully relaxed with the present potentials, and the results shown in Fig. 2. The basic structure properties of these W-H molecules are determined, including the cohesive energy, the bond length, and the bond angle. The results are listed in Table 5.

To reproduce these properties from the first-principles, the present BOP is comparable with the BOP-Juslin, but the BOP-Juslin predicts better.

Finally, we calculate the diffusion properties of a single H in W using the present BOP with a simulation box of 2000 atoms. Here, we determine the diffusion energy barrier of H using a drag method at a fixed volume and constrain the atomic positions to be relaxed in a plane perpendicular to the vector from the initial to final positions [50]. The present BOP gives the diffusion barrier 0.23 eV and 0.43 eV via the diffusion paths of TIS-TIS and TIS-OIS-TIS, respectively, consistent with the first-principles calculations of 0.20 eV and 0.38 eV for the same diffusion paths [10].

## 5. Summary

We have constructed empirical many-body interatomic W-W and W-H potentials in terms of analytical bond-order formalism for a W-H system. The potentials are fitted based on defect energetics and structural properties of W and W-H systems from the experiment and the first-principles calculations using a lattice relaxation fitting approach. We specially consider the defect prop-

![](./images/811713179875803141_2.jpg)

Fig. 2. Configurations of $\mathrm{WH}_{n}$ molecules (here $n=1-4$).

<table>
<caption>Table 5<br>Properties of the $\mathrm{WH}_{n}$ molecules calculated from the present BOP. $E_{c}$ is the cohesive energy (eV/atom), $r_{0}$ is the bond length (nm), and $\theta$ is the H-W-H bond angles (deg). Those from the first-principles and the BOP-Juslin are also given for comparison. The asterisk denotes the properties used in the potential fitting.</caption>
<thead>
<tr>
<th>
</th>
<th>
Present BOP
</th>
<th>
First-principles
</th>
<th>
BOP-Juslin$^{\text{a}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
WH
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$E_{c}$
</td>
<td>
$-1.518^{\ast}$
</td>
<td>
$-1.345^{\text{b}}$,$-1.474^{\text{a}}$
</td>
<td>
$-1.374$
</td>
</tr>
<tr>
<td>
$r_{0}$
</td>
<td>
$0.1763^{\ast}$
</td>
<td>
$0.1727^{\text{b}}$,$0.1715^{\text{c}}$,$0.1714^{\text{a}}$
</td>
<td>
$0.1727$
</td>
</tr>
<tr>
<td>
$\text{WH}_{2}$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
$E_{c}$
</td>
<td>
$-1.887^{\ast}$
</td>
<td>
$-1.851^{\text{a}}$
</td>
<td>
$-1.820$
</td>
</tr>
<tr>
<td>
$r_{0}$
</td>
<td>
$0.1799^{\ast}$
</td>
<td>
$0.1717^{\text{ac}}$,$0.173^{\text{d}}$
</td>
<td>
$0.1730$
</td>
</tr>
<tr>
<td>
$\theta$
</td>
<td>
$124.0^{\ast}$
</td>
<td>
$117.2^{\text{d}}$,$112.9^{\text{ac}}$
</td>
<td>
$112.9$
</td>
</tr>
<tr>
<td>
$\text{WH}_{3}$
</td>
<td>
</td>
<td>
</td>
</td>
</tr>
<tr>
<td>
$E_{c}$
</td>
<td>
$-1.981^{\ast}$
</td>
<td>
$-2.112^{\text{a}}$
</td>
<td>
$-2.033$
</td>
</tr>
<tr>
<td>
$r_{0}$
</td>
<td>
$0.1834^{\ast}$
</td>
<td>
$0.1716^{\text{ac}}$,$0.1689^{\text{e}}$
</td>
<td>
$0.1733$
</td>
</tr>
<tr>
<td>
$\theta$
</td>
<td>
$119.9^{\ast}$
</td>
<td>
$112.6^{\text{a}}$,$112.8^{\text{ce}}$
</td>
<td>
$112.9$
</td>
</tr>
<tr>
<td>
$\text{WH}_{4}$
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Ec
</td>
<td>
$-1.985^{\ast}$
</td>
<td>
$-1.937^{\text{a}}$
</td>
<td>
$-2.154$
</td>
</tr>
<tr>
<td>
$r_{0}$
</td>
<td>
$0.1870^{\ast}$
</td>
<td>
$0.1712^{\text{c}}$,$0.1715^{\text{a}}$
</td>
<td>
$0.1736$
</td>
</tr>
<tr>
<td>
$\theta$
</td>
<td>
$116.3^{\ast}$
</td>
<td>
$109.5^{\text{ac}}$
</td>
<td>
$112.9$
</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="4">
$^{\text{a}}$ Ref. [14].
</td>
</tr>
<tr>
<td colspan="4">
$^{\text{b}}$ Ref. [51].
</td>
</tr>
<tr>
<td colspan="4">
$^{\text{c}}$ Ref. [40].
</td>
</tr>
<tr>
<td colspan="4">
$^{\text{d}}$ Ref. [52].
</td>
</tr>
<tr>
<td colspan="4">
$^{\text{e}}$ Ref. [53].
</td>
</tr>
</tfoot>
</table>

erties such as vacancy and H interstitial formation energies in or- der to make the potential suitable for simulating a defected W–H system. In combination with the Brenner's H–H potential, we dem- onstrate that the fitted potentials can reproduce the energetic of the W surfaces, the defect properties of both W and W–H systems, the W–H molecules, as well as the W melting point and H diffusion barriers in W. It is expected that the present potentials can be em- ployed to investigate the H behaviours in W containing defects such as vacancies and surfaces.

## Acknowledgments
This work has been supported by National Magnetic Confine- ment Fusion Program with Grant No. 2009GB106003 and National Natural Science Foundation of China (NSFC) Grant No. 50871009. F. Gao is grateful for the support by the US Department of Energy, Of- fice of Fusion Energy Science, under Contract DE-AC06-76RLO 1830.

## References
[1] G. Janeschitz, J. Nucl. Mater. 290–293 (2001) 1.
[2] R. Causey et al., J. Nucl. Mater. 269 (1999) 467.
[3] H.T. Lee et al., J. Nucl. Mater. 360 (2007) 196.
[4] G.-N. Luo, W.M. Shu, M. Nishi, J. Nucl. Mater. 347 (2005) 111.
[5] G.-N. Luo, W.M. Shu, M. Nishi, Fusion Eng. Des. 81 (2006) 957.
[6] M. Fukumoto et al., J. Nucl. Mater. 375 (2008) 224.
[7] G.N. Luo et al., J. Nucl. Mater. 363 (2007) 1241.
[8] I.S. Landman, H. Wuerz, J. Nucl. Mater. 313–316 (2003) 77.
[9] K.O.E. Henriksson et al., Appl. Phys. Lett. 87 (2005) 163113.
[10] Y.-L. Liu et al., J. Nucl. Mater. 390–391 (2009) 1032.
[11] Y.-L. Liu et al., Phys. Rev. B 79 (2009) 172103.
[12] H.-B. Zhou et al., Nucl. Fusion 50 (2010) 025016.
[13] P. Träskelin et al., Phys. Rev. B 75 (2007) 174113.
[14] N. Juslin et al., J. Appl. Phys. 98 (2005) 123520.
[15] K.-D. Rasch, R.W. Siegel, H. Schultz, Philos. Mag. A 41 (1980) 91.

[16] C.S. Becquart, C. Domain, Nucl. Instrum. Methods B 255 (2007) 23.
[17] D. Nguyen-Manh, A.P. Horsfield, S.L. Dudarev, Phys. Rev. B 73 (2006) 020101.
[18] X.-C. Li, F. Gao, G.-H. Lu, Nucl. Instrum. Methods B 267 (2009) 3197.
[19] J. Nord et al., J. Phys.: Condens. Matter 15 (2003) 5649.
[20] K. Albe et al., Phys. Rev. B 66 (2002) 035205.
[21] P. Erhart, K. Albe, Phys. Rev. B 71 (2005) 035211.
[22] F. Gao, W.J. Weber, Nucl. Instrum. Methods B 191 (2002) 504.
[23] K. Albe, K. Nordlund, R.S. Averback, Phys. Rev. B 65 (2002) 195124.
[24] C. Björkas et al., J. Phys.: Condens. Matter 21 (2009) 445002.
[25] D.W. Brenner, Phys. Rev. B 42 (1990) 9458.
[26] M. Müller, P. Erhart, K. Albe, J. Phys.: Condens. Matter 19 (2007) 326220.
[27] J.F. Ziegler, J.P. Biersack, U. Littmark, The Stopping and Range of Ions in Matter, Pergamon, New York, 1985.
[28] K. Nordlund, N. Runeberg, D. Sundholm, Nucl. Instrum. Methods B 132 (1997) 45.
[29] LAMMPS Molecular Dynamics Simulator, <http://lammps.sandia.gov/>.
[30] S.J. Plimpton, J. Comp. Phys. 117 (1995) 1.
[31] M.W. Finnis, J.E. Sinclair, Philos. Mag. A 50 (1984) 45.
[32] B.-J. Lee et al., Phys. Rev. B 64 (2001) 184102.
[33] C. Kittel, Introduction to Solid State Physics, seventh ed., Wiley, New York, 1996.
[34] CRC Handbook of Chemistry and Physics, eighty-fifth ed., CRC, Boca Raton, 2004.
[35] D.I. Bolef, J. De Klerk, J. Appl. Phys. 33 (1962) 2311.
[36] K. Einarsdotter et al., Phys. Rev. Lett. 79 (1997) 2073.
[37] P.M. Derlet, D. Nguyen-Manh, S.L. Dudarev, Phys. Rev. B 76 (2007) 054107.
[38] I.M. Neklyudov et al., Phys. Rev. B 78 (2008) 115418.
[39] M.D. Morse, Chem. Rev. 86 (1986) 1049.
[40] X. Wang, L. Andrews, J. Phys. Chem. A 106 (2002) 6720.
[41] H.J.C. Berendsen et al., J. Chem. Phys. 81 (1984) 3684.
[42] W.R. Tyson, W.A. Miller, Surf. Sci. 62 (1977) 267.
[43] W. Xu, J.B. Adams, Surf. Sci. 301 (1994) 371.
[44] L. Vitos et al., Surf. Sci. 411 (1998) 186.
[45] R. Yu, H. Krakauer, D. Singh, Phys. Rev. B 45 (1992) 8671.
[46] H.L. Meyerheim et al., Surf. Sci. 475 (2001) 103.
[47] M. Arnold et al., Surf. Sci. 382 (1997) 288.
[48] H.L. Davis, G.C. Wang, Bull. Am. Phys. Soc. 29 (1984) 221.
[49] O. Grizzi et al., Phys. Rev. B 40 (1989) 10127.
[50] C.-C. Fu, F. Willaime, P. Ordejon, Phys. Rev. Lett. 92 (2004) 175503.
[51] Z. Ma, K. Balasubramanian, Chem. Phys. Lett. 181 (1991) 467.
[52] K. Balasubramanian, Z. Ma, J. Phys. Chem. 95 (1991) 9794.
[53] N.B. Balabanov, J.E. Boggs, J. Phys. Chem. A 104 (2000) 7370.