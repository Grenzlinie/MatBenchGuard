# CALCULATION OF THE EFFECTIVE CHARGE OF
## CRYSTALS AND ITS VOLUME DEPENDENCE

A. BATANA* and J. A. O. BRUNO

Facultad de Ciencias Exactas y Naturales, Universidad de Buenos Aires, 1428 Buenos Aires, Argentina

(Received 13 February 1990; final revision received 27 November 1990;
received for publication 7 February 1991)

Abstract-A program for the calculation of the effective charge and its volume dependence of solids of NaCl, CsCl, CaF₂ and zincblende structures has been developed, which employs three different evaluations: (a) using the second Szigeti equation; (b) using the latter equation with $\gamma_{\mathrm{t}}=-(\partial \ln \omega_{\mathrm{t}} / \partial \ln V)$ obtained from the generalized first Szigeti equation; and (c) using Hardy's model for seven different short-range potential forms. It consists of the FORTRAN-77 program DLOGS.FOR, which reads the input data from up to three input files (INPUTx.INP, x = 1,2,3; each of them with up to four data sets), calls subroutines SZIG2.FOR, SZI G12.FOR and HARDY.FOR for the computations by the three evaluations mentioned, respectively, and produces the corresponding output files (OUTPUTx.OUT, x = 1,2,3). DLOGS.FOR uses subroutines DIFDAT.FOR and DIFMA.FOR for calculating percentual differences between data. HARDY.FOR uses subroutine TABDAT.FOR which performs calculations with the short-range potentials mentioned above.

## 1. INTRODUCTION

It is well known that any theoretical study of the properties of substances requires an adequate model which can explain as completely as possible the general behaviour of these substances.

In the case of ionic and partially-covalent crystals the Exchange Charge Model (Dick & Overhauser, 1958), the Shell Model (Cochran, 1959a, b) and the Deformation Dipole Model (Born & Huang, 1954; Hardy, 1962) are used (Barron et al., 1980); the three include the concept of effective charge of the ions. We shall focus on the frame of Hardy's Model (HM) (Hardy, 1962) which is a deformation dipole model, where the effective charge is taken as that first defined by Szigeti (1949), related to the dielectric, elastic and optical properties of crystals by:

$$
Z e s=\omega_{\mathrm{t}}\left(\frac{\epsilon_{0}-\epsilon_{\infty}}{4 \pi}\right)^{1 / 2}\left(\frac{3}{\epsilon_{\infty}+2}\right)\left(\mu v_{\mathrm{a}}\right)^{1 / 2}, \quad \text { (1) }
$$

where $Z e s$ is the effective ionic charge with $Z$ being the charge of the isolated cation, $e$ is the charge of the electron and $s$ is a parameter whose deviation from unity is interpreted within the HM as due to ionic distortion caused by the mutual interaction of neigh- bouring ions (Mitskevich, 1964), $\mu$ the reduced mass per ion pair, $v_{\mathrm{a}}$ the volume of a unit cell $(2 r^{3}$ for NaCl structure, $(8 / 3^{3 / 2}) r^{3}$ for CsCl and $(16 / 3^{3 / 2}) r^{3}$ for CaF₂ and zincblende structures, with $r$ being the cation-anion distance, $\omega_{\mathrm{t}}$ is the angular frequency of transverse optical waves at long wavelengths, $\epsilon_{0}$ the static dielectric constant and $\epsilon_{\infty}$ the dielectric con stant at frequencies $\omega \gg \omega_{\mathrm{t}}$.

Therefore, any calculation of those properties will include effective ionic charge data. Moreover, in areas such as geophysics, ceramics and the physics of semiconductors, studies related with the anharmonic contribution to elastic, dielectric and optical proper- ties due to high pressure are of interest. In these cases, the models require the evaluation of the volume derivative of the effective ionic charge $(\partial \ln s / \ln v)$. These theoretical studies are relevant because both the effective ionic charge and its volume derivative are not measured experimentally.

In this paper we present the FORTRAN 77 pro- gram DLOGS, which calculates the above quantities as well as the volume dependence of $\omega_{\mathrm{t}}$ and the parameters of the short-range potentials used in HM. The methods of calculation are described in Section 2. The program is described in Section 3, its input data are described in Section 4 and its output in Section 5. Conclusions and a test run are given in Sections 6 and 7, respectively.

## 2. METHODS OF CALCULATION

### 2.1. Szigeti II and Szigeti I + II methods

The volume dependence of the effective ionic charge can be obtained by differentiating equation (1) (known as the second Szigeti equation), that gives (Barron & Batana, 1969):

$$
\begin{aligned}
\left(\frac{\partial \ln s}{\partial \ln v}\right)=-\frac{1}{2 \chi_{\mathrm{t}}} & \left\{\frac { 1 } { \epsilon _ { 0 } - \epsilon _ { \infty } } \left[\left(\frac{\partial \epsilon_{0}}{\partial p}\right)_{\mathrm{T}}-\left(\frac{\partial \epsilon_{\infty}}{\partial p}\right)_{\mathrm{T}}\right]\right. \\
& \left.-\frac{2}{\epsilon_{\infty}+2}\left(\frac{\partial \epsilon_{\infty}}{\partial p}\right)_{\mathrm{T}}\right\}+\frac{1}{2}-\gamma_{\mathrm{t}}. \quad(2)
\end{aligned}
$$

* To whom all correspondence should be addressed.

where $\chi_{t}$ is the isothermal compressibility, and $\gamma_{t}=-(\partial \ln \omega_{t} / \partial \ln v)$.

We shall refer to the calculations made by the use of equation (2) as the Szigeti II method.

Equations (1) and (2) are strictly applicable at $T \to 0$ K (Barron & Batana, 1969; Batana & Hense, 1980; Batana & Soriano, 1983; Batana & Faour, 1984). Unfortunately, experimental values of $\gamma_{t}$ at this temperature are not available in the literature. An alternative way of obtaining $\gamma_{t}$ from available data is by differentiating with respect to the volume the generalized first Szigeti equation (Barron & Batana, 1969):

$$
\omega_{t}^{2}=\frac{1}{\mu}\left(\frac{\epsilon_{\infty}+2}{\epsilon_{0}+2}\right)\left(\frac{\theta r}{\chi_{t}}-\vartheta r p\right) \tag{3}
$$

where $r$ is the cation-anion distance at pressure $p, \theta$ and $\vartheta$ are 6 and 8 for NaCl structure, $8 / 3^{1 / 2}$ and $32 / 3^{3 / 2}$ for CsCl, $16 / 3^{1 / 2}$ and $64 / 3^{3 / 2}$ for $CaF_{2}$ and zincblende structures, respectively, that gives (Barron & Batana, 1969):

$$
\begin{aligned}
\gamma_{t}= & \frac{1}{2 \chi_{t}}\left\{\frac{1}{\epsilon_{\infty}+2}\left(\frac{\partial \epsilon_{\infty}}{\partial p}\right)_{\mathrm{T}}-\frac{1}{\epsilon_{0}+2}\left(\frac{\partial \epsilon_{0}}{\partial p}\right)_{\mathrm{T}}\right\} \\
& +\frac{1}{2} \frac{\partial B_{t}}{\partial p}-\frac{5}{6}-\frac{2}{3} \chi_{t} p\left(1-\frac{4}{3} \chi_{t} p\right)^{-1}\left(\frac{4}{3}-\frac{\partial B_{t}}{\partial p}\right), \quad(4)
\end{aligned}
$$

where $B_{t}$ is the isothermal bulk modulus of the crystal and $B_{t}=\chi_{t}^{-1}$.

Equations (3) and (4) were introduced in the program at $p=0$. We shall refer to the calculations performed by the combination of equations (2) and (4) as the Szigeti I + II method.

### 2.2. Hardy method

Another way to obtain values of $(\partial \ln s / \partial \ln v)$ is by the use of a set of equations derived within the frame of HM.

A generalized expression of $(\partial \ln s / \partial \ln v)$ was recently derived starting from [Born & Huang (1954), equation (9-40), p. 115] and assuming that the magnitude of the deformation dipole $m(r)$ is proportional to a short-range potential $\phi(r)$ (Hardy, 1962). The resulting expression is (Batana et al., 1991):

$$
\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}\left[1-\frac{3 \phi^{\prime}(r)+r \phi^{\prime \prime}(r)}{\frac{2}{r} \phi(r)+\phi^{\prime}(r)}\right], \quad(5)
$$

