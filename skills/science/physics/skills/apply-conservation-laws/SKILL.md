---
name: apply-conservation-laws
description: Use when solving mechanics, fluid dynamics, or electromagnetism problems by applying conservation of energy, momentum, angular momentum, or charge — identifying the system boundary, the conserved quantity, and the conditions under which conservation applies.
source: Halliday, Resnick & Krane "Physics" 5th ed. (2002); Griffiths "Introduction to Electrodynamics" 4th ed. (2013); Goldstein "Classical Mechanics" 3rd ed. (2002)
tags: [conservation-laws, mechanics, energy-conservation, momentum, angular-momentum, physics, dynamics]
---

# Apply Conservation Laws

Solve physics problems systematically using conservation laws — identifying the conserved quantity, defining the system boundary, confirming conservation conditions are met, and applying the conservation equation to find unknowns.

## Why This Is Best Practice

**Why best:** Conservation laws convert dynamics problems into algebra by exploiting an underlying symmetry, avoiding error-prone force-by-force integration of the equations of motion.
**Adopted by:** Noether's theorem (1915) established that every symmetry of a physical system corresponds to a conserved quantity — the mathematical foundation of all conservation laws. Conservation laws are the foundation of classical mechanics (Newton-Euler equations), quantum mechanics (commuting observables), special relativity (four-momentum conservation), and particle physics (Standard Model).
**Impact:** Conservation laws reduce multi-variable dynamics problems to algebraic equations — solving what would otherwise require complex differential equations. Goldstein (2002) demonstrates that the Lagrangian/Hamiltonian formalism unifies conservation law application across all classical physics. In engineering, conservation of momentum is the basis for rocket propulsion analysis, jet engine thrust calculation, and hydraulic force calculations — domains where Newton's laws applied directly become intractable.

## Steps

### 1. Choose the relevant conservation law

Match the conservation law to the problem type:
| Conservation law | Applies when | Symmetry |
|-----------------|-------------|---------|
| Energy | No non-conservative forces (friction, drag) OR account for heat/work | Time translation invariance |
| Linear momentum | No net external force on system | Translational invariance |
| Angular momentum | No net external torque on system | Rotational invariance |
| Charge (Kirchhoff's current law) | Always (charge is always conserved) | Gauge invariance |
| Mass (continuity equation) | Non-relativistic fluid flow | — |
| Baryon number / lepton number | Nuclear/particle physics | — |

### 2. Define the system boundary precisely

The conservation law applies to the entire system, not to any part of it:
- **Conservation of momentum:** the system must include all objects experiencing internal forces; external forces (gravity, table contact) are accounted for separately
- **Conservation of energy:** the system must include all forms of energy (kinetic, potential, thermal, chemical)

Mistakes almost always trace to an incorrectly defined system.

### 3. Apply conservation of energy

**Mechanical energy conservation (no friction):**
```
KE₁ + PE₁ = KE₂ + PE₂
½mv₁² + mgh₁ = ½mv₂² + mgh₂
```

**Work-energy theorem (with non-conservative forces):**
```
ΔKE = W_net = W_conservative + W_non-conservative
KE₂ − KE₁ = −ΔPE + W_friction
```

**Energy conservation with heat (first law of thermodynamics):**
```
ΔU = Q − W
```
Where ΔU = internal energy change, Q = heat added to system, W = work done BY system.

**Relativistic energy:**
```
E² = (pc)² + (mc²)²
E = γmc²  (total energy, including rest mass)
KE = (γ−1)mc²
```

### 4. Apply conservation of linear momentum

**Isolated system (no external net force):**
```
Σp_before = Σp_after
m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f
```

**Collisions — combine with energy to classify:**
- **Elastic:** both KE and momentum conserved (billiard balls, atomic collisions)
- **Inelastic:** momentum conserved, KE not (most real collisions)
- **Perfectly inelastic:** objects stick together; maximum KE loss consistent with momentum conservation

For elastic 1D collision:
```
v₁f = (m₁−m₂)v₁ᵢ / (m₁+m₂) + 2m₂v₂ᵢ / (m₁+m₂)
v₂f = 2m₁v₁ᵢ / (m₁+m₂) + (m₂−m₁)v₂ᵢ / (m₁+m₂)
```

**Impulse-momentum theorem:**
```
J = FΔt = Δp
```
For variable force: J = ∫F dt = Δp.

### 5. Apply conservation of angular momentum

**Isolated system (no external net torque):**
```
L_before = L_after
Iω_before = Iω_after  (for rigid body about fixed axis)
```

**With changing moment of inertia (figure skater effect):**
When I decreases (arms pulled in), ω increases: Iᵢωᵢ = Ifωf.

**Angular momentum of particle about point O:**
```
L = r × p = mvr·sin(θ)
```
Where θ = angle between r and v.

**Kepler's second law** is conservation of angular momentum: as a planet sweeps equal areas in equal times, r×v = constant.

### 6. Verify with dimensional analysis and limiting cases

After applying conservation law:
1. Check units: both sides of the equation must have identical units
2. Test limiting cases: if m₁ >> m₂ in a collision, m₁ should be nearly unaffected — verify
3. Check sign conventions: momentum vectors have direction; energy is scalar (always positive)
4. Sanity check: final KE should never exceed initial KE for an inelastic collision (energy is not created)

## Common Mistakes

- **Including external forces in "isolated system" and still applying momentum conservation:** If there is a net external force (gravity on a falling object, friction from a table), linear momentum is NOT conserved — apply the impulse-momentum theorem instead.
- **Forgetting rotational KE in spinning systems:** Total KE = ½mv² + ½Iω². Forgetting the rotational term in a rolling-without-slipping problem gives wrong energy budgets.
- **Using conservation of mechanical energy when friction is present:** Friction converts mechanical energy to heat — mechanical energy is not conserved. Either include the heat term or use work-energy theorem with friction force.

## When NOT to Use

- Chaotic systems where small perturbations grow exponentially: conservation laws still hold but cannot predict long-term trajectories (e.g., three-body gravitational problem, turbulent flow).