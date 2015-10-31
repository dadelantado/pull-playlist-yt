#!/usr/bin/python
import urllib, json, subprocess, time, sys, getopt

def getplaylist(playlistid):
    apikey = 'AIzaSyA7s-mBPBU5snEKPZ7CAuLwIuvGa6hRGyc'
    inp = urllib.urlopen(r'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={0}&key={1}&maxResults=50'.format(playlistid, apikey))
    resp = json.load(inp)
    inp.close()
    playlist = resp['items']
    return playlist

def generatefile(playlistid):
    print 'Generating playlist ...'
    playlist = getplaylist(playlistid)
    ind = 0
    firstvideo = playlist[ind]['snippet']['resourceId']['videoId']
    file = open('playlist.html', 'w')
    file.write('<div class="responsive-video-list"><div class="featured-video"><iframe width="100%" height="100%" src="https://www.youtube.com/embed/'+firstvideo+'?autoplay=0&amp;rel=0&amp;showinfo=0&amp;modestbranding=1&amp;autohide=1" frameborder="0" allowfullscreen id="FeaturedVideoID"></iframe></div><ul>')

    #Add videos from YouTube playlist to HTML playlist

    for videos in playlist:
        videoid = playlist[ind]['snippet']['resourceId']['videoId']
        title = playlist[ind]['snippet']['title'].encode('ascii', 'replace')
    	file.write('<li><a onclick="switchVideo(\'www.youtube.com/embed/'+videoid+'?autoplay=1&amp;rel=0&amp;showinfo=0&amp;modestbranding=1&amp;autohide=1\');" href="javascript:void(0);"> <img src="http://img.youtube.com/vi/'+videoid+'/0.jpg">'+title+'</a></li>')
    	ind += 1

    file.write('</ul></div>')#Close dive

def openfile():
    print 'Opening HTML file ...'
    #Opening playlist.html on BBEdit
    time.sleep(3)
    cmd = 'bbedit playlist.html'
    procc = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    procc.wait()


def main():

    print "Playlist id?",
    playlistid = raw_input()

    generatefile(playlistid)
    openfile()
if __name__ == "__main__":
    main()
