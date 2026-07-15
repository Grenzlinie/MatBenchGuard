# CHEMICAL EQUILIBRIA FOR ACCIDENT ANALYSIS IN PRESSURISED WATER NUCLEAR REACTOR SYSTEMS

P. E. Potter and M. H. Rand

Chemistry and Materials Development Divisions, AERE, Harwell, Oxon, OX11 ORA, U.K.

## ABSTRACT
In this paper some chemical equilibria for the safety analysis of water cooled nuclear reactors have been calculated using the programme SOLGASMIX. Particular attention has been paid to the behaviour of the fission product elements Cs, I, Te, Ba and Sr. The chemical states of these elements have been calculated for a variety of conditions likely to be encountered in the core of a reactor before and during degradation.

## 1. Introduction
The purpose of this paper is to describe some of the complex chemical equilibria which can occur in or near the core of a water-cooled nuclear reactor such as a pressurised water reactor (PWR).

When the $^{235}U$ atoms of the enriched urania ($UO_2$) fuel undergo fission, over thirty new fission product elements are formed. A detailed knowledge of the chemical changes which can occur within the fuel as a result of fission is of great importance in the interpretation and prediction of the behaviour of fuel in normal operating and accident conditions. We shall discuss some equilibria of relevance to the operation of PWR fuel rods under normal conditions, and then in conditions appropriate to a loss of coolant accident (LOCA).

If there is complete loss of coolant, the fuel rods could eventually melt, leading to the complete collapse of the core. The core consists of fuel rods - pellets of urania, clad in Zircaloy-4 (ca. 95 wt% Zr, 1.5 wt% Sn, remainder Fe, Cr, Ni). In addition, there are absorber and control rods which are borosilicate, and an Ag-Cd-In alloy, both clad in stainless steel. The structural materials are of steel.

During such a melt-down in the presence of water and steam, the Zircaloy will be oxidised by the exothermic reaction

$$Zr + 2H_2O \rightarrow ZrO_2 + 2H_2$$

which in fact produces the larger part of the heat which leads to melting or degradation of the core. Were the molten core material or debris to melt through the stainless steel pressure vessel, it would react with the concrete of the containment and also with any water which may have accumulated in the lower region of the containment building.

The detailed understanding of the chemical and physical processes which might occur at all stages of reactor operation are essential to the assessment of the quantities of radioactive fission products which could be released from the core into the reactor containment.

During operation, the maximum temperature of the centre of the water reactor fuel is approximately $1200^{\circ}C$. The temperature of the coolant is ca. $300^{\circ}C$. Under normal operating conditions, the fission product elements will be essentially distributed throughout the fluorite lattice of the $UO_2$ There will be very little movement of fission product elements

Received April 21, 1983

in the temperature gradient of the fuel rod, except, perhaps, for the most volatile elements, the rare gases krypton and xenon, iodine, caesium and also tellurium.

The relationship between the quantity of the rare gases in the gap between the fuel and clad and the temperature of the fuel is quite well known[1], and there is also some evidence that caesium and iodine behave rather similarly to the rare gases in their movement within the fuel[2].

For fuels operating below ca. $1300^\circ C$, only a very small proportion of the total amount of the fission product elements produced is found in the small gap between the fuel and the cladding. The fission product concentration is essentially due to a temperature independent process involving the recoil of fission product atoms into the fuel-clad gap. Some estimates of these amounts in this region of a fuel pin have been given [1] and for the operating conditions of the fuel in a modern PWR are less than 1% of the total amount of these volatile elements present in the fuel pin.

In addition to these conditions for normal operation, attention has also been given recently to the quantitative prediction of the release of fission products from fuel under accident conditions. Information is required about the nucleation of the fission product phases as the temperature of the fuel rises, and also about the rate of release of fission products to the fuel-clad gap. As the capacity for heat removal is lost from the reactor core, we then have to consider the release of the fission product elements or compounds into steam on failure of the cladding, and finally the behaviour of the compounds and gaseous species of fission product in mixtures of steam and hydrogen (produced by the Zircaloy-water reaction).

The program SOLGASMIX is ideal for the calculation of the many complex equilibria which have to be considered in making assessments of the likely consequences of accidents in which the reactor core might melt. The examples which we have chosen to illustrate some of the problems of chemical equilibria and the application of the program are:

1.  The chemical constitution of the fuel-clad gap of a rod: $UO_2$ pellets clad in Zircaloy.

2.  The chemical constitution of some fission product elements within fuel at temperatures higher than those of normal operation.

3.  The behaviour of caesium and iodine in mixtures of steam and hydrogen.

and 4. The behaviour of barium and strontium in the debris of a reactor core.

Previous calculations have been carried out on the chemistry of the fuel-clad gap by Besmann and Lindemer [3] using SOLGASMIX and on the species of caesium, iodine and tellurium in the gas phase for accident analysis in CANDU reactors by Garisto [4].

## 2. The individual examples

The thermodynamic data have been taken in the main from the data bank (available on-line in Europe via Euronet-Diane) maintained by the Scientific Group, Thermodata Europe (SGTE) [5]. Additional values were taken from Lindemer et al [6] and from assessments by the authors which will be published in the near future.

