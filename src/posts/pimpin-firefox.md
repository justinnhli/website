Title: Pimpin' Firefox
Date: 2007-12-07 02:44
Author: justinnhli
Slug: pimpin-firefox

Er... yeah.

I use a fairly customized version of Firefox, and since I recently
accidentally deleted my profile and had to reset everything, I figured I
would document what I do to make Firefox really mine.

There are several layers of things I do. The first resides in the
preferences section. I disable everything under advanced Javascript, set
the default font to Arial 11px, and use 32 MB for my cache.

Next up are the about:config values. Since I'm almost always connected
to a high speed network, wired or not, I turn up the maximum number of
connections Firefox can establish. There are things which deal with the
delay before submenus pop out as well. The values I change are listed
below.

-   `browser.tabs.tabMinWidth` = 75
-   `content.notify.backoffcount` = 5
-   `network.dns.disableIPv`6 = true
-   `network.http.pipelining` = true
-   `network.http.pipelining.maxrequests` = 30
-   `netowrk.http.proxy.pipelining` = rue
-   `nglayout.initialpaint.delay` = 0
-   `plugin.expose_full_path` = true
-   `ui.submenuDelay` = 0

The most advance stuff I do are stored in userChrome.css. This modifies
how Firefox looks; whereas Firefox has three different toolbars by
default (menus, navigation, and bookmarks), I only have one. Right
clicking on a toolbar allows you to customize them, so I have my back
and forward buttons, my address bar, and my search bar all up in the
menu toolbar, then uncheck the navigation and bookmarks bars for
display. The following CSS maximizes the space of the address bar by
getting rid of a few menus and minimizing the search.

    /* set default namespace to XUL */@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");#go-menu, #bookmarks-menu, #helpMenu, .toolbarbutton-menubutton-dropmarker,   #go-button-stack, .searchbar-engine-button, .search-go-button-stack, #throbber-box {display:none !important;}#search-container, #searchbar {max-width:1px !important;min-width:1px !important;width:1px !important;}

This little snippet of styling gets ride of the History, Bookmarks, and
Help menus, the drop down menu button for back and foward, the go button
at the right of the address bar, the search engine selection button, the
go button at the right of the search box, and finally the "throbber",
the thing that "rotates" when the page is loading. That was the first
line. The second line sets (what is remaining of) the search box to have
a width of 1 - effectively invisible.

Here's the rationale behind all the changes:

-   I can get to history and bookmarks through keyboard shortcuts
    (ctrl+H and ctrl+B, respectively; ctrl+D bookmarks a page)
-   I don't use the help menu, except to know which version of Firefox
    I'm using, for which I go to "about:"
-   I press enter to go to an address and do searches
-   I only use Google to do search
-   There is a throbber for each tab already

The minimization of the search bar means I get to see more of the
address bar. How do I search then? Well, I have a set of special
bookmarks, with keywords assigned to them. They are listed below with
the URL in angled brackets and the keyword in parenthesis:

-   Arch Linux (a)
-   Google (g)
-   Google Image Search (i)
-   Google Video Search (v)
-   Merriam-Webster Dictionary (d)
-   Merriam-Webster Thesaurus (t)
-   Wikipedia (w)

Those of us who have used Opera before will know how these work. All I
have to do is type "g linux firefox" in the address bar, and Firefox
will automatically insert "linux firefox" into the URL of the bookmark
and go to the resulting address. Similarly, I can get the Wikipedia
Firefox page by doing "w firefox". By doing this, I'm using the address
bar as my search bar, together with the ability to change search engines
as needed.

Finally, I use a small number of extensions for Firefox. The one I've
used for the longest is the Mouse Gesture extension from Optimoz Team.
Again something borrowed from Opera, this allows me to go back and
forward, reload a page, open and close tabs, duplicate tabs, and go back
to my home page with a mouse movement. The gestures I have set up are:

-   D New Blank Tab/Link in New Tab
-   DR Close Document
-   DU Duplicate Tab
-   L Back
-   LR Reload Page
-   R Forward
-   RL Reload Page
-   U Load Homepage
-   UL Previous Tab
-   UR Next Tab

I also disable rocker gestures and turn off diagonal movement, as that
makes my gestures harder to perform.

The other two extensions I use are both recent discoveries. Better Gmail
2 from LifeHacker.com extends the Gmail interface. I particularly like
the setting to display message details by default and the extra keyboard
shortcuts for labeling messages and going to those labels, although the
latter screws up the 'g + c' shortcut to go to Contacts. The last
extension is Firebug from Joe Hewitt, which not only duplicates the
Javascript Console function in Firefox, but also allows real time
editing of HTML, CSS and Javascript, and shows a very useful picture of
the position and size of an HTML node is, separating the margin, the
padding, the border, and the actual content. In other words, the perfect
webpage debugger.

The result of all this customization is I have a version of Firefox
which I can call my own.

