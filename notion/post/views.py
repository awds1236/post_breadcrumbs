from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from django.db import connection
from .forms import PostForm

# 게시물 목록 조회
def post_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM post_page WHERE parent_page_id IS NULL")
        posts = cursor.fetchall()

    return render(request, 'post_list.html', {'posts': posts})


# 부모 id를 가져와 브로드크럼즈 생성
def get_breadcrumbs(post_id):
    crumbs = []
    with connection.cursor() as cursor:
        while post_id:
            cursor.execute("SELECT id, title, content, parent_page_id FROM post_page WHERE id = %s", [post_id])
            post = cursor.fetchone()
            if post:
                crumbs.append(post)
                post_id = post[3]  # parent_page_id의 index
            else:
                post_id = None

    return crumbs[::-1]

# 부모 게시물 생성
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO post_page (title, content) VALUES (%s, %s)", [title, content])
            
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

# 게시물 상세 조회, 서브 페이지 조회
def post_detail(request, post_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM post_page WHERE id = %s", [post_id])
        post = cursor.fetchone()

        cursor.execute("SELECT * FROM post_page WHERE parent_page_id = %s", [post_id])
        sub_pages = cursor.fetchall()

    breadcrumbs = get_breadcrumbs(post_id)
    return render(request, 'post_detail.html', {'page': post, 'breadcrumbs': breadcrumbs, 'sub_pages': sub_pages})

# 서브 페이지 생성
def create_sub_post(request, post_id):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO post_page (title, content, parent_page_id) VALUES (%s, %s, %s)", [title, content, post_id])
            
            return redirect('post_detail', post_id=post_id)
    else:
        form = PostForm()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM post_page WHERE id = %s", [post_id])
        parent_post = cursor.fetchone()

    return render(request, 'create_sub_post.html', {'form': form, 'page': parent_post})