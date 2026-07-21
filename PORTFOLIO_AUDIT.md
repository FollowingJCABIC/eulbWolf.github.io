# Portfolio Modernization Audit

Status: **READY FOR HUMAN REVIEW**  
Audit date: 2026-07-21  
Review branch in each modified repository: `codex/portfolio-modernization-20260721`  
Nothing has been merged or intentionally deployed to production.

## 1. Executive summary

The modernization now centers the public portfolio on the three projects confirmed as the primary body of data-science work:

1. Learning App Analytics
2. Mindstate Signal Lab
3. Tutoring Ops Analytics

The public site was rebuilt around recruiter-readable case studies, evidence labels, limitations, responsive navigation, keyboard access, and a coherent reviewer path. The canonical private lab repository received analytical corrections, bounded dependencies, regression tests, durable instructions, and a matrix CI workflow that regenerates each project from synthetic source data through final reports and tests.

Two material data-science validity issues were fixed:

- Mindstate longitudinal features no longer use future observations to backfill earlier user-days.
- Tutoring feature engineering no longer derives missing-value replacements from the full frame before splitting.

A third correctness issue was fixed in Tutoring robustness analysis: the evaluation now selects the strongest supported model from the current experiment table instead of hard-coding a random forest that was not actually the best current model.

Final clean GitHub Actions validation succeeded for all three labs and for the public site. The site was rendered automatically across eight routes at mobile, tablet, and desktop widths, producing 24 successful browser combinations with no page-level horizontal overflow, missing primary landmarks, first-focus failures, or browser errors.

## 2. Verification labels

- `VERIFIED`: directly inspected or successfully executed.
- `PARTIALLY VERIFIED`: important evidence was inspected, but an execution or access limitation remains.
- `BLOCKED`: a specific external limitation prevented verification.
- `NOT RUN`: not attempted, with a stated reason.
- `FAILED`: attempted and failed; subsequent corrections are recorded separately.

## 3. Workspace and repository scope

Thirty-three repositories were accessible under `FollowingJCABIC`. All were inventoried at least by repository metadata. Portfolio-relevant repositories received deeper README, source, report, workflow, or deployment inspection.

### Deep inspection

| Repository | Visibility | Classification | Baseline | Final modification decision |
|---|---:|---|---|---|
| `FollowingJCABIC/eulbWolf.github.io` | Public | Central portfolio repository supported by current site evidence | `main` at `bb05733a3cf31c894a3272ffe21287f1a65f44bc` | Modified; draft PR #1 prepared |
| `FollowingJCABIC/project-viva-data-science-lab` | Private | Canonical executable source for the three core labs | `main` at `2db1105ef2219fa08b6104cbd86e72537a60c9e3` | Modified; draft PR #1 prepared |
| `FollowingJCABIC/mindstate-signal-lab` | Private | Broader research scaffold and possible future extension | `main` at `dc58d6fb0d6332204ed49f40e530aff11f5f95f5` | Read-only classification; not treated as the executed case-study source |
| `FollowingJCABIC/data` | Public | Historical exported data-analysis archive | `main`; README contained only `# data` | Preserved and excluded from this focused pass |

No repository named `FollowingJCABIC.github.io` was available. Repository evidence supports `eulbWolf.github.io` as the current central portfolio for this review.

### Secondary active repositories classified but not modified

Public: `color-mixing-app`, `crossword-creator`, `dictionary-thesaurus-translator`, `ForkPoint`, `language-studio`, `math-explorer-platform`, `news-stocks-python`, `songwriter-app`, `texas-holdem-lan`, and `Website-React-FBD`.

Private: `faith-quiz-fresh`, `ml-study-lab-web`, `nervbluem`, `teacher-trainer-app`, and `world-selector-web`.

These repositories were not allowed to displace the three user-confirmed core projects. They were excluded from modification because they were secondary, private supporting work, empty, unrelated to the data-science objective, or outside the highest-impact scope.

