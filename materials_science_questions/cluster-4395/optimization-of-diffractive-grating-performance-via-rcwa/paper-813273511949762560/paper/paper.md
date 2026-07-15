# Arrays of doped and un-doped semiconductors for sensor applications

Thierry Taliercio · Vilianne N'Tsame Guilengui ·
Eric Tournié

Received: 17 February 2012 / Accepted: 10 October 2012 / Published online: 26 October 2012
© Springer-Verlag Berlin Heidelberg 2012

Abstract This numerical investigation proposes to use a lamellar grating of doped semiconductors as the active re- gion of a nanoplasmonic biosensing device. Working with highly doped semiconductors instead of a metal allows con- trolling the value of the plasma frequency. It is possible to reach a plasma frequency close to the range of detection of the sensor to improve its sensitivity. A red shift of the plas- monic resonance of 10.2 nm for a $10^{-2}$ refractive index unit increase can be achieved.

## 1 Introduction

Surface plasmon resonance (SPR) [1] sensing is a lead- ing technology for biosensing [2]. The principle is to de- tect small changes in the optical refractive index using the high sensitivity of the frequency of the SPR. Until now, the SPR biosensor technology is mainly based on the use of a metal on glass substrate which is not well suited for inte- gration and limited to the visible or near-infrared ranges. Mid-infrared (MIR) surface plasmon resonance has been re- cently investigated and showed a real potential [3] although based only on surface electromagnetic waves propagating at the metal-dielectric interface. To work at MIR wavelengths, ZnS prisms replace glass prisms.

Nanoplasmonics offers the possibility of high integra- tion without degrading the sensitivity of the device. Sev- eral works exploit the unique optical properties of nanoplas- monic structures on Si substrates, allowing proposing new architectures for biosensing [4, 5]. These new designs are based on gold or silver for the sensitive layer. Unfortu- nately both metals have drawbacks: Au is forbidden in mi- croelectronic environment because it generates deep levels in the band gap [6, 7], and Ag is highly reactive in aque- ous media. It is thus interesting to investigate new materials to bypass these limitations while maintaining high sensitiv- ity. In the present work we propose to use a lamellar grat- ing of doped semiconductors as active region for biosens- ing applications. The period of the grating is chosen to be largely sub-wavelength compared to the plasma wavelength of the doped semiconductor and of the wavelength of detec- tion. This allows exciting mainly localized surface plasmon (LSP) modes propagating vertically into the slits [8].

## 2 The metamaterial as sensing media

We used two approaches to model the optical properties of the lamellar structure: (i) an analytical model recently de- veloped [9], which allows us to save considerable time to roughly depict the adapted structure, (ii) a finite difference time domain (FDTD) software [10] to validate the selected structure. Indeed, the analytic model does not take into ac- count the surface plasmon polaritons (SPPs) propagating at the surface of the lamellar structure while in some cases it is necessary to consider them. Figure 1 represents a scheme of the structure. It consists of a highly anisotropic plasmonic medium (yellow).

The structure consists in a grating with a 520 nm period and a thickness of $1\ \mu$m. The widths of the slit and of the doped semiconductor are equal to 260 nm. The dielectric or liquid to analyze will be sitting in the slit. The wavelength corresponding to the plasma frequency of the semiconduc- tor is chosen close to $6\ \mu$m, which is a reasonable value to

T. Taliercio ( ) · V. N’Tsame Guilengui · E. Tournié
Institut d’Electronique du Sud, CNRS-INSIS-UMR 5214,
Université Montpellier 2, 34095 Montpellier Cedex 05, France
e-mail: thierry.taliercio@univ-montp2.fr

![](./images/813273511949762560_1.jpg)

![](./images/813273511949762560_2.jpg)

Fig. 1 Scheme of the lamellar grating of the doped semiconductor (yellow) and the dielectric or liquid (blue). The thickness of the lamel- lar grating is $h$, the period is $d$. $a$ and $b$ are respectively the widths of the doped semiconductor and of the studied liquid

