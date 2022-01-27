from django.shortcuts import render

# Create your views here.

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def test_job():
    print("定时任务")

scheduler.add_job(test_job, 'interval', seconds=5, id='test_job')
scheduler.start()
print("Scheduler started!")
