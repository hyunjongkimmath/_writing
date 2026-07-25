# Algebraic Groups Assessment

**Date:** 2026-07-23
**Purpose:** Inventory what exists, what is needed (especially Lie theory for Langlands), and what remains.

---

## 1. What Already Exists in AlgebraicGroups/content.tex

### Definitions already written (via `\input{}`)
| Section | Items |
|---------|-------|
| **Algebraic groups** | algebraic group scheme, subgroup scheme, homomorphism, GL_n, linear algebraic group |
| **Normal subgroups & quotients** | normal/characteristic subgroup scheme, identity component, finite-index subgroup, quotient, strongly connected, strong identity component |
| **Classical examples** | SL_n, O_n, SO_n, unitary groups, special unitary groups, G_m |
| **Structure theory** | unipotent elements/groups, unit upper triangular matrices, unipotent radical, reductive groups, Borel subgroups |
| **Representations** | GL(E) for locally free module, representation of affine group scheme, faithful representation |
| **Groupoids & Hopf** | groupoid, groupoid object, Hopf algebra, Hopf algebroid, affine groupoid scheme |
| **Appendix (misc.)** | schemes, categories, modules, functors, Grothendieck topologies, sheaves, affine space, etc. |

### Propositions/Lemmas already written
- Every algebraic group scheme over char 0 field is smooth
- Identity component G^0 is characteristic (hence normal)
- Finite-index subgroup iff dimensions coincide
- Dimension = dim(subgroup) + dim(quotient)
- Strong identity component = identity component for smooth groups
- Normal subgroup of reductive group is reductive
- Unipotent radical is characteristic subgroup
- Reps of reductive groups over char 0 are semisimple
- Borel subgroups conjugate (stated, no label)
- Maximal compact subgroups conjugate (stated, no label)
- Maximal tori conjugate (stated, no label)

### TODO markers in the content
1. Are all group schemes over char 0 reduced?
2. Are all subgroups of group schemes over char 0 closed?
3. Does identity-component-is-characteristic hold for more general groups G/S?
4. Check definition of unitary group
5. Define p-adic field
6. Define symplectic groups
7. Show why unipotent radical exists
8. Groupoid object (flesh out)

---

## 2. Lie Groups & Lie Algebras -- What Exists vs What Is Needed for Langlands

### Currently in the vault (sparse, AI-generated, marked TODO)
- `definition_lie_group_over_a_field.tex` -- basic definition of real/complex Lie group
- `definition_representation_of_a_lie_group_on_a_topological_vector_space.tex` -- finite-dim reps, mentions derived representation d\rho
- `definition_isotypic_component_of_a_representation_of_a_lie_group_over_a_field_for_an_irreducible_representation.tex`
- `definition_hermitian_symmetric_domain.tex` -- references semisimple Lie group, center of Lie group (labels may be missing)

**All four are marked `\TODO{AI generated, verify}` or have pending TODOs.**

### Critical gaps for Langlands-level work

#### 2A. Manifolds & Smooth Maps (prerequisites)
None of these definitions exist in the vault:
- [ ] Smooth manifolds (C^k manifolds, charts, atlases)
- [ ] Tangent spaces and tangent bundles
- [ ] Smooth maps between manifolds, diffeomorphisms
- [ ] Lie derivative / vector fields on manifolds

#### 2B. Lie Algebras (completely missing)
No definitions for any of these:
- [ ] **Lie algebra** over a field (vector space + bracket satisfying Jacobi + antisymmetry)
- [ ] **Lie algebra homomorphism**, ideals, quotients
- [ ] **Semisimple / solvable / nilpotent Lie algebras**
- [ ] **Cartan subalgebra** of a Lie algebra
- [ ] **Root system** (Φ ⊂ h*) and root spaces g_α
- [ ] **Weight lattice**, weight spaces in representations
- [ ] **Killing form** and Cartan's criterion for semisimplicity
- [ ] **Classification of finite-dimensional semisimple Lie algebras** (Dynkin diagrams, types A-D-E)
- [ ] **Real forms** of complex Lie algebras (compact real form, split real form)
- [ ] **Exponential map** exp: g → G and its properties

