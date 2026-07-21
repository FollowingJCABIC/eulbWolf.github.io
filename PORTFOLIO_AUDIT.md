# Portfolio Modernization Audit

Status: **IN PROGRESS**  
Review branch: `codex/portfolio-modernization-20260721`  
Audit date: 2026-07-21

## Verification labels

- `VERIFIED`: directly inspected or successfully executed.
- `PARTIALLY VERIFIED`: important evidence was inspected, but an execution or access limitation remains.
- `BLOCKED`: a specific external limitation prevented verification.
- `NOT RUN`: not yet attempted.
- `FAILED`: attempted and failed.

## Scope actually inspected

| Repository | Visibility | Classification | Baseline ref | Modification scope |
|---|---:|---|---|---|
| `FollowingJCABIC/eulbWolf.github.io` | Public | Likely central portfolio; current implementation is an older static site | `main` at `bb05733a3cf31c894a3272ffe21287f1a65f44bc` | Central information architecture, project presentation, accessibility, responsive design, metadata, and documentation |
| `FollowingJCABIC/project-viva-data-science-lab` | Private | Canonical executable collection for the three core data-science labs | `main` at `2db1105ef2219fa08b6104cbd86e72537a60c9e3` | Analytical validity, reproducibility, tests, case studies, claim boundaries, and durable instructions |
| `FollowingJCABIC/mindstate-signal-lab` | Private | Supporting research scaffold and possible future extension of the canonical Mindstate lab | `main` at `dc58d6fb0d6332204ed49f40e530aff11f5f95f5` | Read-only classification unless evidence shows a required canonical-source correction |
| `FollowingJCABIC/data` | Public | Older or supporting data repository; current README is only `# data` | `main` | Shallow review only unless a core project depends on it |

No repository named `FollowingJCABIC.github.io` was available. The current evidence supports treating `eulbWolf.github.io` as the central portfolio repository for this pass.

## Git and workspace baseline

- Default branch for all three principal repositories: `main`.
- No open pull requests were found in either modified repository at baseline.
- No root `AGENTS.md` was found in the inspected repositories.
- Dedicated review branches were created:
  - `FollowingJCABIC/eulbWolf.github.io`: `codex/portfolio-modernization-20260721`
  - `FollowingJCABIC/project-viva-data-science-lab`: `codex/portfolio-modernization-20260721`
- No changes will be merged automatically.
- The execution container cannot resolve `github.com`, and the `gh` CLI is unavailable. Repository inspection and writes therefore use the connected GitHub API. Clean execution validation will be added to the review branch through GitHub Actions rather than inferred from committed artifacts.

## Portfolio architecture baseline

### Central site

`VERIFIED` from source inspection:

- The homepage uses older static HTML, Bootstrap 5, inline styles, MathJax, and decorative interaction code.
- It does not mention the three current data-science labs.
- It links to the obsolete GitHub username `jgcblue` in `coding.html`.
- `coding.html` contains a literal `PLACEHOLDER` link.
- The homepage links to `http://data.redbeginning.online` rather than a secure, locally integrated data-science portfolio route.
- The current site uses fixed padding and very small controls that are unlikely to work well on narrow screens.
- Navigation, headings, calls to action, metadata, project cards, and accessibility need substantial modernization.

### Core project collection

`VERIFIED` from source, reports, tables, and documentation:

- The consolidated private repository intentionally contains three executable synthetic-data labs.
- Each lab provides scripts, tests, generated tables, figures, model cards, final reports, employer case studies, and claim boundaries.
- The projects use ordinary Python dependencies: pandas, NumPy, scikit-learn, matplotlib, and pytest.
- The documented execution path does not require credentials, external data, a database, a notebook server, or a paid service.
- The latest commits add visual-summary command wrappers and tests for all three labs.

## Core-project inventory

### 1. Learning App Analytics

