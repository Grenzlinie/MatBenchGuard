Jinghan You, Weiwei Ju, Zhengxin Tang, Liben Li
School of Science, Henan University of Science and Technology, Luoyang, P.R China

# Study on the dielectric properties of $CaCu_3Ti_4O_{12}$ ceramics using the one-dimensional Ising model

As a high-dielectric cubic perovskite-related material, $CaCu_3Ti_4O_{12}$ (CCTO) has a dielectric constant of $10^4$ at room temperature. Up to now the origin of the peculiar dielectric phenomena in CCTO is not fully understood and there are some disputes in the literature. In this paper, based a one-dimensional Ising model under static electric field, the dielectric properties of CCTO were studied. Results indicate that the theory is nearly consistent with the experiment.

**Keywords:** CaCu3Ti4O12; Dielectric constant; One-dimensional Ising model

## 1. Introduction

Recently, the unusual cubic perovskite-related $CaCu_3Ti_4O_{12}$ (CCTO) has attracted considerable attention [1-21]. The ceramic of CCTO has high dielectric constant in the order of $10^4$, the single crystal of CCTO has high dielectric constant in the order of $10^5$ and remains almost constant in the temperature range from 100 to 600 K. But at a temperature of 100 K the dielectric constant drops rapidly by 2-3 orders of magnitude [1]. Moreover, with the help of neutron powder diffraction, high-resolution X-ray diffraction and Raman investigations, there is no evidence of any structural phase transition in CCTO from 20 to 600 K [1-3].

There are many disputes about the origin of the high dielectric constant in CCTO. Homes et al. [1] observed that there is an anomalous low-temperature vibration mode in the single crystal of CCTO, implying that there is a redistribution of charge within the unit cell at low temperatures. Subramanian et al. [2] demonstrated that twin boundaries enhance the high dielectric constants in CCTO. Sinclair and Adams [3] proposed that the giant-dielectric phenomenon is attributed to a grain boundary (internal) barrier layer capacitance (IBLC). However, up to now the origin of the peculiar dielectric phenomena in CCTO is not fully understood.

In this paper, CCTO ceramics samples were prepared by the traditional solid state reaction method and the dielectric properties were investigated. Figure 1 represents the temperature dependence of the dielectric constant for the samples of CCTO under different frequencies between $10^{3.5}$ Hz and $10^{6.0}$ Hz. It is shown that the dielectric constant of CCTO increases with increasing temperature at the different frequencies investigated. At room temperature the dielectric constant for CCTO, $\varepsilon \sim 10^4$, is weakly temperature dependent over a broad temperature range. The dielectric constant drops rapidly by 2-3 orders of magnitude below a certain temperature. The transition temperature of the dielectric constant increases with the increase of frequency [22].

![](./images/813279044266098689_1.jpg)

Fig. 1. Temperature dependence of the dielectric constant, $\varepsilon$, for the examined samples of CCTO at different frequencies.

In order to understand these phenomena, in this paper the dielectric properties of CCTO were attempted to study by a one-dimensional Ising model.

## 2. Model

### 2.1. One-dimensional dipole model of CCTO

Some unit cells of CCTO are shown in Fig. 2. The big black spheres represent Ca atoms, the medium gray spheres represent Cu atoms, the light gray spheres represent O atoms. The Ti atoms are located at the center of the $TiO_6$ octahedra and are not visible in Fig. 2.

There exists polarization inside the $TiO_6$ octahedra. Considering that the macroscopic polarization is zero, it can be assumed that the spontaneous polarization of four octahedra in each unit cell of CCTO constitutes a parallelogram, so the polarizations counteract each other as shown in Fig. 3a. The projection in a certain direction constitutes a one-dimensional chain shown in Fig. 3b, so the one-dimensional Ising model can be used to it.

### 2.2. One-dimensional Ising model

The one-dimensional Ising model consisted mainly of a polarization lattice [23]. The particle state of the $i$ lattice could

![](./images/813279044266098689_2.jpg)

Fig. 2. The unit cell of CCTO.

![](./images/813279044266098689_3.jpg)

Fig. 3. One-dimensional dipole model of CCTO.

be completely represented by the polaron $\sigma_{i}$. In order to simply study this question, there are some suppositions:
1. Only two polarization: up and down, expressed as $\sigma_{i}=1$ and $\sigma_{i}=-1$, respectively.
2. The interaction exists only with the direct neighbor.
3. The potential of the system can be obtained by adding the interaction energies.

