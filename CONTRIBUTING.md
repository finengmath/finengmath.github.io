
# Contributing to the Finnish–English Mathematical Lexicon

Welcome! This repository collects mathematical concepts with their Finnish and English terms.  
Thank you for helping improve it.

---

## 1. Concept vs serm

- **Concept:** a single mathematical idea. Each BibTeX entry represents one concept.  
- **Term:** a language-specific name for a concept. A concept may have multiple terms per language, listed in order of preference.


## 2. File format rules

### Entry Type

- Use **BibTeX** as the master format.
- Use a custom entry type, `@concept`.
- **One entry per concept**. Do **not** create multiple entries for synonyms.

### Entry Keys

- Entry keys (used as `id`) must:
  - Use hyphens (`absolute-continuity`), never underscores
  - Be unique and immutable once created

### Language-Specific Fields

- Prefix all fields with the ISO language code:
  - `fi_` for Finnish
  - `en_` for English
- **Mandatory public fields:**
  - `fi_terms` — Finnish terms (most important first)
  - `en_terms` — English terms (most important first)
- **Optional public fields:**
  - `fi_notes` / `en_notes` — definitions, examples, inflection guidance
  - `fi_seealso` / `en_seealso` — related terms or concepts
- **Mandatory admin fields (hidden from public):**
  - `id` — unique concept identifier
  - `date` — last updated in ISO-8601 format (`YYYY-MM-DD`)
  - `status` — either `draft` or `ready`
- **Optional admin fields (hidden from public):**
  - `domains` — domains of mathematics (basic, algebra, analysis, computational mathematics, discrete mathematics, geometry, linear algebra, numerical analysis, probability, operations research, statistics)


### Notes

- Terms are **comma-separated** and ordered by importance.
- `*_notes` can include:
  - Definitions
  - Examples
  - Inflection guides
- `*_seealso` should be human-readable references to related concepts; optional but recommended.


### Example

```bibtex
@concept{absolute-continuity,
  % ---------- admin (mandatory, hidden) ----------
  id     = {absolute-continuity},
  date   = {2026-01-12},
  status = {ready},

  % ---------- public (mandatory) ----------
  fi_terms = {absoluuttinen jatkuvuus},
  en_terms = {absolute continuity},

  % ---------- public (optional) ----------
  fi_notes = {%
    Mitta $\mu$ on absoluuttisesti jatkuva mitan $\nu$ suhteen,
    jos $\nu(A)=0$ implikoi $\mu(A)=0$.
    Genetiivi: jatkuvuuden; partitiivi: jatkuvuutta.
  },
  en_notes = {%
    A measure $\mu$ is absolutely continuous with respect to $\nu$
    if $\nu(A)=0$ implies $\mu(A)=0$.
  },

  fi_seealso = {Radonin--Nikodymin lause},
  en_seealso = {Radon--Nikodym theorem}
}
```

---

## 3. Status workflow

- All new entries must have `status = {draft}`.
- Maintainers review entries and set `status = {ready}` once approved.
- Only entries with `status = {ready}` are published to the public site.

---

## 4. How to contribute

- Only dedicated editors are allowed to contribute.

---

## 5. What not to do

- Do **not** add machine-translated terms without review
- Do **not** rename an existing `id`
- Do **not** create multiple concepts for simple synonyms
- Do **not** change published entries without maintainers’ approval (`status = ready`)

---

## 6. References

- Each entry represents **one concept**, independent of language.
- Terms are **language-specific**.
- Use **one entry per concept** to ensure clarity, maintainability, and scalability.


