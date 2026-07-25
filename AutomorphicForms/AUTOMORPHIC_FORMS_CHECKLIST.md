# AutomorphicForms Content Checklist

This checklist identifies discussions that are **genuinely missing** (no definitions/theorems exist in the vault) vs. those that are **merely waiting to be input into content.tex** (definitions/theorems exist in `_definitions/` or `_concepts/` but aren't yet included in `content.tex`).

---

## Summary of Current State

**Sections in `content.tex`:**
1. **Modular forms** (classical, for congruence subgroups of SL₂(ℤ)) — definitions + 1 lemma + L-function theorem with proof
2. *Modular curves* (subsection) — 9 definitions for Y(Γ), X(Γ), X₀(N), X(N), X_H, cusps, etc.
3. **Automorphic forms** (adelic, for linear algebraic groups over global fields) — definitions + theorem/proposition/corollary (marked AI-generated/TODO)
4. **Adèles and idèles of global fields** — definitions only
5. **Appendix**: Topological group, congruence, global fields, adèles, Hecke characters & L-functions

**Total definitions input:** ~48  
**Total definitions available in `_definitions/` (automorphic/modular/adele/hecke/congruence/cusp/modular curve):** ~45  
**Total definitions available in `_concepts/` (modular/hecke/L-function):** ~4  
**All previously identified existing files are now included in `content.tex`.**

---

## 🟢 ALREADY IN content.tex (Definitions/Theorems Exist + Included)

| Topic | Files in content.tex | Status |
|-------|---------------------|--------|
| Congruence subgroup of SL₂(ℤ) | `definition_congruence_subgroup_of_SL_2_Z.tex` | ✅ |
| Lemma: every congruence subgroup has translation matrix | `lemma_every_congruence_subgroup_of_SL_2_Z_has_a_translation_matrix.tex` | ✅ |
| Modular action on upper half-plane | `definition_modular_action_of_a_subgroup_of_SL_2_Z_on_the_upper_half_plane.tex` | ✅ |
| Weight-k operator | `definition_weight_k_operator_on_meromorphic_functions_by_elements.tex` | ✅ |
| Weakly modular form | `definition_weakly_modular_form_with_respect_to_a_subgroup_of_SL_2_Z.tex` | ✅ |
| Lemma: weakly modular form is periodic | `lemma_weakly_modular_form_for_any_congruence_subgroup_of_SL_2_Z_is_periodic.tex` | ✅ |
| Holomorphic at infinity | `definition_holomorphic_at_infinity_for_a_meromorphic_function_on_the_upper_half_plane.tex` | ✅ |
| Modular form of weight k | `definition_modular_form_of_weight_k_with_respect_to_a_congruence_subgroup_of_SL_2_Z.tex` | ✅ |
| Automorphic form of weight k (classical) | `definition_automorphic_form_of_weight_k_with_respect_to_a_congruence_subgroup_of_SL_2_Z.tex` | ✅ |
| L-function of a modular form | `definition_L_function_of_a_modular_form.tex` | ✅ |
| Theorem: Mellin transform = completed L-function | (in content.tex directly) | ✅ |
| Adelic quotient of linear algebraic group | `definition_adelic_quotient_of_a_linear_algebraic_group_over_a_global_field.tex` | ✅ |
| Automorphy for function on adelic quotient | `definition_automorphy_for_a_function_on_the_adelic_quotient_group_of_a_linear_algebraic_group_over_a_global_field.tex` | ✅ |
| Right regular action of adeles | `definition_right_regular_action_of_the_adeles_of_a_linear_algebraic_group_over_a_global_field_on_the_space_of_complex_valued_functions_on_the_adelic_quotient.tex` | ✅ |
| Smooth function on adelic quotient | `definition_smooth_function_on_the_adelic_quotient_group_of_a_linear_algebraic_group_over_a_global_field.tex` | ✅ |
| K-finite function on adelic quotient | `definition_K_finite_function_on_the_adelic_quotient_group_of_a_linear_algebraic_group_over_a_global_field.tex` | ✅ |
| Moderate growth for function on adelic quotient | `definition_moderate_growth_for_a_function_on_the_adelic_quotient_group_of_a_linear_algebraic_group_over_a_global_field.tex` | ✅ |
| Automorphic form (adelic) | `definition_automorphic_form_for_a_linear_algebraic_group_over_a_global_field.tex` | ✅ |
| Basic Properties of Automorphic Forms (theorem, AI-generated) | (in content.tex) | ⚠️ AI-generated, needs verification |
| Equivalent Characterizations (proposition, AI-generated) | (in content.tex) | ⚠️ AI-generated, needs verification |
| Automorphic Forms as Sections (corollary, AI-generated) | (in content.tex) | ⚠️ AI-generated, needs verification |
| Global field | `definition_global_field.tex` | ✅ |
| Completion of global field at a place | `definition_completion_of_a_global_field_at_a_place.tex` | ✅ |
| Restricted product of topological spaces | `definition_restricted_product_of_a_family_of_topological_spaces_with_respect_to_subspaces.tex` | ✅ |
| Adèles and idèles of a global field | `definition_adeles_and_ideles_of_a_global_field.tex` | ✅ |
| Group of adelic points of algebraic group | `definition_group_of_adelic_points_of_an_algebraic_group_over_a_global_field.tex` | ✅ |
| Height function on adelic points | `definition_height_function_on_the_adelic_points_of_a_linear_algebraic_group_over_a_global_field_with_respect_to_an_embedding.tex` | ✅ |
| Linear algebraic group over a scheme | `definition_linear_algebraic_group_over_a_scheme.tex` | ✅ |
| Topological group | `definition_topological_group.tex` | ✅ |
| Principal congruence subgroup Γ(N) | `definition_principal_congruence_subgroup_Gamma_N_of_SL_2_Z.tex` | ✅ |
| Upper half-plane ℍ | `definition_upper_half_plane_in_the_complex_plane.tex` | ✅ |
| Extended upper half-plane ℍ* | `definition_extended_upper_half_plane_in_the_complex_plane.tex` | ✅ |
| Closed upper half-plane | `definition_closed_upper_half_plane_in_the_complex_plane.tex` | ✅ |
| Nontangential limit of holomorphic function on ℍ | `definition_nontangential_limit_of_a_holomorphic_function_on_the_upper_half_plane.tex` | ✅ |
| Modular action on extended upper half-plane | `definition_modular_action_of_a_subgroup_of_SL_2_Z_on_the_extended_upper_half_plane.tex` | ✅ |
| Congruence modulo n | `definition_congruence_modulo_n.tex` | ✅ |
| Star congruence of matrices | `definition_star_congruence_of_matrices_over_a_ring_with_involution.tex` | ✅ |
| Classical affine modular curve Y(Γ) | `definition_classical_affine_modular_curve_associated_to_a_congruence_subgroup_of_SL_2_Z.tex` | ✅ |
| Classical compactified modular curve X(Γ) | `definition_classical_compactified_modular_curve_associated_to_a_congruence_subgroup_of_SL_2_Z.tex` | ✅ |
| Cusps of classical modular curves | `definition_cusps_of_classical_modular_curves.tex` | ✅ |
| Modular curves X₀(N) | `definition_modular_curves_X0.tex` | ✅ |
| Modular curve X(N) with level N structure | `definition_modular_curve_X_N_with_level_N_structure.tex` | ✅ |
| X₀(N) compactified parameterizing cyclic N-isogenies | `definition_X_0_N_compactified_modular_curve_parameterizing_cyclic_N_isogenies_on_generalized_elliptic_curves.tex` | ✅ |
| X_H intermediate modular curve | `definition_X_H_intermediate_modular_curve_parameterizing_elliptic_curves_with_H_structure.tex` | ✅ |
| X(N) compactified parameterizing level N structures | `definition_X_N_compactified_modular_curve_parameterizing_level_N_structures_on_generalized_elliptic_curves.tex` | ✅ |
| X_s(N) nonclassical modular curve (noncongruence) | `definition_X_s_N_nonclassical_modular_curve_quotient_by_noncongruence_subgroup.tex` | ✅ |
| Hecke character of a number field (Grössencharakter) | `definition_hecke_character_of_a_number_field.tex` | ✅ |
| Hecke L-function of a Hecke character | `definition_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | ✅ |
| Completed Hecke L-function | `definition_completed_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` | ✅ |
| Theorem: Functional equation for Hecke L-function | `theorem_functional_equation_for_a_hecke_L_function_of_a_hecke_character_of_a_number_field.tex` (in `_concepts/`) | ✅ |
| Mellin transform of measurable function on ℝ⁺ | `definition_mellin_transform_of_a_measurable_function_on_the_positive_real_numbers.tex` | ✅ |
| Zeta integral of Schwartz-Bruhat function | `definition_zeta_integral_of_a_schwartz_bruhat_function_on_the_adeles_by_a_quasi_character_on_the_ideles_of_a_number_field.tex` | ✅ |

---

## 🟡 DEFINITIONS EXIST IN VAULT BUT NOT IN content.tex (Waiting to be Input)

*All previously identified files have been input. No remaining items in this section.*

## 🔴 GENUINELY MISSING (No Vault Files Exist)

These are standard topics in automorphic forms that have **no definitions, theorems, or propositions** in the vault at all. They need to be created from scratch.

### I. Classical Modular Forms (SL₂(ℤ) and Congruence Subgroups)

| Missing Topic | Priority for QFT/Lie/Langlands | Notes |
|---------------|-------------------------------|-------|
| **Hecke operators Tₙ on modular forms** | 🔴 Critical | Fundamental to arithmetic of modular forms; eigenforms, L-functions |
| **Eisenstein series Eₖ(z)** | 🔴 Critical | Explicit modular forms; constant terms involve ζ(k); Rankin-Selberg |
| **Cusp forms Sₖ(Γ)** | 🔴 Critical | Space of cusp forms; Petersson inner product; Hecke eigenforms |
| **Newforms / oldforms theory (Atkin-Lehner)** | 🔴 Critical | Primitive forms; level lowering/raising; local newforms |
| **Petersson inner product** | 🔴 Critical | Unitary structure on cusp forms; Hecke operators self-adjoint |
| **Fourier expansion of modular forms** | 🔴 Critical | q-expansion principle; coefficients are arithmetic |
| **Modular forms of half-integral weight** | 🟡 High | Shimura correspondence; Waldspurger formula |
| **Modular forms for Γ₁(N), Γ(N)** | 🟡 High | Nebentypus character; diamond operators |
| **Modular forms for general Fuchsian groups** | 🟢 Medium | Triangle groups; Shimura curves |
| **Maass forms (non-holomorphic)** | 🟡 High | Spectral theory of Laplacian on Γ\ℍ; continuous spectrum (Eisenstein) |
| **Weil representation / metaplectic group** | 🟡 High | Theta series; Shimura correspondence |
| **Jacquet-Langlands correspondence (classical)** | 🟡 High | Modular forms ↔ automorphic forms on D^× |
| **Modularity theorem (Taniyama-Shimura-Weil)** | 🔴 Critical | Elliptic curves ↔ weight-2 newforms |
| **Ribet's level-lowering theorem** | 🟡 High | Key to Fermat's Last Theorem |
| **Serre's conjecture (Khare-Wintenberger)** | 🟡 Medium | Mod ℓ Galois representations ↔ modular forms |

### II. Adelic Automorphic Forms & Representations

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Automorphic representation (vs. automorphic form)** | 🔴 Critical | Modern language; irreducible subquotients of L²(G(F)\G(𝔸)) |
| **Cuspidal automorphic representation** | 🔴 Critical | Rapid decay; discrete spectrum; Ramanujan conjecture |
| **Residual spectrum / Eisenstein cohomology** | 🟡 High | Continuous spectrum; residues of Eisenstein series |
| **Hecke algebra (spherical) & Satake isomorphism** | 🔴 Critical | Unramified representations; local Langlands for GL(n) |
| **Hecke operators at ramified primes** | 🟡 High | Iwahori-Hecke algebra; newforms / newvectors |
| **Whittaker models / Kirillov models** | 🟡 High | Generic representations; Fourier coefficients |
| **Local Langlands correspondence for GL(n)** | 🔴 Critical | Harris-Taylor, Henniart; LLC for classical groups |
| **Global Langlands correspondence for GL(n)** | 🔴 Critical | Arthur-Clozel; Cogdell-Piatetski-Shapiro; Lafforgue (function fields) |
| **Functoriality conjectures** | 🟡 High | Langlands functoriality; base change; endoscopy |
| **Arthur-Selberg trace formula** | 🔴 Critical | Spectral side = geometric side; fundamental tool |
| **Stable trace formula / endoscopy** | 🟡 High | Transfer factors; fundamental lemma (Ngô) |
| **Arthur packets / A-packets** | 🟡 High | Tempered and non-tempered; multiplicity formula |
| **Automorphic forms on GL(2) over number fields** | 🟡 High | Hilbert modular forms; base change |
| **Automorphic forms on classical groups** | 🟡 High | Symplectic, orthogonal, unitary; theta correspondence |
| **CAP representations** | 🟢 Medium | Cuspidal associated to parabolic; endoscopic |
| **Yoshida lifts / Saito-Kurokawa lifts** | 🟢 Medium | Non-generic functorial lifts |

### III. Shimura Varieties & Geometric Langlands

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Shimura varieties (definition, axioms)** | 🔴 Critical | Moduli of abelian varieties; Hodge structures; Langlands program |
| **Shimura varieties for GL(2) = modular curves** | 🔴 Critical | Already have classical defs; need Shimura variety perspective |
| **Shimura varieties for GSp(2g) = Siegel modular varieties** | 🟡 High | Principally polarized abelian varieties |
| **Shimura varieties for unitary groups** | 🟡 High | PEL-type; Shimura varieties with level structure |
| **Canonical models over reflex fields** | 🟡 High | Langlands' conjecture on canonical models |
| **Geometric Langlands correspondence** | 🟡 High | D-modules on Bun_G ↔ quasi-coherent sheaves on LocSys_Ǧ |
| **Hecke eigensheaves** | 🟡 High | Geometric Langlands eigen-objects |
| **Affine Grassmannian / loop groups** | 🟡 High | Geometric Satake equivalence; Mirković-Vilonen |
| **Bun_G and LocSys_G (stacks)** | 🔴 Critical | Already have basic definitions in Langlands/content.tex; need more |

### IV. L-Functions & Analytic Theory

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Standard L-function of automorphic representation** | 🔴 Critical | Langlands L-functions; Rankin-Selberg, Godement-Jacquet |
| **Rankin-Selberg L-functions** | 🔴 Critical | Convolution; analytic continuation; functional equation |
| **Langlands-Shahidi method** | 🟡 High | Generic representations; local coefficients; L-functions |
| **Euler products for L-functions** | 🔴 Critical | Local factors at each place; unramified = Satake parameters |
| **Functional equation (global)** | 🔴 Critical | Gamma factors; epsilon factors; root numbers |
| **Analytic continuation** | 🟡 High | Meromorphic continuation; poles related to functoriality |
| **Special values of L-functions** | 🟡 High | Deligne's conjecture; periods; motives |
| **Ramanujan-Petersson conjecture** | 🟡 High | |λₚ| ≤ 2p^{(k-1)/2}; Deligne (Weil II); proven for GL(n) over function fields |
| **Selberg's eigenvalue conjecture** | 🟢 Medium | λ₁ ≥ 1/4 for congruence subgroups |
| **Subconvexity bounds** | 🟡 High | L(1/2, π) ≪ C(π)^{1/4 - δ}; applications to QUE, mass equidistribution |
| **Period formulas (Waldspurger, Gross-Zagier)** | 🟡 High | Central L-values = periods; heights of Heegner points |
| **Ichino-Ikeda formula / Gan-Gross-Prasad** | 🟡 High | Period integrals = L-values; Bessel models |

### V. p-Adic & ℓ-Adic Aspects

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **p-adic modular forms / Hida theory** | 🟡 High | Ordinary parts; Λ-adic forms; Iwasawa theory |
| **p-adic L-functions** | 🟡 High | Kubota-Leopoldt; Mazur-Tate-Teitelbaum; p-adic Birch-Swinnerton-Dyer |
| **Eigenvarieties (Coleman-Mazur, Buzzard)** | 🟡 High | p-adic families of modular forms; modularity lifting |
| **ℓ-adic Galois representations attached to modular forms** | 🔴 Critical | Deligne, Eichler-Shimura, Carayol, Taylor; Langlands reciprocity |
| **Fontaine-Mazur conjecture** | 🟡 High | Geometric Galois representations ↔ automorphic |
| **Potential automorphy / modularity lifting theorems** | 🟡 High | Taylor-Wiles, Kisin, Calegari-Geraghty; FLT, Sato-Tate |
| **Local-global compatibility** | 🟡 High | Compatibility of LLC with L-functions, epsilon factors |
| **p-adic Langlands program (GL₂(ℚₚ))** | 🟡 High | Colmez, Berger, Breuil; (φ,Γ)-modules; trianguline representations |

### VI. Representation Theory of p-Adic / Real Groups

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Smooth/admissible representations of p-adic groups** | 🔴 Critical | Bernstein-Zelevinsky classification for GL(n) |
| **Types and covers (Bushnell-Kutzko)** | 🟡 High | Construction of supercuspidals; Hecke algebras |
| **Supercuspidal representations** | 🟡 High | Building blocks; depth; Yu's construction |
| **Discrete series / square-integrable representations** | 🟡 High | Tempered spectrum; Plancherel formula |
| **Langlands classification (standard modules)** | 🔴 Critical | Induction from tempered; Jantzen filtration |
| **(g,K)-modules / Harish-Chandra modules** | 🟡 High | Real reductive groups; Casselman-Wallach |
| **Unitary dual / complementary series** | 🟢 Medium | Unitary representations; Vogan's work |
| **Character formulas (Harish-Chandra, Weyl)** | 🟢 Medium | Characters as distributions; trace formula |
| **Plancherel formula for p-adic groups** | 🟢 Medium | Bernstein center; spectral decomposition |
| **Bernstein decomposition** | 🟢 Medium | Category of smooth reps = product of blocks |
| **Categorical Langlands (geometric / p-adic)** | 🟢 Medium | Derived categories; D-modules; Fargues-Scholze |

### VII. Arithmetic Applications & Conjectures

| Missing Topic | Priority | Notes |
|---------------|----------|-------|
| **Birch and Swinnerton-Dyer conjecture** | 🟡 High | L(E,1) = rank(E) · regulator · ... |
| **Gross-Zagier formula** | 🟡 High | Heegner points; L'(E,1) = height |
| **Kolyvagin's Euler systems** | 🟡 High | BSD rank 0/1; finiteness of Sha |
| **Iwasawa theory for modular forms** | 🟡 High | p-adic L-functions; Selmer groups; main conjecture |
| **Sato-Tate conjecture (proved)** | 🟡 Medium | Distribution of Frobenius traces; Barnet-Lamb et al. |
| **Modularity of abelian varieties** | 🟢 Medium | GL(2) type; Serre's conjecture |
| **Inverse Galois problem via modular forms** | 🟢 Medium | Realizing groups as Galois groups |
| **Galois representations from torsion in cohomology of Shimura varieties** | 🟡 High | Kottwitz, Harris-Taylor, Scholze; Langlands-Kottwitz method |

---

## 📋 Background Topics in Complex Analysis / Algebraic Number Theory / Analytic Number Theory to Prioritize

### Complex Analysis (Prerequisites for Modular Forms)

| Topic | Priority | Existing in Vault? |
|-------|----------|---------------------|
| **Holomorphic/meromorphic functions on ℂ** | 🔴 Critical | ✅ `definition:holomorphic_function_from_a_subset_of_Cn_to_Cm`, `definition:meromorphic_function_on_an_open_subset_of_the_complex_plane` |
| **Power series & radius of convergence / Cauchy-Hadamard** | 🔴 Critical | ✅ `definition:power_series_in_one_complex_variable_and_its_radius_of_convergence_given_by_the_cauchy_hadamard_formula`, `proposition:cauchy_hadamard_formula_for_power_series_in_one_complex_variable` (proof AI-generated) |
| **Power series converge uniformly on compact subsets** | 🔴 Critical | ✅ `lemma:power_series_in_one_complex_variable_converges_uniformly_on_compact_subsets_of_its_disk_of_convergence` (proof AI-generated) |
| **Cauchy integral theorem** | 🔴 Critical | ✅ `theorem:cauchy_integral_theorem...` (proof AI-generated) |
| **Cauchy integral formula** | 🔴 Critical | ✅ `theorem:cauchy_integral_formula_for_holomorphic_functions...` (proof AI-generated) |
| **Taylor series expansion** | 🔴 Critical | ✅ `definition:taylor_series_expansion_of_a_holomorphic_function_on_an_open_disk_in_the_complex_plane` |
| **Laurent series expansion** | 🔴 Critical | ✅ `definition:laurent_series_expansion_of_a_holomorphic_function_on_an_annulus_centered_at_an_isolated_singularity`, `theorem:laurent_series_expansion_for_holomorphic_functions_on_annuli` (proof AI-generated) |
| **Residue theorem** | 🔴 Critical | ✅ `theorem:the_residue_theorem...` (has proof) |
| **Weierstrass M-test** | 🔴 Critical | ✅ `theorem:weierstrass_m_test_for_uniform_convergence_of_function_series` (has proof, very general ordered-semiring setup) |
| **Weierstrass convergence theorem (uniform limit of holomorphic is holomorphic)** | 🔴 Critical | ✅ `theorem:the_weierstrass_convergence_theorem...` (proof AI-generated) |
| **Liouville's theorem** | 🔴 Critical | ✅ `theorem:liouvilles_theorem_on_bounded_entire_holomorphic_functions` (statement only, **no proof yet**, marked TODO) |
| **Identity theorem** | 🔴 Critical | ✅ `theorem:the_identity_theorem...` (statement only, **no proof**) |
| **Open mapping theorem** | 🔴 Critical | ✅ `theorem:the_open_mapping_theorem...` (statement only, **no proof**) |
| **Maximum modulus principle** | 🔴 Critical | ✅ `theorem:maximum_modulus_principle...` (statement only, **no proof**) |
| **Riemann mapping theorem** | 🟡 High | ✅ `theorem:the_riemann_mapping_theorem...` (statement only, **no proof**, marked TODO) |
| **Analytic continuation** | 🔴 Critical | ✅ `definition:analytic_continuation_of_a_holomorphic_function_on_an_open_subset_of_the_complex_plane` (definition exists; **uniqueness theorem missing**) |
| **Termwise differentiation of series** | 🔴 Critical | ✅ `theorem:termwise_differentiation_of_series_under_uniform_convergence_of_derivative_series` (proof AI-generated) |
| **Dirichlet L-functions & characters** | 🔴 Critical | ✅ `definition:dirichlet_character_modulo_a_nonnegative_integer`, `definition:dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer` |
| **Fourier transform (ℝ, LCA groups)** | 🔴 Critical | ✅ `definition:fourier_transform_of_an_L_1_function_on_R`, `definition:fourier_transform_of_an_L_2_function`, `definition:fourier_transform_of_a_function_on_a_locally_compact_abelian_group` |
| **Riemann zeta function** | 🔴 Critical | ✅ `definition:riemann_zeta_function` (has TODOs about meromorphic continuation, trivial zeroes, functional equation) |
| **Dedekind zeta function** | 🔴 Critical | ✅ `definition:dedekind_zeta_function_of_a_number_field` (has TODOs about Euler product, meromorphic continuation) |
| **Gamma function** | 🔴 Critical | ✅ `definition:gamma_function` (definition with analytic continuation statement; no theorems about functional equation recursion, poles, Stirling's formula) |
| **Mellin transform** | 🔴 Critical | ✅ `definition:mellin_transform_of_a_measurable_function_on_the_positive_real_numbers` |
| **Fourier series / q-expansion** | 🔴 Critical | 🟡 **No dedicated theorem file** for the Fourier series expansion of a periodic holomorphic function on ℍ; the mechanism is implicitly used in `definition:holomorphic_at_infinity_for_a_meromorphic_function_on_the_upper_half_plane` and `lemma:weakly_modular_form_for_any_congruence_subgroup_of_SL_2_Z_is_periodic` |
| **Poisson summation formula** | 🔴 Critical | ❌ **Missing** — needed for Eisenstein series Fourier expansion |
| **Phragmén-Lindelöf / convexity bounds** | 🟡 High | ❌ **Missing** |
| **Residue theorem applications to L-functions** | 🟡 High | ❌ **Missing** |
| **Modular forms as sections of line bundles on modular curves** | 🔴 Critical | ❌ **Missing** (geometric perspective) |
| **Kodaira-Spencer map / Hodge theory on modular curves** | 🟡 High | ❌ **Missing** |

### Algebraic Number Theory (Prerequisites for Adelic Automorphic Forms)

| Topic | Priority | Existing in Vault? |
|-------|----------|---------------------|
| **Adèles & idèles (topology, measure, Fourier analysis)** | 🔴 Critical | ✅ `definition:adeles_and_ideles_of_a_global_field`, `definition:restricted_product_of_a_family_of_topological_spaces_with_respect_to_subspaces`; no measure/Fourier analysis yet |
| **Class field theory (local & global)** | 🔴 Critical | Partial (AlgebraicNumberTheory has checklist but mostly missing) |
| **Hecke characters / Grössencharacters** | 🔴 Critical | ✅ `definition:hecke_character_of_a_number_field`, `definition:hecke_L_function_of_a_hecke_character_of_a_number_field`, `definition:completed_hecke_L_function_of_a_hecke_character_of_a_number_field`, `theorem:functional_equation_for_a_hecke_L_function_of_a_hecke_character_of_a_number_field` |
| **Dirichlet L-functions & characters** | 🔴 Critical | ✅ `definition:dirichlet_character_modulo_a_nonnegative_integer`, `definition:dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer` |
| **Tate's thesis (Fourier analysis on adèles)** | 🟡 High | ❌ **Missing** |
| **Artin L-functions** | 🟡 High | ❌ **Missing** |
| **Galois representations (ℓ-adic, p-adic)** | 🔴 Critical | ✅ `definition:galois_representation_over_a_topological_ring_of_a_field`, `definition:local_galois_representation_of_a_local_field_over_a_topological_ring`, `definition:global_galois_representation_of_a_global_field_over_a_topological_ring` |
| **Local fields (ℚₚ, F_q((t))) — structure, ramification** | 🟡 High | Partial (AlgebraicNumberTheory; `definition:complete_valuation_field`, `definition:completion_of_a_valuation_field`, etc. exist) |
| **Étale cohomology & ℓ-adic sheaves** | 🟡 High | ✅ `definition:etale_cohomology_group_of_a_scheme_with_coefficients_in_an_abelian_group`, `definition:etale_cohomology_of_a_sheaf_of_abelian_groups_on_the_small_etale_site_of_a_schem`, `definition:lambda_adic_cohomology_of_a_derived_etale_adic_sheaf_with_integral_coefficients_on_a_noetherian_scheme`, etc. |
| **Weil conjectures / Riemann hypothesis for varieties over finite fields** | 🟡 High | ❌ **Missing** |

### Analytic Number Theory

| Topic | Priority | Existing in Vault? |
|-------|----------|---------------------|
| **Dirichlet L-functions & characters** | 🔴 Critical | ✅ `definition:dirichlet_character_modulo_a_nonnegative_integer`, `definition:dirichlet_L_function_of_a_dirichlet_character_modulo_a_nonnegative_integer` |
| **Dirichlet series (abscissae, termwise differentiation, holomorphicity on half-planes)** | 🔴 Critical | ✅ `definition:dirichlet_series_of_a_sequence_of_complex_numbers`, `corollary:termwise_differentiation_of_dirichlet_series` (proof AI-generated) |
| **Generalized Riemann Hypothesis** | 🟡 High | ❌ **Missing** |
| **Subconvexity / hybrid bounds for L-functions** | 🟡 High | ❌ **Missing** |
| **Equidistribution (Sato-Tate, quantum unique ergodicity)** | 🟡 High | ❌ **Missing** |
| **Sieve methods & automorphic forms** | 🟢 Medium | ❌ **Missing** |
| **Spectral theory of automorphic forms (Selberg trace formula)** | 🔴 Critical | ❌ **Missing** |
| **Kuznetsov trace formula** | 🟡 High | ❌ **Missing** |
| **Exponential sums & modular forms** | 🟢 Medium | ❌ **Missing** |

### Representation Theory (Prerequisites for Automorphic Representations)

| Topic | Priority | Existing in Vault? |
|-------|----------|---------------------|
| **Representations of GL₂(ℝ), SL₂(ℝ) (principal, discrete, complementary series)** | 🔴 Critical | Missing |
| **Representations of GL₂(ℚₚ) (smooth, admissible, supercuspidal, principal series)** | 🔴 Critical | Missing |
| **Langlands parameters (L-group, Weil-Deligne group)** | 🔴 Critical | Partial (Langlands/content.tex has dual group) |
| **Local Langlands correspondence (statements, not proofs)** | 🔴 Critical | Missing |
| **(g,K)-modules, Harish-Chandra modules** | 🟡 High | Missing |
| **Category O, Verma modules, Bernstein-Gelfand-Gelfand resolution** | 🟢 Medium | Missing |

---

## 🎯 Priority Matrix for Your Three Target Areas

| Topic | QFT | Lie Groups / Lie Algebras | Langlands Program |
|-------|-----|---------------------------|-------------------|
| **Hecke operators & eigenforms** | 🔴 | 🟡 | 🔴 |
| **Eisenstein series (constant terms, Langlands-Eisenstein)** | 🔴 | 🟡 | 🔴 |
| **Automorphic representations (modern language)** | 🟡 | 🟡 | 🔴 |
| **Local Langlands for GL(n)** | 🟡 | 🟡 | 🔴 |
| **Global Langlands for GL(n)** | 🟡 | 🟡 | 🔴 |
| **Arthur-Selberg trace formula** | 🟡 | 🟡 | 🔴 |
| **Shimura varieties (moduli interpretation)** | 🟢 | 🟡 | 🔴 |
| **Geometric Langlands (D-modules, Hecke eigensheaves)** | 🟡 | 🟡 | 🔴 |
| **p-adic / ℓ-adic Galois representations** | 🟢 | 🟢 | 🔴 |
| **Langlands dual group / L-groups** | 🟢 | 🟡 | 🔴 |
| **Endoscopy / fundamental lemma** | 🟢 | 🟢 | 🔴 |
| **Theta correspondence / Howe duality** | 🟡 | 🔴 | 🟡 |
| **Representations of real reductive groups** | 🟡 | 🔴 | 🟡 |
| **Representations of p-adic reductive groups** | 🟢 | 🟡 | 🔴 |
| **L-functions (standard, Rankin-Selberg, Langlands-Shahidi)** | 🟡 | 🟡 | 🔴 |
| **Period formulas (Gross-Zagier, Waldspurger, GGP)** | 🟢 | 🟢 | 🟡 |
| **Modularity / automorphy of Galois representations** | 🟢 | 🟢 | 🔴 |

---

## 📋 Actionable Phases

### Phase 1: Complete Classical Modular Forms in content.tex (Immediate)
- [x] Add all modular curve definitions (Y(Γ), X(Γ), X₀(N), X(N), cusps) — *2026-07-23*
- [x] Add principal congruence subgroup Γ(N) — *2026-07-23*
- [x] Add modular action on extended upper half-plane — *2026-07-23*
- [x] Add upper half-plane definitions (ℍ, ℍ*, closed ℍ, nontangential limit) — *2026-07-23*
- [x] Add congruence modulo n, star congruence — *2026-07-23*
- [x] Add Hecke theory definitions (Hecke character, Hecke L-function, completed Hecke L-function, functional equation theorem) — *2026-07-23*
- [x] Add Mellin transform, zeta integral definitions — *2026-07-23*
- [ ] **Create missing definitions**: Hecke operators, Eisenstein series, cusp forms, Petersson inner product, newforms/oldforms
- [ ] **Create missing theorems**: Hecke operators commute/self-adjoint, multiplicity one, Atkin-Lehner theory

### Phase 2: Adelic Automorphic Forms & Representations (Core)
- [ ] Replace "automorphic form" definitions with "automorphic representation" language
- [ ] Add: cuspidal automorphic representation, residual spectrum, continuous spectrum
- [ ] Add: Hecke algebra, Satake isomorphism, spherical Hecke algebra
- [ ] Add: Whittaker models, generic representations
- [ ] Add: Local Langlands for GL(n) statements
- [ ] Add: Global Langlands for GL(n) statements

### Phase 3: L-Functions & Analytic Theory
- [ ] Add: Standard L-functions, Rankin-Selberg, Langlands-Shahidi
- [ ] Add: Functional equations, Euler products, gamma factors
- [ ] Add: Ramanujan-Petersson, subconvexity, special values

### Phase 4: Geometric & p-Adic Langlands
- [ ] Expand Shimura varieties (canonical models, moduli interpretations)
- [ ] Expand geometric Langlands (Bun_G, LocSys_G, Hecke eigensheaves)
- [ ] Add: p-adic modular forms, Hida theory, eigenvarieties
- [ ] Add: ℓ-adic Galois representations from modular forms

### Phase 5: Background Infrastructure (Prerequisites)

#### Complex Analysis — Write missing proofs for statement-only theorems
- [ ] **Write proof**: Liouville's theorem (via Cauchy integral formula)
- [ ] **Write proof**: Identity theorem (via power series expansion)
- [ ] **Write proof**: Open mapping theorem
- [ ] **Write proof**: Maximum modulus principle
- [ ] **Write proof**: Riemann mapping theorem
- [ ] **Write proof**: Uniqueness of analytic continuation
- [ ] **Create missing**: Poisson summation formula (needed for Eisenstein series Fourier expansion)
- [ ] **Create missing**: Fourier series expansion theorem for periodic holomorphic functions on ℍ
- [ ] **Verify**: 6 AI-generated proofs (Cauchy integral theorem, Cauchy integral formula, Laurent series, Weierstrass convergence, power series lemmas, termwise differentiation)
- [ ] **Fill TODOs**: Riemann zeta function (meromorphic continuation, trivial zeroes, functional equation), Dedekind zeta function (Euler product, meromorphic continuation), Gamma function (functional equation recursion, poles, Stirling's formula)

#### Algebraic Number Theory
- [ ] Complete class field theory (local & global)
- [ ] Create: Tate's thesis (Fourier analysis on adèles)
- [ ] Create: Artin L-functions

#### Representation Theory
- [ ] Build RepresentationTheory for p-adic/real reductive groups
- [ ] Build Langlands folder with precise conjectures

---

## 🔍 How to Verify Existence in Vault

```bash
# Search definitions
rg "definition_.*hecke" _definitions/
rg "definition_.*eisenstein" _definitions/
rg "definition_.*cusp.*form" _definitions/
rg "definition_.*automorphic.*representation" _definitions/

# Search concepts
rg "theorem_.*hecke" _concepts/
rg "proposition_.*eisenstein" _concepts/
rg "corollary_.*cusp" _concepts/

# Check content.tex
grep -n "hecke\|eisenstein\|cusp\|newform\|oldform\|maass\|petersson\|satake\|shimura\|langlands.*correspondence\|trace.*formula\|endoscopy\|arthur" content.tex
```

---

*Generated by examining `content.tex`, searching `_definitions/`, `_concepts/`, and cross-referencing `Langlands/content.tex`, `RepresentationTheory/content.tex`, `AlgebraicNumberTheory/content.tex`, `QuantumFieldTheory/content.tex`. Last updated: 2026-07-22*