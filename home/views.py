from django.views import generic
from django.views.generic import TemplateView

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


class JennPageView(TemplateView):
    template_name = 'jennPage.html'


class AddPostView(generic.CreateView):
    model = BlogPost
    template_name = "addPost.html"
    fields = '__all__'


class DeletePostView(generic.DetailView):
    model = BlogPost
    template_name = 'deletePost.hltm'


class ReadArticle(generic.DetailView):
    model = BlogPost
    template_name = 'read_article.html'
