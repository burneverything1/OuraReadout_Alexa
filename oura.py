import requests

payload={'access_token': 'VXF4W6JLKPQUKTYKEYW3JFCL4UKKGHQN'}

def last_3_avg(response):
  last_3_scores = []
  for i in range(1, 4):
    last_3_scores.append(response[-1-i]['score'])
  return int(sum(last_3_scores)/3)

def get_sleep_score():
  sleep_stats = {}
  response = requests.get(f'https://api.ouraring.com/v1/sleep', params=payload).json()
  sleep_stats = {
    'score': response['sleep'][-1]['score'],
    '3_avg': last_3_avg(response['sleep'])
  }
  return sleep_stats

def get_activity_score():
  response = requests.get(f'https://api.ouraring.com/v1/activity', params=payload).json()
  activity_stats = {
    'score': response['activity'][-1]['score'],
    '3_avg': last_3_avg(response['activity'])
  }
  return activity_stats

def get_readiness_score():
  response = requests.get(f'https://api.ouraring.com/v1/readiness', params=payload).json()
  readiness_stats = {
    'score': response['readiness'][-1]['score'],
    '3_avg': last_3_avg(response['readiness'])
  }
  return readiness_stats

def get_all_scores():
  sleep_stats = get_sleep_score()
  activity_stats = get_activity_score()
  readiness_stats = get_readiness_score()

  def winner(current, avg):
    if current > avg:
      return 'better'
    elif avg > current:
      return 'worse'

  sleep_str = f'Sleep score is: {sleep_stats["score"]}, {winner(sleep_stats["score"], sleep_stats["3_avg"])} than the three day average of: {sleep_stats["3_avg"]}. '

  activity_str = f'Activity score is: {activity_stats["score"]}, {winner(activity_stats["score"], activity_stats["3_avg"])} than the three day average of: {activity_stats["3_avg"]}. '

  readiness_str = f'Readiness score is: {readiness_stats["score"]}, {winner(readiness_stats["score"], readiness_stats["3_avg"])} than the three day average of: {readiness_stats["3_avg"]}. '

  return {'sleep': sleep_str,
    'activity': activity_str,
    'readiness': readiness_str
  }