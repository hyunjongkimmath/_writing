# AlgebraicNumberTheory Content Checklist

This checklist identifies discussions that are **genuinely missing** (no definitions/theorems exist in the vault) vs. those that are **merely waiting to be input into content.tex** (definitions/theorems exist in `_definitions/` or `_concepts/` but aren't yet included in `content.tex`).

---

## Summary of Current State

**Sections in `content.tex`:**
1. Dedekind domains (definitions + 2 propositions)
2. Local and global fields (definitions, classifications, completions)
3. Rings of integers of local/global fields (definitions + 1 theorem)
4. Local fields as completions of global fields (1 theorem + remark)
5. Ramification and inertia (definitions + Chevalley's theorem + Henselian)
6. Valuations at points of schemes (definitions + propositions)
7. Decomposition/inertia groups (definitions only)
8. Prime decomposition in extensions of Dedekind domains (definitions + 1 proposition)
9. Adèles and idèles (2 definitions only)
10. Chebotarev density theorem (incomplete statements with TODOs)
11. Appendices: Galois theory, absolute values/valuations, miscellaneous

---

## 🟢 ALREADY IN content.tex (Definitions/Theorems Exist)

These are **fully present** in content.tex with their component files existing:

| Topic | Status | Files in content.tex |
|-------|--------|---------------------|
| Noetherian ring | ✅ | `definition_noetherian_ring.tex` |
| Discrete valuation ring | ✅ | `definition_discrete_valuation_ring.tex` |
| DVRs ↔ discretely valued fields | ✅ | `theorem_correspondence_between_dvrs_and_discretely_valued_fields.tex` |
| Integral element | ✅ | `definition_integral_element_over_a_ring.tex` |
| Dedekind domain | ✅ | `definition_dedekind_domain.tex` |
| DVRs are Dedekind domains | ✅ | `proposition_dvrs_are_dedekind_domains.tex` |
| Dedekind domain = PID iff UFD | ✅ | `proposition_dedekind_domain_is_a_pid_if_and_only_if_ufd.tex` |
| Local field | ✅ | `definition_local_field.tex` |
| Local fields are complete | ✅ | `theorem_local_fields_are_complete.tex` |
| Classification of local fields | ✅ | `theorem_classification_of_local_fields.tex` |
| Number field | ✅ | `definition_number_field.tex` |
| Global function field | ✅ | `definition_global_function_field.tex` |
| Global field | ✅ | `definition_global_field.tex` |
| Equivalent absolute values | ✅ | `definition_equivalent_absolute_values_on_a_field.tex` |
| Place of a field | ✅ | `definition_place_of_a_field.tex` |
| Equivalent places | ✅ | `definition_equivalent_places_of_a_field.tex` |
| Place of a global field | ✅ | `definition_place_of_a_global_field.tex` |
| Completion at a place | ✅ | `definition_completion_of_a_global_field_at_a_place.tex` |
| Ring of integers (extension of fraction field) | ✅ | `definition_ring_of_integers_of_an_extension_of_fraction_field_of_a_dedekind_domain.tex` |
| Ring of integers (global/local) | ✅ | `definition_ring_of_integers_of_a_global_or_local_ring.tex` |
| Rings of integers are Dedekind | ✅ | `theorem_rings_of_integers_of_global_fields_or_nonarchimedean_local_fields_are_dedekind_domains.tex` |
| Completion = local field | ✅ | `theorem_completion_of_a_global_field_at_a_place_is_a_local_field.tex` |
| Absolute norm of ideal | ✅ | `definition_absolute_norm_of_an_ideal_of_the_ring_of_integers_of_a_global_or_local_field.tex` |
| p-adic valuation/abs value | ✅ | `definition_p_adic_valuation_and_absolute_value_on_a_number_field.tex` |
| Classification of places of global fields | ✅ | `theorem_classification_of_places_of_global_fields.tex` |
| Extension of valuation | ✅ | `definition_extension_of_a_valuation_of_a_field_to_an_extension_field.tex` |
| Chevalley's extension theorem | ✅ | `theorem_chevalleys_extension_theorem_for_valuations_on_extension_of_fields.tex` |
| Henselian field | ✅ | `definition_henselian_field_with_respect_to_a_valuation.tex` |
| Valued field Henselian iff valuation ring Henselian | ✅ | `proposition_valued_field_is_henselian_iff_its_valuation_ring_is_henselian.tex` |
| Context: extension of valuation fields | ✅ | `context_extension_of_valuation_fields.tex` |
| Ramification index | ✅ | `definition_ramification_index_of_extension_of_valuation_fields.tex` |
| Inertial degree | ✅ | `definition_inertial_degree_of_extension_of_valuation_fields.tex` |
| Unramified/totally ramified/tamely/wildly ramified | ✅ | `definition_unramified_extension_of_valuation_fields.tex`, `definition_totally_ramified_extension_of_valuation_fields.tex`, `definition_tamely_and_wildly_ramified_extension_of_valuation_fields.tex` |
| Valuations at points of schemes | ✅ | `definition_dominates_a_local_ring_for_a_local_ring_in_a_field.tex`, `definition_centered_at_for_a_prime_of_an_integral_domain_point_of_an_integral_scheme.tex` |
| Valuation centered at prime/point | ✅ | `proposition_integral_domain_has_a_valuation_centered_at_every_prime_ideal.tex`, `proposition_integral_scheme_has_a_valuation_centered_at_every_point_ideal.tex` |
| Unique DVR at codim-1 normal point | ✅ | `theorem_unique_discrete_valuation_centered_at_every_codimension_one_normal_point_of_an_integral_scheme.tex` |
| Decomposition/inertia groups (finite/general) | ✅ | 4 definition files |
| Frobenius element | ✅ | `definition_frobenius_element_of_a_galois_extension_of_valuation_fields.tex` |
| Prime decomposition in extensions | ✅ | `definition_prime_decomposition_in_extension_of_dedekind_domains.tex` |
| Splitting type | ✅ | `definition_splitting_type_of_a_prime_in_extension_of_dedekind_domains.tex` |
| Connection: prime decomp ↔ valuation extensions | ✅ | `proposition_connection_between_dedekind_prime_decomposition_and_valuation_extensions.tex` |
| Adèles and idèles | ✅ | `definition_adeles_and_ideles_of_a_global_field.tex` |
| Idelic norm | ✅ | `definition_idelic_norm_of_the_ideles_of_a_global_field.tex` |
| Discriminant of number field | ⚠️ Definition exists (`definition_discriminant_of_a_number_field.tex`) but **NOT in content.tex** |
| Ideal class group | ⚠️ Definition exists (`definition_ideal_class_group_of_a_dedekind_domain.tex`) but **NOT in content.tex** |

---

## 🟡 DEFINITIONS EXIST BUT NOT IN content.tex (Waiting to be Input)

These definitions/theorems exist in the vault but are **not yet included** in `content.tex`:

| Missing Topic | Existing File(s) | Notes |
|---------------|------------------|-------|
| **Discriminant of a number field** | `definition_discriminant_of_a_number_field.tex` | Fundamental; should be in "Rings of integers" or new section |
| **Ideal class group of a Dedekind domain** | `definition_ideal_class_group_of_a_dedekind_domain.tex` | Core concept; class number, finiteness missing |
| **Fractional ideal of integral domain** | `definition_fractional_ideal_of_an_integral_domain.tex` | Prerequisite for class group |
| **Principal fractional ideal** | `definition_principal_fractional_ideal_of_an_integral_domain.tex` | Prerequisite for class group |
| **Invertible fractional ideal** | (in fractional ideal def) | Part of class group definition |
| **Different of an extension** | `definition_different_of_an_extension_of_dedekind_domains.tex` (check) | Related to discriminant |
| **Conductor** | `definition_conductor_of_an_extension_of_dedekind_domains.tex` (check) | Related to ramification |
| **Norm of an ideal** | `definition_norm_of_an_ideal_in_dedekind_domain.tex` (check) | Different from absolute norm |

---

## 🔴 GENUINELY MISSING (No Vault Files Exist)

These are **standard algebraic number theory topics** that have **no definitions, theorems, or propositions** in the vault at all. They need to be created from scratch.

### A. Class Group & Class Number Theory

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Finiteness of the class group** (Minkowski's theorem) | 🔴 Critical | The fundamental finiteness result |
| **Minkowski's bound / Minkowski's theorem** | 🔴 Critical | Proof of class group finiteness |
| **Class number formula (analytic)** | 🔴 Critical | Relates class number to L-function values |
| **Dirichlet's Unit Theorem** | 🔴 Critical | Structure of unit group: rank = r₁ + r₂ - 1 |
| **Regulator of a number field** | 🔴 High | Appears in class number formula |
| **Dirichlet's theorem on units in real quadratic fields** | 🟡 Medium | Special case |
| **Computation of class groups** | 🟡 Medium | Algorithmic / examples |

### B. Ramification Theory (Deeper Results)

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Different and discriminant relation** | 🔴 High | $\mathfrak{d}_{L/K} \mid \Delta_{L/K}$ etc. |
| **Conductor-discriminant formula** | 🟡 Medium | Relates Artin conductor to discriminant |
| **Higher ramification groups** | 🟡 Medium | Lower/upper numbering (Herbrand) |
| **Tame vs wild ramification criteria** | 🟡 Medium | $p \nmid e$ for tame |
| **Krasner's lemma** | 🟡 Medium | Application of Hensel's lemma |
| **Local fields: structure of $\mathcal{O}_K^\times$** | 🟡 Medium | Filtration $U^{(n)}$ |

### C. Decomposition/Inertia Groups (Theorems)

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Structure of decomposition group** | 🔴 High | $D/I \cong \text{Gal}(k_{\mathfrak{P}}/k_{\mathfrak{p}})$ |
| **Inertia group is normal in decomposition group** | 🔴 High | $I \trianglelefteq D$ |
| **Ramification index = |I|, Inertial degree = |D/I|** | 🔴 High | Fundamental |
| **Frobenius element properties** | 🟡 Medium | Order = inertial degree, etc. |
| **Chebotarev density (complete statement)** | 🟡 Medium | content.tex has TODO placeholders |

### D. Local Class Field Theory

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Local reciprocity map** | 🔴 High | $K^\times \to \text{Gal}(K^{\text{ab}}/K)$ |
| **Lubin-Tate theory** | 🟡 Medium | Explicit construction for local fields |
| **Local Kronecker-Weber** | 🟡 Medium | $\mathbb{Q}_p^{\text{ab}} = \mathbb{Q}_p(\mu_{p^\infty})$ |
| **Higher local class field theory** | ⚪ Low | Kato-Saito, etc. |

### E. Global Class Field Theory

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Idele class group** $C_K = \mathbb{A}_K^\times / K^\times$ | 🔴 High | Already have adèles/idèles definitions |
| **Global reciprocity map** | 🔴 High | $C_K \to \text{Gal}(K^{\text{ab}}/K)$ |
| **Artin reciprocity law** | 🔴 High | Isomorphism on profinite completion |
| **Hilbert class field** | 🔴 High | Maximal unramified abelian extension |
| **Ray class field / ray class group** | 🔴 High | Generalization with modulus |
| **Conductor of an abelian extension** | 🟡 Medium | Artin conductor = discriminant conductor |
| **Kronecker-Weber theorem** | 🟡 Medium | $\mathbb{Q}^{\text{ab}} = \mathbb{Q}(\mu_\infty)$ |
| **Existence theorem** | 🟡 Medium | Subgroups of idele class group ↔ abelian extensions |

### F. Analytic Theory

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Dedekind zeta function** $\zeta_K(s)$ | 🔴 High | Definition exists: `definition_dedekind_zeta_function_of_a_number_field.tex` but no theorems |
| **Analytic continuation & functional equation** | 🟡 Medium | |
| **Analytic class number formula** | 🔴 Critical | Residue at s=1 involves $h_K, R_K, w_K, \sqrt{|d_K|}$ |
| **Hecke L-functions** | 🟡 Medium | Definitions: `definition_hecke_L_function_of_a_hecke_character_of_a_number_field.tex`, `definition_completed_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` exist but no theorems |
| **Hecke characters / Grössencharacters** | 🟡 Medium | Definition exists: `definition_hecke_character_of_a_number_field.tex` |
| **Artin L-functions** | 🟡 Medium | Non-abelian case |
| **Chebotarev density (analytic proof)** | 🟡 Medium | |

### G. Iwasawa Theory

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **$\mathbb{Z}_p$-extensions** | ⚪ Low | Cyclotomic $\mathbb{Z}_p$-extension |
| **Iwasawa modules** $X_\infty, A_\infty$ | ⚪ Low | |
| **Iwasawa invariants** $\lambda, \mu, \nu$ | ⚪ Low | |
| **Main conjecture** | ⚪ Low | Relates L-functions to characteristic ideals |
| **p-adic L-functions** | ⚪ Low | Kubota-Leopoldt, etc. |

### H. Special Topics

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Quadratic fields: explicit class numbers** | 🟡 Medium | $h(\mathbb{Q}(\sqrt{d}))$ |
| **Cyclotomic fields** | 🟡 Medium | $\mathbb{Q}(\zeta_n)$, Vandiver's conjecture |
| **CM fields / CM theory** | 🟡 Medium | Definitions exist for some |
| **Elliptic curves with CM** | ⚪ Low | Definitions exist for some |
| **Modular forms & Galois representations** | ⚪ Low | |
| **Shimura-Taniyama / Langlands** | ⚪ Low | |

---

## 📋 Action Items

### Immediate (Add to content.tex - files already exist)

- [ ] Add `definition_discriminant_of_a_number_field.tex` to "Rings of integers" section
- [ ] Add `definition_ideal_class_group_of_a_dedekind_domain.tex` to new "Class group" section
- [ ] Add `definition_fractional_ideal_of_an_integral_domain.tex` and `definition_principal_fractional_ideal_of_an_integral_domain.tex` as prerequisites

### Short-term (Create missing definitions/theorems - CORE)

- [ ] **Minkowski's theorem** (geometry of numbers → class group finiteness)
- [ ] **Dirichlet's Unit Theorem** (structure of $\mathcal{O}_K^\times$)
- [ ] **Finiteness of class group** theorem
- [ ] **Analytic class number formula** (with Dedekind zeta function)
- [ ] **Decomposition/inertia group structure theorems**
- [ ] **Different and discriminant** definitions + relation
- [ ] **Hilbert class field** definition + main properties
- [ ] **Ray class group / ray class field** definitions

### Medium-term (Create missing definitions/theorems - CLASS FIELD THEORY)

- [ ] **Idele class group** definition (from existing adèles/idèles)
- [ ] **Global reciprocity map** + **Artin reciprocity law**
- [ ] **Local reciprocity map** + **Local class field theory** basics
- [ ] **Kronecker-Weber theorem**
- [ ] **Artin L-functions** + **Chebotarev density** (complete)

### Long-term (Create - ADVANCED)

- [ ] **Iwasawa theory** basics
- [ ] **p-adic L-functions**
- [ ] **Hecke L-functions** theorems (functional equation, etc.)
- [ ] **CM theory** / **Modular forms** connections

---

## 📍 Suggested New Section Structure for content.tex

```
\section{Class groups and unit groups}
    \subsection{Finiteness of the class group}
    \subsection{Minkowski's theorem and bounds}
    \subsection{Dirichlet's unit theorem}
    \subsection{The analytic class number formula}

\section{Ramification theory (advanced)}
    \subsection{The different and discriminant}
    \subsection{Higher ramification groups}
    \subsection{Conductor-discriminant formula}

\section{Decomposition and inertia (theorems)}
    \subsection{Structure of decomposition and inertia groups}
    \subsection{Frobenius elements and Artin symbols}

\section{Adèles, idèles, and class field theory}
    \subsection{The idele class group}
    \subsection{Local class field theory}
    \subsection{Global class field theory}
    \subsection{The Kronecker-Weber theorem}
    \subsection{Hilbert and ray class fields}

\section{Zeta and L-functions}
    \subsection{Dedekind zeta functions}
    \subsection{Hecke L-functions}
    \subsection{Artin L-functions and Chebotarev density}

\section{Iwasawa theory}
    \subsection{$\mathbb{Z}_p$-extensions and Iwasawa modules}
    \subsection{The main conjecture}
```

---

## 🔍 How to Verify

To check if a topic exists in the vault:
```bash
# Search definitions
rg "definition.*topic" _definitions/

# Search concepts
rg "theorem.*topic" _concepts/
rg "proposition.*topic" _concepts/
rg "corollary.*topic" _concepts/

# Check content.tex
grep -n "topic" content.tex
```

---

*Generated by examining `content.tex` and searching the vault for relevant definitions/theorems. Last updated: 2026-07-22*