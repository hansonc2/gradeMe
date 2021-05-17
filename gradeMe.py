from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess

def grade(driver, repo_name):
    driver.get('https://www.gradescope.com/courses/245333/assignments/1230925/submissions/79488673')
    resubmit_button = driver.find_element_by_xpath('/html/body/div[1]/main/section/ul/li[5]/button')
    resubmit_button.click()
    github_button = driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[2]/form/div[1]/div/div/span[2]/label')
    github_button.click()
    repo_field = driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[2]/form/div[3]/div/div[1]/div/div/input')
    repo_field.send_keys(repo_name)
    branch_field = driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[2]/form/div[3]/div/div[2]/div/div[1]/input')
    branch_field.send_keys('master')
    # submit
    branch_field.send_keys(Keys.ENTER)



def run(*args):
    return subprocess.check_call(['git'] + list(args))

def input_comment():
    print('-' * 50)
    comment = input('Please Enter your comnmit comment: \n')
    print('-' * 50)
    return comment

def commit_n_push():
    comment = input_comment()
    comment = f'{comment}'
    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")

def main():
    commit_n_push()
    print('\n')
    print('Committed! 🎉🎉🎉')
    print('\n')

    print('Submitting to grader 📝')
    print('\n')
    driver = webdriver.Chrome()
    grade(driver)
    driver.close()
    print('✅✅✅ Submitted ✅✅✅')
    print('check your email 📩')


