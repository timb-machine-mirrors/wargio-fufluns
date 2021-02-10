## fufluns - Copyright 2019-2021 - deroad

import os
import xml.etree.ElementTree as ET

## http://androidpermissions.com/permission/android.permission.USE_CREDENTIALS

apk_permissions = {
	"android.permission.ACCEPT_HANDOVER": "Allows a calling app to continue a call which was started in another app.",
	"android.permission.ACCESS_BACKGROUND_LOCATION": "Allows an app to access location in the background.",
	"android.permission.ACCESS_CHECKIN_PROPERTIES": "Allows read/write access to the \"properties\" table in the checkin database, to change values that get uploaded.",
	"android.permission.ACCESS_COARSE_LOCATION": "Allows an app to access approximate location.",
	"android.permission.ACCESS_FINE_LOCATION": "Allows an app to access precise location.",
	"android.permission.ACCESS_LOCATION_EXTRA_COMMANDS": "Allows an application to access extra location provider commands.",
	"android.permission.ACCESS_MEDIA_LOCATION": "Allows an application to access any geographic locations persisted in the user's shared collection.",
	"android.permission.ACCESS_NETWORK_STATE": "Allows applications to access information about networks.",
	"android.permission.ACCESS_NOTIFICATION_POLICY": "Marker permission for applications that wish to access notification policy.",
	"android.permission.ACCESS_WIFI_STATE": "Allows applications to access information about Wi-Fi networks.",
	"android.permission.ACCOUNT_MANAGER": "Allows applications to call into AccountAuthenticators.",
	"android.permission.ACTIVITY_RECOGNITION": "Allows an application to recognize physical activity.",
	"android.permission.ADD_VOICEMAIL": "Allows an application to add voicemails into the system.",
	"android.permission.ANSWER_PHONE_CALLS": "Allows the app to answer an incoming phone call.",
	"android.permission.BATTERY_STATS": "Allows an application to collect battery statistics",
	"android.permission.BIND_ACCESSIBILITY_SERVICE": "Must be required by an AccessibilityService, to ensure that only the system can bind to it.",
	"android.permission.BIND_APPWIDGET": "Allows an application to tell the AppWidget service which application can access AppWidget's data.",
	"android.permission.BIND_AUTOFILL_SERVICE": "Must be required by a AutofillService, to ensure that only the system can bind to it.",
	"android.permission.BIND_CALL_REDIRECTION_SERVICE": "Must be required by a CallRedirectionService, to ensure that only the system can bind to it.",
	"android.permission.BIND_CARRIER_MESSAGING_CLIENT_SERVICE": "A subclass of CarrierMessagingClientService must be protected with this permission.",
	"android.permission.BIND_CARRIER_MESSAGING_SERVICE": "This constant was deprecated in API level 23. Use BIND_CARRIER_SERVICES instead",
	"android.permission.BIND_CARRIER_SERVICES": "The system process that is allowed to bind to services in carrier apps will have this permission.",
	"android.permission.BIND_CHOOSER_TARGET_SERVICE": "Must be required by a ChooserTargetService, to ensure that only the system can bind to it.",
	"android.permission.BIND_CONDITION_PROVIDER_SERVICE": "Must be required by a ConditionProviderService, to ensure that only the system can bind to it.",
	"android.permission.BIND_DEVICE_ADMIN": "Must be required by device administration receiver, to ensure that only the system can interact with it.",
	"android.permission.BIND_DREAM_SERVICE": "Must be required by an DreamService, to ensure that only the system can bind to it.",
	"android.permission.BIND_INCALL_SERVICE": "Must be required by a InCallService, to ensure that only the system can bind to it.",
	"android.permission.BIND_INPUT_METHOD": "Must be required by an InputMethodService, to ensure that only the system can bind to it.",
	"android.permission.BIND_MIDI_DEVICE_SERVICE": "Must be required by an MidiDeviceService, to ensure that only the system can bind to it.",
	"android.permission.BIND_NFC_SERVICE": "Must be required by a HostApduService or OffHostApduService to ensure that only the system can bind to it.",
	"android.permission.BIND_NOTIFICATION_LISTENER_SERVICE": "Must be required by an NotificationListenerService, to ensure that only the system can bind to it.",
	"android.permission.BIND_PRINT_SERVICE": "Must be required by a PrintService, to ensure that only the system can bind to it.",
	"android.permission.BIND_QUICK_SETTINGS_TILE": "Allows an application to bind to third party quick settings tiles.",
	"android.permission.BIND_REMOTEVIEWS": "Must be required by a RemoteViewsService, to ensure that only the system can bind to it.",
	"android.permission.BIND_SCREENING_SERVICE": "Must be required by a CallScreeningService, to ensure that only the system can bind to it.",
	"android.permission.BIND_TELECOM_CONNECTION_SERVICE": "Must be required by a ConnectionService, to ensure that only the system can bind to it.",
	"android.permission.BIND_TEXT_SERVICE": "Must be required by a TextService (e.g.",
	"android.permission.BIND_TV_INPUT": "Must be required by a TvInputService to ensure that only the system can bind to it.",
	"android.permission.BIND_VISUAL_VOICEMAIL_SERVICE": "Must be required by a link VisualVoicemailService to ensure that only the system can bind to it.",
	"android.permission.BIND_VOICE_INTERACTION": "Must be required by a VoiceInteractionService, to ensure that only the system can bind to it.",
	"android.permission.BIND_VPN_SERVICE": "Must be required by a VpnService, to ensure that only the system can bind to it.",
	"android.permission.BIND_VR_LISTENER_SERVICE": "Must be required by an VrListenerService, to ensure that only the system can bind to it.",
	"android.permission.BIND_WALLPAPER": "Must be required by a WallpaperService, to ensure that only the system can bind to it.",
	"android.permission.BLUETOOTH": "Allows applications to connect to paired bluetooth devices.",
	"android.permission.BLUETOOTH_ADMIN": "Allows applications to discover and pair bluetooth devices.",
	"android.permission.BLUETOOTH_PRIVILEGED": "Allows applications to pair bluetooth devices without user interaction, and to allow or disallow phonebook access or message access.",
	"android.permission.BODY_SENSORS": "Allows an application to access data from sensors that the user uses to measure what is happening inside his/her body, such as heart rate.",
	"android.permission.BROADCAST_PACKAGE_REMOVED": "Allows an application to broadcast a notification that an application package has been removed.",
	"android.permission.BROADCAST_SMS": "Allows an application to broadcast an SMS receipt notification.",
	"android.permission.BROADCAST_STICKY": "Allows an application to broadcast sticky intents.",
	"android.permission.BROADCAST_WAP_PUSH": "Allows an application to broadcast a WAP PUSH receipt notification.",
	"android.permission.CALL_COMPANION_APP": "Allows an app which implements the InCallService API to be eligible to be enabled as a calling companion app.",
	"android.permission.CALL_PHONE": "Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call.",
	"android.permission.CALL_PRIVILEGED": "Allows an application to call any phone number, including emergency numbers, without going through the Dialer user interface for the user to confirm the call being placed.",
	"android.permission.CAMERA": "Required to be able to access the camera device.",
	"android.permission.CAPTURE_AUDIO_OUTPUT": "Allows an application to capture audio output.",
	"android.permission.CHANGE_COMPONENT_ENABLED_STATE": "Allows an application to change whether an application component (other than its own) is enabled or not.",
	"android.permission.CHANGE_CONFIGURATION": "Allows an application to modify the current configuration, such as locale.",
	"android.permission.CHANGE_NETWORK_STATE": "Allows applications to change network connectivity state.",
	"android.permission.CHANGE_WIFI_MULTICAST_STATE": "Allows applications to enter Wi-Fi Multicast mode.",
	"android.permission.CHANGE_WIFI_STATE": "Allows applications to change Wi-Fi connectivity state.",
	"android.permission.CLEAR_APP_CACHE": "Allows an application to clear the caches of all installed applications on the device.",
	"android.permission.CONTROL_LOCATION_UPDATES": "Allows enabling/disabling location update notifications from the radio.",
	"android.permission.DELETE_CACHE_FILES": "Old permission for deleting an app's cache files, no longer used, but signals for us to quietly ignore calls instead of throwing an exception.",
	"android.permission.DELETE_PACKAGES": "Allows an application to delete packages.",
	"android.permission.DIAGNOSTIC": "Allows applications to RW to diagnostic resources.",
	"android.permission.DISABLE_KEYGUARD": "Allows applications to disable the keyguard if it is not secure.",
	"android.permission.DUMP": "Allows an application to retrieve state dump information from system services.",
	"android.permission.EXPAND_STATUS_BAR": "Allows an application to expand or collapse the status bar.",
	"android.permission.FACTORY_TEST": "Run as a manufacturer test application, running as the root user.",
	"android.permission.FOREGROUND_SERVICE": "Allows a regular application to use Service.startForeground.",
	"android.permission.GET_ACCOUNTS": "Allows access to the list of accounts in the Accounts Service.",
	"android.permission.GET_ACCOUNTS_PRIVILEGED": "Allows access to the list of accounts in the Accounts Service.",
	"android.permission.GET_PACKAGE_SIZE": "Allows an application to find out the space used by any package.",
	"android.permission.GET_TASKS": "This constant was deprecated in API level 21. No longer enforced.",
	"android.permission.GLOBAL_SEARCH": "This permission can be used on content providers to allow the global search system to access their data.",
	"android.permission.INSTALL_LOCATION_PROVIDER": "Allows an application to install a location provider into the Location Manager.",
	"android.permission.INSTALL_PACKAGES": "Allows an application to install packages.",
	"android.permission.INSTALL_SHORTCUT": "Allows an application to install a shortcut in Launcher.",
	"android.permission.INSTANT_APP_FOREGROUND_SERVICE": "Allows an instant app to create foreground services.",
	"android.permission.INTERNET": "Allows applications to open network sockets.",
	"android.permission.KILL_BACKGROUND_PROCESSES": "Allows an application to call ActivityManager.killBackgroundProcesses(String).",
	"android.permission.LOCATION_HARDWARE": "Allows an application to use location features in hardware, such as the geofencing api.",
	"android.permission.MANAGE_DOCUMENTS": "Allows an application to manage access to documents, usually as part of a document picker.",
	"android.permission.MANAGE_OWN_CALLS": "Allows a calling application which manages it own calls through the self-managed ConnectionService APIs.",
	"android.permission.MASTER_CLEAR": "Not for use by third-party applications.",
	"android.permission.MEDIA_CONTENT_CONTROL": "Allows an application to know what content is playing and control its playback.",
	"android.permission.MODIFY_AUDIO_SETTINGS": "Allows an application to modify global audio settings.",
	"android.permission.MODIFY_PHONE_STATE": "Allows modification of the telephony state - power on, mmi, etc.",
	"android.permission.MOUNT_FORMAT_FILESYSTEMS": "Allows formatting file systems for removable storage.",
	"android.permission.MOUNT_UNMOUNT_FILESYSTEMS": "Allows mounting and unmounting file systems for removable storage.",
	"android.permission.NFC": "Allows applications to perform I/O operations over NFC.",
	"android.permission.NFC_TRANSACTION_EVENT": "Allows applications to receive NFC transaction events.",
	"android.permission.PACKAGE_USAGE_STATS": "Allows an application to collect component usage statistics",
	"android.permission.PERSISTENT_ACTIVITY": "This constant was deprecated in API level 15. This functionality will be removed in the future; please do not use. Allow an application to make its activities persistent.",
	"android.permission.PROCESS_OUTGOING_CALLS": "This constant was deprecated in API level 29. Applications should use CallRedirectionService instead of the Intent.ACTION_NEW_OUTGOING_CALL broadcast.",
	"android.permission.READ_CALENDAR": "Allows an application to read the user's calendar data.",
	"android.permission.READ_CALL_LOG": "Allows an application to read the user's call log.",
	"android.permission.READ_CONTACTS": "Allows an application to read the user's contacts data.",
	"android.permission.READ_EXTERNAL_STORAGE": "Allows an application to read from external storage.",
	"android.permission.READ_INPUT_STATE": "This constant was deprecated in API level 16. The API that used this permission has been removed.",
	"android.permission.READ_LOGS": "Allows an application to read the low-level system log files.",
	"android.permission.READ_PHONE_NUMBERS": "Allows read access to the device's phone number(s).",
	"android.permission.READ_PHONE_STATE": "Allows read only access to phone state, including the phone number of the device, current cellular network information, the status of any ongoing calls, and a list of any PhoneAccounts registered on the device.",
	"android.permission.READ_PROFILE": "Allows the app to read personal profile information stored on your device, such as your name and contact information. This means the app can identify you and may send your profile information to others.",
	"android.permission.READ_SMS": "Allows an application to read SMS messages.",
	"android.permission.READ_SYNC_SETTINGS": "Allows applications to read the sync settings.",
	"android.permission.READ_SYNC_STATS": "Allows applications to read the sync stats.",
	"android.permission.READ_VOICEMAIL": "Allows an application to read voicemails in the system.",
	"android.permission.REBOOT": "Required to be able to reboot the device.",
	"android.permission.RECEIVE_BOOT_COMPLETED": "Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting.",
	"android.permission.RECEIVE_MMS": "Allows an application to monitor incoming MMS messages.",
	"android.permission.RECEIVE_SMS": "Allows an application to receive SMS messages.",
	"android.permission.RECEIVE_WAP_PUSH": "Allows an application to receive WAP push messages.",
	"android.permission.RECORD_AUDIO": "Allows an application to record audio.",
	"android.permission.REORDER_TASKS": "Allows an application to change the Z-order of tasks.",
	"android.permission.REQUEST_COMPANION_RUN_IN_BACKGROUND": "Allows a companion app to run in the background.",
	"android.permission.REQUEST_COMPANION_USE_DATA_IN_BACKGROUND": "Allows a companion app to use data in the background.",
	"android.permission.REQUEST_DELETE_PACKAGES": "Allows an application to request deleting packages.",
	"android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS": "Permission an application must hold in order to use Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS.",
	"android.permission.REQUEST_INSTALL_PACKAGES": "Allows an application to request installing packages.",
	"android.permission.REQUEST_PASSWORD_COMPLEXITY": "Allows an application to request the screen lock complexity and prompt users to update the screen lock to a certain complexity level.",
	"android.permission.RESTART_PACKAGES": "This constant was deprecated in API level 15. The ActivityManager.restartPackage(String) API is no longer supported.",
	"android.permission.SEND_RESPOND_VIA_MESSAGE": "Allows an application (Phone) to send a request to other applications to handle the respond-via-message action during incoming calls.",
	"android.permission.SEND_SMS": "Allows an application to send SMS messages.",
	"android.permission.SET_ALARM": "Allows an application to broadcast an Intent to set an alarm for the user.",
	"android.permission.SET_ALWAYS_FINISH": "Allows an application to control whether activities are immediately finished when put in the background.",
	"android.permission.SET_ANIMATION_SCALE": "Modify the global animation scaling factor.",
	"android.permission.SET_DEBUG_APP": "Configure an application for debugging.",
	"android.permission.SET_PREFERRED_APPLICATIONS": "This constant was deprecated in API level 15. No longer useful, see PackageManager.addPackageToPreferred(String) for details.",
	"android.permission.SET_PROCESS_LIMIT": "Allows an application to set the maximum number of (not needed) application processes that can be running.",
	"android.permission.SET_TIME": "Allows applications to set the system time.",
	"android.permission.SET_TIME_ZONE": "Allows applications to set the system time zone.",
	"android.permission.SET_WALLPAPER": "Allows applications to set the wallpaper.",
	"android.permission.SET_WALLPAPER_HINTS": "Allows applications to set the wallpaper hints.",
	"android.permission.SIGNAL_PERSISTENT_PROCESSES": "Allow an application to request that a signal be sent to all persistent processes.",
	"android.permission.SMS_FINANCIAL_TRANSACTIONS": "Allows financial apps to read filtered sms messages.",
	"android.permission.START_VIEW_PERMISSION_USAGE": "Allows the holder to start the permission usage screen for an app.",
	"android.permission.STATUS_BAR": "Allows an application to open, close, or disable the status bar and its icons.",
	"android.permission.SYSTEM_ALERT_WINDOW": "Allows an app to create windows using the type WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY, shown on top of all other apps.",
	"android.permission.TRANSMIT_IR": "Allows using the device's IR transmitter, if available.",
	"android.permission.UNINSTALL_SHORTCUT": "Allows an application to uninstall a shortcut in Launcher.",
	"android.permission.UPDATE_DEVICE_STATS": "Allows an application to update device statistics.",
	"android.permission.USE_BIOMETRIC": "Allows an app to use device supported biometric modalities.",
	"android.permission.USE_CREDENTIALS": "Allows the app to request authentication tokens.",
	"android.permission.USE_FINGERPRINT": "This constant was deprecated in API level 28. Applications should request USE_BIOMETRIC instead",
	"android.permission.USE_FULL_SCREEN_INTENT": "Required for apps targeting Build.VERSION_CODES.Q that want to use notification full screen intents.",
	"android.permission.USE_SIP": "Allows an application to use SIP service.",
	"android.permission.VIBRATE": "Allows access to the vibrator.",
	"android.permission.WAKE_LOCK": "Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming.",
	"android.permission.WRITE_APN_SETTINGS": "Allows applications to write the apn settings and read sensitive fields of an existing apn settings like user and password.",
	"android.permission.WRITE_CALENDAR": "Allows an application to write the user's calendar data.",
	"android.permission.WRITE_CALL_LOG": "Allows an application to write (but not read) the user's call log data.",
	"android.permission.WRITE_CONTACTS": "Allows an application to write the user's contacts data.",
	"android.permission.WRITE_EXTERNAL_STORAGE": "Allows an application to write to external storage.",
	"android.permission.WRITE_GSERVICES": "Allows an application to modify the Google service map.",
	"android.permission.WRITE_SECURE_SETTINGS": "Allows an application to read or write the secure system settings.",
	"android.permission.WRITE_SETTINGS": "Allows an application to read or write the system settings.",
	"android.permission.WRITE_SYNC_SETTINGS": "Allows applications to write the sync settings.",
	"android.permission.WRITE_VOICEMAIL": "Allows an application to modify and remove existing voicemails in the system.",
	"com.google.android.c2dm.permission.RECEIVE": "Google Cloud Messaging permission required to receive messages from the cloud",
}

