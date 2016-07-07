#! /usr/bin/env sh

set -e

# Archives to download packages from
export SERIES="xenial"
export OUTPUT_DIR="/tmp/apidoc_sources/"
DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

echo $DIR

#### Apps/QML
## QtQML & QtQuick
${DIR}/get_package.py qtdeclarative5-doc-html
${DIR}/manage.py import_qdoc -p -t apps -l qml -r development -s "Language Types" -N QtQml -i ${OUTPUT_DIR}usr/share/qt5/doc/qtqml/qtqml.index
${DIR}/manage.py import_qdoc -p -t apps -l qml -r development -s "Graphical Interface" -n QtQuick -i ${OUTPUT_DIR}usr/share/qt5/doc/qtquick/qtquick.index

## QtMultimedia & QtAudioEngine
${DIR}/get_package.py qtmultimedia5-doc-html
${DIR}/manage.py import_qdoc -p -t apps -l qml -r development -s "Multimedia" -n QtMultimedia -i ${OUTPUT_DIR}usr/share/qt5/doc/qtmultimedia/qtmultimedia.index

## QtSensors
${DIR}/get_package.py qtsensors5-doc-html
${DIR}/manage.py import_qdoc -p -t apps -l qml -r development -s "Device and Sensors" -n QtSensors -i ${OUTPUT_DIR}usr/share/qt5/doc/qtsensors/qtsensors.index

## QtFeedback
${DIR}/get_package.py qtfeedback5-doc-html
${DIR}/manage.py import_qdoc -t apps -l qml -r development -s "Device and Sensors" -n QtFeedback -i ${OUTPUT_DIR}usr/share/qt5/doc/qtfeedback/qtfeedback.index

## QtLocation
${DIR}/get_package.py qtlocation5-doc-html
${DIR}/manage.py import_qdoc -p -t apps -l qml -r development.1 -s "Platform Services" -i ${OUTPUT_DIR}usr/share/qt5/doc/qtlocation/qtlocation.index

## QtOrganizer
${DIR}/get_package.py qtpim5-doc-html
${DIR}/manage.py import_qdoc -t apps -l qml -r development -s "Platform Services" -i ${OUTPUT_DIR}usr/share/qt5/doc/qtorganizer/qtorganizer.index
${DIR}/manage.py import_qdoc -t apps -l qml -r development -s "Platform Services" -i ${OUTPUT_DIR}usr/share/qt5/doc/qtcontacts/qtcontacts.index

## Ubuntu.Components
${DIR}/get_package.py ubuntu-ui-toolkit-doc
${DIR}/manage.py import_qdoc -Pp -t apps -l qml -r development -s "Graphical Interface" -n Ubuntu.Components -i ${OUTPUT_DIR}usr/share/ubuntu-ui-toolkit/doc/html/ubuntuuserinterfacetoolkit.index

## Ubuntu.OnlineAccounts
${DIR}/get_package.py accounts-qml-module-doc
${DIR}/manage.py import_qdoc -Pp -t apps -l qml -r development -s "Platform Services" -N Ubuntu.OnlineAccounts -i ${OUTPUT_DIR}usr/share/accounts-qml-module/doc/html/onlineaccounts-qml-api.index

## Ubuntu.Content
${DIR}/get_package.py libcontent-hub-doc
gunzip -f ${OUTPUT_DIR}usr/share/doc/content-hub/qml/html/ubuntu-content-qml-api.index.gz
${DIR}/manage.py import_qdoc -Pp -t apps -l qml -r development -s "Platform Services" -N Ubuntu.Content -i ${OUTPUT_DIR}usr/share/doc/content-hub/qml/html/ubuntu-content-qml-api.index

# U1db
${DIR}/get_package.py libu1db-qt5-doc
${DIR}/manage.py import_qdoc -p -t apps -l qml -r development -s "Platform Services" -N U1db -i ${OUTPUT_DIR}usr/share/u1db-qt/doc/html/u1db-qt.index

## Ubuntu.DownloadManager
${DIR}/get_package.py libubuntu-download-manager-client-doc
gunzip -f ${OUTPUT_DIR}usr/share/doc/ubuntu-download-manager/qml/html/ubuntu-download-manager-qml-api.index.gz
${DIR}/manage.py import_qdoc -Pp -t apps -l qml -r development -s "Platform Services" -N Ubuntu.DownloadManager -i ${OUTPUT_DIR}usr/share/doc/ubuntu-download-manager/qml/html/ubuntu-download-manager-qml-api.index

