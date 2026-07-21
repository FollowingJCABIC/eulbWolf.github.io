# Portfolio Modernization Audit

Status: **READY FOR HUMAN REVIEW — DRAFT PULL REQUESTS OPEN, NOTHING MERGED**  
Audit date: 2026-07-21  
Central portfolio PR: `FollowingJCABIC/eulbWolf.github.io#1`  
Canonical data-science PR: `FollowingJCABIC/project-viva-data-science-lab#1`

## 1. Executive summary

The portfolio has been reorganized around the three owner-confirmed projects:

1. Learning App Analytics
2. Mindstate Signal Lab
3. Tutoring Ops Analytics

The public site now gives those projects a coherent recruiter-facing narrative, while the private canonical repository provides executable source, tests, robustness analysis, regenerated evidence, and explicit claim boundaries.

The review materially changed the analytical work. It removed future-looking longitudinal feature leakage from Mindstate, removed full-dataset imputation leakage from Tutoring, corrected two temporal robustness splits, made Tutoring robustness choose the model supported by the current experiment table, added regression tests, constrained incompatible dependencies, and established a clean three-project CI workflow.

Final clean validation succeeded for all three labs in GitHub Actions run `29851652113`:

- Learning App Analytics: 20 tests passed
- Mindstate Signal Lab: 25 tests passed
- Tutoring Ops Analytics: 27 tests passed

The public site validator also succeeded after the final Mindstate evidence correction in GitHub Actions run `29851873152`.

No repository was merged, deployed to production, made public, relicensed, or force-pushed.

## 2. Verification language

- **VERIFIED** — directly inspected or successfully executed.
- **PARTIALLY VERIFIED** — important evidence was inspected, but an external or scope limitation remains.
- **BLOCKED** — a specific limitation prevented the check.
- **NOT RUN** — deliberately not attempted, with a reason.
- **FAILED, THEN FIXED** — the check ran, exposed a defect, and later passed after correction.

## 3. Repositories inspected

Thirty-three repositories were available to the connected GitHub account.

### Modified

| Repository | Visibility | Role | Review branch | Draft PR |
|---|---|---|---|---|
| `FollowingJCABIC/project-viva-data-science-lab` | Private | Canonical executable source for the three labs | `codex/portfolio-modernization-20260721` | `#1` |
| `FollowingJCABIC/eulbWolf.github.io` | Public | Central public portfolio | `codex/portfolio-modernization-20260721` | `#1` |

### Inspected but not modified

| Repository | Classification | Reason not modified |
|---|---|---|
| `FollowingJCABIC/mindstate-signal-lab` | Broader private research scaffold | Kept separate from the canonical executed Mindstate lab; its planned multimodal capabilities must not be blended with validated metrics. |
| `FollowingJCABIC/data` | Public legacy data-analysis archive | Historical exported HTML work; lower priority than the three confirmed projects and central site. |
| `FollowingJCABIC/ml-study-lab-web` | Private supporting application | Not one of the owner-confirmed primary projects. |
| `FollowingJCABIC/world-selector-web` | Private supporting application | Not one of the owner-confirmed primary projects. |
| `FollowingJCABIC/teacher-trainer-app` | Private education application | Secondary and outside the focused modernization. |
| `FollowingJCABIC/faith-quiz-fresh` | Private education application | Secondary and outside the focused modernization. |
| `FollowingJCABIC/nervbluem` | Private content/art platform | Unrelated to the data-science portfolio focus. |
| `FollowingJCABIC/math-explorer-platform` | Public mathematical software | Strong secondary work, but not one of the three confirmed projects. |
| `FollowingJCABIC/Website-React-FBD` | Public application | Secondary engineering work. |
| `FollowingJCABIC/color-mixing-app` | Public application | Secondary engineering work. |
| `FollowingJCABIC/texas-holdem-lan` | Public application | Secondary engineering work. |
| `FollowingJCABIC/songwriter-app` | Public application | Secondary engineering work. |
| `FollowingJCABIC/crossword-creator` | Public application | Secondary engineering work. |
| `FollowingJCABIC/dictionary-thesaurus-translator` | Public application | Secondary engineering work. |
| `FollowingJCABIC/language-studio` | Public application | Secondary engineering work. |
| `FollowingJCABIC/news-stocks-python` | Public experimental research project | Interesting but not one of the three owner-confirmed core projects. |
| `FollowingJCABIC/ForkPoint` | Public empty repository | No portfolio evidence available. |

### Archived or superseded repositories

