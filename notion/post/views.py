from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .forms import PostForm

# 게시물 목록 조회
def post_list(request):
    posts = Page.objects.filter(parent_page=None)
    return render(request, 'post_list.html', {'posts': posts})

# 브로드 크럼스 (model의 외래키를 사용하여 생성)
def get_breadcrumbs(post):
    crumbs = []
    while post:
        crumbs.append(post)
        post = post.parent_page
    return crumbs[::-1]

# 부모 게시물 생성
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# 게시물 상세 조회, 서브 페이지 조회
def post_detail(request, post_id):
    post = get_object_or_404(Page, id=post_id)
    breadcrumbs = get_breadcrumbs(post)
    sub_pages = Page.objects.filter(parent_page=post)
    return render(request, 'post_detail.html', {'page': post, 'breadcrumbs': breadcrumbs, 'sub_pages': sub_pages})

# 서브 페이지 생성
def create_sub_post(request, post_id):
    parent_post = get_object_or_404(Page, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            sub_post = form.save(commit=False)
            sub_post.parent_page = parent_post
            sub_post.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = PostForm()
    return render(request, 'create_sub_post.html', {'form': form, 'page': parent_post})

