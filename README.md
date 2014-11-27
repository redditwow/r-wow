# Design for reddit.com/r/wow #

This is the place for the design of the World of Warcraft subreddit.

**If you would like to use any of our assets for your subreddit's stylesheet. PLEASE [contact us](http://www.reddit.com/message/compose?to=%2Fr%2Fwow) before doing so.**

Requirements
----------------------------------------

* python to run the concatenation script at tools/redditcss.py
* upload permissions in a subreddit

Sanity Documentation
----------------------------------------

Sidebar heading markup:

* H1 is used for sectional headings
* H2 is used for H1 children headings
* H3 is reserved for announcements
* H4 is reserved for sidebar link for mobile users
* H5 is open if needed
* H6 is open if needed
* blockquote is reserved for dropdown menu

Building Stylesheets
----------------------------------------

To build the stylesheets, you need to run the redditcss.py script from the directory it's in (or any subdirectory of the project). Then copy and paste the 
stylesheet from the project's top directoy into any subreddit.

You'll have to manually sync right now, which means updates to images, sidebars, etc. are all somewhat painful to deal with.

SASS Rewrite Coding Standards
----------------------------------------

Proposed is the following:

* Indentation must be spaces. 2 spaces each level per 
* All property definitions must end with a semicolon. While not necessary for the last prop in a set, it keeps things clean.
* One space following the colon after the name of a property. Again, for cleanliness.
* No single-line declarations unless you're setting up a million related things in a row. Example: setting the background position for a sprite
