# Schemes Cohomology Theories Checklist

**Purpose:** Track coverage of cohomology theories for schemes, with emphasis on crystalline, de Rham, and other theories beyond étale.
**Source of truth:** `Schemes/content.tex` (active vs. commented inputs) + `_definitions/` + `_concepts/` file existence.
**Cross-ref:** `AlgebraicNumberTheory`, `Topology`, `Langlands`, `QuantumFieldTheory`, `Manifolds`, `RepresentationTheory` vaults.

---

## Legend
| Symbol | Meaning |
|--------|---------|
| ✅ **ACTIVE** | Wired in `content.tex` (not commented), definition file exists |
| 📝 **DEFINED** | Definition file exists in `_definitions/` or `_concepts/`, not yet wired |
| ⏳ **DRAFT** | Draft exists in `_assembly/`, needs review/move |
| ❌ **MISSING** | No file exists, not in content.tex |
| 💬 **COMMENTED** | Referenced in `content.tex` but commented out |
| 🔗 **EXT REF** | Referenced from another vault (definition exists elsewhere) |

---

## Phase 0: Foundations (Prerequisites for all cohomology theories)

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 0.1 | Presheaf / Sheaf (on a site) | ✅ **ACTIVE** | `definition_presheaf_on_a_category.tex`, `definition_sheaf_on_a_site.tex`, `definition_sheafification_functor_on_a_site.tex`, `definition_site_of_opens_on_a_topological_space.tex`, `definition_category_of_opens_of_a_topological_space.tex` | | Wired in §1.1–1.2 |
| 0.2 | Sheaf cohomology (derived functor, Čech, hypercohomology) | ✅ **ACTIVE** | `definition_sheaf_cohomology_group_of_a_sheaf_of_modules_over_a_sheaf_of_rings_on_a_site.tex`, `definition_sheaf_cohomology_objects_of_a_sheaf_on_a_top_space...tex`, `definition_cech_cohomology_of_a_sheaf_of_abelian_groups_on_a_topological_space.tex`, `definition_hypercohomology_groups_of_a_bounded_constructible_complex_with_torsion_coefficients_on_a_scheme.tex` | `theorem_cech_cohom_for_a_sheaf_of_ab_gps_agrees_with_sheaf_cohom_on_a_paracomp_haus_space...tex`, `theorem_leray_spectral_sequence_for_sheaf_cohomology_and_a_continuous_map_of_topological_spaces.tex`, `theorem_lerays_theorem_that_cech_cohom_of_a_sheaf_of_ab_gps_on_top_space_wrt_an_open_cover_agrees_with_sheaf_cohom_if_cover_is_acyclic_for_the_sheaf.tex` | Core machinery; hypercohomology only for constructible torsion |
| 0.3 | Quasi-coherent sheaves | ✅ **ACTIVE** | `definition_quasi_coherent_sheaf_on_a_ringed_site.tex`, `definition_quasi_coherent_sheaf_on_a_ringed_space.tex`, `definition_quasi_coherent_sheaf_on_an_affine_scheme.tex`, `definition_quasi_coherent_sheaf_on_a_general_scheme.tex` | | Wired in §"Quasi-coherent and Coherent sheaves" |
| 0.4 | Coherent sheaves | ✅ **ACTIVE** | `definition_coherent_sheaf_on_a_ringed_site.tex`, `definition_coherent_sheaf_on_a_ringed_space.tex`, `definition_coherent_sheaf_on_a_scheme.tex`, `definition_coherent_object_in_a_locally_small_site.tex`, `definition_coherent_site.tex`, `definition_coherent_topos.tex` | `theorem_a_coherent_topos_has_enough_points.tex`, `theorem_delignes_completeness_theorem_for_coherent_topoi.tex`, `theorem_examples_of_coherent_sites.tex` | Wired in same section |
| 0.5 | Scheme, morphism, affine scheme, structure sheaf | ✅ **ACTIVE** | `definition_scheme.tex`, `definition_morphism_of_schemes.tex`, `definition_affine_scheme.tex`, `definition_ringed_space.tex`, `definition_locally_ringed_space_on_a_topological_space.tex`, `definition_morphism_of_ringed_spaces.tex`, `definition_morphism_of_locally_ringed_spaces.tex` | | Wired in §1 "Formalities..." |
| 0.6 | Flat / smooth / étale / proper / finite morphisms | ✅ **ACTIVE** | `definition_flat_morphism_of_schemes.tex`, `definition_faithfully_flat_morphism_of_schemes.tex`, `definition_smooth_morphism_of_schemes.tex`, `definition_etale_morphism_of_schemes.tex`, `definition_proper_morphism_of_schemes.tex`, `definition_finite_morphism_of_schemes.tex`, `definition_quasifinite_morphism_of_schemes.tex`, `definition_locally_quasifinite_morphism_of_schemes.tex`, `definition_finite_locally_free_morphism_of_schemes.tex`, `definition_syntomic_morphism_of_schemes.tex`, `definition_unramified_morphism_of_schemes.tex`, `definition_G_unramified_morphism_of_schemes.tex`, `definition_weakly_unramified_morphism_of_schemes.tex`, `definition_weakly_etale_morphism_of_schemes.tex`, `definition_ind_etale_morphism_of_schemes.tex`, `definition_profinite_etale_cover_of_schemes.tex` | Many stability propositions wired in §"Stability under base change and composition" | |
| 0.7 | Sites and topoi (Zariski, étale, fppf, fpqc, crystalline) | 📝 **DEFINED** | `definition_grothendieck_topology_on_a_category_site_covering_sieve_topologically_generating_family.tex`, `definition_sheaf_on_a_site.tex`, `definition_site_induced_by_a_site_on_an_over_category.tex`, `definition_site_of_opens_on_a_topological_space.tex`, `definition_site_with_enough_points.tex`, `definition_topos.tex`, `definition_small_zariski_site_of_a_schem.tex`, `definition_small_etale_site_of_a_scheme.tex`, `definition_small_fppf_site_of_a_scheme.tex`, `definition_small_fpqc_site_of_a_schem.tex`, `definition_small_nisnevich_site_of_a_schem.tex`, `definition_big_zariski_site_of_a_scheme.tex`, `definition_big_etale_site_of_a_scheme.tex`, `definition_big_fppf_site_of_a_scheme.tex`, `definition_big_fpqc_site_of_a_scheme.tex`, `definition_big_site_on_the_category_of_schemes_over_a_scheme_and_small_site.tex`, `definition_continuous_functor_of_sites.tex`, `definition_equivalence_of_sites.tex`, `definition_cocontinuous_functor_of_sites.tex`, `definition_morphism_of_sites.tex`, `definition_ringed_site.tex`, `definition_ringed_topos.tex` | `theorem_hierarchy_of_common_grothendieck_topologies_on_Sch_S.tex` | Crystalline site ❌ MISSING |
| 0.8 | Derived category $D(QCoh(X))$, $D(Coh(X))$ | 📝 **DEFINED** | `definition_derived_category_of_an_abelian_category.tex`, `definition_derived_category_of_bounded_above_complexes_of_adic_sheaves_on_a_scheme.tex`, `definition_derived_category_of_bounded_constructible_complexes_of_adic_sheaves_with_integral_coefficients_on_a_noetherian_scheme.tex`, `definition_derived_category_of_cohomologically_bounded_constructible_sheaves_with_rational_adic_coefficients_on_a_noetherian_scheme.tex`, `definition_derived_category_of_cohomologically_constructible_complexes_of_sheaves_of_modules_of_a_sheaf_of_rings_on_a_topological_space_or_scheme.tex`, `definition_derived_category_of_complexes_of_pro_etale_sheaves_whose_cohomology_are_continuously_constant.tex` | `theorem_derived_categories_can_be_identified_with_homotopy_categories_of_injectives_or_projectives.tex`, `theorem_derived_functor_of_additive_functor_between_abelian_categories_is_defined_on_bounded_above_below_complexes_if_enough_acyclics_exist.tex`, `theorem_grothendieck_categories_have_enough_K_injective_complexe.tex` | For adic/constructible sheaves; $D(QCoh)$ specifically ❌ MISSING |
| 0.9 | Six operations formalism ($f_*, f^*, f_!, f^!, \otimes, \mathcal{H}om$) | 📝 **DEFINED** | `definition_six_functor_formalism_for_an_infty_category_with_finite_limtis_and_class_of_morphisms_containing_isomorphisms_and_stable_under_pulback_and_composition.tex`, `definition_six_functor_formalism_on_derived_category_of_bdd_constr_complexes_of_adic_sheaves_with_integral_coefficients_on_a_noetherian_scheme.tex`, `definition_six_functor_formalism_on_derived_category_of_bdd_constr_complexes_with_algebraic_coefficients_on_a_noetherian_scheme.tex`, `definition_six_functor_formalism_on_derived_category_of_bdd_constr_complexes_with_rational_coefficients_on_a_noetherian_scheme.tex`, `definition_six_functor_formalism_on_derived_category_of_etale_sheaves_with_torsion_coefficients_on_a_noetherian_scheme.tex` | `theorem_six_functor_formalism_of_ekedahls_adic_categories_on_schemes.tex`, many projection formula propositions | For adic/constructible sheaves; not for $QCoh$ |

