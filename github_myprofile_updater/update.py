if __name__ == '__main__':
    _header = '## Hi there 👋'
    base_dir = '../_pages/includes/'
    _intro = open(f'{base_dir}/intro.md').read().strip()
    _homepage = open(f'{base_dir}/homepage.md').read().strip()
    _news = open(f'{base_dir}/news.md').read().strip()
    with open('README.md', 'w') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(_intro)
        f.write('\n\n##')
        f.write(_homepage)
        f.write('\n\n')
        # f.write(_news)
        f.write('<img align="left" src="https://github-readme-stats-one-bice.vercel.app/api?username=ruizhaocv&show_icons=true&include_all_commits=true&count_private=true&role=OWNER,ORGANIZATION_MEMBER,COLLABORATOR&theme=default">')