Obviously, due to the interaction between the dipoles the polarizations in the lattice tend to order, while thermal movement leads to polarization disorder. So at a certain temperature the polarization is likely to order. This is the Ising model. Considering the simplest situation, i.e. the polarization is distributed in a one-dimensional linear chain, this is the one-dimensional Ising model.

Assume that the $N$ dipoles arrange into a linear equidistant chain, the polarization coordinate of the $i$ dipole is $\sigma_{i}$. Suppose the interaction potential between polaron $\sigma_{i}$ and $\sigma_{i+1}$ is $-J\sigma_{i}\sigma_{i+1}$, so the contribution to the potential is $-J$ when the dipoles are parallel and $J$ when the dipoles are antiparallel. If $J>0$ the polarization tend to the same direction, so the total potential of the system in an external electric field $E$ is:

$$
H(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{N})=-J \sum_{i=1}^{N-1} \sigma_{i} \sigma_{i+1}-\mu E \sum_{i=1}^{N} \sigma_{i} \tag{1}
$$

where $\mu$ is the electric moment of a single dipole.

If we use the periodic boundary conditions, the problem is greatly simplified. As shown in Fig. 4, the circle with $N$ dipoles indicates the connection between first and last dipole.

Because the dipole interaction decreases quickly with the increase of distance, only the interactions of the nearest dipole need to be considered. Note that because of the infinite structure of the one-dimensional chain and $\sigma_{N+1}=\sigma_{1}$, Eq. (1) can be written more symmetrical:

$$
H(\sigma_{1}, \sigma_{2}, \cdots, \sigma_{N})=-J \sum_{i} \sigma_{i} \sigma_{i+1}-\frac{1}{2} \mu E \sum_{i=1}^{N}\left(\sigma_{i}+\sigma_{i+1}\right) \tag{2}
$$

Each state of the system is decided by $\sigma_{1}, \sigma_{2}, \ldots, \sigma_{N}$, where $\sigma_{i}$ has only two values +1 (electric moment upward) and -1 (electric moment downward), the distribution function is:

$$
\begin{aligned}
Z= & \sum_{j} e^{-\beta H_{j}}=\sum_{\sigma_{1}= \pm 1} \cdots \sum_{\sigma_{N}= \pm 1} \exp \left\{\beta \sum_{i=1}^{N}\left[J \sigma_{i} \sigma_{i+1}+\right.\right. \\
& \left.\left.\frac{1}{2} \mu E\left(\sigma_{i}+\sigma_{i+1}\right)\right]\right\}
\end{aligned} \tag{3}
$$

where $\beta=1 /(K T)$.

## 3. Results and discussion

Define an operator $\hat{P}$ in the space of electric moments, the matrix element is [24]:

$$
\left\langle\sigma_{i}|\hat{P}| \sigma_{i+1}\right\rangle=\exp \left\{\beta\left[J \sigma_{i} \sigma_{i+1}+\frac{1}{2} \mu E\left(\sigma_{i}+\sigma_{i+1}\right)\right]\right\} \tag{4}
$$

The eigenvector for dipole $\sigma_{k}=+1$ is $| \sigma_{+} \rangle=\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and for dipole $\sigma_{k}=-1$ $| \sigma_{-} \rangle=\begin{bmatrix} 0 \\ 1 \end{bmatrix}$, respectively, so the matrix

![](./images/813279044266098689_4.jpg)

Fig. 4. The periodic boundary condition.

element of $\hat{P}$ can be written:

$$
\begin{aligned}
& P_{11} \underset{\sigma_{i+1}=+1}{\stackrel{\sigma_{i}=+1}{=}} \exp \{\beta[J+\mu E]\} \quad P_{12} \underset{\sigma_{i+1}=-1}{\stackrel{\sigma_{i}=+1}{=}} \exp \{-\beta J\} \\
& P_{21} \underset{\sigma_{i+1}=+1}{\stackrel{\sigma_{i}=-1}{=}} \exp \{-\beta J\} \quad P_{22} \underset{\sigma_{i+1}=-1}{\stackrel{\sigma_{i}=-1}{=}} \exp \{\beta[J-\mu E]\}
\end{aligned} \quad (5)
$$

hence

$$
\hat{P}=\left[\begin{array}{cc}
\exp \{\beta[J+\mu E]\} & \exp \{-\beta J\} \\
\exp \{-\beta J\} & \exp \{\beta[J-\mu E]\}
\end{array}\right] \quad (6)
$$

