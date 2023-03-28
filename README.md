# Exploring previous Collaborations Workshop ideas (CW-ideas)
This is a fork of a repo originally produced for a hack day project at the [2021 Collaborations Workshop](http://www.software.ac.uk/cw21). The website presents the collaborative ideas and hackday pitches generated at previous Collaborations Workshops and makes them available through an easily browseable and searchable interface.

A live version of the website is hosted at:

* [https://softwaresaved.github.io/CW-ideas/](https://softwaresaved.github.io/CW-ideas/).

This repo consists of markdown versions of previous collaborative ideas and hackday pitches, plus the code to host a website to view them using.

To contribute to the repository - either by adding new ideas from previous CWs or to the code to view these ideas - please see the [contributing guide](CONTRIBUTING.md).

This repository is licensed under the MIT license, and most of the ideas themselves are CC-BY (explicitly since CW21 - licensing is mentioned in each idea).

The team that created this was: Mario Antonioletti, Heather Turner and Robin Wilson.

## Building locally
The repository is automatically built and deployed on every push using GitHub actions, but if you want to build locally for testing or debugging purposes, follow the instructions below:
1. Install [Hugo](https://gohugo.io/getting-started/installing/).
2. In the root of the repo, run 
   ```bash
   $ hugo server
   ```
3. The site will be built, and served on localhost - see the command-line output for the full URL.


## Task split during the hack day
- Heather Turner: The brains behind the original idea.
- Robin Wilson: The technical guru.
- Mario Antonioletti: The plodder with superpowers.

Tasks divided orthogonally
- Conversion of past google doc proposals to markdown (Mario and Robin)
- Configuring and setting up Hugo (Robin and Heather)
- Provisioning a GitHub repo (Robin)

## Hack day presentation
Available [here](https://docs.google.com/presentation/d/1GOjaNzfhDBwjr1lmJOlYjHYNzxpctGAla5PxpZDzOIQ/edit?usp=sharing).



## ToDo

- [ ] Implementation of ordering: hack-day > hack-ideas > collaborative-ideas in `by_type.html` and `by_year.html`  at `themes/PaperMod/layouts/_default` could be done much more elegantly - it's a bit of a hack just now.