safe_protection_level = [
	"normal",
	"signature",
	"signatureOrSystem",
	"signature|privileged",
]

UNSAFE_PERM_ISSUE       = "Found user-based permissions with unsafe protection level in the AndroidManifest."
UNSAFE_PERM_DESCRIPTION = "Creates a potential risk when the system is granting the permission to an application requesting it. "
UNSAFE_PERM_SEVERITY    = 7.7

def ga(d, k, default=None):
	k = "{http://schemas.android.com/apk/res/android}" + k
	if k in d.attrib:
		return d.attrib[k]
	return default

def run_tests(apk, pipes, u, rzh, au):
	insecure = []
	manifest = os.path.join(apk.apktool, "AndroidManifest.xml")
	root = ET.parse(manifest).getroot()

	permissions = root.findall("uses-permission")
	for tag in permissions:
		perm = ga(tag, "name", "")
		if len(perm) > 0:
			if perm in apk_permissions:
				u.permission(apk, perm, apk_permissions[perm])
			else:
				u.permission(apk, perm, "unknown permission.")
				plvl = ga(tag, "protectionLevel", "")
				if len(plvl) > 0 and plvl not in safe_protection_level:
					insecure.append(perm)
			
	permissions = root.findall("permission")
	for tag in permissions:
		perm = ga(tag, "name", "")
		u.permission(apk, perm, "unknown permission.")
		plvl = ga(tag, "protectionLevel", "")
		if len(plvl) > 0 and plvl not in safe_protection_level:
			insecure.append(tag)

	if len(insecure) > 0:
		u.test(apk, False, UNSAFE_PERM_ISSUE, UNSAFE_PERM_DESCRIPTION, UNSAFE_PERM_SEVERITY)

def name_test():
	return "Detection AndroidManifest.xml permissions"