where $s$ is a parameter according to the definition of the effective ionic charge $(Z e s)$ given by equation (1), $\phi(r)$ is the overlap repulsion energy which we took in different forms as will be described below, $\phi^{\prime}(r)$ and $\phi^{\prime \prime}(r)$ are the first and second derivatives of this short-range potential with respect to the cation-anion distance $r$.

We chose seven different two-parameter potential forms for $\phi(r)$ (Dutt et al., 1985). The values for the potential parameters were obtained by fitting $\phi(r)$ to the experimental values of $r_{0}$ and $\chi_{0}$, which are the cation-anion distance and the isothermal compressibility at the equilibrium volume of the crystal $(p=0)$, respectively, considering an interaction potential of the form:

$$
u(r)=\frac{Z_{+} Z_{-} e^{2} \alpha_{\mathrm{M}}}{r}+M \phi(r), \tag{6}
$$

where $\alpha_{\mathrm{M}}$ is the Madelung constant of the crystal and $M$ its coordination number ($M=6$ for NaCl, 8 for CsCl and $CaF_{2}$ and 4 for zincblende structure). The values of $(\partial \ln s / \partial \ln v)$ were obtained by replacing in equation (5) the analytical forms of $\phi(r), \phi^{\prime}(r)$ and $\phi^{\prime \prime}(r)$ and leaving the final expressions in terms of the potential parameters.

Now the full set of equations derived for each potential form is described. It consists of the analytical form of the potential, and the expressions for the first and second derivatives with respect to $r$, the potential parameters and $(\partial \ln s / \partial \ln v)$. The parameter $s$ is obtained from equation (1).

#### 2.2.1. Born-Landé potential.

$$
\phi(r)=A r^{-n}, \tag{7}
$$

$$
\phi^{\prime}(r)=-n r^{-1} \phi(r), \tag{8}
$$

$$
\phi^{\prime \prime}(r)=\left(n^{2}+n\right) r^{-2} \phi(r), \tag{9}
$$

$$
n=\alpha-1, \tag{10}
$$

$$
A=\zeta n^{-1} r_{0}^{(n-1)}, \tag{11}
$$

$$
\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}(n+1), \tag{12}
$$

where $A$ and $n$ are the potential parameters. Hereafter $\alpha$ and $\zeta$ stand for the relations:

$$
\alpha=\frac{\eta r_{0}^{4}}{\chi_{0} Z_{+} Z_{-} e^{2} \alpha_{\mathrm{M}}}+2, \tag{13}
$$

$$
\zeta=\frac{Z_{+} Z_{-} e^{2} \alpha_{\mathrm{M}}}{M}, \tag{14}
$$

with $\eta=18$ for the NaCl structure, $8.3^{1 / 2}$ for CsCl and $16.3^{1 / 2}$ for $CaF_{2}$ and zincblende structures.

#### 2.2.2. Born-Mayer potential.

$$
\phi(r)=B \exp \left(-r \rho^{-1}\right), \tag{15}
$$

$$
\phi^{\prime}(r)=-\rho^{-1} \phi(r), \tag{16}
$$

$$
\phi^{\prime \prime}(r)=\rho^{-2} \phi(r), \tag{17}
$$

$$
\rho=r_{0} \alpha^{-1}, \tag{18}
$$

$$
B=\zeta\left(\alpha r_{0}\right)^{-1} \exp (\alpha), \tag{19}
$$

$$
\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}\left(r_{0} \rho^{-1}-\frac{2}{r_{0} \rho^{-1}-2}\right), \quad(20)
$$

where $B$ and $\rho$ are the potential parameters.

#### 2.2.3. Hellmann potential.

$$
\phi(r)=B_{1} r^{-1} \exp \left(-r \rho_{1}^{-1}\right), \tag{21}
$$

$$
\phi^{\prime}(r)=-\left(\rho_{1}^{-1}+r^{-1}\right) \phi(r), \tag{22}
$$

$$
\phi^{\prime \prime}(r)=\left[r^{-2}+\left(\rho_{1}^{-1}+r^{-1}\right)^{2}\right] \phi(r), \tag{23}
$$

