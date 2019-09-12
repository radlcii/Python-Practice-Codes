Last updated: 9/12/2019
Maker:  Robert De La Cruz II
Made in Python 3.7.2 and HTML (I didn't make the JavaScripts)

Maker's Notes:

This is a demonstration.  There is no database backing it nor are there any working links.
It's meant to be a Python version of one I wrote in PHP, and it will likely be remade in more languages eventually.
I was also messing with separating as much HTML as possible from the server-side language.  To this end there are the files
	in the Partials folder which are meant to be grabbed by the server script and added to the page that gets shipped.

To see in action will require some tinkering and setup:
	1. A working database built on a file structure similar to what was used in development, this currently uses MySQL
		The database this was developed on has all files of a given type lumped into a single table for that type.
			I simply don't have enough stuff to justify breaking it down in fancy ways.
		e.g. All images are in the Image table, videos in the Videos table, etc.
	2. Folder names in the file system will need to correspond to the POST data made by html buttons, 
		OR the button data will need to be captured and manipulated before being used in queries.
	3. A working server of some kind since python does server-side operations.
		This was deployed to Microsoft IIS running on the same local machine where it was written.
                	IIS settings were as simplistic as possible and found online in many sources.
                        No other testing of any kind was done.
        4. All hyperlinks will need to be entered by hand.
        5. The scripts to create and fill the database will need to be made and used separately as well.
		All testing was done on the local machine, so all the files were present as well.

	I have attempted to sanitize the places where links or login-type info is needed while also hopefully
        making them easy to spot in the code (Having filler text in the fields instead of leaving them blank)

Currently, if anyone takes the time to plug everything in, any change made to the database connection info will 
	need to be applied to each of the 4 database query scripts individually.
It's also worth pointing out that no attempt was made in the "CollectionQueryTags" script to prevent SQL injection.
