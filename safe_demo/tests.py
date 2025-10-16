import pytest
from django.test import Client
from django.urls import reverse
from django.middleware.csrf import CsrfViewMiddleware


@pytest.mark.django_db
class TestSafeDemo:
    def setup_method(self):
        self.client = Client(enforce_csrf_checks=True)

    def test_home_get(self):
        resp = self.client.get(reverse('home'))
        assert resp.status_code == 200
        # CSRF 토큰이 폼에 포함됨
        assert 'csrfmiddlewaretoken' in resp.content.decode('utf-8')

    def test_home_post_echo_requires_csrf(self):
        # CSRF 없는 POST는 403
        resp = self.client.post(reverse('home'), data={'message': 'hello'})
        assert resp.status_code == 403

    def test_search_safe_queryset(self):
        # 검색 페이지는 GET, 템플릿 렌더링
        resp = self.client.get(reverse('search'), {'q': "test"})
        assert resp.status_code == 200
        # 단순 존재 확인
        assert '검색' in resp.content.decode('utf-8')