### Archived repositories classified but not modified

`back_end_api_mongo`, `eulbwolf.github.io-art`, `eulbWolf2.github.io`, `flask-react-boilerplate`, `flask-react-spa`, `flask-restful-jinja2`, `jart`, `jgcweb`, `math-exploration-web`, `minimal-react-webpack-babel-setup`, `myAppGitV`, `react-flask-app`, `reactFML`, and `youtube_video_code`.

## 4. Git and workspace baseline

- `VERIFIED`: default branch for both modified repositories is `main`.
- `VERIFIED`: no open pull request existed in either modified repository at baseline.
- `VERIFIED`: no root `AGENTS.md` existed in either modified repository at baseline.
- `VERIFIED`: dedicated non-default branches were created in both repositories.
- `VERIFIED`: one draft pull request was opened per modified repository.
- `VERIFIED`: neither pull request is merged.
- `VERIFIED`: no production deployment was intentionally initiated.
- `BLOCKED`: the task container could not resolve `github.com`, and the `gh` CLI was unavailable. Repository reads and writes therefore used the connected GitHub API; clean execution used GitHub Actions.
- `VERIFIED`: no pre-existing local uncommitted work was overwritten because no local checkout was used for modifications.

## 5. Original baseline problems

### Central portfolio

- Older static HTML did not present the three current data-science labs.
- The primary data-science navigation depended on `http://data.redbeginning.online` instead of an integrated secure case-study path.
- `coding.html` referenced the obsolete GitHub username `jgcblue` and contained a literal placeholder link.
- The contact page submitted to `send_email.php`, which is not functional on static GitHub Pages hosting.
- The modern contact path included tracking and blinking behavior without a justified portfolio need.
- Page hierarchy, project cards, status labels, metadata, reviewer navigation, limitations, and responsive behavior were weak or absent.
- The repository lacked a root README, durable agent instructions, a useful 404 page, and automated static validation.

### Canonical lab repository

- Mindstate feature construction used per-user forward fill followed by backward fill before splitting. A later user-day could therefore populate an earlier missing value.
- Mindstate engineered proxies also included full-frame missing-value replacement before model splitting.
- Tutoring engineered interactions used full-frame medians before splitting, allowing held-out values to influence derived features.
- Tutoring robustness analysis hard-coded `random_forest_engineered` as the best learned model even when the current experiment table favored logistic regression.
- Dependency ranges were initially too open to guarantee compatibility in a clean runner.
- There was no single branch workflow that independently installed, regenerated, tested, and archived evidence for all three labs.
- Documentation did not consistently include visual-summary generation in the validated command sequence.

## 6. Core-project inventory and final validated evidence

All metrics below are synthetic benchmark results regenerated in GitHub Actions on 2026-07-21. They demonstrate execution and internal workflow consistency only.

### Learning App Analytics

| Field | Final state |
|---|---|
| Main question | Can synthetic practice behavior support cautious next-action classification? |
| Unit of observation | One synthetic practice-problem interaction |
| Target | `advance`, `review`, or `hint_needed` |
| Best current main model | `calibrated_random_forest_engineered` |
| Grouped test evidence | Macro F1 0.759; accuracy 0.760; ECE 0.032 |
| Transparent rule baseline | Macro F1 0.415 on the same grouped test frame |
| Robustness | Learned-model macro F1 0.734–0.750 across temporal-proxy, grouped-student, and random-row checks |
| Complete test suite | 20 passed |
| Strongest hiring signal | Grouped holdout, model-versus-rule comparison, calibration reporting, diagnostic artifacts, and clear separation of prediction from policy |
| Remaining limitation | Inner calibration folds are not group-aware; all labels remain synthetic |
| Portfolio position | Featured project 1 |

### Mindstate Signal Lab