| Field | Baseline |
|---|---|
| Status | Substantially complete; execution not yet independently rerun |
| Location | `project-viva-data-science-lab/data-science-lab/learning-app-analytics` |
| Main question | Can synthetic practice-session behavior support classification of `advance`, `review`, or `hint_needed`? |
| Unit of observation | One synthetic practice-problem interaction |
| Dataset | Generated synthetic learner-session data; 5,200 rows in current configuration |
| Main target | `outcome_label` |
| Main deliverables | Reproducible scripts, tests, reports, visual summary, metrics tables, model card, rule-policy comparison, robustness checks, error analysis |
| Current best reported main model | `calibrated_random_forest_engineered` |
| Current reported grouped-test macro F1 | 0.758 |
| Transparent-rule macro F1 on same test frame | 0.415 |
| Robustness | Random-row, grouped-student, and temporal session-order proxy comparisons |
| Strongest evidence | Clear model-vs-rule comparison, grouped holdout, calibration discussion, diagnostic outputs, strong claim discipline |
| Primary weakness | Synthetic target reconstructs generator assumptions; calibration CV is not group-aware inside the training partition |
| Recommended position | Featured project 1; lead recruiter-facing case study |
| Priority | P1 |

### 2. Mindstate Signal Lab

| Field | Baseline |
|---|---|
| Status | Substantially complete synthetic lab, with a separate broader research scaffold |
| Canonical executable location | `project-viva-data-science-lab/data-science-lab/mindstate-signal-lab` |
| Supporting scaffold | `FollowingJCABIC/mindstate-signal-lab` |
| Main question | Can synthetic non-clinical user-state patterns be modeled with uncertainty and explicit abstention? |
| Unit of observation | One synthetic user-day |
| Dataset | Generated synthetic longitudinal self-reflection signals; 6,240 rows in current configuration |
| Main target | `label`: `steady`, `strained`, `recovering`, `uncertain` |
| Main deliverables | Reproducible scripts, tests, reports, visual summary, robustness checks, class/slice diagnostics, abstention outputs, policy layer, model cards |
| Current reported learned-model macro F1 | 0.483 |
| Current reported abstention coverage | 0.224 |
| Current reported retained accuracy | 0.714 |
| Robustness | Random-row, grouped-user, and temporal day-order proxy comparisons |
| Strongest evidence | Explicit abstention, sensitive-domain language discipline, failure analysis, policy boundaries |
| P0 analytical issue | Feature generation applies `ffill().bfill()` within user timelines before splitting, allowing later observations to influence earlier rows and weakening temporal-robustness claims |
| Secondary analytical issue | Abstention currently uses uncalibrated random-forest probabilities with a fixed threshold whose validation rationale is not explicit |
| Recommended position | Featured project 2; differentiated responsible-modeling case study |
| Priority | P0/P1 |

### 3. Tutoring Ops Analytics

| Field | Baseline |
|---|---|
| Status | Substantially complete; execution not yet independently rerun |
| Location | `project-viva-data-science-lab/data-science-lab/tutoring-ops-analytics` |
| Main question | Can synthetic tutoring-session records support progress review, session-risk review, and planning support? |
| Unit of observation | One synthetic tutoring session record |
| Dataset | Generated synthetic tutoring operations data; 5,600 rows in current configuration |
| Main targets | `progress_label`; secondary `no_show_risk_label` |
| Main deliverables | Reproducible scripts, tests, reports, visual summary, main/secondary models, rule-policy comparison, robustness checks, error analysis, policy layer |
| Current best reported progress model | `logistic_regression_base` |
| Current reported progress macro F1 | 0.609 |
| Current reported no-show-risk macro F1 | 0.571 |
| Transparent-rule progress macro F1 | 0.549 |
| Robustness | Random-row, grouped-student, and temporal date-index proxy comparisons |
| Strongest evidence | Multiple related targets, simple-model competitiveness, human-review workflow, operations-facing interpretation |
| Primary weakness | Targets are contemporaneous synthetic labels derived from same-row signals; presentation must not imply validated future forecasting or business lift |
| Recommended position | Featured project 3; operations-analytics and human-in-the-loop case study |
| Priority | P1 |

## Original project scores

Scale: 0 absent/unusable, 1 major deficiencies, 2 substantial gaps, 3 competent, 4 strong, 5 exceptional and thoroughly validated.

