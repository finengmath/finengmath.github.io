# FI–EN–FI Dictionary Format

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



Dictionary File format
We use bibtex to store dictionary data internally

Each dictionary entry is a @concept block with a unique identifier and a set of fields.

@concept{<term-id>,
  <field> = {<value>},
  ...
}



@concept{term-id,
 en_terms = {term-1, term-2, term-3, ...}, % mandatory, user
 fi_terms = {termi-1, termi-2, termi-3, ...}, % mandatory, user
 domains = {basic}, % admin, optional?
 tags = {set theory}, % admin, optional?
 comments = {Onkohan tämä ok? Vai pelkkä "disjoint"?}, % optional, admin
 status = {ready/draft}, % admin, mandatory
 date = {2026-01-14}, % admin last update, 
}


Example

@concept{disjoint-union,
 en_terms = {disjoint union},
 fi_terms = {erillinen yhdiste, erillinen unioni, pistevieras},
 domains = {basic},
 tags = {set theory},
 comments = {Onkohan tämä ok? Vai pelkkä "disjoint"?},
 status = {draft},
 date = {2026-01-14},
}
