## 테이블 구조
![테이블 구조](https://github.com/awds1236/post_breadcrumbs/assets/102665306/9ea0ed2a-38b1-46d6-8bfb-41742e20e898)

## 비지니스 로직
1. 게시물 목록 조회 (post_list)
> * 모든 게시물 중 부모 페이지 id(parant_page_id)가 NULL인 게시물만 조회   
> * 조회된 게시물들은 post_list.html 템플릿으로 전달
2. 부모 게시물 생성 (create_post)
> * POST 요청을 통해 제목과 내용을 받아 새로운 게시물을 생성   
> * 게시물 생성 후에는 게시물 목록 페이지(post_list.html)로 리다이렉트
3. 브레드크럼즈 생성 (get_breadcrumbs)
> * 현재 게시물 ID로부터 부모 게시물을 추적 (parant_page_id)
> * 현재 게시물 ID부터 추적된 부모 게시물의 ID를 리스트에 저장 
> * 가장 처음의 게시물부터 현재 게시물 순으로 정렬해서 반환
4. 게시물 상세 조회 및 서브 페이지 조회 (post_detail)
> * 주어진 게시물 ID에 해당하는 게시물의 상세 정보를 조회   
> * 해당 게시물의 자식으로 등록된 서브 페이지들도 함께 조회
> * 브레드크럼즈 정보도 함께 생성되어 post_detail.html 템플릿에 전달
5. 서브 페이지 생성 (create_sub_post)
> * 주어진 부모 게시물 ID에 해당하는 게시물 아래에 새로운 서브 페이지를 생성
> * POST 요청을 통해 제목과 내용을 받아 새로운 서브 페이지를 생성, 생성 시 부모 게시물 ID가 함께 저장
> * 서브 페이지 생성 후에는 해당 부모 게시물의 상세 페이지로 리다이렉트

## 결과 정보
    {   
        "pageId" : 3,   
        "title" : 3,  
        "content" : 3,
        "Parent Page" : ['1','2'],
        "SubPage" : ['4','5'],
        "breadcrumbs" : "1 / 2 / 3"   
    }

