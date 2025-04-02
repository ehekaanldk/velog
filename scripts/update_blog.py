

import feedparser
import git
import os
from datetime import datetime

# Git repo
repo_path = '.'
repo = git.Repo(repo_path)

# ✅ Git user 설정 추가
repo.git.config('--global', 'user.email', 'github-actions[bot]@users.noreply.github.com')
repo.git.config('--global', 'user.name', 'github-actions[bot]')

# Velog RSS 주소
rss_url = 'https://api.velog.io/rss/@ehekaanldk'

# 프로젝트 루트 경로
repo_path = '.'
posts_dir = os.path.join(repo_path, 'velog-posts')

if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

repo = git.Repo(repo_path)
feed = feedparser.parse(rss_url)

# 파일이 이미 존재하는지 velog-posts 하위 전체 탐색
def file_already_exists(base_dir, file_name):
    for root, dirs, files in os.walk(base_dir):
        if file_name in files:
            return os.path.join(root, file_name)  # 경로 반환
    return None

for entry in feed.entries:
    # 파일 이름 생성
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'

    # 본문 내용
    if hasattr(entry, 'content'):
        content = entry.content[0].value
    elif hasattr(entry, 'description'):
        content = entry.description
    elif hasattr(entry, 'summary'):
        content = entry.summary
    else:
        content = '본문이 없습니다.'

    # 작성일자 (예: 2024-04-02)
    published = datetime(*entry.published_parsed[:3]).strftime('%Y-%m-%d')

    # 메타데이터 포함한 마크다운
    series = 'Uncategorized'
    if hasattr(entry, 'tags') and entry.tags:
        series = entry.tags[0]['term']  # 시리즈 또는 태그 중 첫 번째
    markdown = f"""---
title: "{entry.title}"
date: "{published}"
link: "{entry.link}"
series: "{series}"
---

{content}
"""

    # 기존 파일이 있는지 확인
    existing_file = file_already_exists(posts_dir, file_name)

    if existing_file:
        with open(existing_file, 'r', encoding='utf-8') as f:
            old_content = f.read()

        if old_content.strip() == markdown.strip():
            continue  # 내용 같으면 스킵
        else:
            file_path = existing_file  # 수정 → 덮어쓰기
    else:
        # 새 글이면 기본 경로에 저장
        file_path = os.path.join(posts_dir, file_name)

    # 저장
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(markdown)

# Git 커밋 & 푸시
repo.git.add(all=True)
repo.git.commit('-m', 'Update Velog posts')  # 변경 없으면 무시됨
repo.git.push()
