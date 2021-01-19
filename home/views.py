from django.db import models
from django.views import generic
from .models import BlogPost

# Create your views here.
'''def home_view(request):
    qs = BlogPost.objects.all()
    template_name = "home.html"
    context = {'object_list': qs}
    return render(request, template_name, context)
'''


class HomeView(generic.ListView):
    queryset = BlogPost.objects.order_by('-created_at')
    template_name = 'home.html'


'''def read_article(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'read_article.html'
    context = {'object': obj}
    return render(request, template_name, context)

'''


class ReadArticle(generic.DetailView):
    model = BlogPost
    template_name = 'read_article.html'