| Project | Hiring relevance | Analytical rigor | Statistical validity | Technical depth | Reproducibility | Code quality | Visual communication | Written communication | Completeness | Interview defensibility |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Learning App Analytics | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 |
| Mindstate Signal Lab | 4 | 3 | 2 | 4 | 3 | 3 | 3 | 4 | 3 | 4 |
| Tutoring Ops Analytics | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 |
| Current central site | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 1 |

Scores are provisional until branch validation runs. Mindstate statistical validity is reduced because of temporal feature leakage. Central-site scores reflect the current public presentation, not the quality of the three labs.

## Featured-project selection

1. **Learning App Analytics** — strongest first-minute explanation and clearest learned-model versus transparent-rule comparison.
2. **Mindstate Signal Lab** — most differentiated project because it foregrounds uncertainty, abstention, sensitive-domain limitations, and human review.
3. **Tutoring Ops Analytics** — strongest operations-analytics story and useful evidence that simpler models can be preferable to more complex alternatives.

The three projects will remain the primary portfolio focus. Other repositories will not displace them merely because they are newer or more visually elaborate.

## Baseline validation record

| Repository | Check | Result | Evidence or blocker |
|---|---|---|---|
| `project-viva-data-science-lab` | README and execution-path inspection | VERIFIED | All three labs document setup, generation, experiments, robustness, report building, visual summaries, and pytest |
| `project-viva-data-science-lab` | Dependency-file inspection | VERIFIED | Each lab lists pandas, NumPy, scikit-learn, matplotlib, and pytest |
| `project-viva-data-science-lab` | Current generated metric-table inspection | VERIFIED | Model, rule-policy, and robustness tables were inspected for all three labs |
| `project-viva-data-science-lab` | Clean install and top-to-bottom execution | NOT RUN | Will be performed through branch CI because local GitHub checkout is unavailable |
| `project-viva-data-science-lab` | Current artifact freshness | PARTIALLY VERIFIED | Artifacts exist and recent commits add visual-summary tests; full regeneration still required |
| `eulbWolf.github.io` | Homepage and coding-page source inspection | VERIFIED | Outdated links, unsupported presentation, placeholder text, and narrow-screen risks identified |
| `eulbWolf.github.io` | Public deployment inspection | BLOCKED | Public deployment URL could not be established reliably from repository evidence in the current environment |
| `eulbWolf.github.io` | Responsive/browser baseline | NOT RUN | Will be performed against the modernized static subset and, if available, a branch preview |

## Prioritized implementation plan

### P0

- Remove future-looking backward fill from Mindstate feature generation.
- Add regression tests proving that changing a later observation cannot alter earlier engineered features.
- Make calibration folds group-aware when repeated-user or repeated-student groups are present.
- Ensure claims and robustness documentation reflect the corrected pipeline.
- Add branch CI that runs clean generation, experiments, robustness, report building, visual-summary building, and pytest for all three labs.

### P1

- Rebuild the central homepage around the three featured projects.
- Add concise, recruiter-readable case-study pages for each project.
- Add responsive navigation, visible focus states, semantic headings, skip navigation, status labels, and accessible project cards.
- Replace obsolete GitHub links and remove placeholder content from the primary path.
- Add truthful source-access status because the canonical repository is currently private.
- Add consistent metadata, Open Graph fields, canonical structure, a 404 page, sitemap, and robots configuration where justified.
- Update the project README/reproducibility command sequences so visual-summary generation is included consistently.
- Add concise durable `AGENTS.md` guidance after commands are validated.

### P2

- Clarify the standalone Mindstate scaffold as a research roadmap/supporting repository rather than the canonical executed case study.
- Review lower-priority legacy pages without deleting them.
- Recommend repository descriptions/topics and public-source strategy for owner action.

## Known constraints and owner decisions

- The canonical three-project repository is private. Recruiters cannot inspect source without access. The final report must recommend either a privacy-reviewed visibility change or a sanitized public mirror; this pass will not change repository visibility.
- Existing résumé, degree, employment, and biography claims will not be rewritten without direct evidence.
- No production deployment, merge, license change, or repository-visibility change is authorized.

## Next audit updates

This document will be updated after:

1. P0 analytical fixes
2. Central-site implementation
3. Initial branch CI
4. Browser/responsive/accessibility inspection
5. Independent adversarial review
6. Corrective changes
7. Final validation and scoring
