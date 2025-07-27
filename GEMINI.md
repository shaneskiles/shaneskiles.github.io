# Gemini Project Configuration
# This file is optimized for the Gemini CLI assistant.
# Human readability is secondary to machine-parsable clarity.

project_vitals:
  project_type: "jekyll"
  primary_language: "ruby"
  primary_framework: "jekyll"
  theme: "remote: abhinavs/moonwalk"
  goal: "Personal blog for Shane Skiles. Focus on software development, personal thoughts, and a serialized sci-fi story."

key_files:
  - path: "_config.yml"
    purpose: "Main Jekyll configuration. Site-wide settings, theme, plugins."
  - path: "_sass/moonwalk.scss"
    purpose: "Primary SASS file for theme customization. All color variables are defined here."
  - path: "_data/home.yml"
    purpose: "Controls content on the homepage (navbar, project cards, footer)."
  - path: "_posts/"
    purpose: "All blog posts. Format: YYYY-MM-DD-title.md"
  - path: "nightmare/"
    purpose: "Directory for the 'Dream of the 20 Watt Sleepwalker' story. See nightmare/GEMINI.md for specific story context."
  - path: "sleepwalker/"
    purpose: "Legacy directory for the same story. See sleepwalker/GEMINI.md."
  - path: "Gemfile"
    purpose: "Manages Ruby dependencies for the project."
  - path: "assets/"
    purpose: "Contains all static assets like CSS entry points, images, and favicons."

commands:
  build: "bundle exec jekyll build"
  serve: "bundle exec jekyll serve --livereload"
  clean: "bundle exec jekyll clean"
  update_deps: "bundle update"

conventions:
  post_frontmatter:
    required: ["layout: post", "author: Shane Skiles", "title", "tags"]
  story_chapter_format: "number-short-description.md"
  image_path: "/assets/images/"
  commit_message_style: "imperative, short summary, optional body"

workflows:
  spotify_playlist_integration:
    description: "Process to add a Spotify playlist to music.md, including downloading its thumbnail."
    steps:
      - name: "Get playlist metadata"
        action: "Use `curl` to fetch HTML, then `grep` to extract `<title>` and `og:image` URL."
        output_variables: ["page_title", "og_image_url"]
      - name: "Derive shortname"
        action: "Extract the playlist name from `page_title` (e.g., 'K African Mix' from 'K African Mix - playlist by MrKudani | Spotify')."
        output_variables: ["shortname"]
      - name: "Download thumbnail"
        action: "Download the image from `og_image_url` to `assets/images/` using `curl`, renaming it to `shortname` (no spaces) with a `.png` extension."
        input_variables: ["og_image_url", "shortname"]
      - name: "Add entry to music.md"
        action: "Append a new list item to `music.md` with a link to the original playlist URL, embedding the downloaded image, displaying the `shortname`, and including a placeholder description."
        input_variables: ["original_url", "shortname"]