### 2.1 The chemical species in the fuel-clad gap

A fuel rod consists of pellets of urania ($UO_2$) in a can fabricated from the alloy Zircaloy-4. The pins are filled with helium at a pressure of ca. 24 atm. at room temperature. We have taken the amount of the volatile fission products, Kr, Xr, Cs, I and Te in the gap, to be 1% of the total fission product element concentration within a fuel rod, in which the burn-up of the fissile atoms is 2.9% of the uranium.

### TABLE I
The likely Chemical Constitution in the Region of the Fuel-Clad Gap of a PWR Fuel Rod

Temperature 1000K
Volume of free space in fuel rod $27.61cm^3$
Pressure of helium and rare gases 84.09 atm
Initial amount of $UO_2$ $7.33mol$
Initial amounts of fission product elements
I $2.35x10^{-5}mol$
Cs $4.11x10^{-4}mol$
Te $6.25x10^{-5}mol$
He + rare gases $2.61x10^{-2}mol$

---

#### Case 1. After equilibration

<table>
  <tr>
    <th colspan="2">Amounts of condensed phases (mol)</th>
    <th colspan="2">Pressures of Predominant Species (atm)</th>
    <th>Oxygen potential $J.mol\ O_2^{-1}$</th>
  </tr>
  <tr>
    <td>$UO_2$</td>
    <td>7.33</td>
    <td>Cs</td>
    <td>$7.1x10^{-1}$</td>
    <td rowspan="4">-905921</td>
  </tr>
  <tr>
    <td>U</td>
    <td>$2.22x10^{-16}$</td>
    <td>$Cs_2$</td>
    <td>$3.5x10^{-2}$</td>
  </tr>
  <tr>
    <td>CsI</td>
    <td>$2.25x10^{-5}$</td>
    <td>CsI</td>
    <td>$2.1x10^{-3}$</td>
  </tr>
  <tr>
    <td>$Cs_2Te$</td>
    <td>$6.24x10^{-5}$</td>
    <td>$Cs_2I_2$</td>
    <td>$3.9x10^{-4}$</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>I</td>
    <td>$1.8x10^{-16}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Te</td>
    <td>$7.6x10^{-12}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>$Te_2$</td>
    <td>$1.1x10^{-14}$</td>
    <td></td>
  </tr>
</table>

#### Case 2. After equilibration with further amount of $O_2$ ($5x10^{-5}mol$)

<table>
  <tr>
    <th colspan="2">Amounts of condensed phases (mol)</th>
    <th colspan="2">Pressures of Predominant Species (atm)</th>
    <th>Oxygen potential $J.mol\ O_2^{-1}$</th>
  </tr>
  <tr>
    <td>$UO_2$</td>
    <td>7.33</td>
    <td>Cs</td>
    <td>$3.8x10^{-1}$</td>
    <td rowspan="4">-581644</td>
  </tr>
  <tr>
    <td>CsI</td>
    <td>$2.25x10^{-5}$</td>
    <td>$Cs_2$</td>
    <td>$1.0x10^{-2}$</td>
  </tr>
  <tr>
    <td>$Cs_2UO_{3.56}$</td>
    <td>$6.41x10^{-5}$</td>
    <td>CsI</td>
    <td>$2.1x100^{-3}$</td>
  </tr>
  <tr>
    <td>$Cs_2Te$</td>
    <td>$6.24x10^{-5}$</td>
    <td>$Cs_2I_2$</td>
    <td>$3.9x10^{-4}$</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>I</td>
    <td>$3.3x10^{-16}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Te</td>
    <td>$2.7x10^{-11}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>$Te_2$</td>
    <td>$1.3x10^{-13}$</td>
    <td></td>
  </tr>
</table>

#### Case 3. After equilibration with a further amount of $O_2$ ($5x10^{-5}mol$)

<table>
  <tr>
    <th colspan="2">Amounts of condensed phases (mol)</th>
    <th colspan="2">Pressures of Predominant Species (atm)</th>
    <th>Oxygen potential $J.mol\ O_2^{-1}$</th>
  </tr>
  <tr>
    <td>$UO_2$</td>
    <td>7.33</td>
    <td>Cs</td>
    <td>$1.1x10^{-1}$</td>
    <td rowspan="5">-556224</td>
  </tr>
  <tr>
    <td>CsI</td>
    <td>$2.25x10^{-5}$</td>
    <td>$Cs_2$</td>
    <td>$9.2x10^{-4}$</td>
  </tr>
  <tr>
    <td>$Cs_2UO_{3.56}$</td>
    <td>$5.22x10^{-5}$</td>
    <td>CsI</td>
    <td>$2.1x10^{-3}$</td>
  </tr>
  <tr>
    <td>$Cs_2UO_4$</td>
    <td>$5.93x10^{-5}$</td>
    <td>$Cs_2I_2$</td>
    <td>$3.9x10^{-4}$</td>
  </tr>
  <tr>
    <td>$Cs_2Te$</td>
    <td>$6.24x10^{-5}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>I</td>
    <td>$1.1x10^{-15}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Te</td>
    <td>$2.9x10^{-10}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>$Te_2$</td>
    <td>$1.6x10^{-11}$</td>
    <td></td>
  </tr>
