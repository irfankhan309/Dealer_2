from django.shortcuts import render
from DealerApp.models import PostEnquiry
from DealerApp import forms
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index_view(request):
    return render(request,'DealerApp/index.html')


def Engquiry_view(request):
    form=forms.PostForm()
    if request.method == 'POST':
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        form=forms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'DealerApp/thanks.html')
        else:
            form=PostForm()
    my_dic={'form':form}
    return render(request,'DealerApp/sell.html',context=my_dic)



def Service_view(request):
    return render(request,'DealerApp/services.html')


def contact_view(request):
    return render(request,'DealerApp/contact.html')
