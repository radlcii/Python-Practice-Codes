"""
Written by Robert De La Cruz II on 9/11/2019
Written in Python 3.7.2
The whole "site" was built to be deployed to a local area network using Microsoft's IIS software, and would certainly need heavy modification for a real deployment to the web.
I already wrote a version of this site using PHP, now I'm trying my hand with Python

This particular script is for searching a single database table containing all the content of a particular type, Videos, by a field of "tags" that describe the video in question.  e.g. forest, clouds, flying, dream, surreal, etc.
"""
import mysql.connector  # Built using a MySQL database
def CollectionQueryTags(incomingTags):
    try:
        conn = mysql.connector.connect(user='USER_NAME_HERE', password='PASSWORD_HERE', host='HOST_URL_HERE', database='DATABSE_NAME_HERE') # Establish the connection, supply your own MySQL databse's credentials here
        cursor = conn.cursor()
        query = ("SELECT fileTags, fileTitle, fileURL, thumbnailURL FROM Videos WHERE fileTags LIKE '%{}%'".format(incomingTags))   # The table contains a field of words that describe the video
        cursor.execute(query)
        #print ("{}<br>".format(query))   # Debugging aid

        # This takes the results of the query and generates a formatted return
        # A single HTML Table Row whose elements are:
        #       A hidden table column containing file tags that describe the video
        #       A column that contains the given name of the video (From a DB field)
        #       And an HTML5 video player element that takes the URL of the queried video as a source as well as a thumbnail image to display before playing (Taken by hand and stored elsewhere)  All this info is stored in separate DB fields
        print ('<table id="myTable">')
        for (fileTags, fileTitle, fileURL, thumbnailURL) in cursor:
            print ('<tr>')
            print ('<td hidden> <p hidden> {} </p> </td>'.format(fileTags))
            print ('<td> <p> {} </p> </td>'.format(fileTitle))
            print ('<td style="width:320px;" > <video controls poster="/{}" preload="none" style="max-width:300px;max-height:300px" > <source src="/{}" type="video/mp4" > </video> </td>'.format(thumbnailURL, fileURL))
            print ('</tr>')
        print ('</table>')

    except mysql.connector.Error as err:    # If it errors out, print the error
        print(err)
    else:
        conn.close()    # Always close the connection when you're done with it
