Title: AJAX Upload (Of Sorts)
Date: 2008-03-09 08:25
Author: justinnhli
Slug: ajax-upload-of-sorts

I've said before that I'm working on a project to put a graphical front
end to regular expressions. One feature we put in (among the plethora
which are not really necessary) is the ability to upload a text file
from your computer, and play with regex on it.

Despite all the tutorials out there, it turns out that getting a
callback function from upload is really really easy. Since my method is
the simplest I've seen (and I've seen quite a few while trying to figure
out how to do it), I thought I would share.

Here's the html:  

</code>  
That's it! All uppercase variables should match, through all code in
this post. The max\_file\_size above is not really necessary, as it is
easily overridden (or so I read). When the user clicks submit, the
iframe (as the target of the form) will reload with the output of
server\_upload\_script.php. For my purposes, I just need to echo to
file, so my php script is simple:  
`<?php$tmp_file = "tmp.txt";if (move_uploaded_file($_FILES['FILE_IDENTIFIER']['tmp_name'], $tmp_file)) {  $file_handler = fopen($tmp_file, 'r');  $contents = fread($file_handler, filesize($tmp_file));  fclose($file_handler);  unlink($tmp_file);  echo $contents;} else{  echo "There was an error uploading the file, please try again!";}?>`  
This will save the file to a temporary tmp.txt (creative naming, I
know), then open the file and read it back. If there's an error with
writing the file, an error message will appear instead of the file. This
could be ignored, but works well for our purposes since it shows up on a
text area anyway.

Finally, now the iframe has the file you need, the last thing is to use
javascript to do whatever you want with that data. That's below:  
`function CALLBACK_FUNCTION() {  var file = document.getElementById(TARGET_IFRAME_ID).contentDocument.body.innerHTML;  if (file !== '') {    /*     * DO OTHER STUFF     */  }}`  
And that's it! Three short sections of code to get an upload, not that
bad.

The funny thing about this is that I spent 2 hours just to come up with
this. And when I started, I didn't even know a `input` element can take
`type="file"`

