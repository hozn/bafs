# Your settings

SQLALCHEMY_DATABASE_URI = 'mysql://bafs@localhost/bafs?charset=utf8'

# Need a Strava Client ID and secret in order to authorize users
#STRAVA_CLIENT_ID = ''
#STRAVA_CLIENT_SECRETE = ''

# The strava team (club) IDs
BAFS_TEAMS = [
              46292, # Team 0
              46334, # Team ??
              46418, # Team 3
              46225, # Team 4
              
              46402, # Team 6
              46246, # Team 7
              46209, # Team 8
              46202, # Team 9
              ]

# When does the competition start?
BAFS_START_DATE = '2014-01-01'

# When does the competition end?  (This can be an exact time; API will stop fetching after this time.)
BAFS_END_DATE = '2014-03-19 21:30:00-04:00'

# Keywords to exclude from ride titles
BAFS_EXCLUDE_KEYWORDS = ['#NoBAFS']