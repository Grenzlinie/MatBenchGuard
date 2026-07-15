![](./images/811118379585765376_1.jpg)

Nuclear Instruments and Methods in Physics Research B 160 (2000) 328-332

![](./images/811118379585765376_2.jpg)

# Monte Carlo calculations of hydrogen depth profiles in a-Si and a-Si:H

H. Horiki *, A. Koyama

The Institute of Physical and Chemical Research, Hirosawa 2-1, Wako-shi, Saitama 351-0198, Japan

Received 19 July 1999; received in revised form 3 September 1999

## Abstract
Ranges and variances of 15-1000 eV H-atoms implanted into a-Si and a-Si:H are calculated by using a Monte Carlo calculation program. The results for a-Si are in good agreement with those from other simulation codes of TRIM-92, BABOUM, and TRIM-SP examined by Mayer and Eckstein. Values of ranges and variances calculated for a-Si:H are compared with those for a-Si and the implantation dose effect is shortly discussed. © 2000 Elsevier Science B.V. All rights reserved.

PACS: 6170T; 6180J
Keywords: Monte Carlo simulation; Low energy H-atom implantation; Amorphous silicon; Hydrogenated amorphous silicon

---

## 1. Introduction
Understanding of low energy ion implantation is important to a technique of plasma CVD or impurity depth profile controlling in nano-meter scale. In the last two decades, investigations on depth profiles of H-atoms implanted into Si were carried out in the energy region below 1000 eV and compared with theoretical results.

Demond et al. measured the depth profile in the energy region from 0.5 to 300 keV by using the resonance nuclear reaction of p and $^{15}$N [1]. Surface of the target was amorphized by Ne irradiation. They evaluated the values of mean projected ranges (MPR) and standard deviations ($\Sigma$) and compared them with those of the calculation by Winterbon [2]. In the low energy region, the electronic energy loss in the non-local Lindhard-Sharff (LS) model is given by

$$
S_{\mathrm{e}}=C K_{\mathrm{LS}} \sqrt{E}, \tag{1}
$$

where $K_{\mathrm{LS}}$ is the stopping factor due to the LS theory [3], and $C$ is experimental correction factor which was deduced to be 1.7 from the comparison with the theory.

Ross and Terreault [4] carried out the experiment in the energy region from 720 to 2080 eV.

---

*Corresponding author. Tel.: +81-48-467-9322; fax: +81-48-462-4634.
E-mail address: horiki@postman.riken.go.jp (H. Horiki).

0168-583X/00/$ - see front matter © 2000 Elsevier Science B.V. All rights reserved.
PII: S0168-583X(99)00608-4

Implantation was done at the incident angle tilted off the channeling axis. They evaluated the depth profiles by using the technique of elastic recoil detection analysis [ERDA]. Values of MPR due to this experiment were larger than those due to Demond et al. by 20–100%. They were compared with the values calculated from Monte Carlo simulations (MCS) of BABOUM [5] and MAR- LOWE [6], and with the compilation of Anderson and Ziegler (A–Z) [7]. The code BABOUM is ap- plicable only to amorphous target, and basically the same with the code TRIM [8]. MARLOWE takes into account the structure of the solid in computing trajectories, but it is time-consuming. BABOUM gave the closest value, while MAR- LOWE was too large compared to the experiment. The value due to A–Z is only a half of the exper- imental one and near to that from Demond et al. [1].

Leblanc and Ross [9] measured MPR and $\Sigma$ in the energy region from 200 to 1000 eV by using ERDA and compared to those deduced from the TRIM-92, BABOUM and A–Z compilation. When the value of $C$ was set to be 1.1, results from TRIM-92 and BABOUM were in excellent agree- ment with the experimental data. The A–Z com- pilation values were too low.

Mayer and Eckstein [10] calculated H-depth profiles by using the code TRIM-SP [11]. The applicability of this program is extended to small energies through the consideration of simulta- neous collisions. In this calculation, the krypton– carbon potential [12] and the ZBL (universal) po- tential [13] were examined for the interaction po- tential. The difference in the values evaluated from these potentials was only 10%. The inelastic energy loss was also examined. The extrapolation of the Andersen–Ziegler compilation to ion energies of 100 eV, factor $C$ was found to be 1.38. Values of MPR calculated from TRIM-92, BABOUM and TRIM-SP were all in good agreement with the data of Leblanc and Ross [9] and Ross [4]. When the stopping cross section was calculated from the local Oen–Robinson energy loss [14], it was con- siderably smaller than that of Lindhard–Scharff. This Oen–Robinson stopping cross section gave too large values of MPR compared to those of experimental data.

