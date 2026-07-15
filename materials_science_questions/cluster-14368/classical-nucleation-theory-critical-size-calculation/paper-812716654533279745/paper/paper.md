# Calculation of supersaturation maximum and droplet concentration at cloud boundaries

Mark Pinsky, Alexander Khain*

Department of Atmospheric Sciences, The Hebrew University of Jerusalem, Israel

![](./images/812716654533279745_1.jpg)

---

## ARTICLE INFO

**Keywords:**
Nucleation
Cloud base supersaturation maximum
Droplet concentration

## ABSTRACT

Most parameterizations of droplet concentration at cloud base in cloud models are derived under the assumption that all droplets at the cloud base form by nucleation of dry CCN crossing the lifting condensation level in updraft. In this study, a novel method of calculation of the supersaturation maximum and droplet concentration at cloud base is described that takes into account the existence of liquid at the level of droplet nucleation. Liquid exists in haze particles, as well as in the form of cloud droplets and raindrops. It is shown that the presence of liquid water inside non-activated CCN, as well as of cloud droplets and raindrops substantially decreases supersaturation maximum in case of high aerosol concentration. The possible effect of the supersaturation maximum decrease on formation of DSD in clouds is discussed. The method can be also applied to calculation of supersaturation and droplet nucleation at cloud edges.

---

## 1. Introduction

Droplet concentration is one of the most important parameters of cloud microphysics. Typically, most droplets are formed near cloud base via the process of activation of cloud condensational nuclei (CCN). The concentration of droplets nucleated at cloud base is largely caused by the value of supersaturation maximum $S_{\text{max}}$ and the CCN activation spectrum $N_{CCN}(S)$, determining the dependence of CCN concentration on supersaturation (see Khain and Pinsky, 2018). Droplets nucleated near cloud base play the dominating role in raindrop formation. For typical values of the vertical velocity at cloud base and typical activation spectra, the height of supersaturation maximum formation above cloud base varies from tens of centimeters to tens of meters. Since the vertical grid spacing in most cloud models is larger than the distance between the supersaturation maximum level and the lifting condensation level (LCL), the supersaturation maximum cannot be resolved in most cloud models (Ghan et al., 2011; Pinsky et al., 2012).

There are two main approaches to determine droplet concentration at cloud base used in cloud resolving models and large-scale models. The first one is utilization of parcel models offline or using lookup tables obtained from multiple simulations with the help of parcel models at different vertical velocities and CCN distributions (Segal and Khain, 2006). The second approach implies using parameterizations based on semi-analytical solution of the diffusional growth equation of aerosol particles above the level of zero supersaturation (e.g., von der Von der Emde and Wacker, 1993; Ghan et al., 1993, 1997, 2011; Cohard et al., 1998; Abdul-Razzak and Ghan, 2000; Abdul-Razzak et al., 1998; Shipway and Abel, 2010). All these studies are based on the classical work by Twomey (1959) and analyze the process of droplet nucleation within an air volume ascending from cloud base (where supersaturation is equal to zero) at a given vertical velocity. The growth rate of newly nucleated droplets affects both the supersaturation profile and the supersaturation maximum. Thus, the above-mentioned studies considered a complicated process of continuously increasing droplet concentration within the narrow layer between the cloud base and the level of the supersaturation maximum. Mathematically, this approach implies solving a system of integral-differential equations for $S_{\text{max}}$ and droplet concentration expressed in terms of beta-functions and hypergeometric functions. The complexity of the equations increases as the CCN activation spectra and the CCN size distributions become more complex. The growth of small droplets slows down the supersaturation increase and leads to the appearance of supersaturation maximum. Aerosols ascending above the cloud base are considered dry until the moment of their activation, so the effects of liquid water within haze particles are neglected.

Pinsky et al. (2012) derived a simple analytical formula for $S_{\text{max}}$ based on the balance equation for supersaturation (Pinsky et al., 2013) and applied it to calculate droplet concentration at cloud base assuming mononodisperse (or narrow) size distribution of CCN. The expression for $S_{\text{max}}$ thus has a form:

---

* Corresponding author.
E-mail address: alexander.khain@mail.huji.ac.il (A. Khain).

https://doi.org/10.1016/j.atmosres.2019.104694
Received 26 June 2019; Received in revised form 24 September 2019; Accepted 24 September 2019
Available online 31 October 2019
0169-8095/ © 2019 Published by Elsevier B.V.

$$S_{\max }=E w^{3 / 4} N^{-1 / 2} \tag{1}$$

where $w$ is the velocity of air flow updraft at cloud base, $N$ is droplet concentration and $E$ is a coefficient depending on the thermodynamical parameters (see notations in Table A). This expression allows a simple procedure for calculating droplet concentration and $S_{\max }$. Indeed, the concentration of droplets is equal to concentration of CCN within the range of radii exceeding the critical value:

$$N=\int_{r_{n_{-} c r}}^{\infty} f\left(r_{n}\right) d r_{n} \tag{2}$$