</table>

#### Case 4. After equilibration with a further amount of $O_2$ ($5x10^{-5}mol$)

<table>
  <tr>
    <th colspan="2">Amounts of condensed phases (mol)</th>
    <th colspan="2">Pressures of Predominant Species (atm)</th>
    <th>Oxygen potential $J.mol\ O_2^{-1}$</th>
  </tr>
  <tr>
    <td>$UO_2$</td>
    <td>7.33</td>
    <td>Cs</td>
    <td>$5.6x10^{-4}$</td>
    <td rowspan="4">-467647</td>
  </tr>
  <tr>
    <td>CsI</td>
    <td>$2.25x10^{-5}$</td>
    <td>$Cs_2$</td>
    <td>$2.2x10^{-8}$</td>
  </tr>
  <tr>
    <td>$Cs_2UO_4$</td>
    <td>$1.50x10^{-4}$</td>
    <td>CsI</td>
    <td>$2.1x10^{-3}$</td>
  </tr>
  <tr>
    <td>$Cs_2Te$</td>
    <td>$4.35x10^{-5}$</td>
    <td>$Cs_2I_2$</td>
    <td>$3.9x10^{-4}$</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>I</td>
    <td>$2.2x10^{-13}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Te</td>
    <td>$1.2x10^{-5}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>$Te_2$</td>
    <td>$2.8x10^{-2}$</td>
    <td></td>
  </tr>
</table>

The conditions and the results of the calculations are shown in Table I. It is assumed firstly in these calculations that the Zircaloy clad takes no part in the reactions in this region of a fuel rod at these temperatures due, for example, to the impermeable coating of ZrO₂ on the inner surface. Some considerations of the effects of the presence of zirconium are however considered at the end of this section.

The calculations shown in Table I indicate the changes in chemical constitution which would occur when the oxygen potential is increased slightly. It is thought that during the process of fission the oxygen potential of the fuel matrix will increase, since the average valency of the fission products is less than four, some of the U⁴⁺ cations being oxidised to U⁵⁺ or U⁶⁺. For case 1 of Table I, we see that formally there is an extremely small amount of elemental uranium present because some of the oxygen of the UO₂ is required for the gas phase after equilibration: in practice, this would manifest itself as hypostoichiometric urania (UO₂₋ₓ). The addition of a small quantity of oxygen (case 2) results in the oxidation of UO₂₋ₓ and the appearance of Cs₂UO₃.₅₆. The other condensed phases, CsI and Cs₂Te remain unchanged in all the four cases considered here. The addition of a further small quantity of oxygen (case 3) results in the appearance of a further condensed phase, Cs₂UO₄; there are now five condensed phases present. The result of a further addition of oxygen (case 4) is to remove Cs₂UO₃.₅₆ leaving the four phases - UO₂, Cs₂UO₄, CsI and Cs₂Te.

The gas phase species which have been considered in these calculations are Cs, Cs₂, CsI, Cs₂I₂, Cs₂O, CsO, I, I₂, Te, Te₂, TeO, TeO₂ and Te₂O₂. The only species with significant pressures are Cs, Cs₂, CsI and Cs₂I₂. Te and Te₂ are the major species of this element but their pressures are very low. It will be noticed that as the oxygen potential increases the pressure of atomic iodine increases, but for these conditions is always insignificant.

After Zircaloy is allowed to react with the elements of the fuel-clad gap then because of the very low iodine pressures those of the four zirconium iodide gaseous species ZrI, ZrI₂, ZrI₃ and ZrI₄ are very low. We have considered two cases, one in which the activities of oxygen and iodine are taken from the conditions given for case 4 in Table I, and those where the iodine activity is the same but the oxygen activity is lower. In the first case, the oxygen is sufficient for the all the zirconium to be oxidised to ZrO₂, whilst in the second case the oxygen potential is that of the two phase system Zr + ZrO₂. The details of these two cases are given in Table II. The low pressures of iodine and of zirconium iodides in the fuel clad gap make any explanation on a basis of equilibrium thermodynamics for the corrosion of Zircaloy by iodine within an operating fuel rod extremely unlikely.

TABLE II
The Reaction of Zirconium with Iodine and Oxygen at 1000K

