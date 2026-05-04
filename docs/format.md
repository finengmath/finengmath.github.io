# Lexicon file format

## Overview

The dictionary uses a custom **BibTeX-style format** for representing mathematical concepts with English and Finnish terms.
Other languages can be added later.

Each entry is a `@concept` block with structured fields.

---

## Examples

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

```bibtex
@concept{set-difference,
 en_terms = {set difference, difference, relative complement},
 fi_terms = {joukkoerotus, erotus, suhteellinen komplementti},
 en_notes = {The difference of sets $A$ and $B$
 is the set of elements in $A$ that are not elements of $B$.},
 fi_notes = {Joukkojen $A$ ja $B$ erotus on niiden $A$:n alkioiden joukko,
 jotka eivät ole $B$:n alkioita.},
 domains = {basic},
 tags = {set theory},
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

- **status**

### Optional (admin)

- **date**
Last update in ISO format ```YYYY-MM-DD```


## Conventions

- **Preferred term first**
The first term in each list is the recommended term.
- **UTF-8 encoding**
Finnish characters (ä, ö) are allowed.
- **Naming of IDs**
Use lowercase and hyphens:

```
disjoint-sets
poisson-process
```
