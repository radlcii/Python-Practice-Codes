"""
Written by Robert De La Cruz II on 9/11/2019
Written in Python 3.7.2
The whole "site" was built to be deployed to a local area network using Microsoft's IIS software, and would certainly need heavy modification for a real deployment to the web.
I already wrote a version of this site using PHP, now I'm trying my hand with Python

This particular script is for searching a single database table containing all the content of a particular type, Images, by the field "fileFolderName" which should reflect a folder on the file system.
"""
import mysql.connector  # Built using a MySQL database
def CollectionImageQuery(fileFolderName):
    try:
        conn = mysql.connector.connect(user='USER_NAME_HERE', password='PASSWORD_HERE', host='HOST_URL_HERE', database='DATABSE_NAME_HERE') # Establish the connection, supply your own MySQL databse's credentials here
        cursor = conn.cursor()
        query = ("SELECT fileURL, fileTitle, fileExt  FROM Images WHERE fileFolderName LIKE '{}';".format(fileFolderName))  # The Database keeps the file's containing folder's name, and searches for that entry
        cursor.execute(query)
        #print ("{}<br>".format(query))   # Debugging aid
        
        # This takes the results of the query and generates a formatted return
        # It generates an HTML <figure> element to contain an image and label whose information is contained in the fields of the database's Image table (Typically alphabetical by file name)
        # These figures are displayed in the order the query returns them
        for (fileURL, fileTitle, fileExt) in cursor:
            print('<figure>')
            print(  '<img class="myImg" src="/{}" style="max-height:300px;max-width:300px" />'.format(fileURL))
            print(  '<br>')
            print(  '<label>"{}.{}"</label>'.format(fileTitle,fileExt))
            print('</figure>')

    except mysql.connector.Error as err:    # If it errors out, print the error
        print(err)
    else:
        conn.close()    # Always close the connection when you're done with it
