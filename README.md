# Jose G. Chavez Data Science Portfolio

This repository contains a static portfolio centered on three synthetic-data research labs:

1. Learning App Analytics
2. Mindstate Signal Lab
3. Tutoring Ops Analytics

The public site emphasizes problem framing, data provenance, baseline comparison, grouped and temporal evaluation, error analysis, uncertainty, human review, and explicit claim boundaries.

## Current site map

- `index.html` — recruiter-facing overview and featured projects
- `projects/index.html` — reviewer map
- `projects/learning-app-analytics.html` — educational analytics case study
- `projects/mindstate-signal-lab.html` — uncertainty and abstention case study
- `projects/tutoring-ops-analytics.html` — operations analytics case study
- `coding.html` — secondary public software
- `contact.html` — verified public contact route
- `404.html` — static-hosting error page
- `PORTFOLIO_AUDIT.md` — evidence, baseline, validation, adversarial review, and remaining limitations

Older HTML and media remain in the repository for historical continuity. They are not the primary portfolio navigation.

## Run locally

No dependency installation or build step is required:

```bash
python3 -m http.server 8000
```

Open `http://127.0.0.1:8000/`.

## Validate

```bash
python3 scripts/validate_site.py
```

The validator checks the modern page set for required metadata, semantic landmarks, a single main heading, duplicate IDs, missing internal targets, unsafe new-tab behavior, and missing image alt text.

## Source repositories

The canonical executable source for the three labs is currently private: `FollowingJCABIC/project-viva-data-science-lab`. The public case studies summarize the projects without claiming that the private source is publicly inspectable.

A separate private `FollowingJCABIC/mindstate-signal-lab` repository is a broader research scaffold, not the source of the current executed Mindstate metrics.

## Deployment

The site uses only relative URLs and can be served from a GitHub Pages project path. Confirm the final Pages URL and deployment source in repository settings before adding canonical URLs or an absolute sitemap.

## Truthfulness and privacy

- All three featured datasets and labels are synthetic.
- Do not imply real-world learner outcomes, clinical meaning, tutoring impact, business lift, production use, or deployment.
- Do not expose private repository content, credentials, direct personal contact information, or unverified résumé facts.
- Do not add analytics, tracking, or a nonfunctional contact form.
