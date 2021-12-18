from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from footimgapp.models import Footimg
from footimgapp.forms import FootimgCreationForm
from django.utils.decorators import method_decorator
from footimgapp.decorators import footimg_ownership_required
from django.urls import reverse


class FootimgCreateView(CreateView):
    model = Footimg
    context_object_name = "target_footimg"
    form_class = FootimgCreationForm
    template_name = 'footimgapp/create.html'

    def form_valid(self, form):
        temp_footimg = form.save(commit=False)
        temp_footimg.user = self.request.user
        temp_footimg.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(footimg_ownership_required, 'get')
@method_decorator(footimg_ownership_required, 'post')
class FootimgUpdateView(UpdateView):
    model = Footimg
    context_object_name = "target_footimg"
    form_class = FootimgCreationForm
    template_name = 'footimgapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

