from flask import Flask, render_template
from werkzeug.exceptions import abort
import json
import copy

app = Flask(__name__)

def get_tracklist():
	jf = open('tracklist.json')	
	return json.load(jf)

tracklist = get_tracklist()
tr_list = get_tracklist()['tracklist']


@app.route('/')
def index():
	p=[]	
	for chapter in tracklist['tracklist']:
		for track in chapter['tracks']:
			p.append(track['page'])
	pages = set(p)
	return render_template('index.html', pages=pages)

@app.route('/test')
def test():
		return render_template('test.html', tracklist=tracklist['tracklist'])


@app.route('/p/<int:page_num>')
def get_tracks_on_page(page_num):	
	out_tracks = []
	for chapter in tr_list:
		chap = copy.copy(chapter)
		chap['tracks'] = []
		for track in chapter['tracks']:
			if int(track['page']) == page_num:
				chap['tracks'].append(track)
		if len(chap['tracks']) > 0:
			out_tracks.append(chap)	
	if len(out_tracks) > 0:
		return render_template('tracks.html', tracklist = out_tracks)
	else:
		abort(404)


#http://www.objgen.com/json/models/eNs - модель треклиста

