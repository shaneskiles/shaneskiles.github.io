# Project Summary

This is a Jekyll-based personal blog for Shane Skiles. It uses a heavily customized version of the "moonwalk" theme and includes a significant amount of personal writing, including technical blog posts and a serialized science fiction story.

## File Breakdown

*   **`_config.yml`**: The main Jekyll configuration file. It defines site-wide settings, the remote theme, and the theme's appearance ("dark").
*   **`_posts/`**: Contains all the technical and personal blog posts.
*   **`_sass/moonwalk.scss`**: The core SASS file for the theme. This is where all color variables and primary styles are defined.
*   **`_data/home.yml`**: Configures the content of the homepage, including the navigation bar, project cards, and footer links.
*   **`_layouts/`**: Contains the main HTML layouts for different page types (`home`, `post`, `blog`).
*   **`nightmare/` & `sleepwalker/`**: Directories containing chapters and notes for the serialized story, "Dream of the 20 Watt Sleepwalker."
*   **`assets/`**: Contains CSS entry points, images, and favicons.
*   **`Gemfile`**: Manages the project's Ruby dependencies.

## How it works

The site is built with [Jekyll](https://jekyllrb.com/) and uses the `moonwalk` remote theme as a base. The theme's appearance and content structure are heavily configured through `_config.yml` and `_data/home.yml`. All styling is handled via SASS, with `_sass/moonwalk.scss` being the primary file for customization.

## Recent Changes

*   **Theme Overhaul**: Replaced the default Jekyll "minima" theme with the "moonwalk" theme and imported a large collection of new blog posts and story chapters.
*   **Color Palette Customization**: Modified the dark theme's colors in `_sass/moonwalk.scss`:
    *   Changed the primary background to a slate gray (`#323945`).
    *   Changed the secondary background to a lighter gray (`#5A697A`).
    *   Updated heading colors to a softer blue (`#A7CBE5`).
    *   Updated link colors to a brighter blue (`#8DBCFF`).
*   **New Blog Post**: Added a new post to summarize the recent theme color updates.