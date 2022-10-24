# Contributing to CW-ideas
There are multiple components of the CW-ideas project that are accepting contributions.

## Contributing ideas from Collaborations Workshops
The main data source for CW-ideas is a set of markdown documents containing the ideas (both collaborative ideas and hack day pitches) from previous Collaborations Workshops. These are created by converting the Google Documents used during the conference into Markdown, and adding some metadata. Instructions for doing this are below:

### Convert Doc to Markdown
1. Install the [Docs to Markdown](https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607) extension for Google Docs. You may need to restart Chrome after installation if you find that the relevant menu items do not appear.
2. Open a Collaborative Idea/Hack Day pitch document
3. Go to the `Add-ons` menu, choose `Docs to Markdown` and then `Convert`.
4. Tick two options in the configuration area at the top of the sidebar: `Demote headings` and `Suppress top comment`.
5. Click the `Markdown` button at the top, and a markdown version of the document will be displayed in the document and copied to the clipboard.
6. Open a text editor and paste the converted markdown.

### Clean up the Markdown
If the document included images, then these are not extracted automatically. Instead, 'alerts' are included in the document, reminding you to download the images manually. To fix these:
1. Scroll to each image in the document and take a screenshot of the image (it appears to be impossible to download the images as the original files) and use an image editor to save this as a PNG file in the `ideas\images` subdirectory.
2. Find the alert areas in the document - they look like this:
```html
<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>
```
3. Delete the alert (everything within the `<p>` tag).
4. Find the image code that follows the alert (it will look like `![alt_text](images/image1.png "image_tooltip")`) and edit it to include the correct path to the image.
5. Delete all of the alert areas that appear at the top of the file (these are just telling you that there are other alerts later on in the file). Again, they are wrapped in `<p>` tags, and normally cover 3-4 lines.

### Add the metadata
At the top of the file, add a metadata section with the following format:
```yaml
---
title: 
author:
- 
year: 2021
type: hack day
tags: 
---
```

This should be filled in, so that it looks like this example:

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
tags: software-carpentry training
---
```

Specifically, note that:
- The `title` is the full text title of the idea, not the ID number nor the ID name (eg. 'Garfield') used for the idea. This can often be found under the _Idea Name_ heading in the document. If it has special characters in it like `:` or `&` then wrap the title in double-quotes.
- The `author` is a YAML list of authors, one per line.
- The `year` is the year of the Collaborations Workshop when the idea was proposed.
- The `type` is either:
  -  `hack day` for a Hack Day idea or 
  - `collaborative idea` for a Collaborative Idea.

- The `tags` contains a list (one per line) of tags for the entry.

### Save the file
The file should be saved in the `ideas` directory, with a name formatted such as `cwXX-title-here-separated-by-dashes.md` where the `XX` represents the CW year identifier. For example, `ideas/cw21-using-raspberry-pis-to-deliver-carpentries-training-in-remote-locations.md`. If the idea title is extremely long then a shortened version can be used for the filename.

## Contributing to the website code
The templates for the website are in `themes/PaperMod/layouts` and the 'special pages' (like the 'By Year' view) are defined as special markdown pages in `content`. Please see the [Hugo documentation](https://gohugo.io/documentation/) for more information on how to edit these.

## Publishing pages

The publishing of the pages is done by GitHub Actions. You should ensure that these have been enabled by your repository.