<table>
  <thead>
    <tr>
      <th colspan="2">Initial Conditions (atm)</th>
      <th>Condensed Phase</th>
      <th colspan="4">Pressures of Zr iodides (atm)</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>ZrI</th>
      <th>ZrI₂</th>
      <th>ZrI₃</th>
      <th>ZrI₄</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I₂</td>
      <td>1.66x10⁻²³</td>
      <td rowspan="2">Zr + ZrO₂</td>
      <td rowspan="2">3.59x10⁻³⁶</td>
      <td rowspan="2">1.03x10⁻¹⁴</td>
      <td rowspan="2">3.38x10⁻¹⁶</td>
      <td rowspan="2">1.15x10⁻²⁶</td>
    </tr>
    <tr>
      <td>O₂</td>
      <td>3.72x10⁻²⁵</td>
    </tr>
    <tr>
      <td>I₂</td>
      <td>1.66x10⁻²³</td>
      <td rowspan="2">ZrO₂</td>
      <td rowspan="2">5.83x10⁻⁵⁹</td>
      <td rowspan="2">1.66x10⁻³⁷</td>
      <td rowspan="2">5.49x10⁻³⁹</td>
      <td rowspan="2">1.87x10⁻⁴⁹</td>
    </tr>
    <tr>
      <td>O₂</td>
      <td>6.03x10⁻⁴⁸</td>
    </tr>
  </tbody>
</table>

### 2.2 Chemical equilibria in the fuel rods at temperatures higher than those of operation

The maximum temperature of the operation of PWR fuel rods is determined by the interaction of urania with Zircaloy. If the fuel touches the cladding, then a uranium-rich liquid could form at temperatures in the range 1300-1500°C [7]. If the cladding were to become imperviously oxidised or if no contact between fuel and cladding took place, then the fuel rod would remain intact up to higher temperatures than that for the urania-Zircaloy reaction.

In this section we shall give an example of the calculation of the constitution of a fuel pin at 1500K, in which the fission products, Cs, I and Te are present, together with Mo. Mo was earlier believed to buffer the oxygen potential of irradiated oxide fuels [7] by the equilibrium reaction

$$Mo + O_2 \rightleftarrows MoO_2$$

The Mo would be a component of the fission product alloy Mo-Tc-Ru-Rh-Pd [8]. The present calculations would demonstrate that in fact the oxygen potential is controlled by the formation of caesium uranates up to temperatures of ca. 1500K. We shall see that at 1600K, using the available data for the Gibbs energies of formation of the caesium uranates [4], these compounds have decomposed and thus can no longer control the rise in oxygen potential during irradiation of the urania fuel.

Table III gives the phases and pressures of the predominant vapour species at the two temperatures, 1500 and 1600K.

It will be noted that for cases 1-2 in Table III the condensed phases are identical to cases 1-2 of Table I, with the additional of elemental molybdenum. Further addition of oxygen (case 3) simply results in the formation of more $Cs_2UO_{3.56}$. The oxygen potential is unchanged for cases 2 and 3.

At 1600K, for case 4, the requirements for oxygen in the gas phase result in the formation of $UO_{2-x}$. On further addition of oxygen (case 5) uranium is no longer present and hyperstoichiometric urania is formed. In these calculations, for convenience, we have expressed the single phase urania as a mixture of $UO_{2.00}$ and $UO_{2.05}$; this will make negligible difference to the calculated values. It will be noted that at this temperature $Cs_2UO_{3.56}$ is no longer present in this system.

Although we give only the pressure of the predominant gas phase species, we have also considered the following gases in our calculations: $Cs_2O$, $CsO$, $TeO$, $TeO_2$ and $Te_2O_2$.

### 2.3 Failed fuel

#### 2.3.1 The behaviour of caesium, iodine and tellurium in mixtures of steam and hydrogen

The conditions of temperature and pressure at a given moment in a degraded reactor core depend on the type of failure, for example, on whether there is a rapid depressurisation of the primary coolant circuit, due to a large breach of the circuit (in which case the total pressure in the system would rapidly fall to a value of a few atmospheres) or whether the depressurisation is slow because of a small leak. We have selected total pressures of 3atm and 70atm as being typical values for these two conditions of failure.

We shall first examine the behaviour of the fission products which would be released on failure of a fuel rod, and secondly we examine the behaviour of Cs and I in steam-hydrogen mixtures.

Let us then first consider a pin containing the same fission product concentration as given in Table III; on failure of the cladding we shall assume that all of these fission products react with the gaseous atmosphere of hydrogen and steam. We have carried out the calculation at 1500K, for the two total pressures, and different hydrogen:water ratios.

Elemental iodine, HI and $H_2Te$ would not condense so readily as CsI and the gaseous Te species (Te, $Te_2$, $TeOH$, $Te(OH)_2$, $TeO$, $TeO_2$ and $Te_2O_2$). These volatile species would most probably behave differently within the reactor system during an accident and therefore it is important that their amount be known. Most of the Cs will be in the form of CsOH. The details of the proportions of the gaseous species for these conditions are given in Table IV.