so the distribution function is:

$$
\begin{aligned}
Z & =\sum_{j} e^{-\beta H_{j}} \\
& =\sum_{\sigma_{1}= \pm 1} \cdots \sum_{\sigma_{N}= \pm 1}\left\langle\sigma_{1}|\hat{P}| \sigma_{2}\right\rangle\left\langle\sigma_{2}|\hat{P}| \sigma_{3}\right\rangle \cdots\left\langle\sigma_{N}|\hat{P}| \sigma_{1}\right\rangle
\end{aligned} \quad (7)
$$

and with $\sum_{\sigma_{k}= \pm 1}\left|\sigma_{k}\right\rangle\left\langle\sigma_{k}\right|=1:$

$$
Z=\sum_{\sigma_{1}= \pm 1}\left\langle\sigma_{1}\left|\hat{P}^{N}\right| \sigma_{1}\right\rangle=\operatorname{Tr} \hat{P}^{N} \quad (8)
$$

If changing $\hat{P}$ into a digonal matrix, the eigenvalue appears in the diagonal and the trace can be easily calculated.

The eigenvalue of $\hat{P}$ can be obtained from the equation:

$$
\left|\begin{array}{cc}
\exp \{\beta[J+\mu E]\}-\lambda & \exp \{-\beta J\} \\
\exp \{-\beta J\} & \exp \{\beta[J-\mu E]\}-\lambda
\end{array}\right|=0
$$

$$
\lambda^{2}-2 \lambda e^{\beta J} \cosh (\beta \mu E)+2 \sinh (2 \beta J)=0
$$

with the solutions:

$$
\lambda_{1,2}=e^{\beta J} \cosh (\beta \mu E) \pm \sqrt{e^{-2 \beta J}+e^{2 \beta J} \sinh ^{2}(\beta \mu E)} \quad (9)
$$

So the distribution function is:

$$
Z=\operatorname{Tr} \hat{P}^{N}=\operatorname{Tr}\left[\begin{array}{cc}
\lambda_{1} & 0 \\
0 & \lambda_{2}
\end{array}\right]^{N}=\lambda_{1}^{N}+\lambda_{2}^{N} \quad (10)
$$

and the free energy of the system is:

$$
F(N, E, T)=-k T \ln Z=-k T \ln \left(\lambda_{1}^{N}+\lambda_{2}^{N}\right) \quad (11)
$$

The thermodynamics properties of the system can be obtained from the derivative of the free energy. Therefore, we introduce two useful abbreviations

$$
x=\beta \mu E=\frac{\mu E}{k T} \quad y=\beta J=\frac{J}{k T}
$$

Thus

$$
\lambda_{1,2}(x, y)=e^{y} \cosh x \pm \sqrt{e^{-2 y}+e^{2 y} \sinh ^{2} x} \quad (12)
$$

If we don't consider the interactions among dipoles ($J=0$, $y=0$):

$$
\begin{aligned}
\lambda_{1,2}(x, y) & =\cosh x \pm \sqrt{1+\sinh ^{2} x}=\cosh x \pm \cosh x \\
& = \begin{cases}2 \cosh x \\
0\end{cases}
\end{aligned}
$$

and free energy is:

$$
F(x, 0)=-N k T \ln Z=-N k T \ln (2 \cosh x) \quad (13)
$$

If no external field is considered, but considering the interaction among dipoles, the properties of the spontaneous polarization for the system can be obtained. Therefore, the total electric moment can be calculated:

$$
\begin{aligned}
P & =-\left.\frac{\partial F}{\partial E}\right|_{N, T}=-\beta \mu \frac{\partial F}{\partial x}=\mu \frac{\partial}{\partial x} \ln \left(\lambda_{1}^{N}+\lambda_{2}^{N}\right) \\
& =\mu N \frac{\lambda_{1}^{N-1} \frac{\partial}{\partial x} \lambda_{1}+\lambda_{2}^{N-1} \frac{\partial}{\partial x} \lambda_{2}}{\lambda_{1}^{N}+\lambda_{2}^{N}}
\end{aligned} \quad (14)
$$

Because

$$
\begin{aligned}
\frac{\partial}{\partial x} \lambda_{1,2} & =e^{y} \sinh x\left[1 \pm \frac{e^{y} \cosh x}{\sqrt{e^{-2 y}+e^{2 y} \sinh ^{2} x}}\right] \\
& =\frac{e^{y} \sinh x}{\sqrt{e^{-2 y}+e^{2 y} \sinh ^{2} x}}\left( \pm \lambda_{1,2}\right)
\end{aligned}
$$

