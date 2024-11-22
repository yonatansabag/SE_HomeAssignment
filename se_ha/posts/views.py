import requests
from django.shortcuts import render


def post_list(request):
    # Fetch all posts from the API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    # As requested, only showing a brief snippet of the body
    for post in posts:
        post['body'] = post['body'][:50] + '...'
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detailed(request, post_id):
    # Fetch a post from the API
    post_response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    post = post_response.json()
    # Fetch the comments of this particular post
    comments_response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    comments = comments_response.json()
    return render(request, 'posts/post_detailed.html', {
        'post': post,
        'comments': comments
    })
