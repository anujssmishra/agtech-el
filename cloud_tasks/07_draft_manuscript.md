# 07 Draft the Economics Letters manuscript

Needs task 06.

1. Read CLAUDE.md, `results/results_summary.md`, `results/descriptives.md` and `play_reviews/README.md`
   (for how languages are labelled).
2. Write `paper/manuscript.tex` with Elsevier's `elsarticle` class (install with tlmgr or apt if missing; if
   LaTeX cannot be installed, write `paper/manuscript.md` instead). Include:
   - Title, abstract of at most 100 words, 3–5 highlights of at most 85 characters each, 1–7 keywords,
     and at most 6 JEL codes (likely O33, Q16, L86, D83).
   - Sections: Introduction; Data (apps, reviews, language labels with the hand-check accuracy, launch
     dating); Empirical strategy (equation, fixed effects, inference); Results; Robustness; Conclusion.
   - The main table and the event-study figure from results/.
   - A data availability statement: aggregate panel and code shared; review text not shared; sources.
   - References in BibTeX (`paper/refs.bib`). Include Santos Silva and Tenreyro (2006) on PPML; IndicLID
     (Madhani, Khapra and Kunchukuttan, ACL 2023); wordfreq (Speer, 2022); staggered-adoption papers as
     needed. Verify every reference; never invent one.
3. Count words excluding references and the abstract (script in `paper/`), and report the count. Stay at or
   under 2,000.
4. Commit and tick task 07 in TODO.md. List open questions for Anuj at the end of the summary.