The following archived repositories were inventoried but excluded from modernization: `reactFML`, `myAppGitV`, `back_end_api_mongo`, `flask-restful-jinja2`, `youtube_video_code`, `react-flask-app`, `flask-react-spa`, `flask-react-boilerplate`, `minimal-react-webpack-babel-setup`, `jgcweb`, `jart`, `eulbWolf2.github.io`, `eulbwolf.github.io-art`, and `math-exploration-web`.

No repository named `FollowingJCABIC.github.io` was available. Repository evidence supports `eulbWolf.github.io` as the current central-site repository.

## 4. Git baseline and safety

| Repository | Default branch | Baseline commit | Working branch |
|---|---|---|---|
| Canonical labs | `main` | `2db1105ef2219fa08b6104cbd86e72537a60c9e3` | `codex/portfolio-modernization-20260721` |
| Central site | `main` | `bb05733a3cf31c894a3272ffe21287f1a65f44bc` | `codex/portfolio-modernization-20260721` |

- Dedicated non-default branches were used.
- No force-push or history rewrite was performed.
- No default branch was modified directly.
- No existing pull request was overwritten.
- Both resulting pull requests remain drafts.
- No license was added, removed, or changed.

## 5. Projects discovered and selected for featuring

### Learning App Analytics

- **Question:** Can synthetic practice interactions support cautious next-action classification?
- **Unit of observation:** one synthetic practice-problem interaction.
- **Target:** `advance`, `review`, or `hint_needed`.
- **Why featured:** clearest recruiter-facing problem, strongest rule-versus-model comparison, grouped holdout, calibration, diagnostics, slices, and a policy layer separate from prediction.

### Mindstate Signal Lab

- **Question:** Can ambiguous synthetic self-reflection patterns be modeled with uncertainty and explicit abstention without diagnostic claims?
- **Unit of observation:** one synthetic user-day.
- **Target:** four non-clinical signal classes plus abstention.
- **Why featured:** most differentiated responsible-modeling project; demonstrates causal longitudinal features, grouped-user evaluation, chronological review, coverage-aware abstention, and strong safety boundaries.

### Tutoring Ops Analytics

- **Question:** Can synthetic tutoring-session records support progress and session-risk review?
- **Unit of observation:** one synthetic tutoring session.
- **Targets:** `progress_label` and secondary `no_show_risk_label`.
- **Why featured:** strongest operations-analytics case; demonstrates related-target separation, simple-model competitiveness, human review, and cautious operational interpretation.

## 6. Original scores

Scale: 0 absent or misleading; 1 major deficiencies; 2 substantial gaps; 3 competent; 4 strong; 5 exceptional and thoroughly validated.

| Project | Hiring | Analytical rigor | Statistical validity | Technical depth | Reproducibility | Code quality | Visual communication | Written communication | Completeness | Interview defensibility |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Learning App Analytics | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 |
| Mindstate Signal Lab | 4 | 3 | 2 | 4 | 3 | 3 | 3 | 4 | 3 | 4 |
| Tutoring Ops Analytics | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 |
| Central public presentation | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 1 |

## 7. Major baseline problems

### Central site

- Older static homepage did not feature the three current projects.
- Primary navigation included obsolete, placeholder, or weakly supported links.
- The coding page linked to the obsolete username `jgcblue` and contained a literal `PLACEHOLDER` link.
- The contact form posted to PHP despite static GitHub Pages hosting.
- The contact experience loaded tracking and used distracting animation.
- Fixed spacing and tiny controls created narrow-screen and keyboard-use risks.
- There was no central project map, structured case-study system, validator, CI workflow, README, or durable `AGENTS.md`.

### Canonical labs

- No repository-level clean validation workflow covered all three projects.
- Dependencies were too loosely bounded; scikit-learn 1.8 broke the current code path.
- Mindstate used `ffill().bfill()` before splitting, allowing later observations to influence earlier user-days.
- Mindstate’s previous temporal robustness cut could split a shared time index across partitions.
- Tutoring computed full-frame medians before splitting for engineered interactions.
- Tutoring’s previous temporal robustness cut could split a date index across partitions.
- Tutoring robustness hard-coded a random forest even when the current experiment table favored logistic regression.
- Some integration tests encoded stale model assumptions.
- Generated artifact snapshots could drift from source after analytical corrections.

## 8. Changes implemented

### Canonical repository

- Added root `AGENTS.md` and clarified the canonical-source relationship with the separate Mindstate scaffold.
- Added `.github/workflows/portfolio-labs.yml` to install and execute all three labs independently.
- Added unit and full-suite stages plus uploaded command logs and regenerated evidence.
- Bounded shared dependency families to compatible major versions.
- Completed and standardized all three `REPRODUCIBILITY.md` guides.
- Added `VALIDATION_ARTIFACTS.md` with the final commands, versions, metrics, test counts, corrections, and artifact-freshness warning.
- Updated the three-project map and employer-facing case studies with validated evidence and limitations.

