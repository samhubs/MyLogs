# Publishing Guide

<p class="post-meta">How I keep this site organized</p>

This page is the operating manual for the blog. It keeps collections, tags, and post formats consistent as the site grows.

## Collections

Use one of these folders for every new post:

- `docs/posts/research-100/` for paper implementations and reproduction logs
- `docs/posts/technical-notes/` for engineering notes, tutorials, debugging notes, and opinions
- `docs/posts/short-stories/` for fiction and reflective writing

## Tag Vocabulary

Tags are shown inside each post with a `tag-row`. Keep them short and reusable.

Recommended technical tags:

- Machine Learning
- Research
- Reproducibility
- Computer Vision
- NLP
- Systems
- Python
- MLOps
- Geometry
- Debugging

Recommended creative tags:

- Fiction
- Fragment
- Diary
- Reflection

## Research Post Template

```markdown
# Day 000: Paper Title

<p class="post-meta">Research · Reproducibility · Topic</p>

<div class="tag-row">
  <span>Research</span>
  <span>Reproducibility</span>
  <span>Topic</span>
</div>

## Paper

- **Title:**
- **Authors:**
- **Link:**
- **Code:**
- **Dataset:**
- **Goal:**

## Why This Paper?

## Core Idea

## Implementation Plan

## Reproduction Log

## Results

## What I Learned

## References
```

## Technical Note Template

```markdown
# Post Title

<p class="post-meta">Topic · Engineering Note</p>

<div class="tag-row">
  <span>Topic</span>
  <span>Tool</span>
</div>

## Problem

## Approach

## Details

## Takeaways
```

## Publishing Checklist

- Add the post to the right collection folder.
- Add a card on that collection's `index.md`.
- Add the post to `mkdocs.yml` navigation if it should appear in the left sidebar.
- Add a featured card on `docs/index.md` only for work that should represent the site.
- Run `mkdocs build --strict` before pushing.
