Title: Bugger Blog II
Date: 2007-12-01 04:56
Author: justinnhli
Slug: bugger-blog-ii

I was setting up a new Gmail account today, and wanted import all my
contacts to that new account. To my frustration, Gmail's import/export
contacts feature is not working quite right. Currently, each Gmail
contact can have multiple emails, which when exported are put into a
semicolon separated list. That's great, because it means a simple
javascript.split(';') will give an array of all the addresses. The
import feature, however, doesn't do that, instead, it thinks the entire
list, semicolon included, is one email address, and so I get someone
with an address like "abc@example.com; def@example.com" I can still send
emails to that person, but now they'll get multiple copies of it.

I've [posted a
question](http://groups.google.com/group/Gmail-Problem-solving/browse_thread/thread/1855c75fba9c3ffe#62939679517da650)
to the Gmail Help Dicussion group, but no one has answered me yet.

