# from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_invalid(self, form):
        temp_article = form.save(commit=False)
        temp_article.write = self.request.user
        temp_article.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'





