# Design for reddit.com/r/wow #

This is the place for the design of the World of Warcraft subreddit.

**If you would like to use any of our assets for your subreddit's stylesheet. PLEASE [contact us](http://www.reddit.com/message/compose?to=%2Fr%2Fwow) before doing so.**

System Status
----------------------------------------

| Subreddit     | Status                                      |||
| ------------- |:-------------:|:-------------:|:-------------:|
| **/r/wow**    | [![wowcssstatus][wowcssstatus]][wowcssstatus] | [![wowimgstatus][wowimgstatus]][wowimgstatus] | [![wowsdbstatus][wowsdbstatus]][wowsdbstatus] |


[wowcssstatus]: http://gohan.fluxflashor.net/status/wow-css.png
[wowimgstatus]: http://gohan.fluxflashor.net/status/wow-images.png
[wowsdbstatus]: http://gohan.fluxflashor.net/status/wow-sidebar.png


Sanity Documentation
----------------------------------------

Sidebar heading markup:

* H1 is used for sectional headings
* H2 is used for H1 children headings
* H3 is reserved for announcements
* H4 is reserved for special events (Battle.Net World Championships)
* H5 is reserved for countdowns (Mists of Pandaria Launch)
* H6 is currently available for use

SASS Rewrite Coding Standards
----------------------------------------

Proposed is the following:

* Indentation must be spaces. 4 spaces each level per [PEP8](http://www.python.org/dev/peps/pep-0008/#indentation)
* All property definitions must end with a semicolon. While not necessary for the last prop in a set, it keeps shit clean.
* One space following the colon after the name of a property. Again, for cleanliness.
* All colors must be in hexadecimal format. Letters should also be capitalized.
* No single-line declarations unless you're setting up a million related things in a row. Example: setting the background position for a sprite