where $f(r_n)$ is a given size distribution of dry aerosol particles and $r_{n,cr}$ is the critical radius of aerosols activated under $S_{\max }$. This critical radius relates to $S_{\max }$ as (e.g., Khain et al., 2000; Khain and Pinsky, 2018)

$$r_{n_{-} c r}=\frac{A}{3}\left(\frac{4}{B S_{\max }^{2}}\right)^{1 / 3} \tag{3}$$

where $A$ and $B$ are the coefficients in the Kohler equation $S=\frac{A}{r}-\frac{B r_{n}^{3}}{r^{3}}$ relating radius of dry soluble particle $r_{n}$, haze particle radius $r$ and supersaturation in the equilibrium state. The expressions for coefficients $A$ and $B$ are presented in Table A.

Eqs. (1), (2), and (3) lead to the transcendental equation with respect to $S_{\max }$

$$S_{\max }\left[\int_{r_{n_{-} c r}}^{\infty} f\left(r_{n}\right) d r_{n}\right]^{1 / 2}=E w^{3 / 4} \tag{4}$$

Eq. (4) can be easily solved numerically using simple iterations. The solution of Eq. (4) agrees well with the results obtained with parcel model (Pinsky et al., 2012) as well with different parameterization expressions (Ghan et al., 2011). This approach applied by Ilotoviz and Khain (2016) in simulations of a hail storm enabled to obtain a reasonable cloud structure with a very pronounced cloud base. At the same time, it demonstrated the tendency to overestimate droplet concentration at cloud base, especially in case of very high aerosol concentration.

All parameterized approaches mentioned above, including parameterization described by Eqs. (1-4), were developed under the assumption that all droplets existing at cloud base formed as a result of nucleation of dry CCN ascending through cloud base. The presence of liquid water inside haze particles at zero supersaturation level was typically neglected. Another, even more important drawback of these parameterizations is neglecting the presence of raindrops falling through the cloud base, which leads to non-zero liquid water content (LWC) at cloud base. Significant LWC at the cloud base may also arise in storms producing a large amount of sea spray. Note that droplet nucleation can take place at cloud edges by entrainment of environmental aerosol into clouds above cloud base. Nucleation at cloud edges takes place also in the presence of LWC that has to affect supersaturation.

In addition to the physical reasons, there is a numerical reason for possible existence of droplets at cloud base in numerical cloud models. The altitude corresponding to $S=0$ (LCL) is typically located between model levels, so at the first level where $S>0$, considered as cloud base, droplets can already exist.

The existence of cloud droplets and raindrops at the cloud base should decrease $S_{\max }$, and correspondingly, the droplet concentration at cloud base (Shpund et al., 2019a). The decrease of $S_{\max }$ at cloud base can intensify in-cloud nucleation a few kilometers above cloud base, which in turn, significantly affects both the warm and the ice micro-structure of clouds (Pinsky and Khain, 2002; Khain et al., 2012; Khain and Pinsky, 2018; Ilotoviz and Khain, 2016; Fan et al., 2018; Shpund et al., 2019a, 2019b). Thus, ignoring the presence of drops at the cloud base may lead to significant errors in the microphysical structure of modeled clouds.

The goal of the present study is to generalize the algorithms of droplet nucleation at cloud base in order to take into account the existence of liquid water inside haze, as well as the possible presence of large liquid drops at LCL.

## 2. The universal profile of supersaturation at cloud base

We consider the profile of supersaturation in an isolated air parcel ascending at a constant velocity $w$. As shown by Pinsky et al. (2013), in case of monodisperse aerosol spectra the equation for supersaturation can be written as follows

$$\frac{d S}{d z}=A_{1}-\frac{3}{F w}\left(\frac{4 \pi \rho_{w} A_{2} N}{3 \rho_{a}}\right)^{2 / 3}\left(A_{1} z+C-S\right)^{1 / 3} S \tag{5}$$

where $A_{1}, A_{2}$ and $F$ are coefficients depending on the temperature at cloud base (see notations in Table A), $N$ is concentration of droplets nucleated at cloud base, and $C=A_{2} q_{0}$ is determined by the initial liquid water mixing ratio $q_{0}$ at cloud base. The value $q_{0}=q_{1}+q_{2}$ is determined by the sum of two quantities, namely of liquid water contained inside the haze particles $q_{1}$, and the liquid water associated with drops that can appear at cloud base due to processes of sedimentation, recirculation etc., $q_{2}$.

Eq. (5) was derived under the assumption that the aerosol spectra are monodisperse. Pinsky et al. (2014) showed that Eq. (5) can be applied for polydisperse aerosol spectra as well, since this equation leads to generation of the same height profiles of supersaturation in the monodisperse and polydispese cases. Applicability of Eq. (5) for polydisperse spectra was tested for cases where haze particles are present at cloud base. The tested spectra form at different aerosol concentration, depending on cloud type. To get supersaturation profiles similar to those in the monodisperse case, the mean CCN radius should be used to calculate $q_{0}$. We believe that this equation is also valid when drops formed due to other reasons are initially present at cloud base.