$$
\rho_{1}=\frac{2 r_{0}}{(\alpha-2)+\left[(\alpha-2)^{2}+4(\alpha-2)\right]^{1 / 2}}, \quad(24)
$$

$$B_{1}=\zeta\left(1+r_{0} \rho_{1}^{-1}\right)^{-1} \exp \left(r_{0} \rho_{1}^{-1}\right),\tag{25}$$

$$\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}\left(2+\frac{1}{\left(\rho_{1} r^{-1}\right)^{2}+\rho_{1} r^{-1}}\right),\tag{26}$$

where $B_{1}$ and $\rho_{1}$ are the potential parameters.

### 2.2.4. Wasastjerna potential.
$$\phi(r)=C r^{7} \exp (-\beta r),\tag{27}$$

$$\phi^{\prime}(r)=\left(7 r^{-1}-\beta\right) \phi(r),\tag{28}$$

$$\phi^{\prime \prime}(r)=\left[\left(7 r^{-1}-\beta\right)^{2}-7 r^{-2}\right] \phi(r),\tag{29}$$

$$\begin{aligned}
\beta=\left(2 r_{0}\right)^{-1}\{(\alpha+14) & \\
& \left.+\left[(\alpha+14)^{2}-28(\alpha+6)\right]^{1 / 2}\right\}, \quad(30)
\end{aligned}$$

$$C=-\zeta\left(7-\beta r_{0}\right)^{-1} r_{0}^{-8} \exp \left(\beta r_{0}\right),\tag{31}$$

$$\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}\left(\frac{9}{9-\beta r}+\beta r-7\right),\tag{32}$$

where $\beta$ and $C$ are the potential parameters.

### 2.2.5. Varshni-Shukla potential.
$$\phi(r)=\lambda_{1} \exp \left(-k_{1} r^{2}\right),\tag{33}$$

$$\phi^{\prime}(r)=-2 k_{1} r \phi(r),\tag{34}$$

$$\phi^{\prime \prime}(r)=\left[\left(2 k_{1} r\right)^{2}-2 k_{1}\right] \phi(r),\tag{35}$$

$$k_{1}=\frac{\alpha+1}{2 r_{0}^{2}}\tag{36}$$

$$\lambda_{1}=\zeta\left[r_{0}(\alpha+1)\right]^{-1} \exp \left(\frac{\alpha+1}{2}\right),\tag{37}$$

$$\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}\left(2 k_{1} r^{2}-\frac{2}{k_{1} r^{2}-1}-1\right).\tag{38}$$

where $\lambda_{1}$ and $k_{1}$ are the potential parameters.

### 2.2.6. Modified Varshni-Shukla potential.
$$\phi(r)=\lambda_{2} \exp \left(-k_{2} r^{3 / 2}\right),\tag{39}$$

$$\phi^{\prime}(r)=\left(-\frac{3}{2} k_{2} r^{1 / 2}\right) \phi(r),\tag{40}$$

$$\phi^{\prime \prime}(r)=\left(\frac{9}{4} k_{2}^{2} r-\frac{3}{4} k_{2} r^{-1 / 2}\right) \phi(r),\tag{41}$$

$$k_{2}=\frac{2}{3}\left(\alpha+\frac{1}{2}\right) r_{0}^{-3 / 2},\tag{42}$$

$$\lambda_{2}=\zeta\left[r_{0}\left(\alpha+\frac{1}{2}\right)\right]^{-1} \exp \left[\frac{2}{3}\left(\alpha+\frac{1}{2}\right)\right],\tag{43}$$

$$\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s}\left(1+\frac{3}{2} k_{2} r^{3 / 2}+\frac{9}{\frac{8}{k_{2} r^{3 / 2}}-6}\right),\quad(44)$$

where $\lambda_{2}$ and $k_{2}$ are the potential parameters.

### 2.2.7. Logarithmic potential.
$$\phi(r)=a \ln \left(1+b r^{-9}\right),\tag{45}$$

$$\phi^{\prime}(r)=-9 a b\left(b r+r^{10}\right)^{-1},\tag{46}$$

$$\phi^{\prime \prime}(r)=9 a b\left(10 r^{9}+b\right)\left(r^{10}+b r\right)^{-2},\tag{47}$$

$$b=\left[9(\alpha-1)^{-1}-1\right] r_{0}^{9},\tag{48}$$

$$a=\zeta\left[r_{0} b(\alpha-1)\right]^{-1},\tag{49}$$

$$\left(\frac{\partial \ln s}{\partial \ln v}\right)=\frac{1-s}{3 s} \frac{\ln (1+\xi)^{2}+\frac{9 \xi}{1+\xi}\left(1+\frac{9}{1+\xi}\right)}{\ln (1+\xi)^{2}-\frac{9 \xi}{1+\xi}},\quad(50)$$

where $a$ and $b$ are the potential parameters and $\zeta=b r^{-9}$.

We shall refer to the calculations made using these equations as the Hardy method.

## 3. DESCRIPTION OF THE PROGRAM

The program DLOGS.EXE consists of a main program called DLOGS.FOR linked with several subroutines that perform the calculations required according to the options given by the user; it requires up to three different data input files (INPUTx.INP, x being a number between 1 and 3), each one with up to four different data sets. The main program reads the input data written in files INPUTx.INP, calls the selected subroutines which are described below, and writes the output data in files OUTPUTx.OUT, with x the same as was described for the input files.

### 1. SUBROUTINE SZIG2 (CHISBT, ECERO, EINF,DECERO,DEINF,GAMAT,C11,C12,N1 5,DLNSO2,H1,CHISUB) (selected by the user, see the next section) (SZIGETI II method)
It calculates the logarithmic volume derivative of the effective charge using equation (2).

### 2. SUBROUTINE SZIG12 (CHISBT, ECERO, EINF, DECERO, DEINF, DECHI, DCMU, C11, C12, DEC11, DEC12, N15, DLNS12, H1, H2, H4, CHISUB, DECHJ, DCMUC, GAMAC). (selected by the user, see the next section) (SZIGETI I + II method)
It calculates $(\partial \ln s / \partial \ln v)$ using equation (2), with $\gamma_{i}$ obtained from equation (4), taking $p=0$.