| Field | Final state |
|---|---|
| Main question | Can ambiguous synthetic self-reflection patterns be modeled with uncertainty and explicit abstention without diagnostic claims? |
| Unit of observation | One synthetic user-day |
| Target | `steady`, `strained`, `recovering`, or `uncertain`, plus an abstention wrapper |
| Best current full-coverage model | `random_forest_engineered` |
| Grouped test evidence | Macro F1 0.475; accuracy 0.478; ECE 0.042 |
| Transparent rule baseline | Macro F1 0.257 on the same grouped test frame |
| Robustness | Learned-model macro F1 0.479–0.481 across temporal-proxy, grouped-user, and random-row checks |
| Abstention evidence | About 21.8% retained coverage and 71.2% retained accuracy; about 78.2% abstention |
| Complete test suite | 23 passed |
| Strongest hiring signal | Causal longitudinal features, uncertainty, abstention, sensitive-domain limits, policy boundaries, and explicit weak-class discussion |
| Remaining limitation | Threshold is a fixed experiment choice; tree probabilities are not separately calibrated for threshold selection; no clinical meaning is established |
| Portfolio position | Featured project 2 |

### Tutoring Ops Analytics

| Field | Final state |
|---|---|
| Main question | Can synthetic tutoring records support progress review, session-risk review, and planning support? |
| Unit of observation | One synthetic tutoring session |
| Targets | `progress_label`; secondary `no_show_risk_label` |
| Best current progress model | `logistic_regression_base` |
| Grouped test evidence | Macro F1 0.608; accuracy 0.603; ECE 0.041 |
| Transparent rule baseline | Macro F1 0.549 on the same grouped test frame |
| Robustness | Learned-model macro F1 0.616–0.648 across temporal-proxy, random-row, and grouped-student checks |
| Secondary no-show-risk model | Random-forest macro F1 0.575 |
| Complete test suite | 27 passed |
| Strongest hiring signal | Separate operational targets, simple-model competitiveness, evidence-driven robustness selection, training-boundary-safe missingness handling, and human-review routing |
| Remaining limitation | Targets are contemporaneous synthetic labels rather than validated future outcomes or business effects |
| Portfolio position | Featured project 3 |

## 7. Original project scores

Scale: 0 absent or unusable; 1 major deficiencies; 2 substantial gaps; 3 competent; 4 strong; 5 exceptional and thoroughly supported.

| Project | Hiring relevance | Analytical rigor | Statistical validity | Technical depth | Reproducibility | Code quality | Visual communication | Written communication | Completeness | Interview defensibility |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Learning App Analytics | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 |
| Mindstate Signal Lab | 4 | 3 | 2 | 4 | 3 | 3 | 3 | 4 | 3 | 4 |
| Tutoring Ops Analytics | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 |
| Central portfolio presentation | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 1 |

## 8. Final project scores

| Project | Hiring relevance | Analytical rigor | Statistical validity | Technical depth | Reproducibility | Code quality | Visual communication | Written communication | Completeness | Interview defensibility |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Learning App Analytics | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 |
| Mindstate Signal Lab | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 |
| Tutoring Ops Analytics | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 |
| Central portfolio presentation | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 |

Meaningful score changes are supported by clean CI regeneration, regression tests for leakage boundaries, corrected robustness selection, current evidence tables, employer case studies, public structured case studies, rendered responsive checks, and explicit claim limits. Scores remain below 5 where real-world validity, production evidence, public-source access, or deeper engineering maturity is absent.

## 9. Changes implemented

### Public central site

- Rebuilt the homepage around the three confirmed featured projects.
- Added a reviewer-oriented project map and one structured case study per featured project.
- Added actual validated synthetic metrics only after clean CI regeneration.
- Kept synthetic-data, source-visibility, clinical, educational, operational, and deployment boundaries visible near the evidence.
- Replaced obsolete and placeholder primary-path content.
- Replaced the nonfunctional PHP contact form with a working GitHub contact route.
- Removed tracking from the modern contact experience.
- Added semantic landmarks, skip links, visible keyboard focus, reduced-motion handling, responsive card stacking, and internal table scrolling on narrow screens.
- Added a useful 404 page, favicon, robots policy, README, durable `AGENTS.md`, static validator, rendered-browser validator, browser screenshots, and pull-request CI.
- Preserved older pages and assets rather than deleting historical work.