The differential equation for supersaturation (5) can be written in the normalized form (Pinsky et al., 2013, 2014). To do it, we introduce a non-dimensional parameter $R$,

$$R=\frac{3}{F A_{1} w}\left(\frac{4 \pi \rho_{w} A_{2} N}{3 \rho_{a}}\right)^{2 / 3}, \tag{6}$$

the normalized supersaturation $S^{*}$

$$S^{*}=R^{3 / 4} S, \tag{7}$$

and a non-dimensional height above cloud base, defined as the height where supersaturation is equal to zero, $S^{*}(z^{*}=0)=0$.

$$z^{*}=A_{1} R^{3 / 4} z \tag{8}$$

Eqs. (5-8) lead to the non-dimensional equation of supersaturation

$$\frac{d S^{*}}{d z^{*}}=1-\left(z^{*}+Q_{0}-S^{*}\right)^{1 / 3} S^{*} \tag{9}$$

In this equation, $Q_{0}$ is the normalized initial liquid mixing ratio at cloud base, calculated as

$$
\begin{aligned}
Q_{0} & =R^{3 / 4} C \\
& =\left(\frac{3}{F A_{1} w}\right)^{3 / 4}\left(\frac{4 \pi \rho_{w} A_{2} N}{3 \rho_{a}}\right)^{3 / 2} r_{0}^{3}+\left(\frac{3}{F A_{1} w}\right)^{3 / 4}\left(\frac{4 \pi \rho_{w} A_{2} N}{3 \rho_{a}}\right)^{1 / 2} A_{2} q_{2}
\end{aligned}
\tag{10}
$$

The first term on right-hand side of Eq. (10) relates to haze particles having mean radius $r_{0}$, while the second term corresponds to drops that are exist at cloud base but are not the result of nucleation. Radius $r_{0}$ could be chosen in different ways. As shown by Pinsky et al. (2014), the mean haze particle radius at the level $S=0$ chosen as $r_{0}$ provides the best agreement between profiles of supersaturation calculated under very different aerosol conditions for monodisperse and polydisperse cases.

The Eq. (9) should be solved with the initial condition $S^{*}(z^{*}=0)=0$. Since $Q_{0}$ is the single free parameter in this equation, Eq. (9) describes a group of universal profiles of supersaturation. Several profiles $S^{*}(z^{*})$ at different values of $Q_{0}$ are shown in Fig. 1.

![](./images/812716654533279745_2.jpg)

Fig. 1. Profiles $S^{*}(z^{*})$ at different values of $Q_{0}$.

The figure shows that an increase in $Q_{0}$ value leads to a decrease in supersaturation maximum. At $Q_{0}=5$ the supersaturation maximum twice as low as at $Q_{0}=0$. An increase in $Q_{0}$ indicates that droplets or haze at cloud base absorb water vapor decreasing both $S_{max}$ and the corresponding droplet concentration. Fig. 1 is for $w = const$ when supersaturation tends to zero at $z=\infty$. So, we have the supersaturation equal to zero both at the cloud base and at higher cloud levels, which indicates the existence of a supersaturation maximum at any value of $Q_{0}$, even at very high values. The supersaturation maximum can disappear if the updraft velocity slowly increases with height (Pinsky and Khain, 2002).

### 3. Supersaturation maximum
Since parameter $Q_{0}$ is a single free parameter in Eq. (9), the maximum of normalized supersaturation, $S_{max}^{*}$, and the non-dimensional height where this maximum is located $z_{max}^{*}$ depend on parameter $Q_{0}$ only. At $Q_{0}=0$ these quantities were calculated by Pinsky et al. (2012); the corresponding values are equal to $S_{max}^{*}=1.058$ and $z_{max}^{*}=1.904$. The universal functions $S_{max}^{*}(Q_{0})$ and $z_{max}^{*}(Q_{0})$were calculated using Eq. (9) and are shown in Fig. 2.

The figure shows that an increase in $Q_{0}$ value leads to a decrease in supersaturation maximum and to an increase in the height of its

<table><thead><tr><th colspan="6">Table 1Values of $S_{max}^{*}(Q_{0})$ and $z_{max}^{*}(Q_{0})$.</th></tr><tr><th>$Q_{0}$</th><th>$S_{max}^{*}$</th><th>$z_{max}^{*}$</th><th>$Q_{0}$</th><th>$S_{max}^{*}$</th><th>$z_{max}^{*}$</th></tr></thead><tbody><tr><td>0</td><td>1.0540</td><td>1.9080</td><td>1.6000</td><td>0.6931</td><td>2.0960</td></tr><tr><td>0.1000</td><td>0.9589</td><td>1.9930</td><td>1.7000</td><td>0.6850</td><td>2.0970</td></tr><tr><td>0.2000</td><td>0.9147</td><td>2.0210</td><td>1.8000</td><td>0.6772</td><td>2.0970</td></tr><tr><td>0.3000</td><td>0.8821</td><td>2.0390</td><td>1.9000</td><td>0.6698</td><td>2.0970</td></tr><tr><td>0.4000</td><td>0.8557</td><td>2.0520</td><td>2.0000</td><td>0.6628</td><td>2.0970</td></tr><tr><td>0.5000</td><td>0.8333</td><td>2.0610</td><td>2.1000</td><td>0.6561</td><td>2.0970</td></tr><tr><td>0.6000</td><td>0.8139</td><td>2.0690</td><td>2.2000</td><td>0.6497</td><td>2.0970</td></tr></tbody></table>