Bourque and Terreault [15] measured the depth profiles of 1 keV H-atom implantation into a-Si and into c-Si in random and channeled directions by using the method of ERDA. They compared profiles themselves between the experiment and theory. Examined codes were MARLOWE, CRYSTAL-TRIM, TRIM-SP and TRIM-95. The interatomic potential was the ZBL universal po- tential [13]. All the simulations under the non-local inelastic energy loss model were not in good agreement with the experiment in a-Si and in c-Si in a random direction, even though the factor $C=1.38$ was used. Taking into account simulta- neous collisions slightly improved the calculated results. But in the aligned direction, even when taking into account them, the results were totally inadequate. Concerned with the local inelastic energy loss, the profile calculated by MARLOWE was in good agreement with the experimental one for c-Si, both in random and aligned directions. When simultaneous collisions were taken into ac- count, agreement became better. But for a-Si, agreement was not good. These studies represent that a single theoretical model cannot reproduce all the experimental data. The recommended val- ues of the correction factor are different between Leblanc and Ross [9] and Mayer Eckstein [10], for the same code TRIM. The local inelastic energy loss model is unsuccessful for the evaluation of MPR due to TRIM-SP [10], but successful to evaluate the depth profile due to MARLOWE [15]. It seems plausible from the study by Mayer Eck- stein [10] to use the non-local inelastic model for the calculation of MPR of H-atoms in a-Si.

In the present report, we have calculated the depth profile of H-atoms implanted into a-Si and hydrogenated amorphous Si, a-Si:H, by using the MCS code developed by us. In this code simulta- neous collisions are not taken into account, be- cause they induce only small effect [10]. The energy of H-atoms is from 15 to 1000 eV. This study will serve to have an insight on the implantation into a- Si:H itself, and also on the effect of preceding implanted atoms on the depth profiles for high dose implantation. The concentration of H-atoms concerned here is below 30 at.%. At the energy of 1000 eV, both the MPR and the standard devia- tion ($\Sigma$) are about 30% larger than those for pure

a-Si, at the H-atom concentration of 30 at.%. But those increases become small with the decrease of energy, and negligible at the energy of 15 eV. Be- low, the present MCS code is briefly described, results of the present calculation for pure a-Si are represented, and finally calculated values of MPR and $\Sigma$ for a-Si:H are compared with those for a-Si.

## 2. Simulation

We have referred to the method of physical quantity determination presented by Adesida and Karapiperis [16]. It is assumed that an impinging H-atom goes straight until it suffers an elastic collision with a target atom of H or Si. It loses its energy in proportion to the length of the path passed before the next elastic collision. Elastic events and energy losses are followed until its en- ergy becomes lower than 0.5 eV or it goes out from the surface. The universal scattering cross section derived by Kalbitzer and Oetzmann [17] is used to describe nuclear scattering events. The total cross section of nuclear collisions between H and H, and H and Si is given by $N^{-2/3}$, where $N$ is the density of atoms in a-Si:H, and is assumed to be equal to that of a-Si; $N=5\times10^{-20}/\text{cm}^3$. The maximum scattering angle is equal to $\pi$. The minimum scat- tering angle is given by

$$
\sigma_{\mathrm{T}}=\int_{t_{\min}}^{t_{\max}} \mathrm{d} \sigma=N^{-2 / 3},
\tag{2}
$$

where $N$ is the density of atoms in a-Si:H, $t_{\max}=\varepsilon\sin(\pi/2)=\varepsilon$ and $t_{\min}=\varepsilon\sin(\theta_{\min}/2)$. The scattering angle $\theta$ for each elastic collision is given by

$$
R_{1}=\int_{t_{\min}}^{t} \mathrm{d} \sigma \bigg/ \int_{t_{\min}}^{t_{\max}} \mathrm{d} \sigma,
\tag{3}
$$

where $t=\varepsilon\sin(\theta/2)$, and $R_1$ is a uniform random number. The azimuthal angle $\phi$ is calculated from