<table>
<caption>TABLE III<br>The Chemical Constitution of some Fission Product Elements in Urania Fuel</caption>
<tbody>
<tr>
<td colspan="2">Temperature 1500K</td>
<td colspan="2">Volume 27.61cm³</td>
<td colspan="2">Pressure 157.8atm</td>
</tr>
<tr>
<td colspan="3">Initial composition (mol): UO₂ 7.33</td>
<td colspan="3">He + rare gases 2.90x10⁻²</td>
</tr>
<tr>
<td colspan="3">Cs 4.11x10⁻²</td>
<td colspan="3">Te 6.24x10⁻³</td>
</tr>
<tr>
<td colspan="3">I 2.35x10⁻³</td>
<td colspan="3">Mo 5.00x10⁻²</td>
</tr>
<tr>
<td colspan="6">1. After equilibration</td>
</tr>
<tr>
<td colspan="2">Condensed phases<br>(mol)</td>
<td colspan="3">Pressures of predominant<br>species (atm)</td>
<td>Oxygen potential<br>J.mol O₂⁻¹</td>
</tr>
<tr>
<td>UO₂</td>
<td>7.33</td>
<td>Cs</td>
<td>19.59</td>
<td>He + rare</td>
<td>-544618</td>
</tr>
<tr>
<td>U</td>
<td>2.22x10⁻¹⁶</td>
<td>Cs₂</td>
<td>8.36</td>
<td>gases 129.4</td>
<td>
</td>
</tr>
<tr>
<td>Mo</td>
<td>5.00x10⁻²</td>
<td>CsI</td>
<td>4.32x10⁻¹</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Cs</td>
<td>1.81x10⁻²</td>
<td>Cs₂I₂</td>
<td>4.54x10⁻²</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>CsI</td>
<td>2.23x10⁻³</td>
<td>Te</td>
<td>7.68x10⁻⁴</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂Te</td>
<td>6.24x10⁻³</td>
<td>Te₂</td>
<td>2.67x10⁻³</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>I</td>
<td>1.03x10⁻⁹</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>I₂</td>
<td>7.85x10⁻⁹</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="6">2. After equilibration with further amount of oxygen ($5x10^{-5}$mol O₂)</td>
</tr>
<tr>
<td>UO₂</td>
<td>7.33</td>
<td colspan="3" rowspan="6">Pressures identical to those<br>for case 1</td>
<td>-330154</td>
</tr>
<tr>
<td>Mo</td>
<td>5.00x10⁻²</td>
<td>
</td>
</tr>
<tr>
<td>Cs</td>
<td>1.80x10⁻²</td>
<td>
</td>
</tr>
<tr>
<td>CsI</td>
<td>2.23x10⁻⁶</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂UO₃.₅₆</td>
<td>6.40x10⁻⁶</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂Te</td>
<td>6.24x10⁻³</td>
<td>
</td>
</tr>
<tr>
<td colspan="6">3. After equilibration with further amount of oxygen ($5x10^{-5}$mol O₂)</td>
</tr>
<tr>
<td>UO₂</td>
<td>7.33</td>
<td colspan="3" rowspan="6">Pressures identical to those<br>for cases 1 and 2</td>
<td>-330154</td>
</tr>
<tr>
<td>Mo</td>
<td>5.00x10⁻²</td>
<td>
</td>
</tr>
<tr>
<td>Cs</td>
<td>1.80x10⁻³</td>
<td>
</td>
</tr>
<tr>
<td>CsI</td>
<td>2.23x10⁻³</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂UO₃.₅₆</td>
<td>5.79x10⁻⁵</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂Te</td>
<td>6.24x10⁻³</td>
<td>
</td>
</tr>
<tr>
<td colspan="6">Temperature 1600K. Pressure 179.5 atm<br>Same initial concentrations as for cases 1, 2, 3 at 1500K</td>
</tr>
<tr>
<td colspan="6">4. After equilibration</td>
</tr>
<tr>
<td>UO₂</td>
<td>7.33</td>
<td>Cs</td>
<td>26.86</td>
<td>
</td>
<td>-499344</td>
</tr>
<tr>
<td>U</td>
<td>2.22x10⁻¹⁶</td>
<td>Cs₂</td>
<td>13.59</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Mo</td>
<td>5.00x10⁻²</td>
<td>CsI</td>
<td>8.41x10⁻¹</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Cs</td>
<td>1.50x10⁻²</td>
<td>Cs₂I₂</td>
<td>8.22x10⁻²</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>CsI</td>
<td>2.13x10⁻³</td>
<td>Te</td>
<td>9.37x10⁻³</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂Te</td>
<td>6.20x10⁻³</td>
<td>Te₂</td>
<td>1.05x10⁻¹</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>I</td>
<td>7.96x10⁻⁹</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>I₂</td>
<td>2.19x10⁻¹⁷</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="6">5. After equilibration with further amount of oxygen ($5x10^{-5}$mol O₂)</td>
</tr>
<tr>
<td>UO₂</td>
<td>7.32</td>
<td colspan="3" rowspan="6">Pressures identical to<br>those of case 4</td>
<td>-304374</td>
</tr>
<tr>
<td>UO₂.₀₅</td>
<td>2.00x10⁻⁴</td>
<td>
</td>
</tr>
<tr>
<td>Mo</td>
<td>5.00x10⁻²</td>
<td>
</td>
</tr>
<tr>
<td>Cs</td>
<td>1.50x10⁻³</td>
<td>
</td>
</tr>
<tr>
<td>CsI</td>
<td>2.13x10⁻³</td>
<td>
</td>
</tr>
<tr>
<td>Cs₂Te</td>
<td>6.20x10⁻³</td>
<td>
</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE IV
The Chemical Species of the Fission Products Cs, I and Te
after Release from a Fuel Pin at 1500K</caption>
<thead>
<tr>
<th rowspan="2">Pressure
(atm)</th>
<th colspan="5">Relative amounts of species</th>
</tr>
<tr>
<th>$\frac{H_2}{H_2O}$</th>
<th>$\frac{I}{CsI}$</th>
<th>$\frac{HI}{CsI}$</th>
<th>$\frac{H_2Te}{\text{other Te species}}$</th>
<th>$\frac{CsOH}{CsI}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>2.4</td>
<td>$5.36x10^{-5}$</td>
<td>$2.74x10^{-4}$</td>
<td>$5.20x10^{-2}$</td>
<td>15.2</td>
</tr>
<tr>
<td></td>
<td>33.6</td>
<td>$8.27x10^{-6}$</td>
<td>$4.96x10^{-5}$</td>
<td>$1.24x10^{-1}$</td>
<td>8.3</td>
</tr>
<tr>
<td>70</td>
<td>1</td>
<td>$2.26x10^{-4}$</td>
<td>$4.74x10^{-3}$</td>
<td>$1.64x10^{-2}$</td>
<td>10.0</td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>$4.33x10^{-5}$</td>
<td>$1.15x10^{-3}$</td>
<td>$2.55x10^{-1}$</td>
<td>16.1</td>
</tr>
</tbody>
</table>