location. Values $S_{max}^{*}$ and $z_{max}^{*}$ are rigidly connected by equation

$$(z_{\max }^{*}+Q_{0}-S_{\max }^{*})^{1/3}S_{\max }^{*}=1\qquad(11)$$

Function $S_{max}^{*}(Q_{0})$ is essential for calculating droplet concentration at cloud base. The relevant dependence is presented in Table 1 containing values of $S_{max}^{*}(Q_{0})$ and $z_{max}^{*}(Q_{0})$.

After calculating normalized values of the supersaturation maximum and the height of its location using Fig. 2 and Table 1, one can calculate non-normalized values of supersaturation maximum and the corresponding height as

$$S_{\max }=R^{-3/4}S_{\max }^{*}(Q_{0})\qquad(12)$$

$$z_{\max }=\frac{1}{A_{1}}R^{-3/4}z_{\max }^{*}(Q_{0})\qquad(13)$$

To calculate droplet concentration just above the cloud base, one needs to know the mean radius of haze particles $r_{0}$ at cloud base (Eq.10). To calculate it one should use the relationship between droplet concentration, mean radius $r_{0}$ and supersaturation maximum $S_{max}$ near cloud base. Let's denote the predetermined size distribution of dry aerosol particles as $f(r_{n})$, and dry aerosol radius as $r_{n}$. Knowing the maximum value of supersaturation, one can evaluate droplet concentration and the radius of haze particles $r$ from the Kohler equation

$$S \approx \frac{A}{r}-\frac{Br_{n}^{3}}{r^{3}}\qquad(14)$$

The relationship between the radii of wet and dry aerosols at cloud base (at $S=0$) is calculated from Eq. (14) as

$$r=\sqrt{\frac{B}{A}}r_{n}^{3/2}\qquad(15)$$

To determine the mean radius $r_{0}$ one should take into account that only some fraction of aerosols with radius exceeding $r_{n\_cr}$ is nucleated at cloud base. The critical aerosol radius can be also calculated from Eq.(14) using condition $\frac{dS}{dr}=0$. The expressions for the critical radius $r_{n\_cr}$ and for droplet concentration were given above (Eqs. (2) and (3), respectively). The mean radius $r_{0}$ then is calculated as

![](./images/812716654533279745_3.jpg)

Fig. 2. Functions $S_{max}^{*}(Q_{0})$ (left) and $z_{max}^{*}(Q_{0})$ (right).

<table>
<caption>Table 2<br>Aerosol distribution parameters for four tested casesª</caption>
<thead>
<tr>
<th>Aerosol</th>
<th colspan="3">Nuclei Mode</th>
<th colspan="3">Accumulation Mode</th>
<th colspan="3">Coarse Mode</th>
</tr>
<tr>
<th></th>
<th>$R_1$</th>
<th>$\sigma_1$</th>
<th>$N_1$</th>
<th>$R_2$</th>
<th>$\sigma_2$</th>
<th>$N_2$</th>
<th>$R_3$</th>
<th>$\sigma_3$</th>
<th>$N_3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Marine</td>
<td>0.005</td>
<td>1.6</td>
<td>340</td>
<td>0.035</td>
<td>2.0</td>
<td>60</td>
<td>0.31</td>
<td>2.7</td>
<td>3.1</td>
</tr>
<tr>
<td>Clean continental</td>
<td>0.008</td>
<td>1.6</td>
<td>1000</td>
<td>0.034</td>
<td>2.1</td>
<td>800</td>
<td>0.46</td>
<td>2.2</td>
<td>0.72</td>
</tr>
<tr>
<td>Background</td>
<td>0.008</td>
<td>1.7</td>
<td>6400</td>
<td>0.038</td>
<td>2.0</td>
<td>2300</td>
<td>0.51</td>
<td>2.16</td>
<td>3.2</td>
</tr>
<tr>
<td>Urban</td>
<td>0.007</td>
<td>1.8</td>
<td>106,000</td>
<td>0.027</td>
<td>2.16</td>
<td>32,000</td>
<td>0.43</td>
<td>2.21</td>
<td>5.4</td>
</tr>
</tbody>
</table>

$^{\text{a}}$ From Ghan et al. (2011). The aerosol radii and the width of aerosol modes are given in $\mu$m, concentrations in the modes in cm$^{-3}$.

$$
r_{0}=\frac{1}{N} \sqrt{\frac{B}{A}} \int_{r_{n_{-} c r}}^{\infty} r_{n}^{3 / 2} f\left(r_{n}\right) d r_{n}
\tag{16}
$$