$$
\phi=2\pi R_{2},
\tag{4}
$$

where $R_2$ is a uniform random number.

The mean free path of the elastic collision of the H-atom with a target H or Si is given by

$$
\lambda_{\mathrm{T}}=N^{-1 / 3}.
\tag{5}
$$

The mean free paths for H-H collision and H- Si are given by

$$
\begin{aligned}
\lambda_{\mathrm{Si}} & =\lambda_{\mathrm{T}} /(1-c), \\
\lambda_{\mathrm{H}} & =\lambda_{\mathrm{T}} / c,
\end{aligned}
\tag{6}
$$

where $c$ is the concentration of H-atoms.

The type of atom with which the H-atom is to collide is selected by using a random number $R_3$; when $R_3>\lambda_{\mathrm{T}}/\lambda_{\mathrm{Si}}$, a collision with H-atom occurs, and $R_3\leqslant\lambda_{\mathrm{T}}/\lambda_{\mathrm{Si}}$, a collision with Si-atom occurs. The individual free path $S$ is given by

$$
S=-\lambda_{\mathrm{T}} \ln R_{4},
\tag{7}
$$

where $R_4$ is also the uniform random number. After each collision, the direction of the penetrat- ing H-atom is calculated with respect to the labo- ratory system.

For electronic energy loss, the corrected LS formulae are used. The factor $C$ in Eq. (1) is ex- amined for the a-Si target. The stopping power for the inelastic energy loss in the a-Si:H target with H-atom concentration $c$ is calculated according to Bragg's rule as follows:

$$
-\frac{\mathrm{d} E}{\mathrm{~d} x}=-(1-c)\left(\frac{\mathrm{d} E}{\mathrm{~d} x}\right)_{\mathrm{H}-\mathrm{Si}}-c\left(\frac{\mathrm{d} E}{\mathrm{~d} x}\right)_{\mathrm{H}-\mathrm{H}},
\tag{8}
$$

where $-(\mathrm{d}E/\mathrm{d}x)_{\mathrm{Si}}$ and $-(\mathrm{d}E/\mathrm{d}x)_{\mathrm{H}}$ are given by the LS formulae, and $C=1.38$ for Si, and $C=1.0$ for H.

## 3. Results and discussion

Fig. 1 shows the calculated MPR and $\Sigma$ for a- Si. The abscissa and the ordinate are both loga- rithmic. The filled circles are experimental data from Leblanc and Ross [9]. The energy loss cor- rection factor $C=1.38$ gives the best agreement between the calculated MPR and experimental data, as was noticed by Mayer and Eckstein [10]. This means that the universal potential from Kalbitzer and Oetzmann operates as well as the krypton-carbon or the ZBL potential. However, in the case of $\Sigma$, it gives values smaller than the experimental data by 20%, also as the results by

![](./images/811118379585765376_3.jpg)

Fig. 1. Mean projected ranges and widths of the depth distribution of H in a-Si as a function of energy. $C$ is the correction factor of the LS non-local electronic energy loss. The filled circles are experimental data from Leblanc and Ross [9].

Mayer and Eckstein. This discrepancy has not been elucidated. It is seen that the energy dependence of MPR or $\Sigma$ calculated from different values of $C$ are almost the same. This will be because the fraction of the electronic energy loss in the total loss is almost independent of the incident energy. Fig. 2 shows the incident energy dependence of the ratio between $\Sigma$ and MPR in a-Si calculated with the correction factor $C=1.38$. The ratio is almost constant. The filled circles represent the data evaluated from the experimental data for MPR and $\Sigma$ from Leblanc and Ross [9].

![](./images/811118379585765376_4.jpg)

Fig. 2. Ratio of width to mean projected range for a-Si with the inelastic energy loss correction factor $C=1.38$. The filled circles are evaluated from the data by Leblanc and Ross [9].

Fig. 3 shows the MPR and $\Sigma$ for a-Si and a-Si:H with H-concentration of 30 at.%, drawn in the logarithmic scales. The MPR and $\Sigma$ for a-Si:H are larger than those for a-Si. It will be induced by the small inelastic energy loss due to H-atoms in a-Si:H compared to a-Si. At the incident energy of 1000 eV, the increases in MPR and $\Sigma$ for a-Si:H compared to a-Si are about 30%. With decreasing energy, the increases become small. This will be because at low energy, the drag effect due to H–H