### Public site

- Rebuilt the homepage around the three confirmed projects.
- Added a reviewer map and one structured case-study page per project.
- Added status labels, source-visibility disclosure, and synthetic-data claim boundaries.
- Replaced the obsolete coding page with a restrained secondary-software map.
- Replaced the nonfunctional PHP form with a verified GitHub contact route.
- Removed tracking from the modern contact path.
- Added semantic landmarks, skip links, visible focus states, reduced-motion support, responsive layouts, and a useful 404 page.
- Added reusable `portfolio.css` and `case-study.css`.
- Added `README.md`, `AGENTS.md`, `robots.txt`, favicon, static validation, and pull-request CI.
- Preserved older files rather than deleting historical work.

## 9. Data-quality and data-science validity fixes

### Mindstate

1. Removed backward fill from longitudinal features.
2. Removed full-frame fallback statistics from pre-split feature construction.
3. Left unresolved leading missing values for the training-fitted model pipeline.
4. Added regression tests proving a later user-day cannot alter earlier engineered features.
5. Changed the temporal proxy to hold out complete later `day_index` values across users.
6. Added tests proving no time index appears in both temporal partitions.
7. Reframed abstention evidence so coverage, retained accuracy, and retained macro F1 are reported together.

### Tutoring

1. Removed full-frame engagement and confidence medians from feature building.
2. Preserved missing values for the training-fitted pipeline imputer.
3. Added tests proving appended held-out extremes cannot alter earlier engineered rows.
4. Changed the temporal proxy to hold out complete later `date_index` values.
5. Added tests proving no date index appears in both temporal partitions.
6. Made robustness analysis select the strongest supported current model from `model_metrics.csv`.
7. Updated integration tests so they validate current experiment evidence rather than a hard-coded model name.

### Learning

- Preserved grouped-student outer evaluation, calibration reporting, transparent-rule comparison, class/slice diagnostics, and temporal-proxy review.
- Documented the remaining limitation that inner calibration folds are not yet group-aware.

## 10. Final validated evidence

Final execution: GitHub Actions run `29851652113`, conclusion **success**.

### Learning App Analytics

- Rows generated: 5,200
- Best current model: calibrated engineered random forest
- Grouped test accuracy: **0.760**
- Grouped test macro F1: **0.759**
- Expected calibration error: **0.032**
- Transparent rule macro F1 on the same grouped test frame: **0.415**
- Robustness macro F1:
  - random row: **0.750**
  - grouped student: **0.740**
  - temporal session-order proxy: **0.734**
- Complete suite: **20 passed**

### Mindstate Signal Lab

- Rows generated: 6,240
- Best full-coverage model: engineered random forest
- Grouped test accuracy: **0.478**
- Grouped test macro F1: **0.475**
- Expected calibration error: **0.042**
- Transparent rule macro F1: **0.257**
- Robustness macro F1:
  - random row: **0.481**
  - grouped user: **0.481**
  - chronological shared-day proxy: **0.462**
- Fixed-threshold abstention:
  - coverage: **21.8%**
  - retained accuracy: **71.2%**
  - retained macro F1: **0.392**
- Complete suite: **25 passed**

### Tutoring Ops Analytics

- Rows generated: 5,600
- Best progress model: base logistic regression
- Grouped test accuracy: **0.603**
- Grouped test macro F1: **0.608**
- Expected calibration error: **0.041**
- Transparent rule macro F1: **0.549**
- Robustness macro F1:
  - random row: **0.635**
  - grouped student: **0.648**
  - chronological date-index proxy: **0.616**
- Secondary no-show-risk random-forest macro F1: **0.575**
- Complete suite: **27 passed**

These are synthetic benchmark results. They establish an internally reproducible workflow, not real learner outcomes, clinical meaning, tutoring impact, causality, business lift, production readiness, or deployment success.

## 11. Notebook reproducibility

The canonical execution path is script-first, not notebook-first. No notebook is presented as the source of the validated evidence. The three project paths are regenerated with Python scripts and pytest. Notebook-specific validation was therefore **NOT RUN because notebooks are not the canonical deliverable**.

## 12. Website, UX, accessibility, and responsive design

### Verified improvements

- One clear `h1` and one `main` landmark on each modern route.
- Skip link is the first keyboard focus target.
- Visible `:focus-visible` treatment.
- Semantic navigation and current-page indication.
- No JavaScript dependency for primary content.
- `prefers-reduced-motion` handling.
- Mobile card stacking and readable line lengths.
- No horizontal overflow on the reviewed routes.
- No tracking, autoplay, or nonfunctional form on the modern path.