Distribution of dry aerosol is often presented in the form of a trimodal lognormal distribution

$$
f\left(r_{n}\right)=\sum_{i=1}^{3} \frac{N_{i}}{r_{n} \sqrt{2 \pi} \log \sigma_{i} \ln 10} \exp \left\{-\frac{\left(\log r_{n} / R_{i}\right)^{2}}{2\left(\log \sigma_{i}\right)^{2}}\right\}
\tag{17}
$$

where $N_i$, $R_i$ and $\sigma_i$ are given parameters characterizing the $i$-th mode. In this case, the integrals (2) and (16) can be calculated analytically

$$
N=\sum_{i=1}^{3} \frac{N_{i}}{2}\left[1-\operatorname{erf}\left(\frac{\ln r_{n_{-} c r} / R_{i}}{\sqrt{2\left(\ln \sigma_{i}\right)^{2}}}\right)\right]
\tag{18}
$$

$$
r_{0}=\frac{1}{N} \sum_{i=1}^{3} \frac{N_{i}}{2} R_{i}^{*} \exp \left(\frac{1}{2} \alpha_{i}^{2}\right)\left[1+\operatorname{erf}\left(\frac{\ln R_{i}^{*}+\alpha_{i}^{2}-\ln r^{*}}{\sqrt{2} \alpha_{i}}\right)\right]
\tag{19}
$$

where $\text{erf}(y)$ is the error function, and parameters $r^{*}$, $\alpha_i$ and $R_i^{*}$ are calculated as.

$$
r^{*}=\sqrt{\frac{B}{A}} r_{n_{-} c r}^{3 / 2}, \quad \alpha_{i}=\frac{3}{2} \ln \sigma_{i}, \quad R_{i}^{*}=\sqrt{\frac{B R_{i}^{3}}{A}}
\tag{20}
$$

### 4. Procedure for calculating supersaturation maximum and droplet concentration near cloud base

Using equations presented above, supersaturation maximum and droplet concentration near cloud base can be calculated by the following algorithm (iteration cycle):

a) set the initial value of $S_{\text{max}}$.
b) calculate critical aerosol radius using Eq. (3).
c) calculate droplet concentration using Eq. (2). In case aerosol distribution is described by log-normal modes, Eq. (18) can be used instead of Eq. (2).
d) calculate parameter $R$ using Eq. (6).
e) calculate the mean radius of haze particles $r_0$ using Eq. (16). In case aerosol distribution is described by log-normal modes, Eqs. (19–20) can be used instead of Eq. (16).
f) calculate normalized initial liquid water mixing ratio $Q_0$ using Eq. (10).
g) determine the value of $S_{\text{max}}^{*}(Q_0)$using Table 1.
h) calculate the new value of $S_{\text{max}}$ using Eq. (12), and then return to Step b).

The iterations should be repeated until the needed convergence of results is reached. The final values of droplet concentration and supersaturation maximum should be applied in cloud models to determine distributions of aerosols and droplets at cloud base to be used in further investigation of the cloud structure.

### 5. Sensitivity of the proposed algorithm to aerosol conditions and the initial LWC at cloud base

Pinsky et al. (2012) estimated droplet concentration near cloud base for clouds of different types developing under different aerosol distributions, neglecting the presence of liquid water at cloud base. The aerosol size distribution was defined as a trimodal lognormal distribution (Eq. 17) whose parameters were chosen following Ghan et al. (2011) for four types of clouds: “marine”, “clean continental”, “background” and “urban”. These parameters are given in Table 2.

In this section we compare the results obtained by Pinsky et al. (2012) using a simplified algorithm briefly described in Introduction (Eqs. (1–4)) with results obtained in the present study.

#### 5.1. Case 1: liquid water is contained inside haze particles

This is the case when $q_1 \neq 0$ and $q_2 = 0$. Figs. 3 and 4 show the dependences of the supersaturation maximum and the fraction of aerosol activated at cloud base on the vertical velocity. The dependences were calculated using the above-described procedure, at aerosol conditions presented in Table 2 used by Ghan et al. (2011) and later by Pinsky et al. (2012, 2014). The air temperature was chosen the same as in these studies ($T = 6^\circ\text{C}$). The dependences obtained using simpler and less accurate method by Pinsky et al. (2012) are also presented in Figs. 3 and 4 for comparison.

A significant difference between the results obtained using the presented approach and those obtained using the simplified approach (described by Eqs. (1–4)), takes place only in case of highly polluted atmosphere (Urban). In clouds of this type, the mass of liquid water within haze is large enough to affect $S_{\text{max}}$. In all the cases, the existence of water within haze particles leads to decreasing of $S_{\text{max}}$ and, therefore, to decreasing droplet number concentration. The activated fraction of aerosol concentration decreases significantly at low vertical velocities typical of small Cu and stratiform clouds. Indeed, at low vertical velocities supersaturation maximum is small, so only small fraction of aerosol is activated regardless of whether there is liquid water at the cloud base or not.

#### 5.2. Case 2: liquid drops are present at cloud base

