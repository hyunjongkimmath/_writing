# AlgebraicNumberTheory Content Checklist

> **Generated:** 2026-07-22  
> **Purpose:** Track what discussions are **genuinely missing** (no vault files exist) vs. what is **waiting to be input** into `content.tex` (vault files exist but not yet included).

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Already in `content.tex` (fully integrated) |
| ⏳ **Waiting to input** | Vault files exist in `_definitions/` or `_concepts/` but **NOT** in `content.tex` |
| ❌ **Genuinely missing** | No vault files exist; need to create new definitions/theorems |
| 📝 **Needs expansion** | In `content.tex` but incomplete (TODOs, partial statements) |

---

## Current `content.tex` Structure

```
1. Dedekind domains
2. Local and global fields
   2.1 Local fields
   2.2 Global fields
   2.3 Rings of integers of local and global fields
   2.4 Local fields as completions of global fields at places
   2.5 Ramification and inertia of extensions of local and global fields
       2.5.1 Valuations at points of schemes
       2.5.2 Decomposition groups and inertia groups
   2.6 Prime decomposition in extensions of Dedekind domains
3. Adèles and idèles of global fields
4. Chebotarev density theorem
Appendix A. Galois theory
Appendix B. Absolute values and valuations on fields
Appendix C. Miscellaneous definitions
```

---

## Section-by-Section Checklist

### 1. Dedekind domains

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Noetherian ring | ✅ | `definition_noetherian_ring.tex` | |
| Discrete valuation ring | ✅ | `definition_discrete_valuation_ring.tex` | |
| DVR ↔ discretely valued field | ✅ | `theorem_correspondence_between_dvrs_and_discretely_valued_fields.tex` | |
| Integral element over a ring | ✅ | `definition_integral_element_over_a_ring.tex` | |
| Dedekind domain | ✅ | `definition_dedekind_domain.tex` | |
| DVRs are Dedekind domains | ✅ | `proposition_dvrs_are_dedekind_domains.tex` | |
| Dedekind domain = PID ⇔ UFD | ✅ | `proposition_dedekind_domain_is_a_pid_if_and_only_if_ufd.tex` | |

**Missing from this section (genuinely missing):**
- ❌ **Ideal class group of a Dedekind domain** — vault file EXISTS but not in content.tex → see **Section 2.3** below
- ❌ **Fractional ideals** — vault files exist but not in content.tex → see **Section 2.3** below
- ❌ **Finiteness of the class group** — no vault file exists
- ❌ **Dirichlet's unit theorem** — no vault file exists

---

### 2.1 Local fields

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Local field | ✅ | `definition_local_field.tex` | |
| Convention: metric from absolute value | ✅ | (inline in content.tex) | |
| Local fields are complete | ✅ | `theorem_local_fields_are_complete.tex` | |
| Classification of local fields | ✅ | `theorem_classification_of_local_fields.tex` | |

**Genuinely missing from this section:**
- ❌ **Structure of complete DVRs** (Cohen structure theorem, etc.)
- ❌ **Ramification groups for local fields** (higher ramification)
- ❌ **Local class field theory** (Artin reciprocity for local fields)

---

### 2.2 Global fields

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Number field | ✅ | `definition_number_field.tex` | |
| Global function field | ✅ | `definition_global_function_field.tex` | |
| Global field | ✅ | `definition_global_field.tex` | |
| Equivalent absolute values | ✅ | `definition_equivalent_absolute_values_on_a_field.tex` | |
| Place of a field | ✅ | `definition_place_of_a_field.tex` | |
| Equivalent places | ✅ | `definition_equivalent_places_of_a_field.tex` | |
| Place of a global field | ✅ | `definition_place_of_a_global_field.tex` | |
| ~~Places as equivalence classes of absolute values~~ | 📝 | Commented out in content.tex | `theorem_places_of_a_global_field_are_equivalences_classes_of_nontrivial_absolute_values.tex` exists? |
| Completion at a place | ✅ | `definition_completion_of_a_global_field_at_a_place.tex` | |

