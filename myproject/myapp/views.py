from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm
from moviepy.editor import VideoFileClip
import datetime
from myproject.myapp.models import VideoQueue



def upload(request):
    # Handle file upload
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect('/accounts/login')
    print(request.user.is_authenticated())
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'], videoname=request.POST['videoname'])
            newdoc.save()
            clip = VideoFileClip('media/'+str(newdoc.docfile))
            clip.save_frame('media/frame'+str(newdoc.id)+'.png', t=2)
            newVideo = VideoQueue(videoID=newdoc.id, clipduration=clip.duration, clipurl='frame'+str(newdoc.id)+'.png')
            newVideo.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect('/myapp/index?videoid='+str(newVideo.id))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
def createuser(request):
    if request.method == 'POST':
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
    return render_to_response('createuser.html')

#def login(request):
#    form = UserLoginForm(request.POST or None)
#    if form.is_valid():
#        username = form.cleaned_data.get("username")
#        password = form.cleaned_data.get("password")
#        user = authenticate(username=username, password=password)
#        login(request, user)
#        print(request.user.is_authenticated())
#    return render(request, 'login.html', {'form': form})
#
def index(request):
    if 'videoid' in request.GET:
        videoid = request.GET['videoid']
        videoid = VideoQueue.objects.get(pk=videoid)
        fileid = Document.objects.get(pk=videoid.videoID)
        return render(request, 'index.html', {'videotitle': fileid.videoname, 'videoduration': videoid.clipduration, 'videoqueue': videoid.created_at, 'clipurl': videoid.clipurl})
    else: 
        return render(request, 'index.html', {'videotitle': '', 'videoduration': '', 'videoqueue': ''})

def logout_view(request):
    logout(request)
    print(request.user.is_authenticated())
    return HttpResponseRedirect('/accounts/login')
            