In all conditions in these calculations the contributions to the gas from elemental I and HI are very small. The contribution of $H_2Te$ compared with those of the other Te species can be significant under the more reducing conditions. The remaining condensed phases are hyperstoichiometric urania and elemental molybdenum.

We shall now examine the behaviour of caesium and iodine in steam-hydrogen mixtures, again at the previously chosen pressures of 3 and 70 atm but at higher temperatures, 1750, 2000 and 2250K. The hydrogen:steam ratios (14:1, 2:1 for the large break accident, 4:1 and 1:1 for the small break) and the $(Cs,I)/(H_2+H_2O)$ ratios are taken to span the corresponding ratios obtained from preliminary thermo-hydraulic modelling calculations of failed core. We shall again be concerned with the amounts of elemental iodine and HI compared with that of CsI. The results of the calculations of the relative amounts of these species are given in Table V.

<table>
<caption>TABLE V
The Behaviour of Cs and I in Mixtures of Steam and Hydrogen
at Temperatures 1750-2250K</caption>
<thead>
<tr>
<th rowspan="2">Total
Pressure
(atm)</th>
<th rowspan="2">Temp.
(K)</th>
<th colspan="2">Initial Amount</th>
<th colspan="4">Proportions of gaseous species</th>
</tr>
<tr>
<td>$H_2$</td>
<td>$H_2O$</td>
<td>$\frac{I}{CsI}$</td>
<td>$\frac{HI}{CsI}$</td>
<td>$\frac{CsOH}{CsI}$</td>
<td>$\frac{Cs}{CsI}$</td>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>1750</td>
<td>140</td>
<td>10</td>
<td>$3.64x10^{-4}$</td>
<td>$8.32x10^{-4}$</td>
<td>8.75</td>
<td>7.77</td>
</tr>
<tr>
<td></td>
<td></td>
<td>100</td>
<td>50</td>
<td>$1.34x10^{-3}$</td>
<td>$2.59x10^{-3}$</td>
<td>14.45</td>
<td>2.11</td>
</tr>
<tr>
<td></td>
<td>2000</td>
<td>140</td>
<td>10</td>
<td>$4.87x10^{-3}$</td>
<td>$5.45x10^{-3}$</td>
<td>5.92</td>
<td>10.76</td>
</tr>
<tr>
<td></td>
<td></td>
<td>100</td>
<td>50</td>
<td>$1.35x10^{-2}$</td>
<td>$1.28x10^{-2}$</td>
<td>13.02</td>
<td>3.94</td>
</tr>
<tr>
<td></td>
<td>2250</td>
<td>140</td>
<td>10</td>
<td>$3.96x10^{-2}$</td>
<td>$2.54x10^{-2}$</td>
<td>4.22</td>
<td>13.41</td>
</tr>
<tr>
<td></td>
<td></td>
<td>100</td>
<td>50</td>
<td>$8.61x10^{-2}$</td>
<td>$4.68x10^{-2}$</td>
<td>12.23</td>
<td>6.55</td>
</tr>
<tr>
<td>70</td>
<td>1750</td>
<td>800</td>
<td>200</td>
<td>$9.38x10^{-4}$</td>
<td>$9.60x10^{-3}$</td>
<td>15.82</td>
<td>0.87</td>
</tr>
<tr>
<td></td>
<td></td>
<td>500</td>
<td>500</td>
<td>$2.86x10^{-3}$</td>
<td>$2.32x10^{-2}$</td>
<td>16.66</td>
<td>0.29</td>
</tr>
<tr>
<td></td>
<td>2000</td>
<td>800</td>
<td>200</td>
<td>$8.75x10^{-3}$</td>
<td>$4.38x10^{-2}$</td>
<td>15.65</td>
<td>1.77</td>
</tr>
<tr>
<td></td>
<td></td>
<td>500</td>
<td>500</td>
<td>$2.57x10^{-2}$</td>
<td>0.10</td>
<td>18.08</td>
<td>0.65</td>
</tr>
<tr>
<td></td>
<td>2250</td>
<td>800</td>
<td>200</td>
<td>$5.11x10^{-2}$</td>
<td>0.15</td>
<td>16.64</td>
<td>3.32</td>
</tr>
<tr>
<td></td>
<td></td>
<td>500</td>
<td>500</td>
<td>0.14</td>
<td>0.32</td>
<td>23.18</td>
<td>1.46</td>
</tr>
</tbody>
</table>

