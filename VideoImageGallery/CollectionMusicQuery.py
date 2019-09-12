"""
Written by Robert De La Cruz II on 9/12/2019
Written in Python 3.7.2
The whole "site" was built to be deployed to a local area network using Microsoft's IIS software, and would certainly need heavy modification for a real deployment to the web.
I already wrote a version of this site using PHP, now I'm trying my hand with Python

This particular script is for searching a single database table containing all the content of a particular type, Music, by the field "fileFolderName" which should reflect a folder on the file system.
"""
import mysql.connector  # Built using a MySQL database
def CollectionMusicQuery(fileFolderName):
    try:
        conn = mysql.connector.connect(user='USER_NAME_HERE', password='PASSWORD_HERE', host='HOST_URL_HERE', database='DATABSE_NAME_HERE') # Establish the connection, supply your own MySQL databse's credentials here
        cursor = conn.cursor()
        query = ("SELECT fileURL, fileTitle FROM Music_DB.Music WHERE fileURL LIKE '%{}%';".format(fileFolderName))   # The table contains a field of words that describe the music
        cursor.execute(query)
        data = cursor.fetchall()
        #print ('{}<br> Returned {} rows'.format(query, cursor.rowcount))   # Debugging aid
        trackNo = 1
        print ('<div class="container">')   # Container for all elements of the player
        print (     '<audio id="audio" preload="none" tabindex="0">')   # Audio section
        for row in data:
            print (     '<source src="/{}" data-track-number={}  type="audio/mpeg" />'.format(row[0], trackNo))  # Make the sources
            trackNo += 1
        print (     '</audio>')     # Close Audio tag

        # The player code was not loading properly as a partial, hense this
        print( """
                    <!-- The player -->
                    <div class="player">
                        <div class="large-toggle-btn">
                            <i class="large-play-btn"><span class="screen-reader-text">Large toggle button</span></i>
                        </div>
                        <!-- /.play-box -->
                        <div class="info-box">
                            <div class="track-info-box">
                            <div class="track-title-text"></div>
                                <div class="audio-time">
                                    <span class="current-time">00:00</span> /
                                    <span class="duration">00:00</span>
                                </div>
                            </div>
                            <!-- /.info-box -->
                            <div class="progress-box">
                                <div class="progress-cell">
                                    <div class="progress">
                                        <div class="progress-buffer"></div>
                                        <div class="progress-indicator"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /.progress-box -->
                        <div class="controls-box">
                            <i class="previous-track-btn disabled"><span class="screen-reader-text">Previous track button</span></i>
                            <i class="next-track-btn"><span class="screen-reader-text">Next track button</span></i>
                        </div>
                        <!-- /.controls-box -->
                    </div>
                    <!-- /.player -->
        """)
        
        trackNo = 1
        print (     '<div class="play-list">')  # Create the visible playlist
        for row in data:
            print ('    <div class="play-list-row" data-track-row={}>'.format(trackNo))
            print ('        <div class="small-toggle-btn">')
            print ('            <i class="small-play-btn"><span class="screen-reader-text">Small toggle button</span></i>')
            print ('        </div>')
            print ('        <div class="track-number"> {}. </div>'.format(trackNo))
            print ('        <div class="track-title">')
            print ('            <a class="playlist-track" href="#" data-play-track={}> {} </a>'.format(trackNo, row[1]))
            print ('        </div>')
            print ('    </div>')
            trackNo += 1
        print (     '</div>') # Close playlist div

        print ('</div>') # Close container div

    except mysql.connector.Error as err:    # If it errors out, print the error
        print(err)
    else:
        conn.close()    # Always close the connection when you're done with it
