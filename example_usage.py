import mparticle
import calendar
import time

batch = mparticle.Batch()
batch.environment = 'development'

identities = mparticle.UserIdentities()
identities.customerid = '123456'
identities.email = 'user@example.com'
batch.user_identities = identities

device_info = mparticle.DeviceInformation()
# set any IDs that you have for this user
device_info.ios_advertising_id = '07d2ebaa-e956-407e-a1e6-f05f871bf4e2'
device_info.android_advertising_id = 'a26f9736-c262-47ea-988b-0b0504cee874'
batch.device_info = device_info

# arbitrary example allowing you to create a segment of users trial users
batch.user_attributes = {'Account type': 'trial', 'TrialEndDate': '2016-12-01'}

ccpa_consent_state = mparticle.CCPAConsentState()
ccpa_consent_state.document = 'document_agreement.v3'
ccpa_consent_state.consented = True
ccpa_consent_state.timestamp_unixtime_ms = calendar.timegm(time.gmtime())
ccpa_consent_state.location = 'mparticle.test/signup'
ccpa_consent_state.hardware_id = 'IDFA:a5d96n32-224a-3b11-1088-a202695bc710'

gdpr_consent_state = mparticle.GDPRConsentState()
gdpr_consent_state.document = 'document_agreement.v2'
gdpr_consent_state.consented = True
gdpr_consent_state.timestamp_unixtime_ms = calendar.timegm(time.gmtime())
gdpr_consent_state.location = 'dtmgbank.com/signup'
gdpr_consent_state.hardware_id = 'IDFA:a5d934n0-232f-4afc-2e9a-3832d95zc702'

consent_state = mparticle.ConsentState()
# Workspace Settings > Workspace > Regulations
# https://docs.mparticle.com/guides/consent-management/
consent_state.ccpa = {'data_sale_opt_out': ccpa_consent_state}
consent_state.gdpr = {'document_agreement': gdpr_consent_state}

batch.consent_state = consent_state

app_event = mparticle.AppEvent('Example', 'navigation')
app_event.timestamp_unixtime_ms = 1552596256103
app_event.custom_flags = {
    'answer': 42,
    'question': 'What is the answer to life, the universe, and everything?',
    'dolphins': [
        'So long',
        'Thanks for all the fish'
    ]
}

product = mparticle.Product()
product.name = 'Example Product'
product.id = 'sample-sku'
product.price = 19.99

product_action = mparticle.ProductAction('purchase')
product_action.products = [product]
product_action.tax_amount = 1.50
product_action.total_amount = 21.49

commerce_event = mparticle.CommerceEvent(product_action)
commerce_event.timestamp_unixtime_ms = 1552596256103

session_start = mparticle.SessionStartEvent()
session_start.session_id = 12345678
session_start.timestamp_unixtime_ms = 1552596256103

session_end = mparticle.SessionEndEvent()
session_end.session_id = session_start.session_id  # its mandatory that these match
session_end.session_duration_ms = 10000
session_end.timestamp_unixtime_ms = 1552596266103 + 10000

screen_view_event = mparticle.ScreenViewEvent()
screen_view_event.custom_flags = {
    "foo": 'bar',
    'answer': 42,
    'arrays': [
        'foo', 'bar', 'baz'
    ]
}

batch.events = [session_start, app_event, commerce_event, session_end]

batch.mpid = '600868121729048600'
batch.mp_deviceid = '59780f39-d7a0-4ebe-9950-280f937c29e2'

install = mparticle.ApplicationStateTransitionEvent.create_install_event()
install.timestamp_unixtime_ms = 1552596256103

upgrade = mparticle.ApplicationStateTransitionEvent.create_upgrade_event()
upgrade.timestamp_unixtime_ms = 1552596256103

foreground = mparticle.ApplicationStateTransitionEvent.create_foreground_event()
foreground.timestamp_unixtime_ms = 1552596256103

background = mparticle.ApplicationStateTransitionEvent.create_background_event()
background.timestamp_unixtime_ms = 1552596256103

configuration = mparticle.Configuration()
configuration.api_key = 'foo-key'
configuration.api_secret = 'foo-secret'
configuration.debug = True  # enable logging of HTTP traffic
api_instance = mparticle.EventsApi(configuration)

try:
    api_instance.upload_events(batch)
    # you can also send multiple batches at a time to decrease the amount of network calls
    # api_instance.bulk_upload_events([batch, batch])
except mparticle.rest.ApiException as e:
    print "Exception while calling mParticle: %s\n" % e
