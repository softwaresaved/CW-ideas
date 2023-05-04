# Contributing to CW-ideas

There are multiple components to the CW-ideas project that are accepting contributions.

- [Contributing to CW-ideas](#contributing-to-cw-ideas)
  - [Contributing ideas from Collaborations Workshops](#contributing-ideas-from-collaborations-workshops)
    - [Convert Doc to Markdown](#convert-doc-to-markdown)
    - [Clean up the Markdown](#clean-up-the-markdown)
    - [Add the metadata](#add-the-metadata)
    - [Save the file](#save-the-file)
    - [Images](#images)
  - [Contributing to the website code](#contributing-to-the-website-code)
  - [Publishing pages](#publishing-pages)

## Contributing ideas from Collaborations Workshops

The main data source for CW-ideas is a set of markdown documents containing the ideas (both collaborative ideas and hack day pitches) from previous Collaborations Workshops. These are created by converting the Google Documents used during the conference into Markdown, and adding some metadata. Instructions for doing this are below.

### Convert Doc to Markdown

1. Install the [Docs to Markdown](https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607) extension for Google Docs. You may need to restart Chrome after installation if you find that the relevant menu items do not appear.
2. Open a Collaborative Idea/Hack Day pitch document.
3. Go to the `Add-ons` menu, choose `Docs to Markdown` and then `Convert`.
4. Tick the following two options in the configuration area at the top of the sidebar:
   - `Demote headings` and
   - `Suppress info comment`.
5. Click the `Markdown` button at the top, and a markdown version of the document will be displayed in the document and copied to the clipboard.
6. Open a text editor and paste the converted markdown.
7. Save the file to a file in the `content` directory using the following format: `cwXX-Idea-title-with-no-spaces.md` where `XX` corresponds to the CW year/number.

### Clean up the Markdown

If the document included images, then these are not extracted automatically. Instead, 'alerts' are included in the document, reminding you to download the images manually. To fix these:

1. Scroll to each image in the document and take a screenshot of the image (it appears to be impossible to download the images as the original files) and use an image editor to save this as a PNG file in the `static/images` subdirectory. In the markdown you need to point to the file `cwXX-uniquename.png` using `../images/cwXX-uniquename.png`. Note the image will not be shown if you are using a wysiwyg markdown editor as the path does not correspond but it will be ok when the document is published on the web site - if you use `../static/images/cwXX-uniquename.png` it will NOT work.
2. Find the alert areas in the document - they look like this:

```html
<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>
```

1. Delete the alert (everything within the `<p>` tag).
1. Find the image code that follows the alert (it will look like `![alt_text](images/image1.png "image_tooltip")`) and edit it to include the correct path to the image.
1. Delete all of the alert areas that appear at the top of the file (these are just telling you that there are other alerts later on in the file). Again, they are wrapped in `<p>` tags, and normally cover 3-4 lines.

### Add the metadata

At the top of the file, add a metadata section with the following format:

```yaml
---
title: 
author:
- 
year: 2022
type: hack day
tags:
- 
prize: 
---
```

There is a `template.md` which contains the above - you can copy this to the new file name but remove the `draft: true` line from the metadata otherwise your addition will not be displayed. This should be filled in, so that it looks like this example:

```yaml
---
title: Using Raspberry Pis to deliver Carpentries training in remote locations
author:
- Becca Wilson
- Irma Hafidz
- Alison Clarke
- Talia Caplan
- Jannetta Steyn
year: 2021
type: hack day
tags:
- software-carpentry 
- training
prize: 2
---
```

Specifically, note that:

- The `title` is the full text title of the idea, not the ID number nor the ID name (eg. 'Garfield') used for the idea. This can often be found under the _Idea Name_ heading in the document. If it has special characters in it like `:` or `&` then wrap the title in double-quotes.
- The `author` is a YAML list of authors, one per line.
- The `year` is the year of the Collaborations Workshop when the idea was proposed.
- The `type` is either:
  - `hack day` for a Hack Day idea or
  - `collaborative idea` for a Collaborative Idea.

- The `tags` contains a list (one per line) of tags for the entry.
- The `prize` indicates whether this entry won a prize. It can be:
  - `1`, `2` or `3` for 1st, 2nd and 3rd place to display a gold/silver/bronze medal icon. 
  - An arbitrary string which will be displayed as-is next to a generic medal icon, e.g. `prize: "Punniest Project Title"`.

### Save the file

The file should be saved in the `ideas` directory, with a name formatted such as `cwXX-title-here-separated-by-dashes.md` where the `XX` represents the CW year identifier. For example, `ideas/cw21-using-raspberry-pis-to-deliver-carpentries-training-in-remote-locations.md`. If the idea title is extremely long then a shortened version can be used for the filename.

### Images

Any images in the Google document will have to be saved in `static/images/`. These will not show properly in the `main` thread but they should be fine in the `gh-pages` thread. You can get images to show by putting in a symbolic link (but do not commit this). In the git root directory do:

```bash
ln -s static/images .
```

## Contributing to the website code

The templates for the website are in `themes/PaperMod/layouts` and the 'special pages' (like the 'By Year' view) are defined as special markdown pages in `content`. Please see the [Hugo documentation](https://gohugo.io/documentation/) for more information on how to edit these.

The theme is manually updated from the upstream theme last on 04/05/2023. To update it, copy the files from the upstream theme and resolve any merge conflicts.

## Publishing pages

The pages can be [hosted on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/).The publishing of the pages is done through GitHub Actions (See the `.github/workflows/hugo.yml` in the root directory of the repository). You need ensure that [Action workflows](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow) have been enabled for your repository on GitHub. Whenever you push content to GitHub it will be processed and published to the `gh-pages` branch which is published on GitHub at:

- [softwaresaved.github.io/CW-ideas/](https://softwaresaved.github.io/CW-ideas/)

If, after a bit of time, things do not appear to have worked check the status of the workflow:

1. Go to the repo: <https://github.com/softwaresaved/CW-ideas>
2. Click on the `Actions` on the top menu item: <https://github.com/softwaresaved/CW-ideas/actions>
3. If there is no green tick at the top workflow click on it and check what has gone wrong - it will give you an indication of where things went wrong. If the changes corresonding to your commit message have a green tick and you still do not see the changes you may have to search elsewhere.
