"""
Written by Robert De La Cruz II on 9/11/2019
Written in Python 3.7.2
The whole "site" was built to be deployed to a local area network using Microsoft's IIS software, and would certainly need heavy modification for a real deployment to the web.
I already wrote a version of this site using PHP, now I'm trying my hand with Python

This is the main page which stitches Python and HTML together to be served to a client.
It is NOT ajaxified in any way, the page is reloaded in full every time a selection is made.
"""
#!/usr/bin/python
import codecs           # For reading the HTML pages with contain characters beyond ASCII's scope
import cgi              # This is for dealing with HTML requests
from CollectionVideoQuery import CollectionVideoQuery   # Module that takes a file folder name supplied by an HTML POST and queries the DB "Videos" table
from CollectionFlashQuery import CollectionFlashQuery   # Module that takes a file folder name supplied by an HTML POST and queries the DB "Flash" table
from CollectionImageQuery import CollectionImageQuery   # Module that takes a file folder name supplied by an HTML POST and queries the DB "Images" table
from CollectionQueryTags import CollectionQueryTags     # Module takes input text and searches a database field filled with descriptors, e.g. "Mountains"
from CollectionMusicQuery import CollectionMusicQuery   # Module takes input text and searches a database field filled with descriptors, e.g. "Metal"

print () # This empty print appears to be necessary for the server software.  It dodges an empty header error.
print ("<html>") # Open HTML Tag.

#Because printing HTML is ugly, as much raw HTML as possible has been moved to separate files.
f=codecs.open("VideoImageGallery/Partials/CollectionHeader.html", 'r') # HTML file containing <header> info
print (f.read())

print ("<body>") # Open HTML Body Tag

f=codecs.open("VideoImageGallery/Partials/CollectionNavigationButtons.html", 'r') # HTML file containing Top-Nabvar dropdowns and buttons
print (f.read())

print ("<h2> Filterable Search Page</h2>")      # HTML Header-Text Tag

f=codecs.open("VideoImageGallery/Partials/CollectionResultFilter.html", 'r') # HTML div-filtering scripts.  It "filters" by hiding generated table row elements
print (f.read())

print ("<br>")  # This forces a linebreak after the filter text box

f=codecs.open("VideoImageGallery/Partials/MakersNotes.html", 'r') # HTML div-filtering scripts.  It "filters" by hiding generated table row elements
print (f.read())

form = cgi.FieldStorage()                       # Capture the POST from the form in ./Partials/CollectionNavigationButtons.html
try:
    formData = form.value[0].value              # Storing the value captured by the form's POST

    if "searchTags" in form.keys():             # Database query using the 'fileTags' field
        if "MUSIC_" in formData:
            CollectionMusicQuery(formData)      # Music is thrown in with an ugly implementation and I know it.  It really should be on its own separate page.
        else:
            CollectionQueryTags(formData)

    elif "Videos_and_Images_Mixed_Folder" in formData:  # Handle a mix of images and videos in separate directories
        CollectionVideoQuery(formData)                  # This searches the "Videos_and_Images_Mixed_Folder"
        formData = "NOT_REAL_FOLDER_ONE"                # This folder has both images and videos, videos come out first
        CollectionVideoQuery(formData)
        formData = "NOT_REAL_FOLDER_TWO"                # The remaining ones have already been searched for videos or are known to have only images
        CollectionImageQuery(formData)
        formData = "NOT_REAL_FOLDER_THREE"
        CollectionImageQuery(formData)
        formData = "NOT_REAL_FOLDER_MOAR"
        CollectionImageQuery(formData)

    elif "Art_Folder" in formData:              # Initiates a search for images in separate directories
        formData = "FAKE_MAIN_ART_FOLDER_NAME"
        CollectionImageQuery(formData)
        formData = "FAKE_SECONDARY_ART_FOLDER_NAME"
        CollectionImageQuery(formData)

    elif "_FLASH" in formData:                  # Searches a specific kind of folder
        CollectionFlashQuery(formData)

    elif "_IMAGES" in formData:                 # These folders are specially marked in the menu buttons file but not in the file system
        formData = formData[:-7]                # Removing the "_IMAGES" mark from the POST value before sending it to be processed
        CollectionImageQuery(formData)
    else:                                       # Else take the POST information and query all 3 table types
        CollectionVideoQuery(formData)
        CollectionImageQuery(formData)
        CollectionFlashQuery(formData)


except:
    formData = ""       # If an exception is thrown, which always happens on first load, the page performs a blank search

f=codecs.open("VideoImageGallery/Partials/CollectionModal.html", 'r')    # HTML modal file with script for viewing images without leaving the current page
print (f.read())
f=codecs.open("VideoImageGallery/Partials/CollectionBackToTopButtonScripts.html", 'r') # HTML Back to Top button and required scripts
print (f.read())
f=codecs.open("VideoImageGallery/Partials/MusicPlayerScripts.html", 'r') # Javascript For the Music Player
print (f.read())
print ("</body>") # Close HTML Body Tag
print ("</HTML>") # Close HTML Tag