The initial amounts of Cs and I are 0.7 and 0.04 mol respectively.

The calculations show that only for the higher pressure of 70 atm does the amount of HI become appreciable (ca. 10% of CsI) at 2000K and that of elemental iodine (ca. 5% of CsI) at 2250K. It will be noted that for the lower pressure of 3 atm, the amount of elemental Cs can be greater than that of CsOH. The formation of I(g) at high temperatures arises from the dissociation and hydrolysis reactions:

$$\mathrm{CsI(g) \rightarrow Cs(g) + I(g)}$$

$$\mathrm{CsI(g) + H_2O(g) \rightarrow CsOH(g) + HI(g)}$$

$$\mathrm{CsI(g) + H_2O(g) \rightarrow CsOH(g) + I(g) + \frac{1}{2}H_2(g)}$$

It is clear from considerations of the law of mass action that, as found from the SOLGASMIX results, the factors which increase the I/CsI ratio are:
- increase in temperature
- decrease in pressure
- decrease in $(Cs,I)/(H_2O+H_2)$
- increase in $H_2O/H_2$ ratio

These results, however, show that for realistic conditions in the pressure vessel during a core melt, virtually all of the iodine will remain as CsI(g) or HI(g). As the mass of steam, hydrogen and fission product cools, any free I(g) formed above 2000K will of course recombine to form CsI (as in Table III).

### 2.3.2 The behaviour of barium and strontium in the debris of a reactor core

The volatile fission products Cs, I and Te considered so far are removed from the fuel by the time the core has melted. Other fission products remain dissolved in the $(UO_2,ZrO_2)$ oxide or the (Zircaloy-steel) melts. In particular, the barium and strontium (which have appreciable fission yields) are likely to dissolve in the $UO_2$ matrix, either as oxides or as zirconates. (Zr is also a fission product $(Zr/(Ba+Sr) \approx 2)$ so that the barium and strontium will be in intimate contact with zirconium during operation and heating up of the core). Although some vaporisation may occur during the period when the core slumps down to the bottom of the pressure vessel, we have studied the release of Ba and Sr for the later period when the molten core has melted through the pressure vessel and is vaporising water, present in the containment (including that bound in the concrete structure).

We have therefore calculated the vaporisation of barium and strontium as oxides and hydroxides in realistic flows of hydrogen/steam mixtures, at 2250K. The results are shown in Table VI. Two cases are presented, one where no zirconate formation is assumed, and one with such formation. In both cases, similar compounds of Ba and Sr are assumed to form ideal solid or liquid solutions.

As expected the predominant species are the dihydroxide gases, although in keeping with the much higher stability of BaO(g) compared to the other alkaline earth monoxide gases, this species comprises about 5% of the barium vapour species. Barium species are rather more volatile than strontium species, so that in cases 3 and 4, where there is a high $H_2O/(Ba+Sr)$ ratio, the condensed phase is considerably depleted in barium. The pressures of fission products are not negligible, even in the more probable cases where zirconates are formed.

Vaporisation of Ba and Sr from oxide melts

Temperature 2250K. Pressure 3 atm.
Initial compositions Ba 7.35 mol, Sr 8.11 mol.

| Case | $\boldsymbol{H_2O}$ (mol) | $\boldsymbol{H_2}$ |
|------|---------------------------|--------------------|
| 1    | 100                       | 10                 |
| 2    | 100                       | 100                |
| 3    | 1000                      | 100                |
| 4    | 1000                      | 1000               |

### a. Without (Ba,Sr)ZrO₃

Condensed phases: $\ce{Ba_{x}Sr_{1-x}O(s) + ZrO_{2}(s)}$

