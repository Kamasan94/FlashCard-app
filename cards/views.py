from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Card
from django.shortcuts import get_object_or_404, redirect
from .forms import CardCheckForm, CardArchiveForm
from django.views.generic import TemplateView

import random

class ArchivedCardListView(ListView):
    model = Card
    queryset = Card.objects.filter(archived=1)
    template_name = "cards/archived_card_list.html"

class CardListView(ListView):
    model = Card
    queryset = Card.objects.filter(archived=0)

class CardCreateView(CreateView):
    model = Card
    template_name = "cards/card_create_form.html"
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")
    
class CardUpdateView(UpdateView):
    model = Card
    template_name = "cards/card_update_form.html"
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-list")
    
class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy("card-list")
    
class CardArchiveView(TemplateView): 
    success_url = reverse_lazy("card-list")
    model = Card
    template_name = "cards/card_archive.html"
    form_class = CardArchiveForm
    
    def post(self, request, *args, **kwargs):
        print("Before archiving")
        card = get_object_or_404(Card, id=self.kwargs["pk"])
        card.archive()
        print("After archiving")
        return redirect("card-list")
    
class CardRestoreView(TemplateView): 
    success_url = reverse_lazy("card-list")
    model = Card
    template_name = "cards/card_restore.html"
    form_class = CardArchiveForm
    
    def post(self, request, *args, **kwargs):
        print("Before restoring")
        card = get_object_or_404(Card, id=self.kwargs["pk"])
        card.restore()
        print("After restoring")
        return redirect("card-list")
        
    
    
class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))