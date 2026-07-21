# Repository instructions

## Purpose

Maintain a truthful, accessible, static portfolio centered on Learning App Analytics, Mindstate Signal Lab, and Tutoring Ops Analytics.

## Important paths

- `index.html`: primary portfolio entry point
- `projects/`: reviewer map and structured case studies
- `portfolio.css`: shared responsive design system
- `scripts/validate_site.py`: modern-page validation
- `PORTFOLIO_AUDIT.md`: current audit and validation evidence
- legacy HTML and media: preserved historical work; do not promote it without a separate accuracy and reproducibility review

## Commands

```bash
python3 -m http.server 8000
python3 scripts/validate_site.py
```

## Writing rules

- Keep the synthetic-data boundary visible near every featured result.
- Do not invent model scores, users, clients, impact, deployment, production use, or real-world validity.
- Do not describe the private source repository as publicly inspectable.
- Distinguish the canonical executed Mindstate lab from the separate research scaffold.
- Do not expose private email, phone numbers, credentials, or sensitive information.
- Do not alter résumé, education, publication, or employment facts without evidence.

## Frontend rules

- Keep the primary site usable without JavaScript.
- Maintain semantic landmarks, one clear `h1` per page, visible focus states, keyboard-accessible navigation, sufficient contrast, and reduced-motion handling.
- Inspect major changes near 390 px, 768 px, and 1440 px widths.
- Use relative links so GitHub Pages project-path deployment remains valid.
- Avoid tracking, autoplay, decorative charts, arbitrary skill percentages, and framework migration without demonstrated need.

## Definition of done

- `python3 scripts/validate_site.py` passes.
- Modern internal links resolve.
- The rendered site is inspected at mobile, tablet, and desktop widths.
- Case-study claims match current project evidence and limitations.
- No private-source or deployment claim is overstated.
