from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all().order_by("title")
    return render(request, "movies/video_list.html", {"videos": videos})

def video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("video_list")
    else:
        form = VideoForm()
    return render(request, "movies/video_form.html", {"form": form, "mode": "Add"})

def video_detail(request, movie_id):
    video = get_object_or_404(Video, movie_id=movie_id)
    return render(request, "movies/video_detail.html", {"video": video})

def video_update(request, movie_id):
    video = get_object_or_404(Video, movie_id=movie_id)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            # movie_id may have changed; redirect using the new one
            return redirect("video_detail", movie_id=form.instance.movie_id)
    else:
        form = VideoForm(instance=video)
    return render(request, "movies/video_form.html", {"form": form, "mode": "Edit"})

def video_delete(request, movie_id):
    video = get_object_or_404(Video, movie_id=movie_id)
    if request.method == "POST":
        video.delete()
        return redirect("video_list")
    return render(request, "movies/video_confirm_delete.html", {"video": video})
