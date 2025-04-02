# import feedparser
# import git
# import os

# # 벨로그 RSS 피드 URL
# # example : rss_url = 'https://api.velog.io/rss/@rimgosu'
# rss_url = 'https://api.velog.io/rss/@ehekaanldk'

# # 깃허브 레포지토리 경로
# repo_path = '.'

# # 'velog-posts' 폴더 경로
# posts_dir = os.path.join(repo_path, 'velog-posts')

# # 'velog-posts' 폴더가 없다면 생성
# if not os.path.exists(posts_dir):
#     os.makedirs(posts_dir)

# # 레포지토리 로드
# repo = git.Repo(repo_path)

# # RSS 피드 파싱
# feed = feedparser.parse(rss_url)


# for entry in feed.entries:
#     file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
#     file_path = os.path.join(posts_dir, file_name)

#     if not os.path.exists(file_path):
#         if hasattr(entry, 'content'):
#             content = entry.content[0].value
#         elif hasattr(entry, 'description'):
#             content = entry.description
#         elif hasattr(entry, 'summary'):
#             content = entry.summary
#         else:
#             content = '본문이 없습니다.'

#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(content)

# repo.git.add(all=True)
# repo.git.commit('-m', 'Update Velog posts')
# repo.git.push()

import feedparser
import git
import os
from datetime import datetime
import pprint


# 벨로그 RSS 피드 URL (본인 계정)
rss_url = 'https://api.velog.io/rss/@ehekaanldk'

# 깃허브 레포 경로
repo_path = '.'
posts_dir = os.path.join(repo_path, 'velog-posts')

# 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 깃 레포지토리 로딩
repo = git.Repo(repo_path)
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    # 제목 기반으로 파일 이름 만들기
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'

    # 시리즈명 (없으면 Uncategorized)
    series = entry.tags[0]['term'] if hasattr(entry, 'tags') and entry.tags else 'Uncategorized'
    series_dir = os.path.join(posts_dir, series)

    if not os.path.exists(series_dir):
        os.makedirs(series_dir)

    file_path = os.path.join(series_dir, file_name)

    # 본문 내용 가져오기
    if hasattr(entry, 'content'):
        content = entry.content[0].value
    elif hasattr(entry, 'description'):
        content = entry.description
    elif hasattr(entry, 'summary'):
        content = entry.summary
    else:
        content = '본문이 없습니다.'

    # 날짜 포맷: 2024-04-02
    published = datetime(*entry.published_parsed[:3]).strftime('%Y-%m-%d')

    # 메타데이터 포함된 마크다운 내용
    markdown = f"""---
title: "{entry.title}"
date: "{published}"
link: "{entry.link}"
series: "{series}"
---

{content}
"""

    # 무조건 덮어쓰기 (수정 반영)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(markdown)

# 깃 커밋 & 푸시
repo.git.add(all=True)
repo.git.commit('-m', 'Update Velog posts')  # 변경사항 없을 땐 에러 나도 무시됨
repo.git.push()
