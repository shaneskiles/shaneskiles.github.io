# Project Summary

This is a standard Jekyll website. It appears to be the default site created by `jekyll new`.

## File Breakdown

*   **`_config.yml`**: The main configuration file for the Jekyll site. It contains global settings like the site title, description, theme, and plugins.
*   **`_posts/2025-07-23-welcome-to-jekyll.markdown`**: An example blog post that demonstrates how to create and format posts. It explains the required file naming convention (`YEAR-MONTH-DAY-title.MARKUP`) and the use of Front Matter.
*   **`.gitignore`**: A standard Git ignore file that tells Git which files and folders to ignore. This includes the generated site (`_site`), cache directories, and the `vendor` folder for gems.
*   **`404.html`**: A custom "Page Not Found" error page.
*   **`about.markdown`**: The "About" page for the site, which links to more information about Jekyll and the "minima" theme.
*   **`Gemfile`**: A file used by Bundler to manage the project's Ruby dependencies (gems), such as `jekyll` and the `minima` theme.
*   **`index.markdown`**: The main landing page of the site, which uses the `home` layout.
*   **`LICENSE`**: The MIT License for the project's source code.
*   **`assets/css/style.scss`**: A SASS stylesheet for custom site styling.
*   **`_layouts/default.html`**: A custom layout that overrides the theme's default to include the custom stylesheet.

## How it works

This project uses [Jekyll](https://jekyllrb.com/), a static site generator written in Ruby.

1.  Content is written in Markdown files (like `index.markdown` and the post in `_posts`).
2.  Jekyll reads these files, along with the configuration in `_config.yml` and layout files from the `minima` theme.
3.  It then renders the final HTML pages into the `_site` directory (which is not present as it's in the `.gitignore`).
4.  The site can be served locally by running `bundle exec jekyll serve`.

## Recent Changes

*   **Dark Theme & Responsive Design**: Created a custom stylesheet (`assets/css/style.scss`) to implement a dark theme and ensure the site is readable on mobile devices.
*   **Homepage Update**: Modified `index.markdown` to include placeholder "lorem ipsum" text.
*   **Layout Override**: Created a custom `_layouts/default.html` to load the new stylesheet.