### 3. SUBROUTINE HARDY (CHISBT, ECERO, EINF, C11, C12, RZ, CTEMAD, XMASAR, ZCAT, ZAN, OMEGAT, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, ENE, A, DLNS1, RO, B, DLNS2, RO1, B1, DLNS3, BETA, C, DLNS4, XK1, XLAM1, DLNS5, XK2, XLAM2, DLNS6, BE, AA, DLNS7, S, H1, H3, CHISUB, OMEGAS, R1) (selected by the user, see the next section) (Hardy method).
It calculates $(\partial \ln s / \partial \ln v)$ using equations (12), (20), (26), (32), (38), (44) and (50). The subroutine also calculates the potential parameters given by equations (10-11), (18-19), (24-25), (30-31), (36-37), (42-43) and (48-49). The parameter $s$ is obtained from equation (1).

### 4. SUBROUTINE DIFDAT (CHISUB, ECERO, EINF, DECERO, DEINF, GAMAT, DECHJ, C11, C12, DEC11, DEC12, RZ, CTEMAD, XMASAR, ZCAT, ZAN, OMEGAS, DCMUC,

DLNS02, DLNS12, GAMAC, S,DLNS1,
DLNS2, DLNS3, DLNS4, DLNS5, DLNS7,
N15, DIF) (always called)

It calculates the percentual difference between different sets of input data within each input file, and also the percentual difference between the corresponding different output data sets within each output file.

5. SUBROUTINE DIFMA (DIFM, M1*M, N15,
DIFMAX) (always called if HARDY is selected).

It calculates the maximum percentual difference between logarithmic volume derivatives of the effective charge obtained from different short-range potentials with subroutine HARDY.

6. SUBROUTINE TAB DAT (N15, N8, N9, N10,
N11, N12, N13, N14, XLIM1, XLIM2, R1,
ENE, A, RO, B, RO1, B1, BETA, C, XK1,
XLAM1, XK2, XLAM2, BE, AA, LL,
RADIO, PHI, PHIPRI, PHISEG, DOSRPH)
(selected by the user, see the next section).

It calculates the potential $\phi$, its first and second derivatives with respect to the cation-anion distance $r$ [equations (7-9), (15-17), (21-23), (27-29), (33-35), (39-41) and (45-47), respectively], and the $[(2/r)\phi(r)]$ values for a range of $r$s calculated between lower and upper limits given by the user.

All the results are tabulated and stored in individual files (one for each kind of interaction potential selected by the user), which are listed below:

<table>
<tbody>
<tr>
<td>
BORN-LANDE potential data correspond to files BLANDEX.DAT
</td>
</tr>
<tr>
<td>
BORN-MAYER potential data correspond to files BMAYERx.DAT
</td>
</tr>
<tr>
<td>
HELLMAN potential data correspond to files HELLMANx.DAT
</td>
</tr>
<tr>
<td>
WASASTJERNA potential data correspond to files WASASTx.DAT
</td>
</tr>
<tr>
<td>
VARSHNI-SHUKLA potential data correspond to files VSHUKLAX.DAT
</td>
</tr>
<tr>
<td>
MODIFIED VARSHNI-SHUKLA potential data correspond to files VSMODIFx.DAT
</td>
</tr>
<tr>
<td>
LOGARITHMIC potential data correspond to files LOGARITx.DAT
</td>
</tr>
</tbody>
</table>

with $x$ the same as was described for the data input files. The user can select the following options:

- The number of different input files to be processed.
- The number of simultaneous calculations within each input file.
- The methods of calculation.
- The different interaction potential forms involved in Hardy method computations.
- The possibility of obtaining a set of cation-anion distances $r$ and the corresponding values of potential $\phi$, its first and second derivatives with respect to $r$, and the relation $[(2/r)\phi(r)]$ for each $r$-value of the set.
- The isothermal compressibility data can be either entered by the user or calculated from elastic data by entering the elastic constants $C_{11}$ and $C_{12}$. The program will compute $\chi_t$ from the relation:
$$
\chi_{\mathrm{t}}=3\left(C_{11}+2 C_{12}\right)^{-1}. \tag{51}
$$
- The pressure derivative of the isothermal bulk modulus can be either entered by the user or calculated by the program, which will use one of the following relations, depending on the input data supplied by the user:
$$
\frac{\partial B_{\mathrm{t}}}{\partial p}=\frac{\partial \chi_{\mathrm{t}}^{-1}}{\partial p}=-\frac{1}{\chi_{\mathrm{t}}^{2}} \frac{\partial \chi_{\mathrm{t}}}{\partial p}=\frac{1}{3}\left(\frac{\partial C_{11}}{\partial p}+2 \frac{\partial C_{12}}{\partial p}\right), \tag{52}
$$
with $\chi_{\mathrm{t}}$ entered directly or calculated by equation (51).
- The transverse optical mode frequency can be either entered by the user or calculated by the program with equation (3), taking $p=0$.

The program was designed for PCs or true compatibles under IBM PC-DOS or Microsoft MS-DOS, and runs satisfactorily when it is compiled with a PROFESSIONAL FORTRAN COMPILER Version 1.0 (Ryan-McFarland).

### 4. DATA INPUT

Although the user may complete only the minimum data required according to the method or methods chosen, we will describe the complete input data to be written in each file INPUTx.INP. The minimum data required by each method will be detailed later. Each INPUTx.INP consists of:

#### (i) The following switches:

Line 1-N15: number of input data sets. $(N15=1,...,4)$ in I2.

Line 2-N1, N2, N3: switches for computation by the Szigeti II method, Szigeti I + II method and Hardy method, respectively, $(N1, N2, N3=0,1)$ in 3I2. Switches equal to zero stand for do not compute, and switches equal to 1 stand for compute.

Line 3-N4,..., N7: in 4I2, selection of the crystalline structure of the substance/s under study, in the following order: N4 for the NaCl structure, N5 for CsCl, N6 for the $\mathrm{CaF}_{2}$ and N7 for the zincblende structure. e.g. For substances with $\mathrm{CaF}_{2}$ structure the entry must be: 0 0 1 0.

