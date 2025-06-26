from django.views.generic import CreateView, DetailView, ListView, UpdateView, base
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Repeat

def RepeatTable(request):
    items = Repeat.objects.all()
    return render(request, "repeatTable.html", {"repeats": items})

# class RepeatDetailView(DetailView):
#   """renders html for single protein page"""
  
#   # slug_field = 'gene'
#   model = ProteinTF
#   context_object_name = 'protein'   # name for the data that will be used by template
#   queryset = ProteinTF.objects
#   template_name = 'proteins/proteinPage.html'
 
#   def get_object(self, query_set=None):
#      # print(self.kwargs['slug'])
#      if query_set is None:
#            query_set = self.get_queryset()
#      # print(self.kwargs['slug'])
#      # print(ProteinTF.objects.get(gene=self.kwargs['slug']))
#      obj = ProteinTF.objects.get(gene=self.kwargs['gene'])
#      # print(query_set.get(gene=self.kwargs['slug']))
#      # obj = query_set.get(gene=self.kwargs['slug'])
#      # obj = queryset.get(uuid=self.kwargs.get("slug", "").upper())
#      return obj

#   def get(self, request, *args, **kwargs):
#      self.object = self.get_object()
#      # print(self.object)
#      context = self.get_context_data(object=self.object)
#      # print(context['protein'].satellite)
#      return render(request, 'proteins/proteinPage.html', context)
   
#      # context = {'protein': obj}
#      # return render(request, 'proteins/proteinPage.html', context)
 
#   def get_context_data(self, **kwargs):
#      data = super().get_context_data(**kwargs)
#      return data

