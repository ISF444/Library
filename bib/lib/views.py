from django.shortcuts import render

from .forms import FormBookRegis, FormRegisNewReaders


# def lib_get(request):
#     return render(request, 'lib_page.html')


def book_regis_get(request):
    form = FormBookRegis()
    context = {"form": form}
    if request.method == "POST" and request.FILES:
        form = FormBookRegis(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'lib_page.html', context)


def readers_regis_get(request):
    form = FormRegisNewReaders()
    context = {"form": form}
    if request.method == "POST":
        form = FormRegisNewReaders(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    return render(request, 'regis_new_readers_page.html', context)