Line 4-N8,...,N14: in 7I2, selection of interaction potential forms within the frame of HM. The order is as follows: N8 for the Born-Landé potential. N9 for Born-Mayer, N10 for Hellmann, N11 for Wasastjerna, N12 for Varshni-Shukla, N13 for

modified Varshni-Shukla and N14 for the logarithmic potential. Possible values are 0 (do not compute) and 1 (compute).

Line 5—N16, XLIM1, XLIM2: in (I2, 2(2X), F4.1)). N16 is a switch for calculation of potential $\phi$, its first and second derivatives with respect to the cation-anion distance $r$ and $[(2/r)\phi(r)]$ values for different $r$s. (N16 = 0,1). The zero value stands for do not calculate. The values of $r$ are calculated by the program between lower (XLIM1) and upper (XLIM2) limits given by the user in units of the cation-anion distance.

### (ii) The following arrays:

Line 6--NSAL: the name/s of the substance/s in k(A7,2X). Hereafter "k" stands for the number of input data sets in the file considered (given by N15).

Line 7---TEMP: temperature/s at which data were obtained in k(A7, 2X).

Line 8--CHISBT: isothermal compressibility (in units of $E - 11\ \text{m}^2\ \text{N}^{-1}$) in k(2X, F8.5).

Line 9-ECERO: static dielectric constant, in k(2X, F8.5).

Line 10-EINF: high-frequency dielectric constant, in k(2X, F8.5).

Line 11-DECERO: pressure derivative of the static dielectric constant (in units of $E - 11\ \text{m}^2\ \text{N}^{-1}$) in k(2X, F8.5).

Line 12--DEINF: pressure derivative of the high-frequency dielectric constant (in units of $E - 11\ \text{m}^2$ $\text{N}^{-1}$), in k(2X, F8.5).

Line 13-GAMAT: logarithmic volume derivative of the transverse optical mode frequency, in k(2X, F8.5).

Line 14-DECHI: pressure derivative of the isothermal compressibility (in units of $E - 11\ \text{m}^4\ \text{N}^{-2}$), in k(2X, F8.5).

Line 15-DCMU: pressure derivative of the bulk modulus, in k(2X, F8.5).

Line 16-C11: elastic constant $C_{11}$ (in units of $E + 11\ \text{N m}^{-2}$), in k(2X, F8.5).

Line 17-C12: elastic constant $C_{12}$ (in units of $E + 11\ \text{N m}^{-2}$), in k(2X, F8.5).

Line 18-DEC11: pressure derivative of $C_{11}$, in k(2X, F8.5).

Line 19-DEC12: pressure derivative of $C_{12}$, in k(2X, F8.5).

Line 20-RZ: cation-anion distance (in units of $E - 10$ m), in k(2X, F8.5).

Line 21-CTEMAD: Madelung constant, in k(2X, F8.5).

Line 22-ZCAT: charge of the cation, in k(2X, F8.5).

Line 23-ZAN: charge of the anion (absolute value), in k(2X, F8.5).

Line 24-XMASAR: reduced mass per ion pair (in units of E-26 kg) in k(2X, F8.5).

Line 25--OMEGAT: transverse optical mode frequency (in units of $E + 2\ \text{m}^{-1}$), in k(2X, F8.5).

Lines 26-30--OBSERV: observations made by the user, in format A.

At this point, we will detail the minimum data required for each computation method. The non-necessary lines may be either filled or left blank, as desired, except for those cases explicitly mentioned below.

**Necessary data for Szigeti II method:**
Complete lines: 1, 2, 8, 9, 10, 11, 12 and 13.

If the user wants the isothermal compressibility value from elastic data, complete lines: 1, 2, 9, 10, 11, 12, 13, 16 and 17. In this case the corresponding fields in line 8 must be left blank.

**Necessary data for Szigeti I + II method:**
Complete lines: 1, 2, 8, 9, 10, 11, 12 and 15.

For isothermal compressibility values from elastic data, complete lines: 1, 2, 9, 10, 11, 12, 15, 16 and 17. In this case the corresponding fields in line 8 must be left blank. If the pressure derivative of the isothermal bulk modulus values are not available, the user can choose from the following alternatives:
a-Complete lines: 1, 2, 8 (or 16 and 17), 9, 10, 11, 12 and 14.
b-Complete lines: 1, 2, 8 (or 16 and 17), 9, 10, 11, 12, 18 and 19.

**Necessary data for Hardy method:**
Complete lines: 1, 2, 3, 4, 9, 10, 20, 21, 22, 23, 24 and 25.

If the user wants the transverse optical mode frequency values from equation (3), complete lines: 1, 2, 3, 4, 8 (or 16 and 17), 9, 10, 20, 21, 22, 23 and 24. In this case blanks must be left in the corresponding fields of line 25.

---

## 5. OUTPUT

In this section the complete output data generated by the program is described. The order is as follows:

1. A list of input data, and their percentual differences between sets (these values are stored in the array DIF). In those cases where a zero or blank entry implies a calculation of that property by the program, that entry value is replaced with the calculated one, and this situation is indicated writing a "c" beside the new value (these characters are stored in arrays H1, H2, H3 and H4).

In each line four results will appear corresponding to the four input data sets (N15 = 4). If N15 < 4 (i.e. 1, 2 or 3) zeros will appear in the last (3, 2 or 1) columns. Beside them the corresponding percentual differences already mentioned will appear.

The variables included in the list are now described in order of appearance (one array by line in the output file).

NSAL and TEMP: the same as described in Section 4.

