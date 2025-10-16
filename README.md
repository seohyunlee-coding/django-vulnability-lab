# django-vulnability-lab

연구 목적의 프레임워크 보안 비교를 위한 Django 기반 샘플 프로젝트입니다. 의도적으로 "취약한" 코드를 만들거나 공격 페이로드를 배포하지 않습니다. 대신, Django가 제공하는 기본 방어(XSS 자동 이스케이프, ORM 파라미터 바인딩, CSRF 미들웨어)를 작은 데모와 테스트로 확인하고, 실제 취약점 실습은 공개된 학습용 랩(예: OWASP DVWA, Juice Shop, WebGoat 등)과 연동하여 진행하도록 설계합니다.

중요: 본 리포지토리는 공격 기법, 익스플로잇 코드, 의도적 취약 코드 삽입 방법을 제공하지 않습니다. 합법적이고 통제된 환경에서 교육/연구 목적으로만 사용하세요.

## 목표
- 프레임워크 보안 특성 비교 시 기준점 제공: XSS/SQLi/CSRF에 대해 Django의 기본 방어가 어떻게 동작하는지 검증
- 설정 플래그/미들웨어/템플릿/ORM 레이어의 역할을 요약
- 외부 취약 애플리케이션(DVWA 등)과 병행 실습할 때 비교 관찰 포인트 제시

## 구성 개요
- 안전 데모 앱(safe_demo)
	- XSS: 템플릿 자동 이스케이프 동작 확인
	- SQL Injection: ORM의 파라미터 바인딩으로 쿼리 안전성 확인
	- CSRF: 폼 POST 시 CSRF 토큰 검증 확인
- 테스트: 위 동작을 단위 테스트로 검증(공격 페이로드 제공 없음)

## 실행(로컬)
1) Python 3.10+ 권장. 가상환경 생성 후 의존성 설치
2) Django 프로젝트 초기화 후 서버/테스트 실행

자세한 실행 방법은 아래 "How to run" 섹션을 참조하세요.

## 외부 학습용 랩(권장)
- OWASP DVWA: 의도적 취약점 실습용 PHP 앱
- OWASP Juice Shop: 현대적 웹 취약점 학습용
- WebGoat: OWASP 유지 자바 기반 학습용

이 리포지토리의 데모와 테스트로 프레임워크 방어 동작을 이해한 뒤, 위 랩에서 공격 실습을 수행하고 결과를 비교/분석하는 방식으로 연구를 진행하세요.

## How to run (요약)
아래 명령은 PowerShell 기준 예시입니다.

```powershell
# (선택) 가상환경 생성
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# 의존성 설치
pip install -r requirements.txt

# 장고 프로젝트 초기화(최초 1회만)
python -m django startproject labsite .
python manage.py startapp safe_demo

# 마이그레이션/서버/테스트
python manage.py migrate
python manage.py runserver
pytest -q
```

Windows에서 실행 시 경로 구분자는 `\`를 사용하세요. 가상환경 활성화 스크립트는 `Activate.ps1`입니다.

## 주의 및 윤리 가이드
- 회사/학교/허가받지 않은 시스템에 대한 테스트는 금지합니다.
- 공격 자동화/익스플로잇 제작은 본 리포지토리의 범위 밖입니다.
- 목적은 프레임워크의 방어 메커니즘을 이해하고 안전한 코딩 습관을 학습하는 것입니다.