### Canonical three-lab repository

- Added root `AGENTS.md` and improved portfolio/reproduction documentation.
- Bounded the shared Python dependency families to tested compatible major versions.
- Added one matrix workflow covering all three labs independently.
- Regenerated data, models, robustness evidence, written reports, visual summaries, and tests on clean runners.
- Preserved validation logs and generated reports as workflow artifacts even when a stage fails.
- Updated employer case studies and the three-project map with final evidence and limitations.

### Analytical validity corrections

- Replaced Mindstate backward fill with causal within-user forward fill only.
- Preserved unresolved Mindstate missing values for a training-fitted imputer.
- Added a regression test proving future user-day changes cannot alter earlier engineered features.
- Added a temporal robustness boundary test for Mindstate.
- Removed Tutoring full-frame median replacement from feature construction.
- Added Tutoring tests proving held-out values cannot change earlier engineered interactions.
- Made Tutoring robustness model selection read the current experiment table.
- Added selection tests and evidence-driven integration assertions.
- Added a Tutoring temporal robustness boundary test.

## 10. Accessibility and responsive-design review

`VERIFIED` through source review and rendered Chromium automation:

- Eight modern routes rendered at 390×844, 768×1024, and 1440×900.
- 24 route/viewport combinations returned HTTP 200.
- No combination produced page-level horizontal overflow.
- Every checked page had exactly one `h1`, one `main` landmark, and one skip link.
- The first keyboard focus target was the skip link on every combination.
- Browser console and page-error collections were empty.
- Responsive evidence tables scroll inside their own container rather than widening the page.
- Reduced-motion rendering was requested during browser checks.
- Twelve screenshots and a JSON result summary were uploaded as the `portfolio-browser-evidence` workflow artifact.

This is not a claim of complete WCAG conformance. Automated and focused keyboard checks cannot replace a full manual assistive-technology audit.

## 11. Adversarial review findings and corrective work

| Finding | Severity | Correction |
|---|---|---|
| Mindstate future-looking backward fill weakened temporal validity | Critical | Replaced with causal forward fill; added future-row leakage regression test |
| Mindstate full-frame replacements crossed the split boundary | High | Left unresolved missing values for training-fitted preprocessing |
| Tutoring full-frame medians influenced engineered features | High | Preserved missing values until training-fitted preprocessing; added boundary tests |
| Tutoring robustness hard-coded a model contradicted by its experiment table | High | Added evidence-driven model selection and tests |
| Initial clean CI exposed incompatible unconstrained dependency resolution | High | Added tested major-version bounds to all three requirement files |
| Initial workflow did not retain enough failure evidence | Medium | Made stages diagnostic, uploaded logs/reports on failure, and added a final status gate |
| Existing Tutoring integration test expected the old hard-coded random forest | Medium | Replaced the assertion with experiment-driven expected-model logic |
| New floating-point boundary test used exact equality | Low | Replaced exact comparison with tolerant `pytest.approx` |
| Public Tutoring copy became stale after the final imputation correction | Medium | Refreshed the private map, employer case study, and public case study from final artifacts |
| Case-study evidence tables could create narrow-screen risk | Medium | Added a contained responsive table-scrolling layer and rendered overflow checks |
| Learning inner calibration CV is not group-aware | Medium, remaining | Documented clearly; not changed without a larger estimator and validation redesign |
| Mindstate abstention threshold is fixed and probabilities are not separately calibrated for threshold selection | Medium, remaining | Reported coverage, retained performance, and limitation explicitly; no safety claim made |
| Canonical source is private | Portfolio limitation | Public pages state the limitation; no private source was copied or exposed |

