
# Finnish–English Mathematical Lexicon

**Finnish–English mathematical lexicon with text search support**

Lasse Leskelä  
_Last updated: 2026-01-13_

---

## Overview

This project aims to build a Finnish–English mathematical lexicon with bidirectional search, browsing, and community-supported translation requests. The lexicon is designed to scale to thousands of entries and to support both web-based use and classical PDF publication.

The authoritative data source is a BibTeX file with a fixed schema, which is automatically mapped to JSON for use in web interfaces and other tools.

---

## System components

- **Database**  
  BibTeX master file, automatically mapped to a JSON representation

- **Translation request queue**  
  Mechanism for collecting new term requests and corrections (initially via email to editor(s), later possibly via a web interface)

- **Browser-based user interface**  
  For browsing and searching mathematical terms

- **Browser-based submission interface**  
  For submitting new translation requests and proposed translations

- **PDF mapping tool**  
  Generates a classical alphabetical dictionary in PDF format

---

## User types

- **Admin**  
  Technical administrator responsible for system maintenance and access control

- **Editor**  
  Responsible for reviewing translation requests and maintaining dictionary entries

- **Anyone**  
  Public users who can browse, search, and propose new translations and corrections

---

## Features

### General (web browsers on laptops and phones)

- Search **English → Finnish** and **Finnish → English** translations by full or partial word
- Browse **English → Finnish** and **Finnish → English** translations alphabetically by starting letter
- Submit new term translation requests, with optional proposed translations, via a simple online form

### Editor features

- Add, edit, and delete dictionary entries
- View and manage the translation request queue
- Generate a PDF version of the lexicon

### Admin features

- Add, modify, and remove editors and contributors
- Maintain system configuration and access control

---

## Contributing

Editing and direct contributions to the lexicon are coordinated through a dedicated editorial team.

Public users are welcome to suggest new terms or propose translations via the translation request mechanism. Editorial access is granted only to designated editors.

For questions about the project or editorial collaboration, please contact the maintainers.

---

## License

The lexicon content and data in this repository are licensed under the
Creative Commons Attribution 4.0 International (CC BY 4.0) license.


