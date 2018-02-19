"""Project: Gallery catalog."""

# NOTE Import the necessary modules to make the server side with flask.
# Modules for making the server app with flask, login with google
# apis, upload files, etc.

from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from flask import session as login_session
from flask import make_response
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Gallery, Pictures, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from werkzeug.utils import secure_filename
import httplib2
import requests
import random
import string
import json
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# NOTE: Connect to Database and create database session

engine = create_engine(
    'postgresql://project-catalog:database@localhost/imagegallery.db'
    )
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

app.secret_key = 'project-catalog-key'
a

###################
# Gallery section #
###################


# NOTE: Show all images

@app.route('/')
def showGalleries():
    # gallery = session.query(Gallery).all()
    return 'Hello'


# NOTE: Add a new gallery

@app.route('/gallery/new/', methods=['GET', 'POST'])
def newGallery():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        file = request.files['pic']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        addgallery = Gallery(
            title=request.form['title'],
            imgfile=filename
            )
        session.add(addgallery)
        # flash('New Gallery {} Successfully Created'.format(addgallery.title))
        session.commit()
        return redirect(url_for('showGalleries'))
    else:
        return render_template('newgallery.html')


# NOTE: Edit gallery

@app.route('/gallery/<int:gallery_id>/edit/', methods=['GET', 'POST'])
def editGallery(gallery_id):
    if 'username' not in login_session:
        return redirect('/login')
    editgallery = session.query(Gallery).filter_by(id=gallery_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editgallery.title = request.form['title']
            flash('Gallery edited {} Successfully'.format(editgallery.title))
            return redirect(url_for('showGalleries'))
    else:
        return render_template('editgallery.html', gallery=editgallery)


# NOTE: Delete gallery

@app.route('/gallery/<int:gallery_id>/delete/', methods=['GET', 'POST'])
def deleteGallery(gallery_id):
    if 'username' not in login_session:
        return redirect('/login')
    deletegallery = session.query(Gallery).filter_by(id=gallery_id).one()
    if request.method == 'POST':
        session.delete(deletegallery)
        flash('Gallery {} Successfully Deleted'.format(deletegallery.title))
        session.commit()
        return redirect(url_for('showGalleries'))
    else:
        return render_template('deletegallery.html', gallery=deletegallery)


####################
# Pictures Section #
####################

# NOTE: Pictures from gallery presentation

@app.route('/gallery/<int:gallery_id>/')
@app.route('/gallery/<int:gallery_id>/pictures/')
def showPictures(gallery_id):
    pictures = session.query(Pictures).filter_by(gallery_id=gallery_id).all()
    gallery = session.query(Gallery).filter_by(id=gallery_id).one()
    return render_template(
        'pictures.html', pictures=pictures,
        gallery=gallery, gallery_id=gallery_id
        )


# NOTE: Add New Picture

@app.route('/gallery/<int:gallery_id>/new/', methods=['GET', 'POST'])
@app.route('/gallery/<int:gallery_id>/picture/new/', methods=['GET', 'POST'])
def newPicture(gallery_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        addpicture = Pictures(
            title=request.form['title'],
            imgfile=request.form['imgfile'],
            gallery_id=gallery_id
            )
        file = request.files['pic']
        filename = request.form['imgfile']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session.add(addpicture)
        # flash('New Gallery {} Successfully Created'.format(addgallery.title))
        session.commit()
        return redirect(url_for('showPictures', gallery_id=gallery_id))
    else:
        return render_template('newpicture.html', gallery_id=gallery_id)


# NOTE: Edit Picture

@app.route(
    '/gallery/<int:gallery_id>/<int:picture_id>/edit/',
    methods=['GET', 'POST']
    )
@app.route(
    '/gallery/<int:gallery_id>/picture/<int:picture_id>/edit/',
    methods=['GET', 'POST']
    )
def editPicture(picture_id, gallery_id):
    if 'username' not in login_session:
        return redirect('/login')
    editpicture = session.query(Pictures).filter_by(id=picture_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editpicture.title = request.form['title']
            flash('Picture edited {} Successfully'.format(editpicture.title))
            return redirect(url_for('showPictures', gallery_id=gallery_id))
    else:
        return render_template(
            'editPicture.html', picture=editpicture, gallery_id=gallery_id
            )


# NOTE: Delete Picture

@app.route(
    '/gallery/<int:gallery_id>/<int:picture_id>/delete/',
    methods=['GET', 'POST']
    )
@app.route(
    '/gallery/<int:gallery_id>/picture/<int:picture_id>/delete/',
    methods=['GET', 'POST']
    )
def deletePicture(picture_id, gallery_id):
    if 'username' not in login_session:
        return redirect('/login')
    gallery = session.query(Gallery).filter_by(id=gallery_id).one()
    deletepicture = session.query(Pictures).filter_by(id=picture_id).one()
    if request.method == 'POST':
        session.delete(deletepicture)
        flash('Picture {} Successfully Deleted'.format(deletepicture.title))
        session.commit()
        return redirect(url_for('showPictures', gallery_id=gallery_id))
    else:
        return render_template(
            'deletepicture.html', picture=deletepicture, gallery_id=gallery_id
            )


########################
# Picture Presentation #
########################

# NOTE: Individual pictures presentation

@app.route('/gallery/<int:gallery_id>/<int:picture_id>/')
@app.route('/gallery/<int:gallery_id>/<int:picture_id>/pictures/')
def showPicture(gallery_id, picture_id):
    picture = session.query(Pictures).filter_by(id=picture_id).one()
    gallery = session.query(Gallery).filter_by(id=gallery_id).one()
    return render_template('picture.html', picture=picture, gallery=gallery)


##################
# Log-in section #
##################

# NOTE: Login page

@app.route('/login/')
def showLogin():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for x in xrange(32)
        )
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# NOTE: Google Login connection

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads((h.request(url, 'GET')[1]).decode())
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(regsult.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # See if a user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;'
    output += '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# NOTE: Disconnect based on provider

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']  # NOQA
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


###########################
# User creation functions #
###########################

# NOTE: create user

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# NOTE: Get info from user table

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# NOTE: Check user email


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:  # NOQA
        return None


################################
# JSON Information definitions #
################################

# NOTE JSON APIs to view Gallery Information

@app.route('/gallery/<int:gallery_id>/JSON')
def galleryJSON(gallery_id):
    gallery = session.query(Gallery).filter_by(id=gallery_id).one()
    pictures = session.query(Pictures).filter_by(
        gallery_id=gallery_id).all()
    return jsonify(pictures=[picture.serialize for picture in pictures])


# NOTE JSON APIs to view picture Information

@app.route('/gallery/<int:gallery_id>/<int:picture_id>/JSON')
def pictureJSON(gallery_id, picture_id):
    picture = session.query(Pictures).filter_by(id=picture_id).one()
    return jsonify(picture=picture.serialize)


# NOTE JSON APIs to view galleries Information

@app.route('/gallery/JSON')
def galleriesJSON():
    galleries = session.query(Gallery).all()
    return jsonify(galleries=[gallery.serialize for gallery in galleries])


if __name__ == '__main__':
    app.run()