CHISUB: stores either the isothermal compress- ibility input values if they were different from zero, or those calculated by equation (51).
ECERO, EINF, DECERO, DEINF and GAMAT: the same as described in Section 4.
DECHJ: stores either the pressure derivative of the isothermal compressibility input values if they were different from zero or the calculated from equation (52) if lines 16, 17, 18 and 19 were filled and Szigeti I+II method was chosen.
DCMUC: stores either the pressure derivative of the bulk modulus input values if they were different from zero, or the calculated from equation (52), if Szigeti I+II method was chosen.
C11, C12, DEC11, DEC12, RZ, CTEMAD, ZCAT, ZAN and XMASAR: the same as de- scribed in Section 4.
OMEGAS: stores either the transverse optical mode frequency input values if they were different from zero, or those calculated from equation (3) if the Hardy method was chosen.
2. If SZIGETI II method is selected: The values of NSAL, TEMP, $(\partial \ln s / \partial \ln v)$ stored in DLNS02 and their percentual differences between sets stored in DIF are written.
3. If SZIGETI I+II method is selected: the values of NSAL, TEMP, the Grüneisen gamma $(\gamma_{t})$ stored in GAMAC, the corresponding $(\partial \ln s / \partial \ln v)$ stored in DLNS12 and their percentual differences between sets stored in DIF are written.
4. If HARDY method is selected: (i) the values of NSAL and TEMP are written; (ii) the values of $s$ derived from the effective charge definition (Zes), stored in $S$ are written; (iii) the values of the inter action potential parameters and $(\partial \ln s / \partial \ln v)$ for each potential form selected, stored in the followingarrays:
maximum allowed for variable N15], potential $\phi$ , its first and second derivatives with respect to r and $[(2 / r) \phi(r)]$ for 60 r-values [stored respectively in arrays $PHI(60, M 1^{*} M), PHIPRI(60, M 1^{*} M)$ , PHISEG(60, M1*M) and DOSRPH(60, M1*M), Ml being a parameter that stands for the number of potential forms available for the HM compu- tations] are written in individual output files created by subroutine TABDAT, as was described in Section 3.
5. If lines 26-30 of the input files INPUTx.INP were filled, they will be written.
All the output data described are written in the files OUTPUTx.OUT, which are created by the exe- cutable file, with the exception of those results pro- vided by subroutine TABDAT.
## 6. CONCLUSIONS
In previous sections we pointed out the need of obtaining effective charge data and its volume depen- dence, and in this sense program DLOGS was devel- oped. Within it, several ways of calculating these quantities were performed and the reason why we did so lies in the fact that equations (2) and (4) (Szigeti II and Szigeti I+II Methods) are very sensitive toexperimental uncertainties (Barron & Batana, 1969;Batana & Hense, 1980; Batana & Soriano, 1983; Batana & Faour, 1984). Because of this, we included a theoretical calculation (HM) as a way of predicting( $\partial \ln s / \partial \ln v$ ) values. Due to its capability of making simultaneous calculations for several data sets and the format in which output data is presented. DLOGS allows the user to: (a) study the influence ofexperimental uncertainties; (b) update $(\partial \ln s / \partial \ln v)$  data; (c) compare results for different salts within the
| Potential         | Parameters | Parameters <br> stored in | $(\partial \ln s / \partial \ln v)$ <br> stored in |
|-------------------|------------|---------------------------|--------------------------------------------------|
| Born-Landé        | $A, n$     | A,ENE                     | DLNS1                                            |
| Born-Mayer        | $\rho, B$  | RO,B                      | DLNS2                                            |
| Hellmann          | $\rho_{1}, B_{1}$ | RO1,B1                  | DLNS3                                            |
| Wasastjerna       | $\beta, C$ | BETA,C                    | DLNS4                                            |
| Varshni-Shukla    | $k_{1}, \lambda_{1}$ | XK1,XLAM1              | DLNS5                                            |
| Modified V-S      | $k_{2}, \lambda_{2}$ | XK2,XLAM2              | DLNS6                                            |
| Logarithmic       | $a, b$     | AA,BE                     | DLNS7                                            |

