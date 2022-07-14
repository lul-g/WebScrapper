from random import betavariate
from turtle import pos
from bs4 import BeautifulSoup
from bs4.builder import SAXTreeBuilder
import requests
import time
import smtplib
from email.message import EmailMessage


url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
                   ).text
soup = BeautifulSoup(url, 'lxml')


# girma0
# ltzosxbrtgcneldo

def send_email(new_job):
    # get msg content
    from_addr = 'lulsegedgirma10@gmail.com'
    to_addr = 'lulsegedwork@gmail.com'
    subject = 'New JOB list'
    body = 'WAZZZAAA OOOOOUUUUIIIII'

    # make message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    # msg.set_content(body)

    with open(f'Jobs/{new_job}', 'r') as f:
        data = f.read()
        msg.set_content(data)

    # send
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_addr, 'ltzosxbrtgcneldo')
        smtp.send_message(msg)


def find_jobs():
    familiar_skills = []
    word = input('Put Familiar SKILL. 0 to quit\n')
    while word != '0':
        familiar_skills.append(word)
        word = input()

    print(f'Filtiring for jobs with {familiar_skills} skills. . .\n')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        post_date = job.find('span', class_='sim-posted').span.text
        if 'few' in post_date:
            comp_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')
            skill = job.find(
                'span', class_='srp-skills').text.replace('\n', '').replace(' ', '').replace(',', ' ')
            link = job.header.h2.a['href']
            for familiar_skill in familiar_skills:
                if familiar_skill in skill:
                    with open(f'Jobs/{index}.txt', 'w') as f:
                        f.write(f"Company Name: {comp_name.strip()}\n")
                        f.write(f"Required skills: {skill.strip()}\n")
                        f.write(f'APPLY: {link}')
                        f.write('')
                    print(f'File saved: {index}.txt')
                    new_job = f'{index}.txt'
                    send_email(new_job)
                    print('EMAIL sent')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 24 * 60
        print(f'Emailing in {time_wait} minutes. . .')
        time.sleep(time_wait)
