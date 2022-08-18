web: python fetch_metadata/manage.py runserver 0.0.0.0:$PORT --settings=fetch_metadata.herokusettings
release: python fetch_metadata/manage.py migrate accounts zero --settings=fetch_metadata.herokusettings
release: python fetch_metadata/manage.py migrate file_control zero --settings=fetch_metadata.herokusettings
release: python fetch_metadata/manage.py migrate commons zero --settings=fetch_metadata.herokusettings
release: python fetch_metadata/manage.py migrate --settings=fetch_metadata.herokusettings