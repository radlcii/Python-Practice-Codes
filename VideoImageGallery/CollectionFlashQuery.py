"""
Written by Robert De La Cruz II on 9/11/2019
Written in Python 3.7.2
The whole "site" was built to be deployed to a local area network using Microsoft's IIS software, and would certainly need heavy modification for a real deployment to the web.
I already wrote a version of this site using PHP, now I'm trying my hand with Python

This particular script is for searching a single database table containing all the content of a particular type, Flash, by the field "fileFolderName" which should reflect a folder on the file system.
"""
import mysql.connector  # Built using a MySQL database
def CollectionFlashQuery(fileFolderName):
    try:
        fileFolderName =fileFolderName.replace('_',' ')
        conn = mysql.connector.connect(user='USER_NAME_HERE', password='PASSWORD_HERE', host='HOST_URL_HERE', database='DATABSE_NAME_HERE') # Establish the connection, supply your own MySQL databse's credentials here
        cursor = conn.cursor()
        query = ('SELECT fileTags, fileTitle, fileURL, thumbnailURL FROM Flash WHERE LOCATE ("{}", fileURL);'.format(fileFolderName))   # The Database keeps the file's containing folder's name, and searches for that entry
        cursor.execute(query)
        #print ("{}<br>".format(query))   # Debugging aid
        
        # This takes the results of the query and generates a formatted return
        # A single HTML Table Row whose elements are:
        #       A hidden table column containing file tags that describe the SWF object
        #       A column that contains the given name of the SWF file (From a DB field)
        #       And a thumbnail hyperlink that points to the flash object in the directory structure, which opens in a new browser tab
        # They are displayed in the order the query returns them, typically alphabetically by file name
        print ('<table id="myTable">')
        for (fileTags, fileTitle, fileURL, thumbnailURL) in cursor:
            print ('<tr>')
            print ('    <td hidden> <p hidden> {} </p> </td>'.format(fileTags))
            print ('    <td> <p> {} </p> </td>'.format(fileTitle))
            print ('    <td style="width:320px;" >')
            print ('        <a href="/{}" target="_blank" >'.format(fileURL))
            print ('            <img src="/{}"  style="max-height:300px;max-width:300px" />'.format(thumbnailURL))
            print ('        </a>')
            print ('    </td>')
            print ('</tr>')
        print ('</table>')

    except mysql.connector.Error as err:    # If it errors out, print the error
        print(err)
    else:
        conn.close()    # Always close the connection when you're done with it