### Rendered review

The modern route set was rendered with headless Chromium at approximately:

- 390 × 844
- 768 × 1024
- 1440 × 900

No reviewed route produced horizontal scrolling. The homepage and project case studies remained readable at mobile, tablet, and desktop widths.

This is a practical accessibility review, not a claim of complete WCAG conformance.

## 13. Code-quality and documentation improvements

- Added deterministic regression tests around leakage and split boundaries.
- Added evidence-driven model selection in robustness analysis.
- Added dependency compatibility bounds.
- Added CI failure artifacts and explicit failure gates.
- Added root maintenance guidance in both repositories.
- Replaced machine- or context-dependent documentation with project-relative commands.
- Added current project status, source visibility, claim boundaries, validation evidence, and remaining limitations.
- Kept generated-artifact freshness separate from source-code validation.

## 14. Metadata and deployment readiness

- Added page titles, descriptions, Open Graph summary metadata, theme color, favicon, robots policy, and a 404 page.
- Used relative URLs so a GitHub Pages project-path deployment remains possible.
- Added static validation CI.
- Did not add analytics, cookies, advertising, or tracking.

### Deployment status

- Local and CI static validation: **VERIFIED**
- Public GitHub Pages URL and repository-setting source: **BLOCKED — not confirmed through the available connector**
- Production deployment: **NOT RUN — not authorized**

## 15. Adversarial review findings and corrective work

| Finding | Severity | Resolution |
|---|---|---|
| Future-looking Mindstate backward fill | Critical | Removed; causal feature tests added |
| Full-frame Tutoring median imputation | High | Removed; held-out-row regression tests added |
| Row-order temporal cuts could share time/date indices | High | Replaced with complete unique-index holdouts; boundary tests added |
| Hard-coded Tutoring robustness model | High | Replaced with current-evidence selection |
| scikit-learn 1.8 incompatibility | High | Compatible bounds added and clean CI rerun |
| Integration assertion expected stale model | Medium | Test now derives expected model from current metrics |
| Exact floating-point equality in regression test | Medium | Replaced with numerical tolerance |
| Public Mindstate page retained older temporal/test figures | Medium | Corrected to 0.462 and 25 tests |
| Nonfunctional PHP contact form and tracking | High | Replaced with working, privacy-conscious contact route |
| Obsolete username and placeholder links | Medium | Removed from primary navigation path |
| Generated report snapshots can drift after source corrections | Medium | Added durable validation record and explicit regeneration warning |

## 16. Final scores

| Project | Hiring | Analytical rigor | Statistical validity | Technical depth | Reproducibility | Code quality | Visual communication | Written communication | Completeness | Interview defensibility |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Learning App Analytics | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 |
| Mindstate Signal Lab | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 |
| Tutoring Ops Analytics | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 |
| Central public presentation | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 |

Meaningful gains came from independently rerunnable evidence, corrected split and feature boundaries, explicit limitations, and a public narrative that accurately reflects the underlying work.

## 17. Exact validation commands and results

### Canonical repository

Each lab ran independently on Python 3.11:

```bash
python -m pip install -r requirements.txt
python scripts/run_pipeline.py
python scripts/run_experiments.py
python scripts/run_robustness.py
python scripts/build_report.py
python scripts/build_visual_summary.py
pytest tests/unit -q
pytest -q
```

| Project | Installation | Pipeline | Experiments | Robustness | Reports | Visual summary | Unit tests | Full tests |
|---|---|---|---|---|---|---|---|---|
| Learning | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 20 passed |
| Mindstate | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 25 passed |
| Tutoring | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 27 passed |

Final workflow: `Portfolio lab validation`, run `29851652113`, **success**.

### Central site

```bash
python3 scripts/validate_site.py
```

Result: eight modern HTML pages and required assets validated successfully.

Final corrected-content workflow: `Portfolio site checks`, run `29851873152`, **success**.

Rendered browser review: PASS at 390 × 844, 768 × 1024, and 1440 × 900.

### Failed checks that led to fixes

- Initial canonical clean run failed because unconstrained resolution installed scikit-learn 1.8 and exposed a removed API.
- A later Tutoring run failed because an integration test hard-coded the previously preferred model.
- A boundary-test run failed because an exact floating-point equality compared `0.10000000000000009` with `0.1`.

All three issues were corrected and the complete final workflow passed.

## 18. Checks not completed