<table>
  <thead>
    <tr>
      <th>Case</th>
      <th>$\boldsymbol{\frac{Ba}{(Ba+Sr)}}$</th>
      <th colspan="7">Pressures (atm)</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>$\boldsymbol{Ba(OH)_2}$</th>
      <th>$\boldsymbol{BaOH}$</th>
      <th>$\boldsymbol{BaO}$</th>
      <th>$\boldsymbol{Sr(OH)_2}$</th>
      <th>$\boldsymbol{SrOH}$</th>
      <th>$\boldsymbol{Sr}$</th>
      <th>$\boldsymbol{H_2O}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0.43</td>
      <td>$3.3x10^{-2}$</td>
      <td>$2.3x10^{-3}$</td>
      <td>$1.9x10^{-3}$</td>
      <td>$2.0x10^{-3}$</td>
      <td>$3.8x10^{-5}$</td>
      <td>$2.3x10^{-5}$</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.42</td>
      <td>$1.8x10^{-2}$</td>
      <td>$2.6x10^{-3}$</td>
      <td>$1.9x10^{-3}$</td>
      <td>$1.1x10^{-3}$</td>
      <td>$4.3x10^{-4}$</td>
      <td>$5.6x10^{-5}$</td>
      <td>0.65</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>0.10</td>
      <td>$1.8x10^{-2}$</td>
      <td>$2.7x10^{-4}$</td>
      <td>$4.6x10^{-4}$</td>
      <td>$6.9x10^{-3}$</td>
      <td>$2.9x10^{-6}$</td>
      <td>$4.0x10^{-6}$</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.10</td>
      <td>$9.2x10^{-3}$</td>
      <td>$5.0x10^{-4}$</td>
      <td>$4.4x10^{-4}$</td>
      <td>$3.8x10^{-3}$</td>
      <td>$5.6x10^{-4}$</td>
      <td>$2.7x10^{-5}$</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>

### b. With zirconates

Condensed phases: $\ce{(Ba_{x}Sr_{1-x})ZrO_{3} + ZrO_{2}}$

<table>
  <thead>
    <tr>
      <th>Case</th>
      <th>$\boldsymbol{\frac{Ba}{(Ba+Sr)}}$</th>
      <th colspan="7">Pressures (atm)</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>$\boldsymbol{Ba(OH)_2}$</th>
      <th>$\boldsymbol{BaOH}$</th>
      <th>$\boldsymbol{BaO}$</th>
      <th>$\boldsymbol{Sr(OH)_2}$</th>
      <th>$\boldsymbol{SrOH}$</th>
      <th>$\boldsymbol{Sr}$</th>
      <th>$\boldsymbol{H_2O}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0.48</td>
      <td>$2.0x10^{-4}$</td>
      <td>$1.3x10^{-5}$</td>
      <td>$1.1x10^{-5}$</td>
      <td>$1.4x10^{-5}$</td>
      <td>$2.5x10^{-6}$</td>
      <td>$1.5x10^{-7}$</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.48</td>
      <td>$1.1x10^{-4}$</td>
      <td>$1.5x10^{-5}$</td>
      <td>$1.1x10^{-5}$</td>
      <td>$7.6x10^{-6}$</td>
      <td>$2.8x10^{-6}$</td>
      <td>$3.5x10^{-7}$</td>
      <td>0.67</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.47</td>
      <td>$4.2x10^{-4}$</td>
      <td>$6.4x10^{-6}$</td>
      <td>$1.1x10^{-5}$</td>
      <td>$2.9x10^{-5}$</td>
      <td>$1.2x10^{-6}$</td>
      <td>$1.7x10^{-8}$</td>
      <td>2.6</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.47</td>
      <td>$2.3x10^{-4}$</td>
      <td>$1.2x10^{-5}$</td>
      <td>$1.1x10^{-5}$</td>
      <td>$1.6x10^{-5}$</td>
      <td>$2.3x10^{-6}$</td>
      <td>$1.1x10^{-7}$</td>
      <td>1.4</td>
    </tr>
  </tbody>
</table>

## 3. Conclusions

This paper describes some of our preliminary attempts to examine the complex chemical changes which could occur during an accident due to loss of coolant in a PWR type nuclear reactor. It is our intention to develop a collection of critically assessed thermodynamic data of all the condensed phases and gaseous species likely to be encountered at all stages of an accident.

We have shown aspects of the behaviour of Cs, I, Te, Ba and Sr, all of which have potentially hazardous radionuclides. It is clear that the conditions of temperature, pressure and oxygen potential must be well defined so that the predominant chemical species can be determined for a particular accident sequence.

We are most grateful to Dr. Gunnar Eriksson for his generous provision of the program SOLGASMIX, and for many stimulating discussions.

REFERENCES:

[1] J.H.Gittus. PWR degraded core analysis. UKAEA Report ND-R610(S) 1982. Chapter VII p.461

[2] R.A.Lorenz, J.L.Collins, A.P.Malinauskas, O.L.Kirkland, R.L.Towns. Report NUREG-CR-0722 (1980)

[3] T.M.Besmann, T.B.Lindemer. Report ORNL/TM-6130 (1978)

[4] P.Garisto. Report AECL-7782 (1982)

[5] T.I.Barry. "Contributions of European Thermochemical Data Banks". 22nd CEFA, Rapports Techniques CEBELCOR 142 1982 137

[6] T.B.Lindemer, T.M.Besmann, C.E.Johnson. J.Nucl.Mats. 100 (1981) 178

[7] P.Hofmann, C.Politis. J.Nucl.Mats. 87(1979) 375

[8] P.E.Potter. Behaviour and Chemical State of Irradiated Ceramic Fuels. IAEA Vienna (1974) p.115