---

## Phase 1: Étale Cohomology (Baseline — you know this)

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 1.1 | Étale site, étale sheaf | ✅ **ACTIVE** | `definition_small_etale_site_of_a_scheme.tex`, `definition_big_etale_site_of_a_scheme.tex`, `definition_etale_morphism_of_schemes.tex`, `definition_etale_O_X_algebra_over_a_scheme.tex`, `definition_etale_algebra_over_a_commutative_ring.tex`, `definition_ind_etale_algebra_over_a_commutative_ring.tex`, `definition_ind_etale_morphism_of_schemes.tex`, `definition_profinite_etale_cover_of_schemes.tex`, `definition_weakly_etale_morphism_of_schemes.tex`, `definition_additive_sheaf_on_the_small_etale_site_of_a_scheme.tex` | | Wired in §"Properties of morphisms" and §"Inverse limits" |
| 1.2 | Étale cohomology groups $H^i_{\text{ét}}(X, \mathcal{F})$ | ✅ **ACTIVE** | `definition_etale_cohomology_group_of_a_scheme_with_coefficients_in_an_abelian_group.tex`, `definition_etale_cohomology_of_a_sheaf_of_abelian_groups_on_the_small_etale_site_of_a_schem.tex`, `definition_ell_adic_cohomology_of_a_scheme.tex`, `definition_ell_adic_sheaf_Z_ell_on_small_etale_site_of_a_scheme.tex`, `definition_ell_adic_tate_twist_sheaves_on_the_small_etale_site_of_a_scheme.tex`, `definition_lambda_adic_cohomology_of_a_derived_etale_adic_sheaf_with_integral_coefficients_on_a_noetherian_scheme.tex`, `definition_lambda_adic_cohomology_of_a_derived_etale_adic_sheaf_with_rational_coefficients_on_a_noetherian_scheme.tex`, `definition_lambda_adic_sheaf_on_the_small_etale_site_of_a_scheme_for_an_ideal_of_a_commutative_ring.tex`, `definition_compactly_supported_cohomology_groups_for_various_coefficient_systems.tex`, `definition_compactly_supported_lambda_adic_cohomology_groups_with_algebraic_coefficients_on_a_noetherian_scheme.tex`, `definition_compactly_supported_lambda_adic_cohomology_groups_with_integral_coefficients_on_a_noetherian_scheme.tex`, `definition_compactly_supported_lambda_adic_cohomology_groups_with_rational_coefficients_on_a_noetherian_scheme.tex` | `theorem_proper_base_change_theorem_for_derived_category_of_adic_sheaves_with_algebraic_coefficients_on_schemes.tex`, `theorem_proper_base_change_theorem_for_derived_category_of_adic_sheaves_with_integral_coefficients_on_schemes.tex`, `theorem_proper_base_change_theorem_for_derived_category_of_adic_sheaves_with_rational_coefficients_on_schemes.tex`, `theorem_proper_base_change_theorem_for_derived_category_of_bounded_constructible_sheaves_over_a_scheme_over_a_field.tex`, `theorem_smooth_base_change_theorem_for_derived_category_of_Z_nZ_sheaves_on_schemes.tex`, `theorem_smooth_base_change_theorem_for_derived_category_of_adic_sheaves_with_algebraic_coefficients_on_schemes.tex`, `theorem_smooth_base_change_theorem_for_derived_category_of_adic_sheaves_with_integral_coefficients_on_schemes.tex`, `theorem_smooth_base_change_theorem_for_derived_category_of_adic_sheaves_with_rational_coefficients_on_schemes.tex` | Comprehensive coverage |
| 1.3 | $\ell$-adic sheaves, constructible sheaves | ✅ **ACTIVE** | `definition_constructible_sheaf_on_a_small_site_on_a_scheme_or_a_topological_space.tex`, `definition_lambda_torsion_sheaf_of_modules_over_a_sheaf_of_rings_on_a_site_for_a_sheaf_of_ideals.tex`, `definition_ell_adic_sheaf_Z_ell_on_small_etale_site_of_a_scheme.tex`, `definition_ell_adic_tate_twist_sheaves_on_the_small_etale_site_of_a_scheme.tex`, `definition_lambda_adic_sheaf_on_the_small_etale_site_of_a_scheme_for_an_ideal_of_a_commutative_ring.tex` | | |
| 1.4 | Proper base change, smooth base change | ✅ **ACTIVE** | See 1.2 | See 1.2 | Multiple coefficient systems covered |
| 1.5 | Poincaré duality, trace map | ❌ **MISSING** | | | No definition for étale Poincaré duality or trace map |
| 1.6 | Cycle class map $\mathrm{CH}^i(X) \to H^{2i}_{\text{ét}}(X, \mathbb{Q}_\ell(i))$ | ❌ **MISSING** | `definition_chow_ring_of_smooth_variety_over_a_field.tex`, `definition_operational_chow_ring_of_a_noetherian_scheme.tex`, `definition_relative_chow_ring_of_a_smooth_projective_scheme_over_a_noetherian_base.tex` | | Chow groups exist but no cycle class map to étale cohomology |
| 1.7 | Étale fundamental group $\pi_1^{\text{ét}}$ | ❌ **MISSING** | | | |
| 1.8 | Galois representations from étale cohomology | ❌ **MISSING** | `definition_compatible_system_of_representations_on_a_profinite_group_equipped_with_dense_frobenius_elements.tex` | | Related but not specifically étale cohomology → Galois reps |
| 1.9 | Weil conjectures (Deligne's proof) | ❌ **MISSING** | | | Statement only |
| 1.10 | $p$-adic étale cohomology (Fontaine's period rings) | 📝 **DEFINED** | `definition_absolute_p_nth_power_frobenius_endomorphism_of_a_ring_of_prime_characteristic.tex`, `definition_absolute_p_nth_power_frobenius_morphism_on_a_scheme.tex`, `definition_frobenius_action_on_compactly_supported_cohomology_with_torsion_coefficients.tex`, `definition_frobenius_action_on_compactly_supported_lambda_adic_cohomology_with_algebraic_coefficients.tex`, `definition_frobenius_action_on_compactly_supported_lambda_adic_cohomology_with_integral_coefficients.tex`, `definition_frobenius_action_on_compactly_supported_lambda_adic_cohomology_with_rational_coefficients.tex`, `definition_geometric_frobenius_action_of_a_derived_object_on_a_scheme_of_characteristic_p_at_a_stalk.tex` | | Frobenius actions exist; $B_{\text{dR}}, B_{\text{cris}}, B_{\text{st}}$ ❌ MISSING |

---

## Phase 2: Crystalline Cohomology

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 2.1 | **Crystalline site** $\text{Crys}(X/S)$ (PD-thickenings, divided power structures) | ❌ **MISSING** | | | Core foundation — Berthelot |
| 2.2 | **Crystal** $\mathcal{E}$ on crystalline site (coherent sheaf + integrable connection) | ❌ **MISSING** | | | "Crystal = sheaf with connection" |
| 2.3 | **Crystalline cohomology** $H^i_{\text{crys}}(X/S, \mathcal{E})$ | ❌ **MISSING** | | | Derived functor on crystalline site |
| 2.4 | **Divided power envelope** $\mathfrak{D}_\gamma(I)$ | ❌ **MISSING** | | | For closed immersions |
| 2.5 | **Berthelot's theorem**: comparison with de Rham (liftable case) | ❌ **MISSING** | | | $H^i_{\text{crys}}(X/W) \otimes_W K \cong H^i_{\text{dR}}(X_K/K)$ |
| 2.6 | **Mazur's theorem**: comparison with étale (Fontaine-Messing) | ❌ **MISSING** | | | $H^i_{\text{crys}} \otimes B_{\text{cris}} \cong H^i_{\text{ét}} \otimes B_{\text{cris}}$ |
| 2.7 | **Convergent cohomology** (overconvergent site, rigid cohomology) | ❌ **MISSING** | | | Berthelot, for non-proper varieties |
| 2.8 | **Frobenius action** on crystalline cohomology | ❌ **MISSING** | | | $F$-isocrystals, Dieudonné theory |
| 2.9 | **Hodge-Witt decomposition** (Illusie) | ❌ **MISSING** | | | $H^i_{\text{crys}} \otimes k \cong \bigoplus H^{j}(X, W\Omega^{i-j}_X)$ |
| 2.10 | **Crystalline Dieudonné module** (for $p$-divisible groups) | ❌ **MISSING** | | | Classification of $p$-divisible groups |

---

## Phase 3: de Rham Cohomology (Algebraic)

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 3.1 | **Algebraic de Rham complex** $\Omega^\bullet_{X/S}$ | ❌ **MISSING** | | | $\mathcal{O}_X \to \Omega^1_{X/S} \to \Omega^2_{X/S} \to \cdots$ |
| 3.2 | **Algebraic de Rham cohomology** $H^i_{\text{dR}}(X/S) = \mathbb{H}^i(X, \Omega^\bullet_{X/S})$ | ❌ **MISSING** | | | Hypercohomology of de Rham complex |
| 3.3 | **Hodge filtration** $F^p H^i_{\text{dR}} = \operatorname{im}(\mathbb{H}^i(X, \Omega^{\geq p}) \to \mathbb{H}^i(X, \Omega^\bullet))$ | 📝 **DEFINED** | `definition_hodge_filtration_on_a_hodge_structure.tex`, `definition_hodge_filtration_on_a_free_abelian_group_of_finite_rank_hodge_filtration_associated_to_a_hodge_structure.tex` | `definition_hodge_components_of_classical_hodge_structure_on_integral_cohomology_of_complex_algebraic_variety.tex` | For Hodge structures, not algebraic de Rham |
| 3.4 | **Gauss-Manin connection** on $H^i_{\text{dR}}(X/S)$ | 📝 **DEFINED** | `definition_connection_on_a_quasi_coherent_O_X_module_on_a_scheme.tex`, `definition_connection_on_a_quasi_coherent_O_X_module_on_a_relative_scheme.tex` | | Connections exist; Gauss-Manin specifically ❌ MISSING |
| 3.5 | **Katz-Oda theorem**: comparison with singular cohomology (over $\mathbb{C}$) | ❌ **MISSING** | | | $H^i_{\text{dR}}(X/\mathbb{C}) \cong H^i_{\text{sing}}(X^{\text{an}}, \mathbb{C})$ |
| 3.6 | **$p$-adic de Rham cohomology** (Fontaine's $B_{\text{dR}}$) | ❌ **MISSING** | | | $H^i_{\text{dR}} \otimes B_{\text{dR}} \cong H^i_{\text{ét}} \otimes B_{\text{dR}}$ |
| 3.7 | **Hodge-de Rham spectral sequence** $E_1^{p,q} = H^q(X, \Omega^p) \Rightarrow H^{p+q}_{\text{dR}}$ | ❌ **MISSING** | | | Degeneration in char 0 (Deligne-Illusie) |
| 3.8 | **Relative de Rham cohomology** for families | ❌ **MISSING** | | | |

---

## Phase 4: Other $p$-adic Cohomology Theories

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 4.1 | **Rigid cohomology** (Berthelot) — overconvergent isocrystals | ❌ **MISSING** | | | For non-proper / non-smooth varieties |
| 4.2 | **Log crystalline cohomology** (Kato, Hyodo-Kato) | ❌ **MISSING** | | | Semistable reduction |
| 4.3 | **Syntomic cohomology** (Fontaine-Messing, Nizioł) | ❌ **MISSING** | `definition_syntomic_morphism_of_schemes.tex` | `proposition_syntomic_morphism_of_schemes_stable_under_base_change_and_composition.tex` | Syntomic *morphisms* exist; syntomic *cohomology* ❌ MISSING |
| 4.4 | **Prismatic cohomology** (Bhatt-Scholze) | ❌ **MISSING** | | | Unifying theory: $\Delta$-rings, $\mathrm{Prism}_X$ |
| 4.5 | **$A_{\text{inf}}$-cohomology** (Bhatt-Lurie) | ❌ **MISSING** | | | $A_{\inf} = W(\mathcal{O}_C^\flat)$ |
| 4.6 | **Topological Hochschild homology (THH)** | ❌ **MISSING** | | | $\mathrm{THH}(A)$ relates to prismatic |
| 4.7 | **$p$-adic Hodge theory comparison isomorphisms** | ❌ **MISSING** | | | $H_{\text{ét}} \otimes B_{\text{dR}} \cong H_{\text{dR}} \otimes B_{\text{dR}}$, etc. |
| 4.8 | **Fargues-Fontaine curve** $X_{C,E}$ | ❌ **MISSING** | | | Geometric Fargues-Fontaine |

---

## Phase 5: Hodge Theory & Complex Geometry Bridge

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 5.1 | **Hodge decomposition** $H^k(X^{\text{an}}, \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}$ | 📝 **DEFINED** | `definition_hodge_components_of_classical_hodge_structure_on_integral_cohomology_of_complex_algebraic_variety.tex`, `definition_hodge_filtration_on_a_hodge_structure.tex`, `definition_hodge_filtration_on_a_free_abelian_group_of_finite_rank_hodge_filtration_associated_to_a_hodge_structure.tex` | | For classical Hodge structures |
| 5.2 | **Mixed Hodge structure** (Deligne) | ❌ **MISSING** | | | For singular / non-compact varieties |
| 5.3 | **Period domains** & period mappings | ❌ **MISSING** | | | |
| 5.4 | **Variation of Hodge structure** (Griffiths) | ❌ **MISSING** | | | |
| 5.5 | **Comparison: singular vs. de Rham vs. étale** | ❌ **MISSING** | | | Over $\mathbb{C}$: $H^i_{\text{sing}} \cong H^i_{\text{dR}} \cong H^i_{\text{ét}} \otimes \mathbb{Q}_\ell$ |

---

## Phase 6: Motivic & Intersection Cohomology

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 6.1 | **Chow groups** $\mathrm{CH}^i(X)$, cycle class maps | ✅ **ACTIVE** | `definition_k_dimensional_algebraic_cycles_of_a_noetherian_scheme.tex`, `definition_rationally_equivalent_k_dimensional_algebraic_cycles_of_a_noetherian_scheme.tex`, `definition_kth_chow_group_chow_group_of_codimension_p_of_a_noetherian_scheme.tex`, `definition_operational_chow_ring_of_a_noetherian_scheme.tex`, `definition_chow_ring_of_smooth_variety_over_a_field.tex`, `definition_relative_chow_groups_of_a_finite_type_scheme_over_a_noetherian_base.tex`, `definition_relative_operational_chow_ring_of_a_finite_type_scheme_over_a_noetherian_base.tex`, `definition_relative_chow_ring_of_a_smooth_projective_scheme_over_a_noetherian_base.tex`, `definition_category_of_relative_chow_motives_over_a_noetherian_base_and_coefficients_in_a_commutative_ring.tex`, `definition_relative_chow_motive_over_a_noetherian_base_and_commutative_ring_of_coefficients.tex`, `definition_tate_chow_motive_over_a_scheme.tex`, `definition_tate_twist_of_a_relative_chow_motive_over_a_noetherian_base_and_commutative_ring.tex`, `definition_composition_of_corrs_of_relative_chow_motives_over_a_noetherian_base_with_coefficients_in_a_comm_ring.tex`, `definition_morphism_of_relative_chow_motives_over_a_noetherian_base_and_coefficients_in_a_commutative_ring.tex`, `definition_ideal_of_endomorphisms_for_a_chow_motive_over_a_field_with_coefficients_in_a_commutative_ring.tex`, `definition_rost_nilpotence_for_a_chow_motive_over_a_field_with_coefficients_in_a_commutative_ring.tex` | | Comprehensive; wired in §"Intersection theory" |
| 6.2 | **Motivic cohomology** $H^{p,q}_{\mathcal{M}}(X, \mathbb{Z})$ | 📝 **DEFINED** | `definition_category_of_relative_chow_motives_over_a_noetherian_base_and_coefficients_in_a_commutative_ring.tex`, related Chow motive definitions | | Chow motives exist; motivic cohomology (Bloch's higher Chow groups) ❌ MISSING |
| 6.3 | **Intersection cohomology** $IH^*(X)$ (Goresky-MacPherson) | ❌ **MISSING** | | | Perverse sheaves |
| 6.4 | **Decomposition theorem** (Beilinson-Bernstein-Deligne-Gabber) | ❌ **MISSING** | | | For proper maps |
| 6.5 | **Weil cohomology theories** (axiomatic) | ❌ **MISSING** | | | Kleiman's axioms |

---

## Phase 7: Coherent Sheaf Cohomology & Classical Results

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 7.1 | **Coherent cohomology** $H^i(X, \mathcal{F})$ for $\mathcal{F} \in \mathrm{Coh}(X)$ | ✅ **ACTIVE** | `definition_sheaf_cohomology_group_of_a_sheaf_of_modules_over_a_sheaf_of_rings_on_a_site.tex`, `definition_euler_characteristic_of_a_coherent_sheaf_on_a_proper_scheme_over_a_field.tex` | `theorem_classical_riemann_roch_for_a_curve_over_a_field.tex`, `theorem_relative_riemann_roch_for_a_family_of_curves.tex`, `theorem_geometric_and_arithmetic_genera_of_nice_curves_are_equal.tex` | Wired in §"Cohomology of quasi-coherent sheaves on schemes" |
| 7.2 | **Serre duality** $\mathrm{Ext}^i(\mathcal{F}, \omega_X)^\vee \cong H^{n-i}(X, \mathcal{F})$ | ❌ **MISSING** | | | $\omega_X$ dualizing sheaf |
| 7.3 | **Grothendieck duality** $f^!$, trace map | 📝 **DEFINED** | `definition_dualizing_complex_for_verdier_duality_in_the_bdd_constr_derived_category_of_adic_sheaves_with_algebraic_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_dualizing_complex_for_verdier_duality_in_the_bdd_constr_derived_category_of_adic_sheaves_with_integral_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_dualizing_complex_for_verdier_duality_in_the_bdd_constr_derived_category_of_adic_sheaves_with_rational_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_dualizing_complex_for_verdier_duality_in_the_bounded_below_derived_category_of_etale_sheaves_with_torsion_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_verdier_dual_of_an_object_in_the_bdd_constr_derived_category_of_adic_sheaves_with_algebraic_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_verdier_dual_of_an_object_in_the_bdd_constr_derived_category_of_adic_sheaves_with_integral_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_verdier_dual_of_an_object_in_the_bdd_constr_derived_category_of_adic_sheaves_with_rational_coefficients_on_a_finite_type_scheme_over_a_noetherian_scheme.tex`, `definition_exceptional_inverse_image_functor_on_bdd_const_derived_category_of_adic_sheaves_with_algebraic_coefficients_on_schemes_of_finite_type_over_a_a_noetherian_scheme_via_a_compactifiable_morphism.tex`, `definition_exceptional_inverse_image_functor_on_bdd_const_derived_category_of_adic_sheaves_with_integral_coefficients_on_schemes_of_finite_type_over_a_a_noetherian_scheme_via_a_compactifiable_morphism.tex`, `definition_exceptional_inverse_image_functor_on_bdd_const_derived_category_of_adic_sheaves_with_rational_coefficients_on_schemes_of_finite_type_over_a_a_noetherian_scheme_via_a_compactifiable_morphism.tex`, `definition_exceptional_inverse_image_functor_on_the_bounded_below_derived_categories_of_etale_sheaves_with_torsion_coefficients_on_schemes_of_finite_type_over_a_noetherian_scheme_via_a_compactifiable_morphism.tex` | `theorem_derived_direct_image_with_proper_support_independent_of_compactification_up_to_canonical_isomorphism.tex` | Verdier duality for adic/constructible sheaves; $f^!$ for coherent ❌ MISSING |
| 7.4 | **Riemann-Roch** (Grothendieck-Hirzebruch-Riemann-Roch) | ✅ **ACTIVE** | `definition_euler_characteristic_of_a_coherent_sheaf_on_a_proper_scheme_over_a_field.tex`, `definition_arithmetic_genus_of_a_proper_scheme_over_a_field.tex`, `definition_geometric_genus_of_a_smooth_projective_variety_over_a_field.tex` | `theorem_classical_riemann_roch_for_a_curve_over_a_field.tex`, `theorem_relative_riemann_roch_for_a_family_of_curves.tex`, `theorem_geometric_and_arithmetic_genera_of_nice_curves_are_equal.tex` | Classical for curves; GRR for higher dim ❌ MISSING |
| 7.5 | **Hilbert polynomial**, Castelnuovo-Mumford regularity | ❌ **MISSING** | | | |
| 7.6 | **Formal functions theorem**, Grothendieck's existence theorem | ❌ **MISSING** | | | |

---

## Phase 8: Specialized / Advanced Topics

| # | Topic | Status | Definition File(s) | Concept File(s) | Notes |
|---|-------|--------|-------------------|-----------------|-------|
| 8.1 | **$p$-adic Simpson correspondence** (Faltings, Diao-Lan-Liu-Zhu) | ❌ **MISSING** | | | Higgs bundles $\leftrightarrow$ local systems |
| 8.2 | **Geometric Langlands** (coherent sheaves on $\mathrm{Bun}_G$) | ❌ **MISSING** | | | Link to `Langlands` vault |
| 8.3 | **Derived algebraic geometry** (spectral schemes, derived stacks) | ❌ **MISSING** | `definition_artin_stack_over_a_scheme_for_a_grothendieck_topology_on_the_category_of_S_schemes.tex` | | Artin stacks exist; derived/spectral ❌ MISSING |
| 8.4 | **Categorical trace / Hochschild homology** | ❌ **MISSING** | | | |
| 8.5 | **Factorization homology** (Beilinson-Drinfeld) | ❌ **MISSING** | | | Link to `QuantumFieldTheory` |

---

## Cross-Reference with Other Vaults

| Vault | Relevant Content | Status |
|-------|-----------------|--------|
| **AlgebraicNumberTheory** | Galois representations, $p$-adic Hodge theory, Fontaine's rings | Check `definition_galois_representation_*`; Fontaine's rings ❌ MISSING here |
| **Langlands** | Geometric Langlands, automorphic forms, Shimura varieties | |
| **Topology** | Sheaf cohomology, derived functors, spectral sequences, $E_\infty$-rings | |
| **QuantumFieldTheory** | Factorization algebras, topological field theories, extended TFT | |
| **Manifolds** | Hodge theory, de Rham cohomology of manifolds, period mappings | |
| **RepresentationTheory** | Langlands parameters, $L$-groups, $p$-adic groups | |

---

## Immediate Next Steps (Priority Order)

1. **Crystalline site & crystals** (Phase 2.1–2.3) — foundation for all $p$-adic cohomology
2. **Divided power structures & envelopes** (Phase 2.4) — technical prerequisite
3. **Algebraic de Rham complex & cohomology** (Phase 3.1–3.2) — parallel foundation
4. **Hodge filtration & Hodge-de Rham spectral sequence** (Phase 3.3, 3.7)
5. **Comparison theorems** (Phase 2.5, 3.5, 4.7) — the "why we care" part
6. **Prismatic cohomology** (Phase 4.4) — modern unifying framework
7. **Syntomic / $A_{\text{inf}}$** (Phase 4.3, 4.5) — for Fontaine's period rings
8. **Fontaine's period rings** $B_{\text{dR}}, B_{\text{cris}}, B_{\text{st}}$ (Phase 1.10, 3.6, 4.7)
9. **Étale Poincaré duality & trace map** (Phase 1.5)
10. **Serre duality & Grothendieck duality for coherent sheaves** (Phase 7.2, 7.3)
11. **GRR for higher-dimensional schemes** (Phase 7.4)
12. **Cycle class map to étale cohomology** (Phase 1.6)

---

## Notes for Writing

- **Prismatic cohomology** is the modern "master theory" (Bhatt-Scholze 2019) — everything else (crystalline, de Rham, étale, Hodge) recovers from it via base change along $\Delta \to A_{\text{inf}} \to B_{\text{dR}}, B_{\text{cris}}, \dots$
- **Crystalline cohomology** requires: PD-rings, PD-envelopes, crystalline site, crystals (= coherent sheaves with integrable connection satisfying Griffiths transversality)
- **de Rham cohomology** in algebraic geometry = hypercohomology of the algebraic de Rham complex; Hodge filtration comes from the stupid filtration $\sigma_{\geq p} \Omega^\bullet$
- **Fontaine's period rings**: $B_{\text{dR}}$ (de Rham), $B_{\text{cris}}$ (crystalline), $B_{\text{st}}$ (semistable) — all are $\Delta$-rings or prismatic
- **All comparison isomorphisms** are Galois-equivariant and compatible with filtrations / Frobenius