according to Eq. (14), we get

$$
P=\mu N \frac{\lambda_{1}^{N}-\lambda_{2}^{N}}{\lambda_{1}^{N}+\lambda_{2}^{N}} \frac{\sinh x}{\sqrt{e^{-4 y}+\sinh ^{2} x}} \quad (15)
$$

Obviously, when there is no external field ($x=0$), $P=0$, i.e. the electric moment disappears. So the macroscopic spontaneous polarization of CCTO is zero when there is no external electric field.

Based on $P=\varepsilon_{0}(\varepsilon-1) E \approx \varepsilon_{0} \varepsilon E$ the relative dielectric constant of CCTO can be obtained:

$$
\varepsilon=\frac{P}{\varepsilon_{0} E}=\frac{\mu N}{\varepsilon_{0} E} \frac{\lambda_{1}^{N}-\lambda_{2}^{N}}{\lambda_{1}^{N}+\lambda_{2}^{N}} \frac{\sinh x}{\sqrt{e^{-4 y}+\sinh ^{2} x}} \quad (16)
$$

Because $\lambda_{1}>\lambda_{2}$ and $N \rightarrow \infty$, thus

$$
\frac{\lambda_{1}^{N}-\lambda_{2}^{N}}{\lambda_{1}^{N}+\lambda_{2}^{N}} \rightarrow 1
$$

so

$$
\varepsilon=\frac{\mu N}{\varepsilon_{0} E} \frac{\sinh x}{\sqrt{e^{-4 y}+\sinh ^{2} x}}=\frac{\mu N}{\varepsilon_{0} E} \frac{\sinh \left(\frac{\mu E}{k T}\right)}{\sqrt{\exp \left(-\frac{4 J}{k T}\right)+\sinh ^{2}\left(\frac{\mu E}{k T}\right)}}
$$

The $\varepsilon \sim T$ curve can be obtained based on Eq. (17) and is shown in Fig. 5, the fitting parameters for $N=3 \times 10^{21}$, $E=100 \mathrm{~V} \mathrm{~m}^{-1}, \mu=0.6309 \times 10^{-23} \mathrm{~J} \mathrm{~m} \mathrm{~V}^{-1}, J=-0.9315 \times$ $10^{-20} \mathrm{~J}$, respectively. It is found that the dielectric constant increases with the increase of temperature. Obviously, the theoretical curve is nearly consistent with the experimental curve.

### 4. Conclusions

The dielectric properties of CCTO were discussed based on the one-dimensional Ising model. It is found that the dielectric constant increases with the increase of temperature, at

![](./images/813279044266098689_5.jpg)

Fig. 5. Comparison of the theoretical curve and experimental curve at the frequency of $10^{6}$ Hz.

about 150 ~ 250 K there is a strong increase, and the dielectric constant is about $10^{4}$ at room temperature. Com- paring with the experimental curve, there is still a little dif- ference, the possible reason is that the theoretical model re- gards $Ti^{+4}$ displacement polarization and $O^{-2}$ electronic polarization as a strong correlation dipole in an electrostatic field, but does not consider the frequency response of the relaxation in an alternating electric field. A more strict dis- cussion will be reported in the near future.

This work was supported by the National Science Foundation of China (Grant No 10574066) and the Scientific Research Foundation of Henan University of Science and Technology (Grant No 2008ZY036, 2007QN060).

### References

[1] C.C. Homes, T. Vogt, S.M. Shaoirp, S. Wakimoto, A.P. Ramirez: Science 293 (2001) 673. PMid:11474105;
DOI:10.1126/science.1061655

[2] M.A. Subramanian, L. Dong, N. Duan, B.A. Reisner, A.W. Sleight: Solid State Chem. 151 (2000) 323.
DOI:10.1006/jssc.2000.8703

[3] D.C. Sinclair, T.A. Adams: Appl Phys Lett. 80 (2002) 2153.
DOI:10.1063/1.1463211

[4] C.C. Homes, T. Vogt, S.M. Shaoirp, S. Wakimoto, M.A. Subra- manian, A.P. Ramirez: Phys Rev B 67 (2003) 092106.
DOI:10.1103/PhysRevB.67.092106

[5] Y. Liu, R.L. Withers, X.Y. Wei: Phys Rev B 72 (2005) 134104.
DOI:10.1103/PhysRevB.72.134104

