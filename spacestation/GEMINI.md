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
  - path: "sleepwalker/"
    purpose: "Directory for the 'Dream of the 20 Watt Sleepwalker' story. See sleepwalker/GEMINI.md for specific story context."
  - path: "Gemfile"
    purpose: "Manages Ruby dependencies for the project."
  - path: "assets/"
    purpose: "Contains all static assets like CSS entry points, images, and favicons."
  - path: "_spacestation_adventure/"
    purpose: "Choose your own adventure game set on a space station. Contains 'before' and 'after' scenarios."

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
  internal_linking: "When linking to other posts on the site, use the post's slug (e.g., /my-post-slug)."

workflows:
  add_spotify_playlist:
    description: "Adds a Spotify playlist to music.md and downloads its thumbnail."
    command: "python3 bin/add_playlist.py [SPOTIFY_URL]"
    dependencies: "Requires Python 3, `requests`, and `beautifulsoup4`. Install with: pip install -r requirements.txt"
    example: "python3 bin/add_playlist.py 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M'"

choose_your_own_adventure:
  base_directory: "_spacestation_adventure/"
  scenarios:
    before:
      start_file: "before/01-start.md"
      description: "Player character (Milo) arrives at Terrapin Station before the events of 'Dream of the 20 Watt Sleepwalker'. This scenario is actively being developed with multiple branching paths."
    after:
      start_file: "after/01-start.md"
      description: "Player character (Milo) awakens on Terrapin Station after the events of 'Dream of the 20 Watt Sleepwalker', with fragmented memories."