reach [11]. In these conditions, we have recently demon- strated that the lamellar grating can be viewed as an ionic crystal characterized by an oscillator wavelength $\lambda_{r}$ under a transverse magnetic (TM) field and as a metal character- ized by a pseudo volume plasmon wavelength $\lambda_{t}$ under a transverse electric (TE) field [9]. We look at the transmis- sion of this metamaterial and try to evaluate its sensitivity to index variation of the dielectric material. It is also pos- sible to investigate the metamaterial in reflectance, which gives us equivalent sensitivity to the index variation. We fo- cus ourselves on the experimental configuration proposed in Ref. [5], in which a setup based on orthogonal linear light polarization of a laser beam was proposed. This particular optical configuration leads to a sensitivity improvement and noise reduction.

## 3 Results and discussion

Before investigating a particular structure we compare both models used in this study. Figure 2 shows the calculated transmittance of the previously defined lamellar grating us- ing the analytic model and the FDTD method. We can see a good agreement between both methods. The differences are due to the approximation of the analytic model that supposes that we are in the long-wavelength limit. However, the es- sential results are similar: resonances, amplitudes, etc. The real advantage of the analytic model is saving much time (several orders of magnitude) that allows us to quickly iden- tify the best structure. However, because of the imperfection of the analytical model, it is necessary to use FDTD simu- lation to refine the design of the structure and to obtain an accurate value of the sensitivity. In the remainder of the ar- ticle we just present FDTD results except when it will be specified.

![](./images/813273511949762560_3.jpg)

Fig. 2 Calculated transmittance at normal incidence of the lamellar grating with $a=b=260$ nm, $d=520$ nm, $h=1$ $\mu$m, using the FDTD method (dark symbols) and analytic model (red curve). The index of the dielectric part is taken equal to 1.5. The polarization is TM

![](./images/813273511949762560_4.jpg)

Fig. 3 Calculated transmittance at normal incidence of the lamellar grating with $a=b=260$ nm, $d=520$ nm, $h=1$ $\mu$m, in TM polar- ization (black symbols and red curve) and in TE polarization (green symbols and blue curve). The index of the liquid is taken equal to 1.5 (symbols) or 1.51 (lines). Vertical arrows show the wavelengths asso- ciated to $\lambda_{p}$ and to $\lambda_{t}$ and $\lambda_{r}$

We now study the lamellar structure to identify the more sensitive wavelength range. Figure 3 shows the calculated transmittance at normal incidence of the lamellar grating with $a=b=260$ nm, $d=520$ nm, $h=1$ $\mu$m, in TM polar- ization (black squares and red curve) and in TE polarization (green squares and blue curve). The vertical black arrows show respectively the wavelength associated to the plasma wavelength of the doped semiconductor $\lambda_{p}$ and $\lambda_{t}$ and $\lambda_{r}$. To demonstrate the sensing concept, the index of the studied material is taken equal to 1.5 (solid symbols) or 1.51 (solid lines). We can see that $\lambda_{t}$ is associated to the small shoul- der at 5.95 $\mu$m TM polarization (dark symbols). In the same time, $\lambda_{r}$ corresponds exactly to the pseudo volume plasma wavelength in TE polarization (green symbols). Both wave- lengths are degenerate due to identical values of $a$ and $b$ (see Ref. [9] for more details).

![](./images/813273511949762560_5.jpg)

![](./images/813273511949762560_6.jpg)

Fig. 4 Transmission variation $\Delta T$ for an index modification of $\Delta n=0.01$, under TM polarization (dark curve) and TE polarization (red curve). The summation of the absolute value of $\Delta T$ for both polarizations is the curve $\Sigma$ (blue)

The modulation of the transmitted signal at wavelengths larger than $\lambda_p$ is due to interference effects in the metamaterial layer which selects some LSP modes. To identify the best working area it is interesting to draw the transmittance modification, $\Delta T$, for an index variation of the dielectric medium from 1.50 to 1.51, that is $\Delta n=0.01$. Results are represented in Fig. 4. $\Delta T$ values are drawn for TM (dark) and TE polarizations (red). The blue curve corresponds to the summation of the absolute value of $\Delta T$ of both polarizations.

The small amplitude interferences observed for each spectrum are due to numerical artifacts arising from the step size in time and in space of FDTD techniques. They have no physical meaning. The zone of interest is obtained for the maximum amplitude of $\Sigma$. Indeed, this corresponds to the maximum sensitivity of the metamaterial. We obtain an amplitude modulation of $2.5$ % for a wavelength of $6.32\ \mu$m corresponding to $\lambda_W$. This is exactly the spectral range where spectra in both polarizations cross (see Fig. 4).

