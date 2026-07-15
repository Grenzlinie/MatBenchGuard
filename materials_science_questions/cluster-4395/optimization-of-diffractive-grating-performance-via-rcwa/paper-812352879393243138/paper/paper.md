# Antenna Design Notes

## Reflection Grating Polarizers

EDWARD V. JULL, SENIOR MEMBER, IEEE, AND
JAMES W. HEATH

Abstract—Triangular and rectangular groove surfaces which reflect only transverse electric (TE) polarization while totally backscattering transverse magnetic (TM) polarization are described. The other arrangement, essentially complete TM polarized reflection with simultaneous complete TE polarized backscatter, requires a unique combination of rectangular groove dimensions. Experimental examples at 8.6-mm wavelength are given.

### I. INTRODUCTION

Polarization of an arbitrarily polarized incident electromagnetic wave can be achieved by reflection from a corrugated surface of appropriate profile. With rectangular grooves, for example, the reflected wave may be wholly transverse electric (TE) polarized or transverse magnetic (TM) polarized or eliminated entirely [1]–[4]. In each case the energy not reflected is scattered back in the direction of incidence. Data for the design of these polarizers and experimental examples at 8.6-mm wavelength are given here.

### II. SCATTERING BY A GRATING

An arbitrarily polarized wave incident on a corrugated surface may be resolved into TE (electric field parallel to the grooves) and TM (magnetic field parallel to the grooves) components. For a linear polarizer the unwanted component may be eliminated by total backscatter for incidence normal to the corrugations. This requires a period

$$
d=\frac{\lambda}{2 \sin \theta_{i}} \tag{1}
$$

where $\lambda$ is the wavelength and $\theta_{i}$ is the angle of incidence from the surface normal (see Fig. 1). As scattering occurs in directions $\theta_{n}$ given by

$$
\sin \theta_{n}=\sin \theta_{i}+n \lambda / d, \quad n=0, \pm 1, \cdots \tag{2}
$$

(1) assures that it is only in the directions of specular reflection ($n = 0$) and backscatter ($n = -1$) for $\lambda/2 < d < 3\lambda/2$ ($90^\circ > \theta_{i} > 19.5^\circ$).

Evidently virtually any conducting periodic surface can provide this total backscatter of a single polarization with corrugations of appropriate depth. This depth generally must be determined numerically. The rigorous analytical and numerical procedure used for the rectangular groove examples here has already been given [1], [5] and its validity demonstrated for a wide range of parameters [3], [5]. The requirement of the total simultaneous reflection of one polarization and backscatter of the other restricts the choice of surface profiles; only triangular and rectangular grooves are considered here.

![](./images/812352879393243138_1.jpg)
Fig. 1. Coordinates of a rectangular groove reflection grating.

![](./images/812352879393243138_2.jpg)
Fig. 2. Reduction in TE and TM polarized reflection from a $32.2\ \lambda\times13.1\ \lambda$ brass surface due to 54 right-angled triangular grooves across its width. $d = 0.577\lambda$, $h = 0.250\lambda$, and $\lambda = 8.571$ mm.

### III. TE POLARIZATION

Right-angled triangular grooves of depth

$$
h=\frac{\lambda}{2} \cos \theta_{i} \tag{3}
$$

will completely backscatter the TM polarized component of a wave incident at $\theta_{i}$ and $(\pi/2)-\theta_{i}$, while reflecting most of the TE component incident at one of these angles [6]. This is the simplest design in this situation. An example of experimental results at 8.6-mm wavelength for incidence at $\theta_{i}=60^\circ$ is given in Fig. 2, which shows the effect of 54 right-angled facets on TE and TM polarized reflector from a $32.2\ \lambda\times13.1\ \lambda$ brass surface in an experimental arrangement described elsewhere [7]. The TE component is almost completely reflected for polarizers designed for near-grazing incidence [6].

Rectangular grooves can also be used. Then the simplest arrangement consists of groove widths $a < \lambda/2$, which admit TEM but not TM₁ or TE₁ mode propagation. These surfaces, perfectly blazed to the $n=-1$ order for the TM polarization, will almost