This is the case when $q_1 = 0$ and $q_2 \neq 0$. Fig. 5 shows the dependences of supersaturation maximum on the vertical velocity (left) and of the activated fraction of aerosol concentration on the vertical velocity (right) for Marine clouds (see Table 2) at different initial liquid water mixing ratios $q_2$ at cloud base.

Fig. 6 shows the dependences of supersaturation maximum on the vertical velocity (left) and the activated fraction of aerosol concentration on the vertical velocity (right) for Clean Continental clouds (see Table 2) at different initial liquid water mixing ratios $q_2$ at cloud base.

In both cases one can see a significant effect of the initial LWC at cloud base. This effect is much stronger than that in the case of liquid water within haze. In Clean Continental case, significant LWC can

![](./images/812716654533279745_4.jpg)

Fig. 3. Dependences of supersaturation maximum on the vertical velocity in different cloud types at $q_{1} \neq 0$; $q_{2}=0$.

prevent nucleation until the vertical velocities exceed 0.3 m/s. In both cases, significant LWC at cloud base leads to a decreasing the fraction of activated CCN by more than twice at $w < 3$ m/s. The droplet concentration decreases accordingly. The results indicate the importance of taking into account the existence of liquid water at cloud base in all microphysical cloud models.

## 6. Conclusions

Most parameterizations of droplet concentration at cloud base are derived under the assumption that all the droplets form by nucleation of dry CCN crossing the lifting condensation level in updraft. Diffusion growth of haze particles is considered only after the end of nucleation.

![](./images/812716654533279745_5.jpg)

Fig. 4. Dependences of the aerosol fraction activated at cloud base on the vertical velocity in different cloud types (at $q_{1} \neq 0$; $q_{2}=0$).

![](./images/812716654533279745_6.jpg)

Fig. 5. Dependences of supersaturation maximum on the vertical velocity (left) and the aerosol fraction activated at cloud base on the vertical velocity (right) for Marine clouds at different initial liquid water mixing ratios at cloud base. "haze" corresponds to the case when $q_1=0$; $q_2 \neq 0$.

![](./images/812716654533279745_7.jpg)

Fig. 6. The same is in Fig. 5, but for Clean Continental clouds.

Since these small haze particles absorb comparatively little water vapor, the supersaturation maximum near cloud base may reach significant values, up to a few percent. This is the reason why supersaturation in the ascending volume does not exceed the value of supersaturation at cloud base, which often leads to the lack of in-cloud nucleation above cloud base and formation of unimodal and narrow DSDs.

In the present study, a new method of calculating the supersaturation maximum near cloud boundaries is described that takes into account the fact that aerosol particles being wet, contain a significant liquid fraction. The effects of cloud droplets and raindrops at the cloud base level on nucleation process are also investigated. Cloud droplets and raindrops at cloud base can appear due to drop falling, transport of sea spray, etc.

It is shown that the presence of liquid water in non-activated CCN substantially decreases supersaturation maximum in case of very high aerosol concentration. The presence of cloud droplets and raindrops at cloud base also leads to a decrease in supersaturation maximum at cloud base, substantially reducing the fraction of activated CCN.

A decrease in supersaturation maximum leads to larger amount of non-activated CCN ascending in cloud updrafts. This increases the probability of supersaturation in accelerating updrafts to exceed this maximum, which, in turn, will increase the intensity of in-cloud activation of aerosols that were not activated at cloud base. In-cloud nucleation leads to formation of bi-modal and multimodal wide DSDs, as well as to appearance of a large concentration of small ice crystals above the level of homogeneous freezing, thus strongly affecting cloud microphysics and cloud radiative properties. One can expect that the amount of droplets and raindrops at the cloud base level increases in the course of cloud evolution, leading to decreasing concentration of droplets nucleated at cloud base. It may be hypothesized that the intensity of in-cloud nucleation increases at the precipitating stage of cloud evolution. Additional investigations are required to investigate the role of intensification of in-cloud nucleation in the course of cloud evolution and its influence on accumulated rain, cloud ice concentration, cloud radiative properties and other cloud characteristics.

As was mentioned above, droplet nucleation can take place at cloud edges. The method developed here is applicable, in principle, for calculation of supersaturation at the cloud edges in the regions $w>0$. Equation for supersaturation (5) is strictly valid for adiabatic updrafts. In case of nucleation near cloud edges, mixing with environment may affect the supersaturation profile. This problem requires further investigation.

### Declaration of competing interest

We have no conflicts of interest.

### Acknowledgements

This research was supported by the Israel Science Foundation (grants 1393/14; 2027/17), the Office of Science (BER)., Partial support for this work was provided from grants DE-SC008811, DE-SC0014295 and ASR DE-FOA-1638 from the U.S. Department of Energy Atmospheric System Research program.

### Appendix

#### Table A
List of symbols.