Figure 5 demonstrates the impact of the index variation on the calculated transmittance spectra in TE and TM polarizations. Figure 5 corresponds to a zoom of Fig. 3 for a wavelength around $\lambda_W$. The red arrow shows the red shift of the LSP resonance, 10.2 nm, due to a $10^{-2}$ refractive index unit (RIU) modification. This corresponds to a sensitivity of $1.02\times 10^3$ nm/RIU. This is comparable to values obtained with conventional SPR biosensors [3] in the same range of wavelengths, but smaller than which is achieved in the visible range [12]. Biosensors based on localized surface plasmon resonators (pillar [13], split ring resonator [14] in the near-infrared range), which are comparable to structures of this study, gave smaller values of sensitivity.

![](./images/813273511949762560_7.jpg)

Fig. 5 Zoom of the intersection between both spectra in TM and TE polarizations of Fig. 2. The dark and red arrows are respectively the amplitude modification between both polarizations and the red shift of the spectra in TM polarization due to index variation

The nanoplasmonic sensors are generally based on the measurement of the wavelength of the localized plasmons. It is also possible to propose intensity plasmonic sensing. In this configuration the wavelength is fixed (for example at $\lambda_W$) and the amplitude variation is measured for both polarizations by a detector behind the metamaterial [5]. In our case, an index variation of $\Delta n=0.01$ at a wavelength of $\lambda_W$ provokes an amplitude modification of $2.5$ %. This is in the same order of magnitude as in Ref. [5].

It is necessary to integrate this metamaterial into a complete device and evaluate its sensitivity in the MIR range.

## 4 Device proposition

We propose to study a device equivalent to that adopted in Ref. [5]. Figure 6 represents a scheme of the structure. It consists in a highly anisotropic plasmonic medium (yellow) deposited onto a MIR detector (gray). Linearly polarized light is injected backwards in the $y$ direction. The light to be detected should be a laser beam polarized along $x$ (TM polarized) or $z$ axes (TE polarized). The MIR detector should be a quantum well infrared photodetector (QWIP) [15], a quantum dot infrared photodetector (QDIP) [16] or a superlattice infrared photodetector (SLIP) [17].

Simulations of the complete structure are shown in Fig. 7. Spectra are somewhat modified by the presence of the detector layer behind the metamaterial. This is mainly due to the refractive-index difference between both faces of the metamaterial ($n_{\text{det}}=3.6$). The resonance associated to LSP is not deeply modified. As we can see, we conserve a good agreement between the FDTD simulation and the analytic model (red dashed line) around $6\ \mu$m (Fig. 7).

![](./images/813273511949762560_8.jpg)

![](./images/813273511949762560_9.jpg)

Fig. 6 Scheme of nanoplasmonic sensing. The lamellar grating of doped semiconductors (yellow) deposited onto a MIR detector (gray). The blue parts correspond to the liquid that will be analyzed

![](./images/813273511949762560_10.jpg)

Fig. 7 Calculated transmittance at normal incidence of the lamellar grating deposited on a detector modeled by a dielectric with an index of refraction $n_{\text{det}}=3.6$, in TE polarization (green symbols and blue curve) and in TM polarization (dark symbols and red curve). The index of the liquid is taken equal to 1.5 (symbols) or 1.51 (lines). The red dashed line corresponds to the calculated transmittance in TM polarization using the analytical model

On the other hand, at longer wavelengths we can see two resonances at 8 and 9.3 $\mu$m associated to SPPs propagating at both interfaces of the metamaterial. We do not detail much more this point and focus ourselves on the LSP resonance. The LSP resonance modifies a little bit their shape and wavelength as compared to the lamellar grating alone. This provokes a small blue shift until 6.24 $\mu$m. This demonstrates that the LSP is essentially sensitive to what is happening in the metamaterial.

Figure 8 shows a zoom of the transmittance spectra in TM (dark) and TE (red) polarizations for different indexes of liquid ($n=1.50$ for solid line curves and $n=1.51$ for dashed line curves). The sensitivity of the device is slightly degraded. We obtain a sensitivity of $7.8\times 10^{-2}$ nm/RIU.

