from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def pagefun(request):
    all_post = Post.objects.all().order_by('id')
    fm = Paginator(all_post,2,orphans=1)
    # print("-----------",fm)
    page_number = request.GET.get('page')
    print("-----------",page_number)
    
    page_obj = fm.get_page(page_number)
    print("----------->>>>",page_obj)

    return render(request,'page.html',{'form':page_obj,'page_no':page_number})    