and the percentual differences between these( $\partial \ln s / \partial \ln v$ ) values stored in DIF are written:(iv) another presentation of $(\partial \ln s / \partial \ln v)$ values in such a way that the influence of the different potential forms are easily analyzed, and the maximum percen- tual difference between those potential forms for the same input data set (these differences are stored in DIFMAX are written); and (v) the tabulated data of cation-anion distances r [stored in array RADIO-(60,M), M being a parameter whose value is the same model and vice versa; and (d) compare results- for different short-range potential forms with Hardy's model, in a simple, systematic and exhaustive way. Another usefulness of DLOGS lies in that with moreprecise $(\partial \ln s / \partial \ln v)$ data obtained from equation (2)(which imply more precise experimental measure- ments of elastic, dielectric and optical properties andtheir pressure dependence near 0 K, specially $\gamma_{t}$  measurements), the validity of Hardy's model and its parametrizations could be confirmed.

## 7. TEST RUN

Appendix A shows a typical input file in which some of the options described in Sections 3 and 4 are used. Note that in column 2 elastic data (lines 16-19) are used to calculate $\chi_{t}$ and $\partial B_{t} / \partial p$ (lines 8 and 15, respectively). In columns 2, 3 and 4 the values of $\omega_{t}$ (line 25) are calculated from equation (3). Due to the data used, values of $\partial \chi_{t} / \partial p$ are not necessary and in consequence line 14 is empty.

The corresponding output file (OUTPUT1.OUT) is shown in Appendix B.

According to the data at lines 2 (the three methods were selected) and 5 (potential calculations to be made between $0.9 r$ and $1.1 r$ with $r$ the equilibrium cation-anion distance were selected) in file INPUT1.INP, subroutine TABDAT is called. According to the data at line 4 (Born-Landé, Born-Mayer and Hellmann short-range potentials were selected) in file INPUT1.INP, TABDAT will create 3 files (BLANDE1.DAT, BMAYER1.DAT and HELLMAN1.DAT). In Appendix C the content of file BLANDE1.DAT for the 10 first values of set No. 1 is listed as an example.

Program availability-Program DLOGS listing, source and executable files are available at the Grupo de Quimica Teórica Departamento de Quimica Inorgánica, Analitica y Quimica Fisica, Facultad de Clencias Exactas y Naturales, Universidad de Buenos Aires, Pabellón II, Ciudad Universi- taria, (1428) Capital Federal, República Argentina.

Acknowledgments-The authors gratefully acknowledge the financial assistance given by the Universidad de Buenos Aires, Argentina.

## REFERENCES

Barron T. H. K. & Batana A. (1969) Phil. Mag. 20, 619.
Barron T. H. K., Collins J. G. & White G. K. (1980) Adv. Phys. 29, 609.
Barsch G. R. & Achar B. N. N. (1969) Phys. Stat. Sol. 35,881.
Bartels R. A. & Schuele D. E. (1965) J. Phys. Chem. Sol. 26,537.
Batana A. & Faour J. (1984) J. Phys. Chem. Sol. 45, 571.
Batana A. & Hense C. (1980) J. Phys. Chem. Sol. 41, 863.
Batana A. & Soriano M. R. (1983) J. Phys. Chem. Sol. 44,741.
Batana A., Castillo A. D. & Fracchia R. M. (1991) To be published.
Born M. & Huang K. (1954) Dynamical Theory of Crystal Lattices. Clarendon Press, Oxford.
Cochran W. (1959a) Phys. Rev. Lett. 2, 495.
Cochran W. (1959b) Proc. R. Soc. (Lond.) A253, 260.
Dick Jr B. G. & Overhauser A. W. (1958) Phys. Rev. 112,90.
Dutt N., Agrawal G. G. & Shanker J. (1985) Phys. Stat. Sol.85, 91.
Hardy J. R. (1962) Phil. Mag. 7, 315.
Madan M. P. (1971) J. Chem. Phys. 55, 464.
Mitskevich V. V. (1964) Sov. Phys. Sol. State 5, 2568.
Szigeti B. (1949) Trans. Faraday. Soc. 45, 155.

## APPENDIX A
### Listing of file INPUT1.INP

```
4
111
1000
1110000
1 .9 1.1
KC1 KC1 KBr KI
0K 300 K 300 K 300 K
5.07 7.04 9.09
4.49 4.85 4.91 5.10
2.20 2.17 2.36 2.64
-36.3 -49.6 -56.7 -61.6
3.79 4.37 9.92 10.10
2.46 2.46 2.83 2.11

5.34 5.63 6.42
     0.405
     0.0698
     12.89
      1.67
3.12 3.14 3.30 3.54
1.74756 1.74756 1.74756 1.74756
1. 1. 1. 1.
1. 1. 1. 1.
3.08761 3.08761 4.35967 4.96362
151.
Sources of data: (Barron & Batana, 1969) except Gamma from Madan
(1971) for sets 1,2,3 and Barsch & Achar (1969) for set 4. Elastic
data from Bartels & Schuele (1965).

&&&&&&&&&&&&&&&&& END OF DATA INPUT &&&&&&&&&&&&&&&&&
```

### APPENDIX B
Listing of file OUTPUT1.OUT

#### INPUT DATA

| VARIABLE                | SET #1<br>KCl<br>0 K | SET #2<br>KCl<br>300 K | SET #3<br>KBr<br>300 K | SET #4<br>KI<br>300 K | Z2-1 | Z3-1 | Z4-1(4)<br>Z3-2(3) | Z3-2 | Z4-2 | Z4-3 |
|-------------------------|----------------------|------------------------|------------------------|-----------------------|------|------|---------------------|------|------|------|
| Vol.compr.†1E-11 m2/N   | 5.07000              | 5.50863c               | 7.04000                | 9.89000               | 8.7  | 38.9 | 79.3                | 27.8 | 65.8 | 29.1 |
| Static dielec.const.    | 4.49000              | 4.85000                | 4.91000                | 5.10000               | 8.0  | 9.4  | 13.6                | 1.2  | 5.2  | 3.9  |
| High freq.diel.const    | 2.20000              | 2.17000                | 2.36000                | 2.64000               | -1.4 | 7.3  | 20.8                | 8.8  | 21.7 | 11.9 |
| d $\epsilon_0$/dP †1E-11 m2/N | -36.30000         | -49.60000              | -56.70000              | -61.60000             | 36.6 | 56.2 | 69.7                | 14.3 | 24.2 | 8.6  |
| d $\epsilon_\infty$/dP †1E-11 m2/N | 3.79000        | 4.37000                | 9.92000                | 18.10000              | 15.3 | 161.7| 166.5               | 127.0| 131.1| 1.8  |
| Gamma T                 | 2.46000              | 2.46000                | 2.83000                | 2.11000               | 0.0  | 15.8 | -14.2               | 15.0 | -14.2| -25.4|
| dV.comp/dP †1E-11 m4/N2 | 0.000                | -164.16bc              | 0.000                  | 0.0000                | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| d Bulk modulus/d P      | 5.34000              | 5.41000c               | 5.63000                | 6.42000               | 1.3  | 5.4  | 20.2                | 4.1  | 18.7 | 14.0 |
| C11 †1E11 N/m2          | 0.00000              | 0.40500                | 0.00000                | 0.00000               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| C12 †1E11 N/m2          | 0.00000              | 0.06980                | 0.00000                | 0.00000               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| d C11/dP                | 0.00000              | 12.89000               | 0.00000                | 0.00000               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| d C12/d P               | 0.00000              | 1.67000                | 0.00000                | 0.00000               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| Cat.-anion dist.†1E-10m | 3.12000              | 3.14000                | 3.30000                | 3.54000               | 0.6  | 5.8  | 13.5                | 5.1  | 12.7 | 7.3  |
| Madelung const.         | 1.74756              | 1.74756                | 1.74756                | 1.74756               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| Z cation                | 1.00000              | 1.00000                | 1.00000                | 1.00000               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| Z anion                 | 1.00000              | 1.00000                | 1.00000                | 1.00000               | 0.0  | 0.0  | 0.0                 | 0.0  | 0.0  | 0.0  |
| Reduced mass†1E-26 kg   | 3.08761              | 3.08761                | 4.35967                | 4.96362               | 0.0  | 41.2 | 60.8                | 41.2 | 60.8 | 13.9 |
| TO mode freq.†1E+2 m-1  | 151.00               | 137.76c                | 107.03c                | 93.05c                | -8.0 | -29.1| -38.4               | -22.3| -32.5| -13.1|

Data with a "c" were computed by the program.

---

#### OUTPUT DATA

##### SZIGETI II METHOD

|                | SET #1<br>KCl<br>0 K | SET #2<br>KCl<br>300 K | SET #3<br>KBr<br>300 K | SET #4<br>KI<br>300 K | Z2-1 | Z3-1 | Z4-1(4)<br>Z3-2(3) | Z3-2 | Z4-2 | Z4-3 |
|----------------|----------------------|------------------------|------------------------|-----------------------|------|------|---------------------|------|------|------|
| dln$\sigma$/dlnV | -0.05553            | 0.05810                | -0.15131               | 0.23267               | -204.6| 172.5| -519.0              | -360.4| 300.4| -253.8|

##### SZIGETI I+II METHOD

|                | SET #1<br>KCl<br>0 K | SET #2<br>KCl<br>300 K | SET #3<br>KBr<br>300 K | SET #4<br>KI<br>300 K | Z2-1 | Z3-1 | Z4-1(4)<br>Z3-2(3) | Z3-2 | Z4-2 | Z4-3 |
|----------------|----------------------|------------------------|------------------------|-----------------------|------|------|---------------------|------|------|------|
| dln$\sigma$/dlnV | -0.07279            | -0.10591               | -0.04735               | -0.63096              | 45.5 | -35.0| 766.8               | -55.3| 495.7| 1252.6|
| Gamma          | 2.47726              | 2.62482                | 2.72604                | 2.97363               | 5.9  | 10.0 | 20.0                | 3.9  | 13.3 | 9.1  |

### HARDY METHOD

|  |  | POTENTIAL & PARAM./(units) | SET #1 KCl 0 K | SET #2 KCl 300 K | SET #3 KBr 300 K | SET #4 KI 300 K | Z2-1 | Z3-1 | Z4-1(4) Z3-2(3) | Z4-2 | Z4-3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | s |  | 0.76250 | 0.78535 | 0.72879 | 0.69323 | 0.4 | -6.9 | -11.4 | -7.2 | -11.7 -4.9 |
| BORN-LANDE | n |  | 0.9344D+01 | 0.9879D+01 | 0.8521D+01 | 0.8713D+01 |  |  |  |  |  |
|  | A | (J.m**n) | 0.3459-108 | 0.1021-103 | 0.3893-100 | 0.9825-102 |  |  |  |  |  |
| dlns/dlnV |  |  | 0.95839 | 0.89999 | 1.18100 | 1.43275 | -6.1 | 23.2 | 49.5 | 31.2 | 59.2 21.3 |
| BORN-MAYER | r0 | (m) | 0.3016D-10 | 0.3179D-10 | 0.3466D-10 | 0.3645D-10 |  |  |  |  |  |
|  | B | (J) | 0.6470D-15 | 0.4226D-15 | 0.2917D-15 | 0.3230D-15 |  |  |  |  |  |
| dlns/dlnV |  |  | 0.93618 | 0.87686 | 1.14802 | 1.39450 | -6.3 | 22.6 | 49.0 | 30.9 | 59.0 21.5 |
| HELLMANN | r01 | (m) | 0.3374D-10 | 0.3578D-10 | 0.3922D-10 | 0.4112D-10 |  |  |  |  |  |
|  | B1 | (J.m) | 0.6800D-25 | 0.4453D-25 | 0.3220D-25 | 0.3832D-25 |  |  |  |  |  |
| dlns/dlnV |  |  | 0.95839 | 0.89999 | 1.18100 | 1.43275 | -6.1 | 23.2 | 49.5 | 31.2 | 59.2 21.3 |

---

### POTENTIALS

|  |  |  | B-Lande | B-Mayer | Hellman | Masast. | V.Shuk. | Mod V-S Logarit | MAX.DIFF% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SET #1 | KCl | 0 K | 0.9584 | 0.9362 | 0.9584 | 0.0000 | 0.0000 | 0.0000 | 0.0000 2.4 |
| SET #2 | KCl | 300 K | 0.9008 | 0.8769 | 0.9008 | 0.0000 | 0.0000 | 0.0000 | 0.0000 2.6 |
| SET #3 | KBr | 300 K | 1.1810 | 1.1480 | 1.1810 | 0.0000 | 0.0000 | 0.0000 | 0.0000 2.9 |
| SET #4 | KI | 300 K | 1.4327 | 1.3945 | 1.4327 | 0.0000 | 0.0000 | 0.0000 | 0.0000 2.7 |

---

### OBSERVATIONS:
Sources of data: (Barron & Batana, 1969) except Gamma from Madan
(1971) for sets 1,2,3 and Barsch & Achar (1969) for set 4. Elastic
data from Bartels & Schuele (1965).

---

## APPENDIX C
### Listing of file BLANDE1.DATA (first 10 values of set No. 1 only)

<table>
<thead>
<tr>
<th colspan="2">BLANDE1.DAT</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th>A-C DISTANCE</th>
<th>PHI</th>
<th>d PHI/d r</th>
<th>d2PHI/d2 r</th>
<th>2/r * PHI</th>
</tr>
<tr>
<th>xE-10 m</th>
<th>xE-19 J</th>
<th>xE-8 J/m</th>
<th>xE+2 J/m2</th>
<th>xE-9 J/m</th>
</tr>
<tr>
<th>Set #: 1</th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>2.8184</td>
<td>0.5980</td>
<td>-0.1976</td>
<td>0.7252</td>
<td>0.3820</td>
</tr>
<tr>
<td>2.8288</td>
<td>0.5758</td>
<td>-0.1902</td>
<td>0.8955</td>
<td>0.3691</td>
</tr>
<tr>
<td>2.8392</td>
<td>0.5564</td>
<td>-0.1831</td>
<td>0.6871</td>
<td>0.3587</td>
</tr>
<tr>
<td>2.8496</td>
<td>0.5377</td>
<td>-0.1783</td>
<td>0.6400</td>
<td>0.3447</td>
</tr>
<tr>
<td>2.8600</td>
<td>0.5197</td>
<td>-0.1698</td>
<td>0.6141</td>
<td>0.3331</td>
</tr>
<tr>
<td>2.8704</td>
<td>0.5024</td>
<td>-0.1835</td>
<td>0.5894</td>
<td>0.3220</td>
</tr>
<tr>
<td>2.8808</td>
<td>0.4857</td>
<td>-0.1575</td>
<td>0.5857</td>
<td>0.3113</td>
</tr>
<tr>
<td>2.8912</td>
<td>0.4698</td>
<td>-0.1518</td>
<td>0.5430</td>
<td>0.3010</td>
</tr>
<tr>
<td>2.9016</td>
<td>0.4541</td>
<td>-0.1462</td>
<td>0.5213</td>
<td>0.2911</td>
</tr>
<tr>
<td>2.9120</td>
<td>0.4392</td>
<td>-0.1409</td>
<td>0.5008</td>
<td>0.2815</td>
</tr>
</tbody>
</table>