The sensitivity of our devices should be comparable to those recently proposed [5]. To increase the sensitivity of the metamaterial we can adjust the size of the slit, $a$, compared to the ribbon width, $b$. Indeed, decreasing the ratio $a/b$ increases the sensitivity because the reflectance spectra for both polarizations cross in a range of very high reflectance signal variations. Of course it is necessary to keep a period of the array smaller than $\lambda_p$ and larger than 200 nm, (i) first because propagative modes appear in the range of wavelengths of interest reducing the sensitivity of the structure, (ii) second because the analytic model fails due to homogenization not being possible at all (iii) and third because of the technological limit (limit of resolution, large aspect ratio $h/a$). It is also quite easy to extend the validity of our metamaterial to longer wavelengths by modifying the doping level [11] of the semiconductor or the geometry of the system [9].

![](./images/813273511949762560_11.jpg)

Fig. 8 Zoom of the intersection between both spectra in TM and TE polarizations of Fig. 7. The dark and red arrows are respectively the amplitude modification between both polarizations and the red shift of the spectra in TM polarization due to index variation

## 5 Conclusions

Lamellar gratings of doped semiconductors are very interesting for the fabrication of integrated biosensors operating in the IR wavelength range. We have demonstrated that a sensitivity of $10^{-3}$ nm/RIU can be reached. The analytical model has allowed us to easily identify the best structure and using the FDTD simulation we have obtained an accurate design of the structure and of the expected performance. Experimental validation of this concept in the IR range is now needed. The use of doped semiconductors allows easy integration into silicon technology while maintaining high sensitivity. By simply adjusting the geometry or the doping level it is possible to control efficiently the resonance position of the LSP. This allows finely defining the kind of biological material to be detected to be much more selective. It is also possible to extend the use of doped semiconductors to experimental techniques such as surface enhanced infrared absorption (SEIRA) spectroscopy by adapting the geometry of the metamaterial.

![](./images/813273511949762560_12.jpg)

### References

1. H. Reather, *Surface Plasmons on Smooth and Rough Surfaces and on Gratings*. Springer Tracts Mod. Phys., vol. 111 (Springer, Berlin, 1988)
2. B. Liedberg, C. Nylander, I. Lundström, Biosens. Bioelectron. **10**(8), i (1995)
3. M. Golosovsky, V. Lirtsman, V. Yashunsky, D. Davidov, B. Aroeti, J. Appl. Phys. **105**, 102036 (2009)
4. Y. Wang, X. Su, Y. Zhu, Q. Wang, D. Zhu, J. Zhao, S. Chen, W. Huang, S. Wu, Appl. Phys. Lett. **95**, 241106 (2009)
5. L. Guyot, A.-P. Blanchard-Dionne, S. Patskovsky, M. Meunier, Opt. Express **19**, 9962 (2011)
6. J.D. Struthers, J. Appl. Phys. **27**, 1560 (1956)
7. H. Feichtinger, in *Electronic Structure and Properties of Semi- conductors*, Materials Science and Technology, vol. 4, ed. by W. Schröter (VCH, Weinheim, 1991), pp. 143–195

8. J.A. Porto, F.J. Garcia-Vidal, J.B. Pendry, Phys. Rev. Lett. **83**, 2845 (1999)
9. J. Léon, T. Taliercio, Phys. Rev. B **82**, 195301 (2010)
10. FDTD Solutions 8.0, Lumerical Solutions, Inc., Canada
11. Y.B. Li, R.A. Stradling, T. Knight, J.R. Birch, R.H. Thomas, C.C. Philips, I.T. Ferguson, Semicond. Sci. Technol. **8**, 101 (1993)
12. J. Homola, S.S. Yee, G. Gauglitz, Sens. Actuators B, Chem. **54**, 3 (1999)
13. C.-C. Liang, M.-Y. Liao, W.-Y. Chen, T.-C. Cheng, W.-H. Chang, C.-H. Lin, Opt. Express **19**, 4768 (2011)
14. Y.T. Chang, Y.-C. Lai, C.-T. Li, C.-K. Chen, T.-J. Yen, Opt. Ex- press **18**, 9561 (2010)
15. J.Y. Andersson, L. Lundqvist, Appl. Phys. Lett. **59**, 857 (1991)
16. K.W. Berryman, S.A. Lyon, M. Segev, Appl. Phys. Lett. **70**, 1861 (1997)
17. J.B. Rodriguez, C. Cervera, P. Christol, Appl. Phys. Lett. **97**, 251113 (2010)

![](./images/813273511949762560_13.jpg)