[6] S.F. Shao, J.L. Zhang, P. Zheng, C.L. Wang: Solid State Com- mun. 142 (2007) 281. DOI:10.1016/j.ssc.2007.02.025

[7] J. Li, A.W. Sleighta, M.A. Subramanian: Solid State Commun. 135 (2005) 260. DOI:10.1016/j.ssc.2005.04.028

[8] C.C. Wang, Y.J. Yan: Scripta Mater. 54 (2006) 1501.
DOI:10.1016/j.scriptamat.2005.12.047

[9] T.T. Fang, L.T. Mei, H.F. Ho: Acta Mater. 54 (2006) 2867.
DOI:10.1016/j.actamat.2006.02.037

[10] L. Fang, M.R. Shen: J. Cryst Growth 310 (2008) 3470.
DOI:10.1016/j.jcrysgro.2008.05.011

[11] B. Shri Prakash, K.B.R. Varma: Physica B 403 (2008) 2246.
DOI:10.1016/j.physb.2007.12.004

[12] S.D. Hutagalung, M.I.M. Ibrahim, Z.A. Ahmad: Ceram. Int. 34 (2008) 939. DOI:10.1016/j.ceramint.2007.09.074

[13] A.F.L. Almeida, R.R. Silva, H.H.B. Rocha, P.B.A. Fechine, F.S.A. Cavalcanti, M.A. Valente, F.N.A. Freire, R.S.T.M. Sohn, A.S.B. Sombra: Physica B 403 (2008) 586.
DOI:10.1016/j.physb.2007.08.222

[14] K.M. Kim, J.H. Lee, K.M. Lee, D.Y. Kim, D.H. Riu, S.B. Lee: Mater. Res. Bull. 43 (2008) 284.
DOI:10.1016/j.materresbull.2007.03.014

[15] C.M. Wang, K.S. Kao, S.Y. Lin, Y.C. Chen, S.C. Weng: J. Phys. Chem. Solids. 69 (2008) 608. DOI:10.1016/j.jpcs.2007.07.049

[16] C.K. Yeoh, M.F. Ahmad, Z.A. Ahmad: J. Alloy Compd. 443 (2007) 155. DOI:10.1016/j.jallcom.2006.10.016

[17] V.P.B. Marques, A. Ries, A.Z. Simoes, J.A. Varela, E. Longo: Ceram. Int. 33 (2007) 1187.
DOI:10.1016/j.ceramint.2006.04.003

[18] J.J. Mohamed, S.D. Hutagalung, M.F. Ain, K. Deraman, Z.A. Ah- mad: Mater. Lett. 61 (2007) 1835.
DOI:10.1016/j.matlet.2006.07.192

[19] L. Ni, X.M. Chen, X.Q. Liu, R.Z. Hou: Solid State Commun. 139 (2006) 45. DOI:10.1016/j.ssc.2006.05.015

[20] V. Brize, G. Gruener, J. Wolfman, K. Fatyeyeva, M. Tabellout, M. Gervais, F. Gervais: Mater. Sci. Eng. B 129 (2006) 135.
DOI:10.1016/j.mseb.2006.01.004

[21] G.L. Li, Z. Yin, M.S. Zhang: Phys. Lett. A 344 (2005) 238.
DOI:10.1016/j.physleta.2005.07.005

[22] J.H. You, Q.D. Chen, W.W. Ju, L.B. Li, K. Chen: Key Eng. Ma- ter. 368 (2008) 118.
DOI:10.4028/www.scientific.net/KEM.368-372.118

[23] D. Feng: Metal Physics (Volume II: Phase transition), Science Press, Beijing (1990).

[24] Y.X. Zhong: Thermodynamics and Statistcal Mechanics, Peking University Press, Beijing (2001).

(Received November 9, 2008; accepted May 8, 2009; on- line since August 23, 2012)

### Bibliography

DOI 10.3139/146.110839
Int. J. Mater. Res. (formerly Z. Metallkd.)
104 (2013) 2; page 175-178
© Carl Hanser Verlag GmbH & Co. KG
ISSN 1862-5282

### Correspondence address

Prof. Jinghan You
Henan University of Science and Technology
School of Science
48 Xiyuan Road
471003 Luoyang
P.R China
Tel: 86-379-64279209
E-mail: youjinghan0196@163.com

You will find the article and additional material by enter- ing the document number **MK110839** on our website at www.ijmr.de