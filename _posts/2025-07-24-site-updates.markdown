---
layout: post
title:  "Site Updates: Dark Theme and Customizations"
date:   2025-07-24 10:00:00 -0500
categories: jekyll update
---

Today, I made several updates to the site to implement a new look and feel and prepare for future customizations.

Here's a summary of the changes:

### Dark Theme and Styling

A new custom stylesheet was created at `assets/css/style.scss`. This file introduces a dark theme that is easy on the eyes and ensures the content is readable on mobile devices with a responsive, fixed-width layout.

To complement the custom styles, I also enabled the Minima theme's built-in `dark` skin via the `_config.yml` file. This ensures that all theme components, including syntax highlighting for code snippets, have a consistent dark appearance.

### Layout Overrides

To apply the new stylesheet and allow for further customization, I've brought copies of the core layout files from the Minima theme into our local project. The following files were created:

-   `_layouts/default.html`: The main site template, updated to link to our new stylesheet.
-   `_includes/head.html`: The HTML head section.
-   `_includes/header.html`: The site header.
-   `_includes/footer.html`: The site footer.

By having local copies of these files, we can now easily modify them without altering the underlying theme gem.

### Content Updates

Finally, the homepage (`index.markdown`) was updated with placeholder "lorem ipsum" text to better visualize the new theme.
