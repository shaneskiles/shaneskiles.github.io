# AI Agent Instructions for sskiles.github.io

This is a Jekyll-based personal blog using a modified version of the Moonwalk theme. Here's what you need to know to work effectively in this codebase:

## Project Structure

- `_posts/`: Blog posts in markdown format with YAML frontmatter
  - File naming convention: `YYYY-MM-DD-title-slug.md`
  - Example: `2025-11-04-old-tech-new-tricks.md`
- `_layouts/`: HTML templates for different page types
- `_includes/`: Reusable HTML components
- `_sass/`: SCSS styling files
- `assets/`: Static files (CSS, images)

## Content Patterns

### Blog Post Structure
```markdown
---
layout: post
author: Shane Skiles
title: "Post Title"
tags: [tag1, tag2]
---

Content in markdown format
```

### Key Configuration
- Site settings are in `_config.yml`
- Navigation and footer links in `_data/home.yml`
- Theme configuration in `theme_config` section of `_config.yml`

## Development Workflow

1. **Local Development**
   - Site uses Jekyll with the Moonwalk theme (via remote_theme)
   - Posts should be dated with future dates (see existing posts)
   - Minimal dependencies, focused on content over features

2. **Content Guidelines**
   - Technical blog posts focused on software development and coding
   - Code snippets use markdown code blocks with language tags
   - Images should be placed in `assets/images/`

3. **Theme Customization**
   - Custom styles go in `_sass/` directory
   - Layout modifications in `_layouts/` and `_includes/`

## Common Operations

- To add a new blog post:
  1. Create file in `_posts/` with correct date format
  2. Include required frontmatter (layout, author, title, tags)
  3. Write content in markdown
  4. Use future dates for post scheduling

## Special Notes

- Theme is intentionally minimalist - avoid adding unnecessary features
- Dark mode is the default theme
- Posts use a clean, technical writing style with code examples
- Focus is on developer-centric content and technical tutorials