Manuscript received May 30, 1979; revised February 1, 1980.
E. V. Jull is with the Department of Electrical Engineering, University of British Columbia, Vancouver, BC, Canada, and the Electrical Engineering Division of the National Research Council, Ottawa, K1A OR8, Canada.
J. W. Heath was with the University of British Columbia, Vancouver, BC, Canada. He is now with Phillips Cables Ltd., Vancouver, BC, Canada.

0018-926X/80/0700-0586$00.75 © 1980 IEEE

![](./images/812352879393243138_3.jpg)

Fig. 3. Fraction of TE polarized power specularly reflected by con- ducting rectangular grooves of period $d=\lambda /(2 \sin \theta_{i})$.

TABLE I
GROOVE DEPTH $h / \lambda$ FOR TOTAL BACKSCATTER OF TM POLARIZATION FROM RECTANGULAR GROOVES
WITH PERIODS $d=\lambda /(2 \sin \theta_{i})$

<table>
  <thead>
    <tr>
      <th>$a/d \setminus \theta_i$</th>
      <th>$35^\circ$</th>
      <th>$45^\circ$</th>
      <th>$55^\circ$</th>
      <th>$65^\circ$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.00001</td>
      <td>0.250</td>
      <td>0.250</td>
      <td>0.250</td>
      <td>0.250</td>
    </tr>
    <tr>
      <td>0.001</td>
      <td>0.249</td>
      <td>0.249</td>
      <td>0.249</td>
      <td>0.249</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>0.241</td>
      <td>0.243</td>
      <td>0.244</td>
      <td>0.244</td>
    </tr>
    <tr>
      <td>0.05</td>
      <td>0.221</td>
      <td>0.227</td>
      <td>0.230</td>
      <td>0.232</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>0.210</td>
      <td>0.218</td>
      <td>0.223</td>
      <td>0.225</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>0.206</td>
      <td>0.213</td>
      <td>0.214</td>
      <td>0.205</td>
    </tr>
    <tr>
      <td>0.333</td>
      <td></td>
      <td></td>
      <td>0.206</td>
      <td>0.185</td>
    </tr>
  </tbody>
</table>

TE polarized power is at least 99 percent reflected with these groove widths $a$. $\theta_{i}$ is the angle of incidence (see Fig. 1).

totally reflect TE polarization, particularly for narrow grooves and near-grazing incidence, as shown in Fig. 3. With very narrow grooves the depth should be about $\lambda / 4$, but such designs require close dimensional tolerances and have narrow frequency band- widths. Surfaces with wider grooves are more practical. Data for the design of polarizers for $\theta_{i}=35-65^{\circ}$ in which TE polarized power is at least 99 percent reflected are given in Table I. Numerical results for other angles of incidence [5], [8] and an experimental example [5] are illustrated elsewhere.

## IV. TM POLARIZATION

Rectangular grooves may also completely backscatter TE polarization while simultaneously totally reflecting TM polar- ization. Now both components must penetrate the grooves and, in contrast to the TE polarizer, there is no range of parameters capable of providing the desired effect. Fig. 4 shows TE and TM polarized reflected power for unit power incident at $\theta_{i}=45^{\circ}$ on rectangular grooves of period $d=0.707 \lambda$ and groove width $a=$ $0.533 \lambda$. When the groove depth $h=0.96 \lambda$ the conditions are met. These parameters are unique for fulfilling the requirements at this angle of incidence with rectangular grooves of moderate depth.

Fig. 5 shows the effect, measured at $\lambda=8.57 \mathrm{~mm}$, of rectangular grooves of the above dimensions on TE and TM polarized reflected power as the angle of incidence is varied. The $31.3 \lambda \times 13.1 \lambda$ brass surface had 44 rectangular grooves across its width over the entire length, but smaller surfaces, with cor- respondingly fewer grooves, will show essentially the same effect. The measured behavior with frequency of this surface is shown in Fig. 6. In Figs. 5 and 6 TM values above $0 \mathrm{~dB}$ are due to experimental error in the measurement technique, which consisted of removing a flat conducting plate from the corrugated surface and observing the reduction in reflected power [7].

