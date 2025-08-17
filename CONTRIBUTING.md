# Contributing to the VAXPH Listing Documentation

Welcome, operator! This repository serves as the definitive source of truth for all listing-related documentation across VAXPH brands, including SecuLife and SpeedTalk Mobile. Our goal is to maintain a clean, logical, and easily navigable knowledge base that empowers every team member.

## Directory Structure

To ensure consistency and clarity, we adhere to a strict directory hierarchy:

```
listing-documentation/
├── 📂 brands/             # Brand-specific documentation (e.g., SecuLife, SpeedTalk)
│   ├── 📂 seculife/
│   └── 📂 stk/
├── 📂 playbooks-and-tools/ # General playbooks, tools, and reports applicable across brands
│   ├── 📂 helium-10/
│   └── 📂 reports/
├── 📂 _internal/           # Internal strategic documents and operator manuals
│   ├── 📄 what-i-do.md
│   └── 📄 executive-assistant.md
├── 📄 README.md            # Repository overview and navigation hub
└── 📄 CONTRIBUTING.md      # Guidelines for contributing to this repository
```

### Brand-Specific Structure

Each brand directory (`brands/[brand-name]/`) **MUST** contain the following standardized sub-directories:

```
brands/[brand-name]/
├── 📂 a-plus-content/        # Enhanced content, A+ pages, and rich media documentation
├── 📂 listings/              # Specific product listing documentation (e.g., ASIN-based files)
└── 📂 reports-and-analysis/  # Brand-specific reports and data analysis insights
```

## File Naming Convention

To maintain order and facilitate easy searching, all new files, especially within `listings/`, **MUST** follow this strict naming convention:

`[YYYY-MM-DD]-[ASIN]-[Brief-Description].md`

*   `YYYY-MM-DD`: The date the document was created or last significantly updated (e.g., `2023-10-27`)
*   `ASIN`: The Amazon Standard Identification Number relevant to the listing (e.g., `B0BFZQKB2V`). If not applicable, use a relevant identifier or `N/A`.
*   `Brief-Description`: A concise, hyphen-separated description of the file's content (e.g., `S8-Kids-Smartwatch-Features`).

**Example:** `2023-10-27-B0BFZQKB2V-S8-Kids-Smartwatch-Features.md`

## Markdown Style Guidelines

*   Use clear, concise language.
*   Utilize Markdown headings (`#`, `##`, `###`) to structure your content logically.
*   Use bullet points (`*` or `-`) for lists.
*   Use code blocks (``````) for code snippets, file paths, or specific syntax.
*   Ensure consistent capitalization and punctuation.
*   Avoid overly informal language or jargon unless clearly defined.

By following these guidelines, we ensure that this repository remains a powerful and accessible resource for the entire VAXPH team. Thank you for your contribution!