**Genuinely missing from this section:**
- ❌ **Product formula** (for number fields and function fields)
- ❌ **Finiteness of class number** (for global fields)
- ❌ **Dirichlet's unit theorem** (for global fields)
- ❌ **Artin-Whaples approximation theorem**

---

### 2.3 Rings of integers of local and global fields

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Ring of integers (extension of fraction field) | ✅ | `definition_ring_of_integers_of_an_extension_of_fraction_field_of_a_dedekind_domain.tex` | |
| Ring of integers (global/local) | ✅ | `definition_ring_of_integers_of_a_global_or_local_ring.tex` | |
| Rings of integers are Dedekind | ✅ | `theorem_rings_of_integers_of_global_fields_or_nonarchimedean_local_fields_are_dedekind_domains.tex` | |

**⏳ Waiting to input (vault files exist):**
| Topic | Vault File | Suggested Location |
|-------|------------|-------------------|
| **Discriminant of a number field** | `definition_discriminant_of_a_number_field.tex` | Here or new subsection |
| **Ideal class group of a Dedekind domain** | `definition_ideal_class_group_of_a_dedekind_domain.tex` | New subsection "Ideal class group" |
| **Fractional ideal of an integral domain** | `definition_fractional_ideal_of_an_integral_domain.tex` | Prerequisite for class group |
| **Principal fractional ideal** | `definition_principal_fractional_ideal_of_an_integral_domain.tex` | Prerequisite for class group |
| **Dedekind zeta function** | `definition_dedekind_zeta_function_of_a_number_field.tex` | New subsection "Zeta functions" |

