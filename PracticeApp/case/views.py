from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def countwords(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        word_list = list(filter(lambda x: x.strip(), text.split(' ')))
        word_count = len(word_list)
        return render(request, 'case.html', {'word_count': word_count})
    return render(request, 'case.html')