## Ubuntu.Web
${DIR}/get_package.py qtdeclarative5-ubuntu-web-plugin-doc
gunzip -f ${OUTPUT_DIR}usr/share/doc/ubuntu-web/html/ubuntuweb.index.gz
${DIR}/manage.py import_qdoc -Pp -t apps -l qml -r development -s "Graphical Interface" -N Ubuntu.Web -i ${OUTPUT_DIR}usr/share/doc/ubuntu-web/html/ubuntuweb.index

## Ubuntu.Connectivity
${DIR}/get_package.py connectivity-doc
${DIR}/manage.py import_qdoc -Pp -t apps -l qml -r development -s "Platform Services" -N Ubuntu.Connectivity -i ${OUTPUT_DIR}usr/share/doc/connectivity-api/qml/html/connectivity.index

#### Aps/HTML5
## UbuntuUI
${DIR}/get_package.py ubuntu-html5-ui-toolkit-doc
${DIR}/manage.py import_yuidoc -i -t apps -l html5 -r development -s "Graphical Interface" -d ${OUTPUT_DIR}usr/share/doc/ubuntu-html5-ui-toolkit-doc/data.json

## Platform Bindings
${DIR}/get_package.py unity-webapps-qml-doc
## OnlineAccounts3
${DIR}/manage.py import_yuidoc -t apps -l html5 -r development -s "Platform Services" -d ${OUTPUT_DIR}usr/share/unity-webapps-qml/doc/api/online-accounts/data.json
## AlarmAPI
${DIR}/manage.py import_yuidoc -t apps -l html5 -r development -s "Platform Services" -d ${OUTPUT_DIR}usr/share/unity-webapps-qml/doc/api/alarm-api/data.json
## ContentHub
${DIR}/manage.py import_yuidoc -t apps -l html5 -r development -s "Platform Services" -d ${OUTPUT_DIR}usr/share/unity-webapps-qml/doc/api/content-hub/data.json
## RuntimeAPI
${DIR}/manage.py import_yuidoc -t apps -l html5 -r development -s "Platform Services" -d ${OUTPUT_DIR}usr/share/unity-webapps-qml/doc/api/runtime-api/data.json

#### Autopilot/Python
## Autopilot
${DIR}/get_package.py python3-autopilot
find ${OUTPUT_DIR}usr/share/doc/python3-autopilot/json/ -name "*.gz" -print0 |xargs -0 gunzip
${DIR}/manage.py import_sphinx -t autopilot -l python -r development -s ./api_docs/importers/autopilot_sections.py -i ${OUTPUT_DIR}usr/share/doc/python3-autopilot/json/objects.inv

${DIR}/get_package.py ubuntu-ui-toolkit-autopilot
find ${OUTPUT_DIR}usr/share/doc/ubuntu-ui-toolkit-autopilot/json/ -name "*.gz" -print0 |xargs -0 gunzip
${DIR}/manage.py import_sphinx -t autopilot -l python -r development -s ./api_docs/importers/autopilot_sections.py -i ${OUTPUT_DIR}usr/share/doc/ubuntu-ui-toolkit-autopilot/json/objects.inv

${DIR}/get_package.py python3-scope-harness
find ${OUTPUT_DIR}usr/share/doc/python3-scope-harness/json/ -name "*.gz" -print0 |xargs -0 gunzip
${DIR}/manage.py import_sphinx -t autopilot -l python -r development -s ./api_docs/importers/autopilot_sections.py -i ${OUTPUT_DIR}usr/share/doc/python3-scope-harness/json/objects.inv

#### Scopes/C++
## unity.scopes
${DIR}/get_package.py libunity-scopes-doc
${DIR}/manage.py import_doxygen -t scopes -l cpp -r development -s ./api_docs/importers/scope_sections.py -N unity.scopes -d ${OUTPUT_DIR}usr/share/doc/unity-scopes/

## Accounts
${DIR}/get_package.py libaccounts-qt-doc
${DIR}/manage.py import_doxygen -t scopes -l cpp -r development -s ./api_docs/importers/accounts_sections.py -n Accounts -d ${OUTPUT_DIR}usr/share/doc/libaccounts-qt/html/

## U1db
${DIR}/get_package.py libu1db-qt5-doc
${DIR}/manage.py import_qdoc -Pp -N U1db -t scopes -l cpp -r development -s "Platform Services" -i ${OUTPUT_DIR}usr/share/u1db-qt/doc/html/u1db-qt.index

#### Scopes/Javascript
SOURCE=http://ppa.launchpad.net/ubuntu-sdk-team/ppa/ubuntu ${DIR}/get_package.py unity-js-scopes-doc
${DIR}/manage.py import_yuidoc -t scopes -l js -r development -s "Platform Services" -d ${OUTPUT_DIR}usr/share/unity-js-scopes/doc/docbuild/data.json

rm -r ${OUTPUT_DIR}
