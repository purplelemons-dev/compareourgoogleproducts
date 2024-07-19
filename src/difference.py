apps1 = """Access Log Activity
Alerts
Android Device Configuration Service
Arts & Culture
Assignments
Business messages
Calendar
Chrome
Classic Sites
Classroom
Contacts
Crisis User Reports
Data Shared for Research
Discover
Drive
Fit
Fitbit
Google Account
Google Business Profile
Google Chat
Google Cloud Search
Google Developers
Google Feedback
Google Fi Wireless
Google Finance
Google Help Communities
Google One
Google Pay
Google Photos
Google Play Books
Google Play Games Services
Google Play Movies & TV
Google Play Store
Google Podcasts
Google Shopping
Google Store
Google Translator Toolkit
Google Workspace Marketplace
Groups
Home App
Keep
Location History (Timeline)
Mail
Maps
Maps (your places)
My Activity
My Maps
News
Phone Audio
Pinpoint
Profile
Purchases & Reservations
Recorder
Reminders
Saved
Search Contributions
Search Notifications
Street View
Tasks
Voice
YouTube and YouTube Music"""

apps2 = """Access Log Activity
Alerts
Android Device Configuration Service
Arts & Culture
Assignments
Calendar
Chrome
Classroom
Contacts
Crisis User Reports
Data Shared for Research
Discover
Drive
Fit
Google Account
Google Business Profile
Google Chat
Google Cloud Search
Google Developers
Google Finance
Google Help Communities
Google Pay
Google Photos
Google Play Books
Google Play Console
Google Play Games Services
Google Play Movies & TV
Google Play Store
Google Podcasts
Google Shopping
Google Store
Google Translator Toolkit
Google Workspace Marketplace
Groups
Home App
Keep
Location History (Timeline)
Mail
Maps
Maps (your places)
My Activity
News
Phone Audio
Pinpoint
Profile
Purchases & Reservations
Reminders
Saved
Search Contributions
Search Notifications
Street View
Tasks
Voice
YouTube and YouTube Music"""


apps1set = {i for i in apps1.split("\n") if i}
apps2set = {i for i in apps2.split("\n") if i}

difference = apps1set - apps2set

print(f"{difference= }")
print(f"{len(difference)= }")
