from django.shortcuts import render
from django.views import generic
from .models import Post, Photo
from .forms import TitlePhotoForm

#from .models import Image


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DeleteView):
    model = Post
    template_name = 'post_detail.html'

def photo_create(request):
    template_name = 'photo_form.html'
    form = TitlePhotoForm(request.POST or None)

    if request.method == 'POST':
        photos = request.FILES.getlist('photo')  # pega vários arquivos.

        if form.is_valid():
            title = form.save()

            for photo in photos:
                Photo.objects.create(title=title, photo=photo)

            return redirect('post_detail', title.pk)

    context = {'form': form}
    return render(request, template_name, context)


#def image_upload_view(request):
#    """Process images uploaded by users"""
#    if request.method == 'POST':
#        form = ImageForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            #Get the current instance object to display in the template
#            img_obj = form.instance
#            return render(request, 'postagem.html', {'form': form, 'img_obj': img_obj})
#    else:
#        form = ImageForm()
#    return render(request, 'postagem.html', {'form': form})