## 12. Final validation record

### Canonical lab repository

GitHub Actions workflow: `Portfolio lab validation`, run 24, conclusion `success`.

Each matrix job ran from its own project directory:

```bash
python -m pip install -r requirements.txt
python scripts/run_pipeline.py
python scripts/run_experiments.py
python scripts/run_robustness.py
python scripts/build_report.py
python scripts/build_visual_summary.py
pytest -q tests/unit
pytest -q
```

| Project | Install | Pipeline | Experiments | Robustness | Written reports | Visual summary | Unit tests | Complete suite |
|---|---|---|---|---|---|---|---|---|
| Learning App Analytics | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED — 20 passed |
| Mindstate Signal Lab | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED — 23 passed |
| Tutoring Ops Analytics | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED | VERIFIED — 27 passed |

### Public site

GitHub Actions workflow: `Portfolio site checks`, rendered-browser implementation run 13, conclusion `success`.

```bash
python scripts/validate_site.py
python -m pip install playwright==1.55.0
python -m playwright install --with-deps chromium
python scripts/browser_check.py
```

| Check | Result |
|---|---|
| Static validation of modern routes and required assets | VERIFIED |
| Internal modern-page targets | VERIFIED |
| Mobile rendered checks at 390×844 | VERIFIED |
| Tablet rendered checks at 768×1024 | VERIFIED |
| Desktop rendered checks at 1440×900 | VERIFIED |
| Page-level horizontal overflow | VERIFIED absent across 24 combinations |
| Primary landmarks and first keyboard focus | VERIFIED |
| Browser console/page errors | VERIFIED absent |
| Screenshot and JSON evidence upload | VERIFIED |

### Checks not fully completed

| Check | Status | Reason |
|---|---|---|
| Public production deployment | NOT RUN | Publishing or production promotion was not authorized |
| Final GitHub Pages URL and source setting | BLOCKED | Repository settings were outside the connected version-controlled interface |
| Public live-demo testing | NOT RUN | No featured project claims a working live demo |
| External-link crawl beyond the modern internal route set | PARTIALLY VERIFIED | GitHub repository and PR routes were accessible; a complete third-party crawl was not required for the focused three-project pass |
| Full WCAG conformance audit | NOT RUN | Automated rendered and keyboard checks do not establish conformance |
| Historical Git secret scan | NOT RUN | No history rewrite was authorized; a targeted current-content privacy and secret review was performed |
| Dedicated linting, formatting, or type checking | NOT RUN | No existing configured toolchain was present; adding overlapping tools was not justified for this pass |
| Notebook execution | NOT APPLICABLE TO THE PRIMARY PATH | The three featured labs use scripts rather than notebooks as their canonical execution path |

## 13. Files changed

### `FollowingJCABIC/eulbWolf.github.io`

- `.github/workflows/site-checks.yml`
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
- `projects/learning-app-analytics.html`
- `projects/mindstate-signal-lab.html`
- `projects/tutoring-ops-analytics.html`
- `robots.txt`
- `scripts/browser_check.py`
- `scripts/validate_site.py`

### `FollowingJCABIC/project-viva-data-science-lab`