![](./images/811118379585765376_5.jpg)

Fig. 3. Mean projected ranges and widths of the depth distribution of H in a-Si:H with H concentration of 30 at.% as a function of energy. Those in a-Si are also represented. The used values of the correction factors are $C=1.38$ for Si and $C=1.0$ for H, respectively.

![](./images/811118379585765376_6.jpg)

Fig. 4. Mean projected range and width of the depth distributions of H in a-Si:H as a function of H-concentration at the energy of 1000 eV.

nuclear collisions becomes prominent, and the smaller inelastic energy loss is compensated.

Fig. 4 shows MPR and $\Sigma$ for a-Si:H at the incident energy of 1000 eV, as a function of H-atom concentration. They increase linearly with increasing concentration and their increasing rates are almost the same. When the interaction of implanting H-atoms with preceding implanted H-atoms cannot be neglected, the final values of MPR are given by averaging on time the instantaneous value of MPR. That is, if H-atoms are implanted with some constant rate and if the final concentration averaged on depth is equal to $c$, the final value of MPR will be equal to that of a target of a-Si:H with H-atom concentration of $c/2$. For more rigorous treatment, a serial Monte Carlo simulation like Tridyn [18] should be used.

## 4. Conclusion

We have developed an MCS code applicable to the penetration of particle in amorphous materials. Low energy H-atom implantation into a-Si is simulated and calculated values of MPR and $\Sigma$ are in good agreement with those from TRIM-SP [10]. H-atom implantation into a-Si:H is also simulated and compared with the results for a-Si. MPR and $\Sigma$ are increased almost linearly with H-atom concentration in a-Si:H. At 1000 eV, both MPR and $\Sigma$ for a-Si:H with H-atom concentration of 30 at.% are larger than those for a-Si by about 30%. But with decreasing energy, those differences become small and are negligible at the energy of 15 eV. When H-atoms are implanted into a-Si at the incident energy of 1000 eV up to the H-atom concentration of $c$ at.% averaged on the depth region of the standard deviation, values of MPR and $\Sigma$ should be increased by $c/2\%$ compared to the case of very dilute implantation.

## References

[1] F.-J. Demond, S. Kalbitzer, H. Mannsperger, G. Müller, Nucl. Instr. and Meth. 168 (1980) 69.
[2] K.B. Winterbon, Radiat. Eff. 13 (1972) 215.
[3] J. Lindhard, M. Scharff, Phys. Rev. 124 (1961) 128.
[4] G.G. Ross, B. Terreault, Nucl. Instr. and Meth. B 15 (1986) 61.
[5] G. Abel, G. Ross, B. Terreault, J.P. Labrie, Nucl. Instr. and Meth. 170 (1980) 171.
[6] O.S. Oen, M.T. Robinson, Inst. Phys. Conf. Ser. 28 (1976) 329.
[7] H.H. Andersen, J.F. Ziegler, Hydrogen Stopping Powers and Ranges in All Elements, Pergamon, New York, 1977.
[8] Biersack, L.G. Haggmark, Nucl. Instr. and Meth. 174 (1980) 257.
[9] L. Leblanc, G. Ross, Nucl. Inst. and Meth. B 83 (1993) 15.
[10] M. Mayer, W. Eckstein, Nucl. Instr. and Meth. B 94 (1994) 22.
[11] Biersack, W. Eckstein, Appl. Phys. A 34 (1984) 73.
[12] W. Wilson, L. Haggmark, J. Biersack, Phys. Rev. B 15 (1977) 2458.
[13] J. Ziegler, J. Biersack, U. Littmark, The Stopping and Range of Ions in Solids, Vol. 1 of The Stopping and Ranges of Ions in Matter, Pergamon, New York, 1985.
[14] O.S. Oen, M.T. Robinson, Nucl. Instr. and Meth. 132 (1976) 647.
[15] G. Bourque, B. Terreault, Nucl. Instr. and Meth. B 115 (1996) 468.
[16] I. Adesida, L. Karapiperis, Radiat. Eff. 61 (1982) 223.
[17] S. Kalbitzer, H. Oetzmann, Radiat. Eff. 47 (1980) 57.
[18] W. Eckstein, Computer Simulation of Ion-Solid interactions, Springer, Berlin, 1991.