<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Description</th>
      <th>Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$A$</td>
      <td>$\frac{2\varsigma_W}{\rho_W R_v T}$</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$A_1$</td>
      <td>$\frac{g}{R_d T}\left(\frac{L_W R_d}{c_p R_v T}-1\right)$</td>
      <td>m⁻¹</td>
    </tr>
    <tr>
      <td>$A_2$</td>
      <td>$\frac{1}{q_v}+\frac{L_W^2}{c_p R_v T^2}$</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$B$</td>
      <td>$\frac{\gamma_n \Phi_s \varepsilon_m M_W \rho_n}{M_n \rho_W}$</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$C$</td>
      <td>coefficient</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$c_p$</td>
      <td>specific heat capacity of moist air at constant pressure</td>
      <td>J kg⁻¹ K⁻¹</td>
    </tr>
    <tr>
      <td>$D$</td>
      <td>coefficient of water vapor diffusion in the air</td>
      <td>m² s⁻¹</td>
    </tr>
    <tr>
      <td>$e$</td>
      <td>water vapor pressure</td>
      <td>N m⁻²</td>
    </tr>
    <tr>
      <td>$E$</td>
      <td>$C_1(FA_1/3)^{3/4}\left(\frac{3\rho_d}{4\pi\rho_W A_2}\right)^{1/2}$, coefficient</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$e_w$</td>
      <td>saturation vapor pressure above the flat surface of water</td>
      <td>N m⁻²</td>
    </tr>
    <tr>
      <td>$g$</td>
      <td>acceleration of gravity</td>
      <td>m s⁻²</td>
    </tr>
    <tr>
      <td>$F$</td>
      <td>$\left(\frac{\rho_W L_W^2}{k_d R_v T^2}+\frac{\rho_W R_v T}{e_{W}(T) D}\right)$</td>
      <td>m⁻² s</td>
    </tr>
    <tr>
      <td>$f(r_n)$</td>
      <td>size distribution of dry aerosol particles</td>
      <td>m⁻⁴</td>
    </tr>
    <tr>
      <td>$k_a$</td>
      <td>coefficient of air heat conductivity</td>
      <td>J m⁻¹ s⁻¹ K⁻¹</td>
    </tr>
    <tr>
      <td>$L_w$</td>
      <td>latent heat for liquid water</td>
      <td>J kg⁻¹</td>
    </tr>
    <tr>
      <td>$M_n$</td>
      <td>molecular weight of aerosol salt</td>
      <td>kg mol⁻¹</td>
    </tr>
    <tr>
      <td>$M_w$</td>
      <td>molecular weight of water</td>
      <td>kg mol⁻¹</td>
    </tr>
    <tr>
      <td>$N$</td>
      <td>concentration of liquid droplets</td>
      <td>m⁻³</td>
    </tr>
    <tr>
      <td>$N_{CCN}(S)$</td>
      <td>CCN activation spectrum</td>
      <td></td>
    </tr>
    <tr>
      <td>$Q_0$</td>
      <td>normalized initial liquid water mixing ratio</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$q_v$</td>
      <td>water vapor mixing ratio</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$q_0$</td>
      <td>initial liquid water mixing ratio</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$q_1$</td>
      <td>liquid water mixing ratio inside haze</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$q_2$</td>
      <td>liquid water mixing ratio of drops at cloud base</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$r$</td>
      <td>liquid droplet radius</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$r_0$</td>
      <td>mean radius of wet aerosol at cloud base</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$r_n$</td>
      <td>radius of dry aerosol</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$r_{n\_cr}$</td>
      <td>critical radius of aerosol particles</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$R$</td>
      <td>$\frac{3}{FA_1 w}\left(\frac{4\pi\rho_W N A_2}{3\rho_d}\right)^{2/3}$</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$S$</td>
      <td>$S = e/e_w - 1$ supersaturation over water</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$S_{max}$</td>
      <td>maximum of supersaturation</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$T$</td>
      <td>absolute temperature</td>
      <td>°K</td>
    </tr>
    <tr>
      <td>$w$</td>
      <td>vertical velocity</td>
      <td>m/s⁻¹</td>
    </tr>
    <tr>
      <td>$z$</td>
      <td>height above LCL</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$z_{max}$</td>
      <td>height of supersaturation maximum normalized height of supersaturation maximum above</td>
      <td>m</td>
    </tr>
    <tr>
      <td>$z_{max}^*$</td>
      <td>LCL</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$\varepsilon_m$</td>
      <td>soluble fraction</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$\rho_a$</td>
      <td>air density</td>
      <td>kg m⁻³</td>
    </tr>
    <tr>
      <td>$\rho_N$</td>
      <td>density of a dry aerosol particle</td>
      <td>kg m⁻³</td>
    </tr>
    <tr>
      <td>$\rho_w$</td>
      <td>density of liquid water</td>
      <td>kg m⁻³</td>
    </tr>
    <tr>
      <td>$\sigma_w$</td>
      <td>surface tension of water-air interface</td>
      <td>N m⁻¹</td>
    </tr>
    <tr>
      <td>$\nu_n$</td>
      <td>the Van't Hoff factor</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$\Phi_s$</td>
      <td>molar osmotic coefficient</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

