
from django.shortcuts import render, redirect
from django.db import connection
from .forms import MessageForm, NoteForm
from .models import Note

# CSRF 미들웨어를 비활성화하여 CSRF에 취약하게 만듦
def index(request):
    message_form = MessageForm(request.POST or None)
    note_form = NoteForm(request.POST or None)
    message_text = None

    # XSS 취약점: 사용자 입력을 템플릿에서 |safe로 출력
    if request.method == 'POST':
        if 'message' in request.POST and message_form.is_valid():
            message_text = message_form.cleaned_data.get('message') or ''
        elif 'text' in request.POST and note_form.is_valid():
            # SQL Injection 취약점: 사용자 입력을 직접 쿼리 문자열에 삽입
            user_text = note_form.cleaned_data['text']
            with connection.cursor() as cursor:
                # 아래 쿼리는 사용자 입력이 그대로 들어가므로 SQL Injection에 취약함
                cursor.execute(f"INSERT INTO safe_demo_note (text, created_at) VALUES ('{user_text}', datetime('now'))")
            return redirect('home')

    # SQL Injection 취약점: 노트 목록도 직접 쿼리로 불러옴
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, text, created_at FROM safe_demo_note ORDER BY created_at DESC LIMIT 10")
        notes = [type('NoteObj', (), {'text': row[1]}) for row in cursor.fetchall()]

    return render(request, 'safe_demo/home.html', {
        'message_form': message_form,
        'note_form': note_form,
        'message_text': message_text,
        'notes': notes,
    })

# SQL Injection 취약점: 검색 기능도 직접 쿼리 문자열에 사용자 입력 삽입
def search(request):
    q = request.GET.get('q', '')
    results = []
    if q:
        with connection.cursor() as cursor:
            # 아래 쿼리는 사용자 입력이 그대로 들어가므로 SQL Injection에 취약함
            cursor.execute(f"SELECT id, text, created_at FROM safe_demo_note WHERE text LIKE '%{q}%' ORDER BY created_at DESC")
            results = [type('NoteObj', (), {'text': row[1]}) for row in cursor.fetchall()]
    return render(request, 'safe_demo/search.html', {'q': q, 'results': results})