| Check | Status | Reason |
|---|---|---|
| Public deployment smoke test | BLOCKED | Final Pages URL and deployment source were not confirmed through the available interface. |
| Production deployment | NOT RUN | Not authorized. |
| Public source-code inspection by an unauthenticated recruiter | BLOCKED | Canonical project repository remains private. |
| Full synchronization of every historical generated report artifact | PARTIALLY VERIFIED | CI regenerated them as temporary artifacts; a separate reviewed artifact-sync commit is still advisable. |
| Current résumé verification | BLOCKED | Owner confirmation required before promoting the existing PDF as current. |
| Professional email publication | BLOCKED | No owner-verified professional email was supplied. |
| Complete WCAG conformance audit | NOT RUN | Automated and practical manual checks do not prove full conformance. |

## 19. Files changed

### Canonical repository — 24 files

- `.github/workflows/portfolio-labs.yml`
- `AGENTS.md`
- `README.md`
- `THREE_PROJECT_PORTFOLIO_MAP.md`
- `VALIDATION_ARTIFACTS.md`
- all three `REPRODUCIBILITY.md` files
- all three `requirements.txt` files
- all three employer case studies
- Mindstate feature builder and robustness module
- Mindstate temporal-feature and temporal-split tests
- Tutoring feature builder and robustness module
- Tutoring imputation, model-selection, temporal-split, and integration tests

### Central site — 18 files

- `.github/workflows/site-checks.yml`
- `.gitignore`
- `404.html`
- `AGENTS.md`
- `PORTFOLIO_AUDIT.md`
- `README.md`
- `case-study.css`
- `coding.html`
- `contact.html`
- `favicon.svg`
- `index.html`
- `portfolio.css`
- `projects/index.html`
- three project case-study pages
- `robots.txt`
- `scripts/validate_site.py`

## 20. Commits, branches, and pull requests

### Canonical labs

- Branch: `codex/portfolio-modernization-20260721`
- Draft PR: `FollowingJCABIC/project-viva-data-science-lab#1`
- Review commits: 30
- Final reviewed branch commit before audit closure: `f219dd05c7d4d700256ba99d694781a7eff832de`

### Central site

- Branch: `codex/portfolio-modernization-20260721`
- Draft PR: `FollowingJCABIC/eulbWolf.github.io#1`
- Review commits after this audit update: 31

Recommended review order:

1. Canonical data-science PR
2. Central public-site PR

The public case studies depend on the canonical evidence and should be reviewed second.

## 21. Remaining limitations

- All datasets and labels are synthetic.
- Learning’s inner calibration folds are not group-aware.
- Mindstate’s abstention threshold is a fixed experimental choice on uncalibrated tree probabilities.
- Mindstate’s retained accuracy must be read with low coverage and retained macro F1.
- Tutoring targets are contemporaneous synthetic labels, not validated future forecasts.
- The canonical source repository is private.
- Some historical generated report snapshots may predate the final corrected pipeline; regenerate before quoting them.
- Public deployment has not been verified or performed.

## 22. Owner-verification items

1. Decide whether to make the canonical repository public or create a sanitized public mirror.
2. Confirm the intended GitHub Pages URL and deployment source.
3. Confirm whether `joseresumesite.pdf` is current.
4. Supply or approve a professional contact email if GitHub-only contact is insufficient.
5. Decide whether to commit the full regenerated artifact set after reviewing the large diff.
6. Review older legacy pages for personal contact details and archival policy.

## 23. Recommended next actions by impact

1. Review and merge the canonical PR after checking the generated workflow artifacts and synthetic-data boundaries.
2. Decide on a public-source strategy for the three labs.
3. Review and merge the central-site PR after the source-visibility decision is understood.
4. Confirm GitHub Pages settings and inspect the actual deployed URL at mobile, tablet, and desktop widths.
5. Make Learning’s inner calibration cross-validation group-aware.
6. Give Mindstate a validation-selected, calibrated abstention policy with explicit utility and coverage tradeoffs.
7. Add a dedicated generated-artifact synchronization policy or stop committing large generated outputs.
8. Verify the résumé and professional contact route.

## 24. Suggested pull-request titles

- Canonical: **Modernize and validate the three-project data science portfolio**
- Central site: **Rebuild the portfolio around three data science case studies**

## 25. Review readiness

| Branch | Ready for human review? | Notes |
|---|---|---|
| Canonical labs | **YES** | Full three-lab workflow green; analytical corrections and limitations documented; remains draft and private. |
| Central site | **YES** | Static validation and rendered responsive review passed; deployment and source-visibility decisions remain owner actions. |
| Complete modernization | **YES, for human review** | No merge or production deployment has been performed. |