![](./images/812352879393243138_4.jpg)

Fig. 4. Relative TE and TM mode power reflected from rectangular grooves with $a=0.754 d, d=0.707 \lambda$, for incidence at $\theta_{i}=45^{\circ}$. Total TM polarized reflection and TE polarized backscatter occurs for $h=$ $0.96 \lambda$.

![](./images/812352879393243138_5.jpg)

Fig. 5. Reduction of TM and TE polarized specular reflection from a $31.3 \lambda \times 13.1 \lambda$ brass surface by 44 rectangular grooves with $a=0.75 d$, $d=0.707 \lambda, h=0.96 \lambda$; and $\lambda=8.571 \mathrm{~mm}$. TE polarization is essentially totally backscattered over a broad angular range about $\theta_{i}=$ $45^{\circ}$.

## V. CONCLUDING REMARKS

Essentially 100 percent diffraction efficiency can be obtained without difficulty with the proper grating design at centimeter and millimeter wavelengths. At optical and infrared frequencies oxide films and finite conductivity limit the efficiency of practical blazed gratings [2]. The grating size at microwave frequencies presents no difficulty, for it has been shown that grating surfaces blazed to the $n=-1$ order with as few as five corrugations can be 96 percent efficient [9]. The spread of the diffracted beam due to the finite grating size should be no disadvantage in polarizer design. In another numerical investigation high efficiency over a wide frequency band and relative insensitivity to errors in groove dimensions and angle of incidence was shown for a TE polarizer with $a=0.5 d$ and $\theta_{i}=50^{\circ}$ [8]. These examples and the results

![](./images/812352879393243138_6.jpg)

given here show that high efficiency TE polarizers for millimeter waves are easily made with rectangular groove diffraction gratings. Very efficient TM polarizers are also possible, but these will generally have less bandwidth.

## ACKNOWLEDGEMENTS
B. Saunders and P. Dawson obtained the experimental values in Figs. 5 and 6. The assistance of a reviewer, J. Shmoys, in correcting the original paper is gratefully acknowledged.

## REFERENCES
[1] A. Hessel, J. Shmoys, and D.Y. Tseng, "Bragg-angle blazing of diffraction gratings," *J. Opt. Soc. Am.*, vol. 65, pp. 380-384, Apr. 1975.
[2] J.L. Roumiguieres, D. Maystre, and R. Petit, "On the efficiencies of rectangular groove gratings," *J. Opt. Soc. Am.*, vol. 66, pp. 772-775, Aug. 1976.
[3] E.V. Jull, J.W. Heath, and G.R. Ebbeson, "Gratings that diffract all incident energy," *J. Opt. Soc. Am.*, vol. 67, pp. 557-560, Apr. 1977.
[4] J.W. Heath and E.V. Jull, "Total backscatter from conducting rectangular corrugations," *IEEE Trans. Antennas Propagat.*, vol. AP-27, pp. 95-97, Jan. 1979.
[5] ----"Perfectly blazed reflection gratings with rectangular grooves," *J. Opt. Soc. Am.*, vol. 68, pp. 1211-1217, Sept. 1978.
[6] D. Maystre and R. Petit, "Étude quantitative de l'efficacité du réseau échelette dans un montage a déviation constant," *Nouv. Rev. d'Optique appliquée*, vol. 2, pp. 115-120, 1971.
[7] E.V. Jull and G.R. Ebbeson, "The reduction of interference from large reflecting surfaces," *IEEE Trans. Antennas Propagat.*, vol. AP-25, pp. 565-570, July 1977.
[8] J.L. Roumiguieres, "The rectangular-groove grating used as an infrared polarizer," *Optics Comm.*, vol. 19, pp. 76-78, Oct. 1976.
[9] P. Facq, "Application des matrices de Toeplitz à la théorie de la diffraction par les structures cylindriques périodiques limiteés," D.Sc. dissertation, Limoges, 1977.