- `.github/workflows/portfolio-labs.yml`
- `AGENTS.md`
- `README.md`
- `THREE_PROJECT_PORTFOLIO_MAP.md`
- `data-science-lab/learning-app-analytics/REPRODUCIBILITY.md`
- `data-science-lab/learning-app-analytics/docs/employer_case_study.md`
- `data-science-lab/learning-app-analytics/requirements.txt`
- `data-science-lab/mindstate-signal-lab/REPRODUCIBILITY.md`
- `data-science-lab/mindstate-signal-lab/docs/employer_case_study.md`
- `data-science-lab/mindstate-signal-lab/requirements.txt`
- `data-science-lab/mindstate-signal-lab/src/analysis/robustness.py`
- `data-science-lab/mindstate-signal-lab/src/features/build_features.py`
- `data-science-lab/mindstate-signal-lab/tests/unit/test_temporal_feature_leakage.py`
- `data-science-lab/mindstate-signal-lab/tests/unit/test_temporal_robustness_split.py`
- `data-science-lab/tutoring-ops-analytics/REPRODUCIBILITY.md`
- `data-science-lab/tutoring-ops-analytics/docs/employer_case_study.md`
- `data-science-lab/tutoring-ops-analytics/requirements.txt`
- `data-science-lab/tutoring-ops-analytics/src/analysis/robustness.py`
- `data-science-lab/tutoring-ops-analytics/src/features/build_features.py`
- `data-science-lab/tutoring-ops-analytics/tests/integration/test_robustness_outputs.py`
- `data-science-lab/tutoring-ops-analytics/tests/unit/test_feature_imputation_boundaries.py`
- `data-science-lab/tutoring-ops-analytics/tests/unit/test_robustness_model_selection.py`
- `data-science-lab/tutoring-ops-analytics/tests/unit/test_temporal_robustness_split.py`

## 14. Branches, commits, and pull requests

### Private canonical labs

- Branch: `codex/portfolio-modernization-20260721`
- Base: `main` at `2db1105ef2219fa08b6104cbd86e72537a60c9e3`
- Validated implementation head: `e5165ba376a60f9765c43d6192a27a483223290a`
- Draft PR: https://github.com/FollowingJCABIC/project-viva-data-science-lab/pull/1
- PR state: open, draft, mergeable, not merged
- Commits at final validation: 29

### Public central site

- Branch: `codex/portfolio-modernization-20260721`
- Base: `main` at `bb05733a3cf31c894a3272ffe21287f1a65f44bc`
- Rendered-browser implementation head: `6c736eaee0dbd03cabedffc82d234b073869260e`
- Draft PR: https://github.com/FollowingJCABIC/eulbWolf.github.io/pull/1
- PR state: open, draft, mergeable, not merged
- This audit update is the 29th branch commit; the pull request commit tab is the complete commit-level record.

Recommended review and merge order:

1. Review the private canonical-labs PR first because the public metrics and claims depend on that evidence.
2. Review the public portfolio PR second.
3. Verify GitHub Pages settings and preview behavior before any production merge or deployment decision.

## 15. Remaining limitations and owner-verification items

1. Decide whether the canonical lab repository should remain private, become public after a privacy/licensing review, or be represented by a sanitized public mirror.
2. Confirm the final GitHub Pages deployment source and public URL.
3. Confirm whether the existing résumé PDF is current before making it a primary call to action.
4. Choose a professional public contact method if GitHub-only contact is insufficient.
5. Confirm any biography, employment, education, or publication wording before expanding the site; those facts were not rewritten in this pass.
6. Consider group-aware inner calibration for Learning App Analytics.
7. Consider a separately calibrated Mindstate probability model and validation-selected abstention threshold with class-aware utility reporting.
8. Treat real-data extensions as new governed projects requiring consent, privacy, provenance, prospective targets, subgroup analysis, monitoring, and domain oversight.

## 16. Final pull-request titles

- Private labs: **Modernize and validate the three-project data science portfolio**
- Public site: **Rebuild the portfolio around three data science case studies**

## 17. Human-review readiness

| Branch | Ready for human review? | Reason |
|---|---|---|
| Private canonical labs | **Yes** | All three independent matrix jobs pass through generation, experiments, robustness, reports, visual summaries, and complete tests; analytical corrections and remaining limitations are documented |
| Public central site | **Yes** | Static validation and rendered mobile/tablet/desktop checks pass; claims match regenerated evidence; no private source or production claim is exposed |
| Complete modernization | **Yes, for review—not merge or production release** | Cross-repository evidence is coherent, the diff is reviewable, both pull requests remain draft, and owner decisions are explicitly separated from validated implementation work |