#### 2C. Lie Group Structure Theory (missing or incomplete)
- [ ] **Lie algebra of a Lie group** (tangent space at identity with bracket from left-invariant vector fields)
- [ ] Fundamental theorem: correspondence between Lie subalgebras and connected Lie subgroups
- [ ] **Covering groups**, simply connected Lie groups
- [ ] **Center of a Lie group** (label referenced by hermitian_symmetric_domain.tex but may not exist)
- [ ] **Semisimple Lie group** (not yet defined)
- [ ] **Adjoint representation** Ad: G → GL(g) and ad: g → gl(V)

#### 2D. Structure Theory of Reductive Groups over fields (partially present, needs deepening)
Already have: Borel subgroups, maximal tori conjugacy, reductive/unipotent definitions. **Still missing:**
- [ ] **Parabolic subgroups** and Levi decompositions P = L ⋉ U
- [ ] **Root datum** (X*, Φ, X, Φ∨) -- essential for Langlands dual groups
- [ ] **Weyl group** W = N_G(T)/T and its action
- [ ] **Based root datum** and L-groups (the core object of the Langlands program)
- [ ] **Satake isomorphism** for unramified Hecke algebras
- [ ] **Iwasawa decomposition** G = KAN
- [ ] **Cartan/Iwasawa decompositions** over local fields

#### 2E. Topological Groups (for adelic theory)
Already have: `definition_topological_group.tex`. Missing:
- [ ] **p-adic numbers Q_p and finite extensions** (called out as TODO in content.tex)
- [ ] **Local fields** -- definition, classification (R, C, R((t)), C((t)), p-adic fields, their completions)
- [ ] **Haar measure** on locally compact groups
- [ ] **Locally compact groups**, unimodularity, modular function
- [ ] **Restriction of scalars** (Weil restriction) -- for transferring algebraic groups between fields

---

## 3. What AutomorphicForms/content.tex Needs from AlgebraicGroups

Reading the AutomorphicForms file, these concepts are invoked but not yet formally defined in the vault:

| Used in AutomorphicForms | Status |
|--------------------------|--------|
| Adeles, ideles of global fields | Defined (`definition_adeles_and_ideles_of_a_global_field.tex`) |
| Adelic points of algebraic groups G(A_F) | Defined (`definition_group_of_adelic_points...`) |
| Automorphic forms on G(F)\G(A_F) | Defined but marked TODO for precision |
| Lie algebra g in "(g, K)-module" context (line 191) | **Not defined** -- only referenced informally |
| Maximal compact subgroup K | Mentioned in AlgebraicGroups but not formally defined as concept |
| Hecke operators / spherical Hecke algebra | Not defined |
| Smooth admissible representations | "K-finite" and "smooth" defined, but "admissible" missing |

---

## 4. Recommended Writing Order (Langlands-motivated)

To build toward Langlands-level content efficiently:

### Phase 1 -- Foundations (prerequisites for everything else)
1. Smooth manifolds, tangent spaces, smooth maps
2. Lie algebras over a field (definition, homomorphisms, ideals, quotients)
3. Lie algebra of a Lie group, exponential map
4. Solvable/nilpotent/semisimple Lie algebras

### Phase 2 -- Structure theory of semisimple Lie algebras
5. Cartan subalgebras, root space decomposition
6. Root systems (axioms, Weyl groups, Dynkin diagrams)
7. Classification of complex semisimple Lie algebras
8. Real forms, compact real forms

### Phase 3 -- Reductive algebraic groups + arithmetic structure
9. Parabolic subgroups, Levi decompositions
10. Root datum, based root datum, Weyl group of G relative to T
11. Langlands dual group G^L
12. p-adic fields, local fields, Haar measure

### Phase 4 -- Bridge to Automorphic Forms
13. Iwasawa decomposition, Cartan decomposition over local fields
14. (g, K)-modules and Harish-Chandra modules
15. Satake isomorphism
16. Hermitian symmetric domains (clean up existing definition)

---

## 5. Quick Wins (definitions that are short but needed now)

These can be written immediately without deep prerequisites:
- [ ] `definition_lie_algebra_over_a_field.tex` -- one paragraph, pure algebra
- [ ] `definition_semisimple_lie_algebra.tex` -- via Killing form or derived series
- [ ] `definition_killing_form_of_a_lie_algebra.tex`
- [ ] `definition_cartan_subalgebra_of_a_lie_algebra.tex`
- [ ] `definition_root_space_decomposition.tex`
- [ ] `definition_symplectic_group_over_a_scheme.tex` -- called out as TODO in content.tex
- [ ] Fix the 8 existing TODO markers in AlgebraicGroups/content.tex
