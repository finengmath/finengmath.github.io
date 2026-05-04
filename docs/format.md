# Lexicon file format

## Overview

The dictionary uses a custom **BibTeX-style format** for representing mathematical concepts with English and Finnish terms.
Other languages can be added later.

Each entry is a `@concept` block with structured fields.

---

## Example

```bibtex
@concept{disjoint-sets,
  en_terms = {disjoint, mutually disjoint},
  fi_terms = {erilliset, toisensa poissulkevat},
  domains = {basic},
  tags = {set theory},
  comments = {Onkohan tämä ok? Vai pelkkä "disjoint"?},
  status = {draft},
  date = {2026-01-14},
}
```

## Structure

    @concept{<term-id>,
      <field> = {<value>},
      ...
    }

- `<term-id>`: unique identifier (lowercase, hyphen-separated recommended)
- Fields are key–value pairs
- Values are enclosed in `{...}`
- Lists are comma-separated

## Fields

### Mandatory (user)

- **en_terms**
English terms (list)

Example:

```bibtex
en_terms = {graph, network}
```

- **fi_terms**
Finnish terms (list)
Example:

```bibtex
fi_terms = {verkko, verkosto, graafi}
```

### Mandatory (admin)


