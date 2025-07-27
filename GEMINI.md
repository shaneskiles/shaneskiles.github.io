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