### References

Abdul-Razzak, H., Ghan, S.J., 2000. A parameterization of aerosol activation 2. Multiple aerosol types. J. Geophys. Res. 105 (D5), 6837-6844.

Abdul-Razzak, H., Ghan, S.J., Rivera-Carpio, C., 1998. A parameterization of aerosol activation. 1. Single aerosol type. J. Geophys. Res. 103 (D6), 6123-6131.

Cohard, J.-M., Pinty, J.-P., Bedos, C., 1998. Extending Twomey's analytical estimate of nucleated cloud droplet concentrations from CCN spectra. J. Atmos. Sci. 55, 3348-3357.

Fan, J., Rosenfeld, D., Zhang, Y., Giangrande, S.E., Li, Z., Machado, L.A.T., Martin, S.T., Yang, Y., Wang, J., Artaxo, P., Barbosa, H.M.J., Braga, R.C., Comstock, J.M., Feng, Z., Gao, W., Gomes, H.B., Mei, F., Pöhlker, C., Pöhlker, M.L., Pöschl, U., de Souza, R.A.F., 2018. Substantial convection and precipitation enhancements by ultrafine aerosol particles. Science 359 (6374), 411-418.

Ghan, S.J., Chuang, C.C., Penner, J.E., 1993. A parameterization of cloud droplet nucleation. Pt.1: single aerosol type. Atmos. Res. 30, 197-221.

Ghan, S.J., Leung, L.R., Easter, R.C., Abdul-Razzak, H., 1997. Prediction of cloud droplet number in a general circulation model. J. Geophys. Res. 112 (D18), 21,777-21,794.

Ghan, S.J., Hayder, A.-R., Nenes, A., Ming, Y., Xiaohong, L., Ovchinnikov, M., Shipway, B., Meskhidze, N., Xu, J., Shi, X., 2011. Droplet nucleation: physically-based parameterizations and comparative evaluation. J. Adv. Model. Earth Syst. 3, M10001 33 pp. https://doi.org/10.1029/2011MS000074.

Ilotoviz, E., Khain, A.P., 2016. Application of a new scheme of cloud base droplet nucleation in a spectral (bin) microphysics cloud model: sensitivity to aerosol size distribution. Atmos. Chem. Phys. 16, 14317-14329. https://doi.org/10.5194/acp-16-14317.

Khain, A.P., Pinsky, M., 2018. Physical Processes in Clouds and Cloud Modeling. Cambridge University Press, pp. 642.

Khain, A.P., Ovtchinnikov, M., Pinsky, M., Pokrovsky, A., Krugliak, H., 2000. Notes on the state-of-the-art numerical modeling of cloud microphysics. Atmos. Res. 55, 159-224.

Khain, A.P., Phillips, V., Bennoshe, N., Pokrovsky, A., 2012. The role of small soluble aerosols in the microphysics of deep maritime clouds. J. Atmos. Sci. 69, 2787-2807.

Pinsky, M., Khain, A.P., 2002. Effects of in-cloud nucleation and turbulence on droplet spectrum formation in cumulus clouds. Q. J. R. Meteorol. Soc. 128, 1-33.

Pinsky, M., Khain, A., Mazin, I., Korolev, A., 2012. Analytical estimation of droplet concentration at cloud base. J. Geophys. Res. 117, D18211. https://doi.org/10.1029/2012JD017753.

Pinsky, M., Mazin, I.P., Korolev, A., Khain, A., 2013. Supersaturation and diffusional droplet growth in liquid clouds. J. Atmos. Sci. 70, 2778-2793.

Pinsky, M., Mazin, I.P., Korolev, A., Khain, A., 2014. Supersaturation and diffusional droplet growth in liquid clouds: polydisperse spectra. J. Geophys. Res. Atmos. 119, 12,872-12,887.

Segal, Y., Khain, A., 2006. Dependence of droplet concentration on aerosol conditions in different cloud types: application to droplet concentration parameterization of aerosol conditions. J. Geophys. Res. 111, D15204.

Shipway, B.J., Abel, S.J., 2010. Analytical estimation of cloud droplet nucleation based on an underlying aerosol population. Atmos. Res. 96, 344-355.

Shpund, J., Khain, A.P., Rosenfeld, D., 2019a. Effects of sea spray on the dynamics and microphysics of an idealized tropical cyclone. J. Atmos. Sci. 76, 2213-2234.

Shpund, J., Khain, A.P., Rosenfeld, D., 2019b. Effects of sea spray on microphysics and intensity of deep convective clouds. J. Geophys. Res. 124, 9484-9509. https://doi.org/10.1029/2018JD029893.

Twomey, S., 1959. The nuclei of natural cloud formation: the supersaturation in natural clouds and the variation of cloud droplet concentration. Geofis. Pura Appl. 43, 243-249.

Von der Emde, K., Wacker, U., 1993. Comments on the relationship between aerosol spectra, equilibrium drop size spectra, and CCN spectra. Beitr. Phys. Atmosph. 66 (1-2), 157-162.