# UWA NLP-TLP Website

The website of the UWA Natural and Technical Language group. Now built using Eleventy.

## How to clone this repo and run it locally

To clone the repo:

    git clone https://github.com/nlp-tlp/nlp-tlp.github.io.git

To run it locally, first navigate to the location in which you cloned the site and install the required packages:

    npm install

Then to run the development server:

    npm run dev

This will keep the site alive on [https://localhost:8080](https://localhost:8080) and should refresh it if you make any changes.

## How to update this website

This is an [Eleventy](https://www.11ty.dev/) website that automatically deploys to GitHub pages upon commits to the main branch.

All of the content of the website is located in [/content](/content). The `.njk` files in this directory are the main pages (the homepage, current research, our team, etc), and the `.md` files in each of the corresponding folders are the data that is used to populate those pages.

For example, [/content/current-research.njk](/content/current-research.njk) is the "Current Research" page (https://nlp-tlp.github.io/current-research). This Nunjucks file is responsible for the layout of that page. Each research item is represented by a seperate file in [/content/current-research/](/content/current-research), e.g. [adaptive-user-interfaces-for-industrial.md](content/current-research/adaptive-user-interfaces-for-industrial.md).

Each markdown file generally consists of (key, value) pairs that carry the respective item's data. For example, the aforementioned research item looks like this:

    ---
    name: Adaptive User Interfaces for Industrial Maintenance Procedures
    authors: Caitlin Woods
    description: In many organisations, maintenance procedure documentation (used to guide technicians through complex manual tasks) is still paper-based. Caitlin's research combines Human-Computer Interaction and Ontology Engineering to transform the way that organisations manage and use procedure documentation to support maintenance technicians.
    group: PhD and Honours Projects
    ---

The Nunjucks file knows where to put each of these values to render the page.

### Adding/editing/deleting new items

If you want to add a new item (a person, news item, etc), the easiest way is to clone this repo, duplicate one of the files, edit it, and push back to the main branch.

Editing is similar - just edit the markdown file of the item you want to change, then push to main.

Same goes for deleting - just delete the file and push to main.

#### Images

In general, images should be placed under the [/public/images](/public/images) folder into their respective collections. For example, if you want to add a person, add their profile photo to [/public/images/people](/public/images/people).

The exception is News. News images should be placed under [/content/news/images](/content/news/images) (this allows them to work with Lightbox, which makes them enlarge when the user clicks on them).

#### Example - adding a person

Let's say I want to add a person to the site. Here's an example of how to do that.

First, clone this repo, and run the dev server (so you can see the changes you make) as per the first section.

Then, navigate to `/content/our-team`. Assuming the person you want to add is a current member, navigate to `/current`. Copy one of the existing people, then name it to the name of your person.

Then, open that new file in your text editor, and edit the relevant data as necessary. Save the file.

Add your files to a new commit and commit your changes:

    git add .
    git commit -m "Added person <person's name>"

And push to the main branch:

    git push -u origin main

And in a minute or so, the website will have updated automatically.

## Other details

### What are the `.11tydata` files in each folder?

You may have noticed that each folder in `/content` has an `.11tydata` file in it. This file tells Eleventy the collection each page belongs to, and ensures that they don't get rendered as individual pages with their own URLs. These files should not be deleted or changed.

### What if I want to add a new page, not just an item on an existing page?

If you want to do this, you'll need to make a new `.njk` file under `/content`, similar to all the others. It might be easiest to adapt an existing file to do what you want it to do.

Note that some of the pages have grouped collections (e.g. Current Research, Our Team etc) and some are not grouped (e.g. News).

### Other nuances

-   The "Our team" folder is separated into Current and Alumni (it was the only good way I could think of to force Alumni to the bottom).
-   To edit the stylesheet, make sure to edit the SASS files (under [/\_sass](/_sass)) and not the CSS files under [/public/css](/public/css). The way I built the site, the SASS renders into the public folder (this is not standard practice with Eleventy but I much prefer SASS).
-   **Please be sure to keep the filename conventions the same** - all new pages should be slug case, e.g. no capital letters, and hyphens between words. `michael-stewart.md` is good, `michael_stewart.md`, `Michael-stewart.md` etc is not.