**❌ Genuinely missing (no vault files):**
- ❌ **Different / discriminant of an extension**
- ❌ **Integral basis / existence of integral basis**
- ❌ **Relative discriminant**
- ❌ **Conductor-discriminant formula**
- ❌ **Finiteness of the class group** (Minkowski's theorem)
- ❌ **Minkowski bound**
- ❌ **Dirichlet's unit theorem** (structure of unit group)
- ❌ **Regulator of a number field**
- ❌ **Class number formula** (analytic class number formula)

---

### 2.4 Local fields as completions of global fields at places

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Completion of global field at place = local field | ✅ | `theorem_completion_of_a_global_field_at_a_place_is_a_local_field.tex` | |
| Remark: all local fields arise this way | ✅ | (inline remark) | |
| Absolute norm of an ideal | ✅ | `definition_absolute_norm_of_an_ideal_of_the_ring_of_integers_of_a_global_or_local_field.tex` | |
| p-adic valuation/absolute value on number field | ✅ | `definition_p_adic_valuation_and_absolute_value_on_a_number_field.tex` | |
| Classification of places of global fields | ✅ | `theorem_classification_of_places_of_global_fields.tex` | |

**Genuinely missing from this section:**
- ❌ **Local degrees** ($n_v = [K_v : \mathbb{Q}_p]$ or $[K_v : \mathbb{F}_p((t))]$)
- ❌ **Local norm maps** ($N_{L_w/K_v}$)
- ❌ **Global-local principle for norms** (Hasse norm theorem)

---

### 2.5 Ramification and inertia

#### 2.5.1 Valuations at points of schemes

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Extension of valuation | ✅ | `definition_extension_of_a_valuation_of_a_field_to_an_extension_field.tex` | |
| Chevalley's extension theorem | ✅ | `theorem_chevalleys_extension_theorem_for_valuations_on_extension_of_fields.tex` | |
| Henselian field | ✅ | `definition_henselian_field_with_respect_to_a_valuation.tex` | |
| Valued field Henselian ⇔ valuation ring Henselian | ✅ | `proposition_valued_field_is_henselian_iff_its_valuation_ring_is_henselian.tex` | |
| Context: extension of valuation fields | ✅ | `context_extension_of_valuation_fields.tex` | |
| Ramification index | ✅ | `definition_ramification_index_of_extension_of_valuation_fields.tex` | |
| Inertial degree | ✅ | `definition_inertial_degree_of_extension_of_valuation_fields.tex` | |
| Unramified/totally ramified/tamely/wildly ramified | ✅ | 3 definition files | |
| Dominates a local ring | ✅ | `definition_dominates_a_local_ring_for_a_local_ring_in_a_field.tex` | |
| Centered at (prime/point) | ✅ | `definition_centered_at_for_a_prime_of_an_integral_domain_point_of_an_integral_scheme.tex` | |
| Valuation centered at every prime ideal | ✅ | `proposition_integral_domain_has_a_valuation_centered_at_every_prime_ideal.tex` | |
| Valuation centered at every point | ✅ | `proposition_integral_scheme_has_a_valuation_centered_at_every_point_ideal.tex` | |
| Unique DVR at codim-1 normal point | ✅ | `theorem_unique_discrete_valuation_centered_at_every_codimension_one_normal_point_of_an_integral_scheme.tex` | |

**Genuinely missing:**
- ❌ **Higher ramification groups** (lower/upper numbering)
- ❌ **Herbrand function** / Hasse-Arf theorem
- ❌ **Local fundamental class** / local class field theory

#### 2.5.2 Decomposition groups and inertia groups

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Decomposition group (finite Galois) | ✅ | `definition_decomposition_group_of_a_finite_galois_extension_of_valuation_fields.tex` | |
| Inertia group (finite Galois) | ✅ | `definition_inertia_group_of_a_finite_galois_extension_of_valuation_fields.tex` | |
| Decomposition group (general Galois) | ✅ | `definition_decomposition_group_of_a_general_galois_extension_of_valuation_fields.tex` | |
| Inertia group (general Galois) | ✅ | `definition_inertia_group_of_a_general_galois_extension_of_valuation_fields.tex` | |
| Frobenius element | ✅ | `definition_frobenius_element_of_a_galois_extension_of_valuation_fields.tex` | |

**Genuinely missing:**
- ❌ **Ramification groups** ($G_i$ for $i \ge 0$)
- ❌ **Tame/wild inertia** structure
- ❌ **Frobenius density** / Chebotarev (covered in Section 4 but could be introduced here)

---

### 2.6 Prime decomposition in extensions of Dedekind domains

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Prime decomposition in extension | ✅ | `definition_prime_decomposition_in_extension_of_dedekind_domains.tex` | |
| Splitting type | ✅ | `definition_splitting_type_of_a_prime_in_extension_of_dedekind_domains.tex` | |
| Connection to valuation extensions | ✅ | `proposition_connection_between_dedekind_prime_decomposition_and_valuation_extensions.tex` | |

**Genuinely missing:**
- ❌ **Decomposition/inertia groups for Dedekind domains** (global version of 2.5.2)
- ❌ **Decomposition field, inertia field, ramification field**
- ❌ **Frobenius automorphism for Dedekind domains**
- ❌ **Splitting laws** (quadratic/cyclotomic extensions)
- ❌ **Discriminant and ramification** (which primes ramify)

---

### 3. Adèles and idèles of global fields

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Adèles and idèles | ✅ | `definition_adeles_and_ideles_of_a_global_field.tex` | |
| Idelic norm | ✅ | `definition_idelic_norm_of_the_ideles_of_a_global_field.tex` | |

**❌ Genuinely missing (entire section is skeletal):**
- ❌ **Topology on adèles** (restricted product topology)
- ❌ **Adèle ring is locally compact**
- ❌ **Idèle group is locally compact**
- ❌ **Diagonal embedding** $K \hookrightarrow \mathbb{A}_K$
- ❌ **Compactness of $\mathbb{A}_K / K$** (number fields) / $\mathbb{A}_K^1 / K^\times$ (idèles of norm 1)
- ❌ **Strong approximation theorem** (adèles)
- ❌ **Idèle class group** $C_K = \mathbb{A}_K^\times / K^\times$
- ❌ **Class field theory via idèles** (Artin reciprocity, global reciprocity map)
- ❌ **Existence theorem** for abelian extensions

---

### 4. Chebotarev density theorem

| Topic | Status | Vault File(s) | Notes |
|-------|--------|---------------|-------|
| Chebotarev for number fields | 📝 | (inline in content.tex) | Has `\TODO{define natural density of primes}` |
| Chebotarev for function fields | 📝 | (inline in content.tex) | Has `\TODO{continue statement}` |

**❌ Genuinely missing:**
- ❌ **Natural density / Dirichlet density** definitions
- ❌ **Effective Chebotarev** (Lagarias-Odlyzko, etc.)
- ❌ **Chebotarev for infinite extensions** (Kronecker-Weber, etc.)
- ❌ **Applications**: infinitude of primes in arithmetic progressions, etc.

---

## Appendix Sections (Already in content.tex)

### Appendix A: Galois theory
- ✅ `definition_galois_extension_of_fields.tex`

### Appendix B: Absolute values and valuations
- ✅ Multiple definition files (absolute value, discrete, trivial, metric, archimedean, topology, valuation, valuation ring, discrete valuation, nonarchimedean absolute value from valuation)

### Appendix C: Miscellaneous
- ✅ Abstract algebra definitions (commutative ring, zero divisor, localization, prime/maximal ideal, local ring, PID, UFD, function field)
- ✅ Absolute values and norms (locally compact, extended metric/norm topologies)

---

## Summary: Priority Actions

### ⏳ **High Priority: Input existing vault files into content.tex**
These files exist in `_definitions/` or `_concepts/` but are NOT in `content.tex`:

| File | Suggested Section |
|------|-------------------|
| `definition_discriminant_of_a_number_field.tex` | 2.3 (new subsection "Discriminants") |
| `definition_ideal_class_group_of_a_dedekind_domain.tex` | 2.3 (new subsection "Ideal class group") |
| `definition_fractional_ideal_of_an_integral_domain.tex` | 2.3 (prerequisite) |
| `definition_principal_fractional_ideal_of_an_integral_domain.tex` | 2.3 (prerequisite) |
| `definition_dedekind_zeta_function_of_a_number_field.tex` | 2.3 (new subsection "Zeta functions") |

### ❌ **High Priority: Create missing core theorems**
No vault files exist for these fundamental results:

1. **Finiteness of the class group** (Minkowski's theorem)
2. **Minkowski bound**
3. **Dirichlet's unit theorem** (structure of $\mathcal{O}_K^\times$)
4. **Regulator of a number field**
5. **Analytic class number formula**
6. **Different / discriminant of an extension**
7. **Product formula** (global fields)
8. **Strong approximation** (adèles)
9. **Idèle class group & global class field theory**
10. **Chebotarev: natural density definition + complete statements**

### 📝 **Medium Priority: Complete TODOs in content.tex**
- Define "natural density of primes" in Section 4
- Complete Chebotarev statement for function fields

---

## Notes for Future Work

1. **Section 2.3 is the most incomplete** — it has the ring of integers definitions but none of the deep theorems (class group, unit group, discriminants, zeta functions).

2. **Section 3 (Adèles/Idèles)** is just two definitions — needs massive expansion to be useful.

3. **Section 4 (Chebotarev)** has theorem statements with TODOs but no supporting definitions (density, etc.).

4. Consider creating **new subsections** in Section 2.3:
   - "Discriminants and the different"
   - "Ideal class group and class number"
   - "Unit group and Dirichlet's unit theorem"
   - "Zeta functions and the class number formula"

5. Consider moving **Section 3** to be a full chapter on "Adèles, Idèles, and Class Field Theory" with:
   - Adèle ring topology
   - Idèle class group
   - Artin reciprocity
   - Existence theorem
   - Kronecker-Weber / local class field theory